# Presentación interactiva de ingresos

El dashboard incorpora la fotografía del BYD Dolphin Mini que compartiste. La presentación tiene cinco escenas navegables —horas, demanda estimada, techo de capacidad, meta de ahorro y rutas de posicionamiento—, con animaciones hechas en Manim Community Edition y navegación de diapositivas de HyperFrames. Los clips y la foto se guardan en `assets/` dentro de esta carpeta para que el deck no dependa de rutas fuera de ella.

## Abrir en el navegador

Desde la raíz del proyecto, abre dos terminales:

```powershell
npx hyperframes present .\presentacion\composition --port 4173 --no-open
```

```powershell
python -m http.server 4174 --bind 127.0.0.1
```

Después abre `http://127.0.0.1:4174/dashboard-clases-ingles.html`. La presentación independiente está en `http://127.0.0.1:4173/`. Para cerrar cada servidor, pulsa `Ctrl+C` en su terminal.

## Supuestos del modelo

- El escenario del dashboard usa 40 horas de trabajo al mes (≈9.2 por semana) como “medio tiempo”, igual que la configuración anterior.
- La comparación añade una media jornada convencional de 20 horas semanales (≈86.7 horas al mes) y tiempo completo definido por la persona usuaria: 8 horas al día × 5 días a la semana (40 horas semanales, ≈173.3 al mes; conversión 52/12).
- La demanda ilustrativa parte de 24 clases al mes a $250 MXN; elasticidad −1 es una hipótesis, no una estimación con ventas observadas. Por eso los tres horarios muestran $6,000 de ingreso bruto con la demanda base.
- El techo de capacidad, si cada hora disponible se vendiera como una clase de una hora, es $10,000 para 40 horas mensuales, ≈$21,667 para media jornada y ≈$43,333 para tiempo completo. No es un pronóstico de ventas.
- Ingresos y techos son brutos; no descuentan impuestos, pago por preparación, cancelaciones ni el costo de internet aún pendiente.
- Las referencias de mercado son precios publicados consultados el 22 de octubre de 2026: [perfil de preparación para entrevistas y CV](https://www.superprof.mx/native-brit-bilingual-spanish-and-english-interview-preparation-and-job-application-assessment-writing-coach-for-tests.html), [curso IELTS del British Council](https://www.britishcouncil.org.mx/ingles/universitarios/preparacion-ielts), [curso corporativo de Wibby](https://wibby.com.mx/cursos-de-ingles-para-negocios/) y [paquetes individuales de BE School](https://beschool.com.mx/es/individuals). No prueban transacciones ni la tarifa que recibiría una docente nueva.

Antes de tomar decisiones, contrasta estas hipótesis con reservas pagadas, asistencia, renovaciones y tiempo real de preparación; un economista debe revisar las recomendaciones.
