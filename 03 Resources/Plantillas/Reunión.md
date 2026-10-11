<%*
const nombre = await tp.system.prompt("Nombre de la nota");
if (nombre && nombre.trim()) await tp.file.rename(nombre.trim());
-%>
---
tipo: reunion
tema: "<% tp.file.title %>"
participantes: []
fecha: <% tp.date.now("YYYY-MM-DD") %>
proyecto: ""
estado: captura
tags:
  - trabajo/reunion
---

# <% tp.file.title %>

## Objetivo


## Puntos tratados

- 

## Decisiones

- 

## Acciones

- [ ] Acción — responsable — fecha

## Seguimiento

### Próxima revisión

- 
