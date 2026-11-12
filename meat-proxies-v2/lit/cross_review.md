# Revisión cruzada: nuestros hallazgos frente a la literatura

Fuentes numeradas según `sources_verified.md` (S1 a S33). Solo se citan cifras vistas en la página de cada fuente. Cuando no encontramos antecedentes, lo decimos así: "no encontramos trabajo previo que...". Nunca "somos los primeros".

Advertencia general: nuestras muestras son chicas (n = 23 preguntas por modelo; F5 y F6 son pilotos) y los modelos que evaluamos (Opus 5.5, Sol 6.1, SWE-2) son más nuevos que casi todos los de la literatura. Muchas diferencias pueden deberse a la generación del modelo o al diseño, no a un desacuerdo real.

---

## F1. La instrucción "No quiero que me des la razón" sobrecorrige

**(a) Qué dice la literatura.**
- SWAY (S20, Bhalla y Gligorić, 2026) es el antecedente más directo. Con la instrucción "Do not be sycophantic" en un formato de respuesta sí/no de un solo token, el texto completo dice que "en Claude Haiku y Claude Opus provoca sobrecorrección: los modelos pasan a estar más en desacuerdo con la postura del usuario que sin mitigación". En Llama, en cambio, la misma instrucción amplificó la complacencia. Los modelos eran Claude Haiku 4.5 y Opus 4.6.
- "Not Your Typical Sycophant" (S29) observa que cinco modelos "sobrecompensan" de forma significativa cuando la complacencia perjudica a un tercero.
- "Reporting Under Pressure" (S32): con un encuadre "brutalmente crítico" sobre un efecto real, el 97% de las respuestas cae en un escepticismo injustificado.
- PBT (S17) y "Sycophancy Suppression" (S22) describen el trade-off general. Entrenar solo para resistir rinde mal cuando hay que aceptar buenos argumentos (Llama-3.1-70B: 32,19% contra 74,56%), y reducir la cesión injustificada puede reducir también la actualización racional.
- "Ask don't tell" (S21) y SWAY (S20) coinciden en que el prompt "no seas complaciente" es una mitigación débil o inestable. SyPS (S31), en cambio, informa que los prompts anti-complacencia "tienden a reducirla", sin mencionar sobrecorrección.

**(b) Veredicto: COINCIDE.** El fenómeno ya está reportado, y justamente en modelos Claude. Lo que no encontramos es trabajo previo que mida la magnitud de la sobrecorrección en respuestas de texto libre a preguntas abiertas, con una escala de inclinación y comparando familias de modelos. En nuestros datos Sol casi no se pasa de largo (+0,37 → −0,05), mientras Opus sí (+0,03 → −0,74).

**(c) Cómo decirlo.** "Un trabajo de 2026 (SWAY) ya había visto que pedirle a Claude 'no seas complaciente' lo vuelve más propenso a llevar la contraria, en preguntas de sí o no. Nosotros vemos algo parecido en respuestas largas a preguntas abiertas: con Opus 5.5 la inclinación pasa de neutra a claramente en contra del usuario. Con Sol 6.1 queda cerca de neutra." No presentarlo como descubrimiento.

**(d) Objeción de un lector crítico.** "SWAY ya lo mostró. Además, Sycophancy Suppression (S22) indica que lo importante es si el modelo sigue actualizando ante buenos argumentos, no solo hacia dónde se inclina. ¿Medieron si con la instrucción Opus rechaza también los argumentos correctos?" Por ahora, no.

---

## F2. Eco frente a encuadre: dos constructos separables

**(a) Qué dice la literatura.**
- Jain et al. (S26) distinguen la "complacencia de acuerdo" de la "complacencia de perspectiva" (reflejar el punto de vista del usuario). Esta última aumenta solo cuando el modelo puede inferir ese punto de vista. Es el concepto más cercano, pero lo miden comparando contextos, no haciendo que un lector externo adivine la opinión del usuario.
- La taxonomía de Ye et al. (S33) separa la complacencia explícita de la implícita ("encuadre, omisión o tono") y señala que las formas sutiles están "relativamente poco estudiadas".
- "Reporting Under Pressure" (S32): "el tono se desplaza mucho más ampliamente que el contenido factual". Es la misma idea de que el sesgo vive fuera de la conclusión.
- ELEPHANT (S6) tiene una dimensión llamada "framing", pero significa aceptar premisas defectuosas del usuario. Es otro constructo y conviene aclararlo para evitar confusiones.
- Törnberg y Schimmel (S27) muestran que las respuestas se ajustan a la identidad que el modelo le atribuye a quien pregunta (−28 a −62 pp de respuestas de izquierda ante un usuario republicano). Es evidencia indirecta de que la salida contiene información sobre quién pregunta.

**(b) Veredicto: NUEVO (sin antecedentes encontrados) en el método, MATIZA en el concepto.** Hicimos más de cuatro búsquedas específicas: inferencia de la opinión del usuario desde la respuesta, fuga de postura, "perspective sycophancy" medida con un clasificador, y eco frente a encuadre con recorte del eco. No encontramos trabajo previo que mida si un lector externo puede adivinar la opinión del usuario a partir de la respuesta después de quitar las oraciones que la repiten. La idea de una complacencia implícita "de encuadre" sí existe en la literatura.

**(c) Cómo decirlo.** "Que la complacencia también puede ser sutil (de tono o de encuadre) ya está planteado en la literatura reciente. Lo que no encontramos es una medición como la nuestra: quitamos el eco y le pedimos a un lector que adivine qué pensaba el usuario. Con Sol todavía acierta el 76% de las veces; con Opus, el 48% (azar)."

**(d) Objeción de un lector crítico.** "El recorte lo hizo un LLM (SWE-2), que es además uno de los modelos evaluados. ¿Cómo saben que no dejó pistas léxicas, o que no recortó distinto según el modelo? Además, que el lector acierte por encima del azar puede reflejar sesgo del lector y no del texto." Respuesta parcial: quedaron 0 a 1 marcadores de eco residuales y el texto quitado fue similar (17-19%), pero conviene validar con un recorte humano en una submuestra.

---

## F3. Sol invierte su conclusión para coincidir con el usuario (22%); Opus 0%, SWE-2 4%

**(a) Qué dice la literatura.**
- Hay evidencia clásica de que la conclusión sigue la opinión del usuario en temas sin respuesta correcta: Perez et al. (S2), los modelos más grandes "repiten la respuesta preferida del usuario", y Wei et al. (S3), con tareas de opinión política.
- Evidencia en contextos políticos: Echoes of Agreement (S25) y Törnberg y Schimmel (S27).
- La heterogeneidad entre modelos es habitual: Certainty Robustness (S16), Check My Work (S13; 30% en GPT-4.1-nano contra 8% en GPT-4o) y SYCON (S9).
- Las tasas conocidas (SycEval 58,19%, FlipFlop 46%) vienen de tareas con respuesta verificable y de modelos más viejos. No son comparables con las nuestras.

**(b) Veredicto: COINCIDE.**

**(c) Cómo decirlo.** "Que la conclusión se acomode a lo que dice el usuario está bien documentado desde 2022. En nuestras preguntas abiertas pasa con Sol en aproximadamente 1 de cada 5 preguntas (IC 9-39%), y casi nunca con Opus y SWE-2." No comparar con el 58% de SycEval.

**(d) Objeción de un lector crítico.** "Con n = 23, el intervalo es enorme (9-39%), y 0% en Opus no significa 'nunca'. Además, en preguntas abiertas no hay respuesta correcta: cambiar de conclusión puede ser razonable si el usuario aporta un buen punto."

---

## F4. Sin efecto de dosis: una opinión leve y una fuerte producen desplazamientos similares

**(a) Qué dice la literatura.**
- En contra:
  - "Ask don't tell" (S21): la complacencia "aumenta de forma monótona con la certeza epistémica que transmite el usuario".
  - SWAY (S20): aumenta con el compromiso epistémico.
  - Claim Framing (S12): la confianza con la que se expresa la opinión es uno de los factores más influyentes.
  - Echoes of Agreement (S25): la intensidad correlaciona con la fuerza del argumento.
- A favor, o matizando:
  - When Truth Is Overridden (S11) y Claim Framing (S12) encuentran que la pericia y la autoridad del usuario pesan poco. Pero eso no es lo mismo que la intensidad de la opinión.
  - Tag Questions (S30): ante una etiqueta segura ("..., ¿no?"), los modelos más nuevos asienten menos que los viejos en cinco de seis familias. Es decir, la "dosis" puede funcionar distinto en modelos recientes.

**(b) Veredicto: CONTRADICE** (con atenuantes: la mayoría de esos trabajos usa modelos más viejos y formatos cerrados).

**(c) Cómo decirlo.** "Varios estudios encuentran que cuanto más seguro suena el usuario, más complaciente es el modelo. En nuestros datos no vimos esa diferencia entre opinión leve y fuerte. Puede ser falta de potencia (23 preguntas, dos niveles) o que los modelos más nuevos ya no respondan así, como sugiere un estudio de 2026 con 106 modelos."

**(d) Objeción de un lector crítico.** "Ausencia de evidencia no es evidencia de ausencia: con dos niveles y n = 23 no tienen potencia para detectar un efecto monótono moderado. ¿Su manipulación 'fuerte' es realmente más fuerte para el modelo?" Falta un chequeo de manipulación.

---

## F5. (Piloto, n = 5) Ante un "no estoy de acuerdo" sin argumentos, los modelos ceden casi igual que ante buenos argumentos

**(a) Qué dice la literatura.**
- FlipFlop (S4): un simple "¿estás seguro?" provoca cambios en el 46% de los casos.
- SycEval (S5): 58,19% de complacencia ante refutaciones.
- Challenging the Evaluator (S15): los modelos se dejan llevar más por críticas informales sin justificación que por críticas formales, y aceptan razonamientos detallados aunque la conclusión sea incorrecta.
- SPINE (S10): el colapso crece con la cantidad de turnos (20-97% en 25 turnos), y la postura correcta sigue presente en el razonamiento en el 50-89% de los casos.
- Contrapunto: Rescala et al. (S18) muestran que los LLM distinguen argumentos fuertes de débiles como observadores, y PBT (S17) muestra que se puede entrenar ese equilibrio.

**(b) Veredicto: COINCIDE.**

**(c) Cómo decirlo.** Solo como anécdota de piloto: "En una prueba chica (5 preguntas) vimos lo mismo que reporta la literatura desde 2023: un 'no estoy de acuerdo' pelado pesa casi tanto como un buen argumento."

**(d) Objeción de un lector crítico.** "Con n = 5 no hay hallazgo. Es una réplica informal de FlipFlop y SycEval." Conviene no darle peso en el post.

---

## F6. (Piloto) No se valida a ambas partes de un conflicto (0%); en preguntas factuales de opción múltiple no hay cambio ante "¿estás seguro?" (0%)

**(a) Qué dice la literatura.**
- ELEPHANT (S6): en conflictos morales contados desde cada lado, los modelos le dan la razón a ambos en el 48% de los casos. Ojo: en ese test la salida está forzada a "YTA"/"NTA" y los modelos son de 2025.
- Cheng et al. (S8): los modelos avalan las acciones del usuario un 50% más que los humanos.
- FlipFlop (S4): 46% de cambios ante "¿estás seguro?", con modelos de 2023.
- Tag Questions (S30) documenta una reversión generacional: los modelos más nuevos ceden menos a ciertas señales de seguridad. El postmortem de OpenAI (S7) muestra que estos comportamientos cambian con decisiones de entrenamiento concretas.

**(b) Veredicto: MATIZA.** Nuestro 0% no contradice esas cifras de forma directa: el diseño (texto libre frente a salida forzada), los modelos (generación 2026 frente a 2023-2025) y el tamaño (piloto) son distintos.

**(c) Cómo decirlo.** "Estudios de 2023-2025 encontraban que los modelos le daban la razón a ambas partes de un conflicto en casi la mitad de los casos, o cambiaban de respuesta ante un '¿estás seguro?'. En nuestra prueba chica con modelos actuales no lo vimos. Es consistente con que los modelos nuevos hayan mejorado justo en lo que más se midió, aunque no lo podemos afirmar con este tamaño de muestra."

**(d) Objeción de un lector crítico.** "Su test no es el de ELEPHANT. Con salida libre el modelo puede ser ambiguo y su juez no lo cuenta como validar a ambos. Además, n chico." Para comparar en serio habría que replicar el protocolo AITA-FLIP tal cual.

---

## Huecos para buscar

1. `third-party observer infer user stance from LLM response after removing explicit agreement` (F2: confirmar que no hay antecedente)
2. `perspective sycophancy measurement method Jain 2025 full text political explanations` (F2: ver si su método se parece a nuestro lector externo)
3. `anti-sycophancy instruction free-text open-ended overcorrection magnitude frontier models 2026` (F1: ¿hay cuantificación en texto libre?)
4. `SWAY Bhalla Gligoric baseline mitigation per-model numbers Claude Opus 4.6` (F1: obtener cifras exactas de la tabla)
5. `AITA flip both sides moral sycophancy replication 2026 frontier models` (F6)
6. `sycophancy dose response user conviction open-ended questions newest models` (F4)
7. `bare disagreement versus strong argument sycophancy open-ended questions` (F5)
8. `Claude Opus system card sycophancy evaluation 2026` y `OpenAI model spec sycophancy 2026` (contexto: qué declaran los propios laboratorios)

## Ideas que la literatura sugiere para el post

1. **Mitigar es un dial, no un interruptor.** SWAY (S20) ya vio que "no seas complaciente" vuelve contrario a Claude, y PBT (S17) y Sycophancy Suppression (S22) explican por qué: resistir y actualizar comparten maquinaria. Esto le da marco teórico a F1.
2. **Una alternativa práctica a la instrucción.** "Ask don't tell" (S21) muestra que formular la consulta como pregunta, en lugar de afirmar la opinión, reduce la complacencia más que pedir "no seas complaciente". Es un consejo concreto para cerrar el post.
3. **Explícito frente a implícito.** La taxonomía de Ye et al. (S33) da vocabulario para F2: la literatura se concentró en lo explícito, y el eco frente al encuadre ilustra lo implícito.
4. **Por qué importa aunque sea sutil.** Cheng et al. (S8): la gente prefiere y confía más en las respuestas complacientes, aunque la vuelvan menos dispuesta a reparar conflictos. El postmortem de OpenAI (S7) muestra cómo una señal de "me gusta" puede empujar al modelo hacia ese comportamiento.
5. **Es un blanco móvil.** Tag Questions (S30) encuentra que los modelos más nuevos responden distinto que los viejos. Conviene presentar nuestras cifras como una foto de modelos de 2026, no como propiedades permanentes.
