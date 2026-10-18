---
tipo: recurso
estado: en-progreso
proyecto: Evaluador Académico
resumen: "Especificaciones vigentes"
utilidad: "Guiar el desarrollo y verificación de esta aplicación."
contexto: "Handoff v1.0 y planeación integral."
tags: [proyecto/evaluador-academico, desarrollo/sdd]
relacionado_con: ["[[01 Projects/Evaluador Académico/Contexto/handoff]]"]
---

# Especificaciones vigentes

Revisión funcional 0.3. Fuente vigente: [aclaración directa del docente](../Contexto/aclaracion-funcional.md), que corrige el handoff y el lienzo originales. Confirmado: agente externo con entorno/skills del repositorio, conjuntos en tres carpetas, JSON obligatorio e importación automática en DB, visor/revisión e histórico y traslado final automatizable. El agente no accede directamente a DB. Stack, esquema detallado y detección de archivos siguen por concretar.

## Organización por propósito

```text
specs/
  product/        alcance y requisitos RF/RNF/CA
  capabilities/   catálogo CAP, flujo y entorno AG/CAG
  features/       entregas FEAT con spec.md y futuros plan/tasks
  architecture/   componentes, datos, tecnología y seguridad
  contracts/      contrato JSON obligatorio
  decisions/      historial y ADR individuales
  standards/      convenciones locales
  verification/   pruebas y evidencia prevista
  delivery/       plan global INC
  research/       fuentes e investigación
```

| Categoría          | Entrada                                                                                                                                                                                                                                                                                                                                        |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Producto           | [Alcance](product/alcance.md) · [Requisitos](product/requisitos.md) · [Vistas y calificaciones](product/vistas-calificaciones.md) · [Wireframes](product/interfaz-wireframes.md)                                                                                                                                                               |
| Capacidades        | [Catálogo CAP](capabilities/catalogo.md) · [Flujo](capabilities/flujo-evaluacion.md) · [Agente preevaluador](capabilities/agente-preevaluador.md)                                                                                                                                                                                              |
| Features           | [Recepción](features/001-recepcion-conjuntos/spec.md) · [Agente externo](features/002-preevaluacion-externa/spec.md) · [Importación JSON](features/003-importacion-json/spec.md) · [Revisión docente](features/004-revision-docente/spec.md) · [Histórico](features/005-historico/spec.md) · [Recuperación](features/006-recuperacion/spec.md) |
| Arquitectura       | [Estructura](architecture/arquitectura.md) · [Datos](architecture/datos.md) · [Tecnologías](architecture/tecnologias.md) · [Seguridad](architecture/seguridad.md)                                                                                                                                                                              |
| Contratos          | [JSON e importación automática](contracts/preevaluacion-json.md)                                                                                                                                                                                                                                                                               |
| Decisiones         | [Registro y ADR](decisions/registro.md)                                                                                                                                                                                                                                                                                                        |
| Estándares locales | [Convenciones](standards/convenciones.md) · [Organización documental](standards/organizacion-specs.md) · [Guía visual](standards/interfaz-visual.md)                                                                                                                                                                                           |
| Verificación       | [Estrategia y escenarios](verification/estrategia-pruebas.md)                                                                                                                                                                                                                                                                                  |
| Entrega            | [Plan de incrementos](delivery/plan.md)                                                                                                                                                                                                                                                                                                        |
| Investigación      | [Fuentes del producto](research/fuentes.md) · [Criterios SDD investigados](research/organizacion-sdd.md)                                                                                                                                                                                                                                       |

Capacidad describe qué debe poder hacer el producto; feature define una porción implementable. Los IDs previos se conservan y las features enlazan RF/CA sin sustituirlos. La taxonomía es una convención de este proyecto informada por fuentes actuales; no una estructura ISO obligatoria ni una declaración de conformidad.

## Mantenimiento
AGENTS.md contiene reglas de trabajo; specs/ define comportamiento. Ante contradicciones, registrar la decisión y corregir documentos explícitamente. Esta carpeta concentra las especificaciones vigentes; no mantener contratos activos duplicados.

Estados documentales: borrador → en revisión → acordado → implementado → verificado. Acuerdo requiere decisión registrada; verificado requiere evidencia. Registrar motivo, fecha y requisitos afectados al cambiar una especificación.
