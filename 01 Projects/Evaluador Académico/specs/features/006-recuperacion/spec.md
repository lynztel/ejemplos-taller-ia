---
tipo: "recurso"
estado: "en-progreso"
categoria: "feature"
proyecto: "Evaluador Académico"
resumen: "FEAT-006 — Respaldo y recuperación"
utilidad: "Organizar, especificar y verificar el desarrollo de la aplicación."
contexto: "Especificaciones vigentes y organización documental basada en fuentes técnicas primarias."
tags: ["proyecto/evaluador-academico", "desarrollo/sdd"]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# FEAT-006 — Respaldo y recuperación

Estado: borrador, no implementado. Capacidad: CAP-006 del [catálogo](../../capabilities/catalogo.md). Entrega: INC-007, controles desde INC-001 del [plan global](../../delivery/plan.md).

## Objetivo
Recuperar datos, documentos y operaciones pendientes sin pérdida ni duplicación.

## Requisitos y aceptación de referencia
RF-011/012; CA-011/012; RNF-001/003/005. Fuente normativa: [requisitos](../../product/requisitos.md). No renumerar ni copiar sus reglas como una segunda fuente de verdad. Para detalles AG/CAG consultar [agente preevaluador](../../capabilities/agente-preevaluador.md).

## Escenarios
- Dado respaldo consistente, cuando restaura en aislamiento, entonces verifica DB, hashes y asociaciones documento/anotación.
- Dada operación interrumpida, cuando reconcilia, entonces muestra pendiente/error y reintenta sin duplicar confirmaciones ni resultados.

## Dependencias y límites
Política de respaldo, motor de movimientos e importador. No integrar API de modelos ni confirmar notas por agente. Los escenarios precisan el flujo existente, no cierran decisiones de producto pendientes.

## Verificación
PR-005/009/015/019/021; [estrategia](../../verification/estrategia-pruebas.md). Todavía no hay evidencia de ejecución.

## Paso a implementación
Crear plan.md y tasks.md aquí cuando comience trabajo concreto, con diseño, dependencias, tareas y evidencia. No generar documentos vacíos ni presentar el borrador como implementado. Seguir [convención documental](../../standards/organizacion-specs.md).
