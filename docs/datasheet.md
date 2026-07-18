# Datasheet for Dataset — Give Me Some Credit

Ficha de datos (formato Gebru et al., *Datasheets for Datasets*) del dataset
usado en este proyecto.

## Motivación

- **¿Por qué se creó el dataset?** Competencia de Kaggle (2011) para predecir la
  probabilidad de que un solicitante de crédito incurra en impago severo en los
  próximos 2 años, con fines de scoring crediticio.
- **¿Quién lo creó?** Kaggle / Credit Fusion, en el marco de la competencia
  "Give Me Some Credit".
- **¿Quién lo financió?** No documentado públicamente por el proveedor de la
  competencia.

## Composición

- **¿Qué representan las instancias?** Cada fila es un solicitante de crédito
  individual (persona natural).
- **¿Cuántas instancias hay?** 150,000 en el set de entrenamiento (`cs-training.csv`).
- **¿Contiene datos sensibles?** No incluye variables directas de género, etnia o
  ubicación; `age` es la única variable demográfica. El desempeño del modelo se
  desagregó por tramo de edad (ver `docs/model_card.md`): no se observó una
  disparidad grave, aunque el modelo discrimina algo peor en solicitantes
  menores de 35 años.
- **¿Hay valores faltantes?** Sí, en `MonthlyIncome` (19.8%) y `NumberOfDependents`
  (2.6%). Ambas se tratan como faltantes genuinos e imputan con la mediana del
  conjunto de entrenamiento (ver `docs/diccionario_datos.md`).
- **¿Existen errores conocidos?** Códigos 96/98 en las variables de días de atraso
  no son conteos válidos (ver diccionario de datos).

## Proceso de recolección

- **¿Cómo se recolectaron los datos?** No documentado en detalle por el
  proveedor de la competencia; se declara como limitación del dataset.
- **¿Sobre qué población son representativos?** Solicitantes de crédito en EE.UU.
  (según origen de la competencia); no representativo de otras geografías —
  limitación relevante si se extrapola el modelo a otro mercado.

## Preprocesamiento / etiquetado

- La variable objetivo (`SeriousDlqin2yrs`) ya viene etiquetada por el
  proveedor del dataset. La limpieza aplicada (tratamiento de los códigos de
  error 96/98, imputación de `MonthlyIncome`/`NumberOfDependents`/`age`, y
  winsorización de `RevolvingUtilizationOfUnsecuredLines`/`DebtRatio`) se
  documenta en `docs/diccionario_datos.md` y se implementa en
  `notebooks/src/preprocessing.py`.

## Usos previstos y desaconsejados

- **Uso previsto:** ejercicio académico de scoring crediticio y demostración del
  ciclo completo EDA → predictivo → prescriptivo → tablero.
- **Uso desaconsejado:** no usar el modelo resultante para decisiones reales de
  crédito sin revalidación con datos locales, actuales y una auditoría de sesgo
  formal (dataset desactualizado y de otra geografía).

## Distribución y mantenimiento

- **Distribución:** disponible públicamente en Kaggle bajo los términos de la
  competencia.
- **Mantenimiento:** dataset estático (no se actualiza); cualquier proyecto que
  lo use en producción necesitaría datos propios y vigentes.
