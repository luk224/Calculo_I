# Problemas de examen real: Tema 1.3 Series numéricas

Fuente **X** = *Exámenes resueltos de Cálculo* (`E:\UNED\CALCULO\Examenes-resueltos-Calculo.pdf`); se cita la **página PDF**. Enunciados y soluciones leídos sobre la página renderizada (PyMuPDF, 110 dpi), no sobre `examenes.txt`.
Teoría citada con página impresa de **U** (§1.3, pp. 33-41). Anclas del resumen: `#s1`…`#s7` de `temas/tema_1_3_series.html`.

**Selección.** En `indice_examenes_1..4.md` hay 6 preguntas de §1.3 (X pp. 28, 52, 106 ×2, 109, 150). Se usan las seis (todas de tipo distinto). Descartadas: X p.126 (radio de convergencia de $\sum(1+\frac1n)^{2n^2}x^n$) y X pp.46, 96, 99, 105, 112 (series de potencias: tema 3.2); X pp.38, 135, 142 (series de funciones, §1.5: fuera de examen).

Orden de dificultad: 1 (definición) → 2 (cociente) → 3 (alternada absolutamente convergente) → 4 (alternada condicionalmente convergente) → 5 (cociente que no decide) → 6 (tipo test teórico).

---

## Problema 1 — Definición de serie alternada

**Fuente:** `X p.106` (I. Electrónica Industrial y Automática, examen sin fecha [«Electrónica 4» en el índice], pregunta corta 3, 1 punto).

**Enunciado.** Defina serie alternada.

**Solución.**
1. **Definición (U Def. 1.17, p. 41):** una serie $\sum_{n=1}^\infty a_n$ es *alternada* si sus términos son alternativamente positivos (o nulos) y negativos (o nulos).
2. **Forma habitual** (para reconocerla): $a_n=(-1)^{n}b_n$ o $a_n=(-1)^{n-1}b_n$ con $b_n\ge 0$; entonces $|a_n|=b_n$. Ejemplo (U Ej. 1.40, p. 41): $\sum(-1)^n$.
3. **Para asegurar la nota conviene añadir el resultado que la hace útil, el criterio de Leibniz (U p. 41):** si $\sum a_n$ es alternada y $\{|a_n|\}$ es decreciente, entonces la serie converge **si y solo si** $\lim a_n=0$.
4. Contraejemplo de lo que *no* es alternada: $\sum \frac{\cos n}{n^2}$ (cambia de signo, pero no alternando término a término; U Ej. 1.39, pp. 40-41).

**Receta:** definición + forma $(-1)^n b_n$, $b_n\ge0$ + un ejemplo; si sobra tiempo, enunciar Leibniz.
**Parte del tema:** §6 del resumen (`#s6`), U Def. 1.17 p. 41.
**Verificación:** cotejada con el texto de U p. 41 (`ingenieros.txt`, PDF 39).
**Avisos:** la solución impresa solo dice «Vea la Definición 1.17 del texto base»; el número 1.17 es correcto.

---

## Problema 2 — $\sum n^2/4^n$ con el criterio del cociente

**Fuente:** `X p.106` (I. Electrónica Industrial y Automática, examen sin fecha [«Electrónica 4»], pregunta corta 1, 1 punto).

**Enunciado.** Estudie si la serie $\displaystyle\sum_{n=1}^{\infty}\frac{n^2}{4^n}$ es convergente.

**Solución.**
1. **Tipo de serie.** $a_n=\dfrac{n^2}{4^n}>0$ para todo $n\ge1$: es de términos positivos, así que valen comparación, cociente y raíz (U p. 38).
2. **Elección del criterio.** Aparece una potencia $4^n$, que se multiplica por $4$ al pasar de $n$ a $n+1$: al dividir $a_{n+1}/a_n$ se simplifica. Esto sugiere el **criterio del cociente** (receta del Ej. 1.20 del resumen).
3. **Cociente.**
   $$\frac{a_{n+1}}{a_n}=\frac{(n+1)^2/4^{n+1}}{n^2/4^n}=\frac{(n+1)^2}{n^2}\cdot\frac{4^n}{4^{n+1}}=\frac14\Big(1+\frac1n\Big)^2 .$$
4. **Límite.** Como $1/n\to0$, $\big(1+\frac1n\big)^2\to1$ (álgebra de límites, U §1.2), luego $\ell=\lim\frac{a_{n+1}}{a_n}=\frac14$.
5. **Conclusión.** $\ell=\frac14\in[0,1)$ ⇒ la serie **converge** (criterio del cociente, U p. 38).
6. (Comprobación alternativa) Raíz: $\sqrt[n]{a_n}=\frac{(\sqrt[n]{n})^2}{4}\to\frac14$ usando $\sqrt[n]{n}\to1$ (U Ej. 1.38, p. 39). Mismo resultado.

**Receta:** polinomio en $n$ por (o entre) $a^n$ ⇒ cociente; el polinomio aporta un factor que tiende a $1$ y el límite es $1/a$ (o $a$).
**Parte del tema:** §5 (`#s5`), criterio del cociente U p. 38.
**Verificación (sympy):** `limit(((n+1)**2/4**(n+1))/(n**2/4**n), n, oo)` = `1/4`. Además `summation(n**2/4**n,(n,1,oo))` = $20/27$ (dato extra, no pedido).
**Avisos:** ninguno; la solución impresa escribe directamente $\lim\frac{n^2+2n+1}{4n^2}=\frac14$, correcta.

---

## Problema 3 — $\sum (-1)^{n-1}/n^3$ (alternada; de hecho, absolutamente convergente)

**Fuente:** `X p.28` (Septiembre 2012, reserva, Ingeniería Mecánica, Modelo A, pregunta corta 1, 1 punto).

**Enunciado.** Demuestre que es convergente la siguiente serie: $\displaystyle\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n^3}$.

**Solución.**
1. **Signo de los términos.** $a_n=\frac{(-1)^{n-1}}{n^3}$: para $n$ impar $(-1)^{n-1}=1$ y $a_n>0$; para $n$ par $a_n<0$. Los signos alternan: es una **serie alternada** (U Def. 1.17, p. 41). No se pueden usar directamente comparación, cociente o raíz porque no es de términos positivos.
2. **Primer intento (receta del resumen: mirar antes $\sum|a_n|$).** $|a_n|=\frac1{n^3}$ y $\sum\frac1{n^\gamma}$ converge si y solo si $\gamma>1$ (U p. 38). Con $\gamma=3>1$, $\sum|a_n|$ converge: la serie es **absolutamente convergente** (U Def. 1.16, p. 40).
3. **De absoluta a convergente.** Por la Prop. 1.8 (U p. 40), toda serie absolutamente convergente es convergente. Queda demostrado.
4. **Vía del libro (Leibniz, U p. 41), también válida.** (a) es alternada (paso 1); (b) $\{|a_n|\}=\{1/n^3\}$ es decreciente porque $n<n+1\Rightarrow n^3<(n+1)^3\Rightarrow \frac1{(n+1)^3}<\frac1{n^3}$; (c) $|a_n|=\frac1{n^3}\to0$, luego $a_n\to0$. Por Leibniz, converge.

**Receta:** ante $(-1)^n$, prueba primero la convergencia absoluta con series $p$; Leibniz solo si la absoluta falla.
**Parte del tema:** §4 (series $p$) y §6 (absoluta, alternada, Leibniz): `#s4`, `#s6`.
**Verificación:** sympy da $\sum_{n\ge1}(-1)^{n-1}/n^3=\eta(3)=\tfrac34\zeta(3)\approx0{,}9015$ (finita).
**Avisos:** la solución impresa usa solo Leibniz (correcto) y no menciona que la convergencia es absoluta, resultado más fuerte y más rápido de justificar. Escribe «la sucesión $\{|a_n|\}$ es decreciente» sin justificarlo: en examen conviene añadir la línea del paso 4(b).

---

## Problema 4 — $\sum (-1)^{n-1}/\sqrt n$ (Leibniz imprescindible: convergencia condicional)

**Fuente:** `X p.150` (Febrero 2019, 1ª semana, I. Electrónica Industrial y Automática, pregunta corta 3, 1 punto).

**Enunciado.** Estudie la convergencia de la serie $\displaystyle\sum_{n=1}^{+\infty}\frac{(-1)^{n-1}}{\sqrt n}$.

**Solución.**
1. **Alternada.** $(-1)^{n-1}$ hace que los signos sean $+,-,+,-,\dots$ y $\frac1{\sqrt n}>0$: serie alternada (U Def. 1.17, p. 41) con $|a_n|=\frac1{\sqrt n}$.
2. **¿Absolutamente convergente?** $\sum|a_n|=\sum\frac1{n^{1/2}}$ es una serie $p$ con $\gamma=\frac12\le1$: **diverge** (U p. 38). Luego **no** es absolutamente convergente y la Prop. 1.8 no sirve; hay que usar Leibniz.
3. **Decrecimiento de $\{|a_n|\}$.** $n<n+1\Rightarrow\sqrt n<\sqrt{n+1}$ (la raíz es creciente) $\Rightarrow\frac1{\sqrt{n+1}}<\frac1{\sqrt n}$.
4. **Límite.** $\frac1{\sqrt n}\to0$, luego $|a_n|\to0$ y por tanto $a_n\to0$ (si $|a_n|\to0$ entonces $a_n\to0$, U §1.2).
5. **Leibniz (U p. 41).** Alternada + $\{|a_n|\}$ decreciente + $a_n\to0$ ⇒ la serie **converge**.
6. **Conclusión completa.** Converge, pero no absolutamente: es **condicionalmente convergente**.

**Receta:** alternada con $|a_n|=1/n^\gamma$: si $\gamma>1$, absolutamente convergente; si $0<\gamma\le1$, convergente solo por Leibniz (condicional).
**Parte del tema:** §4 y §6 (`#s4`, `#s6`).
**Verificación:** `limit(sqrt(n)/sqrt(n+1), n, oo)` = 1 (y el cociente $|a_{n+1}|/|a_n|=\sqrt{n/(n+1)}<1$ para cada $n$, coherente con el decrecimiento); `mpmath.nsum` da $\approx0{,}60490$ ($=(1-\sqrt2)\,\zeta(1/2)$), finita.
**Avisos (de redacción, no de resultado):** la solución impresa dice «la serie del enunciado es decreciente»; lo decreciente es la sucesión $\{|a_n|\}=\{1/\sqrt n\}$, no la serie. Tampoco comenta que la convergencia es solo condicional; si se pide «estudie la convergencia», conviene indicarlo (pasos 2 y 6).

---

## Problema 5 — $\sum\binom nk$: el cociente da $1$ y no decide

**Fuente:** `X p.52` (Septiembre 2015, Grado en Ingeniería Mecánica, código 68031029, Modelo A, pregunta corta 1, 1 punto).

**Enunciado.** Sean $k,n\in\mathbb N$, $k>1$. ¿Podemos aplicar el criterio del cociente para estudiar el carácter de la siguiente serie? ¿Nos permite decidir si es convergente? $\displaystyle\sum_{n=1}^{\infty}\binom nk$.

**Solución.**
1. **Término general.** $a_n=\binom nk=\frac{n!}{k!\,(n-k)!}$ para $n\ge k$; para $n<k$ (no se pueden elegir $k$ objetos entre $n$) es $\binom nk=0$.
2. **¿Se puede aplicar el cociente?** El criterio exige $a_n>0$ (U p. 38). Los primeros $k-1$ términos son nulos, pero **quitar un número finito de términos no cambia el carácter** de la serie: las sumas parciales de la serie recortada difieren de las originales en una constante fija, así que una converge si y solo si la otra converge. Para $n\ge k$, $a_n>0$, de modo que sí se aplica a la cola $\sum_{n\ge k}\binom nk$.
3. **Cociente.** Para $n\ge k$:
   $$\frac{a_{n+1}}{a_n}=\frac{(n+1)!}{k!\,(n+1-k)!}\cdot\frac{k!\,(n-k)!}{n!}=\frac{(n+1)\,n!}{n!}\cdot\frac{(n-k)!}{(n+1-k)\,(n-k)!}=\frac{n+1}{n+1-k}.$$
4. **Límite.** $\frac{n+1}{n+1-k}=\frac{1+1/n}{1+(1-k)/n}\to1$. Con $\ell=1$ **el criterio no decide** (U p. 38). Respuesta a las dos preguntas: sí se puede aplicar, pero no permite decidir.
5. **Decidir por otra vía (no lo pide el enunciado, pero cierra el problema).** Para $n\ge k$, $\binom nk$ es un número natural no nulo, luego $\binom nk\ge1$. Así $a_n\not\to0$ y, por la **condición necesaria** (U Prop. 1.6, p. 36), la serie **diverge**. Equivalentemente, por comparación (U p. 38) con $\sum 1$, que diverge.

**Receta:** si el cociente (o la raíz) da $\ell=1$, mira primero si $a_n\to0$: si no, diverge por la condición necesaria; si sí, compara con una serie $p$.
**Parte del tema:** §3 (condición necesaria) y §5 (cociente, caso $\ell=1$): `#s3`, `#s5`.
**Verificación (sympy):** `combsimp(binomial(n+1,k)/binomial(n,k))` para $k=2,3,5$ da $\frac{n+1}{n-1},\frac{n+1}{n-2},\frac{n+1}{n-4}$, es decir $\frac{n+1}{n+1-k}$, con límite $1$; primeros valores de $\binom n2$: $0,1,3,6,10,\dots$ (no tienden a 0).
**Avisos:** (a) la solución impresa afirma que «la serie es de términos positivos», pero $a_n=0$ para $n<k$ (solo es de términos **no negativos**); hay que justificar el recorte del paso 2. (b) Responde «no nos dice si converge o diverge» y se para: es lo pedido, pero el alumno debe saber que la serie **diverge** (paso 5), pregunta típica de seguimiento.

---

## Problema 6 — Tipo test: si $\sum a_n$ converge ($a_n>0$), ¿qué otra serie converge?

**Fuente:** `X p.109` («Examen 1 elaborado con exámenes de asignaturas similares a Cálculo de la Ingeniería Superior y de la Ingeniería Técnica», ejercicio 1, tipo test; sin puntuación indicada).

**Enunciado.** Sea $\displaystyle\sum_{n=1}^{\infty}a_n$ una serie convergente de términos positivos. Señale la opción válida:
**A)** $\sum e^{a_n}$ converge; **B)** $\sum\frac1{a_n}$ converge; **C)** $\sum a_n^2$ converge; **D)** $\sum\sqrt{a_n}$ converge.

**Solución.**
1. **Dato clave.** $\sum a_n$ converge ⇒ $a_n\to0$ (condición necesaria, U Prop. 1.6, p. 36). Además $a_n>0$.
2. **A es falsa.** Como $a_n>0$, $e^{a_n}>e^0=1$ (la exponencial es creciente), así que $e^{a_n}\not\to0$ y $\sum e^{a_n}$ diverge por la condición necesaria.
3. **B es falsa.** $a_n\to0$ con $a_n>0$ ⇒ $\frac1{a_n}\to+\infty$ (U §1.2), luego $\frac1{a_n}\not\to0$ y la serie diverge.
4. **C es verdadera.** Por la definición de límite con $\varepsilon=1$, existe $n_0$ tal que $0<a_n<1$ para $n\ge n_0$. Multiplicando $a_n<1$ por $a_n>0$: $a_n^2<a_n$ para $n\ge n_0$. Por el **criterio de comparación** (U p. 38, que admite «a partir de $n_0$»), como $\sum a_n$ converge, $\sum a_n^2$ converge.
5. **D es falsa (contraejemplo).** $a_n=\frac1{n^2}$: $\sum\frac1{n^2}$ converge (U p. 38, suma $\pi^2/6$), pero $\sqrt{a_n}=\frac1n$ y $\sum\frac1n$ (armónica) diverge (U Ej. 1.35, p. 37).
6. **Respuesta: C.**

**Receta:** en un test «si $\sum a_n$ converge, ¿converge $\sum f(a_n)$?»: descarta con la condición necesaria lo que no tiende a 0, demuestra con comparación ($a_n<1$ a partir de un $n_0$) y refuta con series $p$ ($1/n^2$ frente a $1/n$).
**Parte del tema:** §3 (condición necesaria, armónica) y §4 (comparación, series $p$): `#s3`, `#s4`; definición de límite de U §1.2.
**Verificación (sympy):** `summation(1/n**2,(n,1,oo))` = $\pi^2/6$; `summation(1/n,(n,1,oo))` = `oo`.
**Avisos:** ninguno de resultado. Observación: para excluir A la solución impresa usa $\lim e^{a_n}=e^{\lim a_n}$ (continuidad de la exponencial, propia de §1.4); el argumento $e^{a_n}>1$ del paso 2 solo usa lo de §1.3.

---

## Tipos de pregunta del tema que caen en examen y no hay en el PDF

En X no aparece, para §1.3, ninguna pregunta de:
- **Suma de una serie geométrica o telescópica** (calcular $s_n$ y su límite; U p. 36, resumen `#s2`).
- **Criterio de la raíz** aplicado a una serie numérica (solo aparece en series de potencias, X p.126, tema 3.2).
- **Comparación por paso al límite** con una serie $p$ (p. ej. $\sum\frac{1}{n^2+3n}$ o $\sum\frac{1}{\sqrt n+n}$).
- **Alternada en la que falla o hay que trabajar el decrecimiento** de $\{|a_n|\}$ (resumen, ejemplo propio 3).
- **Linealidad / «convergente + divergente»** (U Prop. 1.7, p. 37; E 1.17).

Se recomienda cubrirlos con E 1.17-1.22 y los ejemplos propios del resumen.
