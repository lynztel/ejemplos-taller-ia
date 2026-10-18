---
categoria: capabilities
tipo: recurso
estado: en-progreso
proyecto: Evaluador Académico
resumen: "Flujos y estados"
utilidad: "Especificar y verificar el desarrollo de esta aplicación."
contexto: "Handoff v1.0 corregido por aclaración funcional directa del usuario."
tags: [proyecto/evaluador-academico, desarrollo/sdd]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# Flujo operativo y estados

## 1. Recepción del conjunto
El docente define un conjunto (ejemplo: Primera tarea del parcial), descarga los archivos de su plataforma y los deposita en `data/Tareas no procesadas/<conjunto>/`. La descarga por conector de un agente es alternativa opcional hacia la misma entrada. Registrar conjunto, actividad/grupo, archivos y asociación al alumno; la identificación dudosa se informa sin inventarla.

## 2. Sesión de agente externo
Docente abre el repositorio y solicita preevaluar el conjunto. Agente lee AGENTS.md, reglas académicas, rúbrica vigente y skills aplicables. Reclama cada tarea para evitar doble procesamiento, la mueve a `data/Tareas en proceso/<conjunto>/`, la analiza y escribe un archivo JSON completo con hallazgos, criterios, evidencias y sugerencias en storage/resultados-json/pendientes/. No accede a DB. La aplicación detecta el archivo terminado, valida esquema y referencias y lo importa transaccionalmente. Reporta completas, incompletas y fallidas; el docente no importa desde la UI por tarea.

## 3. Revisión continua
La aplicación muestra las tareas del conjunto y abre la seleccionada en su visor. El docente recorre anterior/siguiente manteniendo filtros, compara evidencia, añade notas, ajusta puntuaciones y guarda borradores. Consulta histórico por tarea y global. Una preevaluación incompleta se señala y puede completarse mediante revisión docente conforme a rúbrica.

## 4. Finalización y traslado
El docente confirma nota y marca evaluada/calificada. Se persisten nota final, autor, fecha e historial y se programa el traslado a `data/Tareas evaluadas/<conjunto>/`. Un servicio/script local lo ejecuta automáticamente. El agente también puede invocar el cierre autorizado si se elige esa variante, pero no decide qué tarea está evaluada ni su nota. Traslado pendiente/fallido no revoca una calificación ya confirmada.

## Estados académicos propuestos
| Origen | Acción | Destino | Condición |
|---|---|---|---|
| SIN_PROCESAR | Agente inicia por operación controlada | EN_PROCESO | Conjunto/archivo identificados y traslado a proceso completado |
| EN_PROCESO | Aplicación importa automáticamente el JSON del agente | PREEVALUADA | Esquema y referencias válidos, transacción confirmada y completitud visible |
| PREEVALUADA | Docente inicia revisión | EN_REVISION_DOCENTE | Archivo disponible para visor o error legible |
| EN_REVISION_DOCENTE | Docente confirma nota | EVALUADA | Rangos y requisitos docentes satisfechos |

«Evaluada»/«calificada» representan el mismo cierre académico; se propone EVALUADA como valor técnico y no dos pasos distintos. Los nombres técnicos y reapertura aún se diseñan; no preservar por obligación la cadena antigua CALIFICADA → PROCESADA.

## Estado de movimiento independiente
PENDIENTE → EN_CURSO → COMPLETADO; fallo → ERROR_REINTENTABLE. Guardar origen, destino, archivo, conjunto, hash, intentos y causa. Reintento con destino ya existente e igual archivo/hash completa sin duplicar; colisión de otro archivo no sobrescribe ni elimina. Origen ausente y destino ausente produce incidencia visible. Un traslado fallido no desaparece de bandeja ni duplica nota/preevaluación. DB conserva identidad; ruta solo indica localización.

## Subcarpetas por conjunto
La misma clave de conjunto se mantiene en las tres etapas; el nombre visible puede ser descriptivo, pero identidad interna debe ser estable y evitar colisiones entre cursos/grupos. Cada tarea individual avanza de forma independiente. Al finalizar la revisión parcial pueden coexistir archivos del mismo conjunto en proceso y evaluados.
