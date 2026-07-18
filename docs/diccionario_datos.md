# Diccionario de datos — Give Me Some Credit

Fuente: `datos/raw/cs-training.csv` (Kaggle, [Give Me Some Credit](https://www.kaggle.com/c/GiveMeSomeCredit)).
Unidad de análisis: un cliente/solicitante de crédito por fila.

| Variable | Tipo | Dominio / unidad | Significado de negocio | Reglas de calidad conocidas |
|---|---|---|---|---|
| `SeriousDlqin2yrs` | binaria (0/1) | 0 = sin impago severo, 1 = impago severo | **Variable objetivo.** Impago de 90+ días en los siguientes 2 años | Desbalanceada (~6.7% de positivos) |
| `RevolvingUtilizationOfUnsecuredLines` | continua | proporción (puede exceder 1) | Saldo total de tarjetas y líneas de crédito no garantizadas sobre el límite total | Valores > 1 o extremos indican posible error de captura |
| `age` | entera | años | Edad del solicitante | Verificar registros con edad = 0 (dato faltante disfrazado) |
| `NumberOfTime30-59DaysPastDueNotWorse` | entera | conteo, últimos 2 años | Veces con atraso de 30-59 días sin llegar a peor | Valores 96/98 son códigos de error/missing, no conteos reales |
| `DebtRatio` | continua | razón | Pagos de deuda + gastos fijos sobre ingreso mensual bruto | Presenta outliers extremos cuando `MonthlyIncome` es bajo o nulo |
| `MonthlyIncome` | continua | moneda | Ingreso mensual bruto | Alto porcentaje de valores faltantes (~20%); requiere imputación documentada |
| `NumberOfOpenCreditLinesAndLoans` | entera | conteo | Líneas de crédito y préstamos abiertos | — |
| `NumberOfTimes90DaysLate` | entera | conteo, últimos 2 años | Veces con atraso de 90+ días | Mismos códigos de error 96/98 que la variable de 30-59 días |
| `NumberRealEstateLoansOrLines` | entera | conteo | Préstamos hipotecarios y líneas sobre inmuebles (incluye home equity) | — |
| `NumberOfTime60-89DaysPastDueNotWorse` | entera | conteo, últimos 2 años | Veces con atraso de 60-89 días sin llegar a peor | Mismos códigos de error 96/98 |
| `NumberOfDependents` | entera | conteo | Dependientes del solicitante (excluyéndose a sí mismo) | Pequeño porcentaje de valores faltantes |

## Notas de preprocesamiento (confirmadas en P1 — ver `notebooks/P1_eda_estadistica.ipynb`)

- **Códigos 96/98** (269 filas, 0.18%): no son conteos válidos. Su tasa de impago real
  es 54.6% (~8x la tasa base de 6.68%), por lo que no deben eliminarse ni imputarse
  con la media sin más — se recomienda crear una variable binaria `flag_codigo_error`
  antes de imputar el valor numérico, para no perder la señal de riesgo.
- **`MonthlyIncome`** (19.8% faltante) y **`NumberOfDependents`** (2.6% faltante):
  imputar (ej. mediana condicionada a `age`/`NumberOfOpenCreditLinesAndLoans`) y
  documentar el método elegido en P3 antes de derivar `DebtRatio`.
- **`RevolvingUtilizationOfUnsecuredLines` > 1** (3,321 filas, 2.2%, máx. 50,708):
  winsorizar o topear en 1-2 (dado que teóricamente es una proporción).
- **`DebtRatio` > 1** (35,137 filas, 23.4%, máx. 329,664): distorsionado por
  `MonthlyIncome` bajo/nulo; recalcular tras imputar ingreso y winsorizar el resto.
- **`age == 0`** (1 fila): valor faltante disfrazado; tratar como NaN e imputar.
