---
tipo: "recurso"
estado: "en-progreso"
categoria: "decision"
proyecto: "Evaluador Académico"
resumen: "ADR-005 — Rutas variables e identidad estable"
utilidad: "Organizar, especificar y verificar el desarrollo de la aplicación."
contexto: "Especificaciones vigentes y organización documental basada en fuentes técnicas primarias."
tags: ["proyecto/evaluador-academico", "desarrollo/sdd"]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# ADR-005 — Rutas variables e identidad estable

## Estado
Flujo confirmado; mecanismo técnico propuesto.

## Contexto
Usuario requiere tres carpetas por etapa y subcarpetas por conjunto.

## Decisión o propuesta
Mantener ID/hash y cambiar ruta mediante operaciones controladas reconciliables. Sustituye propuesta previa de rutas fijas.

## Consecuencias y comprobación
Filesystem y DB no comparten transacción: registrar/reconciliar sin pérdida ni sobrescritura.

## Procedencia
Extraída y desarrollada del [registro histórico](registro.md). No inventa fecha de aprobación ni implementación; conserva estado ya documentado. [Especificación afectada](../capabilities/flujo-evaluacion.md). Nuevas decisiones que la sustituyan deben enlazar este registro, no borrar antecedentes.
