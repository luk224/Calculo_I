# Dossier Tema 6.1: Definición de integral de Riemann

Generado el 2026-10-23 a partir de `fuentes_txt/ingenieros.txt` (U), `ejercicios.txt` (E), `stewart.txt` (S), `larson.txt` (L) e `indice_examenes_1..4.md` (X, con comprobación en `examenes.txt` y render de las pp. 107 y 144 del PDF de exámenes). Páginas: U impresa = PDF + 2; E impresa = PDF; L impresa = PDF − 17 (comprobado con las cabeceras); S: número de la cabecera/pie.

## 0. Rangos de páginas

| Apartado | Impresas | PDF (U) | Contenido |
|---|---|---|---|
| U §6.1.1 Motivación | **p. 236** | 234 | Eudoxo, objetivos |
| U §6.1.2 Integral definida | **pp. 236–240** | 234–238 | Ej. 6.1 (pp. 236–238), partición y finura (p. 238), suma de Riemann y Def. 6.1 (p. 239), Ej. 6.2 (p. 239), propiedades (p. 240), Ej. 6.3 (p. 240), notación (p. 240) |
| U §6.1.3 Integral indefinida | **pp. 241–242** | 239–240 | Def. 6.2 (p. 241), Ej. 6.4 (pp. 241–242), recuadros Maxima (pp. 239, 241, 242) |
| Figuras del libro | Fig. 6.1 p. 237; Fig. 6.2 p. 238 | 235; 236 | Recortables con `herramientas/extraer_figura.py` si hacen falta |
| Fuera de 6.1 (no citado aquí) | desde p. 242 | desde 240 | §6.2 Teoremas fundamentales (6.2.1 en p. 242) |

Nota: el rango pedido «Ej. 6.1 p. 237–238» es en realidad pp. 236–238: el enunciado empieza al final de la p. 236.

## 1. U (libro oficial)

### U §6.1.1 Motivación (p. 236)
> «El cálculo de áreas o de volúmenes es un problema que, para algunas figuras, ya se sabía resolver en el antiguo Egipto (hacia 1800 a.C.) y en la Grecia clásica. La primera técnica sistemática utilizada es el método de exhaución de Eudoxo y se basa en la división de la figura en otras figuras cuyo área (o volumen) conocemos, que es el mismo principio de la integración definida.»

Objetivo declarado (p. 236): «Repasar y afianzar el concepto de integral definida e indefinida.»

### U §6.1.2 Idea de área por rectángulos (pp. 236–237)
> «Supongamos que tenemos una función continua f : [a, b] → R, que cumple f(x) ≥ 0 en [a, b] y que queremos calcular el área comprendida entre su gráfica, el eje x y las rectas verticales x = a y x = b. Podemos aproximar esta región con rectángulos, sumar sus áreas (Figura 6.1) y tomar límites cuando la base de los rectángulos se hace muy pequeña.» (p. 236)

Figura 6.1 (p. 237, PDF 235): «Aproximación del área bajo una gráfica por rectángulos.»

### U Ej. 6.1 (pp. 236–238): área bajo f(x) = eˣ en [0, 1]
- Enunciado (p. 236): «Vamos a calcular el área comprendida entre la gráfica de la parábola f(x) = eˣ en [0,1] y el eje x.» (El libro llama «parábola» a la gráfica de eˣ; ver Faltas.)
- Pasos (p. 237): se divide [0,1] en n intervalos [0,1/n], [1/n,2/n], …, [(n−1)/n, 1]; base 1/n; altura f((i−1)/n) = e^{(i−1)/n}; área del i-ésimo rectángulo (1/n)e^{(i−1)/n}; suma Sₙ = (1/n)(e⁰ + e^{1/n} + … + e^{(n−1)/n}).
- Resultado (p. 238): Sₙ = (1/n)·(e − 1)/(e^{1/n} − 1) y, «Entonces, el área que buscamos es el límite A = lím_{n→∞} Sₙ = (e − 1) lím_{n→∞} (1/n)/(e^{1/n} − 1) = e − 1». Indica: «Hemos aplicado la regla de L'Hôpital para realizar este cálculo.»
- Comprobado: la suma geométrica da (e−1)/(e^{1/n}−1) y el límite es e−1 (sympy/cálculo manual coherente con el libro).

### U §6.1.2 Áreas con signo, partición, finura y suma de Riemann (pp. 238–239)
- (p. 238) «Hemos aproximado, partiendo de rectángulos, el área bajo la gráfica de f : [a, b] → [0, ∞) sobre el eje x, entre a y b. Haciendo que la base del rectángulo sea cada vez de menor longitud y tomando límites, tenemos el área buscada.»
- (p. 238) «Podemos generalizar el cálculo del área: si la función f, continua, tiene también valores negativos, asignamos un signo al área, de forma que para f(x) ≥ 0 el área se sume y para f(x) < 0 el área se reste (Figura 6.2).»
- (p. 238) «Así, una forma general de calcular el área es a través de una partición P del intervalo [a, b] en n subintervalos dados por n + 1 puntos x₀, x₁, …, xₙ con a = x₀ < x₁ < x₂ < ··· < xₙ = b. La longitud del intervalo i-ésimo es Δxᵢ = xᵢ − xᵢ₋₁ y la finura de la partición, denotada ‖P‖, es el máximo de Δxᵢ. Elegimos cualquier cᵢ (para i = 1,…,n) en cada uno de los intervalos [xᵢ₋₁, xᵢ] y la altura de cada rectángulo es f(cᵢ).»
- Nota 1 (p. 238, al pie): «Como se hará que la base tienda a 0, la diferencia en el área por elegir distinto cᵢ resulta despreciable. Observe que para este razonamiento la continuidad de f es fundamental.»
- (p. 239) «La suma de Riemann es la suma de las áreas de estos rectángulos: S = f(c₁)Δx₁ + f(c₂)Δx₂ + ··· + f(cₙ)Δxₙ = Σᵢ₌₁ⁿ f(cᵢ)Δxᵢ. Está asociada a la partición y a los representantes cᵢ. Para funciones continuas, que son con las que trabajaremos, cuando la finura de la partición tiende a cero existe lím_{‖P‖→0} Σ f(cᵢ)Δxᵢ.»

Recuadro Maxima (p. 239): «Maxima: con “integrate(f(x),x,a,b)” se calcula la integral definida de f(x) entre a y b.»

### U Def. 6.1 (p. 239)
> «Definición 6.1. Para una función continua f : [a, b] → R, la integral definida es ∫ₐᵇ f(x) dx = lím_{‖P‖→0} Σᵢ₌₁ⁿ f(cᵢ) Δxᵢ.»

### U Ej. 6.2 (p. 239): ∫_{−1}^{2} 2x dx
- Partición: x₀ = −1, xᵢ = −1 + 3i/n, xₙ = 2; longitud Δxᵢ = 3/n; cᵢ = xᵢ (extremo derecho).
- Suma: f(cᵢ) = 2xᵢ = −2 + 6i/n; Sₙ = Σ(−2 + 6i/n)(3/n) = −6 + (18/n²)·n(n+1)/2 = 3 + 9/n.
- «Observe que la finura de la partición tiende a 0 cuando n tiende a infinito. Por eso, la integral definida es ∫_{−1}^{2} 2x dx = lím_{n→∞}(3 + 9/n) = 3.»
- Comprobado: sympy da 3.

Nota de notación (p. 240): «La integral definida también se escribe ∫ₐᵇ f.» (en el texto aparece como «a f»; los límites son los de la integral).

### U Propiedades de la integral definida (p. 240)
> «Sean f(x) y g(x) funciones continuas definidas en [a, b] y k es una constante, entonces:»
- ∫ₐᵃ f = 0 para todo f.
- Producto por constante: ∫ₐᵇ kf = k ∫ₐᵇ f.
- Suma de funciones: ∫ₐᵇ (f + g) = ∫ₐᵇ f + ∫ₐᵇ g.
- Monotonía: si f(x) ≤ g(x) en [a, b], entonces ∫ₐᵇ f ≤ ∫ₐᵇ g.
- Valor absoluto: |∫ₐᵇ f| ≤ ∫ₐᵇ |f|. (En el texto extraído la barra izquierda no aparece; ver Faltas.)
- Aditividad: si c ∈ [a, b], entonces ∫ₐᵇ f = ∫ₐᶜ f + ∫ᶜᵇ f.
- Cambio de orden en los límites: ∫ₐᵇ f = −∫ᵦᵃ f.
- «Las propiedades son fáciles de deducir a partir de la definición y su aplicación simplifica el cálculo de integrales.»

### U Ej. 6.3 (p. 240): ∫_{−1}^{2} 2x dx con propiedades
- Descomposición: ∫_{−1}^{2} 2x dx = 2∫_{−1}^{2} x dx = 2∫_{−1}^{0} x dx + 2∫_{0}^{2} x dx.
- La primera integral es −1/2 (triángulo de base 1 y altura 1 bajo el eje x: «por eso este valor se resta»); la segunda es 2 (triángulo de base 2 y altura 2).
- Resultado del libro: 2·(−1/2) + 2·2 = 3. Comprobado: 3.

### U §6.1.3 Integral indefinida (pp. 241–242)
- (p. 241) «El cálculo de integrales definidas utilizando la definición o sus propiedades puede resultar bastante laborioso, incluso puede que no lleguemos a ningún resultado. Por eso, vamos a estudiar un procedimiento más directo.»
- (p. 241) «En el capítulo anterior hemos estudiado derivadas; ahora es el momento de preguntarnos cuándo y cómo se puede invertir este proceso. Vamos a seguir trabajando con funciones continuas.»

### U Def. 6.2 (p. 241)
> «Definición 6.2. Si tenemos una función continua f : (a, b) → R, cualquier F que verifique F′(x) = f(x) para todo x ∈ (a, b) es una primitiva de f. Se denota: F(x) = ∫ f(x) dx. La integral indefinida de f es el conjunto de todas las primitivas de f. En esta expresión, f(x) es el integrando, x es la variable de integración y dx indica respecto a qué variable se integra.»

- Notación (p. 241): «La notación es muy similar a la usada para la integral definida: la diferencia formal obvia entre ambas es que las integrales definidas tienen límites de integración, que son los números indicados a la derecha del símbolo de integración y que nos indican el intervalo sobre el que se integra.»
- Notación (p. 241, margen): «Con F se denota también una primitiva de f.»

### U Ej. 6.4 (pp. 241–242): primitivas de 2x − 1
- (p. 241) «Dada F(x) = x² − x, sabemos que F′(x) = 2x − 1. Por eso, una primitiva de 2x − 1 es x² − x. Pero también lo son x² − x + 1 o x² − x + 3. Y en general, ∫(2x − 1) dx = x² − x + k para cualquier número real k. Se comprueba derivando el resultado.»
- (p. 241) «En el tema 2 vimos que dos funciones con la misma derivada en un intervalo se diferencian en una constante y viceversa. Lo mismo ocurre para integrales indefinidas. La integral indefinida es un conjunto de funciones porque si F(x) es una primitiva de f(x) también lo va a ser F(x) + k para cualquier constante real k, al cumplirse F′ = (F + k)′.»
- (p. 241–242) «… si tenemos dos primitivas F(x) y G(x) de una función f(x) en [a, b], entonces existe una constante real k tal que F(x) − G(x) = k. Por eso, al escribir la integral indefinida de f elegimos cualquier primitiva y le añadimos una constante k.»

Recuadros Maxima: p. 241 «Maxima: para una integral indefinida se utiliza “integrate(f(x),x);”»; p. 242 «Maxima toma por defecto la arbitraria constante k = 0» (la extracción reparte el recuadro en dos líneas).

### Otros textos de p. 242 (inicio de §6.2, fuera de 6.1)
Encabezado de §6.2 y su introducción aparecen en p. 242. El Teorema 6.1 (p. 243) y el 6.2 (p. 244) pertenecen a §6.2 y no se transcriben aquí.

## 2. S (Stewart) y L (Larson)

### S §5.1 Áreas y distancias: área como límite (p. 363)
- Resumen: el área de una región se define como límite de las sumas de rectángulos de aproximación.
- Extracto (p. 363, cabecera «SECCIÓN 5.1 ÁREAS Y DISTANCIAS 363»): «Por tanto, definimos el área A como el límite de las sumas de las áreas de los rectángulos de aproximación; esto es, A = lím_{n→∞} Rₙ = lím_{n→∞} Lₙ.»

### S §5.2 La integral definida: Definición 2 (p. 372)
- Resumen: la integral como límite de sumas de Riemann con puntos muestra arbitrarios; es la definición que usa el libro para todo el tema.
- Extracto (p. 372): «Entonces la integral definida de f, desde a hasta b, es ∫ₐᵇ f(x) dx = lím_{n→∞} Σᵢ₌₁ⁿ f(x*ᵢ) Δx, siempre que este límite exista y dé el mismo valor para todas las posibles elecciones de los puntos muestra. Si existe, decimos que f es integrable sobre [a, b].»
- Extracto (p. 372): «La suma de Riemann… Sabemos que si f es positiva, entonces la suma de Riemann puede interpretarse como una suma de áreas de los rectángulos de aproximación.»

### S §5.2 Integral como área neta (p. 373)
- Resumen: si f cambia de signo, la integral es diferencia de áreas.
- Extracto (p. 373): «Una integral definida puede interpretarse como un área neta; es decir, una diferencia de áreas: ∫ₐᵇ f(x) dx = A₁ − A₂, donde A₁ es el área de la región arriba del eje x y debajo de la gráfica de f, y A₂ corresponde al área de la región debajo del eje x y arriba de la gráfica de f.»
- Nota 4 (p. 373): anchos desiguales, «máx Δxᵢ → 0». Nota 5 (p. 373): Teorema 3 (continuidad o pocas discontinuidades de salto implican integrabilidad).

### S §5.2 Teorema 4: puntos extremos derechos (p. 374) y Ej. 1 (p. 374)
- Resumen: con puntos muestra en el extremo derecho, la definición se simplifica; útil para «leer» un límite de sumas como integral.
- Extracto (p. 374): «Si f es integrable sobre [a, b], entonces ∫ₐᵇ f(x) dx = lím_{n→∞} Σᵢ₌₁ⁿ f(xᵢ) Δx, donde Δx = (b − a)/n y xᵢ = a + iΔx.»
- Ej. 1 (p. 374): expresar lím Σ(xᵢ³ − xᵢ sen xᵢ)Δx como integral sobre [0, π] (el signo menos no se extrae bien del texto; confirmar en PDF) (paso de límite de suma a integral; «reemplazamos lím Σ por ∫, x*ᵢ por x y Δx por dx»).

### S §5.2 Propiedades de la integral (pp. 379–381)
- Resumen: linealidad, monotonía y aditividad; las propiedades 1–4 y 5 se enuncian en las pp. 379–381.
- Extracto (p. 379–380): «Suponga que f y g son funciones continuas. 1. ∫ₐᵇ c dx = c(b − a); 2. ∫ₐᵇ [f(x) + g(x)] dx = ∫ₐᵇ f(x) dx + ∫ₐᵇ g(x) dx; 3. ∫ₐᵇ c f(x) dx = c ∫ₐᵇ f(x) dx; 4. ∫ₐᵇ [f(x) − g(x)] dx = ∫ₐᵇ f(x) dx − ∫ₐᵇ g(x) dx.»
- Extracto (p. 381): «5. ∫ₐᶜ f(x) dx + ∫ᶜᵇ f(x) dx = ∫ₐᵇ f(x) dx» (propiedad de intervalos, con el ejemplo 7: si ∫₀¹⁰ f = 17 y ∫₀⁸ f = 12, entonces ∫₈¹⁰ f = 5).
- Pág. 379: Stewart define ∫ₐᵃ f = 0 y ∫ₐᵇ f = −∫ᵦᵃ f para a > b.

### L §4.2 Área (pp. 259–262)
- Teorema 4.3 (p. 260): «Sea f continua y no negativa en el intervalo [a, b]. Los límites cuando n → ∞ de las sumas inferior y superior existen y son iguales entre sí.»
- Ej. 5 (p. 261): área bajo f(x) = x³ en [0,1] como límite de sumas con extremos derechos cᵢ = i/n; resultado 1/4.
- Ej. 7 (p. 262): región limitada por x = y² y el eje y, con resultado 1/3 (ejemplo de «eje y»).

### L §4.3 Sumas de Riemann e integrales definidas (pp. 266–272)
- Definición de suma de Riemann (p. 267, PDF 284):
  > «Sea f definida en el intervalo cerrado [a, b] y sea Δ una partición de [a, b] dada por a = x₀ < x₁ < … < xₙ₋₁ < xₙ = b, donde Δxᵢ es el ancho del i-ésimo subintervalo. Si cᵢ es cualquier punto en el i-ésimo subintervalo [xᵢ₋₁, xᵢ], entonces la suma Σ f(cᵢ) Δxᵢ se denomina suma de Riemann de f para la partición Δ.»
  Norma (p. 267): «El ancho del subintervalo más grande de la partición Δ es la norma de la partición y se denota por ‖Δ‖.» Y: «ʈʈ∆ʈʈ → 0 implica n → ∞; la afirmación recíproca no es cierta» (contraejemplo con particiones de norma 1/2, p. 267).
- Definición de integral definida (p. 268, PDF 285):
  > «Si f se define en el intervalo cerrado [a, b] y el límite de las sumas de Riemann sobre las particiones Δ, lím_{‖Δ‖→0} Σ f(cᵢ) Δxᵢ, existe…, entonces f es integrable en [a, b] y el límite se denota por ∫ₐᵇ f(x) dx. El número a es el límite inferior de integración, y el número b es el límite superior de integración.»
  Comentario (p. 268): «Una integral definida es un número, en tanto que una integral indefinida es una familia de funciones.»
- Teorema 4.4 (p. 268): «Si una función f es continua en el intervalo cerrado [a, b], entonces f es integrable en [a, b].»
- Ej. 2 (p. 269): ∫_{−2}^{1} 2x dx como límite de sumas con extremos derechos; resultado −3 (negativa; no es área).
- Teorema 4.5 (p. 269): «Si f es continua y no negativa en el intervalo cerrado [a, b], entonces el área de la región acotada por la gráfica de f, el eje x y las rectas verticales x = a y x = b está dada por Área = ∫ₐᵇ f(x) dx.»
- Ej. 3 (p. 270): áreas geométricas (rectángulo, trapecio, semicírculo) para evaluar ∫ sin fórmula de límite.
- Definiciones especiales y Ej. 4 (p. 271): «1. Si f está definida en x = a, entonces ∫ₐᵃ f(x) dx = 0. 2. Si f es integrable en [a, b], entonces ∫ₐᵇ f(x) dx = −∫ᵦᵃ f(x) dx.»
- Teorema 4.6, propiedad aditiva de intervalos (p. 271): «Si f es integrable en los tres intervalos cerrados determinados por a, b y c, entonces ∫ₐᵇ f = ∫ₐᶜ f + ∫ᶜᵇ f.»
- Teorema 4.7 (p. 272): «Si f y g son integrables en [a, b] y k es una constante, entonces kf y f ± g son integrables en [a, b], y 1. ∫ₐᵇ kf = k∫ₐᵇ f; 2. ∫ₐᵇ [f ± g] = ∫ₐᵇ f ± ∫ₐᵇ g.»
- Teorema 4.8 (p. 272): conservación de desigualdades: si f es integrable y no negativa, ∫ₐᵇ f ≥ 0; si f ≤ g en [a, b], ∫ₐᵇ f ≤ ∫ₐᵇ g.

## 3. E (libro de ejercicios): Ejercicios 6.1 a 6.10

Enunciados transcritos (E = PDF, pp. 214–218). Mapa U: 6.1–6.3 → §6.1.2 (partición, finura, suma de Riemann); 6.4–6.8 → §6.1.2 propiedades (p. 240); 6.9 → TVM del cálculo integral (propiedades + continuidad; el enunciado de TVM integral se menciona en el margen de U p. 244, §6.2, y no se transcribe aquí); 6.10 → §6.1.3 Def. 6.2 (integral indefinida).

### Ejercicio 6.1 (E p. 214) [§6.1.2, finura]
- Enunciado: «Calcula la finura ‖P‖ de la partición P = {1, 2, 3, 5, 6} del intervalo [1, 6].»
- Solución (p. 214): subintervalos [1,2], [2,3], [3,5], [5,6]; el de mayor longitud es [3,5] con longitud 2 → ‖P‖ = 2.
- Método: finura = máxima longitud de los subintervalos.

### Ejercicio 6.2 (E p. 214) [§6.1.2, construir particiones]
- Enunciado: «Define una partición de [0, 4] con cien elementos distintos y finura igual a 3.»
- Solución (p. 214): dos particiones válidas: P = {0, 3, x₃, …, x₁₀₀} con xᵢ = 3 + i/100; o P = {y₀, y₁, …, y₉₈, 4} con yᵢ = i/98 (confirmado en render).
- Método: construir una partición explícita y comprobar que el mayor subintervalo mide 3.

### Ejercicio 6.3 (E p. 214) [§6.1.2, cota de la finura]
- Enunciado: «¿Puede ser la finura ‖P‖ de una partición del intervalo [−π, π] igual a 7?»
- Solución (p. 214): no; cada subintervalo mide como mucho 2π ≈ 6.2832 < 7.
- Método: cota superior de la longitud de cualquier subintervalo.

### Ejercicio 6.4 (E pp. 214–215) [§6.1.2, integral de la función nula]
- Enunciado: «Muestra que la integral definida de la función nula es cero en cualquier intervalo: (i) utilizando la definición de integral; (ii) utilizando las propiedades de la integral (pista: solamente 0 verifica 0 + 0 = 0).»
- Solución (p. 215): (i) ∫ₐᵇ 0 = lím Σ 0·Δxᵢ = 0. (ii) ∫ₐᵇ 0 = ∫ₐᵇ (0 + 0) = ∫ₐᵇ 0 + ∫ₐᵇ 0; como a = a + a solo tiene solución a = 0, la integral es 0.
- Método: definición; o propiedad de suma y «único número con a + a = a».

### Ejercicio 6.5 (E pp. 215–216) [§6.1.2, propiedades]
- Enunciado: «Dadas f, g continuas en [a, b] señala la o las propiedades que no son siempre correctas: a) ∫ₐᵇ (f + g) = ∫ₐᵇ f + ∫ₐᵇ g; b) ∫ₐᵇ |f + g| = ∫ₐᵇ |f| + ∫ₐᵇ |g|; c) ∫ₐᵇ (f − g) = ∫ₐᵇ f + ∫ᵇₐ g; d) ∫ₐᵇ |f − g| = ∫ₐᵇ |f| − ∫ᵇₐ |g|.»
- Solución (pp. 215–216): a) y c) son ciertas (c: ∫(f − g) = ∫f + ∫(−g) = ∫f − ∫g = ∫f + ∫ᵇₐ g). b) y d) son falsas: contraejemplo f = 1 y g = −f en [a,b]: en b) la izquierda vale 0 y la derecha 2(b − a); en d) la izquierda vale 2(b − a) y la derecha 0.
- Método: propiedades de linealidad y contraejemplo constante.

### Ejercicio 6.6 (E pp. 216–217) [§6.1.2, propiedades]
- Enunciado: «Dadas f, g : [a, b] → R continuas, señala la propiedad que no es siempre correcta: a) (b − a) mín f ≤ ∫ₐᵇ f ≤ (b − a) máx f; b) ∫ₐᵇ f·g = ∫ₐᵇ f · ∫ₐᵇ g; c) ∫ₐᵇ f = ∫ₐ^{(a+b)/2} f + ∫_{(a+b)/2}ᵇ f.»
- Solución (pp. 216–217): a) es cierta (monotonía con f mín ≤ f ≤ f máx). c) es cierta (aditividad con c = (a+b)/2). b) es falsa: f(x) = g(x) = x en [0,1]: ∫₀¹ x·x dx = 1/3 ≠ (1/2)(1/2) = 1/4 (sympy: 1/3 y 1/4). Respuesta: b).
- Método: monotonía y aditividad; contraejemplo numérico.

### Ejercicio 6.7 (E p. 217) [§6.1.2, acotación]
- Enunciado: «Demuestra que si f : [−1, 1] → R es continua y tal que −2 ≤ f(x) ≤ 4 para todo x ∈ [−1, 1], entonces −4 ≤ ∫₋₁¹ f(x) dx ≤ 8.»
- Solución (p. 217): por monotonía, ∫₋₁¹ (−2) dx ≤ ∫₋₁¹ f ≤ ∫₋₁¹ 4 dx; −4 = −2·[1 − (−1)] ≤ ∫ ≤ 4·[1 − (−1)] = 8.
- Método: acotar por funciones constantes (monotonía).

### Ejercicio 6.8 (E p. 217) [§6.1.2, aditividad]
- Enunciado: «Calcula ∫_{−π}^{π/2} f, con f continua en R y tal que ∫_{−π}^{e} f = ∫_{π/2}^{e} f.» (El límite superior «e» se lee en el render de la p. 217.)
- Solución (p. 217): por aditividad ∫_{−π}^{e} f = ∫_{−π}^{π/2} f + ∫_{π/2}^{e} f; restando la igualdad dada: 0 = ∫_{−π}^{π/2} f. Resultado: 0.
- Método: aditividad y resta de igualdades.

### Ejercicio 6.9 (E p. 218) [§6.1.2, teorema del valor medio integral]
- Enunciado: «Demuestra el teorema del valor medio del cálculo integral que garantiza, para cualquier función continua en [a, b], la existencia de un punto c ∈ [a, b] tal que ∫ₐᵇ f(x) dx = f(c)(b − a).»
- Solución (p. 218): usa (b − a) mín f ≤ ∫ₐᵇ f ≤ (b − a) máx f (ejercicio 6.6 a) y el teorema de los valores intermedios aplicado a (b − a)f en [a,b]; hay un c con ∫ = f(c)(b − a).
- Método: TVI + monotonía de la integral.

### Ejercicio 6.10 (E p. 218) [§6.1.3, primitiva]
- Enunciado: «Sea F : R → R una primitiva de una función continua f : R → R y C ∈ R una constante. Señala la opción correcta: a) F′(x) = f(x) para x ∈ R. b) f′(x) = F(x) + C para x ∈ R. c) f′(x) = F(x) para x ∈ R. d) F′(x) = f(x) + C para x ∈ R.»
- Solución (p. 218): a) es la definición de primitiva (Def. 6.2). Contraejemplo f = 1, F = x, C = 1 invalida b), c) y d).
- Método: aplicar la definición de primitiva y contraejemplo.

### Ejercicio 6.11 (E pp. 218–219) [FUERA DEL ALCANCE: Teorema fundamental del cálculo, §6.2]
- Enunciado en p. 218 (opciones a)–d) sobre derivada de F + C, derivada de f + C, F = ∫ f + C, «ninguna»). Solución en pp. 218–219: a) es correcta (G = F + C también es primitiva; G′ = f); b) falsa (f puede no ser derivable); c) falsa (contraejemplo F = x, f = 1). Excluido de este tema.

## 4. X (exámenes resueltos, pruebas presenciales): preguntas de 6.1

Búsqueda por palabras clave en `indice_examenes_1..4.md` (Riemann, suma, propiedad, área, V/F, F(x)=∫f, signo, integrable, valor medio) y lectura en `examenes.txt`. Ningún índice tiene la palabra «Riemann» ni preguntas de sumas de Riemann o propiedades puras.

| Convocatoria | Pág. PDF (enunc. → sol.) | Pregunta | Qué tipo | Verificación | Estado |
|---|---|---|---|---|---|
| Electrónica 4 (sin fecha, Electrónica Industrial y Automática) | **107** (enunciado y solución en la misma página) | P4 corta: V/F «Si f es derivable y decreciente en (0,∞), entonces F(x) = ∫₀ˣ f(s) ds es decreciente en (0,∞)». Solución: falsa, con f = 1/x | F(x)=∫f, signo de F′ (TFC) | Render de la p. 107 (leído) y texto | Enunciado correcto; **el contraejemplo es inválido** (∫₀ˣ ds/s diverge; ver Faltas). Tema principal: 6.2 (TFC), relacionado con 6.1 |
| Examen 1 («elaborado con exámenes de asignaturas similares», no es examen oficial UNED) | **109** (enunc.) → **110** (sol.) | Ej. 4: F(x) = ∫₀ˣ t sen t dt definida en [0, ∞): A) creciente; B) máximo en x = 7π; C) decreciente; D) ninguna | F(x)=∫f, monotonía y extremos | Texto pp. 109–110; sympy: F′ = x sen x, F″(7π) = −7π < 0 | Respuesta B correcta. Tema principal 6.2/3.4 |
| Feb 2018, 1ª semana (I. Electrónica Industrial y Automática) | **144** (enunciado y solución en la misma página) | P3 corta: V/F «Si f es continua y creciente en (0,∞), entonces F(x) = ∫₀ˣ f(t) dt es creciente en (0,∞)». Solución: falsa, con f(x) = −1/x² | F(x)=∫f, monotonía | Render de la p. 144 (leído) | Conclusión correcta; **el contraejemplo es inválido** (∫₀ˣ −1/t² dt diverge; ver Faltas). Contraejemplo válido: f(t) = t − 1 (sympy: F = x²/2 − x, F′ = x − 1, no creciente en (0,1)) |
| Examen 5 («elaborado con exámenes de asignaturas similares») | **122** (enunc.) → **122–123** (sol.) | Ej. 1: f = x², g = x³, h = √x; área encerrada por f y g frente a f y h frente a g y h en [0,1]: opción B | Área entre curvas como ∫(sup − inf) (g ≤ f ≤ h en [0,1]) | Sympy: A(f,g) = 1/12; A(f,h) = 1/3; A(g,h) = 5/12 → B | Verificada en texto; solución correcta. Render de p. 122 no visto (solo texto) |

Preguntas de X que se resuelven con material de 6.1 y que **quedan para otros temas** (no incluidas arriba):
- **6.3 (primitivas)**: Examen 2 Ej. 3 (p. 113): área bajo tg x entre 0 y π/4 = (ln 2)/2 (requiere ∫ tg x); Examen 4, Ej. 3 (p. 119): primitiva de (x+1)/(x²−3x).
- **6.4 (numérica)**: trapecio/Simpson de «∫ f» con tablas, p. ej. Examen 1 Ej. 6 (p. 111), Examen 5 Ej. 5 (pp. 123–124), Electrónica 4 Ej. 5 (p. 107), Feb 2016 Ej. 5 (pp. 65–66), Feb 2014 PC3 (p. 40), Feb 2012 Ej. 5 (p. 23).
- **6.5 (impropias)**: Sept 2012 PC2 (p. 25): «Razone si ∫ₐᵇ f con a, b ∈ (−10,10) puede ser impropia» → «sí, de segunda especie» (toca la definición de integrable; conviene leerlo en 6.5). Electrónica 3 Ej. 5 (p. 105), Feb 2019 P2 (p. 150), Sept 2016 Modelo B P3 (p. 73: clasificar ∫₀^∞ e^{−x} dx).

## 5. Faltas o dudas

1. **Ej. 6.1 de U (p. 236–238)**: el rango pedido (237–238) no es exacto: el enunciado empieza en la p. 236; el texto dice «parábola» para f(x) = eˣ (dudosa redacción del libro, sin efecto en el cálculo).
2. **Finura en U (p. 238)**: la extracción da «denotada P» sin barras; el símbolo correcto (‖P‖) aparece en E (p. 214) y en la definición. Confirmar en el PDF.
3. **Valor absoluto en propiedades de U (p. 240)**: la extracción da «b f ≤ b |f|»; la barra izquierda no aparece. Interpretado como |∫ₐᵇ f| ≤ ∫ₐᵇ |f|; confirmar en el PDF.
4. **Recuadros Maxima (pp. 239, 241, 242)**: texto recuperado de la extracción; el de p. 242 («k = 0») está repartido en dos líneas. Revisar en PDF si se cita textualmente.
5. **X, Electrónica 4 P4 (p. 107)**: la solución da como contraejemplo f(x) = 1/x; esa f no es integrable en [0, x] (∫₀ˣ ds/s = ∞; sympy), así que el contraejemplo no vale aunque la conclusión (falsa) sea correcta. Alternativa válida que sí comprobamos: f(s) = 1/(s + 1) (F = ln(1 + x), F′ > 0 con f decreciente). Sin renombrar el examen; solo a efectos de estudio.
6. **X, Feb 2018 1ª semana P3 (p. 144)**: mismo problema: f(x) = −1/x² no es integrable en [0, x]. Conclusión (falsa) correcta; contraejemplo válido sugerido f(t) = t − 1.
7. **X, Examen 1 Ej. 4 (pp. 109–110)**: es un «examen elaborado con exámenes de asignaturas similares», no un examen oficial de Cálculo UNED; su solución es correcta. Tiene una errata menor de escritura («F(x)» en lugar de «F″(x)» al derivar dos veces).
8. **E 6.2 (p. 214)**: yᵢ = i/98 confirmado en el render. Ninguna duda.
9. **E 6.8 (p. 217)**: límite superior «e» en la condición (confirmado en el render; se interpreta como el número e, coherente con la solución).
10. **S (Stewart), pp. 379–381**: propiedades 1–4 en pp. 379–380 y propiedad 5 en p. 381 según cabeceras; las páginas PDF 800–801 no tienen cabecera extraída y la numeración 379/380/381 en esa zona no está confirmada al 100 %. Revisar antes de citar exactamente.
11. **S (Stewart), p. 372–374**: Def. 2 (p. 372), área neta (p. 373), Teorema 4 y Ej. 1 (p. 374) verificados por cabecera. Stewart 5.1 (p. 363): cabecera verificada.
12. **L (Larson)**: impresa = PDF − 17 verificado con las cabeceras (pp. 259–272 verificadas). Teorema 4.3 (p. 260) y Ej. 5 (p. 261), Ej. 7 (p. 262) verificados por texto, no por render.
13. **U 6.1 (pp. 236–242)**: verificado en texto (`ingenieros.txt`, PDF 234–240). No se ha renderizado el PDF de U en esta tarea; las figuras 6.1 y 6.2 no están recortadas.
14. **Teorema del valor medio integral**: el libro lo cita en el margen de p. 244 (§6.2) y E 6.9 lo demuestra; no se ha transcrito el enunciado del libro porque cae en 6.2. Pendiente de confirmar la página exacta del enunciado en U.
15. **S, Ej. 1 (p. 374)**: el signo de f(x) = x³ − x sen x se lee con dificultad en la extracción; confirmar en PDF.
16. **X**: no se han encontrado en los índices 1–4 preguntas sobre sumas de Riemann ni sobre la definición formal de la integral. Si el usuario quiere cubrir ese hueco, habría que buscar en el PDF de exámenes sin índice (páginas no indexadas).
