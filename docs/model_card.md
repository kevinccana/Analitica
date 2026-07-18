# Model Card — Modelo de Scoring de Riesgo Crediticio

Ficha de modelo (formato Mitchell et al., *Model Cards for Model Reporting*),
que documenta el modelo de scoring desarrollado en `P3_predictivo.ipynb`.

## Detalles del modelo

- **Autor:** Jeison Kevin Ccana Romero
- **Versión:** v1.0 (`models/scoring_model_v1.joblib`)
- **Fecha:** 2026-07-13
- **Tipo de modelo / arquitectura:** LightGBM (`LGBMClassifier`), gradient
  boosting sobre árboles. Se comparó contra un baseline de regresión logística
  (`sklearn.linear_model.LogisticRegression`, con `StandardScaler`); LightGBM
  ganó en ambas métricas y se seleccionó como modelo final.
- **Hiperparámetros clave:** `n_estimators=300`, `learning_rate=0.05`,
  `num_leaves=31`, `class_weight='balanced'`, `random_state=42`.
- **Código / experimento asociado:** `notebooks/P3_predictivo.ipynb`;
  experimento MLflow `riesgo_crediticio` (runs `logreg_baseline` y
  `lightgbm`), tracking en `mlflow.db` (backend sqlite, ver `src/config.py`).

## Uso previsto

- **Caso de uso:** estimar la probabilidad de impago severo de un solicitante de
  crédito a 2 años, como insumo para una política de aprobación/límite (ver P4).
- **Usuarios objetivo:** equipo académico del curso; no apto para uso productivo
  real sin revalidación (ver Datasheet, sección "usos desaconsejados").

## Datos de entrenamiento / evaluación

- **Origen:** Give Me Some Credit (Kaggle). Ver [datasheet.md](datasheet.md).
- **Partición:** 85/15 train/test (127,500 / 22,500 filas), estratificada por
  `SeriousDlqin2yrs` dado el desbalance de clases (6.68% de positivos en
  ambos conjuntos). La limpieza (`fit_preprocessing`, ver
  [diccionario_datos.md](diccionario_datos.md)) se ajustó solo con el train
  para evitar fuga de información hacia el test.
- **Periodo representado:** dataset histórico (~2011), sin fecha exacta de corte
  documentada por el proveedor.

## Métricas de desempeño

- **Métricas principales (test, n=22,500):**

  | Modelo | AUC-ROC | KS |
  |---|---|---|
  | Regresión logística (baseline) | 0.862 | 0.565 |
  | **LightGBM (final)** | **0.869** | **0.580** |

  Al umbral que maximiza KS (0.411): precisión=0.192, recall=0.830 y
  f1=0.312 para la clase de impago (1); recall alto es intencional dado el
  costo asimétrico de un falso negativo (cliente que impaga y fue aprobado)
  frente a un falso positivo (cliente bueno rechazado) — ver P4 para la
  cuantificación económica de este trade-off.
- **Desagregación por tramo de edad** (única variable demográfica disponible):

  | Tramo | n (test) | Tasa de impago real | AUC |
  |---|---|---|---|
  | <35 años | 3,234 | 12.1% | 0.846 |
  | 35-49 años | 7,326 | 8.4% | 0.846 |
  | 50-64 años | 7,683 | 5.2% | 0.865 |
  | 65+ años | 4,257 | 2.2% | 0.867 |

  El modelo discrimina ligeramente mejor en clientes mayores (AUC ~0.865-0.867)
  que en los más jóvenes (AUC ~0.846), aunque la diferencia es pequeña
  (<0.02). No se observa una caída abrupta de desempeño en ningún tramo.
- **Comparación contra baseline:** LightGBM mejora el AUC en +0.007 y el KS en
  +0.015 frente a la regresión logística; la mejora es modesta, lo que sugiere
  que gran parte de la señal predictiva es capturable con un modelo lineal
  simple (relevante para la elección de modelo en un contexto donde la
  interpretabilidad importa).

## Consideraciones éticas

- `age` es la única variable demográfica disponible y se usa como predictor
  directo. La desagregación por tramo (sección anterior) no muestra
  disparidad grave de AUC entre tramos, pero el modelo sí discrimina algo
  peor en los solicitantes más jóvenes (<35 años) — el tramo con mayor tasa
  de impago real (12.1%). Cualquier uso real debería auditar si esto se
  traduce en una tasa de rechazo desproporcionada para ese grupo.
- El umbral elegido (KS) prioriza fuertemente el recall de impago (0.83)
  sobre la precisión (0.19): en un despliegue real esto implica rechazar a
  muchos clientes que sí habrían pagado (5,240 falsos positivos en el test)
  a cambio de capturar la mayoría de los que no pagarían. Esta es una
  decisión de negocio, no solo técnica — debe validarse con el área de
  riesgo antes de fijar el umbral de producción (ver P4).
- El dataset no representa la población local del equipo (otro país/época);
  cualquier despliegue real requeriría reentrenar con datos representativos.

## Limitaciones y recomendaciones

- No usar para decisiones de crédito reales sin revalidación (ver Datasheet).
- El modelo hereda las limitaciones de los datos de entrada: los códigos de
  error 96/98 (0.18% de los casos) se tratan como faltantes e imputan con la
  mediana, lo que puede subestimar el riesgo de ese subgrupo específico pese
  a que su tasa de impago real es 8x la base (ver P1, hallazgo 2).
- `DebtRatio` sigue siendo una variable ruidosa para solicitantes con ingreso
  reportado muy bajo o nulo, incluso tras la winsorización (ver P1, hallazgo 4).
- Plan de monitoreo si el modelo se usara en producción: vigilar deriva de
  datos (distribución de `RevolvingUtilizationOfUnsecuredLines`, `DebtRatio`,
  ingreso) y deriva de concepto (relación entre variables y tasa de impago
  real observada), con alertas si el AUC out-of-time cae por debajo de 0.80
  (referencia: sección 7.5 del curso, herramientas como Evidently AI).
