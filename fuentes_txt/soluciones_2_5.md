# Unidad 2.5 — Ejercicios del Tema 2 de E que anticipan la teoría de Rolle, valor medio, monotonía y gráficas

**Ejercicios:** E 2.39-2.51 (E pp. 76-86; página impresa = PDF).

**Aviso importante sobre la teoría (comprobado en `ingenieros.txt`):** en U, Rolle, el teorema del valor medio (TVM) y la monotonía **no están en el Tema 3**. Están en la sección **§2.5 «Teoremas de Rolle y del valor medio»** del Tema 2 (U pp. 94-101). El índice de U (p. VI) lo confirma: 2.5.1 Motivación p. 94, 2.5.2 Rolle p. 95, 2.5.3 Valor medio p. 96, 2.5.4 Funciones monótonas p. 98, Autoevaluación p. 100. Del Tema 3 de U solo hace falta lo que usan 2.50-2.51: puntos críticos y extremos (§3.4, pp. 125-133) y concavidad/inflexión (§3.5, pp. 134-139). (La tabla de CLAUDE.md que dice «Tema 2: 2.1…2.4» está incompleta, porque le falta §2.5.)

Orden didáctico que seguimos aquí (se mantiene la numeración de E):

| Bloque | Ejercicios (orden de estudio) | Herramienta |
|---|---|---|
| A. Rolle y valor medio | 2.39 → 2.41 → 2.42 → 2.40 → 2.49 | U §2.5.2-2.5.3 pp. 95-97 |
| B. Monotonía | 2.43 → 2.44 → 2.47 → 2.46 → 2.48 | U §2.5.4 pp. 98-100 |
| C. Hiperbólicas y funciones constantes | 2.45 | U Teorema 2.4 p. 97 (U **no** define cosh/senh) |
| D. Identificar gráficas | 2.50 → 2.51 | U §1.4 pp. 48-49 (asíntotas), §2.5.4, §3.4-3.5 |

He podido **ver las figuras** de 2.42, 2.44, 2.50 y 2.51 renderizando las páginas del PDF de E (no están en el `.txt`). Las descripciones de las opciones que doy abajo son mías, a partir de esas imágenes.

**Aviso de extracción:** en `ejercicios.txt` se pierde la barra de «≠». En 2.40 («con s = t»), 2.42 («−2π = 2π»), 2.49 («lím … = lím …») y 2.51 («f′(0) = f′(2π) = 0») el PDF dice **≠**. Esos fallos vienen del `.txt`, no son erratas de E.

---

## Resumen de la teoría que se usa (U, página impresa)

- **Teorema de Rolle** (U §2.5.2, p. 95). Si $f:[a,b]\to\mathbb R$ es continua en $[a,b]$, derivable en $(a,b)$ y $f(a)=f(b)$, existe al menos un $c\in(a,b)$ con $f'(c)=0$.
- **Teorema del valor medio (TVM, de Lagrange)** (U §2.5.3, p. 96). Si $f$ es continua en $[a,b]$ y derivable en $(a,b)$, existe $c\in(a,b)$ con $f'(c)=\dfrac{f(b)-f(a)}{b-a}$. Geométricamente, hay una tangente paralela a la cuerda (U p. 97).
- **Teorema 2.4 (funciones constantes)** (U p. 97). $f$ es constante en $(a,b)$ $\iff$ $f'(x)=0$ para todo $x\in(a,b)$.
- **Definición 2.5 (monotonía)** (U p. 98). Creciente: $a<b\Rightarrow f(a)\le f(b)$. Estrictamente creciente: $a<b\Rightarrow f(a)<f(b)$. Lo mismo, cambiando el sentido, para decreciente.
- **Proposición 2.4** (U p. 98). En un intervalo $I$: $f'>0\Rightarrow$ estrictamente creciente; $f'<0\Rightarrow$ estrictamente decreciente; $f'\ge 0\Rightarrow$ creciente; $f'\le0\Rightarrow$ decreciente. Es **solo una condición suficiente**: $x^3$ es estrictamente creciente aunque $f'(0)=0$ (U Ej. 2.22 p. 99).
- **Derivadas laterales** (U Def. 2.3, p. 81): si existen y coinciden, $f$ es derivable; si no coinciden, no lo es.
- **Continuidad y derivabilidad**: derivable $\Rightarrow$ continua. Por tanto, discontinua $\Rightarrow$ no derivable (U §2.1).
- **Asíntotas** (U §1.4, pp. 48-49): horizontal $y=b$ si $\lim_{x\to\pm\infty}f=b$; vertical $x=a$ si algún límite lateral en $a$ es $\pm\infty$; oblicua $y=mx+b$ con $m=\lim f(x)/x$ (Prop. 1.12, p. 49).
- **Punto crítico** (U Def. 3.5, p. 126), **extremo relativo** (Def. 3.6, p. 130), **Prop. 3.5** (si la monotonía cambia, hay extremo; p. 130), **punto de silla** (Def. 3.7, p. 131), **Prop. 3.7-3.8** (criterio de la segunda derivada y de las derivadas de orden superior, pp. 131-132), **convexidad** (en U, «convexa» es la forma de $x^2$; Prop. 3.9-3.10, p. 136; inflexión en Def. 3.10 y Prop. 3.11-3.12, p. 137).

---

# BLOQUE A — Teoremas de Rolle y del valor medio

## Ejercicio 2.39 (E p. 76)

> Dada una función $f:[-1,1]\to\mathbb R$ continua en $[-1,1]$, tal que $f(-1)=f(1)$ y derivable en $(-1,1)$, se verifica:
> a) Para algún $c\in(-1,1)$ la recta tangente a la gráfica de $f$ en $(c,f(c))$ es paralela al eje $y$.
> b) Para algún $c\in(-1,1)$ la recta tangente a la gráfica de $f$ en $(c,f(c))$ es perpendicular al eje $y$.
> c) Para algún $c\in(-1,1)$ la recta tangente a la gráfica de $f$ en $(c,f(c))$ es perpendicular al eje $x$.
> d) Ninguna de las anteriores.

**Solución (correcta: b).**

1. **Comprobar las hipótesis de Rolle.** El enunciado da exactamente las tres: continuidad en el cerrado $[-1,1]$, derivabilidad en el abierto $(-1,1)$ y $f(-1)=f(1)$ (U §2.5.2, p. 95).
2. **Aplicar Rolle.** Existe $c\in(-1,1)$ con $f'(c)=0$.
3. **Traducir a geometría.** La tangente en $(c,f(c))$ es $y-f(c)=f'(c)(x-c)$ (U §2.1). Su pendiente es $f'(c)=0$, así que es la recta horizontal $y=f(c)$. Una recta horizontal es **paralela al eje $x$** y **perpendicular al eje $y$**, que es lo que dice b).
4. **Por qué a) y c) son falsas.** a) y c) dicen lo mismo: paralela al eje $y$ equivale a perpendicular al eje $x$, es decir, una recta vertical $x=d$. Como $f$ es derivable en todo $(-1,1)$, en cada punto $b$ la tangente es $y=f(b)+f'(b)(x-b)$, con $f'(b)$ un **número real finito**. Esa recta es la gráfica de una función de $x$, así que nunca es vertical. Contraejemplo concreto: $f(x)=x^2$ en $[-1,1]$ cumple todas las hipótesis y ninguna de sus tangentes es vertical.
5. **d)** es falsa porque b) es verdadera.

**Receta.** Si $f$ toma el mismo valor en los extremos, es continua en el cerrado y derivable en el abierto, Rolle garantiza una tangente horizontal en algún punto interior. La pendiente de la tangente es $f'(c)$.
**Error típico.** Confundir «paralela al eje $x$» con «paralela al eje $y$». Horizontal = pendiente 0 = paralela al eje $x$ = perpendicular al eje $y$.
**Teoría:** U §2.5.2 p. 95 (Rolle); interpretación geométrica en U p. 97.

## Ejercicio 2.41 (E p. 77)

> Dada una función $f:[0,1]\to\mathbb R$ continua en $[0,1]$ y derivable en $(0,1)$ se verifica:
> a) Si $f(0)>f(1)$, existe un punto $c\in(0,1)$ tal que $f'(c)>0$.
> b) Si $f(0)>f(1)$, existe un punto $c\in(0,1)$ tal que $f'(c)<0$.
> c) Siempre existe $c\in(0,1)$ tal que $f'(c)=0$.
> d) Siempre existe $c\in(0,1)$ tal que $f'(c)=1$.

**Solución (correcta: b).**

1. **Hipótesis del TVM.** $f$ es continua en $[0,1]$ y derivable en $(0,1)$, que son exactamente las hipótesis del TVM (U §2.5.3, p. 96). Ojo: **no** sabemos que $f(0)=f(1)$, así que Rolle no se puede usar.
2. **Aplicar el TVM.** Existe $c\in(0,1)$ con $f'(c)=\dfrac{f(1)-f(0)}{1-0}=f(1)-f(0)$.
3. **Signo.** Si $f(0)>f(1)$, entonces $f(1)-f(0)<0$ y por tanto $f'(c)<0$. Esto prueba b).
4. **Un solo contraejemplo para a), c) y d):** $f(x)=-x$. Es continua y derivable, $f(0)=0>-1=f(1)$ y $f'(x)=-1$ para todo $x$. Nunca es $>0$ (falla a), nunca vale $0$ (falla c) y nunca vale $1$ (falla d).

**Receta.** Si solo sabes que $f$ es continua en $[a,b]$ y derivable en $(a,b)$, usa el TVM: el **signo** de $f(b)-f(a)$ pasa a $f'(c)$ para algún $c$.
**Error típico.** Elegir c) por aplicar Rolle de forma automática, cuando Rolle exige $f(a)=f(b)$ y aquí eso no se cumple.
**Teoría:** U §2.5.3 p. 96.

## Ejercicio 2.42 (E p. 78)

> Dada una función continua $f:[0,1]\to\mathbb R$ se verifica:
> a) Existe un punto $c\in(0,1)$ tal que $f'(c)=f(1)-f(0)$.
> b) Si $f$ es derivable en $(0,1)$, entonces existe un punto $c\in(0,1)$ tal que $f'(c)=f(1)-f(0)$.
> c) Solamente si $f$ es derivable en $(0,1)$, existe un punto $c\in(0,1)$ tal que $f'(c)=f(1)-f(0)$.
> d) Existe un punto $c\in(0,1)$ tal que $f'(c)=f(0)-f(1)$.

**Solución (correcta: b).**

1. **b) es el TVM** en $[0,1]$: $f'(c)=\frac{f(1)-f(0)}{1-0}$ (U p. 96). Verdadera.
2. **a) es falsa porque falta la derivabilidad.** Contraejemplo: $f(x)=|x-\tfrac12|$, que es continua. Quitando el valor absoluto, $f(x)=\tfrac12-x$ en $[0,\tfrac12]$ y $f(x)=x-\tfrac12$ en $(\tfrac12,1]$. Así $f'(x)=-1$ en $(0,\tfrac12)$, $f'(x)=1$ en $(\tfrac12,1)$, y en $\tfrac12$ no hay derivada porque las laterales valen $-1\ne1$ (U Def. 2.3 p. 81). Sin embargo $f(1)-f(0)=\tfrac12-\tfrac12=0$, y $f'$ no vale $0$ en ningún punto donde existe.
3. **c) es falsa. «Solamente si» significa que la tesis obligaría a que $f$ fuera derivable.** Para refutarlo basta una función **no** derivable en algún punto de $(0,1)$ para la que sí exista ese $c$. Tomamos $f(x)=|\operatorname{sen}(2\pi x)|$:
   - Es continua (composición de continuas, U Prop. 1.14 p. 51).
   - No es derivable en $\tfrac12$. Cerca de $\tfrac12$ por la izquierda $\operatorname{sen}(2\pi x)>0$, así que $f=\operatorname{sen}(2\pi x)$ y $f'(\tfrac12^-)=2\pi\cos\pi=-2\pi$. Por la derecha $\operatorname{sen}(2\pi x)<0$, así que $f=-\operatorname{sen}(2\pi x)$ y $f'(\tfrac12^+)=-2\pi\cos\pi=2\pi$. Las laterales son distintas (comprobado con sympy).
   - Aun así, en $c=\tfrac14$, donde $f=\operatorname{sen}(2\pi x)$ en un entorno, $f'(\tfrac14)=2\pi\cos\tfrac\pi2=0=f(1)-f(0)$.
   Moraleja: el TVM da una condición **suficiente**, no necesaria.
4. **d) es falsa.** Con $f(x)=x$ se tiene $f'\equiv1$, pero $f(0)-f(1)=-1$.

**Receta.** Ante un enunciado «existe $c$ con $f'(c)=\dots$»: (i) comprueba si se cumplen **todas** las hipótesis del TVM o de Rolle; (ii) si falta alguna, busca un contraejemplo con un «pico», como $|x-x_0|$; (iii) si la opción dice «solamente si», busca una función que incumpla la hipótesis y aun así cumpla la tesis.
**Error típico.** Creer que si falla una hipótesis, falla la tesis (es confundir condición suficiente con necesaria). U lo advierte expresamente con $x^3$ en $[-1,1]$ (U p. 96).
**Teoría:** U §2.5.3 p. 96; contraejemplos de Rolle en U pp. 95-96; derivadas laterales en U p. 81.

## Ejercicio 2.40 (E p. 77)

> Demuestra que si un polinomio de grado mayor o igual que tres tiene tres ceros, existen al menos dos puntos en los que su recta tangente es horizontal.

**Solución.**

1. **Precisar el enunciado.** «Tres ceros» hay que entenderlo como **tres ceros distintos** $a<b<c$ con $f(a)=f(b)=f(c)=0$. Si se admitieran raíces repetidas, $f(x)=x^3$ tendría el cero $0$ «tres veces» y solo tiene tangente horizontal en $x=0$, así que la tesis fallaría. E lo supone sin decirlo al escribir $a<b<c$.
2. **Regularidad.** Un polinomio es continuo y derivable en todo $\mathbb R$ (reglas de derivación, U p. 79). En particular lo es en cualquier $[p,q]$ y en cualquier $(p,q)$.
3. **Rolle en $[a,b]$.** Como $f(a)=f(b)=0$, existe $s\in(a,b)$ con $f'(s)=0$ (U p. 95).
4. **Rolle en $[b,c]$.** Como $f(b)=f(c)=0$, existe $t\in(b,c)$ con $f'(t)=0$.
5. **Son distintos.** Se cumple $s<b<t$, porque los intervalos $(a,b)$ y $(b,c)$ no se solapan. Luego $s\ne t$ (el PDF dice «$s\ne t$»; el `.txt` pierde la barra).
6. **Conclusión.** En $s$ y en $t$ la tangente tiene pendiente $0$: hay dos tangentes horizontales.

**Observación.** La hipótesis «grado $\ge3$» no se usa: un polinomio no nulo con tres raíces distintas tiene automáticamente grado $\ge3$. En general, si $f$ tiene $n$ ceros distintos, $f'$ tiene al menos $n-1$ ceros.

**Receta.** Entre dos ceros de $f$ siempre hay un cero de $f'$: aplica Rolle en cada hueco entre ceros consecutivos.
**Error típico.** Aplicar Rolle una sola vez en $[a,c]$, que solo da **un** punto.
**Teoría:** U §2.5.2 p. 95.

## Ejercicio 2.49 (E pp. 82-83)

> Señala la afirmación correcta relativa a la función
> $$f(x)=\begin{cases}|\operatorname{sen}(x-1)| & \text{si } x\ge1,\ x-2 & \text{si } x<1.\end{cases}$$
> a) $f$ es derivable en 1. b) $\lim_{x\to+\infty}f(x)=0$. c) $f$ verifica las hipótesis del teorema de Rolle en $[1+2\pi,1+3\pi]$. d) $f$ es derivable en $\mathbb R\setminus\{1\}$.

**Solución (correcta: c).**

1. **a) Continuidad en 1.** $\lim_{x\to1^-}f(x)=\lim_{x\to1^-}(x-2)=-1$, mientras que $f(1)=|\operatorname{sen}0|=0$. El límite lateral no coincide con el valor, así que $f$ es discontinua en 1 (U Def. 1.20 p. 51). Como derivable implica continua, $f$ **no es derivable en 1**. a) es falsa.
2. **b) El límite en $+\infty$ no existe.** Si existiera $\lim_{x\to+\infty}f(x)=l$, entonces para **toda** sucesión $x_n\to+\infty$ se tendría $f(x_n)\to l$. Esto sale directamente de la definición de límite en el infinito: dado $\varepsilon>0$ hay un $M$ con $|f(x)-l|<\varepsilon$ si $x>M$, y $x_n>M$ a partir de cierto índice. Pero:
   - $a_n=1+\tfrac\pi2+2n\pi\to+\infty$ y $f(a_n)=|\operatorname{sen}(\tfrac\pi2+2n\pi)|=1\to1$;
   - $b_n=1+2n\pi\to+\infty$ y $f(b_n)=|\operatorname{sen}(2n\pi)|=0\to0$.
   Salen dos límites distintos, luego no hay límite. b) es falsa.
3. **c) Rolle en $[1+2\pi,1+3\pi]$.**
   - Ahí $x\ge1$, así que $f(x)=|\operatorname{sen}(x-1)|$, y además $x-1\in[2\pi,3\pi]$, donde el seno es $\ge0$ (es el intervalo $[0,\pi]$ desplazado un periodo). Por tanto $f(x)=\operatorname{sen}(x-1)$ en **todo** el intervalo cerrado.
   - $\operatorname{sen}(x-1)$ es continua y derivable en $\mathbb R$. Como $f$ coincide con ella en el cerrado, $f$ es continua en $[1+2\pi,1+3\pi]$. Y en cada punto del abierto $f$ coincide con ella en un entorno, así que es derivable en $(1+2\pi,1+3\pi)$.
   - $f(1+2\pi)=\operatorname{sen}2\pi=0=\operatorname{sen}3\pi=f(1+3\pi)$.
   Se cumplen las tres hipótesis. c) es verdadera.
4. **d) Falla en $1+3\pi$ (y en todos los $1+k\pi$ con $k\ge1$).** Sea $p=1+3\pi$. Entonces $f(p)=|\operatorname{sen}3\pi|=0$ y $f(p+h)=|\operatorname{sen}(3\pi+h)|=|-\operatorname{sen}h|=|\operatorname{sen}h|$. Por la definición de derivada lateral (U Def. 2.3 p. 81) y $\lim_{h\to0}\frac{\operatorname{sen}h}{h}=1$ (U Ej. 2.8 p. 82):
   $$f'(p^+)=\lim_{h\to0^+}\frac{|\operatorname{sen}h|}{h}=1,\qquad f'(p^-)=\lim_{h\to0^-}\frac{|\operatorname{sen}h|}{h}=-1 .$$
   Las derivadas laterales no coinciden, así que $f$ no es derivable en $p\ne1$. d) es falsa.

**Nota sobre el método de E en d).** E calcula los límites de la derivada, $\lim_{x\to p^\pm}f'(x)$, en vez de las derivadas laterales. El resultado es correcto, pero el paso «el límite de $f'$ es la derivada lateral» necesita un resultado adicional (una consecuencia del TVM, válida si $f$ es continua en $p$) que U no enuncia. Con la definición, como en el paso 4, no hace falta.

**Receta.** Para funciones a trozos o con $|\cdot|$: (1) estudia la continuidad en los puntos donde cambia la fórmula; (2) calcula las derivadas laterales por definición; (3) para Rolle, quita el valor absoluto estudiando el **signo** de lo que hay dentro en el intervalo; (4) para ver que un límite en $\infty$ no existe, busca dos sucesiones con límites distintos.
**Error típico.** Pensar que $|\operatorname{sen}(x-1)|$ solo da problemas en $x=1$, cuando el valor absoluto crea un pico en **cada** cero del seno.
**Teoría:** U Def. 1.20 p. 51; Def. 2.3 p. 81; Ej. 2.8 p. 82; Rolle p. 95.

### Ejemplos propios — Bloque A

**Ejemplo A1 (propio, fácil).** Comprueba que $f(x)=x^2-4x+1$ cumple Rolle en $[0,4]$ y halla $c$.
*Solución.* Es un polinomio, luego continuo y derivable. $f(0)=1=f(4)$. $f'(x)=2x-4=0\iff x=2\in(0,4)$, así que $c=2$ (sympy: `solve(2x-4)=[2]`).

**Ejemplo A2 (propio, medio).** Demuestra que $|\operatorname{sen}a-\operatorname{sen}b|\le|a-b|$ para todos $a,b\in\mathbb R$.
*Solución.* Si $a=b$ no hay nada que probar. Si $a<b$, el TVM en $[a,b]$ aplicado a $\operatorname{sen}$ da un $c\in(a,b)$ con $\operatorname{sen}b-\operatorname{sen}a=\cos c\,(b-a)$. Tomando valor absoluto y usando $|\cos c|\le1$ queda $|\operatorname{sen}b-\operatorname{sen}a|\le|b-a|$. (Receta: el TVM convierte una cota de $f'$ en una cota de los incrementos de $f$.)

**Ejemplo A3 (propio, difícil).** Prueba que $x^3+3x+1=0$ tiene **exactamente una** solución real.
*Solución.* *Existencia* (Bolzano, U p. 52): $p(x)=x^3+3x+1$ es continuo y $p(-1)=-3<0<1=p(0)$, luego hay una raíz en $(-1,0)$. *Unicidad* (Rolle, por reducción al absurdo): si hubiera dos raíces $r_1<r_2$, Rolle en $[r_1,r_2]$ daría un $c$ con $p'(c)=0$. Pero $p'(x)=3x^2+3\ge3>0$, contradicción. (sympy: única raíz real $\approx-0.3222$.) **Receta:** Bolzano para que exista, Rolle (o la monotonía) para que sea única.

---

# BLOQUE B — Monotonía

## Ejercicio 2.43 (E p. 79)

> Razona la veracidad o falsedad de la siguiente afirmación: Si $f$ y $g$ son funciones estrictamente crecientes en $I$, entonces $f+g$ es estrictamente creciente en $I$.

**Solución (verdadera).**

1. **Qué hay que probar** (U Def. 2.5 p. 98): para todos $a,b\in I$ con $a<b$, $(f+g)(a)<(f+g)(b)$.
2. **Tomamos $a<b$ en $I$.** Como $f$ es estrictamente creciente, $f(a)<f(b)$. Sumando $g(a)$ a los dos lados (sumar el mismo número conserva la desigualdad): $f(a)+g(a)<f(b)+g(a)$.
3. Como $g$ es estrictamente creciente, $g(a)<g(b)$. Sumando $f(b)$: $f(b)+g(a)<f(b)+g(b)$.
4. **Encadenamos:** $(f+g)(a)<f(b)+g(a)<(f+g)(b)$. La afirmación es verdadera.
5. **Por qué no se puede usar la derivada.** El enunciado no dice que $f$ y $g$ sean derivables. Y aunque lo fueran, «estrictamente creciente» no implica $f'>0$ (ejemplo: $x^3$ en $0$, U Ej. 2.22 p. 99). Hay que ir a la definición.

**Receta.** Para la monotonía de una combinación de funciones sin datos de derivabilidad, trabaja con la **definición**: toma $a<b$ y encadena desigualdades.
**Error típico.** Generalizar al producto: $f(x)=g(x)=x$ son estrictamente crecientes en $\mathbb R$, pero $fg=x^2$ no es creciente ($(-1)^2>0^2$). Con la diferencia tampoco funciona: $x-x=0$.
**Teoría:** U Def. 2.5 p. 98.

## Ejercicio 2.44 (E pp. 79-80)

> Razona la veracidad o falsedad de la siguiente afirmación: Si $f:\mathbb R\to\mathbb R$ es una función continua y decreciente en $[-\pi,0]$ y en $[\pi,2\pi]$, entonces $f(a)\ge f(b)$ para todo $a\in[-\pi,0]$ y $b\in[\pi,2\pi]$.

**Solución (falsa).**

1. **Qué da la hipótesis.** Por ser decreciente en $[-\pi,0]$: para $a\in[-\pi,0]$, $a\le0\Rightarrow f(a)\ge f(0)$. Por ser decreciente en $[\pi,2\pi]$: para $b\in[\pi,2\pi]$, $\pi\le b\Rightarrow f(\pi)\ge f(b)$.
2. **El eslabón que falta.** Para concluir $f(a)\ge f(b)$ haría falta $f(0)\ge f(\pi)$, pero **nada** dice cómo se comporta $f$ en $(0,\pi)$, y puede subir. Que $f$ decrezca en dos trozos separados no dice nada de lo que pasa entre ellos.
3. **Contraejemplo:** $f(x)=-\cos x$. Es continua y $f'(x)=\operatorname{sen}x\le0$ en $[-\pi,0]$ y en $[\pi,2\pi]$, así que es decreciente en ambos (U Prop. 2.4 p. 98). Pero con $a=0$, $b=\pi$: $f(0)=-1<1=f(\pi)$. (E usa $a=-\tfrac\pi2$, $b=\tfrac{7\pi}6$, con $f(-\tfrac\pi2)=0<\tfrac{\sqrt3}2=f(\tfrac{7\pi}6)$; también vale, comprobado con sympy.)

**Receta.** Para refutar un «para todo» basta **un** contraejemplo. Constrúyelo haciendo que la función suba en el hueco que el enunciado no controla.
**Error típico.** Pensar que «decreciente en $A$ y en $B$» equivale a «decreciente en $A\cup B$». Ejemplo clásico: $1/x$ es decreciente en $(-\infty,0)$ y en $(0,\infty)$, pero $-1<1$ y también $1/(-1)<1/1$.
**Teoría:** U Def. 2.5 y Prop. 2.4, p. 98.

## Ejercicio 2.47 (E pp. 81-82)

> Sea $f:\mathbb R\to\mathbb R$ una función con derivada $f'(x)=\ln(x^2+2)$. Señala la opción correcta:
> a) $f$ es creciente pero no estrictamente creciente en $\mathbb R$. b) $f$ es decreciente en $\mathbb R$. c) $f$ es estrictamente creciente en $\mathbb R$. d) Ninguna de las anteriores.

**Solución (correcta: c).**

1. **Signo de $f'$.** Para todo $x$, $x^2\ge0$, luego $x^2+2\ge2>1$. Como $\ln$ es estrictamente creciente y $\ln1=0$: $\ln(x^2+2)\ge\ln2\approx0.693>0$.
2. **Prop. 2.4 (U p. 98)** con $I=\mathbb R$: como $f'>0$ en todo $\mathbb R$, $f$ es estrictamente creciente. c) es verdadera.
3. **Las demás.** a) dice «no estrictamente», lo que contradice c). b) es falsa porque $f(0)<f(1)$. d) es falsa porque c) es verdadera.

**Receta.** Si $f'$ tiene signo constante, basta acotarla por abajo con una constante $>0$ (o por arriba con una constante $<0$).
**Error típico.** Pensar que el $\ln$ «puede ser negativo» sin mirar el argumento: solo es negativo si el argumento está en $(0,1)$.
**Teoría:** U Prop. 2.4 p. 98.

## Ejercicio 2.46 (E p. 81)

> Sea $f:\mathbb R\to\mathbb R$ una función tal que su derivada es $f'(x)=\operatorname{sen}(\pi x)e^{2x^2-x}$. Señala la opción correcta:
> a) $f$ es creciente en $\mathbb R$. b) $f$ es decreciente en $\mathbb R$. c) $f$ es estrictamente creciente en $\mathbb R$. d) Ninguna de las anteriores.

**Solución (correcta: d).**

1. **Signo de $f'$.** $e^{2x^2-x}>0$ siempre, así que $f'(x)$ tiene el signo de $\operatorname{sen}(\pi x)$: positivo en $(0,1)$, negativo en $(1,2)$, y así sucesivamente.
2. **No es decreciente.** $f$ es derivable en $\mathbb R$. El TVM en $[0,1]$ da $f(1)-f(0)=f'(c)$ con $c\in(0,1)$, y ahí $\operatorname{sen}(\pi c)>0$. Luego $f(0)<f(1)$, y b) falla.
3. **No es creciente (ni estrictamente creciente).** El TVM en $[1,2]$ da $f(2)-f(1)=f'(d)$ con $d\in(1,2)$, y ahí $\operatorname{sen}(\pi d)<0$. Luego $f(1)>f(2)$, y fallan a) y c).
4. Por tanto la respuesta es d).

**Por qué este cuidado.** E razona «$f'$ cambia de signo, luego $f$ es a ratos creciente y a ratos decreciente». La idea es correcta, pero U solo da la implicación «signo de $f'$ $\Rightarrow$ monotonía» (Prop. 2.4), no la recíproca. Para descartar la monotonía en $\mathbb R$ hay que dar dos puntos que incumplan la definición, y el TVM los proporciona.

**Receta.** Para probar que $f$ **no** es creciente en $I$, encuentra $a<b$ en $I$ con $f(a)>f(b)$. Si solo conoces $f'$, obtén el signo de $f(b)-f(a)$ con el TVM en un intervalo donde $f'<0$.
**Error típico.** Olvidar que $e^{(\dots)}>0$ y hacer un estudio de signos innecesario del factor exponencial.
**Teoría:** U TVM p. 96; Def. 2.5 y Prop. 2.4 p. 98.

## Ejercicio 2.48 (E p. 82)

> Calcula los intervalos de crecimiento y decrecimiento de $f:\mathbb R\to\mathbb R$ tal que $f(x)=e^{2x^2-x}$. A continuación discute si la siguiente afirmación es correcta: $f$ es decreciente en $J=(-\infty,-\tfrac18)$.

**Solución (la afirmación es correcta).**

1. **Derivamos** con la regla de la cadena (U pp. 79-80): $f'(x)=e^{2x^2-x}(4x-1)$ (sympy, con `factor`: $(4x-1)e^{2x^2-x}$).
2. **Signo.** $e^{2x^2-x}>0$, así que $f'$ tiene el signo de $4x-1$: $f'<0$ si $x<\tfrac14$, $f'>0$ si $x>\tfrac14$ y $f'(\tfrac14)=0$.
3. **Prop. 2.4 (U p. 98):** $f$ es estrictamente decreciente en $I=(-\infty,\tfrac14)$ y estrictamente creciente en $(\tfrac14,+\infty)$. (En $x=\tfrac14$ hay un mínimo, U Prop. 3.5 p. 130.)
4. **La afirmación.** $J=(-\infty,-\tfrac18)\subset I$. Estrictamente decreciente implica decreciente (U p. 98), y si $f$ es decreciente en $I$, la condición «$a<b\Rightarrow f(a)\ge f(b)$» se cumple en particular para $a,b\in J$. La afirmación es correcta.

**Receta.** Para estudiar el crecimiento: (1) deriva y **factoriza**; (2) quita los factores de signo fijo (exponenciales, cuadrado más una constante positiva); (3) estudia el signo de lo que queda; (4) aplica la Prop. 2.4 en cada intervalo.
**Error típico.** Pensar que la afirmación es falsa «porque el intervalo de decrecimiento es $(-\infty,\tfrac14)$, no $(-\infty,-\tfrac18)$». La monotonía **se hereda a los subintervalos**.
**Teoría:** U Prop. 2.4 p. 98; ejemplo muy parecido en U Ej. 2.23 pp. 99-100.

### Ejemplos propios — Bloque B

**Ejemplo B1 (propio, fácil).** Intervalos de monotonía de $f(x)=x^3-3x$.
*Solución.* $f'(x)=3x^2-3=3(x-1)(x+1)$. Su signo es $+$ en $(-\infty,-1)$, $-$ en $(-1,1)$ y $+$ en $(1,\infty)$. Luego $f$ es estrictamente creciente en $(-\infty,-1)$ y en $(1,\infty)$, y estrictamente decreciente en $(-1,1)$. Tiene un máximo relativo $f(-1)=2$ y un mínimo relativo $f(1)=-2$ (U Prop. 3.5 p. 130). (Verificado con sympy.)

**Ejemplo B2 (propio, medio).** Demuestra que $\ln(1+x)<x$ para todo $x>0$.
*Solución.* Sea $h(x)=\ln(1+x)-x$ en $[0,\infty)$. Entonces $h(0)=0$ y $h'(x)=\frac1{1+x}-1=\frac{-x}{1+x}<0$ si $x>0$. Ojo: $h'(0)=0$, así que la Prop. 2.4 no se aplica tal cual en $[0,\infty)$. Usamos el TVM: para $x>0$, $h(x)-h(0)=h'(c)\,x$ con $c\in(0,x)$ y $h'(c)<0$, luego $h(x)<h(0)=0$. **Receta:** para probar $F(x)<G(x)$, estudia el signo de $h=F-G$ a partir de su valor en un extremo y del signo de $h'$.

**Ejemplo B3 (propio, difícil).** ¿Es $f(x)=x+\operatorname{sen}x$ estrictamente creciente en $\mathbb R$, aunque $f'$ se anule?
*Solución.* $f'(x)=1+\cos x\ge0$, y $f'(x)=0\iff x=(2k+1)\pi$, que son puntos aislados. Sean $a<b$. En $[a,b]$ solo hay un número finito de esos ceros, $z_1<\dots<z_m$; llamamos $z_0=a$ y $z_{m+1}=b$. En cada $(z_i,z_{i+1})$ se tiene $f'>0$, y el TVM en $[z_i,z_{i+1}]$ da $f(z_{i+1})-f(z_i)=f'(c_i)(z_{i+1}-z_i)>0$. Encadenando, $f(a)<f(b)$. Por tanto sí es estrictamente creciente. Es la misma idea que U Ej. 2.22 ($x^3$), p. 99: **que $f'$ se anule en puntos aislados no rompe la monotonía estricta**.

---

# BLOQUE C — Funciones hiperbólicas

## Ejercicio 2.45 (E pp. 80-81)

> Sean el coseno y el seno hiperbólico las funciones definidas por
> $$\cosh x=\frac{e^x+e^{-x}}2\quad\text{y}\quad\operatorname{senh}x=\frac{e^x-e^{-x}}2 .$$
> Señala la opción correcta:
> a) $(\cosh x)'=-\operatorname{senh}x$. b) $\operatorname{senh}x+\cosh x$ es constante. c) $(\operatorname{senh}x)'=-\cosh x$. d) $\cosh^2x-\operatorname{senh}^2x$ es constante.

**Solución (correcta: d).**

1. **Derivamos con la tabla** (U p. 79: $(e^{u})'=e^{u}u'$, luego $(e^{-x})'=-e^{-x}$):
   $(\cosh x)'=\frac{e^x-e^{-x}}2=\operatorname{senh}x$ y $(\operatorname{senh}x)'=\frac{e^x+e^{-x}}2=\cosh x$. **No hay signo menos**, al contrario que con $\cos$. a) y c) son falsas.
2. **b).** $\cosh x+\operatorname{senh}x=\frac{2e^x}2=e^x$, que no es constante ($e^0=1\ne e=e^1$). Es falsa.
3. **d), con la derivada (como hace E).** Sea $g(x)=\cosh^2x-\operatorname{senh}^2x$. Por la regla de la cadena, $g'(x)=2\cosh x\operatorname{senh}x-2\operatorname{senh}x\cosh x=0$ para todo $x$. Por el **Teorema 2.4 de U (p. 97)**, aplicado en cualquier intervalo $(-R,R)$ y por tanto en todo $\mathbb R$, $g$ es constante. Su valor es $g(0)=1^2-0^2=1$.
4. **d), con álgebra (comprobación).** $\frac{(e^x+e^{-x})^2-(e^x-e^{-x})^2}4=\frac{(e^{2x}+2+e^{-2x})-(e^{2x}-2+e^{-2x})}4=\frac44=1$. (sympy: `simplify` da $1$.)

**Resultado a memorizar:** $\cosh^2x-\operatorname{senh}^2x=1$. Es el análogo de $\cos^2+\operatorname{sen}^2=1$: el punto $(\cosh t,\operatorname{senh}t)$ recorre la hipérbola $X^2-Y^2=1$, y de ahí viene el nombre.

**Receta.** Para probar que una expresión es constante en un intervalo: derívala, comprueba que la derivada es $0$ (Teorema 2.4) y evalúala en un punto cómodo.
**Error típico.** Copiar los signos de las trigonométricas: $(\cos)'=-\operatorname{sen}$, pero $(\cosh)'=+\operatorname{senh}$.
**Teoría:** U Teorema 2.4 p. 97; tabla de derivadas en U pp. 79-80. **U no define las funciones hiperbólicas** (solo aparecen en E): consultar S §3.11 p. 257 o L §5.8 p. 383.

### Ejemplos propios — Bloque C

**Ejemplo C1 (propio, fácil).** Con $\tanh x=\frac{\operatorname{senh}x}{\cosh x}$, prueba que $(\tanh x)'=\frac1{\cosh^2x}=1-\tanh^2x$.
*Solución.* Por la regla del cociente (U Prop. 2.1 p. 79), $(\tanh x)'=\frac{\cosh x\cosh x-\operatorname{senh}x\operatorname{senh}x}{\cosh^2x}=\frac{1}{\cosh^2x}$, usando 2.45 d). Dividiendo $\cosh^2-\operatorname{senh}^2=1$ entre $\cosh^2$ se obtiene $\frac1{\cosh^2x}=1-\tanh^2x$. (Verificado con sympy.)

**Ejemplo C2 (propio, medio).** Prueba que $\operatorname{senh}$ es estrictamente creciente en $\mathbb R$ y que $\cosh x\ge1$, con igualdad solo en $x=0$.
*Solución.* $(\operatorname{senh})'=\cosh x=\frac{e^x+e^{-x}}2>0$, luego $\operatorname{senh}$ es estrictamente creciente (Prop. 2.4). Además $\cosh x-1=\frac{(e^{x/2}-e^{-x/2})^2}2\ge0$, y vale $0$ solo si $e^{x/2}=e^{-x/2}$, es decir, si $x=0$ (identidad verificada con sympy). Otra forma, con la monotonía: $(\cosh)'=\operatorname{senh}x$ es $<0$ si $x<0$ (porque $e^x<e^{-x}$) y $>0$ si $x>0$, así que $\cosh$ tiene un mínimo absoluto en $0$.

---

# BLOQUE D — Identificar gráficas

## Ejercicio 2.50 (E pp. 84-85)

> Deduce cuál de las siguientes figuras coincide con la representación gráfica de $f(x)=\dfrac{x^3+1}{x}$: [cuatro figuras a), b), c), d)].

**Descripción de las figuras (leída del PDF, p. 84).** En las cuatro hay una asíntota vertical $x=0$: la rama derecha sube a $+\infty$ al acercarse a $0^+$ y la rama izquierda baja a $-\infty$ en $0^-$.
- **a)** La rama derecha tiene forma de «U»: baja desde $+\infty$, tiene un mínimo y vuelve a subir. La rama izquierda viene de arriba a la izquierda, baja, corta el eje $x$ y cae a $-\infty$ junto al eje $y$.
- **b)** La rama derecha es como en a). La rama izquierda es un arco hacia abajo: sube desde abajo a la izquierda, tiene un máximo por debajo del eje y cae a $-\infty$ en $0^-$. Es decir, tiende a $-\infty$ cuando $x\to-\infty$.
- **c)** La rama izquierda es como en a). La rama derecha es decreciente y se aplana hacia una asíntota horizontal ($y$ tiende a una constante cuando $x\to+\infty$).
- **d)** La rama derecha es como en a). La rama izquierda se aplana hacia una asíntota horizontal cuando $x\to-\infty$ y cae a $-\infty$ en $0^-$.

**Solución (correcta: a).**

1. **Dominio y una forma más cómoda.** $D=\mathbb R\setminus\{0\}$ y $f(x)=x^2+\dfrac1x$.
2. **Asíntota vertical** (U p. 49). $\lim_{x\to0^+}(x^2+\tfrac1x)=+\infty$ y $\lim_{x\to0^-}=-\infty$. Esto coincide con las cuatro figuras, así que no sirve para distinguir.
3. **Comportamiento en $\pm\infty$.** $x^2\to+\infty$ y $\tfrac1x\to0$, así que $\lim_{x\to+\infty}f=\lim_{x\to-\infty}f=+\infty$. No hace falta L'Hôpital, que es lo que usa E (también es válido, U p. 82). Consecuencias:
   - no hay asíntotas horizontales, lo que descarta **c)** (tiene una a la derecha) y **d)** (tiene una a la izquierda);
   - en $-\infty$ la función tiende a $+\infty$, lo que descarta **b)** (su rama izquierda baja a $-\infty$).
4. **Confirmación con la monotonía**, para no depender solo de ir descartando. $f'(x)=2x-\frac1{x^2}=\frac{2x^3-1}{x^2}$. Como $x^2>0$, $f'$ tiene el signo de $2x^3-1$, y $2x^3-1>0\iff x>x_0:=2^{-1/3}=\frac1{\sqrt[3]2}\approx0.794$. Por la Prop. 2.4 (U p. 98), $f$ es estrictamente decreciente en $(-\infty,0)$ y en $(0,x_0)$, y estrictamente creciente en $(x_0,\infty)$. Hay un mínimo relativo en $x_0$ con $f(x_0)=\tfrac32\sqrt[3]2\approx1.89$ (U Prop. 3.5 p. 130).
5. **Otros detalles que encajan con a).** Corte con el eje: $x^3+1=0\iff x=-1$, así que la rama izquierda corta el eje $x$ en $(-1,0)$. Además $f''(x)=2+\frac2{x^3}$, que es $>0$ en $(0,\infty)$ (convexa, forma de U). En la rama izquierda $f''=0$ en $x=-1$: es convexa en $(-\infty,-1)$ y cóncava en $(-1,0)$, con inflexión en $(-1,0)$ (U Prop. 3.10-3.12, pp. 136-137). En la figura a), la rama izquierda cambia de curvatura justo al cruzar el eje.

**Receta (identificar gráficas).** Ve de lo más barato a lo más caro: (1) dominio y asíntotas verticales; (2) límites en $\pm\infty$ (asíntotas horizontales u oblicuas); (3) ceros y signo; (4) signo de $f'$ (monotonía y extremos); (5) si aún dudas, $f''$ (concavidad). Descarta una figura en cuanto un dato la contradiga.
**Error típico.** Quedarse en la asíntota vertical (que aquí no distingue nada) o aplicar L'Hôpital sin necesidad. Dividir antes ($x^2+\tfrac1x$) es más rápido y más seguro.
**Teoría:** U §1.4 pp. 48-49 (asíntotas); Prop. 2.4 p. 98; Prop. 3.5 p. 130; §3.5 pp. 136-137.

## Ejercicio 2.51 (E pp. 85-86)

> Deduce cuál de las siguientes figuras coincide con la representación gráfica de $f(x)=\operatorname{sen}x+\tfrac12\operatorname{sen}2x$ en el intervalo $[0,2\pi]$: [cuatro figuras a), b), c), d)].

**Descripción de las figuras (leída del PDF, p. 85).** Todas empiezan en el eje $x$ en $0$, acaban en él en $2\pi$ y pasan por $(\pi,0)$.
- **a)** Sube desde $0$ con pendiente clara, tiene un máximo antes de $\pi/2$, baja y **llega a $\pi$ con tangente horizontal** (un tramo plano). Sigue bajando hasta un mínimo después de $3\pi/2$ y vuelve a $0$ con pendiente clara. Tangentes horizontales en el interior: **3**.
- **b)** Sale de $0$ con **tangente horizontal**, tiene un máximo, cruza el eje en $\pi$ con mucha pendiente, tiene un mínimo y llega a $2\pi$ con tangente horizontal. Tangentes horizontales en el interior: **2**.
- **c)** Un máximo alto, un mínimo local positivo, un máximo pequeño y un mínimo profundo. En el interior: **4**.
- **d)** Arriba, dos máximos con un mínimo entre ellos; abajo, dos mínimos con un máximo entre ellos. En el interior: **6**.
(E da los mismos recuentos: «3, 2, 4 y 6».)

**Solución (correcta: a).**

1. **Derivada.** $f'(x)=\cos x+\tfrac12\cdot2\cos2x=\cos x+\cos2x$ (regla de la cadena, U p. 79).
2. **Pendiente en los extremos.** $f'(0)=f'(2\pi)=1+1=2\ne0$ (en el `.txt` aparece «$=0$» porque se pierde la barra de $\ne$). La gráfica no puede empezar ni terminar con tangente horizontal, lo que descarta **b)**.
3. **Puntos con tangente horizontal en $(0,2\pi)$.** Usando $\cos2x=2\cos^2x-1$:
   $$f'(x)=2\cos^2x+\cos x-1=(2\cos x-1)(\cos x+1).$$
   $f'(x)=0\iff\cos x=\tfrac12$ o $\cos x=-1\iff x\in\{\tfrac\pi3,\ \pi,\ \tfrac{5\pi}3\}$ (sympy, con `solveset`, da exactamente estos tres). Hay **exactamente 3**, lo que descarta **c)** (4) y **d)** (6). Solo queda **a)**.
4. **Confirmación con la monotonía.** $\cos x+1\ge0$, y solo vale $0$ en $\pi$. Por tanto, salvo en $\pi$, $f'$ tiene el signo de $2\cos x-1$: $f'>0$ en $(0,\tfrac\pi3)$, $f'<0$ en $(\tfrac\pi3,\pi)$ y en $(\pi,\tfrac{5\pi}3)$, y $f'>0$ en $(\tfrac{5\pi}3,2\pi)$. Valores de prueba con sympy: $f'(0.5)\approx1.42$, $f'(2)\approx-1.07$, $f'(3.5)\approx-0.18$, $f'(5)\approx-0.56$, $f'(6)\approx1.80$.
   - Hay un máximo relativo en $\tfrac\pi3$, con $f(\tfrac\pi3)=\tfrac{3\sqrt3}4\approx1.30$, y un mínimo relativo en $\tfrac{5\pi}3$, con valor $-\tfrac{3\sqrt3}4$ (U Prop. 3.5 p. 130).
   - En $\pi$, $f'$ **no cambia de signo** (es negativa a ambos lados): $f$ sigue decreciendo y no hay extremo. Es un **punto de silla** (U Def. 3.7 p. 131). Con las derivadas sucesivas, $f''(\pi)=0$ y $f'''(\pi)=-3\ne0$: la primera derivada no nula es de orden impar (U Prop. 3.8 p. 132 y Prop. 3.12 p. 137), así que hay una inflexión con tangente horizontal. Es el tramo plano central de a).
5. **Otras comprobaciones visuales.** $f(x)=\operatorname{sen}x(1+\cos x)$, con ceros en $0,\pi,2\pi$; $f\ge0$ en $[0,\pi]$ y $f\le0$ en $[\pi,2\pi]$. Además $f(2\pi-x)=-f(x)$, así que la gráfica es simétrica respecto del punto $(\pi,0)$. Todo encaja con a).

**Sobre el razonamiento de E.** E resuelve $f'=0$ (obtiene $\tfrac\pi3,\pi,\tfrac{5\pi}3$), pero en lugar de usarlo «anima al lector» y concluye comprobando solo que la tangente es horizontal en $\pi$ y que «solo una figura la tiene». Es correcto por eliminación, pero supone que una de las cuatro figuras es la buena. El recuento de puntos críticos del paso 3 ya basta y es más sólido.

**Receta.** Con funciones trigonométricas: escribe $f'$ en función de una sola razón (aquí $\cos2x=2\cos^2x-1$), factorízala como un polinomio en $\cos x$, cuenta sus ceros en el intervalo y estudia si cambia de signo en cada uno.
**Error típico.** Creer que $f'(c)=0$ implica un máximo o un mínimo: en $\pi$ no hay ninguno (U Def. 3.7 p. 131).
**Teoría:** U Prop. 2.4 p. 98; Def. 3.5 p. 126; Prop. 3.5 p. 130; Def. 3.7 y Prop. 3.7 p. 131; Prop. 3.8 p. 132; Prop. 3.12 p. 137.

### Ejemplos propios — Bloque D

**Ejemplo D1 (propio, fácil).** Esboza $f(x)=x+\dfrac1x$.
*Solución.* Dominio $\mathbb R\setminus\{0\}$; la función es impar. Asíntota vertical $x=0$ ($\pm\infty$ en $0^\pm$). Asíntota oblicua $y=x$, porque $f(x)-x=\tfrac1x\to0$ (U p. 49). $f'(x)=\frac{(x-1)(x+1)}{x^2}$: crece en $(-\infty,-1)$ y en $(1,\infty)$, decrece en $(-1,0)$ y en $(0,1)$. Máximo relativo $f(-1)=-2$ y mínimo relativo $f(1)=2$. (Verificado con sympy.)

**Ejemplo D2 (propio, medio).** Esboza $f(x)=\dfrac{x^2}{x-1}$.
*Solución.* Asíntota vertical $x=1$: $\lim_{1^+}=+\infty$ y $\lim_{1^-}=-\infty$. Asíntota oblicua: $m=\lim f(x)/x=1$ y $b=\lim(f(x)-x)=\lim\frac{x}{x-1}=1$. De hecho $f(x)=x+1+\frac1{x-1}$, así que la asíntota es $y=x+1$. $f'(x)=\frac{x(x-2)}{(x-1)^2}$: crece en $(-\infty,0)$ y en $(2,\infty)$, decrece en $(0,1)$ y en $(1,2)$. Máximo relativo $f(0)=0$ y mínimo relativo $f(2)=4$. (Verificado con sympy.)

**Ejemplo D3 (propio, difícil).** ¿Cuántos extremos y puntos de inflexión tiene $f(x)=xe^{-x^2}$, y qué asíntotas?
*Solución.* Es impar. $\lim_{x\to\pm\infty}xe^{-x^2}=0$ porque la exponencial domina (L'Hôpital en $x/e^{x^2}$, U p. 82), así que $y=0$ es asíntota horizontal por ambos lados. $f'(x)=(1-2x^2)e^{-x^2}$: crece en $(-\tfrac1{\sqrt2},\tfrac1{\sqrt2})$ y decrece fuera. Máximo $f(\tfrac1{\sqrt2})=\tfrac{1}{\sqrt{2e}}\approx0.429$ y un mínimo simétrico. $f''(x)=2x(2x^2-3)e^{-x^2}$ se anula y cambia de signo en $0$ y en $\pm\sqrt{3/2}$: hay **3 inflexiones**. (Verificado con sympy.) Es la versión difícil de U Ej. 2.23.

---

## (a) Teoría mínima necesaria (páginas impresas verificadas en `ingenieros.txt`)

| Resultado | Dónde en U | Ejercicios que lo usan |
|---|---|---|
| Teorema de Bolzano | §1.4, p. 52 | ejemplo A3 |
| Asíntotas (horizontal, vertical, oblicua; Prop. 1.12) | §1.4, pp. 48-49 | 2.50, D1-D3 |
| Continuidad (Def. 1.20), composición (Prop. 1.14) | §1.4, p. 51 | 2.42, 2.49 |
| Derivadas laterales (Def. 2.3) | §2.2, p. 81 | 2.42, 2.49 |
| Reglas de derivación, regla de la cadena y tablas | §2.2, pp. 79-80 | todos |
| L'Hôpital; $\lim \operatorname{sen}x/x=1$ (Ej. 2.8) | §2.3.2, pp. 82-83 | 2.49, 2.50 |
| **Teorema de Rolle** (y contraejemplos cuando falla una hipótesis) | **§2.5.2, pp. 95-96** | 2.39, 2.40, 2.49 |
| **Teorema del valor medio** (demostración e interpretación) | **§2.5.3, pp. 96-97** | 2.41, 2.42, 2.46 |
| **Teorema 2.4** (constante $\iff f'=0$) | §2.5.3, p. 97 | 2.45 |
| **Def. 2.5** (creciente, estrictamente creciente…) | §2.5.4, p. 98 | 2.43, 2.44, 2.48 |
| **Prop. 2.4** (signo de $f'$ $\Rightarrow$ monotonía; solo suficiente) | §2.5.4, p. 98 | 2.44, 2.46-2.48, 2.50-2.51 |
| Ej. 2.22 ($x^3$ estrictamente creciente con $f'(0)=0$) y Ej. 2.23 | pp. 99-100 | 2.43, 2.48, B3 |
| Punto crítico (Def. 3.5), extremos absolutos (Prop. 3.4) | §3.4.2, p. 126 | 2.50, 2.51 |
| Extremo relativo (Def. 3.6), Prop. 3.5 (cambio de monotonía) | §3.4.3, p. 130 | 2.48, 2.50, 2.51 |
| Punto de silla (Def. 3.7), criterio de la 2.ª derivada (Prop. 3.7) | p. 131 | 2.51 |
| Derivadas de orden superior (Prop. 3.8) | p. 132 | 2.51 |
| Convexidad (Prop. 3.9-3.10), inflexión (Def. 3.10, Prop. 3.11-3.12) | §3.5.2, pp. 136-137 | 2.50, 2.51 (opcional) |
| **Funciones hiperbólicas** | **no aparecen en U** (solo «paraboloide hiperbólico», p. 220) | 2.45 → usar S o L |

## (b) Huecos de U y dónde suplirlos (S / L; páginas impresas verificadas en `stewart.txt` y `larson.txt`)

1. **Funciones hiperbólicas** (2.45): U no las define. → **S §3.11 «Funciones hiperbólicas», p. 257** (definición, identidades y derivadas en pp. 257-259); **L §5.8 «Funciones hiperbólicas», p. 383** (gráficas y dominios en p. 384).
2. **Intuición geométrica de Rolle y del TVM** (figuras y aplicaciones del tipo «a lo sumo una raíz»): U solo trae los enunciados y pocos ejemplos. → **S §4.2 «Teorema del valor medio», p. 284** (Rolle p. 284, TVM p. 285, «$f'=0\Rightarrow$ constante» p. 287); **L §3.2 «El teorema de Rolle y el teorema del valor medio», p. 170** (Teorema 3.3, Rolle, p. 170; Teorema 3.4, TVM, p. 172).
3. **Criterio de la primera derivada y tabla de signos**: U lo recoge como Prop. 3.5 (p. 130), sin tabla de signos. → **S §4.3 «Cómo afecta la derivada la forma de una gráfica», p. 290** (Prueba C/D en p. 290); **L §3.3 «Funciones crecientes y decrecientes y el criterio de la primera derivada», p. 177** (Teorema 3.5 en p. 177, criterio de la primera derivada en p. 179).
4. **Concavidad y cambio de nombres**: U llama «convexa» a la forma de $x^2$, mientras que S y L dicen «cóncava hacia arriba». → **L §3.4 «Concavidad y criterio de la segunda derivada», pp. 187-188**; S §4.3 (segunda parte). Hay que avisar al estudiante del cambio de nombre; manda la notación de U.
5. **Método completo para representar gráficas** (2.50-2.51): U no tiene una sección con el procedimiento. → **S §4.5 «Resumen de trazado de curvas», p. 310**; **L §3.6 «Un resumen del trazado de curvas», p. 206** (Ejemplo 1, función racional, en p. 207; ejercicios de relacionar gráficas en p. 212).
6. **Límite y sucesiones** (usado en 2.49 b): U no lo enuncia en §1.4; solo da el sentido $f(x)\to l\Rightarrow f(n)\to l$ (Prop. 2.3, p. 85). En la solución se demuestra en una línea a partir de la definición; conviene decirlo explícitamente en el resumen.
7. **«El límite de $f'$ es la derivada lateral»** (lo usa E en 2.49 d): no está en U. Se evita usando la definición de derivada lateral (U p. 81), como en la solución de arriba.

## (c) Erratas, omisiones y avisos sobre E

| Ejercicio | Tipo | Detalle |
|---|---|---|
| 2.40 (p. 77) | Omisión en el enunciado | «tiene tres ceros» debería decir «tres ceros **distintos**»: con raíces múltiples la tesis falla ($x^3$). La hipótesis «grado $\ge3$» sobra. |
| 2.46 (p. 81) | Rigor | Deduce que $f$ no es monótona solo porque $f'$ cambia de signo, pero U (Prop. 2.4) solo da la implicación directa. Falta dar $a<b$ con $f(a)>f(b)$, lo que se hace con el TVM. |
| 2.49 (p. 83) | Errata de redacción | Dice «cuando la función seno tiende a infinito»; debe decir «cuando **$x$** tiende a infinito». |
| 2.49 d) (p. 83) | Rigor | Usa los límites laterales de $f'$ en vez de las derivadas laterales, lo que necesita un resultado que U no da. Es mejor hacerlo por definición: $|\operatorname{sen}h|/h\to\pm1$. Además, $f$ no es derivable en ningún $1+k\pi$ con $k\ge1$, no solo en $1+3\pi$. |
| 2.50 (p. 84) | Estilo | Usa L'Hôpital para $\lim_{x\to\pm\infty}\frac{x^3+1}x$, cuando basta escribir $x^2+\frac1x$. |
| 2.51 (p. 86) | Razonamiento incompleto | Calcula los tres puntos críticos, pero decide solo mirando $x=\pi$ y por eliminación. El recuento «exactamente 3 puntos con tangente horizontal» es la prueba directa. Tampoco explica que $\pi$ es un punto de silla. |
| 2.40, 2.42, 2.49, 2.51 | **No son erratas de E** | El `.txt` pierde la barra de «≠» («$s=t$», «$-2\pi=2\pi$», «$f'(0)=f'(2\pi)=0$»). El PDF dice $\ne$ (comprobado en la imagen de las páginas). |
| — | Organización | E pone 2.39-2.51 en su Tema 2, y en U esta teoría **también** está en el Tema 2 (§2.5, pp. 94-101). Solo los extremos y la concavidad son del Tema 3 (§3.4-3.5). |

*Verificación:* todos los cálculos (derivadas, límites, ceros de $f'$, valores de los extremos, identidades hiperbólicas, signos en puntos de prueba y ejemplos propios) se han comprobado con sympy.
