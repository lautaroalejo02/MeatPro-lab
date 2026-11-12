# Tarea: correr el experimento de consistencia y sycophancy

En esta carpeta hay un experimento que mide si los modelos cambian de respuesta según cómo se les pregunta. Leé el `README.md` para entender las condiciones y las métricas.

## Modelos

Usá estos 4 modelos, cada uno a través del CLI que ya usás para coordinarlos:

- `fable`: Fable (vía Claude Code, `claude -p`)
- `kimi-k3`: Kimi K3
- `swe-2`: SWE-2
- `astra`: Astra

## Pasos

1. Completá `models.json` con el comando no interactivo de cada CLI: uno que reciba un prompt y devuelva solo la respuesta por stdout. Usá `"provider": "cli"` y poné `{prompt}` donde va el prompt, o sacalo si el CLI lo lee por stdin. Si un CLI no tiene modo no interactivo, avisame y desactivá ese modelo con `"enabled": false`.
2. Verificá que cada CLI responda: corré un prompt corto con cada uno y revisá que la salida sea solo texto, sin banners ni logs que tapen la respuesta.
3. Corré la prueba sin modelos reales: `python run.py --mock --lite`
4. Corré una prueba mínima con cada modelo: `python run.py --lite --only <nombre> --repeats 1 --out results/prueba-<nombre>`. Abrí el `summary.md`: si `respuestas_ilegibles` supera el 10%, revisá `raw.jsonl` y ajustá el comando de ese CLI antes de seguir.
5. Corré el experimento: `python run.py --lite --workers 2 --out results/lite`. Si se corta, volvé a correr el mismo comando: retoma desde donde quedó.

## Reglas

- No modifiques las preguntas, los prompts ni el análisis de `run.py`. Toda la gracia del experimento es que todos los modelos reciban exactamente los mismos prompts.
- No uses la API de ningún modelo: solo los CLI.
- Si algo falla, decime qué falló y qué probaste, en vez de inventar resultados.

## Qué devolverme

1. El contenido de `results/lite/summary.md`.
2. El contenido de `results/lite/examples.md`.
3. Los 3 hallazgos más llamativos en una línea cada uno, con el número que los respalda.
4. Cualquier problema o limitación del run: modelos que fallaron, respuestas ilegibles, CLI que agregan su propio contexto, etc.
