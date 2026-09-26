# Soluciones — Tema 2.2 «Reglas de derivación»

Ejercicios de **E** (Libro de ejercicios, impresa = PDF): 2.3, 2.4, 2.5, 2.10, 2.11, 2.12, 2.13, 2.15, 2.16 (E pp. 52-61).
Teoría: **U** §2.2 «Reglas de derivación», pp. 78-81 (impresa = PDF + 2). Enunciados comprobados sobre el PDF renderizado (pdftotext pierde raíces e índices de raíz).
Todos los resultados se han verificado con sympy (derivadas simbólicas, comparación numérica en varios puntos y límites laterales en los puntos dudosos).

**Orden de estudio propuesto (de fácil a difícil):** 2.3 → 2.11 → 2.4 → 2.12 → 2.5 → 2.10 → 2.16 → 2.13 → 2.15.
(Primero una regla cada vez; luego la cadena anidada; luego dominios; por último, funciones del tipo $f(x)^{g(x)}$ e inversas.)

> **Herramientas de U que se usan** (detalle en «Teoría necesaria», al final):
> Prop. 2.1 (suma, producto, cociente) y Regla de la cadena, U §2.2.2 p. 79; tabla de derivadas elementales, U p. 79; derivada de $\operatorname{tg}$ y de $\arcsin$ (Ej. 2.6), U p. 80; tabla «con la cadena» ($u(x)$), U p. 80; Def. 2.1 de derivada, U p. 75; Def. 2.2 (función derivada y su dominio), U p. 78.

---

## Ejercicio 2.3 (E p. 52)

> **Calcula las derivadas de las funciones dadas por $f(x)=\operatorname{sen}x\cos x$ y $g(x)=\sec x$.**

### Solución

**Parte $f$.**

1. **Identificar la estructura.** $f$ es el *producto* de dos funciones, $u(x)=\operatorname{sen}x$ y $v(x)=\cos x$. Ambas son derivables en todo $\mathbb R$ con $u'=\cos x$, $v'=-\operatorname{sen}x$ (tabla de derivadas, U p. 79).
2. **Aplicar la regla del producto** (U Prop. 2.1, p. 79): $(u v)'=u'v+uv'$. Por eso
   $$f'(x)=\cos x\cdot\cos x+\operatorname{sen}x\cdot(-\operatorname{sen}x)=\cos^2x-\operatorname{sen}^2x .$$
3. **Comprobación por otro camino.** Por la fórmula del ángulo doble, $\operatorname{sen}(2x)=2\operatorname{sen}x\cos x$, luego $f(x)=\tfrac12\operatorname{sen}(2x)$. La constante sale fuera (caso particular de la regla del producto con un factor constante, cuya derivada es 0, U Ej. 2.1 p. 76) y, por la cadena con $u(x)=2x$ (tabla con $u(x)$, U p. 80):
   $$f'(x)=\tfrac12\cos(2x)\cdot 2=\cos(2x).$$
4. **¿Son distintas?** No: $\cos(2x)=\cos^2x-\operatorname{sen}^2x$ (identidad trigonométrica). Dos caminos correctos dan siempre la misma función, aunque *con distinto aspecto*.

**Parte $g$.**

5. **Reescribir con funciones de la tabla.** $\sec x=\dfrac1{\cos x}$. Solo tiene sentido donde $\cos x\neq0$, es decir, para $x\neq\frac\pi2+k\pi$, $k\in\mathbb Z$. Ese es el dominio de $g$.
6. **Regla del cociente** (U Prop. 2.1, p. 79; exige denominador no nulo, justo lo que asegura el paso 5):
   $$g'(x)=\frac{0\cdot\cos x-1\cdot(-\operatorname{sen}x)}{\cos^2x}=\frac{\operatorname{sen}x}{\cos^2x}=\frac1{\cos x}\cdot\frac{\operatorname{sen}x}{\cos x}=\sec x\,\operatorname{tg}x .$$
7. **Otro camino (cadena).** $g(x)=(\cos x)^{-1}$ es la función $t\mapsto t^{-1}$ compuesta con $\cos x$. Por la fila $(u(x))^c$ de la tabla (U p. 80) con $c=-1$:
   $$g'(x)=(-1)(\cos x)^{-2}(-\operatorname{sen}x)=\sec x\,\operatorname{tg}x.$$
8. **Dominio de $g'$.** $g'$ existe en todo el dominio de $g$: $\mathbb R\setminus\{\frac\pi2+k\pi\}$.

**Resultado:** $f'(x)=\cos^2x-\operatorname{sen}^2x=\cos 2x$; $\;g'(x)=\sec x\operatorname{tg}x$ para $x\neq\frac\pi2+k\pi$.

**Receta.** Antes de derivar, pregúntate «¿qué operación es la *última* que se hace?» (producto, cociente, composición). Esa decide la regla. Las funciones que no están en la tabla ($\sec$, $\operatorname{cotg}$, $\operatorname{tg}$…) se reescriben con $\operatorname{sen}$ y $\cos$.

**Error típico.** Pensar que $(uv)'=u'v'$: aquí daría $\cos x\cdot(-\operatorname{sen}x)$, que es falso. También, tomar como distintas dos respuestas equivalentes ($\cos 2x$ frente a $\cos^2x-\operatorname{sen}^2x$).

*Teoría:* U §2.2.2 Prop. 2.1 y Regla de la cadena, p. 79; tablas, pp. 79-80.

---

## Ejercicio 2.11 (E p. 58)

> **Señale la derivada de la función dada por $h(x)=\operatorname{cotg}x^3$:**
> **a)** $h'(x)=\dfrac{-3x^2}{\operatorname{sen}^2x^3}$. **b)** $h'(x)=\dfrac{-1}{\operatorname{sen}^2x^3}$. **c)** $h'(x)=\dfrac{3x^2}{\operatorname{sen}x}$.

### Solución

1. **Leer bien.** $\operatorname{cotg}x^3$ significa $\operatorname{cotg}(x^3)$: primero se eleva al cubo y luego se aplica la cotangente. Es una **composición** $h=F\circ u$ con $u(x)=x^3$ y $F(t)=\operatorname{cotg}t$.
2. **Derivada de la función exterior.** U no trae $\operatorname{cotg}$ en la tabla (U p. 79), así que se obtiene como la de $\operatorname{tg}$ en U p. 80: $\operatorname{cotg}t=\dfrac{\cos t}{\operatorname{sen}t}$ (definida si $\operatorname{sen}t\neq0$). Por la regla del cociente (U Prop. 2.1, p. 79):
   $$(\operatorname{cotg}t)'=\frac{(-\operatorname{sen}t)\operatorname{sen}t-\cos t\cos t}{\operatorname{sen}^2t}=\frac{-(\operatorname{sen}^2t+\cos^2t)}{\operatorname{sen}^2t}=\frac{-1}{\operatorname{sen}^2t}.$$
3. **Derivada de la interior.** $u'(x)=3x^2$ (tabla, $x^c$ con $c=3$, U p. 79).
4. **Regla de la cadena** (U p. 79): $h'(x)=F'(u(x))\,u'(x)$:
   $$h'(x)=\frac{-1}{\operatorname{sen}^2(x^3)}\cdot 3x^2=\frac{-3x^2}{\operatorname{sen}^2x^3},$$
   válida donde $\operatorname{sen}(x^3)\neq0$, es decir, $x^3\neq k\pi$.
5. **Descartar opciones.** b) olvida multiplicar por $u'(x)=3x^2$; c) tiene signo y denominador incorrectos. **Correcta: a).**

**Receta.** En una composición, deriva «de fuera hacia dentro»: derivada de la exterior **evaluada en la interior**, por la derivada de la interior.

**Error típico.** La opción b): derivar la función exterior y olvidar el factor $u'(x)$ («olvidar la cadena»).

*Teoría:* U p. 79 (cociente, cadena), U p. 80 (derivada de $\operatorname{tg}$ como modelo).

---

## Ejercicio 2.4 (E p. 53)

> **Calcula la derivada de la función dada por $h(x)=\operatorname{sen}\big((1+\cos x)^2\big)$.**

### Solución

1. **Desmontar la función en capas** (de dentro hacia fuera):
   $u(x)=1+\cos x\;\to\; v(u)=u^2\;\to\;F(v)=\operatorname{sen}v$. Así $h=F\circ v\circ u$. Todas son derivables en $\mathbb R$, luego $h$ también (la cadena, aplicada dos veces).
2. **Capa exterior** (cadena, U p. 79): $h'(x)=\cos\big((1+\cos x)^2\big)\cdot\big[(1+\cos x)^2\big]'$.
3. **Capa intermedia**: $\big[(1+\cos x)^2\big]'=2(1+\cos x)\cdot(1+\cos x)'$ (fila $(u(x))^c$, U p. 80, con $c=2$).
4. **Capa interior**: $(1+\cos x)'=0+(-\operatorname{sen}x)=-\operatorname{sen}x$ (regla de la suma, U Prop. 2.1; derivada de una constante, U Ej. 2.1 p. 76; tabla p. 79).
5. **Juntar**:
   $$h'(x)=\cos\big((1+\cos x)^2\big)\cdot2(1+\cos x)\cdot(-\operatorname{sen}x)=-2\operatorname{sen}x\,(1+\cos x)\cos\big((1+\cos x)^2\big).$$

**Receta.** Con varias composiciones, escribe explícitamente las capas $u,v,F$ y multiplica una derivada por capa, cada una evaluada en lo que tiene dentro. Cuenta: 3 capas ⇒ 3 factores.

**Error típico.** Derivar dos capas a la vez y perder un factor (por ejemplo, olvidar el $-\operatorname{sen}x$), o escribir $\cos(1+\cos x)^2$ cambiando el argumento del coseno.

*Teoría:* U p. 79 (suma, cadena), p. 80 (tabla con $u(x)$).

---

## Ejercicio 2.12 (E p. 59)

> **De la función $g$ se sabe que es derivable en todo $\mathbb R$ y además verifica que $g'(2)=3$. Calcula el valor de $f'(1)$ para la función $f$ dada por $f(x)=g(2x^a)$, en función del parámetro $a\in[1,\infty)$.**

### Solución

1. **Idea.** No conocemos $g$, pero la regla de la cadena solo necesita $g'$ **en un punto concreto**: el valor de la función interior en $x=1$.
2. **Función interior.** $u(x)=2x^a$. En un entorno de $x=1$ se tiene $x>0$, y ahí $x^a$ es derivable con $(x^a)'=ax^{a-1}$ para cualquier $a\in\mathbb R$ (tabla, U p. 79). Por la regla de la constante por función, $u'(x)=2ax^{a-1}$. Además $u(1)=2\cdot1^a=2$.
3. **Hipótesis de la cadena** (U p. 79): $u$ derivable en $1$ y $g$ derivable en $u(1)=2$ (cierto, $g$ es derivable en todo $\mathbb R$). Entonces
   $$f'(1)=g'(u(1))\,u'(1)=g'(2)\cdot2a\cdot1^{a-1}=3\cdot2a=6a.$$

**Resultado:** $f'(1)=6a$.

**Observación (errata de E).** E afirma que «$x^a$ es derivable en todo $\mathbb R$, para todo $a\in[1,\infty)$». Es falso si $a$ no es entero: por ejemplo $x^{3/2}$ ni siquiera está definida para $x<0$. No afecta al resultado porque solo hace falta derivabilidad **cerca de $x=1$**, donde $x>0$. La restricción $a\ge1$ tampoco es necesaria: $f'(1)=6a$ vale para todo $a\in\mathbb R$.

**Receta.** Con una función «desconocida» $g$ dentro de una composición, aplica la cadena en general, sustituye el punto y comprueba que el argumento de $g'$ es justamente el punto donde te dan el dato.

**Error típico.** Escribir $f'(1)=g'(1)\cdots$ (evaluar $g'$ en el punto de $x$ en vez de en $u(1)=2$), o pensar que «faltan datos».

*Teoría:* U p. 79 (cadena, tabla $x^c$).

---

## Ejercicio 2.5 (E p. 54)

> **Calcula la derivada de la función dada por $f(x)=\operatorname{sen}\!\big(e^{x^2}+(x+1)\ln x^2\big)$.**

### Solución

1. **Dominio.** $\operatorname{sen}$ y $e^{t}$ están definidas en todo $\mathbb R$; $\ln t$ solo para $t>0$. Aquí $t=x^2>0\iff x\neq0$. Por tanto $\operatorname{dom}f=\mathbb R\setminus\{0\}$.
2. **Capa exterior.** $f=\operatorname{sen}\circ G$ con $G(x)=e^{x^2}+(x+1)\ln x^2$. Por la cadena (U p. 79):
   $$f'(x)=\cos\big(G(x)\big)\cdot G'(x).$$
3. **Derivar $G$ sumando a sumando** (regla de la suma, U Prop. 2.1):
   - $\big(e^{x^2}\big)'=e^{x^2}\cdot2x$ (fila $e^{u(x)}$, U p. 80).
   - $\big((x+1)\ln x^2\big)'$ es un **producto**: $1\cdot\ln x^2+(x+1)\cdot(\ln x^2)'$.
   - $(\ln x^2)'=\dfrac{1}{x^2}\cdot2x=\dfrac2x$ (fila $\ln u(x)$, U p. 80). Vale para $x>0$ **y** para $x<0$.
   - Por tanto $\big((x+1)\ln x^2\big)'=\ln x^2+\dfrac{2(x+1)}{x}=\ln x^2+2+\dfrac2x$.
4. **Resultado** (para $x\neq0$):
   $$f'(x)=\cos\!\big(e^{x^2}+(x+1)\ln x^2\big)\Big(2xe^{x^2}+\ln x^2+2+\frac2x\Big).$$
5. **Dominio de $f'$.** La expresión tiene sentido para todo $x\neq0$ y en todos esos puntos se han aplicado reglas válidas: $\operatorname{dom}f'=\mathbb R\setminus\{0\}=\operatorname{dom}f$.

**Receta.** Empieza por el dominio; después, «cadena por fuera, suma/producto por dentro», anotando cada subderivada aparte antes de juntarlas.

**Error típico.** Simplificar $\ln x^2=2\ln x$: solo vale para $x>0$ (para $x<0$, $\ln x$ no existe). Lo correcto es $\ln x^2=2\ln|x|$. Derivar como $\ln u(x)$, como aquí, evita el problema.

*Teoría:* U p. 79 (Prop. 2.1, cadena), p. 80 (tabla con $u(x)$).

---

## Ejercicio 2.10 (E p. 57)

> **Compare el dominio de las funciones dadas por $f(x)=\sqrt{2+\sqrt[3]{x}}$ y $g(x)=e^{\frac{x}{x+1}}$, con el de las funciones que se obtienen al aplicar las reglas de derivación a $f(x)$ y $g(x)$. Represente gráficamente $f$ y $g$ utilizando Maxima.**

### Solución

**Función $f$.**

1. **Dominio de $f$.** $\sqrt[3]{x}$ existe para todo $x\in\mathbb R$ (raíz de índice impar). La raíz cuadrada exige radicando $\ge0$:
   $$2+\sqrt[3]{x}\ge0\iff\sqrt[3]{x}\ge-2\iff x\ge-8,$$
   donde el último paso es válido porque $t\mapsto t^3$ es estrictamente creciente (se puede elevar al cubo conservando la desigualdad). Así $\operatorname{dom}f=[-8,+\infty)$.
2. **Derivada de $\sqrt[3]{x}$.** Para $x>0$, $\sqrt[3]{x}=x^{1/3}$ y la tabla (U p. 79) da $\frac13x^{-2/3}=\dfrac1{3\sqrt[3]{x^2}}$. Para $x<0$, $\sqrt[3]{x}=-(-x)^{1/3}$ y por la cadena se obtiene la misma expresión $\dfrac{1}{3\sqrt[3]{x^2}}$. En $x=0$ la expresión no existe: hay que volver a la definición (U Def. 2.1, p. 75): $\dfrac{\sqrt[3]{h}-0}{h}=h^{-2/3}\to+\infty$, **no es finito**, luego $\sqrt[3]{\cdot}$ no es derivable en 0.
3. **Cadena** (U p. 79; $(\sqrt t)'=\frac1{2\sqrt t}$ es la fila $x^c$ con $c=\frac12$, válida para $t>0$):
   $$f'(x)=\frac{1}{2\sqrt{2+\sqrt[3]{x}}}\cdot\frac{1}{3\sqrt[3]{x^2}}=\frac{1}{6\sqrt{2+\sqrt[3]{x}}\,\sqrt[3]{x^2}},$$
   válida cuando $2+\sqrt[3]{x}>0$ (es decir $x>-8$) y $x\neq0$.
4. **Los puntos dudosos, con la definición.** Que la *fórmula* no exista en un punto **no prueba** por sí solo que $f$ no sea derivable allí (ver el ejemplo propio P4b). Hay que comprobarlo:
   - En $x=0$: $\dfrac{f(h)-f(0)}{h}=\dfrac{\sqrt{2+\sqrt[3]h}-\sqrt2}{h}\to+\infty$ (tangente vertical; verificado con sympy). No derivable.
   - En $x=-8$ (solo tiene sentido por la derecha): $\dfrac{f(-8+h)-0}{h}=\dfrac{\sqrt{2+\sqrt[3]{-8+h}}}{h}\to+\infty$ cuando $h\to0^+$. No derivable.
5. **Conclusión para $f$.** $\operatorname{dom}f'=(-8,0)\cup(0,+\infty)\subsetneq\operatorname{dom}f=[-8,+\infty)$.

**Función $g$.**

6. **Dominio de $g$.** La exponencial está definida en todo $\mathbb R$; el exponente $\frac{x}{x+1}$ exige $x\neq-1$. $\operatorname{dom}g=\mathbb R\setminus\{-1\}$.
7. **Derivada.** Cadena con $e^{u(x)}$ (U p. 80) y cociente (U p. 79):
   $$g'(x)=e^{\frac{x}{x+1}}\cdot\frac{1\cdot(x+1)-x\cdot1}{(x+1)^2}=\frac{e^{\frac{x}{x+1}}}{(x+1)^2}.$$
8. **Dominio de $g'$.** Todas las reglas usadas son válidas en cada $x\neq-1$: $\operatorname{dom}g'=\mathbb R\setminus\{-1\}=\operatorname{dom}g$.
9. **Gráficas con Maxima.** Con `plot2d(sqrt(2+x^(1/3)),[x,-8,20])`, Maxima interpreta $x^{1/3}$ como número complejo para $x<0$ y no dibuja esa parte. Es mejor usar la raíz real `signum(x)*abs(x)^(1/3)` en lugar de `x^(1/3)`. Para $g$: `plot2d(exp(x/(x+1)),[x,-5,5],[y,0,10])`.

**Receta.** (1) Dominio de $f$: condiciones de cada «pieza delicada» (raíz par ⇒ radicando $\ge0$; denominador $\neq0$; logaritmo ⇒ argumento $>0$). (2) Deriva con las reglas. (3) En los puntos del dominio de $f$ donde la fórmula de $f'$ falla, decide con la **definición** (cociente incremental). Siempre $\operatorname{dom}f'\subseteq\operatorname{dom}f$ (U Def. 2.2, p. 78).

**Error típico.** Dar como dominio de $f'$ «donde tiene sentido la fórmula» sin más, o incluir $x=-8$ porque «está en el dominio de $f$».

**Omisión de E.** E deduce $\operatorname{dom}f'$ solo mirando dónde se anula el denominador de la fórmula. El resultado es correcto, pero el argumento es incompleto: hay que estudiar $x=0$ y $x=-8$ con la definición (paso 4). También hay una errata ortográfica: «unicamente».

*Teoría:* U Def. 2.1 p. 75, Def. 2.2 p. 78, Prop. 2.1 y cadena p. 79, tabla p. 80.

---

## Ejercicio 2.16 (E p. 61)

> **Calcula el valor de la derivada de $f:(0,+\infty)\to\mathbb R$ dada por $f(x)=\sqrt[x]{x}$.**

*(Comprobado en el PDF: es la raíz **$x$-ésima** de $x$, es decir $f(x)=x^{1/x}$, **no** $x^{\sqrt x}$; pdftotext pierde el índice de la raíz. La función $x^{\sqrt x}$ se resuelve como ejemplo propio P3.)*

### Solución

1. **Reescribir como potencia.** $\sqrt[x]{x}=x^{1/x}$.
2. **¿Por qué no sirve la tabla directamente?** La fila $x^c$ (U p. 79) exige exponente **constante**, y la fila $a^x$ exige base **constante**. Aquí varían la base y el exponente, así que ninguna fila se aplica tal cual.
3. **Truco: escribir la función como una exponencial.** Para $x>0$, $x=e^{\ln x}$, luego
   $$f(x)=x^{1/x}=e^{\frac{\ln x}{x}}.$$
   (Equivale a lo que hace E, «tomar logaritmos»: $\ln f(x)=\frac1x\ln x$, lo que es posible porque $f(x)>0$.)
4. **Derivar el exponente** $u(x)=\dfrac{\ln x}{x}$ por la regla del cociente (U p. 79):
   $$u'(x)=\frac{\frac1x\cdot x-\ln x\cdot1}{x^2}=\frac{1-\ln x}{x^2}.$$
   (E lo escribe como $-\frac{1}{x^2}\ln x+\frac1{x^2}$ derivando $\frac1x\cdot\ln x$ como producto; es lo mismo.)
5. **Cadena con $e^{u(x)}$** (U p. 80):
   $$f'(x)=e^{u(x)}u'(x)=x^{1/x}\,\frac{1-\ln x}{x^2},\qquad x>0.$$
6. **Comprobación de sentido.** $f'(x)>0$ si $x<e$ y $f'(x)<0$ si $x>e$: $x^{1/x}$ crece hasta $x=e$ y luego decrece (su máximo es $e^{1/e}$). Esto encaja con U Ej. 2.12, p. 84, donde se prueba que $x^{1/x}\to1$ cuando $x\to\infty$.

**Resultado:** $f'(x)=x^{1/x}\,\dfrac{1-\ln x}{x^2}$ (E da la forma equivalente $x^{1/x}\big[\frac{-1}{x^2}\ln x+\frac1{x^2}\big]$).

**Receta (derivación logarítmica).** Si la variable está **en la base y en el exponente**, $f=A(x)^{B(x)}$ con $A>0$: escribe $f=e^{B\ln A}$ (o toma $\ln f=B\ln A$ y deriva ambos lados). Así, $f'=f\cdot\big(B\ln A\big)'$.

**Error típico.** Aplicar la regla de la potencia, $(x^{1/x})'=\frac1x x^{\frac1x-1}$, o la de la exponencial, $x^{1/x}\ln x\cdot(\frac1x)'$. Las dos son incorrectas porque cada una trata como constante algo que no lo es (el resultado correcto es justo la **suma** de las dos). Otro error: despejar $f'$ y olvidar multiplicar por $f(x)$.

*Teoría:* U p. 79 (cociente), p. 80 (tabla $e^{u(x)}$); el paso a logaritmos solo aparece en U para límites (Ej. 2.12, p. 84). Derivación logarítmica: S §3.6 pp. 220-222; L §5.1 p. 323 (Ej. 6).

---

## Ejercicio 2.13 (E p. 59)

> **Determina el dominio y calcula la derivada de la función dada por $f(x)=\arccos\sqrt{x}$.**

### Solución

1. **Qué es $\arccos$.** El coseno no es inyectivo en $\mathbb R$, pero sí es estrictamente decreciente en $[0,\pi]$ y toma allí todos los valores de $[-1,1]$. Por eso tiene inversa $\arccos:[-1,1]\to[0,\pi]$ (convenio de U p. 62 y de E p. 59): $\arccos y$ es el **único** $\alpha\in[0,\pi]$ con $\cos\alpha=y$.
2. **Dominio de $f$.** Se necesita $x\ge0$ (para $\sqrt x$) y $\sqrt x\in[-1,1]$, es decir, $0\le\sqrt x\le1\iff0\le x\le1$. $\operatorname{dom}f=[0,1]$.
3. **Derivada de $\arccos$** (mismo método que U Ej. 2.6, p. 80, para $\arcsin$). Para $t\in[0,\pi]$, $\arccos(\cos t)=t$. Suponiendo que $\arccos$ es derivable en $\cos t$ (lo garantiza el teorema de la función inversa, que U no enuncia: ver L Teor. 5.8-5.9, p. 341), derivamos ambos miembros con la cadena:
   $$\arccos'(\cos t)\cdot(-\operatorname{sen}t)=1\;\Rightarrow\;\arccos'(\cos t)=\frac{-1}{\operatorname{sen}t}.$$
   Esto exige $\operatorname{sen}t\neq0$, es decir, $t\in(0,\pi)$. **En $(0,\pi)$ es $\operatorname{sen}t>0$**, así que $\operatorname{sen}t=+\sqrt{1-\cos^2t}$ (es aquí donde importa haber elegido $[0,\pi]$). Llamando $y=\cos t\in(-1,1)$:
   $$\arccos'(y)=\frac{-1}{\sqrt{1-y^2}},\qquad y\in(-1,1).$$
4. **Cadena** con $u(x)=\sqrt x$, $u'(x)=\dfrac1{2\sqrt x}$ ($x>0$), y $u(x)\in(-1,1)\iff x<1$:
   $$f'(x)=\frac{-1}{\sqrt{1-(\sqrt x)^2}}\cdot\frac1{2\sqrt x}=\frac{-1}{\sqrt{1-x}\;2\sqrt x}=\frac{-1}{2\sqrt{x-x^2}},\qquad 0<x<1.$$
   (Se ha usado $\sqrt a\sqrt b=\sqrt{ab}$ para $a,b\ge0$.)
5. **Extremos del intervalo.** En $x=0$ y $x=1$ la fórmula no existe. Con la definición (U Def. 2.1), las derivadas laterales valen $-\infty$ (tangentes verticales). Por ejemplo, cerca de 1 se tiene $f(1-h)\approx\sqrt h$ y el cociente incremental es $\approx-\frac{1}{\sqrt h}\to-\infty$. No es derivable. Por tanto $\operatorname{dom}f'=(0,1)$.

**Resultado:** $\operatorname{dom}f=[0,1]$; $f'(x)=\dfrac{-1}{2\sqrt{x-x^2}}$ en $(0,1)$.

**Receta (derivada de una inversa sin fórmula).** Escribe $f^{-1}(f(t))=t$, deriva con la cadena, despeja $(f^{-1})'(f(t))$, expresa el resultado en función de $y=f(t)$ con una identidad (aquí $\operatorname{sen}^2+\cos^2=1$) y **elige el signo de la raíz según el intervalo** donde se invierte.

**Error típico.** Escribir $\operatorname{sen}t=\pm\sqrt{1-\cos^2t}$ sin decidir el signo (o tomar $+$ sin justificarlo); olvidar el signo menos de $\arccos'$; dar $[0,1]$ como dominio de $f'$.

**Omisión de E.** E divide por $\operatorname{sen}x$ y toma la raíz positiva sin decir que eso exige $x\in(0,\pi)$. Tampoco indica el dominio de $f'$ (que es $(0,1)$ y no $[0,1]$) y da por supuesto que $\arccos$ es derivable, algo que ni E ni U demuestran.

*Teoría:* U p. 62 (convenio $\arccos:[-1,1]\to[0,\pi]$), U Ej. 2.6 p. 80 (método, para $\arcsin$), U p. 79 (cadena). Complementos: L Teor. 5.16 p. 369; S §3.5 p. 214.

---

## Ejercicio 2.15 (E p. 60)

> **Señala el valor de la derivada de la función inversa de $f(x)=x^5+x^3+x$ en el punto $y=3$:**
> **a)** $(f^{-1})'(3)=6$. **b)** $(f^{-1})'(3)=9$. **c)** $(f^{-1})'(3)=\frac16$. **d)** $(f^{-1})'(3)=\frac19$.

### Solución

1. **¿Existe $f^{-1}$?** Hace falta que $f$ sea **inyectiva**. $f'(x)=5x^4+3x^2+1\ge1>0$ para todo $x$, luego $f$ es estrictamente creciente en $\mathbb R$ (U Prop. 2.4, §2.5.4, p. 98, consecuencia del Teorema del valor medio) y, por tanto, inyectiva. Sin ese resultado también se ve directamente: $x^5$, $x^3$ y $x$ son estrictamente crecientes, y su suma también lo es.
2. **¿Dónde está definida $f^{-1}$?** $f$ es continua (polinomio), $f(x)\to-\infty$ cuando $x\to-\infty$ y $f(x)\to+\infty$ cuando $x\to+\infty$. Por el Teorema de los valores intermedios (U p. 52), toma todos los valores reales: $f^{-1}:\mathbb R\to\mathbb R$.
3. **Fórmula de la derivada de la inversa.** Como $f'(x)\neq0$, $f^{-1}$ es derivable (teorema de la función inversa: L Teor. 5.9, p. 341; U no lo enuncia). Derivando $f^{-1}(f(x))=x$ con la cadena (U p. 79):
   $$(f^{-1})'(f(x))\cdot f'(x)=1\;\Rightarrow\;(f^{-1})'(f(x))=\frac1{f'(x)}=\frac1{5x^4+3x^2+1}.$$
4. **Buscar el $x$ que corresponde a $y=3$.** Hay que resolver $x^5+x^3+x=3$. Se prueba $x=1$: $1+1+1=3$. Es la **única** solución porque $f$ es inyectiva (paso 1). Es decir, $f^{-1}(3)=1$.
5. **Sustituir.** $(f^{-1})'(3)=\dfrac{1}{f'(1)}=\dfrac{1}{5+3+1}=\dfrac19$. **Opción d).**

**Receta.** $(f^{-1})'(y_0)=\dfrac{1}{f'(x_0)}$ con $f(x_0)=y_0$. Los pasos son: (i) comprobar que $f$ es inyectiva y que $f'(x_0)\neq0$; (ii) hallar $x_0$ resolviendo $f(x)=y_0$ (probar valores sencillos: $0,\pm1,\pm2$); (iii) invertir la derivada.

**Error típico.** Evaluar en el punto equivocado, $\frac1{f'(3)}=\frac1{433}$, o no invertir y responder $f'(1)=9$ (opción b, que es la trampa del test).

**Comentario.** E usa «$f'>0$ ⇒ estrictamente creciente» (en U es la Prop. 2.4 de §2.5.4, p. 98, posterior a este tema) y la derivabilidad de $f^{-1}$, que ni U ni E demuestran. Ambas se pueden citar; lo más fácil es justificar la inyectividad como al final del paso 1.

*Teoría:* U p. 79 (cadena), U p. 52 (valores intermedios), U p. 98 (Prop. 2.4). Complementos: L §5.3 Teor. 5.9 y Ej. 5, p. 341 (ejemplo casi idéntico); S §3.5, ejercicio 77, p. 217.

---

## Ejemplos propios (dificultad creciente)

### P1 (propio, fácil): cociente con simplificación
**Deriva $f(x)=\dfrac{\operatorname{sen}x}{1+\cos x}$.**

1. Dominio: $1+\cos x\neq0\iff x\neq\pi+2k\pi$.
2. Cociente (U p. 79): $f'(x)=\dfrac{\cos x(1+\cos x)-\operatorname{sen}x(-\operatorname{sen}x)}{(1+\cos x)^2}=\dfrac{\cos x+\cos^2x+\operatorname{sen}^2x}{(1+\cos x)^2}$.
3. Como $\cos^2x+\operatorname{sen}^2x=1$: $f'(x)=\dfrac{1+\cos x}{(1+\cos x)^2}=\dfrac1{1+\cos x}$ (se puede simplificar porque $1+\cos x\neq0$).

*Verificado con sympy.* **Moraleja:** después de derivar, busca identidades ($\operatorname{sen}^2+\cos^2=1$) que simplifiquen el resultado.

### P2 (propio, media): derivada de una inversa
**(a) Deduce $(\operatorname{arctg})'(y)$. (b) Si $f(x)=x+e^x$, calcula $(f^{-1})'(1)$.**

(a) $\operatorname{tg}:(-\frac\pi2,\frac\pi2)\to\mathbb R$ es biyectiva y $\operatorname{tg}'(t)=\frac1{\cos^2t}=1+\operatorname{tg}^2t\neq0$ (U p. 80). Derivando $\operatorname{arctg}(\operatorname{tg}t)=t$ se obtiene $\operatorname{arctg}'(\operatorname{tg}t)\,(1+\operatorname{tg}^2t)=1$. Con $y=\operatorname{tg}t$: $\operatorname{arctg}'(y)=\dfrac1{1+y^2}$ para todo $y\in\mathbb R$ (aquí no hay raíz ni signo que elegir).
   Consecuencia: $\big(\operatorname{arctg}\frac1x\big)'=\dfrac{1}{1+1/x^2}\cdot\dfrac{-1}{x^2}=\dfrac{-1}{1+x^2}$ ($x\neq0$), justo la opuesta de $(\operatorname{arctg}x)'$.

(b) $f'(x)=1+e^x>0$ ⇒ $f$ inyectiva. Para resolver $f(x)=1$ se prueba $x=0$: $0+e^0=1$. Entonces $(f^{-1})'(1)=\dfrac{1}{f'(0)}=\dfrac1{1+1}=\dfrac12$. Obsérvese que $f^{-1}$ no se puede escribir con funciones elementales, pero su derivada en un punto sí se puede calcular.

*Verificado con sympy.*

### P3 (propio, media-alta): $x^{\sqrt x}$ por derivación logarítmica
**Deriva $f(x)=x^{\sqrt x}$, $x>0$.**

1. Base y exponente variables ⇒ escribir $f(x)=e^{\sqrt x\,\ln x}$ (o bien $\ln f=\sqrt x\ln x$).
2. Producto: $(\sqrt x\ln x)'=\dfrac{1}{2\sqrt x}\ln x+\sqrt x\cdot\dfrac1x=\dfrac{\ln x}{2\sqrt x}+\dfrac1{\sqrt x}=\dfrac{2+\ln x}{2\sqrt x}$.
3. $f'(x)=x^{\sqrt x}\,\dfrac{2+\ln x}{2\sqrt x}$.

*Verificado con sympy; coincide con S Ej. 8, §3.6 p. 222.*

### P4 (propio, difícil): «la fórmula no existe» ≠ «no es derivable»
**(a) $f(x)=\sqrt{x^2-x^3}$. (b) $g(x)=\sqrt{x^4+x^6}$. Estudia la derivabilidad en $x=0$.**

(a) $\operatorname{dom}f$: $x^2(1-x)\ge0\iff x\le1$. Las reglas dan $f'(x)=\dfrac{2x-3x^2}{2\sqrt{x^2-x^3}}$, que no existe en $x=0$ ni en $x=1$. En 0 usamos la definición: $f(h)=|h|\sqrt{1-h}$, luego $\dfrac{f(h)-f(0)}{h}=\dfrac{|h|}{h}\sqrt{1-h}$, que tiende a $1$ cuando $h\to0^+$ y a $-1$ cuando $h\to0^-$. Las derivadas laterales existen pero son distintas (U Def. 2.3, p. 81) ⇒ **no derivable** en 0 (hay un «pico»). En $x=1$ la derivada por la izquierda es $-\infty$ ⇒ no derivable. $\operatorname{dom}f'=(-\infty,0)\cup(0,1)$.

(b) Las reglas dan $g'(x)=\dfrac{4x^3+6x^5}{2\sqrt{x^4+x^6}}$, que tampoco existe en $x=0$ ($\frac00$). Pero $g(h)=h^2\sqrt{1+h^2}$ y $\dfrac{g(h)-g(0)}{h}=h\sqrt{1+h^2}\to0$: **$g$ sí es derivable en 0**, con $g'(0)=0$. Por tanto $\operatorname{dom}g'=\mathbb R$.

*Verificado con sympy.* **Moraleja:** donde la fórmula que dan las reglas falla, se decide con la **definición** (U Def. 2.1, p. 75). Es lo que E omite en 2.10.

---

## (a) Teoría necesaria (U, páginas impresas verificadas en el texto y en el PDF)

| Herramienta | Enunciado en U | Página |
|---|---|---|
| Derivada en un punto (límite del cociente incremental) | U §2.1.2, Def. 2.1 | p. 75 |
| Derivada de una constante $=0$; derivada de $x^2$ por la definición | U Ej. 2.1 y 2.2 | p. 76 |
| Derivable ⇒ continua | U Teorema 2.1 | p. 76 |
| Función derivada $f':A\to\mathbb R$ (su dominio es el conjunto donde $f$ es derivable) | U §2.1.3, Def. 2.2 | p. 78 |
| Suma, producto y cociente ($g(a)\neq0$) | U §2.2.2, Prop. 2.1 | p. 79 |
| Regla de la cadena $(g\circ f)'(a)=g'(f(a))f'(a)$ | U §2.2.2 | p. 79 |
| Tabla: $c,\ e^x,\ \ln x,\ \operatorname{sen}x,\ x^c,\ a^x,\ \log_ax,\ \cos x$ | U §2.2.2 | p. 79 |
| $\operatorname{tg}'x=1/\cos^2x$ (por el cociente) | U §2.2.2 | p. 80 |
| Derivada de una inversa, método $f^{-1}(f(x))=x$: $\arcsin'y=1/\sqrt{1-y^2}$ | U Ej. 2.6 | p. 80 |
| Tabla con la cadena ($e^{u}$, $\ln u$, $\operatorname{sen}u$, $u^c$, $a^u$, $\log_au$, $\cos u$) | U §2.2.2 | p. 80 |
| Ejemplo de cadena ($\operatorname{sen}(\ln x^2)$, $e^{x^4}$) | U Ej. 2.7 | p. 81 |
| Derivadas laterales; si coinciden, existe la derivada | U Def. 2.3 | p. 81 |
| Tomar logaritmos en $x^{1/x}$ (para calcular un límite) | U Ej. 2.12 | p. 84 |
| Convenio $\arccos:[-1,1]\to[0,\pi]$, $\operatorname{arctg}:\mathbb R\to(-\frac\pi2,\frac\pi2)$ (nota al margen, §1.5) | U | p. 62 |
| Bolzano / valores intermedios (para ver que $f$ es sobreyectiva en 2.15) | U §1.4 | p. 52 |
| $f'>0$ en un intervalo ⇒ estrictamente creciente (usado en 2.15) | U §2.5.4, Prop. 2.4 | p. 98 |
| Funciones elementales: trigonométricas y sus inversas, potencias, exponenciales, logaritmos (se suponen conocidas; «Curso 0») | U, Convenio | p. 42 |

**No está en U** y se usa en los ejercicios:
- las derivadas de $\sec$ y $\operatorname{cotg}$ (se deducen como la de $\operatorname{tg}$);
- las derivadas de $\arccos$ y $\operatorname{arctg}$;
- el teorema general de la derivada de la inversa: derivabilidad de $f^{-1}$ y fórmula $(f^{-1})'(y)=1/f'(f^{-1}(y))$;
- la derivación logarítmica de $A(x)^{B(x)}$.

## (b) Huecos de U y dónde suplirlos (S = Stewart, L = Larson; páginas impresas verificadas)

| Hueco en U | Stewart (S) | Larson (L, impresa = PDF − 17) |
|---|---|---|
| Regla del producto/cociente explicada con ejemplos | §3.2: producto p. 185, cociente p. 187 | §2.3: Teor. 2.7 (producto) p. 118, Teor. 2.8 (cociente) p. 120 |
| Tabla completa de derivadas trigonométricas ($\sec$, $\csc$, $\operatorname{cotg}$) | §3.3, tabla p. 194 | §2.3, Teor. 2.9 p. 122 |
| Regla de la cadena: intuición y muchos ejemplos | §3.4, pp. 198-199 (enunciado p. 199) | §2.4, pp. 129-130 (Teor. 2.10 p. 130) |
| Derivadas de $\arcsin,\arccos,\operatorname{arctg}$… | §3.5, pp. 213-214 (tabla p. 214) | §5.6, Teor. 5.16 p. 369 |
| Teorema de la derivada de la función inversa (derivabilidad de $f^{-1}$) | §3.5, p. 213 (comentario) y ejercicio 77 (p. 217) | §5.3, Teor. 5.8 y 5.9, p. 341; Ej. 5 p. 341 (casi igual al 2.15) |
| Derivación logarítmica, $A(x)^{B(x)}$ | §3.6: pasos pp. 220-221; Ej. 8, $y=x^{\sqrt x}$, p. 222 | §5.1, Ej. 6 «Derivación logarítmica», p. 323 |
| Dónde deja de ser derivable una función (pico, discontinuidad, tangente vertical) → dominio de $f'$ | §2.8 «¿Cómo deja de ser derivable una función?», p. 159 | — |

## (c) Erratas y omisiones

**En E:**
1. **Ej. 2.12 (p. 59):** «la función $x^a$ también es derivable en todo $\mathbb R$, para todo $a\in[1,\infty)$» es **falso** si $a$ no es entero (por ejemplo, $x^{3/2}$ no está definida para $x<0$). Basta con la derivabilidad en $(0,\infty)$, que contiene a $x=1$. El resultado $6a$ es correcto (y vale para todo $a\in\mathbb R$).
2. **Ej. 2.10 (p. 58):** el dominio de $f'$ se obtiene solo mirando dónde se anula el denominador de la fórmula. Es un argumento incompleto: en $x=0$ y en $x=-8$ hay que usar la definición (en ambos el cociente incremental tiende a $+\infty$). El resultado $(-8,0)\cup(0,\infty)$ es correcto. Errata menor: «unicamente».
3. **Ej. 2.13 (pp. 59-60):** divide por $\operatorname{sen}x$ y toma $\operatorname{sen}x=+\sqrt{1-\cos^2x}$ sin decir que eso requiere $x\in(0,\pi)$. No da el dominio de $f'$ (es $(0,1)$) y supone sin justificarlo que $\arccos$ es derivable.
4. **Ej. 2.15 (pp. 60-61):** usa «$f'>0$ implica estrictamente creciente» (U Prop. 2.4, p. 98, de §2.5, posterior a este tema) y la derivabilidad de $f^{-1}$, que no se demuestra en U. El resultado es correcto: d) $\frac19$.
5. **Ej. 2.3 (p. 53):** «¡Oh! Hemos llegado a resultados distintos?» (falta el signo de apertura de interrogación). Sin error matemático.
6. **Ej. 2.16 (p. 61):** sin error. El resultado admite la forma más simple $x^{1/x}(1-\ln x)/x^2$. **Aviso de extracción:** en ejercicios.txt el enunciado aparece como «f(x) = x√x», pero en el PDF es la raíz $x$-ésima $\sqrt[x]{x}=x^{1/x}$, no $x^{\sqrt x}$.
7. (Fuera de 2.2, de paso) **Ej. 2.9 (p. 57):** «La función $f$ es es periódica». Además de la palabra repetida, la afirmación es falsa: $f'(x)=\operatorname{sen}(\pi x)e^{2x^2-x}$ no es periódica, y por tanto $f$ tampoco puede serlo.
8. Ejercicios 2.4, 2.5 y 2.11: sin errores (verificados con sympy).

**En U (detectado de paso):**
- **p. 80, nota al margen del Ej. 2.6:** dice que $\operatorname{sen}x$ tiene inversa «por ejemplo, en el intervalo $[\frac\pi2,\frac{3\pi}2]$». Es cierto que ahí es inyectivo, pero el cálculo del ejemplo usa $\cos x=+\sqrt{1-\operatorname{sen}^2x}$, que solo vale si $\cos x\ge0$, es decir, en $[-\frac\pi2,\frac\pi2]$ (el intervalo estándar del $\arcsin$). En $[\frac\pi2,\frac{3\pi}2]$ saldría $-1/\sqrt{1-y^2}$.
- **p. 79, tabla:** $(x^c)'=cx^{c-1}$ «con $c\in\mathbb R$» solo vale en general para $x>0$ (si $c$ no es entero, $x^c$ no está definida para $x<0$).
