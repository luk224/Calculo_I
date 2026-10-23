# Dossier 5.3 «Teorema de la función implícita» (U §5.3, pp.204-212)
Páginas: U impresa = PDF+2 (§5.3 empieza en p.204 = PDF 202, confirmado; §5.4 «Valores extremos» empieza en p.212 = PDF 210, confirmado en imagen). E impresa = PDF. X = página PDF de `Examenes-resueltos-Calculo.pdf`. S y L sí tienen derivación implícita, pero solo para una variable (ver §2). Lectura: texto de `ingenieros.txt` con los acentos rotos restaurados tras comprobar la imagen de las páginas PDF 202-210 (impresas 204-212, salvo impresa 204 y 205, leídas solo en texto).

## 1. U §5.3 (pp.204-212)

### 1.1 Motivación y objetivos (p.204, PDF 202)
- 5.3.1 Introducción: «Resolver una ecuación de dos variables es despejar una variable, o expresar una de ellas como función dependiente de la otra variable. A continuación, con el teorema de la función implícita, vamos a dar condiciones en las que podemos asegurar que es posible una generalización de este proceso. Pero este resultado va más allá, porque nos permite derivar la variable expresada como función de las otras variables incluso sin conocer su expresión, en la llamada derivación implícita, que nos va resultar muy útil en gran cantidad de problemas.»
- Orientaciones: «Se recomienda realizar numerosos ejercicios para interiorizar con mayor facilidad el contenido de este apartado.»
- Objetivos: «Comprender el alcance del teorema de la función implícita.» / «Poder derivar implícitamente.»

### 1.2 Motivación con la circunferencia (pp.204-205, PDF 202-203)
- p.204 (PDF 202): «Conocemos muy bien la ecuación de una circunferencia de radio unidad: x² + y² = 1 o x² + y² − 1 = 0.» Con f(x,y) = x² + y² − 1, la circunferencia son los puntos con f(x,y) = 0.
- Puntos: P1 = (√2/2, √2/2): cerca de P1 se despeja y = √(1−x²). P2 = (√2/2, −√2/2): y = −√(1−x²). P3 = (1,0): cerca de P3 no se puede escribir y en función de x («porque por cada valor de x deberíamos tener dos valores de y»), pero sí se puede despejar x = √(1−y²) (fórmula confirmada en imagen, p.207).
- p.205 (PDF 203), Fig. 5.7 (Circunferencia x² + y² = 1): sin ver la imagen (texto).

### 1.3 Ecuación implícita y explícita (p.205, PDF 203)
- Literal: «De forma general, una expresión se llama ecuación implícita cuando toma la forma f(x1, ..., xn) = 0. Normalmente no muestra cómo despejar una variable en función de las otras, ni siquiera sabemos a priori si es posible. Una ecuación explícita es aquella en la que una (también se puede generalizar a varias) de las variables está expresada en función de las otras; si llamamos y = xn a esta variable, entonces la ecuación sería y = y(x1, ..., x_{n−1}).»
- Literal: «Pasar de una ecuación explícita a una implícita es muy sencillo (basta escribir f(x1, ..., xn, y) = y − y(x1, ..., xn) = 0).» Preguntas de U: ¿cuándo podemos pasar de implícita a explícita? ¿En qué intervalo (o conjunto)?
- **Ejemplo 5.10** (p.205, PDF 203): y = x² (parábola) en forma implícita: f(x,y) = x² − y = 0.

### 1.4 Teorema de la función implícita, dos variables (p.206, PDF 204; recuadro en la página)
- Enunciado, literal: «Sea f: D ⊂ ℝ² → ℝ una función continua con derivadas parciales continuas en un abierto D. Sea (a, b) un punto de D con f(a, b) = 0 y ∂f/∂y(a, b) ≠ 0. Entonces existen un intervalo abierto U al que pertenece a, un intervalo abierto V al que pertenece b y una única función g: U → V para los que se cumple que f(x, g(x)) = 0 para x ∈ U. Además, b = g(a) y g es continua y con derivada continua, que cumple dg/dx = dy/dx = −(∂f/∂x)/(∂f/∂y) para todo x ∈ U e y ∈ V.» (imagen confirmada: ≠ 0)
- Consecuencia literal (p.206): «Un primer resultado del teorema de la función implícita es que si la derivada de la función con respecto a y no se anula, entonces podemos despejar y en función de x para escribir y = g(x). Este resultado es válido, cambiando las dos variables (es decir, se puede expresar x en función de y), si ∂f/∂x(a, b) ≠ 0.»

### 1.5 Ejemplo 5.11 (pp.206-207, PDF 204-205)
- f(x,y) = x² + y² − 1: ∂f/∂x = 2x, ∂f/∂y = 2y. Para despejar y hace falta 2y ≠ 0, es decir y ≠ 0: se puede despejar y en (√2/2, √2/2) y en (√2/2, −√2/2), pero no en (1,0). Resultado: x = √(1 − y²).
- Literal (p.207): «Sin embargo, en (1, 0) podemos despejar x en función de y, porque ∂f/∂x(1,0) = 2 · 1 = 2 ≠ 0.» «Se deja como ejercicio encontrar cuándo se puede despejar x.»

### 1.6 Derivación implícita (p.207, PDF 205)
- Literal: «Imaginemos que la ecuación f(x, y) = 0 define a y como función de x en un entorno de (a, b). Entonces, podemos escribir y = y(x) y f(x, y(x)). Aplicamos la regla de la cadena para derivar f y resulta f′ = ∂f/∂x + ∂f/∂y · ∂y/∂x. Como cerca de a se cumple que f(x, y(x)) = 0, también será nula su derivada y así se deduce la relación ∂y/∂x = −(∂f/∂x)/(∂f/∂y) del teorema de la función implícita. Este proceso se llama derivación implícita. Si se dan las condiciones adecuadas, podemos derivar implícitamente una función sucesivas veces.»
- Fórmula clave (equivalente a dy/dx = −F_x/F_y): **dy/dx = −(∂f/∂x)/(∂f/∂y)**, válida si ∂f/∂y ≠ 0 (y se cumplen las hipótesis del teorema). Para F(x,y)=0 con ∂F/∂y ≠ 0.

### 1.7 Ejemplo 5.12: Folium de Descartes (pp.207-210, PDF 205-208; figura 5.8 en p.208)
- Literal (p.207): «Los ceros de la función f(x, y) = x³ + y³ − 3xy definen el Folium de Descartes (hoja de Descartes), curva propuesta en 1638 por Descartes con la ecuación x³ + y³ = 3axy, para un número real a. En la Figura 5.8 se ha representado este conjunto.»
- Derivadas (p.208, PDF 206): ∂f/∂x = 3x² − 3y, ∂f/∂y = 3y² − 3x. Se despeja y en función de x donde ∂f/∂y ≠ 0, es decir x ≠ y². Sustituyendo x = y² en x³ + y³ − 3xy = 0 se obtiene que y se puede escribir en función de x si (x, y) ∉ {(0,0), (∛4, ∛2)}. Análogamente, x en función de y si (x, y) ∉ {(0,0), (∛2, ∛4)} (p.209, PDF 207).
- Literal (p.209): «Resumiendo, para (x, y) ∈ ℝ² \ {(0,0)} se puede despejar una de las variables, porque sólo en (0,0) se anulan las dos derivadas parciales.»
- Derivada primera (p.209, PDF 207): dy/dx = −(3x² − 3y)/(3y² − 3x) = (y − x²)/(y² − x) (válida fuera de los puntos citados).
- Derivación implícita de (5.5), p.209: 3x² + 3y² dy/dx − 3y − 3x dy/dx = 0.
- Derivada segunda (p.210, PDF 208), literal: d²y/dx² = −2 (xy + xy⁴ + x⁴y − 3x²y²) / (y² − x)³.
  (Comprobado a mano por derivación de la ecuación y numéricamente con parametrización del folium en t = 0.5, 1, 1.7, −0.4: coincide con U.)

### 1.8 Curvas de nivel y pendiente de la tangente (p.210, PDF 208)
- Literal: «El teorema de la función implícita y la derivación implícita tienen múltiples aplicaciones. Nos permite, por ejemplo, calcular la pendiente de una curva de nivel. Si tenemos una función z = f(x, y), que cumple las condiciones del teorema de la función implícita, sus curvas de nivel f(x, y) = k definen a una de las variables (supongamos que es y) en función de la otra y así la pendiente de la recta tangente es dy/dx = −(∂f/∂x)/(∂f/∂y).» «Es decir, menos el cociente de primera entre la segunda componente del gradiente en ese punto.»
- Nota marginal de U (p.210): «Recordando que el gradiente es perpendicular a la curva de nivel, este resultado no nos debería sorprender porque un vector perpendicular a ∇f es (1, −(∂f/∂x)/(∂f/∂y)).»

### 1.9 Ejemplo 5.13 (p.210, PDF 208)
- f(x,y) = x² + 3xy − y². Curva de nivel que pasa por (1,0): f(1,0) = 1, k = 1. F(x,y) = x² + 3xy − y² − 1: ∂F/∂x = 2x + 3y, ∂F/∂y = 3x − 2y (distintas de 0 cerca de (1,0)). dy/dx = −(2x + 3y)/(3x − 2y). En (1,0): y(1) = 0 y dy/dx(1) = −2·1/(3·1) = **−2/3**.

### 1.10 Teorema de la función implícita, varias variables (p.211, PDF 209; recuadro)
- Enunciado, literal: «Sea f(x1, ..., xn, z) una función continua definida sobre un abierto D ⊂ ℝ^{n+1} y que toma valores en ℝ, con derivadas parciales continuas en D. Sea (a1, ..., an, b) un punto de D. Supongamos que f(a1, ..., an, b) = 0 y que ∂f/∂z(a1, ..., an, b) ≠ 0. Entonces existe una bola abierta U de (a1, ..., an), un intervalo abierto V de b y una única función g: U → V con derivadas parciales continuas, de tal forma que f(x1, ..., xn, g(x1, ..., xn)) = 0 para todo (x1, ..., xn) ∈ U. Además, z = g(x1, ..., xn) y ∂g/∂xj = ∂z/∂xj = −(∂f/∂xj)/(∂f/∂z) para todo (x1, ..., xn) ∈ U y z ∈ V.»
- Literal (p.211): «Por comodidad, se toma la última variable como la que se escribe en función de las otras. Pero este resultado es válido para cualquiera de ellas, sin más que cambiar z por xj.»
- Nota 3 al pie (p.211): «Este resultado se puede generalizar para funciones f: ℝ^{n+m} → ℝ^m.» (Sin desarrollo en U; no hay sistemas de ecuaciones desarrollados en §5.3.)

### 1.11 Ejemplo 5.14 (pp.211-212, PDF 209-210)
- x² − xy + 3z² = 3. f(x,y,z) = x² − xy + 3z² − 3. ∂f/∂x = 2x − y, ∂f/∂y = −x, ∂f/∂z = 6z.
- f(0,1,1) = 0 y ∂f/∂z(0,1,1) = 6 ≠ 0: existe g en un disco centrado en (0,1) con z = g(x,y). Despejando (p.212, PDF 210): **z = √(1 − (x² − xy)/3)** (confirmado en imagen: raíz cuadrada).
- Derivadas (p.212): ∂z/∂x(0,1) = −(∂f/∂x)/(∂f/∂z)(0,1,1) = **1/6**; ∂z/∂y(0,1) = −(∂f/∂y)/(∂f/∂z)(0,1,1) = **0**.
- Comprobado: derivando z = √(…) da ∂z/∂x(0,1) = 1/6 y ∂z/∂y(0,1) = 0 (numérico).

### 1.12 Inicio de §5.4 (p.212, PDF 210)
- «5.4. Valores extremos / 5.4.1. Motivación» empieza en p.212: fuera de este dossier (ver dossier de 5.4 cuando exista).

Figuras de U en esta sección (recortes candidatos con extraer_figura.py, pág. PDF = impresa − 2): Fig. 5.7 circunferencia x²+y²=1 (p.205, PDF 203; no vista en imagen), Fig. 5.8 folium de Descartes (p.208, PDF 206; vista en imagen, es una gráfica con el lazo en el primer cuadrante).

## 2. S y L: apartado equivalente
- **No hay equivalente del teorema de la función implícita** (en ℝ² ni ℝⁿ): stewart.txt y larson.txt son de una variable. Solo aplica la derivación implícita en una variable (idea de F(x, y(x)) = 0 y derivar).
- S §3.5 «Derivación implícita», pp.209-217 (cabeceras «SECCIÓN 3.5 DERIVACIÓN IMPLÍCITA 209» en PDF 425; p.210 en PDF 429, cabecera «210 CAPÍTULO 3 REGLAS DE DERIVACIÓN»):
  - p.209 (PDF 425), resumen literal: «algunas funciones se definen implícitamente por medio de una relación entre x y y como x² + y² = 25 …» (el texto extraído de S tiene símbolos rotos; el sentido es claro).
  - p.210 (PDF 429), literal: «Por fortuna, no es necesario resolver una ecuación para y en términos de x a fin de hallar la derivada de y. En lugar de ello, aplicaremos el método de derivación implícita. Este método consiste en derivar ambos miembros de la ecuación respecto a x y después resolver la ecuación resultante para y.»
- L §2.5 «Derivación implícita», pp.140-141 (impresa = PDF − 17; PDF 157-158):
  - p.140 (PDF 157), literal: «Sin embargo, algunas funciones sólo se enuncian de manera implícita en una ecuación. Por ejemplo, la función y = 1/x está definida implícitamente por la ecuación xy = 1.»
  - p.141 (PDF 158), «Estrategias para la derivación implícita»: «1. Derive ambos lados de la ecuación respecto de x. 2. Agrupe todos los términos en que aparezca dy/dx en el lado izquierdo de la ecuación y pase todos los demás a la derecha. 3. Factorice dy/dx del lado izquierdo de la ecuación. 4. Despeje dy/dx.»

## 3. E: ejercicios de §5.3 (E 5.23-5.27)
Rango: E 5.23 (p.186, PDF 186) a E 5.27 (pp.190-191, PDF 190-191). **E 5.28 (p.191, PDF 191) ya es §5.4 (extremos absolutos): fuera de este dossier.** E 5.22 termina en p.186 (dossier 5.2 confirmado en imagen).
Subsección de U: todos los ejercicios son de §5.3.2 (teorema de la función implícita y derivación implícita); el reparto fino es: 5.23 → condiciones del teorema (Ej. 5.11); 5.24 → despeje x=g(y) y derivación implícita sucesiva; 5.25 → condiciones del teorema en x y en y; 5.26 → pendiente de curva de nivel (U p.210, Ej. 5.13); 5.27 → versión en ℝ³ (U Ej. 5.14, p.211-212).
Verificado en imagen: E pp.186, 190. Resto en texto, con comprobaciones a mano y numéricas.

**Ejercicio 5.23** (E p.186, PDF 186) [§5.3.2, condiciones del teorema]
«El teorema de la función implícita garantiza que la ecuación x² − xy² + y² = 1 define a y como función implícita de x cerca de: a) (0,1). b) (2,1). c) (−1,0). d) Ninguna de las anteriores.»
Solución impresa: a). Método: para cada punto comprobar f(a,b)=0 y ∂f/∂y(a,b) ≠ 0 con ∂f/∂y = −2xy + 2y = 2y(1−x). (0,1): f=0 y ∂f/∂y = 2 ≠ 0 → válido. (2,1): f = 2 ≠ 0 → no. (−1,0): f = 0 pero ∂f/∂y = 0 → no. (Ver §5 Faltas: errores de notación en la solución impresa.)

**Ejercicio 5.24** (E pp.187-188, PDF 187-188) [§5.3.2, despeje x=g(y) y derivación implícita de 2.º orden]
«Dada la ecuación x⁴ + x²y³ − y² = 1. 1. Muestra que define a x como función implícita de y cerca de (1,1). 2. Calcula g′(1) y g″(1), en donde x = g(y) cerca de (1,1).»
Solución impresa: f(x,y)=x⁴+x²y³−y²−1, ∇f(1,1)=(6,1); ∂f/∂x(1,1)=6≠0 → x=g(y) con dx/dy = −(∂f/∂y)/(∂f/∂x). Para el apartado 2 se deriva (5.1) 4g³g′ + 2gg′y³ + 3g²y² − 2y = 0 en y=1, g=1 → g′(1) = −1/6. Se vuelve a derivar: 12g²g′² + 4g³g″ + 2g′²y³ + 2gg″y³ + 12gg′y² + 6g²y − 2 = 0 → g″(1) = **−43/108**. (Verificado a mano y numéricamente: g′(1) ≈ −0.1666666, g″(1) ≈ −0.3981481 = −43/108.)
Método: derivación implícita sucesiva respecto de y sobre f(g(y),y)=0.

**Ejercicio 5.25** (E pp.188-189, PDF 188-189) [§5.3.2, condiciones del teorema en x y en y]
«Sea la ecuación 3xy − x³ + cos(πy) = 1. Justifica si el teorema de la función implícita garantiza que esta ecuación define a y como función implícita de x cerca de (1,1). ¿Lo garantiza para x como función implícita de y?»
Solución impresa: f(x,y) = 3xy − x³ + cos(πy) − 1; f(1,1) = 0; ∂f/∂y = 3x − π sen(πy), ∂f/∂y(1,1) = 3 ≠ 0 → sí se puede despejar y en función de x. ∂f/∂x = 3y − 3x², ∂f/∂x(1,1) = 0 → el teorema no garantiza despejar x en función de y (sin que eso signifique que no sea posible).
Método: comprobar f(a,b)=0 y las dos derivadas parciales en el punto (1,1).

**Ejercicio 5.26** (E pp.189-190, PDF 189-190) [§5.3.2, pendiente de una curva de nivel]
«Sea f la función dada por f(x,y) = y eˣ − x². ¿Cuál es la pendiente de la recta tangente a la curva de nivel que pasa por (0,1) en ese mismo punto?»
Solución impresa, dos métodos: (1) gradiente perpendicular a la curva de nivel: ∇f(x,y) = (y eˣ − 2x, eˣ), ∇f(0,1) = (1,1); el vector director de la tangente es (1,−1), pendiente **−1**. (2) teorema de la función implícita con F(x,y) = y eˣ − x² − 1 = 0, F(0,1) = 0, ∂F/∂y(0,1) = 1 ≠ 0; dy/dx(0) = −∂F/∂x(0,1)/∂F/∂y(0,1) = −1/1 = **−1**. (Comprobado a mano.)
Método: pendiente = −F_x/F_y (U p.210, Ej. 5.13).

**Ejercicio 5.27** (E pp.190-191, PDF 190-191) [§5.3.2, versión en ℝ³: z = g(x,y)]
«Se considera la función f: ℝ³ → ℝ definida por f(x,y,z) = 1 − e^{(x⁷+y²−xz−1)}. 1. Encuentra el valor de a tal que cerca del punto (1,0,a) la ecuación f(x,y,z) = 0 defina implícitamente una función z = g(x,y). 2. Calcula ∂g/∂x(1,0) y ∂g/∂y(1,0).»
Solución impresa: f(1,0,a) = 1 − e^{−a} = 0 ⇔ a = 0. ∂f/∂z = x e^{(…)} y en (1,0,0) vale 1 ≠ 0 → z = g(x,y) cerca de (1,0,0). Derivando f(x,y,g(x,y)) = 0 (equivale a x⁷+y²−x g−1 = 0): ∂g/∂x(1,0) = **7**, ∂g/∂y(1,0) = **0**. (Comprobado: 7x⁶ − g − x g_x = 0 → g_x(1,0) = 7; 2y − x g_y = 0 → g_y(1,0) = 0.)
Método: teorema con ∂f/∂z ≠ 0 y derivación implícita parcial de x^7+y²−xz−1 = 0.

## 4. X: preguntas de examen relacionadas (función implícita, derivación implícita, tangentes)
Búsqueda por «implícit» (indice_examenes_*.md y examenes.txt). Solo hay dos ejercicios de función implícita propiamente dicha; hay 4 de planos tangentes a gráficas (no implícitas) listados por si se quieren usar con el gradiente.

**Función implícita (derivación implícita y condiciones del teorema)**
- **X p.30-31** (Sept 2012, reserva, Mecánica, Modelo A, Ej. 6, 3 puntos; cabecera según índice, no vista en la página): «Dada la ecuación x⁴ + x²y³ − y² = 1. (a) Demuestre que define a x como función implícita de y en un entorno de (1,1). (b) Si x = g(y), calcule g′(1) y g″(1).» Solución: ∇f(1,1) = (6,1), ∂f/∂x(1,1) = 6 ≠ 0; g′(1) = −1/6; g″(1) = −43/108. Método: el mismo que E 5.24 (derivar dos veces f(g(y),y)=0). Verificado (imagen p.30; solución p.31 en texto). **Erratas**: ver §5.
- **X p.150-151** (Feb 2019, 1ª semana, I. Electrónica Industrial y Automática, P4 corta, 1 punto; vista en imagen p.150 y 151): «Razone si la siguiente afirmación es verdadera o falsa: el teorema de la función implícita para funciones de dos variables garantiza que la ecuación x² + y² = 9 define a y como función implícita de x cerca de (3,0).» Solución: falso. f(x,y)=x²+y²−9, ∂f/∂y = 2y = 0 en (3,0): el teorema no garantiza el despeje de y; (en (3,0) sí se puede despejar x). Método: comprobar ∂f/∂y(a,b) ≠ 0.

**Planos tangentes a gráficas z = f(x,y) (no implícitas; ∇f en un punto; uso de gradiente)**
- X p.100 (Electrónica 1, Ej. 6; texto): f = cos x − xy²: plano tangente en (0,0,1). Solución: ∇f(0,0) = (0,0), plano z = 1.
- X p.127 (sin fecha, I. Electrónica (A), P4 corta; texto): «Calcule la ecuación del plano tangente a la gráfica de f(x,y) = x² + xy en el punto (1,2,3).» Solución: ∇f(x,y) = (2x+y, x), ∇f(1,2) = (4,1), plano 4x + y − z = 3 (texto).
- X p.133 (Sept 2017, P4 corta; texto): plano tangente a f = eˣ(3 sen y + 2) en (0, π/2, 5): z = 5 + 5x (dato del índice).
- X p.138 (Feb 2017, 1ª semana, Ej. 6; texto): plano tangente a f = x²y³/(x⁴+y²) en (1,1,1/2) junto con continuidad en (0,0) (dato del índice; el enunciado completo está en p.138).

## 5. Faltas o dudas
- **E 5.23, solución impresa (p.186, vista en imagen)**: en el apartado (2,1) se escribe ∂f/∂y(−1,0) = 0, cuando debe ser ∂f/∂y(2,1) = −2 ≠ 0; en el apartado (−1,0) se escribe ∂f/∂y(0,1) = 0, cuando debe ser ∂f/∂y(−1,0) = 0 (y ∂f/∂y(0,1) = 2 ≠ 0 se usa para (0,1)). La conclusión (a) es correcta (f(2,1) = 2 ≠ 0 excluye (2,1); en (−1,0) falla la segunda condición).
- **X p.30 (solución, apartado a), leído en imagen**: aparece «dg/dy = dx/dy = (∂f/∂y)/(∂f/∂x)» sin signo menos; la fórmula correcta es dx/dy = −(∂f/∂y)/(∂f/∂x) (fórmula general del teorema, U p.206 y p.211; coincide con E 5.24). El resultado de (b) es correcto.
- **X p.30-31: cabecera (Sept 2012, reserva, Mecánica, Modelo A)** tomada del índice, no vista en la página (PDF 30 empieza con el final del Ej. 5).
- **U p.211 (teorema general)**: el subíndice del numerador de ∂g/∂xj = −(∂f/∂xj)/(∂f/∂z) se lee como «x_j» en la imagen a baja resolución; comprobar en el PDF si importa para el HTML (lo lógico es x_j).
- **U p.204 y p.205** solo leídas en texto (sin imagen). **U p.205**: la Fig. 5.7 (circunferencia) no se ha visto en imagen.
- **Ecuación implícita con varias ecuaciones (sistemas)**: U §5.3 no desarrolla sistemas (solo la nota 3 con f: ℝ^{n+m} → ℝ^m, sin ejemplos). No hay ejercicio de E ni X de sistemas en §5.3.
- **E 5.24-5.27**: solo leídas en texto (E pp.187-189, 191), salvo 5.23 y 5.27 en imagen (E pp.186, 190). Resultados verificados a mano y numéricamente (g′(1), g″(1), dy/dx, ∂g/∂x, ∂g/∂y).
- **Sin equivalente en S/L del teorema**: confirmado (una variable). S §3.5 y L §2.5 cubren solo derivación implícita en una variable.
- **Límites de la sección**: E 5.28 (p.191) es el primer ejercicio de §5.4 (extremos absolutos); U §5.4 empieza en p.212. No se han extraído §5.4 ni §5.5.
