# Tarea: réplica del encuadre con 15 preguntas nuevas

## Para qué

El juez de encuadre encontró que Sol y Opus acomodan el énfasis de sus respuestas a lo que opina el usuario. Pero salió de 12 preguntas diseñadas antes de saber qué íbamos a encontrar. Esta réplica repite exactamente la misma medición con 15 preguntas nuevas, para ver si el patrón se sostiene.

## Antes de correr nada: las hipótesis

Copiá `HIPOTESIS_replica.md` en la carpeta del experimento **antes** de generar respuestas, y no lo modifiques después. Anotá la fecha y hora en que lo copiaste. Al final vamos a comparar los resultados contra esas hipótesis.

## Archivos

Copiá en la carpeta del experimento, sin tocar `models.json` ni los resultados anteriores:

- `open_run.py` (versión nueva: agrega la opción `--only-responses`)
- `replica_questions.json`
- `HIPOTESIS_replica.md`

`framing_judge.py` ya lo tenés: no cambia.

## Modelos

Los mismos de siempre: Opus 5.5, Sol-6.1 y SWE-2 como evaluados, y Fable como juez, todos en high. Todo lo que corra por Claude Code (Opus y Fable), con `--setting-sources ""` y tu CLAUDE.md fuera de juego. Al terminar, confirmame que quedó restaurado.

## Pasos

1. **Respuestas** (180 llamadas: 15 preguntas × 4 respuestas × 3 modelos). Para cada pregunta se generan: una respuesta neutral, una con el usuario inclinado a A, una con el usuario inclinado a B, y una segunda respuesta neutral para el control. Sin juez de letras y sin segundo turno de pushback.

```
python open_run.py --only-responses --questions replica_questions.json --out results/replica
```

2. **Juez de encuadre** (45 llamadas a Fable):

```
python framing_judge.py --judge fable --questions replica_questions.json --src results/replica --out results/replica-encuadre
```

Si algo se corta, volvé a correr el mismo comando: retoma desde donde quedó.

## Reglas

- No modifiques las preguntas, el juez ni el análisis.
- Solo CLI, sin API.
- Si algo falla, decime qué falló en vez de inventar resultados.
- No arranques la v3 ni nada más después de esto.

## Qué devolverme

1. La fecha y hora en que guardaste `HIPOTESIS_replica.md`.
2. La tabla de `results/replica-encuadre/summary_encuadre.md`.
3. Los 3 ejemplos más claros de ese archivo.
4. Tu revisión de 5 evaluaciones al azar del juez (en `framing.jsonl`).
5. **Para cada una de las 4 hipótesis: ¿se cumplió o no?**, con el número que lo respalda. Y si, según el criterio del archivo, el hallazgo quedó replicado.
6. Una tabla que compare la primera ronda (12 preguntas) con la réplica (15 preguntas) para cada modelo: diferencia de encuadre, diferencia del control y % de preguntas donde siguió al usuario.
