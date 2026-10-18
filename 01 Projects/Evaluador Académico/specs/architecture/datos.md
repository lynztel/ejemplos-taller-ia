---
categoria: architecture
tipo: recurso
estado: en-progreso
proyecto: Evaluador Académico
resumen: "Modelo de datos propuesto"
utilidad: "Especificar y verificar el desarrollo de esta aplicación."
contexto: "Handoff v1.0 y planeación integral."
tags: [proyecto/evaluador-academico, desarrollo/sdd]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# Modelo de datos propuesto

No hay tablas implementadas todavía.

| Entidad | Relación e integridad |
|---|---|
| Grupo, Alumno, Membresía | Alumno pertenece a grupo mediante membresía; histórico por definir |
| Actividad | Contexto de grupo y versión de rúbrica |
| ConjuntoEntrega | batch_id, actividad/grupo, nombre visible y clave de subcarpeta estable; agrupa tareas individuales |
| Entrega | Alumno + actividad + conjunto; estados académico y de revisión; política de reentregas pendiente |
| Archivo | Entrega, ID estable, ruta actual controlada y etapa, hash, tamaño, versión y fecha; ruta cambia al mover |
| RúbricaVersión y Criterio | Criterios, modo, máximos y regla de agregación conservados por versión |
| Ejecución | run_id único, entrega, archivo/hash, rúbrica, versión, productor y fecha |
| ResultadoCriterio | Ejecución + criterio únicos; estado, sugerencia nullable y observaciones |
| Evidencia | Resultado, archivo/versión, página/anclaje o limitación explícita |
| Anotación | Entrega, archivo/versión, autor, criterio opcional, comentario, anclaje y fechas |
| Revisión | Puntuaciones docentes y retroalimentación en borrador o confirmadas |
| CalificaciónFinal | Revisión confirmada, total calculado, autor y fecha; conservar revisiones |
| EventoHistorial | Entidad, acción, autor, fecha y cambios pertinentes |
| RegistroPreevaluación | Archivo JSON obligatorio, versión, run_id idempotente, hash de contenido, estado de importación y error |
| OperaciónMovimiento | Archivo, conjunto, origen, destino, estado, hash, intentos, error y fechas; sirve para reconciliar DB y disco |

## Reglas
Claves foráneas activadas por conexión. Rango de puntuaciones según rúbrica. Confirmación, historial y estado atómicos. Informes desde persistencia. Cambiar rúbrica no recalcula silenciosamente historia.

Hash propuesto SHA-256 sobre bytes originales. Duplicado de contenido y reentrega académica no son equivalentes. No fijar unicidad alumno/actividad sin decidir reentregas.

PDF sustituido produce nueva versión; anotaciones antiguas mantienen referencia y se señalan como pendientes de revisión, sin reasignación de coordenadas automática. Propuesta de anclaje: página 1-based y rectángulos normalizados respecto a página sin rotación; guardar versión y transformación de vista, validar zoom/rotación antes de adoptar contrato definitivo. Texto seleccionado es apoyo, no identidad del documento.

## Etapas y subcarpetas
```text
data/
  Tareas no procesadas/<conjunto>/
  Tareas en proceso/<conjunto>/
  Tareas evaluadas/<conjunto>/
```
Los nombres de las tres etapas reflejan lo definido por el usuario; se propone data/ como contenedor. La clave de conjunto evita colisiones y no depende solo del nombre visible. Un archivo mantiene ID, contenido y vínculos a notas al cambiar de ruta. Cada tarea del conjunto avanza individualmente. SQLite en database/evaluador.sqlite; JSON en storage/resultados-json/pendientes/ y aceptados en storage/resultados-json/importados/; rechazados en storage/cuarentena/. Los cambios de ubicación son realizados por el importador y no sustituyen su registro de estado en DB. Anotaciones e histórico persisten en DB aunque el archivo ya esté evaluado.

## Acumulados por curso y período

Añadir Curso y Período como entidades/ámbitos de consulta propuestos; Grupo y Actividad deben vincularse inequívocamente al curso y al período correspondiente. Modelar regla de calificación versionada (puntos/ponderación, escalas, redondeo y tratamiento de faltantes), sin inventar porcentajes. No contabilizar varias ejecuciones de una misma tarea como varias actividades. El acumulado se deriva de revisiones finales vigentes, con trazabilidad a actividad, alumno y regla. No almacenarlo como valor independiente sin estrategia de actualización. [Vistas y reglas](../product/vistas-calificaciones.md).
