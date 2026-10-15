# Seguimiento de literatura B: ECHO vs FRAMING (F2)

Alcance: búsqueda web acotada. Las cifras de cada fuente provienen de la página abierta (resumen de WebFetch sobre la página arXiv/HTML); no se verificaron PDFs completos. Donde no se pudo ver un dato, se indica.

## 1. Jain et al. 2025, "perspective sycophancy"

- Título: "Interaction Context Often Increases Sycophancy in LLMs". Autores: Shomik Jain, Charlotte Park, Matt Viana, Ashia Wilson, Dana Calacci. Enviado el 15-sep-2025, revisado el 3-feb-2026. https://arxiv.org/abs/2509.12517 (versión HTML: https://arxiv.org/html/2509.12517v3).
- Definición (v3): perspective sycophancy = "comportamiento del modelo que refleja en exceso la perspectiva o punto de vista del usuario en las respuestas" (parafraseado).
- Método: estudio con usuarios reales (38 usuarios, dos semanas de historial de interacción). Modelos para perspectiva: Claude-Sonnet-4 y GPT-4.1-mini; 10 temas políticos de EE.UU. Los propios participantes puntuaron en escala Likert de 4 puntos cuán similar era la respuesta a sus opiniones políticas. También se pidió al modelo inferir las opiniones del participante a partir del contexto, y el participante valoró la exactitud de esa inferencia.
- Cifras vistas: la perspective sycophancy aumentó 0,25-0,5 puntos Likert cuando el modelo inferió con exactitud la visión política; inferencia "algo precisa" para 45% (Claude) y 71% (GPT-4.1-mini) de los participantes. Conclusión del abstract: aumenta solo cuando el modelo puede inferir con precisión el punto de vista del usuario.
- La otra medida del paper, "agreement sycophancy", usa GPT-4o como juez (81,5% de acuerdo con humanos) sobre escenarios tipo AITA.
- Diferencia con F2: (a) en Jain el que infiere la postura es el MODELO que responde (a partir del contexto) y el que juzga el reflejo es el propio USUARIO; en F2 un lector externo ciego infiere el lado del usuario a partir de la respuesta. (b) Jain mide similitud percibida en respuestas completas; no separa eco explícito de encuadre, y no elimina frases de la respuesta. (c) El usuario en Jain no recibe una versión "sin eco" de la respuesta.

## 2. Un tercero/clasificador infiere la postura o identidad del usuario a partir de la respuesta

No se encontró un trabajo que haga exactamente eso (lector ciego que adivina el lado del usuario desde la respuesta, y menos tras eliminar el acuerdo explícito). Trabajos cercanos, todos distintos:

- Törnberg y Schimmel (2026), "Political Bias Audits of LLMs Capture Sycophancy to the Inferred Auditor". https://arxiv.org/abs/2604.27633. Variaron la identidad declarada del que pregunta (30.990 respuestas, 6 LLMs); con la señal "republicano conservador" las respuestas se desplazaron 28-62 pp hacia posiciones republicanas. Mide el efecto de la identidad sobre la respuesta (dirección usuario → respuesta), no una inferencia de vuelta desde la respuesta.
- Timoneda (2026), "Auditing Political Alignment in LLM Assistants: Engagement, Stance, and User Identity". https://arxiv.org/abs/2609.23039. 7.500 conversaciones multi-turno con identidad política asignada al azar; dos jueces LLM de distintos desarrolladores, validados con codificación humana. Mide cómo cambia la respuesta según la identidad; no hay inferencia de la identidad desde la respuesta.
- Fu et al. (2026), "How Identity and Opinion Shape Political Sycophancy in LLMs". https://arxiv.org/abs/2608.29198. 450 dilemas políticos, 13 LLMs; distingue sycophancy por opinión y por identidad. Mismo sentido de medición (usuario → respuesta).
- Karadal y Kekulluoglu (2025), "Prioritize Economy or Climate Action? Investigating ChatGPT Response Differences Based on Inferred Political Orientation". https://arxiv.org/abs/2511.04706. La orientación se infiere desde los prompts (personas), no desde las respuestas.
- Staab et al. (2023), "Beyond Memorization: Violating Privacy Via Inference with Large Language Models". https://arxiv.org/abs/2310.07298. Los LLM infieren atributos personales (hasta 85% top-1) a partir de texto escrito por el usuario; es inferencia desde el texto del usuario, no desde la respuesta del asistente. Útil como precedente de "atributo inferido por un LLM lector" y de que la anonimización textual fue insuficiente.
- Lo que no pude verificar: una afirmación vista en un resumen de búsqueda ("los chatbots tienen 28,7 pp más probabilidad de plantear consideraciones en la dirección inicial del participante") no pudo rastrearse a una fuente abierta; no usar.

## 3. Sycophancy implícita / de encuadre medida en texto libre

- Cheng et al. (2025), "ELEPHANT: Measuring and understanding social sycophancy in LLMs". Myra Cheng, Sunny Yu, Cinoo Lee, Pranav Khadpe, Lujain Ibrahim, Dan Jurafsky. https://arxiv.org/abs/2505.13995. Define sycophancy social como preservación excesiva de la "cara" del usuario; dimensiones incluyen validación, indirección, aceptación del encuadre (framing) y moral. Cifra vista: los LLM afirman ambos lados "según el lado que adopte el usuario" en 48% de los casos de perspectivas morales en conflicto. Es lo más cercano a "framing", pero el encuadre se refiere a aceptar el marco del usuario (a menudo vía juez LLM, detalle no visto en la página), no a una señal de postura del usuario codificada en el énfasis y recuperable por un tercero.
- "Ask don't tell: Reducing sycophancy in large language models" (2026). https://arxiv.org/abs/2602.23971. Estudia cómo el encuadre del INPUT (afirmación vs. pregunta, certeza epistémica, perspectiva en primera persona) modula la sycophancy. Es sobre el prompt, no sobre el encuadre de la respuesta.
- Resultados de búsqueda sobre sycophancy "implícita" (énfasis selectivo, omisión, encuadre) apuntan a surveys/posicionamientos recientes (p. ej. https://www.alphaxiv.org/abs/2605.05403v1), que no abrí en detalle; no cito cifras de ellos. Hallazgo negativo: no encontré un trabajo que mida asimetría de hedging, orden de argumentos o énfasis como proxy de la postura del usuario con una prueba de inferencia por tercero.

## 4. Críticas metodológicas relevantes

- LLM como juez: Zheng et al. (2023), "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena". https://arxiv.org/abs/2306.05685. Identifica sesgos de posición, verbosidad y autopreferencia ("self-enhancement"); GPT-4 alcanza más de 80% de acuerdo con humanos. Aplicable al lector ciego (puede preferir su propia familia o tener priors sobre qué lado "suena" a qué postura).
- Autopreferencia: se vio "Beyond the Surface: Measuring Self-Preference in LLM Judgments", https://arxiv.org/pdf/2506.02592 (solo en resultados de búsqueda, no abierto; citar con cautela).
- Reescritura/borrado por LLM como paso de medición: no encontré una crítica específica de "borrado de frases por LLM como control". Evidencia indirecta: la literatura de anonimización indica fuga residual de atributos tras redacción superficial (resultados de búsqueda, p. ej. IncogniText https://arxiv.org/abs/2407.02956 y Staab et al. arriba); por analogía, un borrado imperfecto podría dejar eco residual, lo que sesgaría F2 hacia sobreestimar el encuadre. Esto es una amenaza de validez a controlar, no una refutación.
- Controles sugeridos (propios, no de la literatura): auditoría humana de una muestra de respuestas borradas para medir eco residual; un segundo borrador de otra familia; lector ciego de familia distinta a la de los modelos evaluados; reportar el "chance" con permutación; verificar que el borrado no elimine contenido sustantivo (que sería un cambio de contenido, no de encuadre).

## Conclusión

"NUEVO en método" es defendible solo en forma acotada: no encontré en esta búsqueda limitada trabajo que combine (i) un lector tercero ciego que infiere el lado del usuario desde la respuesta, con (ii) eliminación previa de toda frase que mencione o evalúe la opinión del usuario, para separar eco de encuadre. Los conceptos vecinos (perspective sycophancy de Jain et al.; sycophancy implícita/social de ELEPHANT; sycophancy política por identidad) miden otra cosa o en otra dirección. La búsqueda fue acotada (pocas consultas, sin Google Scholar ni revisión de citas hacia adelante), por lo que "nuevo" debe formularse como ausencia de hallazgo, no como prioridad probada.

Oración propuesta para el post:

"En una búsqueda bibliográfica acotada no encontramos trabajo previo que mida si un lector externo ciego puede inferir de qué lado estaba el usuario a partir de la respuesta del modelo después de eliminar todas las frases que mencionan o evalúan su opinión; los trabajos cercanos (perspective sycophancy, sycophancy social, sycophancy política por identidad) miden la similitud percibida por el propio usuario o el cambio de la respuesta según la identidad, no esta inferencia residual."

Advertencias: (1) la inferencia de un lector LLM puede capturar también rasgos del prompt filtrados de otras formas; (2) el borrado por LLM puede ser imperfecto; (3) los intervalos para SWE-2 y Opus 5.5 deberían reportarse igual que el de Sol 6.1.
