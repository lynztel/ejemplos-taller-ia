# AGENTS.md

Fuente única de reglas para cualquier agente que trabaje en este proyecto. Todas las rutas son relativas a la carpeta del proyecto.

## Propósito

Preevaluar los trabajos en PDF de Geografía Económica (entregas E1 a E6 y TF). El agente solo produce **precalificaciones**. El docente decide las calificaciones finales en el dashboard. El agente nunca asigna una calificación final.

## Entradas

- `rubrica.csv`: columnas `version,concepto,clave,maximo`. Son los únicos criterios que se pueden aplicar. La misma rúbrica cubre todas las entregas.
- `alumnos.csv`: columnas `cuenta,nombre`. Lista de alumnos que llena el docente. Puede estar vacía.
- `Trabajos sin procesar/*.pdf`: trabajos originales por preevaluar.
- `resultados.csv`: base de datos única de resultados.

## Esquema de resultados.csv

Encabezado exacto, en este orden. Si el archivo no existe, crearlo con solo esta línea:

```
cuenta,alumno,entrega,ruta,rubrica_version,fecha_revision,caratula,contenido,referencias,graficas,analisis,representacion,esquemas,mapas,indicadores,precalificacion,revision_docente,anotaciones,doc_caratula,doc_contenido,doc_referencias,doc_graficas,doc_analisis,doc_representacion,doc_esquemas,doc_mapas,doc_indicadores,calificacion_final,nota_docente,fecha_docente
```

Propiedad de las columnas:

- De `cuenta` a `anotaciones`: las llena el agente.
- `doc_*` (una por concepto), `calificacion_final`, `nota_docente` y `fecha_docente`: el agente las deja **vacías**. Las escribe el docente desde el dashboard.
- El agente **nunca** modifica ni borra filas existentes. Solo agrega filas al final.

## Identificación

1. Nombre esperado del archivo: `<ENTREGA>_<Apellido>_<Nombre>.pdf`, donde `<ENTREGA>` es E1, E2, E3, E4, E5, E6 o TF.
2. Si el nombre no permite identificar al alumno o a la entrega, usar la carátula del PDF.
3. Buscar al alumno en `alumnos.csv` por número de cuenta o por nombre.
   - Coincidencia clara: `cuenta` = cuenta del roster y `alumno` = nombre del roster.
   - Sin coincidencia clara, o con `alumnos.csv` vacío: `cuenta=SIN_IDENTIFICAR`, `alumno` = nombre encontrado en el archivo o `SIN_IDENTIFICAR`, y `revision_docente=si`.
4. `entrega` debe ser E1 a E6 o TF. Si no se puede determinar: `SIN_IDENTIFICAR` y `revision_docente=si`.

## Procesamiento de cada PDF

1. **Omitir los ya evaluados.** Si el nombre del archivo ya aparece en la columna `ruta` de `resultados.csv` (comparando solo el nombre final, sin carpeta), omitirlo y contarlo en el resumen. No volver a evaluarlo ni duplicar filas.
2. **Leer el PDF completo** con Read. Si tiene más de 10 páginas, leerlo por bloques con `pages` y revisar todas las páginas.
3. **Puntuar** cada `clave` con un número entre 0 y su `maximo` (hasta 2 decimales). Basarse solo en lo que contiene el PDF. Las referencias se revisan con APA 7.ª edición.
4. **Conceptos no evaluables** (página o imagen ilegible, información insuficiente): dejar la celda **vacía**, explicar el motivo en `anotaciones` y poner `revision_docente=si`.
5. **Casos dudosos** (posible plagio, archivo que no corresponde a la entrega, identificación incierta y similares): `revision_docente=si` y explicar el motivo.
6. **Nunca inventar** puntajes, nombres, cuentas, fechas ni contenido.
7. `precalificacion` = suma de los 9 conceptos, redondeada a 1 decimal. Vacía si algún concepto está vacío.
8. `anotaciones` con formato `clave: nota | clave: nota | general: nota`, con una justificación corta por concepto. No usar `|` dentro de las notas.
9. `rubrica_version` = valor de la columna `version` de `rubrica.csv`. `fecha_revision` = fecha de hoy en formato `YYYY-MM-DD`.
10. `revision_docente` = `si` o `no`.

## Registro y movimiento

Para cada PDF, en este orden:

1. Decidir el nombre final. Si `Trabajos procesados/<nombre>` ya existe, usar `<nombre base>_2.pdf`, `_3`, y así sucesivamente.
2. Armar la fila con `ruta` = `Trabajos procesados/<nombre final>`.
3. Agregar la fila al final de `resultados.csv`.
4. Mover el PDF de `Trabajos sin procesar/` a `Trabajos procesados/` con el nombre final. No editar ni borrar el PDF.

Si el movimiento falla, no volver a agregar la fila. Informar al docente en el resumen.

## Formato CSV

- Codificación UTF-8. Usar el mismo fin de línea que el archivo existente.
- RFC 4180: encerrar entre comillas dobles cualquier campo que tenga coma, comilla o salto de línea, y duplicar las comillas internas.
- Las filas existentes no se reescriben, reordenan ni corrigen.

## Resumen final

Al terminar, informar:

- Cantidad de PDF procesados.
- Cantidad de PDF omitidos por ya estar evaluados, con sus nombres.
- Filas con `revision_docente=si`, con el motivo de cada una.
- Archivos que no se pudieron mover, si los hubo.

## Reglas

- Usar solo la rúbrica aprobada. No agregar criterios.
- Rotular todo resultado como precalificación.
- Mantener el vínculo entre cada fila y su archivo mediante `ruta`.
- No modificar las columnas que pertenecen al docente.
- No mover ni renombrar archivos distintos de los PDF que se acaban de registrar.

## Dashboard

Para revisar resultados, abrir `dashboard/index.html` en Chrome o Edge y elegir la carpeta del proyecto. El dashboard requiere Chrome o Edge por la File System Access API. Muestra los PDF, permite ajustar puntajes por concepto y registrar la calificación final y las notas. Solo escribe las columnas del docente en `resultados.csv`.
