---
categoria: standards
tipo: recurso
estado: en-progreso
proyecto: Evaluador Académico
resumen: "Convenciones"
utilidad: "Especificar y verificar el desarrollo de esta aplicación."
contexto: "Handoff v1.0 y planeación integral."
tags: [proyecto/evaluador-academico, desarrollo/sdd]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# Convenciones

## Código
Propuesta: TypeScript estricto; nombres técnicos en inglés; UI y documentación en español. Archivos kebab-case; componentes PascalCase; funciones/variables camelCase. IDs opacos y estables, sin nombres de alumnos como claves. Fechas persistidas UTC ISO 8601, mostradas en zona del docente.

Validación en servidor; errores con código estable y mensaje comprensible sin datos sensibles. Diferenciar null y cero; precisión y redondeo definidos por rúbrica. Consultas parametrizadas. Migraciones numeradas y versionadas; el agente académico genera JSON y no abre ni modifica DB; únicamente el importador de la aplicación escribe preevaluaciones validadas. Reglas de dominio independientes del framework.

## SDD y cambios
RF/RNF: requisito; CA: aceptación; ADR: decisión; INC: incremento; PR: prueba. No reutilizar IDs retirados. Cada cambio enlaza requisito → aceptación → tareas → evidencia. Decisiones registran contexto, alternativas, elección, consecuencias y quién las confirmó. No atribuir acuerdos al docente por inferencia.

Cambios pequeños y coherentes. Mensajes Git propuestos docs:, feat:, fix:, test:. No crear commits ni remotos como efecto de escribir documentación. Antes de inicializar Git comprobar si la bóveda ya está versionada y definir frontera del repositorio. Versionar bloqueo de dependencias cuando exista; excluir datos operativos y secretos.

## Listo y terminado
Listo: comportamiento, entradas/salidas, errores y aceptación definidos; decisiones bloqueantes resueltas. Terminado: implementado, verificaciones pertinentes pasadas, evidencia registrada y documentación actualizada. Una especificación no equivale a una función terminada.

## Archivos y operaciones académicas
Conservar exactamente las etiquetas Tareas no procesadas, Tareas en proceso y Tareas evaluadas bajo data/. Mantener subcarpeta/clave estable por conjunto. Un movimiento cambia ubicación, no bytes ni identidad; la UI resuelve ID a ruta actual. Confirmación académica y finalización física son estados independientes y recuperables.

## Interfaz docente
Separar sugerido, borrador y confirmado. Etiquetas de formulario, foco visible, teclado y estado de guardado. Confirmación explícita con resumen. Guardar revisión no confirma automáticamente nota.
