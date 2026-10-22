# Soluciones Tema 5.2: Regla de la cadena. Teorema del valor medio

Resolución paso a paso de los ejercicios de **E** de la sección 5.2 de U (Ejercicios 5.13-5.22, E pp. 179-186), de preguntas de examen **X** sobre regla de la cadena, gradiente de composiciones y teorema del valor medio, y de 4 ejemplos propios. Todos los cálculos se han comprobado con sympy (script `v52.py` en el scratchpad de la sesión). Se han leído como imagen X pp. 8, 20, 25, 64, 82, 86, 107, 108, 122, 123, 135, 137, 143, 144; E pp. 179-186 en texto (limpio) y comprobadas con el dossier, que las verificó en imagen.

Páginas: U impresa (= PDF + 2); E impresa = PDF; X = página PDF de `Examenes-resueltos-Calculo.pdf`.

## 0. Herramientas de teoría que se usan

| Clave | Enunciado (resumido) | Dónde |
|---|---|---|
| Reglas de la diferencial | Si $f,g$ son diferenciables en $\bar a$: $f+g$, $cf$, $f\cdot g$ también, y $D(f+g)(\bar a)=Df(\bar a)+Dg(\bar a)$, $D(cf)(\bar a)=c\,Df(\bar a)$, $D(f\cdot g)(\bar a)=Df(\bar a)\,g(\bar a)+f(\bar a)\,Dg(\bar a)$. | U §5.2.2, pp. 194-195 |
| Regla del cociente | Si además $g(\bar a)\ne0$: $f/g$ es diferenciable y $D(f/g)(\bar a)=\dfrac{Df(\bar a)\,g(\bar a)-f(\bar a)\,Dg(\bar a)}{(g(\bar a))^2}$. | U p. 195 |
| Diferencial y gradiente | $Df(\bar a)(\bar h)=\nabla f(\bar a)\cdot\bar h$. Por eso cada regla de la diferencial es la misma regla para el gradiente: $\nabla(fg)=g\nabla f+f\nabla g$, etc. | U Def. 5.3 p. 193; p. 200 |
| Ej. 5.5 | $f=x+2y$, $g=\frac{y}{x+1}$: $Df(0,0)(h,k)=h+2k$, $Dg(0,0)(h,k)=k$. | U p. 195 |
| **Cadena con una variable final** | $\dfrac{d}{dt}f(g(t),h(t))=\dfrac{\partial f}{\partial x}(g(t),h(t))\,g'(t)+\dfrac{\partial f}{\partial y}(g(t),h(t))\,h'(t)$ (Fig. 5.2). | U p. 196; Ej. 5.6 p. 197 |
| **Cadena con dos variables finales** | $\dfrac{\partial}{\partial u}f(g,h)=\dfrac{\partial f}{\partial x}\dfrac{\partial g}{\partial u}+\dfrac{\partial f}{\partial y}\dfrac{\partial h}{\partial u}$ (análoga para $v$). **Regla del diagrama** (Fig. 5.3): tantos sumandos como caminos desde la variable de abajo hasta $f$; cada sumando es el producto de las derivadas a lo largo del camino. | U pp. 197-198 |
| **Regla de la cadena (dos funciones intermedias)** | Si $g,h$ son diferenciables en $\bar a$ y $f$ es diferenciable en $(g(\bar a),h(\bar a))$, entonces $f(g,h)$ es diferenciable en $\bar a$ y $\nabla\big(f(g,h)\big)(\bar a)=\nabla f\big(g(\bar a),h(\bar a)\big)\begin{pmatrix}\nabla g(\bar a)\\ \nabla h(\bar a)\end{pmatrix}$ (fila $1\times2$ por matriz $2\times n$). | U p. 198; Ej. 5.7 y 5.8 p. 199 |
| **Regla de la cadena (general)** | Con $m$ funciones intermedias $g_1,\dots,g_m$: $\nabla\big(f(g_1,\dots,g_m)\big)(\bar a)=\nabla f\big(g_1(\bar a),\dots,g_m(\bar a)\big)\begin{pmatrix}\nabla g_1(\bar a)\\ \vdots\\ \nabla g_m(\bar a)\end{pmatrix}$. Con $n=m=1$ es la regla de la cadena de una variable. | U p. 200 |
| Def. 5.5 (segmento) | Segmento de $\bar a$ a $\bar b$: puntos $(1-\lambda)\bar a+\lambda\bar b$, $\lambda\in[0,1]$. | U p. 200-201 (Fig. 5.4) |
| Def. 5.6 (convexo) | $D$ es convexo si el segmento que une dos puntos cualesquiera de $D$ está contenido en $D$. Discos, bolas, rectas, planos y $\mathbb{R}^2$ lo son; la circunferencia no. | U p. 202 (Fig. 5.5) |
| **Teorema del valor medio** | $f:D\subset\mathbb{R}^2\to\mathbb{R}$ continua y con parciales continuas en $D$. Si el segmento de $(a_1,a_2)$ a $(b_1,b_2)$ está en $D$, existe $(c,d)$ en el segmento con $f(a_1,a_2)-f(b_1,b_2)=\nabla f(c,d)\cdot(a_1-b_1,\,a_2-b_2)$. | U p. 202 |
| **Consecuencias (signo del gradiente)** | En un convexo $A$: si las dos componentes de $\nabla f$ son $>0$, entonces $f(a_1,a_2)>f(b_1,b_2)$ cuando $a_1>b_1$, $a_2>b_2$ (moverse en la dirección de un vector del primer cuadrante aumenta $f$). Si son $<0$, $f(a_1,a_2)<f(b_1,b_2)$ (disminuye). | U pp. 202-203; Ej. 5.9 p. 203 |

**Herramientas de temas anteriores que aparecen:**
- Regla de la cadena de una variable: $(g\circ f)'(a)=g'(f(a))\,f'(a)$ (U §2.2, p. 79).
- Teorema de Rolle (U p. 95), teorema del valor medio de una variable $f'(c)=\frac{f(b)-f(a)}{b-a}$ (U §2.5.3, p. 96) y Proposición 2.4: $f'>0$ en un intervalo ⇒ $f$ estrictamente creciente (U p. 98).
- Gradiente $\nabla f(a,b)=\left(\frac{\partial f}{\partial x}(a,b),\frac{\partial f}{\partial y}(a,b)\right)$ (U §4.3.3, p. 173). Plano tangente $z=f(a,b)+\nabla f(a,b)\cdot(x-a,y-b)$ (U (5.2), p. 189). Condición suficiente de diferenciabilidad: parciales continuas (U p. 192).
- Ángulo entre vectores: $\cos\alpha=\frac{\bar x\cdot\bar y}{\|\bar x\|\,\|\bar y\|}$ (U Def. 4.2, p. 147). Coordenadas polares $x=\rho\cos\theta$, $y=\rho\operatorname{sen}\theta$ (U §4.1, p. 148). Desigualdad triangular $|x+y|\le|x|+|y|$ (U p. 16).

---

### Receta general del tema

> **Derivar una composición** $f(g_1,\dots,g_m)$:
> 1. **Nombrar** las variables intermedias ($x=g(\dots)$, $y=h(\dots)$) y las finales ($t$, o $u,v$).
> 2. **Dibujar el árbol**: $f$ arriba, intermedias en medio, finales abajo.
> 3. **Contar caminos** desde la variable final hasta $f$: cada camino es un sumando = producto de las derivadas que recorre.
> 4. **Evaluar bien**: las parciales de $f$ se evalúan en $(g(\bar a),h(\bar a))$, **no** en $\bar a$.
>
> En forma matricial (cómoda para un punto concreto): $\nabla\big(f(g,h)\big)(\bar a)=\underbrace{\nabla f(g(\bar a),h(\bar a))}_{1\times 2}\ \underbrace{\begin{pmatrix}\nabla g(\bar a)\\\nabla h(\bar a)\end{pmatrix}}_{2\times n}$.
>
> **Comparar valores de $f$ en dos puntos sin calcularlos** (TVM): comprobar que el segmento está en un convexo donde $f$ tiene parciales continuas; entonces $f(\bar a)-f(\bar b)=\nabla f(\bar c)\cdot(\bar a-\bar b)$, y el **signo** o el **tamaño** de ese producto escalar se controla con el gradiente.

---

## 1. Ejercicios de E (orden de dificultad creciente; numeración conservada)

Orden propuesto para aprender: **5.13 → 5.14** (reglas suma/producto/cociente) **→ 5.16 → 5.15** (cadena con una variable final) **→ 5.18 → 5.19** (gradiente de una composición en un punto, forma matricial) **→ 5.17** (cadena con $f$ desconocida) **→ 5.21 → 5.22** (signo del gradiente) **→ 5.20** (demostración con el TVM).

---

### Ejercicio 5.13 (E p. 179)

> Si $f$ y $g$ son funciones de dos variables diferenciables en un punto $(a,b)$, entonces el gradiente en $(a,b)$ de la función producto $fg$ verifica:
> a) $\nabla(fg)(a,b)=\nabla f(a,b)\nabla g(a,b)$. b) $\nabla(fg)(a,b)=\nabla f(a,b)+\nabla g(a,b)$. c) $\nabla(fg)(a,b)=g(a,b)\nabla f(a,b)+f(a,b)\nabla g(a,b)$. d) $\nabla(fg)(a,b)=g(a,b)\nabla f(a,b)-f(a,b)\nabla g(a,b)$.

**Idea en una frase.** Es la regla del producto de una variable, $(fg)'=f'g+fg'$, aplicada a cada derivada parcial.

1. **Por qué vale la regla del producto en cada parcial.** Para calcular $\frac{\partial(fg)}{\partial x}$ se deja $y$ fija y se deriva en $x$ como en una variable (U §4.3, p. 168-169). En una variable, $(fg)'=f'g+fg'$. Así: $\frac{\partial(fg)}{\partial x}=\frac{\partial f}{\partial x}g+f\frac{\partial g}{\partial x}$, y lo mismo en $y$.
2. **Juntar las dos parciales en un vector:** $\nabla(fg)=\left(\frac{\partial f}{\partial x}g+f\frac{\partial g}{\partial x},\ \frac{\partial f}{\partial y}g+f\frac{\partial g}{\partial y}\right)=g\,\nabla f+f\,\nabla g$.
3. **Lo mismo dice U** para la diferencial: $D(f\cdot g)(\bar a)=Df(\bar a)g(\bar a)+f(\bar a)Dg(\bar a)$ (U p. 195), y la diferencial se escribe con el gradiente (U p. 193).
4. **Descartar las demás con un ejemplo numérico:** $f=x$, $g=y$, punto $(2,3)$. Entonces $fg=xy$ y $\nabla(xy)(2,3)=(y,x)=(3,2)$.
   - c): $3\,(1,0)+2\,(0,1)=(3,2)$. Coincide.
   - b): $(1,0)+(0,1)=(1,1)$. No.
   - d): $(3,0)-(0,2)=(3,-2)$. No.
   - a): «producto» de dos vectores fila no da un vector (el producto escalar da el número $0$). No.
5. **Respuesta: c).**

**Receta.** Las reglas de derivación de una variable (suma, producto, cociente) se copian tal cual con $\nabla$ en lugar de $'$; para elegir entre opciones, probar con $f=x$, $g=y$ en un punto sin simetrías.

**Error típico.** Elegir d), que es el **numerador de la regla del cociente**, no la del producto.

sympy: con $f=x^2\operatorname{sen}y$, $g=e^{xy}$, $\nabla(fg)-(g\nabla f+f\nabla g)=(0,0)$.

---

### Ejercicio 5.14 (E pp. 180-181)

> De dos funciones diferenciables $f,g:\mathbb{R}^2\to\mathbb{R}$ se sabe que $f(1,2)=9$, $g(1,2)=2$, $\nabla f(1,2)=(1,9)$ y $\nabla g(1,2)=(2,5)$. Calcula las ecuaciones del plano tangente a las gráficas de las funciones $f+g$, $fg$ y $f/g$ en el punto de su gráfica $(1,2,(f+g)(1,2))$, $(1,2,(fg)(1,2))$ y $(1,2,(f/g)(1,2))$, respectivamente.

**Idea en una frase.** No hace falta conocer las fórmulas de $f$ y $g$: el plano tangente solo necesita el **valor** y el **gradiente** en el punto, y ambos se obtienen con las reglas de la diferencial.

1. **Las tres funciones son diferenciables en $(1,2)$:** suma y producto de diferenciables lo son (U p. 194); el cociente lo es porque $g(1,2)=2\ne0$ (U p. 195). Por tanto tienen plano tangente $z=h(1,2)+\nabla h(1,2)\cdot(x-1,y-2)$ (U (5.2), p. 189).
2. **Suma.** Valor: $9+2=11$. Gradiente: $\nabla(f+g)=\nabla f+\nabla g=(1,9)+(2,5)=(3,14)$.
   $$z=11+3(x-1)+14(y-2).$$
3. **Producto.** Valor: $9\cdot2=18$. Gradiente (regla del producto, Ej. 5.13): $\nabla(fg)=g\nabla f+f\nabla g=2(1,9)+9(2,5)=(2,18)+(18,45)=(20,63)$.
   $$z=18+20(x-1)+63(y-2).$$
4. **Cociente.** Valor: $9/2$. Gradiente (U p. 195): $\nabla(f/g)=\dfrac{g\nabla f-f\nabla g}{g^2}=\dfrac{2(1,9)-9(2,5)}{4}=\dfrac{(2,18)-(18,45)}{4}=\dfrac{(-16,-27)}{4}=\left(-4,-\tfrac{27}{4}\right)$.
   $$z=\tfrac92-4(x-1)-\tfrac{27}{4}(y-2).$$

**Receta.** Plano tangente de una combinación: (1) valor en el punto; (2) gradiente con la regla de la suma/producto/cociente; (3) $z=\text{valor}+\nabla\cdot(x-a,y-b)$.

**Error típico.** En el producto, multiplicar cada gradiente por **su propia** función ($f\nabla f$…) en lugar de **la otra** ($g\nabla f+f\nabla g$); en el cociente, olvidar dividir por $g^2$ o cambiar el orden de la resta.

sympy: suma $(3,14)$, producto $(20,63)$, cociente $(-4,-\frac{27}{4})$.

---

### Ejercicio 5.16 (E p. 182)

> Sean $f$ y $h$ las funciones dadas por $f(x,y)=x^2+\cos y$ y $h(x)=e^{-x}$. Se pide calcular, aplicando la regla de la cadena, la derivada respecto de $x$ de la composición $f(x,h(x))$.

**Idea en una frase.** La primera entrada de $f$ es «la propia $x$»: se ve como la función $g(x)=x$, con derivada $1$ (U Ej. 5.7, p. 199).

1. **Escribir la composición en la forma de U:** $f(g(x),h(x))$ con $g(x)=x$ y $h(x)=e^{-x}$. Solo hay **una** variable final ($x$) y **dos** intermedias.
2. **Ingredientes:** $\nabla f(x,y)=(2x,\,-\operatorname{sen}y)$; $g'(x)=1$; $h'(x)=-e^{-x}$ (cadena de una variable, U p. 79).
3. **Evaluar $\nabla f$ en las intermedias** $(g(x),h(x))=(x,e^{-x})$: $\nabla f(x,e^{-x})=(2x,\,-\operatorname{sen}e^{-x})$.
4. **Regla de la cadena** (U p. 198, con $n=1$):
$$\frac{d}{dx}f(x,h(x))=(2x,\,-\operatorname{sen}e^{-x})\begin{pmatrix}1\\-e^{-x}\end{pmatrix}=2x+e^{-x}\operatorname{sen}(e^{-x}).$$
5. **Comprobación sustituyendo:** $f(x,e^{-x})=x^2+\cos(e^{-x})$, derivada $2x-\operatorname{sen}(e^{-x})\cdot(-e^{-x})$: lo mismo.

**Receta.** Si una entrada de $f$ es la propia variable, tratarla como $g(x)=x$, $g'=1$: $\frac{d}{dx}f(x,h(x))=f_x(x,h(x))+f_y(x,h(x))\,h'(x)$.

**Error típico.** Olvidar el sumando $f_x$ («porque $x$ no es una función»), o evaluar $\operatorname{sen}y$ en $y$ en lugar de en $y=h(x)=e^{-x}$.

sympy: $2x+e^{-x}\operatorname{sen}(e^{-x})$.

---

### Ejercicio 5.15 (E pp. 181-182)

> Sean las funciones dadas por $f(x,y)=x(1-y^2)-y$, $x(t)=e^{2t}$, $y(t)=\frac1t$. A partir de ellas se define $F$ mediante $F(t)=f(x(t),y(t))$. Se pide calcular la derivada de $F(t)$ respecto a $t$ mediante dos procedimientos: 1) sustitución de las expresiones de $x(t)$ e $y(t)$ y derivación posterior y 2) aplicando la regla de la cadena.

**Idea en una frase.** Dos caminos al mismo resultado: sustituir y derivar en una variable, o sumar «derivada de $f$ por derivada de la intermedia» por cada camino del árbol.

**Procedimiento 1 (sustituir).**
1. $F(t)=e^{2t}\left(1-\frac1{t^2}\right)-\frac1t$ (válido para $t\ne0$).
2. Regla del producto y de la cadena de una variable (U p. 79): $\left(e^{2t}\right)'=2e^{2t}$, $\left(1-t^{-2}\right)'=2t^{-3}$, $\left(-t^{-1}\right)'=t^{-2}$.
3. $F'(t)=2e^{2t}\left(1-\frac1{t^2}\right)+e^{2t}\cdot\frac2{t^3}+\frac1{t^2}=2e^{2t}\left(1-\frac1{t^2}+\frac1{t^3}\right)+\frac1{t^2}$.

**Procedimiento 2 (regla de la cadena).**
1. **Árbol:** $f$ arriba; $x$, $y$ en medio; $t$ abajo. Dos caminos de $t$ a $f$ ⇒ dos sumandos (U p. 196):
$$F'(t)=\frac{\partial f}{\partial x}(x(t),y(t))\,x'(t)+\frac{\partial f}{\partial y}(x(t),y(t))\,y'(t).$$
2. **Parciales de $f$:** $\frac{\partial f}{\partial x}=1-y^2$; $\frac{\partial f}{\partial y}=-2xy-1$.
3. **Derivadas de las intermedias:** $x'(t)=2e^{2t}$, $y'(t)=-\frac1{t^2}$.
4. **Sustituir $x=e^{2t}$, $y=\frac1t$ en las parciales** (paso que más se olvida):
$$F'(t)=\left(1-\tfrac1{t^2}\right)2e^{2t}+\left(-\tfrac{2e^{2t}}{t}-1\right)\left(-\tfrac1{t^2}\right)=2e^{2t}\left(1-\tfrac1{t^2}\right)+\tfrac{2e^{2t}}{t^3}+\tfrac1{t^2}.$$
5. **Coincide** con el procedimiento 1.

**Receta.** $\frac{d}{dt}f(x(t),y(t))=f_x\,x'+f_y\,y'$, con $f_x,f_y$ evaluadas en $(x(t),y(t))$; al final todo debe quedar en función de $t$.

**Error típico.** Dejar el resultado mezclando $x$, $y$ y $t$ (sin sustituir), o equivocarse de signo en $y'(t)=-1/t^2$.

sympy: ambos procedimientos dan $2e^{2t}\left(1-\frac1{t^2}+\frac1{t^3}\right)+\frac1{t^2}$ (diferencia $0$).

---

### Ejercicio 5.18 (E pp. 183-184)

> Sean $f,g,h$ las funciones dadas por $f(x,y)=x-y^2$, $g(u,v)=u+uv$ y $h(u,v)=\operatorname{tg}u$. ¿Cuál es el gradiente de $f(g,h)$ en $(u,v)=(0,0)$?

**Idea en una frase.** Gradiente de la composición = (gradiente de $f$ en el punto imagen) × (matriz con los gradientes de $g$ y $h$ en el punto de partida).

1. **Fórmula** (U p. 198): $\nabla\big(f(g,h)\big)(0,0)=\nabla f\big(g(0,0),h(0,0)\big)\begin{pmatrix}\nabla g(0,0)\\\nabla h(0,0)\end{pmatrix}$.
2. **Punto imagen:** $g(0,0)=0+0=0$, $h(0,0)=\operatorname{tg}0=0$. Hay que evaluar $\nabla f$ en $(0,0)$ (aquí coincide con el de partida por casualidad).
3. **Gradiente de $f$:** $\nabla f(x,y)=(1,-2y)$, así que $\nabla f(0,0)=(1,0)$.
4. **Gradientes de $g$ y $h$:** $\nabla g(u,v)=(1+v,\,u)\Rightarrow\nabla g(0,0)=(1,0)$; $\nabla h(u,v)=\left(\frac1{\cos^2u},\,0\right)\Rightarrow\nabla h(0,0)=(1,0)$.
5. **Producto fila × matriz:**
$$(1,0)\begin{pmatrix}1&0\\1&0\end{pmatrix}=(1\cdot1+0\cdot1,\ 1\cdot0+0\cdot0)=(1,0).$$
6. **Comprobación sustituyendo:** $f(g,h)=u+uv-\operatorname{tg}^2u$; en $(0,0)$: $\frac{\partial}{\partial u}=1+v-2\operatorname{tg}u\frac1{\cos^2u}=1$, $\frac{\partial}{\partial v}=u=0$.

**Receta.** (1) Calcular el punto imagen $(g(\bar a),h(\bar a))$; (2) $\nabla f$ **allí**; (3) gradientes de $g,h$ en $\bar a$ como filas de una matriz; (4) multiplicar fila por matriz.

**Error típico.** Evaluar $\nabla f$ en $\bar a$ en lugar de en $(g(\bar a),h(\bar a))$ (aquí no se nota porque ambos son $(0,0)$; en el Ej. 5.19 sí).

sympy: $(1,0)$.

---

### Ejercicio 5.19 (E pp. 184-185)

> Calcula el gradiente en $(u,v)=(1,0)$ de $f(g(u,v),h(u,v),k(u,v))$ para $f(x,y,z)=3x+y+z^2$, $g(u,v)=uv$, $h(u,v)=\operatorname{sen}u+3$ y $k(u,v)=e^u$.

**Idea en una frase.** Igual que 5.18 pero con **tres** intermedias: la matriz tiene tres filas (U p. 200).

1. **Fórmula general** (U p. 200), con $m=3$, $n=2$: $\nabla\big(f(g,h,k)\big)(1,0)=\nabla f\big(g(1,0),h(1,0),k(1,0)\big)\begin{pmatrix}\nabla g(1,0)\\\nabla h(1,0)\\\nabla k(1,0)\end{pmatrix}$ (fila $1\times3$ por matriz $3\times2$ = fila $1\times2$).
2. **Punto imagen:** $g(1,0)=0$, $h(1,0)=\operatorname{sen}1+3$, $k(1,0)=e$.
3. **$\nabla f$ allí:** $\nabla f(x,y,z)=(3,1,2z)\Rightarrow\nabla f(0,\,3+\operatorname{sen}1,\,e)=(3,1,2e)$.
4. **Gradientes en $(1,0)$:** $\nabla g=(v,u)=(0,1)$; $\nabla h=(\cos u,0)=(\cos1,0)$; $\nabla k=(e^u,0)=(e,0)$.
5. **Producto:**
$$(3,1,2e)\begin{pmatrix}0&1\\\cos1&0\\e&0\end{pmatrix}=\big(3\cdot0+1\cdot\cos1+2e\cdot e,\ 3\cdot1+0+0\big)=(\cos1+2e^2,\ 3).$$

**Receta.** Matriz de la cadena: **una fila por cada función intermedia**, **una columna por cada variable final**.

**Error típico.** Usar $z=k(1,0)$ mal: escribir $2z=2$ (evaluando en $u=1$ sin aplicar $k$) en lugar de $2z=2e$.

sympy: $(\cos1+2e^2,\ 3)$.

---

### Ejercicio 5.17 (E p. 183)

> Sea la función $z$ dada por $z(u,v)=f(u-2v,\,2v-u)$, donde $f:\mathbb{R}^2\to\mathbb{R}$ es una función diferenciable, demuestra que $2\dfrac{\partial z}{\partial u}+\dfrac{\partial z}{\partial v}=0$.

**Idea en una frase.** No se conoce $f$, pero la regla de la cadena expresa $z_u$ y $z_v$ en términos de $f_x$ y $f_y$; al combinarlas, se cancelan.

1. **Intermedias:** $x(u,v)=u-2v$, $y(u,v)=2v-u$ (diferenciables: polinomios). $f$ es diferenciable por hipótesis, así que se puede aplicar la regla de la cadena (U p. 198).
2. **Derivadas de las intermedias:** $\frac{\partial x}{\partial u}=1$, $\frac{\partial x}{\partial v}=-2$, $\frac{\partial y}{\partial u}=-1$, $\frac{\partial y}{\partial v}=2$.
3. **Árbol:** de $u$ a $z$ hay dos caminos (por $x$ y por $y$); igual desde $v$ (U p. 198):
$$\frac{\partial z}{\partial u}=\frac{\partial f}{\partial x}\cdot1+\frac{\partial f}{\partial y}\cdot(-1)=f_x-f_y,\qquad \frac{\partial z}{\partial v}=\frac{\partial f}{\partial x}\cdot(-2)+\frac{\partial f}{\partial y}\cdot2=-2f_x+2f_y,$$
con $f_x,f_y$ evaluadas en $(u-2v,\,2v-u)$.
4. **Combinar:** $2(f_x-f_y)+(-2f_x+2f_y)=0$. Queda demostrado.
5. **Comprobación con un ejemplo** (no es demostración, solo confianza): $f(x,y)=x^2$: $z=(u-2v)^2$, $z_u=2(u-2v)$, $z_v=-4(u-2v)$, y $2z_u+z_v=0$.

**Receta.** Ecuaciones con una $f$ «genérica»: nombrar las intermedias, escribir cada derivada de $z$ como combinación de $f_x$ y $f_y$, sustituir en la expresión pedida y simplificar.

**Error típico.** Pensar que hace falta conocer $f$, o escribir $\frac{\partial z}{\partial u}=f_x$ (olvidando el camino por $y$).

sympy: con $f$ genérica, $2z_u+z_v$ se simplifica a $0$.

---

### Ejercicio 5.21 (E p. 185)

> Indica cómo se comportará la función $f(x,y)=-x-y$ si nos movemos en la dirección de vectores del primer cuadrante.

**Idea en una frase.** El gradiente $(-1,-1)$ tiene las dos componentes negativas en todo el plano (convexo): $f$ **disminuye**.

1. **Gradiente:** $\nabla f(x,y)=(-1,-1)$, continuo; ambas componentes $<0$ en todo $\mathbb{R}^2$.
2. **$\mathbb{R}^2$ es convexo** (U p. 202).
3. **Consecuencia del TVM** (U p. 202): si $a_1>b_1$, $a_2>b_2$, entonces $f(a_1,a_2)<f(b_1,b_2)$. Pasar de $(b_1,b_2)$ a $(a_1,a_2)$ es moverse con el vector $(a_1-b_1,a_2-b_2)$, que está en el primer cuadrante.
4. **Comprobación directa:** $f(\bar b+\bar w)-f(\bar b)=-w_1-w_2<0$ si $w_1,w_2\ge0$ y no ambos nulos.
5. **Respuesta:** **decrece** al movernos en la dirección de cualquier vector del primer cuadrante.

**Receta.** Signo de las dos componentes del gradiente en un convexo: ambas $>0$ ⇒ crece hacia el primer cuadrante; ambas $<0$ ⇒ decrece.

**Error típico.** Mirar solo una componente del gradiente.

---

### Ejercicio 5.22 (E pp. 185-186)

> Encuentra la afirmación correcta para la función $f(x,y)=x^2-y^3$ si nos movemos en la dirección de vectores del primer cuadrante: a) Los valores de $f$ decrecen. b) Los valores de $f$ crecen. c) Los valores de $f$ en el interior del segundo cuadrante decrecen. d) Ninguna de las anteriores.

**Idea en una frase.** El signo del gradiente cambia de una zona a otra; hay que buscar una zona **convexa** donde las dos componentes tengan el mismo signo.

1. **Gradiente:** $\nabla f(x,y)=(2x,\,-3y^2)$ (continuo).
2. **Signos:** $-3y^2<0$ si $y\ne0$; $2x<0$ si $x<0$. En el **interior del segundo cuadrante** $\{x<0,\ y>0\}$ ambas son estrictamente negativas.
3. **Ese conjunto es convexo:** si dos puntos tienen $x<0$ e $y>0$, cualquier punto del segmento, $(1-\lambda)\bar a+\lambda\bar b$, es una media de números negativos (en $x$) y de positivos (en $y$), así que sigue en el conjunto (Def. 5.6, U p. 202).
4. **Consecuencia del TVM** (U p. 202): allí $f$ **decrece** en la dirección de los vectores del primer cuadrante. **c) es cierta.** Ejemplo: $f(-2,1)=4-1=3$ y $f(-1,2)=1-8=-7$: al sumar $(1,1)$, baja.
5. **a) es falsa:** de $\left(\frac12,\frac12\right)$ a $(2,1)$ nos movemos con $\left(\frac32,\frac12\right)$, del primer cuadrante, y $f$ pasa de $\frac14-\frac18=\frac18$ a $4-1=3$: **sube**.
6. **b) es falsa:** el ejemplo del paso 4 baja. **d)** es falsa porque c) es cierta.
7. **Respuesta: c).**

**Receta.** Para «¿crece o decrece hacia el primer cuadrante?»: estudiar el signo de cada componente de $\nabla f$ por zonas, quedarse con una zona convexa con signos iguales; para desmentir una afirmación global, basta un par de puntos.

**Error típico.** Concluir «decrece» en todo $\mathbb{R}^2$ porque la segunda componente es siempre $\le0$, sin mirar la primera.

sympy: $f(2,1)=3>f\left(\frac12,\frac12\right)=\frac18$.

---

### Ejercicio 5.20 (E p. 185)

> El teorema del valor medio para funciones de una variable se utiliza para demostrar que una función con derivada cero en un intervalo es constante en ese intervalo. Muestra que una función continua $f:\mathbb{R}^2\to\mathbb{R}$ con gradiente nulo en un conjunto convexo es constante en ese conjunto.

**Idea en una frase.** El TVM dice que la diferencia de valores es «gradiente por desplazamiento»; si el gradiente es cero, la diferencia es cero.

1. **Ejemplo concreto primero.** $f(x,y)=7$ en el disco unidad: $\nabla f=(0,0)$ y, en efecto, es constante. La pregunta es si **solo** pasa con funciones así.
2. **Hipótesis del TVM** (U p. 202): sea $A$ el convexo. Como $\nabla f=(0,0)$ en todo $A$, las parciales existen y valen siempre $0$; una función constante es continua, así que **las parciales son continuas** en $A$. Además $f$ es continua.
3. **Tomar dos puntos cualesquiera** $\bar a,\bar b\in A$. Por ser $A$ convexo, el segmento que los une está en $A$ (Def. 5.6, U p. 202).
4. **Aplicar el TVM:** existe $\bar c$ en ese segmento con $f(\bar a)-f(\bar b)=\nabla f(\bar c)\cdot(\bar a-\bar b)$.
5. **Usar la hipótesis:** $\bar c\in A$, así que $\nabla f(\bar c)=(0,0)$ y $f(\bar a)-f(\bar b)=(0,0)\cdot(\bar a-\bar b)=0$.
6. **Conclusión:** $f(\bar a)=f(\bar b)$ para todo par de puntos de $A$: **$f$ es constante en $A$**. (Si se prefiere por reducción al absurdo: suponer $f(\bar a)\ne f(\bar b)$ y llegar a $f(\bar a)-f(\bar b)=0$.)
7. **Por qué importa «convexo»:** el TVM necesita el segmento dentro del conjunto. En un conjunto formado por dos discos separados, $f=0$ en uno y $f=1$ en el otro tiene gradiente nulo y **no** es constante.

**Receta.** «Gradiente nulo en un convexo ⇒ constante»: TVM en el segmento entre dos puntos arbitrarios.

**Error típico.** Olvidar justificar que el segmento está en el conjunto (es ahí donde se usa la convexidad).

---

## 2. Preguntas de examen (X)

Ordenadas de corta a larga. Las de mayor interés para este tema llevan ★. Las de una variable son **refuerzo**: la regla de la cadena de varias variables con $n=m=1$ es exactamente la de una variable (U p. 200).

---

### ★ X p. 20 (Feb 2012, 1ª semana, Ing. Mecánica, Modelo A, P4, 1 punto)

> Sea $f:\mathbb{R}^2\to\mathbb{R}$ una función continua y con derivadas parciales continuas en $\mathbb{R}^2$. Defina gradiente de $f$ en un punto. Calcule el gradiente de $f(x,y)=x^2e^{x+y}$ en el punto $(x_0,y_0)=(1,-1)$.

**Idea en una frase.** Producto ($x^2$ por $e^{x+y}$) y cadena en la exponencial.

1. **Definición** (U p. 173): $\nabla f(x_0,y_0)=\left(\frac{\partial f}{\partial x}(x_0,y_0),\ \frac{\partial f}{\partial y}(x_0,y_0)\right)$.
2. $\frac{\partial f}{\partial x}=2x\,e^{x+y}+x^2e^{x+y}$ (producto; la derivada de $e^{x+y}$ respecto a $x$ es $e^{x+y}\cdot1$).
3. $\frac{\partial f}{\partial y}=x^2e^{x+y}$ ($x^2$ es constante respecto a $y$).
4. En $(1,-1)$: $e^{0}=1$, así que $\nabla f(1,-1)=(2+1,\ 1)=(3,1)$.

**Receta.** Producto + cadena: derivar el factor «de fuera» y multiplicar por la derivada interior.

**Error típico.** Olvidar el término $2xe^{x+y}$ del producto.

sympy: $(3,1)$.

---

### ★ X p. 82 (Feb 2017, Ing. Mecánica, Modelo B, P4, 1 punto)

> Determine el gradiente de la función $f(x,y)=(x+y^3)\cos(\pi x^2)$ en el punto $(1,0)$.

1. $\frac{\partial f}{\partial x}=1\cdot\cos(\pi x^2)+(x+y^3)\cdot\big(-\operatorname{sen}(\pi x^2)\big)\cdot2\pi x$ (producto y cadena: la derivada interior de $\pi x^2$ es $2\pi x$).
2. $\frac{\partial f}{\partial y}=3y^2\cos(\pi x^2)$.
3. En $(1,0)$: $\cos\pi=-1$, $\operatorname{sen}\pi=0$: $\nabla f(1,0)=(-1-0,\ 0)=(-1,0)$.

**Receta.** Igual que la anterior; al evaluar, simplificar primero $\cos\pi$ y $\operatorname{sen}\pi$.

**Error típico.** Olvidar el factor $2\pi x$ de la derivada interior.

sympy: $(-1,0)$.

---

### ★ X p. 8 (Sept 2010, Grado en Ing. Eléctrica, P4, 1 punto)

> Calcule el gradiente de la función $f(x,y)=y\operatorname{tg}e^x+\cos^2(x+y)$.

1. **Primer sumando, respecto a $x$:** $y$ es constante; cadena $\operatorname{tg}(e^x)$: $(\operatorname{tg}u)'=\frac1{\cos^2u}$ y $u'=e^x$. Da $y\,\frac{e^x}{\cos^2e^x}$.
2. **Segundo sumando:** $\cos^2(x+y)=\big(\cos(x+y)\big)^2$; cadena doble: $2\cos(x+y)\cdot\big(-\operatorname{sen}(x+y)\big)\cdot1$. Respecto a $y$ la derivada interior también es $1$.
3. **Respecto a $y$, primer sumando:** $\operatorname{tg}e^x$ (no depende de $y$).
$$\nabla f(x,y)=\left(\frac{y\,e^x}{\cos^2e^x}-2\cos(x+y)\operatorname{sen}(x+y),\ \ \operatorname{tg}e^x-2\cos(x+y)\operatorname{sen}(x+y)\right)$$
(válido donde $\cos e^x\ne0$). Equivalentemente, $-2\cos(x+y)\operatorname{sen}(x+y)=-\operatorname{sen}(2x+2y)$.

**Receta.** Potencia de una función: $(u^2)'=2u\,u'$; tangente: $(\operatorname{tg}u)'=\frac{u'}{\cos^2u}$.

**Error típico.** Derivar $\cos^2(x+y)$ como $-\operatorname{sen}^2(x+y)$ o como $2\cos(x+y)$ (olvidando la derivada del coseno).

sympy: $\left(\frac{ye^x}{\cos^2e^x}-\operatorname{sen}(2x+2y),\ \operatorname{tg}e^x-\operatorname{sen}(2x+2y)\right)$.

---

### ★ X pp. 107-108 (I. Electrónica Industrial y Automática, examen sin fecha «Electrónica 4», Ej. 6, 3 puntos)

> Para la función dada por $g(x,y)=x^2y$:
> - Calcule el dominio de $f(x,y)=\ln(g(x,y))$.
> - Calcule los gradientes de $f$ y $g$ en el punto $(1,1)$.
> - Calcule el coseno del ángulo formado por los vectores gradientes del apartado anterior.

**Idea en una frase.** $f=\ln\circ g$, así que por la regla de la cadena $\nabla f=\frac{1}{g}\nabla g$: los dos gradientes son **paralelos** y apuntan igual.

1. **Dominio.** $\ln s$ solo existe si $s>0$: hace falta $x^2y>0$. Como $x^2\ge0$, eso es $x\ne0$ e $y>0$:
$$D=\{(x,y)\in\mathbb{R}^2:\ x\ne0,\ y>0\}$$
(semiplano superior abierto sin el eje $y$).
2. **Gradiente de $g$:** $\nabla g=(2xy,\ x^2)$; $\nabla g(1,1)=(2,1)$.
3. **Gradiente de $f$ por la cadena** (U p. 200 con una intermedia, $m=1$: $f=\varphi(g)$ con $\varphi(s)=\ln s$): $\nabla f=\varphi'(g)\,\nabla g=\frac{1}{x^2y}(2xy,\ x^2)=\left(\frac2x,\ \frac1y\right)$. En $(1,1)$: $\nabla f(1,1)=(2,1)$.
4. **Coseno del ángulo** (U Def. 4.2, p. 147): $\cos\alpha=\frac{(2,1)\cdot(2,1)}{\sqrt5\,\sqrt5}=\frac55=1$. El ángulo es $0$.
5. **Explicación:** como $\nabla f=\frac1g\nabla g$ con $g>0$ en el dominio, los dos gradientes son paralelos y del mismo sentido **en todo punto** del dominio (en $(1,1)$ además coinciden porque $g(1,1)=1$).

**Receta.** $\nabla\big(\varphi(g)\big)=\varphi'(g)\,\nabla g$ (cadena con una sola intermedia). Para el dominio de $\ln(\cdot)$: argumento $>0$.

**Error típico.** Poner como dominio $x>0$, $y>0$ (olvidando que $x^2>0$ también si $x<0$), o incluir $x=0$.

sympy: $\nabla g(1,1)=(2,1)$, $\nabla f=\left(\frac2x,\frac1y\right)$, $\nabla f(1,1)=(2,1)$, $\cos\alpha=1$.

---

### ★ X p. 143 (Sept 2018, I. Electrónica Industrial y Automática, Ej. 6, 3 puntos)

> Para la función dada por $f(x,y)=\ln(36-x^2-y^2)$:
> - (1 punto) Determine y dibuje su dominio.
> - (1 punto) Calcule el gradiente de $f$ en el punto $(1,5)$.
> - (1 punto) Calcule $f\circ g$ donde $g(\rho,\theta)=(\rho\cos\theta,\rho\operatorname{sen}\theta)$.

**Idea en una frase.** $f$ solo depende de la distancia al origen; en polares queda una función de $\rho$ solo.

1. **Dominio:** $36-x^2-y^2>0\iff x^2+y^2<36$: **disco abierto** de centro $(0,0)$ y radio $6$ (sin la circunferencia frontera). Dibujo: círculo de radio 6 con el borde a trazos.
2. **Gradiente:** $\frac{\partial f}{\partial x}=\frac{-2x}{36-x^2-y^2}$, $\frac{\partial f}{\partial y}=\frac{-2y}{36-x^2-y^2}$ (cadena con $\ln$). En $(1,5)$: $36-1-25=10$, así que $\nabla f(1,5)=\left(-\frac2{10},-\frac{10}{10}\right)=\left(-\frac15,-1\right)$. (El punto está en el dominio: $1+25<36$.)
3. **Composición con polares:** sustituir $x=\rho\cos\theta$, $y=\rho\operatorname{sen}\theta$ y usar $\cos^2\theta+\operatorname{sen}^2\theta=1$:
$$f(g(\rho,\theta))=\ln\big(36-\rho^2\cos^2\theta-\rho^2\operatorname{sen}^2\theta\big)=\ln(36-\rho^2),$$
definida para $0\le\rho<6$ y cualquier $\theta$.
4. **Comprobación con la regla de la cadena** (opcional): $\frac{\partial}{\partial\theta}f(g)=f_x\cdot(-\rho\operatorname{sen}\theta)+f_y\cdot\rho\cos\theta=\frac{-2\rho\cos\theta(-\rho\operatorname{sen}\theta)-2\rho\operatorname{sen}\theta\,\rho\cos\theta}{36-\rho^2}=0$: no depende de $\theta$, como se ve en la fórmula.

**Receta.** «Calcule $f\circ g$» pide **sustituir** (no derivar): poner $g$ dentro de $f$ y simplificar.

**Error típico.** Incluir la frontera $x^2+y^2=36$ en el dominio ($\ln0$ no existe).

sympy: $\nabla f(1,5)=\left(-\frac15,-1\right)$; $f(g)=\ln(36-\rho^2)$; $\partial_\theta f(g)=0$.

---

### ★ X p. 86 (Sept 2017, Ing. Mecánica, Modelo A, P4, 1 punto)

> Sea $f:\mathbb{R}^2\to\mathbb{R}$ una función tal que las derivadas parciales son positivas en cualquier $(x,y)\in\mathbb{R}^2$. Razone si es cierto que si para cada par de puntos $(x,y)$ y $(x_0,y_0)$ con $x>x_0$, $y>y_0$, se tiene que cumplir: $f(x,y)>f(x_0,y_0)$.
> Nota: se recomienda aplicar el teorema del valor medio.

**Idea en una frase.** Ir de $(x_0,y_0)$ a $(x,y)$ es avanzar en las dos coordenadas; si $f$ crece al avanzar en cada una, sube.

**Lo que hay que escribir en el examen (con el TVM, suponiendo parciales continuas, como pide el TVM de U):**
1. $\mathbb{R}^2$ es convexo (U p. 202), así que el segmento que une $(x,y)$ y $(x_0,y_0)$ está en $\mathbb{R}^2$.
2. TVM (U p. 202): existe $(c,d)$ en el segmento con
$$f(x,y)-f(x_0,y_0)=\frac{\partial f}{\partial x}(c,d)\,(x-x_0)+\frac{\partial f}{\partial y}(c,d)\,(y-y_0).$$
3. Los cuatro factores son positivos: las parciales por hipótesis, $x-x_0>0$ e $y-y_0>0$ por enunciado. La suma es $>0$.
4. **Es cierto:** $f(x,y)>f(x_0,y_0)$.

**Otra forma, que no necesita que las parciales sean continuas (solo el TVM de una variable):**
1. Escribir la diferencia en dos pasos, primero en horizontal y luego en vertical:
$$f(x,y)-f(x_0,y_0)=\underbrace{\big[f(x,y)-f(x_0,y)\big]}_{\text{solo cambia }x}+\underbrace{\big[f(x_0,y)-f(x_0,y_0)\big]}_{\text{solo cambia }y}.$$
2. $\varphi(s)=f(s,y)$ ($y$ fija) es derivable con $\varphi'(s)=\frac{\partial f}{\partial x}(s,y)>0$, así que es estrictamente creciente (U Prop. 2.4, p. 98): como $x>x_0$, el primer corchete es $>0$.
3. Igual con $\psi(s)=f(x_0,s)$: $\psi'(s)=\frac{\partial f}{\partial y}(x_0,s)>0$ y $y>y_0$: el segundo corchete es $>0$.
4. La suma de dos positivos es positiva. (Si $f$ tuviera varias componentes, cada una con parciales positivas, se razona igual con cada componente.)

**Receta.** «Parciales positivas ⇒ $f$ crece hacia el primer cuadrante»: TVM en el segmento (en un convexo) o dos pasos paralelos a los ejes con el TVM de una variable.

**Error típico.** Responder «cierto» sin citar la convexidad, o creer que basta con que $x>x_0$ (si solo una coordenada aumenta y la otra disminuye, no se puede concluir nada).

Ejemplo numérico: $f=x^3+y^3+x+y$ tiene parciales $3x^2+1>0$, $3y^2+1>0$; $f(-1,-2)=-1-8-1-2=-12$ y $f(0,0)=0$: al pasar de $(-1,-2)$ a $(0,0)$ (las dos coordenadas aumentan), sube.

---

### X p. 25 (Sept 2012, original, Ing. Mecánica, Modelo A, P1, 1 punto) — refuerzo de una variable

> Sea $f$ una función derivable y que verifica $f(0)=1$ y $f'(0)=-2$ y sea $g$ una función definida en $\mathbb{R}$. Calcule, aplicando la regla de la cadena, $g'(0)$ para $g(x)=f^2(\operatorname{sen}(x))$.

1. **Capas:** de fuera a dentro, «cuadrado», $f$, $\operatorname{sen}$. Tres factores (U p. 79, dos veces).
2. $g'(x)=2f(\operatorname{sen}x)\cdot f'(\operatorname{sen}x)\cdot\cos x$.
3. En $0$: $\operatorname{sen}0=0$, $\cos0=1$: $g'(0)=2\cdot f(0)\cdot f'(0)\cdot1=2\cdot1\cdot(-2)=-4$.

**Receta.** Derivar capa a capa, evaluando cada derivada en lo que tiene dentro.

**Error típico.** Escribir $f'(x)$ en lugar de $f'(\operatorname{sen}x)$.

sympy: $-4$.

---

### X p. 64 (Feb 2016, Ing. Mecánica, Modelo B, P2, 1 punto) — refuerzo de una variable

> Se sabe que $f$ y $g$ son funciones derivables, $g(2)=-1$, $f'(1)=2$ y que $f(x)=xg(2x)$. Calcule $g'(2)$.

1. **Derivar** (producto y cadena, U p. 79): $f'(x)=1\cdot g(2x)+x\cdot g'(2x)\cdot2$.
2. **Evaluar en $x=1$** (porque se conoce $f'(1)$ y $2x=2$ da justo $g(2)$, $g'(2)$): $2=g(2)+2g'(2)=-1+2g'(2)$.
3. **Despejar:** $g'(2)=\frac32$.

**Receta.** Derivar la relación y evaluar en el punto que hace aparecer los datos.

**Error típico.** Olvidar el factor $2$ de la derivada interior de $g(2x)$.

sympy: $f'(x)=g(2x)+2xg'(2x)$; $g'(2)=\frac32$.

---

### X pp. 122-123 (Examen 5, elaborado con exámenes de asignaturas similares, Ej. 4) — refuerzo de una variable

> Sabiendo que $f$ es derivable y verifica $f(0)=\pi$ y $f'(0)=2$ calcule $g'(\pi/2)$ para $g(x)=\cos(f(\cos(x)))$: A) $g'(\pi/2)=0$; B) $g'(\pi/2)=\pi$; C) $g'(\pi/2)=2\pi$; D) Ninguna de las anteriores.

1. $g'(x)=-\operatorname{sen}\big(f(\cos x)\big)\cdot f'(\cos x)\cdot(-\operatorname{sen}x)=\operatorname{sen}\big(f(\cos x)\big)\,f'(\cos x)\,\operatorname{sen}x$.
2. En $\frac\pi2$: $\cos\frac\pi2=0$, $\operatorname{sen}\frac\pi2=1$: $g'\left(\frac\pi2\right)=\operatorname{sen}(f(0))\cdot f'(0)\cdot1=\operatorname{sen}\pi\cdot2=0$.
3. **Respuesta A.**

**Error típico.** Perder uno de los dos signos menos (dan $+$ al multiplicarse).

sympy: $g'(x)=\operatorname{sen}x\,\operatorname{sen}(f(\cos x))\,f'(\cos x)$; valor $0$.

---

### X p. 144 (Feb 2018, 1ª semana, I. Electrónica Industrial y Automática, P2, 1 punto) — refuerzo de una variable

> Sabiendo que $f$ es derivable y verifica $f(2)=\pi$ y $f'(2)=3$, calcular $g'(\sqrt2)$ siendo $g(x)=\operatorname{sen}(f(5x^2-8))$.

1. $g'(x)=\cos\big(f(5x^2-8)\big)\cdot f'(5x^2-8)\cdot10x$.
2. En $\sqrt2$: $5\cdot2-8=2$: $g'(\sqrt2)=\cos(f(2))\cdot f'(2)\cdot10\sqrt2=\cos\pi\cdot3\cdot10\sqrt2=-30\sqrt2$.

sympy: $-30\sqrt2$.

---

### X p. 137 (Feb 2017, 1ª semana, I. Electrónica Industrial y Automática, P3, 1 punto) — refuerzo: comparar con el TVM de dos variables

> Enuncie el Teorema del Valor Medio (para funciones de una variable) y explique la interpretación geométrica de este resultado.

1. **Enunciado** (U §2.5.3, p. 96): si $f:[a,b]\to\mathbb{R}$ es continua en $[a,b]$ y derivable en $(a,b)$, existe al menos un $c\in(a,b)$ con $f'(c)=\dfrac{f(b)-f(a)}{b-a}$.
2. **Interpretación:** la recta tangente en $(c,f(c))$ es **paralela** al segmento que une $(a,f(a))$ y $(b,f(b))$ (pendiente de la tangente = pendiente de la cuerda).
3. **Relación con §5.2:** escrito como $f(b)-f(a)=f'(c)(b-a)$, es el caso de una variable de $f(\bar a)-f(\bar b)=\nabla f(\bar c)\cdot(\bar a-\bar b)$ (U p. 202): el «intervalo» pasa a ser el «segmento» y la derivada, el gradiente.

---

## 3. Ejemplos propios (dificultad creciente)

### Propio 1: derivada de una composición con polares (fácil)

> Sea $f(x,y)=x^2+xy$ y $z(\rho,\theta)=f(\rho\cos\theta,\rho\operatorname{sen}\theta)$. Calcula $\frac{\partial z}{\partial\rho}$ y $\frac{\partial z}{\partial\theta}$ en $\rho=2$, $\theta=\frac\pi4$ con la regla de la cadena.

1. **Intermedias:** $x=\rho\cos\theta$, $y=\rho\operatorname{sen}\theta$ (U p. 148). Derivadas: $x_\rho=\cos\theta$, $y_\rho=\operatorname{sen}\theta$, $x_\theta=-\rho\operatorname{sen}\theta$, $y_\theta=\rho\cos\theta$.
2. **Punto imagen:** $\rho=2$, $\theta=\frac\pi4$ da $(x,y)=(\sqrt2,\sqrt2)$.
3. **Parciales de $f$ allí:** $f_x=2x+y=3\sqrt2$, $f_y=x=\sqrt2$.
4. **Cadena** (dos caminos por variable, U p. 198):
   - $z_\rho=f_x\cos\theta+f_y\operatorname{sen}\theta=3\sqrt2\cdot\frac{\sqrt2}2+\sqrt2\cdot\frac{\sqrt2}2=3+1=4$.
   - $z_\theta=f_x(-\rho\operatorname{sen}\theta)+f_y(\rho\cos\theta)=3\sqrt2(-\sqrt2)+\sqrt2\cdot\sqrt2=-6+2=-4$.
5. **Comprobación sustituyendo:** $z=\rho^2(\cos^2\theta+\cos\theta\operatorname{sen}\theta)$; $z_\rho=2\rho(\cos^2\theta+\cos\theta\operatorname{sen}\theta)=4\left(\frac12+\frac12\right)=4$. ✓

**Receta.** En polares: $z_\rho=f_x\cos\theta+f_y\operatorname{sen}\theta$, $z_\theta=\rho(-f_x\operatorname{sen}\theta+f_y\cos\theta)$.

sympy: $z_\rho=4$, $z_\theta=-4$; la cadena coincide con la sustitución.

### Propio 2: dos intermedias, dos finales y matriz de la cadena (medio)

> Sean $x=u+v$, $y=uv$. (a) Calcula $\nabla F(1,2)$ para $F(u,v)=f(x,y)$ con $f(x,y)=x^2y$. (b) Si además $G(u,v)=x+y$, escribe en una sola matriz las derivadas de $(F,G)$ respecto a $(u,v)$ en $(1,2)$.

1. **Punto imagen:** $(x,y)=(1+2,\ 1\cdot2)=(3,2)$.
2. **$\nabla f$ allí:** $\nabla f=(2xy,\ x^2)=(12,\ 9)$.
3. **Matriz de las intermedias** (filas = $\nabla x$, $\nabla y$ en $(1,2)$): $\nabla x=(1,1)$, $\nabla y=(v,u)=(2,1)$; $M=\begin{pmatrix}1&1\\2&1\end{pmatrix}$.
4. **(a)** $\nabla F(1,2)=(12,9)\,M=(12+18,\ 12+9)=(30,21)$ (U p. 198).
5. **(b)** Para $G$: $\nabla(x+y)=(1,1)$, así que $\nabla G(1,2)=(1,1)M=(3,2)$. Apilando las dos filas (cada componente con la regla de U):
$$\begin{pmatrix}\nabla F\\\nabla G\end{pmatrix}(1,2)=\begin{pmatrix}12&9\\1&1\end{pmatrix}\begin{pmatrix}1&1\\2&1\end{pmatrix}=\begin{pmatrix}30&21\\3&2\end{pmatrix}.$$
   Es decir: la matriz de derivadas de la composición es el producto de las matrices de derivadas (la de fuera, evaluada en el punto imagen, por la de dentro).
6. **Comprobación sustituyendo:** $F=(u+v)^2uv$: $F_u=2(u+v)uv+(u+v)^2v=12+18=30$; $G=u+v+uv$: $G_u=1+v=3$, $G_v=1+u=2$. ✓

**Receta.** Composición vectorial: matriz (fila por función de fuera) × matriz (fila por función intermedia); orden: **fuera × dentro**.

sympy: $\nabla F(1,2)=(30,21)$; producto de matrices $\begin{pmatrix}30&21\\3&2\end{pmatrix}$.

### Propio 3: una identidad en polares para cualquier $f$ (medio-difícil)

> Sea $f$ diferenciable y $z(\rho,\theta)=f(\rho\cos\theta,\rho\operatorname{sen}\theta)$. Prueba que, para $\rho>0$, $\left(\frac{\partial z}{\partial\rho}\right)^2+\frac1{\rho^2}\left(\frac{\partial z}{\partial\theta}\right)^2=\left(\frac{\partial f}{\partial x}\right)^2+\left(\frac{\partial f}{\partial y}\right)^2$.

1. **Cadena** (Propio 1, ahora con $f$ genérica): $z_\rho=f_x\cos\theta+f_y\operatorname{sen}\theta$, $\frac1\rho z_\theta=-f_x\operatorname{sen}\theta+f_y\cos\theta$.
2. **Elevar al cuadrado:** $z_\rho^2=f_x^2\cos^2\theta+2f_xf_y\cos\theta\operatorname{sen}\theta+f_y^2\operatorname{sen}^2\theta$ y $\frac1{\rho^2}z_\theta^2=f_x^2\operatorname{sen}^2\theta-2f_xf_y\cos\theta\operatorname{sen}\theta+f_y^2\cos^2\theta$.
3. **Sumar:** los términos cruzados se cancelan y $\cos^2\theta+\operatorname{sen}^2\theta=1$: queda $f_x^2+f_y^2$. ✓
4. **Ejemplo concreto** (Propio 1 en $(\sqrt2,\sqrt2)$): $4^2+\frac14(-4)^2=16+4=20$ y $f_x^2+f_y^2=18+2=20$. ✓
5. **Lectura:** el tamaño del gradiente, $\|\nabla f\|$, se puede calcular también en polares.

sympy: con $f_x,f_y$ simbólicos, la diferencia se simplifica a $0$.

### Propio 4: cota del cambio de una función con el TVM (difícil)

> Sea $f(x,y)=\operatorname{sen}x\cos y$. (a) Prueba que $|f(a_1,a_2)-f(b_1,b_2)|\le|a_1-b_1|+|a_2-b_2|$ para todo par de puntos. (b) Acota $|f(1{,}1;\,0{,}9)-f(1,1)|$ sin calculadora y compara con el valor real.

1. **Hipótesis del TVM:** $f$ es continua con parciales continuas $f_x=\cos x\cos y$, $f_y=-\operatorname{sen}x\operatorname{sen}y$ en $\mathbb{R}^2$, que es convexo (U p. 202).
2. **TVM** (U p. 202): existe $(c,d)$ en el segmento con $f(\bar a)-f(\bar b)=f_x(c,d)(a_1-b_1)+f_y(c,d)(a_2-b_2)$.
3. **Acotar cada parcial:** $|f_x(c,d)|=|\cos c|\,|\cos d|\le1$ y $|f_y(c,d)|\le1$. No hace falta saber dónde está $(c,d)$.
4. **Desigualdad triangular** (U p. 16): $|f(\bar a)-f(\bar b)|\le|f_x(c,d)|\,|a_1-b_1|+|f_y(c,d)|\,|a_2-b_2|\le|a_1-b_1|+|a_2-b_2|$. Queda (a).
5. **(b)** Con $\bar a=(1{,}1;\,0{,}9)$, $\bar b=(1,1)$: $|f(\bar a)-f(\bar b)|\le0{,}1+0{,}1=0{,}2$.
6. **Comparación:** el valor real es $0{,}0993\ldots$, por debajo de la cota, como debe ser. (La cota es «del peor caso»: no conoce $(c,d)$.)

**Receta.** Para acotar $|f(\bar a)-f(\bar b)|$: TVM + cota de $|f_x|$ y $|f_y|$ en el segmento + desigualdad triangular: $|f(\bar a)-f(\bar b)|\le M_1|a_1-b_1|+M_2|a_2-b_2|$.

**Error típico.** Aplicar el TVM sin comprobar que el segmento está dentro de un conjunto donde las parciales son continuas.

sympy: $f(1{,}1;\,0{,}9)-f(1,1)\approx0{,}09933$; $\operatorname{sen}0{,}1\cos0{,}2\approx0{,}0978$ (otro ejemplo con cota $0{,}3$).

---

## Notas internas (no pasar al HTML)

- **E 5.14, enunciado:** el impreso da dos veces $\nabla f(1,2)$; el segundo es $\nabla g(1,2)=(2,5)$ (así lo usa la propia solución). **Solución impresa:** $\nabla(fg)(1,2)=(27,63)$ y plano $z=18+27(x-1)+63(y-2)$; lo correcto es $(20,63)$ y $z=18+20(x-1)+63(y-2)$. $\nabla(f/g)(1,2)=(-\frac94,-\frac{27}4)$ y plano con $-\frac94(x-1)$; lo correcto es $(-4,-\frac{27}4)$ y $z=\frac92-4(x-1)-\frac{27}4(y-2)$. Verificado con sympy.
- **E 5.20:** el texto extraído muestra «$f(\bar a)=f(\bar b)$» donde la imagen dice $\ne$ (pdftotext pierde la barra). La solución impresa no comprueba que las parciales sean continuas (hipótesis del TVM de U); arriba se justifica (son la función nula).
- **E 5.17:** el diagrama impreso escribe $\frac{\partial z}{\partial x}$ en las ramas superiores; arriba se usa $\frac{\partial f}{\partial x}$ evaluada en las intermedias, que es lo que corresponde.
- **X p. 86:** el enunciado impreso dice $f:\mathbb{R}^2\to\mathbb{R}^2$; la desigualdad $f(x,y)>f(x_0,y_0)$ solo tiene sentido para $f$ real (o componente a componente). Arriba se escribe $f:\mathbb{R}^2\to\mathbb{R}$ y se añade la frase sobre componentes. Además el enunciado no pide parciales continuas (hipótesis del TVM de U p. 202); por eso se da la segunda vía (dos pasos con el TVM de una variable y U Prop. 2.4), válida sin continuidad. La solución impresa remite a «página 250 del libro de teoría» (otra edición): en U es p. 202.
- **X pp. 107-108:** la solución impresa escribe dos veces «$\nabla g(1,1)=(2,1)$»; la segunda es $\nabla f(1,1)$. Valores correctos. El examen no lleva fecha (índice: «Electrónica 4»).
- **X p. 20:** la solución remite a «páginas 219-220» de otra edición; en U la definición de gradiente está en p. 173.
- **X p. 8:** la página PDF 8 es continuación del examen cuya cabecera está en la p. 7 (Grado en Ing. Eléctrica, Septiembre 2010).
- **X p. 135** (Rolle con $e^{(x+1)^2}$ en $[-2,0]$): no se incluye; es de §2.5 y no aporta a la comparación con el TVM de dos variables (se incluye solo X p. 137).
- U p. 195 (cociente) y p. 203 (Ej. 5.9, $xy\ne0$): pdftotext pierde el $\ne$.
- La versión matricial «jacobiana de la composición = producto de jacobianas» (Propio 2 b) no está enunciada en U §5.2; se obtiene aplicando la regla de U a cada componente (se presenta así).
