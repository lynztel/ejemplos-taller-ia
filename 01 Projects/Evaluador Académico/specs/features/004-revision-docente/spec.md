---
tipo: "recurso"
estado: "en-progreso"
categoria: "feature"
proyecto: "Evaluador Académico"
resumen: "FEAT-004 — Revisión y cierre docente"
utilidad: "Organizar, especificar y verificar el desarrollo de la aplicación."
contexto: "Especificaciones vigentes y organización documental basada en fuentes técnicas primarias."
tags: ["proyecto/evaluador-academico", "desarrollo/sdd"]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# FEAT-004 — Revisión y cierre docente

Estado: borrador, no implementado. Capacidad: CAP-004 del [catálogo](../../capabilities/catalogo.md). Entrega: INC-004/005 del [plan global](../../delivery/plan.md).

## Objetivo
El docente recorre tareas dentro del visor, contrasta hallazgos, guarda notas y confirma calificación; el sistema mueve evaluadas sin sesión IA.

## Requisitos y aceptación de referencia
RF-001/007/008/009/016/017; CA correspondientes. Fuente normativa: [requisitos](../../product/requisitos.md). No renumerar ni copiar sus reglas como una segunda fuente de verdad. Para detalles AG/CAG consultar [agente preevaluador](../../capabilities/agente-preevaluador.md).

## Escenarios
- Dado conjunto preevaluado, cuando navega anterior/siguiente y guarda notas, entonces conserva contexto y anotaciones por ID/versión.
- Dada nota confirmada y fallo de traslado, cuando se reintenta, entonces conserva nota e historial y no sobrescribe otro archivo.

## Dependencias y límites
Visor/formato, anclajes, reglas de puntuación e importación; reapertura por definir. No integrar API de modelos ni confirmar notas por agente. Los escenarios precisan el flujo existente, no cierran decisiones de producto pendientes.

## Verificación
PR-001/006/007/014/015/016; [estrategia](../../verification/estrategia-pruebas.md). Todavía no hay evidencia de ejecución.

## Paso a implementación
Crear plan.md y tasks.md aquí cuando comience trabajo concreto, con diseño, dependencias, tareas y evidencia. No generar documentos vacíos ni presentar el borrador como implementado. Seguir [convención documental](../../standards/organizacion-specs.md).

## Ampliación: matriz y visor flotante

RF-019/020/021/022 y CA correspondientes. Seguir [vistas docentes](../../product/vistas-calificaciones.md) y [guía visual](../../standards/interfaz-visual.md). Matriz alumno × criterio con notas y botón Ver entrega; ventana superpuesta con documento, hallazgos IA y edición docente, anterior/siguiente y retorno a la tabla preservando contexto. Iframe solicitado como preferencia de integración; probar contrato y foco frente a componente integrado sin perder experiencia flotante. No basar anotaciones propias en capacidades supuestas del visor nativo.

## Wireframes de referencia

Implementar UI-001/003/004/005/006 de [interfaz](../../product/interfaz-wireframes.md): matriz, modal dividido, notas por autor, guardado y retorno a contexto. PR-023/024/025 deben comprobar comportamiento, no solo coincidencia visual.
