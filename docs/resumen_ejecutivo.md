# Resumen ejecutivo — Riesgo Crediticio

> Principio de la pirámide (Minto): conclusión y recomendación primero, luego
> los argumentos, y al final el detalle metodológico. Máximo 1-2 páginas.

## ¿Qué encontramos?

1. Solo el 6.7% de los solicitantes históricos incurre en impago severo — la
   cartera está fuertemente desbalanceada hacia buenos pagadores.
2. Existe un segmento claramente identificable de alto riesgo (~5% de los
   clientes, 45% de tasa de impago): son más jóvenes, usan casi todo su
   cupo de crédito disponible y ya tienen atrasos activos.
3. El ingreso reportado y el patrimonio (líneas de crédito, propiedades) **no**
   son los mejores predictores de riesgo — el comportamiento de pago reciente
   (atrasos, utilización de crédito) discrimina mucho mejor.
4. Un modelo de scoring (LightGBM) distingue correctamente entre buenos y
   malos pagadores en 87 de cada 100 comparaciones posibles (AUC = 0.869),
   con desempeño consistente entre tramos de edad.

## ¿Qué significa para el negocio?

- El riesgo de la cartera no se puede gestionar con reglas simples de ingreso
  o patrimonio: se necesita un modelo de comportamiento (scoring) para
  separar bien el 5% de clientes de alto riesgo del resto.
- El modelo predictivo es suficientemente bueno (AUC 0.869) para sustentar
  una política de aprobación automatizada, con una mejora solo marginal
  frente a un modelo lineal simple más interpretable (regresión logística,
  AUC 0.862) — una alternativa a considerar si la explicabilidad regulatoria
  pesa más que 0.7 puntos de AUC.
- Bajo supuestos razonables de tasa de interés (18%) y pérdida en caso de
  impago (60% del monto), la rentabilidad esperada de la cartera se maximiza
  aprobando a quienes el modelo estima con menos de 23% de probabilidad de
  impago — sin necesidad de imponer un límite de riesgo adicional, porque el
  óptimo económico ya deja la cartera aprobada con ~1% de impago real, muy
  por debajo de cualquier límite de riesgo razonable (5%).

## ¿Qué se recomienda hacer?

**Aprobar solicitudes con probabilidad de impago estimada menor a 23%**
(~54% de los solicitantes evaluados). Bajo los supuestos declarados en P4
(tasa 18%, LGD 60%, monto uniforme US$ 10,000), esta política genera una
utilidad esperada de ~US$ 511 por solicitante evaluado (~US$ 11.5M sobre los
22,500 casos de prueba) con una tasa de impago dentro de la cartera aprobada
de ~1%. La tasa de interés ofrecida es la palanca de negocio más potente: 
subirla a 24% casi duplica la utilidad esperada porque permite aprobar más
cartera manteniendo rentabilidad. La limitación más relevante a resolver
antes de producción es que el monto de crédito se asumió uniforme — en la
práctica debería variar según capacidad de pago del cliente.

## Checklist de Definition of Done (DoD)

| Criterio | Verificación | Estado |
|---|---|---|
| Reproducible | Cada notebook corre de principio a fin ("Restart & Run All") sin errores | [x] |
| Versionado | Código, datos (referencia/hash) y modelo versionados y etiquetados | [x] |
| Documentado | README, diccionario de datos, Model Card y Datasheet completos | [x] |
| Validado | Métricas reportadas sobre conjunto de prueba; supuestos de P4 explícitos | [x] |
| Ético y conforme | Revisión de sesgos (ver Model Card), privacidad y trazabilidad | [x] |
| Comunicado | Este resumen ejecutivo y el tablero HTML listos para la audiencia | [x] |

## Audiencias y formato de entrega

| Audiencia | Qué le interesa | Formato |
|---|---|---|
| Directiva / docente evaluador | Decisión, impacto, riesgo | Este resumen + tablero HTML (`powerbi/dashboard.html`) + presentación (`presentacion/presentacion.html`) |
| Equipo técnico | Reproducibilidad y rigor | Notebooks P1-P4 + Model Card |
