# Soluciones Tema 6.1 — Definición de integral de Riemann

Resolución paso a paso de los ejercicios de **E** de la sección 6.1 de U (Ejercicios 6.1-6.10, E pp. 214-218; el 6.11 se deja para 6.2, porque usa el teorema fundamental) y de 4 ejemplos propios. Todos los cálculos se han comprobado con sympy (script `v61.py` en el scratchpad). Los enunciados de E pp. 214-218 se han leído también como imagen.

Páginas: U impresa (= PDF + 2); E impresa = PDF; L impresa = PDF − 17.

## 0. Herramientas de teoría que se usan

| Clave | Enunciado (resumido) | Dónde |
|---|---|---|
| Idea: área con rectángulos | Para $f\ge0$ continua en $[a,b]$, el área bajo la gráfica se aproxima por rectángulos y se toma el límite cuando su base se hace pequeña. Ej. 6.1: $\int_0^1e^x\,dx=e-1$ por sumas geométricas y L'Hôpital. | U §6.1.2, pp. 236-238 (Fig. 6.1 p. 237) |
| Área con signo | Si $f$ toma valores negativos, los rectángulos por debajo del eje **restan** (Fig. 6.2). | U p. 238 |
| **Partición y finura** | Partición $P$ de $[a,b]$: puntos $a=x_0<x_1<\dots<x_n=b$; $\Delta x_i=x_i-x_{i-1}$; **finura** $\|P\|=\max_i\Delta x_i$ (longitud del subintervalo más largo). | U p. 238 |
| **Suma de Riemann** | Elegido un $c_i\in[x_{i-1},x_i]$ en cada subintervalo, $S=\sum_{i=1}^n f(c_i)\,\Delta x_i$. | U p. 239 |
| **Def. 6.1** | Para $f:[a,b]\to\mathbb R$ continua, $\displaystyle\int_a^b f(x)\,dx=\lim_{\|P\|\to0}\sum_{i=1}^n f(c_i)\,\Delta x_i$. Para $f$ continua el límite existe y **no depende** de las particiones ni de los $c_i$ elegidos (nota 1, p. 238; p. 240). | U p. 239 |
| Ej. 6.2 | $\int_{-1}^2 2x\,dx=3$ con la partición equiespaciada y $c_i=x_i$; usa $\sum_{i=1}^n i=\frac{n(n+1)}2$ (truco de Gauss en el margen). | U p. 239 |
| **Propiedades** | (P0) $\int_a^a f=0$. (P1) $\int_a^b kf=k\int_a^b f$. (P2) $\int_a^b(f+g)=\int_a^b f+\int_a^b g$. (P3) **Monotonía**: $f\le g$ en $[a,b]$ ⇒ $\int_a^b f\le\int_a^b g$. (P4) $\left|\int_a^b f\right|\le\int_a^b|f|$. (P5) **Aditividad**: $c\in[a,b]$ ⇒ $\int_a^b f=\int_a^c f+\int_c^b f$. (P6) **Cambio de orden**: $\int_a^b f=-\int_b^a f$. | U p. 240 |
| Ej. 6.3 | $\int_{-1}^2 2x\,dx=2\left(-\frac12\right)+2\cdot2=3$ con áreas de triángulos. | U p. 240 |
| **Def. 6.2** | $F$ es **primitiva** de $f$ continua en $(a,b)$ si $F'(x)=f(x)$ para todo $x\in(a,b)$. Notación $\int f(x)\,dx$. La integral indefinida es el conjunto de todas las primitivas: $F+k$, $k\in\mathbb R$. | U p. 241 |
| TVM integral | Si $f$ es continua en $[a,b]$, existe $c\in[a,b]$ con $\int_a^b f=f(c)(b-a)$ (U lo enuncia en el margen y remite a E 6.9 para la demostración). | U p. 244 (margen) |

**Herramientas de temas anteriores que aparecen:**
- **Teorema de los valores intermedios** (U p. 52): si $f$ es continua en $[a,b]$ y $d$ está estrictamente entre $f(a)$ y $f(b)$, existe $c\in(a,b)$ con $f(c)=d$.
- **Teorema de Weierstrass** (U Prop. 1.15, pp. 52-53): una función continua en un intervalo cerrado y acotado alcanza en él un **máximo** y un **mínimo**.
- Regla de L'Hôpital (U §2.3, p. 82), solo para el límite de U Ej. 6.1.
- Fórmula $\sum_{i=1}^n i=\frac{n(n+1)}2$ (U p. 239, margen). La de $\sum i^2$ se deduce en el Propio 1.

**Sumas inferior y superior** (no aparecen en U con ese nombre; se usan en el Propio 4 y ayudan en E 6.6-6.7). Dada una partición, en cada $[x_{i-1},x_i]$ sea $m_i$ el mínimo y $M_i$ el máximo de $f$ (existen por Weierstrass). Entonces
$$s(P)=\sum_{i=1}^n m_i\,\Delta x_i\qquad\text{(suma inferior)},\qquad S(P)=\sum_{i=1}^n M_i\,\Delta x_i\qquad\text{(suma superior)}.$$
Son sumas de Riemann particulares (con $c_i$ en el punto de mínimo o de máximo) y cumplen $s(P)\le\int_a^b f\le S(P)$ (se prueba en el Propio 4 solo con monotonía y aditividad). Explicación detallada en L §4.2, p. 258.

---

### Receta general del tema

> **Calcular una integral por la definición** (sumas de Riemann):
> 1. Partición **equiespaciada**: $\Delta x=\frac{b-a}n$, $x_i=a+i\,\frac{b-a}n$. Su finura es $\frac{b-a}n$, que tiende a $0$ cuando $n\to\infty$: el límite $\|P\|\to0$ se convierte en $\lim_{n\to\infty}$.
> 2. Elegir $c_i$ cómodo (casi siempre $c_i=x_i$, el extremo derecho). Como $f$ es continua, la elección no cambia el resultado (U p. 239).
> 3. Escribir $S_n=\sum_{i=1}^n f(c_i)\,\Delta x$, sacar fuera del sumatorio todo lo que **no** dependa de $i$ y usar $\sum 1=n$, $\sum i=\frac{n(n+1)}2$, $\sum i^2=\frac{n(n+1)(2n+1)}6$.
> 4. Calcular $\lim_{n\to\infty}S_n$.
>
> **Calcular una integral con propiedades/geometría**: partir el intervalo por donde la función cambia de signo o de fórmula (aditividad), sacar constantes (producto por constante) y leer cada trozo como un área conocida (triángulo, rectángulo, semicírculo), **con signo menos** si está bajo el eje.
>
> **Acotar una integral sin calcularla**: si $m\le f(x)\le M$ en $[a,b]$, entonces $m(b-a)\le\int_a^b f\le M(b-a)$ (monotonía + integral de una constante). Para mejorar la cota, partir el intervalo y acotar en cada trozo.

Esquema de las propiedades más usadas, con lo que **no** se cumple:

$$\int(f+g)=\int f+\int g\ \checkmark\qquad \int kf=k\int f\ \checkmark\qquad \int fg\ne\int f\cdot\int g\ \text{(en general)}\qquad \int|f+g|\ne\int|f|+\int|g|\ \text{(en general; solo }\le\text{)}$$

---

## 1. Ejercicios de E (orden de dificultad creciente; numeración conservada)

Orden propuesto para aprender: **6.1 → 6.3 → 6.2** (particiones y finura) **→ 6.4** (definición frente a propiedades) **→ 6.10** (qué es una primitiva) **→ 6.5 → 6.6** (qué propiedades son verdaderas: V/F) **→ 6.8** (aditividad) **→ 6.7** (acotar con la monotonía) **→ 6.9** (demostración del teorema del valor medio integral).

---

### Ejercicio 6.1 (E p. 214)

> Calcula la finura $\|P\|$ de la partición $P=\{1,2,3,5,6\}$ del intervalo $[1,6]$.

**Idea en una frase.** La finura es la longitud del trozo **más largo** en que la partición corta el intervalo.

1. **Comprobar que es una partición de $[1,6]$** (U p. 238): los puntos están ordenados, $1<2<3<5<6$, el primero es $a=1$ y el último $b=6$. Sí lo es, con $n=4$ subintervalos.
2. **Subintervalos:** $[1,2]$, $[2,3]$, $[3,5]$, $[5,6]$.
3. **Longitudes** $\Delta x_i=x_i-x_{i-1}$: $1,\ 1,\ 2,\ 1$.
4. **Finura** = máximo de las longitudes (U p. 238): $\|P\|=\max\{1,1,2,1\}=\boxed{2}$.

**Receta.** Restar puntos consecutivos y quedarse con la mayor diferencia.

**Error típico.** Confundir la finura con el número de puntos ($5$), con el de subintervalos ($4$) o con la longitud media ($\frac54$).

sympy: $\max\{1,1,2,1\}=2$.

---

### Ejercicio 6.3 (E p. 214)

> ¿Puede ser la finura $\|P\|$ de una partición del intervalo $[-\pi,\pi]$ igual a $7$?

**Idea en una frase.** Ningún trozo de un intervalo puede ser más largo que el intervalo entero.

1. **Cada subintervalo está dentro de $[-\pi,\pi]$:** si $-\pi=x_0<\dots<x_n=\pi$, entonces $[x_{i-1},x_i]\subset[-\pi,\pi]$.
2. **Su longitud está acotada:** $\Delta x_i=x_i-x_{i-1}\le \pi-(-\pi)=2\pi$, porque $x_i\le\pi$ y $x_{i-1}\ge-\pi$.
3. **Por tanto la finura** (el máximo de esas longitudes, U p. 238) cumple $\|P\|\le2\pi\approx6{,}2832$.
4. **Comparar:** $7>2\pi$. **No es posible.**
5. **Qué valores sí son posibles:** cualquier número de $(0,2\pi]$. El valor $2\pi$ lo da la partición trivial $P=\{-\pi,\pi\}$ (un único subintervalo).

**Receta.** Para cualquier partición de $[a,b]$: $0<\|P\|\le b-a$.

**Error típico.** Pensar que, añadiendo puntos, la finura puede crecer: añadir puntos solo puede dejarla igual o hacerla más pequeña.

sympy: $2\pi\approx6{,}28319<7$.

---

### Ejercicio 6.2 (E p. 214)

> Define una partición de $[0,4]$ con cien elementos distintos y finura igual a $3$.

**Idea en una frase.** Un salto grande de longitud exactamente $3$ fija la finura; los demás puntos se meten en el trozo que sobra, con saltos pequeños.

1. **Hacer que un subintervalo mida 3:** tomar $x_0=0$ y $x_1=3$. El subintervalo $[0,3]$ mide $3$.
2. **Cuántos puntos faltan:** ya hay $2$; faltan $98$ puntos distintos en $(3,4]$, y el último debe ser $4$.
3. **Repartirlos con saltos pequeños:** por ejemplo $x_{k+1}=3+\frac{k}{98}$, $k=1,\dots,98$. Así $x_2=3+\frac1{98}$, …, $x_{99}=3+\frac{98}{98}=4$.
   $$P=\Big\{0,\ 3,\ 3+\tfrac1{98},\ 3+\tfrac2{98},\ \dots,\ 4\Big\}.$$
4. **Contar:** $2+98=100$ puntos, todos distintos y ordenados; empieza en $0$ y acaba en $4$. Es una partición (U p. 238).
5. **Finura:** el primer subintervalo mide $3$; todos los demás miden $\frac1{98}<3$. Así $\|P\|=3$.
6. **Otra posible** (el trozo grande al final): $y_i=\frac{i}{98}$ para $i=0,\dots,98$ (de $0$ a $1$ con saltos de $\frac1{98}$) y después el punto $4$. Son $99+1=100$ puntos; el último subintervalo $[1,4]$ mide $3$ y es el mayor. Hay infinitas respuestas válidas.

**Receta.** Para finura $\delta$: un subintervalo de longitud exactamente $\delta$ y el resto de puntos con saltos menores que $\delta$. Comprobar al final: número de puntos, primer y último punto, y máximo de las longitudes.

**Error típico.** Contar mal: «cien elementos» son $100$ **puntos**, es decir, $99$ subintervalos.

sympy: ambas particiones tienen $100$ elementos distintos y finura $3$.

---

### Ejercicio 6.4 (E pp. 214-215)

> Muestra que la integral definida de la función nula es cero en cualquier intervalo: (i) utilizando la definición de integral; (ii) utilizando las propiedades de la integral (pista: solamente $0$ verifica $0+0=0$).

**Idea en una frase.** (i) Todos los rectángulos tienen altura $0$; (ii) llamando $I$ a la integral, las propiedades dan $I=I+I$, y eso solo lo cumple $I=0$.

**(i) Con la definición (Def. 6.1, U p. 239).**
1. **Hipótesis de la definición:** la función nula $f(x)=0$ es continua en $[a,b]$ ($a<b$), así que la integral existe y es el límite de las sumas de Riemann.
2. **Cualquier suma de Riemann:** para cualquier partición y cualesquiera $c_i$, $f(c_i)=0$, luego
   $$\sum_{i=1}^n f(c_i)\,\Delta x_i=\sum_{i=1}^n 0\cdot\Delta x_i=0.$$
3. **Límite:** las sumas son **todas** iguales a $0$, así que su límite cuando $\|P\|\to0$ es $0$ (el límite de una constante es esa constante):
   $$\int_a^b0\,dx=\lim_{\|P\|\to0}0=0.$$
4. **Si $a=b$** vale por (P0) y si $a>b$, por (P6): $\int_a^b0=-\int_b^a0=-0=0$.

**(ii) Con las propiedades (U p. 240).**
1. **Llamar $I=\int_a^b 0\,dx$.** Es un número real; queremos ver que $I=0$.
2. **Escribir la función nula como suma:** $0=0+0$ (como funciones: para cada $x$, $0=0+0$). Así $I=\int_a^b(0+0)\,dx$.
3. **Integral de la suma (P2):** $\int_a^b(0+0)=\int_a^b0+\int_a^b0=I+I$.
4. **Juntar:** $I=I+I$. Restando $I$ a ambos lados: $0=I$. (Es la pista: el único real con $I+I=I$ es el $0$.)
5. **Otra forma (P1):** $0=0\cdot g$ para cualquier función continua $g$, luego $\int_a^b0=\int_a^b0\cdot g=0\cdot\int_a^b g=0$.

**Receta.** Para probar que un número $I$ es $0$ basta ver que cumple una propiedad que solo tiene el $0$ ($I=I+I$, $I=-I$, $I=0\cdot J$…).

**Error típico.** Decir «es cero porque el área es cero» sin usar ni la definición ni las propiedades: el ejercicio pide justificar con ellas.

---

### Ejercicio 6.10 (E p. 218)

> Sea $F:\mathbb R\to\mathbb R$ una primitiva de una función continua $f:\mathbb R\to\mathbb R$ y $C\in\mathbb R$ una constante. Señale la opción correcta: a) $F'(x)=f(x)$ para $x\in\mathbb R$. b) $f'(x)=F(x)+C$ para $x\in\mathbb R$. c) $f'(x)=F(x)$ para $x\in\mathbb R$. d) $F'(x)=f(x)+C$ para $x\in\mathbb R$.

**Idea en una frase.** «$F$ es primitiva de $f$» significa exactamente «derivando $F$ sale $f$»; la constante va en $F$, no en $F'$.

1. **Definición** (Def. 6.2, U p. 241, aquí con dominio $\mathbb R$): $F$ es primitiva de $f$ si $F'(x)=f(x)$ para todo $x$.
2. **a) Verdadera:** es literalmente la definición.
3. **Ejemplo para probar las demás:** $f(x)=1$ (continua), $F(x)=x$ (primitiva, pues $F'=1$) y $C=1$.
4. **b) Falsa:** $f'(x)=0$ pero $F(x)+C=x+1$; no coinciden (por ejemplo en $x=0$: $0\ne1$). Además, $f$ no tiene por qué ser derivable (solo se sabe que es continua).
5. **c) Falsa:** $f'(x)=0\ne x=F(x)$ para $x\ne0$. Confunde la dirección: es $F'=f$, no $f'=F$.
6. **d) Falsa:** $F'(x)=1$ y $f(x)+C=2$. Solo sería cierta si $C=0$, pero $C$ es una constante cualquiera. Lo correcto es que $F+C$ es otra primitiva: $(F+C)'=F'=f$.
7. **Respuesta: a).**

**Receta.** Ante una afirmación sobre primitivas, traducirla a «derivada de la primitiva = integrando» y probar con $f=1$, $F=x$.

**Error típico.** Poner la constante en el lado de la derivada ($F'=f+C$): la constante aparece en la primitiva, $\int f=F+C$, y desaparece al derivar.

---

### Ejercicio 6.5 (E pp. 215-216)

> Dadas $f,g$ continuas en $[a,b]$ señala la o las propiedades que **no** son siempre correctas:
> a) $\displaystyle\int_a^b(f+g)=\int_a^b f+\int_a^b g$. b) $\displaystyle\int_a^b|f+g|=\int_a^b|f|+\int_a^b|g|$. c) $\displaystyle\int_a^b(f-g)=\int_a^b f+\int_b^a g$. d) $\displaystyle\int_a^b|f-g|=\int_a^b|f|-\int_b^a|g|$.

**Idea en una frase.** La integral respeta sumas y constantes, pero **no** el valor absoluto: $|f+g|$ no es $|f|+|g|$ cuando $f$ y $g$ tienen signos opuestos.

Se supone $a<b$ (si $a=b$ todo vale $0$ y no hay nada que discutir).

1. **a) Verdadera:** es la propiedad (P2) de la suma (U p. 240).
2. **c) Verdadera.** Se transforma el lado izquierdo con las propiedades, justificando cada igualdad:
   $$\int_a^b(f-g)\overset{(P2)}=\int_a^b f+\int_a^b(-1)g\overset{(P1)}=\int_a^b f-\int_a^b g\overset{(P6)}=\int_a^b f+\int_b^a g.$$
   En el último paso, (P6) dice $\int_a^b g=-\int_b^a g$, así que $-\int_a^b g=+\int_b^a g$.
3. **b) Falsa.** Basta un contraejemplo. Con $f(x)=1$ y $g(x)=-1$:
   - Izquierda: $|f+g|=|0|=0$, así que $\int_a^b|f+g|=0$ (E 6.4).
   - Derecha: $|f|=|g|=1$, así que $\int_a^b1+\int_a^b1=2(b-a)>0$.
   - $0\ne2(b-a)$. (Lo único cierto en general es la desigualdad $\int_a^b|f+g|\le\int_a^b|f|+\int_a^b|g|$, que sale de $|f+g|\le|f|+|g|$ y la monotonía.)
4. **d) Falsa.** Primero se simplifica el lado derecho con (P6): $-\int_b^a|g|=+\int_a^b|g|$, luego d) dice
   $$\int_a^b|f-g|=\int_a^b|f|+\int_a^b|g|.$$
   Contraejemplo: $f(x)=g(x)=1$. Izquierda: $|f-g|=0$, integral $0$. Derecha: $(b-a)+(b-a)=2(b-a)\ne0$.
   (Cuidado al elegir el contraejemplo: con $f=1$, $g=-1$ los dos lados valen $2(b-a)$ y **no** sirve. Un contraejemplo tiene que hacer falsa la igualdad, no basta con elegir funciones «sencillas».)
5. **Respuesta: b) y d)** no son siempre correctas.

**Receta.** En un V/F de propiedades: si coincide con una propiedad de U p. 240 (o se obtiene encadenando varias), es verdadera; si no, buscar un contraejemplo con funciones constantes ($1$, $-1$) y **comprobar** que los dos lados dan distinto.

**Error típico.** Pasar el valor absoluto «a través» de la suma, y no simplificar primero los $\int_b^a$ con el cambio de orden antes de buscar el contraejemplo.

sympy: b) con $f=1,g=-1$ en $[0,1]$: $0$ frente a $2$; d) con $f=g=1$: $0$ frente a $2$; d) con $f=1,g=-1$: $2$ frente a $2$ (no es contraejemplo).

---

### Ejercicio 6.6 (E pp. 216-217)

> Dadas $f,g:[a,b]\to\mathbb R$ continuas, señala la propiedad que **no** es siempre correcta:
> a) $\displaystyle(b-a)\min_{x\in[a,b]}f(x)\le\int_a^b f(x)\,dx\le(b-a)\max_{x\in[a,b]}f(x)$. b) $\displaystyle\int_a^b f(x)g(x)\,dx=\int_a^b f(x)\,dx\cdot\int_a^b g(x)\,dx$. c) $\displaystyle\int_a^b f(x)\,dx=\int_a^{\frac{b+a}2}f(x)\,dx+\int_{\frac{b+a}2}^b f(x)\,dx$.

**Idea en una frase.** La integral está entre el rectángulo «bajo» y el «alto» (a), se puede partir por cualquier punto (c), pero no convierte productos en productos (b).

1. **a) Verdadera.**
   - **Existen el mínimo y el máximo:** $f$ es continua en el intervalo cerrado y acotado $[a,b]$, así que, por Weierstrass (U Prop. 1.15, p. 52), alcanza un mínimo $m$ y un máximo $M$.
   - **Desigualdad punto a punto:** por definición de mínimo y máximo, $m\le f(x)\le M$ para todo $x\in[a,b]$.
   - **Monotonía (P3, U p. 240):** $\int_a^b m\,dx\le\int_a^b f\le\int_a^b M\,dx$.
   - **Integral de una constante:** $\int_a^b k\,dx=k\int_a^b1\,dx=k(b-a)$, porque toda suma de Riemann de la función $1$ vale $\sum\Delta x_i=b-a$ (Def. 6.1) y (P1) saca la $k$.
   - Juntando: $m(b-a)\le\int_a^b f\le M(b-a)$.
2. **b) Falsa.** Contraejemplo con $f(x)=g(x)=x$ en $[0,1]$:
   - $\int_0^1x\cdot x\,dx=\int_0^1x^2\,dx=\frac13$ (se calcula por la definición en el Propio 1).
   - $\int_0^1x\,dx=\frac12$ (triángulo de base $1$ y altura $1$), así que el producto es $\frac12\cdot\frac12=\frac14$.
   - $\frac13\ne\frac14$.
3. **c) Verdadera.** $\frac{a+b}2$ es el punto medio de $[a,b]$, luego pertenece a $[a,b]$, y la aditividad (P5, U p. 240) con $c=\frac{a+b}2$ da exactamente c).
4. **Respuesta: b).**

**Receta.** Recordar la lista de U p. 240: suma, constante, monotonía, valor absoluto (desigualdad), aditividad, cambio de orden. **No** hay propiedad para el producto ni para el cociente.

**Error típico.** Creer que $\int fg=\int f\int g$ «porque con la suma funciona».

sympy: $\int_0^1x^2=\frac13$, $\left(\int_0^1x\right)^2=\frac14$.

---

### Ejercicio 6.8 (E p. 217)

> Calcula $\displaystyle\int_{-\pi}^{\frac\pi2}f$, con $f$ continua en $\mathbb R$ y tal que $\displaystyle\int_{-\pi}^{e}f=\int_{\frac\pi2}^{e}f$.

**Idea en una frase.** El trozo de $-\pi$ a $e$ es el trozo de $-\pi$ a $\frac\pi2$ más el de $\frac\pi2$ a $e$; si el total es igual al segundo trozo, el primero vale $0$.

1. **Situar los puntos:** $-\pi\approx-3{,}14<\frac\pi2\approx1{,}57<e\approx2{,}72$. Así $\frac\pi2\in[-\pi,e]$.
2. **Aditividad (P5, U p. 240)** con $c=\frac\pi2$ (se puede porque $f$ es continua en $[-\pi,e]$ y $c$ está dentro):
   $$\int_{-\pi}^{e}f=\int_{-\pi}^{\frac\pi2}f+\int_{\frac\pi2}^{e}f.$$
3. **Usar el dato:** el lado izquierdo es igual a $\int_{\pi/2}^{e}f$:
   $$\int_{\frac\pi2}^{e}f=\int_{-\pi}^{\frac\pi2}f+\int_{\frac\pi2}^{e}f.$$
4. **Restar** $\int_{\pi/2}^{e}f$ (un número real) a ambos lados: $\boxed{\displaystyle\int_{-\pi}^{\frac\pi2}f=0}$.

**Receta.** Si aparecen integrales sobre intervalos que encajan, escribirlas todas con la aditividad en función de los trozos «básicos» y resolver como un sistema de ecuaciones.

**Error típico.** Concluir que $f=0$ en $[-\pi,\frac\pi2]$. Solo es cero la **integral** (áreas con signo que se compensan). Por ejemplo, $f(x)=\operatorname{sen}\!\big(\tfrac43(x+\pi)\big)$ es continua en $\mathbb R$ y no es nula, pero en $[-\pi,\frac\pi2]$ su argumento recorre $[0,2\pi]$ (una vuelta completa): la parte positiva y la negativa se compensan y $\int_{-\pi}^{\pi/2}f=0$. Como la integral sobre $[-\pi,\frac\pi2]$ es $0$, por la aditividad cumple también el dato del enunciado.

sympy: $\int_{-\pi}^{\pi/2}\operatorname{sen}\!\big(\tfrac43(x+\pi)\big)\,dx=0$.

---

### Ejercicio 6.7 (E p. 217)

> Demuestra que si $f:[-1,1]\to\mathbb R$ es continua y tal que $-2\le f(x)\le4$ para todo $x\in[-1,1]$, entonces $\displaystyle-4\le\int_{-1}^1f(x)\,dx\le8$.

**Idea en una frase.** El área con signo está entre la de un rectángulo de altura $-2$ y la de uno de altura $4$, ambos de base $2$.

1. **Comparar funciones:** en $[-1,1]$ se tiene $-2\le f(x)\le4$, es decir, la función constante $-2$ queda por debajo de $f$ y la constante $4$ por encima.
2. **Monotonía (P3, U p. 240)**, aplicada dos veces (las tres funciones son continuas):
   $$\int_{-1}^1(-2)\,dx\le\int_{-1}^1f(x)\,dx\le\int_{-1}^14\,dx.$$
3. **Integral de una constante** ($\int_a^b k\,dx=k(b-a)$, ver E 6.6 a): la base es $1-(-1)=2$, luego $\int_{-1}^1(-2)\,dx=-4$ y $\int_{-1}^14\,dx=8$.
4. **Conclusión:** $-4\le\int_{-1}^1f\le8$.
5. **Las cotas no se pueden mejorar con solo estos datos:** $f\equiv-2$ da exactamente $-4$ y $f\equiv4$ da $8$.

**Receta.** $m\le f\le M$ en $[a,b]$ ⇒ $m(b-a)\le\int_a^b f\le M(b-a)$. La base es $b-a$, **no** $b$.

**Error típico.** Multiplicar por $1$ (el extremo superior) en lugar de por la longitud $2$, y obtener $-2\le\int\le4$.

sympy: $-2\cdot2=-4$, $4\cdot2=8$.

---

### Ejercicio 6.9 (E p. 218)

> Demuestra el teorema del valor medio del cálculo integral que garantiza, para cualquier función continua en $[a,b]$, la existencia de un punto $c\in[a,b]$ tal que $\displaystyle\int_a^b f(x)\,dx=f(c)(b-a)$.

**Idea en una frase.** La «altura media» $\mu=\frac1{b-a}\int_a^b f$ está entre el mínimo y el máximo de $f$ (E 6.6 a), y una función continua toma todos los valores entre su mínimo y su máximo (valores intermedios).

Se supone $a<b$ (si $a=b$ ambos lados valen $0$ y cualquier $c=a$ sirve).

1. **Mínimo y máximo alcanzados** (Weierstrass, U Prop. 1.15, p. 52): existen $p,q\in[a,b]$ con $f(p)=m$ (mínimo) y $f(q)=M$ (máximo).
2. **Acotar la integral** (E 6.6 a): $m(b-a)\le\int_a^b f\le M(b-a)$.
3. **Dividir entre $b-a>0$** (no cambia el sentido de las desigualdades) y llamar $\mu=\frac1{b-a}\int_a^b f$:
   $$f(p)=m\le\mu\le M=f(q).$$
4. **Buscar un $c$ con $f(c)=\mu$.** Hay tres casos:
   - Si $\mu=m$: sirve $c=p$.
   - Si $\mu=M$: sirve $c=q$.
   - Si $m<\mu<M$: entonces $p\ne q$. Se aplica el **teorema de los valores intermedios** (U p. 52) a $f$ en el intervalo cerrado de extremos $p$ y $q$ (en $[p,q]$ si $p<q$, o en $[q,p]$ si $q<p$): $f$ es continua ahí y $\mu$ está estrictamente entre los valores de $f$ en los extremos, $f(p)=m$ y $f(q)=M$. Existe $c$ entre $p$ y $q$ (luego $c\in[a,b]$) con $f(c)=\mu$.
5. **Deshacer la división:** $f(c)=\frac1{b-a}\int_a^b f$ equivale a $\int_a^b f(x)\,dx=f(c)(b-a)$. ∎

**Interpretación.** El área bajo $f$ es igual a la de un rectángulo de la misma base y de altura $f(c)$, un valor que la función realmente toma.

**Receta.** Para probar que una función continua toma un valor $\mu$: encajar $\mu$ entre dos valores de la función (aquí, mínimo y máximo, por Weierstrass) y aplicar valores intermedios en el intervalo que une los puntos donde se alcanzan.

**Error típico.** Aplicar valores intermedios en $[a,b]$ con $f(a)$ y $f(b)$: $\mu$ no tiene por qué estar entre $f(a)$ y $f(b)$ (ej.: $f(x)=\operatorname{sen}x$ en $[0,\pi]$, $f(0)=f(\pi)=0$ y $\mu=\frac2\pi$). Hay que usar los puntos del mínimo y del máximo. Otro error: olvidar los casos $\mu=m$ o $\mu=M$, en que el teorema (con desigualdades estrictas) no se aplica pero el punto ya se tiene.

sympy: $\frac1\pi\int_0^\pi\operatorname{sen}x\,dx=\frac2\pi\approx0{,}6366$, que está entre $0$ y $1$ y no entre $f(0)=0$ y $f(\pi)=0$.

---

## 2. Ejemplos propios (dificultad creciente)

### Propio 1 — Integrales por la definición: una recta y $x^2$ en $[0,1]$ (fácil-medio)

> (a) Calcula $\displaystyle\int_0^1(3x+1)\,dx$ con sumas de Riemann. (b) Calcula $\displaystyle\int_0^1x^2\,dx$ con sumas de Riemann.

**(a)**
1. **Partición equiespaciada** de $[0,1]$ en $n$ trozos: $x_i=\frac in$, $\Delta x_i=\frac1n$. Finura $\frac1n\to0$ cuando $n\to\infty$ (Def. 6.1, U p. 239).
2. **Puntos $c_i$:** el extremo derecho, $c_i=x_i=\frac in$ (vale cualquiera porque $f$ es continua).
3. **Suma de Riemann:** $S_n=\sum_{i=1}^n\Big(3\frac in+1\Big)\frac1n=\frac3{n^2}\sum_{i=1}^n i+\frac1n\sum_{i=1}^n1$.
4. **Sumatorios** (U p. 239, margen): $\sum_{i=1}^n i=\frac{n(n+1)}2$, $\sum_{i=1}^n1=n$. Así $S_n=\frac{3(n+1)}{2n}+1=\frac{5n+3}{2n}$.
5. **Límite:** $\lim_{n\to\infty}\frac{5n+3}{2n}=\frac52$. Luego $\int_0^1(3x+1)\,dx=\frac52$.
6. **Comprobación geométrica:** es un trapecio de alturas $f(0)=1$ y $f(1)=4$ y base $1$: área $\frac{1+4}2=\frac52$.

**(b)**
1. **Misma partición** y $c_i=\frac in$: $S_n=\sum_{i=1}^n\frac{i^2}{n^2}\cdot\frac1n=\frac1{n^3}\sum_{i=1}^n i^2$.
2. **Fórmula de $\sum i^2$** (truco telescópico, análogo al de Gauss): para cada $i$, $(i+1)^3-i^3=3i^2+3i+1$. Sumando de $i=1$ a $n$, a la izquierda se cancela todo salvo $(n+1)^3-1$:
   $$(n+1)^3-1=3\sum i^2+3\,\frac{n(n+1)}2+n\ \Longrightarrow\ \sum_{i=1}^n i^2=\frac{n(n+1)(2n+1)}6.$$
   (Comprobación con $n=2$: $1+4=5=\frac{2\cdot3\cdot5}6$.)
3. **Suma:** $S_n=\frac{(n+1)(2n+1)}{6n^2}$.
4. **Límite:** dividiendo numerador y denominador por $n^2$, $S_n=\frac{(1+\frac1n)(2+\frac1n)}6\to\frac26=\frac13$.
5. **Con el extremo izquierdo** $c_i=\frac{i-1}n$ sale $\frac{(n-1)(2n-1)}{6n^2}$, distinto para cada $n$ (con $n=10$: $0{,}285$ frente a $0{,}385$ por la derecha) pero **con el mismo límite** $\frac13$, como asegura U p. 239.

**Receta.** $\Delta x=\frac{b-a}n$, $c_i=a+i\Delta x$, sacar del sumatorio lo que no depende de $i$, aplicar $\sum1,\sum i,\sum i^2$ y tomar $\lim_{n\to\infty}$.

**Error típico.** Olvidar el factor $\Delta x=\frac1n$ (la base de los rectángulos): la suma diverge.

sympy: (a) $S_n=\frac{5n+3}{2n}\to\frac52$; (b) $S_n=\frac{(n+1)(2n+1)}{6n^2}\to\frac13$, izquierda $\frac{(n-1)(2n-1)}{6n^2}\to\frac13$; $\sum i^2=\frac{n(n+1)(2n+1)}6$.

### Propio 2 — Área con signo y propiedades con una gráfica (medio)

> (a) Calcula $\displaystyle\int_{-1}^2 2x\,dx$ con áreas. (b) Calcula $\displaystyle\int_{-2}^2\big(x+\sqrt{4-x^2}\big)\,dx$ y $\displaystyle\int_{2}^{-2}\big(x+\sqrt{4-x^2}\big)\,dx$ sin primitivas.

**(a)** (U Ej. 6.3, p. 240)
1. **Constante fuera (P1):** $\int_{-1}^2 2x\,dx=2\int_{-1}^2x\,dx$.
2. **Partir donde cambia el signo (P5):** $x<0$ en $(-1,0)$ y $x>0$ en $(0,2)$; $\int_{-1}^2x=\int_{-1}^0x+\int_0^2x$.
3. **Leer áreas:** en $[-1,0]$ la recta $y=x$ forma bajo el eje un triángulo de base $1$ y altura $1$: área $\frac12$, **con signo menos** (U p. 238). En $[0,2]$, triángulo de base $2$ y altura $2$ sobre el eje: $+2$.
4. **Resultado:** $2\left(-\frac12+2\right)=3$, como con la definición (U Ej. 6.2).

**(b)**
1. **Separar (P2):** $\int_{-2}^2x\,dx+\int_{-2}^2\sqrt{4-x^2}\,dx$.
2. **Primer sumando:** dos triángulos de base $2$ y altura $2$, uno debajo ($-2$, en $[-2,0]$) y otro encima ($+2$, en $[0,2]$): total $0$.
3. **Segundo sumando:** $y=\sqrt{4-x^2}\ge0$ es la mitad superior de la circunferencia $x^2+y^2=4$ (radio $2$). El área bajo ella es medio círculo: $\frac{\pi\cdot2^2}2=2\pi$.
4. **Resultado:** $\int_{-2}^2\big(x+\sqrt{4-x^2}\big)\,dx=0+2\pi=2\pi$.
5. **Con los límites al revés (P6):** $\int_2^{-2}(\dots)=-2\pi$.
6. **Variante:** $\int_{-2}^2\big(\sqrt{4-x^2}-1\big)\,dx=2\pi-4$ (se resta el rectángulo de base $4$ y altura $1$).

**Receta.** Dibujar, partir por los ceros (aditividad), separar sumandos y constantes, y leer figuras conocidas con su signo.

**Error típico.** Sumar el área del triángulo de debajo del eje con signo $+$: eso daría el **área geométrica** ($\frac12+2=\frac52$ en (a), antes de multiplicar por 2), no la integral.

sympy: $\int_{-1}^22x=3$; $\int_{-2}^2(x+\sqrt{4-x^2})=2\pi$; $\int_{-2}^2(\sqrt{4-x^2}-1)=2\pi-4$.

### Propio 3 — Estimar una integral con cotas mínimo/máximo (medio-difícil)

> Sin calcular primitivas, acota $\displaystyle I=\int_0^1e^{-x^2}\,dx$. Mejora la cota partiendo el intervalo en dos y en cuatro trozos.

1. **Monotonía de $f(x)=e^{-x^2}$ en $[0,1]$:** al crecer $x\ge0$ crece $x^2$, decrece $-x^2$ y decrece $e^{-x^2}$ (la exponencial es creciente). Así el máximo está a la izquierda de cada trozo y el mínimo a la derecha.
2. **Un trozo** ($m=f(1)=e^{-1}$, $M=f(0)=1$; E 6.6 a): $e^{-1}\cdot1\le I\le1\cdot1$, es decir, $0{,}3679\le I\le1$.
3. **Dos trozos** (aditividad P5 con $c=\frac12$ y el mismo argumento en cada mitad):
   $$\tfrac12\big(e^{-1/4}+e^{-1}\big)\le I\le\tfrac12\big(1+e^{-1/4}\big)\ \Longrightarrow\ 0{,}5733\le I\le0{,}8894.$$
4. **Cuatro trozos** (puntos $0,\frac14,\frac12,\frac34,1$): $\frac14\sum_{k=1}^4e^{-(k/4)^2}\le I\le\frac14\sum_{k=0}^3e^{-(k/4)^2}$, es decir, $0{,}6640\le I\le0{,}8220$.
5. **Qué se observa:** la horquilla se estrecha al refinar ($0{,}63$ → $0{,}32$ → $0{,}16$: en este caso la anchura es $\frac{f(0)-f(1)}n=\frac{1-e^{-1}}n$, se divide por 2 al duplicar los trozos). El valor real es $I\approx0{,}7468$.
6. **TVM integral (E 6.9):** existe $c\in[0,1]$ con $e^{-c^2}=I\approx0{,}7468$, es decir, $c\approx0{,}54$.

**Receta.** Si $f$ es monótona en cada trozo, $m_i$ y $M_i$ están en los extremos del trozo: suma inferior $\le I\le$ suma superior. Para afinar, más trozos.

**Error típico.** Tomar el mínimo en el extremo izquierdo sin mirar si la función crece o decrece.

sympy: $I=0{,}746824$; cotas $[0{,}3679;1]$, $[0{,}5733;0{,}8894]$, $[0{,}6640;0{,}8220]$.

### Propio 4 — Suma inferior y superior con una partición no equiespaciada (difícil)

> Sea $f(x)=x^2$ en $[-1,2]$ y $P=\{-1,0,\frac12,2\}$. (a) Calcula la finura, la suma inferior $s(P)$ y la superior $S(P)$. (b) Justifica que $s(P)\le\int_{-1}^2x^2\,dx\le S(P)$ usando solo propiedades de U. (c) Añade el punto $1$ y repite. Compara con el valor exacto $3$.

**(a)**
1. **Subintervalos y longitudes:** $[-1,0]$ ($\Delta x_1=1$), $[0,\frac12]$ ($\Delta x_2=\frac12$), $[\frac12,2]$ ($\Delta x_3=\frac32$). Finura $\|P\|=\frac32$.
2. **Mínimo y máximo en cada trozo** ($x^2$ decrece en $[-1,0]$ y crece en $[0,2]$; Weierstrass asegura que existen):
   - $[-1,0]$: $m_1=f(0)=0$, $M_1=f(-1)=1$.
   - $[0,\frac12]$: $m_2=0$, $M_2=\frac14$.
   - $[\frac12,2]$: $m_3=\frac14$, $M_3=4$.
3. **Sumas:** $s(P)=0\cdot1+0\cdot\frac12+\frac14\cdot\frac32=\frac38$; $S(P)=1\cdot1+\frac14\cdot\frac12+4\cdot\frac32=1+\frac18+6=\frac{57}8$.

**(b)**
1. En cada trozo $m_i\le f(x)\le M_i$, y por **monotonía** (P3) e integral de constante: $m_i\,\Delta x_i\le\int_{x_{i-1}}^{x_i}f\le M_i\,\Delta x_i$.
2. Sumando las tres desigualdades y usando la **aditividad** (P5) dos veces, $\int_{-1}^0+\int_0^{1/2}+\int_{1/2}^2=\int_{-1}^2$:
   $$\tfrac38=s(P)\le\int_{-1}^2x^2\,dx\le S(P)=\tfrac{57}8.$$

**(c)**
1. **Nueva partición** $P'=\{-1,0,\frac12,1,2\}$: el trozo $[\frac12,2]$ se parte en $[\frac12,1]$ ($m=\frac14$, $M=1$, base $\frac12$) y $[1,2]$ ($m=1$, $M=4$, base $1$). Finura $1$.
2. **Sumas:** $s(P')=0+0+\frac14\cdot\frac12+1\cdot1=\frac98$; $S(P')=1+\frac18+1\cdot\frac12+4\cdot1=\frac{45}8$.
3. **Comparación:** $\frac38\le\frac98\le3\le\frac{45}8\le\frac{57}8$. Al **añadir puntos**, la suma inferior sube y la superior baja: la horquilla se estrecha alrededor de $3$.
4. **Por qué:** al partir un trozo, el mínimo en cada mitad es $\ge$ el mínimo en el trozo entero (se mira en menos puntos) y el máximo es $\le$.
5. **Cualquier suma de Riemann** con la partición $P$ queda entre $s(P)$ y $S(P)$; por ejemplo, con los puntos medios sale $\frac{21}8=2{,}625$.

**Receta.** Para cada subintervalo: localizar dónde $f$ es mínima y máxima (extremos del trozo, o un punto interior donde la función cambia de crecer a decrecer, como $x=0$ para $x^2$), multiplicar por la longitud de **ese** trozo y sumar.

**Error típico.** Tomar siempre $m_i$ en el extremo izquierdo: en $[-1,0]$, $f(-1)=1$ es el **máximo**, no el mínimo, porque $x^2$ decrece ahí. Otro: usar una longitud común para todos los trozos cuando la partición no es equiespaciada.

sympy: $s(P)=\frac38$, $S(P)=\frac{57}8$, $s(P')=\frac98$, $S(P')=\frac{45}8$, puntos medios $\frac{21}8$, $\int_{-1}^2x^2=3$.
