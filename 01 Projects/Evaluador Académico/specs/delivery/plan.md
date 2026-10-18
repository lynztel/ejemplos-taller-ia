---
categoria: delivery
tipo: recurso
estado: en-progreso
proyecto: Evaluador Académico
resumen: "Plan por incrementos"
utilidad: "Guiar el desarrollo y la verificación de esta aplicación."
contexto: "Handoff v1.0 y planeación integral."
tags: [proyecto/evaluador-academico, desarrollo/sdd]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# Plan por incrementos

| INC | Fase handoff | Tareas y entregables | Dependencias | Cierre |
|---|---|---|---|---|
| INC-000 | 0–1 | Aclaración funcional incorporada; rúbrica, identidad, formatos y esquema JSON | Respuestas de producto | Acuerdos y bloqueos registrados |
| INC-001 | 2 | Experimentos técnicos, scaffold, dependencias, migración inicial e instrucciones reales | Stack y distribución elegidos | Servidor local, DB temporal y pruebas técnicas |
| INC-002 | 3 | Conjuntos, grupos/alumnos/actividad, rúbricas, recepción por carpetas, hashes, versiones y motor de movimientos | Identificación, formatos | CA-002/003/004/013 |
| INC-003 | 4 | Entorno académico, skills por rúbrica, inicio por agente, JSON obligatorio, detección/importación automática, validación y transacciones | INC-002, rúbrica y contrato | CA-005/006/012/014/015 |
| INC-004 | 5 | Bandeja por conjunto, visor integrado, anterior/siguiente, criterios y evidencia | INC-003 | CA-007/017 (navegación) |
| INC-005 | 6 | Anotaciones, puntuaciones, confirmación, historial y traslado automático a evaluadas | INC-004 y prueba de anclajes | CA-001/008/009/016 |
| INC-006 | 7 | Histórico individual/global filtrable, indicadores y consultas | Notas finales, métricas definidas | CA-010/017 (histórico) |
| INC-007 | 8 | Recuperación, errores, usabilidad y guía docente | Política de respaldo | CA-011 y controles de seguridad |

Estado: INC-000 en progreso; demás pendientes. Seguridad y trazabilidad son transversales desde infraestructura, no se aplazan al último incremento.

## Ficha al iniciar cada incremento
ID, objetivo, RF/RNF, decisiones necesarias, entradas/salidas, CA Dado/Cuando/Entonces, errores/recuperación, diseño, tareas/dependencias, PR, evidencia, pendientes y estado. Guardar en specs/features/<feature-id>/plan.md y tasks.md cuando se inicie, sin generar fichas vacías.

## Entorno del agente académico

Aplicar [SDD del agente preevaluador](../capabilities/agente-preevaluador.md), etapas EAG-01 a EAG-06 y criterios AG/CAG. INC-001 prueba aislamiento y proceso local; INC-002 añade manifiesto e inicio controlado; INC-003 construye instrucciones/skills y publicación/importación JSON. INC-004/005 completan verificación en visor y cierre. Este trabajo configura un agente externo; no construye un runtime de IA propio.

## Próximo trabajo
Objetivo y recorrido ya definidos por el docente. Concretar formatos del visor, rúbrica, identidad de conjunto/alumno y reentregas; definir esquema JSON, detección automática y permisos que impidan al agente académico acceso directo a DB. Probar movimientos recuperables y navegación integrada además del stack. Los conectores son opcionales: descarga manual y cierre automático no dependen de ellos. No crear ahora scripts operativos ni mover entregas reales al corregir especificaciones.

## Ampliación de interfaz global

INC-002 define relaciones Curso/Período y configuración de cálculo. INC-004 incorpora matriz alumno × criterio y visor flotante (RF-019/020/022); INC-005 asegura anotaciones y guardado continuo (RF-021); INC-006 añade acumulados por curso/período (RF-018). Vincular PR-022 a PR-026 a los planes de FEAT-004/005. La regla de agregación debe resolverse antes de implementar cálculo definitivo.
