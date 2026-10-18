---
tipo: "recurso"
estado: "en-progreso"
categoria: "feature"
proyecto: "Evaluador Académico"
resumen: "FEAT-005 — Histórico e indicadores"
utilidad: "Organizar, especificar y verificar el desarrollo de la aplicación."
contexto: "Especificaciones vigentes y organización documental basada en fuentes técnicas primarias."
tags: ["proyecto/evaluador-academico", "desarrollo/sdd"]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# FEAT-005 — Histórico e indicadores

Estado: borrador, no implementado. Capacidad: CAP-005 del [catálogo](../../capabilities/catalogo.md). Entrega: INC-006 del [plan global](../../delivery/plan.md).

## Objetivo
Consultar tareas, observaciones y resultados individuales/globales distinguiendo preevaluación y nota final.

## Requisitos y aceptación de referencia
RF-010/017; CA-010/017. Fuente normativa: [requisitos](../../product/requisitos.md). No renumerar ni copiar sus reglas como una segunda fuente de verdad. Para detalles AG/CAG consultar [agente preevaluador](../../capabilities/agente-preevaluador.md).

## Escenarios
- Dado historial con varias ejecuciones, cuando consulta una tarea, entonces conserva versiones y decisiones sin mezclar sugerido y confirmado.
- Dado filtro por conjunto/grupo, cuando consulta histórico global, entonces presenta solo registros asociados y métricas coherentes.

## Dependencias y límites
Filtros/indicadores acordados y revisiones persistidas. No integrar API de modelos ni confirmar notas por agente. Los escenarios precisan el flujo existente, no cierran decisiones de producto pendientes.

## Verificación
PR-008/016; [estrategia](../../verification/estrategia-pruebas.md). Todavía no hay evidencia de ejecución.

## Paso a implementación
Crear plan.md y tasks.md aquí cuando comience trabajo concreto, con diseño, dependencias, tareas y evidencia. No generar documentos vacíos ni presentar el borrador como implementado. Seguir [convención documental](../../standards/organizacion-specs.md).

## Ampliación: calificaciones globales

RF-018/CA-018. Añadir vista por curso/período con alumnos, actividades, notas confirmadas, acumulado y progreso, con enlace al conjunto y su matriz. [Reglas de vistas y cálculo](../../product/vistas-calificaciones.md). Probar puntos de escalas comparables, ponderaciones configuradas, faltantes y reentregas; no fijar promedio o suma universal ni sustituir pendientes por cero sin regla docente. Dirección visual en [guía](../../standards/interfaz-visual.md).

## Wireframe global

UI-001/002 de [interfaz](../../product/interfaz-wireframes.md): contexto curso/grupo/período, tabla dinámica, desglose de acumulado y navegación al conjunto. Contadores coherentes con columnas y alumnos filtrados; números del mockup no se copian como constantes.
