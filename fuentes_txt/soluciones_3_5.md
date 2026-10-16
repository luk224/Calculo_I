# Soluciones Tema 3.5 — Concavidad y convexidad

Resolución paso a paso de los ejercicios de **E** de la sección 3.5 (3.39-3.43, 3.45-3.48 y la parte de 3.5 de 3.30 y 3.36), de los problemas de examen **X** de 3.5 (o 3.4 + 3.5) y de 4 ejemplos propios. Todos los cálculos se han comprobado con sympy (salidas resumidas al final de cada bloque). Los enunciados y las soluciones de E, X y las páginas de U §3.5 se han leído **como imagen** (páginas renderizadas con PyMuPDF), no del `.txt`.

Páginas: U impresa (= PDF + 2); E impresa = PDF; X = página PDF de `Examenes-resueltos-Calculo.pdf`.

## 0. Herramientas de teoría que se usan

| Clave | Enunciado (resumido) | Dónde |
|---|---|---|
| **Def. 3.8** | $f$ es **convexa** en un intervalo $I$ si $f((1-t)x+ty)\le(1-t)f(x)+tf(y)$ para todo $x,y\in I$ y todo $t\in[0,1]$. Geometría: entre $x$ e $y$ la gráfica está **por debajo del segmento** (cuerda) que une $(x,f(x))$ y $(y,f(y))$. Forma de $\bigcup$. | U §3.5.2, p. 135 |
| **Def. 3.9** | $f$ es **cóncava** en $I$ si $-f$ es convexa en $I$ (gráfica **por encima** de la cuerda; forma de $\bigcap$). | U §3.5.2, p. 135 |
| Ej. 3.28 | $x^3$ no es convexa ni cóncava en $[-1,1]$ (comprobado con la definición). «Una función puede no ser cóncava ni convexa en un intervalo». | U p. 136 |
| **Prop. 3.9** | $f$ derivable en $I$: $f$ convexa en $I$ $\iff$ $f'$ creciente en $I$; $f$ cóncava $\iff$ $f'$ decreciente. | U p. 136 |
| **Prop. 3.10** | $f$ dos veces derivable en $I$: $f''\ge0$ en $I$ $\Rightarrow$ convexa; $f''\le0$ $\Rightarrow$ cóncava. | U p. 136 |
| **Def. 3.10** | **Punto de inflexión**: punto en el que $f$ pasa de cóncava a convexa o al revés; es decir, existe $\varepsilon>0$ con $f$ convexa en $(c-\varepsilon,c)$ y cóncava en $(c,c+\varepsilon)$, o viceversa. | U p. 137 |
| **Prop. 3.11** | Si $f$ es dos veces derivable en $I$ y $c\in I$ es de inflexión, entonces $f''(c)=0$. (Condición **necesaria**, no suficiente.) | U p. 137 |
| **Prop. 3.12** | Si $f''(c)=0$ y la primera derivada de orden $>2$ que no se anula en $c$ es de orden **impar**, hay inflexión en $c$: de cóncava a convexa si esa derivada es positiva, de convexa a cóncava si es negativa. | U p. 137 |
| Ej. 3.29, 3.30 | $x^4-x^3-3x^2+10x+1$ (inflexiones $-\tfrac12$ y $1$); $\operatorname{tg}x$ y $-x^5$ en $0$. | U pp. 137-138 |
| Representación gráfica | Dominio, continuidad, asíntotas, crecimiento, extremos, concavidad e inflexiones. | U p. 139 |
| **Asíntotas** | Horizontal $y=b$: $\lim_{x\to\pm\infty}f(x)=b$. Vertical $x=a$: $\lim_{x\to a^\pm}f(x)=\pm\infty$. Oblicua $y=mx+b$ ($m\ne0$): $\lim_{x\to\pm\infty}[f(x)-(mx+b)]=0$; se calcula $m=\lim_{x\to\pm\infty}\frac{f(x)}{x}$ (Prop. 1.12) y después $b=\lim_{x\to\pm\infty}[f(x)-mx]$. | U §1.4, pp. 48-50 (Prop. 1.12 p. 49, Ej. 1.48 pp. 49-50) |
| Monotonía | Def. 2.5 (creciente: $a<b\Rightarrow f(a)\le f(b)$, **no estricto**) y Prop. 2.4 ($f'>0\Rightarrow$ estrictamente creciente, etc.). | U §2.5.4, p. 98 |
| TVM | $f$ continua en $[a,b]$ y derivable en $(a,b)$ $\Rightarrow$ $\frac{f(b)-f(a)}{b-a}=f'(\xi)$ para algún $\xi\in(a,b)$. | U §2.5.3, p. 96 |
| Prop. 3.7 | $f'(c)=0$, $f''(c)>0\Rightarrow$ mínimo relativo; $f''(c)<0\Rightarrow$ máximo relativo. | U §3.4.3, p. 131 |

**Vocabulario (aviso para quien use Stewart o Larson).** U dice **convexa** = S/L «cóncava hacia arriba» ($\bigcup$); U **cóncava** = S/L «cóncava hacia abajo» ($\bigcap$). En el examen se usa el de U.

**Tres observaciones que U no dice explícitamente y que los ejercicios usan:**
1. *Candidatos a inflexión.* Si $f$ es dos veces derivable, solo los ceros de $f''$ (Prop. 3.11). Pero también puede haber inflexión donde $f''$ **no existe** (E 3.40 en $x=4$, E 3.48 y X9 en $x=0$), siempre que el punto **esté en el dominio** de $f$ (E 3.43, E 3.46, X4: no hay inflexión en una asíntota vertical). Larson lo enuncia así: «si $(c,f(c))$ es de inflexión, entonces $f''(c)=0$ o $f''$ no existe en $c$» (L §3.4, Teorema 3.8, p. 190).
2. *La convexidad se dice de un intervalo.* Escribir «convexa en $(-\infty,-2)\cup(2,\infty)$» es incorrecto: hay que decir «convexa en $(-\infty,-2)$ y en $(2,\infty)$» (lo explica la propia solución de X7; E 3.41 y 3.45 muestran por qué).
3. *Recíproco de la Prop. 3.10.* Si $f$ es dos veces derivable y convexa en $I$, entonces $f''\ge0$ en $I$ (por la Prop. 3.9, $f'$ es creciente, y la derivada de una función creciente es $\ge0$). Por eso «$f'$ creciente $\Leftrightarrow$ $f''\ge0$ $\Leftrightarrow$ convexa» cuando $f$ es dos veces derivable.

---

## 1. Ejercicios de E (orden de dificultad creciente; numeración conservada)

Orden propuesto para aprender: **3.39 → 3.30 → 3.43 → 3.40 → 3.36 c) → 3.42 → 3.45 → 3.41 → 3.47 → 3.48 → 3.46**.

---

### Ejercicio 3.39 (E pp. 122-123)

> Sea $f$ la función dada por $f(x)=3x^5-5x^4-20x^3+2x-1$. ¿Cuándo es cóncava y cuándo convexa?

**Idea en una frase.** La concavidad la decide el **signo de $f''$**: se factoriza $f''$ y se hace una tabla de signos por intervalos.

1. **¿Se puede usar la Prop. 3.10?** $f$ es un polinomio: es dos veces derivable en todo $\mathbb R$. Sí.
2. **Derivar dos veces.** $f'(x)=15x^4-20x^3-60x^2+2$ y $f''(x)=60x^3-60x^2-120x$.
3. **Factorizar $f''$.** Sacar factor común $60x$: $f''(x)=60x(x^2-x-2)$. Las raíces de $x^2-x-2$ son $x=\frac{1\pm\sqrt{1+8}}{2}=2,\,-1$, así que $f''(x)=60x(x-2)(x+1)$.
   *Por qué factorizar:* un producto solo puede cambiar de signo donde se anula algún factor. Entre dos raíces consecutivas, $f''$ tiene signo constante (es continua y no se anula; Bolzano, U §1.4).
4. **Tabla de signos** (evaluar cada factor en un punto de prueba: $-2$, $-\tfrac12$, $1$, $3$):

| intervalo | $x+1$ | $x$ | $x-2$ | $f''$ | $f$ |
|---|---|---|---|---|---|
| $(-\infty,-1)$ | $-$ | $-$ | $-$ | $-$ | cóncava |
| $(-1,0)$ | $+$ | $-$ | $-$ | $+$ | convexa |
| $(0,2)$ | $+$ | $+$ | $-$ | $-$ | cóncava |
| $(2,\infty)$ | $+$ | $+$ | $+$ | $+$ | convexa |

5. **Conclusión (Prop. 3.10).** $f$ es **convexa en $[-1,0]$ y en $[2,\infty)$** y **cóncava en $(-\infty,-1]$ y en $[0,2]$**. (Se pueden cerrar los intervalos porque en los extremos $f''=0$, que cumple a la vez $\ge0$ y $\le0$.)
6. **Extra (no se pide): inflexiones.** $f''$ cambia de signo en $-1$, $0$ y $2$ $\Rightarrow$ tres puntos de inflexión (Def. 3.10): $(-1,9)$, $(0,-1)$, $(2,-141)$. Con la Prop. 3.12: $f'''(-1)=180>0$ (cóncava → convexa), $f'''(0)=-120<0$ (convexa → cóncava), $f'''(2)=360>0$ (cóncava → convexa).

**Receta.** Concavidad de un polinomio: $f''$ → factorizar → tabla de signos → $f''\ge0$ convexa, $f''\le0$ cóncava; donde cambia el signo, inflexión.
**Error típico.** Estudiar el signo de $f'$ en vez del de $f''$ (eso da crecimiento, no concavidad); o escribir «convexa en $[-1,0]\cup[2,\infty)$» (ver observación 2).

Verificación sympy: $f''=60x(x-2)(x+1)$; $f(-1)=9$, $f(0)=-1$, $f(2)=-141$; $f'''(-1),f'''(0),f'''(2)=180,-120,360$. Coincide con E.

---

### Ejercicio 3.30, parte de inflexión (E p. 114)

> Sea $f$ la función dada por $f(x)=ax^3+bx^2+cx+d$, para $a,b,c,d\in\mathbb R$ con $a\ne0$. ¿Es cierto que $f$ tiene exactamente un máximo local y un mínimo local en su dominio, cualesquiera que sean $a,b,c,d$?

(La parte de extremos está resuelta en `soluciones_3_4.md`: la respuesta es **no**; contraejemplos $2x^3+6x$, sin puntos críticos, y $x^3$, con un punto crítico que no es extremo.) Aquí se completa lo que toca a 3.5.

**Idea en una frase.** Toda cúbica tiene **exactamente un** punto de inflexión, en $x=-\frac{b}{3a}$; la raíz doble de $f'$ del ejemplo $x^3$ es un caso particular en el que la inflexión además tiene tangente horizontal.

1. $f''(x)=6ax+2b$. Es una recta con pendiente $6a\ne0$: se anula en un solo punto, $x_0=-\dfrac{b}{3a}$, y **cambia de signo** allí.
2. Por la Def. 3.10 (o por la Prop. 3.12, ya que $f'''(x_0)=6a\ne0$, de orden 3, impar), $x_0$ es **el único punto de inflexión**. Si $a>0$, pasa de cóncava a convexa; si $a<0$, al revés.
3. En $f=x^3$: $x_0=0$ y $f'(0)=0$ → inflexión con tangente horizontal (y no es extremo). En $f=2x^3+6x$: $x_0=0$ pero $f'(0)=6\ne0$ → inflexión con tangente inclinada.

**Errata en E (p. 114).** La solución empieza: «Como los extremos locales **y los puntos de inflexión** de una función derivable en todo $\mathbb R$ se alcanzan en puntos donde se anula su derivada». Para la inflexión eso es falso: el candidato se busca con $f''=0$ (U Prop. 3.11), y $2x^3+6x$, el propio contraejemplo de E, tiene inflexión en $0$ con $f'(0)=6\ne0$. La respuesta («no es cierto») no cambia.

**Receta.** Inflexión: candidatos con $f''=0$ (no con $f'=0$), y comprobar que $f''$ cambia de signo (o Prop. 3.12).
**Error típico.** El de E: confundir los candidatos a extremo ($f'=0$) con los candidatos a inflexión ($f''=0$).

Verificación sympy: $f''=2(3ax+b)$.

---

### Ejercicio 3.43 (E pp. 125-126)

> Sea $f$ la función dada por: $f(x)=\dfrac{1}{1-x}$. ¿Alcanza extremos relativos? ¿Tiene algún punto de inflexión?

**Idea en una frase.** La concavidad cambia al cruzar $x=1$, pero $x=1$ **no está en el dominio** (es una asíntota vertical): no puede ser punto de inflexión.

1. **Dominio.** $\mathbb R\setminus\{1\}$. En él, $f$ es cociente de funciones derivables con denominador no nulo: derivable tantas veces como se quiera.
2. **Extremos.** $f'(x)=\dfrac{1}{(1-x)^2}>0$ en todo el dominio. Nunca vale $0$ y no hay puntos de no derivabilidad dentro del dominio, así que no hay puntos críticos (U Def. 3.5, p. 126) ni, por tanto, extremos relativos (Prop. 3.6, p. 131). Además $f$ es estrictamente creciente en $(-\infty,1)$ y en $(1,\infty)$ (Prop. 2.4).
3. **Concavidad.** $f''(x)=\dfrac{2}{(1-x)^3}$. Si $x<1$, $1-x>0$ y $f''>0$: **convexa en $(-\infty,1)$**. Si $x>1$, $1-x<0$ y $f''<0$: **cóncava en $(1,\infty)$**.
4. **¿Inflexión?** Un punto de inflexión es un punto $c$ **de la gráfica** donde cambia la concavidad (Def. 3.10). El cambio ocurre «a través» de $x=1$, pero $f(1)$ no existe. Y $f''$ no se anula en ningún punto del dominio, así que por la Prop. 3.11 tampoco hay otro candidato. **No tiene puntos de inflexión.**
5. **Asíntota.** $\lim_{x\to1^-}f(x)=+\infty$ y $\lim_{x\to1^+}f(x)=-\infty$: $x=1$ es asíntota vertical (U p. 49).

**Receta.** Antes de declarar una inflexión, comprobar que el punto está **en el dominio** de $f$.
**Error típico.** Ver el cambio de signo de $f''$ en la tabla y anotar «inflexión en $x=1$».

Verificación sympy: $f'=(x-1)^{-2}$, $f''=-2/(x-1)^3=2/(1-x)^3$.

---

### Ejercicio 3.40 (E p. 123)

> Sea $f$ la función dada por $f(x)=x\,\lvert x-4\rvert$. Es cierto que: **a)** Es cóncava en $(4,+\infty)$. **b)** Es convexa en $(-4,4)$. **c)** En $x=4$ tiene un punto de inflexión. **d)** Ninguna de las anteriores.

**Idea en una frase.** Quitando el valor absoluto, $f$ es una parábola «hacia abajo» a la izquierda de $4$ y una «hacia arriba» a la derecha: en $x=4$ cambia la concavidad, aunque allí no haya derivada.

1. **Quitar el valor absoluto.** Si $x<4$, $\lvert x-4\rvert=4-x$ y $f(x)=-x(x-4)=-x^2+4x$. Si $x\ge4$, $f(x)=x(x-4)=x^2-4x$.
2. **Derivadas fuera de $4$.** Si $x<4$: $f'(x)=-2x+4$, $f''(x)=-2<0$. Si $x>4$: $f'(x)=2x-4$, $f''(x)=2>0$.
3. **Concavidad (Prop. 3.10).** Cóncava en $(-\infty,4)$ y convexa en $(4,\infty)$.
4. **Descartar a) y b).** a): en $(4,\infty)$ es convexa y no cóncava ($f''=2>0$ y no es una recta). b): $(-4,4)\subset(-\infty,4)$, donde $f''=-2<0$: es cóncava, no convexa.
5. **c) ¿Inflexión en $4$?** $f$ es continua en $4$ ($f(4)=0$ y ambos trozos tienden a $0$), $4$ está en el dominio, y existe $\varepsilon>0$ (cualquiera) con $f$ cóncava en $(4-\varepsilon,4)$ y convexa en $(4,4+\varepsilon)$. Por la **Def. 3.10**, sí: **c) es correcta**.
6. **¿Contradice la Prop. 3.11?** No: $f$ **no es derivable** en $4$ ($f'(4^-)=-4$, $f'(4^+)=4$), así que la Prop. 3.11 no se aplica. Es un ejemplo de inflexión donde $f''$ no existe (observación 1).

**Respuesta: c).**

**Nota sobre el `.txt`.** En el `.txt` parece que E dice «$f$ es derivable si $x=4$»; en el PDF pone **$x\ne4$** (la barra se pierde al extraer). No es errata de E.

**Receta.** Valor absoluto → escribir a trozos → $f''$ en cada trozo → buscar inflexión también en el punto de unión (si es del dominio y $f$ es continua allí).
**Error típico.** Descartar c) porque «$f''(4)$ no existe, luego no puede ser inflexión».

Verificación sympy: $f''=-2$ y $2$; $f'(4^\mp)=\mp4$.

---

### Ejercicio 3.36 c) (E p. 120)

> La gráfica de la derivada de una función dos veces derivable $f$ con dominio todo $\mathbb R$ aparece en la siguiente figura. Razona si alguna de las siguientes afirmaciones es correcta: **a)** $f$ tiene dos puntos críticos, pero un solo extremo relativo. **b)** $f$ tiene dos extremos relativos. **c)** La ecuación $f''(x)=0$ no tiene soluciones reales.

(Figura de E p. 120: $f'$ corta al eje en $x=-2$ pasando de $-$ a $+$, sube hasta un máximo de altura $2$ en un punto $x_0\in(-1,0)$, baja hasta tocar el eje en $x=1$ (mínimo, valor $0$) y vuelve a subir. Apartados a) y b): ver `soluciones_3_4.md`; a) correcta, b) falsa.)

**Idea en una frase.** $f''$ es la derivada de $f'$: se anula donde la gráfica de $f'$ tiene **tangente horizontal** (sus máximos y mínimos).

1. $f$ es dos veces derivable, así que $f'$ es derivable y $f''=(f')'$.
2. En la figura, $f'$ tiene un **máximo relativo** en $x_0\in(-1,0)$ y un **mínimo relativo** en $x=1$. En un extremo relativo interior de una función derivable, su derivada vale $0$ (U Prop. 3.6, aplicada a $f'$): $f''(x_0)=0$ y $f''(1)=0$.
3. **c) es falsa**: la ecuación $f''(x)=0$ tiene al menos dos soluciones reales. (Coincide con E.)
4. **Extra (3.5):** $f'$ crece en $(-\infty,x_0)$, decrece en $(x_0,1)$ y crece en $(1,\infty)$. Por la **Prop. 3.9**: $f$ es convexa en $(-\infty,x_0]$, cóncava en $[x_0,1]$ y convexa en $[1,\infty)$; $x_0$ y $1$ son **puntos de inflexión**. Fíjate en que $x=1$ es a la vez punto crítico de $f$ ($f'(1)=0$) e inflexión: es el «punto de silla» de a).

**Receta.** Con la gráfica de $f'$: ceros de $f'$ → críticos de $f$; **extremos de $f'$** → ceros de $f''$ (candidatos a inflexión); tramos donde $f'$ sube → $f$ convexa; donde baja → $f$ cóncava.
**Error típico.** Buscar los ceros de $f''$ donde $f'$ corta al eje (esos son los ceros de $f'$).

---

### Ejercicio 3.42 (E p. 125)

> De una función $f:\mathbb R\to\mathbb R$ tres veces derivable conocemos la gráfica de su derivada primera $f'$ que mostramos a continuación. Razona si las siguientes afirmaciones son correctas. **a)** La función $f$ es cóncava en $(-\infty,0)$. **b)** La función $f$ es convexa si $(-\infty,0)$. **c)** La función $f$ tiene un punto de inflexión en $x=1$.

(Figura: $f'\ge0$; baja hasta $0$ en $x=0$, sube a un máximo pequeño en $x=0{,}5$, baja a $0$ en $x=1$ y sube de nuevo. Una fórmula compatible con la figura es $f'(x)=x^2(x-1)^2$, que vale $\tfrac1{16}$ en $0{,}5$.)

**Idea en una frase.** Leer en la gráfica de $f'$ dónde **sube** y dónde **baja**; eso es, por la Prop. 3.9, dónde $f$ es convexa y dónde cóncava.

1. **Tramos de monotonía de $f'$** (lectura de la figura): decreciente en $(-\infty,0]$, creciente en $[0;\,0{,}5]$, decreciente en $[0{,}5;\,1]$, creciente en $[1,\infty)$.
2. **a) y b).** $f$ es derivable y $f'$ es decreciente en $(-\infty,0)$ $\Rightarrow$ $f$ **cóncava** en $(-\infty,0)$ (Prop. 3.9). **a) correcta.** b) diría convexa: si lo fuese, $f'$ sería creciente allí (Prop. 3.9), y la figura muestra que es estrictamente decreciente. **b) falsa.**
3. **c).** En $(0{,}5;\,1)$ $f'$ decrece → $f$ cóncava; en $(1,\infty)$ $f'$ crece → $f$ convexa. Hay cambio de concavidad en $x=1$, que está en el dominio: **inflexión en $x=1$** (Def. 3.10). **c) correcta.**
4. **Extra.** Igual se ve que $x=0$ (cóncava → convexa) y $x=0{,}5$ (convexa → cóncava) también son de inflexión. En los tres $f''=0$ (son extremos de $f'$), como exige la Prop. 3.11. $x=0$ y $x=1$ son además puntos críticos de $f$ que no son extremos ($f'\ge0$: $f$ crece a ambos lados).

**Errata tipográfica en E.** En b) falta «en»: «convexa **en** $(-\infty,0)$» (confirmado en la imagen).

**Receta.** Gráfica de $f'$: sube ⇒ $f$ convexa; baja ⇒ $f$ cóncava; cada máximo o mínimo de $f'$ es una inflexión de $f$.
**Error típico.** Mirar el **signo** de $f'$ ($f'\ge0$ en todo $\mathbb R$) y concluir algo de la concavidad: el signo de $f'$ da el crecimiento de $f$; la concavidad la da la **monotonía** de $f'$.

Verificación sympy (con el modelo $f'=x^2(x-1)^2$): $f''=2x(x-1)(2x-1)$, negativo en $(-\infty,0)$ y en $(\tfrac12,1)$, positivo en $(0,\tfrac12)$ y en $(1,\infty)$.

---

### Ejercicio 3.45 (E pp. 127-128)

> Sea $f:\mathbb R\to\mathbb R$ una función dos veces derivable con continuidad en $\mathbb R\setminus\{1\}$. Su derivada se representa en la siguiente figura. A partir de la gráfica de $f'$, ¿cuáles son los intervalos de concavidad y convexidad de la función $f$? ¿Tiene puntos de inflexión? ¿Es convexa en $\mathbb R$?

(Figura: dos ramas de $f'$ separadas por la recta $x=1$. Rama izquierda: creciente, pasa por $(0,0)$ y tiende a $+\infty$ cuando $x\to1^-$. Rama derecha: creciente, viene de $-\infty$ cuando $x\to1^+$ y corta al eje en $x=2$.)

**Idea en una frase.** $f'$ sube en cada lado, así que $f$ es convexa a cada lado; pero al cruzar $x=1$ la pendiente pasa de «muy positiva» a «muy negativa», y eso es un pico $\bigwedge$: **no** puede ser convexa en todo $\mathbb R$.

1. **Intervalos.** En $(-\infty,1)$ $f$ es derivable y $f'$ es creciente $\Rightarrow$ **convexa en $(-\infty,1)$** (Prop. 3.9). Igual en $(1,\infty)$: **convexa en $(1,\infty)$**. (Equivalente: $f''\ge0$ en cada uno, Prop. 3.10.) No es cóncava en ningún intervalo abierto, porque $f'$ no decrece en ningún tramo.
2. **Inflexiones.** No hay: a ambos lados de cualquier punto $f$ es convexa, nunca cambia a cóncava (Def. 3.10).
3. **¿Convexa en $\mathbb R$? No.** Intuición: justo antes de $1$ la gráfica sube con pendiente enorme y justo después baja con pendiente enorme: cerca de $1$ tiene forma de $\bigcap$, que es lo contrario de convexa.
4. **Argumento riguroso (con la Def. 3.8 y el TVM).**
   - *Hecho previo (pendientes crecientes).* Si $f$ es convexa en un intervalo y $p<q<r$ están en él, la pendiente de la cuerda $[p,q]$ es $\le$ la de la cuerda $[q,r]$. (Basta escribir $q=(1-t)p+tr$ con $t=\frac{q-p}{r-p}$ en la Def. 3.8, multiplicar por $r-p$ y reordenar: $(r-q)\,(f(q)-f(p))\le(q-p)\,(f(r)-f(q))$.) Gráficamente: en una $\bigcup$ las cuerdas se van empinando de izquierda a derecha.
   - Supón que $f$ fuese convexa en $\mathbb R$. Toma $p=0{,}5<q=0{,}6<r=1{,}2<s=1{,}3$. Aplicando el hecho dos veces: $\dfrac{f(q)-f(p)}{q-p}\le\dfrac{f(r)-f(q)}{r-q}\le\dfrac{f(s)-f(r)}{s-r}$.
   - $f$ es derivable en $[0{,}5;\,0{,}6]$ y en $[1{,}2;\,1{,}3]$ (no contienen a $1$), así que por el TVM (U p. 96) la primera pendiente es $f'(\xi)$ con $\xi\in(0{,}5;\,0{,}6)$ y la última es $f'(\eta)$ con $\eta\in(1{,}2;\,1{,}3)$.
   - En la figura, $f'>0$ en $(0,1)$ y $f'<0$ en $(1,2)$. Quedaría «positivo $\le$ negativo»: contradicción. **$f$ no es convexa en $\mathbb R$**, sea o no continua en $1$.

**Errata en E (p. 128).** E dice: «Sin embargo, no podemos saber si es convexa en $\mathbb R$ con los datos facilitados. Podría serlo o no. Fíjate en que $f$ puede ser discontinua en $x=1$». Es **incorrecto**: con la gráfica dada **sí** se sabe que no es convexa en $\mathbb R$ (paso 4). El salto de $f'$ de $+\infty$ a $-\infty$ lo impide aunque $f$ fuese continua en $1$ (por ejemplo, $-\sqrt{\lvert x-1\rvert}$ tiene una derivada de ese tipo cerca de $1$, es convexa a cada lado y no lo es en $\mathbb R$; compárese con E 3.41).

**Receta.** «¿Convexa en todo $\mathbb R$?» cuando hay un punto malo $c$: la derivada (donde exista) tiene que seguir siendo creciente **al cruzar $c$**; si $f'$ «salta hacia abajo» en $c$, no es convexa.
**Error típico.** Unir los intervalos: «convexa en $(-\infty,1)$ y en $(1,\infty)$, luego convexa en $\mathbb R$».

---

### Ejercicio 3.41 (E pp. 123-124)

> La función dada por $f(x)=\sqrt{\lvert x\rvert}$ es continua en $\mathbb R$ y tiene derivada segunda negativa en $\mathbb R\setminus\{0\}$. Muestra que no es cóncava en $\mathbb R$.

(Ojo: el enunciado real es $\sqrt{\lvert x\rvert}$, no $\lvert x\rvert$ como decía el dossier; confirmado en la imagen de E p. 123.)

**Idea en una frase.** Para probar que **no** es cóncava basta **un** contraejemplo a la definición: una cuerda que quede **por encima** de la gráfica.

1. **Por qué no sirve la Prop. 3.10.** Si $x>0$, $f(x)=\sqrt x$ y $f''(x)=-\frac{1}{4x^{3/2}}<0$; si $x<0$, $f(x)=\sqrt{-x}$ y $f''(x)=-\frac{1}{4(-x)^{3/2}}<0$. Pero en $0$ no existe $f''$ (ni siquiera $f'$: la gráfica tiene un pico en $0$), y la Prop. 3.10 exige $f$ dos veces derivable **en todo el intervalo**. Así que no se puede concluir «cóncava en $\mathbb R$».
2. **Qué hay que contradecir.** Cóncava en $\mathbb R$ significaría (Def. 3.9: $-f$ convexa) $f((1-t)a+tb)\ge(1-t)f(a)+tf(b)$ para todo $a,b\in\mathbb R$ y $t\in[0,1]$ (gráfica por encima de la cuerda).
3. **Elegir $a$ y $b$.** Tienen que estar a lados opuestos de $0$ (si no, $[a,b]$ no contiene a $0$ y ahí $f''<0$ sí da concavidad). Tomamos $a=-1$, $b=1$: $f(-1)=f(1)=1$, y la cuerda es el segmento horizontal de altura $1$.
4. **El punto medio ($t=\tfrac12$).** $(1-t)a+tb=0$ y $f(0)=0$. La cuerda en ese punto vale $\tfrac12\cdot1+\tfrac12\cdot1=1$. Como $0<1$, la gráfica está **por debajo** de la cuerda: falla la desigualdad de concavidad.
5. **Conclusión.** $f$ no es cóncava en $\mathbb R$. Sí es cóncava en $(-\infty,0]$ y en $[0,\infty)$ por separado: la concavidad **no se conserva al unir intervalos**.

**Erratas / avisos en E (p. 124).**
- E escribe: «Para $t=1/2$ resulta $\sqrt{\lvert2t-1\rvert}=0$, **que no es menor que 1**». Debe decir «que **es** menor que $1$» (o «que no es mayor o igual que $1$»): justo eso rompe la desigualdad $\sqrt{\lvert2t-1\rvert}\ge1$.
- E remite a «el Ejercicio 3» para las derivadas de $\sqrt{\lvert x\rvert}$. No hemos encontrado en E ningún ejercicio que estudie esa función: la remisión parece rota. Las derivadas están en el paso 1.

**Receta.** Para negar la concavidad/convexidad en un intervalo: elegir dos puntos a ambos lados del punto problemático y comprobar el punto medio ($t=\tfrac12$).
**Error típico.** «$f''<0$ en todos los puntos donde existe, luego es cóncava». Falla en cuanto hay dentro del intervalo un punto sin $f''$.

Verificación sympy: $f''(x)=-\tfrac14x^{-3/2}$ ($x>0$) y $-\tfrac14(-x)^{-3/2}$ ($x<0$).

---

### Ejercicio 3.47 (E pp. 131-133)

> Da una expresión, si es posible, que defina una función real de una variable real que verifique las propiedades que se indican en cada apartado:
> **a)** Derivable en su dominio, creciente en el intervalo $(-\infty,2)$ y decreciente en el intervalo $(2,+\infty)$.
> **b)** Derivable en su dominio, estrictamente creciente en el intervalo $(-\infty,2)$ y estrictamente decreciente en el intervalo $(2,+\infty)$.
> **c)** Derivable en su dominio, convexa en el intervalo $(-\infty,0)$ y cóncava en el intervalo $(0,+\infty)$.
> **d)** Derivable en su dominio y con asíntota vertical $x=-\pi$.
> **e)** Positiva en $(-\infty,1)$, con gráfica que corta al eje $x$ en $(2,0)$ y al eje $y$ en $(0,-3)$.

**Idea en una frase.** Partir de una función «modelo» conocida ($-x^2$, $x^3$, $\ln x$…), trasladarla o cambiarle el signo, y comprobarla derivando.

1. **a) $f(x)=\pi$** (o cualquier constante). Es derivable y, con la **Def. 2.5 de U (no estricta, p. 98)**, una constante es creciente y decreciente en cualquier intervalo ($a<b\Rightarrow f(a)\le f(b)$ y $f(b)\le f(a)$). También vale la de b).
2. **b) $f(x)=-(x-2)^2$.** $f'(x)=-2(x-2)$: $>0$ si $x<2$ y $<0$ si $x>2$ → estrictamente creciente en $(-\infty,2)$ y estrictamente decreciente en $(2,\infty)$ (Prop. 2.4). Es $-x^2$ trasladada para que el vértice esté en $x=2$.
3. **c) $f(x)=-x^3$.** $f''(x)=-6x$: $>0$ si $x<0$ (convexa) y $<0$ si $x>0$ (cóncava) (Prop. 3.10). También vale $\operatorname{arctg}x$ ($f''=\frac{-2x}{(1+x^2)^2}$, mismos signos) y, con la Def. 3.8 (que usa $\le$), la constante $\pi$ o la recta $f(x)=x$, que son a la vez convexas y cóncavas en cualquier intervalo (caso límite). **No vale $\operatorname{tg}x$**: no está definida en $-\frac\pi2,-\frac{3\pi}2,\dots$, así que no tiene sentido decir que es convexa «en $(-\infty,0)$»; y además en $(-\frac\pi2,0)$ es cóncava ($f''=\frac{2\operatorname{sen}x}{\cos^3x}<0$), justo al revés de lo pedido.
4. **d) $f(x)=\ln(x+\pi)$** (dominio $(-\pi,\infty)$, $\lim_{x\to-\pi^+}f(x)=-\infty$) o **$f(x)=\dfrac1{x+\pi}$** ($\lim_{x\to-\pi^\pm}f(x)=\pm\infty$). Ambas derivables en su dominio; $x=-\pi$ es asíntota vertical (U p. 49).
5. **e) No existe.** $0\in(-\infty,1)$, así que «positiva en $(-\infty,1)$» exige $f(0)>0$; pero «corta al eje $y$ en $(0,-3)$» dice $f(0)=-3<0$. Contradicción.

**Avisos sobre E.** (i) En d) E escribe «Para **el tercero**», pero es el cuarto apartado (d): numeración confusa. (ii) a) con $f=\pi$ es correcto **solo** porque U define «creciente» en sentido no estricto; conviene decirlo, porque muchos alumnos piensan que una constante «no crece». (iii) En c), «la más sencilla $f(x)=x$» es convexa y cóncava a la vez (Def. 3.8 con $\le$): válido, pero degenerado; en el examen es más seguro dar $-x^3$ o $\operatorname{arctg}x$.

**Receta.** Construir ejemplos: modelo + traslación ($x\mapsto x-a$) + cambio de signo; comprobar con $f'$ (monotonía) o $f''$ (concavidad). Si dos condiciones hablan del mismo punto, comprobar que sean compatibles (e).
**Error típico.** Dar $\operatorname{tg}x$ en c) sin mirar su dominio ni el signo de $f''$.

Verificación sympy: $(-x^3)''=-6x$; $(\operatorname{arctg}x)''=-2x/(x^2+1)^2$; $(\operatorname{tg}x)''=2\operatorname{tg}x/\cos^2x$; $(-(x-2)^2)'=-2(x-2)$.

---

### Ejercicio 3.48 (E pp. 133-134)

> Dibuja la gráfica de una función continua que sea decreciente en todo $\mathbb R$, cóncava en $(-\infty,0)$, convexa en $(0,+\infty)$ y tenga dos asíntotas (una horizontal y una oblicua).

**Idea en una frase.** $-\operatorname{arctg}x$ ya baja, es cóncava a la izquierda y convexa a la derecha y tiene asíntotas horizontales; para conseguir una **oblicua** a la derecha se le suma la recta $-\tfrac x2$ solo para $x>0$ (una recta no cambia $f''$).

1. **Propuesta (E):** $f(x)=\begin{cases}-\operatorname{arctg}x,& x\le0,\\  -\tfrac x2-\operatorname{arctg}x,& x>0.\end{cases}$
2. **Continua.** Cada trozo es continuo. En $0$: $f(0)=0$ y $\lim_{x\to0^+}\big(-\tfrac x2-\operatorname{arctg}x\big)=0$.
3. **Decreciente.** $x<0$: $f'(x)=-\frac1{1+x^2}<0$. $x>0$: $f'(x)=-\frac12-\frac1{1+x^2}<0$. Cada trozo es estrictamente decreciente (Prop. 2.4) y, como $f$ es continua en $0$, lo es en todo $\mathbb R$ (si $a<0<b$: $f(a)>f(0)>f(b)$).
4. **Concavidad.** En ambos trozos $f''(x)=\dfrac{2x}{(1+x^2)^2}$ (la recta $-\tfrac x2$ tiene segunda derivada $0$). Si $x<0$, $f''<0$: **cóncava en $(-\infty,0)$**; si $x>0$, $f''>0$: **convexa en $(0,\infty)$** (Prop. 3.10). Por la Def. 3.10, $x=0$ es punto de inflexión, aunque $f$ no sea derivable en $0$ ($f'(0^-)=-1$, $f'(0^+)=-\tfrac32$).
5. **Asíntota horizontal.** $\lim_{x\to-\infty}f(x)=-\big(-\tfrac\pi2\big)=\tfrac\pi2$: $y=\tfrac\pi2$ (a la izquierda).
6. **Asíntota oblicua.** $m=\lim_{x\to+\infty}\frac{f(x)}{x}=-\tfrac12$ (Prop. 1.12) y $b=\lim_{x\to+\infty}\big(f(x)+\tfrac x2\big)=\lim_{x\to+\infty}(-\operatorname{arctg}x)=-\tfrac\pi2$: $y=-\tfrac x2-\tfrac\pi2$ (a la derecha).

**Comentario.** La solución de E es correcta. Solo falta decir que en $x=0$ $f$ no es derivable (el enunciado no lo exige) y que, por eso, la inflexión en $0$ no sale de $f''(0)=0$ sino de la Def. 3.10.

**Receta.** Gráfica con propiedades dadas: elegir una función base con la concavidad pedida y **sumarle una recta** en el lado donde haga falta una asíntota oblicua (no cambia $f''$; sí cambia $f'$, así que comprobar la monotonía).
**Error típico.** Sumar la recta con pendiente positiva ($+\tfrac x2$): se rompe «decreciente».

Verificación sympy: $f'=-1/(x^2+1)$ y $-(x^2+3)/(2(x^2+1))$; $f''=2x/(x^2+1)^2$ en ambos; $\lim_{x\to-\infty}f=\pi/2$; $\lim_{x\to+\infty}[f-(-x/2-\pi/2)]=0$.

---

### Ejercicio 3.46 (E pp. 128-131)

> Sea $f$ la función definida por $f(x)=\dfrac{x^2}{x-1}$. ¿Cuál es su representación gráfica?

(Enunciado confirmado en la imagen de E p. 128.)

**Idea en una frase.** Aplicar la lista de U p. 139 en orden (dominio → cortes → asíntotas → $f'$ → $f''$) y dibujar con todo junto.

1. **Dominio y regularidad.** $x-1\ne0$: dominio $\mathbb R\setminus\{1\}$. Ahí $f$ es cociente de polinomios con denominador no nulo: continua y derivable las veces que haga falta.
2. **Cortes con los ejes.** Eje $y$: $f(0)=0$ → $(0,0)$. Eje $x$: $\frac{x^2}{x-1}=0\iff x=0$. Único corte: el origen.
3. **Asíntota vertical.** $\lim_{x\to1^-}\frac{x^2}{x-1}=-\infty$ (numerador $\to1$, denominador $\to0^-$) y $\lim_{x\to1^+}\frac{x^2}{x-1}=+\infty$: **$x=1$** (U p. 49).
4. **Asíntotas horizontales.** $\lim_{x\to\pm\infty}f(x)=\pm\infty$: no hay.
5. **Asíntota oblicua.** $m=\lim_{x\to\pm\infty}\frac{x^2}{x(x-1)}=1$ y $b=\lim_{x\to\pm\infty}\Big(\frac{x^2}{x-1}-x\Big)=\lim_{x\to\pm\infty}\frac{x}{x-1}=1$: **$y=x+1$** en $\pm\infty$ (Prop. 1.12).
6. **Crecimiento.** $f'(x)=\frac{2x(x-1)-x^2}{(x-1)^2}=\frac{x(x-2)}{(x-1)^2}$. El denominador es $>0$; el signo es el de $x(x-2)$: $+$ en $(-\infty,0)$, $-$ en $(0,1)$ y en $(1,2)$, $+$ en $(2,\infty)$. Estrictamente creciente en $(-\infty,0)$ y $(2,\infty)$; estrictamente decreciente en $(0,1)$ y $(1,2)$ (Prop. 2.4).
7. **Extremos.** $f'=0\iff x=0$ o $x=2$. Con $f''$ (paso 8): $f''(0)=-2<0$ → **máximo relativo** $(0,0)$; $f''(2)=2>0$ → **mínimo relativo** $(2,4)$ (Prop. 3.7). Ninguno es absoluto (hay límites $\pm\infty$ junto a la asíntota).
8. **Concavidad.** $f''(x)=\frac{(2x-2)(x-1)^2-(x^2-2x)\cdot2(x-1)}{(x-1)^4}=\frac{2\big[(x-1)^2-(x^2-2x)\big]}{(x-1)^3}=\frac{2}{(x-1)^3}$ (el corchete vale $1$). $f''<0$ en $(-\infty,1)$: **cóncava**; $f''>0$ en $(1,\infty)$: **convexa** (Prop. 3.10).
9. **Inflexiones.** $f''$ no se anula nunca y el cambio de concavidad es en $x=1$, fuera del dominio: **no hay** (igual que E 3.43).
10. **Dibujo** (E Figura 3.5, p. 131; no confundir con la Figura 3.5 de U, p. 136). Rama izquierda: viene de abajo pegada a $y=x+1$, sube hasta el máximo $(0,0)$, cae a $-\infty$ junto a $x=1$; forma $\bigcap$. Rama derecha: baja desde $+\infty$ junto a $x=1$ hasta el mínimo $(2,4)$ y sube pegada a $y=x+1$; forma $\bigcup$. (Posición respecto a la oblicua: $f(x)-(x+1)=\frac1{x-1}$, positivo a la derecha y negativo a la izquierda.)

**Comentario.** Sin errores de cálculo en E. La nota al margen de E p. 128 sobre la asíntota oblicua («tiene una asíntota oblicua si $\lim_{x\to\pm\infty}f(x)/x=m$ … y es de la forma $y=mx+c$») está incompleta: además hace falta que $c=\lim_{x\to\pm\infty}(f(x)-mx)$ **exista y sea finito** (U Prop. 1.12 solo da una condición necesaria; contraejemplo de U, p. 49: $x+\operatorname{sen}x$). E sí lo calcula en el desarrollo.

**Receta (estudio completo).** Dominio → cortes → asíntotas (vertical en los ceros del denominador; oblicua con $m$ y $b$) → $f'$ factorizada: crecimiento y extremos → $f''$: concavidad e inflexiones (solo en puntos del dominio) → dibujo.
**Error típico.** Olvidar el punto $x=1$ en las tablas de signo de $f'$ y $f''$ (hay que partir los intervalos también en los puntos fuera del dominio).

Verificación sympy: $f'=x(x-2)/(x-1)^2$, $f''=2/(x-1)^3$, $m=1$, $b=1$ en $\pm\infty$, $f(2)=4$, límites laterales en $1$: $\mp\infty$.

---

## 2. Así lo preguntan en el examen (X)

La mayoría son de **Ingeniería Mecánica** (código 68031029); X9 y X10 son de **I. Electrónica Industrial y Automática** (sin fecha). El temario de Cálculo es el mismo. Orden: primero las de leer una gráfica, luego cálculo de $f''$, y al final las de estudio completo.

### X1. Septiembre 2011, Mecánica (X pp. 16-17), Pregunta corta 4 (1 punto)

> Sea $f:\mathbb R\to\mathbb R$ una función continua y derivable cinco veces cuya derivada segunda se representa en la siguiente figura. Determine sus puntos de inflexión y los intervalos de concavidad y convexidad. Razone la respuesta.

(Figura, X p. 17: $f''$ es una parábola con vértice en $(0,-1)$ que corta al eje en $x=-2$ y $x=2$.)

**Idea en una frase.** Con la gráfica de $f''$ basta mirar si está por encima o por debajo del eje.

1. $f''>0$ en $(-\infty,-2)$ y en $(2,\infty)$ → **convexa en $(-\infty,-2]$ y en $[2,\infty)$** (Prop. 3.10).
2. $f''<0$ en $(-2,2)$ → **cóncava en $[-2,2]$**.
3. $f''$ cambia de signo en $-2$ y en $2$ → **inflexión en $x=-2$ y $x=2$** (Def. 3.10).

**Precisión sobre la solución de X.** Escribe «convexa en $(-\infty,-2)\cup(2,\infty)$». Según la Def. 3.8, la convexidad es en **un intervalo**; lo correcto es «en $(-\infty,-2)$ y en $(2,\infty)$» (la propia corrección de X7, 2018, lo señala). La unión no es un intervalo, y el «intervalo más pequeño» que la contiene es $\mathbb R$, donde $f$ no es convexa (en $(-2,2)$ es cóncava).

**Receta.** Gráfica de $f''$: encima del eje → convexa; debajo → cóncava; cruces del eje → inflexiones.
**Error típico.** Leer la gráfica como si fuera la de $f$ o la de $f'$ (comprobar siempre la etiqueta: aquí pone $f''(x)$).

### X3. Febrero 2014, Mecánica Modelo B (X p. 43), Pregunta corta 2 (1 punto)

> Sea $f:[-2,2]\to\mathbb R$ una función continua y dos veces derivable con continuidad. Su derivada segunda se representa en la siguiente figura. Determine los intervalos de concavidad, de convexidad y sus puntos de inflexión. Razone la respuesta.

(Figura: $f''$ con forma de cúbica, ceros en $-1$, $0$ y $1$; negativa en $(-2,-1)$, positiva en $(-1,0)$, negativa en $(0,1)$, positiva en $(1,2)$.)

1. $f''\ge0$ en $[-1,0]$ y en $[1,2]$ → **convexa** ahí (Prop. 3.10).
2. $f''\le0$ en $[-2,-1]$ y en $[0,1]$ → **cóncava** ahí.
3. $f''$ cambia de signo en $-1$, $0$ y $1$ → **inflexiones en $x=-1,0,1$**. (Los extremos $\pm2$ del dominio no pueden ser de inflexión: la Def. 3.10 necesita un trozo a cada lado.)

La solución de X coincide. **Receta y error típico:** como X1.

### X6. Febrero 2017, Mecánica Modelo A (X p. 77), Pregunta corta 3 (1 punto)

> Sea $f$ una función cuya derivada segunda, para el intervalo $[a,b]$ se representa en la siguiente gráfica: […] Llamamos $x_0$, $x_1$ y $x_2$ a los puntos de corte de la gráfica de $f''(x)$ con el eje $x$, ordenados de menor a mayor. Indique en qué intervalos es $f$ cóncava y en qué intervalos es convexa.

(Figura: $f''$ negativa en $[a,x_0)$, positiva en $(x_0,x_1)$, negativa en $(x_1,x_2)$, positiva en $(x_2,b]$.)

1. **Cóncava en $[a,x_0]$ y en $[x_1,x_2]$** ($f''\le0$).
2. **Convexa en $[x_0,x_1]$ y en $[x_2,b]$** ($f''\ge0$).
3. (No se pide: inflexiones en $x_0,x_1,x_2$.)

Coincide con X. **Receta.** Como X1, con letras en lugar de números.

### X8. Febrero 2018, Mecánica Modelo B (X p. 93), Pregunta corta 3 (1 punto)

> Determine los intervalos de concavidad y convexidad de la función $f$ dada por $f(x)=x^4-2x$.

**Idea en una frase.** $f''=12x^2$ nunca es negativa: convexa en todo $\mathbb R$, **aunque** $f''(0)=0$.

1. $f'(x)=4x^3-2$, $f''(x)=12x^2\ge0$ para todo $x$.
2. **Convexa en $(-\infty,\infty)$** (Prop. 3.10). No es cóncava en ningún intervalo abierto.
3. **Sin inflexiones:** $f''(0)=0$ pero $f''$ **no cambia de signo** en $0$. (Con derivadas: $f'''(0)=0$, $f^{(4)}(0)=24\ne0$, de orden **par**: la Prop. 3.12 no da inflexión.)

**Receta.** Si $f''$ es un cuadrado (o $\ge0$ siempre), convexa en todo $\mathbb R$.
**Error típico.** «$f''(0)=0$ ⇒ inflexión en $0$» (la Prop. 3.11 es solo condición necesaria).

### X2. Febrero 2013, 1ª semana, Mecánica Modelo A (X p. 33), Problema 5 (a) — (b) **requiere Tema 6**

> Sea $f:\mathbb R\to\mathbb R$ la función dada por $f(x)=xe^x$. (a) ¿Cuáles son los intervalos de concavidad y de convexidad? (b) Calcule $\int f(x)\,dx$.

**Idea en una frase.** $e^x>0$ siempre, así que el signo de $f''$ es el del factor polinómico.

1. $f'(x)=e^x+xe^x=(1+x)e^x$; $f''(x)=e^x+(1+x)e^x=(x+2)e^x$.
2. Como $e^x>0$: $f''\le0\iff x\le-2$ y $f''\ge0\iff x\ge-2$.
3. **Cóncava en $(-\infty,-2]$, convexa en $[-2,\infty)$**; inflexión en $x=-2$ (cambio de signo), punto $(-2,-2e^{-2})$.
4. (b) *Tema 6 (integración por partes):* $\int xe^x\,dx=xe^x-e^x+C$. Se entenderá tras U Tema 6.

**Errata menor en X.** «menor o igual mayor o igual)»: falta el paréntesis de apertura.
**Receta.** Producto por exponencial: sacar $e^x$ factor común y estudiar solo el signo del polinomio.
**Error típico.** Olvidar que $(xe^x)''$ lleva **dos** veces el término $e^x$: $(x+2)e^x$, no $(x+1)e^x$.

Verificación sympy: $f''=(x+2)e^x$; $\int xe^x\,dx=(x-1)e^x$.

### X4. Febrero 2016, Mecánica Modelo B (X pp. 64-65), Pregunta corta 3 (1 punto)

> Determine los intervalos donde la función $f(x)=\dfrac{x^2}{x+1}$ sea cóncava y donde sea convexa.

**Idea en una frase.** Es «hermana» de E 3.46: $f''=\frac{2}{(x+1)^3}$ y el cambio de concavidad ocurre en la asíntota.

1. Dominio $\mathbb R\setminus\{-1\}$.
2. $f'(x)=\frac{2x(x+1)-x^2}{(x+1)^2}=\frac{x(x+2)}{(x+1)^2}$.
3. $f''(x)=\frac{(2x+2)(x+1)^2-x(x+2)\cdot2(x+1)}{(x+1)^4}=\frac{2(x+1)\big[(x+1)^2-x(x+2)\big]}{(x+1)^4}=\frac{2}{(x+1)^3}$ (el corchete vale $1$).
4. $f''>0\iff x>-1$: **convexa en $(-1,\infty)$**; $f''<0\iff x<-1$: **cóncava en $(-\infty,-1)$**.
5. **Sin inflexiones:** $f''\ne0$ y $x=-1$ no es del dominio (asíntota vertical).

**Errata en X (p. 64).** La cadena impresa es
$$f''(x)=\frac{2(x+2)(x+1)^2-2x(x+2)(x+1)}{(x+1)^4}=\frac{2x^2+6x+4}{(x+1)^4}=\frac{2}{(x+1)^3}.$$
El primer numerador está mal: la derivada de $x(x+2)=x^2+2x$ es $2x+2=2(x+1)$, **no** $2(x+2)$. Con ese error, la expresión intermedia vale $\frac{2(x+2)}{(x+1)^3}$, que **no** es igual a $\frac{2}{(x+1)^3}$ (el último «$=$» es falso). El resultado final sí es correcto (paso 3) y la conclusión no cambia.

**Receta.** Cociente: regla del cociente, **sacar factor común** $(x+1)$ antes de simplificar, y comprobar sustituyendo un número (p. ej. $x=0$: $f''(0)=2$).
**Error típico.** El de X: derivar mal el numerador y «arreglarlo» al final.

Verificación sympy: $f''=2/(x+1)^3$; $(2x^2+6x+4)/(x+1)^4=2(x+2)/(x+1)^3$.

### X7. Febrero 2018, Mecánica Modelo A (X pp. 89-90), Ejercicio 5 (b) — (c) es de §2.4

> Sea $f$ la función dada por $f(x)=\dfrac{1}{x^2+4}$. (a) (1 punto) Estudie si es una función continua y derivable en $\mathbb R$, determinando la derivada cuando exista. (b) (1 punto) Determine intervalos de concavidad y convexidad de esta función. (c) (1 punto) Aproxime un punto fijo de $f$, sabiendo que la función es contractiva y que el punto fijo está en el intervalo $[0,1]$, comenzando con $x_0=0$ y tras 3 iteraciones.

**Idea en una frase.** El denominador de $f''$ es siempre positivo: el signo lo da el numerador $6x^2-8$.

1. (a) $x^2+4>0$: continua y derivable en $\mathbb R$; $f'(x)=-\frac{2x}{(x^2+4)^2}$.
2. (b) $f''(x)=-\frac{2(x^2+4)^2-2x\cdot2(x^2+4)\cdot2x}{(x^2+4)^4}=-\frac{2(x^2+4)-8x^2}{(x^2+4)^3}=\frac{6x^2-8}{(x^2+4)^3}$.
3. $(x^2+4)^3>0$. $6x^2-8\ge0\iff x^2\ge\frac43\iff\lvert x\rvert\ge\frac{2}{\sqrt3}\approx1{,}155$.
4. **Convexa en $\big(-\infty,-\tfrac2{\sqrt3}\big]$ y en $\big[\tfrac2{\sqrt3},\infty\big)$; cóncava en $\big[-\tfrac2{\sqrt3},\tfrac2{\sqrt3}\big]$.**
5. **Inflexiones en $x=\pm\frac2{\sqrt3}$** (cambia el signo de $f''$), con $f\big(\pm\tfrac2{\sqrt3}\big)=\frac{1}{4/3+4}=\frac{3}{16}$. X no lo dice, pero es lo primero que se espera.
6. (c) (§2.4, punto fijo) $x_1=\frac14$, $x_2=\frac{16}{65}\approx0{,}24615$, $x_3=\frac{4225}{17156}\approx0{,}24627$.

**Erratas en X (p. 90).** Escribe «convexa en $\big(\infty,-\tfrac2{\sqrt3}\big)$» (dos veces): falta el signo, es $(-\infty,\dots)$. «$(x^2+4)^3\ge0$»: es $>0$ (si fuese $0$ no se podría dividir). «$0..24615$»: punto doble. La observación de X «no es correcto decir que es convexa en la unión… porque en el conjunto unión de los dos intervalos no se cumple la Def. 3.8» es **acertada**: con la cuerda de $-2$ a $2$, en $0$ la gráfica vale $\tfrac14$ y la cuerda $\tfrac18$; la gráfica queda por encima.

**Receta.** Cociente con denominador $(\dots)^n$ siempre positivo: solo importa el signo del numerador de $f''$.
**Error típico.** Escribir la convexidad en la unión de intervalos.

Verificación sympy: $f''=2(3x^2-4)/(x^2+4)^3$, ceros $\pm2\sqrt3/3$; $f(0)=1/4$, $(f(-2)+f(2))/2=1/8$; iteraciones $0,\tfrac14,\tfrac{16}{65},\tfrac{4225}{17156}$.

### X5. Septiembre 2016, Mecánica Modelo A (X pp. 70-71), Ejercicio 5 (3 puntos) — (a) es de §3.1

> Sea $f(x)=(3x-1)e^x$ una función definida en $\mathbb R$. (a) Obtenga el polinomio de Taylor de $f$ de orden 3 centrado en $x=-1$. (b) Determine los intervalos de crecimiento y decrecimiento de $f$. ¿Tiene puntos de inflexión? (c) Determine los puntos donde se alcanzan extremos relativos y estudie si son máximos o mínimos relativos.

**Idea en una frase.** Cada derivada suma $3$ al término independiente: $f^{(k)}(x)=(3x-1+3k)e^x$; con eso se hace todo.

1. $f'=(3x+2)e^x$, $f''=(3x+5)e^x$, $f'''=(3x+8)e^x$. En $-1$: $f(-1)=-4e^{-1}$, $f'(-1)=-e^{-1}$, $f''(-1)=2e^{-1}$, $f'''(-1)=5e^{-1}$.
2. (a) $p_3(x)=-4e^{-1}-e^{-1}(x+1)+\frac{2}{2!}e^{-1}(x+1)^2+\frac{5}{3!}e^{-1}(x+1)^3=e^{-1}\big[-4-(x+1)+(x+1)^2+\tfrac56(x+1)^3\big]$.
3. (b) Crecimiento: $e^x>0$, signo de $3x+2$: **decreciente en $(-\infty,-\tfrac23]$, creciente en $[-\tfrac23,\infty)$**.
4. (b) Inflexión: $f''=0\iff x=-\tfrac53$. $f'''(-\tfrac53)=3e^{-5/3}\ne0$ (orden 3, impar, positiva) → **inflexión en $x=-\tfrac53$**, de cóncava a convexa (Prop. 3.12). Equivalente: $f''<0$ si $x<-\tfrac53$ (cóncava) y $f''>0$ si $x>-\tfrac53$ (convexa).
5. (c) Único crítico $x=-\tfrac23$; $f$ decrece antes y crece después → **mínimo relativo** (Prop. 3.5), valor $f(-\tfrac23)=-3e^{-2/3}$. (También $f''(-\tfrac23)=3e^{-2/3}>0$.)

**Errata en X (p. 70).** En $p_3$ escribe el último coeficiente como $\frac{3}{3!}e^{-1}$; debe ser $\frac{5}{3!}e^{-1}$, porque $f'''(-1)=5e^{-1}$ (la línea siguiente ya pone $\frac56$, que es lo correcto).

**Receta.** Inflexión con la Prop. 3.12: $f''(c)=0$ y $f'''(c)\ne0$ ⇒ inflexión (el signo de $f'''$ da el sentido del cambio).
**Error típico.** Contestar a «¿tiene puntos de inflexión?» con el punto donde $f'=0$.

Verificación sympy: derivadas $(3x-1+3k)e^x$; valores en $-1$: $-4,-1,2,5$ (por $e^{-1}$); $f'''(-5/3)=3e^{-5/3}$.

### X9. I. Electrónica Industrial y Automática, sin fecha (X p. 99), Pregunta corta 3 (1 punto)

> Dibuje la gráfica de una función que sea creciente en todo $\mathbb R$, convexa en $(-\infty,0)$, cóncava en $(0,\infty)$ y tenga dos asíntotas (una horizontal y una oblicua).

**Idea en una frase.** Es E 3.48 cambiada de signo: $\operatorname{arctg}x$ a la izquierda y $\tfrac x2+\operatorname{arctg}x$ a la derecha.

1. $f(x)=\operatorname{arctg}x$ si $x\le0$; $f(x)=\tfrac x2+\operatorname{arctg}x$ si $x>0$. Continua en $0$ (ambos lados valen $0$).
2. Creciente: $f'=\frac1{1+x^2}>0$ ($x<0$) y $f'=\tfrac12+\frac1{1+x^2}>0$ ($x>0$), y continua en $0$.
3. $f''=\frac{-2x}{(1+x^2)^2}$ en ambos trozos: $>0$ si $x<0$ (convexa), $<0$ si $x>0$ (cóncava). Inflexión en $0$.
4. Asíntotas: $y=-\tfrac\pi2$ cuando $x\to-\infty$; $y=\tfrac x2+\tfrac\pi2$ cuando $x\to+\infty$.

**Aviso de notación en X.** Escribe «$1/2x$», que podría leerse $\frac{1}{2x}$; por la gráfica (pendiente $\tfrac12$) significa $\tfrac12x=\tfrac x2$. En el examen, escribir $\tfrac x2$.
**Receta / error típico.** Como E 3.48.

Verificación sympy: $f''=-2x/(x^2+1)^2$ (ambos trozos), $f'=(x^2+3)/(2(x^2+1))$ ($x>0$); límites $-\pi/2$ y $\lim_{x\to+\infty}[f-x/2]=\pi/2$.

### X10. I. Electrónica Industrial y Automática (A), sin fecha (X pp. 127-128), Ejercicio 5 (3 puntos)

> Para la función dada por $f(x)=e^{x^k}$ con $k$ un número fijo que pertenece al conjunto $\{0,1,2,3,\dots\}$: Calcule su **dominio** y su **imagen** en función del valor de $k$. Calcule sus intervalos de **crecimiento**, **decrecimiento**, **concavidad** y **convexidad** para $k=2$ y $k=3$. Estudie sus **asíntotas** y **extremos relativos** para $k=2$ y $k=3$.

**Idea en una frase.** Regla de la cadena: $(e^{u})''=(u''+u'^2)e^{u}$, y $e^u>0$ siempre, así que el signo lo da $u''+u'^2$.

1. **Dominio:** $\mathbb R$ para todo $k$.
2. **Imagen.** $k=0$: $x^0=1$ y $f\equiv e$: imagen $\{e\}$. $k\ge2$ par: $x^k\in[0,\infty)$, imagen $[1,\infty)$. $k$ impar: $x^k$ recorre $\mathbb R$, imagen $(0,\infty)$.
3. **$k=2$.** $f'=2xe^{x^2}$: decreciente en $(-\infty,0]$, creciente en $[0,\infty)$; mínimo relativo y absoluto en $0$ ($f(0)=1$). $f''=(4x^2+2)e^{x^2}>0$: **convexa en $\mathbb R$**, sin inflexiones. Sin asíntotas ($f\to\infty$ y $f/x\to\pm\infty$ en $\pm\infty$).
4. **$k=3$.** $f'=3x^2e^{x^3}\ge0$, que solo vale $0$ en $x=0$: **creciente en $\mathbb R$**; $x=0$ es crítico sin extremo. $f''=(6x+9x^4)e^{x^3}=3x(3x^3+2)e^{x^3}$. Ceros: $x=0$ y $x=-\sqrt[3]{2/3}\approx-0{,}874$.

| intervalo | $3x$ | $3x^3+2$ | $f''$ | $f$ |
|---|---|---|---|---|
| $(-\infty,-\sqrt[3]{2/3})$ | $-$ | $-$ | $+$ | convexa |
| $(-\sqrt[3]{2/3},0)$ | $-$ | $+$ | $-$ | cóncava |
| $(0,\infty)$ | $+$ | $+$ | $+$ | convexa |

   **Dos inflexiones:** $x=-\sqrt[3]{2/3}$ y $x=0$. Asíntota horizontal $y=0$ cuando $x\to-\infty$ ($e^{x^3}\to0$); ninguna en $+\infty$.

**Erratas / omisiones en X (p. 128).**
- Imagen para $k=0$: X dice $\{1\}$; es **$\{e\}$** ($e^{x^0}=e^1$).
- Para $k=3$ X solo menciona «un punto de inflexión» (en el crítico $0$). Hay **dos**: también $x=-\sqrt[3]{2/3}$, donde $f''$ cambia de signo (lo confirma su propia frase de concavidad: cóncava en $(-\sqrt[3]{2/3},0)$ y convexa a la izquierda).

**Receta.** $e^{u(x)}$: $f'=u'e^u$, $f''=(u''+u'^2)e^u$; tabla de signos del polinomio $u''+u'^2$.
**Error típico.** Quedarse con la inflexión que coincide con el punto crítico y olvidar la otra raíz de $f''$.

Verificación sympy: $k=2$: $f''=2(2x^2+1)e^{x^2}$ (sin ceros reales); $k=3$: $f''=3x(3x^3+2)e^{x^3}$, ceros $0$ y $-\sqrt[3]{2/3}\approx-0{,}8736$; $e^{x^0}=e$.

---

## 3. Ejemplos propios (dificultad creciente)

### Propio 1 — Concavidad por $f''$ e inflexiones (propio)

> Estudia la concavidad y los puntos de inflexión de $f(x)=\ln(1+x^2)$.

**Idea en una frase.** $f''$ es un cociente con denominador positivo: el signo lo da $1-x^2$.

1. Dominio $\mathbb R$ ($1+x^2>0$). $f'(x)=\frac{2x}{1+x^2}$.
2. $f''(x)=\frac{2(1+x^2)-2x\cdot2x}{(1+x^2)^2}=\frac{2(1-x^2)}{(1+x^2)^2}$.
3. Signo de $1-x^2$: $>0$ en $(-1,1)$, $<0$ si $\lvert x\rvert>1$. **Convexa en $[-1,1]$; cóncava en $(-\infty,-1]$ y en $[1,\infty)$** (Prop. 3.10).
4. **Inflexiones en $x=\pm1$**, puntos $(\pm1,\ln2)$. Comprobación con la Prop. 3.12: $f'''(1)=-1<0$ (de convexa a cóncava).

**Receta.** $f''$ → denominador positivo fuera → signo del numerador.
**Error típico.** Decir «cóncava en $(-\infty,-1)\cup(1,\infty)$» (unión).

### Propio 2 — $f''(c)=0$ sin inflexión, y con inflexión (propio)

> (a) Estudia la concavidad de $f(x)=x^4-4x^3+6x^2+x$. (b) Lo mismo para $g(x)=x^5-5x^4+10x^3-10x^2$. ¿Hay inflexión en $x=1$?

**Idea en una frase.** $f''(c)=0$ es solo un candidato: lo que cuenta es si $f''$ **cambia de signo** (o la paridad de la primera derivada no nula, Prop. 3.12).

1. (a) $f''(x)=12x^2-24x+12=12(x-1)^2\ge0$. **Convexa en $\mathbb R$.** $f''(1)=0$, pero no cambia de signo: **no hay inflexión**. Con derivadas: $f'''(1)=0$, $f^{(4)}(1)=24$ (orden 4, **par**): la Prop. 3.12 no se aplica, y el signo de $f''$ confirma que no hay inflexión.
2. (b) $g''(x)=20x^3-60x^2+60x-20=20(x-1)^3$: $<0$ si $x<1$, $>0$ si $x>1$. **Cóncava en $(-\infty,1]$, convexa en $[1,\infty)$; inflexión en $(1,-4)$.** Con derivadas: $g''(1)=g'''(1)=g^{(4)}(1)=0$ y $g^{(5)}(1)=120>0$ (orden 5, impar, positiva): de cóncava a convexa (Prop. 3.12).

**Receta.** Factorizar $f''$: un factor $(x-c)^{\text{par}}$ no cambia el signo (no hay inflexión); $(x-c)^{\text{impar}}$ sí.
**Error típico.** «$f''(1)=0$ ⇒ inflexión» (es la afirmación 10 de la autoevaluación de U, p. 140, que es falsa).

### Propio 3 — Una desigualdad sacada de la concavidad (propio)

> Demuestra que $\operatorname{sen}x\ge\dfrac{2}{\pi}x$ para todo $x\in\big[0,\tfrac\pi2\big]$.

**Idea en una frase.** Una función cóncava queda **por encima** de sus cuerdas; la recta $y=\frac2\pi x$ es justo la cuerda de $\operatorname{sen}$ entre $0$ y $\frac\pi2$.

1. **Concavidad.** $(\operatorname{sen}x)''=-\operatorname{sen}x\le0$ en $\big[0,\tfrac\pi2\big]$ → $\operatorname{sen}$ es cóncava ahí (Prop. 3.10).
2. **Definición de cóncava (Def. 3.9: $-\operatorname{sen}$ convexa)** con $x=0$, $y=\frac\pi2$: $\operatorname{sen}\big((1-t)\cdot0+t\tfrac\pi2\big)\ge(1-t)\operatorname{sen}0+t\operatorname{sen}\tfrac\pi2$, es decir, $\operatorname{sen}\big(t\tfrac\pi2\big)\ge t$ para todo $t\in[0,1]$.
3. **Cambio de nombre.** Todo $x\in[0,\tfrac\pi2]$ se escribe $x=t\frac\pi2$ con $t=\frac{2x}{\pi}\in[0,1]$. Sustituyendo: $\operatorname{sen}x\ge\frac{2x}{\pi}$. ∎
4. **Comprobación numérica:** $x=\tfrac\pi6$: $\operatorname{sen}\tfrac\pi6=0{,}5\ge\tfrac13$.
5. **Variante:** $\sqrt{x}$ es cóncava en $[0,\infty)$ ($(\sqrt x)''=-\tfrac14x^{-3/2}<0$ si $x>0$); con $t=\tfrac12$ en la Def. 3.9: $\dfrac{\sqrt a+\sqrt b}{2}\le\sqrt{\dfrac{a+b}{2}}$ para $a,b\ge0$ (p. ej. $a=3$, $b=11$: $2{,}524\le2{,}646$).

**Receta.** Desigualdad «función $\ge$ recta» en un intervalo: si la recta es la cuerda, basta la concavidad (Def. 3.9); si es «función $\le$ cuerda», la convexidad (Def. 3.8).
**Error típico.** Usar la cuerda fuera del intervalo $[x,y]$: fuera de $[0,\tfrac\pi2]$ la desigualdad puede fallar (en $x=\pi$: $\operatorname{sen}\pi=0<2$).

### Propio 4 — Estudio completo con asíntotas vertical y oblicua (propio)

> Representa $f(x)=\dfrac{x^3}{x^2-1}$.

**Idea en una frase.** Es impar, tiene dos asíntotas verticales, la oblicua $y=x$, dos extremos y una inflexión en el origen con tangente horizontal.

1. **Dominio:** $\mathbb R\setminus\{-1,1\}$. **Simetría:** $f(-x)=-f(x)$ (impar). **Corte:** solo $(0,0)$.
2. **Asíntotas verticales.** $\lim_{x\to1^-}f(x)=-\infty$, $\lim_{x\to1^+}f(x)=+\infty$, $\lim_{x\to-1^-}f(x)=-\infty$, $\lim_{x\to-1^+}f(x)=+\infty$: $x=1$ y $x=-1$.
3. **Oblicua.** $m=\lim_{x\to\pm\infty}\frac{x^3}{x(x^2-1)}=1$; $f(x)-x=\frac{x}{x^2-1}\to0$, así que $b=0$: **$y=x$** en $\pm\infty$ (la gráfica queda por encima de la recta si $x>1$ y por debajo si $x<-1$).
4. **Crecimiento.** $f'(x)=\frac{3x^2(x^2-1)-x^3\cdot2x}{(x^2-1)^2}=\frac{x^2(x^2-3)}{(x^2-1)^2}$. Signo $=$ signo de $x^2-3$ (salvo en $0$): creciente en $(-\infty,-\sqrt3]$ y $[\sqrt3,\infty)$; decreciente en $[-\sqrt3,-1)$, $(-1,1)$ y $(1,\sqrt3]$.
5. **Extremos.** Críticos: $0$, $\pm\sqrt3$. $x=-\sqrt3$: crece y luego decrece → **máximo relativo** $\big(-\sqrt3,-\tfrac{3\sqrt3}2\big)$. $x=\sqrt3$: **mínimo relativo** $\big(\sqrt3,\tfrac{3\sqrt3}2\approx2{,}60\big)$ (también $f''(\sqrt3)=\tfrac{3\sqrt3}{2}>0$). $x=0$: decrece a ambos lados → no es extremo.
6. **Concavidad.** $f''(x)=\frac{2x(x^2+3)}{(x^2-1)^3}$. Como $x^2+3>0$, mandan los signos de $x$ y de $(x^2-1)^3$:

| intervalo | $x$ | $(x^2-1)^3$ | $f''$ | $f$ |
|---|---|---|---|---|
| $(-\infty,-1)$ | $-$ | $+$ | $-$ | cóncava |
| $(-1,0)$ | $-$ | $-$ | $+$ | convexa |
| $(0,1)$ | $+$ | $-$ | $-$ | cóncava |
| $(1,\infty)$ | $+$ | $+$ | $+$ | convexa |

7. **Inflexión:** solo en $x=0$ (los cambios en $\pm1$ ocurren en asíntotas, fuera del dominio). Con la Prop. 3.12: $f'''(0)=-6<0$, de convexa a cóncava. Como además $f'(0)=0$, la tangente en el origen es horizontal.
8. **Dibujo.** Rama $x<-1$: sube pegada (por debajo) a $y=x$ hasta el máximo en $-\sqrt3$ y cae a $-\infty$ junto a $x=-1$ ($\bigcap$). Rama central: baja desde $+\infty$ (junto a $x=-1$), pasa por el origen con tangente horizontal cambiando de $\bigcup$ a $\bigcap$, y baja a $-\infty$ junto a $x=1$. Rama $x>1$: simétrica de la primera respecto del origen.

**Receta.** La del Ejercicio 3.46, más **simetría** (si es par o impar, basta estudiar $x\ge0$) y **partir las tablas en todos los puntos fuera del dominio**.
**Error típico.** Poner inflexiones en $x=\pm1$; o decir que $x=0$ es un extremo porque $f'(0)=0$.

Verificación sympy (propios): P1 $f''=-2(x-1)(x+1)/(x^2+1)^2$, $f'''(1)=-1$; P2 $f''=12(x-1)^2$, derivadas 2ª-4ª en $1$: $0,0,24$; $g''=20(x-1)^3$, derivadas 2ª-5ª en $1$: $0,0,0,120$, $g(1)=-4$; P3 $\min_{[0,\pi/2]}(\operatorname{sen}x-2x/\pi)=0$ (malla de $200\,001$ puntos; se alcanza en los extremos); P4 $f'=x^2(x^2-3)/(x^2-1)^2$, $f''=2x(x^2+3)/(x^2-1)^3$, $m=1$, $b=0$, $f(\sqrt3)=3\sqrt3/2$, $f''(\sqrt3)=3\sqrt3/2$, $f'''(0)=-6$, límites laterales en $\pm1$: $-\infty$ por la izquierda y $+\infty$ por la derecha.

---

## 4. Resumen de erratas y avisos

| Dónde | Qué dice | Qué debería decir / comentario |
|---|---|---|
| E 3.30, p. 114 | «los extremos locales **y los puntos de inflexión**… se alcanzan en puntos donde se anula su derivada» | Las inflexiones se buscan con $f''=0$ (U Prop. 3.11); su propio ejemplo $2x^3+6x$ tiene inflexión en $0$ con $f'(0)=6$. |
| E 3.40, p. 123 | (`.txt`) «derivable si $x=4$» | El PDF dice $x\ne4$: error de extracción, no de E. |
| E 3.41, p. 123 | (dossier) $f=\lvert x\rvert$ | El enunciado real es $f(x)=\sqrt{\lvert x\rvert}$. |
| E 3.41, p. 124 | «$\sqrt{\lvert2t-1\rvert}=0$, que **no es menor** que 1» | «que **es** menor que 1» (por eso falla la concavidad). |
| E 3.41, p. 124 | «ya la hemos estudiado en el Ejercicio 3» | Remisión rota: no hay en E un ejercicio con $\sqrt{\lvert x\rvert}$. |
| E 3.42, p. 125 | b) «convexa si $(-\infty,0)$» | «convexa **en** $(-\infty,0)$». |
| **E 3.45, p. 128** | «no podemos saber si es convexa en $\mathbb R$… Podría serlo o no» | **Falso**: con la gráfica de $f'$ ($f'>0$ en $(0,1)$, $f'<0$ en $(1,2)$) $f$ **no** es convexa en $\mathbb R$ (pendientes de cuerdas + TVM). |
| E 3.46, p. 128 (margen) | Oblicua si $\lim_{x\to\pm\infty}f(x)/x=m$, «de la forma $y=mx+c$» | Falta exigir que $c=\lim_{x\to\pm\infty}(f(x)-mx)$ exista y sea finito (U Prop. 1.12 es solo necesaria). |
| E 3.47, pp. 132-133 | a) $f=\pi$; c) «la más sencilla $f(x)=x$»; d) «Para el tercero» | Válidos solo con las definiciones no estrictas de U (Def. 2.5, Def. 3.8); «tercero» es el apartado d). |
| X p. 17 (Sep 2011, PC4) | «convexa en $(-\infty,-2)\cup(2,\infty)$» | En $(-\infty,-2)$ y en $(2,\infty)$ (convexidad en intervalos). |
| X p. 33 (Feb 2013 A, Pr. 5) | «menor o igual mayor o igual)» | Falta «(». (b) es del Tema 6. |
| X p. 64 (Feb 2016 B, PC3) | $f''=\frac{2(x+2)(x+1)^2-\dots}{(x+1)^4}=\frac{2x^2+6x+4}{(x+1)^4}=\frac{2}{(x+1)^3}$ | Derivada del numerador mal ($2x+2$, no $2(x+2)$); el último «$=$» es falso. Resultado final correcto: $f''=2/(x+1)^3$. |
| X p. 70 (Sep 2016 A, Ej. 5a) | coeficiente $\frac{3}{3!}e^{-1}$ | $\frac{5}{3!}e^{-1}$ ($f'''(-1)=5e^{-1}$). |
| X p. 90 (Feb 2018 A, Ej. 5b) | «convexa en $(\infty,-\tfrac2{\sqrt3})$»; «$(x^2+4)^3\ge0$»; «$0..24615$» | $(-\infty,\dots)$; $>0$; $0{,}24615$. Falta decir que hay inflexiones en $\pm\frac2{\sqrt3}$. |
| X p. 99 (Electrónica, PC3) | «$1/2x$» | Significa $\tfrac x2$ (lo confirma la gráfica). |
| X p. 128 (Electrónica A, Ej. 5) | Imagen $\{1\}$ para $k=0$; para $k=3$ «un punto de inflexión» | Imagen $\{e\}$; para $k=3$ hay **dos** inflexiones: $x=-\sqrt[3]{2/3}$ y $x=0$. |
| U §3.5 | Páginas | §3.5 va de la p. 134 (título) a la 140 (autoevaluación); Def. 3.8-3.9 p. 135, Ej. 3.28 y Prop. 3.9-3.10 p. 136, Def. 3.10 y Prop. 3.11-3.12 p. 137, representación gráfica p. 139 (comprobado en imagen). |
