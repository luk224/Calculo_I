# Problemas de examen real — Tema 2.4 (Newton, punto fijo, bisección)

Fuente **X** = `Examenes-resueltos-Calculo.pdf` (página = página PDF). Enunciados y soluciones comprobados sobre la página renderizada. Notación y recetas del resumen `temas/tema_2_4_newton_punto_fijo.html`: Teorema 2.2 (hipótesis H0 continuidad, H1 $g:[a,b]\to[a,b]$, H2 $|g'|\le k<1$), Teorema 2.3 ($|x_n-\tilde x|<\frac{k^n}{1-k}(b-a)$), U pp. 88-92; bisección: error $<\frac{b-a}{2^n}$, U p. 54.

Orden: de fácil a difícil. Verificación numérica: `mpmath` con 20 cifras (iteraciones sin redondear) y `sympy` para derivadas.

---

## X1. Bisección: cuántas iteraciones para error < 0.15

**Fuente:** X p.73 (Septiembre 2016, Grado en Ing. Mecánica, Modelo B, pregunta corta 2, 1 punto).

**Enunciado.** Tenemos una función continua $f:[-1,1]\to\mathbb R$, con $f(-1)=1$ y $f(1)=-2$. Buscamos una solución aproximada en $[-1,1]$ por el método de la bisección para la ecuación $f(x)=0$. ¿Cuántas iteraciones son necesarias para asegurar que el error que cometemos al tomar la solución aproximada es menor que $0.15$?

**Solución.**
1. **¿Se puede aplicar bisección?** $f$ es continua en $[-1,1]$ y $f(-1)f(1)=-2<0$: por el Teorema de Bolzano (U §1.4) hay al menos una raíz en $(-1,1)$. Es justo lo que exige el método.
2. **Cota del error.** Cada paso parte el intervalo por la mitad; tras $n$ pasos la raíz está en un intervalo de longitud $\frac{b-a}{2^n}$, y el error de la aproximación es menor que esa longitud (U p. 54). Aquí $b-a=1-(-1)=2$, luego error $<\dfrac{2}{2^n}=\dfrac1{2^{n-1}}$.
3. **Imponer la tolerancia.** Queremos $\dfrac1{2^{n-1}}<0.15\iff 2^{n-1}>\dfrac1{0.15}=6.\overline6$.
4. **Menor natural.** $2^2=4<6.67$ y $2^3=8>6.67$, luego $n-1=3$: **$n=4$** (cota $2/16=0.125<0.15$; con $n=3$ la cota sería $0.25$, que no basta).

**Receta.** Bisección: menor $n$ con $\frac{b-a}{2^n}<\varepsilon$, es decir $n>\log_2\frac{b-a}{\varepsilon}$; se tantea con potencias de 2.

**Parte del tema.** §3 (tabla «¿cuántas iteraciones?», fila bisección); U §1.4 p. 54.

**Verificación.** $2/2^n$ para $n=1,\dots,5$: $1,\ 0.5,\ 0.25,\ 0.125,\ 0.0625$; el primer valor $<0.15$ es el de $n=4$. Coincide con X.

**Avisos.** Ninguna errata. No hace falta conocer $f$: solo la longitud del intervalo. X llama $x_0,x_1$ a los extremos del intervalo (no son iteraciones).

---

## X2. Newton, dos iteraciones: $4-2x=e^x$

**Fuente:** X p.133 (Septiembre 2017, Grado en Ing. Electrónica Industrial y Automática, pregunta corta 3, 1 punto; el examen empieza en p.132).

**Enunciado.** Utilice el método de Newton para aproximar una solución de la ecuación $4-2x=e^x$, tomando como dato inicial el punto $x_0=0$ y realizando dos iteraciones.

**Solución.**
1. **Pasar a la forma $f(x)=0$.** $f(x)=e^x+2x-4$ (el signo da igual: Newton busca ceros).
2. **Hipótesis.** $f$ es derivable en $\mathbb R$ con $f'(x)=e^x+2>0$: nunca se anula, así que la fórmula de Newton siempre está definida (U p. 88). Además $f(0)=-3<0$ y $f(1)=e-2>0$: hay raíz en $(0,1)$ (Bolzano), única porque $f$ es estrictamente creciente.
3. **Fórmula.** $x_{n+1}=x_n-\dfrac{e^{x_n}+2x_n-4}{e^{x_n}+2}$.
4. **$x_1$.** $x_1=0-\dfrac{1+0-4}{1+2}=0-\dfrac{-3}{3}=1$.
5. **$x_2$.** $x_2=1-\dfrac{e+2-4}{e+2}=1-\dfrac{e-2}{e+2}=\dfrac{4}{e+2}\approx 0.8477$.

**Receta.** Escribe $f$ y $f'$, comprueba $f'(x_n)\ne0$, simplifica $x-f/f'$ y rellena la tabla $n\,|\,x_n\,|\,f(x_n)\,|\,f'(x_n)$.

**Parte del tema.** §1 Método de Newton (U pp. 86-90).

**Verificación.** $x_1=1$, $x_2=0.8477662\ldots$; una tercera iteración daría $0.8408544$, y la raíz es $\tilde x=0.8408415\ldots$ Coincide con X.

**Avisos.** Ninguna errata. Forma cerrada útil: $x_2=4/(e+2)$.

---

## X3. Punto fijo, cinco iteraciones: $f(x)=1-\frac1{x^2+2}$

**Fuente:** X p.1 (Febrero 2010, 1ª semana, Ing. Eléctrica, pregunta corta 2, 1 punto).

**Enunciado.** Se da la función $f(x)=1-\dfrac{1}{x^2+2}$. Utilizando el método del punto fijo, encuentre un punto fijo de $f$. Realice 5 iteraciones y comience con $x_0=0$.

**Solución.**
1. **Qué se busca.** Un punto fijo: $x$ con $x=f(x)$. La función de iteración ya viene dada, $g=f$, y se itera $x_{n+1}=g(x_n)$ (U p. 90).
2. **(Opcional, pero da el porqué) ¿Converge?** En $[a,b]=[0,1]$: (H0) $g$ es continua (el denominador es $\ge2$). (H1) $g'(x)=\dfrac{2x}{(x^2+2)^2}\ge0$, así que $g$ es creciente y $g([0,1])=[g(0),g(1)]=[\tfrac12,\tfrac23]\subset[0,1]$. (H2) En $(0,1)$ el numerador $2x\le2$ y el denominador $(x^2+2)^2\ge4$, luego $|g'(x)|\le\frac12=k<1$. Por el Teorema 2.2 (U p. 91) hay un único punto fijo en $[0,1]$ y la sucesión converge desde $x_0=0$.
3. **Iteraciones** (con todas las cifras de la calculadora):
   - $x_1=1-\frac1{2}=\frac12$
   - $x_2=1-\dfrac{1}{1/4+2}=1-\frac49=\frac59\approx0.55556$
   - $x_3=1-\dfrac1{(5/9)^2+2}$; como $(5/9)^2+2=\frac{25}{81}+2=\frac{187}{81}$, $x_3=1-\frac{81}{187}=\frac{106}{187}\approx0.56684$
   - $x_4\approx0.56921$
   - $x_5\approx0.56971$
4. **(Extra) Cota del error** (Teorema 2.3): $|x_5-\tilde x|<\dfrac{(1/2)^5}{1/2}\cdot1=\dfrac1{16}=0.0625$ (cota pesimista: el error real es $\approx1.3\cdot10^{-4}$).

**Receta.** Punto fijo con $g$ dada: itera $x_{n+1}=g(x_n)$ guardando todas las cifras; si piden justificar, comprueba H0-H2 del Teorema 2.2 en un intervalo que contenga a $x_0$.

**Parte del tema.** §2 Método de punto fijo, Teoremas 2.2 y 2.3 (U pp. 90-92).

**Verificación.** $x_1,\dots,x_5=0.5,\ 0.5555556,\ 0.5668449,\ 0.5692094,\ 0.5697073$; punto fijo $\tilde x=0.5698403\ldots$; $\max_{[0,1]}g'\approx0.2296$ (luego $k=\frac12$ es válida). Coincide con X.

**Avisos.** X imprime $x_3\approx0.56685$ porque redondea antes $x_2$ a $0.5556$; con todas las cifras $x_3=0.566845$ (diferencia irrelevante). X no justifica la convergencia: en una pregunta de 1 punto basta iterar, pero conviene saber hacerlo.

---

## X4. Newton con criterio de parada: $x-2^{-x}=0$

**Fuente:** X p.20 (Febrero 2012, 1ª semana, Ing. Mecánica, Modelo A, ejercicio 5, 3 puntos; el examen empieza en p.19).

**Enunciado.** Mediante el Método de Newton, encontrar una raíz próxima a $x_0=0$ de la ecuación $x-2^{-x}=0$. Utilizar tres decimales redondeados en cada iteración hasta que se cumpla $|x_{n-1}-x_n|<10^{-3}$.

**Solución.**
1. **Localizar la raíz.** $f(x)=x-2^{-x}$ es continua; $f(0)=-1<0$ y $f(1)=\frac12>0$: hay raíz en $(0,1)$ (Bolzano). Como $f'>0$ (paso 2), $f$ es estrictamente creciente y la raíz es única.
2. **Derivada.** $2^{-x}=e^{-x\ln2}$, luego $(2^{-x})'=-\ln2\cdot2^{-x}$ y $f'(x)=1+\ln2\cdot2^{-x}>0$: nunca se anula.
3. **Fórmula.** $x_{n+1}=x_n-\dfrac{x_n-2^{-x_n}}{1+\ln2\cdot2^{-x_n}}$.
4. **Iteraciones** (redondeando a 3 decimales, como pide el enunciado):

   | $n$ | $x_n$ | $2^{-x_n}$ | $f(x_n)$ | $f'(x_n)$ | $x_{n+1}$ | diferencia $\lvert x_{n+1}-x_n\rvert$ |
   |---|---|---|---|---|---|---|
   | 0 | 0 | 1 | $-1$ | $1.693$ | $0.591$ | $0.591$ |
   | 1 | 0.591 | 0.664 | $-0.073$ | $1.460$ | $0.641$ | $0.050$ |
   | 2 | 0.641 | 0.641 | $\approx -0.0001$ | $1.444$ | $0.641$ | $0<10^{-3}$ |

5. **Parar.** En la tercera iteración $|x_3-x_2|=0<10^{-3}$: se cumple el criterio. **Raíz $\approx0.641$.**

**Receta.** Newton «hasta que $|x_n-x_{n-1}|<$ tol»: Bolzano para localizar, $f'\neq0$, tabla con una columna para la diferencia entre iterados, y parar en la primera fila que cumpla la tolerancia.

**Parte del tema.** §1, «Cuándo parar: los errores aproximados» (U pp. 89-90). Aquí el criterio es el error **absoluto** aproximado, no el relativo $\varepsilon_r$ del resumen.

**Verificación.** Sin redondear: $x_1=0.5906161$, $x_2=0.6409096$, $x_3=0.6411857$ ($|x_3-x_2|=2.8\cdot10^{-4}<10^{-3}$); raíz $\tilde x=0.6411857\ldots$ Con o sin redondeo: 3 iteraciones y $0.641$. Coincide con X.

**Avisos.** Errata tipográfica en X: en el cálculo de $x_3$ escribe «$\approx 0.64091-\ldots$» en lugar de $0.641-\ldots$ (no afecta). El criterio $|x_n-x_{n-1}|<10^{-3}$ es práctico: **no garantiza** que el error real sea $<10^{-3}$ (U no da cota de error para Newton).

---

## X5. Punto fijo completo: convergencia, cuatro iteraciones y cota del error ($\frac12\operatorname{sen}x-x+1=0$)

**Fuente:** X p.141 (Febrero 2018, 2ª semana, Grado en Ing. Electrónica Industrial y Automática, ejercicio 6, 3 puntos; el examen empieza en p.140).

**Enunciado.** Dada la ecuación $\dfrac12\operatorname{sen}x-x+1=0$:
- Compruebe que el método del punto fijo converge para cualquier dato inicial $0\le x_0\le\pi$. (1 PUNTO)
- Utilice el método del punto fijo para aproximar la solución de la ecuación partiendo del dato inicial $x_0=2$ y realizando cuatro iteraciones. (1 PUNTO)
- Estime el error absoluto cometido al realizar la aproximación del apartado anterior. (1 PUNTO)

**Solución.**
1. **Pasar a $x=g(x)$.** Despejando la $x$ que no está dentro del seno: $x=\frac12\operatorname{sen}x+1$, así que $g(x)=\frac12\operatorname{sen}x+1$ y $[a,b]=[0,\pi]$.
2. **(H0)** $g$ es continua en $\mathbb R$.
3. **(H1) $g([0,\pi])\subset[0,\pi]$.** Si $x\in[0,\pi]$, $\operatorname{sen}x\in[0,1]$, luego $g(x)\in[1,\tfrac32]\subset[0,\pi]$.
4. **(H2)** $g'(x)=\frac12\cos x$ y $|g'(x)|\le\frac12=k<1$ para todo $x\in(0,\pi)$.
5. **Conclusión (a).** Por el Teorema 2.2 (U p. 91), $g$ tiene un único punto fijo $\tilde x\in[0,\pi]$ (que es la solución de la ecuación) y $x_{n+1}=g(x_n)$ converge a él para todo $x_0\in[0,\pi]$.
6. **(b) Iteraciones** desde $x_0=2$ (calculadora en radianes):
   - $x_1=g(2)=\frac12\operatorname{sen}2+1\approx1.454649$
   - $x_2=g(x_1)\approx1.496631$
   - $x_3=g(x_2)\approx1.498626$
   - $x_4=g(x_3)\approx1.498698$
7. **(c) Cota del error** (Teorema 2.3, U p. 91): $|x_4-\tilde x|<\dfrac{(1/2)^4}{1-1/2}(\pi-0)=\dfrac{\pi}{8}\approx0.392699$.

**Receta.** Convergencia de punto fijo: despeja $x=g(x)$, comprueba **las tres** hipótesis (continuidad, $g([a,b])\subset[a,b]$, $|g'|\le k<1$) y cita el Teorema 2.2; para el error, sustituye en $\frac{k^n}{1-k}(b-a)$.

**Parte del tema.** §2, Teoremas 2.2 y 2.3; mismo esquema que el Ejemplo 2.17 de U (pp. 92-93) y el Ejercicio 2.38 de E.

**Verificación.** $x_1,\dots,x_4=1.4546487,\ 1.4966312,\ 1.4986255,\ 1.4986984$; $\tilde x=1.4987011\ldots$; error real $2.7\cdot10^{-6}$, muy por debajo de la cota $\pi/8\approx0.3927$. Coincide con X.

**Avisos (erratas de X).**
- Escribe «$x_1=g(1)=\frac12\operatorname{sen}2+1$»: debe ser **$g(2)$** (el valor numérico es correcto).
- Cita el Teorema 2.2 en la «página 89 del libro de teoría»: en la edición de U que usamos está en la **p. 91**.
- X solo comprueba $|g'|\le\frac12$ y **omite (H1)** ($g([0,\pi])\subset[0,\pi]$), que es imprescindible (ver «Error típico: comprobar solo $|g'|<1$» del resumen). En el examen hay que escribirla.

---

## X6. Punto fijo: número de iteraciones para error $\le0.1$ ($\cos x^2\operatorname{sen}(x+1)-2x=0$)

**Fuente:** X pp.29-30 (Septiembre 2012, reserva, Ing. Mecánica, Modelo A, ejercicio 5, 3 puntos; el examen empieza en p.28).

**Enunciado.** Aplíquese el método del punto fijo para encontrar una solución aproximada, con 5 cifras significativas y un error menor o igual de $0.1$ de la ecuación
$$\cos x^2\operatorname{sen}(x+1)-2x=0$$
con el punto inicial $x_0=0$. ¿Cuántas iteraciones hay que hacer? (La función $f(x)=\frac12\cos x^2\operatorname{sen}(x+1)$ es contractiva en $[0,1]$.)

($\cos x^2$ significa $\cos(x^2)$: así lo usa la solución impresa y así salen sus números; con $\cos^2x$ las iteraciones serían otras.)

**Solución.**
1. **Pasar a $x=g(x)$.** $\cos(x^2)\operatorname{sen}(x+1)=2x\iff x=\tfrac12\cos(x^2)\operatorname{sen}(x+1)=:g(x)$.
2. **Dónde caen los valores de $g$.** Para $x\in[0,1]$: $x^2\in[0,1]\subset[0,\frac\pi2)$, luego $\cos(x^2)\in(0,1]$; y $x+1\in[1,2]\subset(0,\pi)$, luego $\operatorname{sen}(x+1)\in(0,1]$. Por tanto $0<g(x)\le\frac12$: $g$ manda $[0,1]$, y en particular $[0,\frac12]$, dentro de $[0,\frac12]$. Trabajamos en $[a,b]=[0,\tfrac12]$, que contiene a $x_0=0$.
3. **(H0), (H1).** $g$ es continua (producto de continuas) y, por el paso 2, $g([0,\frac12])\subset[0,\frac12]$.
4. **(H2): derivada** (regla del producto y regla de la cadena, $(\cos x^2)'=-2x\operatorname{sen}x^2$):
   $$g'(x)=\tfrac12\big[-2x\operatorname{sen}(x^2)\operatorname{sen}(x+1)+\cos(x^2)\cos(x+1)\big]=-x\operatorname{sen}(x^2)\operatorname{sen}(x+1)+\tfrac12\cos(x^2)\cos(x+1).$$
   En $(0,\frac12)$: $|x\operatorname{sen}(x^2)\operatorname{sen}(x+1)|\le\frac12\operatorname{sen}\frac14\approx0.124$ y $|\frac12\cos(x^2)\cos(x+1)|\le\frac12\cos1\approx0.270$ (pues $x+1\in(1,1.5)$, donde $\cos$ es positivo y decreciente). Por la desigualdad triangular, $|g'(x)|\le0.394<\frac12=:k$.
5. **Número de iteraciones** (Teorema 2.3, U pp. 91-92): basta que $\dfrac{k^n}{1-k}(b-a)=\dfrac{(1/2)^n}{1/2}\cdot\dfrac12=\dfrac1{2^n}\le0.1$, es decir $2^n\ge10$. Como $2^3=8<10\le16=2^4$: **$n=4$** iteraciones garantizan error $\le0.1$ (de hecho $<0.0625$).
6. **Iteraciones** (5 cifras significativas): $x_1=\frac12\operatorname{sen}1=0.42074$, $x_2=0.48666$, $x_3=0.48432$, $x_4=0.48449$ (y $x_5=0.48448$). Solución aproximada: $0.48449$.

**Respuesta de X:** trabaja en $[0,1]$ con $k=\frac12$, obtiene $\frac1{2^{n-1}}<0.1\Rightarrow n=5$ y calcula hasta $x_5=0.48448$. El número $5$ también garantiza el error (más iteraciones nunca empeoran la cota), pero **su justificación es incorrecta** (ver avisos). Si se quiere mantener $[0,1]$ hace falta un $k$ válido: $\max_{[0,1]}|g'|=|g'(1)|\approx0.878$, y con $k=0.88$ la cota exige $n>\frac{\ln(0.1\cdot0.12)}{\ln0.88}\approx34.6$, es decir 35 iteraciones: correcto pero muy pesimista. De ahí la ventaja de reducir el intervalo.

**Receta.** Para «¿cuántas iteraciones garantizan error $<\varepsilon$?»: elige el intervalo $[a,b]$ más pequeño que contenga a $x_0$ y que $g$ lleve en sí mismo, acota $|g'|$ ahí por $k<1$ y toma el menor natural con $\frac{k^n}{1-k}(b-a)<\varepsilon$.

**Parte del tema.** §2 Teoremas 2.2 y 2.3; §3 «Lista de pasos para el caso garantizar error $<\varepsilon$» (U pp. 91-92).

**Verificación.** Iteraciones con todas las cifras: $0.4207355,\ 0.4866554,\ 0.4843234,\ 0.4844902,\ 0.4844785$; punto fijo $\tilde x=0.4844793\ldots$ (error real de $x_4$: $1.1\cdot10^{-5}$). `sympy`: $g'(x)=-x\operatorname{sen}(x^2)\operatorname{sen}(x+1)+\frac12\cos(x^2)\cos(x+1)$. Muestreo fino: $\max_{[0,1]}|g'|=0.8776$ (en $x=1$), $\max_{[0,1/2]}|g'|=0.2702$ (en $x=0$); $g([0,1])\subset[0.2456,\,0.4867]$.

**Avisos (errata grave de X).**
- **Derivada mal calculada:** X escribe $|f'(x)|=\frac12|-\operatorname{sen}x^2\operatorname{sen}(x+1)+\cos x^2\cos(x+1)|=\frac12|\cos(x^2+x+1)|\le\frac12$. Falta el factor $2x$ de la regla de la cadena en $(\cos x^2)'=-2x\operatorname{sen}x^2$. Con la derivada correcta $|g'(1)|\approx0.878>\frac12$, así que **$k=\frac12$ no es válida en $[0,1]$**.
- El resultado $n=5$ sí garantiza error $\le0.1$ (lo respalda el razonamiento corregido en $[0,\frac12]$, que da $n=4$), y los valores numéricos de X son correctos.
- X tampoco comprueba $f([0,1])\subset[0,1]$; solo lo afirma. El enunciado lo da por hecho («contractiva en $[0,1]$»), pero conviene justificarlo (paso 2).

---

## Tipos de pregunta del tema que caen en examen y no se han incluido arriba

- **Teoría (pregunta corta):** «Describa el método de Newton: para qué sirve, cómo se usa» (X p.129, I. Electrónica); «condiciones para que $g:[a,b]\to[a,b]$ tenga un único punto fijo» (Febrero 2014, Modelo B, P1, según `indice_examenes_2.md`); «describa el método del punto fijo y sus condiciones de aplicación» e «importancia de la cota de error» (X p.9, sin solución impresa). Se responden con el enunciado de los Teoremas 2.2-2.3 y la deducción geométrica de Newton (recta tangente).
- **Newton para raíces cúbicas:** $\sqrt[3]9$ con $x_0=1$ (Septiembre 2018, Modelo A, X pp.96-97; $x_1=3.6667$, $x_2=2.6676$, verificado) y $\sqrt[3]5$ con $x_0=2$ (Febrero 2013, X p.32). Mismo tipo que X2 (receta del Ejercicio 2.34 de E).
- **Newton dentro de un ejercicio largo:** función a trozos con continuidad y derivabilidad y después Newton para $f(x)=1$ (Febrero 2017, Modelo B, X pp.82-83); una iteración para $x^5-x^4+2x^3-1=0$ (Febrero 2016, Modelo A).
- **Punto fijo dentro de un estudio de funciones:** $g(x)=1/(x^2+4)$, 3 iteraciones en $[0,1]$ (Febrero 2018, Modelo A, X pp.89-90).
- **Bisección con la ecuación explícita:** $x^3+2x^2-1=0$ en $(0,1)$ con error $<0.3$ o $<0.2$ (X p.10, pp.17-18, pp.116-117): mismo tipo que X1, pero además se escriben los intervalos sucesivos.
- No aparece en el PDF ninguna pregunta de **número de iteraciones de Newton garantizado** (U no da esa cota) ni de **elegir, entre varias $g$, la que converge** (Ejemplo 2.18 de U); esta última podría caer como teoría.
