<%*
const nombre = await tp.system.prompt("Nombre de la nota");
if (nombre && nombre.trim()) await tp.file.rename(nombre.trim());
-%>
---
tipo: curso
nombre: "<% tp.file.title %>"
proveedor: ""
url: ""
fecha_inicio: <% tp.date.now("YYYY-MM-DD") %>
fecha_fin: ""
estado: en-progreso
progreso: 0
prioridad: media
tags:
  - estudio/curso
---

# <% tp.file.title %>

## Propósito

¿Por qué estoy tomando este curso y cómo lo aplicaré?

## Resultado esperado


## Módulos

- [ ] Módulo 1 — 
- [ ] Módulo 2 — 
- [ ] Módulo 3 — 

## Notas relacionadas

- 

## Aplicaciones a mi trabajo o emprendimiento

- 

## Evaluación personal

### Qué aprendí

### Qué todavía no domino

### Siguiente paso

