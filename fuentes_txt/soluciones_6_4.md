# Soluciones Tema 6.4 — Integración numérica

Resolución paso a paso de los ejercicios de **E** de la sección 6.4 de U (Ejercicios 6.36-6.41, E pp. 242-246), de los ejemplos 6.29-6.35 de U (pp. 265-270), de 9 preguntas de exámenes **X** y de 4 ejemplos propios, más una **tabla de valores de referencia** para un interactivo. Todo se ha comprobado con sympy y con fracciones exactas (scripts `v64.py`, `x64.py`, `p64.py`, `t64.py` en el scratchpad, carpeta `r64/`). Las fórmulas de U (Def. 6.3-6.8, Teor. 6.3-6.4, Ej. 6.29-6.35) se han leído **como imagen** (render de U PDF 262-268 = pp. impresas 264-270); los enunciados de E (pp. 242-246) y de X (pp. 13, 36-37, 65-66, 78-79, 107, 109, 111, 136, 141, 151) también.

Páginas: U impresa (= PDF + 2); E impresa = PDF; X = página del PDF de exámenes. Convocatorias de X tomadas de `indice_examenes_*.md` y de la cabecera de la página.

## 0. Herramientas de teoría que se usan

Notación de U: $[a,b]$ se divide en $n$ (o $m$) **subintervalos iguales** de longitud $h=\frac{b-a}{n}$, con $x_k=a+kh$ y $f_k=f(x_k)$.

| Clave | Enunciado (como en U) | Dónde |
|---|---|---|
| **Idea de partida** | Las fórmulas se apoyan en dos propiedades: (1) $\int_a^bf$ es el área encerrada por la gráfica, el eje $x$ y las rectas $x=a$, $x=b$; (2) $\int_a^bf=\int_a^cf+\int_c^bf$ para $c\in(a,b)$. Se aproxima $f$ por una función sencilla construida con valores de $f$ en ciertos puntos, se integra esa, y luego se divide el intervalo y se suma. | U §6.4.2, p. 264 |
| **Rectángulos (simples)** Def. 6.3 | $\int_a^bf\approx f(a)(b-a)$ (izquierdo); $\approx f(b)(b-a)$ (derecho); $\approx f\!\left(\frac{a+b}2\right)(b-a)$ (central o punto medio). | U p. 264 |
| **Rectángulos compuestos** Def. 6.4 | $\int_a^bf\approx\frac{b-a}{n}\sum_{k=0}^{n-1}f(x_k)$ (izq.); $\approx\frac{b-a}{n}\sum_{k=1}^{n}f(x_k)$ (der.); $\approx\frac{b-a}{n}\sum_{k=0}^{n-1}f\!\left(\frac{x_k+x_{k+1}}2\right)$ (central). | U p. 266 |
| **Trapecio** Def. 6.5 | $\displaystyle\int_a^bf(x)\,dx\approx\frac{f(b)+f(a)}{2}(b-a)$: se sustituye $f$ por la recta que pasa por $(a,f(a))$ y $(b,f(b))$; es el área de un trapecio «acostado» de altura $b-a$ y bases $f(a)$, $f(b)$. | U p. 267 (Ej. 6.31) |
| **Trapecio compuesto** Def. 6.6 | $\displaystyle\int_a^bf(x)\,dx\approx\frac h2\big(f_0+2f_1+2f_2+\dots+2f_{n-1}+f_n\big)$, $f_k=f(x_k)$, $k=0,\dots,n$. Regla: $I\approx\frac h2(\text{Extremos}+2\,\text{Centrales})$. **$n$ subintervalos = $n+1$ nodos.** | U p. 267 (Ej. 6.32) |
| **Simpson** Def. 6.7 | $\displaystyle\int_a^bf(x)\,dx\approx\frac{f(a)+4f\!\left(\frac{a+b}2\right)+f(b)}{6}(b-a)$: se sustituye $f$ por la parábola (polinomio de grado 2) que pasa por $(a,f(a))$, $\left(\frac{a+b}2,f(\frac{a+b}2)\right)$, $(b,f(b))$. Usa **3 nodos** igualmente espaciados. | U pp. 267-268 |
| **Simpson compuesta** Def. 6.8 | Se divide $[a,b]$ en $n$ subintervalos iguales de longitud $h=\frac{b-a}n$ y a **cada uno** se le aplica Simpson. Los nodos son $x_k=a+k\frac h2$, $k=0,1,\dots,2n$ (extremos y punto medio de cada subintervalo) y $f_k=f(x_k)$: $$\int_a^bf(x)\,dx\approx\frac h6\big(f_0+4f_1+2f_2+4f_3+\dots+2f_{2n-2}+4f_{2n-1}+f_{2n}\big).$$ Regla: $I\approx\frac h6(\text{Extremos}+2\,\text{Pares}+4\,\text{Impares})$. **$n$ subintervalos = $2n+1$ nodos** (siempre un número impar de nodos). | U p. 268 (Ej. 6.33, pp. 268-269) |
| **Error del trapecio** Teor. 6.3 | Con el trapecio compuesto en $m$ subintervalos, el error absoluto cumple $\varepsilon\le\dfrac{(b-a)^3}{12m^2}M_2$, donde $f$ es dos veces derivable y $\lvert f''(x)\rvert\le M_2$ para todo $x\in[a,b]$. | U p. 269 (Ej. 6.34, pp. 269-270) |
| **Error de Simpson** Teor. 6.4 | Con Simpson compuesta en $m$ subintervalos, $\varepsilon\le\dfrac{(b-a)^5}{2880m^4}M_4$, donde $f$ es cuatro veces derivable y $\lvert f^{(4)}(x)\rvert\le M_4$ para todo $x\in[a,b]$. | U p. 270 (Ej. 6.35, p. 270) |

**Herramientas de temas anteriores:** Barrow (U Teor. 6.2, p. 244) y técnicas de primitivas (U §6.3, pp. 247-263) para el valor exacto; extremos absolutos de una función continua en un intervalo cerrado (se alcanzan en los extremos o donde la derivada se anula, U §3.4, pp. 125-134), para calcular $M_2$ y $M_4$; polinomio interpolador por diferencias divididas (U §3.3, pp. 119-124).

**Dos hechos que se deducen de lo anterior y se usan mucho:**
- **El trapecio es exacto si $f$ es una recta en cada subintervalo** (la recta que usa la fórmula es la propia $f$). Con el Teor. 6.3: $f''=0\Rightarrow M_2=0\Rightarrow\varepsilon\le0$.
- **Simpson es exacto si $f$ es un polinomio de grado $\le3$**: entonces $f^{(4)}=0$, se puede tomar $M_4=0$ y el Teor. 6.4 da $\varepsilon\le0$, es decir, $\varepsilon=0$ (Propio 2).
- Relación útil (propia, verificada con sympy): con los mismos $n$ subintervalos, $\text{Simpson}_n=\dfrac{\text{Trapecio}_n+2\cdot\text{PuntoMedio}_n}{3}$.

---

### Receta general del tema

> **Paso 1. ¿Qué fórmula?** Lee qué se pide: «rectángulo», «trapecio» o «Simpson», y si es **simple** (un solo intervalo $[a,b]$) o **compuesta** (en $n$ subintervalos). Si el enunciado da una **tabla de valores**, usa *todos* los datos: si hay $N$ nodos igualmente espaciados, eso es trapecio compuesto en $N-1$ subintervalos; Simpson exige un número **impar** de nodos ($3$ nodos = Simpson simple; $2n+1$ nodos = Simpson compuesta en $n$ subintervalos). Si falta algún nodo (p. ej. el punto medio para Simpson), **no se puede** aplicar la fórmula con esos datos (E 6.37).
>
> **Paso 2. Contar bien (convención de U).** Trapecio compuesto en $n$ subintervalos: $h=\frac{b-a}n$, nodos $a,a+h,\dots,b$ ($n+1$ nodos). Simpson compuesta en $n$ subintervalos: $h=\frac{b-a}n$ pero los nodos van de $\frac h2$ en $\frac h2$: $a,a+\frac h2,a+h,\dots,b$ ($2n+1$ nodos). «Simpson con 3 nodos» = Simpson simple.
>
> **Paso 3. Tabla de valores.** Haz una tabla $x_k\mid f(x_k)$ y marca cada valor como **extremo** (peso 1), **central/par** (peso 2) o **impar** (peso 4, solo en Simpson). En Simpson los índices impares son los **puntos medios** de los subintervalos.
>
> **Paso 4. Sustituir:** trapecio $\frac h2(E+2C)$; Simpson $\frac h6(E+2P+4I)$. Comprueba el orden de magnitud: el resultado debe parecerse a (longitud del intervalo) × (valor medio de $f$).
>
> **Paso 5. Si piden comparar con el valor exacto:** calcúlalo con Barrow, y da el error $\lvert\text{exacto}-\text{aprox.}\rvert$. Explicación estándar: el trapecio sustituye $f$ por rectas y Simpson por parábolas, que se pegan más a la curva; Simpson es exacto en polinomios de grado $\le3$.
>
> **Paso 6. Si piden una cota del error o cuántos subintervalos hacen falta:** (a) deriva hasta $f''$ (trapecio) o $f^{(4)}$ (Simpson); (b) calcula $M_2=\max_{[a,b]}\lvert f''\rvert$ o $M_4=\max_{[a,b]}\lvert f^{(4)}\rvert$ mirando los extremos del intervalo y los puntos donde la siguiente derivada se anula (o acotando a mano, p. ej. $\lvert\mathrm{sen}\rvert\le1$); (c) impón cota $\le$ tolerancia y **despeja $m$**:
> $$\text{trapecio: }m\ge\sqrt{\frac{(b-a)^3M_2}{12\,\text{tol}}},\qquad\text{Simpson: }m\ge\sqrt[4]{\frac{(b-a)^5M_4}{2880\,\text{tol}}};$$
> (d) $m$ es el **primer entero** mayor o igual que ese número (se redondea siempre hacia arriba).

---

## 1. Ejemplos de U (§6.4, pp. 265-270)

Todos usan, salvo 6.33-6.35, la misma integral (U Ej. 6.29, p. 265):
$$I=\int_1^{5/2}f(x)\,dx,\qquad f(x)=x^3-3{,}3x^2+3x,\qquad I=\Big[\tfrac{x^4}4-1{,}1x^3+\tfrac32x^2\Big]_1^{5/2}=\frac{417}{320}=1{,}303125.$$

### Ejemplos 6.29-6.32 (U pp. 265-267): rectángulos y trapecio

**Antes de calcular**
- **Qué me piden:** aproximar $I$ con cada fórmula y ver cuánto se equivoca.
- **Cómo lo pienso:** cada fórmula cambia la curva por algo cuya área sé calcular (rectángulo, trapecio); más subintervalos = rectángulos/trapecios más estrechos que siguen mejor la curva.
- **Qué uso:** Def. 6.3-6.6 (U pp. 264-267).
- **Por dónde empiezo:** $f(1)=0{,}7$, $f(2{,}5)=2{,}5$, $f(1{,}75)=0{,}503125$.

1. **Rectángulos simples** ($b-a=1{,}5$): izquierdo $f(1)\cdot1{,}5=0{,}7\cdot1{,}5=1{,}05$; derecho $f(2{,}5)\cdot1{,}5=3{,}75$; central $f(1{,}75)\cdot1{,}5=0{,}7546875\approx0{,}75$. Errores grandes: un único rectángulo no sigue la curva.
2. **Rectángulos compuestos con $n=3$** ($h=0{,}5$, nodos $1;1{,}5;2;2{,}5$): izquierdo $0{,}5\,(f(1)+f(1{,}5)+f(2))=0{,}975$; derecho $0{,}5\,(f(1{,}5)+f(2)+f(2{,}5))=1{,}875$; central $0{,}5\,(f(1{,}25)+f(1{,}75)+f(2{,}25))=1{,}2421875\approx1{,}242$ (Ej. 6.30, p. 266).
3. **Trapecio simple:** $\frac{f(1)+f(2{,}5)}2\cdot1{,}5=\frac{0{,}7+2{,}5}2\cdot1{,}5=2{,}4$ (Ej. 6.31, p. 267).
4. **Trapecio compuesto con $n=2$** ($h=0{,}75$, nodos $1;1{,}75;2{,}5$): $\frac{0{,}75}2\big(f(1)+2f(1{,}75)+f(2{,}5)\big)=0{,}375\,(0{,}7+1{,}00625+2{,}5)=\frac{2019}{1280}=1{,}57734375\approx1{,}577$ (Ej. 6.32, p. 267).
5. **Simpson simple** (propio, con la Def. 6.7): $\frac{1{,}5}6\big(0{,}7+4\cdot0{,}503125+2{,}5\big)=1{,}303125$: **coincide con el valor exacto**, porque $f$ es un polinomio de grado 3 (Propio 2).

**Receta.** Tabla de valores primero, fórmula después. Para comparar métodos, calcular el error $\lvert I-\text{aprox.}\rvert$ de cada uno.

**Error típico.** En el trapecio compuesto, olvidar el **2** delante de $f(1{,}75)$ (daría $1{,}39$).

sympy: $I=\frac{417}{320}$; valores 1,05; 3,75; 0,7546875; 0,975; 1,875; 1,2421875; 2,4; 1,57734375; Simpson 1,303125.

---

### Ejemplo 6.33 (U pp. 268-269): Simpson simple y compuesta con una tabla

> De una función conocemos la siguiente tabla de valores
>
> | $x$ | 1 | 1,1 | 1,2 | 1,3 | 1,4 | 1,5 | 1,6 |
> |---|---|---|---|---|---|---|---|
> | $f(x)$ | 2 | 2,2 | 2,3 | 2,1 | 2,4 | 2,3 | 1,9 |
>
> Aproximemos el valor de $I=\int_1^{1{,}6}f(x)\,dx$ utilizando la fórmula de Simpson y la fórmula compuesta de Simpson en tres subintervalos.

**Antes de calcular**
- **Qué me piden:** dos aproximaciones de $I$ con Simpson: simple y compuesta con $n=3$ subintervalos.
- **Cómo lo pienso:** hay 7 nodos ($=2\cdot3+1$), justo los que pide Simpson compuesta en 3 subintervalos. Simpson simple solo usa extremos y punto medio.
- **Qué uso:** Def. 6.7 y 6.8 (U p. 268).
- **Por dónde empiezo:** el punto medio de $[1;1{,}6]$ es $1{,}3$, y está en la tabla.

1. **Simpson simple:** $b-a=0{,}6$, punto medio $1{,}3$:
   $$I\approx\frac{f(1)+4f(1{,}3)+f(1{,}6)}6\cdot0{,}6=\frac{2+8{,}4+1{,}9}6\cdot0{,}6=1{,}23.$$
2. **Compuesta, contar:** $n=3$ subintervalos $\Rightarrow h=\frac{1{,}6-1}3=0{,}2$; los subintervalos son $[1;1{,}2]$, $[1{,}2;1{,}4]$, $[1{,}4;1{,}6]$ y sus puntos medios $1{,}1$, $1{,}3$, $1{,}5$. Nodos de $\frac h2=0{,}1$ en $0{,}1$: $x_0=1,\dots,x_6=1{,}6$.
3. **Clasificar:** extremos $f_0=2$, $f_6=1{,}9$; **pares** (fronteras interiores) $f_2=2{,}3$, $f_4=2{,}4$; **impares** (puntos medios) $f_1=2{,}2$, $f_3=2{,}1$, $f_5=2{,}3$.
4. **Sustituir:**
   $$I\approx\frac{0{,}2}6\big(3{,}9+2\cdot4{,}7+4\cdot6{,}6\big)=\frac{0{,}2}6(3{,}9+9{,}4+26{,}4)=\frac{0{,}2\cdot39{,}7}{6}\approx1{,}3233.$$

**Receta.** En Simpson compuesta, el $h$ de la fórmula es la longitud de **cada subintervalo** (aquí 0,2), no la separación entre nodos (0,1); los «impares» son los puntos medios.

**Error típico.** Poner $\frac{0{,}1}{6}$ (separación entre nodos) en lugar de $\frac{0{,}2}6$: saldría la mitad. (Con la separación entre nodos $\delta=\frac h2$ la fórmula equivalente es $\frac{\delta}{3}(E+2P+4I)$.)

Verificado: 1,23 y 1,32333…

---

### Ejemplo 6.34 (U pp. 269-270): cota de error del trapecio

> Calculemos el error máximo que cometemos al aproximar numéricamente $\int_0^1e^{-x^2}dx$, considerando 10 y 20 subintervalos.

**Antes de calcular**
- **Qué me piden:** una cota del error del trapecio compuesto con $m=10$ y $m=20$.
- **Cómo lo pienso:** el Teor. 6.3 necesita $M_2$, el máximo de $\lvert f''\rvert$ en $[0,1]$: es un problema de extremos absolutos.
- **Qué uso:** Teor. 6.3 (U p. 269); extremos absolutos (U §3.4).
- **Por dónde empiezo:** derivar dos veces $e^{-x^2}$.

1. **Derivadas:** $f'(x)=-2xe^{-x^2}$, $f''(x)=2e^{-x^2}(2x^2-1)$.
2. **Máximo de $\lvert f''\rvert$ en $[0,1]$:** candidatos $x=0$, $x=1$ y los ceros de $f'''(x)=4xe^{-x^2}(3-2x^2)$, es decir $x=0$ y $x=\pm\sqrt{3/2}\approx\pm1{,}22$ (fuera de $[0,1]$). Valores: $\lvert f''(0)\rvert=2$, $\lvert f''(1)\rvert=2/e\approx0{,}74$. Así $M_2=2$.
3. **Cotas:** $\varepsilon_{10}\le\frac{1^3}{12\cdot10^2}\cdot2=\frac1{600}$; $\varepsilon_{20}\le\frac{1^3}{12\cdot20^2}\cdot2=\frac1{2400}$.
4. **Lectura:** doblar $m$ divide la cota entre $2^2=4$.

**Receta.** $M_2$ = el mayor de $\lvert f''\rvert$ en los extremos y en los ceros de $f'''$ dentro del intervalo.

**Error típico.** Tomar $M_2=\lvert f''(1)\rvert$ (el extremo «de la derecha») o usar $\max f''$ sin valor absoluto: aquí $f''(0)=-2$ es negativo y es el que manda.

sympy: $f''=2(2x^2-1)e^{-x^2}$, $f'''=0\iff x\in\{0,\pm\sqrt6/2\}$; cotas $1/600$ y $1/2400$.

---

### Ejemplo 6.35 (U p. 270): cuántos subintervalos con Simpson

> Sea $f$ una función cuatro veces derivable y que verifica $\lvert f^{4)}(x)\rvert\le50$ para todo $x\in\mathbb R$. Queremos utilizar la fórmula compuesta de Simpson para aproximar $\int_0^2f(x)\,dx$ y tener la seguridad de que el error absoluto cometido es menor que $0{,}0001$. ¿En cuántos subintervalos debemos dividir $[0,2]$ para lograrlo?

**Antes de calcular**
- **Qué me piden:** el menor número $m$ de subintervalos que **garantiza** error $<10^{-4}$.
- **Cómo lo pienso:** la cota del Teor. 6.4 baja como $1/m^4$; pido que la cota sea $\le10^{-4}$ y despejo $m$.
- **Qué uso:** Teor. 6.4 (U p. 270) con $M_4=50$, $b-a=2$.
- **Por dónde empiezo:** escribir la desigualdad.

1. **Imponer:** $\dfrac{2^5\cdot50}{2880\,m^4}\le0{,}0001$.
2. **Despejar** (todo positivo, se puede multiplicar sin cambiar el sentido): $m^4\ge\dfrac{2^5\cdot50}{2880\cdot0{,}0001}=\dfrac{1600}{0{,}288}\approx5555{,}6$.
3. **Raíz cuarta** (creciente): $m\ge\sqrt[4]{5555{,}6}\approx8{,}6334$.
4. **Redondear hacia arriba:** $m=9$ subintervalos, es decir, $2\cdot9+1=19$ nodos.

**Receta.** Despejar $m$ y tomar el primer entero mayor o igual; contestar en subintervalos (y, si se quiere, en nodos).

**Error típico.** Redondear $8{,}63$ a $8$ (no garantiza la precisión) o responder «9 nodos» (con la convención de U son 9 subintervalos y 19 nodos).

sympy: $\big(2^5\cdot50/(2880\cdot10^{-4})\big)^{1/4}=8{,}63340\ldots$

---

## 2. Ejercicios de E (de fácil a difícil; numeración conservada)

Orden propuesto: 6.36 (idea) → 6.37 (qué se puede aplicar con unos datos) → 6.41 (todas las fórmulas con una tabla) → 6.39 (trapecio compuesto con tabla) → 6.40 (trapecio de una función) → 6.38 (cuándo el trapecio es exacto).

---

### Ejercicio 6.36 (E p. 242)

> ¿La integración numérica solamente es útil si no conocemos la expresión explícita de la función a integrar?

**Antes de calcular**
- **Qué me piden:** una respuesta razonada sí/no.
- **Cómo lo pienso:** Barrow necesita una primitiva; conocer $f$ no garantiza tenerla.
- **Qué uso:** motivación de U §6.4.1 (p. 263): la integración numérica sirve cuando no es posible calcular una primitiva o cuando solo conocemos valores de $f$ en ciertos puntos.

1. **No.** Hay funciones con fórmula explícita sencilla cuya primitiva no puede escribirse con funciones elementales, como $e^{-x^2}$ (U Ej. 6.34), $\frac{\mathrm{sen}\,x}{x}$ o $e^{x^3}$; para ellas Barrow no sirve en la práctica.
2. Otras veces la primitiva existe pero es muy larga de obtener (racionales con muchos factores, etc.) y una aproximación numérica basta.
3. Y, por supuesto, también es útil cuando solo se conoce una tabla de valores (mediciones).

**Receta.** Integración numérica = cuando Barrow no es posible o no compensa, o cuando solo hay datos.

**Error típico.** Creer que «tener la fórmula» equivale a «saber integrarla».

---

### Ejercicio 6.37 (E pp. 242-243)

> De una función $f$ se conocen los siguientes valores $f(0)=42$, $f(3)=41$. ¿Es posible utilizar la fórmula del trapecio para aproximar el valor de $\int_0^3f(x)\,dx$? Si la respuesta es afirmativa, calcula tal aproximación. ¿Puede utilizar la fórmula de Simpson para aproximar el valor de tal integral?

**Antes de calcular**
- **Qué me piden:** decidir qué fórmulas se pueden aplicar con solo dos datos y, si se puede, aproximar.
- **Cómo lo pienso:** cada fórmula necesita unos valores concretos: el trapecio, los dos extremos; Simpson, además el punto medio.
- **Qué uso:** Def. 6.5 y 6.7 (U pp. 267-268).
- **Por dónde empiezo:** listar qué nodos pide cada fórmula.

1. **Trapecio:** necesita $f(a)=f(0)$ y $f(b)=f(3)$. Los tenemos:
   $$\int_0^3f(x)\,dx\approx\frac{f(0)+f(3)}2(3-0)=\frac{42+41}2\cdot3=41{,}5\cdot3=124{,}5.$$
2. **Simpson:** necesita también $f\!\left(\frac{0+3}2\right)=f(1{,}5)$, que **no** se conoce. Con estos datos **no** se puede aplicar.

**Receta.** Antes de aplicar una fórmula, comprobar que se tienen **todos** sus nodos.

**Error típico.** «Inventarse» $f(1{,}5)$ como media de $f(0)$ y $f(3)$: eso es suponer que $f$ es una recta, y entonces Simpson daría lo mismo que el trapecio.

Verificado: $\frac{83}2\cdot3=124{,}5$.

---

### Ejercicio 6.41 (E pp. 245-246)

> De una función $f$ se conocen los siguientes valores $f(-1)=40$, $f(0)=42$, $f(1)=41$, $f(2)=42$, $f(3)=41$.
> 1. Aproxima el valor de $\int_{-1}^3f(x)\,dx$ utilizando la fórmula del rectángulo derecho y la fórmula del rectángulo derecho compuesta.
> 2. Aproxima el valor de $\int_{-1}^3f(x)\,dx$ utilizando la fórmula del trapecio y la fórmula del trapecio compuesta.
> 3. Aproxima el valor de $\int_{-1}^3f(x)\,dx$ utilizando la fórmula de Simpson y la fórmula de Simpson compuesta.

**Antes de calcular**
- **Qué me piden:** seis aproximaciones de la misma integral.
- **Cómo lo pienso:** hay 5 nodos con paso 1 en $[-1,3]$. Las fórmulas compuestas deben usar los 5: rectángulos y trapecio en $4$ subintervalos ($h=1$); Simpson compuesta en $2$ subintervalos ($h=2$, porque $5=2\cdot2+1$).
- **Qué uso:** Def. 6.3-6.8 (U pp. 264-268).
- **Por dónde empiezo:** $b-a=3-(-1)=4$.

1. **Rectángulo derecho simple:** $f(3)(b-a)=41\cdot4=164$.
2. **Rectángulo derecho compuesto** ($n=4$, $h=1$, $x_k=-1+k$): $h\sum_{k=1}^4f(x_k)=1\cdot(42+41+42+41)=166$.
3. **Trapecio simple:** $\frac{f(-1)+f(3)}2\cdot4=\frac{81}2\cdot4=162$.
4. **Trapecio compuesto** ($n=4$, $h=1$): extremos $40+41=81$, centrales $42+41+42=125$:
   $$\frac12(81+2\cdot125)=\frac{331}2=165{,}5.$$
5. **Simpson simple:** punto medio de $[-1,3]$ es $1$:
   $$\frac{f(-1)+4f(1)+f(3)}6\cdot4=\frac{40+164+41}6\cdot4=\frac{245\cdot4}6=\frac{490}3\approx163{,}33.$$
6. **Simpson compuesta** con $n=2$ subintervalos $[-1,1]$ y $[1,3]$ ($h=2$); nodos $x_0=-1,\ x_1=0,\ x_2=1,\ x_3=2,\ x_4=3$. Extremos $81$; pares $f_2=f(1)=41$; impares (puntos medios) $f_1+f_3=42+42=84$:
   $$\frac26\big(81+2\cdot41+4\cdot84\big)=\frac13(81+82+336)=\frac{499}3\approx166{,}33.$$

**Receta.** Con $N$ nodos equiespaciados: rectángulos y trapecio compuestos en $N-1$ subintervalos; Simpson compuesta en $\frac{N-1}2$ subintervalos (solo si $N$ es impar).

**Error típico.** Usar $h=1$ en Simpson compuesta (o dividir entre 3 subintervalos): con 5 nodos son 2 subintervalos de longitud 2. Otro: en el rectángulo derecho compuesto, incluir $f(-1)$ (es el izquierdo).

Verificado con fracciones: 164; 166; 162; 331/2; 490/3; 499/3.

---

### Ejercicio 6.39 (E p. 244)

> Aproxima utilizando la fórmula del trapecio compuesta el área de una finca comprendida entre tres caminos (de longitud 130, 500 y 150 metros respectivamente) y un río que pasa por los siguientes puntos ($x$ e $y$ se miden en metros):
>
> | $x$ | 0 | 100 | 200 | 300 | 400 | 500 |
> |---|---|---|---|---|---|---|
> | $y$ | 130 | 120 | 125 | 140 | 140 | 150 |
>
> Los caminos son rectos, como se muestra en la figura siguiente. *(Figura: la finca es la región entre el eje $x$, de 0 a 500, las verticales $x=0$, $x=500$ y la curva del río.)*

**Antes de calcular**
- **Qué me piden:** un área, es decir, $\int_0^{500}y(x)\,dx$, donde $y=f(x)$ es la curva del río.
- **Cómo lo pienso:** 6 nodos con paso 100 = 5 subintervalos; trapecio compuesto con todos los datos.
- **Qué uso:** área = integral (U §6.4.2, p. 264); Def. 6.6 (U p. 267).
- **Por dónde empiezo:** $h=\frac{500-0}5=100$.

1. **Clasificar:** extremos $130+150=280$; centrales $120+125+140+140=525$.
2. **Sustituir:**
   $$\int_0^{500}f(x)\,dx\approx\frac{100}2\big(280+2\cdot525\big)=50\cdot1330=66\,500\ \text{m}^2.$$
3. **Sentido:** la altura media ronda 133 m y el ancho es 500 m: $500\cdot133=66\,500$. Cuadra.

**Receta.** Área bajo una curva conocida por puntos = trapecio compuesto con todos los puntos.

**Error típico.** Poner unidades de longitud (m) en lugar de superficie (m²), o tomar $h=500$.

Verificado: $50\cdot1330=66\,500$.

---

### Ejercicio 6.40 (E pp. 244-245)

> Aproxima el valor de la integral $I=\int_0^\pi\cos x\,dx$ aplicando la fórmula compuesta del trapecio en 4 intervalos. Compara el valor obtenido con el real.

**Antes de calcular**
- **Qué me piden:** el trapecio compuesto con $n=4$ y compararlo con el valor exacto.
- **Cómo lo pienso:** $h=\frac\pi4$, nodos $0,\frac\pi4,\frac\pi2,\frac{3\pi}4,\pi$. El coseno es «antisimétrico» respecto de $\frac\pi2$: lo que sube a un lado baja al otro.
- **Qué uso:** Def. 6.6 (U p. 267); Barrow (U Teor. 6.2, p. 244).
- **Por dónde empiezo:** tabla de valores.

1. **Tabla:** $f(0)=1$, $f(\frac\pi4)=\frac{\sqrt2}2$, $f(\frac\pi2)=0$, $f(\frac{3\pi}4)=-\frac{\sqrt2}2$, $f(\pi)=-1$.
2. **Extremos:** $1+(-1)=0$. **Centrales:** $\frac{\sqrt2}2+0-\frac{\sqrt2}2=0$.
3. **Trapecio:** $I\approx\frac{\pi/4}2(0+2\cdot0)=0$.
4. **Valor real:** $\int_0^\pi\cos x\,dx=[\mathrm{sen}\,x]_0^\pi=0-0=0$. **Coinciden.**
5. **Por qué:** el área positiva en $[0,\frac\pi2]$ y la negativa en $[\frac\pi2,\pi]$ son iguales, y como los nodos son simétricos respecto de $\frac\pi2$, también los errores del trapecio en cada mitad son iguales y de signo contrario, y se cancelan. Es una casualidad de la simetría, no una propiedad general del trapecio (con $\int_0^{\pi/2}\cos x\,dx$ ya no es exacto: X p. 36).

**Receta.** Trapecio de una función: tabla de $f$ en los nodos, después $\frac h2(E+2C)$.

**Error típico.** Tomar $h=\pi$ (un solo intervalo) o $h=\frac\pi5$ (confundir 4 intervalos con 4 nodos).

sympy: trapecio $=0$, exacto $=0$.

---

### Ejercicio 6.38 (E p. 243)

> Dada la función $f(x)=\begin{cases}3+x,&x\le1,\\4x,&x>1,\end{cases}$ el valor de la integral $\int_{-1}^3f(x)\,dx$ ¿se obtiene de forma exacta por la fórmula compuesta del trapecio con un número par de subintervalos, todos ellos de la misma longitud?

**Antes de calcular**
- **Qué me piden:** decidir si el trapecio compuesto da el valor exacto cuando $n$ es par.
- **Cómo lo pienso:** $f$ es una recta en $[-1,1]$ y otra en $[1,3]$ (gráfica con un «codo» en $x=1$). El trapecio es exacto en un subintervalo donde $f$ sea una recta. El único problema es un subintervalo que contenga el codo en su interior.
- **Qué uso:** Def. 6.6 (U p. 267); Teor. 6.3 (U p. 269) con $M_2=0$ en cada tramo recto; aditividad (U p. 264).
- **Por dónde empiezo:** ¿cuándo es $x=1$ un nodo?

1. **Nodos:** con $n$ subintervalos, $h=\frac4n$ y $x_k=-1+\frac{4k}n$. Es $x_k=1\iff\frac{4k}n=2\iff k=\frac n2$, que es entero **si y solo si $n$ es par**.
2. **Si $n$ es par**, cada subintervalo está entero en $[-1,1]$ o entero en $[1,3]$, donde $f$ es una recta (en $x=1$ ambas fórmulas dan $4$: $f$ es continua). En cada subintervalo, la recta que usa el trapecio es la propia $f$, así que el trapecio da su integral exacta; sumando (aditividad), el trapecio compuesto da $\int_{-1}^3f$ exacta. **Respuesta: sí.**
3. **Valor exacto:** $\int_{-1}^1(3+x)dx=\big[3x+\frac{x^2}2\big]_{-1}^1=6$; $\int_1^34x\,dx=[2x^2]_1^3=16$; total $22$.
4. **Comprobación con $n=4$** ($h=1$, nodos $-1,0,1,2,3$; $f$: $2,3,4,8,12$): $\frac12\big(2+12+2(3+4+8)\big)=\frac12\cdot44=22$ ✓.
5. **Con $n$ impar no:** con $n=3$ el codo cae dentro de $[\frac13,\frac53]$ y el trapecio da $\frac{68}3\ne22$; con $n=1$ da $\frac{2+12}2\cdot4=28$.

**Receta.** Trapecio compuesto exacto ⇔ (en la práctica) $f$ es una recta en cada subintervalo: los puntos donde cambia la fórmula deben ser nodos.

**Error típico.** Pensar que «$f$ a trozos lineal» basta, sin comprobar dónde caen los nodos.

sympy: exacto 22; trapecio con $n=1,2,3,4,6,8$: $28,\ 22,\ 68/3,\ 22,\ 22,\ 22$.

---

## 3. Así lo preguntan en el examen (X)

Orden: tabla de datos (p. 13) → trapecio y Simpson de una función con el exacto (pp. 36, 78-79) → datos + interpolación + Simpson (pp. 65-66, 107) → Simpson simple tras una integral por partes (p. 136) → Simpson compuesta (p. 141) → trapecio compuesto con muchos nodos (pp. 109-111) → interpolación + Simpson compuesta (p. 151). En X no hay preguntas de cota de error; para eso, los Ej. 6.34-6.35 de U y los propios 3-4.

---

### X p. 13 (Febrero 2011, 2ª semana, Ingeniería Mecánica, Modelo B, Pregunta corta 3)

> De una función $f$ se conocen los siguientes valores $f(-1)=1$, $f(0)=2$, $f(1)=-1$, $f(2)=-3$, $f(3)=0$. Aproxime el valor de $\int_{-1}^3f(x)\,dx$ utilizando la fórmula del trapecio compuesta.

**Antes de calcular**
- **Qué me piden:** un número: el trapecio compuesto con todos los datos.
- **Cómo lo pienso:** 5 nodos de paso 1 = 4 subintervalos, $h=1$. Hay valores negativos: el resultado puede salir negativo (área con signo).
- **Qué uso:** Def. 6.6 (U p. 267).
- **Por dónde empiezo:** separar extremos y centrales.

1. **Extremos:** $f(-1)+f(3)=1+0=1$. **Centrales:** $f(0)+f(1)+f(2)=2-1-3=-2$.
2. **Fórmula:** $\int_{-1}^3f\approx\frac12\big(1+2\cdot(-2)\big)=\frac12(-3)=-\frac32$.

**Receta.** $\frac h2(E+2C)$ con $h$ = separación entre datos.

**Error típico.** Pensar que un resultado negativo es un error: la integral cuenta con signo.

Verificado: $-\frac32$.

---

### X pp. 36-37 (Febrero 2013, 2ª semana, Ingeniería Mecánica, Modelo B, Problema 6)

> Dada la integral $I=\int_0^{\pi/2}\cos x\,dx$
> (a) Determínese su valor aproximado aplicando la regla del trapecio en 2 intervalos.
> (b) Determínese su valor aproximado aplicando la regla de Simpson.
> (c) Compárense los resultados de los puntos anteriores con el valor real.

**Antes de calcular**
- **Qué me piden:** trapecio con $n=2$, Simpson (simple, 3 nodos) y comparar con el exacto.
- **Cómo lo pienso:** ambas fórmulas usan los **mismos 3 nodos** $0,\frac\pi4,\frac\pi2$; solo cambian los pesos. El coseno es cóncavo en $[0,\frac\pi2]$: las cuerdas quedan por debajo, así que el trapecio se quedará corto.
- **Qué uso:** Def. 6.6 y 6.7 (U pp. 267-268); Barrow (U Teor. 6.2, p. 244).
- **Por dónde empiezo:** $f(0)=1$, $f(\frac\pi4)=\frac{\sqrt2}2$, $f(\frac\pi2)=0$.

1. **(a) Trapecio, $n=2$:** $h=\frac\pi4$:
   $$I\approx\frac{\pi/4}2\Big(1+2\cdot\tfrac{\sqrt2}2+0\Big)=\frac\pi8\big(1+\sqrt2\big)\approx0{,}9481.$$
2. **(b) Simpson:** $b-a=\frac\pi2$:
   $$I\approx\frac{1+4\cdot\frac{\sqrt2}2+0}6\cdot\frac\pi2=\frac\pi{12}\big(1+2\sqrt2\big)\approx1{,}0023.$$
3. **(c) Exacto:** $\int_0^{\pi/2}\cos x\,dx=[\mathrm{sen}\,x]_0^{\pi/2}=1$.
   Errores: trapecio $\lvert1-0{,}9481\rvert\approx0{,}0519$; Simpson $\lvert1-1{,}0023\rvert\approx0{,}0023$, unas 23 veces menor.
4. **Explicación:** el trapecio sustituye la curva por dos segmentos (por debajo de una curva cóncava: aproximación por defecto); Simpson la sustituye por una parábola por los tres puntos, que se ajusta mucho mejor.

**Receta.** Mismos nodos, distintos pesos: trapecio $\frac h2(1,2,1)$; Simpson $\frac{b-a}6(1,4,1)$.

**Error típico.** En el trapecio con 2 intervalos, olvidar el 2 del nodo central ($\frac\pi8(1+\frac{\sqrt2}2)\approx0{,}67$).

sympy: $\frac\pi8(1+\sqrt2)=0{,}94806$; $\frac\pi{12}(1+2\sqrt2)=1{,}00228$; exacto 1.

---

### X pp. 78-79 (Febrero 2017, Modelo A, Ejercicio 5)

> Tenemos la integral $I=\int_0^1\frac{x}{(x^2+1)^2}dx$.
> a) Calcule el valor real de esta integral.
> b) Aproxime el valor de la integral por la regla del trapecio subdividiendo el intervalo en dos subintervalos iguales.
> c) Aproxime el valor de la integral por la regla de Simpson con 3 nodos igualmente espaciados.
> d) Compare los valores obtenidos en los apartados anteriores y explique a qué se deben las diferencias.

**Antes de calcular**
- **Qué me piden:** el exacto, trapecio con $n=2$, Simpson simple y una comparación razonada.
- **Cómo lo pienso:** el numerador es (salvo un factor $\frac12$) la derivada de $x^2+1$: inmediata. Los dos métodos usan los nodos $0,\frac12,1$.
- **Qué uso:** tabla de inmediatas, fila $\int f^af'$ (U p. 248); Barrow (U p. 244); Def. 6.6-6.7 (U pp. 267-268).
- **Por dónde empiezo:** $\int\frac{x}{(x^2+1)^2}dx=\frac12\int(x^2+1)^{-2}\,2x\,dx$.

1. **a) Primitiva:** $\frac12\cdot\frac{(x^2+1)^{-1}}{-1}=-\frac1{2(x^2+1)}$. **Barrow:** $I=-\frac14-\big(-\frac12\big)=\frac14=0{,}25$.
2. **Tabla:** $f(0)=0$; $f(\frac12)=\frac{1/2}{(5/4)^2}=\frac12\cdot\frac{16}{25}=\frac8{25}$; $f(1)=\frac14$.
3. **b) Trapecio, $n=2$, $h=\frac12$:**
   $$I\approx\frac{1/2}2\Big(0+\frac14+2\cdot\frac8{25}\Big)=\frac14\cdot\frac{25+64}{100}=\frac{89}{400}=0{,}2225.$$
4. **c) Simpson simple:**
   $$I\approx\frac{0+4\cdot\frac8{25}+\frac14}6\cdot1=\frac{\frac{128+25}{100}}6=\frac{153}{600}=\frac{51}{200}=0{,}255.$$
5. **d) Comparación:** errores $\lvert0{,}25-0{,}2225\rvert=0{,}0275$ (trapecio) y $\lvert0{,}25-0{,}255\rvert=0{,}005$ (Simpson). El trapecio cambia $f$ por segmentos (polinomios de grado 1) y Simpson por una parábola (grado 2), que se adapta a la curvatura de la gráfica; por eso Simpson está más cerca. Ninguno es exacto porque $f$ no es un polinomio.

**Receta.** Tabla común de valores con fracciones exactas → trapecio y Simpson → errores absolutos → explicación «recta frente a parábola».

**Error típico.** Calcular mal $f(\frac12)$ por no elevar al cuadrado $\frac54$.

sympy: $I=\frac14$; trapecio $\frac{89}{400}$; Simpson $\frac{51}{200}$.

---

### X pp. 65-66 (Febrero 2016, Modelo B, Ejercicio 5)

> Se consideran los siguientes valores de una función
>
> | $x$ | 1 | 2 | 3 |
> |---|---|---|---|
> | $f(x)$ | 31 | 26 | 43 |
>
> (a) Calcule $\int_1^3f(x)\,dx$ por la regla del trapecio.
> (b) Calcule $\int_1^3f(x)\,dx$ por la regla de Simpson con 3 nodos igualmente espaciados.
> (c) La función $g(x)=11x^2-38x+58$ verifica $f(1)=g(1)$, $f(2)=g(2)$, $f(3)=g(3)$. Calcule $\int_1^3g(x)\,dx$ y compárelo con los valores obtenidos en los apartados anteriores. Justifique a qué se debe la diferencia.

**Antes de calcular**
- **Qué me piden:** trapecio y Simpson con los 3 datos, y la integral exacta de la parábola $g$ que pasa por ellos.
- **Cómo lo pienso:** con los tres datos, el trapecio es compuesto en 2 subintervalos ($h=1$). Simpson construye *precisamente* la parábola por los tres puntos, que es $g$: Simpson tiene que coincidir con $\int g$.
- **Qué uso:** Def. 6.6-6.7 (U pp. 267-268); Barrow; unicidad del polinomio interpolador (U §3.3).
- **Por dónde empiezo:** extremos $31+43=74$, central $26$.

1. **(a) Trapecio con los 3 datos** ($n=2$, $h=1$):
   $$\int_1^3f\approx\frac12\big(31+43+2\cdot26\big)=\frac{126}2=63.$$
2. **(b) Simpson** ($b-a=2$, punto medio 2):
   $$\int_1^3f\approx\frac{31+4\cdot26+43}6\cdot2=\frac{178}{6}\cdot2=\frac{178}3\approx59{,}33\qquad(31+104+43=178).$$
3. **(c) Integral de $g$:** primero se comprueba $g(1)=31$, $g(2)=26$, $g(3)=43$ ✓. Barrow:
   $$\int_1^3(11x^2-38x+58)\,dx=\Big[\frac{11x^3}3-19x^2+58x\Big]_1^3=(99-171+174)-\Big(\frac{11}3-19+58\Big)=102-\frac{128}3=\frac{178}3.$$
4. **Comparación:** $\int g=\frac{178}3$ coincide **exactamente** con Simpson, y difiere del trapecio ($63$) en $\frac{11}3\approx3{,}67$.
5. **Por qué:** Simpson integra la única parábola que pasa por los tres puntos, y esa parábola es $g$. El trapecio integra la poligonal que une los puntos; como $g$ es convexa ($g''=22>0$), la poligonal queda por encima de $g$ y el trapecio da más.

**Receta.** Simpson simple = integral exacta de la parábola que interpola los 3 datos. Si te dan esa parábola, $\int g$ y Simpson deben coincidir (sirve de comprobación).

**Error típico.** Usar el trapecio *simple* ignorando el dato central ($\frac{31+43}2\cdot2=74$): con datos, hay que usarlos todos.

Verificado: $63$; $\frac{178}3$; $\int_1^3g=\frac{178}3$.

---

### X p. 107 (Ingeniería Electrónica, examen 4, sin fecha, Ejercicio 5)

> De una función $f$ se sabe que $f(0)=1$, $f(2)=3$ y $f(4)=2$.
> - Aproxime el valor de f(1) utilizando el polinomio interpolador.
> - Aproxime el valor de $\int_0^4f(x)\,dx$ mediante la fórmula de Simpson.
> - Compruebe que obtiene el mismo resultado que en el apartado anterior si integra el polinomio interpolador entre 0 y 4.

**Antes de calcular**
- **Qué me piden:** el polinomio interpolador (grado $\le2$) en $x=1$, Simpson simple y comprobar que Simpson = $\int p$.
- **Cómo lo pienso:** igual que X p. 65: tres datos equiespaciados, la parábola que los une es la que integra Simpson.
- **Qué uso:** diferencias divididas de Newton (U §3.3, pp. 119-124); Def. 6.7 (U p. 268).
- **Por dónde empiezo:** diferencias divididas.

1. **Orden 1:** $f[0,2]=\frac{3-1}{2}=1$; $f[2,4]=\frac{2-3}{2}=-\frac12$. **Orden 2:** $f[0,2,4]=\frac{-\frac12-1}{4-0}=-\frac38$.
2. **Polinomio:** $p(x)=1+1\cdot(x-0)-\frac38(x-0)(x-2)=1+x-\frac38x(x-2)=-\frac38x^2+\frac74x+1$.
3. **$f(1)\approx p(1)=1+1-\frac38(1)(-1)=2+\frac38=\frac{19}8=2{,}375$.**
4. **Simpson** ($b-a=4$, punto medio 2): $\int_0^4f\approx\frac{1+4\cdot3+2}6\cdot4=\frac{15\cdot4}6=10$.
5. **Integral de $p$:** $\int_0^4\Big(-\frac38x^2+\frac74x+1\Big)dx=\Big[-\frac{x^3}8+\frac78x^2+x\Big]_0^4=-8+14+4=10$ ✓.

**Receta.** Tres datos equiespaciados: Simpson $=\int$ del polinomio interpolador de grado 2.

**Error típico.** Olvidar el factor $(x-2)$ en el término de orden 2 de Newton.

sympy: $p=-\frac38x^2+\frac74x+1$, $p(1)=\frac{19}8$, Simpson $10$, $\int_0^4p=10$.

---

### X p. 136 (Febrero 2017, 2ª semana, Ejercicio 5)

> Dada la integral $\int_0^\pi x^2\,\mathrm{sen}\,x\,dx$:
> - Calcule el valor exacto encontrando una primitiva del integrando. (1.5 PUNTOS)
> - Aproxime su valor utilizando la regla de Simpson. (1.5 PUNTOS)

**Antes de calcular**
- **Qué me piden:** el exacto (partes dos veces) y Simpson simple.
- **Cómo lo pienso:** polinomio × seno: partes con $u=x^2$, luego otra vez. Para Simpson, nodos $0,\frac\pi2,\pi$, y $\mathrm{sen}$ se anula en los extremos.
- **Qué uso:** integración por partes reiterada (U pp. 251-253); Def. 6.7 (U p. 268).
- **Por dónde empiezo:** $u=x^2$, $v'=\mathrm{sen}\,x$.

1. **Partes 1:** $u=x^2$, $u'=2x$; $v=-\cos x$: $\int x^2\mathrm{sen}\,x\,dx=-x^2\cos x+\int2x\cos x\,dx$.
2. **Partes 2:** $u=2x$, $u'=2$; $v=\mathrm{sen}\,x$: $\int2x\cos x\,dx=2x\,\mathrm{sen}\,x-\int2\,\mathrm{sen}\,x\,dx=2x\,\mathrm{sen}\,x+2\cos x$.
3. **Primitiva:** $F(x)=-x^2\cos x+2x\,\mathrm{sen}\,x+2\cos x$. **Barrow:** $F(\pi)=\pi^2+0-2$, $F(0)=2$; $\int_0^\pi x^2\mathrm{sen}\,x\,dx=\pi^2-4\approx5{,}8696$.
4. **Simpson:** $f(0)=0$, $f(\frac\pi2)=\frac{\pi^2}4$, $f(\pi)=0$:
   $$\int_0^\pi x^2\mathrm{sen}\,x\,dx\approx\frac{0+4\cdot\frac{\pi^2}4+0}6\cdot\pi=\frac{\pi^3}6\approx5{,}1677.$$
5. **Comentario:** error $\approx0{,}70$; una sola parábola en un intervalo de longitud $\pi$ es poco: con Simpson compuesta mejoraría mucho.

**Receta.** Exacto: partes con $u$ = polinomio, tantas veces como su grado. Simpson simple: tres valores, pesos $1,4,1$, por $\frac{b-a}6$.

**Error típico.** Calcular «la integral de un producto como el producto de integrales», o equivocarse de signo al integrar $\mathrm{sen}$.

sympy: exacto $\pi^2-4$; Simpson $\frac{\pi^3}6$.

---

### X p. 141 (Febrero 2018, 2ª semana, Ing. Electrónica Industrial y Automática, Ejercicio 5, segundo apartado)

> Dada la integral $\int_0^{\pi/2}(\mathrm{sen}^4x)(\cos^3x)\,dx$: Calcule el valor exacto encontrando una primitiva del integrando. (1.5 PUNTOS) Aproxime su valor utilizando la regla de Simpson compuesta en tres subintervalos. (1.5 PUNTOS)

(El valor exacto, $\frac15-\frac17=\frac2{35}\approx0{,}05714$, está resuelto en `soluciones_6_3.md`, X p. 141.)

**Antes de calcular**
- **Qué me piden:** Simpson compuesta con $n=3$ subintervalos.
- **Cómo lo pienso:** $h=\frac{\pi/2}3=\frac\pi6$; cada subintervalo tiene su punto medio, así que los nodos van de $\frac\pi{12}$ en $\frac\pi{12}$: 7 nodos.
- **Qué uso:** Def. 6.8 (U p. 268).
- **Por dónde empiezo:** subintervalos $[0,\frac\pi6]$, $[\frac\pi6,\frac\pi3]$, $[\frac\pi3,\frac\pi2]$, puntos medios $\frac\pi{12},\frac\pi4,\frac{5\pi}{12}$.

1. **Tabla** ($f=\mathrm{sen}^4x\cos^3x$, 5 decimales):

   | $k$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
   |---|---|---|---|---|---|---|---|
   | $x_k$ | $0$ | $\frac\pi{12}$ | $\frac\pi6$ | $\frac\pi4$ | $\frac\pi3$ | $\frac{5\pi}{12}$ | $\frac\pi2$ |
   | $f(x_k)$ | $0$ | $0{,}00404$ | $\frac{3\sqrt3}{128}\approx0{,}04059$ | $\frac{\sqrt2}{16}\approx0{,}08839$ | $\frac9{128}\approx0{,}07031$ | $0{,}01509$ | $0$ |

   (Por ejemplo, $f(\frac\pi6)=(\frac12)^4(\frac{\sqrt3}2)^3=\frac1{16}\cdot\frac{3\sqrt3}8$.)
2. **Clasificar:** extremos $0+0=0$; pares $f_2+f_4\approx0{,}11091$; impares $f_1+f_3+f_5\approx0{,}10752$.
3. **Fórmula:**
   $$\int_0^{\pi/2}\approx\frac{\pi/6}6\big(0+2\cdot0{,}11091+4\cdot0{,}10752\big)=\frac\pi{36}\cdot0{,}65190\approx0{,}05689.$$
4. **Comparación:** exacto $0{,}05714$; error $\approx0{,}00025$.

**Receta.** Simpson compuesta en $n$ subintervalos: $h=\frac{b-a}n$, nodos cada $\frac h2$, factor $\frac h6$.

**Error típico.** Usar solo los 4 nodos $0,\frac\pi6,\frac\pi3,\frac\pi2$ (eso es un número par de nodos: no vale para Simpson), o poner $\frac{\pi/12}6$ como factor.

sympy: $\frac{\pi}{2304}\big(9+16\sqrt2+3\sqrt3+2\sqrt6\big)\approx0{,}0568903$; exacto $\frac2{35}\approx0{,}0571429$.

---

### X pp. 109-111 (Examen 1 elaborado con exámenes de asignaturas similares, Ejercicio 6)

> Calcular, mediante la regla del trapecio, la integral $\int_3^5\frac{1}{\sqrt{-x^2+8x-7}}dx$.

**Antes de calcular**
- **Qué me piden:** una aproximación con el trapecio; el número de subintervalos lo elijo yo.
- **Cómo lo pienso:** con un solo trapecio la aproximación sería pobre; tomo $n=5$ ($h=0{,}4$), suficiente para una buena aproximación a mano. El integrando es simétrico respecto de $x=4$ ($-x^2+8x-7=9-(x-4)^2$): la tabla se repite.
- **Qué uso:** Def. 6.6 (U p. 267).
- **Por dónde empiezo:** completar el cuadrado para ver el dominio y la simetría.

1. **Dominio:** $-x^2+8x-7=9-(x-4)^2>0\iff1<x<7$; en $[3,5]$ el integrando es continuo.
2. **Tabla** ($h=0{,}4$; por simetría $f(3)=f(5)$, $f(3{,}4)=f(4{,}6)$, $f(3{,}8)=f(4{,}2)$):

   | $x$ | 3 | 3,4 | 3,8 | 4,2 | 4,6 | 5 |
   |---|---|---|---|---|---|---|
   | $-x^2+8x-7$ | 8 | 8,64 | 8,96 | 8,96 | 8,64 | 8 |
   | $f(x)$ | 0,35355 | 0,34021 | 0,33408 | 0,33408 | 0,34021 | 0,35355 |
3. **Fórmula:** extremos $0{,}35355+0{,}35355=0{,}70711$; suma de los cuatro centrales $2\cdot(0{,}34021+0{,}33408)=1{,}34858$ (por la simetría):
   $$I\approx\frac{0{,}4}2\big(0{,}70711+2\cdot1{,}34858\big)=0{,}2\cdot3{,}40427\approx0{,}6808.$$
4. **Comprobación (no pedida):** con $t=\frac{x-4}3$, $\int\frac{dx}{\sqrt{9-(x-4)^2}}=\mathrm{arcsen}\frac{x-4}3$, así que $I=2\,\mathrm{arcsen}\frac13\approx0{,}6797$; error del trapecio $\approx0{,}0012$.

**Receta.** Si el enunciado no fija $n$, elegir uno razonable (4-6 subintervalos) y decirlo; aprovechar simetrías para ahorrar cuentas.

**Error típico.** Evaluar mal la raíz (calcular $\sqrt{-x^2}+\dots$) o no comprobar el dominio.

sympy: trapecio $n=5$: $0{,}680848$; exacto $2\,\mathrm{arcsen}\frac13=0{,}679674$.

---

### X p. 151 (Febrero 2019, 1ª semana, Ejercicio 5)

> De una función $f$ se sabe que $f(1)=2$, $f(3)=3$, $f(4)=2$ y $f(8)=10$.
> - Aproxime el valor de $f(2)$ utilizando el polinomio interpolador. (1.5 PUNTOS)
> - Usando el valor de $f(2)$ obtenido en el apartado anterior, aproxime el valor de $\int_1^4f(x)\,dx$ mediante la fórmula compuesta de Simpson en dos subintervalos. (1.5 PUNTOS)

**Antes de calcular**
- **Qué me piden:** el polinomio interpolador por 4 puntos (grado $\le3$), su valor en 2, y Simpson compuesta en $[1,4]$ con $n=2$.
- **Cómo lo pienso:** Simpson compuesta con $n=2$ en $[1,4]$ necesita 5 nodos equiespaciados $1,\frac74,\frac52,\frac{13}4,4$; solo conozco $f(1)$ y $f(4)$. Los demás los aproximo con el polinomio interpolador $p$ del primer apartado (el mismo que da $f(2)\approx p(2)$). Como $p$ es de grado 3, Simpson sobre $p$ es exacto: el resultado será $\int_1^4p$.
- **Qué uso:** diferencias divididas (U §3.3, pp. 119-124); Def. 6.8 (U p. 268); Simpson exacto en cúbicas (Teor. 6.4 con $M_4=0$, U p. 270).
- **Por dónde empiezo:** tabla de diferencias divididas con nodos $1,3,4,8$.

1. **Orden 1:** $f[1,3]=\frac{3-2}{2}=\frac12$; $f[3,4]=\frac{2-3}1=-1$; $f[4,8]=\frac{10-2}4=2$.
2. **Orden 2:** $f[1,3,4]=\frac{-1-\frac12}{4-1}=-\frac12$; $f[3,4,8]=\frac{2-(-1)}{8-3}=\frac35$.
3. **Orden 3:** $f[1,3,4,8]=\frac{\frac35+\frac12}{8-1}=\frac{11/10}7=\frac{11}{70}$.
4. **Polinomio de Newton:**
   $$p(x)=2+\tfrac12(x-1)-\tfrac12(x-1)(x-3)+\tfrac{11}{70}(x-1)(x-3)(x-4).$$
5. **$f(2)\approx p(2)=2+\frac12+\frac12+\frac{11}{70}\cdot(1)(-1)(-2)=3+\frac{22}{70}=\frac{116}{35}\approx3{,}3143.$**
6. **Simpson compuesta, $n=2$:** $h=\frac{4-1}2=\frac32$; nodos cada $\frac34$: $1,\frac74,\frac52,\frac{13}4,4$. Valores (con $p$ donde falta $f$): $f(1)=2$, $p(\frac74)=\frac{2845}{896}\approx3{,}17522$, $p(\frac52)=\frac{1849}{560}\approx3{,}30179$, $p(\frac{13}4)=\frac{12443}{4480}\approx2{,}77746$, $f(4)=2$.
7. **Fórmula:** extremos $4$; pares $p(\frac52)$; impares $p(\frac74)+p(\frac{13}4)$:
   $$\int_1^4f\approx\frac{3/2}6\Big(4+2\cdot3{,}30179+4\cdot(3{,}17522+2{,}77746)\Big)=\frac14\cdot34{,}41429=\frac{2409}{280}\approx8{,}6036.$$
8. **Comprobación:** $\int_1^4p(x)\,dx=\frac{2409}{280}$ exactamente, como se esperaba (Simpson es exacto en polinomios de grado 3).
9. **Otra forma razonable de usar $f(2)$ directamente:** Simpson simple en $[1,3]$ con nodos $1,2,3$ y trapecio en $[3,4]$: $\frac{2+4\cdot\frac{116}{35}+3}6\cdot2+\frac{3+2}2\approx8{,}5857$. Ambas son aproximaciones de la misma integral; la primera aprovecha toda la información del polinomio.

**Receta.** Si faltan valores en los nodos que pide la fórmula, se obtienen con el polinomio interpolador de los datos; y si ese polinomio es de grado $\le3$, Simpson da su integral exacta.

**Error típico.** Aplicar Simpson compuesta con nodos no equiespaciados ($1,2,3,4$ son 4 nodos: número par, no sirve).

sympy: $p=\frac{11x^3-123x^2+384x-132}{70}$, $p(2)=\frac{116}{35}$; Simpson $=\int_1^4p=\frac{2409}{280}=8{,}60357$; alternativa $8{,}58571$.

---

## 4. Ejemplos propios (dificultad creciente)

### Propio 1 — Las tres fórmulas sobre $\int_0^1x^2\,dx$ (fácil) [propio]

> Aproxima $\int_0^1x^2\,dx=\frac13$ con rectángulo central, trapecio y Simpson, simples y con $n=2$ subintervalos. ¿Qué relación hay entre ellas?

**Antes de calcular**
- **Qué me piden:** seis números y una observación.
- **Cómo lo pienso:** $x^2$ es convexa: la cuerda queda por encima (trapecio por exceso) y la tangente en el punto medio por debajo (punto medio por defecto).
- **Qué uso:** Def. 6.3-6.8 (U pp. 264-268).
- **Por dónde empiezo:** $f(0)=0$, $f(\frac14)=\frac1{16}$, $f(\frac12)=\frac14$, $f(\frac34)=\frac9{16}$, $f(1)=1$.

1. **Simples:** punto medio $f(\frac12)\cdot1=\frac14$; trapecio $\frac{0+1}2=\frac12$; Simpson $\frac{0+4\cdot\frac14+1}6=\frac26=\frac13$ (exacto).
2. **$n=2$:** punto medio $\frac12\big(f(\frac14)+f(\frac34)\big)=\frac12\cdot\frac{10}{16}=\frac5{16}$; trapecio $\frac14\big(0+2\cdot\frac14+1\big)=\frac38$; Simpson ($h=\frac12$, nodos cada $\frac14$) $\frac{1/2}6\big(0+1+2\cdot\frac14+4(\frac1{16}+\frac9{16})\big)=\frac1{12}\cdot4=\frac13$.
3. **Errores:** trapecio $+\frac16$ ($n=1$), $+\frac1{24}$ ($n=2$); punto medio $-\frac1{12}$, $-\frac1{48}$: el del punto medio es **la mitad y de signo contrario**, y al doblar $n$ ambos se dividen entre 4.
4. **Relación:** $\frac{T+2M}3=\frac{\frac12+2\cdot\frac14}3=\frac13=S$. En general $S_n=\frac{T_n+2M_n}3$ con los mismos subintervalos: Simpson «cancela» los errores opuestos de trapecio y punto medio.

**Receta.** Para una parábola, Simpson es exacto; trapecio y punto medio fallan en sentidos opuestos.

**Error típico.** Pensar que el trapecio siempre es mejor que el punto medio (aquí es al revés).

sympy: $\frac12,\frac14,\frac13,\frac38,\frac5{16},\frac13$.

---

### Propio 2 — ¿Por qué Simpson es exacto en las cúbicas? (medio) [propio]

> (a) Comprueba que Simpson simple da exactamente $\int_0^2x^3dx$. (b) Justifica que Simpson (simple o compuesta) es exacta para todo polinomio de grado $\le3$. (c) ¿Lo es para $x^4$ en $[0,1]$?

**Antes de calcular**
- **Qué me piden:** un ejemplo, una justificación general y un contraejemplo.
- **Cómo lo pienso:** la cota del Teor. 6.4 depende de $f^{(4)}$; en una cúbica es cero.
- **Qué uso:** Def. 6.7 y Teor. 6.4 (U pp. 268-270).
- **Por dónde empiezo:** derivar 4 veces una cúbica.

1. **(a)** $\frac{0+4\cdot1^3+2^3}6\cdot2=\frac{12}6\cdot2=4$ y $\int_0^2x^3dx=\big[\frac{x^4}4\big]_0^2=4$ ✓.
2. **(b)** Si $p(x)=c_3x^3+c_2x^2+c_1x+c_0$, entonces $p^{(4)}(x)=0$ para todo $x$, así que se puede tomar $M_4=0$ en el Teor. 6.4: $\varepsilon\le\frac{(b-a)^5}{2880m^4}\cdot0=0$. El error es $0$ para cualquier número $m$ de subintervalos, incluido $m=1$ (Simpson simple).
3. **Idea gráfica** de por qué «gana» un grado: Simpson integra bien las parábolas por construcción; para $x^3$ centrado en el punto medio del intervalo, la diferencia entre la cúbica y la parábola es antisimétrica (lo que sobra a un lado falta en el otro) y su integral se anula.
4. **(c)** $\frac{0+4\cdot(\frac12)^4+1}6=\frac{\frac14+1}6=\frac5{24}\ne\frac15=\int_0^1x^4dx$. Error $\frac1{120}$; ahora $f^{(4)}=24$ y la cota del Teor. 6.4 es $\frac{24}{2880}=\frac1{120}$: en este caso la cota se alcanza.
5. Consecuencias: U Ej. 6.29 (cúbica: Simpson da $1{,}303125$ exacto) y X p. 151 (Simpson sobre el interpolador cúbico = su integral).

**Receta.** Simpson es exacto si $f^{(4)}\equiv0$ (polinomios de grado $\le3$); el trapecio, si $f''\equiv0$ (rectas).

**Error típico.** Decir «Simpson es exacto en parábolas porque usa parábolas» y olvidar que también lo es en cúbicas.

sympy: con $p$ cúbico genérico y $[a,b]$ simbólicos, $\int_a^bp-\frac{b-a}6\big(p(a)+4p(\frac{a+b}2)+p(b)\big)=0$; $x^4$: $\frac5{24}$ frente a $\frac15$.

---

### Propio 3 — ¿Cuántos subintervalos para $\ln2=\int_1^2\frac{dx}x$ con error $<10^{-4}$? (medio-difícil) [propio]

> Determina el número de subintervalos que garantiza error menor que $10^{-4}$ al aproximar $\int_1^2\frac{dx}x$ (a) con el trapecio compuesto y (b) con Simpson compuesta.

**Antes de calcular**
- **Qué me piden:** dos valores de $m$, el mínimo que **garantiza** la precisión según los Teor. 6.3 y 6.4.
- **Cómo lo pienso:** derivo, acoto la derivada por su valor más grande en $[1,2]$ y despejo $m$ de la cota.
- **Qué uso:** Teor. 6.3 y 6.4 (U pp. 269-270).
- **Por dónde empiezo:** $f(x)=x^{-1}$, $f''(x)=\frac2{x^3}$, $f^{(4)}(x)=\frac{24}{x^5}$.

1. **$M_2$:** $\frac2{x^3}$ es positiva y decreciente en $[1,2]$; su máximo está en $x=1$: $M_2=2$.
2. **$M_4$:** $\frac{24}{x^5}$ también decrece: $M_4=24$.
3. **(a) Trapecio:** $\frac{1^3\cdot2}{12m^2}\le10^{-4}\iff m^2\ge\frac{2}{12\cdot10^{-4}}=1666{,}7\iff m\ge40{,}82$. **$m=41$** subintervalos (42 nodos).
4. **(b) Simpson:** $\frac{1^5\cdot24}{2880m^4}\le10^{-4}\iff m^4\ge\frac{24}{0{,}288}=83{,}33\iff m\ge3{,}02$. **$m=4$** subintervalos (9 nodos).
5. **Comparación del coste:** 42 evaluaciones de $f$ con el trapecio frente a 9 con Simpson.
6. **La cota es una garantía, no el error real:** con $m=40$ el trapecio ya tiene error real $3{,}9\cdot10^{-5}$, y Simpson con $m=3$ tiene error real $2{,}3\cdot10^{-5}$; pero con esos $m$ la cota *no* asegura nada ($3{,}02>3$), y la pregunta pide **seguridad**.

**Receta.** $m_{\text{trap}}=\Big\lceil\sqrt{\frac{(b-a)^3M_2}{12\,\text{tol}}}\Big\rceil$, $m_{\text{Simp}}=\Big\lceil\sqrt[4]{\frac{(b-a)^5M_4}{2880\,\text{tol}}}\Big\rceil$ ($\lceil\ \rceil$ = primer entero mayor o igual).

**Error típico.** Tomar $M_2$ en el extremo equivocado ($f''(2)=\frac14$ daría $m=15$, que no garantiza nada) o redondear hacia abajo ($m=40$, $m=3$).

sympy: $m\ge40{,}8248$ y $m\ge3{,}0214$; errores reales: trapecio $m=41$: $3{,}72\cdot10^{-5}$ (cota $9{,}91\cdot10^{-5}$); Simpson $m=4$: $7{,}35\cdot10^{-6}$ (cota $3{,}26\cdot10^{-5}$).

---

### Propio 4 — $\int_0^1e^{-x^2}dx$ con error $<10^{-6}$: hay que buscar $M_4$ (difícil) [propio]

> Continuando el Ej. 6.34 de U, ¿cuántos subintervalos garantizan error $<10^{-6}$ con el trapecio y con Simpson?

**Antes de calcular**
- **Qué me piden:** $m$ para cada método con tolerancia $10^{-6}$.
- **Cómo lo pienso:** $M_2=2$ ya se conoce (U Ej. 6.34). $M_4$ exige derivar cuatro veces y buscar el máximo de $\lvert f^{(4)}\rvert$ en $[0,1]$: extremos y ceros de $f^{(5)}$.
- **Qué uso:** Teor. 6.3-6.4 (U pp. 269-270); extremos absolutos (U §3.4).
- **Por dónde empiezo:** $f^{(4)}(x)=4(4x^4-12x^2+3)e^{-x^2}$.

1. **Derivadas** (sympy): $f^{(4)}(x)=4(4x^4-12x^2+3)e^{-x^2}$, $f^{(5)}(x)=-8x(4x^4-20x^2+15)e^{-x^2}$.
2. **Candidatos en $[0,1]$:** $x=0$; $x=1$; ceros de $4x^4-20x^2+15$: $x^2=\frac{5\pm\sqrt{10}}2$, es decir $x\approx0{,}9586$ (el otro, $\approx1{,}65$, está fuera).
3. **Valores:** $\lvert f^{(4)}(0)\rvert=12$; $\lvert f^{(4)}(0{,}9586)\rvert\approx7{,}42$; $\lvert f^{(4)}(1)\rvert=20/e\approx7{,}36$. Así **$M_4=12$**.
4. **Trapecio:** $\frac{2}{12m^2}\le10^{-6}\iff m\ge\sqrt{166\,667}\approx408{,}2$: **$m=409$**.
5. **Simpson:** $\frac{12}{2880m^4}\le10^{-6}\iff m^4\ge4166{,}7\iff m\ge8{,}03$: **$m=9$** (19 nodos).
6. **Control:** con $m=9$ Simpson da $0{,}7468242$ (error real $7{,}8\cdot10^{-8}$); el valor es $0{,}74682413\ldots$

**Receta.** Para $M_4$: derivar con cuidado (sacando factor común la exponencial), evaluar $\lvert f^{(4)}\rvert$ en los extremos y en los ceros de $f^{(5)}$ dentro del intervalo, y quedarse con el mayor.

**Error típico.** Tomar $M_4$ de un extremo sin mirar los puntos interiores, o tomar como $M_4$ el máximo de $f^{(4)}$ sin valor absoluto.

sympy: $M_4=12$; $m\ge408{,}25$ y $m\ge8{,}034$; $\int_0^1e^{-x^2}dx=0{,}746824132812427$.

---

## 5. Tabla de valores de referencia (para un interactivo)

Convención de U: $T_n$ = trapecio compuesto con $n$ subintervalos ($n+1$ nodos); $M_n$ = rectángulo central (punto medio) compuesto con $n$ subintervalos; $S_n$ = Simpson compuesta con $n$ subintervalos ($2n+1$ nodos, mismos que $T_{2n}$). «Error» = aproximación − exacto. Calculado con sympy a 15 cifras.

**$\int_0^\pi\mathrm{sen}\,x\,dx=2$**

| $n$ | $T_n$ | error | $M_n$ | error | $S_n$ | error |
|---|---|---|---|---|---|---|
| 2 | 1,57079633 | −4,29e−01 | 2,22144147 | +2,21e−01 | 2,0045597550 | +4,56e−03 |
| 4 | 1,89611890 | −1,04e−01 | 2,05234431 | +5,23e−02 | 2,0002691699 | +2,69e−04 |
| 8 | 1,97423160 | −2,58e−02 | 2,01290909 | +1,29e−02 | 2,0000165910 | +1,66e−05 |

**$\int_0^1e^x\,dx=e-1\approx1{,}718281828$**

| $n$ | $T_n$ | error | $M_n$ | error | $S_n$ | error |
|---|---|---|---|---|---|---|
| 2 | 1,75393109 | +3,56e−02 | 1,70051272 | −1,78e−02 | 1,7183188419 | +3,70e−05 |
| 4 | 1,72722190 | +8,94e−03 | 1,71381528 | −4,47e−03 | 1,7182841547 | +2,33e−06 |
| 8 | 1,72051859 | +2,24e−03 | 1,71716366 | −1,12e−03 | 1,7182819741 | +1,46e−07 |

**$\int_1^2\frac{dx}x=\ln2\approx0{,}693147181$**

| $n$ | $T_n$ | error | $M_n$ | error | $S_n$ | error |
|---|---|---|---|---|---|---|
| 2 | 0,70833333 | +1,52e−02 | 0,68571429 | −7,43e−03 | 0,6932539683 | +1,07e−04 |
| 4 | 0,69702381 | +3,88e−03 | 0,69121989 | −1,93e−03 | 0,6931545307 | +7,35e−06 |
| 8 | 0,69412185 | +9,75e−04 | 0,69266055 | −4,87e−04 | 0,6931476528 | +4,72e−07 |

**$\int_0^1e^{-x^2}dx\approx0{,}746824133$** (sin primitiva elemental)

| $n$ | $T_n$ | error | $M_n$ | error | $S_n$ | error |
|---|---|---|---|---|---|---|
| 2 | 0,73137025 | −1,55e−02 | 0,75459794 | +7,77e−03 | 0,7468553798 | +3,12e−05 |
| 4 | 0,74298410 | −3,84e−03 | 0,74874713 | +1,92e−03 | 0,7468261205 | +1,99e−06 |
| 8 | 0,74586561 | −9,59e−04 | 0,74730358 | +4,79e−04 | 0,7468242574 | +1,25e−07 |

Lecturas para el interactivo: al doblar $n$, el error de $T_n$ y $M_n$ se divide aproximadamente entre **4** ($\sim1/n^2$, como la cota del Teor. 6.3) y el de $S_n$ entre **16** ($\sim1/n^4$, Teor. 6.4); $M_n$ tiene aproximadamente la mitad del error de $T_n$ y signo contrario (por encima/debajo según la concavidad: $\mathrm{sen}$ y $e^{-x^2}$ cóncavas en buena parte del intervalo → $T_n$ por defecto; $e^x$ y $\frac1x$ convexas → $T_n$ por exceso); $S_n=\frac{T_n+2M_n}3$. Para la función de U Ej. 6.29 ($x^3-3{,}3x^2+3x$ en $[1;2{,}5]$, exacta $1{,}303125$), $S_n$ es exacto para todo $n$.

---

## 6. Chuleta rápida del tema

- **Trapecio:** $\frac{b-a}2\big(f(a)+f(b)\big)$; compuesto $\frac h2(E+2C)$, $h=\frac{b-a}n$, $n+1$ nodos.
- **Simpson:** $\frac{b-a}6\big(f(a)+4f(\frac{a+b}2)+f(b)\big)$; compuesta $\frac h6(E+2P+4I)$, $h=\frac{b-a}n$, nodos cada $\frac h2$, $2n+1$ nodos (impares = puntos medios).
- **Rectángulos:** $f(a)(b-a)$, $f(b)(b-a)$, $f(\frac{a+b}2)(b-a)$; compuestos: $h\sum$ de los valores izquierdos, derechos o centrales.
- **Cotas:** trapecio $\varepsilon\le\frac{(b-a)^3}{12m^2}M_2$; Simpson $\varepsilon\le\frac{(b-a)^5}{2880m^4}M_4$. Despejar $m$ y redondear **hacia arriba**.
- **Exactitud:** trapecio exacto en rectas; Simpson exacto en polinomios de grado $\le3$.
- **Errores frecuentes:** confundir nodos con subintervalos; olvidar el 2 de los centrales/pares o el 4 de los impares; en Simpson compuesta, usar la separación entre nodos como $h$; aplicar Simpson con un número par de nodos; tomar $M_2$/$M_4$ sin valor absoluto o en un solo extremo; dejar el resultado sin comparar con el exacto cuando lo piden.
