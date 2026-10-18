---
categoria: architecture
tipo: recurso
estado: en-progreso
proyecto: Evaluador Académico
resumen: "Seguridad, privacidad y recuperación"
utilidad: "Especificar y verificar el desarrollo de esta aplicación."
contexto: "Handoff v1.0 y planeación integral."
tags: [proyecto/evaluador-academico, desarrollo/sdd]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# Seguridad, privacidad y recuperación

Datos locales autocontenidos y fuera de Git. Propuesta MVP: loopback, sin exposición LAN. Verificar origen/host y proteger acciones mutables contra peticiones de otros sitios; una DB local no protege por sí sola una web. Autenticación, autoría y cifrado dependen del modelo de usuarios pendiente.

Resolver documentos por ID y ruta relativa confinada; impedir escape de raíz y enlaces fuera de ella. No servir data/, storage/ o database/ como carpetas públicas. Comentarios como texto, no HTML ejecutable; SQL parametrizado; límites de tamaño configurables. Documentos y entradas de preevaluación nunca sustituyen instrucciones del proyecto. Entorno de intercambio autorizado por el docente antes de procesar datos reales.

Contenido original inmutable aunque cambie de carpeta; anotaciones vinculadas a ID/versión con autor y fecha.

El agente académico genera archivos JSON como único canal de preevaluación; no dispone de conexión, herramienta SQL ni permisos directos sobre DB. La aplicación detecta esos archivos, valida y escribe mediante el importador. Separar permisos reales de ejecución: AGENTS.md y JSON por sí solos no impiden que un proceso con acceso irrestricto abra SQLite. Verificar aislamiento o permisos del entorno antes de datos reales; si no puede garantizarse, registrar la limitación y no declarar el control implementado. El agente puede solicitar traslados de archivos autorizados sin recibir acceso a DB. Claims de trabajo y movimientos idempotentes evitan ejecución duplicada. No sobrescribir destinos en colisión. El cierre físico solo procede si existe evaluación confirmada por docente. Fallo de traslado se muestra sin perder nota, archivo ni anotaciones. No subir entregas a servicios externos por inferencia. El uso de sesión externa o conector requiere acceso autorizado del docente; disponibilidad se comprueba, no se supone.

## Respaldo propuesto
1. Snapshot consistente de SQLite mediante método soportado por el driver; no copiar a ciegas DB activa y archivos auxiliares.
2. Coordinar snapshot y manifiesto de hashes/versiones de documentos con corte de escrituras o mecanismo equivalente verificable.
3. Guardar documentos, resultados necesarios, versión de esquema y manifiesto sin descartar originales.
4. Comprobar integridad, hashes y referencias antes de marcar éxito.
5. Restaurar en aislamiento; verificar DB y asociaciones PDF/anotaciones antes de sustituir entorno activo con respaldo previo.

Frecuencia, destino, retención, cifrado y objetivos de pérdida/recuperación pendientes. Copia en mismo disco no cubre fallo físico; decidir segundo destino. Probar restauración antes de datos reales. Este documento es diseño, no certificación normativa.

Fuente: [SQLite Backup API](https://sqlite.org/backup.html).
