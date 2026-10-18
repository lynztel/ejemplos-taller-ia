---
categoria: research
tipo: recurso
estado: en-progreso
proyecto: Evaluador Académico
resumen: "Fuentes y procedencia"
utilidad: "Guiar el desarrollo y la verificación de esta aplicación."
contexto: "Handoff v1.0 y planeación integral."
tags: [proyecto/evaluador-academico, desarrollo/sdd]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# Fuentes y procedencia

- [Aclaración funcional directa del docente](../../Contexto/aclaracion-funcional.md): fuente vigente para agente externo, conjuntos, carpetas, visor y cierre automático, junto con ratificación posterior de JSON obligatorio e importación automática sin acceso directo a DB.
- [Handoff v1.0](../../Contexto/handoff.md), 17 de octubre de 2026: antecedente; se conserva JSON obligatorio y separación agente/DB; la aclaración amplía movimientos y experiencia docente.
- Lienzo Excalidraw del mapa integral: representación histórica de planeación v1.0, todavía no actualizado a esta aclaración.
- AGENTS.md de MiBiblioteca: reglas de lectura y organización.
- [Astro Node](https://docs.astro.build/en/guides/integrations-guide/node/) y [renderizado servidor](https://docs.astro.build/en/guides/on-demand-rendering/): capacidades del servidor, sin confirmar elección del stack.
- [Mozilla PDF.js](https://mozilla.github.io/pdf.js/getting_started/): capas y ejemplos del visor; anclajes propios requieren diseño adicional.
- [SQLite Backup API](https://sqlite.org/backup.html): snapshot consistente; documentos se coordinan aparte.
- [JSON Schema 2020-12](https://json-schema.org/draft/2020-12/): dialecto propuesto.

Fuentes oficiales consultadas al preparar esta documentación; no hay integración instalada o probada. Codex consolidó contexto, reglas y especificaciones. Skill skill-creator aplicada para crear tres skills locales de desarrollo.

CODE: notas capturadas primero en Inbox, clasificadas por uso como documentación del proyecto, distinguiendo confirmado/propuesto/pendiente y convertidas en entorno SDD. PARA: se conserva todo dentro del proyecto activo en 01 Projects. No se recrean las carpetas auxiliares eliminadas por el usuario. Esta corrección usa la explicación directa del usuario; no presupone que productos/conectores mencionados tengan acceso local. Pendiente: detalle de formatos, rúbricas y opciones técnicas.
