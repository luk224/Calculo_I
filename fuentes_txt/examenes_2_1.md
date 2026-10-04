# Problemas de examen real — Tema 2.1 La derivada de una función

Fuente **X** = *Exámenes resueltos de Cálculo* (`E:\UNED\CALCULO\Examenes-resueltos-Calculo.pdf`); páginas = páginas PDF. Enunciados y soluciones leídos como imagen (PyMuPDF, 110 dpi). Notación y recetas: las de `temas/tema_2_1_derivada.html` (Def. 2.1 U p.75; Teorema 2.1 U p.76; Def. 2.3 derivadas laterales U p.81; Teorema 1.4 límites laterales U p.47; reglas de derivación U Prop. 2.1 p.79).

Selección (filas de `indice_examenes_1..4.md` con tema 2.1), de fácil a difícil, sin repetir tipo:

| # | Tipo | Fuente |
|---|---|---|
| 1 | Ecuación de la tangente y corte con un eje | X p.106 |
| 2 | Teoría V/F: laterales iguales ⇒ continua | X p.77 |
| 3 | Derivabilidad de $\lvert g(x)\rvert$ en un cero por definición | X p.22 (variantes p.69, p.93) |
| 4 | Parámetro para continuidad y para una pendiente dada | X p.41 |
| 5 | Función a trozos con dos parámetros: continua y derivable | X pp.35-36 |
| 6 | Oscilación: $x^n\operatorname{sen}\frac1x$ | X p.14 |

Descartadas: X p.4 (Feb 2010) y X p.113 (tangente horizontal / a 45°: idénticas a E 2.7 y 2.8, ya resueltos en el tema); X p.53, p.60, p.82, p.86, p.89 (mezclan con extremos 3.4, Newton 2.4, concavidad 3.5 o L'Hôpital 2.3 imprescindible).

---

## Problema 1 — Tangente a $\ln x$ en $(e,1)$: corte con el eje $Y$

**Fuente:** `X p.106 (sin fecha ni convocatoria; examen «I. Electrónica Industrial y Automática», el 4.º de esa serie; pregunta corta 2, 1 punto)`.

**Enunciado.** Calcule el punto en el que la recta tangente en $(e,1)$ a la gráfica de la función dada por $f(x)=\ln x$ corta al eje $Y$.

**Solución.**
1. **Comprobar que el punto está en la gráfica.** $f(e)=\ln e=1$, así que $(e,1)$ es el punto $(a,f(a))$ con $a=e$. (Si no lo estuviera, «la tangente en ese punto» no tendría sentido.)
2. **Pendiente.** La pendiente de la tangente es $f'(a)$ (U p.75). Por la tabla de derivadas (U p.79), $(\ln x)'=\frac1x$, luego $f'(e)=\frac1e$.
3. **Ecuación de la tangente.** Recta por $(a,f(a))$ con pendiente $f'(a)$: $y=f(a)+f'(a)(x-a)$ (U p.87). Aquí $y=1+\frac1e(x-e)$, es decir, $y=\frac xe$.
4. **Corte con el eje $Y$.** El eje $Y$ es la recta $x=0$. Sustituyendo: $y=1+\frac1e(0-e)=1-1=0$.
5. **Respuesta:** el punto $(0,0)$. (La tangente $y=x/e$ pasa por el origen.)

**Receta.** Tangente en $(a,f(a))$: $y=f(a)+f'(a)(x-a)$; para cortar con el eje $Y$ se pone $x=0$, con el eje $X$ se pone $y=0$.

**Parte del tema.** Apartado 3 (tangente y su ecuación) + tabla de derivadas del apartado 6.

**Verificación.** sympy: $1+(0-e)/e=0$. Correcto.

**Avisos.** Ninguna errata; coincide con la solución impresa. Error típico: olvidar el sumando $f(a)$ y escribir $y=\frac1e(x-e)$, que corta al eje $Y$ en $(0,-1)$.

---

## Problema 2 — ¿Derivadas laterales iguales implican continuidad?

**Fuente:** `X p.77 (Febrero 2017, Grado en Ing. Mecánica, Modelo A, pregunta corta 2, 1 punto)`. Es el Ejercicio 2.17 de E (E pp.61-62); la solución impresa lo cita como «Ejercicio 66 del libro de ejercicios» (numeración de una edición anterior de E).

**Enunciado.** Razone si es verdadera o falsa la siguiente afirmación: Si una función $f$ es derivable en un punto $a$ por la derecha y por la izquierda, verificando que $f'(a^+)=f'(a^-)$, entonces la función es continua.

**Solución.**
1. **Qué dicen las hipótesis.** Por la Def. 2.3 (U p.81), existen y son finitos $f'(a^+)=\lim_{h\to0^+}\frac{f(a+h)-f(a)}{h}$ y $f'(a^-)=\lim_{h\to0^-}\frac{f(a+h)-f(a)}{h}$, y además son iguales a un mismo número $L$.
2. **Laterales iguales implica derivable.** Un límite existe si y solo si existen los dos laterales y coinciden (U Teorema 1.4, p.47). Aplicado al cociente incremental: existe $\lim_{h\to0}\frac{f(a+h)-f(a)}{h}=L\in\mathbb R$, es decir, $f$ es derivable en $a$ con $f'(a)=L$ (U Def. 2.1, p.75).
3. **Derivable implica continua.** Por el Teorema 2.1 (U p.76), $f$ es continua en $a$. (Demostración en una línea: $f(a+h)-f(a)=h\cdot\frac{f(a+h)-f(a)}{h}\to0\cdot L=0$.)
4. **Alcance.** La conclusión es «continua en el punto $a$». La afirmación no da información sobre otros puntos: $f(x)=x$ si $x\le1$, $f(x)=5$ si $x>1$ cumple las hipótesis en $a=0$ y es discontinua en $x=1$.
5. **Respuesta:** verdadera, entendida como continuidad en el punto $a$.

**Receta.** «Laterales existen y coinciden» implica derivable (Teorema 1.4), y derivable implica continua en ese punto (Teorema 2.1). El contrarrecíproco (discontinua implica no derivable) ahorra cálculos.

**Parte del tema.** Apartados 4 (Teorema 2.1) y 5 (Def. 2.3 y criterio).

**Verificación.** Razonamiento teórico; no hay cálculo.

**Avisos.**
- El enunciado es ambiguo («la función es continua» sin decir dónde). La solución impresa lo aclara: continua en $a$, «pero no tiene por qué ser continua en todo $\mathbb R$».
- La hipótesis $f'(a^+)=f'(a^-)$ es innecesaria: **basta con que existan** las dos laterales (finitas). Cada una por separado da continuidad lateral ($f(a+h)-f(a)=h\cdot\text{cociente}\to0$ cuando $h\to0^+$ o $h\to0^-$), y continuidad por los dos lados es continuidad (Teorema 1.4). Ejemplo: $|x|$ en $0$ es continua y no derivable. Ni la solución impresa ni E 2.17 lo comentan.
- No confundir con E 2.18: «derivable por los dos lados implica derivable» es **falsa** ($|x|$ en $0$).

---

## Problema 3 — ¿Es derivable en $0$ la función $f(x)=\lvert x^2\operatorname{sen}x\rvert$?

**Fuente:** `X p.22 (Febrero 2012, 2.ª semana, Ing. Mecánica, Modelo B, pregunta corta 2, 1 punto)`.
Variantes del mismo tipo: `X p.69 (Septiembre 2016, Ing. Mecánica, Modelo A, P2, 1 punto)` con $f(x)=\lvert x^2(e^x-1)\rvert$, y `X p.93 (Febrero 2018, Ing. Mecánica, Modelo B, P2, 1 punto)` con $f(x)=\lvert x^2e^x\rvert$.

**Enunciado.** ¿Es derivable en $x=0$ la función dada por $f(x)=\lvert x^2\operatorname{sen}x\rvert$? Justifique la respuesta.

**Solución.**
1. **Por qué hay que usar la definición.** El valor absoluto $\lvert u\rvert$ puede no ser derivable donde $u=0$ ($|x|$ tiene una esquina en $0$), y aquí $u=x^2\operatorname{sen}x$ vale $0$ en $x=0$. No se puede aplicar ninguna regla de derivación; se usa la Def. 2.1 (U p.75).
2. **Valor en el punto.** $f(0)=\lvert0\rvert=0$.
3. **Cociente incremental.** Para $h\neq0$: $\dfrac{f(h)-f(0)}{h}=\dfrac{\lvert h^2\operatorname{sen}h\rvert}{h}=\dfrac{h^2\,\lvert\operatorname{sen}h\rvert}{h}=h\,\lvert\operatorname{sen}h\rvert$, porque $\lvert h^2\rvert=h^2$ (es $\ge0$) y $h^2/h=h$.
4. **Límite.** $\big\lvert h\,\lvert\operatorname{sen}h\rvert\big\rvert\le\lvert h\rvert$ (pues $\lvert\operatorname{sen}h\rvert\le1$) y $\lvert h\rvert\to0$; por la regla del emparedado (U p.45), $h\lvert\operatorname{sen}h\rvert\to0$.
5. **Conclusión.** El límite existe y es finito: $f$ es derivable en $0$ y $f'(0)=0$.

**Por qué no sale una esquina como en $|x|$.** El factor $x^2$ «aplasta» la función: $0\le f(x)\le\lvert x\rvert^3$, y la cota tiene tangente horizontal en $0$. En cambio $\lvert\operatorname{sen}x\rvert$ no es derivable en $0$ (cociente $\lvert\operatorname{sen}h\rvert/h$, laterales $+1$ y $-1$).

**Receta.** Para $\lvert g\rvert$ en un punto $a$ con $g(a)=0$: escribe el cociente $\frac{\lvert g(a+h)\rvert}{h}$, saca del valor absoluto los factores de signo conocido y mira si queda un factor que tiende a $0$ por un acotado; si quedan valores distintos según el signo de $h$, calcula las dos derivadas laterales.

**Parte del tema.** Apartado 2 (derivar por definición) y apartado 5 (derivadas laterales, ejemplo $|x|$); emparedado del tema 1.4.

**Verificación.** sympy: $\lim_{h\to0^\pm}\frac{\lvert h^2\operatorname{sen}h\rvert}{h}=0$ por ambos lados; ídem para $\lvert h^2(e^h-1)\rvert/h$. Correcto.

**Avisos (erratas en las variantes, no en p.22).**
- X p.69 escribe $\dfrac{\lvert h^2\rvert\cdot\lvert e^h-1\rvert}{h}=\lvert h\rvert\cdot\lvert e^h-1\rvert$; debe ser $h\cdot\lvert e^h-1\rvert$ ($h^2/h=h$, no $|h|$). El límite ($0$) y la conclusión son correctos.
- X p.93 dice «$x^2e^x>0$ siempre»; en $x=0$ vale $0$: lo correcto es $x^2e^x\ge0$. Como no cambia de signo, $\lvert x^2e^x\rvert=x^2e^x$ en todo $\mathbb R$ y es derivable (producto de derivables, U Prop. 2.1 p.79) con $f'(0)=0$. Conclusión correcta.
- La solución de p.22 contesta solo con la cadena de igualdades; conviene justificar por qué el límite es $0$ (paso 4).

---

## Problema 4 — $f(x)=\dfrac{a\,e^x}{2+x}$, $f(-2)=0$: continuidad y pendiente de la tangente

**Fuente:** `X p.41 (Febrero 2014, Grado en Ing. Mecánica, Modelo A, ejercicio 5, 3 puntos: 1 por apartado)` (la cabecera del examen está en X p.40).

**Enunciado.** Para $a\in\mathbb R$, sea $f$ la función dada por
$$f(x)=\begin{cases}\dfrac{a\,e^x}{2+x}, & \text{si } x\neq-2,\[2mm] 0, & \text{si } x=-2.\end{cases}$$
a) ¿Es continua si $x\neq-2$? Razone la respuesta.
b) ¿Se puede encontrar $a\in\mathbb R$ para que $f$ sea continua en $x=-2$? Razone la respuesta.
c) Hallar $a\in\mathbb R$ para que la pendiente de la recta tangente a su gráfica sea $1$ si $x=0$.

**Solución.**
1. **a) Fuera de $-2$.** En un entorno de cada $x_0\neq-2$, $f$ coincide con $\frac{ae^x}{2+x}$, cociente de funciones continuas ($ae^x$ y $2+x$) con denominador no nulo. Por el álgebra de funciones continuas (U §1.4), es continua en $x_0$. **Sí.**
2. **b) Qué hay que conseguir.** Continuidad en $-2$ significa $\lim_{x\to-2}f(x)=f(-2)=0$ (U Def. 1.20, p.51).
3. **Caso $a=0$.** Entonces $f(x)=0$ para todo $x$ (también en $-2$): es la función nula, continua. **Sirve $a=0$.**
4. **Caso $a\neq0$.** El numerador tiende a $ae^{-2}\neq0$ y el denominador $2+x\to0$, positivo por la derecha y negativo por la izquierda. Así los límites laterales son $+\infty$ y $-\infty$ (en un orden u otro según el signo de $a$): el límite no es $0$ (ni siquiera existe). **No es continua.**
5. **Respuesta b):** sí, y solo para $a=0$.
6. **c) Traducir.** La pendiente de la tangente en $x=0$ es $f'(0)$ (U p.75). Cerca de $0$, $f(x)=\frac{ae^x}{2+x}$, cociente de derivables con $2+x\neq0$; por la regla del cociente (U Prop. 2.1, p.79):
$$f'(x)=\frac{ae^x(2+x)-ae^x\cdot1}{(2+x)^2}=\frac{a(1+x)e^x}{(2+x)^2}.$$
7. **Evaluar e imponer.** $f'(0)=\frac{a\cdot1\cdot1}{4}=\frac a4$. Igualando a $1$: $a=4$.
8. **Respuesta c):** $a=4$ (la tangente en $(0,2)$ es $y=2+x$).

**Receta.** Para que $f$ sea continua en el punto donde se fija un valor aparte, el límite de la fórmula debe valer exactamente ese valor; si el denominador se anula y el numerador no, el límite es infinito y no hay continuidad. «Pendiente $m$ en $x_0$» equivale a $f'(x_0)=m$.

**Parte del tema.** Apartado 3 (pendiente de la tangente) + reglas del apartado 6; continuidad del tema 1.4.

**Verificación.** sympy: $\lim_{x\to-2^+}\frac{e^x}{2+x}=+\infty$, $\lim_{x\to-2^-}\frac{e^x}{2+x}=-\infty$; $f'(0)=a/4$, solución $a=4$. Correcto.

**Avisos (errata importante en la solución impresa, apartado b).**
- La solución impresa dice que, si $a\neq0$, «podemos aplicar la regla de L'Hôpital» y obtiene $\lim_{x\to-2}\frac{ae^x}{2+x}=\lim\frac{ae^x}{x}=-ae^{-2}\neq0$. **Es incorrecto por dos motivos**: (i) L'Hôpital no se puede aplicar, porque no hay indeterminación $0/0$ ni $\infty/\infty$ (el numerador tiende a $ae^{-2}\neq0$ y el denominador a $0$); (ii) aun aplicándola, la derivada de $2+x$ es $1$, no $x$. El límite correcto no existe (laterales $\pm\infty$). La conclusión («solo $a=0$») sí es correcta.
- Para $a=0$, en c) $f'(0)=0\neq1$: los valores de b) y c) son distintos; no hay un $a$ que cumpla ambas cosas a la vez (el enunciado no lo pide).

---

## Problema 5 — Hallar $a$ y $b$ para que una función a trozos sea continua y derivable

**Fuente:** `X pp.35-36 (Febrero 2013, 2.ª semana, Ing. Mecánica, Modelo B, problema 5; la puntuación no está impresa en este examen, los problemas de estas pruebas valen 3 puntos)`.

**Enunciado.** Sea $f(x)$ la función dada por
$$f(x)=\begin{cases}bx+2, & x<0,\ a\cos x, & x\ge0.\end{cases}$$
Se pide hallar $a$ y $b$ para que la función sea continua y derivable, en caso de que existan. Si no existen $a$ y $b$ con estas características, se debe demostrar.

**Solución.**
1. **Puntos sin problema.** Si $x<0$, cerca de $x$ la función es el polinomio $bx+2$; si $x>0$, es $a\cos x$. Ambas son continuas y derivables, así que $f$ lo es en todo $x\neq0$. Solo hay que estudiar $x=0$, donde cambia la fórmula.
2. **Continuidad en $0$** (U Def. 1.20 p.51 y Teorema 1.4 p.47): $f(0)=a\cos0=a$; $\lim_{x\to0^+}a\cos x=a$; $\lim_{x\to0^-}(bx+2)=2$. Deben coincidir: $a=2$. (Con $a\neq2$ hay salto y, por el Teorema 2.1, tampoco hay derivabilidad.)
3. **Derivada por la derecha** (Def. 2.3, U p.81), con $a=2$ y $f(0)=2$: para $h>0$, $\dfrac{f(h)-f(0)}{h}=\dfrac{2\cos h-2}{h}=2\cdot\dfrac{\cos h-\cos0}{h}\longrightarrow2\cos'(0)=2(-\operatorname{sen}0)=0$ cuando $h\to0^+$. Es el cociente incremental de $\cos$ en $0$, cuyo límite es $\cos'(0)$ (Def. 2.1 + tabla, U p.79). Así $f'(0^+)=0$.
4. **Derivada por la izquierda:** para $h<0$, $f(h)=bh+2$ y $\dfrac{f(h)-f(0)}{h}=\dfrac{bh+2-2}{h}=b$. Luego $f'(0^-)=b$. (Se usa que $f(0)=2$, que es el valor que toma $bx+2$ en $0$; lo garantiza el paso 2.)
5. **Derivable en $0$** si y solo si $f'(0^+)=f'(0^-)$ (criterio de U p.81 + Teorema 1.4): $b=0$.
6. **Respuesta:** $a=2$, $b=0$. Entonces $f(x)=2$ si $x<0$ y $f(x)=2\cos x$ si $x\ge0$, con $f'(0)=0$.

**Receta.** Función a trozos con parámetros: (1) continuidad en el punto de unión, es decir, límites laterales iguales a $f(a)$ (una ecuación); (2) con eso, derivabilidad: $f'(a^+)=f'(a^-)$ calculadas por definición (otra ecuación). Primero la continuidad: sin ella no hay derivabilidad.

**Parte del tema.** Apartado 5 (derivadas laterales y criterio) + apartado 4 (derivable implica continua).

**Verificación.** sympy: $\lim_{h\to0^+}\frac{2\cos h-2}{h}=0$. Correcto.

**Avisos.**
- La solución impresa calcula $\lim_{x\to0^+}\frac{2\cos x-2}{x}$ con **L'Hôpital** (U §2.3, sección posterior). No hace falta: es la derivada de $\cos$ en $0$ por definición (paso 3), como hace el tema en E 2.20 y 2.23. Mismo resultado.
- También escribe $f'(x)=b$ si $x<0$ y $f'(x)=-2\operatorname{sen}x$ si $x>0$. Es correcto, pero los límites de $f'$ por cada lado **no** son por definición las derivadas laterales (coinciden aquí porque $f$ es continua en $0$ y cada trozo es derivable hasta el borde; el resultado que lo justifica es del tema 2.5). Lo seguro es la Def. 2.3, como arriba.

---

## Problema 6 — $f(x)=x^n\operatorname{sen}\frac1x$, $f(0)=0$: continuidad y derivabilidad

**Fuente:** `X p.14 (Febrero 2011, 2.ª semana, Ing. Mecánica, Modelo B, ejercicio 5, 3 puntos)` (la cabecera del examen está en X p.13).

**Enunciado.** Sea $f$ la función dada por
$$f(x)=\begin{cases}x^n\operatorname{sen}\dfrac1x, & \text{si } x\neq0,\[2mm] 0, & \text{si } x=0.\end{cases}$$
(a) Estudie si es continua en $\mathbb R$ para $n\ge1$.
(b) Estudie si es derivable en $\mathbb R$ si $n=1$.

**Solución.**
1. **Puntos $x\neq0$.** Cerca de $x\neq0$, $f$ es el producto de $x^n$ por $\operatorname{sen}(1/x)$, composición de $\operatorname{sen}$ con $1/x$ (continua y derivable si $x\neq0$). Por el álgebra de continuas y las reglas de derivación (U Prop. 2.1 y regla de la cadena, U p.79), $f$ es continua y derivable en todo $x\neq0$.
2. **(a) Continuidad en $0$.** Para $x\neq0$: $\lvert f(x)-0\rvert=\lvert x\rvert^n\,\lvert\operatorname{sen}\tfrac1x\rvert\le\lvert x\rvert^n$, y $\lvert x\rvert^n\to0$ si $n\ge1$. Por el emparedado (U p.45), $\lim_{x\to0}f(x)=0=f(0)$. **$f$ es continua en $\mathbb R$ para todo $n\ge1$.** Aquí basta que el seno esté **acotado**, aunque $\operatorname{sen}\frac1x$ no tenga límite en $0$ (U Ej. 1.44, p.44).
3. **(b) Con $n=1$, derivada en $0$ por definición** (Def. 2.1): $\dfrac{f(h)-f(0)}{h}=\dfrac{h\operatorname{sen}\frac1h}{h}=\operatorname{sen}\dfrac1h$ para $h\neq0$.
4. **Ese límite no existe.** Para $h_k=\frac1{\pi/2+2k\pi}\to0^+$, $\operatorname{sen}\frac1{h_k}=1$; para $h'_k=\frac1{3\pi/2+2k\pi}\to0^+$, vale $-1$. Si el límite fuese un número $L$, los valores sobre ambas sucesiones tenderían a $L$, y $1\neq-1$. (Es U Ej. 1.44; por la izquierda igual, con $-h_k$ y $-h'_k$.)
5. **Conclusión (b).** $f$ no es derivable en $0$ (oscilación: el cuarto modo de fallo del apartado 5 del tema; mismo fenómeno que U Ej. 2.5, $x\cos\frac{10}x$, p.77). En $x\neq0$ sí lo es, con $f'(x)=\operatorname{sen}\frac1x-\frac1x\cos\frac1x$. **Luego para $n=1$, $f$ es derivable en $\mathbb R\setminus\{0\}$ pero no en $\mathbb R$**: continua y no derivable en $0$.
6. **Comparación (no se pide).** Para $n\ge2$ el cociente es $h^{n-1}\operatorname{sen}\frac1h$, acotado en valor absoluto por $\lvert h\rvert^{n-1}\to0$: derivable en $0$ con $f'(0)=0$ (como U Ej. 2.4, p.76).

**Receta.** Donde la fórmula no se puede evaluar, derivar por definición. Si el cociente queda como (algo que tiende a $0$)$\times$(acotado), el límite es $0$. Si queda solo un término oscilante como $\operatorname{sen}\frac1h$, el límite no existe, y se prueba con dos sucesiones $h_k\to0$ que dan valores límite distintos.

**Parte del tema.** Apartado 4 (continua no implica derivable; U Ej. 2.4 y 2.5) y apartado 5 (oscilación).

**Verificación.** sympy: $\lim_{h\to0^+}h^{n-1}\operatorname{sen}\frac1h=0$ para $n=2,3$; $\frac{d}{dx}\big(x\operatorname{sen}\frac1x\big)=\operatorname{sen}\frac1x-\frac1x\cos\frac1x$; numéricamente $\operatorname{sen}\frac1{h_k}=1$ y $\operatorname{sen}\frac1{h'_k}=-1$. Correcto.

**Avisos.**
- La solución impresa solo calcula $f'(0^-)=\lim_{x\to0^-}\operatorname{sen}\frac1x$ y dice que «no existe» sin justificarlo (falta el paso 4 o la cita de U Ej. 1.44). El resultado es correcto.
- El índice `indice_examenes_1.md` resume (b) como «derivable si $n=1$»: es el enunciado, no la respuesta. La respuesta es que **no** es derivable en $0$.
- La frase impresa «No se puede aplicar L'Hôpital» se refiere al límite de (a), que no es una indeterminación de las que trata L'Hôpital.

---

## Tipos de pregunta del tema que caen en examen y no hay en el PDF

- **Derivar por la definición** una función concreta sin valor absoluto ni trozos (p. ej. $\sqrt x$ o $\frac1x$ en un punto, con el conjugado o común denominador): no aparece como pregunta aislada en X; sí en el tema (U Ej. 2.2).
- **Recta normal**: no aparece en ningún examen indexado (solo tangentes).
- **Tangente vertical** ($\sqrt[3]{x}$ en $0$) y **esquina sin parámetros** ($\lvert x-2\rvert$, $\lvert\operatorname{sen}x\rvert$): no hay pregunta específica; lo más cercano es el Problema 3 (que resulta derivable).
- **Velocidad media / instantánea** (como E 2.2, radar de tramo): no aparece en X.
- **Tangente con un ángulo o perpendicular a un vector** (E 2.8, 2.9): solo X p.113 (45°) y X p.4 y p.56 (tangente horizontal), del mismo tipo que E 2.7-2.8.
