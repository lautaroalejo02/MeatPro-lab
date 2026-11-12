#!/usr/bin/env bash
cd "C:/Users/lauti_lvk88nb/source/repos/MeatPro-lab/meat-proxies-v2"
export PYTHONUTF8=1
for step in "run_single.py" "judge.py single" "judge.py clean" "run_pressure.py" "judge.py pressure" "analyze.py"; do
  echo "== $step $(date +%H:%M)"
  python $step --out runs/full > "/tmp/ff/full-$(echo $step | tr ' ' '_').log" 2>&1; rc=$?
  echo "rc=$rc"
  if [ $rc -ne 0 ]; then echo "STOP at: $step"; exit $rc; fi
done
echo "ALL DONE $(date +%H:%M)"; exit 0
