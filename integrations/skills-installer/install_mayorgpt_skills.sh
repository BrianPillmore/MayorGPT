#!/usr/bin/env bash
# Copy MayorGPT skills (plain SKILL.md folders) into a directory you choose.
# Works with any tool that reads a folder of instruction files.
#
# Safe by default: never deletes anything, never overwrites a skill that differs
# from the repo copy unless --force is given, and is idempotent (re-running with
# the same options changes nothing). Use --dry-run to preview.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)/skills"

TARGET_DIR=""
DRY_RUN=0
FORCE=0
LIST=0
CATEGORIES=()
SKILLS=()

usage() {
  cat <<USAGE
Usage: $(basename "$0") --target DIR [options]

Options:
  --list                 List categories and skills, then exit
  --category NAME        Install every skill in a category (repeatable)
  --skill NAME           Install a single skill by name (repeatable)
  --target DIR           Destination directory (required for installing)
  --dry-run              Show what would happen without changing anything
  --force                Overwrite skills that already exist and differ
  -h, --help             Show this help

With no --category/--skill, all skills are installed. Skills are copied flat as
<DIR>/<skill-name>/SKILL.md.

Examples:
  $(basename "$0") --list
  $(basename "$0") --category finance --category governance --target ./city-skills --dry-run
  $(basename "$0") --skill agenda-packet-builder --target ~/my-project/skills
USAGE
}

die() { echo "error: $*" >&2; exit 1; }

while [ $# -gt 0 ]; do
  case "$1" in
    --list) LIST=1 ;;
    --category) [ $# -ge 2 ] || die "--category needs a value"; CATEGORIES+=("$2"); shift ;;
    --skill) [ $# -ge 2 ] || die "--skill needs a value"; SKILLS+=("$2"); shift ;;
    --target) [ $# -ge 2 ] || die "--target needs a value"; TARGET_DIR="$2"; shift ;;
    --dry-run|-n) DRY_RUN=1 ;;
    --force) FORCE=1 ;;
    -h|--help) usage; exit 0 ;;
    -*) usage >&2; die "unknown option: $1" ;;
    *) usage >&2; die "unexpected argument: $1 (use --target DIR)" ;;
  esac
  shift
done

[ -d "$SOURCE_DIR" ] || die "skills directory not found: $SOURCE_DIR"
if [ "$LIST" -eq 0 ] && [ -z "$TARGET_DIR" ]; then
  usage >&2; die "--target DIR is required"
fi

# Print "category<TAB>skill" for every skill, sorted.
all_skills() {
  local f
  for f in "$SOURCE_DIR"/*/*/SKILL.md; do
    [ -f "$f" ] || continue
    local d; d="$(dirname "$f")"
    printf '%s\t%s\n' "$(basename "$(dirname "$d")")" "$(basename "$d")"
  done | sort
}

if [ "$LIST" -eq 1 ]; then
  current=""
  while IFS=$'\t' read -r cat name; do
    if [ "$cat" != "$current" ]; then echo "$cat:"; current="$cat"; fi
    echo "  $name"
  done < <(all_skills)
  exit 0
fi

# Validate requested names before touching anything.
for c in ${CATEGORIES[@]+"${CATEGORIES[@]}"}; do
  [ -d "$SOURCE_DIR/$c" ] || die "unknown category '$c' (try --list)"
done
for s in ${SKILLS[@]+"${SKILLS[@]}"}; do
  all_skills | cut -f2 | grep -qx -- "$s" || die "unknown skill '$s' (try --list)"
done

selected=()
while IFS=$'\t' read -r cat name; do
  pick=0
  if [ ${#CATEGORIES[@]} -eq 0 ] && [ ${#SKILLS[@]} -eq 0 ]; then pick=1; fi
  for c in ${CATEGORIES[@]+"${CATEGORIES[@]}"}; do [ "$c" = "$cat" ] && pick=1; done
  for s in ${SKILLS[@]+"${SKILLS[@]}"}; do [ "$s" = "$name" ] && pick=1; done
  [ "$pick" -eq 1 ] && selected+=("$cat/$name")
done < <(all_skills)

[ ${#selected[@]} -gt 0 ] || die "no skills matched"

installed=0; unchanged=0; skipped=0
[ "$DRY_RUN" -eq 1 ] && echo "[dry-run] target: $TARGET_DIR"
for entry in "${selected[@]}"; do
  name="${entry#*/}"
  src="$SOURCE_DIR/$entry"
  dest="$TARGET_DIR/$name"
  if [ -d "$dest" ]; then
    if diff -rq "$src" "$dest" >/dev/null 2>&1; then
      unchanged=$((unchanged + 1)); continue
    fi
    if [ "$FORCE" -ne 1 ]; then
      echo "skip (exists and differs, use --force): $dest" >&2
      skipped=$((skipped + 1)); continue
    fi
  fi
  if [ "$DRY_RUN" -eq 1 ]; then
    echo "[dry-run] would install $entry -> $dest"
  else
    mkdir -p "$dest"
    cp -R "$src/." "$dest/"
    echo "installed $name"
  fi
  installed=$((installed + 1))
done

verb="installed"; [ "$DRY_RUN" -eq 1 ] && verb="would install"
echo "Done: $verb $installed, unchanged $unchanged, skipped $skipped (target: $TARGET_DIR)"
echo "Tip: install only the skills you need; see integrations/skills-installer/README.md."
