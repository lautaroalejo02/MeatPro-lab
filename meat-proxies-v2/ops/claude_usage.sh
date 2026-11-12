#!/usr/bin/env bash
# Print "five_hour seven_day" Claude utilization (0-1) using one tiny Haiku call. Output has no CR.
f=$(mktemp)
cd /tmp && echo "ok" | ENABLE_CLAUDEAI_MCP_SERVERS=false timeout 120 /c/Users/lauti_lvk88nb/AppData/Roaming/npm/node_modules/@anthropic-ai/claude-code/bin/claude.exe -p --model claude-haiku-4-5 --setting-sources "" --strict-mcp-config --disable-slash-commands --output-format stream-json --verbose 2>/dev/null > "$f"
python -c "
import json,sys
u=None
for l in open(sys.argv[1],encoding='utf-8',errors='replace'):
    try: e=json.loads(l)
    except Exception: continue
    if e.get('type')=='rate_limit_event':
        w=e['rate_limit_info'].get('unifiedWindows',{}); u=(w.get('five_hour',{}).get('utilization'), w.get('seven_day',{}).get('utilization'))
print('%s %s'%u if u else 'NA NA')" "$(cygpath -w "$f")" | tr -d '\r'
rm -f "$f"
