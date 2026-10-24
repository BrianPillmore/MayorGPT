import csv
import json

import build_catalog as bc
from mayorgpt_common import parse_frontmatter, sections, bullets


def test_parse_frontmatter_and_sections():
    meta, body = parse_frontmatter("---\nname: x\ntags:\n  - a\n  - b\n---\n# T\n\n## S\n\n- i\n")
    assert meta == {"name": "x", "tags": ["a", "b"]}
    assert bullets(sections(body)["S"]) == ["i"]


def test_build_records(mini_repo):
    files = bc.build(mini_repo)
    agents = json.loads(files["agents.json"])
    assert agents == [{"name": "test-agent", "title": "Test Agent", "category": "alpha",
                       "best_for": ["one", "two"], "deliverables": ["memo"]}]
    skills = json.loads(files["skills.json"])
    assert skills[0]["argument_hint"] == "topic" and skills[0]["category"] == "gov"
    prompts = json.loads(files["prompts.json"])
    assert prompts[0]["use_when"] == "You need a test."
    assert json.loads(files["summary.json"]) == {"agents": 1, "prompts": 1, "skills": 1, "stacks": 1}
    assert "- Agents: 1" in files["README.md"]


def test_csv_matches_json(mini_repo):
    files = bc.build(mini_repo)
    rows = list(csv.DictReader(files["agents.csv"].splitlines()))
    assert rows[0]["best_for"] == "one, two"


def test_idempotent_and_check(mini_repo, capsys):
    assert bc.main(["--root", str(mini_repo), "--check"]) == 1
    assert bc.main(["--root", str(mini_repo)]) == 0
    before = {p.name: p.read_text() for p in (mini_repo / "catalog").iterdir()}
    assert bc.main(["--root", str(mini_repo)]) == 0
    after = {p.name: p.read_text() for p in (mini_repo / "catalog").iterdir()}
    assert before == after
    assert bc.main(["--root", str(mini_repo), "--check"]) == 0


def test_category_order_follows_readme(mini_repo):
    (mini_repo / "agents/README.md").write_text("Browse by folder:\n- zeta\n- alpha\n")
    (mini_repo / "agents/zeta").mkdir()
    (mini_repo / "agents/zeta/z.md").write_text(
        (mini_repo / "agents/alpha/test-agent.md").read_text().replace("test-agent", "z").replace("category: alpha", "category: zeta"))
    assert [a["name"] for a in bc.collect_agents(mini_repo)] == ["z", "test-agent"]


def test_real_repo_catalog_is_up_to_date():
    """Fails when someone edits content without regenerating the catalog."""
    assert bc.main(["--check"]) == 0
