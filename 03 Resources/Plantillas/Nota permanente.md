<%*
const nombre = await tp.system.prompt("Nombre de la nota");
if (nombre && nombre.trim()) await tp.file.rename(nombre.trim());
-%>
---
tipo: nota-permanente
tema: "<% tp.file.title %>"
fecha: <% tp.date.now("YYYY-MM-DD") %>
estado: activo
fuente: ""
tags:
  - conocimiento
---

# <% tp.file.title %>

## Idea

Escribe una sola idea completa, con tus propias palabras.

## Explicación


## Ejemplo


## Implicación o uso


## Enlaces

- 
