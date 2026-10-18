---
tipo: "recurso"
categoria: "product"
estado: "en-progreso"
proyecto: "Evaluador Académico"
resumen: "Vistas globales, matriz de evaluación y visor flotante"
utilidad: "Especificar la consulta de calificaciones y la revisión docente integrada."
contexto: "Propuesta funcional y visual directa del docente en esta conversación."
tags: ["proyecto/evaluador-academico", "producto/interfaz"]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# Vistas globales, matriz de evaluación y visor flotante

## Origen y estado

El docente propone tres niveles de consulta: calificaciones acumuladas por curso/período, matriz de alumnos/criterios y entrega en ventana flotante con notas. Se incorpora como alcance funcional del producto; distribución exacta, reglas de agregación y decisiones de implementación se detallan aquí como propuestas. No hay interfaz implementada.

## 1. Vista global por curso y período

Seleccionar curso, grupo y período; mostrar una fila por alumno y columnas por actividad/conjunto, nota confirmada, acumulado y progreso de evaluación. Acceder desde una actividad a su matriz sin perder el contexto. Permitir distinguir calificaciones definitivas de tareas todavía pendientes; las sugerencias IA no se suman como notas finales.

Mostrar tanto puntos obtenidos como máximo aplicable cuando se use sistema por puntos. Si el curso usa ponderaciones, mostrar contribución de cada actividad y total según configuración versionada. No sumar directamente notas en escalas distintas ni dar por hecho que un promedio simple es la regla del curso.

Ejemplo sintético para puntos: dos actividades confirmadas 8/10 y 15/20 producen acumulado confirmado 23/30. Si falta otra actividad de máximo 10, mostrar una pendiente y máximo previsto 40, sin presentarla automáticamente como cero ni publicar 23/40 como calificación final del período. La regla de cierre, faltantes, redondeo y ponderación la define el docente antes de implementar el cálculo definitivo. No renormalizar pesos de pendientes silenciosamente.

Una actividad con varias versiones cuenta una sola vez según la revisión final vigente y la política de reentregas; conservar historia sin duplicar aportaciones. Cada total debe poder desglosarse por tareas, regla y versión. Reabrir una evaluación marca su efecto en el acumulado según política explícita, aún por decidir.

## 2. Matriz específica de alumnos y criterios

Dentro de un conjunto/actividad: filas de alumnos y columnas de identidad, estado de entrega, criterios de rúbrica, puntuación sugerida/docente identificable, total, notas e interacción «Ver entrega». Los criterios son dinámicos según versión de rúbrica; mostrar máximo y explicar estados sin puntuación.

Propuesta de presentación: valor docente como principal cuando existe y sugerencia IA como dato secundario visible al inspeccionar celda; no sustituir un valor por otro de forma ambigua. Notas largas se consultan en panel/visor sin inflar toda la fila. Filtros por alumno/estado, búsqueda y ordenación; columna de alumno y encabezados persistentes, desplazamiento horizontal para rúbricas anchas. Números alineados y cero diferenciado de sin evaluar/no entregada.

El botón «Ver entrega» abre el documento correspondiente al alumno/actividad de esa fila. Si hay varios archivos, mostrar selector de archivo con nombre/versión; si no hay entrega, indicar ausencia sin abrir una ventana vacía. Mantener fila, filtros y posición al volver del visor.

## 3. Ventana emergente flotante de revisión

Se interpreta «iframe tipo banner» como una ventana amplia superpuesta dentro de la misma aplicación con contenido documental embebido, sin navegar a otra página. Propuesta inicial: diálogo modal centrado, cabecera compacta y cuerpo en dos paneles; no un banner estrecho que impida leer páginas. Dimensiones adaptables al viewport, ampliar y cerrar. En pantallas pequeñas puede ocupar toda la superficie disponible.

Cabecera: alumno, actividad/conjunto, nombre/versión de archivo, estado, anterior/siguiente y cerrar. Cuerpo: documento con controles del visor y panel de rúbrica, hallazgos/notas del agente y notas/puntuaciones docentes. Las evidencias seleccionadas navegan a su localización cuando el formato lo admite. Paneles con desplazamiento independiente y tamaño útil; proporciones por validar con el docente.

Guardar anotaciones ligadas a archivo/versión y criterio opcional, distinguiendo autor IA/docente. Estado visible de guardado; no perder texto al cerrar o pasar de tarea. Propuesta: autoguardado de borradores con indicador; ante cambios aún no guardados, guardar o pedir decisión antes de descartar, incluido Escape/cambio de tarea. Confirmación final siempre explícita, separada del guardado de notas y del cierre del visor.

## 4. Iframe y visor: criterio técnico

Iframe es un contenedor de integración, no implementa por sí mismo anotaciones ni selección de evidencia. Si se usa iframe, cargar una ruta local controlada del visor y exponer un contrato explícito de selección de archivo/página, eventos y guardado; no depender del visor PDF nativo del navegador para editar anotaciones propias. Si hay mensajería entre frame y aplicación, validar origen, fuente y esquema de mensajes. Ruta por ID, nunca acceso arbitrario a filesystem.

PDF.js sigue candidato para PDF. Puede funcionar en componente integrado o dentro del iframe; elegir tras probar anotaciones, foco, zoom y navegación. Se conserva el requisito de ventana flotante embebida; el detalle de iframe se documenta como preferencia del docente y alternativa técnica por validar, sin decidir a escondidas su sustitución.

## 5. Accesibilidad y estados

Diálogo con nombre accesible, foco al abrir, navegación por teclado dentro de modal y retorno al botón de la fila al cerrar. Escape cierra con la política de cambios no guardados, no descarta sin aviso. Probar teclado también dentro de un posible iframe. Tabla con encabezados/relación fila-columna; no añadir rol grid sin implementar su interacción de teclado.

Estados: cargando, sin alumnos, sin entregas, preevaluación pendiente, JSON rechazado, documento ilegible/formato no compatible, guardando, guardado y fallo de guardado. Carga fallida del archivo no debe impedir consultar criterios y notas ya persistidos.

## 6. Aceptación

RF-018/CA-018: acumulados por curso/período trazables a tareas confirmadas y regla configurada. RF-019/CA-019: matriz alumno × criterio con notas y acción individual. RF-020/CA-020: apertura flotante con documento y ambos tipos de notas; volver conserva tabla. RF-021/CA-021: guardado y navegación sin pérdida. RF-022/CA-022: estilo y accesibilidad según [guía visual](../standards/interfaz-visual.md).

## Pendientes específicos

Ponderaciones frente a puntos por curso, períodos y reentregas, tratamiento de ausencias/cierre y redondeo; tamaño/modalidad del visor y persistencia de distribución; formatos iniciales; autoguardado definitivo; arquitectura iframe/componente. Referencia de implementación: FEAT-004 y FEAT-005; reglas de cálculo no se delegan a IA.

## Distribución detallada de interfaz

Los [wireframes UI-001 a UI-006](interfaz-wireframes.md) especifican estructura compartida, resumen global, matriz y visor flotante basados en mockups concepto 01, con estados y trazabilidad. Son base de implementación; no convierten datos ficticios ni controles ilustrativos en reglas de negocio.
