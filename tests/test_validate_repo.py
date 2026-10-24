import validate_repo as vr


def run(root, **kw):
    return vr.validate(root, **kw)


def test_clean_mini_repo(mini_repo):
    # counts: catalog files absent except README; fix README count line expectations
    (mini_repo / "catalog/README.md").unlink()
    assert run(mini_repo) == []


def test_skill_name_mismatch_and_missing_description(mini_repo):
    p = mini_repo / "skills/gov/test-skill/SKILL.md"
    p.write_text("---\nname: other\n---\nBody\n")
    errs = run(mini_repo)
    assert any("does not match directory" in e for e in errs)
    assert any("missing description" in e for e in errs)


def test_missing_frontmatter(mini_repo):
    (mini_repo / "skills/gov/test-skill/SKILL.md").write_text("no frontmatter")
    assert any("frontmatter" in e for e in run(mini_repo))


def test_agent_missing_section(mini_repo):
    p = mini_repo / "agents/alpha/test-agent.md"
    p.write_text(p.read_text().replace("## Guardrails", "## Other"))
    assert any("missing required section '## Guardrails'" in e for e in run(mini_repo))


def test_prompt_wrong_category(mini_repo):
    p = mini_repo / "prompts/daily/test-prompt.md"
    p.write_text(p.read_text().replace("category: daily", "category: weekly"))
    assert any("does not match folder" in e for e in run(mini_repo))


def test_duplicate_names(mini_repo):
    import shutil
    d = mini_repo / "skills/other/test-skill"
    d.parent.mkdir()
    shutil.copytree(mini_repo / "skills/gov/test-skill", d)
    assert any("duplicate skill name 'test-skill'" in e for e in run(mini_repo))


def test_broken_link_detected_but_code_and_urls_ignored(mini_repo):
    (mini_repo / "docs").mkdir()
    (mini_repo / "docs/a.md").write_text(
        "[bad](missing.md) [ok](../README.md#x) [web](https://x.org) [anchor](#top)\n"
        "`[code](nope.md)`\n```\n[fenced](nope2.md)\n```\n")
    errs = [e for e in run(mini_repo) if "broken link" in e]
    assert errs == ["docs/a.md: broken link -> missing.md"]


def test_count_mismatch(mini_repo):
    (mini_repo / "README.md").write_text("**5 role agents**\n")
    errs = run(mini_repo)
    assert any("states 5 agents but filesystem has 1" in e for e in errs)


def test_catalog_count_mismatch(mini_repo):
    import build_catalog as bc
    bc.main(["--root", str(mini_repo)])
    assert run(mini_repo) == []
    import json
    (mini_repo / "catalog/summary.json").write_text(json.dumps({"agents": 9, "prompts": 1, "skills": 1, "stacks": 1}))
    assert any("summary.json: agents=9" in e for e in run(mini_repo))


def test_main_exit_codes(mini_repo, capsys):
    (mini_repo / "catalog/README.md").unlink()
    assert vr.main(["--root", str(mini_repo)]) == 0
    (mini_repo / "skills/gov/test-skill/SKILL.md").write_text("---\nname: x\n---\n")
    assert vr.main(["--root", str(mini_repo)]) == 1
    assert "Validation FAILED" in capsys.readouterr().err


def test_real_repo_validates():
    """The actual repository must pass validation."""
    errs = vr.validate(vr.REPO_ROOT)
    assert errs == [], "\n".join(errs)
