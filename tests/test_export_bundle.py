import json

import pytest

import export_bundle as eb


@pytest.fixture
def repo(mini_repo):
    (mini_repo / "context-packs/demo").mkdir(parents=True)
    (mini_repo / "context-packs/demo/README.md").write_text("# Demo City\nFiscal year July 1.")
    return mini_repo


def sections(repo, **kw):
    return eb.build_sections(repo, "test-agent", **kw)


def test_text_contains_all_parts(repo):
    out = eb.render_text(sections(repo, prompt="test-prompt", context_pack="demo", skills=["test-skill"]))
    assert "# ROLE" in out and "Do things." in out
    assert "Fiscal year July 1." in out and "Copy/paste prompt" in out
    assert "SKILL: test-skill" in out and "Does a thing." in out
    assert "name: test-agent" not in out  # frontmatter stripped


def test_unknown_names_fail(repo):
    with pytest.raises(eb.BundleError):
        eb.build_sections(repo, "nope")
    with pytest.raises(eb.BundleError):
        sections(repo, context_pack="missing")
    with pytest.raises(eb.BundleError):
        sections(repo, skills=["missing"])


def test_json_formats(repo):
    system = eb.render_text(sections(repo))
    oa = json.loads(eb.render_openai(system, "hello"))
    assert [m["role"] for m in oa["messages"]] == ["system", "user"]
    assert oa["messages"][1]["content"] == "hello"
    assert "model" not in oa
    g = json.loads(eb.render_gemini(system, None))
    assert g["system_instruction"]["parts"][0]["text"].startswith("# ROLE")
    assert g["contents"][0]["parts"][0]["text"] == eb.USER_PLACEHOLDER


def test_markdown_demotes_headings(repo):
    md = eb.render_markdown(sections(repo), "test-agent")
    assert md.startswith("# MayorGPT bundle: test-agent")
    assert "\n## ROLE" in md and "\n### Mission" in md


def test_custom_gpt_fits_limit_and_lists_knowledge(repo):
    blocks = "\n\n".join(f"<{t}>\n{'x' * 400}\n</{t}>" for t in
                         ["role", "mission", "working-style", "handoffs", "inputs-to-request",
                          "core-work", "escalation-triggers", "authority-limits", "guardrails",
                          "quality-check"])
    p = repo / "agents/alpha/test-agent.md"
    p.write_text(p.read_text().replace("You are a test.", "```xml\n" + blocks + "\n```"))
    ins, know, warns = eb.render_custom_gpt(repo, "test-agent", "test-prompt", "demo", [], limit=2500)
    assert len(ins) <= 2500
    assert "<guardrails>" in ins and "<handoffs>" not in ins
    assert "role-test-agent-full.md" in know and "playbook-test-prompt.md" in know
    assert "context-pack-demo.md" in know and "playbook-test-prompt.md" in ins
    assert warns


def test_main_formats_and_all(repo, tmp_path, capsys):
    base = ["--root", str(repo), "--agent", "test-agent"]
    assert eb.main(base + ["--format", "openai-messages", "--user", "hi"]) == 0
    cap = capsys.readouterr()
    assert json.loads(cap.out)["messages"][1]["content"] == "hi"
    assert "characters" in cap.err  # size estimate
    out = tmp_path / "bundle"
    assert eb.main(base + ["--format", "all", "--out", str(out)]) == 0
    for name in ["system-prompt.txt", "bundle.md", "openai-messages.json", "gemini.json",
                 "custom-gpt/instructions.txt", "custom-gpt/KNOWLEDGE.md"]:
        assert (out / name).is_file(), name


def test_list_and_errors(repo, capsys):
    assert eb.main(["--root", str(repo), "--list"]) == 0
    out = capsys.readouterr().out
    assert "test-agent" in out and "test-prompt" in out and "test-skill" in out
    assert eb.main(["--root", str(repo), "--agent", "nope"]) == 2


def test_large_prompt_warning():
    assert any("large prompt" in w for w in eb.size_warnings("x" * (eb.LARGE_PROMPT_CHARS + 1)))


def test_real_repo_exports():
    secs = eb.build_sections(eb.REPO_ROOT, "mayor")
    assert "# ROLE" in eb.render_text(secs)
    ins, _, _ = eb.render_custom_gpt(eb.REPO_ROOT, "mayor", None, None, [])
    assert len(ins) <= eb.CUSTOM_GPT_LIMIT
