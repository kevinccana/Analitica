# Guion de exposición — Riesgo Crediticio (~10 minutos)

Guion hablado para las 13 diapositivas de `reports/presentacion.html`. Los
tiempos son orientativos (suman ~9 min, dejando margen para transiciones y
preguntas). Practícalo en voz alta al menos una vez — leer el guion tal cual
suena forzado; úsalo como guía, no como libreto.

---

## 1. Título — (15 s)

"Buenos días/tardes. Vamos a presentar un producto de datos completo sobre
riesgo crediticio: partimos de datos crudos de solicitantes de crédito y
llegamos a una recomendación concreta de a quién aprobar. Todo el proceso
está en este repositorio, y hoy les muestro lo esencial en 10 minutos."

## 2. El problema — (40 s)

"Toda decisión de crédito es una apuesta bajo incertidumbre. Si aprobamos de
más, perdemos dinero en impagos. Si rechazamos de más, perdemos negocio
rentable con clientes que sí habrían pagado. La pregunta que queremos
resolver no es solo '¿quién va a pagar?', sino '¿a quién le conviene al
negocio aprobarle, y con qué evidencia tomamos esa decisión?'. Ese es el hilo
conductor de todo el proyecto."

## 3. El dataset — (35 s)

"Trabajamos con el dataset público Give Me Some Credit, de Kaggle: 150 mil
solicitantes de crédito, con 10 variables de comportamiento —edad, ingreso,
utilización de líneas de crédito, historial de atrasos, entre otras—. La
variable que queremos predecir es si el cliente cae en impago severo, es
decir, 90 días o más de atraso, en los siguientes 2 años. Solo el 6.7% de los
clientes históricos cae en impago: es una cartera desbalanceada, y eso va a
condicionar cómo evaluamos todo lo que viene después."

## 4. Metodología — (30 s)

"Organizamos el trabajo en cinco etapas, que corresponden a las cinco partes
del proyecto: primero exploramos y limpiamos los datos, luego buscamos
patrones descriptivos, después construimos un modelo predictivo de
probabilidad de impago, con eso diseñamos una política prescriptiva de
aprobación de crédito, y finalmente lo comunicamos todo en un tablero. Vamos
a recorrer los hallazgos más importantes de cada etapa."

## 5. P1 — Hallazgos del EDA — (60 s)

"Antes de modelar nada, la limpieza de datos ya nos dio información valiosa.
Primero: encontramos un código de error, '96' o '98', en las variables de
atraso, que en teoría no son conteos válidos. La sorpresa fue que esas filas
tienen 54.6% de tasa de impago real, ocho veces la tasa base — es decir, no
son ruido, concentran riesgo altísimo, y hay que tratarlas con cuidado, no
simplemente descartarlas. Segundo: la variable DebtRatio, que mide deuda
sobre ingreso, se distorsiona muchísimo cuando el ingreso reportado es casi
cero. Y tercero, quizás el hallazgo más útil para el negocio: el ingreso y el
patrimonio del cliente NO son los mejores predictores de riesgo — lo que
mejor separa a buenos y malos pagadores es su comportamiento de pago
reciente."

## 6. P2 — Segmentación — (55 s)

"Con esos datos ya limpios, hicimos un clustering para encontrar perfiles de
cliente. Encontramos cuatro segmentos. El más importante: un segmento de
alto riesgo que es solo el 5% de la cartera, pero concentra 45% de tasa de
impago — son clientes más jóvenes, que ya están usando casi todo su cupo de
crédito disponible y tienen atrasos activos. También encontramos dos
segmentos de bajo riesgo con perfiles económicos opuestos —uno de alto
patrimonio, otro más modesto— y un cuarto segmento que confirma el hallazgo
anterior: tiene un DebtRatio altísimo pero riesgo real bajo, así que esa
variable, usada sola, puede engañar."

## 7. P3 — Modelo predictivo — (50 s)

"Con esos patrones como base, entrenamos un modelo de scoring: comparamos una
regresión logística simple contra un modelo más sofisticado, LightGBM.
LightGBM ganó, con un AUC de 0.869 contra 0.862 de la regresión logística —
en otras palabras, el modelo distingue correctamente entre un buen y un mal
pagador en 87 de cada 100 comparaciones posibles. Pero noten que la mejora
sobre el modelo lineal es chica: solo 0.7 puntos. Eso nos dice que casi toda
la señal predictiva ya es capturable con un modelo simple y explicable, algo
importante si en algún momento hay que justificar la decisión ante un
regulador o un cliente."

## 8. P4 — Política de aprobación — (55 s)

"Ahora la parte que conecta el modelo con una decisión de negocio. Definimos
supuestos explícitos: una tasa de interés del 18%, una pérdida del 60% del
monto en caso de impago, y un monto de crédito de referencia de 10 mil
dólares. Con eso, calculamos la utilidad esperada de aprobar a cada cliente
según su probabilidad de impago, y encontramos el punto óptimo: aprobar a
quien tenga menos de 23% de probabilidad de impago, lo que representa
aproximadamente el 55% de los solicitantes. Esa política deja la cartera
aprobada con solo 1% de impago real — muy por debajo de cualquier límite de
riesgo razonable, como un 5%."

## 9. P4 — Sensibilidad — (40 s)

"Un hallazgo interesante del análisis de sensibilidad: la tasa de interés que
se le ofrece al cliente pesa más en la rentabilidad que afinar el modelo.
Si subimos la tasa a 24%, la utilidad esperada casi se duplica, porque
podemos aprobar más cartera sin perder rentabilidad. En cambio, si la pérdida
en caso de impago fuera mayor —un 80% en vez de 60%— la utilidad cae bastante
y hay que ser más conservador al aprobar. La conclusión para el negocio: el
precio del crédito es una palanca más potente que el score."

## 10. P5 — Tablero — (35 s)

"Todo esto lo consolidamos en un tablero interactivo, hecho en HTML puro —
sin Power BI, sin servidor, sin necesidad de conexión a internet: se abre con
doble clic en cualquier navegador. Ahí están los KPIs principales, la
segmentación, el desempeño del modelo y la política de aprobación, todo en
un solo lugar, con gráficos donde se puede pasar el cursor para ver el valor
exacto de cada dato."

## 11. Recomendación — (30 s)

"Si tuviera que resumir todo en una frase, sería esta: aprobar solicitudes
con probabilidad de impago menor a 23% genera una utilidad esperada de
aproximadamente 511 dólares por solicitante, con solo 1% de riesgo real en la
cartera aprobada — muy por debajo del límite de riesgo que nos habíamos
propuesto. Eso significa que, con estos supuestos, el negocio tiene margen
para ser incluso un poco más agresivo si buscara crecer la cartera."

## 12. Limitaciones y próximos pasos — (40 s)

"Para ser honestos sobre los límites de este trabajo: asumimos un monto de
crédito uniforme de 10 mil dólares para todos los clientes, que es la
simplificación más fuerte del ejercicio — en la práctica debería variar según
la capacidad de pago de cada uno. Además, si este modelo se llevara a
producción, necesitaríamos un plan de monitoreo de cómo cambian los datos y
el comportamiento de los clientes en el tiempo. Y por supuesto, antes de usarlo
con datos reales, habría que revalidarlo, porque este dataset es de otra
época y otra geografía."

## 13. Cierre — (10 s)

"Con esto cerramos. Muchas gracias — quedamos abiertos a preguntas."

---

## Notas generales para la exposición

- **Ritmo:** si van sobrando/faltando segundos, las diapositivas 5, 6 y 8 son
  las que más se pueden acortar sin perder el mensaje central; la 11
  (recomendación) es la que menos se debe recortar — es la conclusión de todo.
- **Si preguntan "¿por qué LightGBM y no otro modelo?"**: porque comparamos
  contra un baseline (regresión logística) con las mismas métricas (AUC y
  KS) y ganó, aunque por poco — ver Model Card (`docs/model_card.md`) para el
  detalle completo.
- **Si preguntan por los supuestos de P4**: son explícitos y están
  documentados en `docs/model_card.md` y en el notebook `P4_prescriptivo.ipynb`,
  junto con el análisis de sensibilidad — no son un número arbitrario.
