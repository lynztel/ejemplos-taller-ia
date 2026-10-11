<%*
const nombre = await tp.system.prompt("Nombre de la nota");
if (nombre && nombre.trim()) await tp.file.rename(nombre.trim());
-%>
---
tipo: proyecto
nombre: "<% tp.file.title %>"
resultado: ""
area: ""
estado: en-progreso
prioridad: media
fecha_inicio: <% tp.date.now("YYYY-MM-DD") %>
fecha_limite: ""
responsable: ""
tags:
  - proyecto
---

# <% tp.file.title %>

## Resultado deseado

Describe el entregable observable que marcará el proyecto como terminado.

## Contexto y definición de terminado


## Próxima acción física

- [ ] 

## Hitos

- [ ] 

## Tareas

- [ ] 

## Decisiones

- 

## Recursos y notas relacionadas

- 

## Registro de avances

### <% tp.date.now("YYYY-MM-DD") %>

- 
