---
tipo: "recurso"
estado: "en-progreso"
categoria: "decision"
proyecto: "Evaluador Académico"
resumen: "ADR-006 — Traslado automático al confirmar"
utilidad: "Organizar, especificar y verificar el desarrollo de la aplicación."
contexto: "Especificaciones vigentes y organización documental basada en fuentes técnicas primarias."
tags: ["proyecto/evaluador-academico", "desarrollo/sdd"]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# ADR-006 — Traslado automático al confirmar

## Estado
Opción preferente autorizada; implementación pendiente.

## Contexto
Docente confirma evaluación; el traslado no necesita IA.

## Decisión o propuesta
Script/servicio local programa traslado a evaluadas tras confirmación docente.

## Consecuencias y comprobación
Separar estado académico y físico; un fallo de traslado no revoca nota.

## Procedencia
Extraída y desarrollada del [registro histórico](registro.md). No inventa fecha de aprobación ni implementación; conserva estado ya documentado. [Especificación afectada](../capabilities/flujo-evaluacion.md). Nuevas decisiones que la sustituyan deben enlazar este registro, no borrar antecedentes.
