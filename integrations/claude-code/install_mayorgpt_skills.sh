#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="${1:-.claude/skills}"
SOURCE_DIR="$(cd "$(dirname "$0")/../.." && pwd)/skills"

mkdir -p "$TARGET_DIR"

# Copy all skills, preserving category folders.
rsync -av --exclude 'README.md' "$SOURCE_DIR/" "$TARGET_DIR/"

echo "MayorGPT skills copied to $TARGET_DIR"
echo "Tip: keep only the skill folders you want to load automatically in your project."
