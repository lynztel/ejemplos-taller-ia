---
tipo: "recurso"
estado: "en-progreso"
categoria: "feature"
proyecto: "Evaluador Académico"
resumen: "FEAT-001 — Recepción y organización de conjuntos"
utilidad: "Organizar, especificar y verificar el desarrollo de la aplicación."
contexto: "Especificaciones vigentes y organización documental basada en fuentes técnicas primarias."
tags: ["proyecto/evaluador-academico", "desarrollo/sdd"]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# FEAT-001 — Recepción y organización de conjuntos

Estado: borrador, no implementado. Capacidad: CAP-001 del [catálogo](../../capabilities/catalogo.md). Entrega: INC-002 del [plan global](../../delivery/plan.md).

## Objetivo
El docente deposita una actividad en Tareas no procesadas; la aplicación identifica conjunto, alumno y versiones sin mezclar grupos.

## Requisitos y aceptación de referencia
RF-002/003/004/013; CA-002/003/004/013. Fuente normativa: [requisitos](../../product/requisitos.md). No renumerar ni copiar sus reglas como una segunda fuente de verdad. Para detalles AG/CAG consultar [agente preevaluador](../../capabilities/agente-preevaluador.md).

## Escenarios
- Dado un conjunto con documentos, cuando se incorporan, entonces cada archivo conserva ID/hash y asociación al conjunto.
- Dado el mismo nombre en dos conjuntos, cuando se incorporan, entonces no se sobrescriben ni confunden.

## Dependencias y límites
Formatos, identidad, reentregas y rúbrica/versionado. No integrar API de modelos ni confirmar notas por agente. Los escenarios precisan el flujo existente, no cierran decisiones de producto pendientes.

## Verificación
PR-002/003/011/017; [estrategia](../../verification/estrategia-pruebas.md). Todavía no hay evidencia de ejecución.

## Paso a implementación
Crear plan.md y tasks.md aquí cuando comience trabajo concreto, con diseño, dependencias, tareas y evidencia. No generar documentos vacíos ni presentar el borrador como implementado. Seguir [convención documental](../../standards/organizacion-specs.md).
