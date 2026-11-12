# Limitaciones (borrador para editar)

Esqueleto generado automáticamente con los números de esta corrida. Revisar y redactar antes de publicar.

- **Tamaño:** 23 preguntas con datos, 552 respuestas de un turno válidas, 21 turnos de presión. Con ~20 preguntas, diferencias de ±10 puntos pueden quedar dentro del ruido.
- **Jueces de tres familias:** fable (anthropic), sol-6.1 (openai), swe-2 (cognition) (Anthropic, OpenAI, Cognition). Ningún juez evalúa a su propia familia, pero los jueces son modelos con sus propios sesgos. Que SWE-2 (Cognition) no comparta familia con los demás es un supuesto no verificado.
- **Acuerdo entre jueces (kappa ponderado):** opus-5.5: 0.81; sol-6.1: 0.70; swe-2: 0.79. Si alguno es < 0,4, el tilt de ese generador es poco confiable.
- **Turnos de usuario de la presión:** escritos por swe-2 y validados a ciegas por fable. Descartes por brazo: L0: 0% (0/10), 0 excluidas; L1: 0% (0/4), 0 excluidas; L2: 12% (1/8), 0 excluidas.
- **Transcript reinyectado:** los CLI no tienen memoria multi-turno; en la presión, cada turno del modelo recibe la conversación entera aplanada en un solo prompt ("Persona:" / "Asistente:"). No es idéntico a una conversación real.
- **Posibles negativas:** 6 respuestas de un turno marcadas por la heurística (menos de 200 caracteres o frases típicas). No se descartan; la heurística es gruesa.
- **System prompts de los CLI:** cada modelo corre dentro de su CLI (Claude Code, Codex, Devin) con su system prompt propio de agente de código, no como un chat de consumo. La configuración global del autor se aísla (ver isolation_probe.jsonl), pero el system prompt del producto no.
- **Devin (SWE-2):** el CLI expone su lista de skills en el contexto; no se puede quitar desde el wrapper. Además lee ~/.claude/CLAUDE.md por la API de carpetas conocidas de Windows: hubo que renombrar el archivo durante las corridas.
- **Plantilla leve:** "me inclino un poco por {polo}" con polos que son oraciones completas queda gramaticalmente forzada; se mantuvo porque está pre-registrada.
- **Recorte del eco (M1L):** lo hace SWE-2 (swe-2), que también es uno de los modelos evaluados (y lector/juez). Recortes válidos: 100% (412/412). Marcadores de eco residuales tras el recorte: opus-5.5: 0; sol-6.1: 0; swe-2: 1. El recorte puede quitar de más (encuadre legítimo) o de menos (eco implícito); el leak limpio es una cota, no una medida pura de encuadre. En particular, el recorte puede eliminar también oraciones con la conclusión propia del modelo (por ejemplo, en eti06 B3F1 quitó un título y la oración del veredicto), lo que sesga M1L hacia abajo (conservador).
- **Pregunta política:** his06 se reporta aparte.
