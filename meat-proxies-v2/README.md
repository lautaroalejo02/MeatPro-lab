# meat proxies v2

Pre-registered sycophancy experiment (spec: `PREREG.md`, bank: `questions.json`). Python 3.13, standard
library; matplotlib only for the optional figures.

## Run order

The isolation probe runs automatically before any script that has pending model calls; if any model can
see the author's global instructions, the script aborts (results in `<out>/isolation_probe.jsonl`).

Pilot (5 seeded questions, always including eti06):

```
python run_single.py --pilot --out runs/pilot
python judge.py single --pilot --out runs/pilot
python judge.py clean --pilot --out runs/pilot
python run_pressure.py --pilot --out runs/pilot
python judge.py pressure --pilot --out runs/pilot
python analyze.py --out runs/pilot
```

Full run (23 questions; pressure on 10 seeded questions): the same commands without `--pilot` and with
`--out runs/full`.

Every script is resumable (re-run it after a failure; completed work is skipped) and accepts
`--workers N` (default 2) and `--mock` (deterministic fake replies, no model calls, for testing the
pipeline end to end).

## Files

- `common.py`: seed, model families, evaluator rotation, model calls, parsers, mock replies.
- `run_single.py` → `runs.jsonl`: 8 single-turn conditions per question and model.
- `judge.py` → `judgments.jsonl`, `batches.jsonl`: blind TILT, LEAK and LEAK_PAR evaluations in batches
  of different questions. `judge.py clean` → `clean.jsonl` + `leak_limpio` judgments: SWE-2 strips the
  sentences that echo the user's opinion, then the leak reader re-reads the stripped text (M1L).
- `run_pressure.py` → `pressure_runs.jsonl`, `turn_validation.jsonl`: graded pressure (L0/L1/L2).
- `analyze.py` → `results.md`, `examples.md`, `limitaciones.md`, `validacion_humana.csv`
  (+ `validacion_humana_clave.csv`), `dosis.png`, `presion.png`.
