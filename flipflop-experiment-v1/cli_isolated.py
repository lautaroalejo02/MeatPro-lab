"""Run a model CLI with the user's global agent instructions isolated.

Usage: python cli_isolated.py <model-name>   (prompt is read from stdin)

Each CLI otherwise loads the user's global CLAUDE.md / AGENTS.md, which contain
anti-sycophancy rules that would bias the experiment. This wrapper keeps auth but
skips those instruction files, and prints only the model's answer to stdout.
"""
import os
import subprocess
import sys
import tempfile

HOME = os.path.expanduser("~")
ISO = os.path.join(os.environ["LOCALAPPDATA"], "Temp", "ff-iso")
NPM = os.path.join(os.environ["APPDATA"], "npm", "node_modules")
CLAUDE = os.path.join(NPM, "@anthropic-ai", "claude-code", "bin", "claude.exe")
OPENCODE = os.path.join(NPM, "opencode-ai", "bin", "opencode.exe")
CODEX = os.path.join(os.environ["LOCALAPPDATA"], "Programs", "OpenAI", "Codex", "bin", "codex.exe")
# Must stay below the per-model "timeout" in models.json (300s) so this wrapper,
# not run.py, decides when to give up and can clean up the CLI process tree.
CHILD_TIMEOUT = 280
DEVIN = os.path.join(os.environ["LOCALAPPDATA"], "devin", "cli", "bin", "devin.exe")


def build(name, prompt_file):
    """Return (argv, extra_env, send_prompt_on_stdin) for a model name."""
    if name == "fable":
        return ([CLAUDE, "-p", "--model", "claude-fable-5-1", "--setting-sources", "",
                 "--strict-mcp-config", "--disable-slash-commands"], {}, True)
    if name == "kimi-k3":
        return ([OPENCODE, "run", "-m", "opencode-go/kimi-k3", "--pure"],
                {"XDG_CONFIG_HOME": os.path.join(ISO, "xdg-config"),
                 "OPENCODE_DISABLE_CLAUDE_CODE": "1"}, True)
    if name == "sol-6.1":
        return ([CODEX, "exec", "-m", "gpt-6.1-sol", "--skip-git-repo-check", "--ephemeral", "-"],
                {"CODEX_HOME": os.path.join(ISO, "codex-home")}, True)
    if name == "swe-2":
        return ([DEVIN, "--config", os.path.join(ISO, "devin-config.json"), "-p",
                 "--respect-workspace-trust", "false",
                 "--model", "swe-2-medium", "--prompt-file", prompt_file], {}, False)
    raise SystemExit(f"unknown model: {name}")


def main():
    sys.stdin.reconfigure(encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")
    prompt = sys.stdin.read()
    with tempfile.TemporaryDirectory() as cwd:
        prompt_file = os.path.join(cwd, "prompt.txt")
        with open(prompt_file, "w", encoding="utf-8") as f:
            f.write(prompt)
        argv, env, use_stdin = build(sys.argv[1], prompt_file)
        proc = subprocess.Popen(argv, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, text=True, encoding="utf-8",
                                errors="replace", cwd=cwd, env={**os.environ, **env})
        try:
            out, err = proc.communicate(prompt if use_stdin else None, timeout=CHILD_TIMEOUT)
        except subprocess.TimeoutExpired:
            # Kill the whole tree: run.py's own timeout would only kill this wrapper
            # and leave the CLI (and its children) running as orphans.
            subprocess.run(["taskkill", "/T", "/F", "/PID", str(proc.pid)], capture_output=True)
            proc.communicate()
            sys.stderr.write(f"cli_isolated: {sys.argv[1]} timed out after {CHILD_TIMEOUT}s\n")
            sys.exit(124)
    sys.stdout.write(out)
    sys.stderr.write(err[-2000:])
    sys.exit(proc.returncode)


if __name__ == "__main__":
    main()
