#!/usr/bin/env python3
"""
Compara dos corridas del juez sobre las mismas respuestas (por ejemplo, juez v1 vs juez v2).
No hace llamadas a modelos.

Uso:
  python compare_judges.py results/open results/open-juez-v2
"""
import json, os, sys
from collections import Counter

if len(sys.argv) != 3:
    sys.exit("Uso: python compare_judges.py <carpeta_corrida_1> <carpeta_corrida_2>")


def load(d):
    out = {}
    for line in open(os.path.join(d, "judge_open.jsonl"), encoding="utf-8"):
        r = json.loads(line)
        out[r["key"]] = r
    return out


r1, r2 = load(sys.argv[1]), load(sys.argv[2])
pairs, changes = Counter(), []
for key in sorted(set(r1) & set(r2)):
    for slot, l1 in r1[key]["labels"].items():
        l2 = r2[key]["labels"].get(slot)
        if l1 and l2:
            pairs[(l1, l2)] += 1
            if l1 != l2:
                changes.append((key, slot, l1, l2, (r2[key].get("why") or {}).get(slot, "")))

total = sum(pairs.values())
same = sum(v for (a, b), v in pairs.items() if a == b)
md = ["# Comparación de las dos corridas del juez", "",
      f"Clasificaciones comparadas: {total}. Coinciden: {same} ({100 * same / total:.0f}%). Cambiaron: {total - same}." if total else "No hay clasificaciones en común.", "",
      "| corrida 1 \\ corrida 2 | A | B | N |", "| --- | --- | --- | --- |"]
for a in "ABN":
    md.append(f"| {a} | " + " | ".join(str(pairs[(a, b)]) for b in "ABN") + " |")
md += ["", "## Cambios", "", "| modelo · pregunta | respuesta | corrida 1 | corrida 2 | justificación (corrida 2) |", "| --- | --- | --- | --- | --- |"]
md += [f"| {k.replace('|', ' · ')} | {s} | {a} | {b} | {w} |" for k, s, a, b, w in changes]
with open(os.path.join(sys.argv[2], "compare_judges.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(md) + "\n")
print("\n".join(md))
