# Soluciones Tema 6.3 — Cálculo de integrales

Resolución paso a paso de los ejercicios de **E** de la sección 6.3 de U (Ejercicios 6.17-6.35, E pp. 223-242), de 10 preguntas de exámenes **X** y de 4 ejemplos propios. Todos los resultados se han comprobado con sympy **derivando la primitiva** y comparando con el integrando (y, en las definidas, con la integral numérica). Scripts: `v63.py`, `v63b.py`, `x63.py` en el scratchpad. Los enunciados de E se han leído como imagen (E pp. 223-242) y los de X también (render de las pp. 6, 11, 19, 20, 38, 81, 93, 94, 128, 141, 143 y 148).

Páginas: U impresa (= PDF + 2); E impresa = PDF; X = página del PDF de exámenes. Convocatorias de X tomadas de `indice_examenes_*.md` y de la cabecera de la página.

## 0. Herramientas de teoría que se usan

| Clave | Enunciado (resumido) | Dónde |
|---|---|---|
| **Linealidad** | $\int cf=c\int f$; $\int(f+g)=\int f+\int g$ ($f,g$ continuas, $c$ constante). | U p. 247 (Ej. 6.9) |
| **Tabla de inmediatas** (con $f=f(x)$) | (1) $\int a\,dx=ax+k$; (2) $\int f^a f'=\frac{f^{a+1}}{a+1}+k$ ($a\ne-1$); (3) $\int\frac{f'}{f}=\ln\lvert f\rvert+k$; (4) $\int e^f f'=e^f+k$; (5) $\int a^f f'=\frac{a^f}{\ln a}+k$; (6) $\int\cos f\cdot f'=\mathrm{sen}\,f+k$; (7) $\int\mathrm{sen}\,f\cdot f'=-\cos f+k$; (8) $\int\frac{f'}{\cos^2f}=\int(1+\mathrm{tg}^2f)f'=\mathrm{tg}\,f+k$; (9) $\int\frac{f'}{1+f^2}=\mathrm{arctg}\,f+k$; (10) $\int\frac{f'}{\sqrt{1-f^2}}=\mathrm{arcsen}\,f+k$; (11) $\int\frac{-f'}{\sqrt{1-f^2}}=\mathrm{arccos}\,f+k$. | U p. 248 (Ej. 6.10-6.14, pp. 248-249) |
| **Valor absoluto en el logaritmo** | «Cuando la integral es un logaritmo, escribimos el valor absoluto de su argumento»: $\int\frac{dx}{x}=\ln\lvert x\rvert+k$. | U Ej. 6.14, p. 249 |
| **Cambio de variable** | Con $x=g(t)$, $dx=g'(t)\,dt$: $\int f(x)\,dx=\int f(g(t))\,g'(t)\,dt$; al final se **deshace** el cambio. Consejo: «si [el integrando] se puede descomponer en dos partes y una es la derivada de la otra, ahí tenemos el cambio de variable». | U pp. 249-250 (Ej. 6.15, 6.16) |
| **Cambio de variable en la definida** | Si $x=g(t)$ tiene derivada continua no nula en $[c,d]$, $g(c)=a$, $g(d)=b$: $\int_a^b f(x)\,dx=\int_c^d f(g(t))g'(t)\,dt$ (se cambian los límites); o bien se deshace el cambio antes de sustituir los límites. | U p. 251 (Ej. 6.17) |
| **Integración por partes** | $\int u\,v'\,dx=uv-\int u'v\,dx$. Elegir $u$, $v'$ para que la nueva integral sea **más sencilla**, $v'$ fácil de integrar y $u$ fácil de derivar. Partes **reiterada** (Ej. 6.19) y **cíclica** (se despeja la integral, Ej. 6.20). | U pp. 251-253 |
| **Partes en la definida** | $\int_a^b uv'\,dx=uv\big|_a^b-\int_a^b u'v\,dx$. | U p. 254 (Ej. 6.22) |
| **Integrales racionales** | $\int\frac{p(x)}{q(x)}dx$: si $\mathrm{grado}\,p\ge\mathrm{grado}\,q$, **dividir**: $\frac pq=P+\frac rq$ con $\mathrm{grado}\,r<\mathrm{grado}\,q$. Factorizar $q$ (raíces reales con su multiplicidad y factores $x^2+bx+c$ sin raíces reales; raíces enteras con Ruffini) y descomponer en **fracciones simples**: $\frac{A_1}{x-a}+\dots+\frac{A_n}{(x-a)^n}$ por cada raíz real de multiplicidad $n$, y $\frac{Bx+C}{x^2+bx+c}$ por cada factor irreducible. | U p. 255 (Ej. 6.23, pp. 256-257) |
| **Integrales de las fracciones simples** | $\int\frac{A}{x-a}dx=A\ln\lvert x-a\rvert+k$; $\int\frac{A}{(x-a)^n}dx=\frac{A}{-n+1}(x-a)^{-n+1}+k$ ($n\ge2$); $\int\frac{Bx+C}{x^2+bx+c}dx$ = logaritmo + arcotangente (ajustar el numerador a la derivada del denominador). | U pp. 257-258 (Ej. 6.24, pp. 258-259) |
| **Método de Hermite** | Si $q$ tiene raíces múltiples (sobre todo complejas): $\frac{p}{q}=\frac{d}{dx}\Big(\frac{f}{g}\Big)+\frac{p_1}{q_1}$, $g$ = $q$ con cada multiplicidad rebajada en 1, $\mathrm{grado}\,f=\mathrm{grado}\,g-1$, $q_1$ = factores de $q$ con multiplicidad 1. Entonces $\int\frac pq=\frac fg+\int\frac{p_1}{q_1}$. | U pp. 258-261 (Ej. 6.25, pp. 260-261) |
| **Cambio $t=\mathrm{tg}\frac x2$** | $\mathrm{sen}\,x=\frac{2t}{1+t^2}$, $\cos x=\frac{1-t^2}{1+t^2}$, $dx=\frac{2\,dt}{1+t^2}$: convierte una expresión racional en $\mathrm{sen}\,x$, $\cos x$ en una integral racional en $t$. | U p. 261 (Ej. 6.26, pp. 261-262) |
| **$\mathrm{sen}^nx\cos^mx$** | Si $n$ y $m$ son pares: $\mathrm{sen}^2x=\frac{1-\cos2x}2$, $\cos^2x=\frac{1+\cos2x}2$ (Ej. 6.27, p. 262). Si $n=2k+1$ es impar: $\mathrm{sen}^{2k+1}x\cos^mx=(1-\cos^2x)^k\cos^mx\,\mathrm{sen}\,x$, potencias de $\cos x$ por su derivada cambiada de signo (igual si $m$ es impar). | U pp. 262-263 (Ej. 6.28, p. 263) |
| **Regla de Barrow** | Si $f$ es continua en $[a,b]$ y $F$ es una primitiva: $\int_a^b f=F(b)-F(a)$. | U Teor. 6.2, p. 244 |
| **Área** | Si $f\ge0$ en $[a,b]$, el área bajo la gráfica es $\int_a^b f$; donde $f<0$ el área «se resta» (área con signo). Área entre dos gráficas: $\int_a^b\lvert f-g\rvert$. | U §6.1, p. 238 |

**Herramientas de temas anteriores:** derivadas de las funciones elementales y regla de la cadena (U §2.2, p. 79), con $(\mathrm{arcsen}\,x)'=\frac1{\sqrt{1-x^2}}$ y $(\mathrm{arctg}\,x)'=\frac1{1+x^2}$; propiedades del logaritmo $\ln a+\ln b=\ln(ab)$, $r\ln a=\ln a^r$.

**Cambios para raíces (E 6.28-6.29 y X p. 143):** si aparecen potencias $x^{a/b},x^{c/d},\dots$, el cambio $x=t^r$ con $r=\mathrm{m.c.m.}(b,d,\dots)$ hace desaparecer las raíces (E p. 235, nota al margen); si aparece $\sqrt{\frac{x+1}{x-1}}$ (o en general $\sqrt{\frac{ax+b}{cx+d}}$), se iguala la raíz a $t$ (E 6.29).

---

### Receta general del tema: cómo elegir la técnica

> **Paso 0. Preparar.** Simplificar el integrando y separar sumas (linealidad, U p. 247). Mirar el dominio: ahí es donde la primitiva tiene sentido.
>
> **Paso 1. ¿Inmediata o casi?** Buscar en la tabla de U p. 248 la forma «función compuesta × derivada de lo de dentro». Si solo falta una constante, multiplicar y dividir por ella ($\int\frac{x}{x^2+3}dx=\frac12\int\frac{2x}{x^2+3}dx$).
>
> **Paso 2. ¿Cambio de variable?** Si el integrando se puede partir en «una función» y «su derivada» (salvo constante), llamar $t$ a esa función (U p. 250). También si hay algo molesto dentro de otra función ($\mathrm{sen}\sqrt x$, $e^{2x}$, $\sqrt[3]{1+x^3}$): $t=$ lo molesto.
>
> **Paso 3. ¿Producto de dos tipos distintos?** (polinomio·$e^x$, polinomio·$\mathrm{sen}$/$\cos$, polinomio·$\ln x$, $\ln x$ o $\mathrm{arc}\dots$ solos, $e^x\cos x$): **partes**. Se toma como $u$ la función que se simplifica al derivar. Orientación (regla propia, no de U): $u$ = la que sale primero en **L**ogaritmo → **A**rco → **P**olinomio → **T**rigonométrica/**E**xponencial; $v'$ = el resto. Si la integral vuelve a aparecer, despejarla (cíclica).
>
> **Paso 4. ¿Cociente de polinomios?** (a) Si $\mathrm{grado\,num}\ge\mathrm{grado\,den}$, **dividir**. (b) Mirar si el numerador es (casi) la derivada del denominador: entonces es un $\ln$. (c) Factorizar el denominador y descomponer en **fracciones simples**; si hay factores $x^2+bx+c$ repetidos, **Hermite**. (d) Integrar cada fracción: $\ln$, potencia o $\ln$+$\mathrm{arctg}$.
>
> **Paso 5. ¿Trigonométrica?** (a) $\mathrm{sen}^nx\cos^mx$ con algún exponente impar: separar un factor $\mathrm{sen}\,x$ (o $\cos x$), pasar el resto con $\mathrm{sen}^2+\cos^2=1$ y cambio $t=\cos x$ (o $t=\mathrm{sen}\,x$). (b) Exponentes pares: fórmulas del ángulo doble. (c) Si solo aparece $\mathrm{tg}(\cdot)$: $t=\mathrm{tg}(\cdot)$. (d) Expresión racional en $\mathrm{sen}$ y $\cos$ cualquiera: $t=\mathrm{tg}\frac x2$ (siempre funciona, pero da racionales largas: dejarlo para el final).
>
> **Paso 6. ¿Raíces de $x$?** $x=t^r$ con $r$ = m.c.m. de los índices; $\sqrt{\frac{ax+b}{cx+d}}=t$.
>
> **Paso 7. Si es definida:** comprobar que el integrando es continuo en $[a,b]$; si se cambia de variable, **cambiar también los límites** (o deshacer el cambio); aplicar Barrow. Si se pide un **área**, estudiar el signo y partir el intervalo en los puntos de corte.
>
> **Paso 8. Comprobar SIEMPRE derivando** la primitiva y escribir $+C$.

---

## 1. Ejercicios de E (agrupados por técnica, de fácil a difícil; numeración conservada)

Orden propuesto: **inmediatas** 6.17 → 6.30 → 6.31 · **partes** 6.18 → 6.19 · **racionales** 6.20 → 6.21 → 6.22 → 6.23 → 6.24 → 6.25 · **cambios que racionalizan** 6.28 → 6.29 → 6.27 · **trigonométricas** 6.32 → 6.26 · **áreas** 6.33 → 6.34 → 6.35.

---

### A. Inmediatas y cambio de variable sencillo

---

### Ejercicio 6.17 (E pp. 223-224)

> Calcula las integrales indefinidas siguientes:
> 1. $\displaystyle\int\frac{\ln x}{x}\,dx$. 2. $\displaystyle\int\frac{x^2-1}{x^3-3x+7}\,dx$. 3. $\displaystyle\int\frac{\mathrm{sen}\sqrt{x^3}}{\sqrt{x^3}}\cdot x^2\,dx$.

**Antes de calcular**
- **Qué me piden:** tres primitivas (familias $F(x)+C$).
- **Cómo lo pienso:** en las tres aparece una función y, muy cerca, su derivada: $\ln x$ y $\frac1x$; $x^3-3x+7$ y $3x^2-3$; $\sqrt{x^3}=x^{3/2}$ y $\frac32x^{1/2}$. Son inmediatas de la tabla, ajustando constantes.
- **Qué uso:** tabla de inmediatas (U p. 248): filas (2) $\int f^af'=\frac{f^{a+1}}{a+1}$, (3) $\int\frac{f'}f=\ln\lvert f\rvert$ y (7) $\int\mathrm{sen}\,f\cdot f'=-\cos f$.
- **Por dónde empiezo:** en cada una, derivar la «función de dentro» y comparar con lo que sobra.

**1.**
1. **Dominio.** $\ln x$ exige $x>0$; trabajamos en $(0,\infty)$.
2. **Detectar $f$ y $f'$.** Con $f(x)=\ln x$ se tiene $f'(x)=\frac1x$, y el integrando es $\ln x\cdot\frac1x=f\cdot f'=f^1f'$.
3. **Fila (2) con $a=1$:** $\int f^1f'=\frac{f^2}2+C$, es decir
   $$\int\frac{\ln x}{x}\,dx=\frac{(\ln x)^2}2+C.$$
4. **Comprobación:** $\frac{d}{dx}\frac{(\ln x)^2}2=\frac{2\ln x}{2}\cdot\frac1x=\frac{\ln x}x$ ✓ (regla de la cadena).

**2.**
5. **Antes de pensar en fracciones simples**, mirar si el numerador es la derivada del denominador: $(x^3-3x+7)'=3x^2-3=3(x^2-1)$. El numerador es $\frac13$ de esa derivada.
6. **Ajustar la constante** (multiplicar y dividir por 3, linealidad U p. 247):
   $$\int\frac{x^2-1}{x^3-3x+7}dx=\frac13\int\frac{3(x^2-1)}{x^3-3x+7}dx=\frac13\int\frac{f'}{f}dx.$$
7. **Fila (3):** $=\frac13\ln\lvert x^3-3x+7\rvert+C$ (con valor absoluto: el denominador puede ser negativo, por ejemplo en $x=-3$ vale $-11$).

**3.**
8. **Reescribir con exponentes:** $\sqrt{x^3}=x^{3/2}$, así que $\frac{x^2}{\sqrt{x^3}}=x^{2-3/2}=x^{1/2}$ y el integrando es $\mathrm{sen}(x^{3/2})\cdot x^{1/2}$ (para $x>0$).
9. **Derivada de lo de dentro:** $(x^{3/2})'=\frac32x^{1/2}$. Sobra $x^{1/2}$, que es $\frac23$ de esa derivada.
10. **Ajustar y aplicar la fila (7):**
    $$\int\mathrm{sen}(x^{3/2})\,x^{1/2}dx=\frac23\int\mathrm{sen}(x^{3/2})\cdot\tfrac32x^{1/2}\,dx=-\frac23\cos\sqrt{x^3}+C.$$
11. Aunque es un producto, **no** hace falta partes: es inmediata.

**Receta.** Antes de cualquier técnica, buscar «función + su derivada»; si la derivada aparece multiplicada por una constante distinta, multiplicar y dividir por ella.

**Error típico.** En 2., lanzarse a fracciones simples (el denominador no tiene raíces sencillas) o escribir $\ln(x^3-3x+7)$ sin valor absoluto. En 3., olvidar el factor $\frac23$.

sympy: las tres derivadas coinciden con los integrandos.

---

### Ejercicio 6.30 (E p. 237)

> Señala el valor de $\displaystyle\int_0^1\frac{\mathrm{arcsen}\frac x2}{\sqrt{4-x^2}}\,dx$:
> a) $-\frac{\pi^2}9$. b) $\frac{\pi^2}{72}$. c) $-\frac{\pi}{\sqrt3}$. d) $\frac{\pi}{\sqrt3}$.

**Antes de calcular**
- **Qué me piden:** el valor de una integral definida.
- **Cómo lo pienso:** el integrando es positivo en $[0,1]$ (descarto a) y c)). Además $\frac1{\sqrt{4-x^2}}$ «huele» a la derivada de $\mathrm{arcsen}\frac x2$: el integrando sería $f\cdot f'$.
- **Qué uso:** derivada de $\mathrm{arcsen}$ y regla de la cadena (U §2.2, p. 79); tabla, fila (2) (U p. 248); Barrow (U Teor. 6.2, p. 244).
- **Por dónde empiezo:** derivar $\mathrm{arcsen}\frac x2$.

1. **Continuidad.** En $[0,1]$: $4-x^2\ge3>0$ y $\frac x2\in[0,\frac12]$, donde $\mathrm{arcsen}$ es continuo. Barrow se puede usar.
2. **Derivar $f(x)=\mathrm{arcsen}\frac x2$** con la regla de la cadena:
   $$f'(x)=\frac{1}{\sqrt{1-\frac{x^2}4}}\cdot\frac12=\frac{1}{\sqrt{\frac{4-x^2}{4}}}\cdot\frac12=\frac{2}{\sqrt{4-x^2}}\cdot\frac12=\frac1{\sqrt{4-x^2}}.$$
3. **El integrando es $f\cdot f'$**, cuya primitiva es $\frac{f^2}2$ (fila (2), $a=1$): $F(x)=\frac12\,\mathrm{arcsen}^2\frac x2$.
4. **Barrow:**
   $$\int_0^1\frac{\mathrm{arcsen}\frac x2}{\sqrt{4-x^2}}dx=\frac12\Big(\mathrm{arcsen}^2\tfrac12-\mathrm{arcsen}^20\Big)=\frac12\Big(\frac\pi6\Big)^2=\frac{\pi^2}{72}.$$
5. **Respuesta: b).** Comprobación de sentido: $\frac{\pi^2}{72}\approx0{,}137>0$.

**Receta.** Si aparece una función inversa ($\mathrm{arcsen}$, $\mathrm{arctg}$, $\ln$) junto con algo que parece su derivada, probar «$f\cdot f'$» o «$f'\!\cdot g(f)$».

**Error típico.** Olvidar el factor $\frac12$ de la regla de la cadena en la derivada de $\mathrm{arcsen}\frac x2$ (y no ver que el $2$ del denominador $\sqrt{4-x^2}$ lo compensa).

sympy: $\int_0^1=\frac{\pi^2}{72}$.

---

### Ejercicio 6.31 (E p. 238)

> Señala el valor de $\displaystyle\int_{1/2}^{5/4}\frac{dx}{\sqrt{3-(2x-1)^2}}$: a) $0$. b) $\frac\pi4$. c) $\frac\pi{\sqrt3}$. d) $\frac\pi6$.

**Antes de calcular**
- **Qué me piden:** el valor de una integral definida.
- **Cómo lo pienso:** «$\frac{1}{\sqrt{\text{número}-(\dots)^2}}$» es de tipo arcoseno. Molesta el $2x-1$: lo llamo $t$ y cambio también los límites. Luego saco el $3$ fuera de la raíz para tener $\sqrt{1-(\cdot)^2}$.
- **Qué uso:** cambio de variable en la definida (U p. 251); tabla, fila (10) $\int\frac{f'}{\sqrt{1-f^2}}=\mathrm{arcsen}\,f$ (U p. 248).
- **Por dónde empiezo:** $t=2x-1$.

1. **Continuidad.** En $[\frac12,\frac54]$, $2x-1\in[0,\frac32]$ y $(2x-1)^2\le\frac94<3$: la raíz es positiva y el integrando continuo.
2. **Cambio $t=2x-1$:** $dt=2\,dx$, o sea $dx=\frac{dt}2$. **Límites nuevos:** $x=\frac12\Rightarrow t=0$; $x=\frac54\Rightarrow t=\frac32$.
   $$I=\frac12\int_0^{3/2}\frac{dt}{\sqrt{3-t^2}}.$$
3. **Preparar el arcoseno.** Sacar factor común $3$ dentro de la raíz:
   $$\sqrt{3-t^2}=\sqrt3\sqrt{1-\big(\tfrac t{\sqrt3}\big)^2},\qquad\frac1{\sqrt{3-t^2}}=\frac{\frac1{\sqrt3}}{\sqrt{1-\big(\tfrac t{\sqrt3}\big)^2}}.$$
   Con $f(t)=\frac t{\sqrt3}$, $f'(t)=\frac1{\sqrt3}$: es exactamente $\frac{f'}{\sqrt{1-f^2}}$.
4. **Primitiva:** $\mathrm{arcsen}\frac t{\sqrt3}$. **Barrow** con los límites nuevos (ya no hay que volver a $x$):
   $$I=\frac12\Big(\mathrm{arcsen}\frac{3/2}{\sqrt3}-\mathrm{arcsen}\,0\Big)=\frac12\,\mathrm{arcsen}\frac{\sqrt3}2=\frac12\cdot\frac\pi3=\frac\pi6.$$
   ($\frac{3/2}{\sqrt3}=\frac{3}{2\sqrt3}=\frac{\sqrt3}2$.)
5. **Respuesta: d).**

**Receta.** $\int\frac{dx}{\sqrt{a^2-(\text{lineal})^2}}$: cambio $t=$ lineal y sacar $a$ de la raíz para tener $\mathrm{arcsen}\frac ta$. En una definida, al cambiar de variable se cambian los límites.

**Error típico.** Cambiar la variable pero dejar los límites $\frac12$ y $\frac54$ (que eran de $x$), u olvidar el $\frac12$ de $dx=\frac{dt}2$.

sympy: integral numérica $0{,}5235987\ldots=\frac\pi6$.

---

### B. Integración por partes

---

### Ejercicio 6.18 (E pp. 224-225)

> Queremos resolver la integral indefinida $I=\int xe^x\,dx$ utilizando integración por partes:
> a) Interesa escoger $u=x$ y $v'=e^x$. b) Interesa escoger $u=e^x$ y $v'=x$. c) Las dos opciones anteriores son válidas. d) Ninguna de las anteriores.

**Antes de calcular**
- **Qué me piden:** decidir qué elección de $u$ y $v'$ conviene.
- **Cómo lo pienso:** la fórmula cambia $\int uv'$ por $\int u'v$. Conviene que $u'$ sea más simple que $u$ y que $v$ no se complique: $x$ al derivar se convierte en $1$; $e^x$ no cambia ni al derivar ni al integrar.
- **Qué uso:** integración por partes (U p. 252), con el criterio «la nueva integral debe ser más sencilla».
- **Por dónde empiezo:** probar la opción a).

1. **Opción a):** $u=x\Rightarrow u'=1$; $v'=e^x\Rightarrow v=\int e^xdx=e^x$.
2. **Fórmula** $\int uv'=uv-\int u'v$:
   $$I=xe^x-\int1\cdot e^x\,dx=xe^x-e^x+C=(x-1)e^x+C.$$
   La nueva integral, $\int e^x$, es inmediata: **a) funciona**.
3. **Opción b):** $u=e^x\Rightarrow u'=e^x$; $v'=x\Rightarrow v=\frac{x^2}2$:
   $$I=\frac{x^2}2e^x-\int\frac{x^2}2e^x\,dx.$$
   La nueva integral tiene $x^2$ en vez de $x$: es **más difícil** que la original. b) no interesa, y por tanto c) tampoco.
4. **Respuesta: a).**
5. **Comprobación:** $\frac{d}{dx}(x-1)e^x=e^x+(x-1)e^x=xe^x$ ✓.

**Receta.** Polinomio × $e^x$ (o × $\mathrm{sen}$, $\cos$): $u$ = polinomio (baja de grado al derivar), $v'$ = la exponencial o trigonométrica.

**Error típico.** Elegir $u$ al revés: la integral crece de grado en vez de simplificarse.

sympy: $\frac{d}{dx}(x-1)e^x=xe^x$.

---

### Ejercicio 6.19 (E p. 225)

> Utilizando integración por partes, calcula la siguiente integral: $\displaystyle I=\int\frac{xe^x}{(x+1)^2}\,dx$.

**Antes de calcular**
- **Qué me piden:** una primitiva, por partes.
- **Cómo lo pienso:** $\frac1{(x+1)^2}$ se integra fácil ($-\frac1{x+1}$), así que es buen $v'$. Y al derivar $u=xe^x$ sale $e^x(x+1)$, que tiene un $(x+1)$ que se simplificará con el $\frac1{x+1}$ de $v$.
- **Qué uso:** integración por partes (U p. 252); tabla, fila (2) con $a=-2$ (U p. 248).
- **Por dónde empiezo:** $u=xe^x$, $v'=\frac1{(x+1)^2}$.

1. **Dominio:** $x\ne-1$.
2. **Elección:** $u=xe^x\Rightarrow u'=e^x+xe^x=e^x(x+1)$ (derivada de un producto).
   $v'=(x+1)^{-2}\Rightarrow v=\frac{(x+1)^{-1}}{-1}=-\frac1{x+1}$ (fila (2), $a=-2$).
3. **Fórmula:**
   $$I=xe^x\cdot\Big(-\frac1{x+1}\Big)-\int e^x(x+1)\cdot\Big(-\frac1{x+1}\Big)dx=-\frac{xe^x}{x+1}+\int e^x\,dx.$$
4. **La nueva integral es inmediata:** $I=-\frac{xe^x}{x+1}+e^x+C$.
5. **Simplificar** (denominador común): $-\frac{xe^x}{x+1}+\frac{(x+1)e^x}{x+1}=\frac{e^x}{x+1}$. Así
   $$I=\frac{e^x}{x+1}+C.$$
6. **Comprobación:** $\Big(\frac{e^x}{x+1}\Big)'=\frac{e^x(x+1)-e^x}{(x+1)^2}=\frac{xe^x}{(x+1)^2}$ ✓.

**Receta.** En partes, a veces la clave es que $u'$ «traiga» un factor que cancela con $v$. Si $v'=\frac1{(x+a)^2}$, $v=-\frac1{x+a}$.

**Error típico.** Tomar $u=x$, $v'=\frac{e^x}{(x+1)^2}$: esa $v'$ no tiene primitiva elemental sencilla y el método se atasca.

sympy: la derivada de $-\frac{xe^x}{x+1}+e^x$ coincide con el integrando.

---

### C. Integrales racionales

---

### Ejercicio 6.20 (E pp. 225-226)

> Descompón la expresión racional $f(x)=\dfrac{x^2+7x+3}{(x+1)^3}$ en fracciones simples.

**Antes de calcular**
- **Qué me piden:** escribir $f$ como suma de fracciones del tipo $\frac{A}{(x+1)^k}$.
- **Cómo lo pienso:** el denominador tiene una sola raíz, $x=-1$, triple; el grado del numerador (2) es menor que el del denominador (3), así que no hay que dividir. Por cada potencia de $(x+1)$ hasta la 3ª va una fracción.
- **Qué uso:** descomposición en fracciones simples (U p. 255); igualdad de polinomios por coeficientes.
- **Por dónde empiezo:** plantear $\frac a{x+1}+\frac b{(x+1)^2}+\frac c{(x+1)^3}$.

1. **Comprobaciones previas:** grado $2<3$ (no se divide); el numerador no se anula en $-1$ ($1-7+3=-3\ne0$), así que no se simplifica nada.
2. **Planteamiento** (raíz real de multiplicidad 3 ⇒ tres fracciones, U p. 255):
   $$\frac{x^2+7x+3}{(x+1)^3}=\frac{a}{x+1}+\frac{b}{(x+1)^2}+\frac{c}{(x+1)^3}.$$
3. **Quitar denominadores** (multiplicar por $(x+1)^3$):
   $$x^2+7x+3=a(x+1)^2+b(x+1)+c=ax^2+(2a+b)x+(a+b+c).$$
4. **Igualar coeficientes** (dos polinomios son iguales si lo son sus coeficientes): $a=1$; $2a+b=7\Rightarrow b=5$; $a+b+c=3\Rightarrow c=-3$.
5. **Resultado:**
   $$f(x)=\frac1{x+1}+\frac5{(x+1)^2}-\frac3{(x+1)^3}.$$
6. **Otra forma rápida:** con $u=x+1$ ($x=u-1$), el numerador es $(u-1)^2+7(u-1)+3=u^2+5u-3$, y $\frac{u^2+5u-3}{u^3}=\frac1u+\frac5{u^2}-\frac3{u^3}$. Mismo resultado.
7. **(Para integrar después):** $\int f=\ln\lvert x+1\rvert-\frac5{x+1}+\frac3{2(x+1)^2}+C$ (U p. 257).

**Receta.** Raíz real $a$ de multiplicidad $n$ ⇒ $\frac{A_1}{x-a}+\dots+\frac{A_n}{(x-a)^n}$. Con una única raíz, el cambio $u=x-a$ da la descomposición directamente.

**Error típico.** Poner solo $\frac{c}{(x+1)^3}$ (falta una fracción por cada potencia) o fracciones del tipo $\frac{bx+c}{(x+1)^2}$.

sympy: `apart` da $\frac1{x+1}+\frac5{(x+1)^2}-\frac3{(x+1)^3}$.

---

### Ejercicio 6.21 (E pp. 226-227)

> Calcula $\displaystyle\int\frac{x+2}{x^2-1}\,dx$.

**Antes de calcular**
- **Qué me piden:** una primitiva de una función racional.
- **Cómo lo pienso:** grado $1<2$; el denominador se factoriza $x^2-1=(x-1)(x+1)$, dos raíces reales simples: dos fracciones $\frac A{x-1}+\frac B{x+1}$, cada una da un logaritmo.
- **Qué uso:** fracciones simples (U p. 255) e $\int\frac A{x-a}=A\ln\lvert x-a\rvert$ (U p. 257).
- **Por dónde empiezo:** factorizar el denominador.

1. **Factorizar:** $x^2-1=(x-1)(x+1)$; dominio $x\ne\pm1$.
2. **Planteamiento:** $\frac{x+2}{x^2-1}=\frac A{x-1}+\frac B{x+1}$. Multiplicando por $(x-1)(x+1)$:
   $$x+2=A(x+1)+B(x-1).$$
3. **Dar a $x$ los valores de las raíces** (se anula un sumando cada vez, como en U Ej. 6.23, p. 256):
   - $x=1$: $3=2A\Rightarrow A=\frac32$.
   - $x=-1$: $1=-2B\Rightarrow B=-\frac12$.
4. **Integrar cada fracción:**
   $$\int\frac{x+2}{x^2-1}dx=\frac32\ln\lvert x-1\rvert-\frac12\ln\lvert x+1\rvert+C.$$
5. **Forma compacta** (propiedades del logaritmo): $=\ln\dfrac{\sqrt{\lvert x-1\rvert^3}}{\sqrt{\lvert x+1\rvert}}+C$.
6. **Otra vía:** separar $\frac{x}{x^2-1}+\frac2{x^2-1}$; la primera es $\frac12\frac{2x}{x^2-1}$ (tipo $\frac{f'}f$) y da $\frac12\ln\lvert x^2-1\rvert$; la segunda, $\frac2{x^2-1}=\frac1{x-1}-\frac1{x+1}$. Al sumar se llega a lo mismo.

**Receta.** Denominador con raíces reales simples: $\frac{A}{x-a}+\frac{B}{x-b}$; los coeficientes salen al sustituir $x=a$ y $x=b$ en la igualdad sin denominadores.

**Error típico.** Olvidar el valor absoluto ($\ln(x-1)$ no existe para $x<1$) o el coeficiente al integrar ($\int\frac{3/2}{x-1}=\frac32\ln\lvert x-1\rvert$).

sympy: la derivada de la primitiva coincide con $\frac{x+2}{x^2-1}$.

---

### Ejercicio 6.22 (E pp. 227-229)

> Señala la afirmación correcta relativa a la función racional dada por $f(x)=\dfrac{x^3+3x^2-28x-33}{x^2-x-20}$:
> a) Se verifica $f(x)=\frac3{x-5}+\frac7{x+4}$.
> b) Se verifica $\displaystyle\int f(x)\,dx=\frac{x^2}2+4x+3\ln\lvert x-5\rvert-7\ln\lvert x+4\rvert+C$.
> c) Ninguna de las anteriores.

**Antes de calcular**
- **Qué me piden:** comprobar una descomposición y una primitiva.
- **Cómo lo pienso:** el numerador tiene grado 3 y el denominador 2: **antes de descomponer hay que dividir**. Sin parte entera, a) no puede ser (cuando $x\to\infty$, $f(x)$ crece como $x$, y $\frac3{x-5}+\frac7{x+4}\to0$).
- **Qué uso:** división de polinomios y fracciones simples (U p. 255); integrales de las fracciones simples (U p. 257).
- **Por dónde empiezo:** dividir $x^3+3x^2-28x-33$ entre $x^2-x-20$.

1. **División** (Dividendo = cociente·divisor + resto):
   - $x^3:x^2=x$; $x(x^2-x-20)=x^3-x^2-20x$; resto parcial: $4x^2-8x-33$.
   - $4x^2:x^2=4$; $4(x^2-x-20)=4x^2-4x-80$; resto: $-4x+47$.
   $$f(x)=x+4+\frac{-4x+47}{x^2-x-20}.$$
2. **a) es falsa**: falta la parte entera $x+4$ (y, como se ve abajo, el signo del $7$).
3. **Factorizar el divisor:** $x^2-x-20=0\iff x=\frac{1\pm\sqrt{81}}2$, es decir $x=5$, $x=-4$: $x^2-x-20=(x-5)(x+4)$.
4. **Fracciones simples del resto:** $\frac{-4x+47}{(x-5)(x+4)}=\frac a{x-5}+\frac b{x+4}$, o sea $-4x+47=a(x+4)+b(x-5)$.
   - $x=5$: $27=9a\Rightarrow a=3$.
   - $x=-4$: $63=-9b\Rightarrow b=-7$.
5. **Integrar:**
   $$\int f=\int\Big(x+4+\frac3{x-5}-\frac7{x+4}\Big)dx=\frac{x^2}2+4x+3\ln\lvert x-5\rvert-7\ln\lvert x+4\rvert+C.$$
6. **Respuesta: b).**

**Receta.** Integral racional: lo primero, comparar grados. Si $\mathrm{grado\,num}\ge\mathrm{grado\,den}$, dividir; la parte entera se integra como polinomio y el resto se descompone.

**Error típico.** Descomponer en fracciones simples sin dividir antes: los coeficientes «salen» pero la igualdad es falsa.

sympy: `div` da cociente $x+4$ y resto $47-4x$; `apart` da $x+4+\frac3{x-5}-\frac7{x+4}$.

---

### Ejercicio 6.23 (E p. 229)

> Señala la afirmación correcta relativa a la función racional dada por $f(x)=\dfrac{8x^3}{(x^2+1)^2}$:
> a) Como el polinomio del denominador no admite raíces complejas, no es adecuado utilizar el método de Hermite para calcular $\int f(x)\,dx$.
> b) El polinomio del denominador tiene raíces complejas múltiples y es conveniente utilizar el método de Hermite para calcular $\int f(x)\,dx$.
> c) Se verifica $f(x)=\dfrac{4x}{x^2+1}+\dfrac{d}{dx}\Big(\dfrac4{x^2+1}\Big)$.
> d) Ninguna de las anteriores.

**Antes de calcular**
- **Qué me piden:** reconocer cuándo usar Hermite y comprobar una descomposición.
- **Cómo lo pienso:** $x^2+1=0$ tiene las raíces complejas $\pm i$; al estar al cuadrado, son dobles. Ese es justo el caso en el que U recomienda Hermite. Para c), basta derivar y sumar.
- **Qué uso:** método de Hermite (U pp. 258-259).
- **Por dónde empiezo:** resolver $(x^2+1)^2=0$.

1. **Raíces del denominador:** $(x^2+1)^2=0\iff x^2=-1\iff x=\pm i$, cada una con multiplicidad 2. **a) es falsa.**
2. **Planteamiento de Hermite.** $q=(x^2+1)^2$; $g$ = $q$ con las multiplicidades rebajadas en 1 = $x^2+1$; $f$ de grado 1: $cx+e$; $q_1=x^2+1$:
   $$\frac{8x^3}{(x^2+1)^2}=\frac{ax+b}{x^2+1}+\frac{d}{dx}\Big(\frac{cx+e}{x^2+1}\Big).$$
3. **Derivar** (cociente): $\frac{d}{dx}\frac{cx+e}{x^2+1}=\frac{c(x^2+1)-2x(cx+e)}{(x^2+1)^2}=\frac{-cx^2-2ex+c}{(x^2+1)^2}$.
4. **Quitar denominadores:** $8x^3=(ax+b)(x^2+1)-cx^2-2ex+c=ax^3+(b-c)x^2+(a-2e)x+(b+c)$.
5. **Igualar coeficientes:** $a=8$; $b-c=0$; $a-2e=0\Rightarrow e=4$; $b+c=0$. De las dos con $b,c$: $b=c=0$.
   $$f(x)=\frac{8x}{x^2+1}+\frac{d}{dx}\Big(\frac4{x^2+1}\Big).$$
6. **c) es falsa:** el primer sumando es $\frac{8x}{x^2+1}$, no $\frac{4x}{x^2+1}$ (con $4x$ faltaría $\frac{4x}{x^2+1}$). **b) es la correcta.**
7. **Integral** (aunque no se pide): $\int f=4\ln(x^2+1)+\frac4{x^2+1}+C$ (sin valor absoluto: $x^2+1>0$).
8. **Atajo alternativo:** aquí también sirve el cambio $t=x^2+1$, $dt=2x\,dx$, $x^2=t-1$: $\int\frac{8x^3}{(x^2+1)^2}dx=\int\frac{4(t-1)}{t^2}dt=4\ln t+\frac4t+C$. Mismo resultado.

**Receta.** Denominador con factores irreducibles de grado 2 **repetidos** ⇒ Hermite: $\frac pq=\frac{d}{dx}\frac fg+\frac{p_1}{q_1}$, con $g$ = denominador con exponentes rebajados en uno.

**Error típico.** Pensar que «no tiene raíces» porque no tiene raíces **reales**: sí las tiene complejas.

sympy: $\frac{8x}{x^2+1}+\big(\frac4{x^2+1}\big)'-\frac{8x^3}{(x^2+1)^2}=0$; con $4x$ la diferencia es $-\frac{4x}{x^2+1}\ne0$.

---

### Ejercicio 6.24 (E p. 230)

> Calcula la siguiente integral indefinida $\displaystyle I=\int\frac{3x^4+4x^2+2x+1}{x(x^2+1)^2}\,dx$.

**Antes de calcular**
- **Qué me piden:** una primitiva de una racional con grado num (4) < grado den (5).
- **Cómo lo pienso:** raíces del denominador: $0$ (simple) y $\pm i$ (dobles). Raíces complejas múltiples ⇒ Hermite. La parte «derivada» se integra sola; quedan un $\ln$ y un $\ln$+$\mathrm{arctg}$.
- **Qué uso:** método de Hermite (U pp. 259-261); integrales de fracciones simples (U pp. 257-258).
- **Por dónde empiezo:** escribir la forma de Hermite.

1. **Forma de Hermite.** $q=x(x^2+1)^2$; $g=x^2+1$ (la $x$ simple desaparece de $g$, el factor doble pasa a simple); $f=fx+e$ (grado $1$); $q_1=x(x^2+1)$:
   $$\frac{3x^4+4x^2+2x+1}{x(x^2+1)^2}=\frac ax+\frac{bx+c}{x^2+1}+\frac{d}{dx}\Big(\frac{fx+e}{x^2+1}\Big).$$
2. **Derivada:** $\frac{d}{dx}\frac{fx+e}{x^2+1}=\frac{-fx^2-2ex+f}{(x^2+1)^2}$.
3. **Quitar denominadores** (multiplicar por $x(x^2+1)^2$):
   $$3x^4+4x^2+2x+1=a(x^2+1)^2+(bx+c)(x^2+1)x+(-fx^2-2ex+f)x.$$
4. **Desarrollar y agrupar:** $(a+b)x^4+(c-f)x^3+(2a+b-2e)x^2+(c+f)x+a$.
5. **Igualar coeficientes:** $a=1$; $a+b=3\Rightarrow b=2$; $c-f=0$ y $c+f=2\Rightarrow c=f=1$; $2a+b-2e=4\Rightarrow 4-2e=4\Rightarrow e=0$.
6. **Integrar cada trozo:**
   - $\int\frac{dx}x=\ln\lvert x\rvert$;
   - $\int\frac{2x+1}{x^2+1}dx=\int\frac{2x}{x^2+1}dx+\int\frac{dx}{x^2+1}=\ln(x^2+1)+\mathrm{arctg}\,x$ (filas (3) y (9));
   - $\int\frac{d}{dx}\Big(\frac{x}{x^2+1}\Big)dx=\frac x{x^2+1}$ (la integral de una derivada es la función).
7. **Resultado:**
   $$I=\ln\lvert x\rvert+\ln(x^2+1)+\mathrm{arctg}\,x+\frac x{x^2+1}+C.$$

**Receta.** Hermite: (1) $g$ = denominador con exponentes $-1$; (2) numerador genérico de grado $\mathrm{gr}(g)-1$; (3) derivar, quitar denominadores, igualar coeficientes; (4) la parte $\frac{d}{dx}\frac fg$ se integra sola.

**Error típico.** Olvidar la constante $e$ del numerador de $\frac{fx+e}{x^2+1}$ (aunque aquí salga $0$) o derivar mal el cociente.

sympy: la derivada de $I$ coincide con el integrando.

---

### Ejercicio 6.25 (E pp. 231-232)

> Calcular, usando el método de Hermite, $\displaystyle\int\frac{2x^2-x+1}{(x^2+x+1)^2(x+1)}\,dx$.

**Antes de calcular**
- **Qué me piden:** una primitiva por Hermite.
- **Cómo lo pienso:** $x+1$ da la raíz real simple $-1$; $x^2+x+1$ no tiene raíces reales (discriminante $1-4<0$) y está al cuadrado. Igual que 6.24, pero el trozo final necesita **completar cuadrados** para el arcotangente.
- **Qué uso:** Hermite (U pp. 259-261); $\ln$ + $\mathrm{arctg}$ para el factor irreducible (U p. 258).
- **Por dónde empiezo:** forma de Hermite con $g=x^2+x+1$.

1. **Forma de Hermite:**
   $$\frac{2x^2-x+1}{(x^2+x+1)^2(x+1)}=\frac{d}{dx}\Big(\frac{Ax+B}{x^2+x+1}\Big)+\frac C{x+1}+\frac{Dx+E}{x^2+x+1}.$$
2. **Derivada:** $\frac{d}{dx}\frac{Ax+B}{x^2+x+1}=\frac{A(x^2+x+1)-(Ax+B)(2x+1)}{(x^2+x+1)^2}=\frac{-Ax^2-2Bx+A-B}{(x^2+x+1)^2}$.
3. **Quitar denominadores** (multiplicar por $(x^2+x+1)^2(x+1)$):
   $$2x^2-x+1=(-Ax^2-2Bx+A-B)(x+1)+C(x^2+x+1)^2+(Dx+E)(x^2+x+1)(x+1).$$
4. **Un coeficiente rápido:** con $x=-1$ se anulan el primer y el tercer sumando: $2+1+1=C(1-1+1)^2\Rightarrow C=4$.
5. **Igualar coeficientes** (sistema de 5 ecuaciones):
   $x^4$: $C+D=0$; $x^3$: $-A+2C+2D+E=0$; $x^2$: $-A-2B+3C+2D+2E=2$; $x$: $A-3B+2C+D+2E=-1$; $x^0$: $A-B+C+E=1$.
   Con $C=4$: $D=-4$. La de $x^3$: $-A+8-8+E=0\Rightarrow E=A$. La de $x^0$: $A-B+4+A=1\Rightarrow B=2A+3$. La de $x^2$: $-A-2(2A+3)+12-8+2A=2\Rightarrow -3A-2=2\Rightarrow A=-\frac43$. Así $E=-\frac43$, $B=\frac13$. (La de $x$ se cumple: $-\frac43-1+8-4-\frac83=-1$ ✓.)
6. **Primer trozo:** $\int\frac{d}{dx}\Big(\frac{-\frac43x+\frac13}{x^2+x+1}\Big)dx=\frac{-4x+1}{3(x^2+x+1)}$.
7. **Segundo trozo:** $\int\frac4{x+1}dx=4\ln\lvert x+1\rvert$.
8. **Tercer trozo, $\int\frac{-4x-\frac43}{x^2+x+1}dx$.** Se busca la derivada del denominador, $2x+1$, en el numerador: $-4x-\frac43=-2(2x+1)+\frac23$. Así
   $$\int\frac{-4x-\frac43}{x^2+x+1}dx=-2\int\frac{2x+1}{x^2+x+1}dx+\frac23\int\frac{dx}{x^2+x+1}.$$
   - La primera es $\frac{f'}f$: $-2\ln(x^2+x+1)$ (sin valor absoluto: $x^2+x+1>0$ siempre).
   - **Completar cuadrados:** $x^2+x+1=\big(x+\frac12\big)^2+\frac34=\frac34\Big[\Big(\frac{2x+1}{\sqrt3}\Big)^2+1\Big]$.
   - Con $f=\frac{2x+1}{\sqrt3}$, $f'=\frac2{\sqrt3}$: $\int\frac{dx}{x^2+x+1}=\frac43\int\frac{dx}{f^2+1}=\frac43\cdot\frac{\sqrt3}2\int\frac{f'}{1+f^2}dx=\frac{2}{\sqrt3}\,\mathrm{arctg}\frac{2x+1}{\sqrt3}$.
   - Por tanto $\frac23\int\frac{dx}{x^2+x+1}=\frac4{3\sqrt3}\mathrm{arctg}\frac{2x+1}{\sqrt3}=\frac{4\sqrt3}9\mathrm{arctg}\frac{2x+1}{\sqrt3}$.
9. **Resultado:**
   $$\int\frac{2x^2-x+1}{(x^2+x+1)^2(x+1)}dx=\frac{-4x+1}{3(x^2+x+1)}+4\ln\lvert x+1\rvert-2\ln(x^2+x+1)+\frac{4\sqrt3}9\,\mathrm{arctg}\frac{2x+1}{\sqrt3}+C.$$

**Receta.** $\int\frac{Mx+N}{x^2+bx+c}$ (sin raíces reales): (1) escribir $Mx+N=\frac M2(2x+b)+\text{resto}$; (2) la parte $\frac{2x+b}{x^2+bx+c}$ da $\ln$; (3) completar cuadrados $x^2+bx+c=(x+\frac b2)^2+k^2$ y el resto da $\frac1k\mathrm{arctg}\frac{x+b/2}k$.

**Error típico.** En el sistema, perderse con los signos: sacar primero los coeficientes «fáciles» dando a $x$ el valor de la raíz real ($x=-1\Rightarrow C=4$) reduce el trabajo.

sympy: la derivada de la primitiva coincide con el integrando (comprobado en $x=\frac32,\frac52,\frac73$ y simbólicamente).

---

### D. Cambios de variable que racionalizan

---

### Ejercicio 6.28 (E pp. 234-235)

> Calcula $\displaystyle I=\int\frac{1+\sqrt x-\sqrt[3]{x^2}}{1+\sqrt[3]x}\,dx$ mediante un cambio de variable.

**Antes de calcular**
- **Qué me piden:** una primitiva con raíces de índices 2 y 3.
- **Cómo lo pienso:** si $x=t^6$, entonces $\sqrt x=t^3$, $\sqrt[3]x=t^2$, $\sqrt[3]{x^2}=t^4$: todas las raíces se vuelven potencias enteras y queda una racional en $t$. Se elige 6 porque es el m.c.m. de 2 y 3.
- **Qué uso:** cambio de variable (U pp. 249-250); división de polinomios (U p. 255); tabla, fila (9) (U p. 248). Cambio $x=t^r$, $r$ = m.c.m. de los índices (E p. 235).
- **Por dónde empiezo:** $x=t^6$, $dx=6t^5dt$ ($x>0$, $t=x^{1/6}>0$).

1. **Exponentes:** $\sqrt x=x^{1/2}$, $\sqrt[3]{x^2}=x^{2/3}$, $\sqrt[3]x=x^{1/3}$; m.c.m.$(2,3)=6$.
2. **Cambio $x=t^6$:** $x^{1/2}=t^3$, $x^{2/3}=t^4$, $x^{1/3}=t^2$, $dx=6t^5\,dt$:
   $$I=\int\frac{1+t^3-t^4}{1+t^2}\,6t^5\,dt=6\int\frac{-t^9+t^8+t^5}{t^2+1}\,dt.$$
3. **Grado 9 ≥ 2: dividir.** $-t^9+t^8+t^5=(t^2+1)(-t^7+t^6+t^5-t^4+t^2-1)+1$, es decir
   $$\frac{-t^9+t^8+t^5}{t^2+1}=-t^7+t^6+t^5-t^4+t^2-1+\frac1{1+t^2}.$$
   (Comprobación: al multiplicar $(t^2+1)(-t^7+t^6+t^5-t^4+t^2-1)$ sale $-t^9+t^8+t^5-1$, y $+1$ completa.)
4. **Integrar término a término** (potencias y $\mathrm{arctg}$):
   $$I=6\Big(-\frac{t^8}8+\frac{t^7}7+\frac{t^6}6-\frac{t^5}5+\frac{t^3}3-t+\mathrm{arctg}\,t\Big)+C.$$
5. **Deshacer el cambio** $t=\sqrt[6]x$:
   $$I=6\Big(-\frac{\sqrt[6]{x^8}}8+\frac{\sqrt[6]{x^7}}7+\frac x6-\frac{\sqrt[6]{x^5}}5+\frac{\sqrt x}3-\sqrt[6]x+\mathrm{arctg}\sqrt[6]x\Big)+C.$$

**Receta.** Varias raíces de $x$ ⇒ $x=t^r$ con $r$ = m.c.m. de los índices; queda una racional en $t$ (dividir si hace falta) y al final se deshace el cambio.

**Error típico.** Olvidar el $dx=6t^5dt$ (cambiar solo el integrando) o no dividir antes de integrar.

sympy: la derivada de $I(x)$ coincide con el integrando; `div` confirma cociente y resto $1$.

---

### Ejercicio 6.29 (E pp. 235-237)

> Transforma la integral $\displaystyle I=\int\sqrt{\frac{x+1}{x-1}}\,dx$ mediante el cambio de variable $\dfrac{x+1}{x-1}=t^2$.

**Antes de calcular**
- **Qué me piden:** hacer el cambio indicado, resolver la integral racional que resulta y volver a $x$.
- **Cómo lo pienso:** si llamo $t$ a la raíz, la raíz desaparece; para cambiar $dx$ hay que despejar $x$ en función de $t$ y derivar.
- **Qué uso:** cambio de variable $x=g(t)$, $dx=g'(t)dt$ (U p. 250); fracciones simples con raíces dobles (U p. 255, 257).
- **Por dónde empiezo:** despejar $x$ de $\frac{x+1}{x-1}=t^2$.

1. **Dominio y signo de $t$.** La raíz exige $\frac{x+1}{x-1}\ge0$: $x>1$ o $x\le-1$. Tomamos $t=\sqrt{\frac{x+1}{x-1}}\ge0$ y trabajamos en $x>1$ (ahí $t>1$).
2. **Despejar $x$:** $x+1=t^2(x-1)\Rightarrow x(1-t^2)=-(1+t^2)\Rightarrow x=\frac{t^2+1}{t^2-1}$.
3. **Derivar:** $\frac{dx}{dt}=\frac{2t(t^2-1)-2t(t^2+1)}{(t^2-1)^2}=\frac{-4t}{(t^2-1)^2}$, así que $dx=\frac{-4t}{(t^2-1)^2}dt$.
4. **Integral en $t$:** $I=\int t\cdot\frac{-4t}{(t^2-1)^2}dt=\int\frac{-4t^2}{(t^2-1)^2}dt$ (racional, grado $2<4$).
5. **Fracciones simples.** $(t^2-1)^2=(t-1)^2(t+1)^2$: dos raíces dobles ⇒
   $$\frac{-4t^2}{(t^2-1)^2}=\frac a{t-1}+\frac b{t+1}+\frac c{(t-1)^2}+\frac d{(t+1)^2}.$$
   Quitando denominadores e igualando coeficientes (o dando valores $t=1$, $t=-1$ y dos más): $a=c=d=-1$, $b=1$.
   (Con $t=1$: $-4=4c\Rightarrow c=-1$; con $t=-1$: $-4=4d\Rightarrow d=-1$; los coeficientes de $t^3$ y $t^0$ dan $a+b=0$ y $-a+b+c+d=0$, de donde $b=1$, $a=-1$.)
6. **Integrar:**
   $$\int\frac{-4t^2}{(t^2-1)^2}dt=-\ln\lvert t-1\rvert+\ln\lvert t+1\rvert+\frac1{t-1}+\frac1{t+1}+C=\ln\Big\lvert\frac{t+1}{t-1}\Big\rvert+\frac{2t}{t^2-1}+C.$$
7. **Deshacer el cambio (en $x>1$).** $t=\frac{\sqrt{x+1}}{\sqrt{x-1}}$, de modo que $\frac{t+1}{t-1}=\frac{\sqrt{x+1}+\sqrt{x-1}}{\sqrt{x+1}-\sqrt{x-1}}$ (multiplicando arriba y abajo por $\sqrt{x-1}$). Y $t^2-1=\frac{x+1}{x-1}-1=\frac2{x-1}$, luego $\frac{2t}{t^2-1}=t(x-1)=\sqrt{\frac{x+1}{x-1}}\,(x-1)=\sqrt{(x+1)(x-1)}=\sqrt{x^2-1}$.
8. **Resultado (para $x>1$):**
   $$I=\ln\Big\lvert\frac{\sqrt{x+1}+\sqrt{x-1}}{\sqrt{x+1}-\sqrt{x-1}}\Big\rvert+\sqrt{x^2-1}+C.$$

**Receta.** Cambio $x=g(t)$ dado implícitamente: (1) despejar $x$; (2) derivar para obtener $dx$; (3) sustituir todo; (4) resolver la racional; (5) deshacer el cambio y simplificar.

**Error típico.** Sustituir $dx$ por $dt$ (olvidar $g'(t)$) o equivocarse en el signo de $\frac{dx}{dt}$.

sympy: `apart` da $\frac1{t+1}-\frac1{(t+1)^2}-\frac1{t-1}-\frac1{(t-1)^2}$; la derivada del resultado coincide con $\sqrt{\frac{x+1}{x-1}}$ en $x=2,3,5$.

---

### Ejercicio 6.27 (E pp. 233-234)

> Calcula $\displaystyle I=\int\frac{\mathrm{tg}(2x+1)}{1+2\,\mathrm{tg}^2(2x+1)}\,dx$ utilizando un cambio de variable.

**Antes de calcular**
- **Qué me piden:** una primitiva con un cambio de variable.
- **Cómo lo pienso:** solo aparece $\mathrm{tg}(2x+1)$, siempre con el mismo argumento: llamo $t$ a la tangente. Su derivada es $2(1+t^2)$, así que $dx$ se expresa en $t$ y queda una racional.
- **Qué uso:** cambio de variable (U pp. 249-250); derivada de la tangente $(\mathrm{tg}\,u)'=(1+\mathrm{tg}^2u)\,u'$ (U §2.2, p. 79; tabla U p. 248, fila (8)); fracciones simples (U p. 255).
- **Por dónde empiezo:** $t=\mathrm{tg}(2x+1)$.

1. **Cambio:** $t=\mathrm{tg}(2x+1)\Rightarrow dt=2\big(1+\mathrm{tg}^2(2x+1)\big)dx=2(1+t^2)dx\Rightarrow dx=\frac{dt}{2(1+t^2)}$.
2. **Sustituir:**
   $$I=\int\frac{t}{1+2t^2}\cdot\frac{dt}{2(1+t^2)}=\frac12\int\frac{t}{(1+2t^2)(1+t^2)}dt.$$
3. **Fracciones simples** (dos factores irreducibles distintos): $\frac{t}{(1+2t^2)(1+t^2)}=\frac{at+b}{1+2t^2}+\frac{ct+d}{1+t^2}$. Quitando denominadores: $t=(at+b)(1+t^2)+(ct+d)(1+2t^2)$. Coeficientes: $t^3$: $a+2c=0$; $t^2$: $b+2d=0$; $t$: $a+c=1$; $t^0$: $b+d=0$. Sale $a=2$, $c=-1$, $b=d=0$:
   $$\frac{t}{(1+2t^2)(1+t^2)}=\frac{2t}{1+2t^2}-\frac{t}{1+t^2}.$$
4. **Integrar** (tipo $\frac{f'}f$, ajustando constantes: $(1+2t^2)'=4t$, $(1+t^2)'=2t$):
   $$I=\frac12\Big[\frac12\ln(1+2t^2)-\frac12\ln(1+t^2)\Big]+C=\frac14\ln\frac{1+2t^2}{1+t^2}+C.$$
5. **Deshacer el cambio y simplificar.** Con $\mathrm{tg}=\frac{\mathrm{sen}}{\cos}$ y $1+\mathrm{tg}^2=\frac1{\cos^2}$ (argumento $2x+1$):
   $$\frac{1+2\,\mathrm{tg}^2}{1+\mathrm{tg}^2}=\cos^2\cdot\Big(1+2\frac{\mathrm{sen}^2}{\cos^2}\Big)=\cos^2+2\,\mathrm{sen}^2=1+\mathrm{sen}^2.$$
6. **Resultado:** $I=\frac14\ln\big(1+\mathrm{sen}^2(2x+1)\big)+C$ (sin valor absoluto: el argumento es $\ge1$).

**Receta.** Integrando que solo depende de $\mathrm{tg}(u)$: cambio $t=\mathrm{tg}(u)$, $dx=\frac{dt}{u'(1+t^2)}$; queda racional en $t$.

**Error típico.** Usar $dt=dx$ (olvidar la derivada de la tangente) o la derivada $\frac{1}{\cos^2}$ sin la regla de la cadena (falta el $2$).

sympy: la derivada de $\frac14\ln(1+\mathrm{sen}^2(2x+1))$ coincide con el integrando; `apart` confirma la descomposición.

---

### E. Trigonométricas

---

### Ejercicio 6.32 (E pp. 238-239)

> Calcula el valor de la integral $\displaystyle\int_0^{\pi/2}\cos^2(2x)\,dx$.

**Antes de calcular**
- **Qué me piden:** una integral definida de un coseno al cuadrado.
- **Cómo lo pienso:** $\cos^2$ no está en la tabla, pero con la fórmula del ángulo doble se convierte en $\frac12+\frac12\cos(\text{algo})$, que sí.
- **Qué uso:** $\cos^2\alpha=\frac{1+\cos2\alpha}2$ (U p. 262); tabla, fila (6) (U p. 248); Barrow (U Teor. 6.2, p. 244).
- **Por dónde empiezo:** aplicar la fórmula con $\alpha=2x$.

1. **Ángulo doble** con $\alpha=2x$: $\cos^2(2x)=\frac{1+\cos(4x)}2$.
2. **Primitiva:** $\int\frac{1+\cos4x}2dx=\frac x2+\frac12\cdot\frac{\mathrm{sen}\,4x}4=\frac x2+\frac{\mathrm{sen}\,4x}8$ (en $\int\cos4x\,dx$ falta la derivada de $4x$: se divide por $4$).
3. **Barrow:**
   $$\int_0^{\pi/2}\cos^2(2x)\,dx=\Big[\frac x2+\frac{\mathrm{sen}\,4x}8\Big]_0^{\pi/2}=\frac\pi4+\frac{\mathrm{sen}\,2\pi}8-0=\frac\pi4.$$
4. **Otra forma (por partes).** $u=\cos2x$, $v'=\cos2x$ ⇒ $u'=-2\,\mathrm{sen}\,2x$, $v=\frac12\mathrm{sen}\,2x$. Como $uv=\frac12\cos2x\,\mathrm{sen}\,2x$ vale $0$ en $0$ y en $\frac\pi2$:
   $$J:=\int_0^{\pi/2}\cos^2(2x)\,dx=\int_0^{\pi/2}\mathrm{sen}^2(2x)\,dx=\int_0^{\pi/2}\big(1-\cos^2(2x)\big)dx=\frac\pi2-J\Rightarrow J=\frac\pi4.$$
   Si se intenta otra vez partes en $\int\mathrm{sen}^2$, se vuelve a $J=J$: hay que usar $\mathrm{sen}^2+\cos^2=1$ para «cerrar el círculo».

**Receta.** Potencias **pares** de $\mathrm{sen}$ y $\cos$: bajar el grado con $\mathrm{sen}^2\alpha=\frac{1-\cos2\alpha}2$, $\cos^2\alpha=\frac{1+\cos2\alpha}2$.

**Error típico.** Escribir $\cos^2(2x)=\frac{1+\cos2x}2$ (el ángulo se duplica: $\cos4x$) u olvidar dividir por $4$ al integrar $\cos4x$.

sympy: $\int_0^{\pi/2}\cos^2(2x)\,dx=\frac\pi4$.

---

### Ejercicio 6.26 (E pp. 232-233)

> Siendo $\displaystyle I=\int\frac{dx}{\mathrm{sen}\,x+\cos x}$, señala la afirmación o afirmaciones correctas:
> a) Para calcular $I$, el cambio más adecuado es $\mathrm{sen}\,x=t$.
> b) Para calcular $I$, el cambio más adecuado es $\mathrm{tg}\frac x2=t$.
> c) $I=-\frac1{\sqrt2}\ln\big\lvert\mathrm{tg}(\frac x2)-1-\sqrt2\big\rvert+\frac1{\sqrt2}\ln\big\lvert\mathrm{tg}(\frac x2)-1+\sqrt2\big\rvert+C$.
> d) Ninguna de las anteriores.

**Antes de calcular**
- **Qué me piden:** elegir el cambio y comprobar una primitiva.
- **Cómo lo pienso:** es una expresión racional en $\mathrm{sen}\,x$ y $\cos x$ sin potencias impares que separar: el cambio general $t=\mathrm{tg}\frac x2$ la convierte en racional. Con $\mathrm{sen}\,x=t$ aparece $\sqrt{1-t^2}$ y se complica.
- **Qué uso:** cambio $t=\mathrm{tg}\frac x2$ (U p. 261); fracciones simples (U p. 255).
- **Por dónde empiezo:** sustituir $\mathrm{sen}\,x=\frac{2t}{1+t^2}$, $\cos x=\frac{1-t^2}{1+t^2}$, $dx=\frac{2dt}{1+t^2}$.

1. **a) no es adecuado.** Con $\mathrm{sen}\,x=t$: $\cos x=\sqrt{1-t^2}$ (donde $\cos x\ge0$) y $dx=\frac{dt}{\sqrt{1-t^2}}$; queda $\int\frac{dt}{t\sqrt{1-t^2}+1-t^2}$, con raíces: no es racional.
2. **b) Cambio $t=\mathrm{tg}\frac x2$:**
   $$\mathrm{sen}\,x+\cos x=\frac{2t+1-t^2}{1+t^2},\qquad I=\int\frac{1+t^2}{-t^2+2t+1}\cdot\frac{2\,dt}{1+t^2}=\int\frac{-2}{t^2-2t-1}dt.$$
   Es racional: **b) es correcta**.
3. **Raíces del denominador:** $t^2-2t-1=0\iff t=\frac{2\pm\sqrt8}2=1\pm\sqrt2$.
4. **Fracciones simples:** $\frac{-2}{(t-1-\sqrt2)(t-1+\sqrt2)}=\frac A{t-1-\sqrt2}+\frac B{t-1+\sqrt2}$; quitando denominadores, $-2=A(t-1+\sqrt2)+B(t-1-\sqrt2)$.
   - $t=1+\sqrt2$: $-2=2\sqrt2A\Rightarrow A=-\frac1{\sqrt2}$.
   - $t=1-\sqrt2$: $-2=-2\sqrt2B\Rightarrow B=\frac1{\sqrt2}$.
5. **Integrar y deshacer el cambio:**
   $$I=-\frac1{\sqrt2}\ln\big\lvert t-1-\sqrt2\big\rvert+\frac1{\sqrt2}\ln\big\lvert t-1+\sqrt2\big\rvert+C,\quad t=\mathrm{tg}\tfrac x2.$$
   Coincide con c): **c) es correcta**.
6. **Respuesta: b) y c).**

**Receta.** Expresión racional en $\mathrm{sen}\,x$ y $\cos x$: cambio $t=\mathrm{tg}\frac x2$ con $\mathrm{sen}\,x=\frac{2t}{1+t^2}$, $\cos x=\frac{1-t^2}{1+t^2}$, $dx=\frac{2dt}{1+t^2}$; simplificar los $1+t^2$ y resolver la racional.

**Error típico.** Olvidar el $dx=\frac{2dt}{1+t^2}$ (y con él el $2$ del numerador), o simplificar mal $\frac{2t}{1+t^2}+\frac{1-t^2}{1+t^2}$.

sympy: la derivada de la primitiva de c) coincide con $\frac1{\mathrm{sen}\,x+\cos x}$ en $x=\frac12,\frac15,1$.

---

### F. Integrales definidas y áreas

---

### Ejercicio 6.33 (E pp. 239-240)

> Calcula el área comprendida entre la gráfica de $e^{2x}$; las rectas $x=1$, $x=2$; y el eje $x$.

**Antes de calcular**
- **Qué me piden:** el área bajo $e^{2x}$ en $[1,2]$.
- **Cómo lo pienso:** $e^{2x}>0$ siempre, así que el área es directamente la integral.
- **Qué uso:** área = integral si $f\ge0$ (U §6.1, p. 238); tabla, fila (4) (U p. 248); Barrow (U Teor. 6.2, p. 244).
- **Por dónde empiezo:** primitiva de $e^{2x}$.

1. **Signo:** $e^{2x}>0$ ⇒ área $=\int_1^2e^{2x}dx$.
2. **Primitiva:** $\int e^{2x}dx=\frac12\int e^{2x}\cdot2\,dx=\frac{e^{2x}}2$ (fila (4) ajustando el $2$).
3. **Barrow:** $\Big[\frac{e^{2x}}2\Big]_1^2=\frac{e^4-e^2}2\approx23{,}6$.

**Receta.** Área bajo $f\ge0$: $\int_a^bf$. Para $e^{kx}$, primitiva $\frac{e^{kx}}k$.

**Error típico.** Escribir $e^{2x}$ como primitiva (olvidar dividir por $2$).

sympy: $\frac{e^4}2-\frac{e^2}2$.

---

### Ejercicio 6.34 (E pp. 240-241)

> Sean $f(x)=x^2$, $g(x)=x^3$ y $h(x)=\sqrt x$. Señala la respuesta correcta:
> a) El área encerrada por las gráficas de $f$ y $g$ es mayor que la encerrada por las gráficas de $f$ y $h$.
> b) El área encerrada por las gráficas de $h$ y $g$ es mayor que la encerrada por las gráficas de $f$ y $h$.
> c) El área encerrada por las gráficas de $f$ y $g$ es igual que la encerrada por las gráficas de $f$ y $h$.
> d) Ninguna de las anteriores.

**Antes de calcular**
- **Qué me piden:** comparar tres áreas entre pares de curvas.
- **Cómo lo pienso:** primero dónde se cortan (eso da los límites), luego cuál está encima (eso da el orden de la resta). Las tres pasan por $(0,0)$ y $(1,1)$.
- **Qué uso:** área entre gráficas $\int_a^b(\text{arriba}-\text{abajo})$ (U §6.1, p. 238); Barrow (U Teor. 6.2, p. 244).
- **Por dónde empiezo:** resolver $x^2=x^3$, $x^2=\sqrt x$, $x^3=\sqrt x$.

1. **Cortes** (dominio de $h$: $x\ge0$):
   - $x^2=x^3\iff x^2(1-x)=0\iff x=0,1$.
   - $x^2=\sqrt x\iff x^4=x\iff x(x^3-1)=0\iff x=0,1$.
   - $x^3=\sqrt x\iff x^6=x\iff x=0,1$.
   Cada par encierra una región sobre $[0,1]$.
2. **Orden en $[0,1]$** (probar $x=\frac14$): $g=\frac1{64}$, $f=\frac1{16}$, $h=\frac12$. Así $g\le f\le h$ en $[0,1]$.
3. **Áreas** (primitivas de potencias, $\sqrt x=x^{1/2}\to\frac23x^{3/2}$):
   - $f$ y $g$: $\int_0^1(x^2-x^3)dx=\frac13-\frac14=\frac1{12}$.
   - $f$ y $h$: $\int_0^1(\sqrt x-x^2)dx=\frac23-\frac13=\frac13$.
   - $h$ y $g$: $\int_0^1(\sqrt x-x^3)dx=\frac23-\frac14=\frac5{12}$.
4. **Comparar:** a) $\frac1{12}>\frac13$ falso; b) $\frac5{12}>\frac13=\frac4{12}$ **verdadero**; c) falso. **Respuesta: b).**

**Receta.** Área entre curvas: (1) cortes; (2) cuál va arriba (probar un punto); (3) $\int(\text{arriba}-\text{abajo})$.

**Error típico.** Restar al revés y obtener un área negativa, o creer que $x^2\ge x^3$ «siempre» (solo en $[0,1]$; para $x>1$ es al revés).

sympy: $\frac1{12}$, $\frac13$, $\frac5{12}$.

---

### Ejercicio 6.35 (E pp. 241-242)

> ¿Qué área encierran las gráficas de $f(x)=\cos(\pi x)$ y $g(x)=\mathrm{sen}(\pi x)$ entre $x=-1$ y $x=1$?
> a) $4\frac{\sqrt2}\pi$. b) $3\frac{\sqrt2}\pi$. c) $2\frac{\sqrt2}\pi$. d) $0$.

**Antes de calcular**
- **Qué me piden:** el área total entre dos curvas que se cruzan dentro del intervalo.
- **Cómo lo pienso:** donde se cruzan, cambia cuál está arriba. Hay que partir $[-1,1]$ en los cruces, integrar $f-g$ en cada trozo y sumar los **valores absolutos** (si no, las áreas se cancelan, como sugiere la opción d)).
- **Qué uso:** aditividad de la integral (U p. 240); área $=\int\lvert f-g\rvert$ (U §6.1, p. 238); Barrow (U Teor. 6.2, p. 244).
- **Por dónde empiezo:** resolver $\cos\pi x=\mathrm{sen}\,\pi x$.

1. **Cortes.** Si $\cos\pi x=0$, entonces $\mathrm{sen}\,\pi x=\pm1\ne0$: no hay corte. Si $\cos\pi x\ne0$, dividir: $\mathrm{tg}\,\pi x=1\iff\pi x=\frac\pi4+k\pi\iff x=\frac14+k$. En $[-1,1]$: $x=-\frac34$ y $x=\frac14$.
2. **Primitiva de $f-g$:** $\int(\cos\pi x-\mathrm{sen}\,\pi x)dx=\frac{\mathrm{sen}\,\pi x+\cos\pi x}\pi=:F(x)$ (filas (6) y (7), dividiendo por $\pi$).
3. **Valores:** $F(-1)=\frac{0-1}\pi=-\frac1\pi$; $F(-\frac34)=\frac{-\frac{\sqrt2}2-\frac{\sqrt2}2}\pi=-\frac{\sqrt2}\pi$; $F(\frac14)=\frac{\sqrt2}\pi$; $F(1)=-\frac1\pi$.
4. **Integral en cada trozo:**
   - $[-1,-\frac34]$: $F(-\frac34)-F(-1)=\frac{1-\sqrt2}\pi$ (negativo: ahí $g$ va arriba) ⇒ área $\frac{\sqrt2-1}\pi$.
   - $[-\frac34,\frac14]$: $\frac{2\sqrt2}\pi$ ⇒ área $\frac{2\sqrt2}\pi$.
   - $[\frac14,1]$: $F(1)-F(\frac14)=\frac{-1-\sqrt2}\pi$ ⇒ área $\frac{1+\sqrt2}\pi$.
5. **Sumar:** $\frac{\sqrt2-1+2\sqrt2+1+\sqrt2}\pi=\frac{4\sqrt2}\pi\approx1{,}80$. **Respuesta: a).**
6. **Por qué d) es una trampa:** $\int_{-1}^1(f-g)\,dx=F(1)-F(-1)=0$ (áreas con signo que se cancelan), pero el área no es $0$.

**Receta.** Área entre curvas que se cruzan: partir en los cortes, integrar $f-g$ en cada trozo y sumar valores absolutos.

**Error típico.** Integrar $f-g$ en todo $[-1,1]$ sin partir (sale $0$).

sympy: trozos $\frac{1-\sqrt2}\pi$, $\frac{2\sqrt2}\pi$, $\frac{-1-\sqrt2}\pi$; $\int_{-1}^1\lvert f-g\rvert=\frac{4\sqrt2}\pi\approx1{,}8006$.

---

## 2. Así lo preguntan en el examen (X)

Ordenados por técnica: división (p. 11) → cambio (p. 38) → fracciones simples (pp. 93-94) → cambio + partes (p. 81) → partes en definida (pp. 19-20) → cambio en definida + partes (p. 128) → $\mathrm{sen}^n\cos^m$ (p. 141) → raíz con $x=t^2$ (p. 143) → $\mathrm{tg}\frac x2$ (p. 148) → cambio + partes + fracciones en definida (p. 6). Los apartados de trapecio, Simpson o integrales impropias de esas mismas preguntas son de U §6.4 y §6.5 y se omiten aquí.

---

### X p. 11 (Febrero 2011, 1ª semana, Ingeniería Mecánica, Modelo A, Ejercicio 5)

> Calcule la siguiente integral $\displaystyle\int\frac{x^6}{x^2+1}\,dx$.

**Antes de calcular**
- **Qué me piden:** una primitiva de una racional.
- **Cómo lo pienso:** grado $6\ge2$: hay que dividir. El resto será una constante entre $x^2+1$, que es un arcotangente.
- **Qué uso:** división previa en racionales (U p. 255); tabla, fila (9) (U p. 248).
- **Por dónde empiezo:** dividir $x^6$ entre $x^2+1$.

1. **Dividir.** $x^6=(x^2+1)(x^4-x^2+1)-1$ (comprobación: $(x^2+1)(x^4-x^2+1)=x^6+1$). Por tanto
   $$\frac{x^6}{x^2+1}=x^4-x^2+1-\frac1{x^2+1}.$$
2. **Integrar término a término:**
   $$\int\frac{x^6}{x^2+1}dx=\frac{x^5}5-\frac{x^3}3+x-\mathrm{arctg}\,x+C.$$
3. **Comprobación:** derivando sale $x^4-x^2+1-\frac1{1+x^2}=\frac{x^6}{x^2+1}$ ✓.

**Receta.** Racional con grado del numerador ≥ grado del denominador: dividir primero. Truco para $\frac{x^{2n}}{x^2+1}$: $x^{2n}\pm1$ es divisible por $x^2+1$.

**Error típico.** Olvidar el resto ($-\frac1{x^2+1}$), que es lo que produce el $-\mathrm{arctg}\,x$.

sympy: `div(x**6, x**2+1)` = $(x^4-x^2+1,\,-1)$; derivada ✓.

---

### X p. 38 (Septiembre 2013, Grados en Ing. Mecánica y Electrónica y Automática, Modelo A, Problema 5)

> Calcúlese la siguiente integral $\displaystyle I=\int x^5\sqrt[3]{(1+x^3)^2}\,dx$.

**Antes de calcular**
- **Qué me piden:** una primitiva.
- **Cómo lo pienso:** lo molesto es $1+x^3$, y su derivada $3x^2$ está «dentro» de $x^5=x^3\cdot x^2$. Con $u=1+x^3$, el $x^2dx$ es $\frac{du}3$ y el $x^3$ sobrante es $u-1$.
- **Qué uso:** cambio de variable (U pp. 249-250, consejo de p. 250); potencias (tabla, fila (2), U p. 248).
- **Por dónde empiezo:** $u=1+x^3$.

1. **Cambio:** $u=1+x^3\Rightarrow du=3x^2dx\Rightarrow x^2dx=\frac{du}3$; además $x^3=u-1$.
2. **Reescribir:** $x^5\sqrt[3]{(1+x^3)^2}\,dx=x^3\cdot u^{2/3}\cdot x^2dx=(u-1)\,u^{2/3}\frac{du}3$.
3. **Integrar:**
   $$I=\frac13\int\big(u^{5/3}-u^{2/3}\big)du=\frac13\Big(\frac{3}{8}u^{8/3}-\frac35u^{5/3}\Big)+K=\frac{u^{8/3}}8-\frac{u^{5/3}}5+K.$$
4. **Deshacer el cambio:**
   $$I=\frac18(1+x^3)^{8/3}-\frac15(1+x^3)^{5/3}+K=\frac18(1+x^3)^2\sqrt[3]{(1+x^3)^2}-\frac15(1+x^3)\sqrt[3]{(1+x^3)^2}+K.$$
5. (El cambio $1+x^3=t^3$ también funciona y da lo mismo.)

**Receta.** Si aparece $g(x)$ dentro de una raíz y fuera hay $g'(x)$ por una potencia de $x$, cambio $u=g(x)$ y escribir la $x$ que sobra en función de $u$.

**Error típico.** Quedarse con $x^3$ en la integral en $u$ (mezclar variables): todo debe quedar en $u$.

sympy: la derivada de $\frac18(1+x^3)^{8/3}-\frac15(1+x^3)^{5/3}$ coincide con el integrando.

---

### X pp. 93-94 (Febrero 2018, Modelo B, Grado en Ingeniería Mecánica, Ejercicio 5 a)

> Sea $f$ la función dada por $f(x)=\dfrac{2}{x(x+2)}$. (a) Obtenga una primitiva de $f(x)$, es decir, calcule $\displaystyle\int f(x)\,dx=\int\frac{2}{x(x+2)}\,dx$.

**Antes de calcular**
- **Qué me piden:** una primitiva.
- **Cómo lo pienso:** denominador ya factorizado, dos raíces reales simples ($0$ y $-2$): dos fracciones, dos logaritmos.
- **Qué uso:** fracciones simples (U p. 255) e $\int\frac{A}{x-a}=A\ln\lvert x-a\rvert$ (U p. 257).
- **Por dónde empiezo:** $\frac2{x(x+2)}=\frac Ax+\frac B{x+2}$.

1. **Planteamiento:** $2=A(x+2)+Bx$.
2. **Valores:** $x=0$: $2=2A\Rightarrow A=1$; $x=-2$: $2=-2B\Rightarrow B=-1$.
3. **Integrar:**
   $$\int\frac{2\,dx}{x(x+2)}=\ln\lvert x\rvert-\ln\lvert x+2\rvert+C=\ln\Big\lvert\frac{x}{x+2}\Big\rvert+C.$$
4. **Comprobación:** $\frac1x-\frac1{x+2}=\frac{x+2-x}{x(x+2)}=\frac2{x(x+2)}$ ✓.

**Receta.** Raíces reales simples ⇒ una fracción $\frac{A}{x-a}$ por raíz; cada coeficiente sale sustituyendo su raíz.

**Error típico.** Escribir $\ln x-\ln(x+2)$ sin valor absoluto: la función está definida también para $x<-2$ y $-2<x<0$.

sympy: derivada ✓.

---

### X p. 81 (Febrero 2017, Modelo B, Grado en Ingeniería Mecánica, Pregunta corta 2)

> Calcule la integral: $\displaystyle\int x^3e^{x^2}\,dx$.

**Antes de calcular**
- **Qué me piden:** una primitiva.
- **Cómo lo pienso:** $e^{x^2}$ no tiene primitiva elemental, pero $xe^{x^2}$ sí ($\frac12e^{x^2}$). Así que parto $x^3e^{x^2}=x^2\cdot xe^{x^2}$ y uso partes con $v'=xe^{x^2}$.
- **Qué uso:** integración por partes (U p. 252); tabla, fila (4) (U p. 248).
- **Por dónde empiezo:** $u=x^2$, $v'=xe^{x^2}$.

1. **Elección:** $u=x^2\Rightarrow u'=2x$; $v'=xe^{x^2}\Rightarrow v=\frac12\int2xe^{x^2}dx=\frac12e^{x^2}$.
2. **Partes:**
   $$\int x^3e^{x^2}dx=\frac{x^2}2e^{x^2}-\int2x\cdot\frac12e^{x^2}dx=\frac{x^2}2e^{x^2}-\int xe^{x^2}dx.$$
3. **La nueva integral** es la misma de antes: $\int xe^{x^2}dx=\frac12e^{x^2}$.
4. **Resultado:** $\int x^3e^{x^2}dx=\frac12(x^2-1)e^{x^2}+C$.
5. **Otra vía:** cambio $t=x^2$, $dt=2x\,dx$: $\int x^3e^{x^2}dx=\frac12\int te^t\,dt=\frac12(t-1)e^t$ (E 6.18). Mismo resultado.

**Receta.** En partes, $v'$ debe ser algo que se sepa integrar: si $e^{x^2}$ sola no se integra, se le «presta» un $x$ del polinomio.

**Error típico.** Tomar $v'=e^{x^2}$ (no tiene primitiva elemental) o $u=x^3$, $v'=e^{x^2}$.

sympy: $\frac{d}{dx}\frac12(x^2-1)e^{x^2}=x^3e^{x^2}$ ✓.

---

### X pp. 19-20 (Febrero 2012, 1ª semana, Ingeniería Mecánica, Modelo A, Pregunta corta 3)

> Calcule $\displaystyle\int_{-2}^0(3+4x)\,e^{-x}\,dx$.

**Antes de calcular**
- **Qué me piden:** el valor de una integral definida.
- **Cómo lo pienso:** polinomio × exponencial: partes con $u=3+4x$. Se puede aplicar la fórmula de partes directamente con límites.
- **Qué uso:** partes en la definida (U p. 254); Barrow (U Teor. 6.2, p. 244).
- **Por dónde empiezo:** $u=3+4x$, $v'=e^{-x}$.

1. **Continuidad:** el integrando es continuo en $[-2,0]$.
2. **Elección:** $u=3+4x\Rightarrow u'=4$; $v'=e^{-x}\Rightarrow v=-e^{-x}$ (la derivada de $-x$ es $-1$).
3. **Partes en la definida:**
   $$\int_{-2}^0(3+4x)e^{-x}dx=\Big[-(3+4x)e^{-x}\Big]_{-2}^0+\int_{-2}^04e^{-x}dx=\Big[-(3+4x)e^{-x}-4e^{-x}\Big]_{-2}^0=\Big[-(7+4x)e^{-x}\Big]_{-2}^0.$$
4. **Evaluar:** en $0$: $-7$; en $-2$: $-(7-8)e^{2}=e^2$. Resultado: $-7-e^2\approx-14{,}39$.
5. **Comprobación de signo:** en $[-2,0]$, $3+4x$ es negativo en la mayor parte del intervalo (para $x<-\frac34$) y ahí $e^{-x}$ es grande: un resultado negativo es razonable.

**Receta.** Partes en definida: $\int_a^buv'=[uv]_a^b-\int_a^bu'v$; conviene juntar todo en una primitiva y evaluar una sola vez.

**Error típico.** Primitiva de $e^{-x}$ escrita como $e^{-x}$ (falta el signo menos), o errores de signo al evaluar $e^{-(-2)}=e^2$.

sympy: $\int_{-2}^0(3+4x)e^{-x}dx=-e^2-7$.

---

### X p. 128 (Ing. Electrónica Industrial y Automática, examen A, sin fecha, Ejercicio 6)

> Muestre que el cambio $t=\sqrt x$ transforma el integral $\displaystyle\int_0^{\pi^2}\mathrm{sen}\sqrt x\,dx$ en $\displaystyle\int_0^\pi2t\,\mathrm{sen}\,t\,dt$. Calcule $\displaystyle\int_0^\pi2t\,\mathrm{sen}\,t\,dt$.

**Antes de calcular**
- **Qué me piden:** justificar un cambio de variable en una definida (incluidos los límites) y calcular la nueva integral.
- **Cómo lo pienso:** con $t=\sqrt x$ es $x=t^2$, $dx=2t\,dt$, y los límites $0$, $\pi^2$ pasan a $0$, $\pi$. La nueva integral es polinomio × seno: partes.
- **Qué uso:** cambio de variable en la definida (U p. 251, Ej. 6.17); partes en la definida (U p. 254, Ej. 6.22).
- **Por dónde empiezo:** escribir $x=g(t)=t^2$.

1. **Hipótesis del cambio.** $x=g(t)=t^2$ es continua con derivada $g'(t)=2t$ continua en $[0,\pi]$ (no nula salvo en el extremo $t=0$, lo que no afecta), $g(0)=0$ y $g(\pi)=\pi^2$; $\mathrm{sen}\sqrt x$ es continua en $[0,\pi^2]$.
2. **Cambio:** $\mathrm{sen}\sqrt x=\mathrm{sen}\,t$, $dx=2t\,dt$; **límites:** $x=0\Rightarrow t=0$, $x=\pi^2\Rightarrow t=\pi$:
   $$\int_0^{\pi^2}\mathrm{sen}\sqrt x\,dx=\int_0^\pi\mathrm{sen}\,t\cdot2t\,dt=\int_0^\pi2t\,\mathrm{sen}\,t\,dt.$$
3. **Partes:** $u=t\Rightarrow u'=1$; $v'=\mathrm{sen}\,t\Rightarrow v=-\cos t$:
   $$\int_0^\pi2t\,\mathrm{sen}\,t\,dt=2\Big([-t\cos t]_0^\pi+\int_0^\pi\cos t\,dt\Big)=2\big(-\pi\cos\pi+0+[\mathrm{sen}\,t]_0^\pi\big)=2(\pi+0)=2\pi.$$

**Receta.** Cambio en definida: (1) $x=g(t)$ y $dx=g'(t)dt$; (2) **límites nuevos** $t=g^{-1}(a)$, $t=g^{-1}(b)$; (3) integrar en $t$ y evaluar en los límites nuevos, sin volver a $x$.

**Error típico.** Dejar los límites $0$ y $\pi^2$ en la integral en $t$ (daría un valor distinto).

sympy: $\int_0^{\pi^2}\mathrm{sen}\sqrt x\,dx=\int_0^\pi2t\,\mathrm{sen}\,t\,dt=2\pi$.

---

### X p. 141 (Febrero 2018, 2ª semana, Ing. Electrónica Industrial y Automática, Ejercicio 5, primer apartado)

> Dada la integral $\displaystyle\int_0^{\pi/2}(\mathrm{sen}^4x)(\cos^3x)\,dx$: Calcule el valor exacto encontrando una primitiva del integrando. (El segundo apartado, con la regla de Simpson, es de U §6.4.)

**Antes de calcular**
- **Qué me piden:** el valor exacto con Barrow.
- **Cómo lo pienso:** el exponente del coseno es **impar**: separo un $\cos x$ (que será la derivada de $\mathrm{sen}\,x$) y el $\cos^2x$ restante lo paso a senos. Queda un polinomio en $\mathrm{sen}\,x$ por $\cos x$: inmediata.
- **Qué uso:** $\mathrm{sen}^nx\cos^mx$ con exponente impar (U p. 263); tabla, fila (2) (U p. 248); Barrow (U Teor. 6.2, p. 244).
- **Por dónde empiezo:** $\cos^3x=\cos^2x\cdot\cos x=(1-\mathrm{sen}^2x)\cos x$.

1. **Reescribir:** $\mathrm{sen}^4x\cos^3x=\mathrm{sen}^4x(1-\mathrm{sen}^2x)\cos x=\mathrm{sen}^4x\cos x-\mathrm{sen}^6x\cos x$.
2. **Primitiva** (potencia de $\mathrm{sen}\,x$ por su derivada): $F(x)=\frac{\mathrm{sen}^5x}5-\frac{\mathrm{sen}^7x}7$.
   (Equivale al cambio $t=\mathrm{sen}\,x$: $\int(t^4-t^6)dt$.)
3. **Barrow:** $F(\frac\pi2)-F(0)=\frac15-\frac17-0=\frac2{35}\approx0{,}0571$.

**Receta.** $\mathrm{sen}^nx\cos^mx$ con $m$ impar: separar un $\cos x$, $\cos^2x=1-\mathrm{sen}^2x$, y queda polinomio en $\mathrm{sen}\,x$ por $\cos x$ (si el impar es $n$, lo mismo intercambiando papeles, con un signo menos).

**Error típico.** Intentar el ángulo doble (útil solo si los dos exponentes son pares) o perder el factor $\cos x$ al pasar a senos.

sympy: $\int_0^{\pi/2}\mathrm{sen}^4x\cos^3x\,dx=\frac2{35}$.

---

### X p. 143 (Septiembre 2018, Ing. Electrónica Industrial y Automática, Ejercicio 5, primer apartado)

> Calcule la integral $\displaystyle\int\frac{x}{1+\sqrt x}\,dx$. (El segundo apartado, con la fórmula del trapecio, es de U §6.4.)

**Antes de calcular**
- **Qué me piden:** una primitiva.
- **Cómo lo pienso:** la raíz estorba: con $x=t^2$ ($t=\sqrt x$) desaparece y queda una racional en $t$, que se divide.
- **Qué uso:** cambio de variable (U pp. 249-250); división en racionales (U p. 255).
- **Por dónde empiezo:** $x=t^2$, $dx=2t\,dt$, con $t=\sqrt x\ge0$.

1. **Cambio:** $\int\frac{x}{1+\sqrt x}dx=\int\frac{t^2}{1+t}\,2t\,dt=2\int\frac{t^3}{1+t}dt$.
2. **Dividir** ($3\ge1$): $t^3=(t+1)(t^2-t+1)-1$, así que $\frac{t^3}{1+t}=t^2-t+1-\frac1{1+t}$.
3. **Integrar:** $2\Big(\frac{t^3}3-\frac{t^2}2+t-\ln(1+t)\Big)+C$ (aquí $1+t>0$, el valor absoluto no hace falta).
4. **Deshacer el cambio:**
   $$\int\frac{x}{1+\sqrt x}dx=2\Big(\frac{x^{3/2}}3-\frac x2+\sqrt x-\ln(1+\sqrt x)\Big)+C.$$

**Receta.** Una sola raíz $\sqrt x$: cambio $x=t^2$; si sale racional con grado num ≥ grado den, dividir.

**Error típico.** Olvidar el $2t$ de $dx$ (saldría $\int\frac{t^2}{1+t}dt$).

sympy: la derivada coincide con $\frac{x}{1+\sqrt x}$; `div(t**3, 1+t)` = $(t^2-t+1,\,-1)$.

---

### X p. 148 (Febrero 2019, 2ª semana, Ing. Electrónica Industrial y Automática, Ejercicio 5)

> Calcule la integral $\displaystyle\int\frac{dx}{4+5\cos x}$. *Pista:* use el cambio de variable $t=\tan\big(\frac x2\big)$, $\mathrm{sen}\,x=\frac{2t}{1+t^2}$, $\cos x=\frac{1-t^2}{1+t^2}$.

**Antes de calcular**
- **Qué me piden:** una primitiva con el cambio $t=\mathrm{tg}\frac x2$.
- **Cómo lo pienso:** sustituir $\cos x$ y $dx$; los $1+t^2$ se simplifican y queda $\frac{2}{9-t^2}$, racional con dos raíces reales ($\pm3$).
- **Qué uso:** cambio $t=\mathrm{tg}\frac x2$, $dx=\frac{2dt}{1+t^2}$ (U p. 261); fracciones simples (U p. 255).
- **Por dónde empiezo:** calcular $4+5\cos x$ en función de $t$.

1. **$dx$:** de $x=2\,\mathrm{arctg}\,t$, $dx=\frac{2\,dt}{1+t^2}$.
2. **Denominador:** $4+5\frac{1-t^2}{1+t^2}=\frac{4+4t^2+5-5t^2}{1+t^2}=\frac{9-t^2}{1+t^2}$.
3. **Integral en $t$:** $\int\frac{1+t^2}{9-t^2}\cdot\frac{2\,dt}{1+t^2}=\int\frac{2}{9-t^2}dt$.
4. **Fracciones simples:** $9-t^2=(3-t)(3+t)$; $\frac2{9-t^2}=\frac A{3+t}+\frac B{3-t}$, $2=A(3-t)+B(3+t)$. Con $t=3$: $B=\frac13$; con $t=-3$: $A=\frac13$.
5. **Integrar** (ojo: $\int\frac{dt}{3-t}=-\ln\lvert3-t\rvert$, por el signo de la derivada de $3-t$):
   $$\int\frac{2\,dt}{9-t^2}=\frac13\ln\lvert3+t\rvert-\frac13\ln\lvert3-t\rvert+C=\frac13\ln\Big\lvert\frac{3+t}{3-t}\Big\rvert+C.$$
6. **Deshacer el cambio:**
   $$\int\frac{dx}{4+5\cos x}=\frac13\ln\left\lvert\frac{3+\mathrm{tg}\frac x2}{3-\mathrm{tg}\frac x2}\right\rvert+C.$$

**Receta.** La de E 6.26: $t=\mathrm{tg}\frac x2$, simplificar los $1+t^2$, fracciones simples y deshacer el cambio.

**Error típico.** $\int\frac{dt}{3-t}=+\ln\lvert3-t\rvert$ (falta el signo menos).

sympy: la derivada de la primitiva coincide con $\frac1{4+5\cos x}$ en $x=\frac13,1,\frac52$.

---

### X p. 6 (Febrero 2010, 2ª semana, Ingeniería Eléctrica, Ejercicio 6)

> (3 PUNTOS) Calcule la siguiente integral definida $\displaystyle I=\int_0^1e^{-2x}\ln\big(1+e^{2x}\big)\,dx$.
> *Sugerencia:* Aplique el cambio de variable $e^{2x}=t$ y después utilice integración por partes.

**Antes de calcular**
- **Qué me piden:** el valor de una definida que combina tres técnicas.
- **Cómo lo pienso:** con $t=e^{2x}$ todo se expresa en $t$ ($e^{-2x}=\frac1t$, $dx=\frac{dt}{2t}$) y queda $\int\frac{\ln(1+t)}{t^2}$: logaritmo × potencia, partes con $u=\ln(1+t)$. La integral que sale, $\int\frac{dt}{t(1+t)}$, se hace con fracciones simples.
- **Qué uso:** cambio en la definida (U p. 251); partes en la definida (U p. 254); fracciones simples (U p. 255); Barrow (U Teor. 6.2, p. 244).
- **Por dónde empiezo:** $t=e^{2x}$, límites nuevos.

1. **Cambio:** $t=e^{2x}\Rightarrow dt=2e^{2x}dx=2t\,dx\Rightarrow dx=\frac{dt}{2t}$; $e^{-2x}=\frac1t$. **Límites:** $x=0\Rightarrow t=1$; $x=1\Rightarrow t=e^2$.
   $$I=\int_1^{e^2}\frac1t\ln(1+t)\frac{dt}{2t}=\frac12\int_1^{e^2}\frac{\ln(1+t)}{t^2}dt.$$
2. **Partes:** $u=\ln(1+t)\Rightarrow u'=\frac1{1+t}$; $v'=t^{-2}\Rightarrow v=-\frac1t$:
   $$\int_1^{e^2}\frac{\ln(1+t)}{t^2}dt=\Big[-\frac{\ln(1+t)}t\Big]_1^{e^2}+\int_1^{e^2}\frac{dt}{t(1+t)}.$$
3. **Fracciones simples:** $\frac1{t(1+t)}=\frac1t-\frac1{1+t}$ (con $t=0$: $A=1$; con $t=-1$: $B=-1$). Primitiva: $\ln t-\ln(1+t)=\ln\frac t{1+t}$ ($t>0$).
4. **Evaluar:**
   - $\Big[-\frac{\ln(1+t)}t\Big]_1^{e^2}=-e^{-2}\ln(1+e^2)+\ln2$.
   - $\Big[\ln\frac t{1+t}\Big]_1^{e^2}=\ln\frac{e^2}{1+e^2}-\ln\frac12=2-\ln(1+e^2)+\ln2$.
5. **Sumar y multiplicar por $\frac12$:**
   $$I=\frac12\Big[2\ln2+2-(1+e^{-2})\ln(1+e^2)\Big]=1+\ln2-\frac12\big(1+e^{-2}\big)\ln(1+e^2)\approx0{,}4858.$$
   Escrito de otra forma: $I=\ln2-\frac12e^{-2}\ln(1+e^2)+\frac12\ln\frac{e^2}{e^2+1}$ (es el mismo número, porque $\frac12\ln\frac{e^2}{e^2+1}=1-\frac12\ln(1+e^2)$).

**Receta.** Integral con $e^{kx}$ en varios sitios: $t=e^{kx}$, $dx=\frac{dt}{kt}$, cambiar límites; luego la técnica que pida la integral en $t$ (aquí $\ln$ × potencia ⇒ partes con $u=\ln$).

**Error típico.** Olvidar el $\frac1{2t}$ de $dx$ o los límites nuevos ($1$ y $e^2$, no $0$ y $1$).

sympy: $\int_0^1e^{-2x}\ln(1+e^{2x})dx\approx0{,}485759$, igual que la fórmula; $\frac{d}{dt}\Big(-\frac{\ln(1+t)}t+\ln t-\ln(1+t)\Big)=\frac{\ln(1+t)}{t^2}$ ✓.

---

## 3. Ejemplos propios (dificultad creciente)

### Propio 1 — Partes reiterada (fácil-medio) [propio]

> Calcula $\displaystyle\int x^2\cos x\,dx$ y, con ella, $\displaystyle\int_0^{\pi/2}x^2\cos x\,dx$.

**Antes de calcular**
- **Qué me piden:** una primitiva y una definida.
- **Cómo lo pienso:** polinomio de grado 2 × coseno: cada vez que se aplica partes con $u$ = polinomio, el grado baja en 1. Hacen falta dos pasadas.
- **Qué uso:** partes reiterada (U p. 252, Ej. 6.19); Barrow (U Teor. 6.2, p. 244).
- **Por dónde empiezo:** $u=x^2$, $v'=\cos x$.

1. **1ª pasada:** $u=x^2$, $u'=2x$; $v'=\cos x$, $v=\mathrm{sen}\,x$:
   $\int x^2\cos x\,dx=x^2\mathrm{sen}\,x-\int2x\,\mathrm{sen}\,x\,dx$.
2. **2ª pasada** en $\int2x\,\mathrm{sen}\,x\,dx$: $u=2x$, $u'=2$; $v'=\mathrm{sen}\,x$, $v=-\cos x$:
   $\int2x\,\mathrm{sen}\,x\,dx=-2x\cos x+\int2\cos x\,dx=-2x\cos x+2\,\mathrm{sen}\,x$.
3. **Juntar** (¡el signo menos delante afecta a todo!):
   $$\int x^2\cos x\,dx=x^2\mathrm{sen}\,x+2x\cos x-2\,\mathrm{sen}\,x+C.$$
4. **Comprobar derivando:** $2x\,\mathrm{sen}\,x+x^2\cos x+2\cos x-2x\,\mathrm{sen}\,x-2\cos x=x^2\cos x$ ✓.
5. **Definida:** en $\frac\pi2$: $\frac{\pi^2}4\cdot1+0-2=\frac{\pi^2}4-2$; en $0$: $0$. Resultado $\frac{\pi^2}4-2\approx0{,}467$.

**Receta.** Polinomio de grado $n$ × $\mathrm{sen}$/$\cos$/$e^x$: $n$ pasadas de partes con $u$ = polinomio. Cuidado con los signos al encadenar.

**Error típico.** No distribuir el signo menos de la 1ª pasada sobre el resultado de la 2ª.

sympy: derivada ✓; $\int_0^{\pi/2}x^2\cos x\,dx=\frac{\pi^2}4-2$.

---

### Propio 2 — Fracciones simples con un factor irreducible (medio) [propio]

> Calcula $\displaystyle\int\frac{3x+5}{(x-1)(x^2+2x+5)}\,dx$.

**Antes de calcular**
- **Qué me piden:** una primitiva de una racional (grado $1<3$).
- **Cómo lo pienso:** $x^2+2x+5$ tiene discriminante $4-20<0$: es irreducible. Fracciones: $\frac{A}{x-1}+\frac{Bx+C}{x^2+2x+5}$. El trozo irreducible dará $\ln$ + $\mathrm{arctg}$.
- **Qué uso:** fracciones simples (U p. 255); $\ln$+$\mathrm{arctg}$ (U p. 258, Ej. 6.24); completar cuadrados.
- **Por dónde empiezo:** quitar denominadores y dar $x=1$.

1. **Planteamiento:** $3x+5=A(x^2+2x+5)+(Bx+C)(x-1)$.
2. **$x=1$:** $8=8A\Rightarrow A=1$.
3. **Coeficientes:** $x^2$: $0=A+B\Rightarrow B=-1$; término independiente: $5=5A-C\Rightarrow C=0$.
   $$\frac{3x+5}{(x-1)(x^2+2x+5)}=\frac1{x-1}-\frac{x}{x^2+2x+5}.$$
4. **Trozo irreducible.** Derivada del denominador: $2x+2$. Escribir $x=\frac12(2x+2)-1$:
   $$\int\frac{x\,dx}{x^2+2x+5}=\frac12\ln(x^2+2x+5)-\int\frac{dx}{(x+1)^2+4}.$$
5. **Completar cuadrados:** $x^2+2x+5=(x+1)^2+4=4\Big[\big(\tfrac{x+1}2\big)^2+1\Big]$, y $\int\frac{dx}{(x+1)^2+4}=\frac14\cdot2\int\frac{\frac12\,dx}{(\frac{x+1}2)^2+1}=\frac12\mathrm{arctg}\frac{x+1}2$.
6. **Resultado:**
   $$\int\frac{3x+5}{(x-1)(x^2+2x+5)}dx=\ln\lvert x-1\rvert-\frac12\ln(x^2+2x+5)+\frac12\mathrm{arctg}\frac{x+1}2+C.$$

**Receta.** Factor irreducible $x^2+bx+c$: numerador $Bx+C$; separar la parte proporcional a $2x+b$ ($\ln$) y completar cuadrados en el resto ($\mathrm{arctg}$).

**Error típico.** Poner solo una constante $\frac{C}{x^2+2x+5}$ (falta el $Bx$) o perder el signo del $-1$ al ajustar el numerador.

sympy: `apart` da $\frac1{x-1}-\frac x{x^2+2x+5}$; derivada de la primitiva ✓.

---

### Propio 3 — Cambio de variable en una definida, cambiando los límites (medio) [propio]

> Calcula $\displaystyle\int_0^3\frac{x}{\sqrt{x+1}}\,dx$ con el cambio $t=\sqrt{x+1}$.

**Antes de calcular**
- **Qué me piden:** una definida con un cambio que quita la raíz.
- **Cómo lo pienso:** $t=\sqrt{x+1}$ ⇒ $x=t^2-1$, $dx=2t\,dt$; la $t$ del denominador se va con la de $dx$ y queda un polinomio. Los límites $x=0,3$ pasan a $t=1,2$.
- **Qué uso:** cambio de variable en la definida (U p. 251); Barrow (U Teor. 6.2, p. 244).
- **Por dónde empiezo:** despejar $x$ y calcular $dx$.

1. **Continuidad:** en $[0,3]$, $x+1\ge1>0$: integrando continuo.
2. **Cambio:** $x=t^2-1$, $dx=2t\,dt$; $x=0\Rightarrow t=1$, $x=3\Rightarrow t=2$. ($g(t)=t^2-1$ tiene derivada $2t\ne0$ en $[1,2]$.)
3. **Sustituir:** $\int_1^2\frac{t^2-1}{t}\,2t\,dt=2\int_1^2(t^2-1)\,dt$.
4. **Barrow en $t$:** $2\Big[\frac{t^3}3-t\Big]_1^2=2\Big[\Big(\frac83-2\Big)-\Big(\frac13-1\Big)\Big]=2\Big(\frac23+\frac23\Big)=\frac83$.
5. **Comprobación deshaciendo el cambio:** primitiva $\frac23t^3-2t=\frac23(x+1)^{3/2}-2\sqrt{x+1}$; en $3$: $\frac{16}3-4=\frac43$; en $0$: $\frac23-2=-\frac43$; diferencia $\frac83$ ✓. Las dos vías dan lo mismo.

**Receta.** En una definida, o se cambian los límites (y no se vuelve a $x$), o se deshace el cambio y se usan los límites originales. Nunca mezclar.

**Error típico.** Integrar en $t$ y sustituir los límites de $x$ ($0$ y $3$): daría $2[\,9-3\,]=12$, falso.

sympy: $\int_0^3\frac{x}{\sqrt{x+1}}dx=\frac83=2\int_1^2(t^2-1)dt$.

---

### Propio 4 — $\mathrm{sen}^n\cos^m$: exponente impar y exponentes pares (difícil) [propio]

> a) Calcula $\displaystyle\int\mathrm{sen}^5x\cos^2x\,dx$. b) Calcula $\displaystyle\int\mathrm{sen}^2x\,dx$ y $\displaystyle\int_0^\pi\mathrm{sen}^2x\,dx$.

**Antes de calcular**
- **Qué me piden:** primitivas de productos de potencias de seno y coseno.
- **Cómo lo pienso:** a) el seno tiene exponente impar: separo un $\mathrm{sen}\,x$ (derivada de $-\cos x$), paso $\mathrm{sen}^4x=(1-\cos^2x)^2$ y cambio $u=\cos x$. b) exponente par: ángulo doble.
- **Qué uso:** $\mathrm{sen}^nx\cos^mx$ (U pp. 262-263, Ej. 6.27-6.28); cambio de variable (U p. 250); Barrow (U Teor. 6.2, p. 244).
- **Por dónde empiezo:** a) $\mathrm{sen}^5x=(\mathrm{sen}^2x)^2\,\mathrm{sen}\,x=(1-\cos^2x)^2\,\mathrm{sen}\,x$.

a)
1. **Reescribir:** $\mathrm{sen}^5x\cos^2x=(1-\cos^2x)^2\cos^2x\,\mathrm{sen}\,x$.
2. **Cambio $u=\cos x$**, $du=-\mathrm{sen}\,x\,dx$ (el signo menos importa):
   $$\int(1-u^2)^2u^2(-du)=-\int(u^2-2u^4+u^6)\,du=-\frac{u^3}3+\frac{2u^5}5-\frac{u^7}7+C.$$
3. **Deshacer:** $\int\mathrm{sen}^5x\cos^2x\,dx=-\frac{\cos^3x}3+\frac{2\cos^5x}5-\frac{\cos^7x}7+C$.

b)
4. **Ángulo doble:** $\mathrm{sen}^2x=\frac{1-\cos2x}2$, luego $\int\mathrm{sen}^2x\,dx=\frac x2-\frac{\mathrm{sen}\,2x}4+C$.
5. **Definida:** $\Big[\frac x2-\frac{\mathrm{sen}\,2x}4\Big]_0^\pi=\frac\pi2-0=\frac\pi2$ (la mitad de la longitud del intervalo: el valor medio de $\mathrm{sen}^2$ en un periodo es $\frac12$).

**Receta.** $\mathrm{sen}^nx\cos^mx$: algún exponente impar ⇒ separar un factor y cambio $u$ = la otra función; ambos pares ⇒ bajar grado con el ángulo doble.

**Error típico.** En a), olvidar el signo de $du=-\mathrm{sen}\,x\,dx$; en b), escribir $\int\mathrm{sen}^2x=\frac{\mathrm{sen}^3x}3$ (no hay un $\cos x$ que haga de derivada).

sympy: la derivada de la primitiva de a) es $\mathrm{sen}^5x\cos^2x$; la de b) es $\mathrm{sen}^2x$; $\int_0^\pi\mathrm{sen}^2x\,dx=\frac\pi2$.

---

## 4. Chuleta rápida del tema

| Si veo… | Hago… | Fuente |
|---|---|---|
| $g(f(x))\cdot f'(x)$ (función + su derivada) | inmediata / $t=f(x)$ | U pp. 248, 250 |
| $\frac{f'}{f}$ | $\ln\lvert f\rvert$ (¡valor absoluto!) | U pp. 248-249 |
| polinomio × $e^x$, $\mathrm{sen}$, $\cos$ | partes, $u$ = polinomio (tantas veces como el grado) | U p. 252 |
| $\ln x$, $\mathrm{arctg}\,x$, polinomio × $\ln x$ | partes, $u$ = $\ln$ o $\mathrm{arc}$ | U p. 252 |
| $e^{ax}\cos bx$ | partes dos veces y despejar | U p. 253 |
| racional, grado num ≥ den | dividir | U p. 255 |
| racional, raíces reales | fracciones simples ⇒ $\ln$ y potencias | U pp. 255-257 |
| $x^2+bx+c$ irreducible | $\ln$ + $\mathrm{arctg}$ (completar cuadrados) | U p. 258 |
| $(x^2+bx+c)^2$ o más | Hermite | U pp. 259-261 |
| $\mathrm{sen}^n\cos^m$ con impar | separar un factor + $\mathrm{sen}^2+\cos^2=1$ | U p. 263 |
| $\mathrm{sen}^n\cos^m$ pares | ángulo doble | U p. 262 |
| solo $\mathrm{tg}(u)$ | $t=\mathrm{tg}(u)$ | E 6.27 |
| racional en $\mathrm{sen},\cos$ | $t=\mathrm{tg}\frac x2$ | U p. 261 |
| raíces de $x$ | $x=t^{\mathrm{m.c.m.}}$ | E 6.28 |
| definida | continuidad + primitiva + Barrow; cambiar límites con el cambio | U pp. 244, 251, 254 |

**Lista de comprobación («sé hacer…»):** reconocer una inmediata ajustando constantes · elegir $u$ y $v'$ en partes · partes reiterada y cíclica · dividir y descomponer en fracciones simples (raíces simples, múltiples, factor irreducible) · Hermite · completar cuadrados para el arcotangente · cambio $t=\mathrm{tg}\frac x2$ · $\mathrm{sen}^n\cos^m$ · cambiar los límites en una definida · áreas entre curvas que se cruzan · comprobar derivando.

**Errores frecuentes del tema:** olvidar el $+C$ · olvidar $\lvert\cdot\rvert$ en el $\ln$ · cambiar la variable y no $dx$ · cambiar la variable y no los límites · no dividir antes de descomponer · signos en $\int\frac{dt}{a-t}=-\ln\lvert a-t\rvert$ y en $\int e^{-x}=-e^{-x}$ · en áreas, no partir en los cortes.
