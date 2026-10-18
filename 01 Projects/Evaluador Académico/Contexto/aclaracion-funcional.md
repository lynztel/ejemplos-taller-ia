---
tipo: recurso
estado: activo
proyecto: Evaluador Académico
resumen: "Aclaración del docente sobre conjuntos de tareas, agente externo, base de datos, visor y traslado automático."
utilidad: "Corregir el alcance y resolver contradicciones del handoff y las especificaciones iniciales."
contexto: "Explicación directa del usuario posterior al handoff v1.0."
tags: [proyecto/evaluador-academico, desarrollo/sdd]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/product/alcance]]", "[[01 Projects/Evaluador Académico/specs/capabilities/flujo-evaluacion]]"]
proxima_accion: "Definir esquema JSON, detección automática y formatos iniciales del visor."
---

# Aclaración funcional del docente

Fuente: explicación directa del usuario en este chat, posterior al handoff. Síntesis fiel para desarrollo; no transcripción literal. No se deducen capacidades garantizadas de productos ni conectores a partir de sus nombres.

## Objetivo
Acelerar y optimizar evaluación docente tarea por tarea, reduciendo apertura manual de archivos y trabajo repetitivo. Uso personal con agentes externos disponibles en suscripciones; no integrar un agente propio por API de modelos de pago.

## Recorrido confirmado
1. Docente descarga trabajos de cualquier plataforma escolar y los deposita por conjunto en Tareas no procesadas. Alternativa opcional: sesión de IA con conector autorizado descarga desde Drive a la misma entrada.
2. Docente abre el repositorio en sesión de agente (ejemplos mencionados: ChatGPT Work, CloudQ Work, AntiGravity). Entorno de comportamiento y skills derivadas de rúbricas/criterios guían preevaluación.
3. Agente mueve trabajos a Tareas en proceso y produce JSON de preevaluaciones, criterios, hallazgos y anotaciones; la aplicación los importa automáticamente a la base de datos. El usuario ratificó después que el agente no accede directamente a DB.
4. Aplicación permite visualizar archivos, navegar tareas, revisar criterios y notas del agente, añadir comentarios y dictaminar nota final. Incluye consulta por tarea e histórico global.
5. Docente marca evaluada/calificada con nota. Traslado a Tareas evaluadas puede hacerlo el agente, pero preferentemente lo automatiza un script/servicio de la propia aplicación sin requerir IA.
6. Cada conjunto tiene subcarpeta propia en las etapas, por ejemplo Primera tarea del parcial. Tareas del mismo conjunto avanzan individualmente.

## Correcciones respecto al handoff
JSON obligatorio como salida del agente; importación automática por aplicación, sin paso manual del docente por tarea. La interpretación previa de JSON opcional fue un error del asistente, corregido por el usuario. Movimientos de archivos sí son parte funcional del flujo, conservando contenido e identidad. Visor y navegación son centrales para reducir fricción; formatos admitidos todavía deben definirse. La nota final sigue siendo exclusiva del docente.

## Prioridad de esta fuente
Esta aclaración, con la ratificación posterior de JSON obligatorio y sin acceso directo del agente a DB, prevalece sobre descripciones incompatibles. Mantiene la frontera JSON del handoff y amplía el flujo de carpetas/conjuntos. Se preservan esos antecedentes sin presentarlos como descripción actual completa. No se procesa ni mueve ninguna entrega real al actualizar documentación.
