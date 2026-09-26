# Soluciones — Tema 1.4 Límites y continuidad

**Fuentes.** Ejercicios del libro **E** (*Libro de ejercicios Cálculo 24-25*, `ejercicios.txt`; página impresa = PDF). Teoría del libro **U** (*Cálculo para Ingenieros*, `ingenieros.txt`; página impresa = PDF + 2). Apoyos: **S** (Stewart, `stewart.txt`; página tomada de la cabecera impresa) y **L** (Larson, `larson.txt`; impresa = PDF − 17). Todas las páginas se han comprobado en los `.txt`. Los enunciados dudosos (raíces, fracciones y barras de ≠ que pdftotext pierde) se han contrastado con el PDF de E renderizado a imagen (1.23-1.25, 1.27, 1.30-1.41). Todos los resultados se han verificado con sympy (límites, factorizaciones, raíces) y con una implementación de la bisección en Python.

## 0. Alcance y mapa de la teoría

**Ejercicios de E de §1.4:** del **1.23 al 1.41** (E pp. 25-41). El 1.42 (E p. 42) ya trata de sucesiones de funciones, que no entran en el examen.

**Aviso sobre la extensión de §1.4 en U:** la sección no acaba en la p. 53. El método de bisección sigue en la **p. 54** (fórmula del error), el **Ejemplo 1.49** ocupa las **pp. 55-56** y §1.5 empieza en la p. 56. Hay que citar **U §1.4, pp. 42-56**.

| Contenido de U §1.4 | Página impresa |
|---|---|
| Motivación. **Convenio: los ángulos van en radianes** | 42 |
| §1.4.2 Funciones reales, dominio («el mayor conjunto en el que puede estar definida»), imagen, función acotada, gráfica | 43 |
| **Def. 1.18** (límite ε-δ, con $x\in D\setminus\{a\}$), Ejemplo 1.42 | 43 |
| **Prop. 1.9** (conservación del signo), unicidad del límite, Ejemplos 1.43 y 1.44 ($\operatorname{sen}\frac1x$ no tiene límite en 0) | 44-45 |
| **Regla del emparedado**, **Prop. 1.10** (función que tiende a 0 por función acotada, con su versión local) | 45 |
| **Prop. 1.11** (álgebra de límites), **límites infinitos** ($f(x)\ge k$), Ejemplo 1.45, **Def. 1.19** (restricción) | 46 |
| **Límites laterales**, Ejemplo 1.46 ($1/x$), **Teorema 1.4** (límite ⇔ laterales iguales), **límites en el infinito**, Ejemplo 1.47 | 47-48 |
| **Asíntotas**: horizontal (p. 48), vertical y oblicua, **Prop. 1.12** ($m=\lim f(x)/x$) | 48-49 |
| Ejemplo 1.48 (asíntota oblicua $y=x+1$) | 49-50 |
| §1.4.3 **Def. 1.20** (continuidad), **Prop. 1.13** (suma, producto, cociente), **Prop. 1.14** (composición), **Def. 1.21** | 51 |
| **Teorema de Bolzano**, **teorema de los valores intermedios**, Bolzano en intervalos no cerrados (con límites), **Prop. 1.15 (Weierstrass)** | 52-53 |
| Contraejemplo $x^{-1}$ en $(0,1)$; **método de bisección** (planteamiento) | 53 |
| Iteración de bisección; **error $\lvert c_n-\tilde x\rvert<\frac{b-a}{2^n}$** | 54 |
| $n>\log_2\frac{b-a}{\varepsilon}$; **Ejemplo 1.49** ($e^{-x}=x$) | 54-56 |

Herramientas de §1.2 que se reutilizan: **Def. 1.12** (recta ampliada y operaciones con $\pm\infty$, p. 27), **indeterminaciones** (pp. 29-30), **fórmula (1.1)** $a^b=e^{b\ln a}$ y el paso del límite dentro de una función continua (p. 29), **Prop. 1.5** ($\left(1+\frac1{a_n}\right)^{a_n}\to e$, p. 31).

**Orden didáctico que se sigue** (de fácil a difícil, conservando la numeración de E):
- **A. Dominio y cálculo de límites:** 1.25 → 1.24 → 1.23 → 1.26 → 1.27
- **B. Asíntotas:** 1.28 → 1.29 → 1.30
- **C. Continuidad:** 1.32 → 1.31 → 1.33 → 1.34
- **D. Bolzano, valores intermedios y Weierstrass:** 1.38 → 1.36 → 1.35 → 1.37
- **E. Método de bisección:** 1.40 → 1.41 → 1.39

Cada bloque termina con 2-4 ejemplos propios de dificultad creciente.

---

# A. Dominio y cálculo de límites

## Ejercicio 1.25 (E pp. 26-27)

> Sea $f$ la función definida por
> $$f(x)=\operatorname{sen}\sqrt{\frac{x}{(x-1)^6}}.$$
> Se pide determinar su dominio de definición.

**Solución.**

1. **Qué se pide.** U fija el convenio de que, si no se da el dominio, se toma «el mayor conjunto en el que puede estar definida» la función (U §1.4.2, p. 43). Hay que encontrar todos los $x$ para los que la fórmula tiene sentido.
2. **Descomponer de fuera hacia dentro.** $f$ se calcula en tres etapas: $x\mapsto q(x)=\dfrac{x}{(x-1)^6}\mapsto\sqrt{q(x)}\mapsto\operatorname{sen}\sqrt{q(x)}$. Cada etapa impone su condición:
   - $\operatorname{sen}$ está definido en todo $\mathbb R$, así que no añade ninguna.
   - $\sqrt{\ \cdot\ }$ exige que el radicando exista y sea $\ge 0$.
   - El cociente $q$ exige que el denominador no sea $0$, porque dividir entre $0$ no está definido.
3. **Denominador.** $(x-1)^6=0\iff x=1$. Se excluye $x=1$.
4. **Signo del radicando.** Si $x\neq1$, $(x-1)^6>0$, porque es una potencia par de un número no nulo. Dividir por un número positivo no cambia el signo, así que $q(x)$ tiene el signo de $x$: $q(x)\ge0\iff x\ge0$.
5. **Conclusión.** $D=\{x\in\mathbb R:\ x\ge0,\ x\neq1\}=[0,1)\cup(1,+\infty)$.
   *Comprobación (sympy):* `solve_univariate_inequality(x/(x-1)**6>=0)` → `(x>=0) & Ne(x,1)`.

**Receta.** Para el dominio de una composición, anota la condición de cada pieza (denominador $\neq0$, raíz de índice par con radicando $\ge0$, logaritmo con argumento $>0$) y resuelve el sistema. El signo de un cociente se obtiene del signo de cada factor.

**Error típico.** Olvidar excluir $x=1$ («como $1\ge0$, vale»). También exigir $x>0$, cuando $x=0$ sí vale ($\sqrt0=0$). Y decir, como E, que en $x=1$ «la fracción vale $\pm\infty$»: en $x=1$ la fracción **no está definida**. $\pm\infty$ solo aparece como límite.

*Teoría:* U §1.4.2, p. 43 (convenio del dominio).

## Ejercicio 1.24 (E p. 26)

> Sea $f$ la función dada por $f(x)=\dfrac{x^2-x}{x^2+2x-3}$. Se pide calcular $\lim_{x\to1}f(x)$.

**Solución.**

1. **Intentar sustituir.** Un cociente de polinomios es continuo donde el denominador no se anula (U Prop. 1.13, p. 51), y en esos puntos el límite es el valor de la función. Pero en $x=1$ el denominador vale $1+2-3=0$, así que $1\notin D$. Al sustituir sale $\frac00$, que es una **indeterminación** (U p. 29): no dice nada del límite.
2. **Por qué factorizar.** Si un polinomio se anula en $x=1$, tiene el factor $(x-1)$ (regla de Ruffini o teorema del factor). Los dos polinomios se anulan en 1, así que los dos tienen el factor $(x-1)$ y se puede simplificar.
3. **Factorizar.** Numerador: $x^2-x=x(x-1)$. Denominador: las raíces de $x^2+2x-3$ son $x=\frac{-2\pm\sqrt{4+12}}{2}=\frac{-2\pm4}{2}\in\{1,-3\}$, así que $x^2+2x-3=(x-1)(x+3)$.
4. **Simplificar solo donde se puede.** Para $x\neq1$ (y $x\neq-3$), $f(x)=\dfrac{x(x-1)}{(x-1)(x+3)}=\dfrac{x}{x+3}$. **Por qué basta:** la Def. 1.18 (U p. 43) solo mira los $x\in D\setminus\{a\}$ cercanos a $a$. Si dos funciones coinciden cerca de $a$ salvo en $a$, tienen el mismo límite en $a$ (L Teorema 1.7, p. 62).
5. **Calcular.** $\frac{x}{x+3}$ es continua en $1$, porque su denominador vale $4\neq0$. Por tanto $\displaystyle\lim_{x\to1}f(x)=\frac{1}{1+3}=\frac14$. *(sympy: `1/4`.)*

**Receta.** Si en un cociente de polinomios aparece $\frac00$ en $x=a$, saca el factor $(x-a)$ arriba y abajo, simplifica y vuelve a sustituir.

**Error típico.** Escribir «$f(1)=\frac14$»: $f$ no está definida en 1, lo que vale $\frac14$ es el límite. También decir que $\frac00=1$ o que «$\frac00$ ⇒ el límite no existe».

*Teoría:* U Def. 1.18 p. 43; Prop. 1.13 p. 51; indeterminaciones p. 29.

## Ejercicio 1.23 (E p. 25)

> Sean $f(x)$ y $g(x)$ dos funciones con límite (es decir, sus valores tienden a un número real) cuando $x$ tiende a $x_0$. ¿La función $f/g$ también tiene límite en $x_0$?

**Solución.** No siempre.

1. **Qué dice la teoría.** Por U Prop. 1.11 (p. 46), si $\lim f=l$, $\lim g=m$ y $m\neq0$ (con $g\neq0$ en el dominio), entonces $\lim\frac fg=\frac lm$. Si $m\neq0$ la respuesta es «sí», así que un contraejemplo tiene que tener $m=0$.
2. **Elegir bien el numerador.** Si también $l=0$, sale $\frac00$, que es indeterminado: a veces hay límite (por ejemplo $\frac xx\to1$). Para asegurar que el límite no existe conviene $l\neq0$.
3. **Contraejemplo.** $x_0=0$, $f(x)=\cos x$, $g(x)=x$. Como $\cos$ es continua (U p. 29), $\lim_{x\to0}\cos x=\cos0=1$, y $\lim_{x\to0}x=0$.
4. **Límite por la derecha.** Si $0<x<\pi/3$, entonces $\cos x\ge\frac12$ y $\dfrac{\cos x}{x}\ge\dfrac1{2x}$. Dado $k>0$, basta $0<x<\delta=\min\{\pi/3,\ \frac1{2k}\}$ para tener $\frac{\cos x}{x}\ge k$. Por la definición de límite infinito (U p. 46) aplicada a la restricción a $(0,\infty)$ (U p. 47), $\lim_{x\to0^+}\frac{\cos x}x=+\infty$.
5. **Límite por la izquierda.** Si $x<0$, el numerador sigue siendo positivo y el denominador es negativo. El mismo argumento da $\lim_{x\to0^-}\frac{\cos x}x=-\infty$.
6. **Conclusión.** Si existiera $\lim_{x\to0}\frac{\cos x}{x}=l\in\mathbb R$, por el Teorema 1.4 (U p. 47) los dos laterales valdrían $l$. Pero valen $+\infty$ y $-\infty$, así que no hay límite. *(sympy: `oo`, `-oo`.)* Un contraejemplo aún más simple es $f=1$, $g=x$.

**Receta.** Para refutar un «¿siempre…?», mira qué hipótesis del teorema correspondiente puede fallar (aquí $m\neq0$) y construye un ejemplo en el que falle. Si el denominador tiende a 0 y el numerador a $l\neq0$, estudia los laterales con la **regla del signo**: $\frac{l}{0^{\pm}}=\pm\infty$ según los signos.

**Error típico.** Pensar que «0 en el denominador ⇒ $\infty$» sin mirar signos: $\frac1{x^2}\to+\infty$, pero $\frac1x$ no tiene límite en 0. Sobre E: al decir que «los límites laterales no existen (no son números reales)» mezcla dos cosas. Como límites *reales* (U p. 47) no existen, pero como límites *infinitos* sí existen y son distintos.

*Teoría:* U Prop. 1.11 p. 46; límites infinitos p. 46; límites laterales y Teorema 1.4 p. 47.

## Ejercicio 1.26 (E p. 27)

> Se pide calcular el siguiente límite: $\displaystyle\lim_{x\to+\infty}\frac{\ln x}{\ln 4x^4}$.

**Solución.**

1. **Dominio.** Hace falta $x>0$ para $\ln x$, y $4x^4>0$ si $x\neq0$. Para $x>1$ el cociente está bien definido y tiene sentido hacer $x\to+\infty$ (U p. 47).
2. **Tipo de límite.** $\ln t\to+\infty$ cuando $t\to+\infty$, así que sale $\frac{+\infty}{+\infty}$, que es indeterminado (U p. 30).
3. **Mismo argumento en los dos logaritmos.** Para $x>0$, por las propiedades del logaritmo, $\ln(4x^4)=\ln4+\ln x^4=\ln4+4\ln x$.
4. **Dividir entre el término que crece** ($\ln x>0$ si $x>1$):
$$\frac{\ln x}{\ln4+4\ln x}=\frac{1}{\dfrac{\ln4}{\ln x}+4}.$$
5. **Pasar al límite.** $\frac{\ln 4}{\ln x}\to0$, porque una constante entre algo que tiende a $\infty$ tiende a 0 (U Def. 1.12, p. 27: $\frac{x}{\infty}=0$). El denominador tiende a $4\neq0$, así que por U Prop. 1.11 el límite es $\dfrac14$. *(sympy: `1/4`.)*

**Receta.** Con logaritmos de argumentos distintos, usa $\ln(ab)=\ln a+\ln b$ y $\ln a^b=b\ln a$ para que todo quede en función de un mismo $\ln x$. Luego divide entre el término dominante, como con los polinomios.

**Error típico.** Escribir $\ln(4x^4)=4\ln(4x)$ o $\ln4\cdot\ln x^4$. También «simplificar el $\ln$» como si $\frac{\ln x}{\ln 4x^4}=\frac{x}{4x^4}$.

*Teoría:* U límites en el infinito p. 47; Prop. 1.11 p. 46; Def. 1.12 p. 27.

## Ejercicio 1.27 (E pp. 27-28)

> Se pide calcular el siguiente límite: $\displaystyle\lim_{x\to+\infty}\left(\frac{x+1}{x-1}\right)^{x}$.

**Solución.**

1. **Tipo.** Al dividir entre $x$, la base es $\frac{1+1/x}{1-1/x}\to1$, y el exponente tiende a $+\infty$. Sale $1^{\infty}$, que es una indeterminación (U p. 30). **No vale 1.**
2. **Herramienta.** Para sucesiones, U Prop. 1.5 (p. 31) da $\left(1+\frac{1}{a_n}\right)^{a_n}\to e$ si $a_n\to\pm\infty$. E usa la versión para funciones: $\left(1+\frac1{F(x)}\right)^{F(x)}\to e$ si $F(x)\to\pm\infty$. **U no la enuncia** (ver «Huecos»; S §3.6 p. 222 da $e=\lim_{x\to0}(1+x)^{1/x}$). Aquí se acepta como extensión natural de la Prop. 1.5.
3. **Escribir la base como $1+\frac1F$.** $\dfrac{x+1}{x-1}=\dfrac{(x-1)+2}{x-1}=1+\dfrac{2}{x-1}=1+\dfrac{1}{F(x)}$, con $F(x)=\dfrac{x-1}{2}\to+\infty$.
4. **Hacer aparecer $F$ en el exponente.** Se multiplica y divide por $F$: $x=F(x)\cdot\dfrac{x}{F(x)}=F(x)\cdot\dfrac{2x}{x-1}$. Así
$$\left(\frac{x+1}{x-1}\right)^x=\Big[\big(1+\tfrac1{F(x)}\big)^{F(x)}\Big]^{\frac{2x}{x-1}}\qquad(x>1,\ \text{base}>0).$$
5. **Límite de $A(x)^{B(x)}$.** Aquí $A(x)=\big(1+\frac1F\big)^F\to e$ y $B(x)=\frac{2x}{x-1}\to2$ (dividiendo entre $x$). Con la fórmula (1.1) de U (p. 29), $A^B=e^{B\ln A}$. Como $\ln$ y $\exp$ son continuas (U p. 29), $\ln A\to\ln e=1$, $B\ln A\to2$ y $A^B\to e^2$.
6. **Resultado:** $e^2\approx7.389$. *(sympy: `exp(2)`; con $x=1000$ la expresión vale $7.38906$.)*

**Receta (indeterminación $1^\infty$).** Si $A\to1$ y $B\to\pm\infty$, escribe $A=1+\frac1F$ con $F=\frac1{A-1}$ y el exponente como $B=F\cdot\frac BF$. El resultado es $e^{\lim B(A-1)}$. Aquí: $\lim x\cdot\frac2{x-1}=2$.

**Error típico.** Decir «$1^\infty=1$». Otro error es sacar el límite de la base y del exponente por separado cuando la base tiende a 1: eso solo vale si el resultado no es una indeterminación.

*Teoría:* U indeterminaciones p. 30; fórmula (1.1) p. 29; Prop. 1.5 p. 31 (versión para sucesiones).

### Ejemplos propios (bloque A)

- **(propio A1, fácil)** Dominio de $f(x)=\ln(x^2-4)+\sqrt{5-x}$. El logaritmo exige $x^2-4>0\iff x<-2$ o $x>2$; la raíz exige $x\le5$. **Solución:** $D=(-\infty,-2)\cup(2,5]$. *(sympy.)*
- **(propio A2, fácil)** $\displaystyle\lim_{x\to2}\frac{x^2-4}{x^2-3x+2}$. Sale $\frac00$. Factorizando: $\frac{(x-2)(x+2)}{(x-2)(x-1)}=\frac{x+2}{x-1}\to\frac41=4$. *(sympy: 4.)*
- **(propio A3, media: conjugado)** $\displaystyle\lim_{x\to0}\frac{\sqrt{1+x}-1}{x}$. Sale $\frac00$ y no hay polinomio que factorizar. Se multiplica por el conjugado (como en U Ejemplo 1.24, p. 29): $\frac{(1+x)-1}{x(\sqrt{1+x}+1)}=\frac1{\sqrt{1+x}+1}\to\frac12$. *(sympy: 1/2.)*
- **(propio A4, difícil: $1^\infty$)** $\displaystyle\lim_{x\to+\infty}\left(\frac{x+2}{x-3}\right)^{2x+1}$. La base es $1+\frac5{x-3}$, así que el límite es $e^{\lim(2x+1)\frac{5}{x-3}}=e^{10}$. *(sympy: `exp(10)`.)* Otro de logaritmos: $\displaystyle\lim_{x\to+\infty}\frac{\ln(x^2+1)}{\ln x}=2$, porque $\ln(x^2+1)=2\ln x+\ln\!\left(1+\frac1{x^2}\right)$ y el último término tiende a $\ln1=0$.

---

# B. Asíntotas

**Recordatorio (U pp. 48-49).**
- $y=b$ es **asíntota horizontal** si $\lim_{x\to+\infty}f(x)=b$ y/o $\lim_{x\to-\infty}f(x)=b$.
- $x=a$ es **asíntota vertical** si algún lateral en $a$ vale $\pm\infty$.
- $y=mx+b$ con $m\neq0$ es **asíntota oblicua** si $f(x)-(mx+b)\to0$ en $+\infty$ y/o en $-\infty$. Para encontrarla: $m=\lim\frac{f(x)}{x}$ (Prop. 1.12) y $b=\lim(f(x)-mx)$.

## Ejercicio 1.28 (E pp. 28-29)

> La función dada por $f(x)=\dfrac{x^2+1}{x^2-1}$ tiene: a) Asíntota vertical. b) Asíntota oblicua. c) Asíntota horizontal. d) No tiene asíntotas.

**Solución.** Son correctas **a) y c)**.

1. **Dominio:** $x^2-1\neq0\iff x\neq\pm1$.
2. **Horizontales.** Se divide entre $x^2$: $f(x)=\dfrac{1+1/x^2}{1-1/x^2}\to\dfrac{1+0}{1-0}=1$ cuando $x\to\pm\infty$. Por tanto $y=1$ es asíntota horizontal en $+\infty$ y en $-\infty$. Otra forma de verlo: $f(x)=1+\frac{2}{x^2-1}$, y el último término tiende a 0.
3. **Verticales: dónde buscar.** En cualquier $a\neq\pm1$, $f$ es continua (U Prop. 1.13), así que el límite es el número $f(a)$ y no hay asíntota. Solo pueden estar en $x=\pm1$, donde el denominador se anula y el numerador vale $2\neq0$.
4. **Signos laterales.** Se escribe $x^2-1=(x-1)(x+1)$.
   - $x\to1^+$: $(0^+)(2)\to0^+$ y $f\to+\infty$. $x\to1^-$: $(0^-)(2)\to 0^-$ y $f\to-\infty$.
   - $x\to-1^-$ ($x<-1$): los dos factores son negativos, el producto tiende a $0^+$ y $f\to+\infty$. $x\to-1^+$: el producto tiende a $0^-$ y $f\to-\infty$.

   Por tanto $x=1$ y $x=-1$ son asíntotas verticales. *(sympy: `[-oo, oo, oo, -oo]`.)*
5. **Oblicua.** Una asíntota oblicua exige $f\to\pm\infty$ en ese lado (U p. 49). Aquí $f\to1$, así que no hay. Con la Prop. 1.12 se llega a lo mismo: $\frac{f(x)}x\to0$, y una oblicua necesita $m\neq0$.

**Receta (funciones racionales $P/Q$).**
- **Verticales:** en los ceros de $Q$ que no anulan $P$, con el signo de cada lateral.
- **Horizontal:** si $\operatorname{gr}P\le\operatorname{gr}Q$.
- **Oblicua:** si $\operatorname{gr}P=\operatorname{gr}Q+1$.

**Error típico.** Confundir los signos de los laterales. Creer que la gráfica no puede cortar a una asíntota horizontal (sí puede). Tomar como vertical un punto donde numerador y denominador se anulan a la vez: suele ser un «agujero» (ver 1.24).

*Teoría:* U asíntotas pp. 48-49; Prop. 1.12 p. 49.

## Ejercicio 1.29 (E pp. 30-31)

> Sea $f$ la función dada por $f(x)=\dfrac{x^3+2x^2-1}{x^2-4}$. Se pide encontrar las asíntotas de $f$, si las tiene.

**Solución.**

1. **Dominio:** $x\neq\pm2$.
2. **Verticales.** Si $a\neq\pm2$, $\lim_{x\to a}f=f(a)$ es finito. En $a=2$ el numerador vale $8+8-1=15>0$, y el denominador es $(x-2)(x+2)$.
   - $x\to2^+$: el denominador tiende a $(0^+)(4)=0^+$, así que $f\to+\infty$. Si $x\to2^-$, $f\to-\infty$.
   - En $a=-2$ el numerador vale $-8+8-1=-1<0$. Si $x\to-2^+$: $(x-2)\to-4$ y $(x+2)\to0^+$, así que el denominador tiende a $0^-$ y $f\to\frac{-1}{0^-}=+\infty$. Si $x\to-2^-$, el denominador tiende a $0^+$ y $f\to-\infty$.

   Por tanto **$x=2$ y $x=-2$** son asíntotas verticales. *(sympy: `[-oo, oo, -oo, oo]` para $2^-,2^+,-2^-,-2^+$.)*
3. **Horizontales.** Al dividir entre $x^2$, $f(x)=\dfrac{x+2-1/x^2}{1-4/x^2}$, que tiende a $+\infty$ en $+\infty$ y a $-\infty$ en $-\infty$. No hay horizontales, y se cumple la condición necesaria para una oblicua (U p. 49).
4. **Oblicua, con el método de U (Prop. 1.12 y Ejemplo 1.48).**
   - $m=\displaystyle\lim_{x\to\pm\infty}\frac{f(x)}{x}=\lim\frac{x^3+2x^2-1}{x^3-4x}=1$.
   - $b=\displaystyle\lim_{x\to\pm\infty}\big(f(x)-x\big)=\lim\frac{x^3+2x^2-1-x^3+4x}{x^2-4}=\lim\frac{2x^2+4x-1}{x^2-4}=2$.

   La asíntota oblicua es **$y=x+2$**, la misma en $+\infty$ y en $-\infty$. *(sympy: $m=1$, $b=2$ en ambos lados.)*
5. **Comprobación por división.** $x^3+2x^2-1=(x+2)(x^2-4)+(4x+7)$, así que $f(x)=x+2+\dfrac{4x+7}{x^2-4}$ y el resto tiende a 0. Además el resto es positivo para $x$ grande y negativo para $x\to-\infty$, así que la gráfica queda por encima de la asíntota a la derecha y por debajo a la izquierda, como en la figura de E p. 32.

*Sobre el desarrollo de E:* E calcula $\lim(f-mx)$ con $m$ genérico, en vez de hallar primero $m$ con la Prop. 1.12. Es correcto, aunque más largo. En el `.txt` se han perdido las barras de «$a^2\neq4$» y «$\pm\infty$ si $m\neq1$»; en el PDF están bien.

**Receta.** Asíntota oblicua: $m=\lim\frac{f}{x}$, $b=\lim(f-mx)$, cada lado por separado. En una racional, la división de polinomios da $mx+b$ directamente.

**Error típico.** Quedarse en $m$ y olvidar $b$. Dar por hecho que en $-\infty$ sale la misma recta: con raíces no tiene por qué (ver propio B3).

*Teoría:* U pp. 48-50 (Prop. 1.12, Ejemplo 1.48).

## Ejercicio 1.30 (E p. 32)

> Razone si existen funciones que tengan asíntotas horizontales y oblicuas.

**Solución.** Sí, pero **nunca en el mismo lado**.

1. **En el mismo lado es imposible.** Una horizontal en $+\infty$ significa $\lim_{x\to+\infty}f=b\in\mathbb R$. Una oblicua en $+\infty$ exige $\lim_{x\to+\infty}f=\pm\infty$ (U p. 49). Por la unicidad del límite (U p. 44) no puede pasar lo uno y lo otro. Otra forma de verlo: si $f\to b$, entonces $\frac{f(x)}x\to0$, y una oblicua necesita $m\neq0$.
2. **En lados distintos es posible.** E da la función
$$f(x)=\begin{cases}\dfrac{1}{x-1}, & x<0,\[2mm] \dfrac{x^2+1}{x-1}, & x>0.\end{cases}$$
3. **En $-\infty$:** $\frac1{x-1}\to0$, así que $y=0$ es asíntota horizontal.
4. **En $+\infty$:** $\frac{f(x)}x=\frac{x^2+1}{x^2-x}\to1=m$ y $f(x)-x=\frac{x+1}{x-1}\to1=b$, así que $y=x+1$ es asíntota oblicua. Por división: $\frac{x^2+1}{x-1}=x+1+\frac{2}{x-1}$.
5. **Vertical** $x=1$, dentro de la rama $x>0$: el numerador tiende a $2$, así que $x\to1^-$ da $-\infty$ y $x\to1^+$ da $+\infty$.
6. **En $x=0$** (lo analizamos nosotros; E no lo comenta): $f$ no está definida, pero los dos laterales valen $\frac{1}{-1}=-1$ y $\frac{0+1}{0-1}=-1$. Hay límite ($-1$), así que no hay asíntota; es un «agujero» en la gráfica. *(sympy: $-1$ y $-1$.)* La figura de E lo dibuja como una curva continua.

**Resumen:** horizontal $y=0$ (en $-\infty$), oblicua $y=x+1$ (en $+\infty$) y vertical $x=1$.

**Receta.** Estudia $+\infty$ y $-\infty$ **por separado**. En cada lado hay como mucho una recta asíntota: horizontal u oblicua, nunca las dos.

**Error típico.** Afirmar que «si tiene horizontal no puede tener oblicua» sin decir en qué lado.

*Teoría:* U pp. 48-49; unicidad del límite p. 44.

### Ejemplos propios (bloque B)

- **(propio B1, fácil)** $f(x)=\dfrac{2x+1}{x-3}$. Tiene vertical $x=3$ ($3^-$: $-\infty$; $3^+$: $+\infty$, porque el numerador vale $7>0$) y horizontal $y=2$ en ambos lados. *(sympy.)*
- **(propio B2, media)** $f(x)=\dfrac{x^2-3x}{x+1}$. Tiene vertical $x=-1$ (el numerador vale $4>0$; $-1^-$: $-\infty$; $-1^+$: $+\infty$). No tiene horizontales. Oblicua: $m=\lim\frac{x^2-3x}{x^2+x}=1$ y $b=\lim\frac{-4x}{x+1}=-4$, así que es $y=x-4$ en ambos lados. Por división: $x^2-3x=(x+1)(x-4)+4$. *(sympy.)*
- **(propio B3, difícil: horizontal en un lado y oblicua en el otro)** $f(x)=\sqrt{x^2+1}+x$.
  - En $-\infty$: con el conjugado, $f=\dfrac{1}{\sqrt{x^2+1}-x}\to0$, así que hay horizontal $y=0$.
  - En $+\infty$: $\frac{f}{x}=\sqrt{1+1/x^2}+1\to2$ y $f-2x=\sqrt{x^2+1}-x=\frac1{\sqrt{x^2+1}+x}\to0$, así que hay oblicua $y=2x$.

  *(sympy: 0, 2, 0.)* Es otra respuesta al 1.30, con una sola fórmula en vez de una función a trozos.

---

# C. Continuidad

**Recordatorio.** $f$ es continua en $a\in D$ si $\lim_{x\to a}f(x)=f(a)$ (U Def. 1.20, p. 51). Por tanto hacen falta tres cosas: que $f(a)$ exista, que exista el límite y que coincidan. Sumas, productos, cocientes con denominador no nulo y composiciones de funciones continuas son continuos (U Props. 1.13 y 1.14, p. 51). Polinomios, trigonométricas, exponenciales y logaritmos son continuos en su dominio (U p. 29).

## Ejercicio 1.32 (E p. 34)

> Sea $f$ la función definida por
> $$f(x)=\begin{cases}\dfrac{x^3-8}{x-2}, & x\neq2,\ k, & x=2.\end{cases}$$
> Se pide encontrar para qué valor de $k$ la función es continua en $\mathbb R$.

**Solución.**

1. **Puntos $x\neq2$.** Cerca de cada uno de ellos $f$ es un cociente de polinomios con denominador no nulo, así que es continua (U Prop. 1.13). Esto no depende de $k$.
2. **Punto $x=2$.** Por la Def. 1.20, $f$ es continua en 2 si y solo si $\lim_{x\to2}f(x)=f(2)=k$.
3. **Límite.** Sale $\frac00$, así que $x=2$ es raíz del numerador. Por Ruffini o por la diferencia de cubos $a^3-b^3=(a-b)(a^2+ab+b^2)$: $x^3-8=(x-2)(x^2+2x+4)$.
4. Para $x\neq2$, $f(x)=x^2+2x+4$, y esta expresión es continua. Como el límite en 2 solo usa $x\neq2$ (U Def. 1.18), $\lim_{x\to2}f(x)=4+4+4=12$.
5. **Conclusión:** $f$ es continua en $\mathbb R$ si y solo si **$k=12$**. *(sympy: 12.)*

**Receta.** Para una función definida por separado en un punto con un parámetro: continuidad en ese punto ⇔ (límite, o los dos laterales) = valor. Se despeja el parámetro.

**Error típico.** Poner $k=0$ «porque el numerador se anula». Sustituir en $\frac{x^3-8}{x-2}$ y quedarse en $\frac00$.

*Teoría:* U Def. 1.20 y Prop. 1.13, p. 51.

## Ejercicio 1.31 (E p. 33)

> Sea $f$ la función definida por $f(x)=x\cos\dfrac1x$. ¿Se puede definir en $x=0$ de tal forma que sea continua en $\mathbb R$?

**Solución.** Sí, con $f(0)=0$.

1. **Fuera de 0.** En $\mathbb R\setminus\{0\}$, $f$ es continua: $x\mapsto\frac1x$ es continua si $x\neq0$, $\cos$ es continua, la composición también lo es (Prop. 1.14) y el producto por $x$ también (Prop. 1.13).
2. **Qué hace falta en 0.** Hay que dar un valor $f(0)=L$ con $L=\lim_{x\to0}f(x)$ (Def. 1.20). Por la unicidad del límite, si existe es la única elección posible, y si no existe no hay forma de hacerla continua.
3. **Acotar.** Como $\lvert\cos t\rvert\le1$ para todo $t$, se tiene $-\lvert x\rvert\le x\cos\frac1x\le\lvert x\rvert$ para $x\neq0$.
4. **Emparedado (U p. 45).** $\lim_{x\to0}\lvert x\rvert=\lim_{x\to0}(-\lvert x\rvert)=0$, así que $\lim_{x\to0}x\cos\frac1x=0$. Otra vía es U Prop. 1.10 (p. 45), en su versión local: $x\to0$ y $\cos\frac1x$ está acotada cerca de 0, así que el producto tiende a 0. *(sympy: 0.)*
5. **Redefinición:** $f(0)=0$.

*Comparación:* $\operatorname{sen}\frac1x$ no tiene límite en 0 (U Ejemplo 1.44, p. 44), porque oscila entre $-1$ y $1$. El factor $x$ reduce esas oscilaciones hasta 0.

*Sobre E:* E escribe «$\cos x\in[-1,1]$», pero lo que se usa es $\cos\frac1x$. También escribe «$0\le\lim\lvert f\rvert\le\lim\lvert x\rvert$» antes de saber que $\lim\lvert f\rvert$ existe: es el emparedado el que prueba que existe. La nota al margen de E, $\lim g=0\iff\lim\lvert g\rvert=0$, no está en U, pero sale directamente de la Def. 1.18, porque $\big\lvert\lvert g\rvert-0\big\rvert=\lvert g-0\rvert$.

**Receta.** (función acotada) × (función que tiende a 0) → 0.

**Error típico.** Usar Prop. 1.11 para escribir $\lim x\cdot\lim\cos\frac1x=0\cdot(\text{algo})$: la regla del producto exige que **los dos** límites existan, y $\lim\cos\frac1x$ no existe.

*Teoría:* U Regla del emparedado y Prop. 1.10, p. 45; Def. 1.20, p. 51.

## Ejercicio 1.33 (E pp. 34-35)

> Sea $f$ la función dada por
> $$f(x)=\begin{cases}e^{-\frac{1}{(1+x)^2}}, & x\neq-1,\ e^{-\frac14}, & x=-1.\end{cases}$$
> Se pide calcular $\lim_{x\to-1}f(x)$ y estudiar la continuidad de $f$ en $\mathbb R$.

**Solución.**

1. **Si $x\neq-1$.** El exponente $t(x)=-\frac1{(1+x)^2}$ es un cociente con denominador no nulo, así que es continuo. $\exp$ es continua. Por la Prop. 1.14, $f$ es continua en todo $x\neq-1$.
2. **Límite en $-1$, desde dentro hacia fuera.**
   - $(1+x)^2\to0$, y es **positivo** para $x\neq-1$ por ser un cuadrado; se escribe $0^+$.
   - Por tanto $\frac1{(1+x)^2}\to+\infty$ y el exponente $-\frac1{(1+x)^2}\to-\infty$.
   - $e^{t}\to0$ cuando $t\to-\infty$. Por eso $\lim_{x\to-1}f(x)=0$. *(sympy: 0.)*
   - Justificación: en la recta ampliada, $e^{+\infty}=+\infty$ (U Def. 1.12, $x^\infty=\infty$ si $x>1$), y $e^{-\infty}=\frac1{e^{+\infty}}=0$. El paso «límite de una composición» para funciones no está enunciado en U (ver «Huecos»).
3. **Comparar con el valor.** $f(-1)=e^{-1/4}\approx0.7788\neq0$. Por tanto $f$ **no es continua en $-1$**. Sí lo es en $\mathbb R\setminus\{-1\}$.
4. **Tipo de discontinuidad** (terminología de S §2.5 p. 120, no de U): el límite existe pero no coincide con el valor, así que es **evitable**. Poniendo $f(-1)=0$ la función sería continua.

**Receta.** Con una exponencial, calcula primero el límite del exponente (con su signo) y luego aplica $e^{+\infty}=+\infty$, $e^{-\infty}=0$ o, si es finito, la continuidad de $\exp$.

**Error típico.** Olvidar el signo menos y concluir que el límite es $+\infty$. Decir que $f$ «no está definida en $-1$»: sí lo está, vale $e^{-1/4}$; lo que falla es la igualdad entre límite y valor.

*Teoría:* U Def. 1.20 y Prop. 1.14, p. 51; Def. 1.12, p. 27.

## Ejercicio 1.34 (E p. 35)

> Sean $f$ y $g$ las funciones definidas por $f(x)=\lvert x\rvert$ y
> $$g(x)=\begin{cases}e^{-\frac{1}{(1+x)^2}}, & x\neq-1,\ e^{-\frac14}, & x=-1.\end{cases}$$
> Se pide estudiar la continuidad de $g\circ f$.

**Solución.** $g\circ f$ es continua en todo $\mathbb R$.

1. **$f=\lvert x\rvert$ es continua en $\mathbb R$.** Si $x\neq0$, cerca de $x$ coincide con $x$ o con $-x$, que son polinomios. En $0$, $\lim_{x\to0^-}(-x)=0=\lim_{x\to0^+}x$, así que por el Teorema 1.4 (U p. 47) el límite es $0=f(0)$.
2. **$g$** es continua en $\mathbb R\setminus\{-1\}$ y discontinua en $-1$ (Ejercicio 1.33).
3. **Regla de la composición (U Prop. 1.14, p. 51).** $g\circ f$ es continua en $a$ si $f$ es continua en $a$ y $g$ es continua en $f(a)$. Para cualquier $a$, $f(a)=\lvert a\rvert\ge0$, así que $f(a)\neq-1$, y $g$ es continua en $f(a)$. Por tanto $g\circ f$ es continua en todo $a\in\mathbb R$.
4. **Fórmula explícita:** $(g\circ f)(x)=e^{-\frac1{(1+\lvert x\rvert)^2}}$, con $1+\lvert x\rvert\ge1>0$. El único punto problemático de $g$, el $-1$, no está en la imagen $f(\mathbb R)=[0,\infty)$.

*Sobre E:*
- E dice que «el argumento de $g$ es siempre positivo»; en realidad es **no negativo** (vale $0$ en $x=0$), aunque la conclusión no cambia.
- La frase final de E, «$g\circ f$ es continua, aunque no es composición, suma y cociente de funciones continuas», es **incorrecta o, como poco, confusa**. $g\circ f$ **sí** es composición de funciones continuas: $\lvert x\rvert$, luego $t\mapsto-\frac1{(1+t)^2}$ (continua en $t\ge0$) y luego $\exp$. Lo que importa es que la Prop. 1.14 es **local**: solo pide continuidad de $g$ en los puntos $f(a)$.
- Aunque no se pide: $f\circ g=\lvert g\rvert=g$ (porque $g>0$) sí es discontinua en $-1$.

**Receta.** En $g\circ f$, las discontinuidades de $g$ solo importan si son valores que $f$ alcanza, es decir, si están en $f(D)$.

**Error típico.** Razonar «$g$ es discontinua, luego $g\circ f$ también lo es».

*Teoría:* U Prop. 1.14 y Def. 1.20, p. 51; Teorema 1.4, p. 47.

### Ejemplos propios (bloque C)

- **(propio C1, fácil)** Hallar $a$ para que $f(x)=\begin{cases}x^2+a,&x<1\2x+3,&x\ge1\end{cases}$ sea continua. $\lim_{x\to1^-}f=1+a$ y $\lim_{x\to1^+}f=5=f(1)$. Por el Teorema 1.4, $1+a=5$, así que **$a=4$**. *(sympy.)*
- **(propio C2, media)** ¿Se puede extender $f(x)=x^2\operatorname{sen}\frac1x$ a $x=0$ de forma continua? Como $\lvert x^2\operatorname{sen}\frac1x\rvert\le x^2\to0$, sí, con $f(0)=0$. *(sympy: 0.)*
- **(propio C3, difícil: discontinuidad no evitable)** $f(x)=\dfrac{x^2-1}{\lvert x-1\rvert}$ en $x=1$. Para $x>1$, $f=x+1\to2$; para $x<1$, $f=-(x+1)\to-2$. Los laterales son distintos, así que no hay límite (Teorema 1.4) y **ningún** valor de $f(1)$ la hace continua (discontinuidad de salto). *(sympy: 2 y −2.)*

---

# D. Bolzano, valores intermedios y Weierstrass

**Enunciados (U p. 52).**
- **Bolzano:** si $f:[a,b]\to\mathbb R$ es continua y $f(a)f(b)<0$, existe $c\in(a,b)$ con $f(c)=0$.
- **Valores intermedios (TVI):** si $f$ es continua en $[a,b]$ y $d$ está estrictamente entre $f(a)$ y $f(b)$, existe $c\in(a,b)$ con $f(c)=d$.
- **Weierstrass (Prop. 1.15, pp. 52-53):** una función continua en un intervalo $[a,b]$ cerrado y acotado alcanza en él su máximo y su mínimo.

## Ejercicio 1.38 (E pp. 38-39)

> Sea $f$ la función dada por la expresión $f(x)=\dfrac{x+2}{x^5+1}$. ¿Existe un punto $x_0\in[0,3]$ tal que $f(x_0)=\frac12$? Si es así, demuéstrelo.

**Solución.** Sí.

1. **Continuidad en $[0,3]$.** Numerador y denominador son polinomios, así que son continuos. Si $x\ge0$, $x^5+1\ge1>0$: el denominador no se anula y el cociente es continuo (U Prop. 1.13).
2. **Valores en los extremos.** $f(0)=\frac{2}{1}=2$ y $f(3)=\frac{5}{244}\approx0.0205$.
3. **Colocar $d=\frac12$.** $f(3)<\frac12<f(0)$. Por el **teorema de los valores intermedios** (U p. 52) existe $x_0\in(0,3)$ con $f(x_0)=\frac12$.
   Equivale a aplicar Bolzano a $h=f-\frac12$: $h(0)=\frac32>0$ y $h(3)<0$.
4. *Numéricamente* $x_0\approx1.4236$ (sympy `nsolve`). El ejercicio no pide unicidad.

**Receta.** Para responder a «¿existe $x$ con $f(x)=d$?»: comprueba que $f$ es continua en el intervalo y encuentra dos puntos en los que $f$ quede a cada lado de $d$. Entonces se aplica el TVI.

**Error típico.** No comprobar que el denominador no se anula en el intervalo. En $[-2,0]$ este mismo $f$ **no** es continuo, porque $x^5+1=0$ en $x=-1$.

*Teoría:* U TVI y Bolzano, p. 52.

## Ejercicio 1.36 (E pp. 36-37)

> Sean $f$ y $g$ las funciones definidas, para $x\in[0,+\infty)$, como $f(x)=\dfrac{4x^4}{x^2+x+1}$, $g(x)=\cos x$. ¿Existe algún punto $x\in[0,+\infty)$ donde $f(x)=g(x)$?

**Solución.** Sí.

1. **Convertirlo en un problema de ceros.** $f(x)=g(x)\iff h(x):=f(x)-g(x)=0$. Bolzano sirve para encontrar ceros.
2. **Continuidad de $h$.** $x^2+x+1>0$ para todo $x$, porque su discriminante es $1-4<0$ y el coeficiente principal es positivo. Así $f$ es continua; $\cos$ también, y la diferencia también (Prop. 1.13).
3. **Un punto con $h<0$:** $h(0)=0-\cos0=-1<0$.
4. **Un punto con $h>0$.** E usa $\lim_{x\to+\infty}h(x)=+\infty$ ($f$ se comporta como $4x^2$ y $\cos$ está acotado), que asegura que existe algún $b$ con $h(b)>0$. Es más cómodo dar uno concreto: $b=1$, $h(1)=\frac43-\cos1\ge\frac43-1>0$ (hace falta solo $\cos1\le1$). *(Numéricamente $h(1)\approx0.793$.)*
5. **Bolzano en $[0,1]$:** existe $c\in(0,1)$ con $h(c)=0$, es decir, $f(c)=g(c)$. *(sympy: $c\approx0.8075$.)*

**Receta.** Para una igualdad $f=g$, aplica Bolzano a $h=f-g$. Busca puntos de prueba sencillos ($0$, $1$, $\pi/2$…) antes de recurrir a límites.

**Error típico.** Aplicar Bolzano «en $[0,+\infty)$» sin un extremo finito $b$. U solo lo enuncia en $[a,b]$; la versión para intervalos no acotados (U p. 52) exige hipótesis sobre límites.

*Teoría:* U Bolzano y su extensión, p. 52.

## Ejercicio 1.35 (E pp. 35-36)

> Se pide demostrar, utilizando el teorema de Bolzano, que cualquier polinomio de grado impar con coeficientes reales tiene al menos una raíz real.

**Solución.**

1. **Planteamiento.** $p(x)=a_nx^n+\dots+a_1x+a_0$ con $n$ impar y $a_n\neq0$. Se puede suponer $a_n>0$: si no, se trabaja con $-p$, que tiene las mismas raíces.
2. **Límites en $\pm\infty$.** Para $x\neq0$, $p(x)=x^n\Big(a_n+\frac{a_{n-1}}{x}+\dots+\frac{a_0}{x^n}\Big)$. El paréntesis tiende a $a_n>0$, porque cada $\frac{a_k}{x^{n-k}}\to0$. Como $n$ es impar, $x^n$ tiene el signo de $x$: $x^n\to+\infty$ si $x\to+\infty$ y $x^n\to-\infty$ si $x\to-\infty$. Con las reglas $x\cdot(\pm\infty)$ de U Def. 1.12 (p. 27): $\lim_{x\to+\infty}p=+\infty$ y $\lim_{x\to-\infty}p=-\infty$.
3. **De los límites a dos puntos concretos.** Aplicando la definición de límite infinito en el infinito con $k=1$ (U la deja al lector, p. 47; ver «Huecos»): existe $b$ con $p(b)\ge1>0$ y existe $a<b$ con $p(a)\le-1<0$.
   *(Versión constructiva, propia:* con $M=1+\frac{\lvert a_0\rvert+\dots+\lvert a_{n-1}\rvert}{a_n}$, si $\lvert x\rvert\ge M$ se tiene $\lvert a_{n-1}x^{n-1}+\dots+a_0\rvert\le(\sum\lvert a_k\rvert)\lvert x\rvert^{n-1}=a_n(M-1)\lvert x\rvert^{n-1}<a_n\lvert x\rvert^n$. Por tanto $p(x)$ tiene el signo de $a_nx^n$, y se puede tomar $a=-M$, $b=M$.)
4. **Bolzano.** $p$ es continua en $[a,b]$ (es un polinomio) y $p(a)p(b)<0$, así que existe $c\in(a,b)$ con $p(c)=0$.

*Por qué hace falta que el grado sea impar:* $x^2+1$ no tiene raíces reales, porque con grado par los dos límites tienen el mismo signo.
*Omisión menor de E:* E escribe el grado como $2k+1$ con $k\in\mathbb N$. En U, $\mathbb N=\{1,2,\dots\}$ (U p. 12), así que queda fuera el grado 1. Ese caso es trivial: la raíz es $-a_0/a_1$.

**Receta.** Si hay que probar que existe una raíz sin que den un intervalo, usa los límites en $\pm\infty$ (o en los extremos del dominio) para encontrar dos puntos con signos opuestos.

**Error típico.** Creer que se ha demostrado que hay **una sola** raíz: Bolzano solo da «al menos una». Aplicar el argumento a grado par.

*Teoría:* U Bolzano p. 52; Def. 1.12 p. 27.

## Ejercicio 1.37 (E p. 37)

> Sea $f$ la función definida, en el intervalo $(0,+\infty)$, por $f(x)=\dfrac{e^{-x}}{x}$. ¿Existen los valores $\lim_{x\to0^+}f(x)$ y $\lim_{x\to+\infty}f(x)$? Si existen, ¿alcanza la imagen de $f$ el valor del supremo o del ínfimo en algún punto de $(0,+\infty)$? ¿Contradice esto el teorema de Weierstrass?

**Solución.**

1. **$x\to0^+$.** El numerador tiende a $e^0=1$ y el denominador a $0^+$, así que $\lim_{x\to0^+}f=+\infty$ (mismo razonamiento que en 1.23). La imagen **no está acotada superiormente** y no tiene supremo en $\mathbb R$ (U solo define supremo para conjuntos acotados superiormente, §1.1 p. 20).
2. **$x\to+\infty$.** Para $x>0$, $0<e^{-x}<1$, así que $0<f(x)<\frac1x$. Como $\frac1x\to0$, la regla del emparedado (U p. 45) da $\lim_{x\to+\infty}f=0$. *(sympy: `oo`, `0`.)*
3. **Ínfimo.** $f(x)>0$ para todo $x$, así que $0$ es cota inferior. Como $f\to0$, para cada $\varepsilon>0$ hay puntos con $f(x)<\varepsilon$, y ninguna cota inferior puede ser mayor que 0. Por tanto $\inf f\big((0,\infty)\big)=0$, pero **no se alcanza**, porque $f(x)>0$.
   De hecho, $f$ es continua y estrictamente decreciente (producto de dos funciones positivas y decrecientes, $e^{-x}$ y $\frac1x$). Con los límites anteriores y el TVI se deduce que su imagen es exactamente $(0,+\infty)$.
4. **Weierstrass.** La Prop. 1.15 (U pp. 52-53) exige un intervalo $[a,b]$ **cerrado y acotado**. $(0,+\infty)$ no es ni una cosa ni la otra: basta con que falle una. Si falla una hipótesis, el teorema no dice nada, así que **no hay contradicción**. U da un contraejemplo análogo en p. 53: $x^{-1}$ en $(0,1)$.

*Sobre E:* E escribe «$0\le\lim f\le\lim\frac1x$» antes de saber que $\lim f$ existe (ver el comentario en 1.31) y no dice de forma explícita que $\inf=0$.

**Receta.** Para usar Weierstrass comprueba tres cosas: $f$ continua, intervalo cerrado, intervalo acotado. Si falla una, el máximo o el mínimo pueden no alcanzarse.

**Error típico.** Pensar que «no alcanza el mínimo, luego contradice Weierstrass». Decir que el ínfimo «no es 0» porque no se alcanza: ínfimo y mínimo son cosas distintas.

*Teoría:* U Prop. 1.15, pp. 52-53; emparedado, p. 45; supremo e ínfimo, §1.1 p. 20.

### Ejemplos propios (bloque D)

- **(propio D1, fácil)** $x^3+x-1=0$ tiene una raíz en $(0,1)$: $f(0)=-1<0$, $f(1)=1>0$ y $f$ es continua, así que se aplica Bolzano. *(Raíz $\approx0.6823$.)*
- **(propio D2, media: Weierstrass es condición suficiente, no necesaria)** $f(x)=x^2$ en $(-1,2]$. El intervalo no es cerrado, y aun así $f$ alcanza el mínimo $0$ (en $x=0$) y el máximo $4$ (en $x=2$). En cambio, $f(x)=x$ en $(0,1)$ no alcanza ni el supremo 1 ni el ínfimo 0.
- **(propio D3, difícil: contar raíces con Bolzano)** $p(x)=x^5-3x+1$. $p(-2)=-25$, $p(-1)=3$, $p(0)=1$, $p(1)=-1$, $p(2)=27$. Hay tres cambios de signo, en $(-2,-1)$, $(0,1)$ y $(1,2)$, así que $p$ tiene **al menos 3** raíces reales. *(sympy: $-1.3888,\ 0.3347,\ 1.2147$.)*

---

# E. Método de bisección

**Recordatorio (U pp. 53-55).** Si $f$ es continua en $[a,b]$ y $f(a)f(b)<0$:
- Se toma $c_1=\frac{a+b}2$ y se conserva la mitad en cuyos extremos $f$ cambia de signo.
- Se repite el proceso con la mitad elegida.
- Tras $n$ iteraciones, $\lvert c_n-\tilde x\rvert<\frac{b-a}{2^n}$. Para un error menor que $\varepsilon$ basta $n>\log_2\frac{b-a}{\varepsilon}$.

## Ejercicio 1.40 (E pp. 40-41)

> El polinomio $x^3-3$ tiene una única raíz en el intervalo $[0,4]$. Se pide aproximarla realizando 3 iteraciones con el método de bisección y acotar el error cometido.

**Solución.**

1. **Hipótesis.** $f(x)=x^3-3$ es continua, $f(0)=-3<0$ y $f(4)=61>0$, así que Bolzano garantiza una raíz. Es única porque $x^3$ es estrictamente creciente. La raíz es $\sqrt[3]3$.
2. **Iteraciones:**

| $n$ | $[a,b]$ | $c_n$ | $f(c_n)$ | intervalo siguiente |
|---|---|---|---|---|
| 1 | $[0,4]$ | 2 | $5>0$ | $[0,2]$ |
| 2 | $[0,2]$ | 1 | $-2<0$ | $[1,2]$ |
| 3 | $[1,2]$ | 1.5 | $0.375>0$ | $[1,1.5]$ |

   La mitad que se conserva es siempre la que tiene signos opuestos en sus extremos. **Aproximación:** $c_3=1.5$.
3. **Cota del error (U p. 54):** $\lvert c_3-\sqrt[3]3\rvert<\frac{4-0}{2^3}=\frac12$.
   *Comprobación:* $\sqrt[3]3\approx1.44225$, así que el error real es $\approx0.0578$, muy por debajo de la cota. La cota es para el peor caso.

**Receta.** Haz una tabla con $a$, $b$, $c$ y el signo de $f(c)$. Tras $n$ puntos medios, el error es menor que $\frac{b-a}{2^n}$.

**Error típico.** Quedarse con la mitad equivocada: hay que mirar los **signos**, no qué valor está más cerca de 0. Contar mal las iteraciones: la cota corresponde al número de **puntos medios** calculados.

*Teoría:* U método de bisección, pp. 53-54.

## Ejercicio 1.41 (E p. 41)

> Tenemos una función continua $f:[0,1]\to\mathbb R$, con $f(0)=-1$ y $f(1)=4$. Buscamos una solución aproximada en $[0,1]$ por el método de bisección para la ecuación $f(x)=0$. ¿Cuántas iteraciones son necesarias para asegurar que el error que cometemos al tomar la solución aproximada es menor que $0.11$? a) No se puede aplicar el método de la bisección. b) Faltan datos. c) 3. d) 4.

**Solución.** La respuesta es **d) 4**.

1. **a) es falsa:** $f$ es continua y $f(0)f(1)=-4<0$, así que se cumplen las hipótesis.
2. **b) es falsa:** la cota $\frac{b-a}{2^n}$ solo depende de la longitud del intervalo y de $n$, no de la forma de $f$.
3. **Cálculo:** hace falta $\frac{1}{2^n}<0.11\iff2^n>\frac1{0.11}\approx9.09$. Como $2^3=8<9.09<16=2^4$, el menor $n$ es $4$. Con la fórmula de U (pp. 54-55): $n>\log_2\frac1{0.11}\approx3.18$, así que $n=4$.

**Errata de E:** escribe $\frac1{2^4}=\frac1{16}=0.0635$, pero $\frac1{16}=0.0625$. La respuesta no cambia.
*Matiz:* con 3 iteraciones el error **podría** ser menor que 0.11, pero no se puede **asegurar**, porque la cota es $0.125$.

**Receta.** $n$ es el menor entero con $n>\log_2\frac{b-a}{\varepsilon}$, o lo que es lo mismo, $2^n>\frac{b-a}{\varepsilon}$.

**Error típico.** Elegir 3 porque «$0.125\approx0.11$». Calcular $\log_2(0.11)$ en lugar de $\log_2(1/0.11)$.

*Teoría:* U pp. 54-55.

## Ejercicio 1.39 (E pp. 39-40)

> ¿Por qué no puede aplicarse el método de bisección a cualquier ecuación $f(x)=0$ en un intervalo cerrado $I$? Para ayudar a contestar a esta pregunta, pedimos que se construya analítica o gráficamente una función $f$ para la que $f(x)=0$ tenga una solución en el intervalo $[0,1]$, $f(0)f(1)<0$ y tal que el método de bisección no se pueda aplicar.
> ¿Se puede aplicar a cualquier ecuación $f(x)=0$ en un intervalo cerrado $I$ cuando $f$ sea continua?
> ¿Existen funciones continuas en el intervalo $[0,1]$, para las que $f(c)=0$ para $c\in[0,1]$ y a las que no se puede aplicar el método de la bisección?

**Solución.**

1. **En qué se apoya el método.** En cada paso el método usa **Bolzano** (U pp. 53-54): un cambio de signo en los extremos de un subintervalo garantiza una raíz en él, pero solo si $f$ es **continua**. Sin continuidad, un cambio de signo puede deberse a un salto, y el método puede quedarse con una mitad en la que no hay raíz.
2. **Ejemplo analítico** (propio, que reproduce la figura de E p. 40):
$$f(x)=\begin{cases}-1,&0\le x\le0.3,\ 1,&0.3<x\le0.6,\ x-0.8,&0.6<x\le1.\end{cases}$$
   - $f(0)=-1$ y $f(1)=0.2$, así que $f(0)f(1)<0$. La única raíz es $x=0.8$.
   - Primer paso: $c_1=0.5$ y $f(0.5)=1>0$. Hay cambio de signo en $[0,0.5]$ y el método se queda con esa mitad, **donde no hay raíz**.
   - Los intervalos siguientes se van cerrando sobre el salto $x=0.3$, donde $f(0.3)=-1\neq0$. *(Simulado: tras 12 iteraciones, $c\approx0.30005$.)*
3. **¿Basta con que $f$ sea continua?** No. Además hace falta $f(a)f(b)<0$; si no, el método no puede ni empezar. Ejemplo: $f(x)=(x-\frac13)(x-\frac23)$ en $[0,1]$ tiene dos raíces, pero $f(0)=f(1)=\frac29>0$.
4. **Continua, con raíz y sin bisección posible.** $f(x)=(x-0.6)^2$ en $[0,1]$ tiene la raíz $0.6$, pero $f\ge0$ en todo el intervalo. No hay cambio de signo en ningún subintervalo, así que la bisección no se puede aplicar nunca.
   - La raíz se ha puesto en $0.6$ y no en $\frac12$: si estuviera en $\frac12$, el primer punto medio la encontraría por casualidad.
   - E dice que «si el signo de $f(1/2)$ es el mismo… el método fallará». Más exacto: con $f(0)f(1)>0$ el método **ni siquiera arranca**.

**Receta.** Antes de biseccionar comprueba: (1) continuidad en $[a,b]$ y (2) $f(a)f(b)<0$. La bisección no detecta raíces en las que la función no cambia de signo, como las raíces dobles.

**Error típico.** Creer que basta $f(a)f(b)<0$, o que basta la continuidad.

*Teoría:* U Bolzano, p. 52; método de bisección, pp. 53-54.

### Ejemplos propios (bloque E)

- **(propio E1, fácil)** Aproximar $\sqrt2$ con $f(x)=x^2-2$ en $[1,2]$ haciendo 3 iteraciones.
  - $c_1=1.5$: $f=0.25>0$, se pasa a $[1,1.5]$.
  - $c_2=1.25$: $f=-0.4375<0$, se pasa a $[1.25,1.5]$.
  - $c_3=1.375$: $f\approx-0.109<0$.

  Error $<\frac{1}{2^3}=0.125$; el error real es $\lvert1.375-1.41421\rvert\approx0.039$. *(Python.)*
- **(propio E2, media)** ¿Cuántas iteraciones hacen falta en $[0,1]$ para asegurar un error menor que $10^{-3}$? $n>\log_2 1000\approx9.97$, así que **$n=10$** ($2^{10}=1024>1000$).
- **(propio E3, difícil)** Resolver $\cos x=x$ en $[0,1]$ con 4 iteraciones. Con $f(x)=\cos x-x$: $f(0)=1>0$ y $f(1)\approx-0.46<0$.
  - $c_1=0.5$: $f(c_1)\approx0.378>0$.
  - $c_2=0.75$: $f(c_2)\approx-0.018<0$.
  - $c_3=0.625$: $f(c_3)\approx0.186>0$.
  - $c_4=0.6875$.

  Error $<\frac1{16}=0.0625$; la raíz real es $0.73909$, así que el error es $\approx0.052$. *(Python y sympy.)*

---

# (a) Teoría necesaria (lo que el redactor debe explicar), con página impresa de U verificada

| Concepto / resultado | Dónde (U) | Ejercicios que lo usan |
|---|---|---|
| Dominio por convenio, imagen, función acotada | §1.4.2, p. 43 | 1.25, 1.37 |
| Definición ε-δ de límite (**con $x\neq a$**) | Def. 1.18, p. 43 | 1.24, 1.32 (simplificar), 1.31 |
| Conservación del signo; unicidad del límite | Prop. 1.9 y texto, p. 44 | 1.30 |
| Ejemplo sin límite: $\operatorname{sen}\frac1x$ | Ej. 1.44, pp. 44-45 | contraste con 1.31 |
| Regla del emparedado; Prop. 1.10 (tiende a 0 × acotada) y su versión local | p. 45 | 1.31, 1.37, C2 |
| Álgebra de límites (Prop. 1.11: suma, producto, cociente con $m\neq0$) | p. 46 | 1.23, 1.26 y todos |
| Límites infinitos ($f(x)\ge k$) | p. 46 | 1.23, 1.28, 1.29, 1.37 |
| Restricción (Def. 1.19), límites laterales, Teorema 1.4 | pp. 46-47 | 1.23, 1.28-1.30, 1.34, C1, C3 |
| Límites en el infinito ($\pm\infty$) | p. 47, Ej. 1.47 pp. 47-48 | 1.26-1.30, 1.35, 1.37 |
| Asíntotas horizontal, vertical y oblicua; Prop. 1.12 ($m=\lim f/x$); Ej. 1.48 | pp. 48-50 | 1.28, 1.29, 1.30 |
| Continuidad en un punto (Def. 1.20); Prop. 1.13 (operaciones); Prop. 1.14 (composición); Def. 1.21 | p. 51 | 1.31-1.34, 1.36, 1.38 |
| **Teorema de Bolzano**; **teorema de los valores intermedios**; Bolzano en intervalos no cerrados o no acotados usando límites | p. 52 | 1.35, 1.36, 1.38, 1.39 |
| **Teorema de Weierstrass** (Prop. 1.15) y contraejemplo $x^{-1}$ en $(0,1)$ | pp. 52-53 | 1.37 |
| **Método de bisección**, cota $\frac{b-a}{2^n}$, $n>\log_2\frac{b-a}{\varepsilon}$, Ejemplo 1.49 | pp. 53-56 | 1.39, 1.40, 1.41 |
| Convenio de radianes | p. 42 | 1.23, 1.36 |
| (de §1.2) Recta ampliada y operaciones con $\pm\infty$ (Def. 1.12) | p. 27 | 1.26, 1.33, 1.35 |
| (de §1.2) Indeterminaciones (lista de 7) | pp. 29-30 | 1.24, 1.26, 1.27 |
| (de §1.2) $a^b=e^{b\ln a}$ (fórmula 1.1); el límite «entra» en funciones continuas; lista de funciones continuas | p. 29 | 1.23, 1.27, 1.33 |
| (de §1.2) $\left(1+\frac1{a_n}\right)^{a_n}\to e$ (Prop. 1.5) | p. 31 | 1.27 |
| (de §1.2) Conjugado para $\infty-\infty$ (Ej. 1.24) | p. 29 | A3, B3 |
| (de §1.1) Supremo e ínfimo | p. 20 | 1.37 |

# (b) Huecos de U que hay que cubrir con S o L

1. **Álgebra con divisiones entre 0 (regla del signo $\frac{l}{0^\pm}$).** U Def. 1.12 (p. 27) no define $\frac{x}{0}$. Se usa en 1.23, 1.28, 1.29, 1.30, 1.33 y 1.37. Cubrir con **L §1.5, Teorema 1.14 (asíntotas verticales), p. 85, y Teorema 1.15 (propiedades de los límites infinitos), p. 87**, y con **S §2.2, Def. 6 (asíntota vertical), p. 94**.
2. **Límites infinitos en el infinito** (U p. 47 «deja al lector» su definición). Se usan en 1.29, 1.35 y 1.36. Ver **L §3.5, «Definición de límites al infinito» (límites infinitos al infinito), p. 201**.
3. **Límite de una composición** ($\lim g(f(x))=g(\lim f(x))$ si $g$ es continua; $e^{t}\to0$ si $t\to-\infty$). U solo da la continuidad de la composición (Prop. 1.14, p. 51) y el comentario de p. 29 para sucesiones. Se usa en 1.27 y 1.33. Ver **S §2.5, Teorema 8, p. 124**, y **L §1.3, Teorema 1.5 (límite de una función compuesta), p. 61**.
4. **Funciones que coinciden salvo en un punto tienen el mismo límite** (lo que justifica «simplificar y sustituir»). En U se deduce de la Def. 1.18, pero no está enunciado. Se usa en 1.24 y 1.32. Ver **L §1.3, Teorema 1.7, p. 62**.
5. **$\left(1+\frac1{F(x)}\right)^{F(x)}\to e$ para funciones.** U solo la da para sucesiones (Prop. 1.5, p. 31) y E la usa en 1.27 como si fuera conocida. Ver **S §3.6, «El número $e$ como un límite», p. 222** (usa derivadas, así que conviene presentarlo como hecho admitido).
6. **Tipos de discontinuidad** (evitable, de salto, infinita). U no los nombra. Se usan en 1.33, 1.30 (agujero en $x=0$) y C3. Ver **S §2.5, p. 120** (discontinuidad «removible», infinita y de salto) y **L §1.4, p. 71** («evitable»).
7. **Asíntota oblicua mediante división de polinomios**, como alternativa a $m$ y $b$. Ver **L §3.5, p. 201** (asíntota oblicua) y **S §4.5, «Asíntotas inclinadas», p. 315** (página deducida de las cabeceras vecinas, porque el `.txt` corta mal la página; conviene confirmarla en el PDF).
8. **Regla del emparedado para funciones** (versión detallada con dibujo): **L §1.3, Teorema 1.8, p. 65** y **S §2.3, Teorema 3 (de la compresión), p. 105**.
9. **Límites laterales y continuidad en intervalo cerrado:** **L §1.4, pp. 72-73** (Teorema 1.10).
10. **TVI y bisección con ejemplos:** **S §2.5, Teorema 10 (valor intermedio), p. 125**; **L §1.4, Teorema 1.13, p. 77** y bisección en p. 78. **Aviso:** la traducción de L llama al TVI «**Teorema del valor medio**», que no hay que confundir con el teorema del valor medio de las derivadas (Tema 3).
11. **Teorema de Weierstrass (valor extremo) con figuras:** **S §4.1, Teorema 3, p. 275**; **L §3.1, Teorema 3.1, p. 162**.
12. **Condiciones de límite en $-\infty$ para asíntotas horizontales:** **S §2.6, Defs. 2 y 3, p. 131**; **L §3.5, pp. 195-196** (definición de asíntota horizontal y Teorema 3.10).
13. **$\lim g=0\iff\lim\lvert g\rvert=0$** (nota al margen de E en 1.31): no está en U, pero sale inmediatamente de la Def. 1.18. Se puede explicar como nota propia.

# (c) Erratas e imprecisiones de E (1.23-1.41)

**Pérdidas de extracción en el `.txt` (en el PDF están bien, pero el redactor no debe copiarlas del `.txt`):**
- Barras de ≠ perdidas en: 1.25 «$x\neq1$»; 1.29 «$a^2\neq4$» y «$\pm\infty$ si $m\neq1$»; 1.28 margen «con $m\neq0$»; 1.32 «$x\neq2$»; 1.33 y 1.34 «$x\neq-1$»; 1.35 «$a_{2k+1}\neq0$».
- Raíces y fracciones descolocadas en: 1.25 ($\sqrt{x/(x-1)^6}$), 1.26, 1.27, 1.30 (la función a trozos), 1.36 ($\frac{4x^4}{x^2+x+1}$) y 1.38.

**Erratas e imprecisiones reales de E:**

1. **1.41 (p. 41):** «$\frac1{2^4}=\frac1{16}=0.0635$», pero **$\frac1{16}=0.0625$**. La respuesta d) no cambia.
2. **1.34 (p. 35):** «el argumento de $g$ es siempre positivo»: es **no negativo** ($\lvert0\rvert=0$). La frase final «aunque no es composición, suma y cociente de funciones continuas» es **incorrecta o confusa**: $g\circ f$ sí es composición de funciones continuas; lo que cuenta es que la Prop. 1.14 es local.
3. **1.31 (p. 33):** «como $\cos x\in[-1,1]$» debería ser $\cos\frac1x$. Además escribe desigualdades entre límites ($0\le\lim\lvert f\rvert\le\lim\lvert x\rvert$) antes de saber que existen, cuando la existencia la da el emparedado.
4. **1.37 (p. 37):** el mismo defecto: «$0\le\lim f\le\lim\frac1x$». Tampoco dice explícitamente que $\inf=0$ ni que la imagen es $(0,+\infty)$.
5. **1.35 (pp. 35-36):** con $\mathbb N=\{1,2,\dots\}$ (U p. 12), «grado $2k+1$, $k\in\mathbb N$» deja fuera el grado 1 (caso trivial). Además dice «como el límite es $-\infty$ **y un polinomio es continuo**, existe $a$ con $p(a)<0$», pero ese paso se sigue de la definición de límite, no de la continuidad.
6. **1.25 (p. 26):** «eliminar los puntos donde la fracción sea $\pm\infty$»: en $x=1$ la fracción **no está definida**; $\pm\infty$ es un límite, no un valor.
7. **1.23 (p. 25):** «Los límites laterales no existen (no son números reales)». Es impreciso: como límites infinitos existen ($+\infty$ y $-\infty$) y son distintos, y eso es lo que impide que haya límite.
8. **1.39 (p. 40):** en la tercera pregunta, con $f(0)f(1)>0$ el método **no puede empezar**; E lo explica como si fallara en el paso de $f(1/2)$. Además, si la raíz tangente estuviera exactamente en $\frac12$, el primer punto medio la encontraría (la figura de E la sitúa en $\approx0.55$).
9. **1.30 (p. 32):** no es una errata, pero la figura dibuja continua la unión en $x=0$, donde $f$ **no está definida** (los dos laterales valen $-1$: hay un agujero). La asíntota vertical está en $x=1$.
10. **1.27 (p. 28):** usa $\left(1+\frac1{f(x)}\right)^{f(x)}\to e$ para funciones «porque hemos trabajado su equivalente para sucesiones», pero U no lo enuncia para funciones (hueco 5).
11. **1.29 (p. 30):** el método de E ($\lim(f-mx)$ con $m$ genérico) no es el de U (Prop. 1.12: primero $m=\lim f/x$). Es correcto; conviene enseñar el de U.

**Extensión de U §1.4:** la sección no acaba en la p. 53 sino en la **p. 56** (la cota de error de la bisección está en la p. 54 y el Ejemplo 1.49 en las pp. 55-56).
