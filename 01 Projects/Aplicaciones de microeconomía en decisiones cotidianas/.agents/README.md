---
tipo: recurso
estado: activo
resumen: "Mapa operativo del equipo de agentes para apoyar consultorías microeconómicas y sus reglas de coordinación, evidencia y revisión humana."
utilidad: "Ayuda a elegir el agente adecuado, coordinar un encargo de negocio y mantener trazables los datos, supuestos, modelos y entregables."
contexto: "Proyecto [[Aplicaciones de microeconomía en decisiones cotidianas/Proyecto]] de la bóveda MiBiblioteca."
tags:
  - economia/microeconomia
  - inteligencia-artificial/agentes
relacionado_con:
  - "[[Aplicaciones de microeconomía en decisiones cotidianas/Proyecto]]"
proxima_accion: "Usar el coordinador o un especialista para definir y analizar el primer caso de negocio."
---

# Equipo de agentes para consultoría microeconómica

Este directorio contiene instrucciones de rol para un coordinador y agentes especialistas. Su propósito es acelerar tareas de investigación, organización de datos, modelación y preparación de entregables para economistas. No sustituye el criterio profesional: el economista dirige el encargo, resuelve inconsistencias materiales y valida los resultados.

## Modos de interacción

1. **Coordinación:** pedir al coordinador que estructure el encargo, identifique dependencias y encargue en paralelo las investigaciones independientes.
2. **Especialista directo:** pedir a un agente concreto que trabaje un área, como costos, mercado, capacidad productiva o modelación. Si detecta una dependencia crítica con otra área, la explicita.

Para comenzar un encargo, especificar cuando se conozcan: producto y unidad de venta; ubicación y alcance geográfico; tipo de cliente y nicho; canales; período; modelo de negocio y etapa; objetivos y restricciones; capacidad o proceso conocido; moneda y datos disponibles. No bloquear el análisis por datos faltantes: registrar lo pendiente, proponer cómo obtenerlo y separar los escenarios supuestos.

## Mapa de agentes

| Agente | Cuándo usarlo | Archivo |
|---|---|---|
| Coordinador orquestador | Definir el encargo, planear la investigación, coordinar especialistas y consolidar recomendaciones | [[roles/coordinador-orquestador]] |
| Costos y producción | Desglosar insumos, rendimientos, mermas, costos fijos/variables y costo unitario | [[roles/analista-costos-produccion]] |
| Mercado y demanda | Delimitar mercado relevante, clientes, competidores, sustitutos, precios y evidencia de demanda | [[roles/inteligencia-mercado-demanda]] |
| Investigación primaria | Diseñar la obtención de datos faltantes mediante registros, cotizaciones, observación, entrevistas o encuestas | [[roles/investigacion-primaria]] |
| Operaciones, capacidad y personal | Analizar proceso, cuellos de botella, capacidad efectiva, turnos, plantilla y expansión | [[roles/operaciones-capacidad-personal]] |
| Modelación microeconómica | Traducir evidencia a modelos de costos, demanda, precios, beneficios y escenarios | [[roles/modelacion-microeconomica]] |
| Riesgos de insumos y pronósticos | Analizar incertidumbre de costos clave, inflación, shocks de oferta y escenarios futuros | [[roles/riesgos-insumos-pronosticos]] |
| Auditoría de datos y modelos | Revisar trazabilidad, unidades, cálculos, supuestos y contradicciones | [[roles/auditoria-datos-modelos]] |
| Desarrollo analítico y software | Crear herramientas reproducibles cuando una hoja de cálculo, script o tablero añada valor | [[roles/desarrollo-analitico-software]] |
| Orquestador de presentaciones | Planear la fase final de comunicación a partir de análisis validado | [[roles/comunicacion/orquestador-presentaciones]] |
| Diseño de presentaciones | Organizar la narrativa y el diseño de diapositivas para una audiencia definida | [[roles/comunicacion/diseno-presentaciones]] |
| Visualización de datos | Elegir gráficos claros y fieles a datos y modelos | [[roles/comunicacion/visualizacion-datos]] |
| Animación de modelos | Explicar dinámicamente mecanismos económicos, usando herramientas como Manim o Hyperframes si son adecuadas | [[roles/comunicacion/animacion-modelos]] |

## Flujo de trabajo

1. **Definir el encargo:** negocio, pregunta, producto y unidad, geografía, nicho, cliente, horizonte, canales, objetivos, restricciones y estado del negocio.
2. **Inventariar evidencia:** datos que aporta el negocio, fuentes públicas disponibles, unidades y períodos. Mantener los datos originales separados de las transformaciones.
3. **Investigar en paralelo:** costos y producción, mercado y demanda, operaciones y personal, riesgos de insumos. Alinear primero las definiciones compartidas.
4. **Cerrar brechas de información:** proponer fuentes adicionales y métodos de recolección; si se usan hipótesis, etiquetarlas y justificar su plausibilidad.
5. **Construir y comparar modelos:** elegir métodos proporcionales a la evidencia; explorar estrategias compatibles con la filosofía y objetivos del negocio.
6. **Auditar y revisar:** revisar datos, cifras, fórmulas, periodos, supuestos y sensibilidad. El economista corrige o aprueba inconsistencias materiales.
7. **Recomendar:** presentar opciones, condiciones, trade-offs, incertidumbre y datos que podrían cambiar la decisión. No llamar “óptimo” a una opción sin especificar objetivo y restricciones.
8. **Comunicar:** después de la validación profesional, activar la fase de presentación y producir diapositivas, gráficos o animaciones sin alterar los resultados.

## Estándar de evidencia

Clasificar cada insumo relevante como:

- **Dato del negocio:** registros, facturas o información entregada; identificar período y unidad.
- **Dato publicado:** fuente externa verificable, fecha de consulta, geografía, población/unidad y período.
- **Estimación:** cálculo derivado de datos, con fórmula y supuestos.
- **Hipótesis o escenario:** valor supuesto para explorar una posibilidad; explicar por qué es razonable y cómo probarlo.
- **Inferencia o recomendación:** interpretación del análisis; indicar qué evidencia la sostiene y sus límites.

En investigación de competidores, observar precios publicados no equivale a conocer ventas, curvas de demanda ni disposición a pagar. Delimitar qué productos, sustitutos, territorio, cliente y canales se comparan.

## Formato de traspaso entre agentes

Cada agente que entrega trabajo debe devolver: pregunta asignada; mercado y unidad acordados; hallazgos con fuente y fecha; método y transformaciones; supuestos; nivel de confianza y limitaciones; datos faltantes y cómo conseguirlos; contradicciones detectadas; artefactos creados; siguiente decisión o dependencia.

## Uso en Codex

Estas son especificaciones de rol guardadas en la carpeta solicitada. El `AGENTS.md` local del proyecto las hace operativas como instrucciones de enrutamiento y consulta. Codex descubre perfiles propios desde `.codex/agents/` dentro del proyecto o `~/.codex/agents/` del usuario; este directorio `.agents/` no los registra automáticamente. Mantener los roles aquí evita cambiar la configuración global y permite reutilizar sus instrucciones en las tareas del proyecto.
