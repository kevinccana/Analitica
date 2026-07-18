# Proyecto Grupal — Riesgo Crediticio

Proyecto del curso de Analítica de Datos. Construye un producto de datos completo
sobre riesgo de crédito (probabilidad de default de clientes) siguiendo las cinco
partes del Proyecto Grupal: EDA, descriptivo, predictivo, prescriptivo y tablero.

## Dataset

[Give Me Some Credit](https://www.kaggle.com/c/GiveMeSomeCredit) (Kaggle).
~150,000 registros, variable objetivo `SeriousDlqin2yrs` (impago severo a 2 años).
Ver [docs/diccionario_datos.md](docs/diccionario_datos.md) para el detalle de variables
y [docs/datasheet.md](docs/datasheet.md) para la ficha completa del dataset.

Descargar `cs-training.csv` desde Kaggle y colocarlo en `datos/raw/`. No se versiona
en Git (ver `.gitignore`); si el equipo necesita compartirlo, usar DVC o Git LFS.

## Estructura del repositorio

```
datos/
  raw/          datos originales, sin modificar
  processed/    datos limpios/transformados, listos para modelar
  external/     datos auxiliares de otras fuentes (si aplica)
notebooks/
  P1_eda_estadistica.ipynb
  P2_descriptivo.ipynb
  P3_predictivo.ipynb
  P4_prescriptivo.ipynb
  src/          código reutilizable (carga de datos, features, utilidades)
  models/       modelo entrenado y serializado
  figures/      figuras generadas por los notebooks (P2, P3, P4)
powerbi/        tablero HTML (dashboard.html + dashboard_data.json) y los
                datasets CSV para Power BI Service (ver docs/guia_powerbi.md)
docs/           diccionario de datos, datasheet, model card, guía del tablero,
                guía de Power BI, resumen ejecutivo
presentacion/   diapositivas de la exposición (presentacion.html) + guion
exposición/     video grupal (o enlace) y orden de participación
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
| P5 — Tablero | HTML autocontenido (`powerbi/dashboard.html`) + datasets CSV para Power BI Service (`powerbi/*.csv`) | [docs/guia_tablero.md](docs/guia_tablero.md) · [docs/guia_powerbi.md](docs/guia_powerbi.md) | [presentacion/presentacion.html](presentacion/presentacion.html) + [guion](presentacion/guion_presentacion.md) (13 diapositivas, ~10 min) |

## Exposición

Ver [exposición/orden_participacion.txt](exposición/orden_participacion.txt)
para el orden y tiempos de participación del equipo, y
[exposición/enlace_video.txt](exposición/enlace_video.txt) (o el archivo
`.mp4` en esa misma carpeta) para el video grabado de la sustentación grupal.

## Estado del proyecto

- [x] P1 — EDA y estadística
- [x] P2 — Modelo descriptivo
- [x] P3 — Modelo predictivo
- [x] P4 — Modelo prescriptivo
- [x] P5 — Tablero HTML
- [x] Datasets CSV para Power BI Service listos en `powerbi/` (ver `docs/guia_powerbi.md`)
- [ ] Reporte de Power BI construido y publicado en Power BI Service
- [x] Resumen ejecutivo y checklist de DoD (ver `docs/resumen_ejecutivo.md`)
- [x] Presentación final (`presentacion/presentacion.html`)
- [ ] Video de exposición grupal y orden de participación (`exposición/`)
