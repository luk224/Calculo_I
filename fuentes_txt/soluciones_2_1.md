# Soluciones — Tema 2.1 Derivada de una función (U §2.1, pp. 74-78)

Fuentes: **E** = Libro de ejercicios 24-25 (impresa = PDF); **U** = *Cálculo para ingenieros* (impresa = PDF + 2); **S** = Stewart; **L** = Larson (impresa = PDF − 17). Todos los enunciados se han contrastado con el PDF renderizado, porque pdftotext pierde $\ne$ y $\sqrt{\ }$. Todos los cálculos se han verificado con sympy/mpmath.

**Orden didáctico propuesto** (se conserva la numeración de E):
- Concepto: 2.1 → 2.2
- Recta tangente: 2.6 → 2.7 → 2.8 → 2.9
- Derivadas laterales: 2.19 → 2.18 → 2.17 → 2.20 → 2.23
- Teoría: 2.14 → 2.21 → 2.22

**Resultados:** 2.1 b) · 2.2 $720/13\approx55{,}38$ km/h (sí puede haber multa) · 2.6 a), b) y c) ciertas · 2.7 $(0,-1)$ y $(-2,-7/3)$ · 2.8 $(-1,-5/3)$ · 2.9 b) · 2.14 verdadera · 2.17 verdadera · 2.18 falsa · 2.19 $\pm1$ · 2.20 b) · 2.21 $|f|'(a)=\operatorname{sgn}(f(a))f'(a)$ · 2.22 c) · 2.23 d).

**Dependencias de otras secciones** (se resuelven igualmente aquí):

| Ej. | Sección de la que depende más |
|---|---|
| 2.2 | Velocidad media (U §2.1.2 p.74). La ampliación usa el Teorema del valor medio (U §2.5.3 p.96, Tema 3 del cronograma). |
| 2.6-2.8 | La ecuación de la tangente solo aparece explícita en U §2.4.2 p.87. Las reglas de derivación están en U §2.2.2 p.79. |
| 2.9 | Reglas de derivación (U §2.2). No usa crecimiento para responder, pero su figura solo se entiende con la monotonía (U §2.5.4 Prop. 2.4 p.98). |
| 2.14 | Sobre todo §1.4 (Teorema de Bolzano, U p.52) más el Teorema 2.1 (U p.76). |
| 2.17-2.20, 2.23 | Derivadas laterales: U **§2.2** (Def. 2.3, p.81), no §2.1. E usa L'Hôpital (U §2.3 p.82) en 2.20 y 2.23; aquí se evita. |
| 2.21 | Conservación del signo (U §1.4 Prop. 1.9 p.44). |
| 2.22 | Regla del emparedado (U §1.4 p.45) y $\big||x|-|y|\big|\le|x-y|$ (U §1.1 Teorema 1.1 p.16). |

---

## Ejercicio 2.1 (E p.52)

> La derivada en un punto $a\in\mathbb R$ de una función derivable $f:\mathbb R\to\mathbb R$ es:
> a) Una recta tangente. b) Un número real. c) Una función.

**Solución**
1. Partimos de la definición (U Def. 2.1, p.75): $f$ es derivable en $a$ si existe y es **finito** el límite $\lim_{h\to0}\frac{f(a+h)-f(a)}{h}$, y ese valor se llama $f'(a)$.
2. Un límite finito de números reales es un número real (U Def. 1.18, p.43). Por tanto $f'(a)\in\mathbb R$.
3. Descartamos las otras opciones:
   - a) La recta tangente es un objeto distinto: es la recta que pasa por $(a,f(a))$ y tiene **pendiente** $f'(a)$ (U p.75). $f'(a)$ es un dato de esa recta, no la recta.
   - c) La **función derivada** $f':A\to\mathbb R$ es otra cosa: asigna a cada punto $x$ el número $f'(x)$ (U Def. 2.2, p.78). La derivada *en un punto* es su valor en $a$.
4. Respuesta: **b)**.

**Receta.** Distingue tres objetos: $f'(a)$ es un número (la pendiente), $f'$ es una función, y la tangente es la recta $y=f(a)+f'(a)(x-a)$.

**Error típico.** Llamar «la derivada» indistintamente a $f'$, a $f'(a)$ y a la tangente.

**Teoría:** U §2.1.2 Def. 2.1 p.75; U §2.1.3 Def. 2.2 p.78.

---

## Ejercicio 2.2 (E p.52)

> Un coche entra en un túnel de 3 km limitado a 50 km/h. La cámara de un radar de tramo realiza una foto al entrar, y otra al salir, donde se refleja que ha tardado en recorrer el túnel 3 minutos y 15 segundos. ¿Es posible que al conductor le llegue una multa?

**Solución**
1. **Qué mide el radar.** Solo conoce dos posiciones y dos instantes, así que solo puede calcular el cociente $\frac{f(b)-f(a)}{b-a}$, que es la **velocidad media** (U §2.1.2 p.74). La velocidad instantánea sería la derivada, es decir, el límite de estas medias (U p.75), y el radar de tramo no la mide.
2. **Pasamos el tiempo a horas**, porque la velocidad está en km/h: $3\text{ min }15\text{ s}=3{,}25\text{ min}=\frac{3{,}25}{60}\text{ h}=\frac{13}{240}\text{ h}\approx0{,}054167\text{ h}$.
3. **Velocidad media:** $v_m=\dfrac{3}{13/240}=\dfrac{720}{13}\approx55{,}38$ km/h.
4. **Conclusión.** $55{,}38>50$, así que **sí, puede llegarle una multa**, que es justo lo que sanciona un radar de tramo.
5. **Ampliación (Tema 3).** Supongamos que la posición $f(t)$ es continua en $[0,T]$ y derivable en $(0,T)$. El Teorema del valor medio (U §2.5.3 p.96) garantiza un instante $c$ con $f'(c)=v_m\approx55{,}38$ km/h. Por tanto el coche **superó los 50 km/h en al menos un instante**.

**Receta.** Velocidad media = incremento de posición entre incremento de tiempo, con las unidades homogeneizadas antes de dividir. La derivada es el límite de ese cociente.

**Error típico.** Poner 3,15 min en lugar de 3,25 min, o redondear el tiempo en horas antes de dividir.

**Errata de E.** E toma 0,0541 h y obtiene 55,3914 km/h, pero $3/0{,}0541\approx55{,}45$ y el valor exacto es $720/13\approx55{,}38$: ninguno coincide con el de E. Además E no responde «sí» explícitamente.

**Teoría:** U §2.1.2 pp.74-75; ampliación en U §2.5.3 p.96.

---

## Ejercicio 2.6 (E p.54)

> Si $f:\mathbb R\to\mathbb R$ es derivable en $a\in\mathbb R$, entonces
> a) La recta $y=f'(a)(x-a)+f(a)$ es tangente a la gráfica de $f$ en el punto $(a,f(a))$.
> b) La pendiente de la recta tangente a la gráfica de $f$ en el punto $(a,f(a))$ es $f'(a)$.
> c) La recta $x=-f'(a)(y-f(a))+a$ corta perpendicularmente a la gráfica de $f$ en $(a,f(a))$.

**Solución** (las tres afirmaciones son ciertas)
1. **b)** La derivada es el límite de las pendientes de las secantes entre $(a,f(a))$ y $(a+h,f(a+h))$, y ese límite es la pendiente de la tangente (U p.75, Figura 2.1). **Cierta.**
2. **a)** La recta que pasa por $(x_0,y_0)$ con pendiente $m$ es $y-y_0=m(x-x_0)$ (U §2.4.2 p.87). Con $(x_0,y_0)=(a,f(a))$ y $m=f'(a)$ (paso 1) sale exactamente $y=f'(a)(x-a)+f(a)$. **Cierta.**
3. **c)** «Cortar perpendicularmente a la gráfica» significa ser perpendicular a la tangente en ese punto.
   - *Pasa por el punto.* Si $y=f(a)$, entonces $x=-f'(a)\cdot0+a=a$. ✓
   - *Tiene la dirección correcta.* Reescribimos la recta como $x-a=-f'(a)\,(y-f(a))$. Tomando $y-f(a)=t$, sus puntos son $(a-f'(a)t,\ f(a)+t)$, así que su vector director es $(-f'(a),1)$. La tangente tiene vector director $(1,f'(a))$. El producto escalar vale $1\cdot(-f'(a))+f'(a)\cdot1=0$: son perpendiculares. ✓ **Cierta.**
4. **Por qué se escribe así la normal.** Si $f'(a)=0$ la tangente es horizontal y la normal es la vertical $x=a$. La fórmula de c) da justo $x=a$. En cambio, la forma habitual $y-f(a)=-\frac1{f'(a)}(x-a)$ no tiene sentido cuando $f'(a)=0$.

**Receta.**
- Tangente: $y=f(a)+f'(a)(x-a)$.
- Normal: vector director $(-f'(a),1)$, es decir, $x-a=-f'(a)(y-f(a))$.
- Para comprobar perpendicularidad, basta que el producto escalar de los vectores directores sea 0.

**Error típico.** Escribir la normal con pendiente $-1/f'(a)$ sin excluir el caso $f'(a)=0$.

**Nota sobre el margen de E p.55.** El texto extraído dice «Si $u = 0$, la ecuación … se puede reescribir como $y=mx+c$», pero en el PDF pone $u\ne0$. Es un fallo de extracción, no una errata.

**Teoría:** U §2.1.2 p.75 (pendiente); U §2.4.2 p.87 (ecuación punto-pendiente). La recta normal no está en U: ver S §3.1 p.176-177.

---

## Ejercicio 2.7 (E p.55)

> Encuentra los puntos en los que la recta tangente a la gráfica de la función $f$ dada por $f(x)=-\frac13x^3-x^2-1$ es paralela al eje $x$.

**Solución**
1. **Traducimos la condición.** Paralela al eje $x$ significa horizontal, y una recta horizontal tiene pendiente $0$.
2. **Pendiente de la tangente.** En $(x,f(x))$ la pendiente es $f'(x)$ (U p.75). Buscamos los $x$ con $f'(x)=0$.
3. **Derivamos.** Con la tabla ($(x^c)'=cx^{c-1}$, derivada de una constante $=0$) y la linealidad (U Prop. 2.1 p.79): $f'(x)=-\frac13\cdot3x^2-2x=-x^2-2x$.
4. **Resolvemos.** $-x^2-2x=0\iff -x(x+2)=0\iff x=0$ o $x=-2$.
5. **Ordenadas.** $f(0)=-1$; $f(-2)=-\frac13(-8)-4-1=\frac83-5=-\frac73$.
6. **Puntos:** $(0,-1)$ y $\left(-2,-\frac73\right)$. ✓ (sympy)

**Receta.** «Tangente con pendiente $m$» se resuelve con la ecuación $f'(x)=m$; después se sustituye cada solución en $f$ (no en $f'$) para obtener el punto.

**Error típico.** Dar solo las abscisas, o sustituir en $f'$ para obtener la ordenada.

**Teoría:** U p.75; U §2.2.2 Prop. 2.1 y tabla, p.79.

---

## Ejercicio 2.8 (E pp.55-56)

> Calcula los puntos en los que la recta tangente a la gráfica de la función dada por $f(x)=-\frac13x^3-x^2-1$ forma un ángulo de $\frac\pi4$ radianes con el eje $x$ (medido desde el eje $x$ a la recta en sentido contrario al de las agujas del reloj).

**Solución**
1. **Del ángulo a la pendiente.** Si una recta forma un ángulo $\theta$ con el eje $x$, su pendiente es $m=\tan\theta$ (margen de E p.55). Aquí $m=\tan\frac\pi4=1$.
2. **Ecuación.** Del ejercicio 2.7, $f'(x)=-x^2-2x$. Imponemos $-x^2-2x=1\iff x^2+2x+1=0\iff(x+1)^2=0\iff x=-1$ (raíz doble).
3. **Ordenada.** $f(-1)=-\frac13(-1)-1-1=\frac13-2=-\frac53$.
4. **Resultado.** El punto es $\left(-1,-\frac53\right)$ y la tangente es $y=x-\frac23$ ✓ (sympy).
5. **Por qué hay un solo punto.** $f'(x)=1-(x+1)^2\le1$, así que $1$ es la **pendiente máxima** de la gráfica y solo se alcanza en $x=-1$.

**Receta.** Ángulo $\theta$ ⇒ pendiente $\tan\theta$ ⇒ resolver $f'(x)=\tan\theta$.

**Error típico.** Igualar $f'(x)=\pi/4$, es decir, confundir el ángulo con la pendiente.

**Teoría:** U p.75; U p.79; relación ángulo-pendiente en E p.55 (margen), que U no da.

---

## Ejercicio 2.9 (E pp.56-57)

> De una función derivable $f:\mathbb R\to\mathbb R$ se sabe que $f'(x)=\operatorname{sen}(\pi x)\,e^{2x^2-x}$. Señala la afirmación correcta relativa a la recta tangente a la gráfica de $f$ en $(x,f(x))$:
> a) Nunca es paralela al eje $x$. b) Para $x=\frac12$ es perpendicular al vector $(-1,1)$. c) Sólo es paralela al eje $x$ si $x=0$. d) Ninguna de las anteriores.

**Solución**
1. No conocemos $f$, pero la pendiente en $x$ es $f'(x)$ (U p.75), y eso basta.
2. **Tangente horizontal.** Ocurre cuando $f'(c)=0$. Como $e^{2c^2-c}>0$ siempre, $f'(c)=0\iff\operatorname{sen}(\pi c)=0\iff c=k\in\mathbb Z$. Hay infinitos puntos con tangente horizontal, así que **a) y c) son falsas**.
3. **Pendiente en $x=\frac12$.** $f'(\tfrac12)=\operatorname{sen}\tfrac\pi2\cdot e^{2\cdot\frac14-\frac12}=1\cdot e^0=1$.
4. **Perpendicularidad.** Con pendiente 1, un vector director de la tangente es $(1,1)$. Como $(1,1)\cdot(-1,1)=-1+1=0$, la tangente es perpendicular a $(-1,1)$: **b) es cierta**.
5. Por tanto d) es falsa. **Respuesta: b).**

**Receta.** Pendiente $m$ ⇒ vector director $(1,m)$. «Perpendicular al vector $v$» equivale a $(1,m)\cdot v=0$.

**Error típico.** Confundir «perpendicular al vector $(-1,1)$» con «paralela a $(-1,1)$», que correspondería a pendiente $-1$.

**Errata de E (p.57).**
- E afirma que «la función $f$ es periódica». Es falso: $f'$ no es periódica, por el factor $e^{2x^2-x}$, y ninguna primitiva suya lo es. Numéricamente, con $f(0)=0$: $f(1)\approx0{,}72$ y $f(-1)\approx2{,}41$.
- La gráfica de E no corresponde a ninguna primitiva de $f'$. Según la monotonía (U §2.5.4 Prop. 2.4 p.98): $f'<0$ en $(-1,0)$ y $f'>0$ en $(0,1)$, luego $f$ tiene un **mínimo en 0** y máximos en $\pm1$. La figura, en cambio, pasa por el origen creciendo y tiene extremos hacia $\pm0{,}9$.

**Teoría:** U p.75; U p.79. La figura requiere U §2.5.4 p.98.

---

## Ejercicio 2.19 (E p.62)

> Calcula $f'(0^+)$ y $f'(0^-)$ para la función valor absoluto $f(x)=|x|$. Deduce que la función valor absoluto no es derivable en 0 pese a ser continua en 0.

**Solución**
1. **Derivadas laterales** (U Def. 2.3 p.81): $f'(0^\pm)=\lim_{h\to0^\pm}\frac{f(0+h)-f(0)}{h}=\lim_{h\to0^\pm}\frac{|h|}{h}$.
2. **Por la derecha**, $h>0$: $|h|=h$ (U Def. 1.1 p.15), así que $\frac{|h|}{h}=1$ y $f'(0^+)=1$.
3. **Por la izquierda**, $h<0$: $|h|=-h$, así que $\frac{|h|}{h}=-1$ y $f'(0^-)=-1$.
4. **No es derivable.** El límite bilateral existe si y solo si existen los laterales y coinciden (U Teorema 1.4 p.47). Aquí $1\ne-1$, luego $f'(0)$ no existe.
5. **Sí es continua.** $\lim_{x\to0^+}|x|=0$ y $\lim_{x\to0^-}|x|=0$. Por el Teorema 1.4, $\lim_{x\to0}|x|=0=|0|$ (U Def. 1.20 p.51).

**Receta.** En un punto donde la fórmula cambia (valor absoluto, función a trozos), calcula por separado $f'(a^+)$ y $f'(a^-)$ con la definición, usando en cada lado la expresión que corresponde al signo de $h$.

**Error típico.** Pensar que «continua» implica «derivable». Solo es cierto al revés (U Teorema 2.1 p.76).

**Teoría:** U §2.2.2 Def. 2.3 p.81; U §1.4 Teorema 1.4 p.47. Mejor explicado en S §2.8 Ej. 5 pp.157-158 y L §2.1 Ej. 6 p.102 (con $|x-2|$).

---

## Ejercicio 2.18 (E p.62)

> Razona la veracidad o falsedad de la siguiente afirmación: *Si una función $f$ es derivable por la izquierda y la derecha en $a$, entonces $f$ es derivable en $a$.*

**Solución**
1. Para que exista el límite bilateral hace falta que los laterales existan **y coincidan** (U Teorema 1.4 p.47; criterio de U p.81).
2. Basta un contraejemplo: $f(x)=|x|$ en $a=0$. Por 2.19 tiene $f'(0^+)=1$ y $f'(0^-)=-1$: existen ambas, pero no es derivable.
3. **La afirmación es falsa.**

**Receta.** Para refutar un «si…, entonces…» basta un contraejemplo (U p.16, margen). $|x|$ en 0 es el contraejemplo estándar en derivabilidad.

**Error típico.** Olvidar la condición «y coinciden».

**Teoría:** U p.81; U p.47.

---

## Ejercicio 2.17 (E pp.61-62)

> Razona la veracidad o falsedad de la siguiente afirmación: *Si una función $f$ es derivable en $a$ por la izquierda y la derecha verificando que $f'(a^-)=f'(a^+)$, entonces $f$ es continua en $a$.*

**Solución**
1. Si las derivadas laterales existen y coinciden, $f$ es derivable en $a$ y $f'(a)=f'(a^\pm)$ (U p.81).
2. Si $f$ es derivable en $a$, es continua en $a$ (U Teorema 2.1 p.76). U no da la demostración; es esta: $f(a+h)-f(a)=h\cdot\frac{f(a+h)-f(a)}{h}\xrightarrow[h\to0]{}0\cdot f'(a)=0$, por el límite de un producto (U Prop. 1.11 p.46). Luego $\lim_{h\to0}f(a+h)=f(a)$.
3. **Verdadera.**

**Observación (la hipótesis de igualdad sobra).** La conclusión sigue siendo cierta aunque $f'(a^-)\ne f'(a^+)$:
- Si $h\to0^+$: $f(a+h)-f(a)=h\cdot\frac{f(a+h)-f(a)}{h}\to0\cdot f'(a^+)=0$.
- Si $h\to0^-$: lo mismo con $f'(a^-)$.
- Los dos límites laterales valen $f(a)$, y por el Teorema 1.4 (p.47) $f$ es continua en $a$. El ejemplo $|x|$ lo muestra: derivadas laterales distintas y aun así continua.

**Receta.** Derivable (incluso solo lateralmente por ambos lados) ⇒ continua. Para demostrarlo, multiplica y divide por $h$.

**Error típico.** Creer que hace falta $f'(a^-)=f'(a^+)$ para la continuidad.

**Teoría:** U p.81; U Teorema 2.1 p.76 (sin demostración); demostración en S §2.8 Teorema 4 pp.158-159 y L §2.1 Teorema 2.1 p.102.

---

## Ejercicio 2.20 (E pp.62-63)

> Señala la afirmación correcta:
> a) $f(x)=|x|$ es derivable en 0. b) $g(x)=|x^3|$ es derivable en 0. c) $m(x)=|2\operatorname{sen}x|$ es derivable en 0. d) $j(x)=\sqrt{|x|}$ es derivable en 0.

**Solución**
1. **a)** Falsa, por el ejercicio 2.19.
2. **b)** Como $|h^3|=|h|^3$, $\frac{|h^3|-0}{h}=\frac{|h|^3}{h}=h\,|h|$, que vale $h^2$ si $h>0$ y $-h^2$ si $h<0$. Ambos tienden a 0, así que $g'(0^+)=g'(0^-)=0$ y $g'(0)=0$. **Cierta.**
3. **c)** Para $0<|h|<\pi$ el signo de $\operatorname{sen}h$ es el de $h$. Entonces $m'(0^\pm)=\lim_{h\to0^\pm}\frac{\pm2\operatorname{sen}h}{h}=\pm2\lim_{h\to0}\frac{\operatorname{sen}h-\operatorname{sen}0}{h-0}=\pm2\,\operatorname{sen}'(0)=\pm2\cos0=\pm2$. El último límite es, por definición, la derivada del seno en 0 (U Def. 2.1 p.75 y tabla p.79), sin necesidad de L'Hôpital. Como $2\ne-2$, **c) es falsa**.
4. **d)**
   - Si $h>0$: $\frac{\sqrt h}{h}=\frac1{\sqrt h}\to+\infty$.
   - Si $h<0$: $\frac{\sqrt{-h}}{h}=-\frac1{\sqrt{-h}}\to-\infty$.
   - La definición exige un límite **finito** (U Def. 2.1 y 2.3), así que no hay derivada: la gráfica tiene tangente vertical. **d) es falsa.**
5. **Respuesta: b).** ✓ (sympy: límites laterales $0,0$; $2,-2$; $+\infty,-\infty$)

**Receta.** Con $|\cdot|$ en el punto crítico, quita el valor absoluto según el signo de $h$ a cada lado. Si aparece $\frac{g(h)-g(0)}{h}$ con $g$ conocida, reconócelo como $g'(0)$.

**Error típico.** Dar como derivada un límite infinito (d), o concluir derivabilidad de c) porque $|2\operatorname{sen}x|$ «es suave salvo en 0».

**Errata/omisión de E.** E calcula $\lim\frac{\operatorname{sen}h}{h}$ con L'Hôpital (U §2.3). Es circular: ese límite es precisamente $\operatorname{sen}'(0)$, cuya fórmula ya se usa al derivar. Mejor verlo como una derivada, o citar la prueba geométrica (S §3.3 p.192; L Teorema 1.9 p.65).

**Teoría:** U Def. 2.3 p.81; U Def. 2.1 p.75; tabla U p.79. Tangente vertical: L §2.1 Ej. 7 p.102; S §2.8 p.159.

---

## Ejercicio 2.23 (E pp.65-66)

> Indica los valores de $a$ y $b$ que hacen derivable en todo $\mathbb R$ a la función
> $f(x)=\begin{cases}2x+\operatorname{sen}x & x\le0\\ \operatorname{sen}(ax+b) & x>0.\end{cases}$
> a) $a=-3$ y $b=0$. b) $a=3$ y $b=1$. c) $a=0$ y $b=-3$. d) $a=-3$ y $b=-7\pi$.

**Solución**
1. **Fuera de 0 no hay problema.** En $(-\infty,0)$ y en $(0,\infty)$, $f$ coincide con una suma o una composición de funciones derivables (U Prop. 2.1 y regla de la cadena, p.79). La derivabilidad es local. Solo hay que estudiar $x=0$.
2. **Primero, continuidad en 0.** Es necesaria, porque derivable ⇒ continua (U Teorema 2.1 p.76).
   - $f(0)=0$; $\lim_{x\to0^-}f=0$; $\lim_{x\to0^+}\operatorname{sen}(ax+b)=\operatorname{sen}b$ (U Prop. 1.14 p.51).
   - Hace falta $\operatorname{sen}b=0\iff b=k\pi$ con $k\in\mathbb Z$.
   - Esto descarta b), pues $\operatorname{sen}1\ne0$, y c), pues $3$ no es múltiplo de $\pi$. Quedan a) con $k=0$ y d) con $k=-7$.
3. **Derivada por la izquierda:** $f'(0^-)=\lim_{h\to0^-}\frac{2h+\operatorname{sen}h-0}{h}=2+\operatorname{sen}'(0)=3$.
4. **Derivada por la derecha.** Con $b=k\pi$ se cumple $f(0)=0=\operatorname{sen}(k\pi)$. Por tanto, para $h>0$, $\frac{f(h)-f(0)}{h}=\frac{G(h)-G(0)}{h}$ con $G(x)=\operatorname{sen}(ax+k\pi)$, derivable en $\mathbb R$. Por la regla de la cadena, $f'(0^+)=G'(0)=a\cos(k\pi)=(-1)^k a$.
5. **Igualamos** (U p.81): $(-1)^k a=3$.
   - a) $k=0$: $a=-3$ da $-3\ne3$. Falla.
   - d) $k=-7$: $(-1)^{-7}(-3)=3$. ✓
6. **Respuesta: d).** ✓ (sympy)

**Receta (función a trozos con parámetros).**
1. Estudia solo los puntos de empalme.
2. Impón continuidad: límites laterales iguales a $f(a)$.
3. Impón $f'(a^-)=f'(a^+)$.

Atajo: se puede calcular cada derivada lateral como la derivada de la fórmula de ese lado evaluada en $a$, pero **solo después** de comprobar que esa fórmula toma en $a$ el valor $f(a)$.

**Error típico.** Saltarse la continuidad e igualar directamente las derivadas de las fórmulas. Con b), por ejemplo, se «resolvería» $a\cos1=3$ aunque $f$ ni siquiera es continua.

**Nota sobre E.** Usa L'Hôpital (U §2.3) para $f'(0^+)$. Es correcto pero innecesario, y pertenece a una sección posterior.

**Teoría:** U Teorema 2.1 p.76; Def. 2.3 y criterio p.81; regla de la cadena p.79; Prop. 1.14 p.51.

---

## Ejercicio 2.14 (E p.60) [depende sobre todo de §1.4]

> Señala si es correcta la siguiente afirmación: *sea la función $f:[0,1]\to\mathbb R$ una función derivable en $(0,1)$. Si $\left(\lim_{x\to0^+}f(x)\right)\left(\lim_{x\to1^-}f(x)\right)<0$, entonces la ecuación $f(x)=0$ tiene al menos una solución en $[0,1]$.*

**Solución** (se sobrentiende que ambos límites existen)
1. **Continuidad.** $f$ es derivable en cada punto de $(0,1)$, luego continua en $(0,1)$ (U Teorema 2.1 p.76). No sabemos nada de $f(0)$ ni de $f(1)$.
2. **Signos cerca de los extremos.** Sean $L_0=\lim_{0^+}f$ y $L_1=\lim_{1^-}f$. Como $L_0L_1<0$, tienen signos opuestos; supongamos $L_0<0<L_1$ (el otro caso es simétrico, o se aplica a $-f$). Por conservación del signo (U Prop. 1.9 p.44, aplicada a límites laterales, U p.47):
   - existe $\delta_0>0$ con $f(x)<0$ para $x\in(0,\delta_0)$;
   - existe $\delta_1>0$ con $f(x)>0$ para $x\in(1-\delta_1,1)$.
3. **Elección de $n$.** Tomamos $n\in\mathbb N$ con $\frac1n<\min\{\delta_0,\delta_1,\frac12\}$. Entonces $\frac1n<1-\frac1n$, $f(\frac1n)<0$ y $f(1-\frac1n)>0$.
4. **Bolzano.** $f$ es continua en $[\frac1n,1-\frac1n]\subset(0,1)$ y $f(\frac1n)f(1-\frac1n)<0$. El Teorema de Bolzano (U p.52) da $c\in(\frac1n,1-\frac1n)$ con $f(c)=0$.
5. **Verdadera.** De hecho la solución está en $(0,1)$. U p.52 enuncia literalmente esta versión de Bolzano con $\lim_{a^+}f\cdot\lim_{b^-}f<0$.

**Receta.** Si la hipótesis de Bolzano viene con límites laterales, usa la conservación del signo para bajar a un intervalo cerrado interior $[\frac1n,1-\frac1n]$ y aplica allí Bolzano.

**Error típico.** Aplicar Bolzano en $[0,1]$ con $f(0)$ y $f(1)$: no sabemos si $f$ es continua en 0 y en 1.

**Observación.** «Derivable» es más de lo necesario: basta la continuidad en $(0,1)$.

**Teoría:** U §1.4 Prop. 1.9 p.44; Teorema de Bolzano p.52; U Teorema 2.1 p.76.

---

## Ejercicio 2.21 (E p.63)

> Muestra que si $f$ es derivable en $a$ y $f(a)\ne0$, entonces $|f|$ es derivable en $a$.

**Solución**
1. **Continuidad.** Como $f$ es derivable en $a$, es continua en $a$ (U Teorema 2.1 p.76): $\lim_{h\to0}f(a+h)=f(a)$.
2. **Caso $f(a)>0$.**
   - Por conservación del signo (U Prop. 1.9 p.44), existe $\delta>0$ con $f(a+h)>0$ si $|h|<\delta$.
   - Para esos $h$, $|f(a+h)|=f(a+h)$ y $|f(a)|=f(a)$ (U Def. 1.1 p.15). Entonces $\frac{|f(a+h)|-|f(a)|}{h}=\frac{f(a+h)-f(a)}{h}\xrightarrow[h\to0]{}f'(a)$.
   - Como el límite solo depende de los $h$ pequeños, $|f|'(a)=f'(a)$.
3. **Caso $f(a)<0$.**
   - Del mismo modo, $f(a+h)<0$ para $|h|<\delta$. Entonces $|f(a+h)|=-f(a+h)$ y $|f(a)|=-f(a)$.
   - El cociente es $-\frac{f(a+h)-f(a)}{h}\to-f'(a)$, luego $|f|'(a)=-f'(a)$.
4. **Resumen:** $|f|'(a)=\operatorname{sgn}(f(a))\,f'(a)=\dfrac{f(a)}{|f(a)|}f'(a)$.

**Receta.** Donde $f(a)\ne0$, $|f|$ coincide cerca de $a$ con $f$ o con $-f$, y la derivada se hereda con ese signo.

**Error típico.** Escribir $|f|'=|f'|$. Contraejemplo: $f(x)=x-2$ en $a=1$: $|f|'(1)=-1$, mientras que $|f'(1)|=1$.

**Nota.** En el .txt aparece «$f(a)=0$»; el PDF dice $f(a)\ne0$. Es un fallo de extracción, no una errata.

**Teoría:** U Teorema 2.1 p.76; Prop. 1.9 p.44; Def. 2.1 p.75.

---

## Ejercicio 2.22 (E pp.64-65)

> Sea $f$ derivable en $a$. Señala la afirmación correcta:
> a) $|f|$ siempre es derivable en $a$. b) Si $f'(a)>0$, entonces $|f|$ es derivable en $a$ y $|f|'(a)>0$. c) Si $f'(a)=0$, entonces $|f|$ es derivable en $a$ y $|f|'(a)=0$. d) Si $f'(a)\ne0$, entonces $|f|$ es derivable en $a$ y $|f|'(a)\ne0$.

**Solución**
1. **a), b) y d) son falsas.** Contraejemplo común: $f(x)=x$, $a=0$. Es derivable, con $f'(0)=1>0$ y $f'(0)\ne0$, pero $|f|=|x|$ no es derivable en 0 (ej. 2.19).
2. **c) es cierta.** Queremos $\lim_{x\to a}\frac{|f(x)|-|f(a)|}{x-a}=0$.
   - Como $g\to0\iff|g|\to0$, basta probar que $\left|\frac{|f(x)|-|f(a)|}{x-a}\right|\to0$.
   - *Cota.* Por $\big||u|-|v|\big|\le|u-v|$ (U Teorema 1.1.3 p.16): $0\le\left|\frac{|f(x)|-|f(a)|}{x-a}\right|\le\left|\frac{f(x)-f(a)}{x-a}\right|$.
   - *Límite de la cota.* $\frac{f(x)-f(a)}{x-a}\to f'(a)=0$, luego su valor absoluto también tiende a 0.
   - *Emparedado.* Por la regla del emparedado (U p.45) el término central tiende a 0, así que $|f|'(a)=0$. ✓
3. **Respuesta: c).** Esto vale sea cual sea $f(a)$. Si $f(a)\ne0$ ya lo daba el ej. 2.21, pues $|f|'(a)=\pm f'(a)=0$.

**Complemento: cuadro completo** para $f$ derivable en $a$.

| Caso | ¿$\lvert f\rvert$ derivable en $a$? | $\lvert f\rvert'(a)$ |
|---|---|---|
| $f(a)\ne0$ | Sí (2.21) | $\operatorname{sgn}(f(a))\,f'(a)$ |
| $f(a)=0$, $f'(a)=0$ | Sí (2.22 c) | $0$ |
| $f(a)=0$, $f'(a)\ne0$ | **No** | laterales $\pm\lvert f'(a)\rvert$ |

El caso $f(a)=0$ se ve así: $\frac{|f(a+h)|}{h}=\operatorname{sgn}(h)\left|\frac{f(a+h)}{h}\right|$, y $\left|\frac{f(a+h)}{h}\right|\to|f'(a)|$.

**Receta.** $|f|$ es derivable en $a$ si y solo si $f(a)\ne0$ o $f'(a)=0$. Para demostraciones con $|\cdot|$, combina $\big||u|-|v|\big|\le|u-v|$ con el emparedado.

**Error típico.** Pensar que $f'(a)>0$ «arregla» la esquina. Es al revés: si $f(a)=0$, una pendiente no nula **crea** la esquina.

**Errata de E (p.65).** En la última fórmula aparece $|f|'(a)=\lim_{x\to a}\frac{|f(x)|-|f(a)|}{x}$; el denominador debe ser $x-a$.

**Teoría:** U §1.1 Teorema 1.1 p.16; §1.4 regla del emparedado p.45; Def. 2.1 p.75.

---

## Ejemplos propios (dificultad creciente)

### Propio 1 (fácil): derivada por definición, tangente y normal
Calcula $f'(4)$ para $f(x)=\sqrt x$ usando la definición, y halla la tangente y la normal en $(4,2)$.

1. Por U Def. 2.1: $f'(4)=\lim_{h\to0}\frac{\sqrt{4+h}-2}{h}$. Es del tipo $0/0$; multiplicamos por el conjugado: $=\lim_{h\to0}\frac{(4+h)-4}{h(\sqrt{4+h}+2)}=\lim_{h\to0}\frac1{\sqrt{4+h}+2}=\frac14$.
2. Tangente (U p.87): $y=2+\frac14(x-4)=\frac x4+1$.
3. Normal (como en 2.6 c): $x-4=-\frac14(y-2)$, es decir, $y=-4x+18$.

✓ sympy. Fuente: propio.

### Propio 2 (media): función a trozos con parámetros
Halla $a,b$ para que $f(x)=\begin{cases}ax^2+bx & x\le1\\ \ln x & x>1\end{cases}$ sea derivable en $\mathbb R$.

1. Fuera de $x=1$ es derivable (U p.79). Solo hay que estudiar $x=1$.
2. Continuidad: $f(1)=a+b$ y $\lim_{1^+}\ln x=0$, luego $a+b=0$.
3. $f'(1^-)=\lim_{h\to0^-}\frac{a(1+h)^2+b(1+h)-(a+b)}{h}=\lim_{h\to0^-}(2a+b+ah)=2a+b$.
4. $f'(1^+)=\lim_{h\to0^+}\frac{\ln(1+h)-\ln1}{h}=\ln'(1)=1$ (válido porque $\ln1=0=f(1)$ una vez impuesta la continuidad).
5. Sistema $a+b=0$, $2a+b=1$, que da **$a=1$, $b=-1$**.

✓ sympy. Fuente: propio.

### Propio 3 (difícil): derivabilidad de $|f|$ en varios puntos
¿Dónde son derivables $F(x)=|x^3-x|$ y $G(x)=|x^3-x^2|$?

1. **$F$.** Sea $f(x)=x^3-x$, con ceros en $-1,0,1$ y $f'(x)=3x^2-1$.
   - Fuera de los ceros, $F$ es derivable por 2.21.
   - En los ceros, $f'(\pm1)=2\ne0$ y $f'(0)=-1\ne0$. Por el cuadro de 2.22, $F$ **no** es derivable en $-1,0,1$.
   - Laterales: $F'(\pm1^\pm)=\pm2$ y $F'(0^\pm)=\pm1$.
2. **$G$.** Sea $g(x)=x^3-x^2=x^2(x-1)$, con ceros en $0$ y $1$ y $g'(x)=3x^2-2x$.
   - $g'(0)=0$: por 2.22 c), $G$ **es** derivable en 0 con $G'(0)=0$.
   - $g'(1)=1\ne0$: $G$ **no** es derivable en 1, con laterales $\pm1$.

✓ sympy. Fuente: propio (aplica 2.21-2.22).

---

## (a) Teoría necesaria (U, página impresa verificada en el texto)

| Resultado | U, sección y página |
|---|---|
| Valor absoluto (Def. 1.1) | §1.1 p.15 |
| Teorema 1.1: desigualdad triangular y $\big\lvert\lvert x\rvert-\lvert y\rvert\big\rvert\le\lvert x-y\rvert$ | §1.1 p.16 |
| Límite de una función (Def. 1.18) | §1.4 p.43 |
| Conservación del signo (Prop. 1.9) | §1.4 p.44 |
| Regla del emparedado; Prop. 1.10 | §1.4 p.45 |
| Álgebra de límites (Prop. 1.11) | §1.4 p.46 |
| Límites laterales y Teorema 1.4 (límite ⇔ laterales iguales) | §1.4 p.47 |
| Continuidad (Def. 1.20); Prop. 1.13-1.14 | §1.4 p.51 |
| Teorema de Bolzano (y su versión con límites laterales) | §1.4 p.52 |
| Velocidad media e instantánea | §2.1.2 pp.74-75 |
| Derivada (Def. 2.1) e interpretación como pendiente (Fig. 2.1) | p.75 |
| Ejemplos 2.1-2.2; Teorema 2.1 (derivable ⇒ continua); Ej. 2.3 (Heaviside) | p.76 |
| Ejemplos 2.4-2.5 | pp.76-77 |
| Derivable en un conjunto; función derivada (Def. 2.2) | §2.1.3 p.78 |
| Prop. 2.1 (suma, producto, cociente); regla de la cadena; tabla de derivadas | §2.2.2 p.79 |
| Tabla con regla de la cadena; Ej. 2.6 (arcoseno) | p.80 |
| Derivadas laterales (Def. 2.3) y criterio «existen y coinciden ⇒ derivable» | p.81 (está en §2.2, no en §2.1) |
| L'Hôpital | §2.3.2 p.82 |
| Ej. 2.8, $\lim\frac{\operatorname{sen}x}{x}$ por L'Hôpital | pp.82-83 |
| Ecuación de la tangente $y-f(x_0)=f'(x_0)(x-x_0)$ | §2.4.2 p.87 |
| Rolle ($\lvert x\rvert$ como contraejemplo) | §2.5.2 p.95 |
| Teorema del valor medio | §2.5.3 p.96 |
| Monotonía (Prop. 2.4) | §2.5.4 p.98 |

## (b) Huecos de U y dónde suplirlos

| Hueco en U | Dónde está |
|---|---|
| Ecuación de la recta tangente: U §2.1 solo da la pendiente (p.75); la ecuación aparece de pasada en §2.4 p.87 | S §2.7 Ej. 1 p.144 y recuadro p.147; L §2.1 p.100 |
| Recta normal: no aparece en U | S §3.1 Ej. 3 pp.176-177 |
| Relación pendiente $=\tan\theta$: no está en U | Margen de E p.55 |
| Demostración de «derivable ⇒ continua» (U solo la enuncia, p.76) | S §2.8 Teorema 4 pp.158-159; L §2.1 Teorema 2.1 p.102 |
| Versión lateral (derivable lateralmente ⇒ continua lateralmente) | No está en U ni explícita en S/L; demostración en el ej. 2.17 |
| No derivabilidad de $\lvert x\rvert$ (U solo lo menciona en Rolle, p.95) | S §2.8 Ej. 5 pp.157-158; L §2.1 Ej. 6 p.102 ($\lvert x-2\rvert$) |
| «Cómo deja de ser derivable» (esquinas, tangentes verticales, discontinuidades) | S §2.8 p.159; L §2.1 Ej. 7 p.102 ($\sqrt[3]{x}$) |
| $\lim\frac{\operatorname{sen}x}{x}=1$ sin círculo vicioso (U lo hace con L'Hôpital) | S §3.3 p.192 (prueba geométrica); L §1.3 Teorema 1.9 p.65 |
| Derivadas laterales, que U coloca en §2.2 (p.81) aunque E las ejercita en 2.1 | L §2.1 pp.101-102 |
| Derivabilidad de $\lvert f\rvert$ (ejercicios 2.21-2.22) | No está en U, S ni L como resultado; ver el cuadro del ej. 2.22 |

## (c) Erratas y omisiones de E

1. **Ej. 2.2 (p.52).** «$3/0{,}0541\approx55{,}3914$» es incoherente: $3/0{,}0541\approx55{,}45$ y el valor exacto es $720/13\approx55{,}38$ km/h. Además no se responde explícitamente la pregunta (sí, multa).
2. **Ej. 2.9 (p.57).** «La función $f$ es periódica» es falso. La gráfica mostrada no corresponde a ninguna primitiva de $f'$: debería tener un mínimo en 0 y máximos en $\pm1$.
3. **Ej. 2.22 (p.65).** Denominador $x$ en lugar de $x-a$ en la fórmula final de $|f|'(a)$.
4. **Ej. 2.20 (p.63) y 2.23 (p.65).** $\lim\frac{\operatorname{sen}h}{h}$ y $\lim\frac{\operatorname{sen}(ah+k\pi)}{h}$ se calculan con L'Hôpital (U §2.3, sección posterior). Es circular para $\operatorname{sen}h/h$; basta la definición de derivada.
5. **Ej. 2.17 (p.62).** La solución es correcta, pero no advierte que la hipótesis $f'(a^-)=f'(a^+)$ es innecesaria para la continuidad.
6. **Ej. 2.14 (p.60).** No justifica por qué existe $n$ con $f(\frac1n)f(1-\frac1n)<0$; falta citar la conservación del signo (U Prop. 1.9 p.44).
7. **Fallos de extracción** (en el PDF están bien, no son erratas): $\ne$ en 2.21, 2.22 d) y en el margen de p.55; $\sqrt{|x|}$ en 2.20 d); el enunciado de 2.23, que sale desordenado; en U p.75 «$(a-r,a+r)\cap(D\setminus\{a\})\ne\emptyset$».
