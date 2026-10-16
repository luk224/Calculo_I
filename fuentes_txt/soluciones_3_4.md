# Soluciones Tema 3.4 — Optimización. Extremos relativos y absolutos

Resolución paso a paso de los ejercicios de **E** de la sección 3.4 (3.29-3.38 y 3.44), de los problemas de examen **X** que solo usan 3.4, y de 4 ejemplos propios. Todos los cálculos se han comprobado con sympy (salidas resumidas al final de cada ejercicio). Los enunciados de E y de X se han leído **como imagen** (páginas renderizadas con PyMuPDF), no del `.txt`.

Páginas: U impresa; E impresa = PDF; X = página PDF de `Examenes-resueltos-Calculo.pdf`.

## 0. Herramientas de teoría que se usan (todas de U)

| Clave | Enunciado (resumido) | Dónde |
|---|---|---|
| **Weierstrass** | $f$ continua en $[a,b]$ $\Rightarrow$ existen $c,d\in[a,b]$ con $f(c)\le f(x)\le f(d)$ para todo $x\in[a,b]$ (alcanza máximo y mínimo). | U §1.4, Prop. 1.15, p. 52 |
| **Monotonía** | $f'>0$ en un intervalo $\Rightarrow$ estrictamente creciente; $f'<0$ $\Rightarrow$ estrictamente decreciente; $f'\ge 0$ $\Rightarrow$ creciente. | U §2.5.4, Prop. 2.4, p. 98 |
| **Def. 3.4** | Mínimo (máximo) absoluto en $c$: $f(c)\le f(x)$ ($\ge$) para **todo** $x$ del dominio. | U §3.4.2, p. 126 |
| **Def. 3.5** | Punto crítico: $c\in(a,b)$ con $f'(c)=0$ **o** $f$ no derivable en $c$. | U §3.4.2, p. 126 |
| **Prop. 3.4** | Los extremos absolutos de $f$ continua en $[a,b]$ se alcanzan en los extremos del intervalo o en los puntos críticos. | U §3.4.2, p. 126 |
| **Def. 3.6** | Mínimo (máximo) relativo en $c$: existe un intervalo $I\subset D$ (que contiene a $c$) con $f(c)\le f(x)$ ($\ge$) para todo $x\in I$. | U §3.4.3, p. 130 |
| **Prop. 3.5** | (Criterio de la 1ª derivada, en forma de monotonía.) $f$ continua; decreciente a la izquierda de $c$ y creciente a la derecha $\Rightarrow$ mínimo relativo; al revés $\Rightarrow$ máximo relativo. | U §3.4.3, p. 130 |
| **Prop. 3.6** | Los extremos relativos de $f$ continua en $[a,b]$ están en los extremos del intervalo o en puntos críticos; en $(a,b)$, solo en puntos críticos. | U §3.4.3, p. 131 |
| **Def. 3.7** | Punto de silla: punto crítico donde **no** hay extremo relativo. | U §3.4.3, p. 131 |
| **Prop. 3.7** | (2ª derivada.) $f'(c)=0$: $f''(c)>0\Rightarrow$ mínimo relativo; $f''(c)<0\Rightarrow$ máximo relativo. | U §3.4.3, p. 131 |
| **Prop. 3.8** | (Orden superior.) Si la primera derivada que no se anula en el crítico $c$ es de orden **par**: máximo si es negativa, mínimo si es positiva. Si es de orden **impar**: punto de silla. | U §3.4.3, p. 132 |
| Ejemplos | 3.19 ($4x^3-3x^2-6x+2$ en $[0,2]$), 3.20 ($\lvert\operatorname{sen}x\rvert$), 3.21 ($x/(x^2+1)$ en $(0,\infty)$), 3.24 ($x^4-2x^3$), 3.25-3.26 (tela metálica). | U pp. 126-134 |

**Observación importante sobre la Def. 3.6.** Con la definición de U, un **extremo del intervalo** puede ser extremo relativo (basta tomar $I=[a,a+\delta]$). Por eso la Prop. 3.6 dice que los extremos relativos en $[a,b]$ se alcanzan «en los extremos del intervalo o en los puntos críticos», y por eso E (3.31, 3.32, 3.33) clasifica los puntos $t=0$, $x=\pm1$, $t=6$ como extremos relativos. Otros libros (Stewart §4.1) solo llaman «local» a un extremo interior: en el examen, **seguir el convenio de U** (y, si se quiere, decirlo: «extremo relativo en el borde del intervalo»).

---

## 1. Ejercicios de E (orden de dificultad creciente; numeración conservada)

Orden propuesto para aprender: 3.44 → 3.34 → 3.35 → 3.29 → 3.36 → 3.30 → 3.38 → 3.37 → 3.32 → 3.31 → 3.33.

---

### Ejercicio 3.44 (E pp. 126-127)

> Sea $f$ la función dada por $f(x)=(x-1)^2$. ¿Cuál de las siguientes opciones es correcta?
> **a)** En $x=1$ la función $f$ alcanza un máximo relativo. **b)** En $x=1$ la función $f$ alcanza un mínimo relativo no absoluto. **c)** En $x=1$ la función $f$ alcanza el único mínimo relativo y absoluto. **d)** En $x=1$ la función $f$ tiene un punto de inflexión.

**Idea en una frase.** Un cuadrado nunca es negativo y solo vale $0$ cuando lo de dentro es $0$: el punto $x=1$ es el «fondo» de la parábola.

1. **Puntos críticos.** $f$ es un polinomio, luego es derivable en todo $\mathbb R$ y los únicos puntos críticos son los ceros de $f'$ (Def. 3.5, U p. 126): $f'(x)=2(x-1)=0\iff x=1$.
2. **Clasificación con la 2ª derivada.** $f''(x)=2$, así que $f''(1)=2>0$ y, por la Prop. 3.7 (U p. 131), en $x=1$ hay un **mínimo relativo**. Esto descarta a).
3. **¿Es absoluto?** Para todo $x$, $f(x)=(x-1)^2\ge 0=f(1)$. Es exactamente la Def. 3.4 de mínimo absoluto (U p. 126). Esto descarta b).
4. **¿Es el único?** Cualquier extremo relativo de una función derivable en $\mathbb R$ está en un punto crítico (Prop. 3.6, U p. 131), y el único es $x=1$.
5. **¿Inflexión?** (Esto es de §3.5.) En un punto de inflexión la concavidad cambia; aquí $f''=2>0$ en todo $\mathbb R$: la función es convexa en todas partes y no cambia nunca. d) es falsa.
6. **Respuesta: c).**

**Receta.** Polinomio: $f'=0$ → signo de $f''$ en el crítico → para «absoluto», una desigualdad global (aquí, cuadrado $\ge0$) o los límites en $\pm\infty$.

**Error típico.** Contestar b) pensando que «relativo» y «absoluto» se excluyen. Un mínimo absoluto en un punto interior es **también** relativo.

Verificación sympy: $f'=0\Rightarrow x=1$; $f''=2$.

---

### Ejercicio 3.34 (E p. 119)

> Sea $f$ la función dada por $f(x)=\lvert x-1\rvert$. ¿Tiene un extremo en $x=1$? ¿Es máximo o mínimo?

(Es la misma pregunta que **X Feb 2012, Mecánica Modelo A, PC2**, ver §2.)

**Idea en una frase.** La gráfica es una «V» con el pico hacia abajo en $x=1$: no hay derivada ahí, pero sí un mínimo.

1. **Escribir $f$ a trozos.** $f(x)=x-1$ si $x\ge1$ y $f(x)=1-x$ si $x<1$.
2. **Derivada donde existe.** Si $x>1$, $f'(x)=1$; si $x<1$, $f'(x)=-1$. Nunca vale $0$.
3. **¿Y en $x=1$?** Las derivadas laterales son $\lim_{x\to1^-}\frac{f(x)-f(1)}{x-1}=-1$ y $\lim_{x\to1^+}\frac{f(x)-f(1)}{x-1}=1$. Son distintas: $f$ **no es derivable** en $1$. Por la Def. 3.5 (U p. 126), $x=1$ es punto crítico y es el **único candidato** (Prop. 3.6, U p. 131).
4. **Decidir con la definición.** El valor absoluto nunca es negativo: $f(x)\ge0=f(1)$ para todo $x$. Por la Def. 3.4 (U p. 126), en $x=1$ hay un **mínimo absoluto** (y, por tanto, también relativo).
5. (Alternativa con la Prop. 3.5, U p. 130: $f$ es continua, decreciente en $(-\infty,1)$ porque $f'=-1<0$ y creciente en $(1,\infty)$ porque $f'=1>0$ → mínimo relativo.)

**Receta.** Si hay un valor absoluto (o una raíz), mirar **también** los puntos donde $f$ no es derivable; muchas veces basta la desigualdad $\lvert\cdot\rvert\ge0$.

**Error típico.** «Como $f'$ nunca vale $0$, no hay extremos». Falso: se olvida la otra mitad de la definición de punto crítico (no derivable).

Nota de fuente: el `.txt` de E pone «derivable si $x=1$» porque `pdftotext` pierde la barra; **el PDF dice correctamente $x\ne1$** (comprobado en la imagen). No es errata del libro.

Verificación sympy: derivadas laterales $-1$ y $1$.

---

### Ejercicio 3.35 (E pp. 119-120)

> Sea $f$ la función dada por $f(x)=x^{2/3}$. ¿Alcanza un extremo relativo en $x=0$? Si es así, ¿de qué tipo?

**Idea en una frase.** $x^{2/3}=(\sqrt[3]{x})^2$ es un cuadrado, así que nunca es negativo; en $0$ vale $0$: es un mínimo, aunque la gráfica tenga ahí un «pico» vertical.

1. **¿Es derivable en 0?** Definición de derivada (U §2.1) con límites laterales: $\lim_{x\to0^-}\frac{x^{2/3}-0}{x}=\lim_{x\to0^-}x^{-1/3}=-\infty$ y $\lim_{x\to0^+}x^{-1/3}=+\infty$. ¿Por qué el signo? Si $x$ es negativo y pequeño, $\sqrt[3]{x}$ es negativo y pequeño y su inverso es un número negativo enorme (ej.: $x=-0{,}001$ da $x^{-1/3}=-10$).
2. **Conclusión.** El límite no es finito: $f$ **no es derivable** en $0$ y $x=0$ es punto crítico (Def. 3.5, U p. 126).
3. **Clasificar.** $f(x)=\big(\sqrt[3]{x}\big)^2\ge0=f(0)$ para todo $x$. Por la Def. 3.4, en $0$ hay un **mínimo absoluto**, y por tanto relativo.

**Receta.** Potencias fraccionarias: calcular las derivadas laterales en el punto «sospechoso»; si no existen, es punto crítico y se clasifica por definición o por la monotonía a cada lado.

**Error típico.** Escribir $f'(x)=\tfrac23x^{-1/3}$, sustituir $x=0$, ver «división por cero» y concluir «no hay extremo». La no derivabilidad **no** impide el extremo: lo convierte en candidato.

Verificación sympy: cocientes laterales $\to -\infty$ y $+\infty$.

---

### Ejercicio 3.29 (E p. 114)

> De una función $f:\mathbb R\to\mathbb R$ tres veces derivable conocemos la gráfica de su derivada primera $f'$ que mostramos a continuación: [gráfica de $f'$ con forma de $y=x^3$: pasa por el origen con tangente horizontal, negativa a la izquierda de $0$ y positiva a la derecha]. Razona si alguna afirmación es correcta entre las siguientes. **a)** $f$ alcanza un valor mínimo relativo en $x=0$. **b)** $f$ alcanza un valor máximo relativo en $x=0$. **c)** $f$ es siempre creciente. **d)** Ninguna de las anteriores.

**Idea en una frase.** Leer la gráfica de $f'$ es leer el «semáforo» de $f$: debajo del eje, $f$ baja; encima, $f$ sube.

1. **Puntos críticos.** $f$ es derivable en $\mathbb R$; sus críticos son donde $f'$ corta al eje $x$: solo $x=0$ (Def. 3.5).
2. **Signo de $f'$ a cada lado.** En $(-\infty,0)$ la gráfica está bajo el eje: $f'<0$ y, por la Prop. 2.4 (U p. 98), $f$ es estrictamente decreciente. En $(0,\infty)$, $f'>0$: estrictamente creciente.
3. **Clasificar.** $f$ es continua (es derivable), baja antes de $0$ y sube después: por la Prop. 3.5 (U p. 130), **mínimo relativo** en $0$.
4. **Descartar las otras.** b) es lo contrario de lo probado. c) falla porque en $(-\infty,0)$ decrece.
5. **Respuesta: a).** (De hecho es mínimo absoluto: $f$ decrece hasta $0$ y crece después.)

**Receta.** Con la gráfica de $f'$: críticos = cortes con el eje $x$; hay extremo si $f'$ **cambia de signo** (de $-$ a $+$ mínimo, de $+$ a $-$ máximo).

**Error típico.** Confundir la gráfica de $f'$ con la de $f$ y razonar con «la curva sube» (eso lo hace $f'$, no $f$). Tampoco sirve aquí la Prop. 3.7: $f''(0)=0$ (la tangente de $f'$ en $0$ es horizontal).

Comprobación con un modelo: si $f'(x)=x^3$, $f'(-1)=-1<0$ y $f'(1)=1>0$ (sympy).

---

### Ejercicio 3.36 (E p. 120)

> La gráfica de la derivada de una función dos veces derivable $f$ con dominio todo $\mathbb R$ aparece en la siguiente figura. [Gráfica de $f'$: corta al eje en $x=-2$ subiendo, tiene un máximo de altura $2$ en $x=-1$, vale $1$ en $x=0$, toca el eje en $x=1$ sin cruzarlo y luego crece.] Razona si alguna de las siguientes afirmaciones es correcta: **a)** $f$ tiene dos puntos críticos, pero un solo extremo relativo. **b)** $f$ tiene dos extremos relativos. **c)** La ecuación $f''(x)=0$ no tiene soluciones reales.

**Idea en una frase.** Un cero de $f'$ en el que $f'$ **cruza** el eje da extremo; si solo **toca** el eje y rebota, no hay extremo (es un punto de silla).

1. **Críticos.** $f$ es derivable en $\mathbb R$; críticos = ceros de $f'$: $x=-2$ y $x=1$ (dos).
2. **En $x=-2$.** A la izquierda $f'<0$ ($f$ decrece), a la derecha $f'>0$ ($f$ crece): mínimo relativo (Prop. 3.5, U p. 130).
3. **En $x=1$.** A ambos lados $f'>0$: $f$ es creciente en todo $(-2,\infty)$ y no puede tener extremo en $1$. Es un **punto de silla** (Def. 3.7, U p. 131).
4. **a) es correcta y b) es falsa.**
5. **c).** $f''$ es la derivada de $f'$. La función $f'$ tiene un máximo relativo en $x=-1$ y un mínimo relativo en $x=1$ (se ve en la gráfica); como $f'$ es derivable, esos son puntos críticos de $f'$ y en ellos $(f')'=0$ (Prop. 3.6 aplicada a $f'$). Luego $f''(-1)=f''(1)=0$: **c) es falsa**.

**Receta.** Clasificar cada cero de $f'$ mirando si $f'$ cambia de signo; los «picos» y «valles» de la gráfica de $f'$ son ceros de $f''$.

**Error típico.** Contar «dos ceros de $f'$ = dos extremos». Un cero donde $f'$ no cambia de signo no es extremo.

Comprobación con un modelo que reproduce la figura: $f'(x)=\tfrac12(x+2)(x-1)^2$ da $f'(0)=1$, $f'(-1)=2$, ceros $-2$ y $1$, y $f''=0$ en $-1$ y $1$ (sympy).

---

### Ejercicio 3.30 (E p. 114)

> Sea $f$ la función dada por $f(x)=ax^3+bx^2+cx+d$, para $a,b,c,d\in\mathbb R$ con $a\ne0$. ¿Es cierto que $f$ tiene exactamente un máximo local y un mínimo local en su dominio, cualesquiera que sean $a,b,c,d$?

**Idea en una frase.** Para que haya un máximo y un mínimo, $f'$ (un polinomio de grado 2) tiene que cortar el eje dos veces, y eso no siempre pasa.

1. **Derivada.** $f'(x)=3ax^2+2bx+c$, polinomio de grado 2 (porque $a\ne0$).
2. **Dónde pueden estar los extremos.** $f$ es derivable en $\mathbb R$: los extremos relativos solo pueden estar en los ceros de $f'$ (Prop. 3.6, U p. 131).
3. **Un polinomio de grado 2 puede tener 0, 1 o 2 raíces reales.** Basta un contraejemplo para responder «no»:
   - **Sin raíces:** $f(x)=2x^3+6x$, $f'(x)=6x^2+6>0$ siempre: $f$ es estrictamente creciente (Prop. 2.4) y **no tiene ningún extremo**.
   - **Raíz doble:** $f(x)=x^3$, $f'(x)=3x^2$ se anula solo en $0$, pero $f'\ge0$ a ambos lados: no cambia de signo y no hay extremo (punto de silla; en §3.5 se verá que es de inflexión).
4. **Respuesta: no es cierto.** Solo ocurre cuando $f'$ tiene dos raíces reales distintas, es decir, cuando su discriminante $4b^2-12ac>0$ (ej.: $x^3-3x$, críticos $\pm1$).

**Receta.** Para preguntas «¿siempre…?», buscar un **contraejemplo** sencillo; en cúbicas, mirar el discriminante de $f'$.

**Error típico.** Pensar «las cúbicas tienen forma de S con un pico y un valle»: solo algunas.

Verificación sympy: $6x^2+6$ sin raíces reales; $3x^2$ raíz $0$; $x^3-3x$ críticos $\pm1$.

---

### Ejercicio 3.38 (E p. 121)

> Queremos construir un rectángulo con 100 centímetros de perímetro de tal forma que su área sea máxima. ¿Cuál es la longitud de sus lados?

(Igual que el Ejemplo 3.25 de U, pp. 132-133, con metros en lugar de centímetros.)

**Idea en una frase.** Con la condición del perímetro se despeja un lado en función del otro, y el área queda como función de **una** variable en un intervalo cerrado.

1. **Variables.** Lados $a$ y $b$ (cm). Perímetro: $2a+2b=100\Rightarrow b=50-a$.
2. **Función a optimizar.** Área $S(a)=a(50-a)=50a-a^2$.
3. **Dominio.** Los lados no pueden ser negativos: $a\ge0$ y $b=50-a\ge0$, es decir, $a\in[0,50]$. (En $a=0$ o $a=50$ el «rectángulo» es un segmento de área $0$; incluir esos valores permite usar el intervalo cerrado.)
4. **Críticos.** $S'(a)=50-2a=0\iff a=25$, que está dentro de $[0,50]$.
5. **Comparar (Prop. 3.4, U p. 126).** $S$ es continua en $[0,50]$, así que alcanza su máximo (Prop. 1.15) en $0$, $25$ o $50$: $S(0)=0$, $S(25)=625$, $S(50)=0$. **Máximo absoluto en $a=25$.**
6. (Además $S''=-2<0$: máximo relativo por la Prop. 3.7.)
7. **Respuesta:** $a=b=25$ cm (un **cuadrado**), con área $625$ cm².

**Receta (problemas de optimización).** (1) dibujar y nombrar variables; (2) escribir la cantidad a optimizar; (3) usar la condición para dejar **una** variable; (4) escribir el **dominio**; (5) puntos críticos; (6) comparar con los bordes o usar $f''$, y justificar que es **absoluto**.

**Error típico.** Quedarse en $S''<0$ («máximo relativo») sin decir por qué es el máximo **absoluto**. Aquí se justifica comparando con los bordes.

Verificación sympy: $S'=0\Rightarrow a=25$, $S(25)=625$.

---

### Ejercicio 3.37 (E pp. 120-121)

> A una lámina de acero cuadrada de 40 centímetros de lado se le quitan cuatro cuadrados iguales en sus esquinas y se doblan los lados para formar una caja de base cuadrada. Calcula el lado del cuadrado que hay que quitar en las esquinas para maximizar el volumen de la caja.

**Idea en una frase.** Si quitas cuadrados muy pequeños la caja es casi plana; si los quitas muy grandes, no queda base: el volumen máximo está en medio.

1. **Variable.** $d$ = lado del cuadrado recortado (cm) = altura de la caja. La base es un cuadrado de lado $40-2d$ (se quita $d$ por cada lado).
2. **Función.** $V(d)=(40-2d)^2d=4d^3-160d^2+1600d$.
3. **Dominio.** $d\ge0$ y $40-2d\ge0$: $d\in[0,20]$.
4. **Críticos.** $V'(d)=12d^2-320d+1600=4(3d^2-80d+400)=0\iff d=\dfrac{80\pm\sqrt{6400-4800}}{6}=\dfrac{80\pm40}{6}$, es decir, $d=\tfrac{20}{3}$ o $d=20$. El valor $d=20$ es un borde del intervalo (no es interior); el único crítico interior es $d=\tfrac{20}{3}$.
5. **Comparar (Prop. 3.4).** $V(0)=0$, $V(20)=0$ (no queda base) y $V(20/3)=\big(\tfrac{80}{3}\big)^2\cdot\tfrac{20}{3}=\tfrac{128000}{27}\approx4740{,}7$ cm³. **Máximo absoluto en $d=20/3$.**
6. (Comprobación con la Prop. 3.7: $V''(d)=24d-320$, $V''(20/3)=160-320=-160<0$: máximo relativo.)
7. **Respuesta:** $d=\tfrac{20}{3}\approx6{,}67$ cm (volumen máximo $\tfrac{128000}{27}\approx4741$ cm³).

**Receta.** Igual que 3.38. Un cero de $f'$ que cae en un borde se trata como extremo del intervalo, no como crítico.

**Error típico / omisión de E.** E justifica solo con $V''(20/3)<0$ («el volumen es máximo»), que da un máximo **relativo**. Para que sea el máximo absoluto hay que comparar con $V(0)=V(20)=0$ (paso 5). E tampoco da el volumen máximo.

Verificación sympy: críticos $\{20/3,20\}$, $V''(20/3)=-160$, $V(20/3)=128000/27$.

---

### Ejercicio 3.32 (E pp. 116-117)

> Sea $f$ la función dada por $f(x)=\dfrac{1-x^2}{x+3}$. ¿Dónde alcanza los extremos relativos y absolutos en el intervalo $[-1,1]$? ¿Cuáles son esos valores extremos?

(Es el mismo ejercicio que **X Feb 2010, 1ª semana, Ej. 5**; ver §2.)

**Idea en una frase.** Es el «método del intervalo cerrado»: lista de candidatos (bordes + críticos), evaluar y comparar.

1. **Continuidad.** $f$ es cociente de polinomios y el denominador solo se anula en $x=-3\notin[-1,1]$: $f$ es continua y derivable en $[-1,1]$. Por la Prop. 1.15 (U p. 52) **seguro** que tiene máximo y mínimo absolutos ahí.
2. **Derivada (regla del cociente, U §2.2).** $f'(x)=\dfrac{(-2x)(x+3)-(1-x^2)\cdot1}{(x+3)^2}=\dfrac{-x^2-6x-1}{(x+3)^2}=-\dfrac{x^2+6x+1}{(x+3)^2}$.
3. **Críticos.** No hay puntos de no derivabilidad en $[-1,1]$. $f'=0\iff x^2+6x+1=0\iff x=-3\pm\sqrt8$. Numéricamente, $-3+\sqrt8\approx-0{,}172\in(-1,1)$ y $-3-\sqrt8\approx-5{,}83\notin[-1,1]$. Único crítico: $x_1=-3+\sqrt8=-3+2\sqrt2$.
4. **Clasificar $x_1$ (Prop. 3.7).** $f''(x)=-\dfrac{16}{(x+3)^3}$. En $x_1$ se tiene $x_1+3=\sqrt8$, así que $f''(x_1)=-\dfrac{16}{(\sqrt8)^3}=-\dfrac{16}{8\sqrt8}=-\dfrac{2}{\sqrt8}=-\dfrac{\sqrt2}{2}<0$: **máximo relativo**. (Basta el signo: $x+3>0$ en $[-1,1]$, luego $f''<0$ en todo el intervalo.)
5. **Valores (Prop. 3.4).** $f(-1)=0$, $f(1)=0$ y $f(x_1)=6-2\sqrt8=6-4\sqrt2\approx0{,}3431$. (Cálculo: $x_1^2=17-6\sqrt8$, luego $1-x_1^2=6\sqrt8-16$; dividido entre $x_1+3=\sqrt8$ da $6-\tfrac{16}{\sqrt8}=6-2\sqrt8$.)
6. **Conclusión.** Máximo absoluto (y relativo) en $x_1=-3+2\sqrt2\approx-0{,}17$, de valor $6-4\sqrt2\approx0{,}343$. Mínimo absoluto en $x=-1$ y en $x=1$, de valor $0$. Con la Def. 3.6 de U, esos bordes son también **mínimos relativos** (Prop. 3.6, U p. 131).

**Receta (método del intervalo cerrado).** $f$ continua en $[a,b]$ → críticos interiores ($f'=0$ o no derivable) → evaluar $f$ en los críticos y en $a$, $b$ → el mayor valor es el máximo absoluto y el menor, el mínimo absoluto.

**Error típico.** Dar los puntos cuando se piden los valores, o al revés (aviso de U p. 127). Aquí el máximo **se alcanza en** $x_1\approx-0{,}17$ y **vale** $\approx0{,}34$.

**Errata / fuente.** El `.txt` deja ilegible $f''(x_1)$; **el PDF (E p. 116) escribe $-2/\sqrt8$**, que es correcto ($=-\sqrt2/2$). No es errata de E. En cambio, la solución de **X (Feb 2010)** termina con «No tiene mínimos relativos en este intervalo», que **contradice la Prop. 3.6 de U** y al propio E («Todo extremo absoluto es, en particular, un extremo relativo»): con la Def. 3.6, $x=\pm1$ son mínimos relativos. La frase de X solo vale si «relativo» significa «interior» (convenio de Stewart).

Verificación sympy: $f'=-(x^2+6x+1)/(x+3)^2$, $f''=-16/(x+3)^3$, $f''(x_1)=-\sqrt2/2$, $f(x_1)=6-4\sqrt2\approx0{,}343146$, $f(\pm1)=0$.

---

### Ejercicio 3.31 (E pp. 115-116)

> Un móvil recorre un espacio $s(t)=t^4-8t^3+18t^2$, expresado en metros, siendo $t$ el tiempo expresado en segundos. Supongamos que el instante inicial es $t=0$ y que $t\in[0,+\infty)$. ¿Cuáles son las expresiones de su velocidad y de su aceleración? ¿Alcanza la velocidad algún valor máximo o mínimo relativo? ¿Cuándo? ¿Y absolutos?

**Idea en una frase.** La función a estudiar es la **velocidad** $v$, así que «su derivada» es la aceleración $a$: los críticos de $v$ son los ceros de $a$.

1. **Velocidad y aceleración** (U §2.1, interpretación física de la derivada). $v(t)=s'(t)=4t^3-24t^2+36t$ m/s; $a(t)=v'(t)=s''(t)=12t^2-48t+36$ m/s².
2. **Críticos de $v$.** $a(t)=0\iff12(t^2-4t+3)=0\iff12(t-1)(t-3)=0\iff t=1$ o $t=3$. Además $t=0$ es el borde del dominio $[0,\infty)$: también es candidato (Prop. 3.6).
3. **Signo de $a=v'$** (el factor $12$ es positivo y no cambia el signo):

   | intervalo | $t-1$ | $t-3$ | $a=v'$ | $v$ |
   |---|---|---|---|---|
   | $(0,1)$ | $-$ | $-$ | $+$ | crece |
   | $(1,3)$ | $+$ | $-$ | $-$ | decrece |
   | $(3,\infty)$ | $+$ | $+$ | $+$ | crece |

4. **Relativos (Prop. 3.5).** $t=1$: crece y luego decrece → **máximo relativo**, $v(1)=16$ m/s. $t=3$: decrece y luego crece → **mínimo relativo**, $v(3)=0$. $t=0$: borde izquierdo y $v$ crece justo a su derecha → **mínimo relativo** (en el borde), $v(0)=0$. (Con la Prop. 3.7: $v''(t)=a'(t)=24t-48$; $v''(1)=-24<0$ máximo; $v''(3)=24>0$ mínimo.)
5. **Absolutos.** $\lim_{t\to+\infty}v(t)=+\infty$ (domina $4t^3$): $v$ toma valores tan grandes como se quiera y **no hay máximo absoluto**. Para el mínimo: $v(t)=4t(t-3)^2\ge0$ para $t\ge0$ y vale $0$ en $t=0$ y $t=3$: **mínimo absoluto $0$ en $t=0$ y en $t=3$**.
6. **Respuesta.** $v=4t^3-24t^2+36t$, $a=12t^2-48t+36$. Máximo relativo en $t=1$ s ($16$ m/s); mínimos relativos y absolutos en $t=0$ y $t=3$ s ($0$ m/s); sin máximo absoluto.

**Receta.** «Extremos de la velocidad» = extremos de $s'$: derivar una vez más y hacer tabla de signos. En dominios no acotados, el máximo/mínimo absoluto se decide con los **límites** en el infinito.

**Error típico.** Calcular los extremos de $s$ (ceros de $v$) en lugar de los de $v$ (ceros de $a$).

**Erratas de E.** (i) Escribe «$a(t)=(t-1)(t-3)$»; debe ser $a(t)=12(t-1)(t-3)$ (el factor $12$ no cambia los signos ni la conclusión). (ii) Dice «la **derivada** no tiene asíntotas horizontales»: quiere decir la **velocidad**. (iii) Para el mínimo absoluto E compara $v(0)=v(3)=0$ pero no justifica que $v$ nunca sea negativa; la factorización $v=4t(t-3)^2$ (paso 5) lo hace inmediato.

Verificación sympy: $a=12(t-3)(t-1)$; $v(0),v(1),v(3)=0,16,0$; $v=4t(t-3)^2$; $\lim_{t\to\infty}v=\infty$.

---

### Ejercicio 3.33 (E pp. 117-118)

> La distancia en metros de una partícula a un punto fijo $P$ en función del tiempo viene dada por $s(t)=at^3+bt^2+ct+d$, $t\in[0,6]$, donde $t$ es el tiempo en segundos. Se sabe que la partícula está en $P$ en el instante inicial $t=0$ y que después de un segundo se encuentra a $10$ metros. También se sabe que la velocidad de la partícula es nula en $t=0$ y $t=5$. Determina: los valores de los coeficientes $a$, $b$, $c$ y $d$ y los valores extremos relativos y absolutos de la distancia de la partícula a $P$ en el intervalo de tiempo $[0,6]$.

**Idea en una frase.** Primero se traduce cada frase del enunciado a una ecuación; luego es un problema de intervalo cerrado.

1. **Traducir los datos** (con $\dot s=s'$, notación de E): «está en $P$ en $t=0$» → $s(0)=0$; «a 10 m tras 1 s» → $s(1)=10$; «velocidad nula en 0 y 5» → $\dot s(0)=0$, $\dot s(5)=0$.
2. **Sistema.** $\dot s(t)=3at^2+2bt+c$. Queda: $d=0$; $a+b+c+d=10$; $c=0$; $75a+10b+c=0$.
3. **Resolver.** Con $c=d=0$: $a+b=10$ y $75a+10b=0\Rightarrow b=-7{,}5a$. Entonces $a-7{,}5a=10\Rightarrow a=-\tfrac{20}{13}$ y $b=\tfrac{150}{13}$. Así $s(t)=-\tfrac{20}{13}t^3+\tfrac{150}{13}t^2$.
4. **Críticos en $(0,6)$.** $\dot s(t)=-\tfrac{60}{13}t^2+\tfrac{300}{13}t=-\tfrac{60}{13}t(t-5)=0\iff t=0$ (borde) o $t=5$ (interior).
5. **Monotonía.** Para $0<t<5$: $t>0$ y $t-5<0$, y con el signo $-$ delante, $\dot s>0$ ($s$ crece). Para $5<t<6$: $\dot s<0$ ($s$ decrece). Por la Prop. 3.5, máximo relativo en $t=5$ (o con la Prop. 3.7: $\ddot s(5)=-\tfrac{300}{13}<0$).
6. **Valores.** $s(0)=0$; $s(5)=\tfrac{1250}{13}\approx96{,}15$ m; $s(6)=\tfrac{1080}{13}\approx83{,}08$ m.
7. **Conclusión.** Mínimo absoluto $0$ en $t=0$ (también relativo, en el borde). Máximo absoluto y relativo $\tfrac{1250}{13}$ m en $t=5$. En $t=6$ hay un **mínimo relativo** (borde derecho: $s$ viene decreciendo, así que en $[5,6]$ el valor más pequeño es $s(6)$), pero **no** absoluto, porque $s(0)=0<s(6)$.

**Receta.** Condiciones del tipo «pasa por… / velocidad nula en…» → ecuaciones lineales en los coeficientes. Después, método del intervalo cerrado y, para cada borde, mirar si la función crece o decrece al llegar a él.

**Error típico.** Olvidar que $t=6$ es candidato (no es crítico, es borde) o decir que es mínimo absoluto.

Verificación sympy: $a=-20/13$, $b=150/13$, $c=d=0$; $\ddot s(5)=-300/13$; $s(5)=1250/13$, $s(6)=1080/13$.

---

### Ejercicios de E de §3.5 (pendientes, no se resuelven aquí)

3.39, 3.40, 3.41, 3.42, 3.45, 3.48 (concavidad/convexidad e inflexión) y los mixtos 3.43 (extremos + inflexión), 3.46 (representación completa), 3.47 (construcción de funciones): **pendientes del tema 3.5**. Notas al revisar las imágenes de E:
- **3.40** (E p. 123): el **PDF es correcto** («$f$ es derivable si $x\ne4$… no es derivable si $x=4$»); la «errata» del dossier era un fallo de `pdftotext` (pierde la barra de $\ne$).
- **3.41** (E p. 123): el enunciado real es $f(x)=\sqrt{\lvert x\rvert}$, **no** $\lvert x\rvert$ como dice el dossier.
- **3.43** (E pp. 125-126): la parte «¿alcanza extremos relativos?» es de 3.4: $f'(x)=1/(1-x)^2>0$ nunca se anula y $x=1$ no está en el dominio → no hay extremos relativos.

---

## 2. Así lo preguntan en el examen (X, solo §3.4)

Enunciados leídos de la imagen de la página PDF de X.

### X1. Febrero 2010, 1ª semana (X p. 2), Ejercicio 5 (3 puntos)

> Calcule los extremos relativos y absolutos de $f(x)=\dfrac{1-x^2}{x+3}$ en el intervalo $[-1,1]$.

Es **idéntico a E 3.32** (resuelto arriba). Lo que hay que escribir en el examen: continuidad en $[-1,1]$ (Prop. 1.15) → $f'$ → crítico $x_1=-3+2\sqrt2$ (el otro, fuera) → $f''(x_1)=-\sqrt2/2<0$ → tabla $f(-1)=0$, $f(x_1)=6-4\sqrt2\approx0{,}343$, $f(1)=0$ → conclusiones.

**Errata en X.** La solución termina con «No tiene mínimos relativos en este intervalo». Según U (Def. 3.6 y Prop. 3.6, pp. 130-131) y E 3.32, $x=\pm1$ **sí** son mínimos relativos (y absolutos). En el examen: «mínimo absoluto (y relativo, en el borde) en $x=-1$ y $x=1$».

**Receta.** Método del intervalo cerrado.

### X2. Febrero 2012, Mecánica Modelo A, 1ª semana (X p. 19), Pregunta corta 2 (1 punto)

> Dada la función $f(x)=\lvert x-1\rvert$, ¿tiene un extremo en $x=1$? ¿Es máximo o mínimo? Justifique la respuesta.

**Idea.** Igual que E 3.34.
1. $f$ es continua (valor absoluto de un polinomio).
2. $\lvert x-1\rvert\ge0$ para todo $x$, y $\lvert x-1\rvert=0\iff x=1$.
3. Luego $f(x)\ge f(1)=0$ para todo $x$: **mínimo absoluto en $x=1$** (Def. 3.4, U p. 126), que también es relativo.

**Receta.** Valor absoluto o cuadrado: la desigualdad $\ge0$ da el mínimo sin derivar.
**Error típico.** Intentar resolver $f'(1)=0$: $f$ no es derivable en $1$.

### X3. Febrero 2014, Mecánica Modelo A (X p. 40), Pregunta corta 2 (1 punto)

> Razone si es verdadero o falso que la función $f(x)=x^3\cos(x+1)$ alcanza el máximo y el mínimo absoluto en el intervalo $[-\pi,\pi]$.

**Idea en una frase.** No hay que calcular nada: una función continua en un intervalo **cerrado y acotado** siempre alcanza su máximo y su mínimo.

1. $x^3$ es un polinomio y $\cos(x+1)$ es composición de continuas: su producto es **continuo** en $\mathbb R$ (U §1.4).
2. $[-\pi,\pi]$ es cerrado y acotado.
3. Por la **Prop. 1.15** (U p. 52) existen $c,d\in[-\pi,\pi]$ con $f(c)\le f(x)\le f(d)$: alcanza mínimo y máximo absolutos. **Verdadero.**

**Precisión sobre la solución de X.** X justifica con «la proposición 3.4 … los extremos absolutos se alcanzan en los extremos relativos o en los extremos del intervalo». La Prop. 3.4 dice **dónde** se alcanzan (en los bordes o en **puntos críticos**, no «extremos relativos»), pero la **existencia** la garantiza la Prop. 1.15. Lo correcto es citar la 1.15 (y, si se quiere, la 3.4).

Comprobación numérica (no se pide): máximo $\approx16{,}75$ en $x=-\pi$ (un borde) y mínimo $\approx-17{,}73$ cerca de $x\approx2{,}94$.

**Receta.** «¿Alcanza máximo y mínimo?» → continua + cerrado y acotado ⇒ sí (Prop. 1.15).
**Error típico.** Ponerse a derivar y resolver $f'=0$ (aquí es una ecuación trascendente sin solución exacta).

### X4. Septiembre 2017, Mecánica Modelo A (X p. 85), Pregunta corta 2 (1 punto)

> Señale los puntos donde puede alcanzar los extremos relativos la función $f(x)=x^3-3x^2-9x+2$. No es necesario estudiar si son extremos.

1. $f$ es polinomio: derivable en $\mathbb R$ y sin bordes; los extremos relativos solo pueden estar donde $f'=0$ (Prop. 3.6, U p. 131).
2. $f'(x)=3x^2-6x-9=3(x^2-2x-3)=3(x+1)(x-3)$.
3. **Candidatos: $x=-1$ y $x=3$.**
4. (No se pide, pero: $f''(x)=6x-6$; $f''(-1)=-12<0$, máximo relativo con $f(-1)=7$; $f''(3)=12>0$, mínimo relativo con $f(3)=-25$.)

**Receta.** «Dónde puede alcanzar» = puntos críticos.
**Error típico.** Factorizar mal: comprobar sustituyendo ($3(-1)^2-6(-1)-9=0$).

### X5. Septiembre 2017, Mecánica Modelo A (X p. 87), Ejercicio 6 (3 puntos)

> Encuentre dos números positivos tal que su suma sea 9 y su producto sea máximo.

La solución de X solo dice «Es el ejemplo 6.25 del libro. Han sido errores comunes no considerar $x,y\ge0$ o no comprobar que es un máximo». Esa referencia **no corresponde a U** (en U el problema análogo es el Ejemplo 3.25, p. 132). Resolución completa:

**Idea en una frase.** Como en el rectángulo de perímetro fijo: suma fija → producto máximo cuando los dos números son iguales.

1. **Variables y condición.** $x,y>0$, $x+y=9\Rightarrow y=9-x$.
2. **Función.** $P(x)=x(9-x)=9x-x^2$.
3. **Dominio.** $x>0$ y $9-x>0$: $x\in(0,9)$. Para poder usar la Prop. 1.15, se estudia $P$ en $[0,9]$ (en los bordes $P=0$, que no es el máximo, así que añadirlos no cambia la respuesta).
4. **Críticos.** $P'(x)=9-2x=0\iff x=\tfrac92\in(0,9)$.
5. **Es máximo absoluto.** $P(0)=P(9)=0<P(9/2)=\tfrac{81}{4}$ (Prop. 3.4). Además $P''=-2<0$ (Prop. 3.7).
6. **Respuesta:** $x=y=\tfrac92$, producto $\tfrac{81}{4}=20{,}25$.

**Receta / error típico.** Los dos errores que cita la corrección: no escribir el dominio ($x\in(0,9)$) y no justificar que es máximo (comparar con los bordes o $P''<0$).

### X6. I. Electrónica Industrial y Automática, sin fecha (índice: «Electrónica 3»; X p. 104), Pregunta corta 2 (1 punto)

> Calcule los extremos absolutos de la función dada por $f(x)=xe^{-x}$ en el intervalo $[0,2]$.

1. $f$ es continua y derivable (producto de funciones continuas y derivables): Prop. 1.15 y 3.4 aplicables.
2. $f'(x)=e^{-x}-xe^{-x}=(1-x)e^{-x}$. Como $e^{-x}>0$ siempre, $f'=0\iff x=1\in(0,2)$.
3. Tabla: $f(0)=0$; $f(1)=e^{-1}\approx0{,}368$; $f(2)=2e^{-2}\approx0{,}271$.
4. **Mínimo absoluto $0$ en $x=0$; máximo absoluto $1/e$ en $x=1$.**

**Receta.** Intervalo cerrado; la exponencial nunca se anula y se «quita» al buscar ceros de $f'$.
**Error típico.** Responder solo «el máximo es $x=1$» (punto) cuando se pregunta el extremo (valor $1/e$): dar los dos.

### X7. «Examen 5 elaborado con exámenes de asignaturas similares» (X pp. 122-123), Ejercicio 3

> Señale la afirmación correcta relativa a la función $f(x)=x^4-2x^3$: A) Es una función creciente; B) Tiene dos extremos relativos; C) Tiene un punto de silla; D) Ninguna de las anteriores.

(Es el Ejemplo 3.24 de U, p. 132.)

**Idea en una frase.** Si $f''(c)=0$ hay que seguir derivando hasta la primera derivada no nula y mirar si su orden es par o impar.

1. $f'(x)=4x^3-6x^2=2x^2(2x-3)=0\iff x=0$ o $x=\tfrac32$.
2. $f''(x)=12x^2-12x$: $f''(3/2)=27-18=9>0$ → **mínimo relativo** en $3/2$ (Prop. 3.7), con $f(3/2)=-\tfrac{27}{16}$.
3. $f''(0)=0$: la Prop. 3.7 no decide. $f'''(x)=24x-12$, $f'''(0)=-12\ne0$: la primera derivada no nula es la **3ª (orden impar)** → **punto de silla** en $0$ (Prop. 3.8, U p. 132).
4. Comprobación con signos: $f'=2x^2(2x-3)$ es negativa a ambos lados de $0$ (el factor $x^2\ge0$ no cambia de signo), así que $f$ decrece antes y después de $0$: no hay extremo.
5. A) falsa ($f'<0$ en $(-\infty,3/2)$ salvo en $0$); B) falsa (solo hay uno); **C) correcta**.

**Receta.** Criterio de orden superior: primera derivada no nula de orden par → extremo (positiva: mínimo; negativa: máximo); de orden impar → silla.
**Error típico.** Contar los dos ceros de $f'$ como «dos extremos» (opción B).

### X8. Febrero 2018, 1ª semana (X p. 146), Ejercicio 6 (3 puntos)

> Encuentre dos números reales negativos tales que su suma sea $-15$ y su producto sea máximo. Razone la solución.

1. $x,y<0$, $x+y=-15\Rightarrow y=-15-x$; $y<0\iff x>-15$. Dominio: $x\in(-15,0)$.
2. $P(x)=x(-15-x)=-15x-x^2$.
3. $P'(x)=-15-2x=0\iff x=-\tfrac{15}{2}\in(-15,0)$, y entonces $y=-\tfrac{15}{2}$.
4. Máximo absoluto: estudiando $P$ en $[-15,0]$, $P(-15)=P(0)=0<P(-15/2)=\tfrac{225}{4}$ (Prop. 3.4); además $P''=-2<0$.
5. **Respuesta:** $x=y=-\tfrac{15}{2}$, producto $\tfrac{225}{4}=56{,}25$.

**Imprecisiones de la solución de X.** (i) Escribe el dominio como $x\le0$, $y\le0$, pero el enunciado dice «negativos» (estricto); el máximo no cambia porque en los bordes el producto es $0$. (ii) Mezcla notación: define $f(x)=x(-15-x)$ (una variable) y luego evalúa «$f(-\tfrac{15}{2},-\tfrac{15}{2})$» y «$f(-15,0)$» como si fuera de dos variables. En el examen, escribir $P(-15/2)=225/4$ y $P(-15)=P(0)=0$.

**Receta.** Igual que X5.

### X9. «Examen 1 elaborado con exámenes de asignaturas similares» (X pp. 109-110), Ejercicio 4 — **requiere Tema 6**

> Dada la función $F(x)=\int_0^x t\operatorname{sen}t\,dt$ definida en $[0,\infty)$ señale la opción correcta: A) $F$ es creciente; B) $F$ tiene un máximo en $x=7\pi$; C) $F$ es decreciente; D) Ninguna de las anteriores.

(Usa el teorema fundamental del cálculo, U Tema 6. Marcar como «se entiende del todo tras el Tema 6».)

1. $F'(x)=x\operatorname{sen}x$ (teorema fundamental).
2. $F'$ cambia de signo (p. ej. $F'(\pi/2)=\pi/2>0$, $F'(3\pi/2)=-3\pi/2<0$): A) y C) son falsas.
3. En $x=7\pi$: $F'(7\pi)=0$. Justo antes ($x\in(6\pi,7\pi)$) $\operatorname{sen}x>0$ y $F'>0$; justo después ($x\in(7\pi,8\pi)$) $\operatorname{sen}x<0$ y $F'<0$ → **máximo relativo** (Prop. 3.5). Con la Prop. 3.7: $F''(x)=\operatorname{sen}x+x\cos x$, $F''(7\pi)=-7\pi<0$.
4. **Respuesta B** (máximo relativo; no absoluto, porque $F(x)=\operatorname{sen}x-x\cos x$ no está acotada).

**Receta.** Extremos de una función definida por una integral: derivar con el teorema fundamental y aplicar los criterios de siempre a $F'$.

Verificación sympy (todos los de X): X4 $f'=3(x-3)(x+1)$, $f(-1)=7$, $f(3)=-25$; X5 $x=9/2$, $P=81/4$; X6 $f'=-(x-1)e^{-x}$, $f(1)=1/e$, $f(2)=2e^{-2}\approx0{,}2707$; X7 críticos $0$, $3/2$, $f''(0)=0$, $f'''(0)=-12$, $f''(3/2)=9$, $f(3/2)=-27/16$; X8 $x=-15/2$, $P=225/4$; X9 $F=\operatorname{sen}x-x\cos x$, $F''(7\pi)=-7\pi$, $F'(6{,}9\pi)>0>F'(7{,}1\pi)$. X3: búsqueda numérica en una malla de $200\,001$ puntos.

---

## 3. Ejemplos propios (dificultad creciente)

### Propio 1 — Intervalo cerrado (propio)

> Halla los extremos absolutos de $f(x)=x^3-3x+1$ en $[-2,3]$.

**Idea en una frase.** Lista de candidatos y tabla de valores; el ganador puede ser un borde.

1. $f$ es continua en $[-2,3]$ → tiene máximo y mínimo (Prop. 1.15, U p. 52).
2. $f'(x)=3x^2-3=3(x-1)(x+1)=0\iff x=\pm1$, ambos en $(-2,3)$.
3. Tabla: $f(-2)=-1$, $f(-1)=3$, $f(1)=-1$, $f(3)=19$.
4. **Máximo absoluto $19$ en $x=3$** (un borde, no un crítico). **Mínimo absoluto $-1$, alcanzado en dos puntos: $x=-2$ y $x=1$.**

**Receta.** Método del intervalo cerrado (Prop. 3.4).
**Error típico.** Creer que el máximo absoluto está en el máximo relativo $x=-1$ (valor $3$): el borde $x=3$ da más. Y recordar que un mismo valor mínimo puede alcanzarse en varios puntos.

### Propio 2 — Punto crítico con 2ª derivada y absolutos en $\mathbb R$ (propio)

> Estudia los extremos relativos y absolutos de $f(x)=xe^{-x^2/2}$ en $\mathbb R$.

**Idea en una frase.** Los relativos se clasifican con $f''$; para los absolutos en un dominio no acotado hay que mirar qué pasa en $\pm\infty$.

1. $f'(x)=e^{-x^2/2}+x\cdot(-x)e^{-x^2/2}=(1-x^2)e^{-x^2/2}$. Como $e^{-x^2/2}>0$: críticos $x=\pm1$.
2. $f''(x)=x(x^2-3)e^{-x^2/2}$. $f''(1)=-2e^{-1/2}<0$ → máximo relativo, $f(1)=e^{-1/2}\approx0{,}607$. $f''(-1)=2e^{-1/2}>0$ → mínimo relativo, $f(-1)=-e^{-1/2}$ (Prop. 3.7).
3. Límites: $\lim_{x\to+\infty}xe^{-x^2/2}=0$ y $\lim_{x\to-\infty}xe^{-x^2/2}=0$ (la exponencial gana; L'Hôpital, U §2.3). Además $f>0$ si $x>0$ y $f<0$ si $x<0$.
4. En $(0,\infty)$, $f'>0$ en $(0,1)$ y $f'<0$ en $(1,\infty)$: $f$ sube hasta $x=1$ y luego baja, así que su mayor valor ahí es $f(1)$. En $(-\infty,0]$, $f\le0<f(1)$. Luego **máximo absoluto $e^{-1/2}$ en $x=1$**; igual (o porque $f(-x)=-f(x)$) **mínimo absoluto $-e^{-1/2}$ en $x=-1$**.

**Receta.** Dominio no acotado: relativos con $f''$; absolutos con la monotonía y los límites en $\pm\infty$ (como el Ejemplo 3.21 de U, p. 128).
**Error típico.** Afirmar «es absoluto porque $f''<0$»: la 2ª derivada solo da información **local**.

### Propio 3 — Caso $f''(c)=0$: derivadas de orden superior (propio)

> Clasifica los puntos críticos de $f(x)=x^5-5x^4$.

**Idea en una frase.** Cuando $f''(c)=0$ la Prop. 3.7 calla: se sigue derivando.

1. $f'(x)=5x^4-20x^3=5x^3(x-4)$: críticos $x=0$ y $x=4$.
2. $x=4$: $f''(x)=20x^3-60x^2$, $f''(4)=1280-960=320>0$ → mínimo relativo, $f(4)=-256$.
3. $x=0$: $f''(0)=0$; $f'''(x)=60x^2-120x$, $f'''(0)=0$; $f^{(4)}(x)=120x-120$, $f^{(4)}(0)=-120\ne0$. La primera derivada no nula es de **orden 4 (par)** y **negativa** → **máximo relativo** en $0$, $f(0)=0$ (Prop. 3.8, U p. 132).
4. Comprobación con signos de $f'=5x^3(x-4)$: para $x=-0{,}1$, $f'>0$; para $x=0{,}1$, $f'<0$ → crece y luego decrece: máximo, de acuerdo con el paso 3.
5. No hay extremos absolutos: $\lim_{x\to+\infty}f(x)=+\infty$ y $\lim_{x\to-\infty}f(x)=-\infty$.

**Receta.** Si $f''(c)=0$, seguir derivando y contar el orden de la primera no nula (par → extremo; impar → silla). Como control, mirar el signo de $f'$ a ambos lados.
**Error típico.** Decir «$f''(0)=0$, luego es punto de silla (o de inflexión)». $f''(c)=0$ **no decide nada** (compárese $x^4$, con mínimo en $0$, y $x^3$, con silla).

### Propio 4 — Optimización con restricción en un intervalo abierto (propio)

> Se quiere fabricar una lata cilíndrica cerrada de 1 litro ($1000$ cm³) gastando la menor cantidad de chapa posible. ¿Qué radio y qué altura debe tener?

**Idea en una frase.** La restricción de volumen permite eliminar la altura; queda una función del radio en $(0,\infty)$, que se estudia con monotonía y límites.

1. **Variables.** Radio $r>0$ y altura $h>0$ (cm). Restricción: $\pi r^2h=1000\Rightarrow h=\dfrac{1000}{\pi r^2}$.
2. **Superficie** (dos tapas + lateral): $A=2\pi r^2+2\pi rh=2\pi r^2+\dfrac{2000}{r}$, con $r\in(0,\infty)$.
3. **Críticos.** $A'(r)=4\pi r-\dfrac{2000}{r^2}=0\iff r^3=\dfrac{500}{\pi}\iff r_0=\sqrt[3]{500/\pi}\approx5{,}42$ cm.
4. **Relativo.** $A''(r)=4\pi+\dfrac{4000}{r^3}>0$ para todo $r>0$; en particular $A''(r_0)=12\pi>0$: mínimo relativo (Prop. 3.7).
5. **Absoluto (intervalo abierto).** $A'<0$ en $(0,r_0)$ y $A'>0$ en $(r_0,\infty)$: $A$ baja hasta $r_0$ y luego sube, así que $A(r_0)\le A(r)$ para todo $r>0$: **mínimo absoluto**. (Además $\lim_{r\to0^+}A=+\infty$ y $\lim_{r\to+\infty}A=+\infty$: no hay máximo.)
6. **Altura.** $h_0=\dfrac{1000}{\pi r_0^2}=\dfrac{1000}{\pi r_0^3}\,r_0=\dfrac{1000}{500}\,r_0=2r_0\approx10{,}84$ cm. Superficie mínima $A(r_0)\approx553{,}6$ cm².
7. **Respuesta:** $r=\sqrt[3]{500/\pi}\approx5{,}42$ cm y $h=2r\approx10{,}84$ cm (la altura es igual al diámetro).

**Receta.** Restricción → eliminar una variable → dominio (abierto) → críticos → para el absoluto: signo de $f'$ a cada lado o límites en los bordes del dominio.
**Error típico.** No usar la restricción y derivar $A=2\pi r^2+2\pi rh$ «respecto de $r$» tratando $h$ como constante.

Verificación sympy (propios): P1 $f(-2),f(-1),f(1),f(3)=-1,3,-1,19$; P2 $f''=x(x^2-3)e^{-x^2/2}$, $f''(\pm1)=\mp2e^{-1/2}$, límites $0$; P3 $f'=5x^3(x-4)$, derivadas 1ª-5ª en $0$: $0,0,0,-120,120$; $f''(4)=320$, $f(4)=-256$; P4 $r_0=5\cdot2^{2/3}/\pi^{1/3}\approx5{,}419$, $A''(r_0)=12\pi$, $h_0/r_0=2$, $A(r_0)\approx553{,}58$.

---

## 4. Resumen de erratas y avisos

| Dónde | Qué dice | Qué debería decir / comentario |
|---|---|---|
| E 3.31, p. 115 | $a(t)=(t-1)(t-3)$ | $a(t)=12(t-1)(t-3)$ (no cambia los signos). |
| E 3.31, p. 116 | «la **derivada** no tiene asíntotas horizontales» | «la **velocidad**…». El mínimo absoluto se justifica mejor con $v=4t(t-3)^2\ge0$. |
| E 3.37, p. 121 | Solo $V''(20/3)<0$ ⇒ «el volumen es máximo» | Eso es máximo relativo; falta comparar con $V(0)=V(20)=0$ para el absoluto (omisión). |
| E 3.32, p. 116 | $f''(-3+\sqrt8)=-2/\sqrt8$ | **Correcto** ($=-\sqrt2/2$). La duda del dossier venía del `.txt`. |
| E 3.34 / 3.40 | «derivable si $x=1$» / «si $x=4$» (en el `.txt`) | El **PDF dice $x\ne1$ / $x\ne4$**: no son erratas de E, sino de `pdftotext`. |
| E 3.41 (§3.5) | dossier: $f=\lvert x\rvert$ | Enunciado real: $f(x)=\sqrt{\lvert x\rvert}$. |
| X p. 2 (Feb 2010, Ej. 5) | «No tiene mínimos relativos en este intervalo» | Con la Def. 3.6 y la Prop. 3.6 de U, $x=\pm1$ son mínimos relativos (y absolutos); contradice a E 3.32. |
| X p. 40 (Feb 2014 A, PC2) | Justifica con la Prop. 3.4 («… en los extremos relativos o del intervalo») | La existencia la da la Prop. 1.15 (U p. 52); la 3.4 habla de puntos **críticos**. |
| X p. 87 (Sep 2017 A, Ej. 6) | «Es el ejemplo 6.25 del libro» | No existe en U; el análogo es el Ejemplo 3.25 (U p. 132). Resolución completa en X5. |
| X p. 146 (Feb 2018, Ej. 6) | Dominio $x\le0$, $y\le0$; evalúa $f(-15,0)$ como función de dos variables | El enunciado dice «negativos» (estricto) y $f$ es de una variable: escribir $P(-15)=P(0)=0$. |
| U Def. 3.6, p. 130 | «existe un intervalo $I\subset D$ tal que…» | Omite «que contiene a $c$» (sin eso la definición no tiene sentido). |
