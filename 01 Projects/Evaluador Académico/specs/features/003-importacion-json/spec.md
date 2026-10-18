---
tipo: "recurso"
estado: "en-progreso"
categoria: "feature"
proyecto: "Evaluador Académico"
resumen: "FEAT-003 — Importación automática de preevaluaciones"
utilidad: "Organizar, especificar y verificar el desarrollo de la aplicación."
contexto: "Especificaciones vigentes y organización documental basada en fuentes técnicas primarias."
tags: ["proyecto/evaluador-academico", "desarrollo/sdd"]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# FEAT-003 — Importación automática de preevaluaciones

Estado: borrador, no implementado. Capacidad: CAP-003 del [catálogo](../../capabilities/catalogo.md). Entrega: INC-003 del [plan global](../../delivery/plan.md).

## Objetivo
La aplicación detecta JSON completos, valida esquema/referencias y persiste resultados sin importación manual por tarea.

## Requisitos y aceptación de referencia
RF-005/006/012; CA-005/006/012. Fuente normativa: [requisitos](../../product/requisitos.md). No renumerar ni copiar sus reglas como una segunda fuente de verdad. Para detalles AG/CAG consultar [agente preevaluador](../../capabilities/agente-preevaluador.md).

## Escenarios
- Dado JSON válido, cuando la aplicación lo detecta, entonces importa una ejecución y archiva el resultado sin confirmar nota final.
- Dado reinicio tras commit y antes de archivar, cuando redetecta el JSON, entonces no duplica resultados; inválidos quedan diagnosticados.

## Dependencias y límites
Esquema, IDs, DB e idempotencia; publicación estable y reconciliación. No integrar API de modelos ni confirmar notas por agente. Los escenarios precisan el flujo existente, no cierran decisiones de producto pendientes.

## Verificación
PR-003/004/005/018/019/020/021; [estrategia](../../verification/estrategia-pruebas.md). Todavía no hay evidencia de ejecución.

## Paso a implementación
Crear plan.md y tasks.md aquí cuando comience trabajo concreto, con diseño, dependencias, tareas y evidencia. No generar documentos vacíos ni presentar el borrador como implementado. Seguir [convención documental](../../standards/organizacion-specs.md).
