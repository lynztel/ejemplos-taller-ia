---
tipo: "recurso"
estado: "en-progreso"
categoria: "decision"
proyecto: "Evaluador Académico"
resumen: "ADR-004 — JSON obligatorio e importación automática"
utilidad: "Organizar, especificar y verificar el desarrollo de la aplicación."
contexto: "Especificaciones vigentes y organización documental basada en fuentes técnicas primarias."
tags: ["proyecto/evaluador-academico", "desarrollo/sdd"]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# ADR-004 — JSON obligatorio e importación automática

## Estado
Aceptada por el usuario; implementación pendiente.

## Contexto
Agente externo debe producir resultados sin acceso directo a DB ni importación manual docente por tarea.

## Decisión o propuesta
JSON obligatorio → validación/importador automático → DB. JSON opcional de revisión 0.2 queda superado por ratificación del usuario en 0.3.

## Consecuencias y comprobación
Requiere esquema, idempotencia, detección recuperable y permisos efectivos; JSON solo no aísla DB. Dialecto/detección siguen propuestos.

## Procedencia
Extraída y desarrollada del [registro histórico](registro.md). No inventa fecha de aprobación ni implementación; conserva estado ya documentado. [Especificación afectada](../contracts/preevaluacion-json.md). Nuevas decisiones que la sustituyan deben enlazar este registro, no borrar antecedentes.
