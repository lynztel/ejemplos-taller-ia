---
tipo: proyecto
nombre: "Sistema de preevaluación de entregas de Geografía Económica"
resultado: "Sistema para preevaluar seis entregas y un trabajo final del curso."
area: ""
estado: en-progreso
prioridad: media
fecha_inicio: 2026-10-15
fecha_limite: ""
responsable: ""
resumen: "Proyecto para diseñar un sistema de preevaluación de seis entregas y un trabajo final de Geografía Económica, con ponderaciones y criterios académicos definidos por el docente."
utilidad: "Sirve para organizar la evaluación preliminar del trabajo del alumnado y detectar qué criterios debe revisar el docente antes de asignar calificaciones finales."
contexto: "Curso de nivel superior de Geografía Económica; la nota original indica que el usuario necesita evaluar a sus alumnos durante el curso."
tags:
  - proyecto
  - evaluacion/educacion-superior
relacionado_con: []
proxima_accion: "Definir la rúbrica y los niveles de logro para cada entrega y el trabajo final."
---

# Sistema de preevaluación de entregas de Geografía Económica

## Resultado deseado

Contar con un sistema que permita preevaluar las seis entregas del curso y el trabajo final.

## Contexto y definición de terminado

El proyecto corresponde a un curso de nivel superior de Geografía Económica. Se considerará terminado cuando estén definidos los criterios y la rúbrica de preevaluación y exista un sistema utilizable para las siete entregas. La nota de origen no especifica plataforma, fechas ni niveles de logro.

## Ponderación indicada

| Entrega | Valor |
|---|---:|
| Entregas 1 y 2 | 5% cada una |
| Entregas 3 y 4 | 10% cada una |
| Entregas 5 y 6 | 20% cada una |
| Trabajo final | 30% |

## Elementos que se deben evaluar

- Carátula
- Referencias bibliográficas en formato APA, 7.ª edición
- Análisis estadísticos
- Mapas
- Conclusión

La captura no asigna ponderaciones individuales a estos elementos ni aclara si aplican por igual a cada entrega.

## Próxima acción física

- [ ] Definir una rúbrica con criterios y niveles de logro para las seis entregas y el trabajo final.

## Tareas

- [ ] Aclarar cuáles elementos de evaluación aplican a cada entrega.
- [x] Definir cómo se registrarán las observaciones de preevaluación.

## Registro de avances

### 2026-10-15

- Procesado desde Inbox y organizado como proyecto en PARA.
- Se conservaron las ponderaciones y los elementos indicados en la captura original.
- Decisiones: la rúbrica de la Tarea 1 (9 conceptos, 10 puntos) aplica a las 7 entregas; puntaje libre de 0 al máximo por concepto; trabajos en PDF.
- Creados `rubrica.csv`, el skill `.agents/skills/preevaluar/SKILL.md` (movido después desde `.claude/skills/preevaluar/SKILL.md`), la carpeta `Trabajos sin procesar/` y `dashboard/index.html` (carga `resultados.csv` desde un selector de archivo).
- v2: `AGENTS.md` en la raíz como fuente única de reglas para cualquier agente; el skill remite a él. Creados `alumnos.csv` (`cuenta,nombre`) y la carpeta `Trabajos procesados/`, a donde se mueven los PDF ya preevaluados. `resultados.csv` es la única base de datos, con columnas del agente y columnas del docente (`doc_*`, `calificacion_final`, `nota_docente`, `fecha_docente`). El dashboard permite ver el PDF, ajustar puntajes por concepto y registrar calificación final y notas, escribiendo solo las columnas del docente.
