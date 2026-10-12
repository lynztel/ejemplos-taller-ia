# AGENTS.md — Manual operativo de MiBiblioteca

Este archivo contiene las instrucciones para cualquier agente que consulte, organice o modifique esta bóveda de Obsidian.

## Propósito

MiBiblioteca es una bóveda demostrativa para un taller de inteligencia artificial aplicada. El público es general y diverso; no se debe asumir una profesión, nivel técnico, sector laboral o área de estudio concreta.

El objetivo es mostrar cómo una persona puede transformar una necesidad cotidiana en una aplicación documentada: capturar, investigar, usar herramientas de IA, verificar, producir un resultado y documentar lo aprendido. Los fundamentos y notas de clase viven en una bóveda externa; no deben replicarse aquí.

Los proyectos de la bóveda son ejemplos didácticos. Deben ser comprensibles para personas que estudian, trabajan o ejercen profesiones distintas.

## Principios obligatorios

### CODE

Aplicar siempre este flujo:

1. **Capture:** registrar primero la información sin exigir una clasificación perfecta.
2. **Organize:** ubicarla en PARA según su utilidad actual.
3. **Distill:** resumir, destacar ideas clave y separar hechos de interpretaciones.
4. **Express:** convertir el conocimiento en una acción, entregable, decisión o explicación útil.

### PARA

Usar exclusivamente estas carpetas principales:

- `00 Inbox`: capturas nuevas y notas pendientes de procesar.
- `01 Projects`: resultados concretos, con un objetivo y una condición de terminado.
- `02 Areas`: conocimiento transversal que se reutiliza entre ejemplos, solo cuando exista una necesidad real de reutilización.
- `03 Resources`: plantillas y fuentes crudas sin procesar.
- `04 Archive`: material inactivo, histórico o pausado.

No crear carpetas principales alternativas ni duplicar la estructura PARA.

## Proyectos demostrativos de IA

- Cada ejemplo completo debe vivir en `01 Projects`.
- Un proyecto debe representar una necesidad o resultado comprensible para público general, no una demostración aislada de una herramienta.
- Cada proyecto debe mostrar: problema, resultado esperado, contexto, herramientas utilizadas, instrucciones o prompts relevantes, fuentes, verificación, entregable y lecciones aprendidas.
- El resultado, el contexto y las notas filtradas que solo sirven para el ejemplo deben estar dentro de la carpeta del proyecto.
- Las fuentes crudas, enlaces, PDFs o recortes todavía no procesados pueden guardarse en `03 Resources/Fuentes crudas`; crear esa subcarpeta solo cuando un proyecto la necesite.
- Una fuente cruda debe enlazarse desde el proyecto que la utiliza; no hace falta convertirla en una nota extensa antes de usarla.
- Si una nota filtrada representa aprendizaje continuo reutilizable, debe vivir en `02 Areas` y enlazarse desde los proyectos.
- Si la nota filtrada solo explica el contexto de un proyecto, debe vivir dentro del proyecto, preferentemente en `Contexto/`.
- No crear áreas de fundamentos, cursos o teoría dentro de esta bóveda. Esos contenidos pertenecen a la bóveda externa.
- Las áreas permitidas deben justificar su reutilización entre varios proyectos. Una biblioteca de prompts es un posible ejemplo, no una carpeta obligatoria.
- La carpeta de cada proyecto debe ser legible como una demostración independiente.

### Estructura recomendada de un ejemplo

```text
01 Projects/
└── Nombre del ejemplo/
    ├── Proyecto.md
    ├── Contexto/
    ├── Fuentes usadas.md
    ├── Trabajo/
    └── Entregable/
```

El archivo `Proyecto.md` funciona como índice didáctico y debe enlazar sus fuentes, áreas, notas de trabajo y entregable.

### Decisión sobre una fuente o nota

1. Si está sin procesar, conservarla en `03 Resources/Fuentes crudas`.
2. Si fue filtrada y solo ayuda a construir el ejemplo, moverla a `Contexto/` dentro del proyecto.
3. Si fue filtrada y será útil para varios ejemplos o para aprendizaje continuo, moverla a `02 Areas`.
4. En todos los casos, enlazarla desde `Proyecto.md`.

## Uso responsable de herramientas de IA

- Documentar qué herramienta se utilizó y para qué etapa.
- Conservar los prompts importantes cuando ayuden a reproducir el ejemplo.
- Verificar hechos, cifras, citas y referencias antes de presentar un resultado.
- Señalar las limitaciones, incertidumbres y posibles errores de la IA.
- No presentar texto generado como investigación verificada sin revisión humana.
- Para temas legales, médicos, financieros o de alto impacto, incluir una advertencia y exigir validación profesional.
- Evitar incluir datos personales, confidenciales o sensibles en prompts o notas de demostración.

## Reglas para notas nuevas

- Toda nota nueva debe crearse en `00 Inbox`.
- No mover automáticamente una captura a otra carpeta solo por su tema; primero determinar su uso actual.
- Si una nota contiene varias ideas independientes, separarlas solo cuando eso mejore su reutilización.
- Mantener un título descriptivo y específico.
- En notas creadas con Templater, utilizar el comando `Templater: Create new note from template`.
- Respetar la plantilla apropiada de `03 Resources/Plantillas`.
- Mantener la cabecera YAML válida y no eliminar campos sin una razón clara.

## Metadatos

Usar, cuando sean pertinentes, estos campos:

```yaml
tipo: nota-permanente
estado: captura
fecha: 2026-10-11
tags:
  - tema/subtema
```

Estados permitidos recomendados: `captura`, `en-progreso`, `activo`, `completado`, `archivado` y `por-revisar`.

Las fechas dinámicas de las plantillas deben utilizar sintaxis de Templater, por ejemplo:

```text
<% tp.date.now("YYYY-MM-DD") %>
```

No sustituirla por `{{date:YYYY-MM-DD}}` cuando la nota vaya a procesarse con Templater.

## Criterios para organizar una nota

- **Proyecto:** existe un resultado concreto que puede darse por terminado. Incluir próxima acción, hitos y fecha límite si aplica.
- **Área:** representa una responsabilidad continua, como `Emprendimiento`, `Estudios de economía`, `Telecomunicaciones` o `Capacitación continua`.
- **Recurso:** contiene información útil como referencia, no necesariamente una acción inmediata.
- **Archivo:** dejó de ser activo, pero puede conservar valor histórico o de consulta.
- **Inbox:** aún requiere decisión, contexto, resumen o enlaces.

## Calidad del conocimiento

- Escribir resúmenes con palabras propias.
- Distinguir claramente entre dato, fuente, inferencia y opinión.
- Añadir enlaces internos con `[[Nombre de nota]]` cuando exista una relación útil.
- Evitar copiar información sin indicar su fuente.
- Para temas actuales, técnicos, legales, económicos o de alto impacto, verificar la vigencia y registrar la fuente y la fecha de consulta.
- Preferir una nota permanente bien consolidada frente a muchas notas repetidas.

## Navegación con contexto limitado

La navegación de la bóveda debe ser **metadata-first** para conservar la ventana de contexto:

1. Comenzar por identificar archivos y carpetas relevantes.
2. Leer primero únicamente la cabecera YAML de cada nota: `tipo`, `estado`, fechas, `tags`, proyecto, área, fuente y demás propiedades disponibles.
3. Usar esos metadatos para filtrar, agrupar y decidir qué notas requieren atención.
4. Leer el cuerpo completo solo de las notas seleccionadas y únicamente en la medida necesaria para completar la tarea.
5. No cargar de forma masiva notas completas ni recorrer toda la bóveda sin un motivo concreto.
6. Si los metadatos son insuficientes, ampliar la lectura de forma incremental y registrar qué información adicional se necesitó.

Cuando sea necesario actualizar una nota, conservar su contenido existente y modificar solo la sección pertinente. Los metadatos no sustituyen la lectura del cuerpo cuando la tarea requiere interpretar argumentos, decisiones o instrucciones específicas; funcionan como primera capa de navegación y selección.

## Protocolo mínimo para procesar Inbox

Una nota no se considera procesada hasta que tenga una descripción breve de su utilidad. El agente debe completar, sin inventar información, esta ficha mínima:

```yaml
tipo: recurso
estado: activo
resumen: "Qué contiene la nota en una frase."
utilidad: "Para qué puede servirme y en qué tipo de petición conviene recuperarla."
contexto: "Curso, proyecto, área o situación de origen."
tags:
  - tema/subtema
relacionado_con:
  - "[[Nota relacionada]]"
proxima_accion: "Revisar, aplicar, convertir en proyecto o dejar como referencia."
```

### Descripción mínima útil

La descripción debe responder en una o dos frases:

- **Qué es:** la idea, dato, decisión, fuente o material que contiene.
- **Para qué sirve:** el problema, proyecto o tipo de consulta en el que sería útil.
- **En qué contexto aplica:** área, curso, proyecto, trabajo o interés relacionado.

No escribir resúmenes genéricos como “notas importantes” o “información útil”. La descripción debe permitir decidir si abrir la nota ante una petición concreta.

### Relaciones entre notas

- Buscar primero notas relacionadas por `tipo`, `tags`, `proyecto`, `area`, `tema` y `fuente`.
- Crear enlaces internos con `[[Nombre de nota]]` cuando exista una relación conceptual, causal, temática o de dependencia.
- Preferir enlaces bidireccionales significativos sobre listas extensas de enlaces.
- Si una nota pertenece a un proyecto o área, enlazarla con esa nota índice aunque el archivo esté en `03 Resources`.
- Añadir una sección `## Relacionado` en el cuerpo cuando la relación necesite una explicación breve.
- No crear enlaces solo para aumentar la cantidad de conexiones.

### Secuencia de procesamiento

1. Leer el YAML y determinar tipo, estado, tema y contexto.
2. Añadir o corregir `resumen`, `utilidad` y `contexto`.
3. Clasificar la nota en `01 Projects`, `02 Areas`, `03 Resources` o `04 Archive`.
4. Identificar entre una y tres notas relacionadas y enlazarlas.
5. Registrar una `proxima_accion` solo si existe una acción real; si no, indicar que queda como referencia.
6. Cambiar `estado` de `captura` a `activo`, `en-progreso`, `por-revisar`, `completado` o `archivado`.
7. Mantener el cuerpo original salvo que sea necesario corregir, resumir o estructurar información.

El resultado mínimo esperado es: **una nota clasificable por metadatos, comprensible por su resumen y conectada con el resto de la bóveda mediante relaciones útiles**.

## Proyectos

Al trabajar en `01 Projects`:

- Describir el resultado deseado y la definición de terminado.
- Identificar una próxima acción física y concreta.
- Vincular el proyecto con su área responsable.
- Registrar decisiones y avances sin sobrescribir el historial.
- Guardar entregables dentro de la carpeta del proyecto o enlazarlos desde allí.

## Seguridad y conservación

- No borrar notas, adjuntos ni carpetas sin autorización explícita.
- No sobrescribir cambios del usuario; revisar primero el contenido existente.
- No mover información fuera de la bóveda sin solicitar autorización.
- No revelar datos personales, documentos privados o credenciales encontrados en la bóveda.
- Mantener los archivos adjuntos en `03 Resources/Adjuntos`, salvo que exista una razón específica para conservarlos junto a un proyecto.
- Si una acción puede producir pérdida de información o modificar muchas notas, detenerse y pedir confirmación.

## Resultado esperado de cada intervención

Al finalizar una tarea, el agente debe indicar brevemente:

1. Qué notas o carpetas creó o modificó.
2. Cómo aplicó CODE y PARA.
3. Qué fuentes utilizó, si investigó información externa.
4. Qué elementos quedaron pendientes de revisión humana.
