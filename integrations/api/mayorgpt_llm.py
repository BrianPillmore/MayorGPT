#!/usr/bin/env python3
"""Run a MayorGPT agent against any chat model API. Stdlib only (urllib).

Two wire formats cover most providers:
  * OpenAI-compatible chat/completions: OpenAI, xAI (Grok), Mistral, DeepSeek, Groq,
    Together, Fireworks, Perplexity, OpenRouter, Cohere, Qwen, Azure or any
    OpenAI-compatible gateway, and local servers (Ollama, LM Studio, vLLM, llama.cpp).
  * Native Gemini generateContent (provider "gemini").

Configuration (flags override environment):
  MAYORGPT_PROVIDER   provider preset name (see --list-providers)
  MAYORGPT_MODEL      model identifier, exactly as your provider documents it
  MAYORGPT_BASE_URL   override the preset base URL (required for azure / openai-compatible)
  MAYORGPT_API_KEY    API key; falls back to the provider's conventional variable

No model is built in. Nothing is sent unless you run without --print-prompt / --dry-run.

Examples:
  export MAYORGPT_PROVIDER=ollama MAYORGPT_MODEL=<local model name>
  python integrations/api/mayorgpt_llm.py --agent city-manager --prompt executive-brief \\
      --context-pack sample-springfield-example --user "Draft a brief on the Elm Street water main break."

  python integrations/api/mayorgpt_llm.py --agent mayor --print-prompt     # no network
  python integrations/api/mayorgpt_llm.py --agent mayor --user hi --dry-run  # show request, keys redacted
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import export_bundle as eb  # noqa: E402


class LLMError(Exception):
    """A user-facing configuration or request error."""


# kind: "openai" (chat/completions) or "gemini" (generateContent)
# auth: header style for the key. local servers need no key (key_env None).
PROVIDERS: dict[str, dict] = {
    "openai": {"kind": "openai", "base_url": "https://api.openai.com/v1", "key_env": "OPENAI_API_KEY",
               "max_field": "max_completion_tokens"},
    "xai": {"kind": "openai", "base_url": "https://api.x.ai/v1", "key_env": "XAI_API_KEY"},
    "mistral": {"kind": "openai", "base_url": "https://api.mistral.ai/v1", "key_env": "MISTRAL_API_KEY"},
    "deepseek": {"kind": "openai", "base_url": "https://api.deepseek.com", "key_env": "DEEPSEEK_API_KEY"},
    "groq": {"kind": "openai", "base_url": "https://api.groq.com/openai/v1", "key_env": "GROQ_API_KEY"},
    "together": {"kind": "openai", "base_url": "https://api.together.xyz/v1", "key_env": "TOGETHER_API_KEY"},
    "fireworks": {"kind": "openai", "base_url": "https://api.fireworks.ai/inference/v1",
                  "key_env": "FIREWORKS_API_KEY"},
    "perplexity": {"kind": "openai", "base_url": "https://api.perplexity.ai", "key_env": "PERPLEXITY_API_KEY"},
    "openrouter": {"kind": "openai", "base_url": "https://openrouter.ai/api/v1", "key_env": "OPENROUTER_API_KEY"},
    "cohere": {"kind": "openai", "base_url": "https://api.cohere.ai/compatibility/v1", "key_env": "COHERE_API_KEY"},
    "qwen": {"kind": "openai", "base_url": "https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
             "key_env": "DASHSCOPE_API_KEY"},
    "azure": {"kind": "openai", "base_url": None, "key_env": "AZURE_OPENAI_API_KEY", "auth": "api-key",
              "note": "set MAYORGPT_BASE_URL to your resource's OpenAI-compatible endpoint"},
    "openai-compatible": {"kind": "openai", "base_url": None, "key_env": None, "key_optional": True,
                          "note": "any gateway; set MAYORGPT_BASE_URL"},
    "ollama": {"kind": "openai", "base_url": "http://localhost:11434/v1", "key_env": None},
    "lmstudio": {"kind": "openai", "base_url": "http://localhost:1234/v1", "key_env": None},
    "vllm": {"kind": "openai", "base_url": "http://localhost:8000/v1", "key_env": None, "key_optional": True},
    "llamacpp": {"kind": "openai", "base_url": "http://localhost:8080/v1", "key_env": None,
                 "key_optional": True},
    "gemini": {"kind": "gemini", "base_url": "https://generativelanguage.googleapis.com/v1beta",
               "key_env": "GEMINI_API_KEY", "alt_key_env": "GOOGLE_API_KEY"},
}


@dataclass
class Config:
    provider: str
    kind: str
    base_url: str
    model: str
    api_key: str | None
    auth: str = "bearer"
    max_field: str = "max_tokens"


def list_providers() -> str:
    rows = [f"{'provider':<18}{'api':<8}{'key variable':<22}base URL"]
    for name, p in PROVIDERS.items():
        key = p.get("key_env") or "(none needed)"
        rows.append(f"{name:<18}{p['kind']:<8}{key:<22}{p['base_url'] or '(set MAYORGPT_BASE_URL)'}")
    rows.append("\nBase URLs and key variables are presets; confirm against your provider's current docs.")
    return "\n".join(rows) + "\n"


def resolve_config(provider: str | None = None, model: str | None = None,
                   base_url: str | None = None, env: dict | None = None) -> Config:
    env = os.environ if env is None else env
    provider = provider or env.get("MAYORGPT_PROVIDER")
    if not provider:
        raise LLMError("no provider: set MAYORGPT_PROVIDER or pass --provider "
                       f"(one of: {', '.join(PROVIDERS)})")
    if provider not in PROVIDERS:
        raise LLMError(f"unknown provider '{provider}' (one of: {', '.join(PROVIDERS)})")
    preset = PROVIDERS[provider]
    model = model or env.get("MAYORGPT_MODEL")
    if not model:
        raise LLMError("no model: set MAYORGPT_MODEL or pass --model "
                       "(no default model is built in; use the identifier your provider documents)")
    url = base_url or env.get("MAYORGPT_BASE_URL") or preset["base_url"]
    if not url:
        raise LLMError(f"provider '{provider}' needs a base URL: set MAYORGPT_BASE_URL or pass --base-url")
    key = env.get("MAYORGPT_API_KEY")
    if not key and preset.get("key_env"):
        key = env.get(preset["key_env"]) or (env.get(preset["alt_key_env"]) if preset.get("alt_key_env") else None)
    return Config(provider=provider, kind=preset["kind"], base_url=url.rstrip("/"), model=model,
                  api_key=key or None, auth=preset.get("auth", "bearer"),
                  max_field=preset.get("max_field", "max_tokens"))


def require_key(cfg: Config) -> None:
    preset = PROVIDERS[cfg.provider]
    if cfg.api_key or preset.get("key_optional") or not preset.get("key_env"):
        return
    raise LLMError(f"no API key: set MAYORGPT_API_KEY or {preset['key_env']}")


def build_request(cfg: Config, system: str, user: str, max_tokens: int | None = None,
                  temperature: float | None = None) -> tuple[str, dict, dict]:
    """Return (url, headers, payload). The headers contain the real key; redact before printing."""
    headers = {"Content-Type": "application/json"}
    if cfg.kind == "gemini":
        model = cfg.model if cfg.model.startswith("models/") else f"models/{cfg.model}"
        url = f"{cfg.base_url}/{model}:generateContent"
        payload: dict = {
            "system_instruction": {"parts": [{"text": system}]},
            "contents": [{"role": "user", "parts": [{"text": user}]}],
        }
        gen: dict = {}
        if max_tokens:
            gen["maxOutputTokens"] = max_tokens
        if temperature is not None:
            gen["temperature"] = temperature
        if gen:
            payload["generationConfig"] = gen
        if cfg.api_key:
            headers["x-goog-api-key"] = cfg.api_key
        return url, headers, payload
    url = f"{cfg.base_url}/chat/completions"
    payload = {"model": cfg.model,
               "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}]}
    if max_tokens:
        payload[cfg.max_field] = max_tokens
    if temperature is not None:
        payload["temperature"] = temperature
    if cfg.api_key:
        if cfg.auth == "api-key":
            headers["api-key"] = cfg.api_key
        else:
            headers["Authorization"] = f"Bearer {cfg.api_key}"
    return url, headers, payload


def redact_headers(headers: dict) -> dict:
    out = {}
    for k, v in headers.items():
        out[k] = "REDACTED" if k.lower() in ("authorization", "api-key", "x-goog-api-key") else v
    return out


def redact_text(text: str, key: str | None) -> str:
    return text.replace(key, "REDACTED") if key else text


def dry_run_report(url: str, headers: dict, payload: dict, key: str | None = None) -> str:
    report = {"method": "POST", "url": url, "headers": redact_headers(headers), "body": payload}
    return redact_text(json.dumps(report, indent=2, ensure_ascii=False), key)


def extract_text(kind: str, data: dict) -> str:
    try:
        if kind == "gemini":
            cands = data["candidates"]
            return "".join(p.get("text", "") for p in cands[0]["content"]["parts"])
        content = data["choices"][0]["message"]["content"]
        if isinstance(content, list):
            return "".join(c.get("text", "") for c in content if isinstance(c, dict))
        return content or ""
    except (KeyError, IndexError, TypeError):
        raise LLMError("unexpected response shape: " + json.dumps(data)[:500])


def send(url: str, headers: dict, payload: dict, key: str | None = None, timeout: float = 120) -> dict:
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers,
                                 method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:  # noqa: S310 (user-chosen URL)
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = redact_text(e.read().decode("utf-8", "replace")[:1000], key)
        raise LLMError(f"HTTP {e.code} from {redact_text(url, key)}: {body}")
    except urllib.error.URLError as e:
        raise LLMError(f"could not reach {redact_text(url, key)}: {e.reason}")
    except (json.JSONDecodeError, UnicodeDecodeError):
        raise LLMError("response was not valid JSON")


def read_user(user: str | None, attach: list[str]) -> str:
    if user == "-":
        user = sys.stdin.read()
    for f in attach:
        p = Path(f)
        if not p.is_file():
            raise LLMError(f"attachment not found: {f}")
        user = (user or "") + f"\n\n--- ATTACHMENT: {p.name} ---\n" + p.read_text(encoding="utf-8")
    return user or ""


def build_system(root: Path, agent: str, prompt, pack, skills, mode="portable") -> str:
    try:
        secs = eb.build_sections(root, agent, prompt, pack, eb.split_names(skills), [], mode)
    except eb.BundleError as e:
        raise LLMError(str(e))
    return eb.render_text(secs).rstrip("\n")


def main(argv=None, root: Path = REPO_ROOT) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=__doc__.split("\n\n", 1)[1])
    ap.add_argument("--list-providers", action="store_true", help="show provider presets and exit")
    ap.add_argument("--agent", help="agent name, e.g. city-manager")
    ap.add_argument("--prompt", help="prompt name, e.g. executive-brief")
    ap.add_argument("--context-pack", help="folder name under context-packs/")
    ap.add_argument("--skills", action="append", help="skill names, comma-separated")
    ap.add_argument("--agent-mode", choices=["portable", "full"], default="portable")
    ap.add_argument("--user", help="the request ('-' reads stdin)")
    ap.add_argument("--attach", action="append", default=[], help="text file appended to the request")
    ap.add_argument("--provider", help="overrides MAYORGPT_PROVIDER")
    ap.add_argument("--model", help="overrides MAYORGPT_MODEL")
    ap.add_argument("--base-url", help="overrides MAYORGPT_BASE_URL / the preset")
    ap.add_argument("--max-tokens", type=int, help="output token cap (omitted unless set)")
    ap.add_argument("--temperature", type=float, help="omitted unless set")
    ap.add_argument("--timeout", type=float, default=120)
    ap.add_argument("--print-prompt", action="store_true", help="print the system prompt and exit (no network)")
    ap.add_argument("--dry-run", action="store_true", help="print the request with keys redacted; send nothing")
    args = ap.parse_args(argv)
    try:
        if args.list_providers:
            sys.stdout.write(list_providers())
            return 0
        if not args.agent:
            ap.error("--agent is required")
        system = build_system(root, args.agent, args.prompt, args.context_pack, args.skills, args.agent_mode)
        if args.print_prompt:
            print(system)
            return 0
        if not args.user and not args.attach:
            ap.error("--user (or --attach) is required unless --print-prompt is used")
        cfg = resolve_config(args.provider, args.model, args.base_url)
        user = read_user(args.user, args.attach)
        url, headers, payload = build_request(cfg, system, user, args.max_tokens, args.temperature)
        if args.dry_run:
            print(dry_run_report(url, headers, payload, cfg.api_key))
            return 0
        require_key(cfg)
        data = send(url, headers, payload, cfg.api_key, args.timeout)
        print(extract_text(cfg.kind, data))
        return 0
    except LLMError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
