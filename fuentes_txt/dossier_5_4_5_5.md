# Dossier Tema 5.4 y 5.5: Valores extremos y extremos condicionados

Generado el 2026-10-23 a partir de `fuentes_txt/ingenieros.txt` (U), `ejercicios.txt` (E) e `indice_examenes_1..4.md` (X, con comprobación de páginas por `pdftotext` sobre `Examenes-resueltos-Calculo.pdf`). Páginas: U impresa = PDF + 2; E impresa = PDF.

## 0. Rangos de páginas

| Apartado | Impresas | PDF (U) | Contenido |
|---|---|---|---|
| U §5.4 Valores extremos | **pp. 212–222** | 210–220 | 5.4.1 Motivación (212); 5.4.2 Extremos absolutos/relativos, puntos críticos, Hessiana, teorema de valores extremos (213–222) |
| U §5.5 Extremos condicionados | **pp. 223–231** | 221–229 | 5.5.1 Motivación (223); 5.5.2 Método de los multiplicadores de Lagrange (224–231) |
| Autoevaluación de Tema 5 (general) | pp. 232–233 | 230–231 | Afirmaciones V/F; las 8, 9 y 10 tocan extremos y Lagrange |

Nota: la figura 5.15 y el cierre del tema están en p. 232 (la sección 5.5 acaba en p. 231).

## 1. U (libro oficial)

### U §5.4.1 Motivación (p. 212)
- Motivación: temperatura T(x,y) de una placa; máximos y mínimos absolutos. Se trabaja con funciones regulares y, sobre todo, con dos variables (p. 212).

### U §5.4.2 Extremos absolutos y relativos (pp. 213–214)
- **Def. 5.7 (p. 213).** La función f: D ⊂ ℝ² → ℝ alcanza un máximo absoluto en (a,b) si f(x,y) ≤ f(a,b) para todo (x,y) ∈ D.
- **Def. 5.8 (p. 213).** Alcanza un mínimo absoluto en (a,b) si f(x,y) ≥ f(a,b) para todo (x,y) ∈ D.
- **Def. 5.9 (p. 213).** Máximos y mínimos absolutos se llaman colectivamente extremos absolutos. En ℝⁿ: f(x₁,…,xₙ) ≤ f(a₁,…,aₙ) para todo punto de D; si las desigualdades son estrictas, máximo/mínimo absoluto estricto.
- **Ej. 5.15 (pp. 213–214).** f(x,y)=x²+y² alcanza un mínimo absoluto estricto en (0,0) (f ≥ 0, f=0 ⇔ x=y=0) y no alcanza máximo absoluto (para cualquier t ∈ ℝ, el punto (0,√t) da f ≥ t).
- **Def. 5.10 (p. 214).** f alcanza un máximo relativo en (a,b) si existe un disco abierto A con (a,b) ∈ A tal que f(x,y) ≤ f(a,b) para todo (x,y) ∈ A ∩ D.
- **Def. 5.11 (p. 214).** Mínimo relativo: igual con f(x,y) ≥ f(a,b).
- **Def. 5.12 (p. 214).** Máximos y mínimos relativos se llaman colectivamente extremos relativos. Para ℝⁿ, igual con (x₁,…,xₙ) ∈ A ∩ D. Si las desigualdades son estrictas, extremos relativos estrictos.
- **Ej. 5.16 (p. 215).** Figura 5.9: función con tres máximos relativos (uno absoluto) y tres mínimos relativos (uno absoluto). Texto del ejemplo: «Alcanza tres máximos relativos, uno de ellos es también absoluto… tres mínimos relativos, siendo uno de ellos el mínimo absoluto». *Ojo: la fórmula sale rota en el .txt («15 x3 + xy4 e−(x²+y²)»; probablemente una fracción 1/5). Verificar en el PDF p. 215 antes de citarla.*
- Comentario de transición (p. 215): en funciones de una variable se calculan primero los puntos críticos y luego se clasifican; se quiere extender a varias variables.

### U §5.4.2 Puntos críticos (pp. 216–217)
- **Def. 5.13 (p. 216).** Una función regular f: D ⊂ ℝ² → ℝ tiene un punto crítico en (a,b) si se anulan sus derivadas parciales: ∂f/∂x(a,b) = ∂f/∂y(a,b) = 0. Equivalente a ∇f(a,b) = 0. En ℝⁿ, ∇f(a₁,…,aₙ) = 0. No hay regla general para resolver el sistema (puede requerir ingenio).
- **Ej. 5.17 (pp. 216–217).** f(x,y)=(x²+2y²)e^{1−(x²+y²)}: ∂f/∂x = 2x(1−x²−2y²)e^{…}, ∂f/∂y = 2y(2−x²−2y²)e^{…}. Puntos críticos: (0,0), (±1,0), (0,±1). El caso x=y=0 se descarta en el sistema reducido (no tiene solución).
- **Ej. 5.18 (p. 217).** f(x,y)=x²y²/(x²+y²) si (x,y) ≠ (0,0), f(0,0)=0. En ℝ²∖{(0,0)} las derivadas se anulan cuando x=0 o y=0: todo punto de los ejes es crítico.

### U §5.4.2 Condición necesaria, punto de silla y Hessiana (pp. 218–221)
- **Teorema (Condición necesaria de extremo relativo) (p. 218).** «Sea f: D ⊂ ℝ² → ℝ una función diferenciable en D abierto. Si f alcanza un extremo relativo en (a,b) ∈ D, entonces ∇f(a,b) = 0.» Demostración (p. 218): F(x)=f(x,b) y G(y)=f(a,y); F′(a)=0 y G′(b)=0. Vale también en ℝⁿ.
- **Punto de silla (p. 219).** Punto crítico que no es extremo relativo («punto de ensilladura, punto de silla o punto estacionario»). Un punto crítico no garantiza extremo. Ej. 5.19 (p. 219): f(x,y)=3x²−y² (paraboloide hiperbólico), único punto crítico (0,0), que es silla (f(x,0)=3x²>0, f(0,y)=−y²<0).
- **Teorema (Condición suficiente de extremo) (p. 220).** «Supongamos que f: D ⊂ ℝ² → ℝ tiene un punto crítico en (a,b). Si la matriz Hessiana de f en (a,b) es Hf(a,b) = [[∂²f/∂x², ∂²f/∂x∂y],[∂²f/∂y∂x, ∂²f/∂y²]](a,b) = [[r,s],[t,u]] y su determinante es d = |Hf(a,b)|, entonces:»
  - Si d > 0 y r > 0: mínimo relativo en (a,b).
  - Si d > 0 y r < 0: máximo relativo en (a,b).
  - Si d > 0 y r = 0: caso dudoso.
  - Si d < 0: punto de silla en (a,b).
  - Si d = 0: caso dudoso.
  - Nota (p. 221): se puede sustituir r por u y el resultado es igual de válido. Generalización a ℝⁿ: forma cuadrática de la Hessiana, no se trata en el curso.
- **Ej. 5.20 (pp. 221–222).** f(x,y)=(x²+2y²)e^{1−(x²+y²)}. Hessiana en (0,0) = diag(2e, 4e), d = 8e² > 0, r = 2e > 0 → mínimo relativo. En (±1,0): H = diag(−4,2) (la extracción da «−4 0 / 0 2»), d = −8 < 0 → silla. En (0,±1): H = diag(−2,−8), d = 16 > 0, r = −2 < 0 → máximo relativo. (Verificado con sympy: det 8e², −8, 16.)

### U §5.4 Teorema de los valores extremos y procedimiento (p. 222)
- **Teorema (p. 222).** «Si una función continua f está definida en un subconjunto S ⊂ ℝⁿ cerrado y acotado, entonces alcanza el máximo y el mínimo absolutos en S. Además, los extremos absolutos se alcanzan en la frontera de S o en un punto crítico de f que sea del interior de S.»
- **Procedimiento (p. 222).** (1) Hallar los puntos críticos de f en S. (2) Hallar los puntos de la frontera de S donde se pueden alcanzar extremos. (3) Calcular f en todos esos puntos; el mayor (menor) valor da el máximo (mínimo) absoluto. El paso (2) es el más difícil y se trata en §5.5 (p. 222).
- **Ej. 5.21 (p. 223).** f(x,y)=x²+2y² en S = {x²+y² ≤ 1}. Mínimo absoluto en (0,0) (único punto crítico del interior); el máximo no está en el interior y se estudia con Ej. 5.22.

### U §5.5.1 Motivación (p. 223)
- Problemas de extremos «condicionados» (buscar extremos que cumplan una condición, p. ej. estar en una frontera o curva). Objetivos: entender el método de los multiplicadores de Lagrange y resolver con él.

### U §5.5.2 Ejemplo 5.22, despejando la variable (pp. 224–225)
- f(x,y)=x²+2y² en la frontera de S={x²+y² ≤ 1}, g(x,y)=x²+y²−1. Se despeja y=±√(1−x²) (teorema de la función implícita) y se reduce a F(x)=2−x², x∈(−1,1); F′(x)=−2x=0 ⇔ x=0 ⇒ y=±1. Como ∂g/∂y(x,0)=0, los puntos (±1,0) se estudian aparte. Valores: f(0,0)=0, f(±1,0)=1, f(0,±1)=2. **Máximo absoluto en (0,±1) (valor 2); mínimo en (±1,0) (valor 1).** (p. 225: «hemos aplicado el teorema de la función implícita donde era posible…».)

### U §5.5.2 Ejemplo 5.23, planteamiento (p. 226)
- Lata cilíndrica de volumen dado (300 ml): V(r,h)=πr²h; superficie S(r,h)=2πr²+2πrh; restricción πr²h=300. **El ejemplo sólo plantea el problema; no lo resuelve en el texto.** Ver E 5.40 para la resolución.

### U §5.5.2 Teorema de Lagrange (pp. 226–228)
- **Teorema de Lagrange (dos variables) (p. 226).** «Sean f y g funciones continuas y con derivadas parciales continuas. Supongamos que f tiene un extremo relativo en (a,b) sobre la curva g(x,y)=0 y que ∇g(a,b) ≠ 0. Entonces existe un número λ tal que ∇f(a,b) = −λ∇g(a,b).» Se define F(x,y,λ)=f(x,y)+λg(x,y); λ se llama **multiplicador de Lagrange**; (a,b,λ) es punto crítico de F.
  *Aviso de extracción: el símbolo ≠ no sale en el .txt (aparece «∇g(a,b) = 0»). Confirmar en el PDF p. 226 y 228; la hipótesis que corresponde es ∇g ≠ 0.*
- **Demostración geométrica (p. 227).** Las curvas de nivel f(x,y)=c se tocan tangencialmente en el óptimo; como ∇f es perpendicular a la curva de nivel, ∇f y ∇g son proporcionales. Figura 5.13 (p. 227): curvas de nivel f(x,y)=c_i y la curva g=0. Si el punto crítico de F es extremo relativo de F, f alcanza en (a,b) un extremo condicionado (p. 227).
- **Teorema de Lagrange (n variables) (p. 228).** «Sean f, g: D ⊂ ℝⁿ → ℝ funciones continuas y con derivadas parciales continuas. Supongamos que f tiene un extremo relativo en (a₁,…,aₙ) sobre g(x₁,…,xₙ)=0 y que ∇g(a₁,…,aₙ) ≠ 0. Entonces existe un número λ tal que ∇f(a₁,…,aₙ) = −λ∇g(a₁,…,aₙ).» (p. 228; mismo aviso sobre ≠.)
- Localizar los posibles extremos condicionados es resolver un sistema; para saber cuál es máximo o mínimo se usa la naturaleza del problema o el teorema de valores extremos si el conjunto restricción es cerrado y acotado (p. 228).

### U §5.5.2 Método con una condición (p. 228)
«Si queremos calcular los extremos de f(x,y) sujeta a la restricción g(x,y)=0 …, se procede como sigue:»
1. Definir F(x,y,λ)=f(x,y)+λg(x,y).
2. Resolver ∇F(x,y,λ)=(0,0,0) (puntos críticos de F).
3. Si en el conjunto g=0 se alcanzan los extremos, calcular f en los puntos críticos de F; el máximo (mínimo) absoluto está donde f sea mayor (menor).
4. Si g define y como función implícita de x, y = h(x), se pueden estudiar los extremos de f(x,h(x)).
- Además (p. 229): el método vale en ℝⁿ; si el conjunto restricción no es cerrado y acotado, las condiciones suficientes usan la Hessiana (no se tratan en el texto). Para tres variables con z = h(x,y) se puede estudiar la Hessiana de f(x,y,h(x,y)) (p. 231).
- Generalización con más de una restricción (p. 225): se introduce una variable nueva por restricción; no se trata.

### U §5.5.2 Ejemplos resueltos de Lagrange (pp. 229–231)
- **Ej. 5.24 (p. 229).** f(x,y)=x²+2y² sobre C={x²+y²=1}. F = x²+2y²+λ(x²+y²−1). Puntos críticos: (±1,0) con λ=−1; (0,±1) con λ=−2. (La naturaleza ya se estudió en Ej. 5.22.) Verificado con sympy.
- **Ej. 5.25 (pp. 229–230).** Dos números positivos con suma 9 y producto máximo: f(x,y)=xy, g=x+y−9, con x,y ≥ 0. Puntos críticos de F: x=y=9/2, λ=−9/2; f(9/2,9/2)=81/4; en los extremos del segmento (0,9) y (9,0) f=0. **Máximo en (9/2, 9/2).** (Figura 5.14, p. 230.)
- **Ej. 5.26 (p. 231).** Tres números positivos con suma 9 y producto máximo: f(x,y,z)=xyz, restricción x+y+z−9=0. Puntos críticos de F: (0,0,9), (0,9,0), (9,0,0) con λ=0 (f=0) y (3,3,3) con λ=−9 (f=27). **Producto máximo 27, en x=y=z=3.** (Conjunto cerrado y acotado, Figura 5.15 p. 232.)

### U Autoevaluación de Tema 5 (pp. 232–233)
- Afirmaciones 8, 9 y 10 relacionadas con el tema: 8 (f: ℝ²→ℝ con ∇f(0,1)=(0,0) y Hf(0,1)=[[11],[12]] garbled en el .txt: "¿se garantiza mínimo relativo?"); 9 (posibles extremos de f sujeta a g=0 «son soluciones del sistema ∇f(x,y)=∇g(λx,λy)»); 10 (máximo absoluto en un disco cerrado con derivadas parciales positivas, «se alcanza en la frontera»). **No se dan soluciones en el texto.** La afirmación 8 tiene la matriz rota en el .txt: verificar en PDF p. 233.

### Figuras candidatas para recorte (PDF = impresa − 2)
- Fig. 5.9 (p. 215, PDF 213): gráfica de f con máximos y mínimos relativos (Ej. 5.16).
- Fig. 5.10 (p. 218, PDF 216): plano tangente en punto crítico.
- Fig. 5.11 (p. 220, PDF 218): paraboloide hiperbólico 3x²−y² (silla).
- Fig. 5.12 (p. 225, PDF 223): extremo condicionado de z=f(x,y) con restricción y=k.
- Fig. 5.13 (p. 227, PDF 225): curvas de nivel tangentes a g=0 (demostración geométrica).
- Fig. 5.14 (p. 230, PDF 228): segmento x+y−9=0 en el primer cuadrante.
- Fig. 5.15 (p. 232, PDF 230): triángulo x+y+z=9 en el primer octante.

## 2. S (Stewart) y L (Larson): sin pasajes equivalentes

- **Stewart (`stewart.txt`)**: no contiene material de funciones de varias variables (búsqueda de «derivadas parciales», «gradiente», «Lagrange», «hessian», «multiplicador»: 0 resultados). El cap. 14 (Derivadas parciales y extremos con Lagrange) no está en el fichero. **No localizado.** Hace falta el tomo de varias variables de Stewart para cubrirlo.
- **Larson (`larson.txt`)**: el texto extraído sólo cubre cálculo de una variable y no tiene capítulo 13 (funciones de varias variables) ni extremos condicionados. Sólo aparecen «multiplicadores de Lagrange, 952, 953» en el índice alfabético final (línea ~63860), pero esas páginas no están en el texto extraído (el .txt acaba en la impresa ~776). **No localizado.** El resultado «multiplicador» en larson.txt es el «efecto multiplicador» de series (irrelevante).

## 3. E (libro de ejercicios): Tema 5, extremos y Lagrange

Mapa: los ejercicios de extremos y Lagrange de E están entre el **5.28 y el 5.48**. Los 5.1–5.27 corresponden a diferenciabilidad, regla de la cadena, TVM y función implícita (U §5.1–5.3), fuera de este dossier. Enunciados en su forma del .txt, con las tildes restauradas.

Leyenda de subsección U: [5.4] = §5.4 (valores extremos), [5.5] = §5.5 (Lagrange). Método: «Lagrange» = multiplicadores; «crit+H» = puntos críticos + Hessiana; «abs» = teorema de valores extremos.

### Ejercicio 5.28 (E p. 191) [5.4, extremos absolutos]
¿Alcanza la función f(x,y) = y²x² + y² + 4 sen²x los valores mínimo y máximo absolutos en ℝ²?
Solución (E): f ≥ 0 y sólo se anula en (kπ,0), k ∈ ℤ: mínimo absoluto en esos puntos; no está acotada, luego no hay máximo.
Método: análisis de signo directo (sin derivadas).

### Ejercicio 5.29 (E p. 191) [5.4, puntos críticos]  — marca «MAXIMA»
Localiza los puntos en los que la función f(x,y) = x³ + y³ + xy puede alcanzar los extremos relativos.
Solución (E): ∂f/∂x = 3x²+y, ∂f/∂y = 3y²+x; puntos críticos (0,0) y (−1/3,−1/3). (Verificado con sympy.)
Método: crit (sistema polinómico).

### Ejercicio 5.30 (E p. 192) [5.4, puntos críticos]  — MAXIMA
Determina los puntos críticos de la función f(x,y) = xy(x²+y²). (La fórmula en el .txt sale como «xy x²+y²»; el desarrollo usa f_x = 3x²y+y³, f_y = x³+3xy², que corresponde a xy(x²+y²).)
Solución (E): único punto crítico (0,0) (si x=0 ⇒ y=0 y viceversa; si ambos ≠0 el sistema 3x²+y²=0, x²+3y²=0 es imposible). (Verificado con sympy.)
Método: crit (sistema por casos).

### Ejercicio 5.31 (E p. 193) [5.4, extremos relativos]  — MAXIMA
Sea f(x,y) = x³ + y² − xy. Estudia si la función alcanza sus extremos relativos en los puntos (0,0), (1,−1) y (1/6, 1/12) y, en caso de que así sea, razona si son máximos o mínimos. ¿Es alguno de estos puntos un extremo absoluto de f en ℝ²? ¿Se alcanzan en ℝ² extremos absolutos?
Solución (E): puntos críticos (0,0) y (1/6,1/12) ((1,−1) no es crítico). H(0,0) = [[0,−1],[−1,2]], d = −1 < 0: silla. H(1/6,1/12) = [[1,−1],[−1,2]], d = 1 > 0, r = 1 > 0: mínimo relativo, no absoluto (f(−1,0) = −1 < f(1/6,1/12) = −1/432). Sin extremos absolutos: f(x,0)=x³ no está acotada. (Verificado: det −1 y 1.)
Método: crit + Hessiana (criterio d, r).

### Ejercicio 5.32 (E p. 194) [5.4, puntos críticos]  — MAXIMA
Determina los puntos críticos, y estudia si se alcanza algún extremo en ellos, para la función f(x,y) = y + x²y² − x² + y².
Solución (E): único punto crítico (0,−1/2); H(0,−1/2) = [[−3/2, 0],[0, 2]], d = −3 < 0: silla, no hay extremo. (Verificado con sympy: det −3.)
Método: crit + Hessiana.

### Ejercicio 5.33 (E p. 195) [5.4, extremo relativo, test]  — MAXIMA, Test (a/b/c/d)
La función f(x,y) = x² sen²y verifica: a) Alcanza en (0,0) un mínimo relativo. b) Alcanza en (0,0) un máximo relativo. c) Tiene en (0,0) un punto de silla. d) Ninguna de las anteriores.
Solución (E): gradiente nulo en (0,0); Hessiana nula ⇒ criterio no concluye. Pero f ≥ 0 y f(0,0)=0: mínimo absoluto, luego relativo. Respuesta a).
Método: crit + Hessiana (degenerada) y después argumento de signo.

### Ejercicio 5.34 (E p. 196) [5.4, plano tangente, puntos críticos, polares]  — MAXIMA
Para f(x,y) = (x²+3y²)/(x²+y²+1)²: a) plano tangente en (−1, 0, f(−1,0)); b) puntos críticos; c) expresión en polares.
Solución (E): f(−1,0)=1/4 y ∇f(−1,0)=(0,0): plano z = 1/4. Puntos críticos (0,0), (±1,0), (0,±1). En polares f(ρ,θ) = ρ²(2sen²θ+1)/(ρ²+1)². (Verificado: f(−1,0)=1/4, gradiente nulo.)
Método: derivadas + cambio a polares.

### Ejercicio 5.35 (E p. 197) [5.4, extremo relativo]  — MAXIMA
Sea f(x,y) = x(1−cos y) + y(1−cos x) + xy. Calcula ∇f(π,0), ¿es (π,0) un punto crítico?; estudia si en (0,0) la función alcanza un extremo relativo.
Solución (E): ∇f(π,0) = (0, 2+π) ≠ 0: no crítico. ∇f(0,0)=0; H(0,0) = [[0,1],[1,0]], det = −1 < 0: silla, no extremo.
Método: gradiente + Hessiana.

### Ejercicio 5.36 (E p. 198) [5.4, máximo de beneficio]  — MAXIMA
Dos componentes A y B. Con precios x (A) e y (B) se venden 12−4x+3y (miles) de A y 15+x−10y (miles) de B. Coste de fabricación: A 1 €, B 0.9 €. ¿Qué precios maximizan las ganancias?
Solución (E): f(x,y) = (x−1)(12−4x+3y) + (y−0.9)(15+x−10y) = 15.1x − 4x² + 4xy − 25.5 + 21y − 10y². Crítico: (x,y) ≈ (2.6805, 1.5861) (exacto 193/72, 571/360). Hf: f_xx = −8, det = 144 > 0 ⇒ máximo. (Verificado con sympy: crítico exacto y det 144.)
Método: modelado + crit + Hessiana.

### Ejercicio 5.37 (E p. 199) [5.4, mínimo de suma de cuadrados]
Se quieren instalar tres cables que conecten A=(0,0), B=(4,0), C=(1,3) con un punto P=(x,y). Se busca que la suma d₁²+d₂²+d₃² sea mínima. ¿Cuáles son las coordenadas de P?
Solución (E): f(x,y) = 3x²+3y²−10x−6y+26; crítico (5/3, 1); Hf = diag(6,6), det 36 > 0, f_xx > 0: mínimo en (5/3,1). (Verificado con sympy.)
Método: crit + Hessiana (función cuadrática).

### Ejercicio 5.38 (E p. 200) [5.4, existencia de máximo]
La función f(x,y) = x²y está definida sobre S = {x²+y² ≤ 1}. ¿Alcanza el máximo absoluto en este conjunto? Justifica la respuesta.
Solución (E): sí, S es cerrado y acotado y f es continua (teorema de valores extremos).
Método: abs (teorema de valores extremos).

### Ejercicio 5.39 (E p. 201) [5.5, Lagrange sobre recta]  — MAXIMA, test
Sea f(x,y) = x²−y² y C = {(x,y): x+y=0}. Discute: a) en (1,−1) se alcanza un mínimo condicionado; b) en (1,−1) se alcanza un máximo condicionado; c) en (1,−1) hay un punto de silla; d) ninguna de las anteriores.
Solución (E): F = x²−y²+λ(x+y); punto crítico (1,−1) con λ=−2; f es idénticamente 0 sobre la recta, así que (1,−1) es mínimo y máximo condicionado. Respuestas a) y b).
Método: Lagrange (F = f+λg) y argumento directo (f constante sobre C).

### Ejercicio 5.40 (E p. 202) [5.5, Lagrange, lata]  — MAXIMA
Utilizando el método de los multiplicadores de Lagrange, calcula las dimensiones de una lata cilíndrica cerrada (con ambas tapas) de volumen 300 ml candidatas a maximizar o minimizar su superficie.
Solución (E): f(r,h) = 2πr²+2πrh, g = πr²h−300; F = f + λg. Crítico: 2 + λr = 0, h = 300/(πr²), r³ = 150/π ⇒ r ≈ 3.6278 cm, h ≈ 7.2557 cm (h = 2r). E indica que el método de Lagrange no decide si es máximo, mínimo o silla; propone reducir a una variable (despejar h).
Método: Lagrange; comprobación posterior con una variable.

### Ejercicio 5.41 (E p. 203) [5.5 + abs, procedimiento]
Describe qué procedimiento seguirías para determinar los extremos absolutos de f(x,y) = y² sen²(x+y) − x² en x²+y² ≤ 1.
Solución (E): teorema de valores extremos: (1) críticos en el interior x²+y²<1; (2) Lagrange sobre x²+y²=1; (3) comparar valores de f. No hace falta la Hessiana.
Método: abs + Lagrange (procedimiento).

### Ejercicio 5.42 (E p. 203) [5.5, Lagrange sobre círculo]  — MAXIMA
Sabiendo que f(x,y)=x−y alcanza extremos absolutos condicionados en S={x²+y²=1}, determina en qué puntos los alcanza.
Solución (E): F = x−y+λ(x²+y²−1); puntos (√2/2, −√2/2) con λ = −√2/2 (máximo, f=√2) y (−√2/2, √2/2) con λ=√2/2 (mínimo, f=−√2).
Método: Lagrange.

### Ejercicio 5.43 (E p. 204) [5.4 + 5.5, temperatura en disco]  — MAXIMA, !
La temperatura de una placa circular x²+y² ≤ 4 es T(x,y) = e^{x²} + e^{y²}. ¿Cuáles son la temperatura máxima y mínima?
Solución (E): crítico interior (0,0), T=2; Lagrange sobre x²+y²=4: (0,±2), (±2,0) con T=1+e⁴ ≈ 55.598; (±√2,±√2) con T=2e² ≈ 14.78. **Mínimo 2 en (0,0); máximo 1+e⁴ en (0,±2) y (±2,0).** (Verificado con sympy.)
Método: abs (interior + frontera con Lagrange).

### Ejercicio 5.44 (E p. 206) [5.5, Lagrange, puntos críticos restringidos]  — MAXIMA
Sea f(x,y) = x²+y. Calcula, mediante Lagrange, los puntos críticos de f cuando nos restringimos a (x,y) con 2x−y=0.
Solución (E): F = x²+y+λ(2x−y); λ=1, x=−1, y=−2. Único punto crítico (−1,−2).
Método: Lagrange.

### Ejercicio 5.45 (E p. 206) [optimización con una variable, sin multiplicadores]
Tubería entre A=(0,0) y B=(300,100) en riberas de un río (franja 0 ≤ y ≤ 100). El coste bajo el río es el triple que en tierra. ¿Cuál debe ser el trazado si la tubería es recta al cruzar el río y sigue las riberas?
Solución (E): cruce en P=(x,100); coste k(300−x) + 3k√(x²+100²). Derivando (con k fijo): x = 25√2; comprobación con h″ > 0 y valores en los extremos (h(0)=600, h(300)≈948.68, h(25√2)=300+200√2≈582.84).
Método: optimización de una variable (sin Lagrange).

### Ejercicio 5.46 (E p. 208) [5.5, Lagrange en ℝ³]  — MAXIMA
Halla los puntos críticos de f(x,y,z)=x+y+z sujetos a x²+2y²+3z²=1. ¿Puedes determinar si en alguno se alcanza un extremo absoluto condicionado?
Solución (E): F = x+y+z+λ(x²+2y²+3z²−1); λ=±√66/12. P₁ = (√66/11, √66/22, √66/33) (f = √66/6, máximo); P₂ = −P₁ (f = −√66/6, mínimo). Elipsoide cerrado y acotado ⇒ existen extremos absolutos. (Verificado con sympy.)
Método: Lagrange + teorema de valores extremos.

### Ejercicio 5.47 (E p. 209) [5.5, distancia a superficie]  — MAXIMA, !
Sabiendo que hay una distancia mínima entre (0,0,0) y la superficie z = xy+4, determínala.
Solución (E): minimizar f = x²+y²+z² (cuadrado de la distancia) con g = xy+4−z = 0. Puntos: (0,0,4) (f=16), (√3,−√3,1) y (−√3,√3,1) (f=7). Mínimo f = 7 ⇒ distancia mínima √7. (Verificado con sympy.)
Método: Lagrange (sobre el cuadrado de la distancia).

### Ejercicio 5.48 (E p. 211) [5.4, extremos en cuadrado]  — MAXIMA
Sea f(x,y) = x²−xy+y². Encontrar los valores máximo y mínimo que alcanza f en A = {|x| ≤ 1, |y| ≤ 1}.
Solución (E): interior: único crítico (0,0), mínimo relativo (H det 3>0, f_xx=2). Frontera: vértices (±1,±1), y puntos críticos de cada lado: (1,1/2), (−1,−1/2), (1/2,1), (−1/2,−1). Valores: f(0,0)=0, f(±1,∓1)=3, f(1,1)=1, f(1/2,1)=3/4 etc. **Mínimo 0 en (0,0), máximo 3 en (−1,1) y (1,−1).** (Verificado con sympy.)
Método: abs (interior + frontera, parametrizando cada lado).

## 4. X (exámenes resueltos, pruebas presenciales)

Índice de origen: `indice_examenes_1..4.md`. «pdf» = página PDF de `Examenes-resueltos-Calculo.pdf`. Comprobación: `pdftotext` sobre la página indicada (no se ha visto como imagen; PyMuPDF no está instalado).

| Examen (convocatoria) | Nº | pág. PDF | Enunciado resumido | Método | Comprobación |
|---|---|---|---|---|---|
| Feb 2010, 2ª sem. (Eléctrica) | PC4 | 4–5 | Puntos críticos de x³+y³+xy | crit | pp. 4–5 verificadas (texto) |
| Sept 2010 (Eléctrica) | Ej6 | 8 | Extremos absolutos de x−y en x²+y²=1 | Lagrange | verificada (texto p. 8) |
| sin cabecera (posible Sept 2010 otro modelo) | P1 | 9 | Distancia mín. y máx. del origen a la elipse 5x²+6xy+5y²=8 | Lagrange | **página escaneada, sin texto; no verificada** |
| Feb 2011, 1ª sem. (Mecánica A) | PC4 | 11 | ¿(0,0) crítico de x²−y²+2y? | crit | verificada |
| Feb 2011, 2ª sem. (Mecánica B) | Ej6 | 14–15 | Extremos de x³+y²−xy en (0,0),(1,−1),(1/6,1/12) con Hessiana | crit+H | verificada (p. 14) |
| Feb 2012, 2ª sem. (Mecánica B) | Ej6 | 23–24 | Máx. y mín. absolutos de x+y en x²+y²=1 | Lagrange | verificada (p. 23) |
| Sept 2012, original (Mecánica A) | PC4 | 25 | ¿f=x²y alcanza máximo absoluto en x²+y²=1? | abs | cabecera verificada; enunciado no comprobado en texto |
| Feb 2013, 1ª sem. (Mecánica A) | Pr6 | 33–34 | Paralelepípedo de volumen 1 m³ con área mínima/máxima | Lagrange | verificada (p. 33–34) |
| Feb 2014, Modelo A (Mecánica) | Ej6 | **42** (sol. 42–43) | Extremos relativos y absolutos de x³+y²−xy en (0,0),(1,−1),(1/6,1/12) | crit+H+abs | **verificada en p. 42** (el índice 1 dice 41: error) |
| Sept 2014, Modelo A | P4 | 46 | f=yeˣ sobre S={x+y=0}: cómo hallar extremos | Lagrange | cabecera verificada (p. 46) |
| Feb 2015, Modelo A | Ej6 | 51 | Extremos relativos de f=x²+y sujeta a 2x−y=0 | Lagrange | verificada (texto p. 51) |
| Feb 2016, Modelo B | Ej6 | 67–68 (enunc. 66) | Máx. y mín. absolutos de e^{x²}+e^{y²} en x²+y²≤4 | crit + Lagrange (frontera) | verificada (p. 66, 67–68) |
| Sept 2016, Modelo B | Ej6 | 75–76 | Extremos relativos de x³+3x²y−y³+27x (puntos (±3,±3)) | crit+H | verificada (p. 75–76) |
| Feb 2017, Modelo B | Ej6 | 83–84 | (x²−x)(y²−y) en [0,1]²: extremos relativos y absolutos | crit+abs | verificada (p. 83–84) |
| Feb 2018, Modelo B | Ej6 | 95 (enunc. 94) | x³+y³−3xy: extremos relativos y clasificación | crit+H | verificada (p. 94–95) |
| Sept 2018, Modelo A | P4 corta | 97 | ¿f=x²y³ alcanza máximo absoluto en 1≤x²+y²≤4? | abs | verificada (texto p. 97) |
| Electrónica 1 | Ej6 | 100 | f=cos x − xy²: plano tangente en (0,0,1), H, extremos relativos | crit+H | verificada (texto p. 100) |
| Examen 1 | Ej5 | 109 (sol. 110–111) | Extremos de f=x⁶+x³y+y³ (puntos (0,0) y (−1/∛12, 1/6)) | crit+H | verificada (texto p. 109) |
| Examen 4 (elaborado con asignaturas similares) | Ej6 | **119** (sol. 120–121) | Máximos y mínimos de f=5+x²y² | crit+abs | enunciado verificado en p. 119 (el índice 4 dice 121: error); solución en p. 121 |
| Sept 2017 | Ej6 | 134 | Lagrange: extremos de f=xy sobre x²+y²=1 | Lagrange | verificada (p. 134) |
| Feb 2017, 2ª sem. | Ej6 | 136 | Extremos relativos de f=4xy−2y²−x³+1 | crit+H | verificada (p. 136) |
| Sept 2018, Modelo B (Mecánica) | Ej6 | 139 | Lagrange: extremos absolutos de f=x+y sobre x²+y²=1 | Lagrange | verificada (p. 139); el índice indica «sin solución» |
| Feb 2018, 2ª sem. | P3 corta | 140 | V/F: f diferenciable con ∇f(a,b)=0 ⇒ extremo relativo (falso) | teoría | solución en p. 140 (cabecera) |
| Feb 2019, 1ª sem. | Ej6 | 152 | f=xy(5x−15+y): ∇f(2,−3) y puntos críticos | crit | verificada (texto p. 152) |

Descartadas por ser sólo Hessiana, diferenciabilidad o una variable: filas de índice con tema 4.x/5.x «Hessiana» (p. 38, 50, 74, 102, 142, 144), diferenciabilidad (p. 54–61, 71, 79, 90, 98, 115) y extremos de una variable (p. 2, 19, 40, 85, 104, 122–123, 127). Duplicados: el Feb 2014 A (p. 42) aparece en el índice 1 (como 41) y en el 2 (como 42); el Examen 4 Ej6 aparece en el índice 3 (p. 119) y en el 4 (p. 121) → se usan 42 y 119.

## 5. Faltas o dudas

1. **S y L**: no hay pasaje equivalente en `stewart.txt` (cap. 14 de varias variables ausente) ni en `larson.txt` (sin capítulo de funciones de varias variables). Hace falta un tomo de varias variables para cubrir esto con S/L.
2. **Ley de ≠ en U**: el símbolo ≠ no sale en la extracción de los teoremas de Lagrange (pp. 226 y 228: «∇g(a,b) = 0» en el texto). Confirmar en el PDF; la hipótesis correcta es ∇g ≠ 0.
3. **U Ej. 5.16 (p. 215)**: la fórmula está rota (`15 x3`); no transcrita.
4. **U Ej. 5.20 (p. 221–222)**: la matriz de (1,0) sale como «−4 0 / 0 2» (inferida a partir de d = −8); verificado con sympy.
5. **U autoevaluación 8 (p. 233)**: la matriz Hf(0,1) sale rota («11 / 12»); no transcrita. Revisar en PDF.
6. **E 5.30**: la fórmula sale como «xy x²+y²»; se interpreta como xy(x²+y²) a partir de las derivadas del desarrollo.
7. **E 5.29, 5.48**: algunos valores y puntos de la extracción están rotos (p. ej. en 5.48 f(P₅) aparece como «4»; la lectura correcta, verificada, es 3/4). Interpretado.
8. **E 5.45**: el enunciado se refiere a una tubería con coste triple bajo el río; la solución es una minimización en una variable, sin Lagrange; se incluye porque aparece en el bloque de extremos.
9. **X**: páginas tomadas de los índices y comprobadas con `pdftotext` (no como imagen). No verificadas: p. 9 (escaneada, sin texto, Sept 2010 otro modelo, P1 distancia a elipse) y p. 25 (solo cabecera, enunciado no comprobado en texto). Errores de los índices corregidos: Feb 2014 A Ej6 es p. 42 (no 41); Examen 4 Ej6 es p. 119 (no 121).
10. **U §5.5, Ej. 5.23**: solo planteamiento; la resolución está en E 5.40.
11. **Figuras**: candidatas listadas en §1, pendientes de recorte con `herramientas/extraer_figura.py` (no hecho aquí).
12. **Verificación**: los cálculos de E y U se han comprobado con sympy (ver ejercicios marcados «verificado»). La afirmación de Ej. 5.22 de U (valores 1 y 2) se ha reproducido a mano, no con sympy.
