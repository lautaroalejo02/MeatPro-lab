#!/usr/bin/env python3
"""
Compara qué responde cada modelo a la misma pregunta neutral (sin que el usuario opine),
usando los resultados ya existentes de la v2. No hace ninguna llamada a modelos.

Uso:
  python compare_models.py --out results/open
"""
import argparse, json, os
from collections import defaultdict

ap = argparse.ArgumentParser()
ap.add_argument("--out", default="results/open")
ap.add_argument("--questions", default="open_questions.json")
a = ap.parse_args()

here = os.path.dirname(os.path.abspath(__file__))
qpath = a.questions if os.path.exists(a.questions) else os.path.join(here, a.questions)
items = {it["id"]: it for it in json.load(open(qpath, encoding="utf-8"))}

labels = {}
for line in open(os.path.join(a.out, "judge_open.jsonl"), encoding="utf-8"):
    r = json.loads(line)
    labels[r["key"]] = r["labels"]
texts = {}
for line in open(os.path.join(a.out, "raw_open.jsonl"), encoding="utf-8"):
    r = json.loads(line)
    texts[r["job_id"]] = r

models = sorted({k.split("|")[0] for k in labels})
md = ["# Qué responde cada modelo a la misma pregunta (sin que el usuario opine)", "",
      "Cada celda muestra las dos respuestas neutrales de ese modelo (la de `neutral` y la primera de `pushback`): A, B o N.", "",
      "| pregunta | A | B | " + " | ".join(models) + " | ¿los modelos se contradicen? |",
      "|" + " --- |" * (4 + len(models))]
contra, inconsist = [], defaultdict(int)
for qid, it in items.items():
    cells, sides = [], set()
    for m in models:
        lb = labels.get(f"{m}|{qid}", {})
        pair = (lb.get("neutral") or "?", lb.get("pb1") or "?")
        cells.append(" / ".join(pair))
        sides |= {x for x in pair if x in ("A", "B")}
        if pair[0] != pair[1] and "?" not in pair:
            inconsist[m] += 1
    c = "**sí**" if sides == {"A", "B"} else "no"
    if sides == {"A", "B"}:
        contra.append(qid)
    md.append(f"| {qid}: {it['q'][:60]}{'...' if len(it['q']) > 60 else ''} | {it['A']} | {it['B']} | " + " | ".join(cells) + f" | {c} |")

md += ["", f"**Preguntas donde al menos un modelo se inclinó por A y otro (o el mismo) por B:** {len(contra)} de {len(items)}.", "",
       "**Preguntas donde el mismo modelo dio dos posturas distintas a la misma pregunta neutral:**", ""]
md += [f"- {m}: {inconsist[m]} de {len(items)}" for m in models]

md += ["", "## Ejemplos de respuestas contradictorias", ""]
for qid in contra:
    it = items[qid]
    md += [f"### {qid}: {it['q']}", ""]
    for m in models:
        lb = labels.get(f"{m}|{qid}", {})
        for slot, job in (("neutral", "neutral"), ("pb1", "pushback")):
            if lb.get(slot) in ("A", "B"):
                t = (texts.get(f"{m}|{qid}|{job}", {}).get("text1") or "").strip()
                t = t if len(t) <= 600 else t[:600] + " [...]"
                md += [f"**{m}** ({lb[slot]}: {it[lb[slot]]}):", "", f"> {t}", ""]
                break

with open(os.path.join(a.out, "compare_models.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(md) + "\n")
print("\n".join(md))
