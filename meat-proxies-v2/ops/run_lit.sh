#!/usr/bin/env bash
D=/c/Users/lauti_lvk88nb/AppData/Local/devin/cli/bin/devin.exe
OUT="C:/Users/lauti_lvk88nb/source/repos/MeatPro-lab/meat-proxies-v2/lit"
for id in 1 2 3 4; do
  ( mkdir -p /tmp/ff/litwd$id && cd /tmp/ff/litwd$id && timeout 1500 $D --config "$LOCALAPPDATA\Temp\ff-iso\devin-config.json" -p --respect-workspace-trust false --permission-mode auto --model swe-2-high --prompt-file "$(cygpath -w /tmp/ff/lit_prompt_$id.txt)" > "$OUT/discovery_T$id.md" 2> /tmp/ff/lit_err_$id.log; echo "T$id rc=$?" >> /tmp/ff/lit_done.log ) &
done; wait; echo ALL >> /tmp/ff/lit_done.log
