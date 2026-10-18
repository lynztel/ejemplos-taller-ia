---
tipo: "recurso"
estado: "en-progreso"
categoria: "decision"
proyecto: "Evaluador Académico"
resumen: "ADR-001 — Stack web local"
utilidad: "Organizar, especificar y verificar el desarrollo de la aplicación."
contexto: "Especificaciones vigentes y organización documental basada en fuentes técnicas primarias."
tags: ["proyecto/evaluador-academico", "desarrollo/sdd"]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# ADR-001 — Stack web local

## Estado
Propuesta.

## Contexto
La aplicación necesita visor interactivo y acceso servidor a DB/archivos.

## Decisión o propuesta
Evaluar Astro servidor + Node y React selectivo. Alternativa: UI React y backend local. No hay elección aprobada.

## Consecuencias y comprobación
Probar complejidad del visor, distribución y acceso a disco antes del scaffold.

## Procedencia
Extraída y desarrollada del [registro histórico](registro.md). No inventa fecha de aprobación ni implementación; conserva estado ya documentado. [Especificación afectada](../architecture/tecnologias.md). Nuevas decisiones que la sustituyan deben enlazar este registro, no borrar antecedentes.
