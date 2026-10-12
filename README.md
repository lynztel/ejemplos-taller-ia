# MiBiblioteca — Bóveda demostrativa del taller de IA aplicada

Esta bóveda es un entorno de demostración para un taller de inteligencia artificial aplicada. Está diseñada para un grupo diverso: estudiantes, personas trabajadoras, profesionales del derecho, economía, ingeniería, administración, comunicación y público general.

Aquí se muestran aplicaciones completas, no fundamentos teóricos: plantear una necesidad, investigar, consultar fuentes, usar herramientas de IA, verificar resultados, producir un entregable y documentar el proceso. La teoría y las notas de clase viven en otra bóveda.

La bóveda aplica el método **CODE** de Tiago Forte:

- **Capture:** todo lo nuevo entra primero en `00 Inbox`.
- **Organize:** cada nota madura se mueve según **PARA**.
- **Distill:** resume y destaca lo accionable.
- **Express:** convierte el conocimiento en entregables, decisiones o acciones.

## Estructura PARA

- `00 Inbox`: notas rápidas, ideas, capturas y material pendiente de procesar.
- `01 Projects`: resultados concretos con un objetivo y una fecha de cierre.
- `02 Areas`: conocimiento que conviene conservar y reutilizar entre varios ejemplos, solo cuando exista una necesidad real de reutilización.
- `03 Resources`: plantillas y fuentes crudas sin procesar.
- `04 Archive`: proyectos, áreas o recursos inactivos.

Cada ejemplo completo vive en `01 Projects`. El resultado, el contexto y las notas filtradas que solo sirven para ese ejemplo se guardan dentro del proyecto. Cuando se utilicen fuentes crudas, pueden organizarse en `03 Resources/Fuentes crudas`; si una nota filtrada representa aprendizaje continuo reutilizable, se guarda en `02 Areas` y se enlaza desde los proyectos.

Si el taller necesita una biblioteca de prompts, puede crearse en `02 Areas/Biblioteca de prompts`; no es obligatoria para cada ejemplo.

Las plantillas están en `03 Resources/Plantillas`. Para procesar el Inbox, revisa periódicamente cada nota y decide: eliminar, archivar, convertir en tarea o mover a la carpeta PARA adecuada.

## Cómo leer los ejemplos

1. Abre el proyecto desde `01 Projects`.
2. Revisa su resultado esperado y la próxima acción.
3. Observa las fuentes consultadas y las notas de contexto del proyecto.
4. Revisa qué herramienta de IA se utilizó, qué instrucciones se dieron y cómo se verificó la salida.
5. Consulta el entregable final y las lecciones aprendidas.

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
