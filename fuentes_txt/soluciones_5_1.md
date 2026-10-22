# Soluciones Tema 5.1 — Diferencial de una función. Función diferenciable. Plano tangente

Resolución paso a paso de los ejercicios de **E** de la sección 5.1 de U (Ejercicios 5.1-5.12, E pp. 168-179), de preguntas de examen **X** sobre diferencial, diferenciabilidad y plano tangente, y de 4 ejemplos propios. Todos los cálculos se han comprobado con sympy (script `v51.py` en el scratchpad). Se han leído como imagen E pp. 168-179 y X pp. 9, 35, 54, 55, 60, 61, 62, 63, 71, 72, 79, 80, 98, 122, 124, 125, 127, 133, 138.

Páginas: U impresa (= PDF + 2); E impresa = PDF; X = página PDF de `Examenes-resueltos-Calculo.pdf`.

## 0. Herramientas de teoría que se usan

| Clave | Enunciado (resumido) | Dónde |
|---|---|---|
| Idea del plano tangente | Las parciales dan dos vectores tangentes a la gráfica, $(1,0,\frac{\partial f}{\partial x}(a,b))$ y $(0,1,\frac{\partial f}{\partial y}(a,b))$; el único plano candidato que los contiene es $z=f(a,b)+\nabla f(a,b)\cdot(x-a,y-b)$ (5.1). Que existan las parciales **no basta** para que ese plano sea tangente (U Ej. 4.24). | U §5.1.1, pp. 186-188 (Fig. 5.1 p. 187) |
| **Def. 5.1** | $f$ es **diferenciable** en $(a,b)$ si $\displaystyle\lim_{(h,k)\to(0,0)}\frac{f(a+h,b+k)-f(a,b)-\nabla f(a,b)\cdot(h,k)}{\|(h,k)\|}=0$, con $\|(h,k)\|=\sqrt{h^2+k^2}$. Significa: el error de aproximar $f$ por el plano tiende a $0$ **más deprisa** que la distancia al punto. | U p. 189 |
| **Plano tangente (5.2)** | Si $f$ es diferenciable en $(a,b)$: $z=f(a,b)+\nabla f(a,b)\cdot(x-a,\,y-b)$. | U p. 189 |
| Ej. 5.1 | $f=e^{-1/(x^2+y^2)}$, $f(0,0)=0$, es diferenciable en $(0,0)$ (polares: $\lim_{\rho\to0}e^{-1/\rho^2}/\rho=0$). | U pp. 189-190 |
| **Def. 5.2** | Lo mismo con $n$ variables: $\displaystyle\lim_{\bar h\to\bar 0}\frac{f(\bar a+\bar h)-f(\bar a)-\nabla f(\bar a)\cdot\bar h}{\|\bar h\|}=0$. | U p. 190 |
| **Teorema 5.1** | Si $f$ es diferenciable en un punto: (i) admite derivadas parciales en él; (ii) es continua en él. (Contrarrecíproco: si **no** es continua, o le **falta** una parcial, **no** es diferenciable.) | U p. 191 |
| Ej. 5.2 | $xy+1$ ($x>0$) / $x-y$ ($x\le0$): discontinua en $(0,0)$ ⇒ no diferenciable. $x+|y|$: no existe $\frac{\partial}{\partial y}$ en $(0,0)$ ⇒ no diferenciable. | U p. 191 |
| **Condición suficiente** | Si $f$ admite parciales **cerca** del punto y son **continuas en** el punto, $f$ es diferenciable en él. «Regular» = continua con parciales continuas. | U p. 192 |
| Ej. 5.3 | $\operatorname{sen}\frac1{x^2+y^2}$ es diferenciable en todo su dominio $\mathbb{R}^2\setminus\{(0,0)\}$. | U p. 192 |
| Espacio tangente (5.3) | Para $n>2$: $x_{n+1}=f(\bar a)+\nabla f(\bar a)\cdot(\bar x-\bar a)$. | U pp. 192-193 |
| **Def. 5.3** | **Diferencial** de $f$ diferenciable en $\bar a$: la aplicación lineal $Df(\bar a)(\bar x)=\nabla f(\bar a)\cdot\bar x$. En dos variables: $Df(a,b)(x,y)=\frac{\partial f}{\partial x}(a,b)\,x+\frac{\partial f}{\partial y}(a,b)\,y$. Ej. 5.4: $f=x^2+y$, $Df(1,2)(x,y)=2x+y$. | U p. 193 |
| **Def. 5.4** | Diferenciable en un conjunto $A$ = diferenciable en cada punto de $A$. | U p. 193 |

**Herramientas de temas anteriores que aparecen:**
- Derivada parcial por definición, $\frac{\partial f}{\partial x}(a,b)=\lim_{h\to0}\frac{f(a+h,b)-f(a,b)}{h}$ (U Def. 4.8, p. 169; Def. 4.9, p. 170); gradiente (U pp. 173-174).
- Límites dobles: por **caminos** (rectas $y=mx$, curvas): si dos caminos dan límites distintos, el límite no existe (U §4.2, pp. 162-163); **regla del emparedado** (U p. 163).
- **Criterio de polares** (U p. 165): con $F(\rho,\theta)=f(a+\rho\cos\theta,b+\rho\operatorname{sen}\theta)$: (1) si $\lim_{\rho\to0}F$ depende de $\theta$, el límite no existe; (2) si $|F(\rho,\theta)-l|\le g(\rho)$ con $g(\rho)\to0$, el límite es $l$; (3) en otro caso, no se concluye nada.
- Continuidad (U Def. 4.5, p. 166). Regla de L'Hôpital (U §2.3.2, p. 82). Desigualdades útiles: $|\operatorname{sen}u|\le1$, $|\cos\theta|\le1$, $x^2\le x^2+y^2$.

---

### Receta general del tema

> **Calcular la diferencial o el plano tangente de una función «normal»** (fórmula elemental, sin casos): las parciales existen y son continuas, así que es diferenciable (condición suficiente, U p. 192). Entonces $Df(a,b)(x,y)=f_x(a,b)\,x+f_y(a,b)\,y$ y el plano es $z=f(a,b)+f_x(a,b)(x-a)+f_y(a,b)(y-b)$. **Comprobar antes** que el punto $(a,b,c)$ está en la gráfica: $c=f(a,b)$.
>
> **Estudiar la diferenciabilidad en un punto «especial»** (la función se define aparte en él): seguir el **protocolo de 4 pasos**:
> 1. **¿Es continua?** Si no lo es, **no** es diferenciable (Teorema 5.1) y se acaba.
> 2. **Parciales por definición.** Si alguna no existe, **no** es diferenciable (Teorema 5.1) y se acaba.
> 3. **Cociente de diferenciabilidad** con el candidato $\nabla f(a,b)$: $Q(h,k)=\dfrac{f(a+h,b+k)-f(a,b)-f_x(a,b)\,h-f_y(a,b)\,k}{\sqrt{h^2+k^2}}$.
> 4. **Límite de $Q$ en $(0,0)$** (polares o caminos): si es $0$, **diferenciable**; si no existe o no es $0$, **no diferenciable**.
>
> (Alternativa al paso 3-4: si las parciales existen cerca y son continuas en el punto, es diferenciable. Si no lo son, **no se concluye nada**: hay que ir a la definición.)

Esquema lógico que conviene tener a la vista:

$$\text{parciales continuas en el punto}\;\Longrightarrow\;\text{diferenciable}\;\Longrightarrow\;\text{continua y con parciales}$$

Ninguna flecha se invierte (contraejemplos: E 5.5 para la primera, U Ej. 4.24 / E 5.9 / Propio 2 para la segunda).

---

## 1. Ejercicios de E (orden de dificultad creciente; numeración conservada)

Orden propuesto para aprender: **5.1 → 5.8** (teoría: qué implica qué) **→ 5.2 → 5.3 → 5.4** (plano tangente y diferencial de funciones «normales») **→ 5.12** (falta una parcial) **→ 5.9 → 5.7** (hay parciales pero el cociente no tiende a 0) **→ 5.11 → 5.6** (diferenciable por la definición) **→ 5.5** (diferenciable con parciales discontinuas) **→ 5.10** (diferenciable, con L'Hôpital).

---

### Ejercicio 5.1 (E p. 168)

> Si una función $f:\mathbb{R}^2\to\mathbb{R}$ tiene derivadas parciales en un punto $(a,b)\in\mathbb{R}^2$, entonces ¿es diferenciable en ese punto y tiene plano tangente en $(a,b,f(a,b))$?

**Idea en una frase.** Tener las dos parciales solo asegura dos rectas tangentes (una por cada dirección de los ejes); el plano que forman puede no «pegarse» a la gráfica en las demás direcciones.

1. **Qué dan las parciales** (U pp. 186-188): los vectores $(1,0,f_x)$ y $(0,1,f_y)$, tangentes a los cortes de la gráfica con los planos $y=b$ y $x=a$. Solo miran **dos** direcciones.
2. **Qué exige la diferenciabilidad** (Def. 5.1, U p. 189): que el plano formado con esas parciales aproxime a $f$ cuando nos acercamos **por cualquier camino**. Es una exigencia más fuerte.
3. **Contraejemplo** (U Ej. 4.24, p. 172): $f(x,y)=\operatorname{arctg}\frac{xy}{x^2+y^2}$, $f(0,0)=0$. En los ejes $f=0$, así que $f_x(0,0)=f_y(0,0)=0$. Pero por la recta $y=x$, $f(x,x)=\operatorname{arctg}\frac12\ne0=f(0,0)$: **no es continua** en $(0,0)$ y, por el Teorema 5.1 (U p. 191), **no es diferenciable**.
4. **Plano tangente:** U solo llama plano tangente al plano (5.2) cuando $f$ es diferenciable (U p. 189). Sin diferenciabilidad, no hay plano tangente.
5. **Respuesta:** **no se puede asegurar ninguna de las dos cosas.** La existencia de parciales es condición **necesaria** (Teorema 5.1) pero **no suficiente**. Lo que sí basta es que las parciales existan cerca y sean **continuas** en el punto (U p. 192).

**Receta.** «Parciales ⇒ diferenciable» es **falso**. «Parciales continuas ⇒ diferenciable» es **verdadero**. «Diferenciable ⇔ tiene plano tangente».

**Error típico.** Trasladar la intuición de una variable («derivable = tiene recta tangente») a dos variables cambiando «derivable» por «tiene parciales».

---

### Ejercicio 5.8 (E pp. 174-175)

> De $f:\mathbb{R}^3\to\mathbb{R}$ se sabe que es discontinua en $(1,2,3)$ y diferenciable en $(3,2,1)$. ¿Puedes decir algo sobre su diferenciabilidad en $(1,2,3)$? ¿Y sobre su continuidad en $(3,2,1)$?

**Idea en una frase.** «Diferenciable ⇒ continua» (como «derivable ⇒ continua» en una variable), y su contrarrecíproco «no continua ⇒ no diferenciable».

1. **Teorema 5.1** (U p. 191, válido con $n$ variables por la Def. 5.2, p. 190): si $f$ es diferenciable en un punto, es continua en él.
2. **En $(3,2,1)$:** $f$ es diferenciable, luego (aplicando el teorema tal cual) **es continua** en $(3,2,1)$.
3. **En $(1,2,3)$:** si $f$ fuera diferenciable allí, por el teorema sería continua allí; pero el enunciado dice que **no** lo es. Esa suposición es imposible: $f$ **no es diferenciable** en $(1,2,3)$.
4. **Respuesta:** no diferenciable en $(1,2,3)$; continua en $(3,2,1)$.

**Receta.** Si «A ⇒ B», entonces «no B ⇒ no A» (contrarrecíproco). Aquí A = diferenciable, B = continua.

**Error típico.** Razonar al revés: «es continua, luego es diferenciable» (falso, p. ej. $x+|y|$, U Ej. 5.2).

---

### Ejercicio 5.2 (E p. 168)

> Sea $f:\mathbb{R}^2\to\mathbb{R}$ la función dada por $f(x,y)=\cos y-yx^2$. Decide cuáles de las siguientes condiciones cumple el plano tangente a su gráfica en el punto $(0,0,1)$: a) Verifica la ecuación $1-z=0$. b) Es paralelo al plano $xy$. c) Es paralelo al plano $xz$. d) Ninguna de las anteriores.

**Idea en una frase.** Plano tangente = valor + gradiente; si el gradiente es nulo, el plano es horizontal.

1. **¿El punto está en la gráfica?** $f(0,0)=\cos0-0=1$. Sí: $(0,0,1)=(0,0,f(0,0))$.
2. **¿Es diferenciable?** $f$ es suma y producto de funciones elementales: sus parciales existen en todo $\mathbb{R}^2$ y son continuas, así que es diferenciable (condición suficiente, U p. 192) y tiene plano tangente.
3. **Parciales.** $\frac{\partial f}{\partial x}=-2xy$ ($y$ constante; $\cos y$ no depende de $x$); $\frac{\partial f}{\partial y}=-\operatorname{sen}y-x^2$. En $(0,0)$: $\nabla f(0,0)=(0,0)$.
4. **Plano (5.2)** (U p. 189): $z=1+(0,0)\cdot(x,y)=1$, es decir, $1-z=0$.
5. **Interpretar:** $z=1$ es el conjunto de puntos a altura $1$: un plano horizontal, **paralelo al plano $xy$** (que es $z=0$). No es paralelo al plano $xz$ (que es vertical, $y=0$).
6. **Respuesta: a) y b).**

**Receta.** $\nabla f(a,b)=(0,0)$ ⇔ plano tangente horizontal $z=f(a,b)$.

**Error típico.** Confundir «paralelo al plano $xy$» (horizontal, $z=$ cte) con «paralelo al plano $xz$» (vertical, $y=$ cte).

sympy: $\nabla f(0,0)=(0,0)$.

---

### Ejercicio 5.3 (E p. 169)

> Sea $f:\mathbb{R}^2\to\mathbb{R}$ la función dada por $f(x,y)=x^2+y^3+e^{x+y}$. Obtén la ecuación del plano tangente a su gráfica en el punto $(1,-1,1)$.

**Idea en una frase.** Comprobar el punto, calcular el gradiente en él y sustituir en (5.2).

1. **Diferenciable:** suma de un polinomio y una exponencial; parciales continuas en todo $\mathbb{R}^2$ ⇒ diferenciable (U p. 192).
2. **Punto en la gráfica:** $f(1,-1)=1-1+e^{0}=1$. Correcto.
3. **Parciales** (regla de la cadena en $e^{x+y}$: la derivada interior respecto de $x$ y de $y$ vale $1$): $f_x=2x+e^{x+y}$, $f_y=3y^2+e^{x+y}$.
4. **En $(1,-1)$:** $f_x=2+1=3$; $f_y=3+1=4$. $\nabla f(1,-1)=(3,4)$.
5. **Plano** (U (5.2), p. 189): $z=1+3(x-1)+4(y+1)=1+3x-3+4y+4$, es decir, $\boxed{z=2+3x+4y}$.
6. **Comprobación:** en $(1,-1)$ da $2+3-4=1=f(1,-1)$.

**Receta.** $z=f(a,b)+f_x(a,b)(x-a)+f_y(a,b)(y-b)$ y simplificar; comprobar sustituyendo $(a,b)$.

**Error típico.** Escribir $(y-1)$ en lugar de $(y-(-1))=(y+1)$.

sympy: $f(1,-1)=1$, $\nabla f(1,-1)=(3,4)$, plano $z=3x+4y+2$.

---

### Ejercicio 5.4 (E p. 170)

> Sea $f$ la función dada por $f(x,y)=xe^y+y\cos^2(xy)$. ¿Cuál es su diferencial en un punto genérico $(a,b)$?

**Idea en una frase.** La diferencial es la función lineal «gradiente por vector»: $Df(a,b)(x,y)=f_x(a,b)\,x+f_y(a,b)\,y$.

1. **Diferenciable en todo $\mathbb{R}^2$:** sumas, productos y composiciones de funciones elementales; parciales continuas (U p. 192).
2. **Parcial en $x$** ($y$ constante). $\frac{\partial}{\partial x}(xe^y)=e^y$. Para $y\cos^2(xy)$: $y$ es una constante que multiplica; $\cos^2u$ con $u=xy$ se deriva $2\cos u\cdot(-\operatorname{sen}u)\cdot u_x$ y $u_x=y$. Queda $y\cdot(-2y\cos(xy)\operatorname{sen}(xy))=-y^2\operatorname{sen}(2xy)$ (usando $2\operatorname{sen}u\cos u=\operatorname{sen}2u$). Total: $f_x=e^y-y^2\operatorname{sen}(2xy)$.
3. **Parcial en $y$** ($x$ constante). $\frac{\partial}{\partial y}(xe^y)=xe^y$. El segundo sumando es un **producto** de $y$ por $\cos^2(xy)$: $1\cdot\cos^2(xy)+y\cdot\big(-2\cos(xy)\operatorname{sen}(xy)\cdot x\big)=\cos^2(xy)-xy\operatorname{sen}(2xy)$. Total: $f_y=xe^y+\cos^2(xy)-xy\operatorname{sen}(2xy)$.
4. **Gradiente en $(a,b)$:** $\nabla f(a,b)=\big(e^b-b^2\operatorname{sen}(2ab),\ ae^b+\cos^2(ab)-ab\operatorname{sen}(2ab)\big)$.
5. **Diferencial** (Def. 5.3, U p. 193):
$$Df(a,b)(x,y)=\big(e^b-b^2\operatorname{sen}(2ab)\big)\,x+\big(ae^b+\cos^2(ab)-ab\operatorname{sen}(2ab)\big)\,y.$$

**Receta.** Diferencial en $(a,b)$ = «parciales evaluadas en $(a,b)$» multiplicadas por $x$ e $y$. Las letras $(a,b)$ fijan el punto; $(x,y)$ es el vector sobre el que actúa.

**Error típico.** En $\frac{\partial}{\partial y}\big(y\cos^2(xy)\big)$ olvidar la regla del producto (falta el término $\cos^2(xy)$), o mezclar el punto $(a,b)$ con la variable $(x,y)$.

sympy: las dos diferencias con la fórmula final simplifican a $0$.

---

### Ejercicio 5.12 (E p. 179)

> Sea $f:\mathbb{R}^2\to\mathbb{R}$ definida como $f(x,y)=x^2-xy+y^2$ y $g:\mathbb{R}^2\to\mathbb{R}$ definida por $g(x,y)=\dfrac{f(x,y)+xy}{\sqrt{x^2+y^2}}$ si $(x,y)\ne(0,0)$, $g(0,0)=0$. ¿Es $g$ diferenciable en todo $\mathbb{R}^2$?

**Idea en una frase.** Simplificada, $g$ es la distancia al origen, $\sqrt{x^2+y^2}$: un «cono» con pico en el origen, donde no hay plano tangente.

1. **Simplificar:** $f+xy=x^2+y^2$, luego para $(x,y)\ne(0,0)$: $g=\frac{x^2+y^2}{\sqrt{x^2+y^2}}=\sqrt{x^2+y^2}$. Además $g(0,0)=0=\sqrt{0}$: $g(x,y)=\sqrt{x^2+y^2}$ en todo $\mathbb{R}^2$.
2. **Fuera del origen:** $g_x=\frac{x}{\sqrt{x^2+y^2}}$, $g_y=\frac{y}{\sqrt{x^2+y^2}}$, continuas donde $x^2+y^2\ne0$. Por la condición suficiente (U p. 192), $g$ es diferenciable en $\mathbb{R}^2\setminus\{(0,0)\}$.
3. **En el origen, parcial por definición** (U Def. 4.8, p. 169): $\frac{g(h,0)-g(0,0)}{h}=\frac{\sqrt{h^2}}{h}=\frac{|h|}{h}$ (¡ojo!: $\sqrt{h^2}=|h|$, no $h$).
4. **Ese límite no existe:** por la derecha ($h>0$) vale $1$; por la izquierda ($h<0$) vale $-1$. No existe $\frac{\partial g}{\partial x}(0,0)$.
5. **Teorema 5.1** (U p. 191): sin una parcial, no hay diferenciabilidad. $g$ **no** es diferenciable en $(0,0)$.
6. **Respuesta:** **no**; $g$ es diferenciable en $\mathbb{R}^2\setminus\{(0,0)\}$ pero no en $(0,0)$ (aunque sí es continua allí).

**Receta.** Antes de nada, **simplificar** la expresión. Si una parcial en el punto no existe (típico: $|h|/h$), se acaba: no diferenciable.

**Error típico.** Escribir $\sqrt{h^2}=h$ y obtener $\frac{\partial g}{\partial x}(0,0)=1$.

*Comentario:* es el mismo problema que X pp. 17-18 (Sept 2011, Mecánica, Ej. 6).

sympy: $g=\sqrt{x^2+y^2}$; límites laterales $1$ y $-1$.

---

### Ejercicio 5.9 (E pp. 175-176)

> Dada la función $f:\mathbb{R}^2\to\mathbb{R}$ definida por $f(x,y)=y\operatorname{sen}\frac1x+x$ si $x\ne0$, $f(x,y)=0$ si $x=0$, estudia la continuidad, existencia de derivadas parciales en $(0,0)$ y, si es posible, calcula el plano tangente a la gráfica de $f$ en $(0,0,0)$.

**Idea en una frase.** Continua y con parciales, pero el término $y\operatorname{sen}\frac1x$ oscila tanto que el plano candidato $z=x$ no aproxima bien.

1. **Continuidad en $(0,0)$** (emparedado, U p. 163). Si $x\ne0$: $|f(x,y)|\le|y|\cdot|\operatorname{sen}\tfrac1x|+|x|\le|y|+|x|$. Si $x=0$: $|f|=0\le|y|+|x|$. Como $|x|+|y|\to0$, $\lim_{(x,y)\to(0,0)}f(x,y)=0=f(0,0)$: **continua** en $(0,0)$.
2. **Parcial en $x$:** $f(h,0)=0\cdot\operatorname{sen}\frac1h+h=h$, así que $\frac{f(h,0)-0}{h}=1$ y $\frac{\partial f}{\partial x}(0,0)=1$.
3. **Parcial en $y$:** $f(0,h)=0$ (está en la recta $x=0$), así que $\frac{\partial f}{\partial y}(0,0)=0$. Candidato: $\nabla f(0,0)=(1,0)$, plano candidato $z=x$.
4. **Cociente de diferenciabilidad** (Def. 5.1, U p. 189): $Q(h,k)=\frac{f(h,k)-0-h}{\sqrt{h^2+k^2}}$. Si $h\ne0$: $Q=\frac{k\operatorname{sen}(1/h)}{\sqrt{h^2+k^2}}$.
5. **Un camino concreto: la recta $k=h$ con $h=t>0$.** $Q(t,t)=\frac{t\operatorname{sen}(1/t)}{\sqrt2\,t}=\frac{1}{\sqrt2}\operatorname{sen}\frac1t$.
6. **Ese límite no existe:** con $t_n=\frac1{n\pi}\to0$, $\operatorname{sen}(1/t_n)=0$; con $t_n=\frac1{\pi/2+2n\pi}\to0$, $\operatorname{sen}(1/t_n)=1$. Dos sucesiones que tienden a $0$ dan valores $0$ y $\frac1{\sqrt2}$.
7. **Conclusión:** si $\lim_{(h,k)\to(0,0)}Q$ existiera, el límite por la recta $k=h$ existiría (U pp. 162-163). Como no existe, $f$ **no es diferenciable** en $(0,0)$ y **no tiene plano tangente** en $(0,0,0)$.

**Receta.** Si el cociente $Q$ contiene $\operatorname{sen}(1/\text{algo})$ sin un factor que tienda a $0$ delante, buscar un camino (recta) donde quede solo la oscilación.

**Error típico.** Concluir «existe el plano tangente $z=x$» solo porque existen las parciales.

sympy: en $k=h=t$, $Q=\frac{\sqrt2}{2}\cdot\frac{t\operatorname{sen}(1/t)}{|t|}$.

---

### Ejercicio 5.7 (E pp. 173-174)

> Sea $f$ la función dada por $f(x,y)=\dfrac{4x^3}{x^2+y^2}$ si $(x,y)\ne(0,0)$, $f(0,0)=0$. Estudia su continuidad, si tiene derivadas parciales y si es diferenciable.

**Idea en una frase.** Pasa los dos primeros filtros (continua, parciales), pero el cociente en polares depende del ángulo.

1. **Fuera del origen:** cociente de polinomios con denominador no nulo: continua, con parciales continuas y, por la condición suficiente (U p. 192), **diferenciable** en $\mathbb{R}^2\setminus\{(0,0)\}$. Allí $f_x=\frac{4x^2(x^2+3y^2)}{(x^2+y^2)^2}$, $f_y=\frac{-8x^3y}{(x^2+y^2)^2}$.
2. **Continuidad en $(0,0)$.** Como $x^2\le x^2+y^2$: $|f|=\frac{4x^2|x|}{x^2+y^2}\le4|x|\to0$. Por el emparedado (U p. 163), $\lim_{(x,y)\to(0,0)} f=0=f(0,0)$: **continua**. (En polares: $f=4\rho\cos^3\theta$, y $|4\rho\cos^3\theta|\le4\rho$.)
3. **Parciales en $(0,0)$ por definición:** $f(h,0)=\frac{4h^3}{h^2}=4h$, cociente $\frac{4h}{h}=4$: $\frac{\partial f}{\partial x}(0,0)=4$. $f(0,h)=0$: $\frac{\partial f}{\partial y}(0,0)=0$. Candidato: $\nabla f(0,0)=(4,0)$.
4. **Cociente:** $Q=\dfrac{\frac{4h^3}{h^2+k^2}-4h}{\sqrt{h^2+k^2}}=\dfrac{4h^3-4h(h^2+k^2)}{(h^2+k^2)^{3/2}}=\dfrac{-4hk^2}{(h^2+k^2)^{3/2}}$.
5. **Polares** ($h=\rho\cos\theta$, $k=\rho\operatorname{sen}\theta$): $Q=\frac{-4\rho^3\cos\theta\operatorname{sen}^2\theta}{\rho^3}=-4\cos\theta\operatorname{sen}^2\theta$. No queda $\rho$: el «límite» es este número, que **depende de $\theta$**.
6. **Ejemplo concreto:** por $\theta=0$ (eje $x$) sale $0$; por $\theta=\frac\pi4$ (recta $k=h$, $h>0$) sale $-4\cdot\frac{\sqrt2}2\cdot\frac12=-\sqrt2$. Distintos.
7. **Conclusión** (criterio de polares, caso 1, U p. 165): el límite de $Q$ no existe; $f$ **no es diferenciable** en $(0,0)$.

**Receta.** Protocolo de 4 pasos. Si en polares $Q$ queda solo función de $\theta$ (no constante), **no** es diferenciable.

**Error típico.** Olvidar restar el término del gradiente ($-4h$) en el numerador, o usar $\nabla f(0,0)=(0,0)$ «porque $f(0,0)=0$».

*Comentario:* el mismo ejercicio aparece en X pp. 20-21 (Feb 2012, 1ª semana, Mecánica A, Ej. 6) y X pp. 115, 117-118 (Examen 3, Ej. 6). Muy parecido: $f=\frac{x^3}{x^2+2y^2}$, $f(0,0)=0$ (X pp. 2-3, Feb 2010 1ª, Eléctrica, Ej. 6; X pp. 90-92, Feb 2018 A, Ej. 6): $\nabla f(0,0)=(1,0)$ y $Q=\frac{-2\cos\theta\operatorname{sen}^2\theta}{1+\operatorname{sen}^2\theta}$, que depende de $\theta$: no diferenciable.

sympy: $f_x(0,0)=4$, $f_y(0,0)=0$; $Q=-4\operatorname{sen}^2\theta\cos\theta$.

---

### Ejercicio 5.11 (E p. 178)

> Sea $f$ la función dada por $f(x,y)=\dfrac{xy}{\sqrt[4]{x^2+y^2}}$ si $(x,y)\ne(0,0)$, $f(0,0)=0$. Calcula las derivadas parciales en $(0,0)$ y estudia la diferenciabilidad de $f$ en el mismo punto.

**Idea en una frase.** El numerador es de «grado 2» y el denominador de «grado $\frac12$»; tras dividir por $\rho$ sobra $\sqrt\rho\to0$.

1. **Parciales por definición:** en los ejes $xy=0$, así que $f(h,0)=f(0,h)=0$ y ambos cocientes son $\frac0h=0$: $\nabla f(0,0)=(0,0)$.
2. **Cociente:** $Q=\dfrac{f(h,k)-0-0}{\sqrt{h^2+k^2}}=\dfrac{hk}{\sqrt[4]{h^2+k^2}\,\sqrt{h^2+k^2}}$.
3. **Polares:** $\sqrt[4]{\rho^2}=\sqrt\rho$ y $\sqrt{\rho^2}=\rho$, luego $Q=\dfrac{\rho^2\cos\theta\operatorname{sen}\theta}{\sqrt\rho\cdot\rho}=\sqrt\rho\,\cos\theta\operatorname{sen}\theta$.
4. **Acotar** (criterio de polares, caso 2, U p. 165): $|Q|\le\sqrt\rho$ (porque $|\cos\theta\operatorname{sen}\theta|\le1$) y $\sqrt\rho\to0$. Así $\lim_{(h,k)\to(0,0)}Q=0$.
5. **Conclusión:** $f$ **es diferenciable** en $(0,0)$, con $Df(0,0)=0$ y plano tangente $z=0$.

**Receta.** En polares, si $Q=(\text{potencia positiva de }\rho)\times(\text{algo acotado en }\theta)$, el límite es $0$: diferenciable.

**Error típico.** Concluir solo con $\rho\to0$ sin decir que el factor en $\theta$ está **acotado** (es lo que permite aplicar el caso 2 del criterio).

sympy: $Q=\tfrac12\sqrt\rho\,\operatorname{sen}2\theta$.

---

### Ejercicio 5.6 (E pp. 172-173)

> Estudia la diferenciabilidad en $(0,0)$ de la función $f$ dada por $f(x,y)=x|y|$.

**Idea en una frase.** Aunque $|y|$ tiene un pico, el factor $x$ lo «aplasta»: el cociente es $\rho\cos\theta|\operatorname{sen}\theta|\to0$.

1. **Continua:** producto de funciones continuas ($x$ y $|y|$).
2. **Parciales en $(0,0)$:** $f(h,0)=h\cdot0=0$ y $f(0,h)=0\cdot|h|=0$: $\nabla f(0,0)=(0,0)$.
3. **Cociente:** $Q=\dfrac{h|k|}{\sqrt{h^2+k^2}}$.
4. **Polares:** $Q=\dfrac{\rho\cos\theta\cdot\rho|\operatorname{sen}\theta|}{\rho}=\rho\cos\theta|\operatorname{sen}\theta|$, y $|Q|\le\rho\to0$ (U p. 165, caso 2).
5. **Conclusión:** $f$ **es diferenciable** en $(0,0)$, con $Df(0,0)=0$.
6. **¿Servía la condición suficiente?** **No.** $\frac{\partial f}{\partial y}$ no existe en los puntos $(x_0,0)$ con $x_0\ne0$: $\frac{f(x_0,k)-f(x_0,0)}{k}=x_0\frac{|k|}{k}$, que vale $x_0$ por la derecha y $-x_0$ por la izquierda. Como hay puntos tan cerca como se quiera del origen sin $\frac{\partial f}{\partial y}$, no se cumple «parciales **cerca** del punto» (U p. 192). Por eso aquí hay que usar la **definición**.

**Receta.** Cuando aparecen valores absolutos, las parciales pueden no existir cerca del punto: ir directamente a la definición (Def. 5.1).

**Error típico.** Aplicar la condición suficiente con $\frac{\partial f}{\partial y}=x$ si $y\ge0$, $-x$ si $y<0$: esa fórmula falla sobre la recta $y=0$ (allí la parcial no existe salvo en $x_0=0$).

sympy: $Q=\rho\cos\theta\,|\operatorname{sen}\theta|$.

---

### Ejercicio 5.5 (E pp. 170-172)

> Sea $f:\mathbb{R}^2\to\mathbb{R}$ la función dada por $f(x,y)=(x^2+y^2)\operatorname{sen}\dfrac1{x^2+y^2}$ si $(x,y)\ne(0,0)$, $f(0,0)=0$. ¿Tiene derivadas parciales en $(0,0)$? ¿Es diferenciable en $(0,0)$? ¿Son las derivadas parciales continuas en $(0,0)$?

**Idea en una frase.** Es el ejemplo de que la condición suficiente **no es necesaria**: diferenciable en el origen, pero sus parciales oscilan sin control cerca de él.

1. **Parcial en $x$ en $(0,0)$:** $f(h,0)=h^2\operatorname{sen}\frac1{h^2}$, cociente $h\operatorname{sen}\frac1{h^2}$. Como $|h\operatorname{sen}\frac1{h^2}|\le|h|\to0$: $\frac{\partial f}{\partial x}(0,0)=0$.
2. **Parcial en $y$:** igual por simetría ($f(0,h)=h^2\operatorname{sen}\frac1{h^2}$): $\frac{\partial f}{\partial y}(0,0)=0$.
3. **Cociente:** $Q=\dfrac{(h^2+k^2)\operatorname{sen}\frac1{h^2+k^2}}{\sqrt{h^2+k^2}}=\sqrt{h^2+k^2}\,\operatorname{sen}\dfrac1{h^2+k^2}$. En polares: $Q=\rho\operatorname{sen}\frac1{\rho^2}$, y $|Q|\le\rho\to0$.
4. **Diferenciable** en $(0,0)$ (Def. 5.1), con $Df(0,0)=0$.
5. **Parcial en $x$ fuera del origen** (reglas; producto y cadena; $\frac{\partial}{\partial x}\frac1{x^2+y^2}=\frac{-2x}{(x^2+y^2)^2}$):
$$f_x(x,y)=2x\operatorname{sen}\frac1{x^2+y^2}-\frac{2x}{x^2+y^2}\cos\frac1{x^2+y^2}.$$
6. **¿Es continua en $(0,0)$?** Habría que tener $\lim_{(x,y)\to(0,0)}f_x=0$. Por el eje $x$ ($y=0$, $x>0$): $f_x(x,0)=2x\operatorname{sen}\frac1{x^2}-\frac2x\cos\frac1{x^2}$. Tomamos $x_n=\frac1{\sqrt{2n\pi}}\to0$: $\frac1{x_n^2}=2n\pi$, $\operatorname{sen}=0$, $\cos=1$, y queda $f_x(x_n,0)=-\frac2{x_n}=-2\sqrt{2n\pi}\to-\infty$.
7. **Conclusión:** $f_x$ no tiene límite $0$ en el origen: **no es continua** en $(0,0)$. Por simetría, tampoco $f_y$.
8. **Resumen:** sí tiene parciales ($0$ y $0$); sí es diferenciable; las parciales **no** son continuas en $(0,0)$.

**Receta.** Para probar que una parcial **no** es continua, basta una sucesión de puntos que tienda al origen en la que la parcial no tienda al valor en el origen (elegir puntos donde el $\operatorname{sen}$ o el $\cos$ valgan $0$ o $1$).

**Error típico.** Pensar «las parciales no son continuas, luego no es diferenciable». La condición suficiente es solo suficiente: si falla, hay que ir a la definición.

sympy: $f_x(0,0)=0$; $f_x\big(\tfrac1{\sqrt{2n\pi}},0\big)=-2\sqrt{2n\pi}$.

---

### Ejercicio 5.10 (E pp. 176-177)

> Sea $f:S\to\mathbb{R}$ la función dada por $f(x,y)=\dfrac{x^2+y^2}{\ln(1-x^2-y^2)}$ si $(x,y)\in S\setminus\{(0,0)\}$, $f(0,0)=-1$, donde $S=\{(x,y)\in\mathbb{R}^2: x^2+y^2<1\}$. Estudia si es continua y si es diferenciable en $(0,0)$.

**Idea en una frase.** $f$ solo depende de $u=x^2+y^2$; todo se reduce a dos límites de una variable en $u$ que se hacen con L'Hôpital.

1. **Reducir a una variable.** Con $u=x^2+y^2$ (en polares, $u=\rho^2$): $f=\varphi(u)=\frac{u}{\ln(1-u)}$ para $0<u<1$.
2. **Continuidad: $\lim_{u\to0^+}\frac{u}{\ln(1-u)}$.** Es $\frac00$. L'Hôpital (U §2.3.2, p. 82): $\frac{1}{-1/(1-u)}=-(1-u)\to-1$. Como $u=\rho^2\to0$ cuando $(x,y)\to(0,0)$ y no hay $\theta$, $\lim_{(x,y)\to(0,0)}f=-1=f(0,0)$: **continua**.
3. **Preparar el límite clave.** Definimos $G(u)=\varphi(u)+1=\frac{u+\ln(1-u)}{\ln(1-u)}$ (es $f-f(0,0)$). Vamos a ver que $\lim_{u\to0^+}\frac{G(u)}{u}=\frac12$. Escribimos
$$\frac{G(u)}{u}=\frac{\dfrac{u+\ln(1-u)}{u^2}}{\dfrac{\ln(1-u)}{u}}.$$
4. **Numerador:** $\frac{u+\ln(1-u)}{u^2}$ es $\frac00$; L'Hôpital: $\frac{1-\frac1{1-u}}{2u}=\frac{\frac{-u}{1-u}}{2u}=\frac{-1}{2(1-u)}\to-\frac12$.
5. **Denominador:** $\frac{\ln(1-u)}{u}$ es $\frac00$; L'Hôpital: $\frac{-1/(1-u)}{1}\to-1$.
6. **Cociente:** $\frac{G(u)}{u}\to\frac{-1/2}{-1}=\frac12$.
7. **Parcial en $x$:** $\frac{f(h,0)-f(0,0)}{h}=\frac{G(h^2)}{h}=h\cdot\frac{G(h^2)}{h^2}\to0\cdot\frac12=0$. Igual en $y$ (la función es simétrica en $x$, $y$): $\nabla f(0,0)=(0,0)$.
8. **Cociente de diferenciabilidad:** $Q=\frac{f(h,k)-(-1)-0}{\sqrt{h^2+k^2}}$. En polares, $Q=\frac{G(\rho^2)}{\rho}=\rho\cdot\frac{G(\rho^2)}{\rho^2}\to0\cdot\frac12=0$. No depende de $\theta$, así que el límite doble es $0$.
9. **Conclusión:** $f$ es **continua** y **diferenciable** en $(0,0)$, con $Df(0,0)=0$ y plano tangente $z=-1$.

**Receta.** Si $f$ depende solo de $x^2+y^2$, todo (continuidad, parciales, cociente) se reduce a límites de **una** variable: hacerlos una vez y reutilizarlos.

**Error típico.** Restar $f(0,0)$ con el signo cambiado: aquí $f(0,0)=-1$, así que en el numerador aparece $+1$.

*Comentario:* el mismo ejercicio aparece en X pp. 26-27 (Sept 2012, Mecánica A, Ej. 6).

sympy: $\lim_{\rho\to0}\frac{\rho^2}{\ln(1-\rho^2)}=-1$; $\lim_{u\to0^+}G(u)/u=\frac12$; parciales y cociente $\to0$.

---

## 2. Preguntas de examen (X)

Las preguntas se ordenan de corta a larga. Las de mayor interés para este tema llevan ★. Las idénticas a E 5.7, 5.10 y 5.12 se citan en esos ejercicios (no se repiten).

---

### ★ X p. 35 (Feb 2013, 2ª semana, Mecánica, Modelo B, PC4, 1 punto) — repetida en X p. 44 (Feb 2014, Modelo B, P4) y X p. 57 (Feb 2015, Modelo B, P4)

> Calcule la diferencial de la función $f(x,y)=(x+\operatorname{sen}y)^2$.

**Idea en una frase.** Diferencial = parciales en $(a,b)$ multiplicadas por $x$ e $y$.

1. **Diferenciable en todo $\mathbb{R}^2$:** composición de funciones elementales con parciales continuas (U p. 192).
2. **Parciales** (cadena con $u=x+\operatorname{sen}y$): $f_x=2(x+\operatorname{sen}y)\cdot1$; $f_y=2(x+\operatorname{sen}y)\cdot\cos y$.
3. **Diferencial en $(a,b)$** (Def. 5.3, U p. 193):
$$Df(a,b)(x,y)=2(a+\operatorname{sen}b)\,x+2(a+\operatorname{sen}b)\cos b\;y=2(a+\operatorname{sen}b)\,(x+y\cos b).$$

**Receta.** Escribir la diferencial en un punto genérico $(a,b)$ como función lineal de $(x,y)$.

**Error típico.** Dar solo el gradiente sin escribirlo como aplicación lineal, u olvidar el factor $\cos y$ (derivada interior).

sympy: $\nabla f(a,b)=\big(2(a+\operatorname{sen}b),\,2(a+\operatorname{sen}b)\cos b\big)$.

---

### ★ Preguntas cortas de 1 punto (X p. 60, p. 127, p. 133, p. 9)

**X p. 60 (Feb 2016, Modelo A, P4).** *Enuncie una condición suficiente para que la función $f:\mathbb{R}^2\to\mathbb{R}$ sea diferenciable en el punto $(a,b)$.*
Respuesta (U p. 192): si $f$ admite derivadas parciales en un entorno de $(a,b)$ y estas son continuas en $(a,b)$, entonces $f$ es diferenciable en $(a,b)$, y su diferencial es $Df(a,b)(x,y)=\nabla f(a,b)\cdot(x,y)$.

**X p. 127 (I. Electrónica, examen A sin fecha, P4).** *Calcule la ecuación del plano tangente a la gráfica de la función $f(x,y)=x^2+xy$ en el punto $(1,2,3)$.*
$f(1,2)=1+2=3$ (el punto está en la gráfica). $\nabla f=(2x+y,\,x)$, $\nabla f(1,2)=(4,1)$. Plano: $z=3+4(x-1)+(y-2)$, es decir, $\boxed{4x+y-z=3}$.

**X p. 133 (Sept 2017, P4).** *Calcule la ecuación del plano tangente a la gráfica de la función $f(x,y)=e^x(3\operatorname{sen}y+2)$ en el punto $\left(0,\frac\pi2,5\right)$.*
$f(0,\frac\pi2)=1\cdot(3+2)=5$. $f_x=e^x(3\operatorname{sen}y+2)$, $f_y=3e^x\cos y$; en el punto: $(5,0)$. Plano: $z=5+5(x-0)+0\cdot(y-\frac\pi2)$, es decir, $\boxed{z=5+5x}$.

**X p. 9 (examen sin cabecera, P3b; sin solución impresa).** *Calcular la diferencial de $f(x,y)=y\operatorname{tg}(\operatorname{sen}x)$ en donde esta exista.*
1. **Dónde está definida:** $\operatorname{sen}x\in[-1,1]$ y $1<\frac\pi2$, así que $\cos(\operatorname{sen}x)>0$ y $\operatorname{tg}(\operatorname{sen}x)$ existe para todo $x$. $f$ está definida en todo $\mathbb{R}^2$.
2. **Parciales:** $f_x=y\cdot\frac{1}{\cos^2(\operatorname{sen}x)}\cdot\cos x$; $f_y=\operatorname{tg}(\operatorname{sen}x)$. Son continuas en todo $\mathbb{R}^2$ (el denominador nunca se anula), luego $f$ es diferenciable en todo $\mathbb{R}^2$ (U p. 192).
3. **Diferencial:** $Df(a,b)(x,y)=\dfrac{b\cos a}{\cos^2(\operatorname{sen}a)}\,x+\operatorname{tg}(\operatorname{sen}a)\,y$, para todo $(a,b)\in\mathbb{R}^2$.

**Receta (plano tangente).** (1) comprobar $c=f(a,b)$; (2) gradiente en $(a,b)$; (3) $z=c+f_x(a,b)(x-a)+f_y(a,b)(y-b)$.

**Error típico.** No comprobar que el punto está en la gráfica, o escribir $(x+a)$ en lugar de $(x-a)$.

sympy: X127 $f=3$, $\nabla f=(4,1)$; X133 $f=5$, $\nabla f=(5,0)$; X9 $f_x=\frac{y\cos x}{\cos^2(\operatorname{sen}x)}$, $f_y=\operatorname{tg}(\operatorname{sen}x)$.

---

### ★ X p. 98 (Sept 2018, Modelo A, Ej. 6, 3 puntos)

> Sea $f:\mathbb{R}^2\to\mathbb{R}$ la función definida por $f(x,y)=\operatorname{arctg}\dfrac{xy}{x^2+y^2}$ si $(x,y)\ne(0,0)$, $f(0,0)=0$. Se pide: a) (1 punto) Estudiar si es una función continua en $\mathbb{R}^2$. b) (1 punto) Estudiar si tiene derivadas parciales en $\mathbb{R}^2$. c) (1 punto) Estudiar si es diferenciable en $(0,0)$.

**Idea en una frase.** Tiene parciales en todas partes, pero no es continua en el origen: primer filtro del protocolo, y se acaba.

1. **a) Fuera del origen:** composición de $\operatorname{arctg}$ con un cociente de polinomios de denominador no nulo: continua.
2. **a) En el origen, por rectas** $y=mx$ ($x\ne0$): $f(x,mx)=\operatorname{arctg}\frac{mx^2}{(1+m^2)x^2}=\operatorname{arctg}\frac{m}{1+m^2}$, constante. Con $m=0$ da $0$; con $m=1$ da $\operatorname{arctg}\frac12\ne0$. El límite depende de la recta: **no existe** (U pp. 162-163), así que $f$ **no es continua** en $(0,0)$. Es continua en $\mathbb{R}^2\setminus\{(0,0)\}$.
3. **b) Fuera del origen** (cadena: $(\operatorname{arctg}u)'=\frac{1}{1+u^2}$, con $u=\frac{xy}{x^2+y^2}$, $u_x=\frac{y(y^2-x^2)}{(x^2+y^2)^2}$):
$$f_x=\frac{y(y^2-x^2)}{(x^2+y^2)^2+x^2y^2},\qquad f_y=\frac{x(x^2-y^2)}{(x^2+y^2)^2+x^2y^2}.$$
4. **b) En el origen:** $f(h,0)=\operatorname{arctg}0=0$ y $f(0,h)=0$, así que $\frac{\partial f}{\partial x}(0,0)=\frac{\partial f}{\partial y}(0,0)=0$. **Tiene parciales en todo $\mathbb{R}^2$.**
5. **c)** Por el Teorema 5.1 (U p. 191), una función diferenciable es continua. Como $f$ no es continua en $(0,0)$, **no es diferenciable** en $(0,0)$.

**Receta.** Primer paso del protocolo: si la función es discontinua en el punto, no es diferenciable, aunque tenga parciales.

**Error típico.** Calcular el cociente de diferenciabilidad cuando ya se sabe que $f$ es discontinua (trabajo inútil), o creer que «tiene parciales» basta.

*Comentario:* es exactamente el Ejemplo 4.24 de U (p. 172).

sympy: $f(x,mx)=\operatorname{arctg}\frac{m}{m^2+1}$; $f_x$ como arriba.

---

### ★ X pp. 54-55 (Sept 2015, Modelo A, Ej. 6, 3 puntos)

> Sea la función $f$ de $\mathbb{R}^2$ en $\mathbb{R}$ definida por $f(x,y)=\dfrac{x^2-y^2}{\sqrt[3]{x^3+y^3}}$ si $x\ne-y$, $f(x,y)=0$ si $x=-y$. (a) Estudiar la continuidad de $f$. (b) Calcúlese $\frac{\partial f}{\partial x}(0,0)$ y $\frac{\partial f}{\partial y}(0,0)$. (c) Estudiar la diferenciabilidad de $f$ en el punto $(0,0)$. Nota: cada apartado vale 1 punto.

**Idea en una frase.** Factorizar para quitar la «falsa» indeterminación en la recta $x=-y$; después, continua y con parciales, pero el cociente depende de la dirección.

1. **(a) Factorizar:** $x^2-y^2=(x+y)(x-y)$ y $x^3+y^3=(x+y)(x^2-xy+y^2)$. Con la raíz cúbica (que admite negativos), para $x\ne-y$:
$$f=\frac{(x+y)(x-y)}{\sqrt[3]{x+y}\,\sqrt[3]{x^2-xy+y^2}}=\sqrt[3]{(x+y)^2}\;\frac{x-y}{\sqrt[3]{x^2-xy+y^2}}.$$
2. **(a) Puntos con $x\ne-y$:** cociente de funciones continuas con denominador no nulo: continua.
3. **(a) Puntos $(x_0,-x_0)$ con $x_0\ne0$:** $\sqrt[3]{(x+y)^2}\to0$ y la fracción tiende a $\frac{2x_0}{\sqrt[3]{3x_0^2}}$ (número finito, porque $x^2-xy+y^2\to3x_0^2\ne0$). Producto $\to0=f(x_0,-x_0)$: continua.
4. **(a) Origen, polares:** $x^2-xy+y^2=\rho^2(1-\cos\theta\operatorname{sen}\theta)$ y $(x+y)(x-y)=\rho^2(\cos^2\theta-\operatorname{sen}^2\theta)$, luego $f=\rho\,\dfrac{\cos^2\theta-\operatorname{sen}^2\theta}{\sqrt[3]{1-\cos\theta\operatorname{sen}\theta}}$. Como $\cos\theta\operatorname{sen}\theta=\frac12\operatorname{sen}2\theta\in[-\frac12,\frac12]$, el denominador cumple $1-\cos\theta\operatorname{sen}\theta\ge\frac12$, y la fracción está acotada (por $1/\sqrt[3]{1/2}=\sqrt[3]2$). Así $|f|\le\sqrt[3]2\,\rho\to0$ (U p. 165, caso 2): continua. **$f$ es continua en $\mathbb{R}^2$.**
5. **(b)** $f(t,0)=\frac{t^2}{\sqrt[3]{t^3}}=\frac{t^2}{t}=t$, cociente $1$: $\frac{\partial f}{\partial x}(0,0)=1$. $f(0,t)=\frac{-t^2}{t}=-t$: $\frac{\partial f}{\partial y}(0,0)=-1$.
6. **(c) Cociente:** $Q(h,k)=\dfrac{f(h,k)-0-h+k}{\sqrt{h^2+k^2}}$.
7. **(c) Dos caminos.** Por el eje $x$ ($k=0$, $h=t$): $Q=\frac{t-t}{|t|}=0$. Por la recta $k=2h$ con $h=t>0$: $f(t,2t)=\frac{-3t^2}{\sqrt[3]{9}\,t}=-\frac{3}{\sqrt[3]9}\,t=-\sqrt[3]3\,t$ (porque $\frac{3}{\sqrt[3]9}=\frac{\sqrt[3]{27}}{\sqrt[3]9}=\sqrt[3]3$), y
$$Q(t,2t)=\frac{-\sqrt[3]3\,t-t+2t}{\sqrt5\,t}=\frac{1-\sqrt[3]3}{\sqrt5}\approx-0{,}198\ne0.$$
8. **(c) Conclusión:** dos caminos dan límites distintos ($0$ y $\frac{1-\sqrt[3]3}{\sqrt5}$): el límite de $Q$ no existe y $f$ **no es diferenciable** en $(0,0)$.

**Receta.** Para probar que **no** es diferenciable basta un camino en el que $Q$ no tienda a $0$ (aquí, $Q$ es constante y no nula en la recta $k=2h$).

**Error típico.** Decir «no es diferenciable» sin calcular explícitamente el límite de $Q$ por algún camino (hay que mostrarlo).

sympy: $f_x(0,0)=1$, $f_y(0,0)=-1$; $Q(t,2t)=\frac{1-\sqrt[3]3}{\sqrt5}$ para $t>0$.

---

### ★ X pp. 61-63 (Feb 2016, Modelo A, Ej. 6, 3 puntos)

> Sea $f:\mathbb{R}^2\to\mathbb{R}$ la función definida por $f(x,y)=\dfrac{x^2y^2}{x^2+2y^2}$ si $(x,y)\ne(0,0)$, $f(0,0)=0$. (a) Estudie la continuidad de $f$ en $\mathbb{R}^2$. (b) Calcule las derivadas parciales $\frac{\partial f}{\partial x}$ y $\frac{\partial f}{\partial y}$. (c) Estudia la continuidad de las derivadas parciales en el origen. ¿Es diferenciable $f$?

**Idea en una frase.** Aquí sí funciona la condición suficiente: las parciales se pueden acotar y son continuas en el origen.

1. **(a) Fuera del origen:** cociente de polinomios con denominador no nulo: continua.
2. **(a) Origen (emparedado):** $x^2\le x^2+2y^2$, luego $0\le f=y^2\cdot\frac{x^2}{x^2+2y^2}\le y^2\to0$. Continua. **$f$ es continua en $\mathbb{R}^2$.**
3. **(b) Fuera del origen** (regla del cociente):
$f_x=\dfrac{2xy^2(x^2+2y^2)-x^2y^2\cdot2x}{(x^2+2y^2)^2}=\dfrac{4xy^4}{(x^2+2y^2)^2}$, $\quad f_y=\dfrac{2x^2y(x^2+2y^2)-x^2y^2\cdot4y}{(x^2+2y^2)^2}=\dfrac{2x^4y}{(x^2+2y^2)^2}$.
4. **(b) En el origen** (definición): $f(h,0)=0$ y $f(0,h)=0$, así que $f_x(0,0)=f_y(0,0)=0$.
5. **(c) Continuidad de $f_x$ en el origen.** Como $(x^2+2y^2)^2\ge(2y^2)^2=4y^4$: $|f_x|\le\frac{4|x|y^4}{4y^4}=|x|\to0$ (si $y=0$, $f_x=0$ directamente). Así $\lim_{(x,y)\to(0,0)}f_x=0=f_x(0,0)$: continua.
6. **(c) Continuidad de $f_y$.** Como $(x^2+2y^2)^2\ge x^4$: $|f_y|\le\frac{2x^4|y|}{x^4}=2|y|\to0$ (si $x=0$, $f_y=0$). Continua.
7. **(c) Diferenciable:** las parciales existen en todo $\mathbb{R}^2$ y son continuas en $(0,0)$; por la condición suficiente (U p. 192), $f$ **es diferenciable** en $(0,0)$ (y en todo $\mathbb{R}^2$), con $Df(0,0)=0$.

**Receta.** Para ver si una parcial es continua en el origen, **acotar** su valor absoluto usando que el denominador es mayor que cada uno de sus sumandos.

**Error típico.** Copiar mal el denominador al derivar (es $(x^2+2y^2)^2$ en las dos parciales), o probar la continuidad de las parciales solo con rectas $y=mx$ (no basta).

sympy: $f_x=\frac{4xy^4}{(x^2+2y^2)^2}$, $f_y=\frac{2x^4y}{(x^2+2y^2)^2}$.

---

### ★ X pp. 71-72 (Sept 2016, Modelo A, Ej. 6, 3 puntos)

> Sea $f$ la función definida por $f(x,y)=y^3\operatorname{sen}\dfrac{1}{x^2+2y^2}$ si $(x,y)\ne(0,0)$, $f(0,0)=0$. (a) Estudie la continuidad de $f$. (b) Estudie la existencia de derivadas parciales de $f$. (c) Estudie la diferenciabilidad de $f$.

**Idea en una frase.** El seno está acotado y $y^3$ es «de grado 3»: tras dividir por $\rho$ queda $\rho^2$ por algo acotado.

1. **(a) Fuera del origen:** producto y composición de funciones continuas ($x^2+2y^2\ne0$).
2. **(a) Origen:** $|f|\le|y|^3\to0$ (porque $|\operatorname{sen}|\le1$). Continua: **$f$ es continua en $\mathbb{R}^2$.**
3. **(b) Fuera del origen** (cadena: $\frac{\partial}{\partial x}\frac1{x^2+2y^2}=\frac{-2x}{(x^2+2y^2)^2}$, $\frac{\partial}{\partial y}\frac1{x^2+2y^2}=\frac{-4y}{(x^2+2y^2)^2}$):
$f_x=-\dfrac{2xy^3}{(x^2+2y^2)^2}\cos\dfrac1{x^2+2y^2}$, $\quad f_y=3y^2\operatorname{sen}\dfrac1{x^2+2y^2}-\dfrac{4y^4}{(x^2+2y^2)^2}\cos\dfrac1{x^2+2y^2}$.
4. **(b) En el origen:** $f(t,0)=0$, luego $f_x(0,0)=0$. $f(0,t)=t^3\operatorname{sen}\frac1{2t^2}$, cociente $t^2\operatorname{sen}\frac1{2t^2}$ con $|\cdot|\le t^2\to0$: $f_y(0,0)=0$. **Tiene parciales en todo $\mathbb{R}^2$.**
5. **(c) Fuera del origen:** parciales continuas ⇒ diferenciable (U p. 192).
6. **(c) En el origen, cociente:** $Q=\dfrac{k^3\operatorname{sen}\frac1{h^2+2k^2}}{\sqrt{h^2+k^2}}$. Como $|k|\le\sqrt{h^2+k^2}=\rho$: $|Q|\le\frac{|k|^3}{\rho}\le\frac{\rho^3}{\rho}=\rho^2\to0$.
7. **(c) Conclusión:** $\lim_{(h,k)\to(0,0)}Q=0$: $f$ **es diferenciable** en $(0,0)$ y, por tanto, en todo $\mathbb{R}^2$.

**Receta.** $\operatorname{sen}(\text{lo que sea})$ se acota por $1$; si lo que multiplica al seno, dividido por $\rho$, tiende a $0$, el cociente tiende a $0$.

**Error típico.** Calcular bien $\lim_{(h,k)\to(0,0)}Q=0$ y concluir «no diferenciable»: límite $0$ ⇒ **sí** diferenciable.

sympy: $f_y(0,0)=0$; $f_x$, $f_y$ como arriba.

---

### X pp. 122, 124-125 (Examen 5 «elaborado con exámenes de asignaturas similares», Ej. 6) — para practicar

> Estudiar la continuidad, derivabilidad y diferenciabilidad de la función $f(x,y)=\dfrac{x^3+xy^2+3y^4}{x^2+y^2}$ si $(x,y)\ne(0,0)$, $f(0,0)=0$.

1. **Simplificar:** $x^3+xy^2=x(x^2+y^2)$, así que $f=x+\dfrac{3y^4}{x^2+y^2}$ fuera del origen.
2. **Continuidad:** $0\le\frac{3y^4}{x^2+y^2}\le3y^2\to0$, luego $f\to0=f(0,0)$: continua en $\mathbb{R}^2$.
3. **Parciales en el origen:** $f(t,0)=t$ ⇒ $f_x(0,0)=1$; $f(0,t)=3t^2$ ⇒ $f_y(0,0)=0$.
4. **Cociente:** $Q=\frac{f(h,k)-h}{\rho}=\frac{3k^4}{(h^2+k^2)\rho}$; en polares $Q=3\rho\operatorname{sen}^4\theta$, $|Q|\le3\rho\to0$: **diferenciable** en $(0,0)$ (y fuera, por la condición suficiente).

**Receta.** Separar la parte «lineal» ($x$) de la parte que se anula rápido; la parte lineal no afecta a la diferenciabilidad.

sympy: $f_x(0,0)=1$, $f_y(0,0)=0$; $Q=3\rho\operatorname{sen}^4\theta$.

---

### ★ X p. 138 (Feb 2017, 1ª semana, I. Electrónica Industrial y Automática, Ej. 6, 3 puntos)

> Sea $f:\mathbb{R}^2\to\mathbb{R}$ la función dada por $f(x,y)=\dfrac{x^2y^3}{x^4+y^2}$ si $(x,y)\ne(0,0)$, $f(0,0)=1$. Estudiar la continuidad de $f$ en el punto $(0,0)$ (1.5 puntos). Obtener la ecuación del plano tangente a la gráfica de $f$ en el punto $\left(1,1,\frac12\right)$ (1.5 puntos).

**Idea en una frase.** El valor raro $f(0,0)=1$ rompe la continuidad en el origen; en $(1,1)$ la función es «normal» y el plano sale con la receta.

1. **Continuidad en $(0,0)$:** por el eje $x$ ($y=0$, $x\ne0$), $f(x,0)=0$, que tiende a $0$. Si existiera $\lim_{(x,y)\to(0,0)}f$, tendría que valer $0$ (U pp. 162-163), y $0\ne1=f(0,0)$. **No es continua** en $(0,0)$ (y, por el Teorema 5.1, tampoco diferenciable allí).
2. **Punto en la gráfica:** $f(1,1)=\frac{1}{2}$. Correcto.
3. **Diferenciable en $(1,1)$:** cerca de $(1,1)$ la fórmula es un cociente de polinomios con denominador no nulo; parciales continuas (U p. 192).
4. **Parciales** (cociente): $f_x=\dfrac{2xy^3(x^4+y^2)-x^2y^3\cdot4x^3}{(x^4+y^2)^2}$, $f_y=\dfrac{3x^2y^2(x^4+y^2)-x^2y^3\cdot2y}{(x^4+y^2)^2}$. En $(1,1)$: $f_x=\frac{4-4}{4}=0$, $f_y=\frac{6-2}{4}=1$.
5. **Plano** (U (5.2), p. 189): $z=\frac12+0\cdot(x-1)+1\cdot(y-1)$, es decir, $\boxed{z=y-\frac12}$.

**Receta.** Para probar **discontinuidad** basta un camino cuyo límite sea distinto de $f(a,b)$.

**Error típico.** Usar el valor $f(0,0)=1$ para calcular cosas en $(1,1)$, o no comprobar que $f(1,1)=\frac12$.

sympy: $f(1,1)=\frac12$, $\nabla f(1,1)=(0,1)$, $\lim_{x\to0}f(x,0)=0$.

---

## 3. Ejemplos propios (dificultad creciente)

### Propio 1 — Aproximación numérica con la diferencial (fácil)

> Usa la diferencial para estimar $\sqrt{3{,}02^2+3{,}97^2}$ sin calculadora.

1. **Función y punto «cómodo»:** $f(x,y)=\sqrt{x^2+y^2}$ cerca de $(3,4)$, donde $f(3,4)=5$ es exacto.
2. **Diferenciable en $(3,4)$:** $f_x=\frac{x}{\sqrt{x^2+y^2}}$, $f_y=\frac{y}{\sqrt{x^2+y^2}}$, continuas fuera del origen (U p. 192). En $(3,4)$: $\nabla f=\left(\frac35,\frac45\right)$.
3. **Por qué se puede aproximar:** la Def. 5.1 (U p. 189) dice que $f(a+h,b+k)-\big[f(a,b)+Df(a,b)(h,k)\big]$ es muy pequeño comparado con $\|(h,k)\|$. Por eso $f(a+h,b+k)\approx f(a,b)+Df(a,b)(h,k)$ (es tomar la altura del plano tangente).
4. **Incrementos:** $h=0{,}02$, $k=-0{,}03$.
5. **Cálculo:** $f(3{,}02;\,3{,}97)\approx5+\frac35(0{,}02)+\frac45(-0{,}03)=5+0{,}012-0{,}024=4{,}988$.
6. **Comprobación:** el valor exacto es $4{,}98812\ldots$; el error es del orden de $10^{-4}$, mucho menor que $\|(h,k)\|\approx0{,}036$.

**Receta.** $f(a+h,b+k)\approx f(a,b)+f_x(a,b)\,h+f_y(a,b)\,k$, con $(a,b)$ un punto donde todo se calcula a mano.

sympy: aproximación $\frac{1247}{250}=4{,}988$; valor exacto $4{,}988115877$.

### Propio 2 — Continua, con parciales, y no diferenciable (medio)

> Sea $f(x,y)=\dfrac{xy}{\sqrt{x^2+y^2}}$ si $(x,y)\ne(0,0)$, $f(0,0)=0$. Estudia continuidad, parciales y diferenciabilidad en $(0,0)$.

1. **Continua:** en polares $f=\rho\cos\theta\operatorname{sen}\theta$, $|f|\le\rho\to0=f(0,0)$.
2. **Parciales:** en los ejes $f=0$: $\nabla f(0,0)=(0,0)$.
3. **Cociente:** $Q=\frac{f(h,k)}{\rho}=\frac{hk}{h^2+k^2}=\cos\theta\operatorname{sen}\theta=\frac12\operatorname{sen}2\theta$.
4. **Depende de $\theta$:** $0$ por el eje $x$, $\frac12$ por la recta $k=h$. El límite no existe: **no diferenciable** (U p. 165, caso 1).
5. **Moraleja:** pasa los dos filtros del Teorema 5.1 (continua y con parciales) y aun así no es diferenciable. Comparando con E 5.11 ($\sqrt[4]{\ }$ en lugar de $\sqrt{\ }$): allí sobraba $\sqrt\rho$ y aquí no sobra nada. La «frontera» está en el exponente.

sympy: $Q=\frac12\operatorname{sen}2\theta$.

### Propio 3 — Diferenciable con una parcial discontinua (medio-difícil)

> Sea $f(x,y)=x^2\operatorname{sen}\frac1x+y^2$ si $x\ne0$, $f(0,y)=y^2$. Prueba que $f$ es diferenciable en $(0,0)$ pero $\frac{\partial f}{\partial x}$ no es continua en $(0,0)$.

1. **Parciales en el origen:** $\frac{f(h,0)-0}{h}=h\operatorname{sen}\frac1h$, $|\cdot|\le|h|\to0$: $f_x(0,0)=0$. $f(0,h)=h^2$: $f_y(0,0)=\lim_{h\to0}\frac{h^2}{h}=0$.
2. **Cociente:** $|Q|=\frac{|h^2\operatorname{sen}\frac1h+k^2|}{\rho}\le\frac{h^2+k^2}{\rho}=\rho\to0$ (para $h=0$, $Q=\frac{k^2}{|k|}=|k|$, también $\le\rho$). **Diferenciable**.
3. **$f_x$ fuera de la recta $x=0$:** $f_x=2x\operatorname{sen}\frac1x-\cos\frac1x$.
4. **No continua en $(0,0)$:** en los puntos $\left(\frac1{2n\pi},0\right)\to(0,0)$, $\operatorname{sen}(2n\pi)=0$ y $\cos(2n\pi)=1$, así que $f_x=-1$, que no tiende a $f_x(0,0)=0$.
5. **Moraleja:** como E 5.5, pero más corto: la condición suficiente falla y, sin embargo, $f$ es diferenciable.

sympy: $f_x(0,0)=0$; $f_x\left(\frac1{2n\pi},0\right)=-1$.

### Propio 4 — ¿Para qué exponentes es diferenciable? (difícil)

> Sea $\alpha>0$ y $f(x,y)=|xy|^{\alpha}$. ¿Para qué valores de $\alpha$ es $f$ diferenciable en $(0,0)$?

1. **Continua para todo $\alpha>0$:** $|xy|^\alpha\to0$.
2. **Parciales:** $f(h,0)=f(0,h)=0$: $\nabla f(0,0)=(0,0)$ para todo $\alpha$.
3. **Cociente en polares:** $Q=\frac{|xy|^\alpha}{\rho}=\frac{\rho^{2\alpha}|\cos\theta\operatorname{sen}\theta|^\alpha}{\rho}=\rho^{2\alpha-1}\,|\cos\theta\operatorname{sen}\theta|^\alpha$.
4. **Caso $\alpha>\frac12$:** exponente $2\alpha-1>0$ y $|\cos\theta\operatorname{sen}\theta|^\alpha\le1$: $|Q|\le\rho^{2\alpha-1}\to0$. **Diferenciable.** (Ejemplo concreto: $\alpha=1$, $Q=\rho|\cos\theta\operatorname{sen}\theta|$.)
5. **Caso $\alpha=\frac12$:** $Q=|\cos\theta\operatorname{sen}\theta|^{1/2}$: $0$ por el eje $x$, $\frac1{\sqrt2}$ por la recta $k=h$. Depende de $\theta$: **no diferenciable**.
6. **Caso $0<\alpha<\frac12$:** por la recta $k=h=t>0$, $Q=\frac{t^{2\alpha}}{\sqrt2\,t}=\frac{t^{2\alpha-1}}{\sqrt2}\to+\infty$ (exponente negativo): **no diferenciable**.
7. **Respuesta:** diferenciable en $(0,0)$ **si y solo si $\alpha>\frac12$**.

**Receta.** Con parámetros, escribir $Q$ en polares como $\rho^{\text{exponente}}\times(\text{función de }\theta)$ y discutir el signo del exponente: $>0$ diferenciable; $=0$ depende de $\theta$; $<0$ explota.

sympy: $Q=\rho^{2\alpha-1}|\cos\theta\operatorname{sen}\theta|^\alpha$; en $h=k$: $\alpha=\frac14\to\infty$, $\alpha=\frac12\to\frac{\sqrt2}2$, $\alpha=1\to0$.

---

## Notas internas (no pasar al HTML)

- E 5.6: la solución impresa aplica también la condición suficiente con $\frac{\partial f}{\partial y}=-x$ ($y<0$), $x$ ($y\ge0$) y la declara continua; pero $\frac{\partial f}{\partial y}(x_0,0)$ no existe si $x_0\ne0$, así que la condición suficiente no es aplicable (no hay parciales en un entorno). Arriba se resuelve solo por la definición y se explica por qué falla la condición suficiente.
- E 5.5: el argumento impreso de que $\frac{2}{\rho}\cos\theta\cos\frac1{\rho^2}$ no tiene límite no contempla $\cos\theta=0$; arriba se usa la sucesión $x_n=1/\sqrt{2n\pi}$ en el eje $x$, que es rigurosa.
- E 5.10: la solución impresa calcula la parcial con L'Hôpital aplicado varias veces sobre una expresión larga y luego reutiliza el resultado; arriba se reduce todo a $\lim_{u\to0^+}G(u)/u=\frac12$ (dos L'Hôpital simples).
- E 5.9: la continuidad se prueba arriba con la cota $|f|\le|x|+|y|$, válida también en la recta $x=0$ (la solución impresa solo trata la fórmula para $x\ne0$).
- X p. 18 (Sept 2011, = E 5.12): la solución impresa da $\frac{\partial g}{\partial x}(0,0)=1$ (toma $\sqrt{h^2}=h$); en realidad no existe.
- X p. 21 (Feb 2012, = E 5.7): la solución impresa obtiene $4\cos\theta\operatorname{sen}^2\theta$ (al simplificar $\cos^2\theta-1$ pierde el signo); lo correcto es $-4\cos\theta\operatorname{sen}^2\theta$. No afecta a la conclusión.
- X p. 55 (Sept 2015): la solución impresa dice que el límite de $Q$ «no existe; se comprueba de forma inmediata» sin mostrarlo; arriba se da el camino $k=2h$ con límite $\frac{1-\sqrt[3]3}{\sqrt5}$.
- X pp. 62-63 (Feb 2016): la solución impresa escribe el denominador de $f_y$ como $(x^2+4y^2)^2$ (es $(x^2+2y^2)^2$), en el apartado (a) la expresión polar es incorrecta ($\rho^3(\cos^3\theta+\rho\operatorname{sen}^4\theta)/\rho^2$…) y en la polar de $f_y$ intercambia potencias; arriba se usa una cota directa sin polares.
- X p. 72 (Sept 2016): la solución impresa calcula $L=0$ y concluye «no es diferenciable»; lo correcto es **diferenciable**. Además intercambia $\operatorname{sen}$ y $\cos$ en las polares (sin consecuencias, el seno está acotado).
- X pp. 79-80 (Feb 2017 A, $(x^4+3xy^3)/(x^5+y^4)$): no se incluye porque el dominio no es $\mathbb{R}^2$ (el denominador se anula en la curva $x=-\sqrt[5]{y^4}$) y la solución impresa es confusa en ese punto; la conclusión (no continua en el origen, $\frac{\partial f}{\partial x}(0,0)$ no existe, $\frac{\partial f}{\partial y}(0,0)=0$, no diferenciable) es correcta.
- X p. 138: la solución impresa estudia el límite solo por rectas $y=mx$; para probar discontinuidad basta un camino con límite $\ne1$, que es lo que se hace arriba.
- U Teorema 5.1 está enunciado para $f$ en general; para $f:\mathbb{R}^3\to\mathbb{R}$ (E 5.8) se usa con la Def. 5.2.
