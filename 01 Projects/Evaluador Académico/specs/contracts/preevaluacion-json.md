---
categoria: contracts
tipo: recurso
estado: en-progreso
proyecto: Evaluador Académico
resumen: "JSON obligatorio e importación automática — revisión 0.3"
utilidad: "Especificar y verificar el desarrollo de esta aplicación."
contexto: "Handoff v1.0 corregido por aclaración funcional directa del usuario."
tags: [proyecto/evaluador-academico, desarrollo/sdd]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# Contrato JSON e importación automática

Decisión confirmada por el usuario: agente externo → archivo JSON obligatorio → validación/importación automática por aplicación → SQLite. El agente académico no accede directamente a DB. El docente no exporta/importa manualmente cada resultado. El esquema detallado es propuesta pendiente de rúbrica e identificación, no una implementación disponible.

## Publicación y detección
Propuesta: agente escribe en storage/resultados-json/pendientes/ un archivo temporal y solo al terminar lo renombra a .json dentro del mismo directorio. El importador ignora temporales; un JSON malformado nunca se trata como resultado válido. No procesar un archivo mientras cambia: trabajar sobre una copia estable y verificar identidad/hash antes de aceptar. El mecanismo de detección (watcher o sondeo) se elige en infraestructura.

La aplicación explora pendientes al arrancar y mientras está activa. Si el agente produce resultados con la aplicación cerrada, se importan al siguiente inicio. No exige al docente importación manual por tarea; los errores sí aparecen para corrección. Ante dos detectores simultáneos, reclamar trabajos e impedir duplicados mediante unicidad de run_id en DB.

## Campos propuestos
| Campo | Regla |
|---|---|
| schema_version | Versión soportada del JSON |
| run_id | ID estable para reintentos |
| batch_id, submission_id | Conjunto y tarea existentes |
| file | ID, versión y hash; ruta física variable por etapa |
| rubric | ID y versión asociados a actividad/conjunto |
| processed_at, producer | Fecha con zona y entorno conocido, sin atribución inventada |
| results | criterion_id, status, evidence, observation, suggested_score nullable |
| limitations | Errores y criterios no evaluables |

Estados de criterio propuestos: cumple, parcial, no_cumple y no_evaluable. Puntuar según rúbrica; null no es cero. Evidencia refiere archivo/versión y página o localización soportada. No aceptar campos de nota final ni confirmación docente.

## Validación y persistencia
1. Comprobar archivo completo, tamaño y JSON bien formado; limitar lectura a directorio autorizado.
2. Validar versión y JSON Schema (2020-12 propuesto), campos requeridos y política de campos desconocidos.
3. Verificar conjunto, entrega, archivo/hash, rúbrica y criterios; rechazar repetidos, rangos incorrectos y puntuaciones de criterios exclusivamente docentes.
4. Registrar ejecución, resultados y transición académica en una transacción. Ausencias/no evaluables generan completitud y revisión requerida, no ceros implícitos.
5. Registrar hash y procedencia del JSON. Mismo run_id y mismo contenido aceptado devuelve éxito previo sin duplicar; distinto contenido con mismo ID genera conflicto.
6. Tras commit, archivar JSON en storage/resultados-json/importados/. Si ese traslado falla, conservar estado importado y reintentar archivo sin duplicar DB.

JSON inválido → storage/cuarentena/ con motivo y sin resultados parciales. Falla DB → rollback, resultado pendiente/reintentable. Archivo ya movido a Tareas en proceso conserva localización; no fingir transacción entre DB y disco. Caída tras commit y antes de archivar se resuelve por idempotencia.

## Frontera de seguridad
Solo el importador conecta a DB para preevaluaciones. JSON se trata como datos no confiables; nunca ejecutar instrucciones, SQL, rutas o URLs de su contenido. Separar permisos reales del proceso académico y del proceso de aplicación; una instrucción AGENTS.md o formato JSON no bloquea por sí solo acceso a archivos de DB. Verificar ese control en infraestructura.

Estado: contrato documental. Watcher, importador, esquema ejecutable y permisos todavía no implementados. Los movimientos de tareas por conjunto y cierre automático del docente siguen definidos en specs/capabilities/flujo-evaluacion.md.
