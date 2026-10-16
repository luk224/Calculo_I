# Dossier Tema 3.4: Optimización. Extremos relativos y absolutos

Dossier de fuentes para el proyecto de Cálculo (UNED). Páginas: **U** = impresa (PDF − 2 en `ingenieros.txt`); **E** = impresa = PDF; **L** = impresa = PDF − 17; **S** = número de la cabecera impresa; **X** = página PDF de `Examenes-resueltos-Calculo.pdf`.
Convención: en los `.txt` la extracción cambia algunos símbolos («m» por «=», «w» por «≥», «v» por «≤», y se pierde la barra de «≠»). Los extractos restauran los símbolos; donde hay duda se indica en «Faltas o dudas».

---

## 1. Libro oficial U, §3.4 (pp. 125-134)

**Alcance real:** §3.4 ocupa pp. 125-134 (el título de §3.5 aparece al pie de la p. 134 y su texto empieza en la p. 135). CLAUDE.md indica pp. 125-133: hay que corregirlo.

### 3.4.1 Motivación (U p. 125)
- «Todos estamos acostumbrados a tomar decisiones para tratar de reducir los costes y aumentar los beneficios de nuestras actividades. A la rama de las matemáticas que se dedica a este tipo de problemas se la denomina Optimización.»
- Objetivos (p. 125): «…los conceptos de extremos relativos y absolutos para una función de una variable, el concepto de punto crítico y condiciones suficientes para calcular los extremos de funciones derivables.»

### 3.4.2 Extremos absolutos
- Contexto (U p. 125): «En la Proposición 1.15, al estudiar las propiedades de las funciones continuas definidas sobre intervalos cerrados, establecimos que alcanzan en ese intervalo los valores máximo y mínimo. Sin embargo… no dimos una definición rigurosa de máximo o mínimo. Tampoco facilitamos una forma para su cálculo.»

**Definición 3.4 (U §3.4.2, p. 126).** «La función f: D → ℝ tiene un mínimo absoluto en c si f(c) ≤ f(x) ∀x ∈ D. La función f: D → ℝ tiene un máximo absoluto en c si f(c) ≥ f(x) ∀x ∈ D. La función f: D → ℝ tiene un extremo absoluto en c si alcanza un máximo o un mínimo absoluto en c.»

**Definición 3.5 (U §3.4.2, p. 126).** «El punto c ∈ (a, b) es un punto crítico de la función continua f: [a, b] → ℝ si f′(c) = 0 o f no es derivable en c.»

**Proposición 3.4 (U §3.4.2, p. 126).** «Los extremos absolutos de una función continua f: [a, b] → ℝ se alcanzan en los extremos del intervalo o en los puntos críticos de f.»
- Nota del libro (p. 126): la continuidad es esencial. Contraejemplo: f(x) = 1/x si x ≠ 0 y f(0) = 0 en [−1, 1] no tiene extremos absolutos.

**Ejemplo 3.19 (U pp. 126-127).** f(x) = 4x³ − 3x² − 6x + 2 en [0, 2]. f′ = 12x² − 6x − 6 = 6(2x² − x − 1); críticos en x = 1 (x = −1/2 queda fuera). f(0) = 2, f(1) = −3, f(2) = 10. Mínimo absoluto −3 en x = 1; máximo absoluto 10 en x = 2.
- Aviso del libro (p. 127): «Un error habitual es confundir el punto en donde se alcanza el extremo con el valor extremo que se alcanza.»

**Ejemplo 3.20 (U pp. 127-128).** f(x) = |sen x| en [0, 2π]. Es f = sen x en [0, π] y f = −sen x en (π, 2π]. Críticos: π (no derivable), π/2 y 3π/2 (f′ = 0). Valores: f(0) = 0, f(π/2) = 1, f(π) = 0, f(3π/2) = 1, f(2π) = 0. Máximo absoluto 1 en π/2 y 3π/2; mínimo absoluto 0 en 0, π y 2π. **Figura 3.1** (p. 128, PDF 126): gráfica de |sen x| con sus extremos absolutos en [0, 2π].

**Ejemplo 3.21 (U pp. 128-129).** f(x) = x/(x² + 1) en (0, ∞). f′ = (1 − x²)/(x² + 1)²; único crítico x = 1; lím_{x→0⁺} f = 0 y lím_{x→∞} f = 0 (regla de Hopital). f(1) = 1/2 es el máximo absoluto; no hay mínimo absoluto. **Figura 3.2** (p. 129, PDF 127): «Gráfica de x/(x²+1) y su máximo absoluto en (0, ∞).»
- Aviso (p. 129): «Si f tiene máximo y mínimo absoluto en D su gráfica estará encerrada en una banda determinada por los extremos.»
- Aviso (p. 128): en intervalos abiertos no se puede evaluar en los extremos; se usan los límites, y no hay garantía de que se alcancen los extremos.

### 3.4.3 Extremos relativos (U desde p. 130)

**Definición 3.6 (U p. 130).** «La función f: D → ℝ alcanza un mínimo relativo en c si existe un intervalo I ⊂ D tal que f(c) ≤ f(x) ∀x ∈ I. La función f: D → ℝ alcanza un máximo relativo en c si existe un intervalo I ⊂ D tal que f(c) ≥ f(x) ∀x ∈ I. La función f: D → ℝ alcanza un extremo relativo en c si alcanza un mínimo o máximo relativo en c.»

**Ejemplo 3.22 (U p. 130).** f(x) = 1 + (x + 1)²(x − 3/4)/(4 − x²) (fórmula reconstruida del txt; confirmar en el PDF): no tiene extremos absolutos en (−2, 2), pero sí relativos. Figura al margen en p. 130.

**Proposición 3.5 (U p. 130).** «Sea f: D → ℝ una función continua y c ∈ D. Si existe ε > 0 tal que f es decreciente en (c − ε, c) y creciente en (c, c + ε), entonces f alcanza un mínimo relativo en c. Si existe ε > 0 tal que f es creciente en (c − ε, c) y decreciente en (c, c + ε), entonces f alcanza un máximo relativo en c.» (Es el criterio de la primera derivada en forma de monotonía.)

**Ejemplo 3.23 (U pp. 130-131).** f(x) = x si x < 1; f(x) = 1 − x si x ≥ 1. Es creciente antes de 1 y decreciente después, pero **no** tiene extremo relativo en 1. **Figura 3.3** (p. 131, PDF 129): «Gráfica de función creciente en (−∞, 1) y decreciente en (1, ∞) que no tiene extremo relativo en 1.»

**Proposición 3.6 (U p. 131).** «Los extremos relativos de una función continua f: [a, b] → ℝ se alcanzan en los extremos del intervalo o en los puntos críticos. Los extremos relativos de una función continua f: (a, b) → ℝ se alcanzan, de existir, en los puntos críticos de f.»

**Definición 3.7 (U p. 131).** «El punto c es un punto de silla para f si es un punto crítico de f pero f no alcanza un extremo relativo en c.»

**Proposición 3.7 (U p. 131), criterio de la segunda derivada.** «Sea f: (a, b) → ℝ dos veces derivable y c ∈ (a, b) tal que f′(c) = 0. Si f″(c) > 0, entonces f alcanza un mínimo relativo en c. Si f″(c) < 0, entonces f alcanza un máximo relativo en c.»

**Proposición 3.8 (U p. 132), orden superior.** «Si el orden de la primera derivada que no se anula en un punto crítico c es par, entonces f alcanza un máximo si es negativa y un mínimo si es positiva. Si el orden de la primera derivada que no se anula en un punto crítico c es impar, entonces f tiene un punto de silla en c.»

**Ejemplo 3.24 (U p. 132).** f(x) = x⁴ − 2x³. f′ = 4x³ − 6x² = x²(4x − 6): críticos 0 y 3/2. f″ = 12x² − 12x: f″(3/2) = 27 − 18 = 9 > 0 → mínimo relativo en 3/2. f″(0) = 0; f‴(x) = 24x − 12, f‴(0) = −12 ≠ 0 → orden impar → punto de silla en 0. **Figura 3.4** (p. 133, PDF 131): «Gráfica de f(x) = x⁴ − 2x³ con sus intervalos de crecimiento y decrecimiento, su extremo relativo y su punto de silla.»
- Aviso del libro (p. 133): «Una función puede tener infinitos extremos relativos y los valores en esos extremos pueden no coincidir» (ejemplo x·cos x).

**Ejemplo 3.25 (U pp. 132-133).** 100 m de tela para un recinto rectangular. Lados x y 50 − x; A(x) = x(50 − x), x ∈ [0, 50]. A′ = 50 − 2x, crítico x = 25; A″ = −2 < 0 → máximo relativo; A(0) = A(50) = 0 → máximo absoluto. Solución: cuadrado de 25 m de lado.

**Ejemplo 3.26 (U pp. 133-134).** 100 m de tela para un cuadrado (lado x) y un círculo con el resto. A(x) = x² + (50 − 2x)²/π, x ∈ [0, 25]. A′(x) = 2x − 4(50 − 2x)/π = 0 ⇔ x = 100/(4 + π) ≈ 14.0 (mínimo relativo, A″ = 2 + 8/π > 0). A(0) = 2500/π ≈ 795.77; A(25) = 625. Máximo absoluto en x = 0: toda la tela para el círculo.
- Comprobado con sympy: A(0) = 2500/π, A(25) = 625, A″ = 2 + 8/π.

**Figuras de U §3.4:** Fig. 3.1 (p. 128, PDF 126: |sen x|); Fig. 3.2 (p. 129, PDF 127: x/(x²+1)); Fig. 3.3 (p. 131, PDF 129: f sin extremo en 1); Fig. 3.4 (p. 133, PDF 131: x⁴ − 2x³). Recortes no generados en este encargo.

### Lo que U **no** enuncia por su nombre
- «Teorema de Fermat»: no aparece como tal. Está en Def. 3.5 + Prop. 3.6 (los extremos en un abierto están en puntos críticos). El teorema del valor extremo se cita de la Proposición 1.15 (U §1.4).
- «Máximo/mínimo local»: U dice «relativo».
- «Método del intervalo cerrado»: U lo aplica en los Ejemplos 3.19-3.20 (críticos, extremos, comparar valores) sin enunciarlo como receta.

---

## 2. Apartados equivalentes de S y L

### 2.1 Stewart (Cálculo de una variable. Trascendentes tempranas), cap. 4 «Aplicaciones de la derivada»

Números de página = cabecera impresa. El txt de S no tiene un offset fijo: se usa el número de la cabecera «NNN CAPÍTULO 4» o «SECCIÓN 4.x … NNN».

| Apartado S | Pág. | Contenido | Extracto / resumen |
|---|---|---|---|
| §4.1 «Valores máximos y mínimos» | 273-283 | Máximo/mínimo absoluto y local; teorema del valor extremo; Fermat; método del intervalo cerrado | Def.: «…valor máximo absoluto de f sobre D si f(c) ≥ f(x) para toda x en D» (p. 274). |
| Teorema del valor extremo (S 4.1) | p. 275 | f continua en [a, b] ⇒ alcanza máximo y mínimo absolutos | «Si f es continua sobre un intervalo cerrado [a, b], entonces f alcanza un valor máximo absoluto f(c) y un valor mínimo absoluto f(d) en [a, b].» |
| Teorema de Fermat (S 4.1) | p. 276 | Máximo o mínimo local en x = c con f′(c) existente ⇒ f′(c) = 0 | Resumen: si f tiene un extremo local en c y f′(c) existe, entonces f′(c) = 0. Ejemplo 5 de la sección (pp. 277-278): f(x) = x³ tiene f′(0) = 0 sin extremo en 0. |
| Método del intervalo cerrado (S 4.1) | pp. 278-280 | Pasos para máximo/mínimo absolutos en [a, b] | Resumen: (1) valores en los números críticos de (a, b); (2) valores en los extremos; (3) el mayor es el máximo absoluto y el menor el mínimo absoluto. Ejemplo 9 (pp. 279-280). |
| Ejemplo 1 (S 4.1) | p. 275 | f(x) = cos x: máximo absoluto y local igual a 1 | Ilustra los dos tipos de extremos. |
| §4.3 «Cómo afecta la derivada la forma de una gráfica» | 291-297 | Crecimiento y concavidad; prueba de la 1ª y de la 2ª derivada | Prueba de la 1ª derivada (pp. 291-292): si f′ cambia de + a − en c, máximo local; si cambia de − a +, mínimo local (la cabecera de p. 291 no se ha extraído: verificar). Prueba de la 2ª derivada (p. 295): f′(c) = 0 y f″(c) > 0 ⇒ mínimo local; f″(c) < 0 ⇒ máximo local; f″(c) = 0 no decide (pp. 295-296). |
| §4.7 «Problemas de optimización» | 325-337 | Estrategia para problemas aplicados | Ejemplo 1 (p. 326): agricultor con 2400 pies de material para una barda; pasos «comprenda el problema», «introduzca la notación», etc. |

Uso para 3.4: S 4.1 (extremos y método del intervalo cerrado) + S 4.3 (criterios de la 1ª y 2ª derivada) + S 4.7 (optimización). No se ha localizado en S el caso de x⁴ − 2x³ con «punto de silla» (no es necesario).

### 2.2 Larson (Cálculo Tomo 1), cap. 3 «Aplicaciones de la derivada»

Números de página = PDF − 17 (verificado en PDF 179 = p. 162 y PDF 208 = p. 191).

| Apartado L | Pág. | Contenido | Extracto / resumen |
|---|---|---|---|
| §3.1 «Extremos en un intervalo» | 161-169 | Extremos absolutos, relativos, números críticos, estrategia en intervalo cerrado | Def. de extremos (p. 162): «Sea f definida en un intervalo I que contiene a c. 1. f(c) es el mínimo de f en I si f(c) ≤ f(x) para toda x en I. 2. f(c) es el máximo de f en I si f(c) ≥ f(x) para toda x en I.» (símbolos reconstruidos). |
| Teorema 3.1 (valor extremo) | p. 162 | f continua en [a, b] ⇒ tiene mínimo y máximo en el intervalo | «Si f es continua en el intervalo cerrado [a, b], entonces f tiene tanto un mínimo como un máximo en el intervalo.» |
| Definición de extremos relativos | p. 163 | Máximo/mínimo local en un intervalo abierto | «Si hay un intervalo abierto que contiene a c en el cual f(c) es un máximo, entonces f(c) recibe el nombre de máximo relativo de f…» |
| Ejemplo 1 (valor de f′ en extremos relativos) | pp. 163-164 | (a) f′(3) = 0; (b) f = abs(x), f′(0) no existe; (c) f = sen x, f′ = 0 en π/2 y 3π/2 | Ilustra que en un extremo relativo f′ = 0 o no existe (figura 3.3). |
| Definición de número crítico | p. 164 | c crítico si f′(c) = 0 o f no es derivable en c | «Sea f definida en c. Si f′(c) = 0 o si f no es derivable en c, entonces c es un punto crítico de f.» |
| Teorema 3.2 (extremos en puntos críticos, Fermat) | p. 164 | Extremo relativo ⇒ punto crítico. Demostración con el signo del cociente incremental | «Si f tiene un mínimo relativo o un máximo relativo en x = c, entonces c es un punto crítico de f.» Se atribuye a Fermat (cuadro al margen). |
| Estrategia para extremos en un intervalo cerrado | p. 165 | 1. Críticos en (a, b); 2. evaluar f en los críticos; 3. evaluar f en los extremos; 4. el menor valor es el mínimo y el mayor el máximo | Estrategia literal de L (p. 165). |
| Ejemplo 2 | p. 165 | f(x) = 3x⁴ − 4x³ en [−1, 2]: críticos 0 y 1; mínimo f(1) = −1; máximo f(2) = 16 | Ejemplo con tabla. |
| Ejemplo 3 | p. 166 | f(x) = 2x − 3x^{2/3} en [−1, 3]: mínimo f(−1) = −5; máximo f(0) = 0 | Punto crítico no derivable. |
| Ejemplo 4 | pp. 166-167 | f(x) = 2 sen x − cos 2x en [0, 2π] | Extremos con trigonometría. |
| §3.3 «Funciones crecientes y decrecientes y el criterio de la primera derivada» | 177-185 | Teorema 3.5 (crecimiento por el signo de f′); Teorema 3.6 (criterio de la 1ª derivada) | Teorema 3.6 (p. 179): «Sea c un punto crítico de una función f que es continua en un intervalo abierto I que contiene a c. Si f es derivable en el intervalo, excepto posiblemente en c, entonces f(c) puede clasificarse como sigue. 1. Si f′(x) cambia de negativa a positiva en c, entonces f tiene un mínimo relativo en (c, f(c)).» (El punto 2, máximo, está en la misma página.) |
| §3.4 «Concavidad y criterio de la segunda derivada» | 187-193 | Teorema 3.7 (concavidad); Teorema 3.9 (criterio de la 2ª derivada) | Teorema 3.9 (p. 191): «Sea f una función tal que f′(c) = 0 y la segunda derivada de f existe en un intervalo abierto que contiene a c. 1. Si f″(c) > 0, entonces f tiene un mínimo relativo en (c, f(c)). 2. Si f″(c) < 0, entonces f tiene un [máximo] relativo en (c, f(c)).» **El txt pone «mínimo» en el punto 2; ver «Faltas o dudas».** Ejemplo 4 (p. 191): f(x) = −3x⁵ + 5x³: mínimo relativo en (−1, −2), (0, 0) no es extremo, máximo relativo en (1, 2). La figura 3.30 de la misma página dice «f″(c) < 0 ⇒ máximo relativo». |
| §3.7 «Problemas de optimización» | 215-223 | Estrategia general y ejemplos | Ejemplo 1 (pp. 215-216): caja abierta con base cuadrada y superficie 108 pulg²: V = x²h; S = x² + 4xh = 108 ⇒ V(x) = 27x − x³/4 ⇒ x = 6 y h = 3 (pulgadas). La estrategia general viene después (no transcrita). |

Mapeo de L: L 3.1 (extremos y estrategia en intervalo cerrado) ↔ U Prop. 3.4 y 3.6, Ejemplos 3.19-3.20; L 3.3 (criterio de la 1ª derivada) ↔ U Prop. 3.5; L 3.4 (criterio de la 2ª derivada) ↔ U Prop. 3.7; L 3.7 (optimización) ↔ U Ejemplos 3.25-3.26.

---

## 3. Ejercicios de E (libro de ejercicios 24-25) de la sección 3.4

### 3.1 Mapa: qué ejercicios son de cada subsección

Confirmado con el texto de E (numeración «Ejercicio 3.xx» y contenido). Las páginas E coinciden con el PDF. El Tema 3 de E empieza en p. 87 (CLAUDE.md); el bloque 3.29-3.48 ocupa E pp. 114-134.

| Subsección | Ejercicios E | Comentario |
|---|---|---|
| **3.3** Interpolación | 3.28 (E p. 113) | Único de la franja 3.28-3.48 que no es de 3.4 (los 3.21-3.27 son de interpolación, no revisados aquí). |
| **3.4** Extremos y optimización | **3.29, 3.30, 3.31, 3.32, 3.33, 3.34, 3.35, 3.36, 3.37, 3.38, 3.44** | Extremos relativos y absolutos, criterios de la 1ª y 2ª derivada, optimización. 3.30 y 3.36 mencionan además puntos de inflexión o f″ (3.5). |
| **3.5** Concavidad y convexidad | **3.39, 3.40, 3.41, 3.42, 3.45, 3.48** | Estudio de f″, puntos de inflexión, convexidad. 3.43 mezcla extremos (3.4) con inflexión (3.5). |
| **Mixtos / representación** | **3.43, 3.46, 3.47** | 3.46: representación completa (dominio, asíntotas, f′, f″). 3.47: construir funciones con propiedades de crecimiento y concavidad. Requieren 3.4 + 3.5 y asíntotas. |

Marca «MÁXIMA» en E (uso del software Maxima): 3.31, 3.32, 3.33, 3.39, 3.44, 3.46.

### 3.2 Enunciados, método y erratas

Clasificación entre corchetes. Las figuras de f′ del enunciado no están transcritas en el txt; se describen los signos que da la solución.

**Ejercicio 3.29** (E p. 114) [3.4]
«De una función f: ℝ → ℝ tres veces derivable conocemos la gráfica de su derivada primera f′ (figura no transcrita). Razona si alguna afirmación es correcta entre las siguientes. a) f alcanza un valor mínimo relativo en x = 0. b) f alcanza un valor máximo relativo en x = 0. c) f es siempre creciente. d) Ninguna de las anteriores.»
- Método: f′ < 0 en (−∞, 0) y f′ > 0 en (0, +∞) ⇒ criterio de la 1ª derivada: mínimo relativo en 0. Respuesta **a)**.

**Ejercicio 3.30** (E p. 114) [3.4, con idea de 3.5]
«Sea f(x) = ax³ + bx² + cx + d, con a ≠ 0. ¿Es cierto que f tiene exactamente un máximo local y un mínimo local en su dominio, cualesquiera que sean a, b, c, d?»
- Método: f′ = 3ax² + 2bx + c (grado 2). Puede no tener raíces (f = 2x³ + 6x) o tener raíz doble (punto de inflexión, f = x³). **No** es cierto.

**Ejercicio 3.31** (E pp. 115-116) [3.4] MÁXIMA
«Un móvil recorre un espacio s(t) = t⁴ − 8t³ + 18t², expresado en metros, siendo t el tiempo en segundos. Supongamos que el instante inicial es t = 0 y que t ∈ [0, +∞). ¿Cuáles son las expresiones de su velocidad y de su aceleración? ¿Alcanza la velocidad algún valor máximo o mínimo relativo? ¿Cuándo? ¿Y absolutos?»
- Método: v = s′ = 4t³ − 24t² + 36t; a = s″ = 12t² − 48t + 36 = 12(t − 1)(t − 3). Extremos de v en los ceros de a y en t = 0: mínimo relativo en 0, máximo relativo en 1 (v = 16), mínimo relativo en 3 (v = 0). Como v → +∞, no hay máximo absoluto; mínimo absoluto en t = 0 y t = 3 (v = 0).
- **Erratas:** la solución escribe a(t) = (t − 1)(t − 3) (falta el factor 12; no afecta a los signos). La tabla de signos aparece desordenada en el txt.

**Ejercicio 3.32** (E pp. 116-117) [3.4] MÁXIMA
«Sea f(x) = (1 − x²)/(x + 3). ¿Dónde alcanza los extremos relativos y absolutos en el intervalo [−1, 1]? ¿Cuáles son esos valores extremos?»
- Método: crítico en x₁ = −3 + √8 (∈ [−1, 1]; el otro, −3 − √8, se descarta). f″(x) = −16/(x + 3)³; f″(x₁) = −√2/2 < 0 ⇒ máximo relativo con f(x₁) = 6 − 2√8 ≈ 0.3431. f(±1) = 0 ⇒ mínimos absolutos en −1 y 1. Máximo absoluto en x₁.
- Verificado con sympy: f″(x₁) = −√2/2 y f(x₁) = 6 − 2√8 = 6 − 4√2.
- **Errata/duda:** en el txt el valor de f″(−3 + √8) aparece ilegible («−√2/8»); el cálculo da −√2/2. Confirmar en el PDF (E p. 117).
- Es el mismo ejercicio que la pregunta de examen **X Feb 2010, 1ª sem., Eléctrica, Ej. 5** (PDF 2).

**Ejercicio 3.33** (E pp. 117-118) [3.4] MÁXIMA
«La distancia en metros de una partícula a un punto fijo P en función del tiempo viene dada por s(t) = at³ + bt² + ct + d, t ∈ [0, 6], con t en segundos. Se sabe que la partícula está en P en t = 0 y que después de un segundo se encuentra a 10 metros. También se sabe que la velocidad de la partícula es nula en t = 0 y t = 5. Determina los valores de a, b, c y d y los valores extremos relativos y absolutos de la distancia de la partícula a P en [0, 6].»
- Método: sistema s(0) = 0, s(1) = 10, ṡ(0) = 0, ṡ(5) = 0 ⇒ a = −20/13, b = 150/13, c = d = 0. Puntos críticos t = 0 y t = 5. s(0) = 0 (mínimo absoluto); s(5) = 1250/13 ≈ 96.15 (máximo absoluto y relativo; s″(5) = −300/13 < 0); s(6) = 1080/13 ≈ 83.08 (mínimo relativo en el extremo derecho, porque s decrece en [5, 6]).
- Verificado con sympy (coeficientes, s(0), s(1), s(5), s(6), s″(5)).

**Ejercicio 3.34** (E p. 119) [3.4]
«Sea f(x) = |x − 1|. ¿Tiene un extremo en x = 1? ¿Es máximo o mínimo?»
- Método: no derivable en 1; f ≥ 0 y f(1) = 0 ⇒ mínimo absoluto en 1.
- **Duda de extracción:** la solución dice «derivable si x = 1»; debe ser x ≠ 1 (pdftotext pierde la barra de ≠). Confirmar en el PDF.

**Ejercicio 3.35** (E pp. 119-120) [3.4]
«Sea f(x) = x^{2/3}. ¿Alcanza un extremo relativo en x = 0? Si es así, ¿de qué tipo?»
- Método: f′(0⁻) = −∞ y f′(0⁺) = +∞ (no derivable en 0); f(x) ≥ 0 = f(0) ⇒ mínimo absoluto y relativo en 0. Caso de extremo en un punto no derivable.

**Ejercicio 3.36** (E p. 120) [3.4; c) toca f″]
«La gráfica de la derivada de una función f dos veces derivable, con dominio ℝ, aparece en la figura (no transcrita). Razona si alguna de las siguientes afirmaciones es correcta: a) f tiene dos puntos críticos, pero un solo extremo relativo. b) f tiene dos extremos relativos. c) La ecuación f″(x) = 0 no tiene soluciones reales.»
- Método: puntos críticos = cortes de f′ con el eje x (x = −2 y x = 1). En −2, f′ pasa de − a +: mínimo relativo. En 1, f′ no cambia de signo: no hay extremo. **a)** correcta. **c)** falsa: f′ tiene extremos relativos en su gráfica y en ellos f″ = 0.

**Ejercicio 3.37** (E pp. 120-121) [3.4, optimización]
«A una lámina de acero cuadrada de 40 cm de lado se le quitan cuatro cuadrados iguales en sus esquinas y se doblan los lados para formar una caja de base cuadrada. Calcula el lado del cuadrado que hay que quitar en las esquinas para maximizar el volumen de la caja.»
- Método: V(d) = (40 − 2d)²·d = 4d³ − 160d² + 1600d, d ∈ [0, 20]; V′ = 12d² − 320d + 1600 = 0 ⇒ d = 20/3 (d = 20 se descarta: no queda caja); V″(d) = 24d − 320; V″(20/3) = −160 < 0 ⇒ máximo. **d = 20/3 cm ≈ 6.67 cm.** Verificado con sympy.

**Ejercicio 3.38** (E p. 121) [3.4, optimización]
«Queremos construir un rectángulo con 100 cm de perímetro de tal forma que su área sea máxima. ¿Cuál es la longitud de sus lados?»
- Método: b = 50 − a; S(a) = 50a − a², a ∈ [0, 50]; S′ = 0 ⇒ a = 25; S″ = −2 < 0 (máximo relativo); S(0) = S(50) = 0 ⇒ máximo absoluto. Solución: cuadrado de 25 cm × 25 cm.

**Ejercicio 3.39** (E pp. 122-123) [3.5] MÁXIMA
«Sea f(x) = 3x⁵ − 5x⁴ − 20x³ + 2x − 1. ¿Cuándo es cóncava y cuándo convexa?»
- Método: f″ = 60x(x − 2)(x + 1) (raíces −1, 0, 2); tabla de signos. Convexa en [−1, 0] y [2, +∞); cóncava en (−∞, −1] y [0, 2]. Verificado con sympy.

**Ejercicio 3.40** (E p. 123) [3.5]
«Sea f(x) = x|x − 4|. Es cierto que: a) Es cóncava en (4, +∞). b) Es convexa en (−4, 4). c) En x = 4 tiene un punto de inflexión. d) Ninguna de las anteriores.»
- Método: para x < 4, f = −x(x − 4) ⇒ f″ = −2; para x > 4, f = x(x − 4) ⇒ f″ = 2. Cambia de cóncava a convexa en 4 ⇒ **c)**.
- **Errata importante:** la solución escribe «f es derivable si x = 4» y después «f no es derivable si x = 4». Lo correcto es **no derivable**: f′(4⁻) = −4 y f′(4⁺) = 4 (sympy). La respuesta c) no cambia, porque la inflexión se detecta por el cambio de concavidad en un punto de continuidad; confirmar el criterio de U Def. 3.10 (p. 135).

**Ejercicio 3.41** (E pp. 123-124) [3.5]
«La función f(x) = |x| es continua en ℝ y tiene derivada segunda negativa en ℝ \ {0}. Muestra que no es cóncava en ℝ.»
- Método: contraejemplo geométrico con a = −1, b = 1: la condición de concavidad exige f(2t − 1) ≥ f(−1)(1 − t) + f(1)t = 1 para todo t ∈ [0, 1]; en t = 1/2 el lado izquierdo es |0| = 0 < 1. No es cóncava.
- **Duda:** la solución remite a «el Ejercicio 3» para ver que |x| no es derivable en 0. La referencia correcta sería 3.34 (|x − 1|) o 3.35 (x^{2/3}). Numeración ambigua.

**Ejercicio 3.42** (E p. 125) [3.5]
«De una función f: ℝ → ℝ tres veces derivable conocemos la gráfica de su derivada primera f′ (figura no transcrita). Razona si las siguientes afirmaciones son correctas: a) f es cóncava en (−∞, 0). b) f es convexa en (−∞, 0). c) f tiene un punto de inflexión en x = 1.»
- Método: f′ decreciente en x < 0 ⇒ f″ < 0 ⇒ cóncava: a) sí; b) no. Candidatos a inflexión: ceros de f″ o extremos de f′ (x = 0, 0.5, 1). c) sí (cambia de cóncava a convexa en 1).

**Ejercicio 3.43** (E pp. 125-126) [3.4 extremos + 3.5 inflexión]
«Sea f(x) = 1/(1 − x) (el txt escribe «1 1 x» con el signo perdido; confirmar en el PDF). ¿Alcanza extremos relativos? ¿Tiene algún punto de inflexión?»
- Método: f′ = (1 − x)⁻² > 0 y nunca se anula ⇒ sin extremos. f″ = 2/(1 − x)³ ≠ 0 y no está definida en 1 ⇒ sin inflexión (la concavidad cambia en 1, que no pertenece al dominio). Verificado con sympy.

**Ejercicio 3.44** (E pp. 126-127) [3.4] MÁXIMA
«Sea f(x) = (x − 1)². ¿Cuál de las siguientes opciones es correcta? a) En x = 1 la función alcanza un máximo relativo. b) En x = 1 alcanza un mínimo relativo no absoluto. c) En x = 1 alcanza el único mínimo relativo y absoluto. d) En x = 1 tiene un punto de inflexión.»
- Método: f′ = 2(x − 1) = 0 en 1; f″ = 2 > 0 ⇒ mínimo relativo; f ≥ 0 = f(1) ⇒ absoluto; f″ ≠ 0 ⇒ no es inflexión. **c)**.

**Ejercicio 3.45** (E pp. 127-128) [3.5]
«Sea f: ℝ → ℝ una función dos veces derivable con continuidad en ℝ \ {1}. Su derivada se representa en la figura (no transcrita). A partir de la gráfica de f′, ¿cuáles son los intervalos de concavidad y convexidad de f? ¿Tiene puntos de inflexión? ¿Es convexa en ℝ?»
- Método: f′ creciente en (−∞, 1) y en (1, +∞) ⇒ f convexa en esos intervalos; no hay inflexión (no cambia de cóncava a convexa); no se puede asegurar convexidad en ℝ porque f puede ser discontinua en 1.
- Duda: el enunciado del txt dice «dos veces derivable con continuidad en ℝ \ {1}»; comprobar en el PDF.

**Ejercicio 3.46** (E pp. 128-131) [3.4 + 3.5 + asíntotas] MÁXIMA
«Sea f(x) = x²/(x − 1). ¿Cuál es su representación gráfica?»
- Método: dominio ℝ \ {1}; f′ = x(x − 2)/(x − 1)²; f″ = 2/(x − 1)³. Asíntota vertical x = 1 (límites laterales ±∞); asíntota oblicua y = x + 1 (lím [f(x) − x] = 1 en ±∞). Extremos: máximo relativo en x = 0 (f = 0), mínimo relativo en x = 2 (f = 4). Cóncava en (−∞, 1), convexa en (1, +∞); sin inflexión (f″ no se anula y x = 1 no está en el dominio). Verificado con sympy.
- La solución incluye la gráfica de x²/(x − 1) (Figura 3.5, p. 131).

**Ejercicio 3.47** (E pp. 131-133) [3.5 mayoritariamente; a) usa 3.4]
«Da una expresión, si es posible, que defina una función real de una variable real que verifique las propiedades que se indican: a) Derivable en su dominio, creciente en (−∞, 2) y decreciente en (2, +∞). b) Derivable en su dominio, estrictamente creciente en (−∞, 2) y estrictamente decreciente en (2, +∞). c) Derivable en su dominio, convexa en (−∞, 0) y cóncava en (0, +∞). d) Derivable en su dominio y con asíntota vertical x = −π. e) Positiva en (−∞, 1), con gráfica que corta al eje x en (2, 0) y al eje y en (0, −3).»
- Soluciones dadas: a) f(x) = π (constante); b) f(x) = −(x − 2)²; c) f(x) = −x³ (también valen f(x) = x o arctan x; tg x no); d) f(x) = ln(x + π) o f(x) = 1/(x + π); e) imposible: f debe ser positiva en (−∞, 1) (incluido 0) y a la vez f(0) = −3.
- **Erratas/dudas:** en a) la solución dice «creciente en ℝ y decreciente en ℝ» para f = π: es válido solo en sentido no estricto, y por eso no sirve para b). En c), f = x es lineal, luego cóncava y convexa a la vez (válida).

**Ejercicio 3.48** (E pp. 133-134) [3.5 + asíntotas]
«Dibuja la gráfica de una función continua que sea decreciente en todo ℝ, cóncava en (−∞, 0), convexa en (0, +∞) y tenga dos asíntotas (una horizontal y una oblicua).»
- Solución dada: f(x) = −arctg x si x ≤ 0; f(x) = −x/2 − arctg x si x > 0. Comprobado: continua en 0 (f(0) = 0 en ambos tramos); decreciente (f′ < 0); f″ = 2x/(1 + x²)² (signo correcto en cada tramo); asíntota horizontal y = π/2 en −∞; asíntota oblicua y = −x/2 + π/2 en +∞. Verificado con sympy (f″ y signos).

### 3.3 Tabla resumen E

| Ej. | Pág. E | Subsección | Método principal | Erratas / dudas |
|---|---|---|---|---|
| 3.29 | 114 | 3.4 | Criterio de la 1ª derivada con f′ | figura no transcrita |
| 3.30 | 114 | 3.4 (con 3.5) | Raíces de f′ (grado 2) | — |
| 3.31 | 115-116 | 3.4 | v′ = a, signos de a | a sin factor 12; tabla de signos desordenada |
| 3.32 | 116-117 | 3.4 | f′ = 0 y f″ | f″(x₁) ilegible en el txt (correcto −√2/2) |
| 3.33 | 117-118 | 3.4 | Sistema + críticos + comparación | — |
| 3.34 | 119 | 3.4 | No derivable + valor absoluto ≥ 0 | «derivable si x = 1» (debe ser ≠) |
| 3.35 | 119-120 | 3.4 | Límites laterales de f′ | — |
| 3.36 | 120 | 3.4 (c: 3.5) | Cortes de f′ con el eje x | figura no transcrita |
| 3.37 | 120-121 | 3.4 | Optimización de V(d) | — |
| 3.38 | 121 | 3.4 | Optimización de S(a) | — |
| 3.39 | 122-123 | 3.5 | f″ factorizada | — |
| 3.40 | 123 | 3.5 | f″ a trozos | **f no derivable en 4** (la solución dice lo contrario) |
| 3.41 | 123-124 | 3.5 | Contraejemplo con a = −1, b = 1 | remisión «Ejercicio 3» ambigua |
| 3.42 | 125 | 3.5 | f′ creciente/decreciente | figura no transcrita |
| 3.43 | 125-126 | 3.4 + 3.5 | f′ > 0; f″ ≠ 0 | signo de 1/(1−x) en el txt |
| 3.44 | 126-127 | 3.4 | f″ = 2 | — |
| 3.45 | 127-128 | 3.5 | f′ creciente | enunciado «continuidad en ℝ \ {1}» a confirmar |
| 3.46 | 128-131 | 3.4 + 3.5 + asíntotas | Estudio completo | — |
| 3.47 | 131-133 | 3.5 (+3.4) | Construcción | a) constante = «creciente» no estricto |
| 3.48 | 133-134 | 3.5 + asíntotas | Construcción | — |

---

## 4. Preguntas de examen X relacionadas con 3.4

Fuente: indice_examenes_1 a 4 (filtradas por tema 3.4). Marca OK = enunciado comprobado en la imagen de la pagina PDF (renderizado con PyMuPDF) y, si procede, con sympy. «índice» = viene solo del índice, sin verificar.

### 4.1 Solo requieren 3.4 (extremos u optimización de una variable)

| X (año, convocatoria) | Pág. PDF (enunciado / solución) | Enunciado resumido | Requiere | Estado |
|---|---|---|---|---|
| Feb 2010, 1ª sem., Eléctrica, Ej. 5 | 2 / 2 | Extremos relativos y absolutos de (1 − x²)/(x + 3) en [−1, 1]. Es el mismo ejercicio que E 3.32. | Solo 3.4 | OK |
| Feb 2012, 1ª sem., Mecánica Modelo A, PC2 | 19 / 19 | f(x) = abs(x − 1): ¿extremo en x = 1? ¿máximo o mínimo? Mínimo absoluto (continua, valor absoluto ≥ 0). Igual que E 3.34. | Solo 3.4 | OK |
| Feb 2014, Mecánica Modelo A, P2 | 40 / 40 | V/F: f(x) = x³ cos(x + 1) alcanza máximo y mínimo absolutos en [−π, π]. Respuesta: es cierto, porque es continua y se aplica la Proposición 3.4 de U. | 3.4 (+ 1.4 continuidad) | OK |
| Sep 2017, Modelo A, P2 corta | 85 / 85 | Puntos donde puede alcanzarse un extremo relativo de x³ − 3x² − 9x + 2. f′ = 3(x + 1)(x − 3) ⇒ x = −1, 3. | 3.4 (+ 2.1) | OK |
| Sep 2017, Modelo A, Ej. 6 | 87 / 87 | Dos números positivos con suma 9 y producto máximo. Solución: x = y = 9/2 (producto 81/4). | 3.4 (optimización) | OK (la solución cita «ejemplo 6.25 del libro»: ver dudas) |
| Electrónica, sin fecha en la cabecera (índice: «Electrónica 3»), P2 | 104 / 104 | Extremos absolutos de f(x) = x e^(−x) en [0, 2]. f′ = (1 − x)e^(−x); f(0) = 0 (mínimo), f(1) = 1/e ≈ 0.368 (máximo), f(2) = 2e^(−2) ≈ 0.271. Verificado con sympy. | Solo 3.4 (+ 2.x) | OK |
| Examen 5 (fuera de rango; solución en PDF 123), Ej. 3 | 122 / 122-123 | Afirmación correcta sobre f(x) = x⁴ − 2x³: A) es creciente; B) tiene dos extremos relativos; C) tiene un punto de silla; D) ninguna. Respuesta **C** (mínimo en 3/2, silla en 0). Verificado con sympy. | Solo 3.4 (Prop. 3.7-3.8) | OK |
| Feb 2018, 1ª sem., Ej. 6 | 146 / 146 | Dos reales negativos con suma −15 y producto máximo. Solución: x = y = −15/2, producto 225/4. Verificado con sympy. | 3.4 (optimización) | OK |
| Examen 1 (fuera de rango), Ej. 4 | 109 / 110 | F(x) = integral de 0 a x de t·sen t dt. Opciones: A) creciente; B) máximo en x = 7π; C) decreciente; D) ninguna. Respuesta **B**: F′ = x sen x cambia de + a − en 7π. | 6.x (teorema fundamental) + 3.4 | OK (sympy) |

### 4.2 Monotonía (2.5) con criterio de la 1ª derivada (3.4)

| X | Pág. PDF | Enunciado | Requiere | Estado |
|---|---|---|---|---|
| Sept 2018, Electrónica (solución) | 142 / 142 | f(x) = x² e^(x−5): intervalos de crecimiento y decrecimiento. f′ = x(x + 2)e^(x−5): creciente en (−∞, −2) y (0, +∞); decreciente en (−2, 0). Verificado con sympy. | 2.5 (+ 3.4 para máximos y mínimos) | OK |
| Electrónica 2, P2 | 101 / 101 | f(x) = x² e^(1−x): creciente en (0, 2); decreciente en (−∞, 0) y (2, ∞). f′ = x(2 − x)e^(1−x). Verificado con sympy. | 2.5 (+ 3.4) | OK |
| Examen 1, Ej. 3 | 109 / 110 | f(x) = e^(2x²−x): A) creciente en (−∞, 1/4); B) decreciente en (1/4, ∞); C) creciente en (−∞, 1/4); D) decreciente en (−∞, 1/4). Respuesta **D**: f′ = (4x − 1)e^(2x²−x). Verificado con sympy. | 2.5 (+ 3.4) | OK |
| Feb 2011, 2ª sem., Mecánica Modelo B, PC2 | 13 / 13 | Crecimiento y decrecimiento de x³ e^x. | 2.5 (+ 3.4) | índice |
| Feb 2013, 2ª sem., Mecánica Modelo B, PC1 | 35 / 35 | Dónde es creciente f(x) = x e^x. | 2.5 (+ 3.4) | índice |

### 4.3 Mezclas con 3.4 y otros temas

| X | Pág. PDF | Enunciado resumido | Temas | Estado |
|---|---|---|---|---|
| Sept 2015, Modelo A, Ej. 5 | 53-54 | f(x) = (x² + x − 2)/(x² − 1), f(1) = 3/2, en [0, ∞): continuidad (regla de Hopital), derivabilidad, extremos relativos y absolutos. | 1.4, 2.1, 2.3, 3.4 | índice |
| Feb 2016, Modelo A, Ej. 5 | 60-61 | f(x) = x³ − x si x ≤ 0; x² + x si x > 0: continuidad, derivabilidad y extremos en [−2, 2]. | 1.4, 2.1, 3.4 | índice |
| Sept 2016, Modelo A, Ej. 5 | 70-71 | f(x) = (3x − 1) e^x: Taylor de orden 3 en −1; crecimiento, inflexión y extremos relativos. | 3.1, 3.4, 3.5 | índice |
| Sin fecha, I. Electrónica (A), Ej. 5 | 127-128 | f = e^(x^k), k ∈ {0, 1, 2, …}: dominio, imagen, crecimiento, concavidad (k = 2, 3), asíntotas y extremos. | 3.4, 3.5 | índice |

### 4.4 Solo 3.5 (concavidad), solo para referencia

Sept 2011 PC4 (PDF 17); Feb 2013 Mecánica Modelo A, Pr5 a) (PDF 33); Feb 2014 Modelo B, P2 (PDF 43); Feb 2016 Modelo B, P3 (PDF 64); Feb 2017 Modelo A, P3 (PDF 77); Feb 2018 Modelo B, P3 (PDF 93); Electrónica 1, P3 (PDF 99). Todos según el índice.

## 5. Figuras (para recorte posterior)

| Figura | Libro | Pág. impresa | PDF | Descripción |
|---|---|---|---|---|
| U Fig. 3.1 | U | 128 | 126 | abs(sen x) con extremos en [0, 2π] |
| U Fig. 3.2 | U | 129 | 127 | x/(x² + 1) con máximo en (0, ∞) |
| U Fig. 3.3 | U | 131 | 129 | función creciente/decreciente sin extremo en 1 |
| U Fig. 3.4 | U | 133 | 131 | x⁴ − 2x³ con punto de silla y mínimo |
| U figura al margen Ej. 3.22 | U | 130 | 128 | función con asíntotas x = ±2 |
| E gráficas de f′ (3.29, 3.36, 3.42, 3.45) | E | 114, 120, 125, 127 | igual | gráficas de f′ de los enunciados (no transcritas) |
| E solución 3.46 (Fig. 3.5) | E | 131 | 131 | gráfica de x²/(x − 1) |
| L Fig. 3.1 (extremos en intervalo) | L | 162 | 179 | tres casos de extremos |
| L Fig. 3.30, 3.31 | L | 191 | 208 | criterio de la 2ª derivada; f = −3x⁵ + 5x³ |

Recortes no realizados. Antes de publicar, comprobar con `python herramientas/extraer_figura.py list`.

---

## 6. Faltas o dudas

1. **Páginas de U §3.4:** CLAUDE.md dice pp. 125-133; el texto muestra §3.4 hasta la p. 134 (el Ej. 3.26 termina en p. 134). §3.5 empieza al pie de la p. 134 (su texto en p. 135).
2. **Teorema de Fermat y valor extremo:** U no los enuncia en §3.4 (Fermat aparece solo como consecuencia de Def. 3.5 y Prop. 3.6; el teorema del valor extremo está en la Prop. 1.15 de U §1.4). No he localizado un enunciado literal en §3.4.
3. **Asíntotas:** E 3.46-3.48 y varias preguntas de X usan asíntotas. No he localizado un apartado de asíntotas en U §3.4-3.5 (U §3.5 solo menciona la representación gráfica en p. 139). Confirmar en qué tema de U están.
4. **Símbolos del txt:** en S y L los símbolos ≤, ≥, = y ≠ se han perdido o sustituido («m», «w», «v»). Los extractos de S y L están reconstruidos; para citas literales, verificar en el PDF.
5. **Larson, Teorema 3.9, punto 2:** el txt dice «si f″(c) < 0, entonces f tiene un mínimo relativo». La figura 3.30 de la misma página dice máximo relativo. Probablemente es un error de extracción; el render a baja resolución no basta para confirmarlo. Verificar en el PDF p. 191.
6. **Stewart 4.3:** la cabecera de la página donde empieza la «Prueba de la primera derivada» no se ha extraído; se cita pp. 291-292. Verificar.
7. **Stewart 4.1, método del intervalo cerrado:** el extracto está en el txt (p. 278), pero los pasos aparecen fragmentados; la formulación de la receta es un resumen, no literal.
8. **Larson 3.7, estrategia general:** tras el Ejemplo 1 (pp. 215-216) hay una estrategia de pasos que no he transcrito (el txt la tiene desordenada). Pendiente.
9. **Ejercicios E con figura no transcrita:** 3.29, 3.36, 3.42 y 3.45 dependen de la gráfica de f′. Solo se describen los signos que da la solución. Si el redactor necesita la gráfica, hay que recortarla de E.
10. **Erratas en E:** 3.31 (factor 12 omitido en a(t)); 3.32 (f″(x₁) = −√2/2; en el txt ilegible); 3.40 (la solución dice derivable en 4 y después no derivable; es no derivable); 3.41 (remisión «Ejercicio 3» ambigua); 3.47 a) (una constante es creciente solo en sentido no estricto); 3.34 (x ≠ 1 aparece como x = 1 en el txt).
11. **Enunciados E con signo o símbolo perdido en el txt:** 3.43 («1/(1−x)») y 3.45 (dominio y continuidad). Confirmar en el PDF.
12. **X, Sep 2017 Modelo A, Ej. 6** (PDF 87): la solución remite a «ejemplo 6.25 del libro», que no corresponde a la numeración de U (el cap. 6 es integración). No se ha usado.
13. **X, PDF 104:** la cabecera no indica fecha ni convocatoria («I. Electrónica Industrial y Automática»). El índice lo llama «Electrónica 3». Citar como «Electrónica, sin fecha (índice: Electrónica 3)».
14. **X, Examen 1 (PDF 109-110):** el índice indica enunciado en 109 y solución en 110-111. Verificado visualmente solo el enunciado de los Ejercicios 3 y 4 (PDF 109).
15. **X, índice sin verificar visualmente:** Sept 2015 (PDF 53-54), Feb 2016 Modelo A (PDF 60-61), Sept 2016 Modelo A (PDF 70-71), I. Electrónica (A) Ej. 5 (PDF 127-128), Feb 2011 PC2 (PDF 13), Feb 2013 PC1 (PDF 35), y todo el apartado 4.4.
16. **Ejemplo 3.22 de U:** la fórmula de la función (fracción con (x + 1)² y 4 − x²) está reconstruida del txt; confirmar en el PDF p. 130.
17. **U, Ej. 3.24:** el txt escribe la tercera derivada en f(0) como «−12 = 0» (debe leerse «≠ 0»); confirmar en el PDF.
