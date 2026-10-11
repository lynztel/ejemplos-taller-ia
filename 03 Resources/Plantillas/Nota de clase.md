<%*
const nombre = await tp.system.prompt("Nombre de la nota");
if (nombre && nombre.trim()) await tp.file.rename(nombre.trim());
-%>
---
tipo: nota-clase
titulo: "<% tp.file.title %>"
materia: ""
curso: ""
institucion: ""
fecha: <% tp.date.now("YYYY-MM-DD") %>
profesor: ""
estado: captura
fuente: clase
tags:
  - estudio/clase
---

# <% tp.file.title %>

## Objetivo de la clase

¿Qué debería poder explicar o resolver al terminar?

## Ideas principales

- 

## Conceptos y definiciones

| Concepto | Explicación en mis palabras | Ejemplo |
|---|---|---|
|  |  |  |

## Desarrollo y fórmulas


## Ejemplo aplicado


## Dudas para investigar

- [ ] 

## Próximas acciones

- [ ] Repasar:
- [ ] Resolver:
- [ ] Consultar:

## Resumen de 5 líneas


## Enlaces

- Relacionado: 
