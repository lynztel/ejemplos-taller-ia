---
tipo: "recurso"
estado: "en-progreso"
categoria: "decision"
proyecto: "Evaluador Académico"
resumen: "ADR-002 — Persistencia local"
utilidad: "Organizar, especificar y verificar el desarrollo de la aplicación."
contexto: "Especificaciones vigentes y organización documental basada en fuentes técnicas primarias."
tags: ["proyecto/evaluador-academico", "desarrollo/sdd"]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# ADR-002 — Persistencia local

## Estado
Propuesta.

## Contexto
Metadatos estructurados y documentos requieren conservación e histórico.

## Decisión o propuesta
SQLite y archivos separados, como candidato del handoff; driver y migraciones pendientes.

## Consecuencias y comprobación
Coordinar backup de DB/archivos; validar transacciones, unicidad e integridad.

## Procedencia
Extraída y desarrollada del [registro histórico](registro.md). No inventa fecha de aprobación ni implementación; conserva estado ya documentado. [Especificación afectada](../architecture/datos.md). Nuevas decisiones que la sustituyan deben enlazar este registro, no borrar antecedentes.
