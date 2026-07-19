# Proyecto Grupal — Riesgo Crediticio

Proyecto del curso de Analítica de Datos. Construye un producto de datos completo
sobre riesgo de crédito (probabilidad de default de clientes) siguiendo las cinco
partes del Proyecto Grupal: EDA, descriptivo, predictivo, prescriptivo y tablero.

## Dataset

[Give Me Some Credit](https://www.kaggle.com/c/GiveMeSomeCredit) (Kaggle).
~150,000 registros, variable objetivo `SeriousDlqin2yrs` (impago severo a 2 años).
Ver [docs/diccionario_datos.md](docs/diccionario_datos.md) para el detalle de variables
, [docs/datasheet.md](docs/datasheet.md) para la ficha completa del dataset y resumen ejecutivo [docs/resumen_ejecutivo.md](docs/resumen_ejecutivo.md).

el dataset  [raw/cs-training.csv](cs-training.csv) desde Kaggle.

## Estructura del repositorio

```
datos/
  raw/          datos originale
  processed/    datos limpios/transformados
notebooks/
  P1_eda_estadistica.ipynb
  P2_descriptivo.ipynb
  P3_predictivo.ipynb
  P4_prescriptivo.ipynb
  src/          código reutilizable (carga de datos, features, utilidades)
  figures/      figuras generadas por los notebooks (P2, P3, P4)
powerbi/        tablero HTML (dashboard.html + dashboard_data.json) y los
                datasets CSV para Power BI Service (ver docs/guia_powerbi.md)
docs/           diccionario de datos, datasheet, model card, guía del tablero,
                resumen ejecutivo
presentacion/   diapositivas de la exposición
exposición/     enlace del video y participación
README.md
```

## Entorno

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Todas las semillas aleatorias se fijan mediante `notebooks/src/config.py::SEED`
para garantizar reproducibilidad. Cada notebook se ejecuta de principio a fin
sin errores ("Restart & Run All"), con `notebooks/` como directorio de trabajo.

## Mapeo con las partes del Proyecto Grupal

| Parte | Notebook | Documentación | Comunicación |
|---|---|---|---|
| P1 — Estadística/EDA | `notebooks/P1_eda_estadistica.ipynb` | Diccionario de datos, Datasheet | Hallazgos descriptivos |
| P2 — Descriptivo | `notebooks/P2_descriptivo.ipynb` | Bitácora de patrones | Síntesis de patrones |
| P3 — Predictivo | `notebooks/P3_predictivo.ipynb` | Model Card, métricas de validación | Resumen de desempeño |
| P4 — Prescriptivo | `notebooks/P4_prescriptivo.ipynb` | Supuestos y restricciones | Recomendación de decisión |

## Exposición

Ver [exposición/orden_participacion.txt](exposición/orden_participacion.txt)
para el orden y tiempos de participación del equipo, y
[exposición/enlace_video.txt](exposición/enlace_video.txt) (o el archivo
`.mp4` en esa misma carpeta) para el video grabado de la sustentación grupal.

