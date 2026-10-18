---
name: implementar-incremento
description: Implementar un incremento especificado de la aplicación respetando contratos, autoridad docente y persistencia local.
---

# implementar-incremento

Leer AGENTS.md, specs/standards/convenciones.md y la ficha del incremento desde la raíz. Comprobar aceptación y decisiones relevantes. Implementar casos de uso con dominio independiente de UI/SQLite. El agente académico genera JSON obligatorio sin acceso directo a DB. La aplicación detecta, valida e importa automáticamente sin escribir notas finales ni exigir importación manual por tarea. Mantener registros transaccionales y movimientos reconciliables entre las tres carpetas por conjunto. Implementar traslado al confirmar sin exigir sesión de IA activa. Usar fixtures sintéticos y conservar bytes/IDs aunque cambie la ruta. Ejecutar verificaciones pertinentes disponibles y registrar evidencia. Si cambia el diseño, actualizar especificación y decisión. No marcar verificado sin pruebas reales.
