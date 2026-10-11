# MiBiblioteca

Esta bóveda aplica el método **CODE** de Tiago Forte:

- **Capture:** todo lo nuevo entra primero en `00 Inbox`.
- **Organize:** cada nota madura se mueve según **PARA**.
- **Distill:** resume y destaca lo accionable.
- **Express:** convierte el conocimiento en entregables, decisiones o acciones.

## Estructura PARA

- `00 Inbox`: notas rápidas, ideas, capturas y material pendiente de procesar.
- `01 Projects`: resultados concretos con un objetivo y una fecha de cierre.
- `02 Areas`: responsabilidades permanentes, como emprendimiento, estudios y salud.
- `03 Resources`: temas de referencia, lecturas, cursos y conocimiento reutilizable.
- `04 Archive`: proyectos, áreas o recursos inactivos.

Las plantillas están en `03 Resources/Plantillas`. Para procesar el Inbox, revisa periódicamente cada nota y decide: eliminar, archivar, convertir en tarea o mover a la carpeta PARA adecuada.

## Uso de Templater

Las plantillas utilizan la sintaxis de **Templater**, no la de las plantillas nativas de Obsidian. Al elegir una plantilla, usa el comando `Templater: Create new note from template`. Se abrirá un formulario para escribir el nombre de la nota; Templater usará ese nombre para el archivo, el título y los metadatos.

En Templater configura:

- Carpeta de plantillas: `03 Resources/Plantillas`
- Activar ejecución de JavaScript: debe estar habilitado para que funcione el formulario.

Las fechas se generan con `tp.date.now("YYYY-MM-DD")` en el momento de insertar la plantilla.

## Convenciones sugeridas

- Usa nombres descriptivos y fechas ISO cuando corresponda: `2026-10-10 - Tema`.
- Enlaza notas relacionadas con `[[Nombre de la nota]]`.
- Usa `estado: captura`, `estado: en-progreso`, `estado: activo`, `estado: completado` o `estado: archivado`.
- Mantén una sola fuente de verdad: una idea debe vivir en una nota, no duplicada en varias.
