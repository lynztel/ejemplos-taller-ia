---
categoria: product
tipo: recurso
estado: en-progreso
proyecto: Evaluador Académico
resumen: "Alcance inicial"
utilidad: "Guiar el desarrollo y verificación de esta aplicación."
contexto: "Handoff v1.0 corregido por aclaración funcional directa del usuario."
tags: [proyecto/evaluador-academico, desarrollo/sdd]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# Alcance y experiencia del docente

## Problema y objetivo confirmados
Evaluar tarea por tarea obliga al docente a abrir archivos, contrastar criterios, redactar observaciones y registrar notas repetidamente. El objetivo es acelerar y optimizar ese trabajo con una aplicación local y agentes de IA disponibles en entornos externos, aprovechando las suscripciones del docente. No se construye un agente propio ni se integra una API de modelos de pago dentro de la aplicación.

## Preparación de entregas
El docente descarga el conjunto de trabajos de la plataforma de su escuela o universidad y lo coloca en `data/Tareas no procesadas/<conjunto>/`. El sistema es independiente de una institución concreta. Alternativamente, un agente externo con conector autorizado podría descargar desde una carpeta como Google Drive y depositar los archivos en esa misma entrada. Es una vía opcional; no exigirla ni presuponer que cualquier entorno tiene ese acceso.

Cada conjunto corresponde a una actividad/entrega definida por el docente, por ejemplo «Primera tarea del parcial», y conserva su subcarpeta en las tres etapas. Un conjunto agrupa trabajos individuales; no confundir conjunto, alumno y archivo.

## Preevaluación desde una sesión externa
El docente abre el repositorio en su entorno de agente, por ejemplo los entornos mencionados en la aclaración: ChatGPT Work, Claude cowork o AntiGravity. La disponibilidad y permisos concretos deben comprobarse, sin asumir equivalencia entre productos. El agente lee el entorno de comportamiento y skills académicas del repositorio, definidas a partir de rúbricas y criterios; procesa el conjunto, mueve tareas a `Tareas en proceso` y genera archivos JSON con preevaluaciones, hallazgos y anotaciones. La aplicación los valida e importa automáticamente a la base de datos, sin escritura directa del agente.

JSON es la salida obligatoria del agente y la frontera con la base de datos. La aplicación detecta resultados completos, valida y persiste sin exigir importación manual por tarea al docente. No se admiten canales alternativos que omitan este contrato ni acceso directo del agente a DB.

## Revisión en la aplicación
El docente visualiza archivos dentro de la misma aplicación, revisa criterios, puntuaciones sugeridas y anotaciones del agente, añade notas y decide la calificación individual. Puede navegar entre tareas del conjunto sin abrir cada documento en una aplicación externa, consultar el histórico de cada tarea y el histórico global con filtros.

Al finalizar, marca la tarea como evaluada/calificada con su nota. La aplicación automatiza su traslado a `Tareas evaluadas/<conjunto>/` mediante un servicio/script. El usuario admite que lo haga el agente; la opción preferente de diseño es automatización local sin requerir otra sesión de IA. Las tareas restantes pueden seguir en proceso.

## Confirmado frente a pendiente
Confirmados: uso personal docente, agente externo con entorno en repositorio, skills por rúbrica, registro mediante JSON e importación automática en DB, tres etapas de carpetas, agrupación por conjunto, visor integrado, revisión e historial y calificación final docente. El diseño de producto se orienta a un docente; autenticación y distribución exactas siguen por concretar.

Pendientes: formatos iniciales del visor, rúbrica y puntuación, identificación/reentregas, esquema JSON y detección automática de resultados, entorno concreto y permisos, tecnología final, anclajes por tipo de archivo y respaldo. No trasladar reglas del prototipo anterior ni convertir una elección técnica en requisito confirmado.

Fuente vigente: [aclaración funcional](../../Contexto/aclaracion-funcional.md). El handoff y lienzo anteriores conservan antecedentes, pero se conserva su frontera JSON/agente/DB y se corrige el flujo de movimientos según la aclaración; esta última también incorpora la ratificación posterior de JSON obligatorio.

## Ampliación de vistas docentes

Se incorporan vista acumulada por curso/período, matriz de alumnos/criterios y visor flotante embebido con notas del agente/docente. [Especificación de vistas](vistas-calificaciones.md). Estilo solicitado: minimalista con referencias Vercel y Cloudflare. No queda definida una fórmula de nota final de curso hasta configurar puntos/ponderaciones y reglas de cierre.
