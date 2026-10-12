## Prompt para crear bóveda

```
## Ususario

Describete detalladamente ¿Qué formación tienes? ¿A qué te dedicas? ¿pasatiempos? ¿rutinas de ejercicio y objetivos?, todo lo que quieras documentar.

## Contexto

Plantea todas tus necesidades en base a tu estilo de vida y flujos de trabajo, como; tomar notas te clase, tomar notas rápidas, tomar apuntes a largo plazo, registrar rutinas y progresos, etc.

## Tarea
Crea una bóveda para obsidian, con la metodología de second brain de tiago forte, basado en los principios de CODE en el que vas estructurar las carpetas con el acrónimo PARA:

00-Inbox
01-Projects
02-Areas
03-Resources
04-Archive

Enfocada a satisfacer mis necesidades a partir de mi perfil.

-Vas a generar plantillas con cabecera de meta datos en forma YAML, para:
	- Tomar notas de clase
	- Gestionar proyectos con clientes 
	- Cronogramas
	  .
	  .
	  .
	[Especifica que plantillas te gustaria tener]   
	- Sugiere plantillas que puedan servir para mi perfil
	  
-Genera el archivo AGENTS.md que le indique a los agentes cómo interactuar con la bóveda.
	  
## Restricciones
- Nombre de la bóveda: [Escoge el nombre de tú gusto]
- Cada nota nueva se debe enviar a la carpeta inbox.
- Templater me debe pedir ingresar el nombre de la nota al seleccionar una plantilla.
- Los agentes deben usar los metadatos y enlaces para navegar entre las notas de la bóveda, con el fin de no leer nota por nota y cuidar su ventana de contexto.
- Preguntame lo que no te quede claro.  
```

---

## Ejemplo de prompt para generar presentación

Prompt de ejemplo para mostrar una tarea orquestada por agentes.


```
Vas a hacer una presentación de los resultados de las pruebas pisa, con interpretación enfocada al panorama mexicano, con efectos y repercusiones de impacto económico, a corto y mediano plazo.  
Despliega 4 sub agentes uno experto en investigación, otro experto en estadística descriptiva, un economista experto en interpretación de datos y un experto diseñador de presentaciones académicas animadas.  
Dentro de la bóveda crea la carpeta correspondiente a este proyecto, entrégala en formato de power point.

```

### Prompt mejorado


```
## Objetivo
Producir una presentación académica animada en PowerPoint (.pptx) sobre los resultados de PISA, interpretados para México, con efectos y repercusiones económicas a corto plazo (0-3 años) y mediano plazo (4-10 años). El público es académico y de política pública, con nivel de posgrado en economía. El prompt usa cuatro subagentes en secuencia porque cada etapa depende de los datos verificados de la anterior.

## Contexto
- Trabajas con acceso a mi bóveda de notas y con herramientas de búsqueda web, archivos y subagentes.
- No existe material previo del proyecto. Parte de cero.
- Antes de investigar, determina por búsqueda cuál es la edición PISA más reciente con resultados publicados por la OCDE. Úsala como edición principal y toma la edición anterior como comparación. Declara en la primera diapositiva cuál usaste.

## Estructura de carpeta (créala primero)
[RUTA_DE_LA_BÓVEDA]/PISA-Mexico/
- 00_brief.md (este encargo y las decisiones tomadas)
- 01_investigacion/ (hallazgos y fuentes)
- 02_estadistica/ (tablas CSV y resumen descriptivo)
- 03_economia/ (interpretación económica)
- 04_presentacion/ (PISA_Mexico_Impacto_Economico.pptx)

## Subagentes (ejecutar en este orden; cada uno lee la salida del anterior)

**Subagente 1 — Investigador.** Reúne datos oficiales de PISA para México y comparadores (OCDE, América Latina, países de referencia). Fuentes primarias: informes y bases de la OCDE, INEE/Mejoredu, SEP. Entrega 01_investigacion/hallazgos.md con cada dato acompañado de su fuente y URL, y una lista de vacíos de información.

**Subagente 2 — Estadística descriptiva.** Trabaja solo con los datos del Subagente 1. Calcula puntajes medios por área (matemáticas, lectura, ciencias), distribución por niveles de desempeño, porcentaje bajo el nivel 2, brechas por género y nivel socioeconómico si hay datos, tendencia entre ediciones y distancia frente al promedio OCDE. Respeta los errores estándar publicados. Entrega 02_estadistica/ con CSV, un resumen y las gráficas como imágenes. Indica en cada resultado las condiciones de validez (muestra, comparabilidad entre ediciones, cambios de modalidad).

**Subagente 3 — Economista (interpretación de datos).** Parte de la estadística del Subagente 2. Conecta desempeño PISA con consecuencias económicas usando literatura publicada sobre habilidades cognitivas y crecimiento (por ejemplo Hanushek y Woessmann), productividad laboral, brecha salarial, capital humano, competitividad y nearshoring. Separa explícitamente en cada afirmación: HECHO (dato verificado), INFERENCIA (derivada con método explícito) y CONJETURA. Distingue el corto plazo del mediano plazo, con mecanismos, supuestos y riesgos. Si cuantificas un efecto, muestra la fórmula, los supuestos y el rango de incertidumbre. Entrega 03_economia/interpretacion.md.

**Subagente 4 — Diseñador de presentaciones académicas animadas.** Construye el .pptx con el skill pptx, tomando el contenido de los Subagentes 1 a 3. Longitud: 15 a 18 diapositivas. Flujo: portada, contexto PISA, metodología y límites, resultados de México, comparación internacional, brechas, mecanismos económicos, corto plazo, mediano plazo, riesgos y supuestos, conclusiones, fuentes. Cada gráfica lleva título que enuncia el hallazgo y fuente al pie. Animaciones: transiciones entre diapositivas y entradas progresivas de elementos mediante OOXML, sin exceso ni efectos decorativos. Tipografía legible, contraste adecuado, notas del orador en cada diapositiva.

## Constraints
- NUNCA inventes cifras, citas ni fuentes. Si no hay certeza, escribe "no tengo certeza" o [sin dato] y registra el vacío.
- Todo dato en una diapositiva debe rastrearse a un archivo de 01_investigacion o 02_estadistica.
- Solo haz cambios dentro de PISA-Mexico/. No agregues entregables que no se pidieron.
- No instales dependencias sin avisarme.
- Idioma de todo el material: español de México.

## Acceptance Criteria
- [ ] La carpeta PISA-Mexico/ existe en la bóveda con las cuatro subcarpetas y 00_brief.md
- [ ] El .pptx se abre, tiene entre 15 y 18 diapositivas, notas del orador y animaciones aplicadas
- [ ] Cada cifra del .pptx aparece en los archivos de soporte con su fuente
- [ ] Las afirmaciones económicas están etiquetadas como hecho, inferencia o conjetura
- [ ] Hay diapositivas separadas para corto y mediano plazo
- [ ] Renderizaste las diapositivas a imagen y verificaste que no hay texto cortado ni solapado

## Stop Conditions
Detente y pregunta antes de:
- Eliminar o sobrescribir cualquier archivo existente en la bóveda
- Escribir fuera de PISA-Mexico/
- Continuar si no puedes acceder a datos oficiales de PISA (no los sustituyas con estimaciones)

## Progress
Después de cada subagente: ✅ [qué se hizo] — [archivo(s) creados]
Al final entrega la ruta del .pptx y una lista breve de vacíos de datos o supuestos que requieren mi revisión.

```

**Resultado del prompt:** [[PISA_Mexico_impacto_economico.pptx]]

---

## Prompt de investigación 

**Primer ejemplo:**


```
## Rol: Eres un economista experto en econometría con aplicaciones macroeconómicas

## Contexto
Estas asesorando a un estudiante de economía, que está buscando temas para elaborar una tesis a nivel licenciatura, interesado en aplicaciones al análisis topológico de datos.

## Tarea:
Entregar un listado de propuestas de posibles temas que puedan encajar con los intereses del estudiante.

## Delimitaciones y criterios:
Basarse en el estado del arte del área de investigación con mayor innovación, que le permita realizar un trabajo interesante metologicamente.
Usar exclusivamente fuentes academicas de alto prestigio.
```

### Prompt mejorado


```
<rol>
Eres un economista experto en econometría con aplicaciones macroeconómicas, con dominio de análisis topológico de datos (TDA): homología persistente, Mapper, paisajes e imágenes de persistencia, embeddings de Takens y características topológicas en modelos predictivos.
</rol>

<contexto>
Asesoras a un estudiante de licenciatura en Economía que busca tema de tesis con aplicaciones de TDA. Fecha de referencia: octubre de 2026. Perfil del estudiante: [NIVEL: p. ej. econometría de series de tiempo + R/Python]. Preferencia de datos: [México / global / indiferente].
</contexto>

<tarea>
Propón de 6 a 8 temas de tesis de licenciatura en la frontera del estado del arte de TDA aplicado a macroeconomía, finanzas macro y econometría de series de tiempo. Cada tema debe ser metodológicamente interesante y factible en 6 a 12 meses, con datos públicos y software abierto.
</tarea>

<proceso>
Usa búsqueda web. Antes de redactar, revisa la literatura reciente (prioriza 2020–2026) y verifica cada referencia en la página del editor o por DOI antes de citarla. Identifica brechas reales: combinaciones de técnica TDA y problema macro que estén poco exploradas, no solo las más citadas.
</proceso>

<fuentes>
Permitidas: artículos arbitrados en revistas de alto prestigio de economía, econometría, estadística y matemática aplicada. Ejemplos orientativos, no exhaustivos: Journal of Econometrics, Econometrica, Journal of Business & Economic Statistics, Journal of Applied Econometrics, Journal of Monetary Economics, International Journal of Forecasting, Annals of Applied Statistics, SIAM Journal on Mathematics of Data Science, Journal of Applied and Computational Topology, JMLR. Los working papers de NBER, BIS, BCE, Fed, FMI y Banxico se aceptan solo con la etiqueta [working paper].
Excluidas: blogs, Medium, Wikipedia, prensa, preprints sin etiquetar y contenido generado por IA.
</fuentes>

<formato>
Para cada propuesta, usa exactamente estos campos:
1. Título tentativo
2. Pregunta de investigación (una oración)
3. Brecha en la literatura y por qué es novedosa (2–3 oraciones)
4. Enfoque TDA: técnica específica y objeto que se construye (nube de puntos, filtración, embedding, etc.)
5. Enfoque econométrico y modelo de referencia contra el cual se compara (p. ej. VAR, GARCH, cambio de régimen, modelos de factores)
6. Datos: series, fuente, frecuencia y acceso
7. Software: librerías concretas
8. Factibilidad para licenciatura: Alta / Media / Baja, más el riesgo principal
9. Referencias clave: 2 a 4, con autor, año, revista y DOI/URL
Al final, incluye una tabla comparativa (novedad, factibilidad, riesgo) y recomienda las 2 propuestas con mejor balance, con una justificación breve. Extensión total: 1,800–2,500 palabras.
</formato>

<reglas>
- NUNCA inventes referencias, DOI, cifras ni resultados. Si no pudiste verificar algo, escribe [no verificado] u omítelo.
- En cada propuesta, distingue lo que la literatura ya demostró (hecho), lo que se infiere y lo que es hipótesis de la tesis (conjetura).
- Si un tema tiene pocas fuentes de alto prestigio, dilo explícitamente en lugar de rellenar.
- Tono técnico. Define un término TDA solo si es indispensable, en una línea.
- Sin introducción ni conclusión genéricas.
</reglas>

```
