---
tipo: "recurso"
estado: "en-progreso"
categoria: "feature"
proyecto: "Evaluador Académico"
resumen: "FEAT-002 — Preevaluación desde sesión externa"
utilidad: "Organizar, especificar y verificar el desarrollo de la aplicación."
contexto: "Especificaciones vigentes y organización documental basada en fuentes técnicas primarias."
tags: ["proyecto/evaluador-academico", "desarrollo/sdd"]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# FEAT-002 — Preevaluación desde sesión externa

Estado: borrador, no implementado. Capacidad: CAP-002 del [catálogo](../../capabilities/catalogo.md). Entrega: INC-003, con preparación en INC-001/002 del [plan global](../../delivery/plan.md).

## Objetivo
El agente abre su entorno autorizado, recibe manifiesto/rúbrica, inicia tareas con utilidad y publica JSON obligatorio sin acceso directo a DB.

## Requisitos y aceptación de referencia
RF-014/015; AG-001 a AG-010 y CAG correspondientes. Fuente normativa: [requisitos](../../product/requisitos.md). No renumerar ni copiar sus reglas como una segunda fuente de verdad. Para detalles AG/CAG consultar [agente preevaluador](../../capabilities/agente-preevaluador.md).

## Escenarios
- Dado manifiesto y perfil autorizado, cuando inicia una tarea, entonces se traslada a proceso dentro del mismo conjunto y se genera JSON con evidencia y versiones.
- Dado criterio exclusivamente docente o archivo inaccesible, cuando analiza, entonces no inventa puntuación y declara limitación.

## Dependencias y límites
Aislamiento, manifiesto, utilidad, skills por rúbrica y formatos. No integrar API de modelos ni confirmar notas por agente. Los escenarios precisan el flujo existente, no cierran decisiones de producto pendientes.

## Verificación
PR-012/013/020 y CAG-001 a CAG-010; [estrategia](../../verification/estrategia-pruebas.md). Todavía no hay evidencia de ejecución.

## Paso a implementación
Crear plan.md y tasks.md aquí cuando comience trabajo concreto, con diseño, dependencias, tareas y evidencia. No generar documentos vacíos ni presentar el borrador como implementado. Seguir [convención documental](../../standards/organizacion-specs.md).
