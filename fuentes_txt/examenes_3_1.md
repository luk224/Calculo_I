# Problemas de examen real · Tema 3.1 Teorema de Taylor

Fuente **X** = *Exámenes resueltos de Cálculo* (`Examenes-resueltos-Calculo.pdf`). Las páginas son las del **PDF**. Enunciados y soluciones leídos como imagen (PyMuPDF, 110 dpi). Cálculos verificados con sympy (script en el scratchpad de la sesión).
Notación del resumen `temas/tema_3_1_taylor.html`: $p_n$ = polinomio de Taylor de orden $n$, $f^{(k}$ = derivada $k$-ésima, $R_n(x)=\dfrac{f^{(n+1}(c)}{(n+1)!}(x-x_0)^{n+1}$ con $c$ entre $x_0$ y $x$ (U Prop. 3.2 y Def. 3.3, p. 111).

Filas del índice con tema 3.1: X pp. 46, 70, 126-127, 129, 132, 135, 140, 145-146 y 147. Se han elegido 6, de fácil a difícil y sin repetir tipo. Las de pp. 135, 140 y 147 son del mismo tipo que el problema 3 y se resumen al final como variantes. Se descartan la serie de Taylor de p. 145 (1.ª parte, §3.2) y la de p. 142 (§3.2).

---

## Problema 1 · Escribir el resto de Lagrange

**Fuente:** `X p.46 (Septiembre 2014, Grado en Ing. Mecánica, Modelo A, pregunta corta 3, 1 punto)`

**Enunciado.** Sea $p_3(x)$ el polinomio de Taylor de orden 3, centrado en $x_0=0$, de la función $f:[-1,2]\to\mathbb{R}$, que es cuatro veces derivable con continuidad en $[-1,2]$. Indique la expresión del error cometido al aproximar $f$ por $p_3$ en un punto $x$ del intervalo $[-1,2]$.

**Solución.**
1. **Se comprueban las hipótesis.** $f$ es «cuatro veces derivable con continuidad», es decir, $f^{(4}$ existe y es continua en $[-1,2]$, y $x_0=0$ está dentro del intervalo. Son las hipótesis de la Proposición 3.2 de U con $n=3$ (se necesita la derivada de orden $n+1=4$ continua).
2. **Se define el error.** El error al aproximar $f(x)$ por $p_3(x)$ es el resto $R_3(x)=f(x)-p_3(x)$.
3. **Se aplica el Teorema de Taylor.** Para cada $x\in[-1,2]$ existe un $c$ entre $0$ y $x$ tal que
$$R_3(x)=\frac{f^{(4}(c)}{4!}(x-0)^4=\frac{f^{(4}(c)}{24}\,x^4 .$$
4. **Matiz.** $c$ depende de $x$ y no se conoce. Lo único que se sabe es que está entre $0$ y $x$ (si $x=0$, el error es $0$).

**Receta:** el error de $p_n$ es «el siguiente término del polinomio con la derivada evaluada en un $c$ desconocido»: $\dfrac{f^{(n+1}(c)}{(n+1)!}(x-x_0)^{n+1}$, con $c$ entre $x_0$ y $x$.
**Parte del tema:** §3 del resumen (Prop. 3.2 y Def. 3.3 de U, p. 111).
**Verificación:** es la fórmula del teorema; coincide con la solución impresa.
**Avisos:** ninguno. La solución impresa es correcta pero muy escueta: no comprueba las hipótesis ni dice que $c$ depende de $x$. Error típico: poner $f^{(3}$ o $3!$ (confundir el orden del polinomio con el del resto) o escribir $f^{(4}(x)$ o $f^{(4}(0)$ en lugar de $f^{(4}(c)$.

---

## Problema 2 · ¿Es compatible un polinomio con la recta tangente?

**Fuente:** `X pp.126-127 (sin fecha, I. Electrónica Industrial y Automática, examen que empieza en p. 126, pregunta corta 3, 1 punto)`

**Enunciado.** La recta tangente a la gráfica de la función $f(x)$, derivable en todo $\mathbb{R}$, en $(\pi^2,f(\pi^2))$ es $y=2(x-\pi^2)+1$. ¿Puede ser $p_2(x)=(x-\pi^2)^2+2\pi^2+1$ el polinomio de Taylor de $f$ en $x=\pi^2$ de orden 2? ¿Por qué?

**Solución.**
1. **Datos que da la tangente.** La recta tangente en $x_0$ es $y=f(x_0)+f'(x_0)(x-x_0)$ (U Def. 2.1 e interpretación geométrica, Tema 2). Comparando con $y=1+2(x-\pi^2)$, se obtiene $f(\pi^2)=1$ y $f'(\pi^2)=2$.
2. **Forma obligada de $p_2$.** Por definición,
$$p_2(x)=f(\pi^2)+f'(\pi^2)(x-\pi^2)+\frac{f''(\pi^2)}{2!}(x-\pi^2)^2 = 1+2(x-\pi^2)+\frac{f''(\pi^2)}{2}(x-\pi^2)^2 .$$
Es decir, $p_1$ **es** la recta tangente, y $p_2$ solo añade el término cuadrático.
3. **Se escribe el candidato en potencias de $(x-\pi^2)$.** $(x-\pi^2)^2+2\pi^2+1 = (2\pi^2+1)+0\cdot(x-\pi^2)+1\cdot(x-\pi^2)^2$. Ya lo está; hay que tener cuidado de no confundir la constante $2\pi^2+1$ con un término en $(x-\pi^2)$.
4. **Se comparan los coeficientes.** El término independiente debería ser $f(\pi^2)=1$, pero es $2\pi^2+1\ne1$. El coeficiente de $(x-\pi^2)$ debería ser $f'(\pi^2)=2$, pero es $0$. **Fallan dos coeficientes**, así que **no puede ser** el polinomio de Taylor.
5. **Lo que no se puede decidir.** El coeficiente de $(x-\pi^2)^2$ es $f''(\pi^2)/2$, que no viene en los datos. Por eso no se puede hallar $p_2$, aunque sí se sabe que tiene la forma $1+2(x-\pi^2)+a(x-\pi^2)^2$.

**Receta:** los coeficientes de orden 0 y 1 de cualquier $p_n$ son los de la recta tangente: si no coinciden con ella, el polinomio no es de Taylor.
**Parte del tema:** §2.2 del resumen (polinomio centrado en $x_0$, coeficientes $f^{(k}(x_0)/k!$; Bloque B, receta «compara cada coeficiente con $f^{(k}(a)/k!$ solo donde conozcas $f^{(k}(a)$»).
**Verificación:** comparación directa de coeficientes; no hay nada que calcular con sympy.
**Avisos:** la solución impresa solo señala el término independiente ($f(\pi^2)$ daría $2\pi^2+1$). No es un error, porque basta una contradicción, pero se le escapa que **también** falla el coeficiente lineal ($0\ne2$). Interesa señalarlo: el error típico es tomar $2\pi^2$ como si fuera «la parte lineal».

---

## Problema 3 · Polinomio de Taylor de orden 3 cuyo grado es 2

**Fuente:** `X p.132 (Septiembre 2017, I. Electrónica Industrial y Automática, pregunta corta 2, 1 punto)`

**Enunciado.** Calcule el polinomio de Taylor de orden 3 centrado en $x=\tfrac12$ para la función dada por $f(x)=\operatorname{sen}(\pi x)$.

**Solución.**
1. **Fórmula.** $p_3(x)=\displaystyle\sum_{k=0}^{3}\frac{f^{(k}(\tfrac12)}{k!}\left(x-\tfrac12\right)^k$ (U §3.1.3, pp. 107-110). Hacen falta $f,f',f'',f'''$ en $\tfrac12$.
2. **Derivadas** (regla de la cadena: cada derivada saca un factor $\pi$):
$f'(x)=\pi\cos(\pi x)$, $f''(x)=-\pi^2\operatorname{sen}(\pi x)$, $f'''(x)=-\pi^3\cos(\pi x)$.
3. **Tabla en $x_0=\tfrac12$** (allí $\pi x_0=\pi/2$, con $\operatorname{sen}\frac\pi2=1$ y $\cos\frac\pi2=0$):

| $k$ | $f^{(k}(\tfrac12)$ | $f^{(k}(\tfrac12)/k!$ |
|---|---|---|
| 0 | $1$ | $1$ |
| 1 | $0$ | $0$ |
| 2 | $-\pi^2$ | $-\pi^2/2$ |
| 3 | $0$ | $0$ |

4. **Polinomio:** $p_3(x)=1-\dfrac{\pi^2}{2}\left(x-\tfrac12\right)^2$.
5. **Interpretación.** El orden es 3 pero el grado es 2, porque $f'''(\tfrac12)=0$. Tiene sentido geométrico: en $x=\tfrac12$ la función alcanza su máximo, de modo que la tangente es horizontal y la curva es simétrica respecto a $x=\tfrac12$ (solo aparecen potencias pares). Además $p_2=p_3$, así que para acotar el error de este polinomio se podría usar $R_3$ en vez de $R_2$.

**Receta:** tabla «$k$ | $f^{(k}(x_0)$ | $f^{(k}(x_0)/k!$»; los ceros se escriben y se ven, y el grado es el de la última derivada no nula.
**Parte del tema:** §2 y Bloque B del resumen (receta «orden $n$ = derivadas hasta la $n$; el grado es el de la última no nula»).
**Verificación:** sympy: $p_3=1-\frac{\pi^2}{8}(2x-1)^2 = 1-\frac{\pi^2}{2}(x-\frac12)^2$. Coincide con la solución impresa.
**Avisos:** ninguno. Error típico: olvidar el factor $\pi$ de la regla de la cadena, o «completar» el polinomio hasta grado 3 inventando un término.

---

## Problema 4 · Del polinomio a las derivadas (problema inverso)

**Fuente:** `X p.129 (sin fecha, I. Electrónica Industrial y Automática, examen que empieza en p. 129, pregunta corta 2, 1 punto)`

**Enunciado.** Sabiendo que el polinomio de Taylor de $f(x)$ en $x=\pi$ de orden 4 es $p_4=\left[\frac{(x-\pi)}{4}+1\right](x-\pi)^2$, calcule $f(\pi)$, $f''(\pi)$, $f'''(\pi)$ y $f^{(iv}(\pi)$.

**Solución.**
1. **Forma general.** $p_4(x)=f(\pi)+f'(\pi)(x-\pi)+\dfrac{f''(\pi)}{2!}(x-\pi)^2+\dfrac{f'''(\pi)}{3!}(x-\pi)^3+\dfrac{f^{(4}(\pi)}{4!}(x-\pi)^4$.
2. **Se desarrolla el dato en potencias de $(x-\pi)$, sin expandir $x$.** $p_4=\frac14(x-\pi)^3+(x-\pi)^2$. Es decir, el coeficiente de $(x-\pi)^0$ es $0$, el de $(x-\pi)^1$ es $0$, el de $(x-\pi)^2$ es $1$, el de $(x-\pi)^3$ es $\frac14$ y el de $(x-\pi)^4$ es $0$.
3. **Se igualan los coeficientes.** Dos polinomios iguales, escritos en potencias de $(x-\pi)$, tienen los mismos coeficientes:
   - $f(\pi)=0$;
   - $\frac{f''(\pi)}{2}=1\Rightarrow f''(\pi)=2$;
   - $\frac{f'''(\pi)}{6}=\frac14\Rightarrow f'''(\pi)=\frac32$;
   - $\frac{f^{(4}(\pi)}{24}=0\Rightarrow f^{(4}(\pi)=0$.

   De paso, $f'(\pi)=0$ (no se pide).
4. **Por qué no hay que multiplicar por $x$.** Si se expande en potencias de $x$ aparecen $\pi$, $\pi^2$… y hay que volver a centrar. Trabajar con la variable $t=x-\pi$ evita todo eso: $p_4=t^2+\frac14t^3$.

**Receta:** coeficiente de $(x-x_0)^k$ multiplicado por $k!$ es $f^{(k}(x_0)$; potencia que no aparece significa derivada nula.
**Parte del tema:** §2.2 del resumen (coeficientes $a_k=f^{(k}(x_0)/k!$) y Bloque B (ejercicios de E del tipo «comparar coeficientes»).
**Verificación:** sympy, derivando $p_4$ en $\pi$: $[p_4,p_4',p_4'',p_4''',p_4^{(4}](\pi)=[0,0,2,\tfrac32,0]$. Coincide con la solución impresa.
**Avisos:** ninguno (la impresa escribe «$f^{(iv}$», que es la misma derivada cuarta). Error típico: olvidar multiplicar por $k!$ (dar $f'''(\pi)=\frac14$).

---

## Problema 5 · Taylor de un producto: patrón de derivadas (orden 3)

**Fuente:** `X p.70 (Septiembre 2016, Grado en Ing. Mecánica, Modelo A, ejercicio 5 apartado (a); el ejercicio vale 3 puntos en total)`

**Enunciado.** Sea $f(x)=(3x-1)e^x$ una función definida en $\mathbb{R}$. (a) Obtenga el polinomio de Taylor de $f$ de orden 3 centrado en $x=-1$. (Los apartados (b) crecimiento e inflexión y (c) extremos relativos son de U §2.5 y §3.4-3.5; no se tratan aquí.)

**Solución.**
1. **Derivadas por la regla del producto.** $f'(x)=3e^x+(3x-1)e^x=e^x(3x+2)$. Al derivar otra vez, $f''=e^x(3x+2)+3e^x=e^x(3x+5)$, y $f'''=e^x(3x+8)$.
2. **Patrón (para no equivocarse).** Cada derivada suma $3$ al término independiente: $f^{(k}(x)=e^x(3x-1+3k)$. Se prueba por inducción, porque $\big(e^x(3x+b)\big)'=e^x(3x+b+3)$.
3. **Tabla en $x_0=-1$** (se saca factor común $e^{-1}$):

| $k$ | $f^{(k}(-1)$ | $f^{(k}(-1)/k!$ |
|---|---|---|
| 0 | $-4e^{-1}$ | $-4e^{-1}$ |
| 1 | $-e^{-1}$ | $-e^{-1}$ |
| 2 | $2e^{-1}$ | $e^{-1}$ |
| 3 | $5e^{-1}$ | $\frac56e^{-1}$ |

4. **Polinomio:**
$$p_3(x)=e^{-1}\left[-4-(x+1)+(x+1)^2+\frac56(x+1)^3\right].$$
5. **Cómo se deja.** Hay que dejarlo en potencias de $(x+1)$, porque centrado en $-1$ significa eso. Desarrollado en $x$ (solo para comprobar): $e^{-1}\left(\frac56x^3+\frac72x^2+\frac72x-\frac{19}6\right)$.

**Receta:** en productos «polinomio × exponencial» se deriva dos o tres veces, se busca el patrón $f^{(k}=e^x(\dots)$ y luego se hace la tabla en $x_0$ sacando factor común.
**Parte del tema:** §1 (derivadas sucesivas) y §2 del resumen; Bloque A (derivar por etapas) y Bloque B (tabla de coeficientes).
**Verificación:** sympy: $e\cdot f^{(k}(-1)=[-4,-1,2,5]$ y $e\cdot p_3=\frac56x^3+\frac72x^2+\frac72x-\frac{19}6$. Patrón $f^{(k}/e^x=3x-1+3k$ comprobado hasta $k=5$.
**Avisos (errata en la solución impresa):** en la primera línea de $p_3$ pone $\dfrac{3}{3!}e^{-1}(x+1)^3$, cuando debe ser $\dfrac{5}{3!}e^{-1}(x+1)^3$ (puesto que $f'''(-1)=5e^{-1}$). En la línea siguiente sí escribe el coeficiente correcto $\frac56$, así que el resultado final está bien y la errata es de transcripción.

---

## Problema 6 · Cota de error con el resto de Lagrange: $\cos\frac14$ con error $<0{,}002$

**Fuente:** `X pp.145-146 (Febrero 2018, 1.ª semana, I. Electrónica Industrial y Automática, ejercicio 5, segundo apartado, 1,5 puntos de 3)`

**Enunciado.** Dada la función $f(x)=\cos(x)$: […] Usando el resto de Lagrange de orden $n$, calcule $\cos\left(\frac14\right)$ con un error en valor absoluto menor que $0{,}002$. (El primer apartado, «serie de Taylor de $f$ centrada en $x=\frac12$», es de §3.2 y no se trata aquí.)

**Solución.**
1. **Elegir el centro.** Hace falta un $x_0$ cercano a $\frac14$ en el que se conozcan $\cos x_0$ y $\operatorname{sen}x_0$ **exactamente**. El candidato natural es $x_0=0$, porque $\cos0=1$ y $\operatorname{sen}0=0$. (Con $x_0=\frac12$ los coeficientes serían $\cos\frac12$ y $\operatorname{sen}\frac12$, que no sabemos calcular a mano.)
2. **Derivadas.** $f'=-\operatorname{sen}$, $f''=-\cos$, $f'''=\operatorname{sen}$, $f^{(4}=\cos$, y luego se repiten con periodo 4. En $0$ valen $1,0,-1,0,1,\dots$ Por eso $p_0=p_1=1$, $p_2=p_3=1-\frac{x^2}{2}$ y $p_4=p_5=1-\frac{x^2}2+\frac{x^4}{24}$.
3. **Resto (U Prop. 3.2).** $f$ tiene derivadas de todos los órdenes, continuas en $\mathbb{R}$. Para cada $n$ existe un $c\in(0,\frac14)$ con
$$R_n\!\left(\tfrac14\right)=\frac{f^{(n+1}(c)}{(n+1)!}\left(\tfrac14\right)^{n+1}.$$
4. **Acotar la derivada para todo $c$.** Toda derivada de $\cos$ es $\pm\operatorname{sen}$ o $\pm\cos$, así que $|f^{(n+1}(c)|\le1$ (se toma $M=1$) y
$$\left|R_n\!\left(\tfrac14\right)\right|\le\frac{(1/4)^{n+1}}{(n+1)!}.$$
5. **Buscar el menor $n$ con cota $<0{,}002$:**
   - $n=0$: $0{,}25$; $n=1$: $0{,}03125$; $n=2$: $\frac{1}{6\cdot64}\approx0{,}0026>0{,}002$, **no basta**;
   - $n=3$: $\frac{1}{24\cdot256}\approx0{,}000163<0{,}002$. **Basta.**
6. **El polinomio.** $p_3(x)=1-\frac{x^2}{2}$ (porque $f'''(0)=0$, así que $p_3=p_2$). Por tanto
$$\cos\tfrac14\approx p_3\!\left(\tfrac14\right)=1-\frac{1}{32}=\frac{31}{32}=0{,}96875,\qquad |\text{error}|<0{,}000163<0{,}002 .$$
7. **Comprobación.** $\cos\frac14=0{,}968912\ldots$ El error real es $0{,}000162$, prácticamente igual a la cota $R_3$.

**Receta:** cota $\frac{M}{(n+1)!}|x-x_0|^{n+1}$ y se prueba $n=0,1,2,\dots$ hasta que sea $<\varepsilon$. Si una cota no basta pero $f^{(n+1}(x_0)=0$, el mismo polinomio $p_n=p_{n+1}$ admite el resto $R_{n+1}$, que es mucho menor.
**Parte del tema:** §3 del resumen (método de 4 pasos; Ej. 3.10 de U, p. 111, que es el mismo ejercicio con $\operatorname{sen}\frac12$) y el ejemplo propio C0, con su receta «si $f^{(n+1}(x_0)=0$, usa $R_{n+1}$».
**Verificación:** sympy: cotas $0{,}25$; $0{,}03125$; $0{,}0026042$; $0{,}00016276$; $\cos\frac14=0{,}9689124217$; $\cos\frac14-\frac{31}{32}=0{,}000162422$.
**Avisos (fallo de razonamiento en la solución impresa):** calcula la cota de $n=2$, $\approx0{,}002604$, que es **mayor** que $0{,}002$, y aun así concluye «por tanto es suficiente tomar $p_2$». El resultado ($\frac{31}{32}$) es correcto, pero la justificación no: hay que pasar a $n=3$ (cota $0{,}000163$) y observar que $p_3=p_2$. Otra forma correcta de salvar $n=2$ es afinar $M$: $|f'''(c)|=|\operatorname{sen}c|\le\operatorname{sen}\frac14<\frac14$, con lo que $|R_2|\le\frac{1/4}{6}\cdot\frac1{64}\approx0{,}00065<0{,}002$. Además, la impresa centra en $x_0=0$ aunque el primer apartado usa $x=\frac12$. Es lícito, porque el enunciado no fija el centro, pero conviene decirlo, como hace la impresa.

---

## Variantes del tipo «calcular $p_n$ directamente» (mismo método que el problema 3)

| Fuente | Enunciado | Resultado (verificado con sympy) | Aviso sobre la solución impresa |
|---|---|---|---|
| `X p.140 (Feb. 2018, 2.ª semana, I. Electrónica, pregunta corta 2, 1 punto)` | $p_2$ de $f(x)=\sqrt[3]{x}$ en $x=8$ | $p_2=2+\frac1{12}(x-8)-\frac1{288}(x-8)^2$ (y $p_2(9)=2{,}079861$ frente a $\sqrt[3]9=2{,}080084$) | Llama al polinomio «$p_3$» siendo de orden 2: errata de notación |
| `X p.147 (Feb. 2019, 2.ª semana, I. Electrónica, pregunta corta 3, 1 punto)` | $p_2$ de $f(x)=e^{x^2}$ en $x=\sqrt3$ | $p_2=e^3+2\sqrt3\,e^3(x-\sqrt3)+7e^3(x-\sqrt3)^2$ | Dice «derivadas en $x=2$» (es $\sqrt3$) y llama al polinomio «$p_3$»; deja $\frac{14e^3}{2!}$ sin simplificar. Valores correctos |
| `X p.135 (Feb. 2017, 2.ª semana, I. Electrónica, pregunta corta 3, 1 punto)` | $p_3$ de $f(x)=\ln(2x)$ en $x=2$ | $p_3=\ln4+\frac12(x-2)-\frac18(x-2)^2+\frac1{24}(x-2)^3$ | Correcta. Destaca como «fallo recurrente» centrar en $x=0$. Truco: $\ln(2x)=\ln2+\ln x$, de modo que las derivadas son las de $\ln x$ |

---

## Tipos de pregunta del tema que caen en examen y no hay en el PDF
- **Límites indeterminados resueltos con Taylor/Peano** (p. ej. $\lim_{x\to0}\frac{\operatorname{sen}x-x}{x^3}$): el índice no recoge ninguno con Taylor; en X los límites se hacen con L'Hôpital, con el número $e$ o con el emparedado. Como la notación de Landau es material del Aula Virtual, conviene practicarlos con los ejemplos propios del resumen (§4).
- **«¿Para qué $x$ se garantiza un error $<\varepsilon$?»** (despejar $|x-x_0|$ en la cota, Bloque C de E): en X solo aparece la variante «hallar $n$» (problema 6).
- **Acotar el resto cuando $f^{(n+1}$ no está acotada por una constante obvia** (p. ej. $\ln$ o raíces: hay que buscar el máximo de $|f^{(n+1}(c)|$ en el intervalo de $c$): no aparece en X; sí en E.
- **Taylor de composiciones o productos por sustitución de desarrollos conocidos** (p. ej. $p_4$ de $e^{x^2}$ en $0$ a partir del de $e^t$): no aparece en X.
