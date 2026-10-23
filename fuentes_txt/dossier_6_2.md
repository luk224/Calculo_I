# Dossier Tema 6.2: Teoremas fundamentales

Generado el 2026-10-23 a partir de `fuentes_txt/ingenieros.txt` (U), `ejercicios.txt` (E), `stewart.txt` (S), `larson.txt` (L) e `indice_examenes_1..4.md` (X), con comprobación en `examenes.txt` y render de las pp. 107, 109, 110, 112, 115, 119, 144 del PDF de exámenes, de la p. 220 de E y de las pp. 243–244 de U (PDF 241–242). Páginas: U impresa = PDF + 2 (comprobado con cabeceras); E impresa = PDF; L impresa = PDF − 17 (comprobado: PDF 294 = p. 277, PDF 295 = p. 278, PDF 297 = p. 280, PDF 301 = p. 284, PDF 303 = p. 286); S: número de la cabecera/pie del texto extraído (el PDF de S no está alineado con `stewart.txt`: la página PDF 818 es el Apéndice A1; por eso no se usa offset).

## 0. Rangos de páginas

| Apartado | Impresas (U) | PDF (U) | Contenido |
|---|---|---|---|
| U §6.2.1 Motivación | **p. 242** | 240 | Newton y Leibniz; orientaciones; objetivos |
| U §6.2.2 Introducción y eq. (6.1) | **p. 242** | 240 | Pregunta de si toda integrable tiene primitiva; F(x) = ∫₀ˣ e^{−t²} dt |
| U Ej. 6.5 (erf, Li) | **p. 243** | 241 | Función error e integral logarítmica |
| U Teorema 6.1 (TFC 1ª parte) y demostración geométrica | **p. 243** (enunciado); **p. 243–244** (demostración) | 241–242 | F′(x) = f(x) |
| U Ej. 6.6 y Ej. 6.7 (derivada con límite superior e inferior) | **p. 244** | 242 | Derivadas de integrales con límites variables |
| U Teorema 6.2 (TFC 2ª parte, regla de Barrow) y demostración | **p. 244** (enunciado); **p. 244–245** (demostración) | 242–243 | ∫ₐᵇ f = F(b) − F(a) |
| U margen p. 244 | **p. 244** | 242 | Teorema del valor medio del cálculo integral (enunciado en margen); notación F(x)\|ₐᵇ |
| U Ej. 6.8 y Interpretación intuitiva (eq. 6.2) | **p. 245** | 243 | ∫₀¹ eˣ dx = e − 1; velocidad y espacio recorrido |
| Fuera de 6.2 | **p. 246** → §6.3 | 244 | Motivación de §6.3; **Propiedades de la integral indefinida (linealidad) empiezan en p. 247** (§6.3.2) |

Nota: el enunciado de la fórmula general d/dx ∫_{a(x)}^{b(x)} f(t) dt (dos límites variables) **no aparece en U**. Aparece como ejercicio E 6.15 (pp. 221).

## 1. U (libro oficial)

### U §6.2.1 Motivación (p. 242)
> «Hemos estudiado integrales definidas que surgen a partir de áreas e integrales indefinidas, vistas como el proceso inverso de la derivación. A continuación estudiamos los teoremas fundamentales, que relacionan la integración y la derivación. Estos resultados fueron establecidos y demostrados en el siglo XVII por Newton y Leibniz de forma independiente.»

Objetivo (p. 242): «Detectar la amplitud, la profundidad y la belleza de la integración y su conexión con la derivación, como instrumento imprescindible para formular y resolver muchos problemas de ingeniería.»

### U §6.2.2 Introducción y función F definida por una integral (p. 242)
> «Podemos derivar la mayoría de las funciones que nos hemos encontrado aplicado unas reglas sencillas. Pero, ¿tienen primitiva todas las funciones integrables?» (p. 242)

- Idea (p. 242): f(t) = e^{−t²} es integrable en [0, x] para cualquier x, pero su primitiva no se puede expresar con funciones elementales. Se define la expresión (6.1): F(x) = ∫₀ˣ e^{−t²} dt, «una función porque a cada valor de x le asigna un valor F(x)».
- p. 243: «Como e^{−t²} es continua y no negativa, la función F(x) representa el área de la región limitada por la gráfica de f y el eje x entre 0 y x.»

### U Ej. 6.5 (p. 243): funciones definidas por integrales
- Función error: erf(x) = (2/√π) ∫₀ˣ e^{−t²} dt (p. 243; el factor 2/√π se lee en el render).
- Integral logarítmica: Li(x) = ∫₂ˣ dt / ln t, «cuyo valor es el número aproximado de números primos menores que x» (p. 243).

### U Teorema 6.1 Primer teorema fundamental del Cálculo (p. 243)
> «Teorema 6.1 Primer teorema fundamental del Cálculo. Si f : [a, b] → R es una función continua, entonces la función F(x) = ∫ₐˣ f(t) dt es derivable en [a, b] y se cumple F′(x) = f(x) ∀x ∈ (a, b).»

Demostración geométrica (pp. 243–244): «Sabemos que F(x) es el área delimitada por la gráfica de f y el eje x, entre a y x… ∆F ≈ ∆x · f(x)… Pero el límite es justo F′(x), por definición de derivada. Entonces, F′(x) = f(x).» (p. 244)

Comentario del libro (p. 244): «Se llama teorema fundamental porque relaciona integración y derivación, estableciendo que la derivación es inversa de la integración. Además, nos permite asegurar que cualquier función continua en un intervalo tiene primitiva.»

### U Ej. 6.6 (p. 244): derivada con límite superior variable
> «EJEMPLO 6.6. Calculemos la derivada de F(x) = ∫₀ˣ (t² sen t + 2t) dt.» Solución del libro: «F′(x) = x² sen x + 2x.» (p. 244; integrando verificado en el render de p. 244 del PDF de U.)
- Regla del libro (p. 244): «se elimina el signo integral y se sustituye x por t en el integrando».

### U Ej. 6.7 (p. 244): derivada con límite inferior variable
> «EJEMPLO 6.7. Si G(x) = ∫ₓ⁰ (t⁴ + 2) e^{−t²} dt, su derivada es: G′(x) = (∫ₓ⁰ …)′ = (−∫₀ˣ …)′ = −(x⁴ + 2) e^{−x²}.» (p. 244; verificado en render: G(x) = ∫ₓ⁰, no ∫₀ˣ)
- Idea (p. 244): «si la variable está en el límite inferior de integración… haciendo una sencilla operación podemos aplicar el teorema fundamental» (intercambiar los límites cambia el signo).

### U Teorema 6.2 Segundo teorema fundamental del Cálculo (p. 244)
> «Teorema 6.2 Segundo teorema fundamental del Cálculo. Si f(x) es una función continua en [a, b] y F(x) es cualquier primitiva de f(x), entonces ∫ₐᵇ f(x) dx = F(x)|ₐᵇ = F(b) − F(a).»

Notación en margen (p. 244): «Con F(x)|ₐᵇ se indica F(b) − F(a).»
También (p. 244, texto): «También se conoce como Regla de Barrow.»

Demostración (pp. 244–245): «Por hipótesis, se cumple que F′(x) = f(x) en [a, b]. Definimos G(x) = ∫ₐˣ f(x) dx. Entonces G′(x) = f(x) por el primer teorema fundamental. Por lo tanto (F − G)′ = 0 … F(x) = G(x) + k … k = F(a) … ∫ₐᵇ f(x) dx = G(b) = F(b) − F(a).» (p. 245)

Observación del libro (p. 245): «El Teorema 6.2 es válido para cualquier primitiva de f.» Y: «Lo que no nos dice es cómo hallar la primitiva ni si ésta se puede expresar a partir de funciones elementales.»

### U Margen p. 244: teorema del valor medio del cálculo integral
> «Teorema del valor medio del cálculo integral. Este importante resultado, que se demuestra en el libro de ejercicios, garantiza, para cualquier función continua en [a, b], la existencia de un punto c ∈ [a, b] tal que ∫ₐᵇ f(x) dx = f(c)(b − a).»

(Enunciado en el margen, no en recuadro de teorema. Demostración en E 6.9, ver dossier 6.1 §3.)

### U Ej. 6.8 (p. 245): ∫₀¹ eˣ dx
> «Una primitiva de la función eˣ es F(x) = eˣ … Según el segundo teorema fundamental del cálculo, ∫₀¹ eˣ dx = F(1) − F(0) = e¹ − e⁰ = e − 1.» (p. 245)
- Comentario del libro: «Observe la sencillez del cálculo, frente al realizado en el Ejemplo 6.1.»

### U Interpretación intuitiva (p. 245, eq. 6.2)
> «La velocidad como derivada del espacio recorrido por un móvil nos da una interpretación intuitiva de la Regla de Barrow… ∫ₐᵇ v(t) dt = x(b) − x(a).» (6.2, p. 245)

## 2. S (Stewart) y L (Larson): apartados equivalentes

### S §5.3 Teorema fundamental del cálculo (pp. 387–395)
- **TFC1 (p. 388).** Resumen: la derivada de una integral respecto a su límite superior es el integrando evaluado en ese límite.
  Extracto (p. 388): «Teorema fundamental del cálculo, parte 1. Si f es continua sobre [a, b], entonces la función J definida por J(x) = ∫ₐˣ f(t) dt es continua sobre [a, b] y derivable sobre (a, b), y J′(x) = f(x).»
- **Demostración del TFC1 (pp. 388–389)**: con el área del rectángulo de altura f(x) y ancho h («por intuición, esperamos que…»). Útil para entender la figura del TFC1 (Figura 5, p. 388).
- **TFC2 (p. 391).** Resumen: si F es una antiderivada de f, la integral definida se evalúa con F(b) − F(a).
  Extracto (p. 391): «Teorema fundamental del cálculo, parte 2. Si f es continua sobre [a, b], entonces ∫ₐᵇ f(x) dx = F(b) − F(a), donde F es una antiderivada de f; es decir, una función tal que F′ = f.»
- **Ej. 2 y 3 (pp. 389–390)**: derivadas de integrales con límite superior que contiene una función (texto extraído sin número de página visible en esa zona; ver Faltas).
- **Ej. 4 y 5 (pp. 391–392)**: Ej. 4, derivada de una integral de sec t cuyo límite superior es x⁴ (regla de la cadena); Ej. 5, evaluación de una integral de eˣ. (Página no verificada con cabecera; ver Faltas.)
- **Ej. 6–8 (p. 392)**: Ej. 6, área bajo y = x² desde 0 hasta 1; Ej. 7, evaluación de una integral definida; Ej. 8, área bajo la curva coseno desde 0 hasta b, con 0 ≤ b ≤ π/2.
- **Ej. 9 (p. 393)**: «¿Cuál es el error en el cálculo siguiente?» con ∫₁³ 1/x² dx. Motivo: f(x) = 1/x² no es continua en [1, 3]; el TFC no se puede aplicar, y la integral no existe. Útil como advertencia.
- **Resumen de la sección (p. 393)**: «Teorema fundamental del cálculo. Suponga que f es continua sobre [a, b]. 1. Si F(x) = ∫ₐˣ f(t) dt, entonces F′(x) = f(x). 2. ∫ₐᵇ f(x) dx = F(b) − F(a), donde F es cualquier antiderivada de f.» Y: «la derivación y la integración son procesos inversos» (p. 393).

### S §5.4 Integrales indefinidas y el teorema del cambio neto (pp. 397–406)
- Notación (p. 397): «∫ f(x) dx = F(x) significa que F′(x) = f(x)» (integral indefinida = antiderivada; «F(x) + C» se usa como familia).
- Extracto (p. 397): «Por tradición se usa la notación ∫ f(x) dx para una antiderivada de f y se llama integral indefinida.»
- **Teorema del cambio neto (p. 401).** Extracto: «La integral de una razón de cambio es el cambio neto: ∫ₐᵇ F′(x) dx = F(b) − F(a).» Ejemplos de volumen, concentración y desplazamiento (p. 401).

### L §4.4 Teorema fundamental del cálculo (pp. 277–287)
- **Teorema 4.9 (p. 278).** Enunciado literal: «Si una función f es continua en el intervalo cerrado [a, b] y F es una antiderivada de f en el intervalo [a, b], entonces ∫ₐᵇ f(x) dx = F(b) − F(a).» Demostración con la partición y el teorema del valor medio (p. 278).
- **Teorema 4.10 (p. 280): teorema del valor medio para integrales.** Enunciado: «Si f es continua en el intervalo cerrado [a, b], entonces existe un número c en [a, b] tal que ∫ₐᵇ f(x) dx = f(c)(b − a).» (Figura 4.30–4.31 del libro.)
- **Ej. 3 (p. 279)**: «Usar el teorema fundamental para encontrar integrales definidas» (cálculo directo con F(b) − F(a)).
- **Ej. 4 (p. 281)**: «Determinar el valor medio de una función» (aplicación del TVM integral: f_prom = (1/(b−a)) ∫ₐᵇ f).
- **Ej. 6 (p. 283)**: «La integral definida como función» (derivada respecto al límite superior).
- **Teorema 4.11 (p. 284): segundo teorema fundamental del cálculo.** Enunciado literal: «Si f es continua en un intervalo abierto I que contiene a a, entonces, para todo x en el intervalo, d/dx ∫ₐˣ f(t) dt = f(x).»
- **Ej. 7 (p. 285)**: «Calcule d/dx ∫₀ˣ (t² + 1) dt.» Solución: x² + 1 (aplicación directa del Teorema 4.11).
- **Ej. 8 (p. 285)**: «Usar el segundo teorema fundamental del cálculo» combinado con la regla de la cadena (límite superior que es una función de x; ejemplo con u = x³).
- **Teorema 4.12 (p. 286): teorema del cambio neto.** Enunciado: «La integral definida de la razón de cambio de una cantidad F′(x) proporciona el cambio total, o cambio neto, en esa cantidad en el intervalo [a, b]: ∫ₐᵇ F′(x) dx = F(b) − F(a).»
- **Ej. 9 (p. 286)**: flujo de sustancia química 180 + 3t, 0 ≤ t ≤ 20 (cambio neto de la cantidad).

Nota: L §4.3 (pp. 266–275, sumas de Riemann y propiedades de la integral) pertenece a 6.1 (ver dossier 6.1), salvo el Teorema 4.7 y 4.8 de propiedades, ya citados en el dossier 6.1.

## 3. E (libro de ejercicios): Ejercicios 6.11 a 6.16

Mapa U: 6.9 (TVM integral) se mantiene en el dossier 6.1 §3 (margen U p. 244 lo remite a este libro). 6.11 → Teorema 6.1 (TFC1) y Def. 6.2; 6.12–6.13 → derivada de F(x) = ∫₀ˣ (TFC1) con regla de la cadena; 6.14–6.15 → derivada con límites variables (TFC1 + regla de la cadena; U Ej. 6.7 y E 6.15 como generalización); 6.16 → Regla de Barrow (Teor. 6.2). Ejercicios 6.17 en adelante pertenecen a §6.3 (técnicas de integración: inmediatas, partes, fracciones simples, Hermite).

### Ejercicio 6.11 (E pp. 218–219) [§6.2, Teor. 6.1 y Def. 6.2]
- Enunciado (p. 218): «Sea F : R → R una primitiva de una función continua f : R → R y C ∈ R una constante. Señale la opción correcta: a) d/dx (F(x) + C) = f(x), ∀x ∈ R. b) d/dx (f(x) + C) = F(x), ∀x ∈ R. c) ∫ F(x) dx = f(x) + C, ∀x ∈ R. d) Ninguna de las anteriores.» (En la extracción falta el signo ∫ de c); no renderizado.)
- Solución (pp. 218–219): a) es correcta: G = F + C también es primitiva, G′ = F′ = f. b) falsa (f no tiene por qué ser derivable). c) falsa (contraejemplo F = x, f = 1).
- Método: primitiva = derivada igual a f; cada primitiva difiere en una constante.

### Ejercicio 6.12 (E pp. 219–220) [§6.2, TFC1 + regla de la cadena]
- Enunciado (p. 219): «Sea H = F ∘ G con F(x) = ∫₀ˣ sen(ln t) dt y G(x) = eˣ. Señale la opción correcta: a) H es creciente en R. b) H tiene un punto de inflexión en x = 3π/4. c) H es cóncava en R. d) H alcanza un mínimo en π.»
- Solución (pp. 219–220): H′(x) = F′(G(x)) G′(x) = sen(ln eˣ) eˣ = eˣ sen x. a) falsa (H′ cambia de signo). d) falsa (H″(π) = −e^π < 0). c) falsa (H″ no tiene signo constante). H″ = eˣ(sen x + cos x); H″(3π/4) = 0 y H‴(3π/4) = 2eˣ cos x < 0 → inflexión. Respuesta: b).
- Método: regla de la cadena + TFC1; para inflexión, H″ = 0 y H‴ ≠ 0.
- Verificado con sympy: H′ = eˣ sen x.

### Ejercicio 6.13 (E p. 220) [§6.2, TFC1]
- Enunciado (p. 220, verificado en render): «Dada la función F(x) = ∫₀ˣ t sen t dt definida en I = [0, ∞), señale la opción correcta. a) F alcanza un máximo en x = 7π. b) F es creciente en I. c) F alcanza un mínimo en x = 7π. d) F es decreciente en I.»
- Solución (p. 220): F′(x) = x sen x (TFC1). El signo de F′ cambia: ni creciente ni decreciente (b, d falsas). Puntos críticos x = kπ. F″(x) = sen x + x cos x; F″(7π) = −7π < 0 → máximo. Respuesta: a).
- Método: F′ con TFC1; criterio de la segunda derivada en los puntos críticos.
- Verificado con sympy: F″(7π) = −7π.

### Ejercicio 6.14 (E p. 220–221) [§6.2, límite inferior variable]
- Enunciado (p. 220, verificado en render): «Calcula el valor de d/dx ( ∫ₓ¹ t² dt ).»
- Solución (p. 220–221): el límite variable es el inferior. Intercambiar límites cambia el signo: d/dx ∫ₓ¹ t² dt = −d/dx ∫₁ˣ t² dt = −x². Resultado: **−x²**.
- Método: intercambiar límites (signo menos) y TFC1.
- Verificado con sympy: −x².

### Ejercicio 6.15 (E p. 221) [§6.2, fórmula de Leibniz con límites variables]
- Enunciado (p. 221): «Sea f : R → R una función integrable en R. Sean a : R → R y b : R → R funciones derivables en R. Demuestra que d/dx ∫_{a(x)}^{b(x)} f(t) dt = f(b(x)) b′(x) − f(a(x)) a′(x). Aplica el resultado para calcular el valor de d/dx ∫_{x²}^{eˣ} cos t dt.»
- Solución (p. 221): se separa la integral en ∫_{a(x)}^{c} + ∫_{c}^{b(x)}; el primer término se deriva con la regla de la cadena y TFC1 (− f(a(x)) a′(x)), el segundo con TFC1 (f(b(x)) b′(x)). Aplicación: d/dx ∫_{x²}^{eˣ} cos t dt = cos(eˣ) eˣ − 2x cos(x²).
- Método: fórmula general = TFC1 + regla de la cadena; partir la integral en un punto fijo c.
- Verificado con sympy: cos(eˣ)eˣ − 2x cos(x²).
- Nota: el enunciado dice «integrable», pero la demostración usa la continuidad de f (condición de TFC1). Ver Faltas.

### Ejercicio 6.16 (E pp. 222–223) [§6.2, Regla de Barrow y validez]
- Enunciado (p. 222): «Se sabe que ∫ 1/(x − 1) dx = ln|x − 1| + C en R \ {1}. ¿Qué opción es verdadera? a) No hay relación entre la integral definida y la indefinida. b) Utilizando Barrow resulta ∫₀² 1/(x − 1) dx = 0. c) Utilizando Barrow resulta ∫₂³ 1/(x − 1) dx = ln 2.»
- Solución (pp. 222–223): a) falsa (Barrow relaciona ambas). b) el integrando no es continuo en [0, 2] (x = 1 ∈ [0, 2]); el cálculo naive da 0, pero la regla de Barrow no es aplicable; la integral no tiene sentido. c) es correcta: 1/(x − 1) es continua en [2, 3] y ln|3 − 1| − ln|2 − 1| = ln 2. Respuesta: c).
- Método: comprobar que f es continua en [a, b] antes de aplicar Barrow.
- Verificado con sympy: ∫₂³ 1/(x − 1) dx = ln 2.

## 4. X (exámenes resueltos): preguntas de 6.2

Búsqueda por palabras clave en `indice_examenes_1..4.md` (fundamental, F(x)=∫, derivada de integral, Barrow, valor exacto, área, V/F sobre integrales). Solo dos grupos: (a) preguntas de teoremas fundamentales; (b) integrales evaluadas con Regla de Barrow (que usan 6.2, pero cuya técnica de primitiva es 6.3).

### (a) Preguntas sobre TFC (teoremas fundamentales)

| Convocatoria | Pág. PDF (enunc. → sol.) | Pregunta | Tipo | Verificación | Estado |
|---|---|---|---|---|---|
| Electrónica 4 (sin fecha en el índice) | **107** (enunc. y sol. en la misma página) | P4 corta: V/F «Si f es derivable y decreciente en (0,∞), entonces F(x) = ∫₀ˣ f(s) ds es decreciente en (0,∞)». Solución: falsa; F′ = f, y decreciente no implica f negativa; contraejemplo f = 1/x | Monotonía de F = ∫f vía TFC1 | Render de p. 107 (leído) | Conclusión correcta. **Contraejemplo inválido** (∫₀ˣ ds/s diverge); ver Faltas |
| Examen 1 («elaborado con exámenes de asignaturas similares», sin fecha) | **109** (enunc.) → **110** (sol.) | Ej. 4: F(x) = ∫₀ˣ t sen t dt definida en [0, ∞). A) F es creciente; B) F tiene un máximo en x = 7π; C) F es decreciente; D) ninguna | TFC1 + criterio de la 2ª derivada | Render pp. 109–110; sympy: F′ = x sen x, F″(7π) = −7π < 0 | Respuesta **B** (coincide con E 6.13) |
| Feb 2018, 1ª semana (I. Electrónica Industrial y Automática) | **144** (enunc. y sol. en la misma página) | P3 corta: V/F «Si f es continua y creciente en (0,∞), entonces F(x) = ∫₀ˣ f(t) dt es creciente en (0,∞)». Solución: falsa, con f(x) = −1/x² | Monotonía de F = ∫f vía TFC1 | Render de p. 144 (leído) | Conclusión correcta. **Contraejemplo inválido** (f no es integrable en 0); ver Faltas |

### (b) Integrales evaluadas con Regla de Barrow (6.2 + técnica de 6.3)

| Convocatoria | Pág. PDF | Pregunta | Estado |
|---|---|---|---|
| Examen 2 (elaborado con exámenes similares, sin fecha) | **112** (enunc.); sol. en **113** (no renderizada) | Ej. 3: área entre gráfica de tg x, x = 0, x = π/4 y eje x. A) ln2/2; B) ln4/4; C) π²/4; D) ninguna | Enunciado verificado en render. Resultado sympy: ∫₀^{π/4} tg x dx = ln(2)/2 → **A** |
| Examen 3 (elaborado con exámenes similares, sin fecha) | **115** (enunc.); sol. en **116** (no renderizada) | Ej. 3: ∫₀^{π/2} cos x / √(sen x) dx. A) 0; B) π/4; C) 2; D) ninguna | Enunciado verificado en render. Sympy: 2 → **C** |
| Examen 4 (elaborado con exámenes similares, sin fecha) | **119** (enunc. y solución de la pregunta indicada con letra A, sin desarrollo) | Ej. 4: ∫₀^π cos x · ∛(sen x) dx. A) 0; B) 1; C) π; D) ninguna | Enunciado verificado en render. Sympy: 0 → **A** |

Otras integrales del índice (Feb 2010 PC3 p. 1; Sept 2012 reserva PC3 p. 29; Feb 2017 Mod. A Ej. 5 pp. 78–79; Feb 2017 2ª sem Ej. 5 p. 136; Sept 2018 Mod. B Ej. 5 p. 94; Electrónica 1 Ej. 5 p. 100) quedan para 6.3 (técnicas), 6.4 (numérica) o 6.5 (impropias) y no se listan aquí.

## 5. Faltas o dudas

1. **Contraejemplos inválidos en X (p. 107 y p. 144)**: en ambas soluciones se toma F(x) = ∫₀ˣ f con f = 1/x (p. 107) y f = −1/x² (p. 144). Esas f no son integrables en [0, x] (sympy: ∫₀ˣ ds/s diverge), así que la F no existe. La conclusión (falsa) es correcta, pero el contraejemplo no vale. Contraejemplos válidos comprobados con sympy (usando el límite inferior 1): p. 107: F(x) = ∫₁ˣ dt/t = ln x, creciente aunque f = 1/x sea decreciente; p. 144: F(x) = ∫₁ˣ (−1/t²) dt = 1/x − 1, decreciente aunque f = −1/x² sea creciente en (0, ∞). Ya señalado en el dossier 6.1 §5 (puntos 5 y 6); confirmado aquí.
2. **X: Examen 1–4 (elaborados con exámenes de asignaturas similares, no examen oficial UNED)**: el índice no da año. Se citan por su encabezado y número de página. Examen 1 Ej. 4 (p. 109–110) tiene solución correcta (B).
3. **X, Examen 2 Ej. 3 (sol. p. 113), Examen 3 Ej. 3 (sol. p. 116), Examen 4 Ej. 4 (sol. p. 119)**: los enunciados están verificados en render; las soluciones de Examen 2 y 3 no se han renderizado. Los resultados se comprueban con sympy (ln2/2, 2 y 0) y coinciden con el índice.
4. **E 6.11 (p. 218)**: en la extracción falta el signo ∫ de la opción c) («F(x) dx = f(x) + C»). No se ha renderizado la página; la lectura es la habitual. Confirmar en el PDF si se cita textualmente.
5. **E 6.15 (p. 221)**: el enunciado dice «f integrable en R», pero la solución usa la continuidad de f (TFC1 requiere continuidad). Interpretar con f continua.
6. **E 6.14 (p. 220)** y **E 6.13 (p. 220)**: verificados en render (PDF 220). E 6.12 (p. 219) y E 6.16 (pp. 222–223): enunciado leído en `ejercicios.txt`; no renderizados.
7. **S, páginas de los ejemplos**: Ej. 2–3 de §5.3 (pp. 389–390) y Ej. 4–5 (pp. 391–392) aparecen en el texto extraído sin número de página visible en esa zona; se citan con el rango. Las cabeceras de pp. 388, 391, 392, 393, 397, 401 sí están verificadas en `stewart.txt`. La numeración de S no coincide con el PDF `Cálculo_de_una_variable_Trascendentes_JAMES_STEWART.pdf` (p. 818 = Apéndice A1): usar siempre las cabeceras del texto.
8. **S, Ej. 1 de §5.3 (p. 387) y Ej. 1 de §5.4 (p. 399)**: no transcritos (la extracción de la gráfica del Ej. 1 de §5.3 es ilegible).
9. **L, páginas**: verificadas con cabeceras (PDF 294–304 → pp. 277–287; PDF 295, 297, 301, 303, 309 → pp. 278, 280, 284, 286, 292). Los ejemplos 3, 4, 6, 7 y 9 se leen en el texto (PDF 296, 298, 300, 302, 303), no renderizados.
10. **U, Teorema del valor medio integral**: el enunciado está en el margen de p. 244 (verificado en render); el recuadro de teorema no existe en U.
11. **U, figura del Teorema 6.1**: en p. 243 hay una figura marginal (área F(x) y ΔF). No se ha recortado; candidata para `herramientas/extraer_figura.py` (U PDF 241).
12. **U, Propiedades de la integral indefinida (linealidad)**: empiezan en p. 247 (§6.3.2), fuera de este tema.
13. **Fórmula de Leibniz con ambos límites variables**: no está en U; aparece en E 6.15. En el HTML conviene citarla como «E 6.15» o como consecuencia del TFC1 (no como teorema de U).
14. **Sumas de Riemann vs TFC**: la demostración del TFC2 en U (p. 244–245) usa G(x) = ∫ₐˣ f; no la repito aquí.
