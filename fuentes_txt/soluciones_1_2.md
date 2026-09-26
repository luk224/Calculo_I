# Soluciones — Tema 1.2 Sucesiones

**Fuentes.** Ejercicios: libro **E** (*Libro de ejercicios Cálculo 24-25*, `ejercicios.txt`; página impresa = PDF). Los enunciados se han comprobado **sobre las páginas del PDF renderizadas**, no solo en el `.txt`, que pierde raíces y barras. Teoría: libro **U** (*Cálculo para Ingenieros*, `ingenieros.txt`; impresa = PDF + 2). Apoyo: **S** (Stewart §11.1) y **L** (Larson §9.1; impresa = PDF − 17). Todos los límites se han verificado con sympy 1.14. En 1.11, 1.16 y en los ejemplos propios con sumas se han hecho además comprobaciones numéricas con mpmath.

## 0. Alcance y notas de verificación

**Ejercicios de E de §1.2:** del 1.6 al 1.16 (E pp. 10-20). El 1.6 empieza al final de la p. 10 y el 1.16 ocupa las pp. 19-20. El 1.17 (p. 20) ya trata de series.

**§1.2 de U ocupa las pp. 22-33, no las 22-30.** Las pp. 31-33 siguen siendo §1.2: monotonía (Def. 1.13), Teorema 1.3, **Proposición 1.5** (el número $e$), **Criterio de Stolz** y Ejemplo 1.30. §1.3 «Series» empieza a mitad de la p. 33. **Hay que corregir CLAUDE.md**, que dice «1.2 (p. 22-30)» y «1.3 Series (p. 31-41)». Los ejercicios 1.13, 1.15 y 1.16 necesitan precisamente esas páginas.

**Mapa de U §1.2 (verificado en el texto):**

| Contenido | U, pág. impresa |
|---|---|
| Def. 1.9 (sucesión $a:\mathbb N\to\mathbb R$), Ejemplos 1.14-1.15 | 22 |
| Término general, notación $\{a_n\}$; Def. 1.10 (límite: $\lvert a_n-l\rvert\le\varepsilon$ para $n\ge N$); Ejemplo 1.16 | 23 |
| Ejemplo 1.17 ($1/n\to0$ por la definición); unicidad del límite; Def. 1.11 (sucesión acotada); Prop. 1.1 (convergente ⇒ acotada); $\{(-1)^n\}$ | 24 |
| **Regla del emparedado**; Ejemplo 1.18; **Teorema 1.2** (tiende a 0 × acotada → 0); Ejemplo 1.19; Prop. 1.2 ($\lvert a_n\rvert\to\lvert l\rvert$) | 25 |
| Ejemplo 1.20; **Prop. 1.3** (límite de suma, producto y cociente) | 26 |
| Ejemplo 1.21 y observación «dividir entre el monomio de mayor grado del denominador»; **Def. 1.12** (recta ampliada $\overline{\mathbb R}$ y cómo operar con $\pm\infty$) | 26-27 |
| Límite infinito (definición); Ejemplos 1.22-1.23; **Prop. 1.4** (el emparedado y las Props. 1.2-1.3 siguen valiendo con límites $\pm\infty$) | 28 |
| Indeterminaciones $\frac00,\ \infty-\infty,\ \pm\infty\cdot0,\ \frac{\pm\infty}{\pm\infty}$; Ejemplo 1.24 y nota al margen **«multiplicar por el conjugado»**; **fórmula (1.1)** $\lim a_n^{b_n}=e^{\lim b_n\ln a_n}$; **intercambiar el límite con una función continua** (polinómicas, trigonométricas, exponenciales, logarítmicas) | 29 |
| Ejemplos 1.25-1.26; lista de las **7 indeterminaciones** (se añaden $0^0,\ 1^{\pm\infty},\ \infty^0$) | 30 |
| Def. 1.13 (monotonía); Ejemplos 1.27-1.28; Teorema 1.3 (si es monótona: convergente ⇔ acotada); **Prop. 1.5**: $\left(1+\frac1{a_n}\right)^{a_n}\to e$ si $a_n\to\pm\infty$ | 31 |
| Ejemplo 1.29; **Criterio de Stolz**; Ejemplo 1.30 | 32-33 |

**Símbolos perdidos al extraer el texto (no son erratas de los libros):** en la Prop. 1.3 de U (p. 26), el `.txt` dice «$b_n = 0$ para todo $n$ y $\lim b_n = 0$»; hay que leer $b_n\neq0$ y $\lim b_n\neq0$. En E, el `.txt` rompe todas las raíces de los ejercicios 1.7, 1.9, 1.10, 1.11, 1.12 y 1.15. Los enunciados de este documento se han copiado de la imagen del PDF.

**Orden didáctico propuesto** (de fácil a difícil, conservando la numeración): 1.6 (concepto) → 1.8, 1.7, 1.9 (cocientes: sacar factor común lo que domina) → 1.10, 1.12 (conjugado para $\infty-\infty$) → 1.14 (potencia que no es indeterminación) → 1.13 ($1^\infty$) → 1.11 (emparedado) → 1.15, 1.16 (Stolz).

---

## Ejercicio 1.6 (E pp. 10-11) — concepto

> **Enunciado (E, Ej. 1.6, p. 10).** La sucesión $\{x_n\}$ es convergente y la sucesión $\{y_n\}$ es divergente. Razone si puede ser convergente la sucesión $\{x_ny_n\}$.

**Solución.**

1. **Qué se pregunta.** «¿Puede ser…?» es una pregunta de **existencia**: basta con **un ejemplo**. No hace falta demostrar que ocurra siempre (y no ocurre siempre; ver el paso 5).
2. **Qué significa «divergente».** U no lo define. Solo dice (p. 28) que las sucesiones con límite $\pm\infty$ «no son convergentes». Lo habitual (S p. 692, L p. 585) es: **divergente = no convergente**, ya sea porque tiende a $\pm\infty$ o porque oscila, como $(-1)^n$ (U p. 24). El ejemplo que sigue vale con cualquiera de los dos sentidos.
3. **Elegimos la divergente** $y_n=n$. Su límite es $+\infty$ (U p. 28: «es sencillo probar que $\lim n=\infty$»), así que no es convergente.
4. **Elegimos la convergente** $x_n=\frac1{n^2}\to0$ (U Ejemplo 1.18, p. 25). Entonces $x_ny_n=\frac{n}{n^2}=\frac1n\to0$ (U Ejemplo 1.17, p. 24). **Por tanto, sí puede ser convergente.** Otro ejemplo: con $x_n=\frac1n$ sale $x_ny_n=1$, una sucesión constante y convergente (U Ejemplo 1.16, p. 23).
5. **El factor convergente tiene que tender a 0 (E no lo dice).** Supongamos $x_n\to l\neq0$ y $x_ny_n\to m$. A partir de cierto $n$ se tiene $x_n\neq0$ (aplica la Def. 1.10 con $\varepsilon=\lvert l\rvert/2$). Entonces $y_n=\dfrac{x_ny_n}{x_n}\to\dfrac ml$ por la Prop. 1.3 (U p. 26). Solo importa el final de la sucesión (U p. 23: «no nos importa lo que pasa al principio»). Esto es **absurdo**, porque $\{y_n\}$ diverge. Conclusión: **si $\{x_ny_n\}$ converge, necesariamente $x_n\to0$.**

**Receta.** Si te preguntan «¿puede ocurrir…?», construye un ejemplo con las sucesiones más sencillas ($n$, $1/n$, $1/n^2$, $(-1)^n$). Si te preguntan «¿ocurre siempre?», busca un contraejemplo o razona por reducción al absurdo con la Prop. 1.3.
**Error típico.** Responder «nunca» (porque la divergente lo estropea todo) o «siempre». Otro error es aplicar la Prop. 1.3 como $\lim x_n\cdot\lim y_n$ cuando $\lim y_n$ no existe: la proposición exige que **existan** los dos límites.
**Teoría:** U Def. 1.10 p. 23; Ejemplos 1.16-1.18 pp. 23-25; Prop. 1.3 p. 26; límite infinito p. 28. Para «divergente»: S §11.1 p. 692, L §9.1 p. 585.

---

## Ejercicio 1.8 (E p. 12) — cociente con exponenciales

> **Enunciado (E, Ej. 1.8, p. 12).** Sea la sucesión dada, para $n\in\mathbb N$, por $$x_n=\frac{e^{\,n+\frac3n}+5}{2e^n}.$$ Se pide calcular su límite cuando $n$ tiende a $+\infty$.

**Solución.**

1. **Sustituimos primero.** Numerador y denominador tienden a $+\infty$: $e^{\infty}=\infty$ porque $e>1$ (Def. 1.12, U p. 27). Sale $\frac{\infty}{\infty}$, que es una **indeterminación** (U p. 29), así que no podemos aplicar la Prop. 1.3 directamente.
2. **Separamos lo que domina.** Por las propiedades de las potencias, $e^{n+3/n}=e^n\,e^{3/n}$. Entonces $$x_n=\frac{e^ne^{3/n}}{2e^n}+\frac{5}{2e^n}=\frac{e^{3/n}}2+\frac5{2e^n}.$$ Es la misma idea que dividir entre el término de mayor grado (U p. 27), pero aquí lo que domina es $e^n$.
3. **Primer sumando.** $\frac3n\to0$ (Prop. 1.3 y Ejemplo 1.17). Como la exponencial es continua (U p. 29), $e^{3/n}\to e^0=1$. El primer sumando tiende a $\frac12$.
4. **Segundo sumando.** $2e^n\to\infty$ y $\frac{5}{\infty}=0$ (Def. 1.12 y Prop. 1.4, U pp. 27-28).
5. **Sumamos** (Prop. 1.3): $\lim x_n=\frac12+0=\boxed{\tfrac12}$. Verificado con sympy.

**Receta.** Ante un cociente $\frac\infty\infty$, divide numerador y denominador entre lo que crece más deprisa (una potencia de $n$, $e^n$…) y después aplica la Prop. 1.3.
**Error típico.** Escribir $e^{n+3/n}=e^n+e^{3/n}$. La exponencial convierte **sumas en productos**, no en sumas.
**Teoría:** U Prop. 1.3 p. 26; Def. 1.12 p. 27; Prop. 1.4 p. 28; continuidad de la exponencial p. 29.

---

## Ejercicio 1.7 (E pp. 11-12) — cociente con raíz

> **Enunciado (E, Ej. 1.7, p. 11).** Sea $\{a_n\}$ la sucesión cuyo término general es $$a_n=\frac{n}{\sqrt{n^3+4}}.$$ ¿Es convergente?

**Solución.**

1. Al sustituir sale $\frac{+\infty}{+\infty}$, que es una indeterminación (U p. 29).
2. **Intuición.** Dentro de la raíz domina $n^3$, así que $\sqrt{n^3+4}\approx n^{3/2}$ y $a_n\approx\frac{n}{n^{3/2}}=\frac1{\sqrt n}\to0$. Ahora hay que demostrarlo.
3. **Sacamos factor común dentro de la raíz.** $n^3+4=n^3\left(1+\frac4{n^3}\right)$. Como $\sqrt{pq}=\sqrt p\sqrt q$ para $p,q\ge0$, se tiene $\sqrt{n^3+4}=n^{3/2}\sqrt{1+4/n^3}$, y por tanto $$a_n=\frac{n}{n^{3/2}\sqrt{1+4/n^3}}=\frac1{n^{1/2}\sqrt{1+4/n^3}}.$$
4. **Estudiamos cada factor del denominador.**
   - $\sqrt n\to+\infty$ por la definición de límite infinito (U p. 28): dado $k>0$, si $n\ge k^2$ entonces $\sqrt n\ge k$.
   - $1+\frac4{n^3}\to1$ y, por continuidad de la raíz, $\sqrt{1+4/n^3}\to1$. **Hueco de U:** su lista de funciones continuas (p. 29) no incluye las raíces. Se cubre escribiendo $\sqrt x=e^{\frac12\ln x}$ para $x>0$, o con la «ley de la potencia» de S p. 693.
5. **Conclusión.** El denominador tiende a $+\infty\cdot1=+\infty$ (Def. 1.12 y Prop. 1.4), y el cociente a $\frac1{+\infty}=0$. **La sucesión es convergente y $\lim a_n=0$.** Verificado con sympy.
6. **Otra vía, más corta: el emparedado (U p. 25).** $0\le\frac n{\sqrt{n^3+4}}\le\frac n{\sqrt{n^3}}=\frac1{\sqrt n}\to0$.

**Receta.** Si aparece la raíz de un polinomio, saca factor común dentro de la raíz la **mayor potencia** del radicando, pásala fuera con exponente $\tfrac12$ y compara los exponentes de arriba y abajo.
**Error típico.** Escribir $\sqrt{n^3+4}=\sqrt{n^3}+2$. La raíz no se reparte sobre una suma.
**Teoría:** U Def. 1.12 p. 27; límite infinito y Prop. 1.4 p. 28; continuidad p. 29; emparedado p. 25. Para la raíz, S §11.1 p. 693.

---

## Ejercicio 1.9 (E pp. 12-13) — cociente con dos raíces

> **Enunciado (E, Ej. 1.9, p. 12).** Sea $\{a_n\}$ la sucesión de término general $$a_n=\frac{\sqrt{16n^4-4}}{n\sqrt{4n^2+5}}.$$ Se pide calcular su límite cuando $n$ tiende a infinito.

**Solución.**

1. Al sustituir sale $\frac{+\infty}{+\infty}$, que es una indeterminación.
2. **Intuición.** Arriba domina $\sqrt{16n^4}=4n^2$; abajo, $n\sqrt{4n^2}=2n^2$. Esperamos que el límite sea $\frac{4n^2}{2n^2}=2$.
3. **Sacamos factor común en cada radicando** (su mayor potencia): $$\sqrt{16n^4-4}=n^2\sqrt{16-\tfrac4{n^4}},\qquad n\sqrt{4n^2+5}=n\cdot n\sqrt{4+\tfrac5{n^2}}=n^2\sqrt{4+\tfrac5{n^2}}.$$ Aquí usamos $\sqrt{n^4}=n^2$ y $\sqrt{n^2}=n$, que son ciertas porque $n>0$.
4. **Simplificamos $n^2$:** $a_n=\dfrac{\sqrt{16-4/n^4}}{\sqrt{4+5/n^2}}$.
5. **Límite.** Como $\frac4{n^4}\to0$ y $\frac5{n^2}\to0$, por continuidad de la raíz el numerador tiende a $\sqrt{16}=4$ y el denominador a $\sqrt4=2\neq0$. Por la Prop. 1.3 (cociente), $\lim a_n=\boxed{2}$. Verificado con sympy.

**Receta.** La misma que en el 1.7. Antes de operar, identifica el término que manda arriba y abajo: te anticipa el resultado y sirve para comprobarlo.
**Error típico.** Escribir $\sqrt{16n^4-4}=4n^2-2$.
**Teoría:** U Prop. 1.3 p. 26; observación p. 27; continuidad p. 29 (raíz: S p. 693).

---

## Ejercicio 1.10 (E pp. 13-14) — conjugado para $\infty-\infty$

> **Enunciado (E, Ej. 1.10, p. 13).** Se pide calcular el siguiente límite: $$\lim_{n\to+\infty}\left(\sqrt{n^2+4n+8}-n\right).$$

**Solución.**

1. Al sustituir sale $+\infty-(+\infty)$, que es una **indeterminación** (U p. 29). Aquí no basta con mirar lo que domina: los términos dominantes ($\sqrt{n^2}=n$ y $n$) **se cancelan**, y el límite lo decide lo que queda.
2. **Multiplicamos y dividimos por el conjugado.** Es la nota al margen de U p. 29: si la indeterminación $\infty-\infty$ viene de $a_n-b_n$, conviene multiplicar y dividir por $a_n+b_n$. Usando $(A-B)(A+B)=A^2-B^2$: $$\sqrt{n^2+4n+8}-n=\frac{(n^2+4n+8)-n^2}{\sqrt{n^2+4n+8}+n}=\frac{4n+8}{\sqrt{n^2+4n+8}+n}.$$ El denominador es positivo, así que la operación es válida.
3. **Ahora es un cociente $\frac\infty\infty$.** Dividimos entre $n$, con $\sqrt{n^2+4n+8}=n\sqrt{1+\frac4n+\frac8{n^2}}$: $$\frac{4+\frac8n}{\sqrt{1+\frac4n+\frac8{n^2}}+1}\longrightarrow\frac{4}{1+1}=\boxed{2}.$$ Verificado con sympy.

**Receta.** Si tienes $\infty-\infty$ con raíces, multiplica por el **conjugado**. Después, divide el cociente entre la potencia dominante.
**Error típico.** Concluir que «$\infty-\infty=0$», o que el límite es 0 porque $\sqrt{n^2+4n+8}\approx n$. Esa aproximación pierde justo el término $4n$, que es el que da el 2.
**Teoría:** U indeterminaciones y conjugado p. 29; Prop. 1.3 p. 26.

---

## Ejercicio 1.12 (E pp. 15-16) — conjugado con parámetros

> **Enunciado (E, Ej. 1.12, p. 15).** Se pide encontrar la relación entre $a$ y $b$ para que el siguiente límite valga 2: $$\lim_{n\to+\infty}\left(\sqrt{n^2+an+1}-\sqrt{n^2+bn}\right).$$

**Solución.**

1. Es una **indeterminación** $+\infty-(+\infty)$. Para $n$ grande, los dos radicandos son positivos sean cuales sean $a$ y $b$, y el límite solo depende del final de la sucesión.
2. **Multiplicamos por el conjugado:** $$\sqrt{n^2+an+1}-\sqrt{n^2+bn}=\frac{(n^2+an+1)-(n^2+bn)}{\sqrt{n^2+an+1}+\sqrt{n^2+bn}}=\frac{(a-b)n+1}{\sqrt{n^2+an+1}+\sqrt{n^2+bn}}.$$
3. **Dividimos entre $n$:** $$\frac{(a-b)+\frac1n}{\sqrt{1+\frac an+\frac1{n^2}}+\sqrt{1+\frac bn}}\longrightarrow\frac{a-b}{1+1}=\frac{a-b}2.$$
4. **Imponemos la condición:** $\frac{a-b}2=2\iff\boxed{a-b=4}$. Hay infinitos pares que la cumplen, por ejemplo $a=5$, $b=1$. Verificado con sympy: el límite general es $\frac{a-b}{2}$, y con $(5,1)$ vale 2.

**Receta.** Calcula el límite tratando los parámetros como números y **al final** impón la condición.
**Error típico.** Equivocarse de signo al restar $(n^2+bn)$, o creer que el $+1$ del radicando influye en el resultado (no influye: al dividir entre $n$ desaparece).
**Teoría:** como en el 1.10 (U p. 29; Prop. 1.3 p. 26).

---

## Ejercicio 1.14 (E pp. 17-18) — potencia que NO es indeterminación

> **Enunciado (E, Ej. 1.14, p. 17).** Se pide calcular el límite de la sucesión de término general $$a_n=\left(\frac{n^4-n+1}{2n^4-n+2}\right)^{\frac{n^2}{n+1}}.$$

**Solución.**

1. **Estudiar la base y el exponente por separado.** Hay que hacerlo siempre, antes de lanzarse a la técnica del número $e$.
   - Base: $u_n=\dfrac{1-\frac1{n^3}+\frac1{n^4}}{2-\frac1{n^3}+\frac2{n^4}}\to\frac12$ (dividiendo entre $n^4$, U p. 27). Además $u_n>0$.
   - Exponente: $t_n=\dfrac{n^2}{n+1}=\dfrac{n}{1+1/n}\to\dfrac{+\infty}{1}=+\infty$.
2. **¿Es indeterminación?** La forma es $\left(\tfrac12\right)^{+\infty}$, que **no** está en la lista de U p. 30 ($0^0$, $1^{\pm\infty}$, $\infty^0$). La Def. 1.12 (p. 27) le asigna un valor: $x^\infty=0$ si $x\in(0,1)$.
3. **Justificación correcta, con la fórmula (1.1) (U p. 29).** Se escribe $a_n=e^{t_n\ln u_n}$. Por la continuidad del logaritmo, $\ln u_n\to\ln\frac12<0$. Por la Prop. 1.4 y la Def. 1.12, $t_n\ln u_n\to(+\infty)\cdot(\ln\tfrac12)=-\infty$. Por último, $e^{-\infty}=0$, como usa el propio U en el Ejemplo 1.26 (p. 30). Por tanto $\lim a_n=\boxed0$.
4. **Comprobación elemental por emparedado** (opcional, pero muy sólida). Primero, $u_n\le\frac35\iff 5(n^4-n+1)\le3(2n^4-n+2)\iff0\le n^4+2n+1$, y esto último es siempre cierto. Segundo, $t_n=\frac{n^2}{n+1}\ge n-1$, porque $n^2\ge n^2-1$. Como la base está en $(0,1)$, un exponente mayor da un valor menor, así que $0<a_n\le\left(\frac35\right)^{n-1}\to0$. Verificado con sympy.

**Nota sobre E.** E escribe $\lim(\text{base})^{\lim(\text{exponente})}$: mete el límite en el exponente dejando la base con $n$. Ningún resultado del libro justifica ese paso tal como está escrito. El resultado es correcto, pero la forma rigurosa es la del paso 3.
**Receta.** Ante $u_n^{t_n}$, calcula por separado $\lim u_n$ y $\lim t_n$. Solo necesitas una técnica especial si sale $1^{\pm\infty}$, $0^0$ o $\infty^0$. En otro caso basta con (1.1) y las reglas de $\overline{\mathbb R}$.
**Error típico.** Aplicar mecánicamente la técnica del número $e$ (como en el 1.13) a algo que no es $1^\infty$.
**Teoría:** U Def. 1.12 p. 27; Prop. 1.4 p. 28; fórmula (1.1) y continuidad p. 29; Ejemplo 1.26 y lista de indeterminaciones p. 30; emparedado p. 25.

---

## Ejercicio 1.13 (E pp. 16-17) — indeterminación $1^\infty$

> **Enunciado (E, Ej. 1.13, p. 16).** Se pide calcular, si existe, el siguiente límite $$\lim_{n\to+\infty}\left(\frac{5n+2}{5n+3}\right)^{3n+1}.$$

**Solución.**

1. **Clasificar.** La base tiende a 1 (se ve dividiendo entre $n$) y el exponente a $+\infty$. La forma es $1^{+\infty}$, que es **indeterminada** (U p. 30).
2. **Herramienta: la Prop. 1.5** (U p. 31). Si $a_n\to\pm\infty$, entonces $\left(1+\frac1{a_n}\right)^{a_n}\to e$. Para usarla hay que escribir la base como $1+\frac1{a_n}$.
3. **La base en esa forma:** $$\frac{5n+2}{5n+3}=\frac{(5n+3)-1}{5n+3}=1-\frac1{5n+3}=1+\frac1{a_n},\qquad a_n=-(5n+3)\to-\infty.$$
4. **Hacer que el exponente sea $a_n$.** Multiplicamos y dividimos el exponente por $a_n$: $$\left(1+\tfrac1{a_n}\right)^{3n+1}=\left[\left(1+\tfrac1{a_n}\right)^{a_n}\right]^{s_n},\qquad s_n=\frac{3n+1}{a_n}=-\frac{3n+1}{5n+3}\to-\frac35.$$
5. **Paso al límite con (1.1) (U p. 29).** Si $w_n\to e$ y $s_n\to s$ (finito), entonces $w_n^{s_n}=e^{s_n\ln w_n}\to e^{s\cdot\ln e}=e^s$. Esto se debe a la Prop. 1.3 y a la continuidad de $\ln$ y de $\exp$, y es lo que justifica el paso «$(\lim)^{\lim}$» que hace E. Por tanto $$\lim\left(\frac{5n+2}{5n+3}\right)^{3n+1}=\boxed{e^{-3/5}}.$$ Verificado con sympy.

**Receta para $1^{\pm\infty}$.** Si $x_n\to1$ e $y_n\to\pm\infty$, entonces $\lim x_n^{y_n}=e^{\lim y_n(x_n-1)}$, siempre que este último límite exista. Se deduce con los mismos pasos 3-5, tomando $a_n=\frac1{x_n-1}$. Comprobación en este ejercicio: $(3n+1)\left(-\frac1{5n+3}\right)\to-\frac35$. ✓
**Error típico.** Decir «$1^\infty=1$». O aplicar la Prop. 1.5 sin conseguir que la base sea exactamente $1+\frac1{a_n}$ con **el mismo** $a_n$ en el exponente.
**Teoría:** U lista de indeterminaciones p. 30; Prop. 1.5 p. 31; Ejemplo 1.29 p. 32; fórmula (1.1) p. 29. Para $(1+1/n)^n\to e$: L §9.1 p. 585 (Ejemplo 2).

---

## Ejercicio 1.11 (E pp. 14-15) — regla del emparedado

> **Enunciado (E, Ej. 1.11, p. 14).** Sea $\{b_n\}$ la sucesión dada por la expresión: $$b_n=\frac1{\sqrt{n^2+1}}+\frac1{\sqrt{n^2+2}}+\cdots+\frac1{\sqrt{n^2+n}}.$$ ¿Cuál es su límite, cuando $n$ tiende a infinito?

**Solución.**

1. **Por qué no sirve «límite de la suma = suma de los límites».** La Prop. 1.3 (U p. 26) vale para un número **fijo** de sumandos. Aquí hay $n$ sumandos, que crecen con $n$: cada uno tiende a 0, pero cada vez hay más. E lo describe como «equivalente a $0\cdot(+\infty)$», que es una analogía, no una igualdad.
2. **Comparar cada sumando.** Para $1\le k\le n$ se tiene $n^2+1\le n^2+k\le n^2+n$. Como la raíz es creciente y $x\mapsto1/x$ es decreciente en $(0,\infty)$: $$\frac1{\sqrt{n^2+n}}\le\frac1{\sqrt{n^2+k}}\le\frac1{\sqrt{n^2+1}}.$$ Este es el paso que E da por «evidente».
3. **Sumar las $n$ desigualdades** ($k=1,\dots,n$). Quedan $n$ copias de la cota menor y $n$ copias de la mayor: $$a_n:=\frac n{\sqrt{n^2+n}}\le b_n\le\frac n{\sqrt{n^2+1}}=:c_n.$$
4. **Límites de los «panes».** Se divide entre $n$ usando $\sqrt{n^2+\dots}=n\sqrt{1+\dots}$: $a_n=\frac1{\sqrt{1+1/n}}\to1$ y $c_n=\frac1{\sqrt{1+1/n^2}}\to1$.
5. **Regla del emparedado (U p. 25):** $\lim b_n=\boxed1$. Comprobación numérica: $b_{10}\approx0{,}9739$, $b_{100}\approx0{,}99749$, $b_{10^4}\approx0{,}999975$, siempre entre $a_n$ y $c_n$.

**Receta.** Si tienes una suma de $n$ términos parecidos, acota **cada** término por el menor y por el mayor de ellos, multiplica por el número de términos y aplica el emparedado.
**Error típico.** Sumar los límites de los sumandos ($0+0+\dots=0$) y concluir que el límite es 0.
**Teoría:** U, regla del emparedado p. 25 («jamón y panes»); Prop. 1.3 p. 26. Versión «a partir de un $N$»: S p. 694; L Teorema 9.3, p. 587.

---

## Ejercicio 1.15 (E pp. 18-19) — $\sqrt[n]{n}$ con el criterio de Stolz

> **Enunciado (E, Ej. 1.15, p. 18).** Se pide calcular el límite de la sucesión de término general $$a_n=\sqrt[n]{n}.$$

**Solución.**

1. **Clasificar.** $\sqrt[n]n=n^{1/n}$: la base tiende a $+\infty$ y el exponente a 0. Es la forma $\infty^0$, que es indeterminada (U p. 30).
2. **Fórmula (1.1) (U p. 29):** $n^{1/n}=e^{\frac1n\ln n}$. Si calculamos $L=\lim\frac{\ln n}n$, el límite pedido será $e^L$, por la continuidad de la exponencial.
3. **$\frac{\ln n}{n}$ es de la forma $\frac{\infty}{\infty}$.** Aplicamos el **criterio de Stolz** (U p. 32) con $a_n=\ln n$ y $b_n=n$.
   - Hipótesis: $\{b_n\}$ es monótona (estrictamente creciente, con $b_{n+1}-b_n=1\neq0$) y $b_n\to\infty$. ✓
   - $\dfrac{a_{n+1}-a_n}{b_{n+1}-b_n}=\ln(n+1)-\ln n=\ln\dfrac{n+1}{n}=\ln\left(1+\tfrac1n\right)\to\ln1=0$, por la continuidad del logaritmo en 1.
   - Por Stolz, $\lim\frac{\ln n}n=0$.
4. **Conclusión:** $\lim\sqrt[n]n=e^0=\boxed1$. Verificado con sympy.

**Errata de E (p. 18).** Donde dice «de la igualdad $e^a=e^{\ln a^b}=e^{b\ln a}$» debe decir **$a^b=e^{\ln a^b}=e^{b\ln a}$** (con $a>0$). Además, la nota al margen enuncia Stolz con $l\in\overline{\mathbb R}$, mientras que U (p. 32) lo enuncia solo para $l\in\mathbb R$. La versión con $l=\pm\infty$ es cierta cuando $b_n$ es estrictamente monótona y tiende a $\pm\infty$, pero no está en U. Aquí $l=0$, así que no afecta al resultado.
**Receta.** Ante $\infty^0$, $0^0$ o $1^\infty$, pasa a $e^{\,b_n\ln a_n}$ con (1.1) y calcula el límite del exponente. Si el exponente es un cociente $\frac\infty\infty$ con sumas o logaritmos, prueba con **Stolz**.
**Error típico.** Afirmar «$\infty^0=1$» sin más, o escribir «$n^{1/n}\to n^0=1$», es decir, sustituir solo en el exponente.
**Teoría:** U (1.1) p. 29; indeterminaciones p. 30; Stolz p. 32. S calcula $\frac{\ln n}n$ con la regla de l’Hôpital (S Ejemplo 6, p. 694), que es materia del tema 2: sirve solo como contraste.

---

## Ejercicio 1.16 (E pp. 19-20) — Stolz con una suma de $n$ términos

> **Enunciado (E, Ej. 1.16, p. 19).** Se pide calcular, si existe, el siguiente límite: $$\lim_{n\to+\infty}\frac1{n^2}\left(\frac21+\frac{3^2}2+\frac{4^3}{3^2}+\cdots+\frac{(n+1)^n}{n^{n-1}}\right).$$

**Solución.**

1. **Término $k$-ésimo de la suma:** $\frac{(k+1)^k}{k^{k-1}}$. Comprobación: para $k=1$ da $\frac21$, para $k=2$ da $\frac{3^2}{2}$ y para $k=3$ da $\frac{4^3}{3^2}$. ✓
2. **Escribirlo como cociente:** $s_n=\dfrac{A_n}{B_n}$, con $A_n=\displaystyle\sum_{k=1}^n\frac{(k+1)^k}{k^{k-1}}$ y $B_n=n^2$. Cada sumando es $\ge1$, así que $A_n\ge n\to\infty$ y la forma es $\frac\infty\infty$. El emparedado del 1.11 no funciona bien aquí, porque los sumandos son muy distintos entre sí.
3. **Por qué Stolz.** Al restar dos términos consecutivos, **la suma desaparece** y queda solo el último sumando: $A_{n+1}-A_n=\dfrac{(n+2)^{n+1}}{(n+1)^n}$. Hipótesis: $B_n=n^2$ es monótona creciente, $B_n\to\infty$ y $B_{n+1}-B_n=2n+1\neq0$. ✓
4. **Cociente de Stolz** (en la forma de U, con $n+1$ y $n$): $$\frac{A_{n+1}-A_n}{B_{n+1}-B_n}=\frac{(n+2)^{n+1}}{(2n+1)(n+1)^n}=\frac{n+2}{2n+1}\cdot\left(\frac{n+2}{n+1}\right)^{n}.$$
5. **Primer factor:** $\frac{n+2}{2n+1}=\frac{1+2/n}{2+1/n}\to\frac12$.
6. **Segundo factor** (forma $1^\infty$). Con $m=n+1$: $\left(\frac{n+2}{n+1}\right)^n=\left(1+\frac1m\right)^{m-1}=\dfrac{\left(1+\frac1m\right)^m}{1+\frac1m}\to\dfrac e1=e$, por la Prop. 1.5 con $a_m=m$ (U p. 31) y la Prop. 1.3.
7. **Conclusión** (Stolz, U p. 32): $\lim s_n=\frac12\cdot e=\boxed{\dfrac e2}\approx1{,}35914$. Verificado con sympy (el cociente de Stolz tiende a $e/2$) y numéricamente: $s_{100}\approx1{,}35967$, $s_{1000}\approx1{,}359149$, $s_{5000}\approx1{,}3591413$.

**Sobre el desarrollo de E.** E usa $\frac{a_n-a_{n-1}}{b_n-b_{n-1}}$ en lugar de $\frac{a_{n+1}-a_n}{b_{n+1}-b_n}$. Es la misma sucesión desplazada un lugar y tiene el mismo límite; lo indica la nota al margen de E p. 20. Hay dos erratas menores: «$n\to++\infty$» (p. 19) y, en la p. 20, «límite de una serie de números racionales», cuando lo que se obtiene es $\frac e2$ como límite de una **sucesión** de racionales ($s_n$ contiene una suma finita, no es una serie).
**Receta.** Si el numerador (o el denominador) de un cociente es una **suma de $n$ términos**, usa Stolz: al restar términos consecutivos, la suma se reduce a su último sumando.
**Error típico.** No comprobar la hipótesis de Stolz sobre el denominador (monótono y con límite $\pm\infty$, o numerador y denominador con límite 0). O calcular $B_{n+1}-B_n$ como $1$ en lugar de $2n+1$.
**Teoría:** U, criterio de Stolz y Ejemplo 1.30, pp. 32-33; Prop. 1.5 p. 31; Prop. 1.3 p. 26.

---

## Ejemplos propios (dificultad creciente, agrupados por técnica)

Todos verificados con sympy (y numéricamente los que tienen sumas).

### A. Cocientes («lo que domina»)
- **P1 (propio, fácil).** $\lim\frac{3n^2-n+2}{5n^2+4}$. Dividimos entre $n^2$: $\frac{3-1/n+2/n^2}{5+4/n^2}\to\frac35$.
- **P2 (propio, media).** $\lim\frac{\sqrt{9n^2+n}}{2n+1}$. Como $\sqrt{9n^2+n}=n\sqrt{9+1/n}$, dividimos entre $n$: $\frac{\sqrt{9+1/n}}{2+1/n}\to\frac32$.
- **P3 (propio, difícil).** $\lim\frac{2^n+3^n}{3^{n+1}+1}$. Domina $3^n$; dividimos entre $3^n$: $\frac{(2/3)^n+1}{3+(1/3)^n}\to\frac{0+1}{3+0}=\frac13$. Se usa que $x^\infty=0$ para $x\in(0,1)$ (Def. 1.12, U p. 27).

### B. Conjugado ($\infty-\infty$)
- **P4 (propio, fácil).** $\lim(\sqrt{n^2+n}-n)=\lim\frac{n}{\sqrt{n^2+n}+n}=\lim\frac1{\sqrt{1+1/n}+1}=\frac12$.
- **P5 (propio, media).** $\lim\sqrt n\,(\sqrt{n+1}-\sqrt n)=\lim\frac{\sqrt n}{\sqrt{n+1}+\sqrt n}=\lim\frac1{\sqrt{1+1/n}+1}=\frac12$.
- **P6 (propio, difícil).** ¿Para qué $c$ se cumple $\lim(\sqrt{n^2+cn}-n)=5$? Con el conjugado queda $\frac{cn}{\sqrt{n^2+cn}+n}\to\frac c2$, así que $c=10$. De la misma forma, $\lim(\sqrt{n^2+3n}-\sqrt{n^2-n})=\frac{3-(-1)}2=2$.

### C. Emparedado y «tiende a 0 × acotada»
- **P7 (propio, fácil).** $\lim\frac{\operatorname{sen}n}{n}=0$, porque $\frac1n\to0$ y $\operatorname{sen}n$ está acotada (Teorema 1.2, U p. 25). También sale por emparedado: $-\frac1n\le\frac{\operatorname{sen}n}n\le\frac1n$.
- **P8 (propio, media).** $\lim\sum_{k=1}^n\frac{n}{n^2+k}=1$. Cada sumando está entre $\frac n{n^2+n}$ y $\frac n{n^2+1}$. Por tanto $\frac{n^2}{n^2+n}\le b_n\le\frac{n^2}{n^2+1}$, y las dos cotas tienden a 1. Numéricamente, $b_{1000}\approx0{,}9995$.
- **P9 (propio, difícil).** $\lim\sqrt[n]{2^n+3^n}=3$. Se cumple $3^n\le2^n+3^n\le2\cdot3^n$. Como $x\mapsto x^{1/n}$ es creciente, $3\le a_n\le3\cdot2^{1/n}$. Además, $2^{1/n}=e^{(\ln2)/n}\to e^0=1$ por (1.1). Por el emparedado, el límite es 3.

### D. Potencias: $1^\infty$ y casos no indeterminados
- **P10 (propio, fácil).** $\lim(1+\frac2n)^n=\lim\left[(1+\frac1{a_n})^{a_n}\right]^2$ con $a_n=\frac n2$. El límite es $e^2$ (como en el Ejemplo 1.29 de U, p. 32).
- **P11 (propio, media).** $\lim\left(\frac{n+3}{n-1}\right)^{2n}$. Como $\frac{n+3}{n-1}=1+\frac4{n-1}$, la receta del 1.13 da $2n\cdot\frac4{n-1}\to8$. El límite es $e^8$.
- **P12 (propio, media).** $\lim\left(\frac{n^2+1}{n^2-n}\right)^n$. Aquí $x_n-1=\frac{n+1}{n^2-n}$ y $n(x_n-1)=\frac{n^2+n}{n^2-n}\to1$. El límite es $e$.
- **P13 (propio, trampa).** $\lim\left(\frac{2n+1}{n+3}\right)^n=+\infty$. La base tiende a $2>1$, así que no es $1^\infty$: $x^\infty=\infty$ para $x>1$ (Def. 1.12). En cambio, $\lim\left(\frac{n+1}{3n}\right)^{\sqrt n}=0$, porque la base tiende a $\frac13\in(0,1)$.

### E. Criterio de Stolz
- **P14 (propio, fácil).** $\lim\frac{1^2+2^2+\cdots+n^2}{n^3}$. Stolz con $b_n=n^3$: $\frac{(n+1)^2}{(n+1)^3-n^3}=\frac{(n+1)^2}{3n^2+3n+1}\to\frac13$. Del mismo modo, $\frac{1+2+\cdots+n}{n^2}\to\frac12$.
- **P15 (propio, difícil).** $\lim\frac{\ln n}{\sqrt n}=0$. Stolz con $b_n=\sqrt n$, que es creciente y tiende a $\infty$: $$\frac{\ln(n+1)-\ln n}{\sqrt{n+1}-\sqrt n}=\ln\!\left(1+\tfrac1n\right)(\sqrt{n+1}+\sqrt n)=\underbrace{n\ln\!\left(1+\tfrac1n\right)}_{=\ln(1+1/n)^n\to\ln e=1}\cdot\underbrace{\frac{\sqrt{n+1}+\sqrt n}{n}}_{\to0}\to0.$$ Se usan la Prop. 1.5 y la continuidad del logaritmo.
- **P16 (propio, difícil).** $\lim\frac{1+\sqrt2+\sqrt[3]3+\cdots+\sqrt[n]n}{n}=1$. Stolz con $b_n=n$: el cociente es $\sqrt[n+1]{n+1}\to1$ por el Ejercicio 1.15. Converge despacio: vale $1{,}0248$ para $n=10^3$ y $1{,}00067$ para $n=10^5$.
- **Conceptual, sobre el 1.6 (propio).** Con $x_n=\frac1n$ e $y_n=(-1)^n$ (divergente por oscilación), $x_ny_n\to0$ por el Teorema 1.2. En cambio, con $x_n=1+\frac1n\to1\neq0$ e $y_n=n$, $x_ny_n\to+\infty$: justo lo que predice el paso 5 del 1.6.

---

## (a) Teoría necesaria (U, páginas impresas verificadas)

El redactor debe explicar lo siguiente:

1. **Def. 1.9**: sucesión, término general y notación $\{a_n\}$ (pp. 22-23).
2. **Def. 1.10**: límite en versión ε–N y sucesión convergente; Ejemplos 1.16-1.17 (pp. 23-24). La idea de que «solo importa el final» (p. 23).
3. **Unicidad del límite**, **Def. 1.11** (sucesión acotada) y **Prop. 1.1** (convergente ⇒ acotada; el recíproco falla, como muestra $(-1)^n$) (p. 24).
4. **Regla del emparedado** (Ejemplo 1.18), **Teorema 1.2** (tiende a 0 × acotada → 0; Ejemplo 1.19) y **Prop. 1.2** (p. 25).
5. **Prop. 1.3**: álgebra de límites; en el cociente se exige $b_n\neq0$ y $\lim b_n\neq0$ (p. 26). Ejemplo 1.21 y la **observación de dividir entre la mayor potencia** (pp. 26-27).
6. **Def. 1.12**: recta ampliada y aritmética con $\pm\infty$, incluidas $x^\infty$ e $\infty^x$ (p. 27).
7. **Límite infinito** (definición), Ejemplo 1.22, **Prop. 1.4** y la regla «sustituir $n$ por $\infty$» (p. 28).
8. **Indeterminaciones**, **conjugado** (Ejemplo 1.24 y nota al margen), **fórmula (1.1)** e **intercambio de límite y función continua** (p. 29).
9. Ejemplos 1.25-1.26 y **lista de las 7 indeterminaciones** (p. 30).
10. **Def. 1.13** (monotonía), Teorema 1.3 y **Prop. 1.5**: $(1+1/a_n)^{a_n}\to e$ (p. 31).
11. Ejemplo 1.29, **criterio de Stolz** y Ejemplo 1.30 (pp. 32-33).

## (b) Huecos de U y dónde suplirlos (S = Stewart §11.1; L = Larson §9.1)

| Hueco en U | Lo usan | Suplir con |
|---|---|---|
| No define **«sucesión divergente»** | 1.6 | S Def. 1, p. 692 (converge/diverge); L «Definición del límite de una sucesión», p. 585; S Ejemplo 7 ($(-1)^n$), p. 695 |
| La lista de funciones continuas (U p. 29) no incluye las **raíces**: falta justificar el límite de $\sqrt{a_n}$ | 1.7, 1.9-1.12 | S «Leyes de los límites para las sucesiones» (incluye $\lim a_n^p=(\lim a_n)^p$), p. 693; S Teorema 7 ($f$ continua), p. 695 |
| **Número $e$** como $\lim(1+1/n)^n$ (la Prop. 1.5 lo usa sin definirlo) | 1.13, 1.16 | L Ejemplo 2, p. 585 |
| **Emparedado «a partir de un $N$»** (U lo enuncia «para todo $n$») | 1.11, 1.14 | S p. 694; L Teorema 9.3, p. 587 |
| **Límite de la sucesión $a_n=f(n)$ a partir del límite de la función $f$** (conexión con límites de funciones) | 1.15 (enfoque alternativo) | S Teorema 3, p. 693; L Teorema 9.1, p. 585 |
| **$\lvert a_n\rvert\to0\Rightarrow a_n\to0$** (U solo lo sugiere, p. 26) | P7 | S Teorema 6, p. 694; L Teorema 9.4, p. 588 |
| **$\frac{\ln n}{n}\to0$** (U solo lo permite vía Stolz) | 1.15 | S Ejemplo 6, p. 694 (usa l’Hôpital, que es del tema 2: solo como contraste) |
| **$r^n$**: convergencia según el valor de $r$ | P3, P13, 1.14 | S Ejemplo 11 y resultado (9), p. 696 |
| **Monótona y acotada ⇒ convergente** (U da el Teorema 1.3 sin ejemplos de uso) | contexto | S Teorema 12, p. 698; L «Sucesiones monótonas y sucesiones acotadas», p. 590 |
| **Stolz**: U solo pide «$b_n$ monótona»; además hace falta $b_{n+1}\neq b_n$ (en la práctica, estrictamente monótona) para que el cociente exista. Ni S ni L tratan Stolz | 1.15, 1.16 | Explicación propia (marcar `propia`) |

## (c) Erratas e imprecisiones de E (pp. 10-20)

1. **1.15, p. 18 (errata):** «$e^a=e^{\ln a^b}=e^{b\ln a}$» debe ser **$a^b=e^{\ln a^b}=e^{b\ln a}$** ($a>0$).
2. **1.15, p. 18 (discrepancia con U):** la nota al margen enuncia Stolz con $l\in\overline{\mathbb R}$; U (p. 32) lo enuncia con $l\in\mathbb R$. No afecta al resultado, porque $l=0$.
3. **1.14, p. 18 (paso no justificado):** escribe $\lim(\text{base})^{\lim(\text{exponente})}$ dejando la base todavía con $n$. El resultado (0) es correcto; la justificación rigurosa es por (1.1) o por emparedado con $(3/5)^{n-1}$.
4. **1.11, pp. 14-15 (imprecisiones):** dice «equivalente a $0\cdot(+\infty)$», que es solo una analogía, y da por «evidente» $a_n\le b_n\le c_n$ sin comparar sumando a sumando.
5. **1.16, p. 19 (errata tipográfica):** «$n\to++\infty$». **1.16, p. 20 (imprecisión):** «límite de una serie de números racionales»; en realidad es una sucesión. Además aplica Stolz con los índices $(n,\,n-1)$ en vez de $(n+1,\,n)$ como en U; es equivalente.
6. **1.6, pp. 10-11:** usa «divergente» sin definirlo (U tampoco lo define) y no explica que el factor convergente debe tender a 0 (ver el paso 5 de la solución).
7. **1.7, p. 12:** mezcla «$n\to\infty$» y «$n\to+\infty$», sin consecuencias.

**Todos los resultados finales de E son correctos** (verificados con sympy): 1.7: 0; 1.8: 1/2; 1.9: 2; 1.10: 2; 1.11: 1; 1.12: $a-b=4$; 1.13: $e^{-3/5}$; 1.14: 0; 1.15: 1; 1.16: $e/2$.

**Aviso de extracción:** en `ejercicios.txt` están rotas todas las raíces (1.7, 1.9-1.12, 1.15) y desplazados los exponentes fraccionarios (1.8, 1.14). Los enunciados de este documento se han copiado del PDF renderizado.
