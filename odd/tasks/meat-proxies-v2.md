# meat-proxies-v2 (article version)

Locator: `odd/tasks/meat-proxies-v2.md` · Engram mirror: `odd/meat-proxies-v2/tasks`

## Objective

Run the reduced ("article") version of the meat proxies v2 experiment: leak and fix as headline numbers, plus dose and graded pressure, across Opus 5.5, Sol 6.1 and SWE-2.

## Problem / why

The framing judge (flipflop V2 and its replica) showed models shift emphasis toward the user's opinion. The author wants two numbers that read in one sentence, measured with pre-registered thresholds, within Codex quota.

## Scope and constraints

- CLI only, no API. Author's global instructions isolated (`cli_isolated.py`: Claude `--setting-sources ""` + `ENABLE_CLAUDEAI_MCP_SERVERS=false`; Codex own `CODEX_HOME`; Devin `read_config_from` all false).
- 20 questions, 8 single-turn conditions, pressure 10 questions × 3 arms × 2 turns, batched blind evaluation.
- Two mandatory author checkpoints: question bank, pilot.
- No commits unless the author asks.

## Tasks

- [x] T1 Write `meat-proxies-v2/PREREG.md` (route: inline; one doc).
- [x] T2 Generate question bank with `gen_bank.py` (SWE-2 proposes, Fable filters) and stop at checkpoint 1 (route: inline; single script). Author approved option (a) + adjustments: 23 questions.
- [x] T3 Write the run + judge + analysis scripts (route: delegated writer; 2+ non-trivial files). Writer: done; py_compile + full mock pilot + resume check passed; parent spot check py_compile OK.
- [x] T4 Pilot: 5 questions, all conditions, all models; stop at checkpoint 2. Done (runs/pilot); 15 empty Fable judgments re-judged after Claude session limit (logged in DECISIONES.md).
- [ ] T5 Full single-turn and pressure runs. Single-turn + judges + leak limpio COMPLETE 2026-10-13 (414/414 strips valid; 194 retried after Devin free-tier rate limit). Pressure pending (16/180 turns), author decides.
- [ ] T6 Analysis and deliverables (results.md, examples.md, limitaciones.md, validacion_humana.csv).

## Checks

- Isolation probe per model before each run (no author rules visible).
- Empty CLI output counts as failure (retry up to 3).
- Codex quota read before and after Sol-heavy steps.

## Progress / evidence

- 2026-10-15: literature review in meat-proxies-v2/lit/ (4 SWE-2 discovery, Opus verification of 29 sources, 3 Sonnet follow-ups). F1 overcorrection already reported (SWAY, binary only; our free-text magnitude adds). F2 echo-vs-framing: no prior method found (main novelty candidate). F4 null consistent with low power. F6 0% must be bounded (Li et al.: GPT-5 YTA->NTA 40.6%).

- 2026-10-13 final single-turn (n=23): M1L leak limpio fuerte Opus 48% [39,54] (H1 NO), Sol 76% [67,87] (H1 CUMPLIDA), SWE-2 59% [46,72] (INCONCLUSA). F1: Opus leak limpio 29% (framing points against user), Sol 87%. H3 CUMPLIDA Sol only (others: no effect to fix). H5 NO for all. Kappa 0.70-0.81. Guard v2 (PID kill, CR bug fixed) tested.

- 2026-10-13: interim (n=23, before leak limpio): F1 overcorrects (Opus +0.03 -> -0.74, SWE-2 +0.08 -> -0.42); Sol mirrors (+0.37 [0.18,0.55]) and flips 22% [9,39]; Opus flip 0%; raw leak 93-100% (echo); no dose effect.

- 2026-10-12: pilot complete. Leak 100% everywhere: 50-100% of opinion responses restate the user's view in the first 600 chars, so M1 measures echo, not framing. F1 overcorrects (tilt goes against user). eti06: no refusals or sermons.

- 2026-10-12: bank approved at checkpoint 1 (23 questions; fil03 and his04 out; eti06 flagged).
- 2026-10-12: PREREG.md written; isolation hardened (Devin `read_config_from`, Claude connectors off).

## Next step

Author reviews results; decide on pressure stage; then T6 deliverables (examples, limitaciones, validacion_humana).