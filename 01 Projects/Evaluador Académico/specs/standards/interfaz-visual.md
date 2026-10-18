---
tipo: "recurso"
categoria: "standards"
estado: "en-progreso"
proyecto: "Evaluador Académico"
resumen: "Guía visual minimalista del evaluador"
utilidad: "Especificar la consulta de calificaciones y la revisión docente integrada."
contexto: "Propuesta funcional y visual directa del docente en esta conversación."
tags: ["proyecto/evaluador-academico", "producto/interfaz"]
relacionado_con: ["[[01 Projects/Evaluador Académico/specs/README]]"]
---

# Guía visual minimalista del evaluador

## Dirección solicitada

Interfaz minimalista inspirada en Vercel y Cloudflare: jerarquía clara, controles discretos y prioridad a datos, tablas y documento. Referencias estéticas, sin copiar marcas, logotipos ni presuponer uso de sus librerías. No exige Next.js ni cambiar Astro.

## Propuesta de criterios

Fondos neutros, superficies diferenciadas por bordes sutiles, tipografía sans-serif legible, espaciado consistente y un único acento principal de selección/acción. Reservar colores semánticos para pendiente, error y confirmado, siempre con texto/icono. Evitar gradientes decorativos, sombras pesadas y tarjetas repetitivas para información que se compara mejor en una tabla.

Jerarquía: curso/período → conjunto → alumno/entrega. Navegación breve; filtros agrupados, acción principal clara por contexto. Tablas compactas pero legibles, números alineados y encabezados persistentes; notas completas en visor/panel. No reducir texto hasta hacerlo difícil de leer para acomodar más columnas.

Visor flotante: cabecera compacta, documento protagonista y panel de revisión; fondo de página atenuado si se adopta modal. Estados de carga y guardado consistentes. Cambios de tamaño no deben ocultar guardar/cerrar ni confundir sugerencias y notas finales. Tema oscuro queda opcional, no requisito añadido.

## Accesibilidad propuesta para verificar

Objetivo WCAG 2.2 nivel AA en los componentes implementados: contraste medido, foco visible, etiquetas accesibles y operación por teclado. No afirmar conformidad sin comprobaciones. El patrón de diálogo modal debe gestionar foco y cierre; anotaciones no deben depender solo de color o ratón.

## Referencias primarias

- [Geist de Vercel](https://vercel.com/geist/introduction): referencia de sistema visual.
- [Cloudflare Dashboard](https://dash.cloudflare.com/): referencia visual indicada por el usuario; no se verificó su interfaz autenticada ni se atribuyen componentes concretos.
- [W3C: patrón de diálogo modal](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/): foco, teclado y semántica del diálogo.

Aceptación visual en RF-022/CA-022. Tokens concretos de color, tipografía, medidas y componentes se fijarán en diseño de FEAT-004/005 con una vista de muestra; esta nota establece dirección, no un diseño ya aprobado píxel por píxel.

## Aplicación a pantallas

Consultar [wireframes de interfaz](../product/interfaz-wireframes.md) para distribución y adaptación. El acento naranja y acciones principales oscuras del concepto 01 son propuesta visual; colores semánticos conservan texto/ícono. Usar bordes sutiles, tablas legibles y sombras reservadas al visor superpuesto. La normativa funcional prevalece sobre ambigüedades de las imágenes.
