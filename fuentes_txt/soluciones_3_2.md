# Unidad 3.2 — Series de potencias y series de Taylor (aplicaciones a series y sucesiones de funciones)

**Ejercicios:** E 3.15-3.20 (E pp. 100-107; página impresa = PDF). Para el examen cuentan **3.18, 3.19 y 3.20**. Los ejercicios 3.15, 3.16 y 3.17 son de sucesiones y series de funciones: **fuera de examen**, y aquí se resuelven más breves.
**Teoría:** U §3.2 «Aplicaciones a series y sucesiones de funciones», pp. 113-119 (PDF 111-117). Apartados: 3.2.1 Motivación p. 113; 3.2.2 Derivación de sucesiones y series de funciones pp. 113-115 (fuera de examen); «Derivación de series de potencias» p. 116 (Prop. 3.3 y Teor. 3.1, que **sí** se usan); 3.2.3 Funciones analíticas pp. 117-119.
**Herramientas previas de U que hacen falta:** radio de convergencia de una serie de potencias, que está en U §1.5 pp. 67-70. Esa sección está oficialmente fuera de examen, pero **el radio de convergencia se pregunta en los exámenes** (X pp. 46, 96, 99, 105, 112, 126), así que hay que dominar esas cuatro páginas.

**Avisos de extracción (comprobados renderizando los PDF con PyMuPDF).** En `ejercicios.txt` se pierden símbolos. En 3.15 (E p. 101), «$g$ es derivable si $x=0$» es en realidad **$x\neq 0$**. En 3.16 (E p. 102), «$\frac\pi2=\frac\pi2=0$» es **$\frac\pi2\neq0$**. En 3.17 (E p. 104), el enunciado dice $f_n(x)=e^{-n}x^n$ (el `.txt` da «e−nxn»): **confirmado en la imagen**. En U Ej. 3.11 (p. 115), «$f'(x)=\lim_{n\to\infty} f_n'(x)$» y «$1,\ x=0$» llevan también $\neq$ en el original.

## Orden de estudio recomendado (se mantiene la numeración de E)

| Bloque | Ejercicios (orden de estudio) | Herramienta de U |
|---|---|---|
| 0. Radio de convergencia (repaso) | Propio P1; X p. 46/96, X p. 99, X p. 126, X p. 105 | U §1.5 pp. 67-70 (Def. 1.29, tipos 1-3, criterios de la raíz y del cociente); Prop. 1.6 p. 36 |
| A. Derivar series de potencias | 3.18 → X p. 112 → propio P4 | U Prop. 3.3 y Teor. 3.1 p. 116 |
| B. Series de Taylor | 3.19 → X p. 142 → propio P2 → 3.20 → propio P3 → X pp. 145-146 | U §3.2.3 pp. 117-119 (Ej. 3.13-3.15) |
| C. Fuera de examen | 3.15 → 3.16 → 3.17 | U §3.2.2 pp. 113-115 |

**Notación.** Como en U y E, $f^{(n}$ es la derivada $n$-ésima. Una **serie de potencias centrada en $x_0$** es $\sum_{n=0}^\infty a_n(x-x_0)^n$ (U Def. 1.29 p. 67). Su **radio de convergencia** $R$ es el número que separa los $x$ donde converge ($|x-x_0|<R$) de aquellos donde diverge ($|x-x_0|>R$). En los dos extremos, $x_0\pm R$, hay que mirar a mano (U p. 68 y Ej. 1.60 pp. 68-69).

---

# BLOQUE 0 — Repaso: cómo se calcula el radio de convergencia

**Idea en una frase.** Para cada $x$ fijo, la serie de potencias es una serie de números. El criterio del cociente o el de la raíz dice para qué $x$ esa serie converge, y eso da un intervalo centrado en $x_0$.

**Las dos fórmulas** (U p. 70; E las recuerda en el margen de p. 104). Sea $\sum a_n(x-x_0)^n$:
- **Cociente:** si $\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|=S$, entonces $R=\frac1S$ ($R=\infty$ si $S=0$; $R=0$ si $S=\infty$).
- **Raíz:** lo mismo con $\lim_{n\to\infty}\sqrt[n]{|a_n|}=S$.

**Cuál elegir** (U p. 70: «depende de la naturaleza de los coeficientes»). Si $a_n$ lleva factoriales o productos, se usa el cociente: los factoriales se simplifican. Si $a_n$ es «algo elevado a $n$» (o a $n^2$), se usa la raíz.

**En los extremos** $x=x_0\pm R$ los criterios no deciden, porque el límite vale 1. Se sustituye el valor y se estudia la serie numérica: si el término general no tiende a $0$, la serie diverge (U Prop. 1.6 p. 36). Si tiende a $0$, hay que usar armónica, Leibniz, etc. (U pp. 37, 41).

Los problemas de examen de este bloque están en la sección «Así lo preguntan en el examen» y el propio P1, al final.

---

# BLOQUE A — Derivar una serie de potencias término a término

**Idea.** Dentro de su intervalo de convergencia (abierto), una serie de potencias se comporta como un «polinomio infinito»: se deriva sumando por sumando y la serie derivada tiene **el mismo radio** (U Prop. 3.3 y Teor. 3.1 p. 116). Eso permite fabricar desarrollos nuevos a partir de otros conocidos sin calcular derivadas $n$-ésimas.

## Ejercicio 3.18 (E pp. 104-105)

> Sabemos que $\displaystyle\sum_{n=0}^{+\infty}x^n=\frac{1}{1-x}$, para $x\in(-1,1)$ por ser una serie geométrica. A partir de esta expresión, se pide expresar $(1-x)^{-2}$ como una serie de potencias para $x\in(-1,1)$. **Pista:** calcula la derivada de la función $f(x)=\frac{1}{1-x}$.

**Idea en una frase.** $(1-x)^{-2}$ es la derivada de $\frac1{1-x}$. Derivando los dos lados de la igualdad conocida, a la izquierda queda una serie y a la derecha lo que buscamos.

**Solución.**
1. **Lo que sabemos.** Para $|x|<1$ se cumple $1+x+x^2+x^3+\dots=\frac1{1-x}$: es la serie geométrica de razón $x$ (U Ej. 1.33 p. 36 y Ej. 1.58 p. 68). Es una serie de potencias con todos los $a_n=1$ y radio $1$.
2. **¿Podemos derivar sumando a sumando?** Sí. La Prop. 3.3 de U (p. 116) dice: si $f(x)=\sum a_nx^n$ para todo $x\in(-c,c)$, entonces $f$ es derivable en $(-c,c)$ y $f'(x)=\sum\frac{d}{dx}(a_nx^n)$. Aquí $c=1$. **No hace falta** convergencia uniforme (ver «Errata» abajo).
3. **Derivamos el lado derecho.** Escribimos $f(x)=(1-x)^{-1}$. Por la regla de la cadena (U p. 79), $f'(x)=-1\cdot(1-x)^{-2}\cdot(-1)=(1-x)^{-2}$. Es justo la función del enunciado.
4. **Derivamos el lado izquierdo, sumando a sumando.** $(x^n)'=nx^{n-1}$. El primer sumando es $x^0=1$, una constante, y su derivada es $0$. Por eso la suma derivada empieza en $n=1$:
   $$(1-x)^{-2}=\sum_{n=1}^{\infty}nx^{n-1}=1+2x+3x^2+4x^3+\cdots$$
5. **(Opcional) Reindexar para que empiece en $0$.** Llamamos $m=n-1$, es decir, $n=m+1$. Cuando $n=1$, $m=0$:
   $$\boxed{\frac1{(1-x)^2}=\sum_{m=0}^{\infty}(m+1)x^m,\qquad x\in(-1,1).}$$
   Las dos escrituras son la misma lista de sumandos: $1+2x+3x^2+\dots$
6. **¿Dónde vale?** El Teor. 3.1 (p. 116) garantiza el mismo radio, $1$. También sale con el cociente: $\frac{m+2}{m+1}\to1$. En los extremos, $x=\pm1$, el término $(m+1)(\pm1)^m$ no tiende a $0$, así que la serie diverge (U Prop. 1.6 p. 36). Vale **exactamente** en $(-1,1)$.
7. **Comprobación numérica.** En $x=\frac12$: $\frac1{(1/2)^2}=4$, y la serie da $1+1+\frac34+\frac12+\frac5{16}+\dots$, que suma $4$. Verificado con sympy (también el desarrollo $1+2x+3x^2+\dots+6x^5+O(x^6)$).

**Receta.** Para desarrollar una función que es la **derivada** de otra con serie conocida: se deriva la serie conocida término a término (U Teor. 3.1), se cuida que el término constante desaparece (el índice sube en 1) y se conserva el mismo radio. Después se revisan los extremos.
**Error típico.** (1) Escribir $\sum_{n=0}^\infty nx^n$ o $\sum nx^{n}$: al derivar, el exponente **baja** a $n-1$. (2) Cambiar el índice inicial sin cambiar la fórmula: $\sum_{n=1}nx^{n-1}=\sum_{n=0}(n+1)x^n$, y no $\sum_{n=0}nx^{n-1}$.
**Errata de E (p. 105).** E justifica la derivación diciendo que la geométrica «converge uniformemente en $(-1,1)$». **Es falso**: el resto es $\frac1{1-x}-\sum_{n=0}^Nx^n=\frac{x^{N+1}}{1-x}$, que no está acotado cuando $x\to1^-$ (sympy: el límite es $+\infty$). La convergencia es uniforme solo en cada $[-k,k]$ con $k<1$ (U, Proposición de convergencia, p. 67). La justificación correcta es directamente la Prop. 3.3 de U, que no pide convergencia uniforme. (E escribe también $\sum_{n=0}nx^{n-1}=0+1+2x+\dots$: el sumando $n=0$ es $0\cdot x^{-1}$, que no está definido en $x=0$. Mejor no usar esa forma.)
**Teoría:** U Prop. 3.3 y Teor. 3.1 p. 116; serie geométrica U Ej. 1.33 p. 36 y Ej. 1.58 p. 68.

---

# BLOQUE B — Series de Taylor y funciones analíticas

**Idea.** El polinomio de Taylor $p_n$ (unidad 3.1) se hace «infinito»: la **serie de Taylor** de $f$ en $x_0$ es $\sum_{n=0}^\infty\frac{f^{(n}(x_0)}{n!}(x-x_0)^n$ (U §3.2.3 p. 117). Hay que distinguir tres preguntas:
1. **¿Cuál es la serie?** Se calculan $f^{(n}(x_0)$ y se busca el patrón.
2. **¿Dónde converge?** Radio de convergencia (Bloque 0).
3. **¿Suma $f(x)$?** Si sí, en un intervalo alrededor de $x_0$, $f$ es **analítica** (U pp. 117-118). U afirma (p. 118) que los polinomios, las trigonométricas, las exponenciales y los logaritmos lo son, y que **toda serie de potencias es la serie de Taylor de su suma** en su intervalo de convergencia, porque $a_n=\frac{f^{(n}(0)}{n!}$.

## Ejercicio 3.19 (E pp. 105-106)

> Sea $f$ la función dada por $f(x)=e^x$. Calcula su serie de Taylor centrada en $0$ y deriva término a término la serie resultante. Comprueba que la serie formada por estas derivadas coincide con la serie de Taylor.

**Idea en una frase.** Todas las derivadas de $e^x$ son $e^x$, así que todos los coeficientes valen $\frac1{n!}$. Al derivar $\frac{x^n}{n!}$ sale el sumando anterior, $\frac{x^{n-1}}{(n-1)!}$: la serie «se desplaza» y queda igual.

**Solución.**
1. **Derivadas en $0$.** $f'(x)=e^x$, y por tanto $f''=e^x$, …, $f^{(n}(x)=e^x$ para todo $n$. En $0$: $f^{(n}(0)=e^0=1$.
2. **Coeficientes.** $a_n=\frac{f^{(n}(0)}{n!}=\frac1{n!}$ (definición de serie de Taylor, U p. 117).
3. **La serie.**
   $$\sum_{n=0}^{\infty}\frac{x^n}{n!}=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots$$
4. **Radio.** Por el cociente: $\left|\frac{a_{n+1}}{a_n}\right|=\frac{n!}{(n+1)!}=\frac1{n+1}\to0$, luego $R=\infty$ (U p. 70). Converge para todo $x\in\mathbb R$.
5. **¿Se puede derivar término a término?** Sí, en todo $\mathbb R$, por el Teor. 3.1 (p. 116).
6. **Derivamos cada sumando.** El sumando $n=0$ es la constante $1$, con derivada $0$. Para $n\ge1$:
   $$\left(\frac{x^n}{n!}\right)'=\frac{n\,x^{n-1}}{n!}=\frac{x^{n-1}}{(n-1)!},$$
   porque $n!=n\cdot(n-1)!$ y la $n$ se simplifica. Ejemplo con $n=3$: $\left(\frac{x^3}{6}\right)'=\frac{3x^2}{6}=\frac{x^2}{2!}$.
7. **Escribimos la serie derivada:** $0+1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots$. Con $m=n-1$ queda $\sum_{m=0}^\infty\frac{x^m}{m!}$, **la misma serie** del paso 3.
8. **Interpretación.** La suma $S(x)$ de la serie cumple $S'=S$ y $S(0)=1$, como $e^x$. Que la serie suma exactamente $e^x$ lo afirma U p. 118 (las exponenciales son analíticas). Se demuestra con el resto de Lagrange: $|R_n(x)|\le e^{|x|}\frac{|x|^{n+1}}{(n+1)!}\to0$ (S Ej. 2 p. 757). Verificado con sympy.

**Receta.** Serie de Taylor de $f$ en $x_0$: (1) calcular unas cuantas $f^{(n}(x_0)$ y adivinar el patrón; (2) dividir entre $n!$; (3) radio por el cociente. Para derivar término a término: bajar el exponente, simplificar $n/n!=1/(n-1)!$ y reindexar.
**Error típico.** Olvidar que el sumando constante se anula al derivar y «perder» o «ganar» un término al reindexar.
**Teoría:** U §3.2.3 p. 117 (def. y Ej. 3.13, que hace lo mismo con $e^{2x}$); Teor. 3.1 p. 116; analíticas p. 118.

## Ejercicio 3.20 (E pp. 106-107)

> Sea $f$ la función definida, para $x>-1$, por $f(x)=\dfrac{1}{(1+x)^k}$ para $k\in\mathbb N$, $k>0$. Obtén su desarrollo en serie de Taylor centrado en $x_0=0$ y su radio de convergencia.
> *Nota:* Ten en cuenta que $f^{(n}(x)=(-1)^n\dfrac{(k+n-1)!}{(k-1)!\,(1+x)^{k+n}}$.

**Idea en una frase.** Cada derivada baja el exponente en $1$ y saca un factor (cambiado de signo). En $x=0$ el denominador vale $1$ y solo queda ese producto de factores. Dividido entre $n!$, es un número combinatorio.

**Solución.**
1. **Las primeras derivadas** (regla $((1+x)^{a})'=a(1+x)^{a-1}$):
   - $f(x)=(1+x)^{-k}$, y $f(0)=1$.
   - $f'(x)=-k(1+x)^{-k-1}$, y $f'(0)=-k$.
   - $f''(x)=(-k)(-k-1)(1+x)^{-k-2}=k(k+1)(1+x)^{-k-2}$, y $f''(0)=k(k+1)$.
   - $f'''(x)=-k(k+1)(k+2)(1+x)^{-k-3}$, y $f'''(0)=-k(k+1)(k+2)$.
2. **El patrón.** Cada derivada añade un factor más y un signo menos más:
   $$f^{(n}(0)=(-1)^n\,k(k+1)\cdots(k+n-1)=(-1)^n\frac{(k+n-1)!}{(k-1)!}.$$
   La segunda forma es la de la nota: el producto $k(k+1)\cdots(k+n-1)$ son los factores de $(k+n-1)!$ que **no** están en $(k-1)!$. Ejemplo: $k=3$, $n=2$: $3\cdot4=\frac{4!}{2!}=12$.
3. **Coeficientes** (dividir entre $n!$):
   $$a_n=\frac{f^{(n}(0)}{n!}=(-1)^n\frac{(k+n-1)!}{(k-1)!\,n!}=(-1)^n\binom{k+n-1}{n}.$$
   Ejemplo: $k=3$ da $a_0,a_1,a_2,a_3=1,-3,6,-10$.
4. **La serie:**
   $$\boxed{\frac1{(1+x)^k}=\sum_{n=0}^{\infty}(-1)^n\binom{k+n-1}{n}x^n=1-kx+\frac{k(k+1)}{2!}x^2-\frac{k(k+1)(k+2)}{3!}x^3+\cdots}$$
5. **Radio, por el cociente:**
   $$\left|\frac{a_{n+1}}{a_n}\right|=\frac{k(k+1)\cdots(k+n)}{(n+1)!}\cdot\frac{n!}{k(k+1)\cdots(k+n-1)}=\frac{k+n}{n+1}\xrightarrow[n\to\infty]{}1.$$
   Todo se simplifica salvo el último factor de arriba ($k+n$) y el último de abajo ($n+1$). Por tanto $R=1$.
6. **Extremos (E no los estudia).** $\binom{k+n-1}{n}\ge1$, así que en $x=\pm1$ el término general no tiende a $0$ y la serie diverge (U Prop. 1.6 p. 36). Intervalo de convergencia: $(-1,1)$.
7. **¿La serie suma $f$?** Sí, en $(-1,1)$. Para $k=1$ es la geométrica de razón $-x$: $\frac1{1+x}=\sum(-x)^n$ (U p. 36). Derivando esa igualdad $k-1$ veces término a término (Teor. 3.1 p. 116) se obtiene la de cada $k$. Por ejemplo, para $k=2$: $-\frac1{(1+x)^2}=\sum_{n\ge1}(-1)^n n x^{n-1}$, es decir, $\frac1{(1+x)^2}=1-2x+3x^2-\dots$ Así que $f$ es analítica en $(-1,1)$.
8. **Comprobación.** Con sympy, para $k=1,2,3,4$, los coeficientes de la serie de $(1+x)^{-k}$ hasta $x^6$ coinciden con $(-1)^n\binom{k+n-1}{n}$, y la fórmula de la nota es correcta para $n=0,\dots,5$ ($k=3$).

**Receta.** Para potencias $(1+x)^{-k}$ (o cocientes parecidos): derivar 3 o 4 veces **sin simplificar** los productos, ver qué factor se añade cada vez, evaluar en $x_0$ y dividir entre $n!$. El radio, por el cociente, simplificando los productos «telescópicos».
**Error típico.** Pensar que el radio llega «hasta donde está definida $f$». $f$ existe en $(-1,\infty)$, pero la serie solo converge en $(-1,1)$: en $x=2$, por ejemplo, $f(2)=3^{-k}$ y la serie diverge. El radio lo fija la distancia del centro al «punto malo» $x=-1$, que está a distancia $1$ por los dos lados.
**Errata de E (p. 106).** Escribe «el desarrollo de Taylor de $f$ en $x=0$ de orden $n$ es $f(x)=1-kx+\dots+(-1)^n\frac{k\cdots(k+n-1)}{n!}x^n$». Esa suma finita es el **polinomio** $p_n(x)$, no $f(x)$: falta el resto, $f=p_n+R_n$, o bien escribir la serie infinita con «$+\cdots$». Además, E no estudia los extremos ni justifica que la serie suma $f$ (pasos 6 y 7).
**Teoría:** U §3.2.3 p. 117 (serie de Taylor); criterio del cociente U p. 70; Teor. 3.1 p. 116. La fórmula general $(1+x)^\alpha=\sum\binom{\alpha}{n}x^n$ es la serie binomial de S Teor. 17 p. 761: aquí $\alpha=-k$ y $\binom{-k}{n}=(-1)^n\binom{k+n-1}{n}$.

---

# BLOQUE C — Sucesiones y series de funciones (FUERA DE EXAMEN)

> Estos tres ejercicios usan la convergencia uniforme de U §3.2.2 (pp. 113-115) y §1.5. Van colapsados en el resumen. Se resuelven de forma breve.

**Recordatorio.** $f_n\to f$ **uniformemente** en $I$ si $\lim_{n\to\infty}\sup_{x\in I}|f_n(x)-f(x)|=0$. Proposición de U p. 114: si las $f_n$ son derivables en un intervalo **acotado** $(a,b)$, $\{f_n'\}$ converge uniformemente y $\{f_n(x_0)\}$ converge en algún punto, entonces $f_n\to f$ uniformemente, $f$ es derivable y $f'=\lim_{n\to\infty} f_n'$.

## Ejercicio 3.15 (E pp. 100-102) — fuera de examen

> Sea $\{f_n\}$ la sucesión de funciones dada por $f_n(x)=\sqrt{x^2+\frac1n}$. Calcula su límite. ¿Son derivables las funciones $f_n(x)$?, ¿y su límite? Comprueba que la sucesión converge uniformemente.

**Idea en una frase.** Las $f_n$ son versiones «redondeadas» de $|x|$. Se pegan a $|x|$ uniformemente, pero el pico de $|x|$ no es derivable: la convergencia uniforme de $f_n$ **no** transmite la derivabilidad.

1. **Límite puntual.** Para $x$ fijo, $\frac1n\to0$ y la raíz es continua, así que $f_n(x)\to\sqrt{x^2}=|x|$.
2. **Derivabilidad de $f_n$.** $x^2+\frac1n>0$ siempre, y la raíz es derivable en $(0,\infty)$. Por la cadena, $f_n'(x)=\frac{x}{\sqrt{x^2+1/n}}$ existe en todo $\mathbb R$.
3. **El límite $|x|$ no es derivable en $0$**: sus derivadas laterales valen $-1$ y $1$ (U Def. 2.3 p. 81).
4. **Convergencia uniforme** (camino más corto que el de E, multiplicando por el conjugado):
   $$0\le\sqrt{x^2+\tfrac1n}-|x|=\frac{1/n}{\sqrt{x^2+1/n}+|x|}\le\frac{1/n}{\sqrt{1/n}}=\frac1{\sqrt n},$$
   con igualdad en $x=0$. Luego $\sup_{x}|f_n-f|=\frac1{\sqrt n}\to0$. Coincide con E, que llega al mismo supremo estudiando la monotonía de $g=f_n-|x|$.
5. **Por qué no contradice la proposición de U p. 114.** $\{f_n'\}$ no converge uniformemente. Su límite es $-1$ si $x<0$, $0$ si $x=0$ y $1$ si $x>0$. En $x=\frac1{\sqrt n}$ se tiene $f_n'=\frac1{\sqrt2}$, así que $\sup|f_n'-\lim_{n\to\infty} f_n'|\ge1-\frac1{\sqrt2}$ para todo $n$. E solo lo «ilustra» con la figura 3.2: este es el argumento.

**Receta.** Para el supremo de $|f_n-f|$: simplificar la diferencia (conjugado, cotas) antes de derivar. Si se llega a una cota que tiende a $0$, la convergencia es uniforme.

## Ejercicio 3.16 (E pp. 102-104) — fuera de examen

> Sea $\{f_n\}$ la sucesión de funciones definida por $f_n(x)=\operatorname{arctg}\frac{x}{n}$, $n\in\mathbb N$. Estudia: 1) La convergencia puntual y uniforme de $\{f_n\}$ en $\mathbb R$. 2) La convergencia puntual y uniforme de $\{f_n'\}$. 3) La convergencia uniforme de $\{f_n\}$ en $[0,1]$.

**Idea en una frase.** Para $x$ fijo, $\frac xn\to0$. Pero para cada $n$ siempre hay $x$ muy grandes donde $\operatorname{arctg}\frac xn$ está cerca de $\frac\pi2$: en $\mathbb R$ no es uniforme, y en $[0,1]$ sí.

1. **Puntual:** $\operatorname{arctg}\frac xn\to\operatorname{arctg}0=0$. **Uniforme en $\mathbb R$:** $\sup_{x\in\mathbb R}|\operatorname{arctg}\frac xn|=\frac\pi2$, porque $\lim_{x\to\infty}\operatorname{arctg}\frac xn=\frac\pi2$ (no se alcanza, pero es el supremo). El límite de los supremos es $\frac\pi2\neq0$: **no** es uniforme.
2. $f_n'(x)=\frac1n\cdot\frac1{1+x^2/n^2}=\frac{n}{n^2+x^2}$. Puntualmente tiende a $0$. Además $0<f_n'(x)\le f_n'(0)=\frac1n\to0$: converge **uniformemente** a $0$ en $\mathbb R$.
3. **En $[0,1]$:** el arcotangente es creciente, así que el supremo está en $x=1$: $\operatorname{arctg}\frac1n\to0$. **Uniforme**.
4. **¿Contradice la proposición de U (p. 114)?** No: en 2) las derivadas convergen uniformemente y $f_n(0)=0$ converge, pero $\mathbb R$ **no es un intervalo acotado**, que es una hipótesis. En $[0,1]$ (acotado) todo encaja, como muestra 3).

**Receta.** Antes de aplicar un teorema, comprobar **todas** sus hipótesis (aquí: intervalo acotado). El mismo $f_n$ puede converger uniformemente en un intervalo y no en otro.

## Ejercicio 3.17 (E p. 104) — fuera de examen

> Sea $\displaystyle\sum_{n=1}^{+\infty}f_n(x)$ la serie de funciones con $f_n(x)=e^{-n}x^n$. En los ejercicios del Tema 1 vimos que es una serie absoluta y uniformemente convergente en cualquier intervalo de la forma $[-k,k]$ para $0<k<e$. Construye la serie $\sum_{n=1}^{+\infty}f_n'(x)$ y calcula su radio de convergencia.

(Enunciado confirmado en la imagen de E p. 104: $f_n(x)=e^{-n}x^n$.)

**Idea en una frase.** Es una serie de potencias, $\sum\left(\frac xe\right)^n$, de radio $e$. Su derivada término a término hereda el radio $e$ (U Teor. 3.1).

1. **Derivar cada término:** $f_n'(x)=ne^{-n}x^{n-1}$.
2. **La serie:** $\sum_{n=1}^\infty ne^{-n}x^{n-1}=\sum_{n=0}^\infty(n+1)e^{-(n+1)}x^n$, reindexando con $n\to n+1$.
3. **Radio (cociente):** $\left|\frac{(n+2)e^{-(n+2)}}{(n+1)e^{-(n+1)}}\right|=\frac{n+2}{(n+1)e}\to\frac1e$, luego $R=e$. E calcula el mismo límite con los coeficientes sin reindexar, $\frac{(n+1)e^{-(n+1)}}{ne^{-n}}$, y da también $\frac1e$.
4. **Atajo:** U Teor. 3.1 (p. 116). La serie original es geométrica de razón $\frac xe$, con radio $e$, y la derivada conserva el radio.
5. **Comprobación (propia).** Para $|x|<e$, $\sum_{n\ge1}(x/e)^n=\frac{x}{e-x}$, y su derivada es $\frac{e}{(e-x)^2}=\frac1e+\frac{2x}{e^2}+\frac{3x^2}{e^3}+\dots$, que coincide con la serie del paso 2. Verificado con sympy.

**Receta.** La serie de las derivadas de una serie de potencias tiene el mismo radio. Si además se reconoce una geométrica, se puede sumar.

---

# Así lo preguntan en el examen (X; página = PDF, leída como imagen)

## X p. 46 (Sept. 2014, Modelo A, Grado en Ing. Mecánica, P1) y X p. 96 (Sept. 2018, Modelo A, Mecánica, P1)

> (p. 46) Calcúlese el radio de convergencia de la serie de potencias $\displaystyle\sum_{n=0}^\infty\frac{x^n}{2^n}$. (p. 96: lo mismo con $\frac{x^n}{3^n}$.)

**Idea.** $\frac{x^n}{2^n}=\left(\frac x2\right)^n$ es geométrica: converge si $\left|\frac x2\right|<1$.
1. **Coeficiente:** $a_n=\frac1{2^n}$.
2. **Cociente:** $\frac{a_{n+1}}{a_n}=\frac{2^n}{2^{n+1}}=\frac12$, y su límite es $\frac12$.
3. **Radio:** $R=\frac1{1/2}=2$. Con $3^n$: $R=3$. (X lo escribe como $\frac{a_n}{a_{n-1}}$, que es lo mismo.) Verificado con sympy.

**Receta.** Si $a_n=\frac1{b^n}$, entonces $R=b$. Basta reconocer la geométrica $\left(\frac xb\right)^n$.

## X p. 99 (I. Electrónica Industrial y Automática, sin fecha en la página, P2)

> Calcule el centro, radio de convergencia e intervalo de convergencia de la serie de potencias $\displaystyle\sum_{n=1}^\infty\frac{(2x-1)^n}{n!}$.

**Idea en una frase.** Primero hay que dejar la serie en la forma $(x-x_0)^n$, sacando el $2$ de dentro; solo entonces se leen el centro y los coeficientes.
1. **Forma estándar:** $2x-1=2\left(x-\frac12\right)$, así que $(2x-1)^n=2^n\left(x-\frac12\right)^n$. La serie es $\sum\frac{2^n}{n!}\left(x-\frac12\right)^n$.
2. **Centro:** $x_0=\frac12$ (no $1$, ni $-1$).
3. **Coeficientes:** $a_n=\frac{2^n}{n!}$. **Cociente:** $\frac{2^{n+1}/(n+1)!}{2^n/n!}=\frac2{n+1}\to0$.
4. **Radio** $R=\infty$. **Intervalo de convergencia:** todo $\mathbb R$ (no hay extremos que estudiar). Coincide con X. Verificado con sympy.

**Receta.** Si aparece $(bx-c)^n$, escribir $b^n\left(x-\frac cb\right)^n$: centro $\frac cb$, y el $b^n$ pasa al coeficiente.
**Error típico.** Tomar centro $1$, o leer $a_n=\frac1{n!}$ olvidando el $2^n$. Aquí no cambia el radio (es $\infty$), pero en $\sum(2x-1)^n$ el radio sería $\frac12$, no $1$.

## X p. 126 (I. Electrónica Industrial y Automática, examen sin fecha, P1)

> Calcule el radio de convergencia de la serie $\displaystyle\sum_{n=1}^\infty\left(1+\frac1n\right)^{2n^2}x^n$.

**Idea en una frase.** El coeficiente es «algo elevado a $n^2$»: la raíz $n$-ésima lo baja a «algo elevado a $n$», que es el límite del número $e$.
1. **Elección del criterio:** raíz (U p. 70), por el exponente $n^2$.
2. **Raíz $n$-ésima:** $\sqrt[n]{a_n}=\left(1+\frac1n\right)^{2n^2/n}=\left(1+\frac1n\right)^{2n}=\left[\left(1+\frac1n\right)^n\right]^2$.
3. **Límite:** $\left(1+\frac1n\right)^n\to e$ (U Prop. 1.5 p. 31, con $a_n=n$). Elevando al cuadrado, $S=e^2$.
4. **Radio:** $R=\frac1{e^2}$. Coincide con X. Verificado con sympy.

**Receta.** Coeficientes con potencia $n$ o $n^2$: criterio de la raíz. Si sale una indeterminación $1^\infty$, se usa $\left(1+\frac1{a_n}\right)^{a_n}\to e$.
**Error típico.** «$1+\frac1n\to1$ y $1^{\text{lo que sea}}=1$», que daría $R=1$. Es una indeterminación $1^\infty$.

## X p. 105 (I. Electrónica Industrial y Automática, examen de pp. 104-105 sin fecha, Ej. 6, 3 puntos)

> Dada la serie de funciones $\displaystyle\sum_{n=0}^\infty\ln(n+1)(x+1)^n$: discuta si es una serie de potencias y, en caso afirmativo, indique su centro; estudie si existe un intervalo en el que la serie es convergente; estudie si para $x=-2$ y $x=0$ las series numéricas asociadas son convergentes.

**Idea en una frase.** Es una serie de potencias de centro $-1$ y radio $1$. Los puntos $-2$ y $0$ son justo los extremos, y allí el término general no tiende a $0$.
1. **¿Serie de potencias?** Sí: tiene la forma $\sum a_n(x-x_0)^n$ con $a_n=\ln(n+1)$ y $x-x_0=x+1$, es decir, **centro $x_0=-1$** (U Def. 1.29 p. 67).
2. **Cociente.** $a_0=\ln1=0$, así que miramos $n\ge1$: $\frac{a_{n+1}}{a_n}=\frac{\ln(n+2)}{\ln(n+1)}$.
3. **El límite es $\infty/\infty$.** Se calcula con la función $\frac{\ln(x+2)}{\ln(x+1)}$ y L'Hôpital (U §2.3.2 p. 82): $\frac{1/(x+2)}{1/(x+1)}=\frac{x+1}{x+2}\to1$. Luego $S=1$ y $R=1$. (X escribe $\frac{\ln(n+1)}{\ln n}$, con el índice desplazado: el límite es el mismo.)
4. **Intervalo donde converge:** $|x+1|<1$, es decir, $(-2,0)$.
5. **Extremos.** En $x=0$, la serie es $\sum\ln(n+1)$ y el término tiende a $+\infty$. En $x=-2$, la serie es $\sum(-1)^n\ln(n+1)$ y $|\text{término}|\to\infty$. En los dos casos el término general **no tiende a $0$**, luego ambas divergen (U Prop. 1.6 p. 36). Intervalo de convergencia: $(-2,0)$. Verificado con sympy.

**Receta.** Centro, radio (cociente o raíz) y, **siempre**, los dos extremos por separado. Lo primero que se mira en un extremo es si el término general tiende a $0$.
**Error típico.** Pensar que en $x=-2$ «converge por Leibniz» por ser alternada. Leibniz exige que $|a_n|$ decrezca a $0$, y aquí crece.

## X pp. 112-113 («Examen 2 elaborado con exámenes de asignaturas similares», sin fecha, Ej. 4, test)

> Dada la serie $\displaystyle\sum_{n=1}^\infty nx^{n-1}$, señale la opción correcta: A) La serie es convergente para todo valor de $x$; B) La serie no converge para ningún valor de $x$; C) La serie converge en el intervalo $(-1,1)$; D) Ninguna de las anteriores.

**Idea en una frase.** Es la derivada término a término de la geométrica (Ejercicio 3.18): mismo radio, $1$.
1. **Reconocerla:** $\sum_{n\ge1}nx^{n-1}=\frac{d}{dx}\sum_{n\ge0}x^n$ (E 3.18).
2. **Radio:** el de $\sum x^n$ es $1$ (U Ej. 1.58 p. 68). Por U Teor. 3.1 (p. 116), la derivada tiene el mismo radio. También sale con el cociente: $\frac{n+1}{n}\to1$.
3. **Extremos (X no los mira).** En $x=1$ el término es $n\to\infty$; en $x=-1$ es $n(-1)^{n-1}$, que no tiende a $0$. Las dos divergen (U Prop. 1.6 p. 36).
4. **Descartar opciones:** A es falsa ($x=2$ diverge); B es falsa ($x=0$ da $1$). **Respuesta C**: converge exactamente en $(-1,1)$, con suma $\frac1{(1-x)^2}$.

**Receta.** En un test, reconocer la serie como derivada de una conocida da el radio en un paso. Pero el radio **no dice nada de los extremos**: se miran aparte.
**Omisión de X (p. 113).** «Tendrá el mismo radio … Por lo tanto, la opción C es correcta» no basta: con radio $1$ la serie podría converger también en $x=1$ o en $x=-1$ (como $\sum\frac{x^n}{n}$ en $x=-1$), y entonces la respuesta sería D. Hay que añadir el paso 3.

## X p. 142 (Sept. 2018, I. Electrónica Industrial y Automática, P3)

> Calcule la serie de Taylor de $f(x)=e^{\pi x}$ centrada en $x=0$.

**Idea.** Igual que U Ej. 3.13 ($e^{2x}$), con $\pi$ en lugar de $2$.
1. **Derivadas:** $f^{(n}(x)=\pi^ne^{\pi x}$, porque cada derivada saca un factor $\pi$ (regla de la cadena). En $0$: $f^{(n}(0)=\pi^n$.
2. **Serie:** $\displaystyle\sum_{n=0}^\infty\frac{\pi^n}{n!}x^n$.
3. **Radio (X lo omite):** $\frac{\pi^{n+1}/(n+1)!}{\pi^n/n!}=\frac{\pi}{n+1}\to0$, luego $R=\infty$. Atajo: sustituir $t=\pi x$ en $e^t=\sum\frac{t^n}{n!}$. Verificado con sympy.

**Receta.** $e^{ax}=\sum\frac{a^n}{n!}x^n$ para todo $x$. Conviene dar el radio aunque no se pida.

## X pp. 145-146 (Febrero 2018, 1ª semana, I. Electrónica Industrial y Automática, Ej. 5, 3 puntos) — **con errata**

> Dada la función $f(x)=\cos(x)$:
> • Calcule de manera razonada la serie de Taylor de la función $f$ centrada en el punto $x=\frac12$. (1.5 PUNTOS)
> • Usando el resto de Lagrange de orden $n$, calcule $\cos\left(\frac14\right)$ con un error en valor absoluto menor que $0.002$. (1.5 PUNTOS)

**Idea en una frase.** (a) Las derivadas de $\cos$ se repiten cada 4, así que basta evaluar $\cos$ y $\operatorname{sen}$ en $\frac12$. (b) Se busca el primer $n$ cuya **cota** del resto sea menor que $0{,}002$. Con $n=2$ la cota es $0{,}0026$, que **no** basta; con $n=3$ sí.

**(a) Serie de Taylor en $x_0=\frac12$.**
1. **Derivadas:** $f'=-\operatorname{sen}x$, $f''=-\cos x$, $f'''=\operatorname{sen}x$, $f^{(4}=\cos x$, y el ciclo de 4 se repite.
2. **En $\frac12$:** $f^{(4m}(\tfrac12)=\cos\tfrac12$, $f^{(4m+1}(\tfrac12)=-\operatorname{sen}\tfrac12$, $f^{(4m+2}(\tfrac12)=-\cos\tfrac12$, $f^{(4m+3}(\tfrac12)=\operatorname{sen}\tfrac12$.
3. **Serie:**
   $$\cos x=\cos\tfrac12-\operatorname{sen}\tfrac12\left(x-\tfrac12\right)-\frac{\cos\frac12}{2!}\left(x-\tfrac12\right)^2+\frac{\operatorname{sen}\frac12}{3!}\left(x-\tfrac12\right)^3+\frac{\cos\frac12}{4!}\left(x-\tfrac12\right)^4-\cdots$$
   Coincide con X y con sympy. Radio $\infty$: los coeficientes están acotados por $\frac1{n!}$.

**(b) $\cos\frac14$ con error $<0{,}002$** (X elige $x_0=0$, lo que está permitido porque el enunciado no fija el centro).
4. **Resto de Lagrange** (U Prop. 3.2 y Def. 3.3 p. 111): $R_n(\tfrac14)=\frac{f^{(n+1}(c)}{(n+1)!}\left(\tfrac14\right)^{n+1}$ con $c\in(0,\tfrac14)$.
5. **Cota:** $|f^{(n+1}(c)|\le1$ (siempre es $\pm\operatorname{sen}$ o $\pm\cos$), luego $|R_n(\tfrac14)|\le\frac{(1/4)^{n+1}}{(n+1)!}$.
6. **Tabla de cotas (verificada con sympy):**

   | $n$ | cota $\frac{(1/4)^{n+1}}{(n+1)!}$ | ¿$<0{,}002$? |
   |---|---|---|
   | 0 | $0{,}25$ | no |
   | 1 | $0{,}03125$ | no |
   | 2 | $\frac1{384}\approx0{,}002604$ | **no** |
   | 3 | $\frac1{6144}\approx0{,}000163$ | **sí** |

7. **Se necesita $n=3$.** El polinomio de Mac Laurin de orden 3 de $\cos x$ es $p_3(x)=1-\frac{x^2}{2}$, porque $f'''(0)=\operatorname{sen}0=0$: **$p_3=p_2$** (es lo mismo que U Ej. 3.7 p. 109 muestra para el seno; truco C0 de la unidad 3.1).
8. **Resultado:** $\cos\frac14\approx p_3(\tfrac14)=1-\frac1{32}=\frac{31}{32}=0{,}96875$, con error garantizado $\le0{,}000163<0{,}002$. Valor real: $\cos\frac14=0{,}9689124$, y el error real es $0{,}000162$.

**Errata de X (p. 146).** X calcula $|R_2(\tfrac14)|\le\frac16\left(\frac14\right)^3\approx0{,}002604$ y concluye «por tanto es suficiente tomar $p_2$». Pero $0{,}002604>0{,}002$: **esa cota no garantiza el error pedido**. El valor numérico $\frac{31}{32}$ es correcto, pero la justificación debe ser la de los pasos 7-8: $p_2=p_3$ y la cota de $R_3$ es $0{,}000163$. (Que el error real, $0{,}000162$, sea pequeño no sirve en el examen: el enunciado pide garantizarlo con el resto de Lagrange.)

**Receta.** (a) Derivadas cíclicas: escribir el ciclo y evaluar en $x_0$. (b) Tabular la cota $\frac{M}{(n+1)!}|x-x_0|^{n+1}$ para $n=0,1,2,\dots$ hasta que sea **menor** que la tolerancia. Si $f^{(n+1}(x_0)=0$, entonces $p_n=p_{n+1}$ y se puede usar la cota de $R_{n+1}$, que es mejor.
**Error típico.** Dar por buena una cota «casi» menor que la tolerancia, como hace X.

---

# Ejemplos propios (sencillo → difícil)

**P1 (propio, sencillo-medio: radio e intervalo).** Halla el centro, el radio y el intervalo de convergencia de $\displaystyle\sum_{n=1}^\infty\frac{(x-3)^n}{n\,2^n}$.
*Solución.*
1. **Centro** $x_0=3$; coeficientes $a_n=\frac1{n2^n}$.
2. **Cociente:** $\frac{a_{n+1}}{a_n}=\frac{n\,2^n}{(n+1)2^{n+1}}=\frac{n}{2(n+1)}\to\frac12$, luego $R=2$ y converge en $(1,5)$.
3. **Extremo $x=5$:** $\sum\frac{2^n}{n2^n}=\sum\frac1n$, la armónica, que diverge (U Ej. 1.35 p. 37).
4. **Extremo $x=1$:** $\sum\frac{(-2)^n}{n2^n}=\sum\frac{(-1)^n}{n}$, alternada con $\frac1n$ decreciente a $0$, que converge por Leibniz (U p. 41). Su suma es $-\ln2$.
5. **Intervalo de convergencia:** $[1,5)$. Verificado con sympy.

**Receta:** como en U Ej. 1.60 (pp. 68-69). Los dos extremos pueden comportarse de forma distinta.

**P2 (propio, sencillo: Taylor de $e^{2x}$ fuera del origen).** Serie de Taylor de $f(x)=e^{2x}$ centrada en $x_0=1$, y su radio.
*Solución.*
1. $f^{(n}(x)=2^ne^{2x}$ (U Ej. 3.13 p. 117), así que $f^{(n}(1)=2^ne^2$.
2. **Serie:** $\displaystyle e^{2x}=\sum_{n=0}^\infty\frac{2^ne^2}{n!}(x-1)^n=e^2\left[1+2(x-1)+2(x-1)^2+\tfrac43(x-1)^3+\cdots\right]$.
3. **Radio:** $\frac{2}{n+1}\to0$, luego $R=\infty$.
4. **Comprobación sin derivar:** $e^{2x}=e^2\cdot e^{2(x-1)}$; se sustituye $t=2(x-1)$ en $e^t=\sum\frac{t^n}{n!}$. Verificado con sympy.

**Receta:** cambiar de centro solo cambia dónde se evalúan las derivadas. A veces basta factorizar y sustituir en una serie conocida.

**P3 (propio, medio: sustitución y derivadas altas; U Ej. 3.15 pp. 118-119).** Desarrolla $f(x)=x^2\cos x^3$ en serie de potencias y calcula $f^{(8}(0)$ y $f^{(9}(0)$ **sin derivar**.
*Solución.*
1. $\cos t=\sum_{k\ge0}\frac{(-1)^k}{(2k)!}t^{2k}$ para todo $t$ (U Ej. 3.14 p. 117).
2. **Sustituimos $t=x^3$:** $\cos x^3=1-\frac{x^6}{2!}+\frac{x^{12}}{4!}-\cdots$
3. **Multiplicamos por $x^2$:** $f(x)=x^2-\frac{x^8}{2}+\frac{x^{14}}{24}-\frac{x^{20}}{720}+\cdots=\sum_{k\ge0}\frac{(-1)^k}{(2k)!}x^{6k+2}$, válido en todo $\mathbb R$.
4. **Derivadas en $0$:** en el intervalo de convergencia, $a_n=\frac{f^{(n}(0)}{n!}$ (U p. 118), es decir, $f^{(n}(0)=n!\,a_n$. El coeficiente de $x^8$ es $-\frac12$, luego $f^{(8}(0)=-\frac{8!}{2}=-20160$. No hay término en $x^9$, luego $f^{(9}(0)=0$.
5. **Comprobación** (segunda forma de U): $f=\frac{d}{dx}\left(\frac13\operatorname{sen}x^3\right)$, y derivando término a término la serie de $\frac13\operatorname{sen}x^3$ sale lo mismo. Verificado con sympy: también $f^{(8}(0)=-20160$ y $f^{(14}(0)=\frac{14!}{24}$.

**Receta:** sustituir en una serie conocida es mucho más rápido que derivar. Y la serie da **todas** las derivadas en el centro: $f^{(n}(x_0)=n!\cdot(\text{coeficiente de }(x-x_0)^n)$.

**P4 (propio, difícil: derivar series para sumar y para obtener desarrollos).**
(a) Calcula $\displaystyle\sum_{n=1}^\infty\frac{n}{2^n}$. (b) Demuestra que $\ln(1+x)=\displaystyle\sum_{n=1}^\infty\frac{(-1)^{n+1}}{n}x^n$ para $x\in(-1,1)$, usando solo derivación de series.
*Solución (a).*
1. Por E 3.18, $\sum_{n\ge1}nx^{n-1}=\frac1{(1-x)^2}$ para $|x|<1$.
2. Multiplicamos por $x$ (cada sumando por $x$): $\sum_{n\ge1}nx^n=\frac{x}{(1-x)^2}$.
3. $x=\frac12$ está dentro de $(-1,1)$: $\sum\frac n{2^n}=\frac{1/2}{1/4}=2$. Verificado con sympy. (Repitiendo el truco: $\sum\frac{n^2}{2^n}=6$.)

*Solución (b).*
1. Sea $S(x)=\sum_{n\ge1}\frac{(-1)^{n+1}}{n}x^n$. **Radio:** $\frac{n}{n+1}\to1$, luego $R=1$.
2. **Derivamos término a término** (Teor. 3.1 p. 116): $S'(x)=\sum_{n\ge1}(-1)^{n+1}x^{n-1}=1-x+x^2-\cdots=\frac1{1+x}$ (geométrica de razón $-x$).
3. **La función:** $g(x)=\ln(1+x)$ también cumple $g'(x)=\frac1{1+x}$.
4. **Misma derivada → difieren en una constante:** $h=S-g$ tiene $h'=0$ en $(-1,1)$, luego es constante (U Teor. 2.4 p. 97).
5. **Esa constante es 0:** $h(0)=S(0)-\ln1=0-0=0$. Por tanto $S(x)=\ln(1+x)$ en $(-1,1)$.
6. **Uso:** con $x=\frac12$ y 5 términos, $\ln\frac32\approx0{,}40729$. El valor real es $0{,}405465$. Verificado con sympy.

**Receta:** para «sumar» una serie, buscar una serie conocida cuya derivada (o la de $x$ por ella) sea la dada. Para demostrar un desarrollo: misma derivada y mismo valor en el centro implican misma función (U Teor. 2.4).
**Nota:** integrar término a término es el camino directo, pero en U aparece en el Tema 6 (Prop. 6.1 p. 280). Por eso aquí se usa solo derivación.

---

## (a) Teoría necesaria (U; páginas impresas verificadas en `ingenieros.txt`)

**Series numéricas (U §1.3):** serie geométrica, Ej. 1.33 p. 36 (suma $\frac{r}{1-r}$ desde $n=1$; la nota al margen generaliza). **Prop. 1.6** (si $\sum a_n$ converge, entonces $a_n\to0$), p. 36. Armónica, Ej. 1.35 p. 37. Criterio de Leibniz, p. 41. Criterios del cociente y de la raíz para series numéricas, p. 39. **Prop. 1.5** ($\left(1+\frac1{a_n}\right)^{a_n}\to e$ si $a_n\to\pm\infty$), p. 31.

**Series de potencias (U §1.5, pp. 67-70; la sección está fuera de examen, pero el radio se pregunta):** **Def. 1.29** (serie de potencias centrada en $x_0$), p. 67. Proposición de convergencia (convergencia absoluta y uniforme en $[-k,k]$, $k<|x_p|$) y los tipos 1-3, p. 67. Intervalo y radio de convergencia, Ej. 1.57-1.59, p. 68. Ej. 1.60 (intervalo $(-1,1]$), pp. 68-69. **Criterio de la raíz** y Ej. 1.61 ($R=3$), p. 70. **Criterio del cociente** y Ej. 1.62, p. 70.

**Tema 2:** regla de la cadena, p. 79. Derivadas laterales, Def. 2.3 p. 81. L'Hôpital, §2.3.2 p. 82. **Teor. 2.4** (caracterización de las funciones constantes), p. 97.

**U §3.2 (pp. 113-119):**
- 3.2.1 Motivación, p. 113.
- 3.2.2 (fuera de examen): Proposición sobre convergencia uniforme y derivabilidad, p. 114. **Ej. 3.11** ($\frac{x}{1+n^2x^2}$), pp. 114-115. Versión para series, p. 115.
- «Derivación de series de potencias» (examen): **Prop. 3.3**, **Teor. 3.1** y **Ej. 3.12** (derivar la serie del seno da la del coseno), p. 116.
- 3.2.3 Funciones analíticas: definición de serie de Taylor, **Ej. 3.13** ($e^{2x}$, $R=\infty$) y **Ej. 3.14** ($\cos x$), p. 117. Definición de función analítica, pp. 117-118. «Las funciones polinómicas, trigonométricas, exponenciales y logarítmicas son analíticas» y «una serie de potencias es la serie de Taylor de su suma» ($a_n=f^{(n}(0)/n!$), p. 118. **Ej. 3.15** ($x^2\cos x^3$ de dos formas), pp. 118-119.
- Autoevaluación del Tema 3, p. 139: la n.º 3 (es falsa: contraejemplo, U Ej. 3.11) y la n.º 4 (cierta en el intervalo **abierto** $(-R,R)$; en un extremo puede fallar: $\sum\frac{x^n}{n}$ converge en $x=-1$ y su derivada $\sum x^{n-1}$ no) son de esta unidad. U no da las soluciones.
- Anticipo: integración término a término, Prop. 6.1 y Ej. 6.47, p. 280 (Tema 6).

## (b) Huecos de U y dónde suplirlos

| Hueco | Dónde |
|---|---|
| Por qué los coeficientes son $\frac{f^{(n}(x_0)}{n!}$ (unicidad del desarrollo) | U lo esboza en p. 118. Mejor en S Teor. 5 p. 754 y L Teor. 9.22 p. 664. |
| Cuándo la serie de Taylor **suma** $f$ (resto $\to0$) | U solo lo afirma (p. 118). S Teor. 8 y desigualdad de Taylor (Teor. 9), p. 756; S Ej. 2 ($e^x$), p. 757; L Teor. 9.23, p. 666. |
| Tabla de series básicas ($\frac1{1-x}$, $e^x$, $\operatorname{sen}$, $\cos$, $\operatorname{arctg}$, $\ln(1+x)$, binomial) con sus radios | S Tabla 1, p. 762. Serie binomial, S Teor. 17 p. 761. |
| Método paso a paso para obtener series de Taylor | L, «Directrices», p. 668. L Ej. 3 ($\operatorname{sen}x^2$ por sustitución), p. 668. |
| Que una serie de Taylor puede converger a otra función, o solo en un intervalo pequeño (aviso de L) | L p. 666 («no se puede concluir que la serie de potencias converge a sen x»). El ejemplo clásico $e^{-1/x^2}$ no está en U (explicación propia, si se incluye). |

## (c) Erratas, omisiones y avisos

**Erratas u omisiones de E:**
1. **E 3.18 (p. 105):** «la serie geométrica … converge uniformemente en $(-1,1)$» es **falso** (el resto $\frac{x^{N+1}}{1-x}$ no está acotado). La justificación correcta es U Prop. 3.3 / Teor. 3.1. Además, la forma $\sum_{n=0}nx^{n-1}$ contiene $0\cdot x^{-1}$.
2. **E 3.20 (p. 106):** «el desarrollo de Taylor de $f$ en $x=0$ de orden $n$ es $f(x)=1-kx+\dots+(-1)^n\frac{k\cdots(k+n-1)}{n!}x^n$»: esa suma es $p_n(x)$, no $f(x)$. Omite además los extremos ($x=\pm1$: divergen) y la prueba de que la serie suma $f$.
3. **E 3.15 (p. 102):** la no convergencia uniforme de $\{f_n'\}$ solo se «ilustra» con la figura 3.2. Argumento: en $x=1/\sqrt n$, $f_n'=1/\sqrt2$.
4. **E 3.19 (p. 106):** no justifica que la serie sume $e^x$ (U lo afirma en p. 118). No es un error, porque no se pedía.

**Solo de extracción (no son erratas):** 3.15 «si $x=0$» es $x\neq0$; 3.16 «$\frac\pi2=0$» es $\neq$; 3.17 «e−nxn» es $e^{-n}x^n$ (comprobado en la imagen de E p. 104); U Ej. 3.11 p. 115 pierde los $\neq$.

**Erratas u omisiones de X:**
1. **X p. 146 (Feb. 2018, 1ª sem., Ej. 5b):** la cota con $n=2$ es $0{,}002604>0{,}002$ y X dice que «es suficiente». Corrección: $p_2=p_3$ y la cota de $R_3$ es $0{,}000163<0{,}002$. El resultado $\frac{31}{32}=0{,}96875$ es correcto.
2. **X p. 113 (Ej. 4):** del «mismo radio» no se deduce el intervalo; faltan los extremos (divergen, así que la respuesta C sí es la correcta).
3. **X p. 142 (P3):** no da el radio ($\infty$).
4. **X p. 105 (Ej. 6):** el cociente $\frac{\ln(n+1)}{\ln n}$ no está definido en $n=1$ (porque $a_0=\ln1=0$). Es inofensivo, porque el límite solo depende de $n$ grande.

**Precisiones de U:**
- **Teor. 3.1 (p. 116):** «en su intervalo de convergencia» debe leerse «en el **interior** $(-R,R)$». U llama intervalo de convergencia también a conjuntos con extremos (Ej. 1.60, $(-1,1]$), y en un extremo la derivada puede no converger.
- **Criterio del cociente (p. 70):** U escribe $\lim_{n\to\infty}\frac{a_n}{a_{n-1}}$ sin valor absoluto, pero hay que tomar $\left|\frac{a_n}{a_{n-1}}\right|$ (así lo pone E en el margen de p. 104). Los «$S=0$ y $S=\infty$» del `.txt` son «$S\neq0$, $S\neq\infty$».

**Aviso sobre el dossier:** el dossier afirma que $p_3(\frac14)=0{,}968913$. **Es incorrecto**: $p_3=p_2$ para $\cos x$ en $0$ y vale $0{,}96875$. El valor $0{,}968913$ es $p_4(\frac14)=\frac{5953}{6144}$.

## (d) Figuras

| Libro | Pág. PDF (impresa) | Contenido | Uso |
|---|---|---|---|
| E | 101 (101) | Figura 3.1: $f_1,f_5,f_{50}$ de $\sqrt{x^2+1/n}$ acercándose a $\lvert x\rvert$ | Ej. 3.15 (fuera de examen) |
| E | 102 (102) | Figura 3.2: las derivadas $f_n'$ (tienden a una función con salto) | Ej. 3.15 |
| E | 103 (103) | Figura 3.3: $\operatorname{arctg}(x/n)$ | Ej. 3.16 |
| S | (p. 762) | Tabla 1 de series de Maclaurin | Chuleta (recortar con `list`/`crop`; comprobar la página PDF por la cabecera) |

Para la intuición «la serie de Taylor es el límite de los polinomios», sirven las figuras ya propuestas en la unidad 3.1 ($\operatorname{sen}x$ con $p_3,p_5$, U p. 112; S p. 771, Fig. 6).
