---
tipo: "recurso"
estado: "activo"
fecha: "2026-10-17"
proyecto: "Evaluador Académico"
resumen: "Contexto original: objetivos, arquitectura propuesta, flujo académico, restricciones y decisiones pendientes."
utilidad: "Guiar la especificación y el desarrollo de la aplicación de evaluación académica."
contexto: "Proyecto local basado en el handoff v1.0 del 17 de octubre de 2026."
tags: ["proyecto/evaluador-academico"]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
proxima_accion: "Cerrar el alcance de la primera versión antes de diseñar la implementación."
---

> Contexto histórico v1.0. La [aclaración funcional del docente](aclaracion-funcional.md) amplía el flujo de conjuntos, visor y movimientos. Se conserva la frontera JSON obligatorio → importador → DB, ratificada posteriormente por el usuario. El texto original se conserva debajo.

# Handoff del Evaluador Académico

Fuente: texto adjunto por el usuario. Se conserva el contenido original a continuación. Es contexto de planeación, no evidencia de que la arquitectura esté implementada.

# HANDOFF — Evaluador Académico Asistido por Agentes de IA

**Versión:** 1.0  
**Fecha:** 17 de octubre de 2026  
**Estado:** Planeación y definición de arquitectura  
**Objetivo del documento:** Transferir el contexto completo del proyecto a otra sesión de ChatGPT para continuar la planeación y generar los artefactos técnicos y visuales necesarios.

---

# 1. Resumen ejecutivo

Se propone desarrollar una aplicación local para que un docente gestione, revise y califique entregas académicas con apoyo de agentes externos de inteligencia artificial.

El sistema separará dos responsabilidades:

1. **Desarrollo del software:** agentes de programación que construyen y mantienen la aplicación siguiendo una metodología de desarrollo guiado por especificaciones, conocida como Spec-Driven Development (SDD).
2. **Operación académica:** agentes de IA que utilizan instrucciones y skills especializadas para preevaluar las tareas de los alumnos conforme a criterios y rúbricas definidos por el docente.

La aplicación permitirá administrar entregas, visualizar documentos PDF, revisar hallazgos de los agentes, agregar anotaciones, ajustar puntuaciones, registrar retroalimentación y consultar estadísticas.

## Principio rector

La IA prepara una preevaluación; el docente conserva la responsabilidad de revisar, modificar y confirmar la calificación final.

## Restricción económica

Se busca aprovechar los agentes y las suscripciones de IA que el docente ya tenga disponibles, en lugar de integrar directamente API de modelos que generen consumo adicional por cada evaluación.

La aplicación debe poder funcionar localmente y mantener los documentos académicos, la base de datos y los resultados dentro de la carpeta del proyecto.

---

# 2. Problema que resolverá la aplicación

El docente necesita procesar múltiples entregas académicas y verificar criterios como:

- Cumplimiento de formato.
- Estructura del documento.
- Presencia y organización de secciones.
- Referencias y fuentes bibliográficas.
- Cumplimiento de requisitos explícitos de la actividad.
- Evidencias documentales asociadas con cada criterio.
- Registro de observaciones y retroalimentación.
- Calificaciones preliminares y definitivas.

No todos los criterios pueden automatizarse con fiabilidad. Por ello, cada criterio deberá clasificarse según su naturaleza:

- **Verificable mecánicamente:** puede comprobarse mediante reglas o código.
- **Preevaluable por IA:** requiere interpretación asistida, pero admite evidencia y revisión.
- **Exclusivamente docente:** exige criterio pedagógico, juicio especializado o decisiones que no deben delegarse al agente.

La clasificación definitiva de los criterios se realizará al definir las rúbricas del proyecto.

---

# 3. Arquitectura conceptual: dos capas de agentes

## 3.1. Capa A — Desarrollo de la aplicación

Su responsabilidad es construir, probar y mantener el software.

Componentes:

- Spec-Driven Development (SDD).
- Especificaciones de requisitos y arquitectura.
- Historias de usuario y criterios de aceptación.
- Archivo `AGENTS.md` con instrucciones generales para agentes que trabajan en el repositorio.
- Skills de desarrollo cuando sean necesarias.
- Código fuente de la aplicación.
- Pruebas automatizadas.
- Documentación técnica.

Resultado: una aplicación funcional, probada y mantenible.

## 3.2. Capa B — Operación académica

Su responsabilidad es procesar las entregas y preparar las preevaluaciones.

Componentes:

- Instrucciones de operación para el agente.
- Archivo `AGENTS.md` en la raíz del repositorio.
- Skills académicas ubicadas en `.agents/skills/`.
- Rúbricas y criterios de evaluación.
- Archivos entregados por los alumnos.
- Esquema JSON de salida.
- Resultados estructurados que la aplicación pueda importar.

Resultado: preevaluaciones documentadas y listas para revisión del docente.

## 3.3. Separación de responsabilidades

| Elemento | Capa de desarrollo | Capa académica |
|---|---|---|
| Agente | Desarrolla el software | Analiza entregas |
| Instrucciones | Ingeniería y mantenimiento | Operación y evaluación |
| Skills | Programación, pruebas y arquitectura | Formato, estructura y fuentes |
| Entrada | Requisitos y código | Entregas y rúbricas |
| Salida | Aplicación funcional | JSON de preevaluación |
| Responsable final | Equipo de desarrollo | Docente |

Las dos capas pueden compartir un repositorio, pero sus instrucciones y responsabilidades deben estar claramente diferenciadas.

**Aclaración terminológica:** `AGENTS.md` es el nombre de un archivo de instrucciones, no una herramienta. SDD es una metodología. Si el usuario se refiere a una herramienta específica llamada `AgentCMD`, debe identificarse exactamente antes de incorporarla a la arquitectura. No asumir que `AgentCMD`, `AGENTS.md` y cualquier herramienta llamada Agent son equivalentes.

---

# 4. Flujo de trabajo operativo

El flujo esperado es el siguiente.

## Fase 1. Preparación

1. El docente descarga las entregas.
2. Coloca los documentos en `data/tareas-sin-procesar/`.
3. La aplicación o un script de preparación identifica las entregas y sus metadatos.
4. Se verifica que existan las rúbricas e instrucciones necesarias.

## Fase 2. Preevaluación asistida

1. El docente abre el repositorio en un entorno de agente compatible.
2. El agente accede al espacio de trabajo donde se encuentran las entregas.
3. Lee las instrucciones aplicables en `AGENTS.md`.
4. Consulta las skills pertinentes en `.agents/skills/`.
5. Analiza las tareas conforme a los criterios autorizados.
6. Produce resultados estructurados en JSON.
7. Los resultados incluyen hallazgos, criterios revisados, evidencias, observaciones y estados de cumplimiento.
8. Se conserva trazabilidad de los archivos analizados y de los resultados producidos.

El agente no debe escribir directamente en SQLite.

## Fase 3. Importación

1. El importador recibe el JSON.
2. Valida su estructura contra un esquema versionado.
3. Comprueba que la entrega y los criterios existan.
4. Rechaza o pone en cuarentena resultados inválidos.
5. Registra los resultados aceptados en SQLite.
6. Actualiza el estado de la entrega.

## Fase 4. Revisión docente

1. El docente abre el dashboard.
2. Consulta el grupo, alumno y entrega.
3. Visualiza el documento PDF.
4. Revisa los criterios y hallazgos de la IA.
5. Contrasta los hallazgos con el documento original.
6. Agrega anotaciones vinculadas con páginas, ubicaciones y criterios.
7. Ajusta puntuaciones y redacta retroalimentación.
8. Confirma la calificación final.

## Fase 5. Cierre y consulta

1. La aplicación registra la calificación final y el historial de cambios.
2. La entrega cambia al estado correspondiente de procesamiento.
3. Se conservan las evidencias y la retroalimentación según las reglas de retención definidas.
4. El dashboard actualiza estadísticas por alumno, grupo y criterio.

## Diagrama textual del flujo

```text
DOCENTE
  |
  v
Descarga de entregas
  |
  v
data/tareas-sin-procesar/
  |
  v
AGENTE EXTERNO
  |
  +--> AGENTS.md
  |
  +--> .agents/skills/
  |
  +--> Rúbricas y criterios
  |
  v
Análisis de documentos
  |
  v
Resultados JSON
  |
  v
IMPORTADOR / BACKEND
  |
  +--> Validación del esquema
  +--> Verificación de referencias
  +--> Manejo de errores
  |
  v
SQLite + almacenamiento de archivos
  |
  v
DASHBOARD DOCENTE
  |
  +--> Revisión del PDF
  +--> Revisión de criterios
  +--> Anotaciones
  +--> Ajuste de puntuación
  +--> Retroalimentación
  |
  v
Confirmación docente
  |
  v
Calificación final + historial + métricas
```

---

# 5. Arquitectura técnica propuesta

## 5.1. Aplicación web local

**Framework candidato:** Astro.

Astro se considera una opción viable, pero la elección todavía no es definitiva. Las partes interactivas pueden implementarse con componentes React si resulta conveniente.

La decisión final debe considerar:

- Complejidad del dashboard.
- Interactividad del visor PDF.
- Gestión de formularios y estados.
- Operaciones locales sobre archivos.
- Integración con SQLite.
- Facilidad de mantenimiento.
- Compatibilidad con el entorno de desarrollo elegido.

No migrar a otro framework sin comparar primero las necesidades reales.

## 5.2. Componentes

### Interfaz

- Dashboard principal.
- Selector de grupos y alumnos.
- Bandeja de entregas.
- Vista de detalle de una entrega.
- Visor PDF.
- Panel de criterios de evaluación.
- Panel de anotaciones.
- Editor de puntuaciones.
- Editor de retroalimentación.
- Vista de historial.
- Panel de estadísticas.

### Servicios de aplicación

- Registro de entregas.
- Gestión de estados.
- Importación de JSON.
- Validación de resultados.
- Gestión de rúbricas y criterios.
- Persistencia de anotaciones.
- Confirmación de calificaciones.
- Consultas de estadísticas.
- Copias de seguridad y restauración.

### Persistencia

**Base de datos candidata:** SQLite.

SQLite será la fuente de verdad para los metadatos estructurados de la aplicación, incluidos los estados, evaluaciones importadas, anotaciones, puntuaciones finales e historial.

Los documentos originales se conservarán como archivos. No es necesario introducirlos completos en la base de datos.

### Visor PDF

**Candidato inicial:** PDF.js.

Debe evaluarse si PDF.js cubre las necesidades de visualización, selección de texto, posicionamiento de comentarios y navegación por páginas.

Las anotaciones deben almacenarse como registros estructurados, no depender exclusivamente de anotaciones incrustadas en el archivo PDF.

Stirling PDF puede considerarse como servicio auxiliar para operaciones de procesamiento documental, pero no se ha decidido utilizarlo como visor principal.

---

# 6. Arquitectura de datos

## 6.1. Entidades principales

El modelo de datos deberá contemplar, como mínimo:

- Alumno.
- Grupo.
- Actividad o tarea.
- Entrega.
- Archivo.
- Rúbrica.
- Criterio de evaluación.
- Ejecución de preevaluación.
- Resultado por criterio.
- Evidencia o hallazgo.
- Anotación.
- Retroalimentación.
- Calificación preliminar.
- Calificación final.
- Historial de cambios.

La estructura definitiva deberá diseñarse antes de implementar las tablas.

## 6.2. Relación entre documentos y datos

```text
Alumno
  └── Entrega
       ├── Archivo original
       ├── Ejecución de preevaluación
       │    └── Resultados por criterio
       ├── Anotaciones
       ├── Retroalimentación
       ├── Calificación preliminar
       ├── Calificación final
       └── Historial de cambios
```

## 6.3. Esquema JSON de preevaluación

El contrato JSON debe diseñarse y versionarse antes de implementar el importador.

Debe permitir representar:

- Versión del esquema.
- Identificador de la entrega.
- Archivo analizado.
- Fecha de procesamiento.
- Agente o entorno que produjo el resultado, cuando sea identificable.
- Criterios revisados.
- Estado de cada criterio.
- Evidencia verificable.
- Página o localización documental, cuando sea posible.
- Observaciones.
- Puntuación sugerida, si la rúbrica lo permite.
- Nivel de confianza o limitaciones, cuando tenga un significado definido.
- Errores o criterios no evaluables.

No asumir que todos los agentes producirán datos fiables por defecto. El importador debe validar los datos, comprobar referencias y manejar campos faltantes o inconsistentes.

---

# 7. Estructura propuesta del repositorio

```text
evaluador-academico/
│
├── AGENTS.md
│
├── .agents/
│   └── skills/
│       ├── preevaluar-formato/
│       │   └── SKILL.md
│       ├── preevaluar-estructura/
│       │   └── SKILL.md
│       └── preevaluar-fuentes/
│           └── SKILL.md
│
├── specs/
│   ├── requirements.md
│   ├── architecture.md
│   ├── data-model.md
│   ├── workflow.md
│   └── acceptance-criteria.md
│
├── data/
│   ├── tareas-sin-procesar/
│   ├── tareas-en-proceso/
│   └── tareas-procesadas/
│
├── database/
│   ├── schema.sql
│   └── evaluador.sqlite
│
├── storage/
│   ├── resultados-json/
│   ├── anotaciones/
│   └── historial/
│
├── src/
│   ├── pages/
│   ├── components/
│   ├── services/
│   ├── database/
│   └── styles/
│
├── scripts/
│   ├── import-results/
│   ├── migrations/
│   └── backups/
│
├── tests/
│
├── .gitignore
├── astro.config.mjs
├── package.json
└── README.md
```

Esta estructura es una propuesta inicial, no un diseño cerrado. Puede cambiar después de elaborar las especificaciones.

## 7.1. Ubicación de los datos

Se decidió favorecer un proyecto local autocontenido.

Las carpetas de tareas, los resultados, las anotaciones y SQLite permanecerán dentro de la raíz del proyecto para facilitar su acceso a la aplicación y a los agentes que trabajen sobre ese espacio de trabajo.

## 7.2. Protección de información

Que los datos estén dentro del repositorio físico no significa que deban versionarse en Git.

El `.gitignore` deberá excluir, como mínimo:

- Entregas académicas reales.
- Datos personales.
- Base de datos local.
- Resultados que contengan información sensible.
- Archivos temporales.
- Copias de trabajo.

La estructura de carpetas puede mantenerse mediante archivos `.gitkeep` cuando sea necesario.

Antes de usar documentos reales, deben probarse las reglas de exclusión, los respaldos y los procedimientos de restauración.

## 7.3. Acceso de agentes externos

Un agente en la nube no necesariamente tiene acceso directo al disco local del docente.

Se deberá confirmar cómo funcionará el entorno concreto:

- Acceso local al repositorio.
- Workspace remoto.
- Copia sincronizada.
- Importación o exportación de archivos.
- Devolución de resultados JSON.

No diseñar el flujo suponiendo que todos los agentes externos pueden leer y escribir en las mismas carpetas locales.

---

# 8. Máquina de estados de una entrega

Los nombres y las transiciones definitivas todavía deben especificarse.

Propuesta inicial:

```text
SIN_PROCESAR
     |
     v
EN_PROCESO
     |
     v
PREEVALUADA
     |
     v
EN_REVISION_DOCENTE
     |
     v
CALIFICADA
     |
     v
PROCESADA
```

Deben definirse las transiciones de error:

- Archivo ilegible.
- Formato no soportado.
- JSON inválido.
- Entrega duplicada.
- Identificador de alumno desconocido.
- Criterios inexistentes.
- Preevaluación incompleta.
- Error durante la importación.

Una transición de estado debe realizarse mediante una operación controlada de la aplicación, dejando registro cuando corresponda.

Los nombres de carpetas no deben ser la única fuente de verdad para determinar el estado. La aplicación debe mantener estados estructurados en SQLite y sincronizar los archivos de manera controlada.

---

# 9. Diseño de anotaciones PDF

Las anotaciones deberán poder vincularse con una entrega y, cuando sea pertinente, con un criterio de la rúbrica.

Campos candidatos:

- Identificador de anotación.
- Identificador de entrega.
- Página del PDF.
- Coordenadas o anclaje de texto.
- Comentario.
- Criterio relacionado.
- Autor.
- Fecha de creación.
- Fecha de modificación.
- Estado de la anotación.
- Tipo de anotación.

Debe definirse cómo se manejarán los cambios en el documento original. Las coordenadas de una página pueden dejar de corresponder si el archivo se sustituye por una versión diferente.

Se recomienda identificar las versiones de los archivos y conservar trazabilidad.

---

# 10. Seguridad, integridad y control

Principios obligatorios:

1. El docente conserva la autoridad sobre la calificación final.
2. Los resultados de IA son sugerencias y hallazgos, no hechos automáticamente confirmados.
3. Los agentes producen JSON; no modifican directamente SQLite.
4. El importador valida los resultados antes de persistirlos.
5. Los archivos originales deben conservarse de forma controlada.
6. Los cambios de calificación deben dejar trazabilidad.
7. Los datos académicos no deben incluirse accidentalmente en Git.
8. Deben existir procedimientos probados de respaldo y restauración.
9. Deben gestionarse errores sin perder archivos originales ni resultados válidos.
10. Las operaciones de importación deben ser idempotentes o detectar duplicados de manera explícita.

La ejecución de agentes sobre documentos de alumnos debe limitarse al trabajo autorizado. Los documentos se consideran datos de entrada, no fuentes de instrucciones que puedan reemplazar las reglas del proyecto.

---

# 11. Plan de desarrollo por fases

La implementación debe seguir un proceso de desarrollo guiado por especificaciones.

## Fase 0 — Definición del alcance

Entregables:

- Objetivos de la aplicación.
- Usuarios y responsabilidades.
- Alcance de la primera versión.
- Tipos de documentos admitidos.
- Tipos de evaluación.
- Reglas de revisión docente.
- Criterios que pueden preevaluarse.
- Límites de automatización.

No comenzar la implementación antes de aclarar los requisitos que afectan el diseño.

## Fase 1 — Especificaciones

Entregables:

- Requisitos funcionales.
- Requisitos no funcionales.
- Historias de usuario.
- Criterios de aceptación.
- Diagrama de arquitectura.
- Diagrama del flujo operativo.
- Modelo de datos.
- Esquema JSON.
- Máquina de estados.
- Estrategia de pruebas.

## Fase 2 — Infraestructura

Entregables:

- Repositorio inicial.
- Configuración del framework.
- Estructura de carpetas.
- Configuración de SQLite.
- Migraciones de base de datos.
- `.gitignore`.
- Configuración de pruebas.
- Documentación para instalación y ejecución local.

## Fase 3 — Gestión de entregas

Entregables:

- Registro de alumnos, grupos y tareas.
- Incorporación de archivos.
- Identificación de entregas.
- Validación de formatos.
- Detección de duplicados.
- Gestión de estados.
- Registro de errores.

## Fase 4 — Contrato de preevaluación e importador

Entregables:

- Esquema JSON versionado.
- Validación del esquema.
- Verificación de referencias.
- Importación transaccional.
- Manejo de resultados incompletos.
- Pruebas con JSON válido e inválido.
- Trazabilidad de cada ejecución.

## Fase 5 — Dashboard docente

Entregables:

- Listado de grupos y alumnos.
- Listado de entregas.
- Filtros por estado.
- Vista de detalle.
- Panel de criterios.
- Consulta de hallazgos y evidencias.

## Fase 6 — Visor PDF y evaluación manual

Entregables:

- Visor PDF.
- Navegación por páginas.
- Anotaciones.
- Vinculación de comentarios con criterios.
- Edición de puntuaciones.
- Retroalimentación.
- Confirmación de calificación final.
- Historial de cambios.

## Fase 7 — Informes y estadísticas

Entregables:

- Calificaciones por alumno.
- Resultados por grupo.
- Resultados por criterio.
- Distribuciones de calificaciones.
- Seguimiento de entregas pendientes.
- Historial de evaluación.

## Fase 8 — Validación final

Entregables:

- Pruebas funcionales.
- Pruebas de importación.
- Pruebas de archivos defectuosos.
- Pruebas de duplicados.
- Pruebas de respaldo y restauración.
- Revisión de privacidad.
- Pruebas de usabilidad.
- Guía de operación para el docente.

Cada fase deberá tener criterios de aceptación explícitos antes de considerarse terminada.

---

# 12. Decisiones pendientes

No presentar las siguientes decisiones como si ya estuvieran cerradas:

1. **Framework:** confirmar Astro o comparar con alternativas según las necesidades del dashboard.
2. **Componentes interactivos:** determinar si se utilizará React u otra solución.
3. **Entorno de agentes:** identificar qué agentes y herramientas concretas se utilizarán.
4. **AgentCMD:** aclarar a qué herramienta se refiere el usuario, si se trata de una herramienta independiente.
5. **Rúbricas:** definir su formato y cómo se versionarán.
6. **JSON:** establecer el esquema definitivo y sus reglas de validación.
7. **Identificación:** decidir cómo se vinculan archivos, alumnos, grupos y actividades.
8. **PDF:** confirmar las capacidades requeridas para las anotaciones.
9. **Autenticación:** determinar si la primera versión será estrictamente local y de un solo usuario.
10. **Respaldo:** definir ubicación, frecuencia y política de conservación.
11. **Estadísticas:** especificar los indicadores necesarios.
12. **Tipos de archivo:** confirmar si la primera versión admite únicamente PDF o también DOCX y XLSX.
13. **Versionado de documentos:** decidir cómo se detectan sustituciones de archivos.
14. **Distribución:** establecer si la aplicación se ejecutará desde un servidor local, una aplicación empaquetada o una interfaz web local.

---

# 13. Instrucciones para continuar en la nueva sesión

Actúa como arquitecto de software y diseñador de sistemas para este proyecto.

Utiliza este documento como contexto de trabajo y respeta las siguientes reglas:

- No inventes decisiones que todavía están pendientes.
- Distingue claramente las decisiones confirmadas de las propuestas.
- Prioriza la seguridad y la trazabilidad de los datos académicos.
- Mantén separadas las instrucciones de desarrollo y las instrucciones de preevaluación.
- No integres API de modelos que generen consumo adicional sin autorización expresa.
- No permitas que el agente de preevaluación escriba directamente en SQLite.
- No des por hecho que un agente en la nube tiene acceso al disco local.
- Diseña primero las especificaciones y los criterios de aceptación.
- Trabaja por fases y presenta un solo bloque de trabajo principal por respuesta.
- No pases a la siguiente fase sin cerrar o identificar explícitamente los pendientes de la fase actual.
- No implementes todavía funciones que dependan de decisiones arquitectónicas no resueltas.
- Genera diagramas editables y artefactos que puedan mantenerse en el repositorio.

## Primer encargo en la nueva sesión

**Construir el mapa visual integral del proyecto en un archivo `.excalidraw`.**

El archivo deberá representar, en un único documento editable y organizado en secciones, lo siguiente:

1. Flujo operativo desde la descarga de entregas hasta la calificación final.
2. Arquitectura lógica de la aplicación.
3. Separación entre la capa de desarrollo y la capa de operación académica.
4. Estructura del repositorio y sus carpetas.
5. Relaciones entre agentes, `AGENTS.md`, skills, rúbricas, JSON, importador, SQLite, documentos y dashboard.
6. Flujo de datos y máquina de estados de las entregas.
7. Modelo conceptual de las entidades principales.
8. Plan de desarrollo por fases.
9. Controles de seguridad, privacidad, validación y respaldo.
10. Decisiones pendientes y dependencias técnicas.

### Requisitos del entregable visual

- Formato nativo de Excalidraw, con extensión `.excalidraw`.
- Elementos editables individualmente; evitar una imagen plana como único contenido.
- Distribución amplia y legible, con jerarquía visual clara.
- Flechas que indiquen el sentido de los flujos.
- Colores consistentes para diferenciar agentes, aplicación, almacenamiento, docente y controles de seguridad.
- Etiquetas en español.
- Sin logos inventados.
- Incluir las decisiones pendientes claramente marcadas.
- Verificar que el archivo se haya creado correctamente y proporcionar un enlace funcional al archivo resultante.

Antes de generar el archivo, comprueba qué herramientas están disponibles en el entorno local y cómo crear o validar un documento Excalidraw compatible. No afirmes que el archivo fue creado si no se ha comprobado su existencia.

Después de entregar el diagrama, continúa con la Fase 0 de las especificaciones del proyecto.
