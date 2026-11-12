# ops: orchestration scripts used to run the experiments

These scripts were used from Git Bash on Windows during the runs. They assume machine-specific paths and are kept here for reproducibility, not as a portable tool.

## Path assumptions

- Scripts lived in `/tmp/ff/` (Git Bash temp dir) and call each other there.
- Isolation config lived in `%LOCALAPPDATA%\Temp\ff-iso\`, used by `../cli_isolated.py`:
  - `devin-config.json`: copy of `devin-config.isolated.json` (all `read_config_from` sources off, so Devin ignores `~/.claude/CLAUDE.md`, Cursor rules and imported MCP servers). Devin auth is read from the user's normal Devin login.
  - `codex-home/`: a separate `CODEX_HOME` containing only a copy of `~/.codex/auth.json` (not committed: credentials).
  - `xdg-config/`: empty dir used as `XDG_CONFIG_HOME` for opencode (only needed for Kimi).
- CLI binaries are referenced by absolute paths inside `../cli_isolated.py` (Claude Code, Codex, Devin, opencode).

## Rebuilding after a fresh machine

1. Install and log in to Claude Code, Codex and Devin.
2. Create `%LOCALAPPDATA%\Temp\ff-iso\` with `devin-config.json` (from this folder), `codex-home\auth.json` (copy of `~/.codex/auth.json`) and an empty `xdg-config\`.
3. Copy these scripts to `/tmp/ff/` and `chmod +x` them, or edit their paths.
4. Check isolation before any run: each model must answer `NONE` to the probe in `../common.py` (the pipeline aborts otherwise).

## Files

| File | Purpose |
| --- | --- |
| `run_full.sh` | Full pipeline: `run_single`, `judge single`, `judge clean`, `run_pressure`, `judge pressure`, `analyze` (resumable). |
| `run_clean.sh` | Only `judge clean` + `analyze` (used to finish the clean leak). |
| `run_pilot.sh` | Same as the full pipeline with `--pilot`. |
| `launch.ps1` | Starts a script detached from the session and writes its Windows PID to a file. |
| `usage_guard2.sh`, `guard_run.sh` | Pause the pipeline (kill by PID) when Claude 5h or weekly usage reaches the limit. |
| `claude_usage.sh` | Prints Claude 5h and weekly utilization via one tiny Haiku call (`rate_limit_event`). |
| `codex_quota.sh` | Prints Codex rate-limit usage from a non-ephemeral session rollout. |
| `hide_claude_md.sh` | Old approach (before `read_config_from`): temporarily hides `~/.claude/CLAUDE.md` during Devin runs. |
| `run_lit.sh`, `lit_common.txt` | Parallel SWE-2 literature discovery (search-only). |
| `devin-config.isolated.json` | Devin isolation config (sanitized: no org id). |
