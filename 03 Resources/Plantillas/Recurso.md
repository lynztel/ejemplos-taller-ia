<%*
const nombre = await tp.system.prompt("Nombre de la nota");
if (nombre && nombre.trim()) await tp.file.rename(nombre.trim());
-%>
---
tipo: recurso
titulo: "<% tp.file.title %>"
autor: ""
fuente: ""
url: ""
fecha_consulta: <% tp.date.now("YYYY-MM-DD") %>
estado: captura
calidad: por-evaluar
tags:
  - recurso
---

# <% tp.file.title %>

## Idea central


## Notas permanentes

- 

## Cómo puedo aplicarlo

- 

## Citas o datos relevantes

> 

## Relacionado con

- 
