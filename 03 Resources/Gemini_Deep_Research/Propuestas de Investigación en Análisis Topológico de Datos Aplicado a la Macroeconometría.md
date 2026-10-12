
## Fundamentos Epistemológicos del Análisis Topológico en Macroeconomía

La macroeconometría empírica contemporánea descansa primordialmente sobre formulaciones estadísticas que asumen geometrías euclidianas, relaciones lineales y propiedades de estacionariedad o cuasi-estacionariedad. Metodologías nucleares en el diseño de política económica —tales como los vectores autorregresivos (VAR), los modelos de factores dinámicos (DFM) y las estructuras autorregresivas con cambio de régimen de Markov (MS-AR)— modelan las interdependencias del sistema económico agregando momentos condicionales de primer y segundo orden. No obstante, las fluctuaciones macroeconómicas generadas por fricciones financieras, perturbaciones en cadenas de suministro y asimetrías de información provocan transiciones discontinuas y configuraciones estructurales complejas que habitan sobre variedades diferenciables (_manifolds_) no lineales de dimensión reducida, inmersas dentro de espacios de fase macroeconómicos de dimensionalidad masiva.

El Análisis Topológico de Datos (TDA, por sus siglas en inglés) proporciona un marco matemático riguroso, arraigado en la topología algebraica, diseñado para recuperar y formalizar la "forma" geométrica de los datos prescindiendo de especificaciones paramétricas restrictivas. A diferencia de los métodos de reducción dimensional basados en proyecciones lineales como el Análisis de Componentes Principales (PCA), el TDA extrae propiedades invariantes frente a transformaciones continuas, cambios de escala y perturbaciones estocásticas moderadas.

El pilar operativo del TDA es la homología persistente, la cual evalúa la evolución de las propiedades de conectividad de un conjunto de datos a lo largo de un espectro continuo de resolución métrica denominado filtración. A través de la construcción de complejos simpliciales anidados (como los complejos de Vietoris-Rips o de Čech), la homología persistente rastrea de manera simultánea el nacimiento y la muerte de clases homológicas asociadas a diferentes dimensiones algebraicas. En dimensión cero ($H_0$), el instrumental topológico captura la agrupación y fragmentación de componentes conexas, identificando la cohesión estructural del sistema analizado. En dimensión uno ($H_1$), cuantifica la presencia de bucles o túneles topológicos, lo que en el contexto de series temporales refleja oscilaciones recurrentes, dinámicas cuasi-periódicas o tensiones estructurales que no logran resolverse de forma estacionaria. En dimensión dos ($H_2$), identifica cavidades o vacíos multidimensionales, indicativos de zonas de exclusión o fallas estructurales de diversificación macroeconómica.

Para acoplar este aparato geométrico con la econometría inferencial, la literatura ha superado la restricción de trabajar con diagramas de persistencia abstractos —los cuales carecen de una métrica euclidiana natural y presentan dificultades para el cálculo de medias de Fréchet unívocas— mediante su funcionalización en espacios de Banach. El desarrollo de los paisajes de persistencia (_persistence landscapes_) de Bubenik permite representar los patrones de persistencia como funciones continuas y derivables en $L^p$, habilitando la estimación de medias empíricas, varianzas, pruebas de hipótesis no paramétricas y la integración directa de normas topológicas como variables explicativas dentro de regresiones dinámicas. La combinación entre el análisis de series de tiempo y el TDA no solo robustece la modelación frente a quiebres estructurales, sino que aporta indicadores adelantados con sustento estructural que optimizan los sistemas de alerta temprana macroeconómica.

## Propuesta 1: Detección Temprana de Recesiones y Ciclos Económicos mediante Reconstrucción de Atractores y Paisajes de Persistencia

### Justificación y Relevancia Macroeconómica

La identificación y anticipación de los puntos de inflexión del ciclo económico constituyen uno de los campos de mayor impacto para la política fiscal y monetaria. Los modelos econométricos tradicionales de alerta temprana, estructurados principalmente sobre modelos Probit dinámicos y modelos autorregresivos con cambio de régimen, suelen fallar al capturar las transiciones abruptas hacia fases contractivas, registrando rezagos sistemáticos en la identificación de quiebres. La contracción económica no ocurre como un choque simétrico lineal, sino como una reorganización profunda en la órbita del sistema económico en su espacio de estados.

Al emplear el Teorema de Incrustación de Retardo de Takens, es factible tomar series temporales univariadas o vectores reducidos de actividad económica y reconstruir el atractor determinista que gobierna la dinámica agregada. Las perturbaciones de régimen alteran la topología intrínseca de este atractor, induciendo colapsos o expansiones en los bucles homológicos ($H_1$). Medir sistemáticamente la deformación del espacio de fases a través de la homología persistente provee una herramienta no supervisada capaz de detectar tensiones acumulativas de estrés cíclico con semanas o meses de anticipación respecto a la confirmación oficial de los comités de fechado de ciclos, como el NBER.

### Instrumental Topológico

La estrategia metodológica comienza transformando una serie de actividad agregada $x_t$ en una nube de puntos inmersa en $\mathbb{R}^m$ mediante la incrustación de Takens:

$$v_t = \left( x_t, \, x_{t+\tau}, \, x_{t+2\tau}, \, \dots, \, x_{t+(m-1)\tau} \right)$$

donde el retardo temporal $\tau$ se determina mediante la primera raíz nula de la función de autocorrelación o el primer mínimo local de la función de información mutua promedio, y la dimensión de inmersión $m$ se parametriza utilizando el algoritmo de falsos vecinos más cercanos (_False Nearest Neighbors_). Sobre ventanas temporales deslizantes de tamaño $W$, se construyen filtraciones de complejos de Vietoris-Rips $VR(P_t, \epsilon)$, calculando las clases de homología persistente para las dimensiones $H_0$ y $H_1$.

Posteriormente, los pares de nacimiento y muerte $(b_i, d_i)$ obtenidos se proyectan sobre paisajes de persistencia, definidos como:

$$\lambda(k, t) = k\text{-max}_{i} \left[ \max\left(0, \min(t - b_i, \, d_i - t)\right) \right]$$

donde $k$ representa el nivel o capa del paisaje. A partir de estas funciones, se calcula la trayectoria temporal de las normas $L^1$ y $L^2$:

$$\Vert{}\lambda\Vert{}_{p, t} = \left( \sum_{k=1}^\infty \int_{-\infty}^\infty \lambda(k, t)^p \, dt \right)^{1/p}$$

así como el centroide temporal ponderado de nacimiento de ciclos, permitiendo generar series macroeconómicas puramente topológicas que capturan la frustración o deformación del atractor.

### Datos y Fuentes

El desarrollo empírico se alimenta de indicadores de alta frecuencia y mensuales disponibles públicamente en la plataforma FRED del Banco de la Reserva Federal de San Luis. La especificación requiere el Índice de Producción Industrial, el diferencial de tasas del Tesoro estadounidense (10 años menos 3 meses), el índice de difusión manufacturero del Institute for Supply Management (ISM) y las nóminas no agrícolas. La variable dependiente binaria de referencia corresponde al indicador oficial de recesión económica determinado por el _National Bureau of Economic Research_ (NBER).

### Contraste Econométrico

La contrastación formal se articula mediante modelos Probit dinámicos y modelos Logit autorregresivos. El modelo base estima la probabilidad condicional de recesión a un horizonte de $h$ periodos, $P(y_{t+h} = 1 \mid \Omega_t)$, fundamentándose exclusivamente en el diferencial de rendimientos de la curva soberana y rezagos del crecimiento industrial.

El modelo propuesto incorpora las innovaciones topológicas:

$$P(y_{t+h} = 1 \mid \Omega_t) = \Lambda\left( \alpha + \sum_{j=1}^p \beta_j y_{t-j+1} + \mathbf{\gamma}^\top \mathbf{X}_t + \theta_1 \Vert{}\lambda\Vert{}_{p, t} + \theta_2 \Delta \Vert{}\lambda\Vert{}_{p, t} \right)$$

donde $\mathbf{X}_t$ es el vector de variables macroeconómicas de control y $\Vert{}\lambda\Vert{}_{p, t}$ representa la norma del paisaje de persistencia en $H_1$. La evaluación de ganancia predictiva se ejecuta mediante divisiones estrictamente cronológicas de la muestra, calculando el Área Bajo la Curva ROC (AUROC), la puntuación de probabilidad de Brier y pruebas de cambio estructural de Bai-Perron para validar si las rupturas topológicas preceden estadísticamente a las contracciones cíclicas formales.

|**Componente Metodológico**|**Enfoque Econométrico Estándar**|**Enfoque Topológico Integrado**|
|---|---|---|
|Configuración de entrada|Series temporales estacionarias univariadas o VAR|Atractor dinámico reconstruido vía Takens ($\mathbb{R}^m$)|
|Hipótesis estructural|Transición gobernada por cadena de Markov lineal|Deformación morfológica y bifurcación en el espacio de fases|
|Indicador clave|Probabilidad filtrada del régimen latente|Norma $L^p$ y momento de la homología persistente $H_1$<br><br>[cite: 10, 12, 15]|
|Métrica de contraste|Log-verosimilitud y criterios AIC/BIC|Ganancia marginal en AUROC y precisión fuera de muestra|

## Propuesta 2: Resiliencia y Contagio en Redes de Insumo-Producto Globales bajo Filtraciones Asimétricas de Dowker

### Justificación y Relevancia Macroeconómica

El estudio de la propagación de perturbaciones a través de cadenas globales de valor y redes de producción es un componente central de la macroeconomía moderna. La literatura canónica, fundamentada en el modelo de Leontief y en medidas estándar de teoría de grafos (densidad, centralidad de grado o intermediación), tiende a analizar las transacciones intersectoriales colapsando la red en enlaces bilaterales independientes. Esta simplificación omite las dependencias circulares complejas de orden superior, las cuales determinan la capacidad de absorción o amplificación de choques de oferta.

La existencia de cavidades homológicas multidimensionales en redes productivas revela la ausencia de vías de sustitución técnica directa o redundancia operativa. Si un choque interrumpe un sector perteneciente a un circuito productivo irreductible, el bloqueo se transmite de forma no lineal al resto de la economía. El análisis topológico permite evaluar la resiliencia estructural de las matrices insumo-producto sin necesidad de simetrizar artificialmente las matrices de coeficientes técnicos, preservando la naturaleza dirigida de las cadenas de suministro.

### Instrumental Topológico

A partir de la matriz de transacciones intersectoriales $T \in \mathbb{R}^{N \times N}$, donde las filas indican los sectores proveedores y las columnas los sectores compradores, se genera una estructura de adyacencia dirigida y fuertemente asimétrica. Para capturar las propiedades topológicas sin forzar simetría euclidiana, se utiliza la formulación de filtración de Dowker para grafos dirigidos ponderados.

La técnica asocia a cada relación de insumo-producto dos complejos simpliciales duales denominados complejo de fuentes (_source complex_) y complejo de sumideros (_sink complex_), parametrizados mediante un umbral de intensidad de flujo comercial $\delta$. Al calcular la homología persistente sobre esta secuencia, se obtienen diagramas de persistencia para dimensiones $H_0$ (fragmentación de agrupamientos industriales autónomos) y $H_1$ (lazos cerrados de dependencia de suministros).

A partir de los diagramas resultantes, se deriva la entropía persistente sectorial:

$$H_t = -\sum_{i=1}^M p_i \ln(p_i), \quad \text{con } p_i = \frac{d_i - b_i}{\sum_{j=1}^M (d_j - b_j)}$$

donde $b_i$ y $d_i$ corresponden a los umbrales de flujo en los que nacen y mueren las cavidades. Una disminución persistente en la entropía de ciclos indica una pérdida crítica de redundancia productiva, concentrando la vulnerabilidad sistémica en cadenas rígidas y cuellos de botella irremplazables.

### Datos y Fuentes

La investigación empírica se apoya en las Matrices Insumo-Producto Interpaíses de la Organización para la Cooperación y el Desarrollo Económicos (OCDE ICIO Tables), complementadas con la base _World Input-Output Database_ (WIOD) y la _Eora Global Supply Chain Database_. Las tablas proporcionan flujos comerciales desagregados para múltiples sectores económicos y economías nacionales. Para las variables macroeconómicas de respuesta, se recopilan series del crecimiento del valor agregado manufacturero y los índices de precios al productor sectoriales.

### Contraste Econométrico

La contrastación empírica evalúa la propagación de choques mediante un modelo autorregresivo espacial y de red (_Spatial/Network Autoregressive Model_, SAR):

$$\mathbf{Y}_t = \rho \mathbf{W} \mathbf{Y}_t + \mathbf{X}_t \mathbf{\beta} + \mathbf{\Gamma} \mathbf{\mathcal{T}}_t + \mathbf{\varepsilon}_t$$

donde $\mathbf{Y}_t$ representa el vector de crecimiento del producto o inflación sectorial, $\mathbf{W}$ es la matriz canónica de coeficientes técnicos de Leontief, $\mathbf{X}_t$ captura controles exógenos macroeconómicos y $\mathbf{\mathcal{T}}_t$ denota el vector de invariantes topológicos obtenidos mediante la homología de Dowker (incluyendo la entropía persistente $H_t$ y el índice de centralidad de ciclo $H_1$).

El ejercicio econométrico consiste en probar la hipótesis nula de que los coeficientes topológicos son conjuntamente nulos ($\mathbf{\Gamma} = \mathbf{0}$). Asimismo, se analiza si las economías o sectores con menor entropía persistente exhiben multiplicadores de choque de precios relativos sustancialmente mayores frente a eventos exógenos de disrupción logística o conflictos geopolíticos.

|**Dimensión Analítica**|**Modelo Insumo-Producto Clásico**|**Modelo Topológico de Dowker**|
|---|---|---|
|Tratamiento de direccionalidad|Matrices insumo-producto ponderadas lineales|Complejos simpliciales de fuentes y sumideros|
|Orden de interacción capturado|Enlaces directos e inversas matriciales ($I-A)^{-1}$|Cavidades cíclicas y túneles de orden superior ($H_1, H_2$)|
|Métrica estructural central|Índices de encadenamiento de Rasmussen-Hirschman|Entropía persistente de red y redundancia homológica|
|Identificación de vulnerabilidad|Sectores con alto volumen bruto transaccional|Cuellos de botella en ciclos sin trayectorias de desvío|

## Propuesta 3: Morfología de la Estructura Temporal de Tasas de Interés y Dinámica de la Política Monetaria

### Justificación y Relevancia Macroeconómica

La estructura temporal de las tasas de interés es una fuente primaria de información sobre las expectativas del mercado respecto a la inflación, el crecimiento del producto y la orientación de la política monetaria. El método de referencia en la literatura para resumir la dinámica de la curva de rendimientos es el modelo dinámico de Nelson-Siegel, parametrizado mediante tres factores interpretados económicamente como nivel, pendiente y curvatura. Sin embargo, en escenarios no convencionales —tales como la presencia del límite inferior cero (_Zero Lower Bound_), operaciones masivas de flexibilización cuantitativa o periodos de inversión atípica de la curva— la geometría de la estructura de plazos experimenta dobleces y compresiones locales que no pueden ser adecuadamente ajustados por combinaciones lineales de funciones exponenciales prefijadas.

Modelar la estructura temporal como una variedad métrica en evolución posibilita rastrear deformaciones morfológicas complejas sin imponer restricciones sobre la curvatura. Estas perturbaciones de la variedad son capaces de advertir tensiones en la prima por plazo (_term premium_) y divergencias en la transmisión de la tasa de política monetaria hacia los instrumentos de largo plazo.

### Instrumental Topológico

Para cada fecha $t$, el vector transversal de rendimientos soberanos a lo largo de $K$ vencimientos define un punto en el espacio euclidiano $\mathbb{R}^K$. Al agregar estas observaciones en ventanas móviles de longitud $L$, se conforma una secuencia de nubes de puntos representativas de la variedad local de tasas. Sobre estas nubes se aplica la homología persistente mediante la filtración de Vietoris-Rips, obteniéndose una secuencia de diagramas de persistencia $D_t$.

Para cuantificar el cambio morfológico entre regímenes de mercado consecutivos o distantes, se computa la distancia de Wasserstein de orden $q$ entre los respectivos diagramas de persistencia:

$$W_q(D_t, D_{t-s}) = \left( \inf_{\gamma: D_t \to D_{t-s}} \sum_{x \in D_t} \Vert{}x - \gamma(x)\Vert{}_\infty^q \right)^{1/q}$$

donde $\gamma$ recorre todas las biyecciones posibles entre los puntos de los diagramas, permitiendo emparejamientos con la diagonal. Esta distancia funcional define una métrica de velocidad geodésica topológica que cuantifica la magnitud de la reconfiguración estructural de la curva. Adicionalmente, el algoritmo Mapper permite generar grafos simplificados que mapean cómo la curva se bifurca en distintos subregímenes bajo el influjo de variables exógenas como la liquidez del balance de la banca central.

### Datos y Fuentes

Las series requeridas comprenden los rendimientos a vencimiento constante del Tesoro de EE. UU. (_Treasury Constant Maturity Rates_ para plazos de 1M, 3M, 6M, 1Y, 2Y, 3Y, 5Y, 7Y, 10Y, 20Y y 30Y) extraídos de la base FRED. Las variables macroeconómicas asociadas incluyen la tasa efectiva de fondos federales, el índice de inflación de precios del gasto en consumo personal (PCE) y los balances totales de la Reserva Federal.

### Contraste Econométrico

La evaluación econométrica contrasta el modelo dinámico de Nelson-Siegel estimado mediante el filtro de Kalman frente a modelos de vectores autorregresivos con umbral (_Threshold VAR_, TVAR) gobernados por topología. La especificación TVAR se formula como:

$$\mathbf{Y}_t = \left( \mathbf{\mu}^{(1)} + \sum_{j=1}^p \mathbf{\Phi}_j^{(1)} \mathbf{Y}_{t-j} \right) \mathbb{I}\left( \Delta W_{q, t} \le \gamma \right) + \left( \mathbf{\mu}^{(2)} + \sum_{j=1}^p \mathbf{\Phi}_j^{(2)} \mathbf{Y}_{t-j} \right) \mathbb{I}\left( \Delta W_{q, t} > \gamma \right) + \mathbf{\varepsilon}_t$$

donde $\mathbf{Y}_t$ incluye la tasa de política, el producto y la inflación, y la variable de transición que define el cambio de régimen estructural es la velocidad de cambio de la distancia de Wasserstein $\Delta W_{q, t}$ con umbral $\gamma$ estimado endógenamente.

El contraste evalúa si la respuesta al impulso de la política monetaria sobre la inflación y el producto exhibe asimetrías estadísticamente más marcadas cuando el cambio de régimen es gobernado por la morfología topológica de la curva que cuando se segmenta mediante la regla usual de inversión de la pendiente tradicional de la curva de rendimientos (10Y menos 2Y).

|**Elemento de Comparación**|**Marco Paramétrico de Nelson-Siegel**|**Marco Topológico Funcional**|
|---|---|---|
|Representación geométrica|Superposición de tres curvas base predefinidas|Nube de puntos y homología en variedad $\mathbb{R}^K$<br><br>[cite: 6, 25]|
|Sensibilidad a regímenes no lineales|Limitada por la forma funcional exponencial|Elevada frente a quiebres en el límite inferior cero|
|Métrica de transición|Variación de los factores latentes $\beta_1, \beta_2, \beta_3$|Distancia de Wasserstein y grafos Mapper|
|Aplicación empírica|Suavizamiento y pronóstico lineal de rendimientos|Detección de bifurcaciones y umbrales en modelos TVAR|

## Propuesta 4: Contagio Financiero Multivariable y Rupturas Estructurales frente al Enfoque de Spillovers de Diebold-Yilmaz

### Justificación y Relevancia Macroeconómica

La transmisión transfronteriza y transectorial del riesgo sistémico representa un foco prioritario para las autoridades macroprudenciales y los bancos centrales. El instrumental dominante en la literatura macroeconométrica es la metodología de derrame de volatilidad (_spillover index_) formulada por Diebold y Yilmaz (2009, 2012), la cual computa el porcentaje de la varianza del error de pronóstico atribuible a innovaciones originadas en otras variables dentro de un modelo VAR multivariado. No obstante, el esquema de Diebold-Yilmaz enfrenta rigideces estructurales: requiere estimar un número cuadrático de parámetros respecto a las variables incluidas, asume simetría en la dinámica interna de las perturbaciones y suele registrar las señales de contagio de manera concomitante o rezagada respecto a la volatilidad implícita.

El análisis homológico de matrices de correlación dinámica ofrece una perspectiva predictiva alternativa. Con anterioridad a los episodios de crisis sistémica, los activos financieros o las variables monetarias experimentan una alineación de trayectorias inducida por la aversión al riesgo y el comportamiento de rebaño de los inversionistas. Esta compresión no necesariamente se manifiesta de inmediato en un incremento en el nivel promedio de la correlación, sino que altera de forma anticipada la geometría de los grupos conexos y destruye de manera selectiva los ciclos homológicos ($H_1$), fenómeno documentado en la física económica como condensación o estrés topológico. Evaluar este proceso supera las debilidades del VAR ante choques sistémicos severos.

### Instrumental Topológico

El proceso metodológico sustituye las matrices de covarianza lineal por un espacio métrico de correlaciones dinámicas. Para un conjunto de $N$ series de rendimientos o diferenciales de riesgo, se obtiene la matriz de correlación condicional $R_t$ a través de ventanas rodantes o mediante modelos DCC-GARCH. La distancia ultramétrica entre las variables $i$ y $j$ se define como:

$$d_{ij}(t) = \sqrt{2(1 - \rho_{ij}(t))}$$

constituyendo un espacio métrico finito $(X_t, d)$ sobre el cual se despliega una filtración de Vietoris-Rips.

A partir de los diagramas de persistencia calculados en cada ventana temporal, se extraen dos métricas complementarias: la norma $L^1$ de los paisajes de persistencia en dimensión uno, y el momentum del nacimiento promedio ponderado de los ciclos homológicos ($d\text{AvgBirth}_t$). El indicador de nacimiento promedio se especifica como:

$$\text{AvgBirth}_t = \frac{\sum_{i: p_i > 0} b_i (d_i - b_i)}{\sum_{i: p_i > 0} (d_i - b_i)}$$

donde $b_i$ y $d_i - b_i$ son el nacimiento y la persistencia del ciclo $i$. Un desplazamiento significativo en el momentum de esta métrica refleja que la red de interdependencia está entrando en una fase de contracción geométrica crítica, generando una señal de alerta previa a la materialización del contagio en los mercados.

### Datos y Fuentes

El marco de datos comprende cotizaciones diarias de los índices sectoriales bursátiles de Estados Unidos y Europa, diferenciales de tasas de swaps de incumplimiento crediticio soberano y bancario (CDS), y tipos de cambio representativos de economías avanzadas y emergentes provistos por el Banco de Pagos Internacionales (BIS) y la plataforma Yahoo Finance API. La muestra temporal se estructura para cubrir episodios de choque internacional: el colapso financiero de 2008, la crisis europea de 2011, la caída por la pandemia de 2020 y el endurecimiento monetario de 2022-2023.

### Contraste Econométrico

La validación empírica compara el contenido informativo marginal de las métricas topológicas frente al índice total de derrames de Diebold-Yilmaz (DY). El primer contraste formal se realiza mediante pruebas de causalidad en el sentido de Granger en media y en varianza, evaluando si el vector de normas topológicas causa al índice DY y a las medidas de volatilidad realizada.

El segundo contraste emplea modelos Logit para la detección de eventos de estrés extremo fuera de muestra:

$$\ln\left( \frac{P(S_{t+h} = 1)}{1 - P(S_{t+h} = 1)} \right) = \alpha + \sum_{k=1}^K \beta_k \text{DY}_{t-k+1} + \sum_{k=1}^K \theta_k \Vert{}\lambda\Vert{}_{1, t-k+1}^{H_1} + \sum_{k=1}^K \delta_k \Delta \text{AvgBirth}_{t-k+1}$$

donde $S_{t+h}$ es una variable indicadora de turbulencia sistémica definida como la realización de la volatilidad en el percentil superior 95. Se analizan la precisión predictiva, los falsos positivos y la ganancia temporal (medida en días o semanas de antelación), contrastando si el marco topológico neutraliza la colinealidad intrínseca que afecta a las estimaciones lineales basadas en el VAR.

|**Criterio de Análisis**|**Índice de Spillover de Diebold-Yilmaz**|**Marco de Homología Persistente**|
|---|---|---|
|Supuesto de interdependencia|Sistema lineal VAR con perturbaciones gaussianas|Geometría no paramétrica de dependencias multivariadas|
|Mecanismo de agregación|Descomposición generalizada de varianza (GFEVD)|Filtración de complejos simpliciales y sumas de persistencia|
|Diagnóstico del riesgo|Derrame neto e interconexión contemporánea|Detección previa de compresión y rigidez estructural|
|Restricción muestral|Rápida pérdida de grados de libertad ante $N$ grande|Invariante a la dimensionalidad; escalable a grandes paneles|

## Propuesta 5: Pronóstico Macroeconómico de Alta Dimensión con FRED-MD Mediante Regularización Topológica

### Justificación y Relevancia Macroeconómica

La macroeconometría orientada a la proyección de variables agregadas opera de forma creciente en entornos de alta dimensión (_big data macroeconomics_), en los cuales el número de series temporales disponibles supera ampliamente el tamaño temporal de las muestras. El protocolo estándar de la literatura —popularizado por Stock y Watson y consolidado mediante bases como FRED-MD elaborada por McCracken y Ng— consiste en comprimir la varianza común de más de un centenar de indicadores mediante Modelos de Factores Dinámicos (DFM) lineales o a través de penalizaciones tipo LASSO y Elastic Net.

A pesar de su eficiencia, estos métodos asumen que las variables macroeconómicas se distribuyen en hiperplanos euclidianos y que la dinámica estructural es invariante a lo largo de los ciclos. Sin embargo, la interacción coordinada entre agregados monetarios, precios y mercado laboral genera configuraciones topológicas en el espacio de estados que varían según la severidad del contexto macroeconómico. Extraer características morfológicas del panel completo e insertarlas en modelos econométricos permite retener la información no lineal sin incurrir en la maldición de la dimensionalidad.

### Instrumental Topológico

En cada momento del tiempo $t$, el corte transversal normalizado de las $K$ series macroeconómicas de FRED-MD representa un punto en un espacio métrico de alta dimensión, conformando una trayectoria temporal de estados económicos. Para transformar esta dinámica en descriptores topológicos compatibles con técnicas de estimación supervisada, se aplican sobre ventanas móviles dos mecanismos de vectorización:

Las curvas de Betti, que corresponden a funciones discretas $\beta_d(\epsilon)$ que computan el conteo de agujeros topológicos en dimensión $d$ en función del radio de filtración $\epsilon$. Las imágenes de persistencia (_persistence images_), las cuales transforman el diagrama de persistencia en una superficie continua mediante la convolución de núcleos gaussianos ponderados por la vida de cada característica homológica, discretizándola posteriormente en una matriz o vector de píxeles estandarizados.

A diferencia de los resúmenes puramente univariados, las imágenes de persistencia preservan la dispersión multiescala de los datos macroeconómicos, transformando configuraciones cualitativas en variables numéricas estructuradas para el análisis econométrico.

### Datos y Fuentes

La fuente empírica exclusiva es la base de datos de investigación macroeconómica mensual FRED-MD, desarrollada por el Banco de la Reserva Federal de San Luis. La base abarca aproximadamente 128 variables agregadas categorizadas en ocho grupos: producto e ingreso, mercado laboral, vivienda, consumo y órdenes, dinero y crédito, tasas de interés y tipos de cambio, precios e índices bursátiles. Como variables diana para el pronóstico se seleccionan la inflación medida por el Índice de Precios al Consumidor (IPC), el deflactor del consumo personal (PCE) y el crecimiento del producto industrial.

### Contraste Econométrico

La evaluación metodológica se formula mediante una arquitectura de Regresión Aumentada por Factores y Topología (_Factor-Augmented Topological Regression_, FATR):

$$Y_{t+h} = \alpha + \sum_{j=1}^p \phi_j Y_{t-j+1} + \sum_{m=1}^M \theta_m \hat{F}_{m, t} + \sum_{r=1}^R \psi_r \Phi_{r, t}^{\text{TDA}} + \varepsilon_{t+h}$$

donde $Y_{t+h}$ es la variable macroeconómica a pronosticar en el horizonte $h$, $\hat{F}_{m, t}$ son los factores lineales tradicionales estimados vía componentes principales estáticos, y $\Phi_{r, t}^{\text{TDA}}$ es el vector regularizado de coeficientes de las imágenes de persistencia o curvas de Betti.

El contraste empírico se evalúa frente a tres especificaciones de referencia: un modelo autorregresivo univariado (AR), el modelo de factores dinámicos clásico (DFM) y un modelo Elastic Net tradicional que emplea directamente el panel de 128 variables. El desempeño se contrasta en un entorno de pronóstico fuera de muestra rodante mediante la Raíz del Error Cuadrático Medio de Pronóstico (RMSFE) y la prueba de Diebold-Mariano para diferencias en precisión predictiva, verificando si las características topológicas reducen de manera estadísticamente significativa los errores durante episodios de alta volatilidad macroeconómica.

|**Modelo Evaluado**|**Estructura de Reducción Dimensional**|**Captura de No Linealidad**|**Regularización Matemática**|
|---|---|---|---|
|AR Benchmark|Ninguna (univariada pura)|Nula|Criterios de información AIC/BIC|
|DFM (Stock & Watson)|Proyecciones lineales vía PCA|Restringida a combinaciones lineales|Ortogonalidad de factores|
|Elastic Net Directo|Selección y contracción de variables|Asume aditividad lineal de regresores|Penalización mixta $L_1$ y $L_2$|
|FATR Propuesto|Híbrida: Factores Lineales + TDA|Alta (representación multiescala de la forma)|Regularización sobre imágenes de persistencia|

## Marco Comparativo de Viabilidad y Especificación Metodológica

El diseño de una investigación de licenciatura requiere compatibilizar la sofisticación analítica con la factibilidad computacional y la disponibilidad de datos de acceso libre. La siguiente matriz resume las cinco propuestas, delimitando su complejidad técnica, las fuentes empíricas y el entorno de software idóneo para su ejecución.

|**Propuesta**|**Complejidad Matemática**|**Herramienta TDA Principal**|**Conjunto de Datos Sugerido**|**Marco Econométrico de Contraste**|**Entorno Computacional**|
|---|---|---|---|---|---|
|**1. Recesiones y Ciclos**|Moderada|Takens Embedding + Paisajes de Persistencia ($H_1$)|FRED (Tasas, Producción, Desempleo)|Probit Dinámico / Markov-Switching AR|Python (`giotto-tda`, `statsmodels`)|
|**2. Redes Insumo-Producto**|Alta|Complejos Asimétricos de Dowker + Entropía|OECD ICIO / WIOD Database|Inversa de Leontief / Modelos SAR en Red|R (`TDAstats`, `igraph`, `spatialreg`)|
|**3. Curva de Rendimientos**|Moderada-Alta|Distancias de Wasserstein / Mapper|FRED (Treasury Yield Curves)|Nelson-Siegel Dinámico / TVP-VAR|Python (`ripser`, `persim`, `scikit-tda`)|
|**4. Contagio Financiero**|Moderada|Filtración Vietoris-Rips sobre Correlaciones|BIS (Divisas) / Mercados Sectoriales|Índice de Spillover Diebold-Yilmaz (VAR)|Python/R (`gudhi`, `vars`)|
|**5. Pronóstico con Fred-MD**|Alta|Imágenes de Persistencia / Curvas de Betti|FRED-MD (Panel Macroeconómico Masivo)|Modelos de Factores Dinámicos / LASSO|Python (`scikit-learn`, `giotto-tda`)|

## Directrices de Implementación y Rigor Econométrico

Para garantizar que la tesis mantenga el estándar exigido en la investigación económica aplicada y evite sesgos metodológicos recurrentes, el estudiante debe estructurar el trabajo bajo tres directrices fundamentales:

### Disciplina de Inferencia y Validación Estadística

Uno de los principales riesgos en el uso de herramientas topológicas radica en derivar interpretaciones causales o estructurales a partir de diagramas meramente descriptivos. Dado que los estimadores topológicos no cuentan en todos los casos con distribuciones asintóticas normales estándar bajo hipótesis nulas de interés económico, resulta indispensable recurrir a métodos de remuestreo computacional. Se deben aplicar pruebas de permutación no paramétricas (_permutation tests_) o esquemas de arranque estocástico (_bootstrap_) basados en remuestreo de bloques temporales. Estas pruebas permiten verificar formalmente si las métricas de persistencia obtenidas a partir de los datos observados son estadísticamente distinguibles de aquellas generadas por procesos nulos lineales, tales como caminatas aleatorias o procesos de ruido gaussiano correlacionado.

### Prevención de la Filtración Temporal (_Look-Ahead Bias_)

En el análisis predictivo de series temporales, el preprocesamiento geométrico introduce riesgos severos de fuga de información si no se maneja estrictamente. La selección de hiperparámetros topológicos —incluyendo el retardo de Takens $\tau$, la dimensión de inmersión $m$, los radios de filtración $\epsilon$ y los parámetros de ponderación de las imágenes de persistencia— debe realizarse de manera recursiva o exclusivamente sobre la ventana de calibración (_in-sample_). De igual modo, la estimación de matrices de distancia debe llevarse a cabo de forma causal sin incluir observaciones futuras, garantizando que el diseño de pronóstico fuera de muestra simule las condiciones informativas reales de un analista o diseñador de política económica.

### Principio de Complementariedad Metodológica

La tesis no debe posicionarse bajo la premisa de descartar los modelos macroeconométricos canónicos en favor del TDA, sino bajo un criterio de ganancia informacional marginal. El objetivo científico radica en demostrar que las invariantes algebraicas del TDA rescatan componentes estructurales y morfologías de red que escapan a los momentos condicionales ordinarios. Al confrontar rigurosamente los modelos aumentados topológicamente contra los mejores modelos de referencia paramétricos de la disciplina, el trabajo de grado obtendrá una doble solidez: la innovación del estado del arte computacional y la validez metodológica demandada por la econometría aplicada.