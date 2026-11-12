#!/usr/bin/env bash
# Print current Codex rate-limit usage via one tiny non-ephemeral call in the isolated CODEX_HOME.
H="$LOCALAPPDATA\Temp\ff-iso\codex-home"
cd /tmp && CODEX_HOME="$H" timeout 120 /c/Users/lauti_lvk88nb/AppData/Local/Programs/OpenAI/Codex/bin/codex.exe exec -m gpt-6.1-sol --skip-git-repo-check "ok" < /dev/null > /dev/null 2>&1
f=$(ls -t "$LOCALAPPDATA/Temp/ff-iso/codex-home/sessions"/*/*/*/rollout-*.jsonl | head -1)
grep -o '"rate_limits":{[^}]*}[^}]*}[^}]*}' "$f" | tail -1
