---
tipo: "recurso"
estado: "en-progreso"
categoria: "standards"
proyecto: "Evaluador Académico"
resumen: "Convención de organización de especificaciones"
utilidad: "Organizar, especificar y verificar el desarrollo de la aplicación."
contexto: "Especificaciones vigentes y organización documental basada en fuentes técnicas primarias."
tags: ["proyecto/evaluador-academico", "desarrollo/sdd"]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# Convención de organización de especificaciones

## Qué se adopta

Organización local inspirada en ingeniería de requisitos, arc42, ADR, Spec Kit y OpenSpec. No existe aquí una certificación ISO ni se afirma que las fuentes prescriban estos nombres de carpetas. Se consultaron descripciones públicas de normas; no se realizó una auditoría contra su texto completo. No se instala Spec Kit/OpenSpec ni se promete compatibilidad automática con sus herramientas.

| Categoría | Pregunta | Fuente de verdad |
|---|---|---|
| product | ¿Para quién, para qué y con qué requisitos? | alcance y registro RF/RNF/CA |
| capabilities | ¿Qué capacidades estables debe ofrecer el sistema? | catálogo CAP, flujo transversal y entorno AG/CAG |
| features | ¿Qué porción concreta se entrega y acepta? | una carpeta por feature con spec.md; plan/tasks al iniciar desarrollo |
| architecture | ¿Cómo se estructura y qué restricciones técnicas tiene? | componentes, datos, tecnologías y seguridad |
| contracts | ¿Qué intercambian los componentes? | contrato JSON; futuros esquemas ejecutables en contracts/ de raíz |
| decisions | ¿Por qué se eligió una solución? | registro histórico y un archivo por ADR |
| standards | ¿Qué convenciones aplica el equipo? | organización documental y convenciones de desarrollo |
| verification | ¿Cómo se demuestra cumplimiento y utilidad? | estrategia PR, aceptación y futura evidencia |
| delivery | ¿En qué orden y con qué dependencias? | plan INC y avance global |
| research | ¿Qué fuentes y alternativas sustentan la propuesta? | procedencia y criterios investigados |

## Capacidad frente a feature
CAP identifica una habilidad duradera del producto, por ejemplo preevaluar con agente externo. FEAT identifica una entrega implementable que contribuye a una o varias capacidades, por ejemplo producir e importar un JSON individual. No son sinónimos de carpeta técnica o clase. Las features no sustituyen los RF; enlazan su aceptación para evitar copiar una regla que pueda divergir.

## Ciclo de feature
Cada features/<id-nombre>/spec.md contiene objetivo, capacidad, requisitos, límites, escenarios y dependencias. Al iniciar una feature se generan plan.md (diseño y tareas dependientes) y tasks.md (trabajo verificable). No se crean archivos vacíos ni se inventa un estado implementado. INC del plan global puede cubrir varias features; FEAT no renumera INC.

Una petición de cambio actualiza el spec afectado y registra su decisión; no necesita carpeta changes/ hasta que exista un flujo real que la justifique. Tras implementar, mantener el comportamiento vigente y conservar decisiones superadas. La organización se adapta a este proyecto, sin adoptar simultáneamente dos herramientas SDD.

## Identidad y trazabilidad
IDs existentes RF/RNF, CA, AG/CAG, PR e INC se conservan. Añadir CAP y FEAT para clasificación; ADR para decisiones individuales. Cadena: necesidad → CAP → FEAT → RF/AG → CA/CAG → tareas → PR/evidencia. Una propuesta, una capacidad requerida y una función implementada son estados distintos.

Referencias Markdown relativas para navegar entre archivos; rutas de instrucciones para agentes relativas a raíz del proyecto. Wiki-links con ruta de bóveda cuando se necesiten metadatos. No usar nombre de archivo como identidad de un requisito. Actualizar enlaces al mover y comprobar que sus destinos existen.

## Verificación y validación
Verificación: comprobar requisitos especificados. Validación: comprobar con el docente que el flujo reduce fricción y satisface su necesidad. La carpeta verification reúne ambas para mantener una estructura pequeña, pero los resultados se registran por separado. Compilar o validar JSON no demuestra utilidad pedagógica.

## Registro de reorganización
Se movieron los documentos planos a categorías sin eliminar sus contenidos ni identificadores. Las fuentes y decisiones históricas se preservan; los ADR individuales desarrollan las opciones ya registradas. Las features añadidas son borradores organizativos y no cierran decisiones abiertas. [Investigación y fuentes](../research/organizacion-sdd.md).
