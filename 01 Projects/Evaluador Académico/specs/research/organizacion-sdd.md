---
tipo: "recurso"
estado: "en-progreso"
categoria: "research"
proyecto: "Evaluador Académico"
resumen: "Investigación de organización SDD"
utilidad: "Organizar, especificar y verificar el desarrollo de la aplicación."
contexto: "Especificaciones vigentes y organización documental basada en fuentes técnicas primarias."
tags: ["proyecto/evaluador-academico", "desarrollo/sdd"]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# Investigación de organización SDD

## Resultado y límites

Las fuentes consultadas sustentan una separación por propósito documental. La taxonomía de subcarpetas es una decisión de organización de este proyecto, no una estructura ISO obligatoria. Las versiones citadas son las encontradas en los catálogos oficiales durante esta consulta; no se afirma conformidad normativa.

| Fuente primaria | Criterio aplicado |
|---|---|
| [ISO/IEC/IEEE 29148:2018](https://www.iso.org/standard/72089.html) | Ingeniería de requisitos como disciplina: mantener necesidades/requisitos y su gestión identificables en product |
| [ISO/IEC 25010:2023](https://www.iso.org/standard/78176.html) | Calidad del producto merece requisitos explícitos y comprobables, no solo preferencias de implementación |
| [arc42](https://arc42.org/overview/) | Separar estructura arquitectónica, decisiones, calidad y riesgos sin exigir doce carpetas en un proyecto personal |
| [ADR templates](https://adr.github.io/adr-templates/) | Cada decisión registra estado, contexto, decisión y consecuencias; distinguir propuesta y aceptada |
| [GitHub Spec Kit](https://github.com/github/spec-kit/blob/main/docs/concepts/spec-of-specs.md) | Dividir trabajo grande en features acotadas con spec/plan/tasks y ciclo propio |
| [OpenSpec: conceptos](https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md) | Organizar comportamiento por dominios/capacidades y distinguirlo de propuestas de cambio y detalles de implementación |
| [SEBoK: verificación](https://sebokwiki.org/wiki/System_Verification) y [validación](https://sebokwiki.org/wiki/System_Validation) | Diferenciar evidencia de cumplimiento de requisitos y satisfacción de necesidades del docente |

## Decisión derivada

Mantener producto y requisitos globales, capacidades duraderas, features implementables, arquitectura transversal, contratos, ADR, convenciones, verificación, entrega y fuentes. Se conservan nombres ingleses de carpetas para una navegación uniforme; contenidos en español. No se incorporan dependencias ni comandos de herramientas por copiar su nomenclatura.

No se crea una carpeta por cada concepto de cada estándar. No se duplica la aceptación en feature, requisito y prueba: se enlazan IDs, añadiendo escenarios propios cuando aportan precisión. Tampoco se interpreta «standards» como afirmación de cumplimiento normativo: contiene convenciones locales.

## Mantenimiento

El catálogo de capacidades y la matriz de features definen dónde ubicar trabajo nuevo. Una decisión de tecnología se propone mediante ADR y se refleja en architecture solo cuando corresponda. Investigación no cambia por sí misma el estado de aprobación del stack ni los permisos operativos.
