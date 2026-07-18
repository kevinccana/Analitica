# Guía de uso del tablero

Tablero: [`powerbi/dashboard.html`](../powerbi/dashboard.html).

## Cómo abrirlo

Es un archivo HTML autocontenido: no requiere Power BI, servidor ni conexión a
internet. Basta con abrirlo con doble clic o arrastrarlo a cualquier
navegador moderno (Chrome, Edge, Firefox). Todos los datos y el código de los
gráficos están embebidos en el propio archivo.

## Cómo interactuar

- **Pasar el cursor** sobre una barra o sobre una línea muestra el valor
  exacto en un tooltip (en las líneas, un hairline vertical marca el punto
  más cercano al cursor y el tooltip lista el valor de todas las series a la
  vez).
- **"Ver tabla"** (debajo de cada gráfico) despliega los datos completos en
  una tabla — útil para citar cifras exactas sin depender de leer el gráfico.
- **Botón "Modo oscuro/claro"** (esquina superior derecha) alterna el tema
  visual; también respeta el tema del sistema operativo por defecto.

## Qué significa cada sección

| Sección | Contenido | Notebook fuente |
|---|---|---|
| KPIs superiores | Resumen ejecutivo de una línea: tamaño de cartera, tasa de impago global, desempeño del modelo y resultado de la política de aprobación | P1, P3, P4 |
| 1. Segmentación de riesgo | Los 4 segmentos de clientes hallados por clustering (K-Means) y su tasa de impago / participación en la cartera | P2 |
| 2. Desempeño del modelo predictivo | Curva ROC comparando el baseline (regresión logística) contra el modelo final (LightGBM), matriz de confusión al umbral óptimo, y desempeño desagregado por tramo de edad | P3 |
| 3. Política de aprobación | Utilidad esperada y riesgo de la cartera aprobada en función del umbral de PD, la recomendación de decisión, y el análisis de sensibilidad a la tasa de interés y la LGD | P4 |

## Cómo regenerar el tablero con datos nuevos

El tablero lee un dataset embebido (`powerbi/dashboard_data.json`, generado a
partir de los notebooks P1–P4) que se inyecta directamente en el HTML — no
hace `fetch` en tiempo de ejecución. Para actualizarlo tras reentrenar el
modelo o cambiar los supuestos de P4:

1. Volver a ejecutar los notebooks P1–P4 ("Restart & Run All").
2. Regenerar `powerbi/dashboard_data.json` con las cifras actualizadas
   (mismo procedimiento usado para construir el tablero: cargar el modelo y
   los parámetros de limpieza serializados en `notebooks/models/`, recalcular
   segmentos, métricas y la curva de política, y volcarlos a JSON).
3. Reemplazar el bloque `const DATA = {...};` dentro de
   `powerbi/dashboard.html` con el nuevo JSON.

## Limitaciones

- Es una fotografía de un momento dado (no se conecta a una base de datos
  en vivo). Para monitoreo continuo de deriva de datos/modelo, ver la
  sección de monitoreo en `docs/model_card.md`.
- Los datos de segmentación (P2) usan el dataset completo (150,000 clientes);
  los de desempeño del modelo y política (P3/P4) usan solo el conjunto de
  prueba (22,500 clientes) — evitar comparar tasas entre secciones sin tener
  esto en cuenta.
