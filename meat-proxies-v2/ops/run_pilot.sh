#!/usr/bin/env bash
cd "C:/Users/lauti_lvk88nb/source/repos/MeatPro-lab/meat-proxies-v2"
export PYTHONUTF8=1
for step in "run_single.py --pilot" "judge.py single --pilot" "run_pressure.py --pilot" "judge.py pressure --pilot" "analyze.py"; do
  echo "== $step"; python $step --out runs/pilot > "/tmp/ff/pilot-$(echo $step | cut -d' ' -f1-2 | tr ' ' '_').log" 2>&1; rc=$?; echo "rc=$rc"
  [ $rc -ne 0 ] && { echo "STOP at: $step"; exit $rc; }
done
