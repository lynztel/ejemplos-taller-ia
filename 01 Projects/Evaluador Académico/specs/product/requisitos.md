---
categoria: product
tipo: recurso
estado: en-progreso
proyecto: Evaluador Académico
resumen: "Requisitos y aceptación"
utilidad: "Guiar el desarrollo y verificación de esta aplicación."
contexto: "Handoff v1.0 y planeación integral."
tags: [proyecto/evaluador-academico, desarrollo/sdd]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# Requisitos y aceptación

Requisitos corregidos según la aclaración funcional del docente. RF-001 a RF-012 mantienen sus IDs; se ajustan criterios y se añaden RF-013 a RF-017. Detalle técnico de aceptación propuesto.

| ID | Requisito | Aceptación |
|---|---|---|
| RF-001 | Confirmación final exclusiva del docente | CA-001: registrar preevaluación no confirma; acción explícita registra autor, fecha y resultado |
| RF-002 | Grupos, alumnos y actividades | CA-002: entrega vinculada a entidades existentes; identidad incierta no se acepta silenciosamente |
| RF-003 | Incorporación y conservación | CA-003: hash y versión registrados; no sobrescribir originales; detectar contenido repetido |
| RF-004 | Rúbricas versionadas | CA-004: ejecución conserva versión; cambios posteriores no alteran historia |
| RF-005 | Preevaluación JSON e importación automática | CA-005: agente genera JSON obligatorio sin acceso directo a DB; aplicación detecta, valida e importa automáticamente, sin acción manual por tarea; inválidos no crean resultados y válidos se persisten en transacción |
| RF-006 | Idempotencia | CA-006: mismo run_id y payload no duplica; contenido diferente con mismo ID genera conflicto |
| RF-007 | Visor y evidencia | CA-007: archivo se abre dentro de la aplicación; evidencia navega a versión/localización admitida; fallos visibles sin inventar contenido |
| RF-008 | Anotaciones y retroalimentación | CA-008: comentario, anclaje, criterio, autor y versión persisten al recargar |
| RF-009 | Revisión y nota final | CA-009: al marcar evaluada/calificada se exige nota válida, autor y fecha; revisión posterior preserva historia |
| RF-010 | Informes y pendientes | CA-010: filtros e indicadores coinciden con SQLite; distinguir sugerido y confirmado |
| RF-011 | Respaldo/restauración | CA-011: restaurar en aislamiento recupera DB, archivos y asociaciones verificadas |
| RF-012 | Estados controlados | CA-012: transición ilegal rechazada; estado de movimiento diferenciado del académico |
| RF-013 | Recepción por conjuntos | CA-013: trabajos de una actividad se depositan en Tareas no procesadas con subcarpeta propia; no se mezclan conjuntos de igual nombre en grupos distintos |
| RF-014 | Entorno académico de agentes | CA-014: desde el repositorio el agente identifica rúbrica/skills y opera sin API de modelos integrada; solo registra sugerencias |
| RF-015 | Paso a proceso por agente | CA-015: tarea reclamada se mueve a Tareas en proceso dentro del mismo conjunto; doble inicio no duplica ni sobrescribe |
| RF-016 | Traslado al finalizar | CA-016: confirmar nota programa traslado automático a Tareas evaluadas del mismo conjunto, sin agente activo; fallo/reintento visible, conserva nota y hash |
| RF-017 | Revisión continua e histórico global | CA-017: anterior/siguiente en visor mantiene contexto del conjunto; notas guardadas persisten y son consultables por tarea y en histórico global filtrable |

## Requisitos de calidad
RNF-001: rutas de datos confinadas a raíz configurada. RNF-002: transacciones y restricciones únicas resisten reintentos/concurrencia. RNF-003: datos académicos, logs sensibles y respaldos fuera de Git. RNF-004: dominio independiente de UI y adaptadores. RNF-005: recuperación comprobada antes de datos reales. RNF-006 propuesto: teclado, etiquetas, foco y guardado visible. RNF-007: fijar tamaños, páginas, volúmenes y tiempos con el docente y mediciones representativas, sin inventar capacidad garantizada.

Historias: como docente quiero depositar un conjunto y pedir al agente externo preevaluarlo (RF-013/014/015/005); recorrer las tareas dentro del visor y contrastar criterios/notas (RF-007/017); confirmar una nota y que el archivo se organice automáticamente (RF-009/016); consultar el histórico individual y global (RF-010/017).

Recepción manual funciona sin conectores. Descarga por conector de un entorno externo es opcional y requiere permisos disponibles; no presupone un conector incorporado en esta aplicación.

## Vistas globales y revisión flotante

Detalle en [vistas de calificaciones](vistas-calificaciones.md). Requisitos incorporados por propuesta directa del docente; diseño detallado y reglas de cálculo aún por concretar.

| ID | Requisito | Aceptación |
|---|---|---|
| RF-018 | Calificaciones acumuladas por curso/período | CA-018: filtrar ámbito muestra notas por actividad y acumulado desglosable; no suma sugerencias, versiones duplicadas ni faltantes como cero implícito |
| RF-019 | Matriz de alumnos y criterios | CA-019: filas de alumnos, columnas dinámicas de rúbrica, puntuaciones/notas identificables y botón Ver entrega por fila |
| RF-020 | Visor flotante embebido | CA-020: botón abre documento correcto con panel de notas IA/docente; cerrar retorna a tabla con filtros/fila/posición conservados |
| RF-021 | Edición continua sin pérdida | CA-021: guardar/cambiar tarea/cerrar conserva anotaciones y distingue borrador de confirmación final; error de guardado visible y sin descarte silencioso |
| RF-022 | Interfaz minimalista y accesible | CA-022: tablas, filtros y visor siguen guía visual, foco/teclado comprobados y estados comprensibles sin depender solo del color |
