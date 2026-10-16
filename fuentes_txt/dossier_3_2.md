# Dossier Tema 3.2: Aplicaciones a series y sucesiones de funciones

**Fuentes**: U = *Cálculo para Ingenieros* (`ingenieros.txt`), §3.2, pp. 113-119 impresas (PDF 111-117; impresa = PDF + 2). S = *Cálculo de una variable* (Stewart), cap. 11 (`stewart.txt`). L = *Cálculo Tomo 1* (Larson), cap. 9 (`larson.txt`). E = libro de ejercicios (`ejercicios.txt`, impresa = PDF). X = *Exámenes resueltos* (`Examenes-resueltos-Calculo.pdf`, página PDF, leída como imagen).

**Alcance de examen**: solo las series de Taylor y las funciones analíticas (U §3.2.3, pp. 117-118). El resto de §3.2 (convergencia uniforme y derivación de sucesiones/series de funciones, pp. 113-115, y el ejemplo 3.11) va colapsado en el resumen como «Fuera de examen». La derivación de series de potencias (Prop. 3.3 y Teor. 3.1, p. 116) se trata como examen porque lo usan E 3.18 y X p. 112; confirmar con el docente (ver «Faltas o dudas»).

**Notación**: en `stewart.txt` el signo «=» aparece como «m» en varias fórmulas; los extractos de S están normalizados. Las tildes de U se han restaurado (el texto extraído las pierde). Las derivadas se escriben con el signo ′.

---

## 1. LIBRO OFICIAL (U), §3.2

### 3.2.1 Motivación y objetivos (p. 113)

Texto: «En esta sección veremos por un lado cómo se trasmite la derivación en el paso al límite de una sucesión o serie funcional. Por otro, veremos qué ocurre al hacer un paso al límite en el orden de los polinomios de Taylor de una función f.»

Objetivos (p. 113): «… ciertas funciones tienen la interesante propiedad de poder ser representadas localmente como una serie de potencias.» (Esta es la idea de 3.2.3.)

### 3.2.2 Derivación de sucesiones y series de funciones (pp. 113-115) — FUERA DE EXAMEN

Proposición (p. 114, sin número): sea {f_n} una sucesión de funciones definidas en un intervalo acotado (a,b), con f_n derivables; si {f_n′} converge uniformemente en (a,b) y existe x_0 ∈ (a,b) con {f_n(x_0)} convergente, entonces {f_n} converge uniformemente en (a,b) a una función límite f, derivable en (a,b), y f′(x) = lím_{n→∞} f_n′(x) para todo x ∈ (a,b).
Comentario del libro (p. 114): la convergencia uniforme de {f_n′} es «una condición suficiente pero no es una condición necesaria».

Ejemplo 3.11 (pp. 114-115): f_n(x) = x/(1+n²x²) en (−1,1). Converge puntualmente a 0; sup|f_n − f| = 1/(2n), luego converge uniformemente a 0; pero f_n′(0) = 1 para todo n, así que {f_n′} no converge uniformemente.

Proposición para series (p. 115): análoga para series de funciones derivables con la serie de derivadas uniformemente convergente.

### 3.2.2 (cont.) Derivación de series de potencias (p. 116) — EXAMEN (ver nota de alcance)

Proposición 3.3 (p. 116): «Si f(x) = Σ_{n=0}^∞ a_n x^n para todo x ∈ (−c, c), entonces f es derivable en (−c, c) y f′(x) = Σ_{n=0}^∞ d/dx (a_n x^n) para todo x ∈ (−c, c).»

Teorema 3.1 (p. 116): «Una serie de potencias Σ a_n x^n define una función infinitamente derivable en su intervalo de convergencia, cuyas derivadas pueden obtenerse derivando término a término: d^p/dx^p (Σ a_n x^n) = Σ d^p/dx^p (a_n x^n) para todo p.»

Ejemplo 3.12 (p. 116): derivar término a término la serie f(x) = x − x³/3! + x⁵/5! − … da 1 − x²/2! + x⁴/4! − …

### 3.2.3 Funciones analíticas (pp. 117-118) — EXAMEN

Definición (p. 117, sin número): «… f una función que tiene derivadas de todos los órdenes en x_0; estas series reciben el nombre de serie de Taylor de f en x_0», es decir, Σ_{n=0}^∞ f^{(n)}(x_0)/n! (x − x_0)^n.

Observación (p. 117): «Claramente la serie de Taylor es el resultado de hacer tender a infinito el orden del polinomio de Taylor de f centrado en x_0.»

Ejemplo 3.13 (p. 117): f(x) = e^{2x} en x_0 = 0. f^{(n)}(x) = 2^n e^{2x}, luego la serie es Σ 2^n x^n/n!. Criterio del cociente: lím |a_{n+1}/a_n| = lím 2/(n+1) = 0, radio infinito. (El libro menciona Maxima con «powerseries(exp(2*x), x, 0);».)

Ejemplo 3.14 (p. 117): f(x) = cos x en 0. Las derivadas impares se anulan y las pares valen alternativamente −1 y 1: 1 − x²/2! + x⁴/4! − x⁶/6! + … = Σ_{k=0}^∞ (−1)^k/(2k)! x^{2k}.

Texto (p. 117): «Lo más deseable es que la serie de Taylor converja uniformemente a la función que la define en un intervalo que contenga a x_0. Pero esto no siempre ocurre. Las funciones para las que sí ocurre … reciben el nombre de funciones analíticas.»

Texto (p. 118): «Las funciones polinómicas, trigonométricas, exponenciales y logarítmicas son analíticas.»

Texto (p. 118): «En su intervalo de convergencia una serie de potencias es la serie de Taylor de su suma. Es decir, en su intervalo de convergencia una serie de potencias define una función analítica.» Y: al derivar término a término se comprueba que f^{(n)}(0) = n! a_n, luego a_n = f^{(n)}(0)/n!.

Ejemplo 3.15 (pp. 118-119): desarrollar x² cos x³ en serie de potencias de x.
- Primera forma (p. 118): sustituir x por x³ en cos x = 1 − x²/2! + x⁴/4! − …: cos x³ = 1 − x⁶/2! + x¹²/4! − x¹⁸/6! + …; multiplicar por x²: x² − x⁸/2! + x¹⁴/4! − x²⁰/6! + …, «un desarrollo válido para todo x».
- Segunda forma (p. 119): x² cos x³ = d/dx [ (1/3) sen x³ ]; desarrollar (1/3) sen x³ = x³/3 − x⁹/(3·3!) + … y derivar término a término: x² − x⁸/2! + x¹⁴/4! − …

Nota de U (p. 118): a la vista del ejemplo 3.14, cos x = Σ (−1)^k/(2k)! x^{2k}, y derivando ambos miembros resulta −sen x = −x + x³/3! − x⁵/5! + … (signos tal como aparecen en el libro).

---

## 2. LIBRO STEWART (S), cap. 11: series de Taylor y de Maclaurin (§11.10)

Sección 11.10 desde la p. 753 (cabeceras de página; S impresa = número de la cabecera).

Teorema 5 (p. 754): «Si f se puede representar como una serie de potencias (expansión) en a, es decir, si f(x) = Σ c_n (x − a)^n, |x − a| < R, entonces sus coeficientes están dados por la fórmula c_n = f^{(n)}(a)/n!.»

Definición (p. 754): la serie f(x) = Σ f^{(n)}(a)/n! (x − a)^n se denomina serie de Taylor de f en a. Para a = 0 se llama serie de Maclaurin.

Ejemplo 1 (p. 754): serie de Maclaurin de e^x: Σ x^n/n!; el radio es infinito por la prueba de la razón.

Polinomio de Taylor y residuo (p. 755): T_n(x) = Σ_{i=0}^n f^{(i)}(a)/i! (x − a)^i, polinomio de Taylor de grado n; R_n(x) = f(x) − T_n(x).

Teorema 8 (p. 756): «Si f(x) = T_n(x) + R_n(x), donde T_n es el polinomio de Taylor de n-ésimo grado de f en a y lím_{n→∞} R_n(x) = 0 para |x − a| < R, entonces f es igual a la suma de sus series de Taylor en el intervalo |x − a| < R.»

Teorema 9, desigualdad de Taylor (p. 756): «Si |f^{(n+1)}(x)| ≤ M para |x − a| ≤ d, entonces el residuo R_n(x) cumple |R_n(x)| ≤ M |x − a|^{n+1} / (n+1)! para |x − a| ≤ d.»

Forma de Lagrange del residuo (p. 756): «hay un número z entre x y a tal que R_n(x) = f^{(n+1)}(z)/(n+1)! (x − a)^{n+1}.» (El libro la presenta como generalización del teorema del valor medio.)

Ecuación 10 (p. 757): para todo número real x, lím_{n→∞} x^n/n! = 0.

Ejemplo 2 (p. 757): e^x es igual a la suma de su serie de Maclaurin. Para |x| ≤ d, |f^{(n+1)}(x)| = e^x ≤ e^d; la desigualdad de Taylor da |R_n(x)| ≤ e^d |x|^{n+1}/(n+1)! → 0.

Ejemplo 3 (p. 757): serie de Taylor de e^x en a = 2: Σ e² (x − 2)^n/n!.

Teorema 17, serie binomial (p. 761): si k es cualquier número real y |x| < 1, (1 + x)^k = Σ_{n=0}^∞ C(k,n) x^n = 1 + kx + k(k−1)/2! x² + k(k−1)(k−2)/3! x³ + …

Tabla 1 (p. 762): series de Maclaurin importantes: 1/(1−x) = Σ x^n (R = 1); e^x = Σ x^n/n!; sen x = Σ (−1)^n x^{2n+1}/(2n+1)!; cos x = Σ (−1)^n x^{2n}/(2n)!; arctan x = Σ (−1)^n x^{2n+1}/(2n+1) (R = 1); ln(1+x) = Σ_{n≥1} (−1)^{n+1} x^n/n (R = 1); (1+x)^k binomial (R = 1).

Otros: el ejemplo 10 (p. 762) suma una serie numérica con la tabla; el ejemplo 11 (pp. 762-763) integra e^{−x²} como serie. La sección 11.11 (pp. 769-775) trata la aplicación a la aproximación y a errores (la parte de Taylor que se estudia en 3.1).

---

## 3. LIBRO LARSON (L), cap. 9

### L §9.7 Residuo de un polinomio de Taylor (pp. 641-642)

Teorema 9.19 (Teorema de Taylor, p. 642): «Si una función f es derivable hasta el orden n + 1 en un intervalo I que contiene a c, entonces, para cada x en I, existe z entre x y c tal que f(x) = f(c) + f′(c)(x − c) + … + f^{(n)}(c)/n! (x − c)^n + R_n(x), donde R_n(x) = f^{(n+1)}(z)/(n+1)! (x − c)^{n+1}.»
Consecuencia (p. 642): |R_n(x)| ≤ |x − c|^{n+1}/(n+1)! · máx |f^{(n+1)}(z)|.

### L §9.10 Series de Taylor y Maclaurin (pp. 664-669)

Teorema 9.22 (p. 664): «Si f es representada por una serie de potencias f(x) = Σ a_n (x − c)^n para todo x en un intervalo abierto I que contiene c, entonces a_n = f^{(n)}(c)/n!.»

Definición (p. 665): «Si una función f tiene derivadas de todos los órdenes en x = c, entonces la serie Σ f^{(n)}(c)/n! (x − c)^n se llama serie de Taylor para f(x) en c. Además, si c = 0, entonces la serie es la serie de Maclaurin para f.»

Ejemplo 1 (pp. 665-666): serie de Maclaurin de sen x: x − x³/3! + x⁵/5! − …; «Por el criterio del cociente, puede concluir que la serie converge para todo x.»

Advertencia (p. 666): «… en el ejemplo 1 no se puede concluir que la serie de potencias converge a sen x para todo x. Se puede simplemente concluir que la serie de potencias converge a alguna función, pero no se tiene seguridad de cuál es la función.»

Teorema 9.23, convergencia de la serie de Taylor (p. 666): «Si lím_{n→∞} R_n(x) = 0 para todo x en el intervalo I, entonces la serie de Taylor de f converge y es igual a f(x).»

Ejemplo 3 (p. 668): serie de Maclaurin de sen(x²) por sustitución en la de sen x: x² − x⁶/3! + x¹⁰/5! − …

Directrices (p. 668): 1. derivar f varias veces y evaluar en c; 2. formar los coeficientes f^{(n)}(c)/n! y determinar el intervalo de convergencia; 3. dentro de ese intervalo, determinar si la serie converge a f(x). El libro recomienda usar la lista básica de series elementales y operar con ella (pp. 668-671).

---

## 4. EJERCICIOS DEL LIBRO E (pp. 100-107)

Mapa: E 3.15-3.17 = U §3.2.2 (sucesiones y series de funciones, FUERA DE EXAMEN). E 3.18 = derivación de series de potencias (U Prop. 3.3, Teor. 3.1; examen, ver alcance). E 3.19-3.20 = U §3.2.3 (series de Taylor, funciones analíticas; examen). E 3.14 (pp. 99-100, Lagrange de ln(1+x)) pertenece a §3.1 y no se repite aquí.

### Ejercicio 3.15 (E p. 100) — FUERA DE EXAMEN
Enunciado: «Sea {f_n} la sucesión de funciones dada por f_n(x) = √(x² + 1/n). Calcula su límite. ¿Son derivables las funciones f_n(x)?, ¿y su límite? Compruebe que la sucesión converge uniformemente.»
Método (solución E pp. 101-102): límite puntual f(x) = |x|; cada f_n es derivable, pero el límite |x| no lo es en x = 0; convergencia uniforme: el supremo de √(x² + 1/n) − |x| se alcanza en x = 0 y vale 1/√n → 0.

### Ejercicio 3.16 (E pp. 102-104) — FUERA DE EXAMEN
Enunciado: «Sea {f_n} la sucesión de funciones definida por f_n(x) = arctg(x/n), n ∈ N. Estudia: 1) La convergencia puntual y uniforme de {f_n} en R. 2) La convergencia puntual y uniforme de {f_n′}. 3) La convergencia uniforme de {f_n} en [0, 1].»
Método (solución E pp. 102-104): 1) límite puntual 0; no uniforme en R porque el supremo de arctg(x/n) es π/2 para todo n; 2) f_n′(x) = n/(n² + x²) → 0 uniformemente en R (supremo 1/n); 3) en [0,1] el supremo es arctg(1/n) → 0: converge uniformemente. El libro comenta (p. 104) que no contradice la proposición de U porque R no es un intervalo acotado.

### Ejercicio 3.17 (E p. 104) — FUERA DE EXAMEN
Enunciado: «Sea f_n(x) la serie de funciones con f_n(x) = e^{−n} x^n. En los ejercicios del Tema 1 vimos que es una serie absoluta y uniformemente convergente en cualquier intervalo de la forma [−k, k] para 0 < k < e. Construye la serie Σ f_n′(x) y calcula su radio de convergencia.»
Método (solución E p. 104): f_n′(x) = n e^{−n} x^{n−1}; reindexar a Σ_{n=0}^∞ (n+1) e^{−(n+1)} x^n; radio e por el criterio del cociente (lím (n+1)/(e·n) = 1/e). El libro señala que podía usarse el Teorema 3.1 (derivación de series de potencias).
Nota de transcripción: el texto extraído dice «e−nxn»; se lee e^{−n} x^n (coherente con la solución y con el índice de X p. 38, clasificado como fuera de examen).

### Ejercicio 3.18 (E pp. 104-105) — EXAMEN (derivación de series de potencias)
Enunciado: «Sabemos que Σ_{n=0}^∞ x^n = 1/(1−x) para x ∈ (−1, 1) por ser una serie geométrica. A partir de esta expresión, se pide expresar (1 − x)^{−2} como una serie de potencias para x ∈ (−1, 1). Pista: calcula la derivada de la función f(x) = 1/(1−x).»
Método (solución E pp. 104-105): la serie geométrica converge uniformemente en (−1,1) a f(x) = 1/(1−x); se deriva término a término: f′(x) = (1−x)^{−2} = Σ_{n=1}^∞ n x^{n−1} = 1 + 2x + 3x² + …; reindexado: Σ_{n=0}^∞ (n+1) x^n (el término constante 1 se deriva a 0).
Comprobación (sympy): (1−x)^{−2} = 1 + 2x + 3x² + 4x³ + O(x⁴). Verificado.

### Ejercicio 3.19 (E pp. 105-106) — EXAMEN (serie de Taylor de e^x)
Enunciado: «Sea f la función dada por f(x) = e^x. Calcula su serie de Taylor centrada en 0 y deriva término a término la serie resultante. Comprueba que la serie formada por estas derivadas coincide con la serie de Taylor.»
Método (solución E pp. 105-106): f^{(n)}(0) = 1 para todo n, luego e^x = Σ x^n/n! con radio infinito; derivando término a término se obtiene Σ_{n≥1} x^{n−1}/(n−1)! = Σ_{n≥0} x^n/n!, la misma serie.

### Ejercicio 3.20 (E pp. 106-107) — EXAMEN (serie de Taylor de (1+x)^{−k})
Enunciado: «Sea f la función definida, para x > −1, por f(x) = (1 + x)^{−k}, para k ∈ N, k > 0. Obtén su desarrollo en serie de Taylor centrado en x_0 = 0 y su radio de convergencia.» Nota del enunciado: f^{(n)}(x) = (−1)^n (k(k+1)…(k+n−1))/(1+x)^{k+n}.
Método (solución E pp. 106-107): f^{(n)}(0) = (−1)^n k(k+1)…(k+n−1); coeficiente f^{(n)}(0)/n! = (−1)^n C(k+n−1, n); serie 1 − kx + k(k+1)/2! x² − …; radio 1 por el criterio del cociente: lím |a_{n+1}/a_n| = lím (k+n)/(n+1) = 1.
Comprobación (sympy, k = 3): 1 − 3x + 6x² − 10x³ + O(x⁴), que coincide con (−1)^n C(k+n−1, n). Verificado.

---

## 5. Preguntas del examen X (series de potencias y Taylor)

Localizadas con `indice_examenes_*.md` (filas con «3.2», «series de potencias» o «series Taylor») y leídas como imagen en el PDF. Páginas = PDF.

### X p. 46 — Sept 2014, Modelo A (Grado en Ing. Mecánica), P1 corta (solución en la misma página)
Enunciado: «Calcúlese el radio de convergencia de la serie de potencias Σ_{n=0}^∞ x^n/2^n.»
Solución del libro: criterio del cociente, a_n = 1/2^n, lím a_n/a_{n−1} = 1/2, luego R = 2. Verificado (sympy).
Receta: R = 1/lím |a_{n+1}/a_n| (o 1/lím |a_n|^{1/n}).

### X p. 96 — Sept 2018, Modelo A (Mecánica), P1 corta
Enunciado: «Determine el radio de convergencia de la serie de potencias Σ x^n/3^n.»
Solución (misma página): cociente → 1/3, R = 3 (también con la raíz). Verificado.

### X p. 99 — I. Electrónica Industrial y Automática (sin fecha en el encabezado), P2 corta
Enunciado: «Calcule el centro, radio de convergencia e intervalo de convergencia de la serie de potencias Σ_{n=1}^∞ (2x − 1)^n/n!.»
Solución (misma página): centro 1/2; reescribe la serie como Σ 2^n/n! (x − 1/2)^n; radio infinito; intervalo de convergencia toda la recta real (criterio del cociente). Verificado.

### X p. 105 — I. Electrónica Industrial y Automática (sin fecha), Ej. 6 (3 puntos)
Enunciado: «Dada la serie de funciones Σ_{n=0}^∞ ln(n+1)(x+1)^n: discuta si es una serie de potencias y, en caso afirmativo, indique su centro; estudie si existe un intervalo en el que la serie es convergente; estudie si para x = −2 y x = 0 las series numéricas asociadas son convergentes.»
Solución (misma página): centro −1; criterio del cociente lleva a lím ln(n+1)/ln n = 1 (L’Hôpital sobre lím ln(x+1)/ln x), radio 1 e intervalo de convergencia (−2, 0); en x = −2 y x = 0 el término general no tiende a 0 (ln(n+1) → ∞ en x = 0; ln(n+1)(−1)^n en x = −2), luego divergen. Verificado (sympy: lím ln(n+2)/ln(n+1) = 1; ln(n+1) → ∞).
Receta: serie de potencias en (x − c): centro c, radio por el cociente; en los extremos, el término general debe tender a 0 para que pueda haber convergencia.

### X p. 112 (solución en p. 113) — Examen 2 elaborado con exámenes de asignaturas similares (sin fecha), Ej. 4 (test)
Enunciado: «Señale la opción correcta para la serie Σ_{n=1}^∞ n x^{n−1}: A) converge para todo x; B) no converge para ningún x; C) converge en el intervalo (−1, 1); D) ninguna de las anteriores.»
Solución (p. 113): es la derivada de Σ x^n, que tiene radio 1; por la proposición de derivación de series de potencias tiene el mismo radio; respuesta C. Verificado (en x = ±1 el término general no tiende a 0).

### X p. 126 — I. Electrónica Industrial y Automática (examen A, sin fecha), P1 corta
Enunciado: «Calcule el radio de convergencia de la serie Σ_{n=1}^∞ (1 + 1/n)^{2n²} x^n.»
Solución (misma página): raíz n-ésima: lím (1 + 1/n)^{2n} = e², luego R = 1/e². Verificado con sympy.

### X p. 142 — Sept 2018, I. Electrónica Industrial y Automática, P3 corta
Enunciado: «Serie de Taylor de f(x) = e^{πx} centrada en x = 0.»
Solución (misma página): f^{(n)}(x) = π^n e^{πx}; serie Σ π^n x^n/n!. El libro no escribe el radio (es infinito, serie de e^{πx}); añadirlo como comentario propio en el resumen. Verificado.

### X pp. 145-146 — Feb 2018, 1ª semana, I. Electrónica Industrial y Automática, Ej. 5 (3 puntos)
Enunciado: «f(x) = cos x. (a) Calcule de manera razonada la serie de Taylor de f centrada en x = 1/2. (b) Usando el resto de Lagrange de orden n, calcule cos(1/4) con un error en valor absoluto menor que 0,002.»
Solución (pp. 145-146): (a) derivadas con patrón de periodo 4; serie cos(1/2) − sen(1/2)(x − 1/2) − cos(1/2)(x − 1/2)²/2! + sen(1/2)(x − 1/2)³/3! + … (correcta). (b) toma x_0 = 0 y p_2(x) = 1 − x²/2; escribe |R_2(1/4)| ≤ (1/6)(1/4)³ ≈ 0,002604 y concluye que «es suficiente»; p_2(1/4) = 31/32 = 0,96875; comprobación cos(1/4) ≈ 0,968912.
**Errata a avisar**: con n = 2 la cota de Lagrange es 0,0026 y NO es menor que 0,002, así que la conclusión del libro no queda justificada por esa cota (el error real, 0,000162, sí es menor que 0,002, pero la cota usada no lo garantiza). Con n = 3 la cota es (1/4!)(1/4)^4 = 0,000163 < 0,002 y p_3(1/4) = 0,968913. Verificado con sympy: cos(1/4) = 0,9689124; error real de p_2 = 0,000162; cota n = 2 = 0,002604; cota n = 3 = 0,000163.

Otros ejercicios X sobre Taylor (§3.1, no 3.2): pp. 46 (P3), 126 (P3), 129, 132, 135, 140, 147. Los trata el dossier 3.1.

---

## Faltas o dudas

1. **Alcance de la derivación de series de potencias** (U Prop. 3.3 y Teor. 3.1, p. 116): tratado como examen por E 3.18 y X p. 112. Confirmar con el docente.
2. **§3.2.2 de U (pp. 113-115)** y ejemplo 3.11: fuera de examen según CLAUDE.md. Se han leído solo en el texto extraído, no como imagen; los enunciados están reconstruidos. Si se citan literalmente, revisar en el PDF.
3. **E 3.17**: el texto extraído dice «e−nxn». Se interpreta como e^{−n} x^n (coherente con la solución). Confirmar en la imagen de `Libro ejercicios_Calculo_curso2425.pdf`, p. 104.
4. **X pp. 145-146 (cos x, Lagrange n = 2)**: erratum de la solución (cota 0,0026 > 0,002). Avisar en el resumen; no reproducir la conclusión sin corregirla.
5. **X p. 142**: la solución no indica el radio de convergencia (es infinito). Añadirlo como comentario propio.
6. **Encabezados X**: pp. 99, 105 y 126 no muestran año ni convocatoria (I. Electrónica Industrial y Automática); el índice tampoco lo da. p. 142 es Sept 2018; pp. 145-146, Feb 2018 1ª semana. Las fechas de este dossier son las del encabezado visto en la imagen.
7. **U p. 117**: la definición de serie de Taylor y la de función analítica no llevan número en el texto; citar como «U §3.2.3 p. 117».
8. **S**: la página es la de la cabecera de cada página (regla de CLAUDE.md). Teorema 5 y Ejemplo 1 en p. 754; Teoremas 8 y 9 y forma de Lagrange en p. 756; Ejemplo 2 en p. 757; Teorema 17 en p. 761; Tabla 1 en p. 762.
9. **L**: impresa = PDF − 17 (verificado en cabeceras: PDF 659 = p. 642; PDF 681 = p. 664; PDF 683 = p. 666; PDF 685 = p. 668).
10. **E 3.19 y 3.20**: enunciados en pp. 105 y 106; soluciones en pp. 106 y 107 respectivamente (verificado por cabecera de página).
