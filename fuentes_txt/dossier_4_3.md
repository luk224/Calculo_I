# Dossier 4.3 «Derivadas parciales» (U §4.3 pp.168-174; §4.4 pp.175-178; §4.5 pp.179-183)
Páginas: U impresa = PDF+2 (Tema 4 termina en p.183, autoevaluación; p.184 en blanco; Tema 5 empieza en p.185). E impresa = PDF. X = página PDF de Examenes-resueltos-Calculo.pdf (imágenes leídas para verificar).
S y L NO tienen apartado equivalente: ver sección 0. El tema depende de U, E y X.

## 0. Búsqueda en S y L
- **Stewart** (`stewart.txt`): cero aciertos para «derivada parcial», «derivadas parciales», «gradiente», «derivada direccional», «Hessian» (el libro es de una variable; el cap. 14 no está).
- **Larson** (`larson.txt`): el cuerpo del txt cubre hasta la impresa ≈776 (793 págs. PDF − 17). Solo aparecen términos en el índice final (PDF 775-779: «Derivadas parciales, 890», «Gradiente, 1040», «derivada direccional de, 923»), es decir, páginas que no están en el txt. Sin apartado equivalente utilizable.
- Conclusión: el tema depende de U, E y X.

## 1. U §4.3 Derivada parcial. Gradiente (pp.168-174)
- **4.3.1 Motivación p.168**: generalizar la derivada de una variable a funciones de varias variables; objetivos: derivadas parciales como extensión de la derivada y significado geométrico del gradiente.
- **4.3.2 Derivada parcial p.168**: recuerda la derivada de f: I⊂R→R, f'(a)=lím_{h→0}[f(a+h)−f(a)]/h. Para g: D⊂R²→R, D abierto, se generaliza en un punto (a,b)∈D.
- **Def. 4.8 p.169**: «Se llama derivada parcial de g con respecto a x en el punto (a, b) al límite ∂g/∂x(a,b) = lím_{h→0} [g(a+h, b) − g(a,b)]/h, siempre que éste exista.» Observación (p.169): «la derivada parcial de g con respecto a x en (a, b) no es más que la derivada que conocemos para funciones de una variable, donde la función que se deriva es h(x) = g(x, b).» Interpretación (p.169, Fig. 4.15): (1, 0, ∂g/∂x(a,b)) es vector director de la recta tangente a la curva z=g(x,b) en (a,b).
- **Def. 4.9 p.170**: «Se llama derivada parcial de g con respecto a y en el punto (a, b) al límite ∂g/∂y(a,b) = lím_{h→0} [g(a, b+h) − g(a,b)]/h, siempre que éste exista.» Vector (0, 1, ∂g/∂y(a,b)): director de la tangente a la curva z=g(a,y) (intersección con x=a).
- **Notación p.170**: ∂f/∂x, f_x, D₁f (primera variable); ∂f/∂y, f_y, D₂f.
- **Función derivada parcial p.170**: «Diremos que una función tiene derivada parcial con respecto a x (respectivamente a y) en un subconjunto A de su dominio si tiene derivada parcial con respecto a x (resp. a y) en cada uno de los puntos de A.»
- **Ej. 4.22 p.170**: g(x,y)=xy: ∂g/∂x(1,2)=2 y ∂g/∂y(1,2)=1 (cálculo por definición).
- **Cómo calcular p.171**: se deriva tratando la otra variable como constante; sirven reglas y tablas. Maxima: diff(f,x).
- **Ej. 4.23 p.171**: f=x+3yx, g=xe^{x+y}, h=sen(xy²): ∂f/∂x=1+3y, ∂f/∂y=3x; ∂g/∂x=e^{x+y}+xe^{x+y}, ∂g/∂y=xe^{x+y}; ∂h/∂x=cos(xy²)·y², ∂h/∂y=cos(xy²)·2xy.
- **Ej. 4.24 pp.172 (PDF 170)**: f(x,y)=arctg(xy/(x²+y²)) si (x,y)≠(0,0), f(0,0)=0. Es continua fuera del origen; en (0,0) NO es continua (por y=mx el límite es arctg(m/(1+m²)), depende de m), pero **existen las derivadas parciales en (0,0)** y valen 0 (por la definición). Derivadas fuera del origen: ∂f/∂x = y(y²−x²)/((x²+y²)²+x²y²) y simétrica en y (texto del .txt ilegible; fórmula recalculada y comprobada numéricamente).
  - Enseñanza U: derivadas parciales existen aunque f no sea continua (en una variable, derivable ⇒ continua).
- **Funciones de más de dos variables p.173**: ∂f/∂x_k(a1,…,an) = derivada de h(x_k)=f(a1,…,x_k,…,an) en x_k=a_k.
- **Ej. 4.25 p.173**: f=xyz²: ∂f/∂x=yz², ∂f/∂y=xz², ∂f/∂z=2xyz.
- **4.3.3 Gradiente p.173**: «Si una función f de dos variables admite derivadas parciales con respecto a sus dos variables en (a, b), al vector formado por las derivadas parciales lo llamaremos gradiente de f en (a, b) y lo denotaremos por ∇f(a, b).» Fórmula: ∇f(a,b) = (∂f/∂x(a,b), ∂f/∂y(a,b)). En n variables: ∇f(a1,…,an) = (∂f/∂x1(a1,…,an), …, ∂f/∂xn(a1,…,an)) (p.174).
- **Ej. 4.26 p.174**: f=e^{x+y}+arctg(x²+1): ∇f(x,y)=(e^{x+y}+2x/(1+(x²+1)²), e^{x+y}); ∇f(0,0)=(1,1).
- **Gradientes y curvas de nivel p.174**: figura (sin número en el .txt) con vectores gradiente perpendiculares a las curvas de nivel.
- **Propiedad 4.1 p.174**: «El vector gradiente en un punto (a, b) es perpendicular a la curva de nivel que pasa por ese punto.»
- **Ejercicios de autoevaluación p.183 (V/F)**: nº 5 («Hay una relación entre la existencia de la derivada parcial con respecto a una variable y la existencia de la derivada parcial con respecto a otra en un punto»), nº 7 (dominio de ∂f/∂x ⊂ dominio de ∂²f/∂y∂x), nº 9 (derivada en (1,1) según (sen 1, cos 1) de x²+y² positiva), nº 10 (derivadas direccional máxima 0 ⇒ mínima 0 y ∂f/∂x(1,1)=∂f/∂y(1,1)). Respuestas no transcritas (ver E si se necesitan).

## 2. U §4.4 Derivadas de orden superior (pp.175-178)
- **4.4.2 p.175**: ∂f/∂x es una función (derivada parcial primera); si admite derivada parcial en un subconjunto C⊂D, ∂²f/∂x² = ∂/∂x(∂f/∂x) (derivada parcial segunda o de orden dos con respecto a x).
- **p.176 (mixtas)**: «∂²f/∂y∂x = ∂/∂y (∂f/∂x)» y «∂²f/∂x∂y = ∂/∂x (∂f/∂y)». Notación: ∂²f/∂x², f_xx, D₁₁f; ∂²f/∂y∂x, f_xy, D₁₂f (advertencia de U: no hay criterio único de subíndices; fijarse en el formato del autor).
- Derivadas sucesivas de orden superior (p.176); en tres variables hay 9 parciales segundas.
- **Matriz Hessiana p.177**: Hf(a,b) = [[∂²f/∂x²(a,b), ∂²f/∂x∂y(a,b)], [∂²f/∂y∂x(a,b), ∂²f/∂y²(a,b)]] (tabla n×n). U anticipa: el Hessiano dará la información de los puntos críticos (Tema 5).
- **Ej. 4.27 p.177**: f=ln(x²+e^y): ∂f/∂x=2x/(x²+e^y), ∂f/∂y=e^y/(x²+e^y); ∂²f/∂x²=(2e^y−2x²)/(x²+e^y)², ∂²f/∂x∂y=∂²f/∂y∂x=−2xe^y/(x²+e^y)², ∂²f/∂y²=x²e^y/(x²+e^y)²; **Hf(1,0)=[[0, −1/2],[−1/2, 1/4]]** (comprobado numéricamente).
- **Teorema 4.1 (Schwarz) p.178**: «Sea f una función con derivadas parciales continuas en un conjunto abierto D. Si existe ∂²f/∂x∂y en todos los puntos de D y ∂²f/∂x∂y es continua en (a, b) ∈ D, entonces existe ∂²f/∂y∂x(a, b) y además ∂²f/∂y∂x(a, b) = ∂²f/∂x∂y(a, b).»
- **Ej. 4.28 p.178**: sabiendo ∂²f/∂y∂x = sen(xy) continua y las derivadas primeras continuas: ∂²f/∂x∂y(0,1) = sen(0·1) = 0.

## 3. U §4.5 Derivada direccional (pp.179-183; fin del Tema 4)
- **4.5.1 Motivación p.179**: objetivos: calcular derivadas direccionales y relacionar derivada direccional máxima/mínima con el gradiente. «Se recomienda no estudiarlo hasta no tener asimilados los apartados anteriores».
- **4.5.2 p.179 (base canónica)**: e₁=(1,0), e₂=(0,1); derivadas parciales = derivadas en esas direcciones.
- **Def. 4.10 p.179**: «Dados D⊂R², la función de dos variables f: D⊂R²→R y un punto (a,b)∈D definimos la derivada direccional de f en (a,b) en la dirección del vector unitario v=(v₁,v₂) como D_v f(a,b) = lím_{h→0} [f(a+hv₁, b+hv₂) − f(a,b)]/h, siempre que el límite anterior exista.» Con e₁: D_{e₁}f=∂f/∂x; con e₂: D_{e₂}f=∂f/∂y.
- Interpretación geométrica p.180: la recta tangente a la curva intersección de la gráfica con el plano vertical de dirección v tiene vector director (v₁, v₂, D_v f(a,b)).
- **Teorema 4.2 p.180**: «Si una función f admite derivadas parciales cerca de (a, b) y estas derivadas parciales son funciones continuas en (a, b) entonces se verifica D_v f(a,b) = ∇f(a,b)·v, es decir, la derivada según la dirección del vector unitario v en el punto (a, b) coincide con el producto escalar del gradiente en ese punto de f por v.» Generalización a n variables cambiando (a,b) por (a1,…,an).
- Observaciones p.181: la existencia de derivadas parciales continuas es suficiente pero **no necesaria** para tener derivadas direccionales (hay funciones con todas las derivadas direccionales en un punto y parciales no continuas).
- **Ej. 4.29 p.181**: f=x²y+y³, v=(1/√2,1/√2), (1,0): ∇f=(2xy, x²+3y²)=(0,1) ⇒ D_v f(1,0)=1/√2 (verificado).
- **Dirección de máxima variación p.181** (motivación: subir por una montaña por la pendiente más fuerte).
- **Teorema 4.3 p.182**: «Sea f una función que admite derivadas parciales cerca de (a, b) y sean estas derivadas parciales funciones continuas en (a, b). 1. Si el gradiente de f en (a, b) es distinto del vector nulo, entonces: La derivada direccional máxima de f en (a, b) se obtiene en la dirección del gradiente, es decir, del vector ∇f(a,b)/‖∇f(a,b)‖, y su valor es ‖∇f(a,b)‖. La derivada direccional mínima de f en (a, b) se obtiene en la dirección del vector opuesto al gradiente, es decir, del vector −∇f(a,b)/‖∇f(a,b)‖, y su valor es −‖∇f(a,b)‖. 2. Si el gradiente de f en (a, b) es el vector nulo, entonces todas las derivadas direccionales coinciden y son nulas.» Resumen de U: la función crece más rápido en el sentido del gradiente y decrece más rápido en el opuesto.
- **Ej. 4.30 p.182**: f=x²−y²+z en (1,1,1): ∇f=(2x,−2y,1)=(2,−2,1); máximo en (2/3, −2/3, 1/3) con valor 3; mínimo en (−2/3, 2/3, −1/3) con valor −3.

## 4. E Tema 4.3-4.5: ejercicios 4.25 a 4.44
Mapa a U: 4.3 → E 4.25-4.34 · 4.4 → E 4.35-4.39 · 4.5 → E 4.40-4.44. El tema de E termina en 4.44 (p.165); la p.166 está en blanco; la p.167 es la introducción del Tema 5 y E 5.1 empieza en p.168. Todos los enunciados están en `ejercicios.txt` (tildes rotas en el .txt: acentos restituidos). El 4.40 se ha verificado en imagen (p.163); el 4.43 se ha recalculado numéricamente.

**Ejercicio 4.25** (E p.153). «El precio f de un coche depende, entre otros factores, de la potencia del motor p y de c, el consumo medio cada 100 km. ¿Qué signo podemos esperar que tengan ∂f/∂p y ∂f/∂c?»
Solución: ∂f/∂p>0, ∂f/∂c<0. Método: razonamiento cualitativo (fijar las demás variables y ver si f crece o decrece). U §4.3.2 p.169-170.

**Ejercicio 4.26** (E p.154). «El gradiente en (π, 1, 0), ∇f(π,1,0), de una función de tres variables, de existir, verifica: a) Es un número. b) Es un vector. c) Es la suma de todas las derivadas parciales en el punto (π,1,0). d) Ninguna de las anteriores.»
Solución: b). Método: el gradiente es el vector de las n derivadas parciales; la suma de éstas es la divergencia (no es el gradiente). U §4.3.3 p.173-174.

**Ejercicio 4.27** (E pp.154-155). «Sea f la función dada por f(x,y) = x ∫₀^y s e^s ds para (x,y) ∈ R×(0,+∞). 1. Utilizando el teorema fundamental del Cálculo calcula el gradiente de f en un punto arbitrario. 2. Después de calcular la integral ∫₀^y s e^s ds por partes, se pide determinar el gradiente de f sin utilizar el teorema fundamental del Cálculo.»
Solución: ∇f(x,y) = (1+(y−1)e^y, xye^y). Método: derivar una integral respecto de su límite superior (TFC) e integración por partes. Prerrequisito de integrales (Tema 6); U §4.3.2 p.170.

**Ejercicio 4.28** (E p.155). «Calcula el gradiente de la función dada por f(x,y) = y tg(eˣ) + cos²(x+y) en el punto (0,0).»
Solución: ∇f(0,0) = (0, tg 1). Método: derivadas parciales con regla de la cadena y sustitución. U §4.3.2 p.171 (Ej. 4.23).

**Ejercicio 4.29** (E p.155). «Encuentra un vector perpendicular al gradiente de f(x,y) = e^{x−y} cos(x) + (y−1)³ en el punto (0,0).»
Solución: ∇f(0,0)=(1,2); un vector perpendicular es (−2,1) (cualquier múltiplo). Método: gradiente y producto escalar nulo. U Propiedad 4.1 p.174.

**Ejercicio 4.30** (E p.156). «Calcula la ecuación de la recta tangente a la curva intersección del plano x = 1 con la gráfica de la función dada por f(x,y) = x² + y² en el punto (1,2,5).»
Solución: (x,y,z) = (1,2,5) + λ(0,1,4), λ∈R. Método: vector director (0, 1, ∂f/∂y) de la curva intersección con x=a. U §4.3.2 p.169-170 (Def. 4.9 e interpretación geométrica).

**Ejercicio 4.31** (E p.157). «Calcula el gradiente en (2,3) de la función dada por f(x,y) = ln(xy).»
Solución: ∇f(2,3) = (1/2, 1/3). Método: derivadas parciales de un logaritmo. U §4.3.3 p.173.

**Ejercicio 4.32** (E p.157). «Calcula los puntos de R³ en los que se anula el gradiente de f dada por f(x,y,z) = x² + y³ + z² − 2z.»
Solución: solo (0,0,1). Método: igualar las tres componentes a cero (sistema). U §4.3.3 p.173-174.

**Ejercicio 4.33** (E pp.157-158). «Calcula las funciones derivadas parciales ∂f/∂x y ∂f/∂y, donde f: R²→R es la función definida por f(x,y) = x²y²/(x²+y²) si (x,y)≠(0,0), f(0,0)=0.»
Solución: ∂f/∂x = 2xy⁴/(x²+y²)², ∂f/∂y = 2x⁴y/(x²+y²)² si (x,y)≠(0,0); ∂f/∂x(0,0)=∂f/∂y(0,0)=0 por la definición. Método: reglas de derivación fuera del origen y definición (límite del cociente) en el origen. U Def. 4.8-4.9 y Ej. 4.24 p.172.

**Ejercicio 4.34** (E pp.158-159). «Estudia la continuidad en el origen de las funciones derivadas parciales del ejercicio anterior.»
Solución: ambas son continuas en (0,0). Método: límite en (0,0) por la recta y=mx (da 0, no basta) y después coordenadas polares (ρ·cosθ·sen⁴θ → 0). Relacionado con U Teorema 4.1 p.178 (§4.4).

**Ejercicio 4.35** (E p.159). «Las ecuaciones en las que aparecen derivadas parciales se llaman ecuaciones en derivadas parciales… Comprueba que u(t,x) = sen(x−t) verifica la ecuación de ondas ∂²u/∂t² = ∂²u/∂x², (t,x)∈R², que describe el movimiento de una cuerda vibrando.»
Solución: u_tt = −sen(x−t) = u_xx. Método: derivar dos veces y comparar. U §4.4.2 p.175-176.

**Ejercicio 4.36** (E p.160). «Calcula la matriz Hessiana en (0,1,0) de la función dada por f(x,y,z) = cos x + ½y².»
Solución: Hf(0,1,0) = [[−1,0,0],[0,1,0],[0,0,0]]. Método: derivadas segundas (la mixtas son nulas) con Schwarz. U §4.4.2 p.177.

**Ejercicio 4.37** (E pp.160-161). «Para la función f dada por f(x,y) = x²y calcula: su dominio, el gradiente en el punto (1,0), y la matriz Hessiana en el punto (1,0).»
Solución: dominio R²; ∇f(1,0)=(0,1); Hf(1,0)=[[0,2],[2,0]]. Método: polinomio; tabla de derivadas. U §4.4.2 p.177.

**Ejercicio 4.38** (E pp.161-162). «Considera la función de dos variables dada por f(x,y) = (x³y − xy³)/(x²+y²) si (x,y)≠(0,0), f(0,0)=0. Calcula las derivadas parciales de f en todo punto y las derivadas parciales segundas en (0,0).»
Solución: ∂f/∂x(0,0)=∂f/∂y(0,0)=0; en (0,0): ∂²f/∂y∂x = −1 y ∂²f/∂x∂y = +1 (no coinciden). Método: en el origen, definición de derivada parcial aplicada a las derivadas primeras (cociente de incrementos). U §4.4.2 p.178.

**Ejercicio 4.39** (E pp.162-163). «¿Por qué pueden no coincidir las derivadas parciales segundas cruzadas en el ejercicio anterior pese a que existe un resultado en esa dirección?»
Solución: no se cumple la hipótesis de continuidad de ∂²f/∂x∂y en (0,0) (Teorema de Schwarz). Método: comprobar las hipótesis del teorema. U Teorema 4.1 p.178.

**Ejercicio 4.40** (E p.163). «De una función de tres variables f se sabe que tiene derivadas parciales continuas en todo R³ y que ∇f(1,π,√7) = (√8, 3, √5). ¿Es cierto que su derivada direccional en la dirección de (√2, 3, √5) en el punto (1,π,√7) es menor que π?» (verificado en imagen)
Solución: el vector (√2,3,√5) tiene norma 4; D = (√8·√2 + 9 + 5)/4 = 18/4 = 9/2 = 4,5 > π ⇒ la respuesta es no. Método: D_u f = ∇f·u con u unitario (Teorema 4.2). U Teorema 4.2 p.180.

**Ejercicio 4.41** (E p.163). «Utilizando la definición, calcula la derivada direccional de f en (1,−1,2) en la dirección del vector unitario ū/‖ū‖, donde ū=(0,1,1) y f(x,y,z)=xy−z.»
Solución: ū/‖ū‖=(0,1/√2,1/√2); f(1, −1+h/√2, 2+h/√2) − f(1,−1,2) = 0 para todo h ⇒ D = 0. Método: definición de derivada direccional con límite (Def. 4.10). U Def. 4.10 p.179.

**Ejercicio 4.42** (E p.164). «Para la función f dada por f(x,y) = x cos(x+y), indica el ángulo formado por el vector (1,1) y la dirección de máximo crecimiento de f en (0,0). a) π/2 radianes b) π/4 radianes c) π/8 radianes d) Ninguna de las anteriores.»
Solución: b). ∇f(x,y) = (cos(x+y) − x sen(x+y), −x sen(x+y)); ∇f(0,0)=(1,0); cos α = (1,0)·(1,1)/(1·√2) = 1/√2 ⇒ α=π/4. Método: dirección de máximo crecimiento = gradiente; ángulo con el producto escalar. U Teorema 4.3 p.182.

**Ejercicio 4.43** (E pp.164-165). «Indica la dirección de máximo crecimiento en el punto (1,1) de f dada por f(x,y) = x²/(x²+y²) si (x,y)≠(0,0), f(0,0)=0. a) (√2/2, −√2/2) b) (√2/2, √2/2) c) (−√2/2, −√2/2) d) Ninguna de las anteriores.» (cálculo comprobado numéricamente)
Solución: a). ∇f(1,1)=(1/2,−1/2); normalizado (√2/2, −√2/2). Método: gradiente normalizado. U Teorema 4.3 p.182.

**Ejercicio 4.44** (E p.165). «Calcula la ecuación de la recta tangente en el punto (1,2,2) de la curva intersección de la gráfica de f(x,y) = x²y con un plano paralelo al eje z y al vector (1,1,0).»
Solución: ∇f(1,2)=(4,1); D_{(1,1)/√2} f(1,2) = 5/√2 (comprobado); vector director (1/√2, 1/√2, 5/√2) ∝ (1,1,5); recta (x,y,z)=(1,2,2)+λ(1,1,5). Método: derivada direccional según la dirección del plano vertical = vector director de la tangente. U Teorema 4.2 p.180 e interpretación p.180.


## 5. X (libro de exámenes) relacionadas con 4.3-4.5
Fuente: `indice_examenes_4.md` (y `indice_examenes_*` de otros temas, solo si cruzan). Todas las páginas indicadas se han visto en imagen (PDF renderizado con pdftoppm en el scratchpad). Las fórmulas se han recalculado.

1. **Examen 4 «elaborado con exámenes de asignaturas similares», Ej. 6 — enunciado PDF 119 (impresa 11), solución PDF 121 (impresa 13)**. «Calcúlense los máximos y mínimos de f(x,y) = 5 + x²y²». Solución: puntos críticos en los ejes; mínimo 5 en los ejes, sin máximo. Tema: 4.3 (parciales) + extremos (5.x). **Erratum en la solución**: pone ∂f/∂y = 2xy²; debe ser 2x²y (el índice escribe «f_x=f_y=2xy²»: también incorrecto). La conclusión no cambia.
2. **Examen 5 «elaborado…», Ej. 6 — enunciado PDF 122 (impresa 14), solución PDF 124-125 (impresa 16-17)**. «Estudiar la continuidad, derivabilidad y diferenciabilidad de f(x,y) = (x³+xy²+3y⁴)/(x²+y²) con f(0,0)=0.» Continua (límite 0 por polares), D₁f(0,0)=1, D₂f(0,0)=0, diferenciable (límite de polares = 0). Tema: 4.2 (continuidad) + 4.3 (parciales) + 5.1 (diferencial). Verificado.
3. **Sin fecha, I. Electrónica Industrial y Automática (examen A), P4 corta — PDF 127**. Plano tangente a f=x²+xy en (1,2,3): 4x+y−z=3. Tema: 4.3 (gradiente) → 5.1. Verificado.
4. **Sin fecha, I. Electrónica (examen B), P4 corta — PDF 130**. ∇f(2,3) de f=ln(xy) = (1/2, 1/3). Tema: 4.3. Verificado.
5. **Sin fecha, I. Electrónica (examen B), Ej. 6 — PDF 130-131**. f=x²/(x²+y²), f(0,0)=0: (a) continuidad: no es continua en (0,0) (por y=0 el límite es 1); (b) asíntotas de G(z)=f(π,z)=π²/(π²+z²): y=0 horizontal, sin oblicuas ni verticales; (c) dirección de máximo crecimiento en (1,1): (√2/2, −√2/2). Tema: 4.2 + 4.3 + **4.5 (única X de esta sección que pregunta por la dirección de máximo crecimiento)**. Verificado.
6. **Septiembre 2017 (I. Electrónica), P4 corta — PDF 133**. Plano tangente de f=eˣ(3 sen y+2) en (0, π/2, 5): z=5+5x. Tema: 4.3 → 5.1. Verificado.
7. **Feb 2017, 2ª semana, Ej. 6 — PDF 136**. f=4xy−2y²−x³+1: puntos críticos (0,0) (silla, |Hf|=−16) y (4/3,4/3) (máximo relativo; Hf=[[−8,4],[4,−4]], det=16). Tema: **4.4 (Hessiana)** + 5.x (extremos). Verificado.
8. **Feb 2017, 1ª semana, Ej. 6 — PDF 138**. f=x²y³/(x⁴+y²), f(0,0)=1: (a) discontinua en (0,0); (b) plano tangente en (1,1,1/2): z = y − 1/2 (∇f(1,1)=(0,1)). Tema: 4.2 + 4.3 → 5.1. Verificado. Ver dudas sobre el argumento de discontinuidad.
9. **Feb 2018, 2ª semana, P3 corta — PDF 140**. V/F: «f diferenciable en R² con ∇f(a,b)=(0,0) ⇒ (a,b) es extremo relativo». Solución: falso («Ver texto base página 267», referencia no verificable en nuestras fuentes). Contraejemplo propio: f(x,y)=x³ en (0,0). Tema: 4.3 + 5.x. Verificado.
10. **Sept 2018 (I. Electrónica), P4 corta — PDF 142**. Matriz Hessiana de f=y sen x − y³eˣ + 2: [[−y sen x − y³eˣ, cos x − 3y²eˣ],[cos x − 3y²eˣ, −6yeˣ]]. Tema: **4.4**. Verificado.
11. **Sept 2018 (I. Electrónica), Ej. 6 — PDF 143**. f=ln(36−x²−y²): dominio (disco abierto de radio 6), ∇f(1,5)=(−1/5, −1), f∘g=ln(36−ρ²). Tema: 4.2 + **4.3** (gradiente). Verificado.
12. **Feb 2018, 1ª semana, P4 corta — PDF 144**. Hessiana de f=x²+eˣ+5y²−z³−cos z en (2,1,π): diag(2+e², 10, −6π−1). Tema: **4.4**. Verificado.
13. **Feb 2019, 2ª semana, Ej. 6 — PDF 148-149**. f=ln(4−x²−y²), g=√(x²+y²−1), h=f+g: dominio {1 ≤ x²+y² < 4} (corona); ∇f(0,3/2)=(0,−12/7); ∇g(0,3/2)=(0,3√5/5); producto escalar −36√5/35. Tema: 4.2 + **4.3**. Verificado.
14. **Feb 2019, 1ª semana, Ej. 6 — PDF 152**. f=xy(5x−15+y): ∇f(2,−3)=(−6,−22); puntos críticos (0,0), (3,0), (0,15), (1,5). Tema: **4.3** + 5.x. Verificado.

Fuera de `indice_examenes_4.md` pero relacionadas (no leídas en detalle; ver dudas): Examen 3 Ej. 6 (índice 3) — f=4x³/(x²+y²), continuidad y diferenciabilidad en (0,0) — enunciado en PDF 116, solución PDF 117-118 (la solución está en el .txt). Sept 2018 Mod. B P4 (PDF 139, sin solución) — producto escalar de vectores de R⁴ (4.1, no 4.3).

Preguntas de X no relacionadas con 4.3-4.5 y que el índice clasifica como 4.x/5.x de Lagrange: Sept 2017 Ej. 6 (PDF 134), Sept 2018 Mod. B Ej. 6 (PDF 139, sin solución), Feb 2019 1ª P4 (PDF 150-151, función implícita 5.x): quedan para el Tema 5.

## 6. Faltas o dudas
- **U, Ej. 4.24 (p.172)**: el .txt está ilegible en las fórmulas de las derivadas parciales. He reconstruido ∂f/∂x = y(y²−x²)/((x²+y²)²+x²y²) (y simétrica) y comprobado numéricamente en dos puntos; la función es arctg(xy/(x²+y²)) (confirmado por el límite arctg(m/(1+m²)) del texto). Verificar en el PDF si se cita la fórmula literal.
- **U, Fig. 4.15 (p.169)** tiene número en el texto; la figura de gradientes y curvas de nivel (p.174) no tiene número en el .txt. Ninguna de las dos recortada.
- **U, p.176 y p.178**: las subíndices de las derivadas mixtas se leen bien (∂²f/∂y∂x = ∂_y(∂_x f)); U advierte que no hay criterio único de subíndices.
- **E 4.44**: el .txt rompe la expresión de la derivada direccional («√5 2»); he recalculado 5/√2 = 5√2/2 ≈ 3,5355 (coherente con (1,1,5)).
- **E 4.25-4.44**: no encontré erratas matemáticas (todas las cuentas recalculadas coinciden). E 4.27 usa el teorema fundamental del cálculo y E 4.34 las coordenadas polares (prerrequisitos fuera de este tema).
- **E 4.26 (p.154)**: el enunciado de la solución menciona la «divergencia» (suma de parciales) como concepto distinto del gradiente; no pertenece a U §4.3 y no se usa en el dossier.
- **X, Examen 4, Ej. 6, PDF 121**: la solución escribe ∂f/∂y=2xy² (erratum; debe ser 2x²y). El índice escribe f_x=f_y=2xy². Corregido en el dossier.
- **X, Feb 2017 1ª, Ej. 6 (PDF 138)**: la solución prueba la discontinuidad solo con los límites por rectas (todos dan 0), lo cual no basta para afirmar que el límite es 0. La conclusión es correcta: |f(x,y)| ≤ y²/2 (por x⁴+y² ≥ 2x²|y|), así que lím = 0 ≠ f(0,0)=1. En el HTML usar el acotamiento.
- **X, Feb 2018 2ª, P3 (PDF 140)**: la solución remite a «texto base página 267», que no está en nuestras fuentes; el contraejemplo x³ es propio.
- **X, índice_examenes_4.md**: corregir la entrada del Examen 4 Ej. 6 (f_x=f_y erróneo) y revisar la del Feb 2017 1ª (el índice no indica el argumento insuficiente).
- **X, Examen 3 Ej. 6 (PDF 116-118)**: está en `indice_examenes_3.md`, fuera del rango de este dossier; enunciado no verificado en imagen (solo la solución en el .txt).
- **X, páginas**: no he encontrado en el índice ningún ejercicio de X que pregunte directamente por derivadas direccionales salvo el de la Electrónica B (PDF 130-131). Las derivadas de orden superior (4.4) aparecen en las Hessianas de PDF 136, 142, 144.
- **S y L**: sin apartado equivalente (ver §0).
