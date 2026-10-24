import importlib.util
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "integrations/api/mayorgpt_llm.py"
spec = importlib.util.spec_from_file_location("mayorgpt_llm", SRC)
llm = importlib.util.module_from_spec(spec)
sys.modules["mayorgpt_llm"] = llm
spec.loader.exec_module(llm)

KEY_VARS = ["MAYORGPT_PROVIDER", "MAYORGPT_MODEL", "MAYORGPT_BASE_URL", "MAYORGPT_API_KEY"] + [
    p["key_env"] for p in llm.PROVIDERS.values() if p.get("key_env")] + ["GOOGLE_API_KEY"]


@pytest.fixture(autouse=True)
def clean_env(monkeypatch):
    for k in KEY_VARS:
        monkeypatch.delenv(k, raising=False)


def cfg(provider, **env):
    e = {"MAYORGPT_MODEL": "m1", "MAYORGPT_BASE_URL": "http://example.test/v1"}
    e.update(env)
    return llm.resolve_config(provider, env=e)


def test_missing_model_error():
    with pytest.raises(llm.LLMError, match="MAYORGPT_MODEL"):
        llm.resolve_config("openai", env={})


def test_missing_provider_and_unknown():
    with pytest.raises(llm.LLMError, match="MAYORGPT_PROVIDER"):
        llm.resolve_config(None, "m", env={})
    with pytest.raises(llm.LLMError, match="unknown provider"):
        llm.resolve_config("nope", "m", env={})


def test_base_url_required_for_gateways():
    for p in ("azure", "openai-compatible"):
        with pytest.raises(llm.LLMError, match="base URL"):
            llm.resolve_config(p, "m", env={})


@pytest.mark.parametrize("provider", [p for p, v in llm.PROVIDERS.items() if v["kind"] == "openai"])
def test_openai_style_payload(provider):
    c = llm.resolve_config(provider, "m1", env={"MAYORGPT_BASE_URL": "http://h/v1/", "MAYORGPT_API_KEY": "k"})
    url, headers, payload = llm.build_request(c, "SYS", "USER", max_tokens=50, temperature=0.2)
    assert url == "http://h/v1/chat/completions"
    assert payload["model"] == "m1"
    assert payload["messages"] == [{"role": "system", "content": "SYS"}, {"role": "user", "content": "USER"}]
    assert payload[c.max_field] == 50 and payload["temperature"] == 0.2
    assert "k" in headers.get("Authorization", "") + headers.get("api-key", "")


def test_openai_preset_urls_and_optional_params():
    c = llm.resolve_config("xai", "m1", env={"XAI_API_KEY": "kk"})
    url, headers, payload = llm.build_request(c, "s", "u")
    assert url == "https://api.x.ai/v1/chat/completions"
    assert headers["Authorization"] == "Bearer kk"
    assert "max_tokens" not in payload and "temperature" not in payload


def test_azure_uses_api_key_header():
    c = cfg("azure", AZURE_OPENAI_API_KEY="az")
    _, headers, _ = llm.build_request(c, "s", "u")
    assert headers["api-key"] == "az" and "Authorization" not in headers


def test_local_provider_needs_no_key():
    c = llm.resolve_config("ollama", "m1", env={})
    llm.require_key(c)
    _, headers, _ = llm.build_request(c, "s", "u")
    assert "Authorization" not in headers


def test_hosted_provider_requires_key():
    c = llm.resolve_config("mistral", "m1", env={})
    with pytest.raises(llm.LLMError, match="MISTRAL_API_KEY"):
        llm.require_key(c)


def test_key_precedence():
    c = llm.resolve_config("openai", "m", env={"MAYORGPT_API_KEY": "a", "OPENAI_API_KEY": "b"})
    assert c.api_key == "a"
    c = llm.resolve_config("openai", "m", env={"OPENAI_API_KEY": "b"})
    assert c.api_key == "b"
    c = llm.resolve_config("gemini", "m", env={"GOOGLE_API_KEY": "g"})
    assert c.api_key == "g"


def test_gemini_payload():
    c = llm.resolve_config("gemini", "some-model", env={"GEMINI_API_KEY": "gk"})
    url, headers, payload = llm.build_request(c, "SYS", "USER", max_tokens=10)
    assert url.endswith("/models/some-model:generateContent")
    assert headers["x-goog-api-key"] == "gk"
    assert payload["system_instruction"]["parts"][0]["text"] == "SYS"
    assert payload["contents"][0]["parts"][0]["text"] == "USER"
    assert payload["generationConfig"]["maxOutputTokens"] == 10
    c2 = llm.resolve_config("gemini", "models/x", env={"GEMINI_API_KEY": "gk"})
    assert "/models/x:generateContent" in llm.build_request(c2, "s", "u")[0]


def test_redaction():
    c = llm.resolve_config("openai", "m", env={"MAYORGPT_API_KEY": "sk-secret-123"})
    url, headers, payload = llm.build_request(c, "s", "u")
    report = llm.dry_run_report(url, headers, payload, c.api_key)
    assert "sk-secret-123" not in report and "REDACTED" in report
    g = llm.resolve_config("gemini", "m", env={"GEMINI_API_KEY": "gem-secret"})
    report = llm.dry_run_report(*llm.build_request(g, "s", "u"), g.api_key)
    assert "gem-secret" not in report
    leaked = llm.dry_run_report("http://x/?key=gem-secret", {}, {"a": "gem-secret"}, "gem-secret")
    assert "gem-secret" not in leaked


def test_extract_text():
    assert llm.extract_text("openai", {"choices": [{"message": {"content": "hi"}}]}) == "hi"
    assert llm.extract_text("gemini", {"candidates": [{"content": {"parts": [{"text": "a"}, {"text": "b"}]}}]}) == "ab"
    with pytest.raises(llm.LLMError):
        llm.extract_text("openai", {"error": "x"})


def test_cli_missing_model(capsys):
    assert llm.main(["--agent", "mayor", "--user", "hi", "--provider", "openai"]) == 2
    assert "MAYORGPT_MODEL" in capsys.readouterr().err


def test_cli_dry_run_and_print_prompt(monkeypatch, capsys, mini_repo):
    monkeypatch.setenv("MAYORGPT_PROVIDER", "openai")
    monkeypatch.setenv("MAYORGPT_MODEL", "m1")
    monkeypatch.setenv("OPENAI_API_KEY", "sk-topsecret")
    assert llm.main(["--agent", "test-agent", "--user", "hi", "--dry-run"], root=mini_repo) == 0
    out = capsys.readouterr().out
    body = json.loads(out)
    assert body["body"]["messages"][1]["content"] == "hi"
    assert "sk-topsecret" not in out
    assert llm.main(["--agent", "test-agent", "--print-prompt"], root=mini_repo) == 0
    assert "Do things." in capsys.readouterr().out


def test_cli_unknown_agent(mini_repo, capsys):
    assert llm.main(["--agent", "nope", "--print-prompt"], root=mini_repo) == 2


def test_no_hardcoded_model_ids_or_vendor_wording():
    text = SRC.read_text().lower()
    for p in ("gpt-", "gemini-1", "gemini-2", "grok-", "llama-3", "mistral-large"):
        assert p not in text


def test_claude_payload_and_redaction():
    c = llm.resolve_config("claude", "some-model", env={"ANTHROPIC_API_KEY": "ak-secret"})
    url, headers, payload = llm.build_request(c, "SYS", "USER", max_tokens=100)
    assert url.endswith("/messages")
    assert headers["x-api-key"] == "ak-secret" and "anthropic-version" in headers
    assert payload["system"] == "SYS" and payload["max_tokens"] == 100
    assert payload["messages"] == [{"role": "user", "content": "USER"}]
    assert "ak-secret" not in llm.dry_run_report(url, headers, payload, c.api_key)
    assert llm.extract_text("anthropic", {"content": [{"type": "text", "text": "a"}, {"type": "text", "text": "b"}]}) == "ab"
