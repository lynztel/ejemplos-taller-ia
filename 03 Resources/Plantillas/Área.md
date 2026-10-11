<%*
const nombre = await tp.system.prompt("Nombre de la nota");
if (nombre && nombre.trim()) await tp.file.rename(nombre.trim());
-%>
---
tipo: area
nombre: "<% tp.file.title %>"
responsabilidad: ""
estado: activo
creado: <% tp.date.now("YYYY-MM-DD") %>
revision: mensual
tags:
  - area
---

# <% tp.file.title %>

## Estándar que quiero mantener


## Responsabilidades recurrentes

- [ ] 

## Proyectos relacionados

- 

## Recursos de referencia

- 

## Revisión

### Qué está funcionando

### Qué necesita atención

### Próxima acción

