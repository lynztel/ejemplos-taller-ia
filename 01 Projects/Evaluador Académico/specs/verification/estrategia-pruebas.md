---
categoria: verification
tipo: recurso
estado: en-progreso
proyecto: Evaluador Académico
resumen: "Aceptación y verificación"
utilidad: "Guiar el desarrollo y la verificación de esta aplicación."
contexto: "Handoff v1.0 y planeación integral."
tags: [proyecto/evaluador-academico, desarrollo/sdd]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# Aceptación y verificación

Pruebas previstas, aún no implementadas ni ejecutadas. Solo fixtures sintéticos, incluidos documentos con contenido/localizaciones conocidos según formatos acordados. Verificar comportamiento y recuperación; no pruebas que simplemente repitan el código.

| PR | RF/CA | Escenario y evidencia |
|---|---|---|
| PR-001 | RF-001/CA-001 | Registrar preevaluación no confirma; acción docente deja autor, fecha e historial |
| PR-002 | RF-002/003, CA-002/003 | Identidad incierta, duplicado y versión nueva; hash original intacto |
| PR-003 | RF-004/005, CA-004/005 | Rúbrica incorrecta, criterio desconocido y rango inválido rechazados; historia inalterada |
| PR-004 | RF-006/CA-006 | Reintentos/concurrencia crean un run; contenido distinto con mismo ID genera conflicto |
| PR-005 | RF-005/012, CA-005/012 | Fallo de escritura revierte resultados; movimiento ya realizado a proceso se reconcilia sin perder archivo |
| PR-006 | RF-007/008, CA-007/008 | Evidencia abre página; anotación estable tras zoom/recarga; no reutilizar anclajes de otra versión |
| PR-007 | RF-009/CA-009 | Fuera de rango rechazado, null distinto de cero, rectificación conserva historia |
| PR-008 | RF-010/CA-010 | Métricas contrastadas con dataset conocido, sugerido separado de final |
| PR-009 | RF-011/CA-011 | Restauración aislada valida DB, hashes, PDFs y anotaciones |
| PR-010 | RNF-001/003 | Escape de ruta, HTML en comentario y otro origen no exponen ni mutan datos |
| PR-011 | RF-013/CA-013 | Dos conjuntos y nombres de archivo iguales no se mezclan; subcarpetas preservadas en cada etapa |
| PR-012 | RF-014/005, CA-014/005 | Sesión externa simulada sin acceso a DB produce JSON; aplicación detecta, valida e importa sin API de modelos ni importación manual por tarea |
| PR-013 | RF-015/CA-015 | Iniciar por agente mueve a proceso; doble reclamación no duplica; interrupción se recupera |
| PR-014 | RF-016/CA-016 | Confirmar sin agente activo mueve a evaluadas; una tarea del conjunto permanece en proceso; notas y hash conservados |
| PR-015 | RF-012/016, CA-012/016 | Caída entre intención, traslado y actualización DB; destino colisionado; permisos/disco; reintento sin sobrescritura ni nota duplicada |
| PR-016 | RF-007/017, CA-007/017 | Anterior/siguiente mantiene conjunto/filtros y notas; visor no requiere abrir archivo externo; histórico individual y global consultables |
| PR-017 | RF-013/CA-013 | Recepción manual y flujo completo funcionan sin conector; descarga opcional autorizada usa la misma entrada |

Niveles: dominio unitario; SQLite temporal real para transacciones, migraciones y restricciones; navegador para flujo de revisión/visor. Volumen y umbrales se fijan tras definir carga esperada.

Cada ejecución registra comando real, entorno, fecha, resultado y evidencia sin datos personales. Un INC no se verifica solo por compilar ni por existencia de archivos. La validación de esta entrega documental comprueba estructura y enlaces, no comportamiento de software futuro.

## Aceptación del entorno académico

La matriz AG-001 a AG-010 y CAG-001 a CAG-010 está en [agente preevaluador](../capabilities/agente-preevaluador.md). Antes de datos reales verificar el conjunto sintético de tres tareas, denegación DB, recuperación de movimientos y publicación JSON. Productor simulado valida integración; una sesión real autorizada verifica seguimiento del entorno. No confundir ambos tipos de evidencia.

## Escenarios adicionales de importación automática
- PR-018 (RF-005/006): escribir temporal o interrumpir producción JSON no importa un resultado parcial; al publicar completo se importa una vez.
- PR-019 (RF-005/006/012): producir JSON con aplicación cerrada, iniciar y reabrir importa una sola vez; caída tras commit y antes de archivar no duplica resultados.
- PR-020 (RF-005, RNF-003): el proceso académico carece de acceso directo a DB; JSON con campos finales o referencias inválidas se rechaza sin modificar notas ni crear resultados parciales.
- PR-021 (RF-005/012): watcher/sondeo concurrente, error de DB, cuarentena y fallo de archivado mantienen trazabilidad y permiten reintento sin pérdida.

Son pruebas previstas, no ejecutadas. El mecanismo de permisos debe demostrarse; no darlo por cumplido mediante AGENTS.md.

## Vistas globales y visor flotante

- PR-022 (RF-018): dataset sintético 8/10 + 15/20 = 23/30 confirmados; una tarea pendiente no se convierte en cero; ponderaciones/escala y versiones se prueban con regla explícita.
- PR-023 (RF-019): matriz con rúbricas distintas, notas largas y alumno sin entrega; botón identifica archivo/alumno correctos y distingue IA/docente.
- PR-024 (RF-020/021): abrir visor, anotar, cambiar tarea y cerrar preserva notas, filtro, fila y posición; falla de guardado no descarta cambios.
- PR-025 (RF-020/022): teclado/foco dentro de modal y eventual iframe, Escape con cambios pendientes y retorno al disparador; contraste y estados medidos.
- PR-026 (RF-018): cambiar período, reentrega o reapertura no duplica aportaciones ni mezcla sugeridos y finales; desglose reconstruye acumulado.

Todas son verificaciones previstas, aún no ejecutadas. Validación con docente: recorrer conjunto sin abrir documentos externos y contrastar claridad de la matriz y del acumulado.

## Comprobación de los wireframes

UI-001 a UI-006 de [interfaz](../product/interfaz-wireframes.md) concretan PR-022 a PR-026. Verificar números/etiquetas IA-docente, contador de tareas navegables, contexto conservado, múltiples archivos, datos vacíos y cambios no guardados con Escape o anterior/siguiente. Probar que no aparece información del alumno previo durante carga. No se han ejecutado estas pruebas.
