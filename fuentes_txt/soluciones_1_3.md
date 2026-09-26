# Soluciones — Tema 1.3 Series (E ej. 1.17–1.22)

Fuentes: **U** = *Cálculo para Ingenieros* (§1.3 «Series», impresa pp. 33-41; el `.txt` usa PDF = impresa − 2). **E** = Libro de ejercicios 24-25 (impresa = PDF), pp. 20-25. **S** = Stewart cap. 11. **L** = Larson cap. 9 (impresa = PDF − 17).
Enunciados comprobados sobre el PDF de E renderizado (no solo sobre el `.txt`). Todos los cálculos verificados con sympy/mpmath.

Orden de estudio propuesto (de fácil a difícil): **1.17 → 1.18 → 1.19 → 1.20 → 1.22 → 1.21**.

Notación de U: una serie $\sum a_n$ es **convergente (sumable)** si su sucesión de sumas parciales $s_n=a_1+\dots+a_n$ converge (Def. 1.15, U p.35); si no, es **divergente** (U Ej. 1.32, p.35-36). «Estudiar el carácter» = decidir si converge o diverge (U p.39, nota al margen).

---

## Ejercicio 1.17 (E p. 20-21)

> **Enunciado.** Sean $\sum_{n=1}^{+\infty} a_n$ y $\sum_{n=1}^{+\infty} b_n$ dos series de números reales que son divergentes. ¿Debe ser $\sum_{n=1}^{+\infty}(a_n+b_n)$ también divergente?

**Solución**

1. **Qué se pregunta.** Es una pregunta «¿siempre?». Para responder *no* basta **un contraejemplo**: dos series divergentes cuya suma converja.
2. **Por qué no sirve la Proposición 1.7 (U p.37).** Esa proposición dice que la suma de dos series *sumables* es sumable. Aquí las hipótesis son las contrarias (divergentes), así que no dice nada: hay que investigar.
3. **Idea.** Si los términos de una serie son los opuestos de los de la otra, se cancelan: tomamos $a_n=\dfrac1n$, $b_n=-\dfrac1n$.
4. **$\sum a_n$ diverge.** Es la serie armónica; U Ej. 1.35 (p.37) prueba que $s_{2n}>s_n+\tfrac12$, luego $\{s_n\}$ no converge. Además $\{s_n\}$ es creciente (se suman términos positivos) y, al no converger, no está acotada (Teorema 1.3, U p.31: una sucesión monótona es convergente ⇔ acotada), luego $s_n\to+\infty$.
5. **$\sum b_n$ diverge.** Sus sumas parciales son $-s_n\to-\infty$.
6. **La suma converge.** $a_n+b_n=\frac1n-\frac1n=0$ para todo $n$, así que las sumas parciales de $\sum(a_n+b_n)$ son todas $0$ y convergen a $0$: la serie es convergente con suma $0$ (Def. 1.15, U p.35).
7. **Conclusión: No**; la suma de dos series divergentes puede ser convergente.

Observación (de E, justificada): si $a_n\ge0$ y $b_n\ge0$, entonces $0\le a_n\le a_n+b_n$ y, por el criterio de comparación (U p.38: «si la menor no es convergente, la mayor tampoco»), $\sum(a_n+b_n)$ **sí** es divergente. El contraejemplo necesita signos distintos.

Otro contraejemplo igual de válido: $a_n=1$, $b_n=-1$ (ambas divergen por U Prop. 1.6, p.36, porque el término general no tiende a $0$).

**Receta.** Para refutar un «¿siempre…?» sobre series, busca el contraejemplo más simple: términos que se cancelen ($b_n=-a_n$) o series conocidas (armónica, geométrica, constante).

**Error típico.** Creer que «divergente + divergente = divergente» como si fueran «infinitos que se suman». Solo es cierto si ambas son de términos no negativos (o, en general, si ambas tienden a $+\infty$). Lo que **sí** es siempre cierto: *convergente + divergente = divergente* (ver ejemplo propio P1-d).

**Teoría:** U §1.3.2 Def. 1.15 p.35; Ej. 1.35 (armónica) p.37; Prop. 1.7 p.37; criterio de comparación p.38; Teorema 1.3 p.31. Mismo ejercicio en S §11.2 ej. 84 p.713 y L §9.2 ej. 97 p.604.

---

## Ejercicio 1.18 (E p. 21)

> **Enunciado.** Sea la serie $\sum_{n=1}^{+\infty} a_n$ de término general $a_n=\dfrac{1}{3+\cos n+n^{5/2}}$. Elige la opción u opciones correctas:
> a) Es una serie convergente pero no es absolutamente convergente. b) Es una serie absolutamente convergente. c) Es una serie divergente. d) Es una serie alternada.

**Solución**

1. **Signo de los términos.** Como $-1\le\cos n\le1$, se tiene $3+\cos n\ge2>0$; además $n^{5/2}>0$. El denominador es $>0$, luego $a_n>0$ para todo $n$.
   ⇒ **d) es falsa**: una serie alternada (Def. 1.17, U p.41) cambia de signo, y esta no.
2. **Elegir con qué comparar.** Para $n$ grande, lo que «manda» en el denominador es $n^{5/2}$ (el $3+\cos n$ está acotado entre $2$ y $4$). Así que $a_n$ se parece a $\dfrac1{n^{5/2}}$, una serie $\sum 1/n^\gamma$ con $\gamma=5/2>1$, **convergente** (U p.38).
3. **Desigualdad término a término.** Para todo $n\ge1$:
   $$3+\cos n+n^{5/2}\ \ge\ 2+n^{5/2}\ >\ n^{5/2}\quad\Longrightarrow\quad 0<a_n=\frac1{3+\cos n+n^{5/2}}<\frac1{n^{5/2}},$$
   porque al invertir números positivos la desigualdad cambia de sentido.
4. **Criterio de comparación (U p.38).** Ambas series son de términos no negativos, $a_n\le b_n=1/n^{5/2}$ y $\sum b_n$ converge ⇒ $\sum a_n$ **converge**.
5. **Convergencia absoluta.** Como $a_n>0$, $|a_n|=a_n$, así que $\sum|a_n|=\sum a_n$ converge: la serie es **absolutamente convergente** (Def. 1.16, U p.40) ⇒ **b) es correcta**.
6. **Descartar a) y c).** a) afirma que *no* es absolutamente convergente: falso por el paso 5. c) afirma que diverge: falso por el paso 4 (además, absolutamente convergente ⇒ convergente, Prop. 1.8, U p.40).
7. **Respuesta: solo b).** (Comprobación numérica: $\sum a_n\approx0{,}4948<\sum 1/n^{5/2}\approx1{,}3415$.)

**Receta.** Término general = cociente con una potencia dominante $n^\gamma$ más «ruido acotado» (senos, cosenos, constantes): acota el ruido para obtener $0\le a_n\le C/n^\gamma$ (o $\ge$) y compara con $\sum1/n^\gamma$. En series de términos positivos, *convergente = absolutamente convergente*.

**Error típico.** (i) Ver un $\cos n$ y pensar «alternada»: lo que decide es el signo de **todo** el término. (ii) Comparar en la dirección inútil: mayorar por una serie divergente o minorar por una convergente no concluye nada.

**Teoría:** U Def. 1.16 y Prop. 1.8 p.40; Def. 1.17 (alternada) p.41; criterio de comparación y serie $\sum1/n^\gamma$ p.38; ejemplo gemelo U Ej. 1.39 p.40-41 ($\sum\cos n/n^2$).

---

## Ejercicio 1.19 (E p. 22)

> **Enunciado.** Se pide estudiar el carácter de la siguiente serie: $\displaystyle\sum_{n=1}^{+\infty}\frac{1}{n^{1/2}+n^{2/3}}$.

**Solución**

1. **Tipo de serie.** Términos positivos ⇒ podemos usar comparación (U p.38).
2. **Qué potencia manda.** $\frac12<\frac23$, así que para $n$ grande $n^{2/3}$ domina a $n^{1/2}$ y $a_n\approx\dfrac1{n^{2/3}}$: serie $\sum1/n^\gamma$ con $\gamma=\tfrac23\le1$, **divergente** (U p.38). **Sospecha:** diverge. Para probarlo hay que **minorar** $a_n$ por algo divergente.
3. **Comparar potencias.** Si $n\ge1$ y $p<q$, entonces $n^p\le n^q$ (igualdad solo si $n=1$), porque $n^q/n^p=n^{q-p}\ge1$ al ser $n\ge1$ y $q-p>0$. Con $p=\tfrac12$, $q=\tfrac23$: $n^{1/2}\le n^{2/3}$.
4. **Acotar el denominador por arriba** (para acotar la fracción por abajo):
   $$n^{1/2}+n^{2/3}\le n^{2/3}+n^{2/3}=2n^{2/3}\quad\Longrightarrow\quad a_n=\frac1{n^{1/2}+n^{2/3}}\ \ge\ \frac1{2n^{2/3}}\ \ge0\qquad(n\ge1).$$
5. **La serie minorante diverge.** $\sum\frac1{2n^{2/3}}=\frac12\sum\frac1{n^{2/3}}$. Si convergiera, multiplicándola por $2$ (Prop. 1.7, U p.37) convergería $\sum1/n^{2/3}$, que diverge porque $\gamma=\tfrac23\le1$ (U p.38).
6. **Criterio de comparación (U p.38),** primera parte: si la menor $\sum\frac1{2n^{2/3}}$ no es convergente, la mayor $\sum a_n$ tampoco. **La serie es divergente** (numéricamente $s_{10^6}\approx253{,}5$, y crece como $3n^{1/3}$).

**Receta.** Suma de potencias en el denominador: quédate con la **mayor** potencia $n^{\gamma}$; si sospechas divergencia ($\gamma\le1$), sustituye las potencias pequeñas por la grande para *agrandar* el denominador ($\le k\,n^\gamma$) y obtener $a_n\ge\frac1{k\,n^\gamma}$.

**Error típico.** Acotar $a_n\le\frac1{n^{1/2}}$ (quitando $n^{2/3}$): es cierto, pero mayorar por una serie divergente **no concluye nada**. Para divergencia: $a_n\ge$ (divergente); para convergencia: $a_n\le$ (convergente).

**Teoría:** U criterio de comparación y $\sum1/n^\gamma$ p.38; Prop. 1.7 p.37.

---

## Ejercicio 1.20 (E p. 22-23)

> **Enunciado.** Para la serie con sucesión de sumas parciales $\{s_k\}$ dada por $s_k=\sum_{n=1}^k a_n$, donde $a_n=\dfrac{n^n}{1\cdot3\cdot5\cdots(2n-3)\cdot(2n-1)}$, se pide estudiar su carácter.

**Solución**

1. **Tipo de serie.** Numerador y denominador positivos ⇒ $a_n>0$. Podemos usar cociente o raíz (U p.38).
2. **Por qué el cociente.** El denominador es el producto de los impares hasta $2n-1$; al pasar de $a_n$ a $a_{n+1}$ solo se añade **un** factor, $2n+1$. En los productos «que se alargan» (factoriales, productos de impares) el cociente $a_{n+1}/a_n$ simplifica casi todo; la raíz $n$-ésima de ese producto, en cambio, es difícil.
3. **Calcular el cociente.** Llamamos $P_n=1\cdot3\cdots(2n-1)$, de modo que $P_{n+1}=P_n\,(2n+1)$:
   $$\frac{a_{n+1}}{a_n}=\frac{(n+1)^{n+1}}{P_n(2n+1)}\cdot\frac{P_n}{n^n}=\frac{(n+1)^{n+1}}{(2n+1)\,n^n}=\Big(\frac{n+1}{n}\Big)^{n}\cdot\frac{n+1}{2n+1}.$$
   (Se separa $(n+1)^{n+1}=(n+1)^n(n+1)$ para agrupar $\frac{(n+1)^n}{n^n}$.)
4. **Límite de cada factor.**
   - $\big(\frac{n+1}{n}\big)^n=\big(1+\frac1n\big)^n\to e$ (Prop. 1.5, U p.31, con la sucesión $n\to\infty$).
   - $\frac{n+1}{2n+1}=\frac{1+1/n}{2+1/n}\to\frac12$ (dividir por $n$ y Prop. 1.3, U p.26).
   Ambos límites existen y son finitos, luego el del producto es el producto (Prop. 1.3, U p.26):
   $$\lim_{n\to\infty}\frac{a_{n+1}}{a_n}=\frac e2\approx1{,}359>1.$$
5. **Criterio del cociente (U p.38):** $\ell=e/2\in(1,\infty]$ ⇒ la serie **no es convergente (diverge)**.
6. **Comprobación elemental (propia).** Para todo $n\ge1$, $(1+\frac1n)^n\ge1+n\cdot\frac1n=2$ (primeros términos del binomio, todos positivos) y $\frac{n+1}{2n+1}>\frac12$, así que $\frac{a_{n+1}}{a_n}>1$: $\{a_n\}$ es creciente y $a_n\ge a_1=1$, luego $a_n\not\to0$ y la serie diverge también por la Prop. 1.6 (U p.36). Numéricamente $a_{10}\approx15{,}3$, $a_{20}\approx328$.

**Receta.** Productos que se alargan un factor en cada paso ($n!$, $1\cdot3\cdots(2n-1)$, $a^n$, $n^n$) ⇒ **criterio del cociente**; simplifica $a_{n+1}/a_n$ antes de tomar límites y busca la forma $(1+1/n)^n\to e$.

**Error típico.** (i) Escribir $a_{n+1}$ cambiando solo el numerador y olvidar que el denominador gana el factor $2n+1$. (ii) Pensar que $\ell>1$ significa «converge a algo grande». (iii) Calcular $a_n/a_{n+1}$ (el inverso) y leer al revés la conclusión.

**Teoría:** U criterio del cociente p.38; Prop. 1.5 ($e$) p.31; Prop. 1.3 p.26; Prop. 1.6 p.36. Nota: $1\cdot3\cdots(2n-1)=\frac{(2n)!}{2^n n!}$ (verificado), útil si se quiere expresar con factoriales.

---

## Ejercicio 1.22 (E p. 24-25)

> **Enunciado.** Estudia si la siguiente serie es convergente: $\displaystyle\sum_{n=1}^{+\infty}\frac{(-1)^n e^n}{e^{2n}+1}$.

**Solución** (primero la vía de E con Leibniz; después una vía más corta que además da más información)

1. **Tipo de serie.** Escribimos el término como $(-1)^n c_n$ con $c_n=\dfrac{e^n}{e^{2n}+1}>0$. Los términos pares son positivos y los impares negativos: es **alternada** (Def. 1.17, U p.41). Comparación, cociente y raíz **no** se aplican directamente (solo valen para términos no negativos, U p.39).
2. **Criterio de Leibniz (U p.41).** Para una serie alternada con $\{|a_n|\}=\{c_n\}$ decreciente, la serie converge **si y solo si** el término general tiende a $0$. Hay que comprobar: $c_n$ decreciente y $c_n\to0$.
3. **$c_n$ es decreciente (vía de E).** Como $c_n>0$, «$c_{n+1}\le c_n$» equivale a «$c_{n+1}/c_n\le1$»:
   $$\frac{c_{n+1}}{c_n}=\frac{e^{n+1}}{e^{2n+2}+1}\cdot\frac{e^{2n}+1}{e^n}=\frac{e^{2n+1}+e}{e^{2n+2}+1}.$$
   Como el denominador es positivo:
   $$\frac{c_{n+1}}{c_n}\le1\iff e^{2n+1}+e\le e^{2n+2}+1\iff e^{2n+1}-e^{2n+2}\le1-e\iff e^{2n+1}(1-e)\le1-e.$$
   Dividimos por $1-e<0$ (**la desigualdad cambia de sentido**): $\iff e^{2n+1}\ge1$, cierto para todo $n\ge0$ porque $2n+1>0$ y $e>1$.
   *Vía más rápida (propia):* $c_n=\dfrac{e^n}{e^{2n}+1}=\dfrac1{e^n+e^{-n}}$ (dividiendo por $e^n$) y
   $(e^{n+1}+e^{-n-1})-(e^n+e^{-n})=(e-1)\,(e^n-e^{-n-1})>0$, así que el denominador crece y $c_n$ decrece.
4. **$c_n\to0$.** $e^n+e^{-n}\to\infty+0=\infty$ (U Def. 1.12 p.27 y Prop. 1.4 p.28), luego $c_n\to\frac1\infty=0$; y por tanto $(-1)^nc_n\to0$ (U p.26: si $|b_n|\to0$ entonces $b_n\to0$).
5. **Conclusión por Leibniz:** la serie **es convergente**.
6. **Más fuerte (omitido en E):** $0<c_n=\dfrac{e^n}{e^{2n}+1}<\dfrac{e^n}{e^{2n}}=\Big(\dfrac1e\Big)^n$, y $\sum(1/e)^n$ es geométrica de razón $|r|=1/e<1$, convergente (U Ej. 1.33 p.36). Por comparación (U p.38), $\sum|a_n|=\sum c_n$ converge: la serie es **absolutamente convergente**, y por la Prop. 1.8 (U p.40) convergente. Esta vía hace innecesario Leibniz.
   Valores numéricos: $\sum a_n\approx-0{,}2274$; $\sum|a_n|\approx0{,}5356<\frac1{e-1}\approx0{,}5820$.

**Receta.** Ante una serie con $(-1)^n$: **primero** estudia $\sum|a_n|$ (comparación, cociente, raíz). Si converge ⇒ absolutamente convergente y se acabó. Si no, Leibniz: comprueba que $|a_n|$ decrece (cociente $\le1$, diferencia $\le0$ o reescribiendo) y que tiende a $0$.

**Error típico.** (i) Aplicar Leibniz comprobando solo $a_n\to0$ y olvidar el decrecimiento (ver P3-b: sin él la serie puede divergir). (ii) Dividir una desigualdad por un número negativo ($1-e$) sin cambiar el sentido. (iii) Aplicar el cociente de U al término con signo: U lo enuncia para $a_n>0$.

**Teoría:** U Def. 1.17 y criterio de Leibniz p.41; Def. 1.16 y Prop. 1.8 p.40; geométrica Ej. 1.33 p.36; comparación p.38.

---

## Ejercicio 1.21 (E p. 23-24) — el más difícil

> **Enunciado (literal de E).** Estudia si la siguiente serie es convergente: $\displaystyle\sum_{n=1}^{+\infty}\frac{n^{\ln n}}{(\ln n)^n}$.
>
> **Errata:** para $n=1$, $\ln1=0$ y el término es $\frac{1^0}{0^1}=\frac10$: **no está definido**. La serie debe empezar en $n=2$. (El carácter no cambia al quitar o añadir un número finito de términos; U admite series desde $n=p$, nota al margen p.35.) Estudiamos $\sum_{n=2}^{\infty}$.

**Solución**

1. **Tipo de serie.** Para $n\ge2$, $\ln n>0$, así que $a_n=\frac{n^{\ln n}}{(\ln n)^n}>0$.
2. **Elegir criterio.** El denominador es una potencia $n$-ésima, $(\ln n)^n$: su raíz $n$-ésima es simplemente $\ln n$. El cociente $a_{n+1}/a_n$ no simplifica nada. ⇒ **criterio de la raíz** (U p.38).
3. **Raíz $n$-ésima.** Por las propiedades de las potencias:
   $$\sqrt[n]{a_n}=\frac{\big(n^{\ln n}\big)^{1/n}}{\ln n}=\frac{n^{(\ln n)/n}}{\ln n}.$$
4. **Tomar logaritmos** (convierte potencias en productos: $\ln(x^y)=y\ln x$, U p.29). Llamamos $L_n=\ln\sqrt[n]{a_n}$:
   $$L_n=\frac{\ln n}{n}\cdot\ln n-\ln(\ln n)=\frac{(\ln n)^2}{n}-\ln(\ln n).$$
   (Mejor así que como en E, que escribe $\ln A=\ln\lim(\dots)$ *suponiendo* que el límite $A$ ya existe; aquí calculamos primero $\lim L_n$ y luego volvemos.)
5. **Límite auxiliar $\frac{(\ln n)^2}{n}\to0$** (E lo deja «intuitivo» y remite a L’Hôpital, U §2.3.2 p.82; con herramientas de U §1.2 basta el **criterio de Stolz**, U p.32, con $b_n=n$ monótona y $\to\infty$):
   - (a) $\dfrac{\ln n}{n}\to0$: Stolz lleva a $\dfrac{\ln(n+1)-\ln n}{(n+1)-n}=\ln\!\big(1+\tfrac1n\big)\to\ln1=0$ (continuidad de $\ln$, U p.29).
   - (b) $\dfrac{(\ln n)^2}{n}$: Stolz lleva a
     $$(\ln(n+1))^2-(\ln n)^2=\ln\!\big(1+\tfrac1n\big)\big(\ln(n+1)+\ln n\big)=\underbrace{n\ln\!\big(1+\tfrac1n\big)}_{=\ln(1+1/n)^n\to\ln e=1}\cdot\underbrace{\frac{\ln(n+1)+\ln n}{n}}_{\to0}\to1\cdot0=0.$$
     El primer factor usa la Prop. 1.5 (U p.31) y la continuidad de $\ln$; en el segundo, $\frac{\ln n}{n}\to0$ por (a) y $\frac{\ln(n+1)}{n}=\frac{\ln(n+1)}{n+1}\cdot\frac{n+1}{n}\to0\cdot1=0$ (la sucesión de (a) desplazada un lugar).
6. **Límite de $L_n$.** $\ln(\ln n)\to+\infty$ (porque $\ln n\to\infty$ y $\ln$ es creciente y no acotada). Entonces
   $$L_n=\frac{(\ln n)^2}{n}-\ln(\ln n)\longrightarrow0-\infty=-\infty$$
   (operación válida en la recta ampliada, U Def. 1.12 p.27; no es indeterminación).
7. **Deshacer el logaritmo.** $\sqrt[n]{a_n}=e^{L_n}$ y, por la continuidad de la exponencial (fórmula (1.1), U p.29), $\sqrt[n]{a_n}\to e^{-\infty}=\frac1{e^{+\infty}}=0$.
   *(Atajo propio equivalente: $n^{(\ln n)/n}=e^{(\ln n)^2/n}\to e^0=1$, luego $\sqrt[n]{a_n}=\frac{n^{(\ln n)/n}}{\ln n}\to\frac1\infty=0$.)*
8. **Criterio de la raíz (U p.38):** $\ell=0\in[0,1)$ ⇒ la serie $\sum_{n\ge2}a_n$ **es convergente**. (Numéricamente $\sum_{n=2}^\infty a_n\approx10{,}54$; los primeros términos son grandes, $a_2\approx3{,}37$, pero caen muy rápido: $a_{20}\approx2{,}3\cdot10^{-6}$.)

**Receta.** Potencia $n$-ésima en el término general ⇒ **criterio de la raíz**. Si queda algo del tipo $x_n^{y_n}$, toma logaritmos ($y_n\ln x_n$), calcula ese límite y vuelve con la exponencial. Jerarquía útil: $(\ln n)^k \ll n^\alpha \ll a^n \ll n! \ll n^n$ ($\alpha>0$, $a>1$; demostrable con Stolz o con L’Hôpital en el Tema 2).

**Error típico.** (i) No mirar el dominio (el término $n=1$ no existe). (ii) Escribir $\ln(\lim x_n)=\lim\ln x_n$ sin saber aún que el límite existe y es positivo. (iii) Tratar $0-\infty$ como indeterminación (no lo es: vale $-\infty$). (iv) Confundir $n^{\ln n}$ con $(\ln n)^n$: $n^{\ln n}=e^{(\ln n)^2}$ crece mucho más despacio que $(\ln n)^n=e^{n\ln\ln n}$.

**Teoría:** U criterio de la raíz p.38; fórmula (1.1) y continuidad p.29; Def. 1.12 p.27; Stolz p.32; Prop. 1.5 p.31; series desde $n=p$ p.35.

---

## Ejemplos propios (dificultad creciente) — «propio»

### P1 (fácil) — término general, geométrica, telescópica y «convergente + divergente» *(propio)*

a) $\displaystyle\sum_{n\ge1}\frac{n}{2n+5}$: $\ \frac{n}{2n+5}=\frac{1}{2+5/n}\to\frac12\ne0$ ⇒ **diverge** (U Prop. 1.6 p.36, en forma contrarrecíproca).

b) $\displaystyle\sum_{n\ge1}\frac{3}{2^n}$: geométrica con primer término $\frac32$ y razón $r=\tfrac12$ ⇒ **suma $=\frac{3/2}{1-1/2}=3$** (U Ej. 1.33 y nota al margen p.36). *(Verificado.)*

c) $\displaystyle\sum_{n\ge1}\frac{1}{n(n+1)}$ (**telescópica**, no está en U): $\frac1{n(n+1)}=\frac1n-\frac1{n+1}$, luego $s_n=\big(1-\tfrac12\big)+\big(\tfrac12-\tfrac13\big)+\dots+\big(\tfrac1n-\tfrac1{n+1}\big)=1-\frac1{n+1}\to1$. **Suma $=1$.** *(Verificado.)* Para explicarla: S §11.2 Ej. 7 p.707-708; L §9.2 p.596-597.

d) Si $\sum a_n$ converge y $\sum b_n$ diverge, entonces $\sum(a_n+b_n)$ **diverge**. *Prueba:* si convergiera, por U Prop. 1.7 (p.37) convergería $\sum\big[(a_n+b_n)+(-1)a_n\big]=\sum b_n$, contradicción. Ejemplo: $\sum\big(\frac1{2^n}+\frac1n\big)$ diverge. (L §9.2 ej. 98 p.604.)

### P2 (media) — comparación en ambos sentidos, cociente y raíz *(propio)*

a) $\displaystyle\sum\frac{n+1}{n^3+2}$: para $n\ge1$, $n+1\le2n$ y $n^3+2>n^3$ ⇒ $0<a_n\le\frac{2n}{n^3}=\frac2{n^2}$; $\sum\frac1{n^2}$ converge (U p.38) ⇒ **converge** (suma $\approx1{,}4247$).

b) $\displaystyle\sum\frac{1}{\sqrt n+1}$: $1\le\sqrt n$ ⇒ $\sqrt n+1\le2\sqrt n$ ⇒ $a_n\ge\frac1{2\sqrt n}$; $\sum\frac1{n^{1/2}}$ diverge ($\gamma=\tfrac12\le1$) ⇒ **diverge**.

c) $\displaystyle\sum\frac{n!}{n^n}$ (cociente): $\dfrac{a_{n+1}}{a_n}=\dfrac{(n+1)!}{(n+1)^{n+1}}\cdot\dfrac{n^n}{n!}=\Big(\dfrac{n}{n+1}\Big)^n=\dfrac1{(1+1/n)^n}\to\dfrac1e<1$ ⇒ **converge** (suma $\approx1{,}8799$).

d) $\displaystyle\sum\Big(\frac{n}{n+1}\Big)^{n^2}$ (raíz): $\sqrt[n]{a_n}=\Big(\dfrac n{n+1}\Big)^n\to\dfrac1e<1$ ⇒ **converge** (suma $\approx0{,}8174$).

### P3 (difícil) — Leibniz, convergencia condicional y la trampa del decrecimiento *(propio)*

a) $\displaystyle\sum_{n\ge1}\frac{(-1)^n n}{n^2+1}$.
- *No absolutamente:* $\frac{n}{n^2+1}\ge\frac1{2n}$ (equivale a $2n^2\ge n^2+1$, es decir $n^2\ge1$) y $\sum\frac1{2n}$ diverge ⇒ $\sum|a_n|$ diverge.
- *Leibniz:* $c_n=\frac n{n^2+1}$ decrece: $c_{n+1}\le c_n\iff(n+1)(n^2+1)\le n\big((n+1)^2+1\big)\iff0\le n^2+n-1$, cierto para $n\ge1$. Y $c_n=\frac{1/n}{1+1/n^2}\to0$.
- **Converge, pero no absolutamente** («condicionalmente convergente»: término de S p.733 / L p.622-623, no usado en U). Suma $\approx-0{,}2696$.

b) **Trampa:** $\displaystyle\sum_{n\ge2}\frac{(-1)^n}{\sqrt n+(-1)^n}$. Es alternada y su término tiende a $0$, pero $|a_n|$ **no** decrece ($|a_2|\approx0{,}414<|a_3|\approx1{,}366$), así que Leibniz no se aplica. Multiplicando por el conjugado:
$$\frac{(-1)^n}{\sqrt n+(-1)^n}=\frac{(-1)^n\big(\sqrt n-(-1)^n\big)}{n-1}=\underbrace{\frac{(-1)^n\sqrt n}{n-1}}_{\text{converge (Leibniz)}}-\underbrace{\frac1{n-1}}_{\text{armónica: diverge}}.$$
$\frac{\sqrt n}{n-1}$ decrece para $n\ge2$ (elevando al cuadrado, $\frac{\sqrt{n+1}}{n}\le\frac{\sqrt n}{n-1}\iff(n+1)(n-1)^2\le n^3\iff0\le n^2+n-1$) y tiende a $0$. Convergente + divergente = divergente (P1-d) ⇒ **la serie diverge** (sumas parciales numéricas: $-6{,}55$ en $n=10^3$, $-13{,}48$ en $n=10^6$; bajan aproximadamente como $-\ln n$). Moraleja: la hipótesis «$|a_n|$ decreciente» de Leibniz no es decorativa.

*(Todas las afirmaciones de P1-P3 verificadas con sympy/mpmath: sumas, desigualdades polinómicas e identidad del conjugado.)*

---

## (a) Teoría necesaria (U, páginas impresas verificadas en el texto y en el PDF)

| Concepto / resultado | U | Se usa en |
|---|---|---|
| Sucesión de sumas parciales; Def. 1.14 (serie) | §1.3.2 p.34 | todos |
| Def. 1.15 serie convergente/sumable y suma; abuso de notación; series desde $n=p$ (margen) | p.35 | 1.17, 1.21 |
| «Divergente» = no convergente (Ej. 1.32, serie $\sum n$) | p.35-36 | 1.17 |
| Serie geométrica $\sum r^n$ (Ej. 1.33) y generalización $\sum_{n\ge k}ar^n=\frac{ar^k}{1-r}$, sumable si y solo si $\lvert r\rvert<1$ (margen) | p.36 | 1.22, P1 |
| Prop. 1.6: convergente ⇒ $a_n\to0$ (y su uso contrarrecíproco) | p.36 | 1.20, P1 |
| Ej. 1.34 ($\sum\frac n{n+1}$ y $\sum(-1)^n$ divergen) | p.37 | contexto |
| Ej. 1.35 serie armónica divergente | p.37 | 1.17 |
| Prop. 1.7 linealidad de series sumables | p.37 | 1.17, 1.19, P1-d |
| Criterio de comparación (términos no negativos, desde un $n_0$) | p.38 | 1.18, 1.19, 1.22, P2 |
| $\sum1/n^2=\pi^2/6$; $\sum1/n^\gamma$ converge ⇔ $\gamma>1$ (sin demostración) | p.38 | 1.18, 1.19, P2 |
| Criterio del cociente ($a_n>0$; $\ell<1$ converge, $\ell>1$ no, $\ell=1$ no decide) | p.38 | 1.20, P2 |
| Criterio de la raíz (ídem) | p.38 | 1.21, P2 |
| Advertencia: estos criterios solo para términos no negativos; «si decide el cociente, decide la raíz»; Ej. 1.36-1.38 | p.39-40 | 1.18-1.21 |
| Términos no positivos: $\sum a_n=-\sum\lvert a_n\rvert$ | p.40 | — |
| Def. 1.16 convergencia absoluta; Prop. 1.8 (absoluta ⇒ convergente, $\lvert\sum a_n\rvert\le\sum\lvert a_n\rvert$) | p.40 | 1.18, 1.22 |
| Ej. 1.39 $\sum\cos n/n^2$ | p.40-41 | 1.18 |
| Def. 1.17 serie alternada; criterio de Leibniz; Ej. 1.40-1.41 | p.41 | 1.22, P3 |
| De §1.2: Prop. 1.3 (álgebra de límites) p.26; Def. 1.12 recta ampliada p.27; Prop. 1.4 p.28; indeterminaciones p.29-30; fórmula (1.1) $a_n^{b_n}=e^{b_n\ln a_n}$ y continuidad p.29; Teorema 1.3 (monótona: convergente ⇔ acotada) p.31; Prop. 1.5 $(1+1/a_n)^{a_n}\to e$ p.31; criterio de Stolz p.32 | §1.2 | 1.17, 1.20, 1.21, 1.22 |

Nota: §1.3 empieza en U p.33 (no p.31: pp. 31-32 son el final de §1.2, sucesiones monótonas, número $e$ y Stolz).

## (b) Huecos de U y dónde suplirlos (S / L)

| Hueco en U | Suplir con |
|---|---|
| Series **telescópicas** (no aparecen) | S §11.2 Ej. 7 p.707-708; L §9.2 Ej. 1c p.596 y Ej. 2 p.597 |
| Nombre y enunciado de la **prueba de la divergencia** / término n-ésimo (U solo lo comenta tras Prop. 1.6) | S §11.2 (7) p.709; L Teor. 9.9 p.599 |
| **Convergente + divergente = divergente**; divergente + divergente puede converger | L §9.2 ej. 97-98 p.604; S §11.2 ej. 84 p.713 (es el ej. 1.17 de E) |
| **Por qué** $\sum1/n^\gamma$ converge ⇔ $\gamma>1$ (U lo da sin prueba; requiere el criterio de la integral) | S §11.3 (serie $p$, recuadro 1) p.717; L Teor. 9.10 p.605 y 9.11 p.607 |
| **Comparación por paso al límite** (muy útil en 1.18/1.19; U no la tiene) | S §11.4 p.724; L Teor. 9.13 p.614 |
| Comparación directa: intuición y «solo importa desde un $N$» | S §11.4 p.722-723 (Nota 1); L Teor. 9.12 p.612 |
| Término **condicionalmente convergente** | S §11.6 Def. 2 p.733; L §9.5 p.622-623 |
| Cociente y raíz en versión **absoluta** (términos con signo; U exige $a_n>0$) | S §11.6 p.734 (razón) y p.736 (raíz); L Teor. 9.17 p.627 y 9.18 p.630 |
| Demostración/intuición de Leibniz (sumas parciales pares e impares) | S §11.5 p.727-728; L Teor. 9.14 p.619 |
| **Estrategia** para elegir criterio | S §11.7 p.739-740; L §9.6 «Estrategias para probar series» p.631 |
| Casos $\lvert r\rvert=1$ de la geométrica: el texto de U solo dice «no es convergente si $\lvert r\rvert>1$» (el margen sí dice «si y solo si $\lvert r\rvert<1$») | S §11.2 p.706; L Teor. 9.6 p.597 |
| Límites del tipo $(\ln n)^k/n\to0$ («jerarquía de infinitos»): U no la da en §1.2; E remite a L’Hôpital (U §2.3.2 p.82) | Aquí: Stolz (U p.32), ver 1.21 paso 5 |

(Páginas de S localizadas por la cabecera impresa de cada página; las de L con impresa = PDF − 17, comprobado con la cabecera «630 Capítulo 9».)

## (c) Erratas y omisiones de E (y avisos de extracción de U)

1. **E 1.21 (p.23):** la serie empieza en $n=1$, donde el término $\frac{1^{\ln1}}{(\ln1)^1}=\frac10$ no está definido. Debe ser $\sum_{n=2}^{\infty}$ (confirmado en el PDF, no es fallo de extracción).
2. **E 1.21 (p.24):** escribe $\ln A=\ln\lim(\dots)=\lim\ln(\dots)$ antes de saber que $A$ existe; lógicamente hay que calcular primero $\lim L_n$ y luego exponenciar. Además $\lim\frac{(\ln n)^2}{n}=0$ se deja «intuitivo»/a L’Hôpital, cuando se puede probar con Stolz (U p.32).
3. **E 1.19 (p.22):** en la desigualdad entre series aparece $\dfrac{1}{n^{1/2}+n^{3/2}}$ en lugar de $\dfrac{1}{n^{1/2}+n^{2/3}}$ (confirmado en el PDF). Además: la desigualdad estricta se afirma «para $n>1$» pero se suma desde $n=1$ (en $n=1$ hay igualdad, $\frac12=\frac12$); se escribe «$>$» entre sumas de series que valen ambas $+\infty$ (la comparación debe hacerse término a término); y «$\gamma=2/3<1$»: la condición de divergencia es $\gamma\le1$.
4. **E 1.18 (p.21):** escribe desigualdades entre sumas ($0<\sum\dots<\sum\frac1{n^{5/2}}$) antes de saber que la primera converge; la conclusión es correcta, pero el criterio se aplica término a término.
5. **E 1.20 (p.23):** «conocemos dos criterios: el del cociente y el de la raíz» es impreciso (también comparación y Prop. 1.6, que aquí basta: $a_n$ es creciente y $\ge1$).
6. **E 1.22 (p.24-25):** omite que la serie es **absolutamente convergente** ($c_n<e^{-n}$), vía más corta y más informativa. En la nota al margen, Leibniz usa $a_n$ para el término con signo y en el texto $a_n$ es la parte positiva $c_n$: notación ambigua.
7. **E 1.17 (p.20-21):** correcto. Solo precisar que «$\sum(-\frac1n)=-\infty$» significa que las sumas parciales tienden a $-\infty$.
8. **Avisos de extracción de U (`ingenieros.txt`)**, no erratas del PDF: Ej. 1.33 (p.36) «Para $r=1$» es «$r\ne1$»; tras la Prop. 1.6 (p.36) «$\lim a_n=0$» es «$\lim a_n\ne0$»; en la Prop. 1.3 (p.26) «$b_n=0$ … $\lim b_n=0$» son «$\ne0$»; el Ej. 1.34 (p.37) sale desordenado. Los dos primeros comprobados sobre el PDF renderizado de p.36; los otros dos, por el sentido del enunciado.
