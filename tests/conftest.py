import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

AGENT = """---
name: {name}
title: Test Agent
type: agent
category: alpha
---

# Test Agent

## Mission

Do things.

## Best used for

- one
- two

## Typical deliverables

- memo

## Operating workflow

1. Work.

## Guardrails

- Be careful.

## Portable system prompt

You are a test.
"""

PROMPT = """---
name: {name}
title: Test Prompt
type: prompt
category: daily
---

# Test Prompt

## Use when

You need a test.

## Inputs to gather

- stuff

## Expected output

A result.

## Copy/paste prompt

```
Do it.
```
"""

SKILL = """---
name: {name}
description: Does a thing.
argument-hint: [topic]
---

Body.
"""


@pytest.fixture
def mini_repo(tmp_path):
    """A tiny, valid fake repository."""
    def w(path, text):
        p = tmp_path / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
    w("agents/README.md", "# Agents\n\nIncludes **1 municipal role agents**.\n\nBrowse by folder:\n- alpha\n")
    w("agents/alpha/test-agent.md", AGENT.format(name="test-agent"))
    w("prompts/README.md", "# Prompts\n\nBrowse by folder:\n- daily\n")
    w("prompts/daily/test-prompt.md", PROMPT.format(name="test-prompt"))
    w("skills/README.md", "# Skills\n\nBrowse by folder:\n- gov\n")
    w("skills/gov/test-skill/SKILL.md", SKILL.format(name="test-skill"))
    w("stacks/one-stack.md", "# Stack\n")
    w("README.md", "# Repo\n\n- **1 role agent**\n- **1 skill**\n\nSee [agent](agents/alpha/test-agent.md).\n")
    w("catalog/README.md", "# Catalog\n\n## Counts\n- Agents: 0\n- Prompts: 0\n- Skills: 0\n")
    return tmp_path
