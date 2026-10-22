# Dossier 5.2 «Regla de la cadena. Teorema del valor medio» (U §5.2, pp.194-203)
Páginas: U impresa = PDF+2 (§5.2 empieza en p.194 = PDF 192; §5.3 empieza en p.204 = PDF 202, confirmado). E impresa = PDF. X = página PDF de Examenes-resueltos-Calculo.pdf (verificadas en imagen salvo indicación). S y L NO tienen apartado de varias variables (ver §2). El tema depende de U, E y X.

## 1. U §5.2 (pp.194-203)

### 1.1 Motivación y objetivos (p.194, PDF 192)
- 5.2.1 Motivación: «Estos resultados se pueden extender a funciones diferenciables.» Objetivos: «Saber aplicar la regla de la cadena.» / «Interiorizar el contenido y la importancia del teorema del valor medio.»
- 5.2.2 (p.194): «la suma f + g, el producto f · g y el producto por un escalar cf de funciones f, g diferenciables en un punto ā ... son funciones también diferenciables en este punto.» Funciones constantes: diferencial = aplicación lineal idénticamente nula.

### 1.2 Reglas de la diferencial (p.195, PDF 193)
- Literal: «D(f + g)(ā) = Df(ā) + Dg(ā), D(cf)(ā) = cDf(ā), D(f · g)(ā) = Df(ā)g(ā) + f(ā)Dg(ā)», c ∈ ℝ.
- Cociente (p.195): «f/g ... es diferenciable si g(ā) ≠ 0 y se tiene D(f/g)(ā) = [Df(ā)g(ā) − f(ā)Dg(ā)] / (g(ā))²».
- Nota U: «lo único nuevo es el hecho de que las funciones sean diferenciables porque su diferencial se calcula mediante derivadas parciales». Recuerda Df(a)(x) = ∇f(a)·x.
- **Ejemplo 5.5** (pp.195, PDF 193): f = x + 2y, g = y/(x+1) en (0,0) escritas con m(x,y)=x, j(x,y)=y: Dm(0,0)(h,k)=h, Dj(0,0)(h,k)=k; Df(0,0)(h,k)=h+2k; Dg(0,0)(h,k) = [k·(0+1) − 0·h]/(0+1)² = k. Comentario U: «resulta más complicado que calcular directamente el gradiente... sin embargo, estas reglas ... son muy importantes para ... desarrollos teóricos».

### 1.3 Composición y derivada en t (pp.196-199)
- p.196 (PDF 194), Fig. 5.2 (diagrama de f(g(t),h(t))): «df/dt (g(t), h(t)) = ∂f/∂x (g(t), h(t)) g′(t) + ∂f/∂y (g(t), h(t)) h′(t).» Las variables x, y son «variables mudas».
- **Ejemplo 5.6** (p.197, PDF 195): derivada respecto a t de f(eᵗ, 1+t²), f(x,y)=√(x+2y). Resultado U: df/dt = [1/(2√(eᵗ+2(1+t²)))]·eᵗ + [1/√(eᵗ+2(1+t²))]·2t. (Verificado en imagen; la raíz cubre x+2y.)
- p.197 (PDF 195), Fig. 5.3 (diagrama de f(g(u,v),h(u,v))): derivada parcial de f respecto a u y a v con dos sumandos cada una (ver p.198).
- p.198 (PDF 196): «∂f/∂u (g(u,v),h(u,v)) = ∂f/∂x (g(u,v),h(u,v)) ∂g/∂u (u,v) + ∂f/∂y (g(u,v),h(u,v)) ∂h/∂u (u,v)» (análoga para v). Regla general del diagrama: «la derivada con respecto a una variable de la base tendrá tantos sumandos como caminos desde la base hasta la función en el vértice superior ... cada uno de esos sumandos será el producto de las derivadas de las funciones y variables que determinan el camino.»
- **Regla de la cadena para función de dos variables** (p.198, PDF 196), literal: «Si g y h son funciones diferenciables en ā = (a1, ..., an) y f es una función de dos variables diferenciable en (g(a1, ..., an), h(a1, ..., an)), entonces f(g, h) es diferenciable en ā y se verifica ∇(f(g, h))(ā) = ∇f(g(ā), h(ā)) [∇g(ā); ∇h(ā)].» U añade: ∇f es 1×2, la matriz es 2×n (filas ∇g, ∇h); si n=1 la matriz es (g′; h′) y se recupera d/dx f(g(x),h(x)).
- **Ejemplo 5.7** (p.199, PDF 197): d/dx f(x, h(x)) = ∇f(x,h(x))·(1, h′(x)) = ∂f/∂x (x,h(x)) + ∂f/∂y (x,h(x)) h′(x). Particular f=xy², h=eˣ: (2x+1)e^{2x}. (Verificado.)
- **Ejemplo 5.8** (p.199, PDF 197): f(x,y)=2x+2y, g(u,v)=uv, h(u,v)=sen u+3: ∇(f(g,h))(0,0) = ∇f(0,3)·[∇g(0,0); ∇h(0,0)] = (2,2)·[[0,0],[1,0]] = (2,0). (Verificado.)
- **Regla de la cadena general** (p.200, PDF 198), literal: «Si g1, ..., gm son funciones diferenciables en ā = (a1, ..., an) y f es una función de m variables diferenciable en (g1(ā), ..., gm(ā)), entonces f(g1, ..., gm) es diferenciable en ā y se verifica ∇(f(g1, ..., gm))(ā) = ∇f(g1(ā), ..., gm(ā)) [∇g1(ā); ...; ∇gm(ā)].» U: «generaliza la regla de la cadena para las funciones de una variable ... porque en ese caso el gradiente coincide con la derivada.» Nota: U da la relación con gradiente y no con diferencial, pero Df(ā)(h) = ∇f(ā)·h.

### 1.4 Teorema del valor medio en varias variables (pp.201-203)
- **Definición 5.5** (p.201, PDF 199), segmento: «Llamaremos segmento que une los puntos (a1, ..., an) y (b1, ..., bn) al conjunto formado por los puntos (x1, ..., xn) de la forma (x1, ..., xn) = {(1 − λ)(a1, ..., an) + λ(b1, ..., bn)}, λ ∈ [0, 1].» Ejemplo U: el segmento entre 0 y 1 son los puntos x ∈ [0,1]. En ℝ²: (x1,x2) ∈ segmento si existe λ∈[0,1] con x1 = (1−λ)a1 + λb1, x2 = (1−λ)a2 + λb2 (ecuación (5.4)), Fig. 5.4 (p.201).
- **Definición 5.6** (p.202, PDF 200), convexo: «Un subconjunto D de ℝⁿ se dice convexo si para cualquier par de puntos de D, el segmento que los une está contenido en D.» U: discos, bolas, rectas y planos son convexos; la circunferencia no. Fig. 5.5 (p.202): conjunto convexo y no convexo.
- **Teorema del valor medio** (p.202, PDF 200), literal: «Sea f : D ⊂ ℝ² → ℝ una función continua y con derivadas parciales continuas en D. Si el segmento que une los puntos (a1, a2) y (b1, b2) de D está contenido en D, entonces existe un punto de ese segmento (c, d) tal que f(a1, a2) − f(b1, b2) = ∇f(c, d) · (a1 − b1, a2 − b2).» (U no enuncia la versión en ℝⁿ; solo ℝ².)
- Consecuencias (pp.202-203, PDF 200-201), literal: «Si las dos componentes del gradiente son estrictamente positivas en un conjunto convexo A entonces f(a1, a2) > f(b1, b2) para a1 > b1, a2 > b2.» Análogo con negativas y «<». Interpretación: en un convexo con gradiente de componentes positivas, moverse en la dirección de cualquier vector del primer cuadrante aumenta f.
- **Ejemplo 5.9** (p.203, PDF 201): f(x,y)=x³+y³, ∇f(x,y)=(3x², 3y²); ambas componentes > 0 si xy ≠ 0 (en los ejes xy = 0). Fig. 5.6: gráfica de f. (Verificado; el ≠ está en la imagen.)
- U no enuncia el criterio de monotonía en ℝⁿ más allá de estas consecuencias ni el TVM en ℝⁿ general.

Nota: §5.3 (Teorema de la función implícita) empieza en p.204 (PDF 202) y no entra en este dossier.

Figuras de U en esta sección (candidatas a recorte con extraer_figura.py, pág. PDF = impresa − 2): Fig. 5.2 (p.196, PDF 194), 5.3 (p.197, PDF 195), 5.4 (p.201, PDF 199), 5.5 (p.202, PDF 200), 5.6 (p.203, PDF 201).

## 2. S y L: apartado equivalente
- **No hay equivalente** en varias variables: stewart.txt y larson.txt son de una variable (no aparecen «gradiente» ni regla de la cadena en ℝⁿ; el libro de Larson remite a otro volumen para varias variables).
- Equivalentes de una variable (solo como refuerzo de la idea de regla de la cadena y TVM):
  - S §3.4 «Regla de la cadena», pp.199-207 (cabeceras «SECCIÓN 3.4 REGLA DE LA CADENA 199» … 207).
  - S §4.2 «Teorema del valor medio», pp.284-289 (cabeceras «284 CAPÍTULO 4 APLICACIONES DE LA DERIVADA» y «SECCIÓN 4.2 TEOREMA DEL VALOR MEDIO 285»).
  - L §2.4 «La regla de la cadena», pp.129-139 (impresa = PDF−17; PDF 146-156).
  - L §3.2 «El teorema de Rolle y el teorema del valor medio», pp.170-175 (PDF 187-192).
- No se ha leído ni extraído un extracto de S/L para este tema porque su apartado no cubre ℝⁿ; el formato S/L de extractos se hará solo si el redactor lo pide.

## 3. E: ejercicios de §5.2 (E 5.13-5.22)
Rango: E 5.13 (p.179) a E 5.22 (pp.185-186). **E 5.23 (p.186) ya es §5.3 (implícita): fuera de este dossier.**
Subsección: 5.13-5.14 → §5.2.2 (reglas de la diferencial y plano tangente de f+g, fg, f/g); 5.15-5.19 → §5.2.2 (regla de la cadena); 5.20 → §5.2.3 (TVM en ℝ²); 5.21-5.22 → §5.2.3 (signo del gradiente y crecimiento).
Verificado en imagen: E pp.180-181 y 185-186. Resto (pp.179, 182-184) en texto limpio y cálculos con sympy.

**Ejercicio 5.13** (E p.179, PDF 179) [§5.2.2, reglas de la diferencial]
«Si f y g son funciones de dos variables diferenciables en un punto (a, b), entonces el gradiente en (a, b) de la función producto fg verifica: a) ∇(fg)(a,b) = ∇f(a,b)∇g(a,b). b) ∇(fg)(a,b) = ∇f(a,b) + ∇g(a,b). c) ∇(fg)(a,b) = g(a,b)∇f(a,b) + f(a,b)∇g(a,b). d) ∇(fg)(a,b) = g(a,b)∇f(a,b) − f(a,b)∇g(a,b).»
Solución: c). Método: analogía con (fg)′ = f′g + fg′ (verificado: ∇(fg) = g∇f + f∇g).

**Ejercicio 5.14** (E pp.180-181, PDF 180-181) [§5.2.2, reglas suma/producto/cociente + plano tangente]
«De dos funciones diferenciables f, g: ℝ² → ℝ se sabe que f(1,2) = 9, g(1,2) = 2, ∇f(1,2) = (1, 9), y ∇f(1,2) = (2, 5). Calcula las ecuaciones del plano tangente a las gráficas de las funciones f+g, fg y f/g en el punto de su gráfica (1, 2, (f+g)(1,2)), (1, 2, (fg)(1,2)), y (1, 2, (f/g)(1,2)), respectivamente.»
(En el enunciado impreso la segunda ∇ debe ser ∇g(1,2)=(2,5); ver §5 Faltas.)
Método: plano z = h(a,b) + ∇h(a,b)·(x−a, y−b) con h = f+g, fg, f/g, aplicando las reglas de la diferencial en (1,2).
Resultados correctos (verificados con sympy): f+g: z = 11 + 3(x−1) + 14(y−2); fg: ∇=(20,63), z = 18 + 20(x−1) + 63(y−2); f/g: ∇=(−4, −27/4), z = 9/2 − 4(x−1) − (27/4)(y−2). (E imprime para fg ∇=(27,63) y para f/g ∇=(−9/4,−27/4): erratas, ver §5.)

**Ejercicio 5.15** (E pp.181-182, PDF 181-182) [§5.2.2, regla de la cadena: dos caminos]
«Sean las funciones dadas por f(x,y) = x(1 − y²) − y, x(t) = e^{2t}, y(t) = 1/t. A partir de ellas se define F mediante F(t) = f(x(t), y(t)). Se pide calcular la derivada de F(t) respecto a t mediante dos procedimientos: 1) sustitución de las expresiones de x(t) e y(t) y derivación posterior y 2) aplicando la regla de la cadena.»
Método: (1) F(t) = e^{2t}(1 − 1/t²) − 1/t, derivar; (2) F′ = ∂f/∂x·x′ + ∂f/∂y·y′ con ∂f/∂x = 1−y², ∂f/∂y = −2xy−1, x′=2e^{2t}, y′=−1/t². Resultado común (verificado): F′(t) = 2e^{2t}(1 − 1/t² + 1/t³) + 1/t².

**Ejercicio 5.16** (E p.182, PDF 182) [§5.2.2, cadena con rama g(x)=x]
«Sean f y h las funciones dadas por f(x,y) = x² + cos y y h(x) = e^{−x}. Se pide calcular, aplicando la regla de la cadena, la derivada respecto de x de la composición f(x, h(x)).»
Método: escribir f(g(x),h(x)) con g(x)=x y usar ∇f(g,h)·(g′,h′). Resultado: 2x + e^{−x} sen(e^{−x}) (verificado).

**Ejercicio 5.17** (E p.183, PDF 183) [§5.2.2, cadena con dos variables intermedias]
«Sea la función z dada por z(u,v) = f(u − 2v, 2v − u), donde f: ℝ² → ℝ es una función diferenciable, demuestra que 2 ∂z/∂u + ∂z/∂v = 0.»
Método: x(u,v)=u−2v, y(u,v)=2v−u; ∂z/∂u = ∂f/∂x − ∂f/∂y, ∂z/∂v = −2∂f/∂x + 2∂f/∂y; sustituir (verificado).

**Ejercicio 5.18** (E pp.183-184, PDF 183-184) [§5.2.2, gradiente de una composición en un punto]
«Sean f, g, h las funciones dadas por f(x,y) = x − y², g(u,v) = u + uv y h(u,v) = tg u. ¿Cuál es el gradiente de f(g,h) en (u,v) = (0,0)?»
Método: ∇(f(g,h))(0,0) = ∇f(g(0,0),h(0,0))·[∇g(0,0); ∇h(0,0)]. Resultado (1, 0) (verificado).

**Ejercicio 5.19** (E pp.184-185, PDF 184) [§5.2.2, composición con tres funciones intermedias]
«Calcula el gradiente en (u,v) = (1,0) de f(g(u,v), h(u,v), k(u,v)) para f(x,y,z) = 3x + y + z², g(u,v) = uv, h(u,v) = sen u + 3 y k(u,v) = eᵘ.»
Método: ∇f en (g,h,k)(1,0)=(0, 3+sen1, e) → (3,1,2e); matriz de gradientes en (1,0): [0,1]; [cos1,0]; [e,0]. Resultado (2e² + cos 1, 3) (verificado con sympy: cos(1)+2e², 3).

**Ejercicio 5.20** (E p.185, PDF 185) [§5.2.3, TVM: gradiente nulo ⇒ constante]
«El teorema del valor medio para funciones de una variable se utiliza para demostrar que una función con derivada cero en un intervalo es constante en ese intervalo. Muestra que una función continua f: ℝ² → ℝ con gradiente nulo en un conjunto convexo es constante en ese conjunto.»
Método: reducción al absurdo; TVM en el segmento entre dos puntos de imágenes distintas; ∇f(c)·(b−a) = 0.

**Ejercicio 5.21** (E p.185, PDF 185) [§5.2.3, signo del gradiente, opción abierta]
«Indica cómo se comportará la función f(x, y) = −x − y si nos movemos en la dirección de vectores del primer cuadrante.»
Método: ∇f = (−1,−1), componentes negativas ⇒ f decrece en la dirección de cualquier vector del primer cuadrante.

**Ejercicio 5.22** (E pp.185-186, PDF 185-186) [§5.2.3, opción múltiple con signo del gradiente]
«Encuentra la afirmación correcta para la función f(x, y) = x² − y³ si nos movemos en la dirección de vectores del primer cuadrante: a) Los valores de f decrecen. b) Los valores de f crecen. c) Los valores de f en el interior del segundo cuadrante decrecen. d) Ninguna de las anteriores.»
Solución: c). Método: ∇f = (2x, −3y²); en el 2.º cuadrante (x<0) ambas componentes ≤ 0 ⇒ decrece. Contraejemplo para a): f(2,1)=3 > f(1/2,1/2)=1/8 (verificado).

## 4. X: preguntas de examen relacionadas (regla de la cadena, composiciones, TVM)
Todas verificadas en imagen (página PDF). Las de una variable se marcan como refuerzo de §2.2/§2.5.

**Regla de la cadena en varias variables / composiciones con gradiente**
- X p.8 (Sept 2010, Eléctrica, pregunta 4, 1 punto): gradiente de f(x,y) = y·tg eˣ + cos²(x+y). Solución: ∇f = (y eˣ / cos² eˣ − 2cos(x+y)sen(x+y), tg eˣ − 2cos(x+y)sen(x+y)). Método: regla de la cadena en eˣ y en cos²(x+y).
- X p.20 (Feb 2012, 1ª sem., Mecánica A, pregunta 4): gradiente de f = x²e^{x+y} en (1,−1): (3,1). Método: producto + cadena en e^{x+y}. (La solución remite a «pp.219-220» de otro libro; el gradiente está en U §4.3, desde p.168.)
- X p.82 (Feb 2017, Modelo B, pregunta 4 corta): gradiente de f(x,y)=(x+y³)cos(πx²) en (1,0): (−1,0). Método: producto + cadena en cos(πx²). (Verificado con sympy.)
- X p.107-108 (Electrónica Industrial 4, ejercicio 6, 3 puntos): g(x,y)=x²y, f=ln g. Dominio {x≠0, y>0}; ∇g(1,1)=(2,1); ∇f(1,1)=(2,1) (verificado: f_x = 2x/x², f_y = 1/y); coseno del ángulo = 1. Método: ∇(ln g) = ∇g/g. (En el solucionario el segundo ∇ de g está mal copiado; cálculo correcto.)
- X p.143 (Sept 2018, Electrónica, ejercicio 6, 3 puntos): f=ln(36−x²−y²). (a) dominio: disco abierto de radio 6; (b) ∇f(1,5) = (−1/5, −1) (verificado); (c) f∘g con g(ρ,θ)=(ρcos θ, ρsen θ): f(g(ρ,θ)) = ln(36−ρ²) (verificado). Método: composición con coordenadas polares.

**Regla de la cadena en una variable (refuerzo §2.2; X usa la misma idea)**
- X p.25 (Sept 2012, Mecánica A, pregunta 1 corta): f(0)=1, f′(0)=−2, g(x)=f²(sen x): g′(0) = 2f(0)f′(0)cos 0 = −4 (verificado).
- X p.64 (Feb 2016, Modelo B, pregunta 2 corta, 1 punto): f derivable, g(2)=−1, f′(1)=2, f(x)=x·g(2x): calcular g′(2). Solución (verificada): f′(x) = g(2x) + 2x g′(2x); f′(1) = 2 = −1 + 2g′(2) ⇒ g′(2) = 3/2 (verificado).
- X p.122-123 (Examen 5, elaborado con exámenes de asignaturas similares, ejercicio 4): f derivable, f(0)=π, f′(0)=2; g(x)=cos(f(cos x)); g′(π/2): A) 0. Solución (p.123): g′(x) = sen(f(cos x))·f′(cos x)·sen x; g′(π/2) = sen(f(0))·f′(0) = 2 sen π = 0 (verificado; respuesta A).
- X p.144 (Feb 2018, 1ª sem., Electrónica, pregunta 2 corta): f(2)=π, f′(2)=3, g(x)=sen(f(5x²−8)); g′(√2) = −30√2 (verificado: cos(π)·3·10√2).

**Teorema del valor medio**
- X p.86 (Sept 2017, Modelo A, pregunta 4 corta, 1 punto): f:ℝ²→ℝ² con derivadas parciales positivas en todo ℝ²; ¿si x>x₀, y>y₀ se cumple f(x,y) > f(x₀,y₀)? Respuesta: «Es cierto», por el TVM en el segmento y convexidad de ℝ². Nota: la solución trata f como escalar (ver §5).
- X p.137 (Feb 2017, 1ª sem., pregunta 3 corta): «Enuncie el Teorema del Valor Medio (para funciones de una variable) y explique la interpretación geométrica.» Solución: remite a U pp.94-95 (§2.5; cross-ref, no es §5.2).
- X p.135 (Feb 2017, 2ª sem., pregunta 4 corta): Teorema de Rolle aplicado a f(x)=e^{(x+1)²} en [−2,0] (§2.5; cross-ref).

Fuera de este tema (no duplicar aquí): diferencial de (x+sen y)² (X pp.35, 44, 57) y gradiente/derivadas direccionales de §4 y §5.1 (ver dossier_5_1.md).

## 5. Faltas o dudas
- **E 5.14, enunciado**: aparece ∇f(1,2)=(2,5) dos veces; la segunda debe ser ∇g(1,2). **E 5.14, solución**: ∇(fg)(1,2) impreso (27,63), correcto (20,63) (= g∇f + f∇g = 2(1,9)+9(2,5)); ∇(f/g)(1,2) impreso (−9/4,−27/4), correcto (−4,−27/4) (= [2(1,9)−9(2,5)]/4 = (−16,−27)/4); plano f/g impreso z=9/2−9/4(x−1)−27/4(y−2), correcto z=9/2−4(x−1)−27/4(y−2). Verificado con sympy e imagen (pp.180-181). Para el HTML usar los valores correctos.
- **X p.86**: el enunciado da f:ℝ²→ℝ² y la desigualdad f(x,y)>f(x₀,y₀) solo tiene sentido para f escalar (o componente a componente). La solución razona como si f fuera real; el resultado es cierto para f:ℝ²→ℝ con parciales positivas (TVM), pero no lo he podido confirmar como enunciado vectorial. Revisar antes de usarlo como «respuesta modelo».
- **X p.107-108**: el solucionario escribe ∇g(1,1)=(2,1) dos veces (la primera debe ser ∇f(1,1)); valores correctos.
- **U**: pdftotext pierde el ≠ en p.195 (cociente: “g(ā) = 0” debe leerse g(ā) ≠ 0) y en p.203 (xy ≠ 0). El de p.203 está confirmado en imagen; el de p.195 por el sentido y por la condición de E 5.14 (imagen E p.180).
- **Imágenes no vistas**: U p.194 (PDF 192), p.196 (PDF 194), p.198 (PDF 196), p.200 (PDF 198), p.202 (PDF 200) solo en texto (limpio). E pp.179, 182-184 solo en texto; sus cálculos verificados con sympy.
- **Sin equivalente en S/L**: confirmado (solo una variable).
- **Exámenes fuera de §5.2** (no incluidos): diferencial de (x+sen y)² y diferenciabilidad (5.1, X pp.2-3, 17-18, 20-21, 26-27, 35, 44, 54-55, 57, 60-63, 71-72, 79-80, 90-92, 98, 115-125, 127-140); extremos con Lagrange (5.x posterior); función implícita (§5.3).
