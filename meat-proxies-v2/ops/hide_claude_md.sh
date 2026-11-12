#!/usr/bin/env bash
# Temporarily hide ~/.claude/CLAUDE.md while running "$@"; always restore on exit.
set -u
SRC="$HOME/.claude/CLAUDE.md"; BAK="$HOME/.claude/CLAUDE.md.ffbak"
if [ -e "$BAK" ]; then echo "backup already exists: $BAK — aborting" >&2; exit 1; fi
mv "$SRC" "$BAK" || exit 1
trap 'mv "$BAK" "$SRC" && echo "[restored CLAUDE.md]" >&2' EXIT
trap 'exit 130' INT TERM
"$@"
