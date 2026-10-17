# Dossier 4.1 · El espacio ℝⁿ (U §4.1)

Numeración: U impresa = PDF + 2; E impresa = PDF; X = página PDF del `Examenes-resueltos-Calculo.pdf`; S = número de la cabecera de la página; L = PDF − 17 (larson.txt no contiene esta materia, ver §2).
Aviso: en U, los «Ejemplo 4.x» son del libro de teoría y los «Ejercicio 4.x» son de E; no confundirlos.

**Alcance real de §4.1:** pedía pp. 142-151, pero §4.1 ocupa **pp. 142-152** (Ejemplo 4.8 está en p. 152, y §4.2 empieza al pie de p. 152).

---

## 1. U (libro oficial): §4.1 El espacio ℝⁿ, pp. 142-152

### §4.1.1 Motivación · p. 142
- Introducción (extracto): «Hasta ahora hemos trabajado con funciones definidas sobre los números reales o un subconjunto suyo… la mayor parte depende de más de una variable.»
- Objetivos (p. 142): «Comprender que R² y R³ son espacios vectoriales…»; «…distancia, conjuntos abiertos y cerrados (por analogía a intervalos abiertos y cerrados), disco abierto…, interior, exterior y frontera (por analogía a extremos del intervalo).»

### §4.1.2 El espacio ℝⁿ. Primeras definiciones · pp. 142-147

**p. 142 · Definición de ℝⁿ (literal):** «Para un número natural n el conjunto Rⁿ es el producto cartesiano R×·ⁿ·×R. Sus elementos son n-uplas de la forma (x₁, …, xₙ), donde cada xᵢ ∈ R, para i = 1, …, n. Escribiremos x̄ = (x₁, …, xₙ), entendiendo que x̄ representa un elemento de Rⁿ, no un número.»

**p. 143 · Operaciones y base canónica (literal):** «Suma de elementos: x̄ + ȳ = (x₁+y₁, …, xₙ+yₙ). Producto por escalares: λx̄ = λ(x₁, …, xₙ) = (λx₁, …, λxₙ).» «Es conocido del Álgebra que Rⁿ con estas operaciones tiene estructura de espacio vectorial.»
«Elementos destacados… e₁ = (1,0,…,0), …, eₙ = (0,0,…,1). Forman la llamada base canónica… la dimensión de Rⁿ es n… (x₁,…,xₙ) son las coordenadas cartesianas de x.»
Notación: «Los vectores se denotan también u o −→u.»

**p. 143 · Definición 4.1 (literal):** «El producto escalar de dos elementos de Rⁿ, x̄ = (x₁,…,xₙ) e ȳ = (y₁,…,yₙ) es: x̄·ȳ = x₁y₁ + ⋯ + xₙyₙ = Σᵢ₌₁ⁿ xᵢyᵢ. Su resultado es un número y a partir de él definimos la norma de x̄ como: ‖x̄‖ = √(x̄·x̄) = √(x₁² + ⋯ + xₙ²).» «Intuitivamente la norma es la “longitud” del vector. Los vectores con norma uno se llaman vectores unitarios.»
**p. 143 · Distancia (literal):** «d(x̄, ȳ) = ‖ȳ − x̄‖ = √((y₁−x₁)² + ⋯ + (yₙ−xₙ)²).»
**p. 143 · Advertencia (literal):** «Nos limitamos a enunciar estas operaciones y sus propiedades porque son conocidas del Álgebra.» → U **no enuncia** ni la desigualdad triangular ni Cauchy-Schwarz (ver §5).

**p. 144 · Ejemplo 4.1 (R²):** x̄ = (1,2) = e₁ + 2e₂, ȳ = (3,1) = 3e₁ + e₂; z̄ = x̄ + ȳ = (4,3); v̄ = 2x̄ = (2,4). ‖ȳ‖ = √10; d((1,2),(3,1)) = √(2²+1²) = √5. Figura 4.1 (vectores en R²), p. 144.
**p. 144-145 · Ejemplo 4.2 (R³):** x̄ = (1,2,1), ‖x̄‖ = √6; d((0,1,3),(1,2,1)) = √6. Figura 4.2 (p. 145).

**p. 145 · Discos (literal):** «Definimos disco abierto de centro (a, b) y radio r como el conjunto {(x, y) ∈ R² : d((a,b),(x,y)) < r}.» Disco cerrado: igual con «≤».
**p. 145 · Punto interior (literal):** «Dado un conjunto C de R², decimos que (a, b) es un punto interior a C si existe un disco abierto de centro (a, b) que está incluido en C.»
Nota 1 (p. 145): «Vamos a utilizarlos con frecuencia. Serán necesarios, por ejemplo, al estudiar extremos condicionados o relativos y absolutos de funciones de varias variables.»

**p. 146 · Frontera, abierto, cerrado, acotado (literal):**
- «Un punto (a, b) se llama punto frontera de C si cualquier disco abierto de centro (a, b) tiene puntos de C y puntos que no están en C. El conjunto de todos los puntos frontera de C se llama frontera.»
- «Vamos a llamar conjunto abierto a C ⊂ R² si es vacío o todos sus puntos son interiores… Por tanto, R² es abierto.»
- «Se dice que C es un conjunto cerrado si contiene a su frontera… Si C no tiene puntos frontera (por ejemplo, si C = R²), entonces es cerrado.»
- «Un conjunto acotado es aquel que podemos incluir en un disco.»
- «Si trabajamos en R³ (o en Rⁿ en general), hablamos de bola abierta de centro (x₁,…,xₙ) y radio r, y las definiciones son semejantes.»
Figura 4.3 (puntos interior/frontera y conjuntos abierto/cerrado/acotado), p. 146.

**p. 147 · Ejemplo 4.3:** {(x,y) ∈ R² : (x−1)² + (y+2)² < 9} es el círculo de radio 3 centrado en (1,−2) **sin** la circunferencia; frontera = {(x−1)²+(y+2)² = 9}; puntos frontera de ejemplo (−2,−2), (1,1), (2, 2√2−2); (0,0) es interior → el conjunto es **abierto**. Figura 4.4, p. 147.

**p. 147 · Definición 4.2 (ángulo y ortogonalidad, literal):** «A partir del producto escalar se puede definir el ángulo α que forman dos vectores x̄ e ȳ: cos α = (x̄·ȳ)/(‖x̄‖‖ȳ‖).» «Dos vectores son ortogonales si y solo si su producto escalar es 0.» Nota de p. 147: «…el valor de arc cos x pertenece a [0, π], para cualquier x ∈ [−1, 1].» Figura 4.5 (ángulo), p. 147.

### §4.1.3 Coordenadas polares, cilíndricas y esféricas · pp. 148-152

**p. 148 · Polares (literal):** «…cualquier punto en coordenadas cartesianas (x, y) ∈ R²\{(0,0)} está definido de forma única dados un ángulo θ ∈ [0, 2π) y un radio ρ > 0.» «El número ρ es la distancia de (x,y) al origen… y θ es el ángulo formado por el vector (x,y) y el eje x orientado en sentido positivo.»
Ecuaciones: x = ρ cos θ, y = ρ sen θ ⟷ ρ = √(x²+y²) = ‖(x,y)‖, tg θ = y/x. «Si x = 0, entonces θ = π/2 o θ = 3π/2 según sea el signo de y positivo o negativo.» Figura 4.6, p. 148.

**p. 149 · Ejemplo 4.4:** (2, 2√3) → ρ = √(4+12) = 4; tg θ = √3 → θ = π/3 (primer cuadrante) → coordenadas polares (4, π/3).
**p. 149 · Ejemplo 4.5:** (2, 7π/4) → x = 2 cos(7π/4) = √2, y = 2 sen(7π/4) = −√2.

**p. 149 · Cilíndricas (literal):** «Las coordenadas cilíndricas (ρ, θ, z) son una generalización de las coordenadas polares a R³\{(0,0,0)}… la tercera coordenada queda igual… Estas coordenadas resultan muy convenientes para representar cilindros y superficies de revolución en general.» Ecuaciones: x = ρ cos θ, y = ρ sen θ, z = z; ρ = √(x²+y²), tg θ = y/x (mismas salvedades que en polares).
**p. 150 · Ejemplo 4.6:** (2, 2π/3, −1) en cilíndricas → x = 2 cos(2π/3) = −1, y = 2 sen(2π/3) = √3, z = −1. Figura 4.7 (cilíndricas), p. 150.

**p. 150 · Esféricas (literal):** «Las coordenadas esféricas de un punto son una terna (ρ, θ, ϕ), donde ρ > 0, θ ∈ [0, 2π) y ϕ ∈ [−π/2, π/2]. El número ρ es la distancia del punto a (0,0,0).» «ϕ es el ángulo que forma (x,y,z) con su proyección sobre el plano xy.»
Ecuaciones: x = ρ cos ϕ cos θ, y = ρ cos ϕ sen θ, z = ρ sen ϕ ⟷ ρ = √(x²+y²+z²), tg θ = y/x, sen ϕ = z/√(x²+y²+z²). «El ángulo θ se calcula con las indicaciones dadas en las coordenadas cilíndricas. Como ϕ ∈ [−π/2, π/2], está determinado de forma única por el signo de z.»

**p. 151 · Ejemplo 4.7:** (3, −4, −1). Cilíndricas: ρ = √(9+16) = 5, z = −1, θ ∈ [3π/2, 2π] con tg θ = −4/3 → θ = 5,3559 rad. Esféricas: ρ = √26, mismo θ, ϕ = arcsen(−1/√26) = −0,1974 rad. Figura 4.8 (esféricas), p. 151. «Cada punto de R³\{(0,0,0)} se puede expresar en cualquiera de estos sistemas.»

**p. 152 · Ejemplo 4.8:** (1, 5π/4, π/6) en esféricas → x = cos(π/6) cos(5π/4) = −√6/4; y = cos(π/6) sen(5π/4) = −√6/4; z = sen(π/6) = 1/2.
**p. 152 (pie):** inicio de §4.2 «Funciones de varias variables», 4.2.1 Motivación.

### Verificación de cálculos de U
Los ejemplos 4.1-4.8 de U (normas, distancias, polares, cilíndricas, esféricas) se han comprobado numéricamente: correctos.

---

## 2. S (Stewart) y L (Larson)

### S (stewart.txt)
- **Coordenadas polares: §10.3, pp. 654-656** (verificado con las cabeceras «654 CAPÍTULO 10», «SECCIÓN 10.3 COORDENADAS POLARES 655», «656 CAPÍTULO 10»; el índice del libro también da 10.3 en p. 654).
  - p. 654 (literal): «Por lo general usamos coordenadas cartesianas, que son las distancias dirigidas desde dos ejes perpendiculares. Aquí se describe un sistema coordenado… llamado sistema coordenado polar.» Define polo, eje polar, r y θ; r negativo: los puntos (r, θ) y (−r, θ+π) están en lados opuestos de O. Ejemplo 1 (graficar puntos), pp. 654-655.
  - p. 655: ecuaciones (1): x = r cos θ, y = r sen θ.
  - p. 656: ecuaciones (2): r² = x² + y², tan θ = y/x; Ejemplo 2 (2, 2π/3) → (−1, √3).
  - Aviso: el .txt está corrupto en símbolos (θ aparece como «.» o «¨», π como «p», «=» como «m», p. ej. «3)Y4» = 3π/4). Se ha interpretado.
- **Desigualdad del triángulo (solo reales):** S Apéndice A, **p. A8**, eq. 7: «Si a y b son cualesquier números reales, entonces |a + b| ≤ |a| + |b|.» Útil como analogía de la desigualdad triangular de ℝⁿ (no es la versión vectorial).
- **Distancia en el plano:** S Apéndice B, **p. A12**, «Fórmula de la distancia: La distancia entre P₁(x₁,y₁) y P₂(x₂,y₂) es |P₁P₂| = √((x₂−x₁)² + (y₂−y₁)²).» Ejemplo 2: distancia entre (1,−2) y (5,3) = √41.
- **No encontrado en S:** producto escalar, norma vectorial, Cauchy-Schwarz, bolas/abiertos/cerrados/frontera en ℝⁿ, coordenadas cilíndricas y esféricas. El .txt llega hasta el cap. 11 y los apéndices (no hay cabeceras «SECCIÓN 12» a «15»): los vectores (cap. 12) y las cilíndricas/esféricas (§15.7) no están en `stewart.txt`.

### L (larson.txt)
- **Sin equivalente.** `larson.txt` contiene solo el Tomo 1 (caps. 1-9, pp. 42 a ~776 impresas; cap. 9 Series en p. 584, verificado). Búsquedas de «vector», «polares», «producto escalar», «norma», «bola», «frontera», «Cauchy» en el cuerpo del texto: sin contenido de ℝⁿ.
- El índice del fichero cita «Coordenadas polares, 715», «Producto escalar, 766», «cilíndricas, 804», «esféricas, 807», pero esas páginas **no están** en `larson.txt`: no sirven para localizar el tema.

---

## 3. E (libro de ejercicios): Ejercicios 4.1-4.8 (pp. 136-141)

Corte: **Ejercicios 4.1 a 4.8** son de §4.1 (ℝⁿ, polares, cilíndricas, esféricas). **Ejercicio 4.9** (E p. 142: ley de gases ideales, P(T,V)) ya es §4.2 (funciones de varias variables) y no se incluye; tampoco 4.10 ni 4.11-4.14 (pp. 142-145).

Marcas de importancia del libro (texto extraído): «MÁXIMA» en 4.3, 4.4, 4.6, 4.7, 4.8; «!» en 4.5.

**Ejercicio 4.1 · E p. 136 · U §4.1.2 (Def. 4.1)**
> ¿Se pueden multiplicar escalarmente tres vectores? ¿Y un vector de R² con uno de R³?
- Solución del libro: no a ambas (el producto escalar opera dos vectores del mismo espacio y da un número).
- Método: comprobar qué operación da escalar y si los espacios coinciden.

**Ejercicio 4.2 · E p. 136 · U §4.1.2 (operaciones y Def. 4.1)** (enunciado verificado en imagen)
> El vector (ū · v̄) w̄, con ū, v̄, w̄ ∈ Rⁿ verifica:
> a) Es nulo o paralelo al vector w̄.
> b) Es nulo o paralelo al vector v̄.
> c) Es nulo o paralelo al vector ū.
> d) Esa expresión no da lugar a un vector.
- Solución del libro: (ū·v̄) es un escalar; λw̄ es paralelo a w̄ (o nulo). Respuesta **a)**.
- Método: identificar qué operación da escalar y cuál da vector («número × vector»).

**Ejercicio 4.3 · E p. 136 · U §4.1.2 (Def. 4.1 y ortogonalidad, p. 147)** (MÁXIMA)
> ¿Son ortogonales los vectores (0, 1, 2) y (−3, −4, 2)?
- Solución del libro: (0,1,2)·(−3,−4,2) = 0 − 4 + 4 = 0 → sí, ortogonales.
- Método: producto escalar = 0 ⇔ ortogonales.

**Ejercicio 4.4 · E pp. 136-137 · U §4.1.2 (norma y distancia, p. 143)** (MÁXIMA; enunciado verificado en imagen de p. 136)
> Dados ū = (−1, 1) y v̄ = (2, 3) se pide:
> 1. Calcular ū + v̄, ‖ū‖, ‖v̄‖ y ‖ū + v̄‖. ¿Se cumple ‖ū‖ + ‖v̄‖ = ‖ū + v̄‖? ¿Contradice esto que cumpla la desigualdad triangular?
> 2. Calcular 3ū y ‖3ū‖. ¿Se cumple ‖3ū‖ = 3‖ū‖?
> 3. Representar gráficamente ū, v̄, ū + v̄ y 3ū.
- Solución del libro: ū+v̄ = (1,4); ‖ū‖ = √2; ‖v̄‖ = √13; ‖ū+v̄‖ = √17 ≈ 4,12. √2+√13 ≈ 5,02 → **no** se cumple la igualdad (el signo ≠ se pierde en la extracción de texto). No contradice la desigualdad triangular ‖ū+v̄‖ ≤ ‖ū‖+‖v̄‖ (4,12 < 5,02). Parte 2: 3ū = (−3,3), ‖3ū‖ = √18 = 3√2 = 3‖ū‖ → sí se cumple. Parte 3: gráfica en p. 137.
- Método: sumar vectores componente a componente; norma = √(suma de cuadrados); comparar desigualdades; ‖λū‖ = |λ|‖ū‖.

**Ejercicio 4.5 · E pp. 138-139 · U §4.1.2 (disco, interior, frontera, abierto/cerrado, pp. 145-146)** (!)
> Dado el conjunto C = {(x, y) ∈ R² : x² + y² ≤ 4} se pide:
> 1. Representarlo gráficamente.
> 2. Determinar y representar su frontera.
> 3. Razonar si es un conjunto abierto o cerrado.
- Solución del libro: 1) disco de radio 2 con su circunferencia. 2) frontera = circunferencia x²+y²=4 (p. ej. (2,0) y (√2,√2) pertenecen; cualquier círculo centrado en un punto de la circunferencia tiene puntos de C y puntos fuera de C). 3) **cerrado**, porque contiene a su frontera.
- Método: frontera = puntos en los que todo disco centrado en ellos mezcla puntos de C y de no-C; cerrado ⇔ contiene a su frontera.

**Ejercicio 4.6 · E p. 140 · U §4.1.3 (polares, p. 148) y Def. 4.2 (ángulo, p. 147)** (MÁXIMA)
> Dados ū = (−1, 1) y v̄ = (2, 3), se pide:
> 1. Expresar ū en coordenadas polares.
> 2. Determinar el ángulo que forman ū y v̄.
- Solución del libro: 1) ρ = √2; tg θ = −1; como x<0, y>0 → θ = 3π/4 → (√2, 3π/4). 2) ū·v̄ = −2+3 = 1; cos α = 1/(√2·√13) = 1/√26 → α = arccos(1/√26) ≈ 1,3734 rad (comprobado).
- Método: polares con signos del cuadrante; ángulo entre vectores con cos α = u·v/(‖u‖‖v‖).

**Ejercicio 4.7 · E p. 140 · U §4.1.3 (cilíndricas, p. 149)** (MÁXIMA)
> Si las coordenadas cartesianas de un punto son (1, 1, 1), ¿cuáles son sus coordenadas cilíndricas?
- Solución del libro: ρ = √2, tg θ = 1 con x>0, y>0 → θ = π/4, z = 1 → (√2, π/4, 1).
- Método: ρ = √(x²+y²), tg θ = y/x (cuadrante por signos), z = z.

**Ejercicio 4.8 · E p. 141 · U §4.1.3 (cilíndricas p. 149; esféricas pp. 150-151)** (MÁXIMA; enunciado verificado en imagen)
> 1. Dado (1, 2, −1) en coordenadas cartesianas, se pide determinar sus coordenadas cilíndricas y esféricas.
> 2. Dado (1, π, 0) en coordenadas cilíndricas, se pide determinar sus coordenadas cartesianas.
> 3. Dado (1, π/2, 0) en coordenadas esféricas, se pide determinar sus coordenadas cartesianas.
- Solución del libro: 1) cilíndricas (√5, arctan 2 ≈ 1,1071, −1); esféricas ρ = √6, θ = arctan 2 ≈ 1,1071, ϕ = arcsen(−1/√6) ≈ −0,4205. 2) x = cos π = −1, y = sen π = 0, z = 0 → (−1, 0, 0). 3) x = cos 0 · cos(π/2) = 0; y = cos 0 · sen(π/2) = 1; z = sen 0 = 0 → (0, 1, 0).
- Método: cambios de coordenadas en ambos sentidos; de cartesianas a otro sistema, elegir θ por el cuadrante (signos de x e y); en sentido inverso, sustituir en las ecuaciones.
- Nota: el libro escribe el ángulo esférico como φ (U usa ϕ).

**Erratas en E:** no se han encontrado errores en las soluciones de 4.1-4.8 (cuentas revisadas con sympy). Solo pérdida de símbolos en la extracción (≠ en 4.4; barras de norma en el .txt de 4.4). Los enunciados de 4.2, 4.4 y 4.8 se han verificado en la imagen del PDF; los de 4.1, 4.3, 4.5, 4.6 y 4.7 solo en el .txt (legibles y sin símbolos dudosos).

---

## 4. X (exámenes resueltos): preguntas de ℝⁿ, producto escalar, normas, distancias y polares

Todas verificadas en imagen del PDF `Examenes-resueltos-Calculo.pdf`, salvo que se indique.

| X (PDF) | Convocatoria | Tipo | Enunciado | Solución en X / comprobación |
|---|---|---|---|---|
| **p. 1** | Feb 2010, 1ª sem., Ing. Eléctrica, PC4 (1 punto) | producto escalar, ortogonalidad | «¿Son ortogonales los vectores (0,1,2) y (−3,−4,2)? Justifíquese la respuesta.» | Producto = 0 − 4 + 4 = 0 → ortogonales. Correcta. |
| **p. 13** | Feb 2011, 2ª sem., Mecánica, Modelo B, PC4 | coordenadas polares | «Describa brevemente las coordenadas polares en R². Indique también cómo se cambia de coordenadas polares a cartesianas y viceversa.» | **Solución = «Vea la página 194 del libro Cálculo para Ingenieros»**. Erratum de referencia: en esta edición de U, la p. 194 es §5.2 (regla de la cadena); las polares están en U **pp. 148-149**. No hay desarrollo propio. |
| **p. 22** (enunciado) + **p. 23** (normas) | Feb 2012, 2ª sem., Mecánica, Modelo B, PC4 | producto escalar y normas | «Calcule el producto escalar de (1,2,3,4) y (−1,−2,−3,−4) y la norma de estos dos vectores.» | Producto = −1−4−9−16 = **−30**; ‖(1,2,3,4)‖ = √30; ‖(−1,−2,−3,−4)‖ = √30. Correcta. |
| **p. 53** | Sept 2015, Modelo A, P4 (1 punto) | distancia euclídea en R³ | «Calcular la distancia euclídea entre los puntos (1, −1, 0) y (1, 3, 5).» | (1,−1,0) − (1,3,5) = (0,−4,−5); módulo = √41. Correcta. |
| **p. 70** | Sept 2016, Modelo A, P4 (1 punto) | distancia en R³ | «Calcule la distancia entre los elementos (4, 2, 0) y (1, −1, 3) ∈ R³.» | d = √(3² + 3² + 3²) = √27. Correcta. |
| **p. 89** | Feb 2018, Modelo A, P4 corta (1 punto) | distancia y ángulo | «Calcule la distancia entre los puntos (1, 0, −1) y (2, 0, −1) con la métrica euclídea. Determine el ángulo que forman los vectores (0, 1, 2) y (1, −1, 1).» | Distancia = ‖(−1,0,0)‖ = 1 (correcta). Ángulo: u·v = 1, ‖u‖ = √5, ‖v‖ = √3 → cos α = 1/√15 (correcto). **ERRATA**: el libro escribe «α = 1.209 radianes»; **arccos(1/√15) = 1,3096 rad (≈ 75,04°)**; cos(1,209) ≈ 0,354 ≠ 0,258. Verificado con sympy. |
| **p. 139** | Sept 2018, Modelo B, Mecánica, P4 corta (1 punto) | producto escalar y normas en R⁴ | «Calcule el producto escalar de (1, 2, 0, 1) y (−1, −2, 3, 0) y la norma de estos dos vectores.» | **Sin solución en el PDF** (índice: «sin solución»). Cálculo propio (sympy): producto = −1−4+0+0 = **−5**; ‖(1,2,0,1)‖ = √6; ‖(−1,−2,3,0)‖ = √14. |

Relacionadas con polares pero de §4.2-4.4 (solo según el índice, **no verificadas en imagen**): p. 47 (Sept 2014 Modelo A, Ej. 6: continuidad/parciales con polares); p. 57 (Feb 2015 Modelo B, Ej. 6: continuidad con polares); p. 65 (Feb 2016 Modelo B, P4: límite con polares); p. 143 (Sept 2018 Electrónica, Ej. 6: dominio, gradiente, f∘g con g polares).

---

## 5. Faltas o dudas

1. **U no enuncia la desigualdad triangular ni Cauchy-Schwarz** en §4.1 (p. 143 dice «Nos limitamos a enunciar estas operaciones y sus propiedades…» pero no las enuncia). E 4.4 la usa «al margen» como «‖ū+v̄‖ ≤ ‖ū‖+‖v̄‖ para cualesquiera ū, v̄ ∈ Rⁿ». Cauchy-Schwarz no aparece ni en E, ni en S (cap. 12 ausente), ni en L del fichero. Solo hay la analogía de S App. A p. A8 (|a+b| ≤ |a|+|b| para reales). Hay que decidir si se marca como «propia» o se busca otra fuente.
2. **Erratum X p. 89:** α = 1,209 rad es incorrecto; correcto ≈ 1,3096 rad.
3. **Erratum X p. 13:** remite a «página 194» de U; el contenido de polares está en U pp. 148-149.
4. **X p. 139 sin solución** en el PDF (cálculo propio, ver tabla).
5. **Stewart:** `stewart.txt` no tiene cap. 12 (vectores) ni cap. 15 (cilíndricas/esféricas). Solo §10.3 (polares, pp. 654-656), A8 y A12. Dudoso: la frase sobre r negativo (Stewart p. 654 o 655): en el .txt aparece en una página sin cabecera, interpretada como p. 654; confirmar en el PDF si se cita.
6. **Larson:** sin equivalente en `larson.txt` (solo Tomo 1). Su índice cita páginas que no están en el fichero (715-807).
7. **U §4.1 llega a p. 152**, no a 151 (Ejemplo 4.8 y comienzo de §4.2 en p. 152).
8. **Colisión de numeración:** U «Ejemplo 4.x», E «Ejercicio 4.x» y X usan el mismo formato; citar siempre con prefijo («U Ej. 4.4», «E Ejercicio 4.4»).
9. **E 4.4, signo ≠:** se pierde en el .txt; el sentido («no se cumple») sí aparece en la solución.
10. **Fuentes para polares/cilíndricas/esféricas:** U §4.1.3 + E 4.6-4.8 + S §10.3 (solo polares). L no aporta nada.
