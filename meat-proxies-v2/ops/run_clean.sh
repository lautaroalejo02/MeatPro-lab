#!/usr/bin/env bash
cd "C:/Users/lauti_lvk88nb/source/repos/MeatPro-lab/meat-proxies-v2"
export PYTHONUTF8=1
echo "== judge clean $(date +%H:%M)"; python judge.py clean --out runs/full > /tmp/ff/full-judge.py_clean.log 2>&1 || { echo "STOP judge clean"; exit 1; }
echo "== analyze $(date +%H:%M)"; python analyze.py --out runs/full > /tmp/ff/full-analyze.py.log 2>&1 || { echo "STOP analyze"; exit 1; }
echo "ALL DONE $(date +%H:%M)"
