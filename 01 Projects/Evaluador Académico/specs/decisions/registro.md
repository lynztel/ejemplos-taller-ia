---
categoria: decisions
tipo: recurso
estado: en-progreso
proyecto: Evaluador Académico
resumen: "Decisiones y dependencias"
utilidad: "Guiar el desarrollo y la verificación de esta aplicación."
contexto: "Handoff v1.0 y planeación integral."
tags: [proyecto/evaluador-academico, desarrollo/sdd]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# Decisiones y dependencias

## Fuente vigente
Aclaración directa del docente en [Contexto/aclaracion-funcional.md](../../Contexto/aclaracion-funcional.md), posterior al handoff. Registra decisiones funcionales confirmadas; JSON obligatorio e importación automática fueron ratificados después por el usuario; stack y detalles de detección/esquema siguen abiertos.

## Registro de correcciones
- C-01 vigente: solo docente confirma nota final.
- C-02 vigente y ratificada: agente produce archivos JSON obligatorios; la aplicación valida/importa automáticamente; el agente no accede directamente a DB. La revisión 0.2 que hizo JSON opcional fue una interpretación incorrecta del asistente y queda sustituida por esta revisión 0.3.
- C-03 vigente: datos locales autocontenidos, reales fuera de Git.
- C-04 aclarada: conservar bytes originales, identidad e historial; sí se mueve la ubicación física por etapa.
- C-05 vigente: no integrar agente propio vía API de modelos con consumo adicional.
- C-06 confirmada: adquisición manual por conjunto desde cualquier plataforma escolar. Conector/Drive desde sesión externa es alternativa opcional.
- C-07 confirmada: repositorio abierto en sesión externa; reglas y skills académicas basadas en rúbricas guían preevaluación.
- C-08 confirmada: Tareas no procesadas → Tareas en proceso → Tareas evaluadas, con subcarpeta por conjunto.
- C-09 confirmada: visor integrado para reducir apertura archivo por archivo, notas y criterios, histórico individual y global.
- C-10 confirmada: docente marca evaluada/calificada con nota; traslado final puede automatizarlo aplicación/script sin agente.

## Arquitectura propuesta
| ADR | Propuesta | Estado |
|---|---|---|
| ADR-001 | Astro servidor + Node, React selectivo, comparado con UI React/backend local | Pendiente de prueba y selección |
| ADR-002 | SQLite y archivos separados, respaldos coordinados | Candidata del handoff |
| ADR-003 | PDF.js para PDF, otros formatos por definir | Propuesta |
| ADR-004 | JSON obligatorio, esquema versionado y detección/importación automática | Frontera confirmada; dialecto y detección propuestos |
| ADR-005 | IDs/hash estables con rutas variables, movimientos reconciliables | Sustituye propuesta de rutas fijas |
| ADR-006 | Script/servicio automático al confirmar nota, sin sesión IA activa | Opción preferente dentro del comportamiento autorizado |

## Decisiones abiertas
D-01 formatos iniciales del visor; D-02 autenticación/autoría y distribución para uso personal; D-03 rúbricas, modos y versiones; D-04 entorno externo y permisos concretos (no necesita agente único obligatorio); D-05 identificación, claves de conjunto y reentregas; D-06 tipos de anotación/filtros de histórico; D-07 respaldo/retención; D-08 stack, detección automática y aislamiento de permisos del importador; D-09 precisión, agregación y no evaluables.

Ya están definidos agrupación por conjuntos, tres carpetas, visor como parte central y registro de preevaluaciones en DB mediante importación automática de JSON. No volver a pedirlos como si faltara el objetivo. No mantener AgentCMD como requisito: provenía de una duda del handoff y no es dependencia establecida por el usuario.

D-03/05/09 condicionan contrato final; D-01/06 detalle del visor; D-02/08 infraestructura; D-07 restauración. Registrar futuras decisiones con fecha, autor, alternativas, consecuencias y documentos afectados. No descartar este historial de corrección.

## Ratificación posterior del usuario

Se restablece la frontera del handoff: JSON obligatorio, importador de aplicación y ausencia de acceso directo del agente a DB. La automatización elimina el paso manual del docente, no el JSON. Se mantienen conjuntos, tres carpetas, movimientos reconciliables, visor integrado e histórico. No se ha implementado software al corregir estos documentos.

## Incorporación de criterios técnicos al entorno académico

El usuario solicita incluir la evaluación técnica en el SDD del agente: se incorpora [especificación dedicada](../capabilities/agente-preevaluador.md). Manifiesto, perfil de permisos, utilidades de inicio y recibos, detección recuperable y prueba mínima son criterios de construcción/verificación. Proceso local único y detalles de carpetas operativas son propuestas de implementación; su eficacia no se declara probada. Se mantiene JSON obligatorio, importador como escritor DB y cierre final docente.

## ADR individuales

Este registro conserva historia y pendientes. Para contexto, estado y consecuencias de cada decisión consultar:

- [001-stack-local](001-stack-local.md)
- [002-persistencia](002-persistencia.md)
- [003-visor](003-visor.md)
- [004-json-obligatorio](004-json-obligatorio.md)
- [005-movimientos](005-movimientos.md)
- [006-cierre-automatico](006-cierre-automatico.md)

## Propuesta de vistas y estilo del docente

Se incorporan calificaciones globales por curso/período, matriz alumno/criterios y apertura de entrega en ventana flotante embebida con anotaciones. Referencias visuales: Vercel y Cloudflare, estilo minimalista. Ver [vistas](../product/vistas-calificaciones.md) y [guía visual](../standards/interfaz-visual.md). Modal amplio e iframe/componente son diseño técnico pendiente de validación; tampoco se fijan pesos, escalas o tratamiento de faltantes por inferencia.
