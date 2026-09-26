# Tema 2.4: Método de Newton. Método de punto fijo. Soluciones de los ejercicios 2.34-2.38

**Fuentes.** U = *Cálculo para Ingenieros* (§2.4, pp. 86-94 impresas). E = *Libro de ejercicios* (Ej. 2.34-2.38, pp. 72-76). S = Stewart §4.8 (pp. 338-343). L = Larson §3.8 (pp. 225-230 impresas).
Todas las páginas son **impresas** y se han comprobado en `fuentes_txt/*.txt`. Todas las tablas se han generado con Python (fracciones exactas, `sympy`/`mpmath` con 30 cifras) y se han redondeado al mostrarlas.

**Orden recomendado para estudiar** (la numeración original no cambia):
bloque Newton **2.34 → 2.35 → 2.36**; después el bloque de punto fijo **2.38 → 2.37**. El 2.38 enseña a comprobar las hipótesis del teorema, y el 2.37 solo usa la cota del error, que viene justo después (Teorema 2.3).

**Dos fórmulas que se usan en todo el tema**

| Método | Iteración | Referencia |
|---|---|---|
| Newton (para $f(x)=0$) | $x_{n+1}=x_n-\dfrac{f(x_n)}{f'(x_n)}$ | U §2.4.2, p. 88 |
| Punto fijo (para $x=g(x)$) | $x_{n+1}=g(x_n)$ | U §2.4.3, p. 90, ec. (2.3) |

---

## Ejercicio 2.34 (E p. 72)

> Usando el Método de Newton, calcula un valor aproximado de $\sqrt5$, realizando cuatro iteraciones.

### Solución

1. **Convertir «calcular $\sqrt5$» en «resolver $f(x)=0$».** Newton no calcula números: calcula **ceros de funciones**. Como $\sqrt5$ es el número positivo cuyo cuadrado vale 5, es una solución de $x^2-5=0$. Tomamos $f(x)=x^2-5$, que es un polinomio y por tanto derivable en todo $\mathbb R$ (requisito del método, U p. 88: «se puede aplicar para funciones $f$ derivables»). Su derivada es $f'(x)=2x$.

2. **Elegir $x_0$ con criterio.** $f(2)=-1<0$ y $f(3)=4>0$. Como $f$ es continua, el **Teorema de Bolzano** (U §1.4, p. 52) garantiza un cero en $(2,3)$. Por eso $x_0=2$ es un punto de partida razonable. Además $f'(x_0)=4\neq0$, así que la fórmula se puede aplicar (si $f'(x_n)=0$, la tangente es horizontal, no corta al eje y el método se detiene: U p. 88 y nota al margen de p. 89).

3. **Escribir y simplificar la iteración.** Sustituimos en $x_{n+1}=x_n-f(x_n)/f'(x_n)$:
$$x_{n+1}=x_n-\frac{x_n^2-5}{2x_n}=\frac{2x_n^2-x_n^2+5}{2x_n}=\frac12\Big(x_n+\frac5{x_n}\Big).$$
Esta forma (la «regla de Herón», L §3.8 ej. 19, p. 229) es la media entre $x_n$ y $5/x_n$. Si $x_n$ se queda corto, $5/x_n$ se pasa, y la media cae entre los dos.

4. **Iterar** (con fracciones exactas, para ver qué ocurre de verdad):
$$x_1=\tfrac12\big(2+\tfrac52\big)=\tfrac94,\qquad x_2=\tfrac12\big(\tfrac94+\tfrac{20}{9}\big)=\tfrac{161}{72},\qquad x_3=\tfrac{51841}{23184},\qquad x_4=\tfrac{5374978561}{2403763488}.$$

| $n$ | $x_n$ | $f(x_n)$ | $f'(x_n)$ | error real $\lvert x_n-\sqrt5\rvert$ | $\varepsilon_r=\frac{\lvert x_n-x_{n-1}\rvert}{\lvert x_n\rvert}$ |
|---|---|---|---|---|---|
| 0 | 2 | $-1$ | 4 | $2.36\times10^{-1}$ | — |
| 1 | 2.25 | 0.0625 | 4.5 | $1.39\times10^{-2}$ | $1.11\times10^{-1}$ |
| 2 | 2.236111111111 | $1.93\times10^{-4}$ | 4.472222 | $4.31\times10^{-5}$ | $6.21\times10^{-3}$ |
| 3 | 2.236067977916 | $1.86\times10^{-9}$ | 4.472136 | $4.16\times10^{-10}$ | $1.93\times10^{-5}$ |
| 4 | 2.236067977500 | $1.7\times10^{-19}$ | 4.472136 | $3.9\times10^{-20}$ | $1.86\times10^{-10}$ |

($\sqrt5=2.2360679774997\ldots$)

5. **Conclusión.** $\sqrt5\approx x_4=2.2360679775$. Con 4 decimales, como en E, $x_2=x_3=x_4=2.2361$.

6. **Por qué converge tan rápido (propio, solo álgebra).** Restando $\sqrt5$ en la fórmula del paso 3:
$$x_{n+1}-\sqrt5=\frac{x_n^2-2\sqrt5\,x_n+5}{2x_n}=\frac{(x_n-\sqrt5)^2}{2x_n}.$$
Por tanto, si $x_n>0$: (i) $x_{n+1}\ge\sqrt5$ (a partir de $x_1$ todas las aproximaciones son por exceso, como se ve en la tabla); (ii) el error nuevo es aproximadamente el **cuadrado** del anterior dividido por $2\sqrt5\approx4.47$. Con errores $10^{-2}\to10^{-5}\to10^{-10}\to10^{-20}$, el número de decimales correctos se duplica en cada paso. A esto se le llama **convergencia cuadrática**.

**Receta.** Para aproximar $\sqrt[m]{a}$, toma $f(x)=x^m-a$, localiza la raíz con Bolzano, parte de un entero cercano, simplifica $x_{n+1}=x_n-\frac{x_n^m-a}{m x_n^{m-1}}$ y rellena una tabla $n\,|\,x_n\,|\,f(x_n)\,|\,f'(x_n)$.

**Error típico.** Aplicar Newton a «$x=\sqrt5$», que no es una ecuación $f(x)=0$ útil. Otro error es redondear demasiado pronto: si se trabaja con 2 decimales, la tabla «se estabiliza» en 2.24, que es falso en el tercer decimal.

*Teoría: U §2.4.2, pp. 86-89 (algoritmo p. 88; Ejemplo 2.15, p. 87, que es el mismo esquema con $x^4-5$).*

---

## Ejercicio 2.35 (E p. 73)

> Utiliza el método de Newton para aproximar la solución de $x^2=0$, tomando como dato inicial el punto $x_0=0.4$ y realizando tres iteraciones.
> ¿Es posible utilizar directamente el método de bisección para aproximar la solución de la ecuación $x^2=0$?

### Solución

1. **Función y derivada.** $f(x)=x^2$, $f'(x)=2x$, derivable en $\mathbb R$. La solución exacta es $\tilde x=0$ (la conocemos: el ejercicio sirve para *ver cómo se comporta* el método).

2. **Iteración simplificada.** Si $x_n\neq0$ (condición para poder dividir entre $f'(x_n)=2x_n$):
$$x_{n+1}=x_n-\frac{x_n^2}{2x_n}=x_n-\frac{x_n}{2}=\frac{x_n}{2}.$$
Si $x_0=0.4\neq0$, todas las $x_n=0.4/2^n$ son no nulas, así que el método nunca se bloquea.

3. **Tres iteraciones.**

| $n$ | $x_n$ | $f(x_n)$ | $f'(x_n)$ | error $\lvert x_n-0\rvert$ |
|---|---|---|---|---|
| 0 | 0.4 | 0.16 | 0.8 | 0.4 |
| 1 | 0.2 | 0.04 | 0.4 | 0.2 |
| 2 | 0.1 | 0.01 | 0.2 | 0.1 |
| 3 | 0.05 | 0.0025 | 0.1 | 0.05 |

Resultado: $x_3=0.05$. En general $x_n=0.4/2^n\to0$.

4. **Observación importante (no está en E).** Aquí el error solo se **divide entre 2** en cada paso. No se eleva al cuadrado como en 2.34. El motivo es que $0$ es una raíz **doble**: $f(0)=0$ y también $f'(0)=0$. La tangente se vuelve casi horizontal al acercarse a la raíz y Newton pierde su rapidez. Con raíces dobles, Newton no es más rápido que la bisección.

5. **¿Bisección?** El método de bisección (U §1.4, pp. 53-56) necesita un intervalo $[a,b]$ con $f$ continua y $f(a)\,f(b)<0$, que es la hipótesis del Teorema de Bolzano (U p. 52). Pero $f(x)=x^2\ge0$ para todo $x$, así que **nunca** hay cambio de signo: no existe ese intervalo inicial. Respuesta: **no**, la bisección no se puede aplicar directamente. El Teorema de Bolzano da una condición *suficiente* para que haya raíz, no *necesaria*: aquí hay raíz, pero la gráfica «toca» el eje sin cruzarlo.

**Receta.** Antes de iterar, simplifica $x-\frac{f(x)}{f'(x)}$: a menudo sale una expresión sencilla. Para saber si puedes usar bisección, busca **dos puntos donde $f$ tenga signos opuestos**. Si $f$ no cambia de signo, no se puede.

**Error típico.** Pensar que «si Bolzano no se cumple, no hay raíz». Otro error es creer que Newton siempre converge cuadráticamente: si $f'(\tilde x)=0$, no es así.

*Teoría: U §2.4.2, p. 88 (algoritmo); U §1.4, pp. 52-55 (Bolzano y bisección).*

---

## Ejercicio 2.36 (E pp. 73-74)

> Utilizando el método de Newton, encuentra una solución aproximada de la ecuación $e^{-x}-x=0$ realizando tres iteraciones y partiendo de las condiciones iniciales $x_0=0.5$ y $x_0=5$. Estima el error relativo aproximado en cada caso.

### Solución

1. **Hay una única solución y sabemos dónde está.** Sea $f(x)=e^{-x}-x$, continua y derivable en $\mathbb R$ (suma de derivables, U §2.2). $f(0)=1>0$ y $f(1)=e^{-1}-1\approx-0.632<0$, así que por Bolzano (U p. 52) hay una raíz en $(0,1)$. Es única porque $e^{-x}$ y $-x$ son estrictamente decrecientes, luego $f$ también lo es y no puede anularse dos veces. (Es la misma ecuación del Ejemplo 1.49 de U, p. 55, resuelta allí por bisección.)

2. **Derivada, que nunca se anula.** $f'(x)=-e^{-x}-1<0$ para todo $x$, porque $e^{-x}>0$. Así la división de Newton siempre es posible, sea cual sea $x_n$.

3. **Iteración y simplificación.**
$$x_{n+1}=x_n-\frac{e^{-x_n}-x_n}{-e^{-x_n}-1}=x_n+\frac{e^{-x_n}-x_n}{e^{-x_n}+1}=\frac{x_n e^{-x_n}+x_n+e^{-x_n}-x_n}{e^{-x_n}+1}=\frac{x_n+1}{1+e^{x_n}}.$$
(En el último paso se multiplica numerador y denominador por $e^{x_n}$. Comprobado con sympy.) Esta forma se calcula mejor con la calculadora.

4. **Caso $x_0=0.5$.**

| $n$ | $x_n$ | $f(x_n)$ | $f'(x_n)$ | $\varepsilon_r$ | error real |
|---|---|---|---|---|---|
| 0 | 0.5 | $1.065\times10^{-1}$ | $-1.60653$ | — | $6.7\times10^{-2}$ |
| 1 | 0.566311003197 | $1.305\times10^{-3}$ | $-1.56762$ | $1.17\times10^{-1}$ | $8.3\times10^{-4}$ |
| 2 | 0.567143165035 | $1.96\times10^{-7}$ | $-1.56714$ | $1.47\times10^{-3}$ | $1.3\times10^{-7}$ |
| 3 | 0.567143290410 | $4.5\times10^{-15}$ | $-1.56714$ | $2.21\times10^{-7}$ | $2.8\times10^{-15}$ |

Solución exacta: $\tilde x=0.567143290409784\ldots$ (se comprueba con sympy como `LambertW(1)`).
Error relativo aproximado tras 3 iteraciones: $\varepsilon_r=\dfrac{|x_3-x_2|}{|x_3|}\approx2.2\times10^{-7}$. **Con 4 decimales** (como hace E): $x_1\approx0.5663$, $x_2\approx x_3\approx0.5671$, y sale $\varepsilon_r=0$. Ese «0» no significa error nulo. Significa que el error es menor que lo que 4 decimales pueden mostrar.

5. **Caso $x_0=5$.**

| $n$ | $x_n$ | $f(x_n)$ | $f'(x_n)$ | $\varepsilon_r$ | error real |
|---|---|---|---|---|---|
| 0 | 5 | $-4.99326$ | $-1.00674$ | — | 4.43 |
| 1 | 0.040157105546 | 0.92048 | $-1.96064$ | 123.5 | $5.3\times10^{-1}$ |
| 2 | 0.509637531161 | 0.09108 | $-1.60071$ | $9.21\times10^{-1}$ | $5.8\times10^{-2}$ |
| 3 | 0.566534509041 | $9.54\times10^{-4}$ | $-1.56749$ | $1.004\times10^{-1}$ | $6.1\times10^{-4}$ |

$\varepsilon_r=\dfrac{|x_3-x_2|}{|x_3|}=\dfrac{|0.566535-0.509638|}{0.566535}\approx0.1004$, igual que en E.

6. **Por qué el primer salto es tan grande.** En $x_0=5$ la función es casi la recta $y=-x$ ($e^{-5}\approx0.0067$), con pendiente casi $-1$. Su tangente corta el eje cerca de $0$, al otro lado de la raíz. A partir de ahí el método ya está cerca y converge deprisa. **Conclusión:** el resultado tras un número fijo de pasos, y su error, depende mucho de $x_0$. Por eso conviene localizar antes la raíz (con Bolzano o una gráfica).

7. **Cómo interpretar $\varepsilon_r$** (U p. 89). $\varepsilon_r$ no es el error verdadero: mide cuánto ha cambiado la última iteración. Como $x_n$ está cerca de $\tilde x$, se usa como *estimación*. En la tabla de $x_0=5$ se ve que $\varepsilon_r$ (0.1) sobreestima el error relativo real ($\approx10^{-3}$). En Newton suele ocurrir así, porque el error real ya es mucho menor que el último salto.

**Receta.** (1) Bolzano para localizar la raíz. (2) Comprobar $f'\neq0$. (3) Simplificar $x-f/f'$. (4) Tabla con $x_n$ y $\varepsilon_r=|x_n-x_{n-1}|/|x_n|$. (5) Parar cuando $\varepsilon_r$ sea menor que la tolerancia o se agoten las iteraciones pedidas.

**Error típico.** Olvidar el signo de $f'$: $x_n-\frac{e^{-x_n}-x_n}{-e^{-x_n}-1}$ lleva un signo **menos** en el denominador. Si se pierde ese signo (usando $e^{-x_n}+1$ como denominador), el paso va en sentido contrario: desde $x_0=0.5$ se obtendría $0.434$, que se aleja de la raíz. Otro error es poner en $\varepsilon_r$ el denominador $|x_{n-1}|$ (U usa $|x_n|$).

*Teoría: U §2.4.2, pp. 88-90 (algoritmo p. 88; error relativo y absoluto aproximados y criterios de parada pp. 89-90).*

---

## Ejercicio 2.38 (E pp. 75-76)

> Dada la ecuación $e^{-x}=x$:
> 1. Comprueba que el método de punto fijo converge para cualquier dato inicial $0.1\le x_0\le2$.
> 2. Utiliza el método de punto fijo para aproximar la solución de la ecuación partiendo del dato inicial $x_0=1$ y realizando cuatro iteraciones.

### Solución

**Apartado 1.**

1. **Escribir la ecuación en la forma $x=g(x)$.** Ya lo está: $x=e^{-x}$. Tomamos $g(x)=e^{-x}$. Sus puntos fijos, es decir, los $\tilde x$ con $g(\tilde x)=\tilde x$ (Definición 2.4, U p. 90), son exactamente las soluciones de la ecuación.

2. **Qué hay que comprobar** (Teorema 2.2, U p. 91). Hacen falta dos cosas en $[a,b]=[0.1,2]$:
 (H1) $g$ lleva $[a,b]$ dentro de sí mismo: $g([a,b])\subset[a,b]$;
 (H2) existe $k\in[0,1)$ con $|g'(x)|\le k$ para todo $x\in(a,b)$.

3. **(H1).** $g'(x)=-e^{-x}<0$, luego $g$ es estrictamente decreciente. Para $0.1\le x\le 2$, esto invierte las desigualdades:
$$g(2)\le g(x)\le g(0.1)\iff 0.1353\approx e^{-2}\le e^{-x}\le e^{-0.1}\approx0.9048 .$$
Como $0.1<0.1353$ y $0.9048<2$, se cumple $g(x)\in[0.1,2]$. **Por qué importa:** si alguna iteración saliera de $[a,b]$, ya no podríamos aplicar la cota de $g'$ en el paso siguiente.

4. **(H2).** $|g'(x)|=e^{-x}$ también es decreciente, así que su valor más grande en $(0.1,2)$ está cerca de $x=0.1$:
$$|g'(x)|=e^{-x}< e^{-0.1}\approx 0.9048<1\quad\text{para } x\in(0.1,2).$$
Tomamos $k=e^{-0.1}\approx0.905$. (**E escribe «$k=0.091$», que es una errata**: vale cualquier $k\in[e^{-0.1},\,1)$ (con $k=0.905$ sirve), pero $0.091$ no acota a $|g'|$.)

5. **Conclusión.** Por el Teorema 2.2 (U p. 91), $g$ tiene **un único** punto fijo en $[0.1,2]$, y la sucesión $x_{n+1}=e^{-x_n}$ converge a él para **cualquier** $x_0\in[0.1,2]$.

**Apartado 2.**

6. **Iteraciones** con $x_0=1$ (y cuatro más para ver la tendencia):

| $n$ | $x_n=e^{-x_{n-1}}$ | error real $\lvert x_n-\tilde x\rvert$ | $\varepsilon_r$ |
|---|---|---|---|
| 0 | 1 | 0.4329 | — |
| 1 | 0.367879441171 | 0.1993 | 1.718 |
| 2 | 0.692200627555 | 0.1251 | 0.4685 |
| 3 | 0.500473500564 | 0.0667 | 0.3831 |
| **4** | **0.606243535086** | **0.0391** | 0.1745 |
| 5 | 0.545395785975 | 0.0217 | 0.1116 |
| 6 | 0.579612335503 | 0.0125 | 0.0590 |
| 7 | 0.560115461361 | 0.0070 | 0.0348 |
| 8 | 0.571143115080 | 0.0040 | 0.0193 |

Respuesta: $x_4\approx0.6062$. Coincide con E aunque se redondee a 4 decimales en cada paso: 0.3679, 0.6922, 0.5005, 0.6062.

7. **Lectura de la tabla (propio).** Las iteraciones **oscilan** alrededor de $\tilde x=0.567143$: una por defecto y otra por exceso. Es lo que ocurre cuando $g'<0$. El error se multiplica aproximadamente por $|g'(\tilde x)|=\tilde x\approx0.567$ en cada paso: convergencia **lineal**. Newton, sobre la misma ecuación (Ej. 2.36), lograba 15 decimales exactos en 3 pasos.

8. **¿Qué garantiza la teoría con 4 pasos?** Con la cota del Teorema 2.3 (U p. 91): $\frac{k^4}{1-k}(b-a)=\frac{0.9048^4}{0.0952}\cdot1.9\approx13.4$. Esta cota es **inútil** (el intervalo solo mide 1.9). Para garantizar un error menor que $0.01$ harían falta $n>\ln\!\big(0.01(1-k)/1.9\big)/\ln k\approx75.99$, es decir, 76 iteraciones. En la práctica bastan 7 (tabla: $|x_6-	ilde x|=0.0125$ no basta, $|x_7-	ilde x|=0.0070$ sí). La cota es una *garantía*, no una estimación ajustada. Cuando $k$ está cerca de 1, es muy pesimista.

**Receta (comprobar la convergencia del punto fijo en $[a,b]$).** (1) Pasa la ecuación a la forma $x=g(x)$. (2) Estudia la monotonía de $g$ y calcula $g(a)$, $g(b)$ para ver que $g([a,b])\subset[a,b]$. (3) Acota $|g'|$ en $(a,b)$ por su valor mayor, $k$, y comprueba que $k<1$. (4) Cita el Teorema 2.2.

**Error típico.** Comprobar solo $|g'|<1$ y olvidar que $g$ debe llevar $[a,b]$ en sí mismo. También es un error dar como $k$ un número que no acota realmente a $|g'|$ (la errata de E).

*Teoría: U §2.4.3, pp. 90-93 (Definición 2.4 p. 90; algoritmo (2.3) p. 90; Teoremas 2.2 y 2.3 p. 91; Ejemplo 2.17 pp. 92-93, que es el modelo exacto de este ejercicio con $g(x)=\tfrac12\cos x$).*

---

## Ejercicio 2.37 (E pp. 74-75)

> Sea $f:[-1,1]\to[-1,1]$. Sabiendo que la única solución de la ecuación $f(x)=x$ en el intervalo $[-1,1]$ puede ser aproximada utilizando el método de punto fijo, ¿cuántas iteraciones necesitaremos para garantizar que el error cometido sea menor que $0.1$ si $|f'(x)|<0.8$ en $[-1,1]$? ¿Y si $|f'(x)|<0.2$ en $[-1,1]$?

### Solución

1. **Identificar los datos del Teorema 2.3** (U p. 91). Aquí la función de iteración se llama $f$ (en U es $g$). Tenemos $[a,b]=[-1,1]$, $f([-1,1])\subset[-1,1]$, y $|f'|<k$ con $k=0.8$ o $k=0.2$, ambos en $[0,1)$. Se cumplen las hipótesis del Teorema 2.2 y, por el Teorema 2.3,
$$|x_n-\tilde x|<\frac{k^n}{1-k}(b-a)=\frac{2k^n}{1-k}.$$

2. **Planteamiento** (U p. 92). Buscamos el **menor** $n\in\mathbb N$ con $\dfrac{2k^n}{1-k}<0.1$. Así, el error, que es menor que la cota, también es menor que $0.1$.

3. **Caso $k=0.8$.**
$$\frac{2\cdot0.8^n}{0.2}<0.1\iff 10\cdot0.8^n<0.1\iff0.8^n<0.01 .$$
Tomamos $\ln$, que es creciente y conserva la desigualdad: $n\ln0.8<\ln0.01$. Ahora dividimos entre $\ln0.8<0$, que **invierte** la desigualdad porque $0.8<1$:
$$n>\frac{\ln0.01}{\ln0.8}\approx20.6377 .$$
El primer natural que la cumple es $n=21$. Comprobación: $n=20$ da cota $0.1153$ (no basta) y $n=21$ da $0.0922<0.1$.

4. **Caso $k=0.2$.**
$$\frac{2\cdot0.2^n}{0.8}<0.1\iff0.2^n<0.04 .$$
$0.2^2=0.04$ **no** es $<0.04$, y $0.2^3=0.008<0.04$. Por tanto $n=3$. (Cotas: $n=2\to0.1$, $n=3\to0.02$.)

5. **Moraleja.** Con el mismo intervalo, pasar de $k=0.8$ a $k=0.2$ reduce la garantía de 21 a 3 iteraciones. Cuanto menor es $k$, más rápido converge el punto fijo.

6. **Matiz de rigor (omisión en E).** El Teorema 2.3 de U está enunciado con desigualdad **estricta**, $|x_n-\tilde x|<\frac{k^n}{1-k}(b-a)$. Con $k=0.2$ y $n=2$, la cota vale *exactamente* $0.1$ y el teorema ya daría error $<0.1$. Siguiendo al pie de la letra la receta de U p. 92 («el natural más pequeño para el que $\frac{k^n}{1-k}(b-a)<\varepsilon$»), la respuesta esperada es **3**, y es la que hay que dar en el examen. Para los curiosos: la demostración del teorema (ver apartado (a)) da de hecho la cota más fina $|x_n-\tilde x|\le k^n(b-a)$, con la que bastarían 14 iteraciones para $k=0.8$ y 2 para $k=0.2$. No es la fórmula del libro, así que no la uses en el examen salvo que la justifiques.

**Receta.** Número de iteraciones: resuelve $\frac{k^n}{1-k}(b-a)<\varepsilon$ ⇒ $n>\dfrac{\ln\!\big(\varepsilon(1-k)/(b-a)\big)}{\ln k}$ y toma el **primer natural estrictamente mayor**. Recuerda que $\ln k<0$ invierte la desigualdad.

**Error típico.** No invertir la desigualdad al dividir entre $\ln k$, lo que da $n<20.6$, una respuesta absurda. Redondear $20.64$ a $20$ en vez de a $21$. Olvidar el factor $(b-a)=2$ o el $1/(1-k)$.

*Teoría: U §2.4.3, Teorema 2.3 p. 91 y procedimiento p. 92 (Ejemplo 2.17 d, p. 93).*

---

## Ejemplos propios

### Bloque Newton

**P1 (propio, fácil). Aproxima $\sqrt[3]{10}$ con 3 iteraciones de Newton.**
1. $f(x)=x^3-10$, $f'(x)=3x^2$. Como $f(2)=-2<0<f(3)=17$, por Bolzano la raíz está en $(2,3)$. Tomamos $x_0=2$.
2. $x_{n+1}=x_n-\dfrac{x_n^3-10}{3x_n^2}=\dfrac{2x_n^3+10}{3x_n^2}$.
3. Tabla:

| $n$ | $x_n$ | error real |
|---|---|---|
| 0 | 2 | $1.5\times10^{-1}$ |
| 1 | $13/6=2.166666666667$ | $1.2\times10^{-2}$ |
| 2 | 2.154503616042 | $6.9\times10^{-5}$ |
| 3 | 2.154434692237 | $2.2\times10^{-9}$ |

$\sqrt[3]{10}=2.154434690031\ldots$, así que $x_3$ tiene 8 decimales exactos.

**P2 (propio, medio). Resuelve $x^3-x-1=0$ con Newton hasta que $\varepsilon_r<10^{-6}$.**
1. $f(1)=-1<0$, $f(2)=5>0$ ⇒ hay raíz en $(1,2)$ (Bolzano). $f'(x)=3x^2-1$, que no se anula en $[1,2]$ porque $3x^2-1\ge2$ allí.
2. $x_{n+1}=x_n-\dfrac{x_n^3-x_n-1}{3x_n^2-1}$, con $x_0=1.5$.

| $n$ | $x_n$ | $\varepsilon_r$ |
|---|---|---|
| 0 | 1.5 | — |
| 1 | 1.347826086957 | $1.13\times10^{-1}$ |
| 2 | 1.325200398951 | $1.71\times10^{-2}$ |
| 3 | 1.324718173999 | $3.64\times10^{-4}$ |
| 4 | 1.324717957245 | $1.64\times10^{-7}$ |

Paramos en $n=4$ porque $\varepsilon_r<10^{-6}$: $\tilde x\approx1.3247180$ (valor exacto $1.32471795724\ldots$).

**P3 (propio, difícil). Newton puede no converger: $f(x)=x^3-2x+2$ con $x_0=0$** (es L §3.8 ej. 22, p. 229).
1. $f'(x)=3x^2-2$. Desde $x_0=0$: $x_1=0-\frac{2}{-2}=1$. Desde $x_1=1$: $x_2=1-\frac{1}{1}=0$. La sucesión es $0,1,0,1,\dots$, un **ciclo**: no converge a nada (y además $f(0)=2$, $f(1)=1$ no son raíces).
2. ¿Dónde está la raíz? $f(-2)=-2<0$ y $f(-1)=3>0$ ⇒ raíz en $(-2,-1)$.
3. Desde $x_0=-2$: $-1.8,\ -1.769948186529,\ -1.769292662906,\ -1.769292354239$, con errores $3\times10^{-2},\,6.6\times10^{-4},\,3.1\times10^{-7},\,6.8\times10^{-14}$. **Moraleja:** localizar la raíz con Bolzano *antes* de elegir $x_0$. Es la situación del margen de U p. 89 («¿Es infalible el método de Newton?»).

### Bloque punto fijo

**P4 (propio, fácil).** $g:[0,1]\to[0,1]$ con $|g'(x)|\le0.5$ en $(0,1)$. ¿Cuántas iteraciones garantizan error $<10^{-3}$?
$\dfrac{0.5^n}{0.5}\cdot1<10^{-3}\iff0.5^n<5\cdot10^{-4}\iff n>\dfrac{\ln(5\cdot10^{-4})}{\ln0.5}\approx10.97$, luego $n=11$. (Cotas: $n=10\to1.95\times10^{-3}$, $n=11\to9.8\times10^{-4}$.)

**P5 (propio, medio). $x=\cos x$ en $[0,1]$.**
1. $g(x)=\cos x$ es decreciente en $[0,1]\subset[0,\pi/2]$, luego $g([0,1])=[\cos1,\cos0]=[0.5403,\,1]\subset[0,1]$ (H1).
2. $|g'(x)|=\operatorname{sen}x\le\operatorname{sen}1\approx0.8415<1$ en $(0,1)$, porque el seno es creciente en $[0,\pi/2]$. Tomamos $k=\operatorname{sen}1$ (H2). Por el Teorema 2.2 hay un único punto fijo y la iteración converge desde cualquier $x_0\in[0,1]$.
3. Con $x_0=1$: $x_1=0.540302305868$, $x_2=0.857553215846$, $x_3=0.654289790498$, $x_4=0.793480358743$. El valor exacto es $\tilde x=0.739085133\ldots$ y el error de $x_4$ es $0.054$ (oscila, porque $g'<0$).
4. Iteraciones que garantizan error $<0.01$: $\dfrac{k^n}{1-k}<0.01\iff n>\dfrac{\ln(0.01(1-k))}{\ln k}\approx37.35$, luego $n=38$. Comprobación: la cota con $n=37$ es $0.0106$ y con $n=38$ es $0.0089$. Compáralo con el Ejemplo 3 de S p. 341: Newton resuelve la misma ecuación con 6 decimales en unos 4 pasos.

**P6 (propio, difícil). Elegir bien $g$: $x^3-x-1=0$ en $[1,2]$** (en la línea del Ejemplo 2.18 de U, p. 94).
1. *Opción mala:* $x=x^3-1$, es decir $g_1(x)=x^3-1$. Entonces $g_1'(x)=3x^2\ge3$ en $[1,2]$: (H2) falla, y $g_1([1,2])=[0,7]\not\subset[1,2]$: (H1) también falla. Desde $x_0=1.5$: $2.375,\ 12.40,\ 1904,\ 6.9\times10^{9}$. **Diverge.**
2. *Opción buena:* $x^3=x+1\iff x=\sqrt[3]{x+1}$, $g_2(x)=\sqrt[3]{x+1}$. $g_2$ es creciente: $g_2([1,2])=[\sqrt[3]2,\sqrt[3]3]=[1.2599,\,1.4422]\subset[1,2]$ (H1). $g_2'(x)=\dfrac{1}{3(x+1)^{2/3}}$ es positiva y decreciente, luego $|g_2'(x)|\le g_2'(1)=\dfrac1{3\sqrt[3]4}\approx0.2100=k$ (H2).
3. Desde $x_0=1$: $1.259921049895,\ 1.312293836683,\ 1.322353819139,\ 1.324268744552,\ 1.324632625251$ (errores $6.5\times10^{-2}\to8.5\times10^{-5}$).
4. Error $<10^{-6}$ garantizado si $\frac{k^n}{1-k}<10^{-6}\iff n>9.003$, es decir, $n=10$ (la cota con $n=9$ es $1.005\times10^{-6}$, que por muy poco no basta).
**Moraleja:** la misma ecuación admite muchas $g$ (U p. 93-94). Hay que elegir una con $|g'|<1$ cerca de la raíz.

---

## (a) Teoría necesaria (U, páginas impresas verificadas)

| Contenido | Dónde |
|---|---|
| Motivación: resolver $f(x)=0$ de forma aproximada | U §2.4.1, p. 86 |
| Idea geométrica de Newton (tangente que corta al eje $x$), Figura 2.2 | U §2.4.2, pp. 86-87 |
| Deducción: tangente $y-f(x_0)=f'(x_0)(x-x_0)$, hacer $y=0$ ⇒ $x_1=x_0-\frac{f(x_0)}{f'(x_0)}$; si $f'(x_0)=0$, cambiar $x_0$ | U Ej. 2.15, pp. 87-88 |
| **Algoritmo de Newton** $x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}$ (para $f$ derivable) | U p. 88 |
| Si la sucesión de Newton converge, lo hace a una raíz (tomar límites) | U Ej. 2.16, p. 89 |
| Newton no es infalible: $f'(x_n)=0$ o ciclos (figura al margen) | U p. 89 (margen) |
| **Error relativo aproximado** $\varepsilon_r=\frac{\lvert x_n-x_{n-1}\rvert}{\lvert x_n\rvert}$, error absoluto aproximado $\varepsilon_a=\lvert x_n-x_{n-1}\rvert$; criterio de parada | U p. 89 |
| Error relativo exacto y parada por número máximo de iteraciones | U p. 90 |
| **Punto fijo** (Def. 2.4): $g(\tilde x)=\tilde x$; en la gráfica, corte con $y=x$ | U §2.4.3, p. 90 |
| **Método de punto fijo** $x_{n+1}=g(x_n)$, ec. (2.3) | U p. 90 |
| Si los iterantes convergen, el límite es punto fijo (usa la continuidad de $g$) | U p. 91 |
| **Teorema 2.2** (existencia, unicidad y convergencia): $g:[a,b]\to[a,b]$, $\lvert g'\rvert\le k<1$ en $(a,b)$ | U p. 91 |
| **Teorema 2.3** (cota del error): $\lvert x_n-\tilde x\rvert<\frac{k^n}{1-k}(b-a)$ | U p. 91 |
| Número de iteraciones: menor $n$ con $\frac{k^n}{1-k}(b-a)<\varepsilon$ | U p. 92 |
| Ejemplo modelo completo ($\tfrac12\cos x=x$): hipótesis, 4 iteraciones, cota, nº de iteraciones (9) | U Ej. 2.17, pp. 92-93 |
| Pasar de $f(x)=0$ a $x=g(x)$ (p. ej. $g=f+x$); la $g$ no es única | U pp. 93-94, Ej. 2.18 p. 94 |
| Autoevaluación: ítems 7 (punto fijo) y 8 (Newton para $x=f(x)$) | U p. 100; soluciones p. 285 |
| Herramientas previas: Bolzano (p. 52), bisección y su cota $\frac{b-a}{2^n}$ (pp. 53-55, Ej. 1.49 con $e^{-x}=x$ p. 55); derivable ⇒ continua (Teorema 2.1, p. 76) | U §1.4, §2.1 |

**Contracciones (explicación propia; U no usa esa palabra).** Si $|g'|\le k<1$ en $(a,b)$, el **Teorema del valor medio** (U §2.5.3, p. 96, que viene *después* de §2.4) da, para $x,y\in[a,b]$,
$$|g(x)-g(y)|=|g'(c)|\,|x-y|\le k|x-y| .$$
Es decir, $g$ **acerca** los puntos: es una *contracción*. De aquí salen los teoremas, que U enuncia sin demostrar:
- *Existencia:* $h(x)=g(x)-x$ cumple $h(a)=g(a)-a\ge0$ y $h(b)=g(b)-b\le0$, porque $g(x)\in[a,b]$. Por Bolzano (o porque el extremo ya es un cero) hay un $\tilde x$ con $g(\tilde x)=\tilde x$.
- *Unicidad:* si hubiera dos, $|\tilde x-\tilde y|=|g(\tilde x)-g(\tilde y)|\le k|\tilde x-\tilde y|$ con $k<1$, lo que obliga a $\tilde x=\tilde y$.
- *Convergencia y cota:* $|x_n-\tilde x|=|g(x_{n-1})-g(\tilde x)|\le k|x_{n-1}-\tilde x|\le\dots\le k^n|x_0-\tilde x|\le k^n(b-a)$, que tiende a 0. Como $k^n(b-a)<\frac{k^n}{1-k}(b-a)$ (si $0<k<1$), se obtiene el Teorema 2.3.

**Newton frente a punto fijo frente a bisección (resumen para el examen).**
- *Bisección:* necesita cambio de signo, siempre converge y es lenta (el error se divide entre 2 en cada paso).
- *Punto fijo:* necesita (H1) y (H2), da garantía a priori (Teorema 2.3) y converge linealmente (el error se multiplica por $\approx|g'(\tilde x)|$ en cada paso).
- *Newton:* necesita $f'$ y un buen $x_0$. No tiene garantía en U, pero es muy rápido (cuadrático) si la raíz es simple (2.34, 2.36) y lento si es doble (2.35).
- Newton es un punto fijo de $g(x)=x-f(x)/f'(x)$.

## (b) Huecos de U y dónde suplirlos (S / L)

| Hueco en U | Dónde suplirlo |
|---|---|
| U no enuncia ninguna condición de convergencia para Newton | L §3.8, p. 228: condición suficiente $\left\lvert\frac{f(x)f''(x)}{[f'(x)]^2}\right\rvert<1$ en un intervalo abierto que contenga el cero (con ejemplos de $x^2-2$ y $x^{1/3}$) |
| Presentación paso a paso del algoritmo y del criterio de parada «hasta que dos aproximaciones difieran menos de...» | L §3.8, p. 225 (cuadro «Método de Newton», pasos 1-3); S §4.8, p. 339 (ecuación 2) y p. 340 (cuándo parar) |
| Más ejemplos resueltos con tabla | L p. 226 (ej. 1: $\sqrt2$; ej. 2: cúbica), S pp. 340-341 (ej. 1: $x^3-2x-5$; ej. 2: $\sqrt[6]2$; ej. 3: $\cos x=x$) |
| Fallos de Newton (U solo da una figura al margen) | L p. 227 ($f'(x_n)=0$; ej. 3: $x^{1/3}$ diverge); S p. 340 (fig. 4) y ejercicios 31-34, p. 343; L ejercicios 21-22 (el 22 es el ciclo de P3), p. 229 |
| Regla de Herón (conecta con 2.34) | L ej. 19, p. 229 |
| Demostración de los Teoremas 2.2 y 2.3 (U no la da) | Ni S ni L tratan el método de punto fijo. Hay piezas sueltas: S Problemas adicionales del cap. 2, prob. 8, p. 171 (existencia de punto fijo de $f:[0,1]\to[0,1]$ continua con el teorema del valor intermedio) y S §4.2 ej. 36, p. 289 (unicidad si $f'(x)\neq1$, con el valor medio). El resto está en el recuadro «Contracciones» de arriba (propio) |
| Práctica de punto fijo | L ejercicios 23-24, p. 229 (punto fijo de $\cos x$ y $\cot x$) |
| Convergencia cuadrática / lineal (U no la menciona) | No aparece en S ni L con ese nombre; ver el paso 6 del Ej. 2.34 y el paso 4 del Ej. 2.35 (propio) |

## (c) Erratas y omisiones de E

1. **Ej. 2.38, p. 76:** «Podemos tomar entonces $k=0.091$». **Errata:** debe ser $k=e^{-0.1}\approx0.905$ (o cualquier $k\in[e^{-0.1},1)$). $0.091$ es menor que $\sup|g'|$ y no sirve como cota. La conclusión (convergencia) sigue siendo correcta.
2. **Ej. 2.36, p. 74:** para $x_0=5$ da $x_1\approx0.0401$. El valor es $0.0401571\ldots$, que redondeado a 4 decimales es **$0.0402$** (E trunca). No afecta a $x_2\approx0.5096$, $x_3\approx0.5665$ ni a $\varepsilon_r\approx0.1004$, que son correctos.
3. **Ej. 2.36, p. 74:** «$\varepsilon_r=0$» con $x_0=0.5$ se debe solo al redondeo a 4 decimales (E lo advierte al margen). El valor real es $\varepsilon_r\approx2.2\times10^{-7}$. En el margen, la fórmula de $\varepsilon_r$ aparece en el texto extraído con denominador $x_n$ sin valor absoluto. U (p. 89) y el propio cálculo de E usan $|x_n|$. Conviene confirmarlo en el PDF.
4. **Ej. 2.37, p. 75 (matiz):** como el Teorema 2.3 de U tiene desigualdad estricta, para $k=0.2$ y $n=2$ la cota vale exactamente $0.1$ y ya garantizaría error $<0.1$. E da 3, que es lo que resulta de aplicar la receta de U p. 92 (primer $n$ con cota $<\varepsilon$). Se mantiene 3 como respuesta de examen.
5. **Ej. 2.35, p. 73 (omisión):** E no comenta que Newton converge aquí solo linealmente ($x_n=0.4/2^n$) porque $0$ es una raíz doble ($f'(0)=0$). Es una buena ocasión para mostrar que Newton no siempre es rápido.
6. **Ej. 2.34, p. 72 (omisión menor):** E no justifica la elección de $x_0=2$ (se hace con Bolzano: $f(2)<0<f(3)$). La «estabilización» a partir de $x_2$ es solo a 4 decimales: el error real de $x_2$ es $4.3\times10^{-5}$.
7. **Ej. 2.38 (omisión):** E no dice cuánto vale el error de $x_4$. La cota del Teorema 2.3 ($\approx13.4$) no sirve aquí. El error real es $0.039$.
