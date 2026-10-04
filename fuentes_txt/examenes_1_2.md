# Así lo preguntan en el examen: tema 1.2 Sucesiones

Fuente **X** = *Exámenes resueltos de Cálculo* (`E:\UNED\CALCULO\Examenes-resueltos-Calculo.pdf`). Página = página del PDF. Se ha leído cada enunciado y cada solución impresa en la imagen renderizada de la página (PyMuPDF), no en `examenes.txt`.
Filtro: las filas «1.2» de `indice_examenes_1..4.md` (X pp. 4, 13, 19, 32, 40, 49, 93, 101, 115, 119, 139, 150). Se eligen 6 de tipos distintos, ordenados de fácil a difícil. Todos se resuelven con lo que enseña el tema 1.2 (U §1.2, pp. 22-33). Las «recetas» y apartados citados son los de `temas/tema_1_2_sucesiones.html`.

---

## 1. Teoría: convergente, acotada, monótona (tipo test)

**Fuente:** `X p.119` (Examen 4 «elaborado con exámenes de asignaturas similares», sin fecha ni convocatoria, Ejercicio 1, test, sin puntuación indicada).

**Enunciado.** Una sucesión de números reales puede ser a la vez:
**A)** Convergente y no acotada; **B)** No convergente y acotada; **C)** Estrictamente creciente y estrictamente decreciente; **D)** Ninguna de las anteriores.

**Solución.**
1. **A es imposible.** Toda sucesión convergente está acotada (U Prop. 1.1, p. 24). La idea: si $a_n\to l$, tomando $\varepsilon=1$ hay un $N$ a partir del cual $|a_n-l|\le1$, es decir, $|a_n|\le|l|+1$. Los términos anteriores a $N$ son una cantidad finita, así que tienen un máximo $M_0$ en valor absoluto. Con $M=\max\{M_0,|l|+1\}$ resulta $|a_n|\le M$ para todo $n$.
2. **B es posible.** Ejemplo: $a_n=(-1)^n$. Está acotada porque $|a_n|=1$, pero no converge porque oscila entre $-1$ y $1$ (los términos pares tienden a $1$ y los impares a $-1$, y el límite es único, U p. 24). Es el recíproco de la Prop. 1.1, que **es falso**.
3. **C es imposible.** Estrictamente creciente significa $a_{n+1}>a_n$ para todo $n$ y estrictamente decreciente $a_{n+1}<a_n$ (U Def. 1.13, p. 31). Las dos cosas no pueden cumplirse a la vez ni siquiera para $n=1$. (Sin el «estrictamente» sí sería posible: una sucesión constante es creciente y decreciente a la vez.)
4. **D es falsa** porque B es cierta. **Respuesta: B.**

**Receta:** ante «¿puede ocurrir…?», busca un ejemplo con las sucesiones más sencillas ($(-1)^n$, $n$, $1/n$). Ante «¿ocurre siempre?», recuerda un teorema (convergente $\Rightarrow$ acotada) o busca un contraejemplo.
**Parte del tema:** §2 (convergencia y unicidad del límite), §3 (acotadas, Prop. 1.1), §8 (monotonía). Es el mismo tipo que el Ejercicio 1.6 de E.
**Verificación:** razonamiento teórico, no hay nada que calcular.
**Avisos:** la solución impresa solo dice «La opción cierta es B» y remite a otro libro («Fundamentos de Matemáticas I», 5.2.7 y 5.2.21), que no es del curso. La justificación de arriba es propia y usa U.

---

## 2. Cociente $\frac{\infty}{\infty}$ con raíces

**Fuente:** `X p.4` (Febrero 2010, 2ª semana, Ingeniería Eléctrica, pregunta corta 1, 1 punto).

**Enunciado.** Calcule
$$\lim_{n\to\infty}\frac{\sqrt{n^2+1}-\sqrt{9n^2+2}}{3n-2+\sqrt{4n^2-3}}.$$

**Solución.**
1. **Clasificar.** El denominador tiende a $+\infty$. El numerador es $\infty-\infty$, pero no hace falta el conjugado: cada raíz es «del orden de $n$» y el cociente se resuelve dividiendo entre $n$.
2. **Sacar $n$ de cada raíz.** Como $n>0$, $\sqrt{n^2}=n$, y entonces $\sqrt{n^2+1}=\sqrt{n^2\left(1+\tfrac1{n^2}\right)}=n\sqrt{1+\tfrac1{n^2}}$. Del mismo modo, $\sqrt{9n^2+2}=n\sqrt{9+\tfrac2{n^2}}$ y $\sqrt{4n^2-3}=n\sqrt{4-\tfrac3{n^2}}$.
3. **Dividir numerador y denominador entre $n$:**
$$\frac{\sqrt{1+\frac1{n^2}}-\sqrt{9+\frac2{n^2}}}{3-\frac2n+\sqrt{4-\frac3{n^2}}}.$$
4. **Pasar al límite.** $\frac1{n^2},\frac2n\to0$. La raíz conserva límites (fórmula (1.1) de U, p. 29: $\sqrt{x_n}=x_n^{1/2}$). Por el álgebra de límites (U Prop. 1.3, pp. 26-27), y como el denominador tiende a $3+2=5\neq0$:
$$\frac{1-3}{3+2}=\boxed{-\tfrac25}.$$

**Receta:** si aparecen raíces de polinomios en un cociente, saca de cada raíz la mayor potencia del radicando ($\sqrt{n^2\cdot(\dots)}=n\sqrt{\dots}$) y divide arriba y abajo entre la potencia dominante.
**Parte del tema:** §5 (álgebra de límites), §7 (fórmula (1.1)), receta de los Ejercicios 1.7-1.9 de E.
**Verificación:** sympy `limit(...)` $=-2/5$. Coincide con la solución impresa.
**Avisos:** ninguno. La solución impresa es correcta, pero no explica que $\sqrt{n^2}=n$ porque $n>0$.

---

## 3. $\infty-\infty$ con raíces: el conjugado

**Fuente:** `X p.19` (Febrero 2012, 1ª semana, Ingeniería Mecánica, Modelo A, pregunta corta 1, 1 punto).

**Enunciado.** Calcule el siguiente límite:
$$\lim_{n\to\infty}\left(\sqrt{n^2-2n}-\sqrt{n^2+4}\right).$$

**Solución.**
1. **Clasificar.** Las dos raíces tienden a $+\infty$, así que la forma es $\infty-\infty$, que es indeterminada (U p. 29). Aquí **no** sirve dividir entre $n$, porque no hay cociente. Además, las dos raíces son «casi iguales» ($\approx n$), y lo que importa es su diferencia.
2. **Multiplicar y dividir por el conjugado** $\sqrt{n^2-2n}+\sqrt{n^2+4}$, que es $>0$, para usar $(A-B)(A+B)=A^2-B^2$ y eliminar las raíces del numerador (U Ej. 1.25, p. 30). La expresión es real para $n\ge2$, que es lo que importa en el límite:
$$\frac{(n^2-2n)-(n^2+4)}{\sqrt{n^2-2n}+\sqrt{n^2+4}}=\frac{-2n-4}{\sqrt{n^2-2n}+\sqrt{n^2+4}}.$$
3. **Ahora es un cociente $\frac{\infty}{\infty}$.** Se divide entre $n$ (usando $\sqrt{n^2-2n}=n\sqrt{1-\tfrac2n}$):
$$\frac{-2-\frac4n}{\sqrt{1-\frac2n}+\sqrt{1+\frac4{n^2}}}\longrightarrow\frac{-2}{1+1}=\boxed{-1}.$$

**Receta:** $\infty-\infty$ con raíces $\Rightarrow$ multiplica y divide por el conjugado, y después divide entre la potencia dominante.
**Parte del tema:** §7 (conjugado), Ejercicio 1.10 de E.
**Verificación:** sympy $=-1$. Coincide con la solución impresa.
**Comprobación mental:** $\sqrt{n^2+bn+c}\approx n+\frac b2$ da $(n-1)-(n+0)=-1$.
**Avisos:** ninguno.

---

## 4. Acotada por algo que tiende a 0 (no hace falta calcular lo «feo»)

**Fuente:** `X p.115` (Examen 3 «elaborado con exámenes de asignaturas similares», sin fecha, Ejercicio 1, test).

**Enunciado.** Señale el valor del límite
$$\lim_{n\to\infty}\frac{\cos^2\!\left(\dfrac{\exp\dfrac{n^2}{\sqrt[n]{(n+1)!}}}{\ln|n|}\right)}{n}:\quad \text{A) }\infty;\ \text{B) }0;\ \text{C) }1;\ \text{D) Ninguno de los anteriores.}$$

**Solución.**
1. **No hace falta estudiar lo de dentro del coseno.** Sea $b_n=\cos^2(\cdots)$, sea cual sea el argumento. Como $-1\le\cos t\le1$ para todo $t$, se tiene $0\le b_n\le1$: la sucesión $(b_n)$ está **acotada**. (El argumento está definido para $n\ge2$; con $n=1$ sale $\ln 1=0$ en un denominador. Un número finito de términos no cambia el límite.)
2. **Escribir el término como (acotada)·(tiende a 0):** $a_n=b_n\cdot\frac1n$, con $\frac1n\to0$.
3. **Aplicar el resultado «acotada por infinitésimo» (U Prop. 1.2, p. 26), o bien el emparedado (U Teorema 1.2, p. 25):**
$$0\le a_n\le\frac1n\quad(n\ge2),\qquad 0\to0,\quad \frac1n\to0\ \Longrightarrow\ a_n\to0.$$
**Respuesta: B) 0.**

**Receta:** si aparece $\sin$ o $\cos$ (o cualquier factor acotado) de algo complicado, multiplicado por algo que tiende a 0, el límite es 0. Acota antes de ponerte a calcular.
**Parte del tema:** §3 (acotadas), §4 (emparedado y «tiende a 0 por acotada»), Ejercicio 1.14 de E (emparedado).
**Verificación:** numérica con mpmath (600 dígitos): $a_{10}\approx0{,}0996$, $a_{50}\approx0{,}0126$, $a_{200}\approx0{,}0042$. Todos cumplen $0\le a_n\le 1/n$.
(Curiosidad: el argumento interior $\frac{n^2}{\sqrt[n]{(n+1)!}}$ crece como $e\,n$. Vale $17{,}4$ en $n=10$ y $520$ en $n=200$, así que la exponencial es enorme. Por eso intentar calcularlo es una trampa.)
**Avisos:**
- La fila de `indice_examenes_3.md` (X p.115) transcribe mal la fórmula como «cos²(…)/(ln|n|/n)». Leída en la imagen, $\ln|n|$ está **dentro** del coseno, dividiendo a la exponencial, y el denominador exterior es solo $n$. Con la lectura del índice el límite no sería 0.
- La solución impresa es correcta pero escueta («acotada… y $\lim 1/n=0$»). No cita el resultado que usa (U Prop. 1.2) ni dice que hace falta $n\ge2$.

---

## 5. Indeterminación $1^{\infty}$ (y su contraste: base que no tiende a 1)

**Fuente:** `X p.40` (Febrero 2014, Grado en Ingeniería Mecánica, cód. 68031029, Modelo A, pregunta corta 1, 1 punto).

**Enunciado.** Sea
$$a_n=\left(\frac{n^2+n+1}{n^2-n-1}\right)^{\frac{n^2}{n+2}}.$$
¿Cuánto vale $\lim_{n\to\infty}a_n$? Justifique la respuesta.

**Solución.**
1. **Clasificar (calcular por separado base y exponente).** Base: $x_n=\frac{n^2+n+1}{n^2-n-1}\to1$, dividiendo entre $n^2$. Exponente: $y_n=\frac{n^2}{n+2}\to+\infty$. La forma es $1^{\infty}$, que es indeterminada: no se puede aplicar (1.1) directamente.
2. **Comprobar la hipótesis de la receta.** $x_n-1=\frac{(n^2+n+1)-(n^2-n-1)}{n^2-n-1}=\frac{2n+1}{n^2-n-1}$. Es $>0$ para $n\ge2$, porque $n^2-n-1>0$ si $n\ge2$. Tiende a 0 con signo constante.
3. **Escribir la base como $1+\frac1{c_n}$** con $c_n=\frac{n^2-n-1}{2n+1}\to+\infty$, y repartir el exponente:
$$a_n=\left[\left(1+\frac1{c_n}\right)^{c_n}\right]^{s_n},\qquad s_n=\frac{y_n}{c_n}=y_n(x_n-1)=\frac{n^2(2n+1)}{(n+2)(n^2-n-1)}.$$
4. **Límite del corchete:** $\left(1+\frac1{c_n}\right)^{c_n}\to e$ (U Prop. 1.5, p. 31: vale para cualquier $c_n\to\pm\infty$).
5. **Límite del exponente:** $s_n=\frac{2n^3+n^2}{n^3+n^2-3n-2}\to2$ (cociente de polinomios del mismo grado, se divide entre $n^3$).
6. **Juntar con (1.1)** (U p. 29: si $u_n\to u>0$ y $v_n\to v$, entonces $u_n^{v_n}\to u^v$): $\lim a_n=e^{2}$.
**Atajo** (receta del tema, apartado 9): $\lim x_n^{y_n}=e^{\lim y_n(x_n-1)}=e^{2}$. **Resultado: $\boxed{e^2}$.**

**Contraste: cuando NO es $1^\infty$** (`X p.13`, Febrero 2011, 2ª semana, Mecánica, Modelo B, pregunta corta 1, 1 punto): $\lim\left(\frac{n^2+2n}{16n^2+4n-7}\right)^{n}$. Aquí la base tiende a $\frac1{16}\neq1$, así que no hay indeterminación. La base es positiva y menor que $\frac12$ para $n$ grande, de modo que $0<a_n\le(\tfrac12)^n\to0$. El límite es **0** (es $r^n$ con $|r|<1$, catálogo del tema). Sympy da 0.
*Errata de notación en X p.13:* la vía alternativa impresa escribe «$\ln l=n\ln\lim(\dots)$», con la $n$ **fuera** del límite, lo cual no tiene sentido. Lo correcto es $\ln l=\lim\big(n\ln x_n\big)=-\infty$, luego $l=e^{-\infty}=0$.

**Receta:** ante $x_n^{y_n}$, calcula primero $\lim x_n$ y $\lim y_n$. Solo si sale $1^{\pm\infty}$, usa $\lim x_n^{y_n}=e^{\lim y_n(x_n-1)}$. Si la base tiende a un número distinto de 1, basta con (1.1) o con $r^n$.
**Parte del tema:** §9 (número $e$, receta $1^{\pm\infty}$), §7 (fórmula (1.1)), Ejercicios 1.12-1.13 de E.
**Verificación:** sympy: $\lim a_n=e^2$ y $\lim y_n(x_n-1)=2$. Numérico: $a_{1000}\approx7{,}37433$, $a_{10^5}\approx7{,}38891$, frente a $e^2\approx7{,}38906$.
**Avisos:**
- La solución impresa de p.40 es correcta, pero no justifica el paso al límite del corchete y el exponente (Prop. 1.5 + (1.1)).
- No comprueba que $x_n-1$ tenga signo constante.
- $a_1=(-3)^{1/3}$ no está definida como potencia real de base negativa. Es irrelevante para el límite, pero conviene decir «para $n\ge2$».

---

## 6. Límite con parámetro: $(\cos a)^n$

**Fuente:** `X p.150` (Febrero 2019, 1ª semana, Ingeniería Electrónica Industrial y Automática, pregunta corta 1, 1 punto).

**Enunciado.** Calcule en función de $a\in\mathbb R$ el límite $\displaystyle\lim_{n\to+\infty}(\cos a)^n$.

**Solución.**
1. **Reducir a un caso conocido.** Para cada $a$ fijo, $r=\cos a$ es un número fijo, que no depende de $n$, con $-1\le r\le1$. La sucesión es la geométrica $r^n$ (catálogo de límites del tema): tiende a $0$ si $|r|<1$, vale $1$ si $r=1$ y no converge si $r\le-1$.
2. **Por qué $r^n\to0$ si $|r|<1$.** Si $r=0$, todos los términos valen 0. Si $0<|r|<1$, entonces $|r|^n=e^{n\ln|r|}$ con $\ln|r|<0$, así que el exponente tiende a $-\infty$ y $|r|^n\to0$ por (1.1). Como $-|r|^n\le r^n\le|r|^n$, el emparedado da $r^n\to0$.
3. **Por qué $(-1)^n$ no converge:** vale $1,-1,1,\dots$ y es el caso B del problema 1.
4. **Traducir cada caso a valores de $a$:**
   - $\cos a=1\iff a=2k\pi$, $k\in\mathbb Z$: el límite es **1**.
   - $\cos a=-1\iff a=(2k+1)\pi$: el límite **no existe** (oscila entre $\pm1$).
   - En otro caso, $|\cos a|<1$: el límite es **0**.

**Receta:** con un parámetro, fíjalo y reconoce la sucesión-modelo ($r^n$, $n^p$…). Luego separa los casos en los que cambia el comportamiento ($|r|<1$, $r=1$, $r=-1$) y tradúcelos a condiciones sobre el parámetro.
**Parte del tema:** catálogo de límites ($r^n$), §4 (emparedado), §7 ((1.1)), receta «calcula con los parámetros como números y al final impón la condición» (Ejercicio 1.11 de E).
**Verificación:** sympy: el límite de $(1/2)^n$ es 0 y el de $1^n$ es 1. La no convergencia de $(-1)^n$ se ve por las subsucesiones par e impar.
**Avisos:** la solución impresa es correcta y está completa. Solo hay un detalle de notación: escribe $a=\pi+2k\pi=\pi(2k+1)$.

---

## Descartados (y por qué)
- X p.32 (Feb 2013, $1^\infty$, resultado $e$), p.101 ($(1+1/n^3)^{\pi n^3}=e^\pi$): mismo tipo que el problema 5.
- X p.49 ($\sqrt{16n^4-4}/(n\sqrt{4n^2+5})=2$), p.93 (resultado 2): mismo tipo que el problema 2.
- X p.139 (conjugado, sin solución impresa): mismo tipo que el problema 3. Para practicar: $\lim\left(\sqrt{n^2+2n-1}-\sqrt{n^2-4}\right)=1$ (sympy).
- X p.115 Ejercicio 4 (convergencia uniforme): pertenece a §1.5, fuera de examen.

## Tipos de pregunta del tema que caen en E y en U pero no aparecen en X
- **Criterio de Stolz** (cocientes con una suma de $n$ términos, o $\frac{\ln n}{n}$, $\sqrt[n]n$): ningún examen de X lo pide. En E están los Ejercicios 1.15-1.16.
- **Demostración con la definición $\varepsilon$-$N$** de que $\lim a_n=l$ (E 1.6, U Ej. 1.17).
- **Sucesiones monótonas y acotadas, o definidas por recurrencia** (Teorema 1.3 de U): no aparecen como problema de examen en el índice.
- **Emparedado con una suma de $n$ términos** (E 1.14): X solo trae el caso «acotada por infinitésimo» (problema 4).
