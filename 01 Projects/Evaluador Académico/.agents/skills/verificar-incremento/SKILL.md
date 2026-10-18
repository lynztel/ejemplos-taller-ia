---
name: verificar-incremento
description: Verificar aceptación de incrementos del Evaluador Académico y registrar evidencia de integridad y revisión docente.
---

# verificar-incremento

Leer ficha del incremento y CA/PR de specs/product/requisitos.md y specs/verification/estrategia-pruebas.md desde la raíz. Contrastar escenarios normales, errores y recuperación. Persistencia: JSON obligatorio, detección automática, validación, SQLite temporal real, idempotencia y rollback; verificar que el entorno académico no tiene acceso directo a DB. Movimientos: conjunto, origen/destino, reintentos, colisiones y cierre sin agente activo. Visor: navegación entre tareas, versión/localización, zoom e histórico individual/global. Puntuación: sugerida, borrador y confirmada. Ejecutar comprobaciones pertinentes; registrar comando, entorno y resultado sin datos sensibles. Informar satisfechos, fallidos y no comprobados. No tratar una prueba prevista como ejecutada ni certificar privacidad por mera existencia de .gitignore.
