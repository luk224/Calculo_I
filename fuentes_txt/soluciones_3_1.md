# Unidad 3.1 — El Teorema de Taylor: derivadas sucesivas, polinomio de Taylor, resto y aproximaciones

**Ejercicios:** E 3.1-3.14 (E pp. 88-100; página impresa = PDF). El enunciado de 3.14 está en E p. 99 y su solución termina en E p. 100.
**Teoría:** U §3.1 «El Teorema de Taylor», pp. 104-112 (PDF 102-110): 3.1.1 Motivación p. 104, 3.1.2 Derivadas sucesivas pp. 104-106, 3.1.3 El Teorema de Taylor pp. 107-112. U no tiene ejercicios de autoevaluación propios de §3.1. Los de todo el Tema 3 están en U p. 139, y los n.º 1 y 2 son de esta unidad (los resuelvo como ejemplos propios A3 y B0).
**Fuera de esta unidad:** E 3.15-3.17 (sucesiones de funciones, fuera de examen) y E 3.18-3.20 (series de Taylor, unidad 3.2).

**Avisos de extracción (comprobados renderizando el PDF de E con PyMuPDF).** En `ejercicios.txt` se pierden símbolos. En 3.3 la función es $f(x)=\sqrt{|x|}$, no $|x|$: el `.txt` pierde la raíz. En 3.4 y 3.6 las ramas dicen $x\neq 0$, y en 3.8 aparece «$f'(0)=2\neq-6$»: el `.txt` pierde la barra de $\neq$. Esos fallos vienen de la extracción, no son erratas de E. Las erratas reales de E están en la sección (c) del final.

## Orden de estudio recomendado (se mantiene la numeración de E)

| Bloque | Ejercicios (orden de estudio) | Herramienta de U |
|---|---|---|
| A. Derivadas sucesivas | 3.2 → 3.1 → 3.3 → 3.4 → 3.6 → 3.5 | U §3.1.2 pp. 104-106; reglas de derivación U §2.1-2.2 pp. 75-81; L'Hôpital U §2.3.2 p. 82 |
| B. Polinomio de Taylor | 3.7 → 3.11 → 3.10 → 3.9 → 3.8 → 3.13 | U Def. 3.1, Prop. 3.1, Def. 3.2 pp. 107-108; Ej. 3.4-3.9 pp. 107-110; recuadro p. 112 |
| C. Resto de Lagrange y cotas de error | 3.14 → 3.12 | U Prop. 3.2 (Teorema de Taylor) y Def. 3.3 p. 111; Ej. 3.10 pp. 111-112 |

**Notación de U que usamos.** $f^{(n}(x)$ es la derivada $n$-ésima; U escribe el paréntesis sin cerrar, $f^{(4}$, y así lo hace también E. $p_n$ es el polinomio de Taylor de **orden** $n$, es decir, de grado $\le n$. $R_n(x)=f(x)-p_n(x)$ es el resto.

---

# BLOQUE A — Derivadas sucesivas

**Idea.** La derivada $f'$ es otra función, y se puede volver a derivar. Así se obtienen $f''$, $f'''$, $f^{(4}$, … (U §3.1.2 p. 104). Para calcularlas se aplican **las mismas reglas de siempre**, una y otra vez. En los puntos «problemáticos» (donde cambia la fórmula, o donde hay un $0/0$) hay que usar la **definición** de derivada, aplicada a la función que se esté derivando en ese momento ($f$, luego $f'$, …).

## Ejercicio 3.2 (E p. 88)

> Sea $f:\mathbb R\to\mathbb R$ la función definida por $f(x)=3x^2-x+1$. Entonces se cumple:
> a) $f^{(4}(x)=(f(x))^4$. b) $f^{(4}(x)=0$. c) $f^{(4}(x)$ no existe. d) Ninguna de las anteriores.

**Solución.**
1. **Leer bien la notación.** $f^{(4}$ es la derivada cuarta, es decir, derivar cuatro veces (U §3.1.2 p. 104). **No** es la potencia $(f(x))^4$. Esto descarta a).
2. **¿Existe?** $f$ es un polinomio. La derivada de un polinomio es otro polinomio (U Prop. 2.1 p. 79 y la tabla de derivadas), y los polinomios son derivables en todo $\mathbb R$. Por tanto todas las derivadas sucesivas existen en todo $\mathbb R$, y c) es falsa.
3. **Calcularla.** Cada derivada baja el grado en una unidad:
   $f'(x)=6x-1$, $f''(x)=6$, $f'''(x)=0$, $f^{(4}(x)=0$.
4. **Conclusión:** la respuesta es **b)**.

**Respuesta a la pregunta que deja E.** Si $p(x)=a_nx^n+\dots$ tiene grado $n$, entonces $p^{(n}(x)=n!\,a_n$, que es una constante, y $p^{(k}\equiv 0$ para $k\ge n+1$. Aquí $f''=2!\cdot 3=6$.

**Receta.** Polinomio de grado $n$: su derivada $n$-ésima es $n!$ por el coeficiente principal, y todas las siguientes son $0$. «Es $0$» no significa «no existe».
**Error típico.** Pensar que, como $f'''=0$, las derivadas de orden mayor «no tienen sentido». Sí lo tienen: la derivada de la función nula es la función nula (U, nota al margen del Ej. 3.1, p. 105).
**Teoría:** U §3.1.2 pp. 104-105 (Ej. 3.1).

## Ejercicio 3.1 (E p. 88)

> Calcula la derivada tercera de la función $f(x)=\operatorname{sen}\!\left(x^2+\frac{\pi}{5}\right)$.

**Solución.** Escribimos $u=x^2+\frac{\pi}{5}$, de modo que $u'=2x$.
1. **Primera derivada** (regla de la cadena, U p. 79: $(\operatorname{sen}u)'=\cos u\cdot u'$):
   $$f'(x)=2x\cos\!\left(x^2+\tfrac{\pi}{5}\right).$$
2. **Segunda derivada.** $f'$ es el **producto** de $2x$ por $\cos u$, así que aplicamos la regla del producto (U Prop. 2.1 p. 79) y, dentro, otra vez la cadena, con $(\cos u)'=-\operatorname{sen}u\cdot 2x$:
   $$f''(x)=2\cos u+2x\cdot(-2x\operatorname{sen}u)=2\cos\!\left(x^2+\tfrac{\pi}{5}\right)-4x^2\operatorname{sen}\!\left(x^2+\tfrac{\pi}{5}\right).$$
3. **Tercera derivada.** Derivamos cada sumando por separado:
   - $(2\cos u)'=-2\operatorname{sen}u\cdot 2x=-4x\operatorname{sen}u$.
   - $(-4x^2\operatorname{sen}u)'=-8x\operatorname{sen}u-4x^2\cos u\cdot 2x=-8x\operatorname{sen}u-8x^3\cos u$ (producto y cadena).
4. **Agrupar** los términos semejantes: $-4x\operatorname{sen}u-8x\operatorname{sen}u=-12x\operatorname{sen}u$. Queda
   $$\boxed{f'''(x)=-12x\operatorname{sen}\!\left(x^2+\tfrac{\pi}{5}\right)-8x^3\cos\!\left(x^2+\tfrac{\pi}{5}\right)}$$
   Coincide con E. Verificado con sympy: la diferencia simplifica a $0$.

**Receta.** Derivar por etapas, escribiendo cada derivada completa y agrupada antes de volver a derivar, y aplicar en cada sumando las reglas del producto y de la cadena. Llamar $u$ a la función interior ahorra errores.
**Error típico.** Olvidar el factor $u'=2x$ de la cadena en la segunda y la tercera derivada, o derivar $2x\cos u$ como si fuera $2\cdot(\cos u)'$, sin la regla del producto.
**Teoría:** U §3.1.2 p. 104 (Ej. 3.2 p. 105, que es del mismo tipo); regla de la cadena y del producto, U §2.2 p. 79.

## Ejercicio 3.3 (E pp. 89-90)

> Señale la opción correcta relativa a la función dada por $f(x)=\sqrt{|x|}$.
> a) $f'$ es positiva en $(-\infty,0)$. b) $f'$ es positiva en $\mathbb R$. c) $f$ es derivable en $\mathbb R$. d) $f''$ es negativa en $(-\infty,0)\cup(0,+\infty)$.

(En `ejercicios.txt` aparece como «$f(x)=|x|$» porque la extracción pierde la raíz. El PDF dice $\sqrt{|x|}$.)

**Solución.**
1. **Quitar el valor absoluto** usando su definición (U §1.1): $f(x)=\sqrt{x}$ si $x\ge 0$, y $f(x)=\sqrt{-x}$ si $x<0$.
2. **Derivada fuera de $0$.** En $(0,\infty)$ y en $(-\infty,0)$, $f$ coincide con una función derivable, así que aplicamos la regla de la cadena (U p. 79):
   $$f'(x)=\frac{1}{2\sqrt x}\ (x>0),\qquad f'(x)=\frac{1}{2\sqrt{-x}}\cdot(-1)=\frac{-1}{2\sqrt{-x}}\ (x<0).$$
   Por tanto $f'<0$ en $(-\infty,0)$, y a) y b) son **falsas**.
3. **Derivada en $0$.** En $0$ cambia la fórmula, así que las reglas no sirven y hay que usar derivadas laterales (U Def. 2.3 p. 81):
   $$f'(0^+)=\lim_{h\to0^+}\frac{\sqrt h-0}{h}=\lim_{h\to0^+}\frac{1}{\sqrt h}=+\infty,\qquad f'(0^-)=\lim_{h\to0^-}\frac{\sqrt{-h}}{h}=\lim_{h\to0^-}\frac{-1}{\sqrt{-h}}=-\infty.$$
   En la segunda hemos usado que, si $h<0$, entonces $h=-(-h)=-\sqrt{-h}\sqrt{-h}$. Los límites no son finitos, así que $f$ **no es derivable en $0$** (U Def. 2.1 p. 75 exige un límite finito), y c) es falsa. La gráfica tiene en $0$ un «pico» con tangente vertical.
4. **Segunda derivada fuera de $0$.** Para $x>0$, $f'(x)=\tfrac12x^{-1/2}$, luego $f''(x)=-\tfrac14x^{-3/2}<0$. Para $x<0$, $f'(x)=-\tfrac12(-x)^{-1/2}$, luego $f''(x)=-\tfrac12\cdot(-\tfrac12)(-x)^{-3/2}\cdot(-1)=-\tfrac14(-x)^{-3/2}<0$.
5. **Conclusión:** la respuesta es **d)**. Verificado con sympy.

**Receta.** Con valor absoluto o con funciones a trozos: (i) se reescribe por trozos; (ii) se deriva con las reglas en el interior de cada trozo; (iii) en los puntos de unión se usan derivadas laterales, y solo hay derivada si son **finitas e iguales**.
**Error típico.** Concluir que «$f'(0)$ existe» porque $f$ es continua en $0$. La continuidad es necesaria para la derivabilidad, pero no suficiente (U Teorema 2.1 p. 76). Tampoco hay que olvidar el signo $-1$ que da la cadena al derivar $\sqrt{-x}$.
**Teoría:** U §2.1 Def. 2.1 p. 75, Def. 2.3 p. 81; U §3.1.2 p. 104.

## Ejercicio 3.4 (E pp. 90-91)

> Para la función dada por $f(x)=\dfrac{x^2-1}{x}$ si $x\neq0$, y $f(0)=0$, calcula la derivada primera y la derivada segunda de $f$ en todos los puntos de $\mathbb R$ en que sea posible.

**Solución.**
1. **Si $x\ne0$**, $f$ es un cociente de polinomios cuyo denominador no se anula, así que es derivable y podemos usar la regla del cociente (U Prop. 2.1 p. 79):
   $$f'(x)=\frac{2x\cdot x-(x^2-1)\cdot1}{x^2}=\frac{x^2+1}{x^2}=1+\frac1{x^2}.$$
   Es más cómodo usar la forma simplificada $f(x)=x-\frac1x$, de la que sale $f'(x)=1+x^{-2}$ y, derivando otra vez, $f''(x)=-2x^{-3}=-\dfrac{2}{x^3}$.
2. **En $x=0$: comprobar primero la continuidad**, porque si $f$ no es continua en $0$ tampoco es derivable (U Teorema 2.1 p. 76):
   $$\lim_{x\to0^+}\Big(x-\frac1x\Big)=-\infty,\qquad \lim_{x\to0^-}\Big(x-\frac1x\Big)=+\infty.$$
   El límite no existe, así que $f$ no es continua en $0$ y, por tanto, **no existe $f'(0)$**.
3. **$f''(0)$ tampoco existe.** Para derivar $f'$ en $0$ haría falta que $f'(0)$ estuviera definida, y no lo está.
4. **Comprobación con la definición** (la hace E): $\dfrac{f(h)-f(0)}{h}=\dfrac{h^2-1}{h^2}=1-\dfrac1{h^2}\to-\infty$ cuando $h\to0$. No es finito. Verificado con sympy.

**Resultado:** $f'(x)=\dfrac{x^2+1}{x^2}$ y $f''(x)=-\dfrac2{x^3}$ para $x\ne0$. Ninguna de las dos existe en $0$.

**Receta.** Antes de usar la definición en un punto conflictivo, comprobar si $f$ es continua ahí. Si no lo es, se acaba: no hay derivada, ni primera ni de ningún orden superior.
**Error típico.** Derivar la fórmula $\frac{x^2+1}{x^2}$ y «evaluarla en $0$», o creer que $f'(0)$ existe porque el valor $f(0)=0$ está definido.
**Teoría:** U Teorema 2.1 p. 76; Prop. 2.1 p. 79; §3.1.2 p. 104.

## Ejercicio 3.6 (E pp. 92-93)

> Sea $f$ la función dada por $f(x)=\dfrac{e^x-1}{x}$ si $x\neq0$, y $f(0)=1$. Calcula las derivadas primera y segunda de $f$ en todos los puntos de $\mathbb R$ en los que sea posible.

**Solución.**
1. **$f'$ para $x\ne0$** (regla del cociente, U p. 79):
   $$f'(x)=\frac{e^x\cdot x-(e^x-1)\cdot1}{x^2}=\frac{xe^x-e^x+1}{x^2}.$$
2. **$f'(0)$ por la definición.** En $0$ la fórmula no vale, porque la función está definida aparte:
   $$f'(0)=\lim_{h\to0}\frac{\frac{e^h-1}{h}-1}{h}=\lim_{h\to0}\frac{e^h-1-h}{h^2}.$$
   Al sustituir $h=0$ sale $\frac00$. Numerador y denominador son derivables y $2h\ne0$ para $h\ne0$ cerca de $0$, así que podemos aplicar la regla de L'Hôpital (U §2.3.2 p. 82):
   $$\lim_{h\to0}\frac{e^h-1-h}{h^2}\overset{\text{L'H}}{=}\lim_{h\to0}\frac{e^h-1}{2h}\overset{\text{L'H}}{=}\lim_{h\to0}\frac{e^h}{2}=\frac12.$$
   Por tanto $f'(0)=\tfrac12$, y $f$ es derivable en todo $\mathbb R$.
3. **$f''$ para $x\ne0$.** Derivamos el cociente del paso 1. El numerador $N=xe^x-e^x+1$ tiene derivada $N'=e^x+xe^x-e^x=xe^x$:
   $$f''(x)=\frac{xe^x\cdot x^2-(xe^x-e^x+1)\cdot2x}{x^4}=\frac{x^2e^x-2xe^x+2e^x-2}{x^3}.$$
   En el último paso hemos dividido numerador y denominador entre $x$, lo que se puede hacer porque $x\ne0$.
4. **$f''(0)$ por la definición, aplicada a $f'$** (ahora la función que derivamos es $f'$, con $f'(0)=\tfrac12$):
   $$f''(0)=\lim_{h\to0}\frac{f'(h)-\frac12}{h}=\lim_{h\to0}\frac{2he^h-2e^h+2-h^2}{2h^3}\quad\Big(\tfrac00\Big).$$
   Aplicamos L'Hôpital. La derivada del numerador es $2e^h+2he^h-2e^h-2h=2he^h-2h$, y la del denominador, $6h^2$:
   $$=\lim_{h\to0}\frac{2h(e^h-1)}{6h^2}=\lim_{h\to0}\frac{e^h-1}{3h}\overset{\text{L'H}}{=}\lim_{h\to0}\frac{e^h}{3}=\frac13.$$
   (En el paso intermedio solo hemos simplificado $h$, que es $\ne0$; eso no es L'Hôpital.)
5. **Resultado:** $f'(0)=\frac12$ y $f''(0)=\frac13$, con las fórmulas anteriores para $x\ne0$. $f$ es dos veces derivable en todo $\mathbb R$.

**Comprobación con Taylor** (usa U Ej. 3.6 pp. 108-109). Como $e^x=1+x+\frac{x^2}{2}+\frac{x^3}{6}+\dots$, se tiene $\frac{e^x-1}{x}=1+\frac{x}{2}+\frac{x^2}{6}+\dots$. Eso sugiere $f'(0)=\frac12$ y $\frac{f''(0)}{2!}=\frac16$, es decir, $f''(0)=\frac13$. Coincide. Verificado con sympy: los límites de los pasos 2 y 4 valen $\frac12$ y $\frac13$, y también $\lim_{x\to0}f'(x)=\tfrac12$ y $\lim_{x\to0}f''(x)=\tfrac13$, así que $f'$ y $f''$ son continuas.

**Receta.** Para una función definida aparte en un punto $a$: calcular $f'(a)$ con el cociente incremental y resolver el $\frac00$ con L'Hôpital. Para $f''(a)$ se repite **con $f'$** y el valor $f'(a)$ que acabamos de obtener.
**Error típico.** Calcular $f''(0)$ como $\lim_{x\to0}f''(x)$ usando la fórmula de $x\ne0$. Aquí da el mismo número, pero eso no es la definición y en general no está justificado. También es un error aplicar L'Hôpital sin comprobar antes que el límite es de tipo $\frac00$.
**Teoría:** U §2.1 Def. 2.1 p. 75; U §2.3.2 p. 82; U §3.1.2 p. 104.

## Ejercicio 3.5 (E pp. 91-92)

> La altura de un objeto en función del tiempo viene dada por una función $f$. Se sabe que la gráfica de $f'$ es *(figura de E p. 91: para $t\ge0$ es un segmento de $(0,0)$ a $(1,1)$ y, desde $t=1$, una curva que sale horizontal y crece cada vez más deprisa hasta $\approx7$ en $t\approx4{,}5$)*. ¿Qué puedes decir con respecto a la posición, la velocidad y la aceleración del objeto?

**Solución.** Si $f$ es la posición (altura), entonces $f'$ es la velocidad y $f''$ es la aceleración (U §2.1, interpretación física de la derivada).
1. **Velocidad ($f'$, se lee directamente en la gráfica).** Vale $0$ en $t=0$ y es $>0$ para $t>0$. Además es creciente: cuanto más tarde, más rápido va el objeto.
2. **Posición ($f$).** Como $f'(t)>0$ en $(0,\infty)$, $f$ es estrictamente creciente, es decir, el objeto sube (U Prop. 2.4 p. 98). Como $f'$ es creciente, $f$ es **convexa** (U Prop. 3.9 p. 136, que anticipa §3.5): sube cada vez más deprisa.
3. **Aceleración ($f''$ = pendiente de la gráfica de $f'$).**
   - En $(0,1)$ la gráfica es un segmento de pendiente $\frac{1-0}{1-0}=1$, luego $f''(t)=1$ (aceleración constante).
   - En $t=1$ las derivadas laterales de $f'$ son distintas: $f''(1^-)=1$ y $f''(1^+)=0$, porque la curva sale horizontal. Por tanto **$f''(1)$ no existe** (U Def. 2.3 p. 81), igual que en U Ej. 3.3 p. 106. La gráfica de $f'$ tiene un «pico» en $t=1$.
   - Para $t>1$ la pendiente crece desde $0$, así que la aceleración es positiva y creciente.
4. **Interpretación** (la da E): un cohete que cambia de propulsor en $t=1$.

**Precisión sobre E.** E dice «la velocidad es siempre positiva». Según la figura, $f'(0)=0$, así que lo exacto es «positiva para $t>0$». Además la gráfica solo da información para $t\ge0$ (la parte $t<0$ no está dibujada).

**Receta.** Posición → velocidad → aceleración es $f\to f'\to f''$. En la gráfica de $f'$: el signo de $f'$ indica si $f$ sube o baja, y la pendiente de $f'$ es $f''$. Donde la gráfica de $f'$ tiene un pico, no existe $f''$.
**Error típico.** Confundir la gráfica dada (la de $f'$) con la de $f$, y decir «la altura crece linealmente hasta $t=1$». Es la **velocidad** la que crece linealmente ahí.
**Teoría:** U §2.1 (derivada como tasa de cambio), Prop. 2.4 p. 98; U §3.1.2 pp. 104-106 (Ej. 3.3).

### Ejemplos propios del Bloque A

**A1 (propio, fácil).** Halla una fórmula para $f^{(n}(x)$ si $f(x)=xe^x$.
*Solución.* Calculamos las primeras: $f'=e^x+xe^x=(x+1)e^x$, $f''=e^x+(x+1)e^x=(x+2)e^x$, $f'''=(x+3)e^x$. Aparece el patrón $f^{(n}(x)=(x+n)e^x$. Se prueba por inducción: si $f^{(n}=(x+n)e^x$, entonces $f^{(n+1)}=e^x+(x+n)e^x=(x+n+1)e^x$. Verificado con sympy para $n=1,\dots,6$.

**A2 (propio, medio).** Halla $f^{(n}(x)$ si $f(x)=\dfrac1{1+x}$.
*Solución.* Escribimos $f=(1+x)^{-1}$. Entonces $f'=-(1+x)^{-2}$, $f''=2(1+x)^{-3}$ y $f'''=-6(1+x)^{-4}$. Cada derivada baja el exponente en $1$ y multiplica por él, que es negativo, así que el signo va alternando:
$$f^{(n}(x)=\frac{(-1)^n\,n!}{(1+x)^{n+1}}.$$
Verificado con sympy para $n\le6$. (Este resultado se usa en el Bloque C con $\ln(1+x)$, cuya derivada es precisamente $\frac1{1+x}$.)

**A3 (propio, difícil; es la autoevaluación n.º 1 de U p. 139).** ¿Es cierto que una función puede ser continua y tener derivada continua y, aun así, no tener derivada segunda?
*Solución.* **Sí.** Tomemos $g(x)=x|x|$, es decir, $g(x)=x^2$ si $x\ge0$ y $g(x)=-x^2$ si $x<0$.
- Fuera de $0$: $g'(x)=2x$ si $x>0$ y $g'(x)=-2x$ si $x<0$, es decir, $g'(x)=2|x|$.
- En $0$: $\frac{g(h)-g(0)}{h}=\frac{h|h|}{h}=|h|\to0$, luego $g'(0)=0=2|0|$.

Por tanto $g'(x)=2|x|$ en todo $\mathbb R$, y es continua. Pero $\frac{g'(h)-g'(0)}{h}=\frac{2|h|}{h}$ tiende a $2$ por la derecha y a $-2$ por la izquierda, así que **no existe $g''(0)$**. Es la misma situación que en U Ej. 3.3 pp. 105-106.

---

# BLOQUE B — El polinomio de Taylor

**Idea** (U §3.1.3 pp. 107-108). Queremos un polinomio que «imite» a $f$ cerca de un punto $x_0$. Le pedimos que tenga, **en $x_0$**, el mismo valor que $f$ y las mismas derivadas que $f$ hasta el orden $n$. La Prop. 3.1 (U p. 108) dice que un polinomio queda determinado por sus derivadas en $x_0$. Por tanto hay **un único** polinomio de grado $\le n$ que cumple eso, y es
$$p_n(x)=f(x_0)+f'(x_0)(x-x_0)+\frac{f''(x_0)}{2!}(x-x_0)^2+\dots+\frac{f^{(n}(x_0)}{n!}(x-x_0)^n\qquad\text{(U (3.1), Def. 3.2, p. 108)}.$$
Si $x_0=0$ se llama polinomio de Mac Laurin (U p. 108). Hay dos hechos que se usan mucho:
- **Coeficiente $k$-ésimo** = $\dfrac{f^{(k}(x_0)}{k!}$. Por tanto, a partir de los coeficientes se leen las derivadas, y al revés: $f^{(k}(x_0)=k!\cdot(\text{coeficiente de }(x-x_0)^k)$.
- **Centrar** un polinomio en $x_0$ (U Def. 3.1 p. 107) consiste en escribirlo en potencias de $(x-x_0)$. Se hace sustituyendo $x=(x-x_0)+x_0$ y desarrollando (U Ej. 3.4 p. 107).

## Ejercicio 3.7 (E p. 93)

> Razona si es cierto o falso que el polinomio de Taylor centrado en $x_0$ de orden $n$ de una función $f$ es un polinomio de grado $n$.

**Solución.**
1. Por la definición (U (3.1) p. 108), el término de mayor potencia de $p_n$ es $\frac{f^{(n}(x_0)}{n!}(x-x_0)^n$.
2. Si $f^{(n}(x_0)\neq0$, ese término no se anula y el grado es exactamente $n$. Si $f^{(n}(x_0)=0$, ese término desaparece y el grado es **menor** que $n$.
3. **Contraejemplo:** $f(x)=\cos x$, $x_0=0$, $n=1$. Como $f(0)=1$ y $f'(0)=-\operatorname{sen}0=0$, se tiene $p_1(x)=1$, que tiene grado $0$, no $1$. Otro, de U Ej. 3.7 p. 109: para $\operatorname{sen}x$, $p_2=p_1=x$ tiene grado $1$.
4. **Conclusión: FALSO.** Lo correcto es «grado **menor o igual** que $n$». Por eso U dice «de **orden** $n$» y no «de grado $n$».

**Receta.** «Orden $n$» significa que se usan las derivadas hasta la $n$; el grado es el de la última derivada **no nula** en $x_0$.
**Error típico.** Tomar «orden» como sinónimo de «grado». Ojo: S p. 755 dice «polinomial de grado $n$», lo cual es impreciso (ver sección (b)).
**Teoría:** U Def. 3.2 p. 108; Ej. 3.7 p. 109.

## Ejercicio 3.11 (E pp. 96-97)

> Razona si es cierto o falso que el polinomio de Taylor centrado en $x_0$ de un polinomio $P(x)$ coincide con el polinomio $P(x)$.

**Solución.**
1. **Tal como está enunciado (sin decir el orden), es FALSO.** Contraejemplo: $P(x)=x^2$, $x_0=0$, orden $1$. Como $P(0)=0$ y $P'(0)=0$, se tiene $p_1(x)=0\neq x^2$.
2. **Cuándo sí es cierto: si el orden $n$ es mayor o igual que el grado $m$ de $P$.** El porqué, con U:
   - Por la Prop. 3.1 (U p. 108), $P(x)=\sum_{i=0}^{m}\frac{P^{(i}(x_0)}{i!}(x-x_0)^i$, que es exactamente $p_m$.
   - Para $i>m$ se tiene $P^{(i}\equiv0$ (Ej. 3.2 de E), así que añadir términos de orden $m+1,\dots,n$ suma ceros: $p_n=p_m=P$.
   - Otra forma, con el Teorema de Taylor (U Prop. 3.2 p. 111): $R_n(x)=\frac{P^{(n+1}(c)}{(n+1)!}(x-x_0)^{n+1}=0$ porque $P^{(n+1}\equiv0$ si $n\ge m$. Por tanto $P=p_n$.
3. **Si $n<m$**, $p_n$ es el polinomio que se obtiene al escribir $P$ centrado en $x_0$ y **quedarse con las potencias $\le n$**. Es lo que dice el recuadro de U p. 112: para $f(x)=x^5+3x^4-x^2+1$, $p_3(x)=-x^2+1$.

**Aviso sobre E.** E dice que es cierto «si los dos polinomios tienen el mismo grado» y que «el resto de Lagrange verifica $R_{n+1}(x)=0$». Lo preciso es: cierto si **el orden $n\ge\operatorname{grado}P$**, y el resto que se anula es **$R_n$**, porque depende de $P^{(n+1}\equiv0$. Además, $p_n$ puede tener grado menor que $n$ (Ej. 3.7), así que «mismo grado» no es la condición adecuada.

**Receta.** Taylor de un polinomio de grado $m$ en $x_0$: se centra en $x_0$ y se trunca en la potencia $n$. Si $n\ge m$, se obtiene el propio polinomio.
**Error típico.** Olvidar el orden y responder «sí, siempre».
**Teoría:** U Prop. 3.1 p. 108; recuadro de U p. 112; U Prop. 3.2 p. 111.

## Ejercicio 3.10 (E p. 96)

> Sea $P(x)$ el polinomio dado por $P(x)=x^3-x^2+x-2$. Escríbelo en función de potencias enteras no negativas de $(x-1)$ utilizando el polinomio de Taylor.

**Solución.**
1. **Por qué funciona.** $P$ tiene grado $3$, así que por el Ej. 3.11 (U Prop. 3.1 p. 108) $P=p_3$, su polinomio de Taylor de orden $3$ centrado en $1$.
2. **Derivadas en $x_0=1$:**
   $P(1)=1-1+1-2=-1$; $P'(x)=3x^2-2x+1$, luego $P'(1)=2$; $P''(x)=6x-2$, luego $P''(1)=4$; $P'''(x)=6$, luego $P'''(1)=6$.
3. **Coeficientes** $\frac{P^{(k}(1)}{k!}$: $-1,\ 2,\ \frac42=2,\ \frac66=1$. Por tanto
   $$\boxed{P(x)=-1+2(x-1)+2(x-1)^2+(x-1)^3.}$$
4. **Comprobación por el otro método** (U Ej. 3.4 p. 107). Con $t=x-1$, es decir $x=t+1$:
   $(t+1)^3-(t+1)^2+(t+1)-2=(t^3+3t^2+3t+1)-(t^2+2t+1)+t+1-2=t^3+2t^2+2t-1$. Coincide. Verificado con sympy: la diferencia es $0$.

**Receta.** Para recentrar un polinomio hay dos caminos: (a) usar los coeficientes $\frac{P^{(k}(x_0)}{k!}$; (b) sustituir $x=(x-x_0)+x_0$ y desarrollar. Conviene usar uno y comprobar con el otro.
**Error típico.** Olvidar dividir entre $k!$ (poner $4(x-1)^2$ en vez de $2(x-1)^2$).
**Teoría:** U Def. 3.1 y Ej. 3.4 p. 107; Prop. 3.1 p. 108.
*(Detalle de E: dice «en el ejercicio anterior hemos visto que para órdenes superiores a 3 el polinomio de Taylor coincidirá…», pero eso se ve en el 3.11, que va **después**, y en U p. 112.)*

## Ejercicio 3.9 (E p. 95)

> Calcula el polinomio de Taylor de orden 3 centrado en 0 de la función dada por $f(x)=\ln(x^2+1)$.

**Solución.**
1. **Derivadas** (cadena y cociente, U p. 79):
   - $f'(x)=\dfrac{2x}{x^2+1}$.
   - $f''(x)=\dfrac{2(x^2+1)-2x\cdot2x}{(x^2+1)^2}=\dfrac{2-2x^2}{(x^2+1)^2}$.
   - $f'''(x)=\dfrac{-4x(x^2+1)^2-(2-2x^2)\cdot2(x^2+1)\cdot2x}{(x^2+1)^4}$. Simplificamos un factor $(x^2+1)$: $\dfrac{-4x(x^2+1)-4x(2-2x^2)}{(x^2+1)^3}=\dfrac{4x(x^2-3)}{(x^2+1)^3}$.
2. **Evaluar en $0$:** $f(0)=\ln1=0$, $f'(0)=0$, $f''(0)=2$, $f'''(0)=0$.
3. **Polinomio:** $p_3(x)=0+0\cdot x+\frac{2}{2!}x^2+\frac{0}{3!}x^3=\boxed{x^2}$. Tiene grado $2$ aunque el orden es $3$ (ver 3.7).
4. **Comprobación sin derivar** (idea de U Ej. 3.9 p. 110, sustituir en un desarrollo conocido). En el Bloque C (Ej. 3.14) se ve que $\ln(1+u)\approx u-\frac{u^2}{2}+\dots$. Con $u=x^2$ queda $x^2-\frac{x^4}{2}+\dots$, y la parte de grado $\le3$ es $x^2$. Verificado con sympy: la serie es $x^2-\frac{x^4}{2}+O(x^6)$ y $f'''$ coincide.

**Por qué salen ceros:** $f$ es **par** ($f(-x)=f(x)$), y las derivadas de orden impar de una función par derivable son impares, así que valen $0$ en $0$. Por eso solo aparecen potencias pares.
**Receta.** Tabla de dos columnas «$f^{(k}(x)$ | $f^{(k}(x_0)$», simplificando cada derivada antes de derivar la siguiente; después, coeficientes $\frac{f^{(k}(x_0)}{k!}$.
**Error típico.** No simplificar $f''$ antes de derivarla (las cuentas explotan), o dar como resultado «$p_3=x^2+0x^3$ tiene grado 3».
**Teoría:** U Def. 3.2 p. 108; Ej. 3.9 p. 110.

## Ejercicio 3.8 (E pp. 94-95)

> De una función $f$ se sabe que es dos veces derivable y que $f'(0)=2$ y $f''(-3)=6$. ¿Puede ser alguno de los siguientes polinomios un polinomio de Taylor de orden 2 centrado en 0 de $f$? ¿Y centrado en $-3$?
> a) $1-x+\dfrac{x^2}{2}$. b) $\pi^2+(x-3)^2$. c) $2x+3(x+3)^2$.

**Idea.** El polinomio de Taylor de orden 2 centrado en $a$ es $f(a)+f'(a)(x-a)+\frac{f''(a)}{2}(x-a)^2$. Por tanto:
- **centrado en $0$**, el coeficiente de $x$ tiene que ser $f'(0)=2$;
- **centrado en $-3$**, el coeficiente de $(x+3)^2$ tiene que ser $\frac{f''(-3)}{2}=3$.

No conocemos $f(0)$, $f''(0)$, $f(-3)$ ni $f'(-3)$, así que los demás coeficientes pueden ser cualesquiera. «Puede ser» significa «no contradice los datos».

**Lema útil (propio).** Al recentrar un polinomio de grado $2$, el coeficiente del término de grado $2$ **no cambia**. En efecto, si $x-a=(x-b)+(b-a)$, entonces $\alpha(x-a)^2=\alpha(x-b)^2+2\alpha(b-a)(x-b)+\alpha(b-a)^2$: el cuadrado conserva el coeficiente $\alpha$, y los términos de grado menor no aportan nada a $(x-b)^2$.

**Solución.**
1. **a)** Está centrado en $0$ y el coeficiente de $x$ es $-1\neq2$, así que **no** es de $f$ en $0$. Centrado en $-3$: por el lema, el coeficiente de $(x+3)^2$ es $\frac12\neq3$, así que **no**. Si se desarrolla con $x=(x+3)-3$, sale $\frac{17}{2}-4(x+3)+\frac12(x+3)^2$, y se confirma.
2. **b)** Centrado en $0$: $\pi^2+(x-3)^2=(\pi^2+9)-6x+x^2$, y el coeficiente de $x$ es $-6\neq2$, así que **no**. Centrado en $-3$: por el lema, el coeficiente de $(x+3)^2$ es $1\neq3$, así que **no**.
3. **c)** Centrado en $-3$: $2x=2(x+3)-6$, luego $2x+3(x+3)^2=-6+2(x+3)+3(x+3)^2$. El coeficiente de $(x+3)^2$ es $3=\frac{6}{2}$. **Sí puede serlo**, con $f(-3)=-6$ y $f'(-3)=2$, que no contradicen nada. Centrado en $0$: $2x+3(x^2+6x+9)=27+20x+3x^2$, y el coeficiente de $x$ es $20\neq2$, así que **no**.
4. **Resumen:** solo c), y solo centrado en $-3$. Verificado con sympy.

**Moraleja** (la da E): el polinomio de Taylor es una aproximación **local**. Los polinomios de la misma función centrados en puntos distintos son, en general, distintos.
**Receta.** Para decidir si un polinomio es el de Taylor de $f$ en $a$: escribirlo en potencias de $(x-a)$ y comparar cada coeficiente con $\frac{f^{(k}(a)}{k!}$ **solo donde conozcamos $f^{(k}(a)$**.
**Error típico.** Comparar coeficientes sin haber recentrado antes. Por ejemplo, decir que en c) «el coeficiente de $x$ es $2$» y concluir que vale en $0$, cuando al desarrollar $3(x+3)^2$ también aparecen términos en $x$.
**Teoría:** U Def. 3.1 y Ej. 3.4 p. 107; Def. 3.2 p. 108.

## Ejercicio 3.13 (E pp. 98-99)

> Sabiendo que el polinomio de Taylor centrado en $-1$ de orden 3 de $g(x)=e^x$ es $p(x)=e^{-1}\left(1+(x+1)+\frac{(x+1)^2}{2!}+\frac{(x+1)^3}{3!}\right)$, obtén $p_3(x)$, el polinomio de Taylor de orden 3 centrado en el mismo punto de las funciones dadas por $f(x)=x+e^x$ y $h(x)=(x+1)e^x$.

**Solución.** Usaremos dos propiedades (las enuncia E; U no las demuestra, ver sección (b)):
- **(S) Suma:** el polinomio de Taylor de orden $n$ de $f+g$ es la suma de los de $f$ y $g$. **Porqué, con U:** $(f+g)^{(k}=f^{(k}+g^{(k}$ (U Prop. 2.1 p. 79, aplicada $k$ veces), así que los coeficientes $\frac{(f+g)^{(k}(a)}{k!}$ se suman.
- **(P) Producto:** el de $f\cdot g$ es el producto de los dos polinomios **truncado** en el grado $n$.

1. **$f(x)=x+e^x$.** El polinomio de orden 3 de $j(x)=x$ en $-1$ es la propia $j$ recentrada: $x=-1+(x+1)$. Por (S):
   $$p_3^f(x)=-1+(x+1)+e^{-1}\Big(1+(x+1)+\tfrac{(x+1)^2}{2}+\tfrac{(x+1)^3}{6}\Big)$$
   $$\boxed{p_3^f(x)=(e^{-1}-1)+(1+e^{-1})(x+1)+\frac{e^{-1}}{2}(x+1)^2+\frac{e^{-1}}{6}(x+1)^3.}$$
2. **$h(x)=(x+1)e^x$.** El polinomio de $x+1$ es él mismo. Por (P) multiplicamos y quitamos lo de grado $>3$:
   $$(x+1)\,p(x)=e^{-1}\Big((x+1)+(x+1)^2+\tfrac{(x+1)^3}{2}+\tfrac{(x+1)^4}{6}\Big)\ \Longrightarrow\ \boxed{p_3^h(x)=e^{-1}\Big((x+1)+(x+1)^2+\tfrac{(x+1)^3}{2}\Big).}$$
3. **Comprobación rigurosa derivando** (esto sí usa solo U, Def. 3.2):
   - Para $f$: $f'=1+e^x$, $f''=f'''=e^x$. En $-1$: $f=-1+e^{-1}$, $f'=1+e^{-1}$, $f''=f'''=e^{-1}$. Los coeficientes son $e^{-1}-1,\ 1+e^{-1},\ \frac{e^{-1}}{2},\ \frac{e^{-1}}{6}$. ✓
   - Para $h$: como en el ejemplo propio A1, $h^{(k}(x)=(x+1+k)e^x$. En $-1$: $h=0$, $h'=e^{-1}$, $h''=2e^{-1}$, $h'''=3e^{-1}$. Los coeficientes son $0,\ e^{-1},\ \frac{2e^{-1}}{2}=e^{-1},\ \frac{3e^{-1}}{6}=\frac{e^{-1}}{2}$. ✓

   Verificado con sympy (serie en $-1$): coinciden los dos.

**ERRATA de E (p. 99).** En la última línea del cálculo de $f$, E escribe
$-1+e^{-1}+(1+e^{-1})(x+1)+e^{-1}\big((x+1)^2+\frac{(x+1)^3}{2!}+\frac{(x+1)^4}{3!}\big)$.
Ese paréntesis es el de $h$ (copiado por error): aparece un término de grado 4, que no puede estar en un polinomio de orden 3, y los coeficientes son incorrectos. Lo correcto es $e^{-1}\big(\frac{(x+1)^2}{2}+\frac{(x+1)^3}{6}\big)$. Además, en el caso de $h$ E escribe «$h(x)p(x)$» donde debería decir «$j(x)p(x)$».

**Receta.** Para funciones construidas con otras cuyo Taylor ya conocemos: sumar polinomios (suma), multiplicarlos y truncar (producto), o sustituir (U Ej. 3.9 p. 110). Después se comprueba al menos un coeficiente derivando.
**Error típico.** No truncar (dejar el término $(x+1)^4$), o truncar antes de multiplicar y perder términos.
**Teoría:** U Def. 3.2 p. 108; Ej. 3.9 p. 110 (composición); reglas de U Prop. 2.1 p. 79.

### Ejemplos propios del Bloque B

**B0 (propio, fácil; es la autoevaluación n.º 2 de U p. 139).** ¿Se puede calcular el polinomio de Taylor de orden 2 de $f(x)=|x|$ en el origen?
*Solución.* **No.** La Def. 3.2 (U p. 108) necesita $f'(0)$ y $f''(0)$, y $f'(0)$ no existe: el cociente $\frac{|h|}{h}$ vale $1$ por la derecha y $-1$ por la izquierda (derivadas laterales $f'(0^+)=1\neq f'(0^-)=-1$, U Def. 2.3 p. 81).

**B1 (propio, fácil).** Polinomio de Mac Laurin de orden 4 de $\cos x$.
*Solución.* Las derivadas son $\cos x,-\operatorname{sen}x,-\cos x,\operatorname{sen}x,\cos x$, que en $0$ valen $1,0,-1,0,1$. Queda $p_4(x)=1-\frac{x^2}{2}+\frac{x^4}{24}$. Como $f^{(5}(0)=-\operatorname{sen}0=0$, también $p_5=p_4$. Verificado con sympy.

**B2 (propio, medio).** Polinomio de Taylor de orden 2 de $f(x)=\sqrt x$ centrado en $4$.
*Solución.* $f(4)=2$. $f'(x)=\frac1{2\sqrt x}$, luego $f'(4)=\frac14$. $f''(x)=-\frac1{4x^{3/2}}$, luego $f''(4)=-\frac1{32}$, y su coeficiente es $-\frac1{32}\cdot\frac1{2!}=-\frac1{64}$. Queda
$$p_2(x)=2+\frac{x-4}{4}-\frac{(x-4)^2}{64}.$$
Verificado con sympy. Se usa en C2.

**B3 (propio, difícil).** Polinomio de Mac Laurin de orden 3 de $e^x\operatorname{sen}x$ y de orden 4 de $e^{-x^2}$.
*Solución.* (i) Producto truncado: $(1+x+\frac{x^2}{2}+\frac{x^3}{6})(x-\frac{x^3}{6})=x+x^2+\big(\frac12-\frac16\big)x^3+\dots$. Por tanto $p_3=x+x^2+\frac{x^3}{3}$. Lo comprobamos derivando: $f'=e^x(\operatorname{sen}x+\cos x)$, luego $f'(0)=1$; $f''=2e^x\cos x$, luego $f''(0)=2$ y $\frac22=1$; $f'''=2e^x(\cos x-\operatorname{sen}x)$, luego $f'''(0)=2$ y $\frac26=\frac13$. ✓
(ii) Sustitución (como en U Ej. 3.9): en $1+u+\frac{u^2}{2}$ ponemos $u=-x^2$, y sale $p_4=1-x^2+\frac{x^4}{2}$. Verificado con sympy.

---

# BLOQUE C — El resto de Lagrange y las cotas de error

**Idea** (U §3.1.3 p. 111). $p_n$ aproxima a $f$, pero ¿cuánto nos equivocamos? El **Teorema de Taylor** (U Prop. 3.2 p. 111) da el error **exacto**, aunque en él aparece un punto $c$ desconocido:
$$R_n(x)=f(x)-p_n(x)=\frac{f^{(n+1}(c)}{(n+1)!}(x-x_0)^{n+1},\qquad c\text{ entre }x_0\text{ y }x\qquad\text{(resto de Lagrange, U Def. 3.3 p. 111).}$$
No conocemos $c$, pero sí el intervalo en el que está. Por eso **acotamos** $|f^{(n+1}(c)|$ por su valor más grande posible en ese intervalo. Con $n=0$ se obtiene el teorema del valor medio (U p. 96): $f(x)-f(x_0)=f'(c)(x-x_0)$.

**Método en 4 pasos** (el mismo de U Ej. 3.10 pp. 111-112):
1. Calcular $p_n$ y $f^{(n+1}$.
2. Escribir $R_n(x)$ con $c$ entre $x_0$ y $x$.
3. Acotar $|f^{(n+1}(c)|\le M$ para **todo** $c$ posible, buscando el caso peor.
4. Obtener $|R_n(x)|\le\frac{M}{(n+1)!}|x-x_0|^{n+1}$, y despejar lo que pidan ($n$, $x$ o la cota).

## Ejercicio 3.14 (E pp. 99-100)

> Encuentra valores de $x\ge0$ para los que se pueda asegurar que es válida la aproximación $\ln(1+x)\approx x-\dfrac{x^2}{2}+\dfrac{x^3}{3}$ con un error en valor absoluto menor de $0.0001$.

**Solución.**
1. **¿Es un polinomio de Taylor?** Para $f(x)=\ln(1+x)$, $f'(x)=\frac1{1+x}$, y por el ejemplo propio A2, $f^{(k}(x)=\frac{(-1)^{k-1}(k-1)!}{(1+x)^k}$. En $0$: $f(0)=0$, $f'(0)=1$, $f''(0)=-1$, $f'''(0)=2$. Por tanto
   $$p_3(x)=x-\frac{x^2}{2}+\frac{2}{3!}x^3=x-\frac{x^2}{2}+\frac{x^3}{3},$$
   que es justo el polinomio del enunciado. Así que el error es $R_3$.
2. **Resto de Lagrange** ($n=3$, $x_0=0$). Las hipótesis se cumplen porque $f^{(4}(x)=-\frac{6}{(1+x)^4}$ es continua en $(-1,\infty)$. Entonces
   $$R_3(x)=\frac{f^{(4}(c)}{4!}x^4=\frac{-6}{24(1+c)^4}x^4=-\frac{x^4}{4(1+c)^4},\qquad c\in(0,x).$$
3. **Acotar (caso peor en $c$).** Como $c>0$, se tiene $(1+c)^4>1$, luego $\frac1{(1+c)^4}<1$ y
   $$|R_3(x)|<\frac{x^4}{4}.$$
   Aquí se ve por qué el enunciado pide $x\ge0$: si $x<0$, $c$ puede estar cerca de $-1$ y la cota se dispara.
4. **Despejar.** Basta que $\frac{x^4}{4}\le10^{-4}$, es decir, $x^4\le4\cdot10^{-4}$, es decir, $x\le(4\cdot10^{-4})^{1/4}=\sqrt2\cdot10^{-1}$. (Comprobación: $(\sqrt2/10)^4=4/10^4$.)
5. **Conclusión:** para $x\in\left[0,\frac{\sqrt2}{10}\right]\approx[0,\;0{,}1414]$ el error es **menor** que $10^{-4}$ (en $x=0$ es nulo). Verificado con sympy: en $x=\sqrt2/10$ el error real es $\approx8{,}99\cdot10^{-5}<10^{-4}$.

**Qué significa (lo subraya E).** Es un intervalo en el que **podemos garantizarlo** con esta cota, no «el» intervalo exacto. De hecho, numéricamente el error sigue siendo $<10^{-4}$ hasta $x\approx0{,}1453$ (con sympy). La cota es conservadora porque hemos cambiado $\frac1{(1+c)^4}$ por $1$.
**Receta.** Para «¿para qué $x$ vale la aproximación con error $<\varepsilon$?»: (1) comprobar que es $p_n$; (2) escribir $R_n$; (3) acotar $|f^{(n+1}(c)|$ por una constante, **independiente de $c$**; (4) resolver $\frac{M}{(n+1)!}|x-x_0|^{n+1}<\varepsilon$.
**Error típico.** Tomar $c=0$ o $c=x$ «porque sí», o dejar la cota dependiendo de $c$. $c$ es desconocido, así que hay que acotar para **todos** los valores posibles.
**Teoría:** U Prop. 3.2 y Def. 3.3 p. 111; Ej. 3.10 pp. 111-112.

## Ejercicio 3.12 (E pp. 97-98)

> Sea $f$ la función dada por $f(x)=\ln(\cos x)$. Se pide determinar $p_3(x)$, el polinomio de Maclaurin de orden 3, y encontrar una cota del error cometido en valor absoluto si se aproxima $f(x)$ por el polinomio $p_3(x)$ en el intervalo $(-1,1)$.

**Solución.**
1. **Dominio.** En $(-1,1)$ se tiene $\cos x\ge\cos1>0$ (porque $1<\frac\pi2$), así que $f$ y todas sus derivadas están definidas y son continuas. Se cumplen las hipótesis de U Prop. 3.2.
2. **Derivadas** (cadena, U p. 79):
   - $f'(x)=\frac{-\operatorname{sen}x}{\cos x}=-\operatorname{tg}x$.
   - $f''(x)=-\frac1{\cos^2x}$.
   - $f'''(x)=-\frac{2\operatorname{sen}x}{\cos^3x}$.
   - $f^{(4}(x)=-2\,\frac{\cos x\cos^3x+\operatorname{sen}x\cdot3\cos^2x\operatorname{sen}x}{\cos^6x}=-2\,\frac{\cos^2x+3\operatorname{sen}^2x}{\cos^4x}=-2\,\frac{3-2\cos^2x}{\cos^4x}$, usando $\operatorname{sen}^2=1-\cos^2$.
3. **En $0$:** $f(0)=\ln1=0$, $f'(0)=0$, $f''(0)=-1$, $f'''(0)=0$. Por tanto $\boxed{p_3(x)=-\tfrac12x^2}$.
4. **Resto:** $R_3(x)=\frac{f^{(4}(c)}{4!}x^4$, con $c$ entre $0$ y $x$. Entonces
   $$|R_3(x)|=\frac{x^4}{12}\cdot\frac{3-2\cos^2c}{\cos^4c}.$$
   (El numerador es $\ge1>0$, así que el valor absoluto no cambia nada.)
5. **Caso peor en $c$.** Llamemos $u=\cos^2c$. Como $|c|<|x|<1$ y $\cos$ es par y decreciente en $[0,1]$, se tiene $u\in(\cos^21,\,1]$. La función $g(u)=\frac{3-2u}{u^2}$ es **decreciente** en ese intervalo, porque al crecer $u$ el numerador (positivo) baja y el denominador sube. Por tanto $g(u)<g(\cos^21)$: el caso peor es $\cos c$ **lo más pequeño posible**, es decir, $c$ cerca de $\pm1$.
6. **Cota:** con $x^4<1$,
   $$|R_3(x)|<\frac{3-2\cos^21}{12\cos^41}\approx 2{,}363\qquad\text{para todo }x\in(-1,1).$$
   Verificado con sympy. Es una cota válida, pero muy pesimista: el error real máximo en $(-1,1)$ es $|\ln\cos1+\frac12|\approx0{,}116$.

**ERRATA de E (p. 98).** El primer paso de E es correcto:
$|R_3|\le\frac{x^4}{12}\cdot\frac{3-2\cos^21}{\cos^41}$.
Pero después escribe $|R_3|\le\frac{x^4}{12}\cdot\frac{|2\cos^20-3|}{\cos^41}\le\frac1{12}\cdot\frac{|2-3|}{\cos^41}\approx0{,}97785$. Eso **no es una cota válida**. Al poner $\cos^2c=\cos^20=1$ en el numerador $3-2\cos^2c$, se toma su valor **mínimo** ($=1$), no el máximo ($3-2\cos^21\approx2{,}416$). Es decir, E usa el caso mejor en el numerador y el peor en el denominador, y eso no acota nada. La cota que se deduce correctamente es $\approx2{,}363$. (Que el error real, $\approx0{,}116$, quede por debajo de $0{,}978$ es casualidad: el razonamiento no lo prueba.) Además, la nota al margen de E p. 97 dice «para $c<|x-x_0|$»; lo correcto es «**$c$ entre $x_0$ y $x$**».
**Receta.** Al acotar un cociente $\frac{A(c)}{B(c)}$ con $A,B>0$, hay que usar **a la vez** el máximo de $A$ y el mínimo de $B$, en el mismo intervalo de $c$. Si $A$ y $B$ dependen de la misma cantidad ($\cos^2c$), lo más seguro es estudiar la función $g(u)$ completa.
**Error típico.** El de E: acotar el numerador por abajo. También, olvidar que $c$ recorre **todo** el intervalo entre $0$ y $x$.
**Teoría:** U Prop. 3.2 y Def. 3.3 p. 111; Ej. 3.10 pp. 111-112.

### Ejemplos propios del Bloque C

**C0 (propio: el truco de U Ej. 3.10, pp. 111-112).** U quiere $\operatorname{sen}\frac12$ con error $<0{,}001$ y termina usando $n=4$, con la cota $|R_4|\le\frac{(1/2)^5}{5!}\approx0{,}00026$. Pero $p_4=p_3=x-\frac{x^3}{6}$, porque $f^{(4}(0)=\operatorname{sen}0=0$. Así que **el mismo polinomio $p_3$** tiene dos restos válidos, $R_3$ y $R_4$, y podemos usar el menor. Da $p_3(\frac12)=0{,}479166\ldots$ frente a $\operatorname{sen}\frac12=0{,}4794255\ldots$ (error real $2{,}6\cdot10^{-4}$). Verificado con sympy.
**Receta:** si $f^{(n+1}(x_0)=0$, entonces $p_n=p_{n+1}$ y conviene usar el resto $R_{n+1}$, que tiene una potencia más.

**C1 (propio, fácil).** Aproxima $e^{0{,}1}$ con $p_3$ de $e^x$ en $0$ y acota el error.
*Solución.* $p_3(0{,}1)=1+0{,}1+0{,}005+0{,}000166\ldots=1{,}1051667$. $R_3=\frac{e^c}{4!}(0{,}1)^4$ con $c\in(0;0{,}1)$. Como $e^c<e^{0{,}1}<2$, se tiene $|R_3|<\frac{2\cdot10^{-4}}{24}\approx8{,}3\cdot10^{-6}$. Valor real: $e^{0{,}1}=1{,}1051709$, con un error de $4{,}3\cdot10^{-6}$, dentro de la cota. Verificado con sympy.

**C2 (propio, medio).** Aproxima $\sqrt{4{,}1}$ con el $p_2$ de B2 y acota el error.
*Solución.* $p_2(4{,}1)=2+\frac{0{,}1}{4}-\frac{0{,}01}{64}=2{,}02484375$. La derivada tercera es $f'''(x)=\frac{3}{8x^{5/2}}$. Con $c\in(4;4{,}1)$ se tiene $c^{5/2}>4^{5/2}=32$, luego $f'''(c)<\frac{3}{256}$ (el caso peor es el extremo **izquierdo**, porque $f'''$ decrece). Entonces $|R_2|<\frac{3/256}{3!}(0{,}1)^3\approx1{,}95\cdot10^{-6}$. Valor real: $\sqrt{4{,}1}=2{,}0248457$, con un error de $1{,}92\cdot10^{-6}$, justo por debajo de la cota. Verificado con sympy.

**C3 (propio, medio-difícil).** ¿Qué orden $n$ hace falta para calcular $\sqrt e=e^{1/2}$ con $p_n$ de $e^x$ en $0$ y un error $<10^{-3}$?
*Solución.* $|R_n(\frac12)|=\frac{e^c}{(n+1)!}\left(\frac12\right)^{n+1}$ con $c\in(0,\frac12)$, y $e^c<e^{1/2}<2$. La cota $\frac{2}{(n+1)!\,2^{n+1}}$ vale $0{,}0052$ para $n=3$ (no basta) y $0{,}00052$ para $n=4$ (basta). Con $n=4$: $p_4(\frac12)=\frac{211}{128}=1{,}6484375$. Valor real: $\sqrt e=1{,}6487213$, con un error de $2{,}8\cdot10^{-4}$. Verificado con sympy.

**C4 (propio, difícil).** ¿Para qué $x\ge0$ se puede asegurar que $\cos x\approx1-\frac{x^2}{2}$ con error $<10^{-4}$?
*Solución.* El polinomio es $p_2=p_3$, porque $f'''(0)=\operatorname{sen}0=0$ (truco C0).
- Con $R_2=\frac{\operatorname{sen}c}{3!}x^3$ y $|\operatorname{sen}c|\le1$ saldría $x^3/6<10^{-4}$, es decir, $x<0{,}0843$.
- Con $R_3=\frac{\cos c}{4!}x^4$ y $|\cos c|\le1$: $\frac{x^4}{24}<10^{-4}$, es decir, $x<(24\cdot10^{-4})^{1/4}\approx0{,}2213$. Es **mucho mejor**.

Respuesta: $0\le x<0{,}2213$. Comprobado con sympy: el error real alcanza $10^{-4}$ en $x\approx0{,}2214$, así que la cota es casi óptima.

---

## (a) Teoría necesaria (U; páginas impresas verificadas en `ingenieros.txt` y, donde el `.txt` pierde símbolos, en las páginas renderizadas con PyMuPDF)

**De unidades anteriores (U Tema 2):**
- **Def. 2.1** (derivable en $a$: el cociente incremental tiene límite **finito**), U p. 75. **Teorema 2.1** (derivable $\Rightarrow$ continua), U p. 76.
- **Prop. 2.1** (derivada de suma, producto y cociente) y **Regla de la cadena**, U p. 79. Tabla de derivadas, U pp. 79-80.
- **Def. 2.3** (derivadas laterales; $f'(a)$ existe si y solo si las laterales existen y coinciden), U p. 81.
- **Regla de L'Hôpital**, U §2.3.2 p. 82. **Teorema del valor medio**, U p. 96 (es el caso $n=0$ del Teorema de Taylor). **Prop. 2.4** (signo de $f'$ y monotonía), U p. 98.

**U §3.1 El Teorema de Taylor (pp. 104-112):**
- **3.1.1 Motivación**, p. 104.
- **3.1.2 Derivadas sucesivas**, pp. 104-106: definición de $f''$, $f'''$, $f^{(n}$ y notación $f^{(n}(x)=\frac{d^nf}{dx^n}(x)$ (al margen, p. 104). **Ej. 3.1** ($3x^3$, y la nota de que las derivadas nulas «existen»), p. 105. **Ej. 3.2** ($xe^{x^2}$), p. 105. **Ej. 3.3** (función a trozos $x^2$ / $x^3$: $f'(0)=0$ pero no existe $f''(0)$), pp. 105-106, con figura en p. 106. Al margen de p. 106: los espacios $C(a,b)$, $C^1(a,b)$, …
- **3.1.3 El Teorema de Taylor**, pp. 107-112:
  - **Def. 3.1** (polinomio centrado en $x_0$) y **Ej. 3.4** (recentrar sustituyendo $x=(x-x_0)+x_0$), p. 107.
  - **Prop. 3.1** (todo polinomio de orden $n$ es igual a $\sum_{i=0}^n\frac{p^{(i}(x_0)}{i!}(x-x_0)^i$), p. 108. **Ej. 3.5**, p. 108.
  - **Fórmula (3.1) y Def. 3.2** (polinomio de Taylor de orden $n$; si $x_0=0$, «de Mac Laurin»), p. 108.
  - **Ej. 3.6** ($e^x$, $p_n=\sum x^i/i!$), pp. 108-109. **Ej. 3.7** ($\operatorname{sen}x$, $p_{2n+1}=p_{2n+2}$), p. 109. **Ej. 3.8** ($\operatorname{sen}x$ en $\pi/4$), p. 110. **Ej. 3.9** ($e^{x^2}$ por sustitución), p. 110.
  - **Prop. 3.2 (Teorema de Taylor)**, p. 111: si $f^{(n+1}$ está definida y es continua en $(a,b)$ y $x_0\in[a,b]$, entonces para $x\in(a,b)$, $R_n(x)=f(x)-p_n(x)=\frac{f^{(n+1}(c)}{(n+1)!}(x-x_0)^{n+1}$ con $c$ entre $x_0$ y $x$.
  - **Def. 3.3 (resto de Lagrange de orden $n$)**, p. 111.
  - **Ej. 3.10** ($\operatorname{sen}\frac12$ con error $<0{,}001$, fórmula (3.2) de la cota), pp. 111-112. Figura de $\operatorname{sen}x$, $p_3$, $p_5$, p. 112.
  - **Recuadro** (Taylor de un polinomio = sus monomios de grado $\le n$), p. 112.
- **Anticipos del Tema 3 usados en 3.5:** Prop. 3.9 ($f'$ creciente $\Leftrightarrow$ $f$ convexa), U p. 136. **Autoevaluación del Tema 3**, U p. 139 (los n.º 1 y 2 son de esta unidad; U no da las soluciones).

**Qué dice U sobre la forma del resto, y qué NO incluye.** U solo da la **forma de Lagrange** (Def. 3.3 p. 111) y añade: «Existen otras expresiones de este mismo resto con nombre propio pero no las consideraremos aquí» (p. 111). No da la forma integral ni la de Cauchy, ni la forma de Peano $R_n(x)=o\big((x-x_0)^n\big)$. Tampoco demuestra el teorema. Además:
- **Notaciones de Landau ($o$, $O$).** No están en U. En el índice del PDF de U (PDF p. 4, junto a la entrada 3.1) hay una anotación añadida al margen (sale en `ingenieros.txt`): «tmb cae: notaciones de Landau (tras estudiar el polinomio de Taylor), y la forma de Lagrange en interpolación polinómica están en el Aula Virtual». Coincide con el cronograma: es material del curso virtual, que **no tenemos**. Puente propio que sí se puede justificar con U: si $|f^{(n+1}|\le M$ cerca de $x_0$, entonces $|R_n(x)|\le\frac{M}{(n+1)!}|x-x_0|^{n+1}$, luego $\frac{R_n(x)}{(x-x_0)^n}\to0$. Es decir, $f(x)=p_n(x)+o\big((x-x_0)^n\big)$ (forma de Peano). Esto es lo que justifica las reglas de suma y producto de E 3.13 y la unicidad del desarrollo. **Hay que avisarlo como material externo a U.**
- **Forma de Lagrange del error de interpolación** ($f(x)-p_n(x)=\frac{f^{(n+1}(\xi)}{(n+1)!}\prod(x-x_i)$). **No está en U §3.3** (pp. 119-124). Lo he comprobado: en §3.3 no aparece ninguna fórmula de error. Pertenece a la unidad 3.3 del resumen y también es material del Aula Virtual.
- **Hipótesis de la Prop. 3.2 de U.** Pide $f^{(n+1}$ continua en $(a,b)$. Si $x_0$ fuera un extremo del intervalo, haría falta además que $f^{(n}$ fuese continua en $x_0$. En todos los ejercicios $x_0$ es interior, así que no afecta. L (Teorema 9.19 p. 642) solo exige que $f$ sea derivable hasta el orden $n+1$ en un intervalo $I$ que contenga a $c$.

## (b) Huecos de U y dónde suplirlos (páginas impresas verificadas)

Correspondencia de páginas comprobada. **S:** en estos capítulos, PDF = impresa + 33 (p. 250 = PDF 283; p. 753 = PDF 786; p. 768 = PDF 801), por la cabecera de la página en el PDF. **L:** PDF = impresa + 17 (p. 636 = PDF 653).

| Hueco en U | Dónde suplirlo |
|---|---|
| **Intuición**: por qué igualar derivadas en $x_0$ da un buen ajuste (recta tangente → parábola → …) | **S Proyecto de laboratorio «Polinomios de Taylor»**, pp. 256-257: construye la aproximación cuadrática imponiendo $P(a)=f(a)$, $P'(a)=f'(a)$, $P''(a)=f''(a)$ con $\cos x$, y deduce $c_k=f^{(k}(a)/k!$ (problema 5). **L §9.7** pp. 636-638: Ej. 1 (grado 1 para $e^x$, p. 636), Ej. 2 (tabla $P_3$ frente a $e^x$, p. 637), deducción de los coeficientes y definición, p. 638. |
| **Aproximación lineal = Taylor de orden 1** (U no lo relaciona) | **S §3.10** «Aproximaciones lineales y diferenciales», pp. 250-253: linealización $L(x)=f(a)+f'(a)(x-a)$ (pp. 250-251), Ej. 1 ($\sqrt{x+3}$ en $a=1$, p. 251), Ej. 2 (¿para qué $x$ se tiene una precisión dada?, p. 252, método gráfico). **S §11.11 p. 768**: «$T_1$ es lo mismo que la linealización de $f$ en $a$ que estudiamos en la sección 3.10». |
| **Cómo mejora la aproximación al subir $n$ y al acercarse a $x_0$** (U solo da una figura) | **L §9.7 Ej. 7** p. 641 (tablas de $\ln(1{,}1)$ y conclusiones 1 y 2). **S §11.11** pp. 768-769 (tabla $T_n(0{,}2)$ y $T_n(3)$ para $e^x$). |
| **Más ejemplos de cálculo de $p_n$** | **L §9.7** Ej. 3 ($e^x$, p. 638), Ej. 4 ($\ln x$ en $c=1$, p. 639), Ej. 5 ($\cos x$, p. 640), Ej. 6 ($\operatorname{sen}x$ en $\pi/6$, p. 640; es gemelo de U Ej. 3.8). |
| **Acotar el error: método sistemático y ejemplos** (U solo tiene el Ej. 3.10) | **L Teorema 9.19** (Teorema de Taylor, forma de Lagrange) y la consecuencia $|R_n|\le\frac{|x-c|^{n+1}}{(n+1)!}\max|f^{(n+1}(z)|$, p. 642. **L Ej. 8** ($\operatorname{sen}0{,}1$ con $P_3$ y cota, p. 643) y **Ej. 9** (grado necesario para $\ln1{,}2$ con error $<0{,}001$, p. 643; es gemelo de C3). **S Desigualdad de Taylor** (Teorema 11.10.9, p. 756). **S §11.11 Ej. 1** ($\sqrt[3]x$ en $8$, error en $[7,9]$, pp. 769-770) y **Ej. 2** ($\operatorname{sen}x$ con $|x|\le0{,}3$ y $\operatorname{sen}12^\circ$, pp. 770-771; lo compara con el método gráfico, p. 771). |
| **Otras formas del resto** (U las omite) | **S nota al margen p. 756** «Fórmulas para el residuo de Taylor»: forma integral y forma de Lagrange («generalización del teorema del valor medio»). **L p. 642**: «para $n=0$ … es el teorema del valor medio». |
| **Aplicaciones en física e ingeniería** (motivación) | **S §11.11** «Aplicaciones en la física», pp. 772-774 (relatividad especial, Ej. 3, p. 772; óptica). |
| **Suma, producto y sustitución de polinomios de Taylor** (las usa E 3.13; U solo tiene la sustitución, Ej. 3.9) | U no las demuestra. S las trata con **series** («Multiplicación y división de series de potencias», S §11.10 p. 763; es de la unidad 3.2). Para 3.1 basta con comprobar derivando, como en 3.13, o con el puente de Peano de la sección (a). |
| **Aviso de terminología** | **S p. 755** dice «$T_n$ es una polinomial de **grado** $n$»; U y E 3.7 aclaran que el grado es $\le n$. L p. 638 habla de «polinomio **n-ésimo** de Taylor». Gana U: «**orden** $n$». |

Ejercicios adicionales recomendables: **L §9.7**, pp. 644-646; **S §11.11**, pp. 774-776 (p. ej. el ej. 23 de p. 775: estimar $\cos80^\circ$).

## (c) Erratas, omisiones y avisos

**Erratas reales de E:**
1. **E 3.12 (p. 98): cota del error incorrecta.** Al acotar $\frac{3-2\cos^2c}{\cos^4c}$, E sustituye $\cos^2c$ por $\cos^20=1$ en el numerador, que es el **mínimo** del numerador, y obtiene $\approx0{,}97785$. No es una cota demostrada. La cota correcta por este camino es $\frac{3-2\cos^21}{12\cos^41}\approx2{,}363$. El error real máximo en $(-1,1)$ es $\approx0{,}116$.
2. **E 3.12 (nota al margen, p. 97):** «para $c<|x-x_0|$». Debe decir «**$c$ entre $x_0$ y $x$**».
3. **E 3.13 (p. 99), polinomio de $f=x+e^x$:** el último paréntesis $e^{-1}\big((x+1)^2+\frac{(x+1)^3}{2!}+\frac{(x+1)^4}{3!}\big)$ es el de $h$, copiado por error. Lo correcto es $e^{-1}\big(\frac{(x+1)^2}{2}+\frac{(x+1)^3}{6}\big)$. Tampoco puede haber un término de grado 4 en un polinomio de orden 3.
4. **E 3.13 (p. 99):** «$h(x)p(x)=(x+1)e^{-1}(\dots)$» debería ser «$j(x)p(x)$».
5. **E 3.11 (p. 97):** «$R_{n+1}(x)=0$» debe ser **$R_n(x)=0$**. Además, la condición «los dos polinomios tienen el mismo grado» es imprecisa: lo correcto es «orden $n\ge$ grado de $P$».
6. **E 3.10 (p. 96):** «en el ejercicio anterior hemos visto que para órdenes superiores a 3 el polinomio de Taylor coincidirá con el de orden 3». Eso no se ve en el 3.9, sino en el 3.11 (posterior) y en U p. 112.
7. **E 3.3 (nota al margen, p. 89):** en la definición de derivada escribe $\frac{f(a+h)-f(x)}{h}$ (tres veces). Debe ser $f(a+h)-f(a)$.
8. **E 3.5 (p. 91):** «la velocidad es siempre positiva». En la figura $f'(0)=0$: es positiva para $t>0$.

**Solo de extracción (no son erratas):** en 3.3, $\sqrt{|x|}$ aparece como $|x|$; en 3.4, 3.6 y 3.8 se pierde la barra de $\neq$.

**Pequeñas erratas de U (por si el redactor cita esos pasajes):**
- U Ej. 3.3 pp. 105-106: en $f''(0^+)$ (p. 106) falta el signo «=», y en $f'(0^+)$ (p. 105) y $f''(0^+)$ el límite dice $x\to0^+$ en vez de $h\to0^+$.
- U Ej. 3.10 p. 111: dice «Utilizando la **Propiedad** 3.2»; es la **Proposición** 3.2.
- U Prop. 3.1 p. 108: «polinomio de orden $n$» debe entenderse como «de grado $\le n$».

## (d) Figuras que vale la pena recortar (con `herramientas/extraer_figura.py`; páginas **PDF**)

He comprobado los recortes de U y E renderizándolos. Para S y L, `list` detecta los pies de figura indicados (salvo donde se indica).

| Libro | Pág. PDF (impresa) | Pie / contenido | Uso en el resumen | Comando sugerido |
|---|---|---|---|---|
| U | 104 (p. 106) | Sin pie. Gráficas de $f$ ($x^2$ / $x^3$) y de $f'$, con el «pico» de $f'$ en $0$ (Ej. 3.3) | Bloque A: derivada segunda que no existe | `crop U 104 "150,400,515,645" fig_u_3_ej33` |
| U | 110 (p. 112) | Sin pie. «$f(x)=\operatorname{sen}x$ y sus polinomios de Taylor centrados en el origen de orden 3 y 5» | Intuición de Taylor; más orden, mejor ajuste | `crop U 110 "175,350,485,540" fig_u_3_sen_p3_p5` |
| E | 89 | Gráfica de $\sqrt{\lvert x\rvert}$ (Ej. 3.3) | Ej. 3.3 (opcional) | `crop E 89 "135,525,425,635" fig_e_3_3` |
| E | 91 | Gráfica de $f'$ (Ej. 3.5) | Enunciado de 3.5 (**imprescindible**) | `crop E 91 "180,276,375,434" fig_e_3_5` |
| S | 283 (p. 250) | «FIGURA 1» (la recta tangente como aproximación) | Orden 1 = linealización | `auto S 283 "FIGURA 1" fig_s_3_10_1` |
| S | 284 (p. 251) | «FIGURA 2» ($\sqrt{x+3}$ y su linealización) | Ídem | `auto S 284 "FIGURA 2" fig_s_3_10_2` |
| S | 788 (p. 755) | «FIGURA 1»: $e^x$ con $T_1,T_2,T_3$ | Intuición del polinomio de Taylor | `auto S 788 "FIGURA 1" fig_s_11_10_1` |
| S | 791 (p. 758) | «FIGURA 2»: $\operatorname{sen}x$ con $T_1,T_3,T_5$ | Alternativa a la de U p. 112 | `auto S 791 "FIGURA 2" fig_s_11_10_2` |
| S | 801 (p. 768) | «FIGURA 1»: $e^x$ y sus primeros polinomios de Taylor | Motivación (repite la de p. 755) | `auto S 801 "FIGURA 1" fig_s_11_11_1` |
| S | 803 (p. 770) | «FIGURA 2» ($\sqrt[3]x$ y $T_2$) y «FIGURA 3» ($\lvert R_2(x)\rvert$ en $[7,9]$) | Ver el error gráficamente (Bloque C) | `auto S 803 "FIGURA 3" fig_s_11_11_3` (y la 2) |
| S | 804 (p. 771) | «FIGURA 6»: $\operatorname{sen}x$ con $T_1,T_3,T_5,T_7$ (y las Fig. 4-5, $\lvert R_6\rvert$) | Ajuste en intervalos cada vez mayores | `auto S 804 "FIGURA 6" fig_s_11_11_6` |
| L | 653 (p. 636) | «Figura 9.10» y «Figura 9.11»: $P_1(x)=1+x$ frente a $e^x$ | Idea de «mismo valor y misma pendiente» | `auto L 653 "Figura 9.11" fig_l_9_11` |
| L | 654 (p. 637) | «Figura 9.12» ($P_2$ de $e^x$) y «Figura 9.13» ($P_3$ de $e^x$) | Mejora al subir el grado | `auto L 654 "Figura 9.12" fig_l_9_12` (la 9.13 con `page`/`crop`: `list` no detecta su pie) |
| L | 656 (p. 639) | «Figura 9.14» ($\ln x$ y sus polinomios de Taylor en $c=1$) | Taylor fuera del origen | `page L 656 …` y luego `crop` (`list` no detecta el pie) |
| L | 657 (p. 640) | «Figura 9.15» ($\cos x$ y $P_6$) y «Figura 9.16» ($\operatorname{sen}x$ y $P_3$ en $\pi/6$) | Gemelo de U Ej. 3.8 | `auto L 657 "Figura 9.15" fig_l_9_15`; la 9.16 con `page`/`crop` |

**Prioridad para el redactor:** E 91 (hace falta para el enunciado de 3.5), U 110, U 104, S 788 o L 654, y S 803 (Fig. 3) para ilustrar el resto. La de E 89 es opcional.
