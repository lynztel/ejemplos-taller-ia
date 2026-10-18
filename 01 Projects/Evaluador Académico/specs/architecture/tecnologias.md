---
categoria: architecture
tipo: recurso
estado: en-progreso
proyecto: Evaluador Académico
resumen: "Tecnologías y pruebas técnicas"
utilidad: "Especificar y verificar el desarrollo de esta aplicación."
contexto: "Handoff v1.0 y planeación integral."
tags: [proyecto/evaluador-academico, desarrollo/sdd]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# Tecnologías y pruebas técnicas

Stack de referencia propuesto, no instalado ni aprobado como decisión final. Fijar versiones compatibles y archivo de bloqueo en infraestructura, consultando requisitos oficiales vigentes.

| Componente | Propuesta | Validación previa |
|---|---|---|
| Runtime | Node.js compatible con Astro seleccionado | Acceso a disco y ejecución local en Windows |
| Lenguaje | TypeScript estricto | Tipos y validación de entradas en ejecución |
| Web | Astro servidor con adaptador Node | Endpoint que persiste y sirve PDF autorizado; no asumir exportación estática suficiente |
| Interactividad | React donde se necesite | Estado de formularios y visor sin complejidad excesiva |
| Persistencia | SQLite | Driver pendiente: probar Windows, transacciones, claves y backup |
| Visor integrado de archivos | PDF.js como candidato para PDF | Navegación anterior/siguiente y notas sin abrir cada archivo fuera; formatos iniciales aún por definir |
| Salida del agente | Archivos JSON obligatorios | Agente escribe resultados y mueve tareas por conjunto; no abre DB |
| Importación automática | Servicio local de detección y validación | Procesar archivos JSON completos al iniciar y durante ejecución; mecanismo watcher/sondeo por elegir |
| Automatización | Script/servicio local de movimientos | Cierre sin agente activo, reintentos, colisiones y reconciliación |
| Contratos | JSON obligatorio versionado; JSON Schema 2020-12 propuesto | Validación estructural y semántica antes de escritura en DB |
| Pruebas | Runner TypeScript y automatización de navegador por elegir | Integración real con DB temporal y PDF sintético |
| Presentación | CSS con variables | Estados y diseño accesibles |

## Decisión de framework
Astro conserva la propuesta inicial. Comparar Astro con islas React frente a UI React y backend local si el visor requiere estado compartido intensivo. Evaluar complejidad, persistencia, distribución y mantenimiento; registrar selección antes del scaffold. No migrar por preferencia del agente.

## Entornos externos
No incorporar SDK de modelo ni runtime de agente propio como dependencia del producto. El repositorio aporta comportamiento y skills; la sesión externa aporta capacidades de IA. No hay validación de acceso por nombre de producto. Drive/conector es alternativa opcional externa; adquisición manual debe funcionar siempre.

## Experimentos de infraestructura
Servidor local con acceso controlado a archivo sintético; SQLite con rollback, unicidad y snapshot consistente; anotación estable tras zoom del PDF; validación estructural separada de referencias semánticas. Probar producción JSON desde sesión externa sin acceso a DB, detección e importación automáticas, traslado entre tres etapas por conjunto y fallo a mitad de movimiento con recuperación; visor con cambio de tarea conservando notas. Registrar resultados y versiones probadas.

Fuentes oficiales: [Astro Node](https://docs.astro.build/en/guides/integrations-guide/node/), [PDF.js](https://mozilla.github.io/pdf.js/getting_started/), [SQLite backup](https://sqlite.org/backup.html), [JSON Schema](https://json-schema.org/draft/2020-12/). No certifican las elecciones de producto.
