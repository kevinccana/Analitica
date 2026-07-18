# Guía de uso — Power BI (Service / nube)

Todos los datasets que necesita Power BI están en `powerbi/`, en formato CSV
(sin Excel, sin Power Query, listos para importar tal cual). Se generan
automáticamente al ejecutar los notebooks P2, P3 y P4 — no hace falta
tocarlos a mano.

## Archivos disponibles

| Archivo | Filas | Contenido | Generado en |
|---|---|---|---|
| `segmentos.csv` | 4 | Perfil agregado de cada segmento de riesgo (P2) | P2 |
| `modelo_roc.csv` | ~4,800 | Curva ROC completa de ambos modelos (fpr/tpr) | P3 |
| `modelo_metricas.csv` | 2 | AUC y KS de cada modelo | P3 |
| `modelo_edad.csv` | 4 | Desempeño del modelo por tramo de edad | P3 |
| `matriz_confusion.csv` | 4 | Matriz de confusión en formato largo | P3 |
| `clientes_test_scored.csv` | 22,500 | Un cliente por fila: variables, segmento, PD estimada, aprobado/rechazado | P4 |
| `politica_curva.csv` | ~44 | Utilidad y riesgo por umbral de aprobación | P4 |
| `politica_sensibilidad.csv` | 4 | Escenarios de sensibilidad (tasa/LGD) | P4 |
| `kpis.csv` | 1 | Indicadores de una sola cifra, para tarjetas | P4 |

`dashboard.html` y `dashboard_data.json` (de P5) son para el tablero HTML —
no son necesarios para Power BI, se dejan aparte.

## Cómo construirlo en Power BI Service (sin Desktop)

No necesitas Power BI Desktop ni abrir ningún puerto: todo se hace subiendo
archivos y armando el reporte en el navegador.

1. Entra a [app.powerbi.com](https://app.powerbi.com) con tu cuenta.
2. Ve a un workspace (o "My workspace") → **New** → **Upload a file** → sube
   cada CSV de `powerbi/` (uno por uno; cada uno se convierte en un dataset).
   - Si el workspace lo permite, puedes subirlos también a una carpeta de
     OneDrive/SharePoint conectada y Power BI los detecta automáticamente.
3. Sobre cualquiera de esos datasets: **Create report** → se abre el editor
   de reportes en el navegador (igual que en Desktop: arrastras visuales,
   eliges campos).
4. Para cruzar varias tablas en un mismo reporte (ej. `clientes_test_scored`
   con `segmentos`), añade las demás como fuentes de datos del mismo reporte
   (**Get data** dentro del editor) y crea la relación por la columna común
   (`segmento`).

## Sugerencia de visuales por archivo

- **`kpis.csv`** → tarjetas (Card): total de clientes, tasa de impago global,
  umbral de aprobación, utilidad esperada.
- **`segmentos.csv`** → gráfico de barras: `nombre` vs. `tasa_impago`; y
  `nombre` vs. `pct_total`.
- **`modelo_roc.csv`** → gráfico de líneas: `fpr` (eje X) vs. `tpr` (eje Y),
  con `modelo` como leyenda/serie.
- **`modelo_edad.csv`** → barras: `grupo` vs. `tasa_impago`, con `auc` como
  etiqueta o tooltip.
- **`clientes_test_scored.csv`** → tabla/matriz con segmentadores
  (slicers) por `segmento`, `tramo_edad` y `aprobado`, más un histograma de
  `pd_estimada`.
- **`politica_curva.csv`** → línea: `umbral_pd` vs. `utilidad_total`, y otra
  visual `umbral_pd` vs. `tasa_impago_aprobados`.
- **`politica_sensibilidad.csv`** → tabla o barras agrupadas por `escenario`.

## Actualizar el reporte tras reentrenar

Como los CSV no se conectan en vivo a los notebooks, cualquier cambio
requiere: 1) volver a ejecutar P2→P3→P4 ("Restart & Run All") para
regenerar los CSV en `powerbi/`, y 2) en Power BI Service, usar
**"Refresh now"** sobre cada dataset después de volver a subir el archivo
actualizado (o reemplazarlo si el dataset quedó vinculado a un archivo de
OneDrive).
