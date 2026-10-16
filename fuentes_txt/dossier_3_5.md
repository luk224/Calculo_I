# Dossier Tema 3.5: Concavidad y convexidad

Generado por el agente fuentes-calculo. Páginas impresas: U = PDF+2; E = PDF; L = PDF−17; S = número de cabecera; X = página PDF del `Examenes-resueltos-Calculo.pdf`. Todas las páginas citadas se han visto en el texto extraído o como imagen.

## 0. Alcance y correcciones a CLAUDE.md

- **U §3.5 ocupa pp. 134-140** (CLAUDE.md dice 134-139). El título «3.5. Concavidad y convexidad» aparece al pie de la p. 134 (PDF 132); el texto empieza en la p. 135 (PDF 133). Las autoevaluaciones 6-10 están en la p. 140 (PDF 138). La p. 141 (PDF 139) es el inicio del capítulo 4.
- Mapa de E para 3.5: puro = **3.39, 3.40, 3.41, 3.42, 3.45, 3.48**; solo un apartado = **3.30 (inflexión), 3.36 (apartado c), 3.43 (inflexión)**; mixtos = **3.46, 3.47** (3.5 + asíntotas o 3.4).
- Ojo con el nombre: la «Figura 3.5» de U (p. 136) es x² y ln x; la «Figura 3.5» de E (p. 131) es x²/(x−1). Son distintas.
- En U, el txt pierde los dibujos «forma de …» (∪/∩) de las Def. 3.8 y 3.9 y algunos signos. Los enunciados de abajo se han reconstruido con la fórmula; el dibujo ∪/∩ hay que verlo en el PDF (p. 135).

---

## 1. Libro oficial U §3.5 (pp. 134-140)

### 1.1 Introducción (p. 134 pie; p. 135)
- «3.5. Concavidad y convexidad / 3.5.1 Motivación.» «El último tema de este capítulo está dedicado a la concavidad y la convexidad en un intervalo de una función. Ambos conceptos tienen una clara interpretación geométrica si los trasladamos a la gráfica de la función, pero además, tienen importancia en otros campos como la optimización o el diseño industrial.» *src: U §3.5.1 p.134-135*
- Objetivos (p. 135): «…conozca las definiciones de función convexa y cóncava, su interpretación geométrica y condiciones suficientes en función de las derivadas de orden superior para garantizar la convexidad o concavidad de una función en cierto intervalo.»

### 1.2 Definiciones (p. 135, PDF 133)
- **Definición 3.8 (convexa).** «La función f: D → ℝ es convexa en un intervalo I ⊂ D si f((1 − t)x + ty) ≤ (1 − t)f(x) + tf(y) ∀x, y ∈ I y ∀t ∈ [0, 1].» *src: U §3.5.2 Def. 3.8 p.135*
  - Interpretación del libro: «f es convexa en I si su gráfica entre x, y ∈ I está debajo del segmento que une (x, f(x)) y (y, f(y))», con el segmento (x(t), y(t)) = (1 − t)(a, b) + t(c, d), t ∈ [0, 1].
  - «Intuitivamente una función es convexa en un intervalo I si su gráfica tiene forma de [símbolo perdido en el txt].» (forma de cuenco ∪; comprobar el símbolo en el PDF p.135).
- **Definición 3.9 (cóncava).** «La función f: D → ℝ es cóncava en un intervalo I ⊂ D si −f es convexa en I.» «Intuitivamente… forma de [símbolo perdido].» (forma de ∩). *src: U Def. 3.9 p.135*
- **Ejemplo 3.27.** «Las gráficas de f(x) = x² y g(x) = ln x indican que f es convexa y g es cóncava.» *src: U Ej. 3.27 p.135*

### 1.3 Figura 3.5 y ejemplo 3.28 (p. 136, PDF 134)
- **Figura 3.5**: «Ejemplos de funciones convexa y cóncava» (f = x², convexa; f = ln x, cóncava). Recorte candidato: **U PDF 134**.
- «Una función puede no ser cóncava ni convexa en un intervalo.»
- **Ejemplo 3.28.** «La función f(x) = x³ no es convexa ni cóncava en [−1, 1].» Se prueba con x = −1, y = 1 y la definición. El txt de la parte final del ejemplo está roto: leer PDF p.136 si se cita.
- «Claramente, el uso de la definición para estudiar la convexidad o concavidad de una función resulta laborioso. Los siguientes resultados mostrarán condiciones sencillas que garantizan la concavidad o convexidad.» *src: U p.136*

### 1.4 Proposiciones 3.9 y 3.10 (p. 136, PDF 134)
- **Proposición 3.9.** «Sea f una función derivable en I, entonces: f es convexa en I si y sólo si f′ es creciente en I; f es cóncava en I si y sólo si f′ es decreciente en I.» *src: U Prop. 3.9 p.136*
- **Proposición 3.10.** «Sea f dos veces derivable en I. Si f″(x) ≥ 0 en I, entonces f es convexa en I. Si f″(x) ≤ 0 en I, entonces f es cóncava en I.» *src: U Prop. 3.10 p.136*

### 1.5 Puntos de inflexión (pp. 137, PDF 135)
- **Definición 3.10.** «Llamaremos puntos de inflexión a los puntos en los que una función pasa de cóncava a convexa o de convexa a cóncava.» «Es decir, c es un punto de inflexión para f si existe ε > 0 tal que f es convexa en (c − ε, c) y cóncava en (c, c + ε) o viceversa.» *src: U Def. 3.10 p.137*
- **Ejemplo 3.29.** f(x) = x⁴ − x³ − 3x² + 10x + 1. «f′(x) = 4x³ − 3x² − 6x + 10 y f″(x) = 12x² − 6x − 6.» Raíces de f″: «x = (1 ± √(1 + 8))/4 … 1 y −1/2.» Signos: «f″(x) > 0 en (−∞, −1/2), f″(x) < 0 en (−1/2, 1) y f″(x) > 0 en (1, ∞). La función es cóncava en (−1/2, 1) y sus puntos de inflexión son −1/2 y 1.» *src: U Ej. 3.29 p.137* (comprobado: f″ = 6(2x² − x − 1))
- **Proposición 3.11.** «Si f es dos veces derivable en I y c ∈ I es un punto de inflexión para f, entonces f″(c) = 0.» *src: U Prop. 3.11 p.137*
- **Proposición 3.12.** «Sea f tal que f″(c) = 0. Si la primera derivada de orden superior a dos que no se anula es impar, entonces f tiene un punto de inflexión en c, pasando la función de cóncava a convexa si dicha derivada es positiva y de convexa a cóncava si es negativa.» *src: U Prop. 3.12 p.137*

### 1.6 Figura 3.6 y ejemplo 3.30 (p. 138, PDF 136)
- **Figura 3.6** (PDF 136): «Puntos de inflexión e intervalos de concavidad y convexidad.» Gráfica de f(x) = x⁴ − x³ − 3x² + 10x + 1 con las zonas convexa/cóncava/convexa. Recorte candidato: **U PDF 136**.
- **Ejemplo 3.30.** «Busquemos los puntos de inflexión de f(x) = tg x y g(x) = −x⁵ en el intervalo (−π/2, π/2).»
  - tg: f′ = 1/cos²x, f″ = 2 sen x / cos³x. «0 es un punto de inflexión en el que f pasa de cóncava a convexa» (f‴(0) = 2 > 0).
  - g: g′ = −5x⁴, g″ = −20x³, g‴(0) = 0…, g⁽⁵⁾ = −120. «La primera derivada que no se anula es de orden impar y negativa… 0 es un punto de inflexión en el que g pasa de convexa a cóncava.»
  - Comprobado con sympy: f″ = 2 tan x / cos² x; g‴ = −60x².

### 1.7 Representación gráfica (p. 139, PDF 137)
- «Representación gráfica de funciones. Conociendo el dominio, los puntos de continuidad y discontinuidad, las asíntotas, los intervalos de crecimiento y decrecimiento, los extremos relativos, los intervalos de concavidad y convexidad y los puntos de inflexión es sencillo realizar representaciones gráficas aproximadas de funciones.» (Sin ejemplo; la receta completa está en S §4.5 y L §3.6.)

### 1.8 Autoevaluación (pp. 139-140, PDF 137-138)
Solo enunciados; **U no da soluciones**. Relevantes para 3.5 (literal):
- 6. «Una función continua definida sobre un intervalo, siempre alcanza en él extremos absolutos.» (p. 139)
- 7. «Dada una función f definida en el intervalo [−1, 3], entonces si en el punto x = 0 la función f alcanza un máximo absoluto, también va a alcanzar el máximo relativo en este punto.» (p. 140)
- 8. «Dada una función continua y derivable en x = a, con f′(a) = 0, entonces f tiene un extremo relativo en a.» (p. 140)
- 9. «Existe una función continua y dos veces derivable f: [0, 1] → ℝ con f(x) > 0, f′(x) > 0 y f″(x) < 0 en el intervalo [0, 1].» (p. 140)
- 10. «Si f es una función continua y derivable dos veces en x = 2 con f″(2) = 0, entonces hay un punto de inflexión en x = 2.» (p. 140)

---

## 2. Apartados equivalentes de S (Stewart) y L (Larson)

### 2.1 Stewart, *Cálculo de una variable. Trascendentes tempranas*

**§4.3 «Cómo afecta la derivada la forma de una gráfica», pp. 293-296**
- **Definición de concavidad (p. 293, PDF 575).** «Si la gráfica de f queda por arriba de todas sus rectas tangentes sobre un intervalo I, entonces se dice que es cóncava hacia arriba sobre I. Si la gráfica de f queda por abajo de todas sus rectas tangentes, se dice que es cóncava hacia abajo sobre I.» Intuición: en la figura 6 «la pendiente de la recta tangente es creciente… f′ es creciente y, por tanto, f″ es positiva». *src: S §4.3 p.293*
- **Prueba de concavidad (p. 293; sigue en PDF 576).** «a) Si f″(x) > 0 para toda x en I, entonces la gráfica de f es cóncava hacia arriba sobre I. b) Si f″(x) < 0 para toda x en I, entonces la gráfica de f es cóncava hacia abajo sobre I.» (Los signos > y < se pierden en el txt; leer PDF p.293.)
- **Figura 7 (p. 293).** Ejemplo gráfico de curva con intervalos CA/CB y puntos de inflexión B, C, D, P.
- **Ejemplo 4 (p. 294, PDF 577).** Población de abejas: «La curva parece ser cóncava hacia arriba en (0, 12) y cóncava hacia abajo en (12, 18).» Intuición de la inflexión como cambio de tasa.
- **Definición de punto de inflexión (p. 295, PDF 579; cabecera no extraída, verificar).** «Un punto P sobre una curva y = f(x) se llama punto de inflexión si f es allí continua y la curva cambia de cóncava hacia arriba a cóncava hacia abajo o de cóncava hacia abajo a cóncava hacia arriba en P.» «…existe un punto de inflexión en cualquier punto donde la segunda derivada cambia de signo.»
- **Ejemplo 5 (p. 295, PDF 579-580).** Esbozo de una f con f′ y f″ dadas por signos y asíntotas horizontales y = −2 (rótulo «y=_2» de la figura 9) e y = 0.
- **Prueba de la segunda derivada (p. 296, PDF 581; verificar).** Si f′(c) = 0 y f″(c) > 0, mínimo local; f″(c) < 0, máximo local.
- **Ejemplo 6 (p. 296, PDF 582).** y = x⁴ − 4x³: «Discuta la curva… respecto a la concavidad, puntos de inflexión y máximos y mínimos locales.»

**§4.5 «Resumen de trazado de curvas», pp. 311-316**
- **Guía A-H (pp. 311-313).** A Dominio, B intersecciones, C simetría, D asíntotas horizontales y verticales, E crecimiento, F extremos, **G «Concavidad y puntos de inflexión. Obtenga f″(x) y utilice la prueba de la concavidad. La curva es cóncava hacia arriba donde f″(x) > 0 y cóncava hacia abajo donde f″(x) < 0.»** (p. 313, PDF 648; signos perdidos en el txt), H trazado. *src: S §4.5 pp.311-313*
- **Asíntotas inclinadas (p. 315, PDF 673).** «Si lím_{x→∞}[f(x) − (mx + b)] = 0, entonces la recta y = mx + b se llama asíntota inclinada (oblicua).» El txt pierde algún símbolo; leer PDF p.315.
- **Ejemplo 6 (p. 316, PDF 674).** f(x) = x³/(x² + 1): «…Así que la recta y = x es una asíntota oblicua.» f′ > 0 salvo en 0; f″(x) = 0 en x = 0 y x = ±√3 (comprobado: f″ = −2x(x² − 3)/(x² + 1)³). Ejemplo completo de trazado con tabla de concavidad.

**§2.6 «Límites al infinito; asíntotas horizontales», p. 131 (PDF 298).** Definición de asíntota horizontal (base del punto D de §4.5).

### 2.2 Larson, *Cálculo Tomo 1*

**§3.4 «Concavidad y criterio de la segunda derivada», pp. 187-194**
- **Definición de concavidad (p. 187, PDF 204).** «Sea f derivable en un intervalo abierto I. La gráfica de f es cóncava hacia arriba sobre I si f′ es creciente en el intervalo y cóncava hacia abajo en I si f′ es decreciente en el intervalo.» *src: L §3.4 p.187*
- **Interpretación con tangentes (p. 187, figura 3.23).** «Si la gráfica de f es cóncava hacia arriba en I, entonces la gráfica de f se encuentra arriba de todas sus rectas tangentes en I.» (y al revés para cóncava hacia abajo). Demostración en el apéndice A de L.
- **Teorema 3.7 (criterio de concavidad, p. 188, PDF 205).** «Sea f una función cuya segunda derivada existe en un intervalo abierto I. 1. Si f″(x) > 0 para todo x en I, entonces la gráfica de f es cóncava hacia arriba en I. 2. Si f″(x) < 0 para todo x en I, entonces la gráfica de f es cóncava hacia abajo en I.»
- **Comentario (p. 188).** «…una recta no es ni cóncava hacia arriba ni cóncava hacia abajo.»
- **Ejemplo 1 (p. 189, PDF 206).** f(x) = 6/(x² + 3) (fórmula del txt roto por OCR; comprobado con sympy: f″ = 36(x² − 1)/(x² + 3)³). Cóncava en (−1, 1), convexa en (−∞,−1) y (1, ∞).
- **Teorema 3.8 (inflexión, p. 190, PDF 207).** «Si (c, f(c)) es un punto de inflexión de la gráfica de f, entonces f″(c) = 0 o f″ no existe en x = c.»
- **Ejemplo 3 (p. 190, PDF 207).** f(x) = x⁴ − 4x³: f″ = 12x(x − 2); inflexiones en x = 0 y x = 2.
- **Exploración (p. 190).** «El recíproco del teorema 3.8 por lo general no es cierto.» Ejemplo: f(x) = x⁴, f″(0) = 0 y (0, 0) no es inflexión (error típico).
- Ejercicios 3.4 (pp. 192-194): no extraídos.

**§3.5 «Límites al infinito», pp. 195-197.** Asíntotas horizontales: «La recta y = L es una asíntota horizontal de la gráfica de f si lím_{x→∞} f(x) = L o lím_{x→−∞} f(x) = L.» (L p.196, PDF 213). Ejemplo 2 (p. 197).

**§3.6 «Un resumen del trazado de curvas», pp. 206-214**
- **Lista de características (p. 206, PDF 223).** Intersecciones, simetría, dominio, continuidad, asíntotas verticales, derivabilidad, extremos, **concavidad**, **puntos de inflexión**, asíntotas horizontales, límites al infinito.
- **Ejemplo 1 (p. 207, PDF 224).** f(x) = 2(x² − 9)/(x² − 4). f′ = 20x/(x² − 4)² y f″ = −20(3x² + 4)/(x² − 4)³ (comprobado con sympy). Asíntotas verticales x = ±2, horizontal y = 2, mínimo relativo en x = 0 (f = 9/2), intervalos de prueba y tabla de concavidad.
- **Ejemplo 2 (p. 208, PDF 225).** Función racional con asíntota vertical x = 2 y sin asíntotas horizontales (la fórmula del txt es ilegible; leer PDF).
- **Ejemplo 3 (p. 209, PDF 226).** Función radical: «dos asíntotas horizontales: y = 1 (a la derecha) y y = −1 (a la izquierda)… solo un posible punto de inflexión (x = 0)… simétrica respecto al origen.»

---

## 3. Ejercicios de E (libro de ejercicios 24-25) de la sección 3.5

Leyenda: **[3.5]** = puro; **[3.5 parte]** = solo un apartado; **[mixto]** = 3.4 + 3.5 + asíntotas. Páginas E = PDF.

### Ejercicio 3.30 [3.5 parte: inflexión] (E p. 114)
- **Enunciado:** «Sea f la función dada por f(x) = ax³ + bx² + cx + d, para a, b, c, d ∈ ℝ con a ≠ 0. ¿Es cierto que f tiene exactamente un máximo local y un mínimo local en su dominio, cualesquiera que sean a, b, c, d?»
- **Desarrollo impreso (resumen):** f′(x) = 3ax² + 2bx + c. Puede no tener raíces reales (f = 2x³ + 6x) o tener raíz doble, que es punto de inflexión (f = x³). Respuesta: no es cierto.
- **Método:** extremos con f′ = 0; inflexión con f″ = 0 (f″ = 6ax + 2b).
- **Erratum:** el desarrollo dice «los extremos locales y los puntos de inflexión… se alcanzan en puntos donde se anula su derivada». Para la inflexión el criterio es **f″ = 0** (U Prop. 3.11), no f′ = 0. La conclusión no cambia, pero el texto confunde los dos criterios.
- Sin figura.

### Ejercicio 3.36 [3.5 parte: apartado c] (E p. 120)
- **Enunciado:** «La gráfica de la derivada de una función dos veces derivable f con dominio todo ℝ aparece en la siguiente figura. Razona si alguna de las siguientes afirmaciones es correcta: a) f tiene dos puntos críticos, pero un solo extremo relativo. b) f tiene dos extremos relativos. c) La ecuación f″(x) = 0 no tiene soluciones reales.»
- **Desarrollo impreso (resumen):** puntos críticos = cortes de f′ con el eje x (x = −2 y x = 1). En x = −2 f′ pasa de negativa a positiva (mínimo relativo); en x = 1 no cambia de signo. a) correcta, b) incorrecta.
- **c) (3.5):** «no es correcta porque en la gráfica de f′ aparecen extremos relativos en los que f″ se anularía.»
- **Figura a recortar: E PDF 120** (gráfica de f′; eje horizontal de −2 a 2).

### Ejercicio 3.39 [3.5] MÁXIMA (E pp. 122-123)
- **Enunciado:** «Sea f la función dada por f(x) = 3x⁵ − 5x⁴ − 20x³ + 2x − 1. ¿Cuándo es cóncava y cuándo convexa?»
- **Desarrollo impreso (resumen):** f′(x) = 15x⁴ − 20x³ − 60x² + 2; f″(x) = 60x³ − 60x² − 120x = 60x(x − 2)(x + 1). Raíces de f″: −1, 0, 2. Tabla de signos de (x + 1), x, (x − 2) y f″ en (−∞,−1), (−1,0), (0,2), (2,∞). Conclusión impresa: «convexa en [−1, 0] y en [2, +∞)… cóncava … en (−∞, −1] y en [0, 2].»
- **Comprobado con sympy:** f″ = 60x(x − 2)(x + 1). Correcto.
- **Método:** f″ factorizada y tabla de signos por intervalos.
- Gráfica al margen en p. 123 (**E PDF 123**).

### Ejercicio 3.40 [3.5] (E p. 123)
- **Enunciado:** «Sea f la función dada por f(x) = x |x − 4|. Es cierto que: a) Es cóncava en (4, +∞). b) Es convexa en (−4, 4). c) En x = 4 tiene un punto de inflexión. d) Ninguna de las anteriores.»
- **Desarrollo impreso (resumen):** f(x) = −x(x − 4) si x < 4; f(4) = 0; f(x) = x(x − 4) si x > 4. f″ = −2 para x < 4 y f″ = 2 para x > 4. «Como cambia de cóncava a convexa en x = 4, en este punto hay un punto de inflexión. La única opción correcta es c).»
- **Erratum:** el desarrollo afirma primero «f es derivable si x = 4» y luego «f(x) no es derivable si x = 4». La correcta es **no derivable en 4** (f′(4⁻) = −4, f′(4⁺) = 4; comprobado). La respuesta c) no cambia: f es continua en 4 y la concavidad cambia ahí.
- Gráfica al margen (**E PDF 123**).

### Ejercicio 3.41 [3.5] (E pp. 123-124)
- **Enunciado:** «La función dada por f(x) = |x| es continua en ℝ y tiene derivada segunda negativa en ℝ \ {0}. Muestra que no es cóncava en ℝ.» (Marcado con «!» en el libro.)
- **Desarrollo impreso (resumen):** no basta con f″ < 0 fuera de 0 para concluir en ℝ, porque 0 no está en el dominio de f″. Contraejemplo geométrico con a = −1 y b = 1: la concavidad exigiría f(2t − 1) ≥ f(−1)(1 − t) + f(1)t = 1 para todo t ∈ [0, 1], es decir |2t − 1| ≥ 1. En t = 1/2 el lado izquierdo es 0 < 1. «Es cóncava en (−∞, 0] y en [0, +∞), pero no en ℝ.»
- **Duda de remisión:** el desarrollo dice «esta función ya la hemos estudiado en el Ejercicio 3». No hay ejercicio 3 con |x|; lo más cercano es 3.34 (|x − 1|) o 3.35 (x^{2/3}). Decirlo en el HTML.
- Sin figura en el enunciado.

### Ejercicio 3.42 [3.5] (E p. 125)
- **Enunciado:** «De una función f: ℝ → ℝ tres veces derivable conocemos la gráfica de su derivada primera f′ que mostramos a continuación. Razona si las siguientes afirmaciones son correctas. a) La función f es cóncava en (−∞, 0). b) La función f es convexa si (−∞, 0). c) La función f tiene un punto de inflexión en x = 1.»
- **Erratum tipográfico:** en b) falta «en» («convexa si (−∞,0)», confirmado en la imagen).
- **Desarrollo impreso (resumen):** f′ decreciente en x < 0 ⇒ f″ ≤ 0 ⇒ cóncava en (−∞, 0): a) sí, b) no. Candidatos a inflexión: ceros de f″, que incluyen extremos de f′: x = 0, 0.5 y 1. Cambio de cóncava a convexa en los tres: c) sí.
- **Figura a recortar: E PDF 125** (f′ con mínimo en 0, máximo local en 0.5 y mínimo en 1).

### Ejercicio 3.43 [3.5 parte: inflexión] (E pp. 125-126)
- **Enunciado:** «Sea f la función dada por: f(x) = 1/(1 − x). ¿Alcanza extremos relativos? ¿Tiene algún punto de inflexión?» (Confirmado en la imagen de E p.125: la fracción sí está en el PDF.)
- **Desarrollo impreso (resumen):** f′(x) = (1 − x)⁻² > 0 y nunca 0 ⇒ sin extremos. f″(x) = 2/(1 − x)³ nunca 0 y no definida en 1. Cambia de convexa (x < 1) a cóncava (x > 1), pero en x = 1 f no está definida (asíntota vertical) ⇒ **sin punto de inflexión**.
- Comprobado con sympy: f″ = 2/(1 − x)³.
- Gráfica de f en p.126 (**E PDF 126**).

### Ejercicio 3.45 [3.5] (E pp. 127-128)
- **Enunciado:** «Sea f: ℝ → ℝ una función dos veces derivable con continuidad en ℝ \ {1}. Su derivada se representa en la siguiente figura. A partir de la gráfica de f′, ¿cuáles son los intervalos de concavidad y convexidad de la función f? ¿Tiene puntos de inflexión? ¿Es convexa en ℝ?» (Confirmado en la imagen de E p.127.)
- **Desarrollo impreso (resumen):** f′ creciente en (−∞, 1) y en (1, +∞) ⇒ f″ ≥ 0 ⇒ **convexa** en ambos. No hay inflexión (no cambia de cóncava a convexa). **No se puede afirmar convexidad en ℝ**: f puede ser discontinua en x = 1.
- **Figura a recortar: E PDF 127** (f′ con asíntota vertical en x = 1; corta el eje en 0 y en 2).

### Ejercicio 3.46 [mixto: 3.4 + 3.5 + asíntotas] (E pp. 128-131)
- **Enunciado:** «Sea f la función definida por f(x) = x²/(x − 1). ¿Cuál es su representación gráfica?» (El txt pierde la fracción; la forma x²/(x − 1) se confirma por la solución, no por imagen de p.128.)
- **Desarrollo impreso (resumen):** dominio ℝ menos {1}; f′ = x(x − 2)/(x − 1)²; f″ = 2/(x − 1)³ (comprobado). Corte con los ejes en (0, 0). Asíntota vertical x = 1; oblicua y = x + 1 (lím[f(x) − x] = 1 en ±∞). Creciente en (−∞, 0) y (2, ∞); decreciente en (0, 1) y (1, 2). Máximo relativo en x = 0 (f″(0) = −2 < 0), mínimo relativo en x = 2 (f″(2) = 2 > 0, f(2) = 4). Cóncava en (−∞, 1), convexa en (1, ∞); sin inflexión (f″ no se anula y x = 1 no está en el dominio).
- **Figura 3.5 de E (p. 131):** gráfica de x²/(x − 1). **Recortar E PDF 131.** No confundir con la Figura 3.5 de U.
- Sin errores de cálculo detectados.

### Ejercicio 3.47 [3.5 + 3.4 en a)] (E pp. 131-133)
- **Enunciado:** «Da una expresión, si es posible, que defina una función real de una variable real que verifique las propiedades que se indican en cada apartado: a) Derivable en su dominio, creciente en el intervalo (−∞, 2) y decreciente en el intervalo (2, +∞). b) Derivable en su dominio, estrictamente creciente en el intervalo (−∞, 2) y estrictamente decreciente en el intervalo (2, +∞). c) Derivable en su dominio, convexa en el intervalo (−∞, 0) y cóncava en el intervalo (0, +∞). d) Derivable en su dominio y con asíntota vertical x = −π. e) Positiva en (−∞, 1), con gráfica que corta al eje x en (2, 0) y al eje y en (0, −3).»
- **Desarrollo impreso (resumen):** a) f = π. b) f(x) = −(x − 2)². c) f(x) = −x³; también valen f = x o arctg x (no vale tg x). d) f(x) = ln(x + π) o 1/(x + π). e) No existe: por una parte f(0) > 0 (positiva en (−∞, 1)) y por otra f(0) = −3.
- **Erratum/duda:** a) con f constante es creciente y decreciente solo en sentido no estricto; por eso no sirve para b). c) f = x es lineal: no es estrictamente convexa ni cóncava, válida solo en sentido débil (decirlo). En el desarrollo, «Para el tercero» se refiere a d) (la cuarta opción): numeración confusa.
- **Figuras:** pp. 132-133 (gráficas de f = π, −(x − 2)², −x³, ln(x + π)). Recortar si se quiere: **E PDF 132 y 133**.

### Ejercicio 3.48 [3.5 + asíntotas] (E pp. 133-134)
- **Enunciado:** «Dibuja la gráfica de una función continua que sea decreciente en todo ℝ, cóncava en (−∞, 0), convexa en (0, +∞) y tenga dos asíntotas (una horizontal y una oblicua).»
- **Desarrollo impreso (resumen):** f(x) = −arctg(x) si x ≤ 0; f(x) = −x/2 − arctg(x) si x > 0. Continua en 0 (ambas ramas valen 0); f′ = −1/(1 + x²) < 0 y f′ = −(x² + 3)/(2(x² + 1)) < 0; f″ = 2x/(1 + x²)² (negativa en x < 0, positiva en x > 0). Asíntota horizontal y = π/2 (x → −∞); oblicua y = −x/2 − π/2 (x → +∞). El término −x/2 «no afecta a la convexidad en el intervalo (0, +∞), porque al derivar dos veces su aportación desaparece».
- Comprobado con sympy (f′, f″ y límites).
- Figura en p. 134 (**E PDF 134**).

---

## 4. Preguntas de examen X solo de 3.5 (o 3.4 + 3.5)

Fuente: `Examenes-resueltos-Calculo.pdf` (página PDF). Índices: `fuentes_txt/indice_examenes_1.md` a `_4.md`. Todas las páginas de la tabla se han visto como imagen (PyMuPDF, 100-110 dpi).

| # | Página PDF X | Año / convocatoria | Pregunta | Tema | Verificado |
|---|---|---|---|---|---|
| X1 | p.16 (enunc.), p.17 (sol.) | Sept 2011, Mecánica (PC4) | Gráfica de f″ (parábola): inflexiones y concavidad/convexidad | 3.5 | sí (imagen) |
| X2 | p.33 | Feb 2013, 1ª sem., Mecánica, Modelo A (Pr5) | f = xe^x: (a) concavidad/convexidad; (b) ∫ x e^x dx | 3.5 + 6.x | sí (imagen) |
| X3 | p.43 | Feb 2014, Mecánica, Modelo B (PC2) | Gráfica de f″ en [−2, 2]: concavidad, convexidad, inflexiones | 3.5 | sí (imagen) |
| X4 | p.64-65 | Feb 2016, Mecánica, Modelo B (PC3) | f = x²/(x + 1): intervalos de concavidad/convexidad | 3.5 | sí (imagen) |
| X5 | p.70-71 | Sept 2016, Mecánica, Modelo A (Ej. 5) | f = (3x − 1)e^x: (a) Taylor de orden 3 en −1; (b) crecimiento e inflexión; (c) extremos | 3.1 + 3.4 + 3.5 | sí (imagen) |
| X6 | p.77 | Feb 2017, Mecánica, Modelo A (PC3) | Gráfica de f″ en [a, b] con ceros x₀, x₁, x₂: intervalos cóncavos/convexos | 3.5 | sí (imagen) |
| X7 | p.89-90 | Feb 2018, Mecánica, Modelo A (Ej. 5) | f = 1/(x² + 4): (a) continuidad y derivada; (b) concavidad/convexidad; (c) punto fijo | 2.1 + 3.5 + 2.4 | sí (imagen) |
| X8 | p.93 | Feb 2018, Mecánica, Modelo B (PC3) | f = x⁴ − 2x: concavidad/convexidad | 3.5 | sí (imagen) |
| X9 | p.99 | Sin fecha, I. Electrónica (PC3) | Dibujar gráfica creciente en ℝ, convexa en (−∞,0), cóncava en (0,∞), con asíntota horizontal y oblicua | 3.5 + asíntotas | sí (imagen) |
| X10 | p.127-128 | Sin fecha, I. Electrónica Industrial y Automática (A) (Ej. 5) | f = e^{x^k}: dominio, imagen, crecimiento, **concavidad y convexidad** para k = 2 y k = 3; asíntotas; extremos | 3.4 + 3.5 | sí (imagen) |

### Detalle de cada pregunta

- **X1 (p.16-17, Sept 2011).** Enunciado (p.16, PC4): «Sea f: ℝ → ℝ una función continua y derivable cinco veces cuya derivada segunda se representa en la siguiente figura. Determine sus puntos de inflexión y los intervalos de concavidad y convexidad. Razone la respuesta.» Solución (p.17): «la función f(x) es cóncava en el intervalo (−2, 2) y convexa en (−∞, −2) ∪ (2, ∞). Los puntos de inflexión son los puntos donde f cambia de cóncava a convexa o viceversa; en este caso son x = −2 y x = 2.» Figura de f″ en p.17 (recorte candidato **X PDF 17**).
- **X2 (p.33, Feb 2013 Mod. A, Pr5).** Solución (a): f″(x) = (2 + x)e^x; «la función es cóncava en (−∞, −2] y convexa en [−2, ∞)». Comprobado con sympy. Parte (b) = integración por partes (6.x).
- **X3 (p.43, Feb 2014 Mod. B, PC2).** Figura de f″ en [−2, 2] (ceros en −1, 0 y 1). Solución impresa: «f es convexa en (−1, 0) y en (1, 2) y cóncava en (−2, −1) y en (0, 1). Los puntos de inflexión son x = −1, x = 0 y x = 1.» Coincide con la gráfica. Recorte candidato **X PDF 43**.
- **X4 (p.64-65, Feb 2016 Mod. B, PC3).** f = x²/(x + 1). Solución impresa: «f es cóncava en (−∞, −1) y convexa en (−1, ∞). No tiene puntos de inflexión, porque f″(x) ≠ 0 para todo x… en x = −1 la función no es continua y tiene una asíntota vertical.»
  - **Erratum:** la cadena de f″ de p.64 es incorrecta. Escribe «f″ = [2(x + 2)(x + 1)² − 2x(x + 2)(x + 1)]/(x + 1)⁴ = (2x² + 6x + 4)/(x + 1)⁴ = 2/(x + 1)³». La expresión (2x² + 6x + 4)/(x + 1)⁴ es igual a 2(x + 2)/(x + 1)³, no a 2/(x + 1)³. El valor correcto es **f″ = 2/(x + 1)³** (comprobado: f′ = x(x + 2)/(x + 1)²; el error está en derivar el numerador x(x + 2) como 2(x + 2) en vez de 2(x + 1)). La conclusión de signos no cambia.
- **X5 (p.70-71, Sept 2016 Mod. A, Ej. 5).** f = (3x − 1)e^x. Solución impresa: f″ = e^x(3x + 5), f‴ = e^x(3x + 8); «f″(x) = 0 ⇔ x = −5/3» y «f‴(−5/3) = 3e^{−5/3} ≠ 0» ⇒ inflexión en x = −5/3. (b) f′ = e^x(3x + 2): creciente si x ≥ −2/3 y decreciente si x ≤ −2/3. (c) mínimo relativo en x = −2/3.
  - **Erratum en (a):** en el polinomio de Taylor aparece «(3/3!) e^{−1}(x + 1)³»; debe ser **(5/3!)**, porque f‴(−1) = 5e^{−1} (la línea final ya pone 5/6). Comprobado: p₃(x) = −4e^{−1} − e^{−1}(x + 1) + e^{−1}(x + 1)² + (5/6)e^{−1}(x + 1)³.
  - El apartado de inflexión (f″ = 0 y f‴ ≠ 0) es 3.5; el de Taylor es 3.1 y el de crecimiento/extremos 2.5/3.4.
- **X6 (p.77, Feb 2017 Mod. A, PC3).** Gráfica de f″ en [a, b] con ceros x₀ < x₁ < x₂. Solución impresa: «Es cóncava cuando f″ ≤ 0 y convexa cuando f″ ≥ 0… f es cóncava en [a, x₀] y [x₁, x₂] y convexa en [x₀, x₁] y [x₂, b].» Coincide con la gráfica. Recorte candidato **X PDF 77**.
- **X7 (p.89-90, Feb 2018 Mod. A, Ej. 5).** f = 1/(x² + 4). (a) f′ = −2x/(x² + 4)². (b) f″ = (6x² − 8)/(x² + 4)³ (comprobado; la forma 2(3x² − 4)/(x² + 4)³ es la misma). Solución impresa: «convexa en (−∞, −2/√3) y en (2/√3, ∞) y cóncava en (−2/√3, 2/√3). No es correcto decir que es convexa en (−∞, −2/√3) ∪ (2/√3, ∞) porque en el conjunto unión de los dos intervalos no se cumple la definición 3.8 de convexidad.» (Punto fino: la convexidad se predica de un intervalo.)
  - El examen no dice expresamente que f″ cambia de signo en x = ±2/√3, es decir, que hay dos puntos de inflexión. Decirlo en el HTML.
- **X8 (p.93, Feb 2018 Mod. B, PC3).** f = x⁴ − 2x: f″ = 12x² ≥ 0 siempre ⇒ convexa en (−∞, ∞). Comprobado. Usa U Prop. 3.10.
- **X9 (p.99, Electrónica, PC3).** Enunciado: «Dibuje una gráfica que sea creciente en todo ℝ, convexa en (−∞, 0), cóncava en (0, ∞) y tenga dos asíntotas (una horizontal y una oblicua).» Solución impresa: f(x) = arctg x si x ≤ 0 y f(x) = 1/2x + arctg x (= x/2 + arctg x) si x > 0. Comprobado con sympy: f″ = −2x/(1 + x²)² en ambas ramas (≥ 0 para x ≤ 0 ⇒ convexa; ≤ 0 para x > 0 ⇒ cóncava). Asíntotas: y = −π/2 (x → −∞) e y = x/2 + π/2 (x → +∞). Figura del examen en p.99 (recorte candidato **X PDF 99**).
  - Es la misma idea que E 3.48, pero con arctg x (sin signo menos) en la rama de la izquierda.
- **X10 (p.127-128, I. Electrónica (A), Ej. 5).** f = e^{x^k}, k ∈ {0, 1, 2, …}. Concavidad (solución impresa, p.128): «para k = 2 la función es convexa en todo ℝ. Mientras que si k = 3, la función es cóncava en el intervalo (−∛(2/3), 0) y convexa en los intervalos (−∞, −∛(2/3)) y (0, ∞).» Comprobado con sympy: k = 2: f″ = (4x² + 2)e^{x²} > 0; k = 3: f″ = 3x(3x³ + 2)e^{x³}, ceros en 0 y −∛(2/3).
  - **Erratum/omisión:** para k = 3 hay **dos** puntos de inflexión, x = −∛(2/3) y x = 0, porque f″ cambia de signo en ambos. La solución solo dice «para k = 3 un punto de inflexión» (en x = 0). Corregirlo en el HTML.
  - Crecimiento: k = 2 decrece en (−∞, 0) y crece en (0, ∞); k = 3 es creciente en ℝ (f′ = 3x²e^{x³} ≥ 0, cero solo en 0).

### Vistas en el índice y excluidas (3.4 puro o sin 3.5)
- Sept 2017 Mod. A P2 (3.4: candidatos a extremo de x³ − 3x² − 9x + 2); Electrónica 2 P2 (2.5/3.4); Examen 5 Ej. 3 (f = x⁴ − 2x³: extremos y «punto de silla», 3.4); Feb 2010 Ej. 5 (3.4); Feb 2012 PC2 (3.4, valor absoluto). Pendientes para el dossier 3.4.

---

## 5. Faltas o dudas

1. **Páginas de U §3.5:** el texto va de la p. 134 (pie) a la p. 140. CLAUDE.md dice 134-139: corregir a 134-140.
2. **Símbolos perdidos en U:** en Def. 3.8 y 3.9 falta el dibujo «forma de …» (∪/∩), y el Ejemplo 3.28 está roto en el txt. Verificar en el PDF pp. 135-136.
3. **Autoevaluación de U (pp. 139-140):** no hay soluciones en el libro ni en el txt. No se han resuelto los 10 ítems; solo 6-10 son de 3.4/3.5.
4. **Stewart:** en §4.3 (pp. 293-295) y §4.5 (p. 313) el txt pierde los signos > y < de f″. Leer el PDF antes de citar literal. La cabecera de las pp. 295 (definición de inflexión y Ej. 5) y 296 (prueba de la 2ª derivada y Ej. 6) no se extrajo: la paginación se infiere de la página siguiente y debe verificarse en el PDF.
5. **Larson:** la fórmula del Ejemplo 1 de 3.4 (p. 189) y los ejemplos 1 y 2 de 3.6 (pp. 207-208) provienen de OCR; los signos se han comprobado con sympy, pero verificar en el PDF antes de citarlos. El texto de 3.6 mezcla secciones (la lista de la p. 206 remite a otras secciones) por maquetación.
6. **E 3.30:** el desarrollo confunde la inflexión con f′ = 0 (erratum, sección 3).
7. **E 3.40:** el desarrollo afirma «derivable en 4» y luego «no derivable en 4»; la correcta es no derivable. La respuesta c) no cambia.
8. **E 3.41:** la remisión «Ejercicio 3» es ambigua (no hay un ejercicio 3 con |x|).
9. **E 3.42 b):** falta «en» en el enunciado («convexa si (−∞,0)»): errata tipográfica confirmada en la imagen.
10. **E 3.43, 3.46:** el txt pierde la fracción de los enunciados. 3.43 confirmado en la imagen de E p.125 (f = 1/(1−x)). 3.46: no he visto la imagen de p.128; f = x²/(x−1) se deduce de la solución (p.129-130: f′ = x(x−2)/(x−1)², asíntota en x = 1). Verificar la imagen antes de citar el enunciado literal.
11. **E 3.45:** el enunciado dice «dos veces derivable con continuidad en ℝ \ {1}» (confirmado en imagen).
12. **E 3.47 a):** f = π es creciente/decreciente solo en sentido no estricto, lo que contradice la exigencia de b). En d) la numeración «tercero» es confusa.
13. **Figura 3.5 de E (p. 131)** y **Figura 3.5 de U (p. 136)** tienen el mismo número y son distintas: en el HTML citar siempre el libro y la página.
14. **Figuras a recortar (páginas PDF):**
    - U: **PDF 134** (Fig. 3.5: x², ln x); **PDF 136** (Fig. 3.6: x⁴ − x³ − 3x² + 10x + 1).
    - E: **PDF 114** (3.29, no es de 3.5, solo referencia); **PDF 120** (3.36, gráfica de f′); **PDF 123** (3.39 y 3.40, gráficas al margen); **PDF 125** (3.42, gráfica de f′); **PDF 126** (3.43, gráfica de f); **PDF 127** (3.45, gráfica de f′); **PDF 131** (3.46, Fig. 3.5 de E); **PDF 132-133** (3.47, gráficas de cada apartado); **PDF 134** (3.48).
    - X: **PDF 17** (gráfica de f″ de 2011); **PDF 43** (gráfica de f″ de 2014); **PDF 77** (gráfica de f″ de 2017); **PDF 99** (gráfica del ejercicio de Electrónica).
15. **X7 (Feb 2018 Mod. A, Ej. 5 b):** el examen no dice que hay dos puntos de inflexión en x = ±2/√3; decirlo en el HTML.
16. **X10:** la solución omite el segundo punto de inflexión (−∛(2/3)) para k = 3 (erratum, sección 4).
17. **X5 (Sept 2016, Ej. 5 a):** erratum «3/3!» en el polinomio de Taylor (sección 4).
18. **Exámenes X:** la mayoría de los de 3.5 son de Ingeniería Mecánica (código 68031029); los de «I. Electrónica» (p.99 y p.127-128) no tienen fecha. El temario es el mismo, pero conviene decirlo en «Así lo preguntan en el examen».
19. **Recíproco de la Prop. 3.10:** U 3.5 no enuncia como proposición que «convexa ⇒ f″ ≥ 0» (solo la implicación contraria). Se deduce de la Prop. 3.9 si f′ es derivable. E 3.39 y 3.45 lo usan.
20. **Inflexión donde f no está definida:** U Def. 3.10 no dice si f debe ser continua en c. E 3.43 y 3.46 concluyen que no hay inflexión en x = 1 porque f no está definida allí. Decidir la redacción del HTML.
