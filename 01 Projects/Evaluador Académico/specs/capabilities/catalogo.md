---
tipo: "recurso"
estado: "en-progreso"
categoria: "capabilities"
proyecto: "Evaluador Académico"
resumen: "Catálogo de capacidades"
utilidad: "Organizar, especificar y verificar el desarrollo de la aplicación."
contexto: "Especificaciones vigentes y organización documental basada en fuentes técnicas primarias."
tags: ["proyecto/evaluador-academico", "desarrollo/sdd"]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# Catálogo de capacidades

Capacidades requeridas del producto, no funciones ya implementadas. Las features concretan entregas y el [registro de requisitos](../product/requisitos.md) conserva RF/CA. El [flujo transversal](flujo-evaluacion.md) coordina el recorrido completo.

| CAP | Capacidad | Requisitos principales | Feature |
|---|---|---|---|
| CAP-001 | Organizar conjuntos, alumnos, documentos y versiones | RF-002/003/004/013 | [FEAT-001](../features/001-recepcion-conjuntos/spec.md) |
| CAP-002 | Preevaluar con agente externo autorizado y rúbricas | RF-014/015; AG-001 a AG-010 | [FEAT-002](../features/002-preevaluacion-externa/spec.md) |
| CAP-003 | Integrar resultados JSON validados sin fricción docente | RF-005/006/012 | [FEAT-003](../features/003-importacion-json/spec.md) |
| CAP-004 | Revisar archivos, anotar y confirmar notas con cierre físico | RF-001/007/008/009/016/017 | [FEAT-004](../features/004-revision-docente/spec.md) |
| CAP-005 | Consultar histórico e indicadores | RF-010/017 | [FEAT-005](../features/005-historico/spec.md) |
| CAP-006 | Recuperar el trabajo y conservar integridad | RF-011/012; RNF-001/003/005 | [FEAT-006](../features/006-recuperacion/spec.md) |

El [SDD del agente](agente-preevaluador.md) detalla CAP-002 con comportamiento, diseño objetivo y secuencia EAG; sus secciones técnicas mantienen su estado propuesto. No confundirlo con el agente de desarrollo ni con una integración de API de modelos.

## Vistas docentes ampliadas

CAP-004 incorpora matriz alumno/criterio y visor flotante con notas (RF-019/020/021/022). CAP-005 incorpora acumulados por curso/período (RF-018). [Detalle funcional](../product/vistas-calificaciones.md).
