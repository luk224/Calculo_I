# Así lo preguntan en el examen — Tema 1.4 Límites y continuidad de funciones

Fuente **X** = `Examenes-resueltos-Calculo.pdf` (página = página del PDF). Enunciados y soluciones leídos **como imagen** (PyMuPDF, 110 dpi). Todo lo calculable se ha verificado con sympy (ver «Verificación» en cada problema).
Solo se usan herramientas del tema 1.4 o anteriores (sin L'Hôpital ni derivadas). Las recetas remiten a las del resumen `temas/tema_1_4_limites_continuidad.html`.

Orden: de fácil a difícil.

| # | Tipo | Fuente |
|---|---|---|
| 1 | Continuidad en un punto con límites laterales | X p.64 (Feb 2016, Mecánica, Mod. B, P1) |
| 2 | Hipótesis de Bolzano y Weierstrass (verdadero/falso) | X p.126, X p.22, X p.40 |
| 3 | Valores intermedios: existencia de $x_0$ con $f(x_0)=d$ | X p.49 (Feb 2015, Mecánica, Mod. A, P2) |
| 4 | Límite «acotada × tiende a 0» | X p.81 (Feb 2017, Mecánica, Mod. B, P1) |
| 5 | Indeterminación $1^\infty$ | X p.132 (Sept 2017, Electrónica, P1) |
| 6 | Continuidad y asíntotas de una racional (ejercicio largo) | X pp.44-45 (Feb 2014, Mecánica, Mod. B, Ej. 5) |
| 7 | Método de bisección (nº de pasos y tabla) | X pp.17-18 (Sept 2011, Mecánica, Ej. 5) + variante X p.73 |

---

## Problema 1 · Continuidad en el punto donde cambia la fórmula

**Fuente:** `X p.64 (Febrero 2016, Grado en Ing. Mecánica, Modelo B, pregunta corta 1, 1 punto)`

**Enunciado.** Estudie la continuidad en $x=0$ de
$$f(x)=\begin{cases}\dfrac{2-x}{x-1}, & x\le 0,\[2mm] e^x, & x>0.\end{cases}$$

**Solución.**
1. **Qué hay que comprobar.** $f$ es continua en $0$ si $\lim_{x\to0}f(x)$ existe y vale $f(0)$ (U Def. 1.20, p.51). Como a cada lado de $0$ la fórmula es distinta, el límite se estudia con los dos límites laterales (U Teorema 1.4, p.47): existe si y solo si los dos laterales coinciden.
2. **Valor en el punto.** El $0$ cae en la rama $x\le0$: $f(0)=\dfrac{2-0}{0-1}=-2$.
3. **Límite por la izquierda.** Para $x<0$, $f(x)=\frac{2-x}{x-1}$, un cociente de polinomios cuyo denominador no se anula en $0$; por tanto es continuo en $0$ y basta sustituir: $\lim_{x\to0^-}f(x)=\frac{2}{-1}=-2$.
4. **Límite por la derecha.** Para $x>0$, $f(x)=e^x$, continua: $\lim_{x\to0^+}f(x)=e^0=1$.
5. **Conclusión.** $-2\neq1$: los laterales son distintos, luego **no existe** $\lim_{x\to0}f(x)$ y $f$ **no es continua en $0$**. Es una discontinuidad **de salto** (finito, de altura $3$). Como el lateral izquierdo coincide con $f(0)$, $f$ es **continua por la izquierda** en $0$, pero no por la derecha.

**Receta.** Función a trozos en el punto de corte: calcula $f(a)$ con la rama que incluye el «$=$», cada límite lateral con su rama, y compara los tres números.

**Parte del tema.** §4 Límites laterales (U pp.46-47), §8 Continuidad y tipos de discontinuidad (U p.51).

**Verificación.** sympy: `limit((2-x)/(x-1),x,0,'-') = -2`, `limit(exp(x),x,0,'+') = 1`, $f(0)=-2$.

**Avisos.** Ninguna errata. El impreso solo dice «continua por la izquierda, pero no por la derecha»; conviene nombrar además el tipo (salto).

---

## Problema 2 · Las hipótesis de los teoremas de continuidad (tres preguntas de verdadero/falso)

### 2a. ¿Basta la monotonía para Bolzano?
**Fuente:** `X p.126 (sin fecha, I. Electrónica Industrial y Automática, pregunta corta 2, 1 punto)`

**Enunciado.** Razone la veracidad o falsedad de la siguiente afirmación: «Si $f:\mathbb R\to\mathbb R$ es estrictamente creciente y $f(-1)<0<f(1)$, entonces existe al menos una solución de la ecuación $f(x)=0$».

**Solución.**
1. **Qué teorema parece aplicarse.** El de Bolzano (U p.52): si $f$ es **continua** en $[a,b]$ y $f(a)f(b)<0$, existe $c\in(a,b)$ con $f(c)=0$. El enunciado da el cambio de signo, pero **no** la continuidad. Hay que ver si sin ella puede fallar.
2. **Contraejemplo (el del impreso).** $f(x)=x$ si $x<0$; $f(x)=x+1$ si $x\ge0$.
   - Estrictamente creciente: lo es en cada rama; y si $x<0\le y$, entonces $f(x)=x<0<1\le y+1=f(y)$.
   - $f(-1)=-1<0$ y $f(1)=2>0$.
   - $f(x)=0$ no tiene solución: si $x<0$, $f(x)=x<0$; si $x\ge0$, $f(x)=x+1\ge1$.
3. **Conclusión.** La afirmación es **falsa**. La función «salta» por encima del $0$ (discontinuidad de salto en $x=0$), justo lo que la continuidad impide.

### 2b. ¿Bolzano da unicidad?
**Fuente:** `X p.22 (Febrero 2012, 2ª semana, Ing. Mecánica, Modelo B, pregunta corta 1, 1 punto)`

**Enunciado.** Sea $f(x):[-1,1]\to\mathbb R$ una función continua tal que $f(-1)=-3$ y $f(1)=3$. Razone si es cierto que la ecuación $f(x)=0$ tiene una única solución en el intervalo $[-1,1]$. Apóyese en la gráfica de una función con estas características si lo considera necesario.

**Solución.**
1. **Existencia.** $f$ es continua en $[-1,1]$ y $f(-1)f(1)=-9<0$: por Bolzano (U p.52) hay **al menos** una solución en $(-1,1)$.
2. **Unicidad: no.** Bolzano no dice nada de cuántas. Contraejemplo del impreso: $f(x)=3\operatorname{sen}\frac{5\pi x}{2}$; $f(-1)=3\operatorname{sen}(-\tfrac{5\pi}2)=-3$, $f(1)=3$, y se anula donde $\frac{5\pi x}2=k\pi$, es decir en $x=\frac{2k}5$: $x=0,\ \pm\frac25,\ \pm\frac45$ (**cinco** soluciones). Un contraejemplo más sencillo (propio, polinómico): $f(x)=3x(4x^2-3)$, con $f(-1)=-3$, $f(1)=3$ y ceros $0,\ \pm\frac{\sqrt3}{2}$.
3. **Conclusión.** **Falso**: hay al menos una, pero no tiene por qué ser única. (Para garantizar unicidad haría falta algo más, p. ej. que $f$ sea estrictamente monótona.)

### 2c. ¿Se alcanzan el máximo y el mínimo?
**Fuente:** `X p.40 (Febrero 2014, Grado en Ing. Mecánica, Modelo A, pregunta corta 2, 1 punto)`

**Enunciado.** Razone si es verdadero o falso que la función $f(x)=x^3\cos(x+1)$ alcanza el máximo y el mínimo absoluto en el intervalo $[-\pi,\pi]$.

**Solución.**
1. **Teorema aplicable.** Weierstrass (U p.53): una función **continua** en un intervalo **cerrado y acotado** $[a,b]$ alcanza en él su máximo y su mínimo absolutos.
2. **Hipótesis.** $x^3$ (polinomio) y $\cos(x+1)$ (composición de continuas) son continuas en $\mathbb R$; su producto también (U p.51). $[-\pi,\pi]$ es cerrado y acotado.
3. **Conclusión.** **Verdadero**, por Weierstrass. No hace falta calcular dónde se alcanzan.

**Receta (2a-2c).** Ante un «¿es cierto que…?» sobre Bolzano/Weierstrass: lista las hipótesis del teorema (continuidad; cambio de signo / intervalo cerrado y acotado) y su conclusión exacta («al menos uno», «se alcanza»); si falta una hipótesis o se pide más que la conclusión, busca un contraejemplo sencillo.

**Parte del tema.** §9 Bolzano, valores intermedios y Weierstrass (U pp.52-53); §8 tipos de discontinuidad.

**Verificación.** 2a: valores y ausencia de ceros comprobados con sympy (`Piecewise`). 2b: $3\operatorname{sen}(5\pi x/2)$ en $\pm1$ vale $\pm3$ y se anula en $0,\pm2/5$ (y $\pm4/5$); $3x(4x^2-3)$: $f(\pm1)=\pm3$, raíces $0,\pm\sqrt3/2$.

**Avisos.**
- 2b: el impreso cita «página 51 del libro "Cálculo para Ingenieros"»: en la edición actual de U (2023) Bolzano está en la **p.52**.
- 2c: el impreso justifica con «la proposición 3.4» (extremos absolutos en extremos relativos o en los bordes), que es del Tema 3 y además **presupone** que el máximo existe. La justificación correcta y suficiente es **Weierstrass** (U p.53), que es lo que debe escribirse en este tema.

---

## Problema 3 · Probar que una ecuación tiene solución sin hallarla (valores intermedios)

**Fuente:** `X p.49 (Febrero 2015, Grado en Ing. Mecánica, Modelo A, pregunta corta 2, 1 punto)`

**Enunciado.** Sea $f:\mathbb R\to\mathbb R$ la función definida por $f(x)=\ln\big((ex)^2+1\big)$. Demuéstrese, sin encontrarlo, que existe un punto $x_0\in(0,1)$ tal que $f(x_0)=1$.
*Nota:* utilícese el teorema de los valores intermedios.

**Solución.**
1. **Continuidad en $[0,1]$.** $(ex)^2+1=e^2x^2+1\ge1>0$ para todo $x$, así que el logaritmo está definido en todo $\mathbb R$. $f$ es composición de un polinomio (continuo) con $\ln$ (continua en $(0,+\infty)$), luego es continua en $\mathbb R$ y en particular en $[0,1]$ (U p.51, continuidad de la composición).
2. **Valores en los extremos.** $f(0)=\ln1=0$. $f(1)=\ln(e^2+1)$; como $e^2+1>e^2$ y $\ln$ es creciente, $f(1)>\ln e^2=2$. (No hace falta calculadora: $f(1)\approx2{,}127$.)
3. **Aplicar valores intermedios** (U p.52): $f$ continua en $[0,1]$ toma todos los valores entre $f(0)=0$ y $f(1)>2$. Como $0<1<f(1)$, existe $x_0\in(0,1)$ con $f(x_0)=1$. (Es interior porque $f(0)\neq1$ y $f(1)\neq1$.)
4. Equivalente con Bolzano: $h(x)=f(x)-1$ es continua, $h(0)=-1<0$, $h(1)>1>0$.

**Receta.** Para «existe $x_0$ con $f(x_0)=d$»: continuidad en $[a,b]$ + comprobar que $d$ queda **entre** $f(a)$ y $f(b)$ (o Bolzano a $f-d$).

**Parte del tema.** §9 Teorema de los valores intermedios (U p.52).

**Verificación.** sympy: $f(0)=0$, $f(1)=2{,}12693$; `nsolve` da $x_0\approx0{,}48223$; exacto: $e^2x^2+1=e\Rightarrow x_0=\frac{\sqrt{e-1}}{e}\approx0{,}4822\in(0,1)$.

**Avisos (errata del impreso).** La solución escribe «$1=f(0)<f(x_0)<f(1)\approx2{,}1269$», que es falso ($f(0)=0$, no $1$). Lo correcto es $f(0)=0<1=f(x_0)<f(1)$. La conclusión sí es correcta.

---

## Problema 4 · Límite de «acotada partido por algo que tiende a infinito»

**Fuente:** `X p.81 (Febrero 2017, Grado en Ing. Mecánica, Modelo B, pregunta corta 1, 1 punto)`

**Enunciado.** Calcule el valor del límite siguiente ($\ln$ es el logaritmo neperiano):
$$\lim_{x\to0^+}\frac{5+\cos\big(e^{-x^2}\big)}{\ln x}.$$

**Solución.**
1. **Separar.** Escribe el cociente como producto $g(x)\cdot\frac{1}{\ln x}$ con $g(x)=5+\cos(e^{-x^2})$.
2. **$g$ está acotada.** Como $-1\le\cos t\le1$ para todo $t$, se tiene $4\le g(x)\le6$ para todo $x$.
3. **El otro factor tiende a 0.** $\lim_{x\to0^+}\ln x=-\infty$, luego $\lim_{x\to0^+}\frac1{\ln x}=0$ («$\frac1{\infty}=0$», U p.46).
4. **Acotada × tiende a 0.** Por U Prop. 1.10 (p.45), el producto tiende a $0$: el límite **vale $0$** (se acerca por valores negativos, pues $g>0$ y $\ln x<0$).
5. **Por qué no sirve L'Hôpital (ni hace falta).** El numerador no tiende a $0$ ni a $\infty$ (tiende a $5+\cos1$), así que no hay indeterminación $\frac00$ ni $\frac\infty\infty$; es simplemente $\frac{\text{número}}{-\infty}=0$.
6. (Con emparedado, si se prefiere.) Para $0<x<1$ es $\ln x<0$; al dividir $4\le g\le6$ entre $\ln x$ **se invierten las desigualdades**: $\frac6{\ln x}\le\frac{g(x)}{\ln x}\le\frac4{\ln x}$, y ambos extremos tienden a $0$.

**Receta.** (función acotada) × (función que tiende a 0) → 0; un cociente «acotado / $\pm\infty$» es de ese tipo.

**Parte del tema.** §3 Herramientas: Prop. 1.10 y regla del emparedado (U p.45); §5 límites infinitos.

**Verificación.** sympy: `limit((5+cos(exp(-x**2)))/log(x), x, 0, '+') = 0`; valores en $x=10^{-3}$ y $10^{-10}$: $-0{,}80$ y $-0{,}24$ (negativos y acercándose a 0).

**Avisos (errata del impreso).** El impreso escribe $0=4\lim\frac1{\ln x}\le\lim\frac{5+\cos(\cdot)}{\ln x}\le6\lim\frac1{\ln x}=0$: las desigualdades entre funciones están **al revés**, porque $\ln x<0$ (p. ej. en $x=1/e$ diría $-4\le-g\le-6$, imposible). Además mete límites en la cadena antes de saber que existen. El resultado ($0$) sí es correcto. Usar el paso 4 (Prop. 1.10) evita el problema.

---

## Problema 5 · Indeterminación $1^\infty$

**Fuente:** `X p.132 (Septiembre 2017, I. Electrónica Industrial y Automática, pregunta corta 1, 1 punto)`

**Enunciado.** Calcule el límite $\displaystyle\lim_{x\to\infty}\Big(\frac{x-1}{x+2}\Big)^x$.

**Solución.**
1. **Identificar la forma.** Base $A(x)=\frac{x-1}{x+2}\to1$ (dividir entre $x$: $\frac{1-1/x}{1+2/x}\to1$) y exponente $B(x)=x\to+\infty$: indeterminación $1^\infty$. No se puede decir «$1^\infty=1$».
2. **Escribir la base como $1+\frac1F$.** $A-1=\frac{x-1-(x+2)}{x+2}=\frac{-3}{x+2}$, así que $A=1+\dfrac1{F}$ con $F=\dfrac{x+2}{-3}\to-\infty$. (Para $x>1$, $A>0$ y la potencia está bien definida.)
3. **Ajustar el exponente.** $x=F\cdot\dfrac{x}{F}=F\cdot\dfrac{-3x}{x+2}$, luego
$$A^B=\Big[\Big(1+\frac1F\Big)^F\Big]^{\frac{-3x}{x+2}}.$$
4. **Pasar al límite.** El corchete tiende a $e$ (número $e$ para funciones, $F\to-\infty$; extensión de U Prop. 1.5, p.31) y el exponente $\frac{-3x}{x+2}\to-3$. Por la continuidad de la exponencial: $\lim=e^{-3}$.
5. Atajo de la receta del tema: $\lim A^B=e^{\lim B(A-1)}=e^{\lim x\cdot\frac{-3}{x+2}}=e^{-3}$.

**Receta.** $1^\infty$: $\lim A^B=e^{\lim B\,(A-1)}$; calcula $A-1$ simplificado y multiplícalo por el exponente.

**Parte del tema.** §3 «Indeterminaciones y la forma $1^\infty$» (U pp.29-31 y Prop. 1.5).

**Verificación.** sympy: `limit(((x-1)/(x+2))**x, x, oo) = exp(-3)`; `limit(x*((x-1)/(x+2)-1), x, oo) = -3`.

**Avisos.** Ninguna errata (el impreso hace exactamente los pasos 2-4).

---

## Problema 6 · Continuidad y asíntotas de una función racional

**Fuente:** `X pp.44-45 (Febrero 2014, Grado en Ing. Mecánica, Modelo B, ejercicio 5, 3 puntos: 0,75 por apartado)`

**Enunciado.** Sea $f$ la función dada por $f(x)=\dfrac{x^3+x^2+1}{x^2+4}$.
a) Determínese dónde es continua.
b) Determínese si tiene asíntotas verticales y su ecuación, si las tuviera.
c) Determínese si tiene asíntotas horizontales y su ecuación, si las tuviera.
d) Determínese si tiene asíntotas oblicuas y su ecuación, si las tuviera.

**Solución.**
1. **(a) Continuidad.** Es cociente de polinomios (continuos en $\mathbb R$), y un cociente de continuas es continuo donde el denominador no se anula (U p.51). Como $x^2+4\ge4>0$, el denominador **nunca** se anula: $f$ es continua en todo $\mathbb R$.
2. **(b) Verticales.** $x=a$ es asíntota vertical si algún lateral $\lim_{x\to a^\pm}f(x)$ es $\pm\infty$ (U p.49). Pero por (a), para todo $a\in\mathbb R$, $\lim_{x\to a}f(x)=f(a)$, un número finito. **No hay asíntotas verticales.**
3. **(c) Horizontales.** Dividiendo numerador y denominador entre $x^2$: $f(x)=\dfrac{x+1+\frac1{x^2}}{1+\frac4{x^2}}$. El denominador $\to1$ y el numerador $\to\pm\infty$, así que $\lim_{x\to+\infty}f=+\infty$ y $\lim_{x\to-\infty}f=-\infty$. Ningún límite en el infinito es finito: **no hay asíntotas horizontales**. (Regla rápida: grado del numerador $3>2$.)
4. **(d) Oblicuas, pendiente.** $m=\lim_{x\to\pm\infty}\dfrac{f(x)}{x}=\lim\dfrac{x^3+x^2+1}{x^3+4x}=1$ (mismo grado: cociente de coeficientes principales), en los dos lados.
5. **(d) Ordenada.** $b=\lim_{x\to\pm\infty}\big(f(x)-x\big)=\lim\dfrac{x^3+x^2+1-x^3-4x}{x^2+4}=\lim\dfrac{x^2-4x+1}{x^2+4}=1$, en los dos lados.
6. **Conclusión (d).** $y=x+1$ es asíntota oblicua **en $+\infty$ y en $-\infty$**.
7. **Comprobación por división de polinomios** (receta del tema para racionales): $x^3+x^2+1=(x^2+4)(x+1)+(-4x-3)$, luego $f(x)=x+1+\dfrac{-4x-3}{x^2+4}$ y el último sumando $\to0$. Además (propio, no se pedía): $f(x)-(x+1)<0$ para $x$ grande (la gráfica queda **por debajo** en $+\infty$) y $>0$ en $-\infty$ (por encima); la curva corta a la asíntota en $x=-\frac34$.

**Receta.** Racional $P/Q$: continua donde $Q\neq0$; verticales en los ceros de $Q$ (aquí no hay); horizontal si $\operatorname{gr}P\le\operatorname{gr}Q$; oblicua si $\operatorname{gr}P=\operatorname{gr}Q+1$, con $m=\lim f/x$, $b=\lim(f-mx)$ (o dividiendo $P$ entre $Q$), cada lado por separado.

**Parte del tema.** §7 Asíntotas (U pp.48-50, Prop. 1.12); §8 Continuidad (U p.51); §6 límites en el infinito.

**Verificación.** sympy: `solve(x**2+4)` sin raíces reales; $\lim f/x=1$ y $\lim(f-x)=1$ en $\pm\infty$; `div` da cociente $x+1$, resto $-4x-3$; $f-(x+1)=0$ solo en $x=-3/4$.

**Avisos.** Sin erratas de resultado. El impreso calcula $\lim(f(x)-mx)$ con $m$ genérico y deduce que solo es finito si $m=1$ (método válido, pero menos directo que calcular primero $m=\lim f/x$).

---

## Problema 7 · Método de bisección: número de pasos y tabla

**Fuente:** `X pp.17-18 (Septiembre 2011, Ing. Mecánica, ejercicio 5, 3 puntos)`; variante: `X p.73 (Septiembre 2016, Grado en Ing. Mecánica, Modelo B, pregunta corta 2, 1 punto)`.

**Enunciado.** Sabiendo que la ecuación $x^3+2x^2-1=0$ tiene una raíz en el intervalo $(0,1)$, calcúlese por el método de la bisección con un error menor de $0{,}2$. ¿Cuántos pasos hay que dar?

**Solución.**
1. **Hipótesis (aunque el dato ya lo diga).** $f(x)=x^3+2x^2-1$ es un polinomio, continuo en $[0,1]$; $f(0)=-1<0$, $f(1)=2>0$. Por Bolzano (U p.52) hay una raíz en $(0,1)$ y la bisección es aplicable (U pp.53-54).
2. **Número de pasos.** Tras $n$ puntos medios la raíz está en un intervalo de longitud $\frac{1-0}{2^n}$ que tiene como extremo el último punto medio, así que el error es menor que $\frac1{2^n}$ (U pp.54-55). Se pide $\frac1{2^n}<0{,}2\iff2^n>5\iff n\ge3$ ($2^2=4<5<8=2^3$). **Hacen falta 3 pasos.**
3. **Tabla** (en cada paso se conserva la mitad en cuyos extremos $f$ cambia de signo):

| Paso | $a$ | $b$ | $f(a)$ | $f(b)$ | $c=\frac{a+b}2$ | $f(c)$ | nuevo intervalo |
|---|---|---|---|---|---|---|---|
| 1 | $0$ | $1$ | $-1$ | $2$ | $0{,}5$ | $-0{,}375$ | $[0{,}5;\,1]$ |
| 2 | $0{,}5$ | $1$ | $-0{,}375$ | $2$ | $0{,}75$ | $0{,}546875$ | $[0{,}5;\,0{,}75]$ |
| 3 | $0{,}5$ | $0{,}75$ | $-0{,}375$ | $0{,}546875$ | $0{,}625$ | $0{,}025390625$ | $[0{,}5;\,0{,}625]$ |

4. **Resultado.** $\bar x\approx0{,}625$, con error $<0{,}125<0{,}2$, tras **3 pasos**.

**Variante X p.73.** Enunciado: «Tenemos una función continua $f:[-1,1]\to\mathbb R$, con $f(-1)=1$ y $f(1)=-2$. Buscamos una solución aproximada en $[-1,1]$ por el método de la bisección para la ecuación $f(x)=0$. ¿Cuántas iteraciones son necesarias para asegurar que el error que cometemos al tomar la solución aproximada es menor que $0.15$?» Cota: $\frac{2}{2^n}<0{,}15\iff2^n>13{,}3\iff n\ge4$ ($\frac2{8}=0{,}25$, $\frac2{16}=0{,}125$). **4 iteraciones.** (El impreso llega a lo mismo escribiendo $\frac1{2^{n-1}}<0{,}15$.)

**Receta.** Comprueba continuidad y cambio de signo; $n$ = menor entero con $2^n>\frac{b-a}{\varepsilon}$; tabla $a,b,c,f(c)$ y quédate con la mitad con cambio de signo (mirando signos, no cercanía a 0).

**Parte del tema.** §10 Método de bisección (U pp.53-56), §9 Bolzano.

**Verificación.** Script Python: misma tabla exacta; $f=(x+1)(x^2+x-1)$, raíz exacta $\frac{\sqrt5-1}{2}\approx0{,}6180$, error real $|0{,}625-0{,}618|\approx0{,}007<0{,}2$. Mínimos $n$: $3$ (p.17) y $4$ (p.73).

**Avisos.** Sin erratas. Ojo al contar: el impreso llama «paso» a cada punto medio calculado (3 puntos medios: $0{,}5;\ 0{,}75;\ 0{,}625$), que es el mismo convenio del resumen («tras $n$ puntos medios, error $<\frac{b-a}{2^n}$»).

---

## Tipos de pregunta del tema que caen en examen y no se han desarrollado aquí

Están en X pero no se han elegido (por repetir tipo o por necesitar temas posteriores):
- **Dominio de funciones con raíces y cocientes**: X p.69 ($\sqrt{(2-x)/(x+1)^2}$), X p.85 ($\sqrt{(x^3-1)/(x+1)^2}$, más continuidad), X p.135 ($\sqrt{2x^2-6}$), X p.119 ($\sqrt{x^2-1}$, imagen y gráfica). Se resuelven con desigualdades de 1.1 y la receta de dominio del resumen.
- **Límite «$\frac00$» de un cociente de polinomios** (factorizar y simplificar): X p.59 ($\lim_{x\to-4}\frac{x^2+5x+4}{x+4}=-3$).
- **Asíntota horizontal de una $1^\infty$**: X p.99 ($f=(1+1/x^2)^{2x^2}$: $y=e^2$ en $\pm\infty$, luego sin oblicuas). Combina los problemas 5 y 6.
- **Enunciar Bolzano y aplicarlo**: X p.147 P4 ($e^x-x=2$ en $[1,2]$), igual que el problema 3.
- **Emparedado con $\cos^2$**: X p.147 P1, del mismo tipo que el problema 4.
- **Continuidad con parámetro** (despejar $a$, $b$ para que $f$ sea continua): en X siempre aparece junto con derivabilidad o con L'Hôpital (X pp.35-36, 41, 53-54, 82-83, 86-87; y p.7, $\frac{\operatorname{sen}x}{x}$ en $0$). Se verán en 2.1/2.3; en este tema el tipo está cubierto por los ejercicios 1.31-1.34 de E.
- **No hay en X** preguntas de demostraciones $\varepsilon$-$\delta$ de límites de funciones.
