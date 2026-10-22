# Soluciones Tema 4.3 — Derivadas parciales, gradiente, derivadas de orden superior y derivada direccional

Resolución paso a paso de los ejercicios de **E** de las secciones 4.3-4.5 de U (Ejercicios 4.25-4.44, E pp. 153-165), de las preguntas de examen **X** que piden derivadas parciales, gradientes, Hessianas o direcciones de máximo crecimiento, y de 4 ejemplos propios. Todos los cálculos se han comprobado con sympy (script `v43.py` en el scratchpad; salidas resumidas al final de cada bloque). Se han leído como imagen E p. 165 y X pp. 119, 121, 122, 124, 125, 127, 130, 131, 133, 136, 138, 140, 142, 143, 144, 148, 149, 152.

Páginas: U impresa (= PDF + 2); E impresa = PDF; X = página PDF de `Examenes-resueltos-Calculo.pdf`.

## 0. Herramientas de teoría que se usan

| Clave | Enunciado (resumido) | Dónde |
|---|---|---|
| **Def. 4.8** | Derivada parcial respecto de $x$ en $(a,b)$: $\dfrac{\partial g}{\partial x}(a,b)=\lim_{h\to0}\dfrac{g(a+h,b)-g(a,b)}{h}$, si existe. Es la derivada ordinaria de la función de una variable $x\mapsto g(x,b)$ en $x=a$. | U §4.3.2, p. 169 |
| **Def. 4.9** | Derivada parcial respecto de $y$: $\dfrac{\partial g}{\partial y}(a,b)=\lim_{h\to0}\dfrac{g(a,b+h)-g(a,b)}{h}$. Es la derivada de $y\mapsto g(a,y)$ en $y=b$. | U p. 170 |
| Interpretación geométrica | $(1,0,\frac{\partial g}{\partial x}(a,b))$ es vector director de la tangente a la curva corte de la gráfica con el plano $y=b$; $(0,1,\frac{\partial g}{\partial y}(a,b))$, de la curva corte con el plano $x=a$. | U pp. 169-170 (Fig. 4.15) |
| Cómo se calculan | Se deriva respecto de una variable **tratando las demás como constantes**, con las reglas y tablas de una variable (regla de la cadena incluida). | U p. 171 (Ej. 4.23) |
| Puntos «especiales» | Donde la función se define aparte (p. ej. $f(0,0)=0$) no se pueden usar las reglas: hay que usar la **definición** (límite del cociente). Las parciales pueden existir aunque $f$ no sea continua. | U Ej. 4.24, p. 172 |
| Más variables | $\dfrac{\partial f}{\partial x_k}$: derivar respecto de $x_k$ con las demás fijas. | U p. 173 (Ej. 4.25) |
| **Gradiente** | $\nabla f(a,b)=\left(\frac{\partial f}{\partial x}(a,b),\frac{\partial f}{\partial y}(a,b)\right)$; en $n$ variables, el vector de las $n$ parciales. | U §4.3.3, pp. 173-174 |
| **Propiedad 4.1** | El gradiente en $(a,b)$ es perpendicular a la curva de nivel que pasa por $(a,b)$. | U p. 174 |
| Derivadas segundas | $\dfrac{\partial^2 f}{\partial x^2}=\dfrac{\partial}{\partial x}\Big(\dfrac{\partial f}{\partial x}\Big)$, $\dfrac{\partial^2 f}{\partial y\,\partial x}=\dfrac{\partial}{\partial y}\Big(\dfrac{\partial f}{\partial x}\Big)$, $\dfrac{\partial^2 f}{\partial x\,\partial y}=\dfrac{\partial}{\partial x}\Big(\dfrac{\partial f}{\partial y}\Big)$ (**se deriva primero respecto de la variable de la derecha**). | U §4.4.2, pp. 175-176 |
| **Matriz Hessiana** | $Hf(a,b)=\begin{pmatrix}\frac{\partial^2 f}{\partial x^2}&\frac{\partial^2 f}{\partial x\partial y}\\[2pt] \frac{\partial^2 f}{\partial y\partial x}&\frac{\partial^2 f}{\partial y^2}\end{pmatrix}(a,b)$; en $n$ variables, tabla $n\times n$ de todas las parciales segundas. | U p. 177 (Ej. 4.27) |
| **Teorema 4.1 (Schwarz)** | Si $f$ tiene parciales continuas en un abierto $D$, existe $\frac{\partial^2 f}{\partial x\partial y}$ en todo $D$ y es continua en $(a,b)\in D$, entonces existe $\frac{\partial^2 f}{\partial y\partial x}(a,b)$ y ambas cruzadas coinciden en $(a,b)$. | U p. 178 |
| **Def. 4.10** | Derivada direccional en $(a,b)$ según el vector **unitario** $v=(v_1,v_2)$: $D_vf(a,b)=\lim_{h\to0}\dfrac{f(a+hv_1,b+hv_2)-f(a,b)}{h}$. Con $v=(1,0)$ y $(0,1)$ salen las parciales. | U §4.5.2, p. 179 |
| Interpretación | $(v_1,v_2,D_vf(a,b))$ es vector director de la tangente a la curva corte de la gráfica con el plano vertical que pasa por $(a,b)$ con dirección $v$. | U p. 180 |
| **Teorema 4.2** | Si $f$ tiene parciales cerca de $(a,b)$ y son continuas en $(a,b)$: $D_vf(a,b)=\nabla f(a,b)\cdot v$. (Igual en $n$ variables.) | U p. 180 |
| **Teorema 4.3** | Mismas hipótesis. Si $\nabla f(a,b)\ne0$: la derivada direccional **máxima** se alcanza en la dirección $\frac{\nabla f(a,b)}{\|\nabla f(a,b)\|}$ y vale $\|\nabla f(a,b)\|$; la **mínima**, en la opuesta, y vale $-\|\nabla f(a,b)\|$. Si $\nabla f(a,b)=0$, todas las direccionales son $0$. | U p. 182 |

**Herramientas de temas anteriores que aparecen:** reglas de derivación de una variable (Tema 2), coordenadas polares para límites dobles (U p. 165), producto escalar, norma y ángulo entre vectores $\cos\alpha=\frac{u\cdot w}{\|u\|\,\|w\|}$ (U §4.1).

---

### Receta general del tema

> **Parciales en un punto «normal»** (la fórmula vale alrededor): derivar respecto de una variable con las otras como constantes y sustituir.
>
> **Parciales en un punto «especial»** (la función se define aparte allí): **definición**. Para $\frac{\partial f}{\partial x}(a,b)$ se mueve solo $x$: $\lim_{h\to0}\frac{f(a+h,b)-f(a,b)}{h}$.
>
> **Gradiente**: vector de parciales, en el orden de las variables. **Hessiana**: tabla de parciales segundas (si las cruzadas son continuas, la matriz es simétrica por Schwarz).
>
> **Derivada direccional**: (1) **normalizar** el vector; (2) si las parciales son continuas, $D_vf=\nabla f\cdot v$; si no (o lo piden), usar la definición. **Máximo crecimiento**: dirección de $\nabla f$, valor $\|\nabla f\|$.

---

## 1. Ejercicios de E (orden de dificultad creciente; numeración conservada)

Orden propuesto para aprender: **4.26 → 4.25 → 4.31 → 4.28 → 4.29 → 4.32 → 4.30 → 4.27** (parciales y gradiente con reglas) **→ 4.33 → 4.34** (parciales en un punto especial) **→ 4.37 → 4.36 → 4.35 → 4.38 → 4.39** (orden superior, Hessiana, Schwarz) **→ 4.41 → 4.40 → 4.42 → 4.43 → 4.44** (derivada direccional).

---

### Ejercicio 4.26 (E p. 154)

> El gradiente en $(\pi,1,0)$, $\nabla f(\pi,1,0)$, de una función de tres variables, de existir, verifica: a) Es un número. b) Es un vector. c) Es la suma de todas las derivadas parciales en el punto $(\pi,1,0)$. d) Ninguna de las anteriores.

**Idea en una frase.** El gradiente **junta** las derivadas parciales en una lista ordenada; no las suma.

1. **Definición** (U pp. 173-174): $\nabla f(a_1,a_2,a_3)=\Big(\frac{\partial f}{\partial x_1},\frac{\partial f}{\partial x_2},\frac{\partial f}{\partial x_3}\Big)(a_1,a_2,a_3)$.
2. **Contar componentes:** con tres variables hay tres parciales, así que $\nabla f(\pi,1,0)$ es un vector de $\mathbb{R}^3$.
3. **Descartar c):** sumar las tres parciales da un número, no el gradiente.
4. **Respuesta: b).**

**Receta.** Gradiente de $f:\mathbb{R}^n\to\mathbb{R}$ = vector de $\mathbb{R}^n$ (una componente por variable).

**Error típico.** Sumar las parciales o confundir el gradiente con un número.

---

### Ejercicio 4.25 (E p. 153)

> El precio $f$ de un coche depende, entre otros factores, de la potencia del motor $p$ y de $c$, el consumo medio cada 100 km. ¿Qué signo podemos esperar que tengan $\frac{\partial f}{\partial p}$ y $\frac{\partial f}{\partial c}$?

**Idea en una frase.** Una parcial mide cómo cambia $f$ cuando se mueve **una sola** variable y las demás se quedan quietas; su signo dice si $f$ crece o decrece en esa variable.

1. **Qué es $\frac{\partial f}{\partial p}$** (U p. 169, Def. 4.8): la derivada de la función de una variable $p\mapsto f(p,c,\dots)$ con todo lo demás fijo.
2. **Signo de una derivada de una variable** (Tema 2, monotonía): derivada positiva $\leftrightarrow$ función creciente.
3. **Potencia:** con el mismo consumo y lo demás igual, un motor más potente cuesta más: $f$ crece con $p$, así que se espera $\frac{\partial f}{\partial p}>0$.
4. **Consumo:** con la misma potencia, un coche que gasta más vale menos: $f$ decrece con $c$, así que $\frac{\partial f}{\partial c}<0$.

**Receta.** Para el signo de $\frac{\partial f}{\partial x}$: congelar las demás variables y preguntarse si $f$ sube o baja al aumentar $x$.

**Error típico.** Razonar moviendo varias variables a la vez («los coches potentes gastan más…»): la parcial las mantiene fijas.

---

### Ejercicio 4.31 (E p. 157)

> Calcula el gradiente en $(2,3)$ de la función dada por $f(x,y)=\ln(xy)$.

**Idea en una frase.** Derivar el logaritmo con la regla de la cadena, con la otra variable como constante.

1. **Parcial en $x$** ($y$ constante): $\frac{\partial f}{\partial x}=\frac{1}{xy}\cdot\frac{\partial(xy)}{\partial x}=\frac{y}{xy}=\frac1x$.
2. **Parcial en $y$** ($x$ constante): $\frac{\partial f}{\partial y}=\frac{x}{xy}=\frac1y$.
3. **Sustituir** $(2,3)$ (está en el dominio, $xy=6>0$): $\nabla f(2,3)=\left(\tfrac12,\tfrac13\right)$.

*Atajo equivalente:* si $x,y>0$, $\ln(xy)=\ln x+\ln y$, y se ve directamente.

**Receta.** Parcial = derivada de una variable con las demás congeladas; después, sustituir el punto.

**Error típico.** Olvidar la derivada interior: $\frac{\partial}{\partial x}\ln(xy)\ne\frac{1}{xy}$.

sympy: $(1/2,\,1/3)$.

---

### Ejercicio 4.28 (E p. 155)

> Calcula el gradiente de la función dada por $f(x,y)=y\,\operatorname{tg}(e^x)+\cos^2(x+y)$ en el punto $(0,0)$.

**Idea en una frase.** Regla de la cadena en cada sumando, con la otra variable como constante.

1. **Parcial en $x$.** En el primer sumando $y$ es una constante que multiplica: $\frac{\partial}{\partial x}\big(y\operatorname{tg}(e^x)\big)=y\cdot\frac{1}{\cos^2(e^x)}\cdot e^x$. En el segundo, $\cos^2 u$ con $u=x+y$: $2\cos u\cdot(-\operatorname{sen}u)\cdot\frac{\partial u}{\partial x}=-2\cos(x+y)\operatorname{sen}(x+y)$. Total:
$\frac{\partial f}{\partial x}=\dfrac{y\,e^x}{\cos^2(e^x)}-2\cos(x+y)\operatorname{sen}(x+y)$.
2. **Parcial en $y$.** $\operatorname{tg}(e^x)$ es una constante que multiplica a $y$: su derivada es $\operatorname{tg}(e^x)$. El segundo sumando da lo mismo que antes porque $\frac{\partial u}{\partial y}=1$:
$\frac{\partial f}{\partial y}=\operatorname{tg}(e^x)-2\cos(x+y)\operatorname{sen}(x+y)$.
3. **Sustituir** $(0,0)$: $\frac{\partial f}{\partial x}(0,0)=0-2\cdot1\cdot0=0$; $\frac{\partial f}{\partial y}(0,0)=\operatorname{tg}(e^0)-0=\operatorname{tg}1$.
4. **Resultado:** $\nabla f(0,0)=(0,\operatorname{tg}1)$.

**Receta.** Sumando a sumando: la variable «congelada» se trata como un número (si multiplica, sale fuera; si está sola, su derivada es $0$).

**Error típico.** Derivar $y\operatorname{tg}(e^x)$ respecto de $y$ como si $\operatorname{tg}(e^x)$ dependiera de $y$.

sympy: $(0,\ \operatorname{tg}1)$.

---

### Ejercicio 4.29 (E p. 155)

> Encuentra un vector perpendicular al gradiente de $f(x,y)=e^{x-y}\cos(x)+(y-1)^3$ en el punto $(0,0)$.

**Idea en una frase.** Primero el gradiente; después, un vector cuyo producto escalar con él sea $0$.

1. **Parcial en $x$** (producto $e^{x-y}\cdot\cos x$): $e^{x-y}\cos x-e^{x-y}\operatorname{sen}x$. El término $(y-1)^3$ no depende de $x$: aporta $0$.
2. **Parcial en $y$:** $\frac{\partial}{\partial y}e^{x-y}=-e^{x-y}$, así que $-e^{x-y}\cos x+3(y-1)^2$.
3. **En $(0,0)$:** $\nabla f(0,0)=(1-0,\ -1+3)=(1,2)$.
4. **Perpendicular** (U §4.1: dos vectores son perpendiculares si su producto escalar es $0$): $(a,b)\cdot(1,2)=a+2b=0\iff a=-2b$. Con $b=1$: $(-2,1)$.
5. **Comprobación:** $(-2,1)\cdot(1,2)=-2+2=0$. Cualquier múltiplo $\lambda(-2,1)$ sirve.

*Comentario:* por la Propiedad 4.1 (U p. 174), $(-2,1)$ es tangente a la curva de nivel de $f$ que pasa por $(0,0)$.

**Receta.** En el plano, un perpendicular a $(p,q)$ es $(-q,p)$.

**Error típico.** Olvidar el signo de la regla de la cadena en $e^{x-y}$ al derivar en $y$.

sympy: $\nabla f(0,0)=(1,2)$.

---

### Ejercicio 4.32 (E p. 157)

> Calcula los puntos de $\mathbb{R}^3$ en los que se anula el gradiente de $f$ dada por $f(x,y,z)=x^2+y^3+z^2-2z$.

**Idea en una frase.** Un vector es nulo cuando **todas** sus componentes son $0$: se resuelve un sistema.

1. **Parciales** (cada vez, las otras dos variables constantes): $\frac{\partial f}{\partial x}=2x$, $\frac{\partial f}{\partial y}=3y^2$, $\frac{\partial f}{\partial z}=2z-2$.
2. **Plantear** $\nabla f=(0,0,0)$: $2x=0$, $3y^2=0$, $2z-2=0$.
3. **Resolver:** $x=0$, $y=0$, $z=1$ (las tres ecuaciones son independientes y cada una tiene una sola solución).
4. **Resultado:** solo el punto $(0,0,1)$.

**Receta.** $\nabla f=0$ $\Rightarrow$ sistema «todas las parciales $=0$». (Estos puntos, los *críticos*, se usarán para buscar extremos en el Tema 5.)

**Error típico.** Exigir que solo alguna componente sea $0$.

sympy: $\{(0,0,1)\}$.

---

### Ejercicio 4.30 (E p. 156)

> Calcula la ecuación de la recta tangente a la curva intersección del plano $x=1$ con la gráfica de la función dada por $f(x,y)=x^2+y^2$ en el punto $(1,2,5)$.

**Idea en una frase.** En el plano $x=1$ solo se mueve $y$: la pendiente de la curva es $\frac{\partial f}{\partial y}$, y el vector director es $(0,1,\frac{\partial f}{\partial y})$.

1. **Comprobar el punto:** $f(1,2)=1+4=5$, así que $(1,2,5)$ está en la gráfica.
2. **Qué curva es:** en el plano $x=1$ la gráfica es $\{(1,y,1+y^2)\}$: una parábola recorrida por $y$.
3. **Vector tangente** (U p. 170): derivando la parametrización $y\mapsto(1,y,f(1,y))$ respecto de $y$ se obtiene $(0,1,\frac{\partial f}{\partial y}(1,y))$.
4. **Parcial:** $\frac{\partial f}{\partial y}=2y$; en $(1,2)$ vale $4$. Vector director $(0,1,4)$.
5. **Recta** (punto + vector): $(x,y,z)=(1,2,5)+\lambda(0,1,4)$, $\lambda\in\mathbb{R}$.

**Receta.** Corte con $x=a$ $\to$ director $(0,1,f_y(a,b))$; corte con $y=b$ $\to$ $(1,0,f_x(a,b))$.

**Error típico.** Usar $\frac{\partial f}{\partial x}$: en el plano $x=1$, $x$ no se mueve.

sympy: $f_y(1,2)=4$.

---

### Ejercicio 4.27 (E pp. 154-155)

> Sea $f$ la función dada por $f(x,y)=x\int_0^y s\,e^s\,ds$ para $(x,y)\in\mathbb{R}\times(0,+\infty)$. 1. Utilizando el teorema fundamental del Cálculo calcula el gradiente de $f$ en un punto arbitrario. 2. Después de calcular la integral $\int_0^y s\,e^s\,ds$ por partes, se pide determinar el gradiente de $f$ sin utilizar el teorema fundamental del Cálculo.

**Prerrequisitos (del Tema 6, recordados en E p. 154, margen):** *Teorema fundamental del Cálculo:* si $g$ es continua, $F(y)=\int_0^y g(s)\,ds$ es derivable y $F'(y)=g(y)$. *Integración por partes:* $\int u\,dv=uv-\int v\,du$.

**Idea en una frase.** $f$ es «$x$ por una función solo de $y$»: en $x$ esa función es una constante; en $y$ se deriva la integral con el TFC.

**Apartado 1.**
1. **Nombre auxiliar:** $F(y)=\int_0^y s e^s\,ds$, así $f(x,y)=x\,F(y)$.
2. **Parcial en $x$:** $F(y)$ no depende de $x$, es un número que multiplica: $\frac{\partial f}{\partial x}=F(y)=\int_0^y se^s\,ds$.
3. **Parcial en $y$:** $x$ es una constante que multiplica; por el TFC, $F'(y)=y e^y$. Así $\frac{\partial f}{\partial y}=x\,y\,e^y$.
4. **Gradiente:** $\nabla f(x,y)=\left(\int_0^y se^s\,ds,\ xye^y\right)$.

**Apartado 2.**
1. **Por partes** con $u=s$ ($du=ds$), $dv=e^s ds$ ($v=e^s$): $\int_0^y se^s\,ds=\big[se^s\big]_0^y-\int_0^y e^s\,ds=ye^y-(e^y-1)=1+(y-1)e^y$.
2. **Ahora** $f(x,y)=x\big(1+(y-1)e^y\big)$, una expresión sin integrales.
3. **Parcial en $x$:** $1+(y-1)e^y$.
4. **Parcial en $y$:** $x\cdot\frac{d}{dy}\big((y-1)e^y\big)=x\big(e^y+(y-1)e^y\big)=xye^y$.
5. **Gradiente:** $\nabla f(x,y)=\big(1+(y-1)e^y,\ xye^y\big)$, el mismo que en el apartado 1.

**Receta.** Derivar respecto del límite superior de una integral: $\frac{d}{dy}\int_a^y g(s)\,ds=g(y)$ (se sustituye la variable de integración por el límite).

**Error típico.** Derivar «dentro» de la integral respecto de $s$ o dejar $s$ en el resultado.

sympy: $\int_0^y se^s ds=1+(y-1)e^y$; $\nabla f=(1+(y-1)e^y,\ xye^y)$.

---

### Ejercicio 4.33 (E pp. 157-158)

> Calcula las funciones derivadas parciales $\frac{\partial f}{\partial x}$ y $\frac{\partial f}{\partial y}$, donde $f:\mathbb{R}^2\to\mathbb{R}$ es la función definida por
> $$f(x,y)=\begin{cases}\dfrac{x^2y^2}{x^2+y^2}&\text{si }(x,y)\ne(0,0),\\[4pt] 0&\text{si }(x,y)=(0,0).\end{cases}$$

**Idea en una frase.** Fuera del origen, reglas de derivación; en el origen, donde la fórmula no sirve, la definición.

1. **Fuera del origen** $f$ es un cociente de polinomios con denominador no nulo: se puede usar la regla del cociente (Tema 2). Para $x$ (con $y$ constante):
$\dfrac{\partial f}{\partial x}=\dfrac{2xy^2(x^2+y^2)-x^2y^2\cdot2x}{(x^2+y^2)^2}=\dfrac{2xy^4}{(x^2+y^2)^2}.$
2. **Para $y$** (con $x$ constante), igual intercambiando los papeles:
$\dfrac{\partial f}{\partial y}=\dfrac{2x^2y(x^2+y^2)-x^2y^2\cdot2y}{(x^2+y^2)^2}=\dfrac{2x^4y}{(x^2+y^2)^2}.$
3. **Por qué no vale la fórmula en $(0,0)$:** allí $f$ no está dada por esa expresión (se define aparte) y la fórmula ni siquiera tiene sentido ($0/0$). Hay que usar la Def. 4.8 (U p. 169).
4. **$\frac{\partial f}{\partial x}(0,0)$:** se mueve solo $x$ desde $(0,0)$: $f(h,0)=\frac{h^2\cdot0}{h^2}=0$ para $h\ne0$, así que
$\dfrac{\partial f}{\partial x}(0,0)=\lim_{h\to0}\dfrac{f(h,0)-f(0,0)}{h}=\lim_{h\to0}\dfrac{0-0}{h}=0.$
5. **$\frac{\partial f}{\partial y}(0,0)$:** $f(0,h)=0$, así que $\lim_{h\to0}\frac{0-0}{h}=0$.
6. **Resultado:**
$\dfrac{\partial f}{\partial x}(x,y)=\begin{cases}\dfrac{2xy^4}{(x^2+y^2)^2}&(x,y)\ne(0,0)\\ 0&(x,y)=(0,0)\end{cases}\qquad \dfrac{\partial f}{\partial y}(x,y)=\begin{cases}\dfrac{2x^4y}{(x^2+y^2)^2}&(x,y)\ne(0,0)\\ 0&(x,y)=(0,0)\end{cases}$

**Receta.** Función a trozos: reglas en los puntos «normales» y **definición** en el punto donde cambia la fórmula (en el origen basta mirar $f$ sobre los ejes: $f(h,0)$ y $f(0,h)$).

**Error típico.** Sustituir $(0,0)$ en la fórmula de la derivada (sale $0/0$ y no significa nada) o decir que «no existe» la parcial porque la fórmula no se puede evaluar.

sympy: $f_x=\frac{2xy^4}{(x^2+y^2)^2}$, $f_y=\frac{2x^4y}{(x^2+y^2)^2}$; límites en el origen $=0$.

---

### Ejercicio 4.34 (E pp. 158-159)

> Estudia la continuidad en el origen de las funciones derivadas parciales del ejercicio anterior.

**Idea en una frase.** Hay que ver si $\lim_{(x,y)\to(0,0)}\frac{2xy^4}{(x^2+y^2)^2}$ es $0$ (el valor de la parcial en el origen): las rectas solo orientan; las polares lo prueban.

1. **Qué hay que comprobar** (continuidad, U p. 166): $\lim_{(x,y)\to(0,0)}\frac{\partial f}{\partial x}(x,y)=\frac{\partial f}{\partial x}(0,0)=0$.
2. **Rectas $y=mx$** (para ver qué valor esperar): $\frac{2x(mx)^4}{(x^2+m^2x^2)^2}=\frac{2m^4x}{(1+m^2)^2}\xrightarrow[x\to0]{}0$. Todas dan $0$, pero eso **no basta** para afirmar que el límite existe (U pp. 161-162).
3. **Polares** $x=\rho\cos\theta$, $y=\rho\operatorname{sen}\theta$ (U p. 165): numerador $2\rho^5\cos\theta\operatorname{sen}^4\theta$, denominador $(\rho^2)^2=\rho^4$. Queda $F(\rho,\theta)=2\rho\cos\theta\operatorname{sen}^4\theta$.
4. **Acotar sin $\theta$:** como $|\cos\theta|\le1$ y $|\operatorname{sen}\theta|\le1$, $|F(\rho,\theta)-0|\le2\rho$, y $2\rho\to0$. Por el criterio de polares, el límite es $0$.
5. **Conclusión:** $\frac{\partial f}{\partial x}$ es continua en $(0,0)$.
6. **La otra:** $f(x,y)=f(y,x)$ (la fórmula es simétrica), así que $\frac{\partial f}{\partial y}(x,y)=\frac{\partial f}{\partial x}(y,x)$; en polares, $2\rho\cos^4\theta\operatorname{sen}\theta$, acotado por $2\rho$. También es continua en $(0,0)$.

*Para qué sirve:* con parciales continuas se pueden aplicar los Teoremas 4.2 y 4.3 (derivadas direccionales con el gradiente).

**Receta.** Continuidad de una parcial en un punto especial = límite doble de su fórmula igual al valor obtenido por definición (rectas para orientarse, polares para probar).

**Error típico.** Concluir «continua» solo porque los límites por rectas coinciden.

sympy: en polares $f_x=2\rho\cos\theta\operatorname{sen}^4\theta$.

---

### Ejercicio 4.37 (E pp. 160-161)

> Para la función $f$ dada por $f(x,y)=x^2y$ calcula: su dominio, el gradiente en el punto $(1,0)$, y la matriz Hessiana en el punto $(1,0)$.

**Idea en una frase.** Polinomio: dominio todo el plano; después, derivar una vez (gradiente) y dos veces (Hessiana).

1. **Dominio:** $x^2y$ es un polinomio, tiene sentido para todo $(x,y)$: $\mathbb{R}^2$.
2. **Parciales primeras:** $\frac{\partial f}{\partial x}=2xy$ ($y$ constante), $\frac{\partial f}{\partial y}=x^2$ ($x$ constante).
3. **Gradiente:** $\nabla f(1,0)=(2\cdot1\cdot0,\ 1^2)=(0,1)$.
4. **Parciales segundas** (U pp. 175-176): $\frac{\partial^2 f}{\partial x^2}=\frac{\partial}{\partial x}(2xy)=2y$; $\frac{\partial^2 f}{\partial y^2}=\frac{\partial}{\partial y}(x^2)=0$; $\frac{\partial^2 f}{\partial y\partial x}=\frac{\partial}{\partial y}(2xy)=2x$; $\frac{\partial^2 f}{\partial x\partial y}=\frac{\partial}{\partial x}(x^2)=2x$. Las cruzadas coinciden, como asegura Schwarz para un polinomio.
5. **Hessiana en $(1,0)$** (U p. 177): $Hf(1,0)=\begin{pmatrix}0&2\\2&0\end{pmatrix}$.

**Receta.** Hessiana: fila $i$, columna $j$ = derivar respecto de una variable y luego de la otra; si las cruzadas son continuas, basta calcular una.

**Error típico.** Sustituir el punto **antes** de derivar por segunda vez.

sympy: $\nabla f(1,0)=(0,1)$, $Hf(1,0)=\begin{pmatrix}0&2\\2&0\end{pmatrix}$.

---

### Ejercicio 4.36 (E p. 160)

> Calcula la matriz Hessiana en $(0,1,0)$ de la función dada por $f(x,y,z)=\cos x+\frac12y^2$.

**Idea en una frase.** Con tres variables la Hessiana es $3\times3$; cada sumando depende de una sola variable, así que las cruzadas son $0$.

1. **Primeras:** $\frac{\partial f}{\partial x}=-\operatorname{sen}x$, $\frac{\partial f}{\partial y}=y$, $\frac{\partial f}{\partial z}=0$ ($f$ no depende de $z$).
2. **Segundas puras:** $\frac{\partial^2 f}{\partial x^2}=-\cos x$, $\frac{\partial^2 f}{\partial y^2}=1$, $\frac{\partial^2 f}{\partial z^2}=0$.
3. **Cruzadas:** $-\operatorname{sen}x$ no depende de $y$ ni de $z$; $y$ no depende de $x$ ni de $z$; $0$ es constante. Todas las cruzadas valen $0$ (y son continuas, así que coinciden dos a dos por Schwarz).
4. **En $(0,1,0)$:** $-\cos0=-1$. $Hf(0,1,0)=\begin{pmatrix}-1&0&0\\0&1&0\\0&0&0\end{pmatrix}$.

**Receta.** Si $f=g_1(x)+g_2(y)+g_3(z)$, la Hessiana es diagonal con $g_1'',g_2'',g_3''$.

**Error típico.** Hacer una matriz $2\times2$ porque $z$ «no aparece»: la función es de tres variables.

sympy: $\operatorname{diag}(-1,1,0)$.

---

### Ejercicio 4.35 (E pp. 159-160)

> Las ecuaciones en las que aparecen derivadas parciales se llaman ecuaciones en derivadas parciales. Seguramente ya las has visto en otras asignaturas porque expresan multitud de leyes físicas. Comprueba que $u(t,x)=\operatorname{sen}(x-t)$ verifica la ecuación de ondas $\frac{\partial^2u}{\partial t^2}(t,x)=\frac{\partial^2u}{\partial x^2}(t,x)$, $(t,x)\in\mathbb{R}^2$, que describe el movimiento de una cuerda vibrando.

**Idea en una frase.** Calcular las dos parciales segundas y ver que son la misma función.

1. **En $t$** ($x$ constante; la derivada interior de $x-t$ respecto de $t$ es $-1$): $\frac{\partial u}{\partial t}=-\cos(x-t)$; otra vez: $\frac{\partial^2u}{\partial t^2}=-\big(-\operatorname{sen}(x-t)\big)(-1)=-\operatorname{sen}(x-t)$.
2. **En $x$** (derivada interior $+1$): $\frac{\partial u}{\partial x}=\cos(x-t)$; $\frac{\partial^2u}{\partial x^2}=-\operatorname{sen}(x-t)$.
3. **Comparar:** las dos valen $-\operatorname{sen}(x-t)$ en todo $(t,x)$. Se cumple la ecuación.

**Receta.** «Comprobar que $u$ verifica una EDP»: calcular cada derivada que aparece, sustituir y ver que la igualdad es cierta para **todo** punto.

**Error típico.** Perder el signo de la derivada interior de $x-t$ respecto de $t$ (aparece dos veces y los dos signos se compensan).

sympy: $u_{tt}-u_{xx}=0$.

---

### Ejercicio 4.38 (E pp. 161-162)

> Considera la función $f$ de dos variables dada por
> $$f(x,y)=\begin{cases}\dfrac{x^3y-xy^3}{x^2+y^2},&(x,y)\ne(0,0),\\[4pt] 0,&(x,y)=(0,0).\end{cases}$$
> Calcula las derivadas parciales de $f$ en todo punto y las derivadas parciales segundas en $(0,0)$.

**Idea en una frase.** Como en 4.33: reglas fuera del origen y definición en él; y para las segundas en el origen, otra vez la definición, ahora aplicada a las parciales primeras.

1. **Fuera del origen** (cociente de polinomios, regla del cociente):
$\dfrac{\partial f}{\partial x}=\dfrac{3x^2y-y^3}{x^2+y^2}-\dfrac{2x(x^3y-xy^3)}{(x^2+y^2)^2},\qquad \dfrac{\partial f}{\partial y}=\dfrac{x^3-3xy^2}{x^2+y^2}-\dfrac{2y(x^3y-xy^3)}{(x^2+y^2)^2}.$
2. **En el origen, primeras** (Def. 4.8-4.9): $f(h,0)=0$ y $f(0,h)=0$, así que $\frac{\partial f}{\partial x}(0,0)=\lim_{h\to0}\frac{0-0}{h}=0$ y $\frac{\partial f}{\partial y}(0,0)=0$. Las parciales primeras existen en todo $\mathbb{R}^2$.
3. **Qué valores de las primeras hacen falta.** Para derivar $\frac{\partial f}{\partial x}$ respecto de $y$ en el origen hay que moverse por el eje $y$, es decir, conocer $\frac{\partial f}{\partial x}(0,h)$. Sustituyendo $x=0$, $y=h\ne0$ en la fórmula del paso 1: $\frac{\partial f}{\partial x}(0,h)=\frac{-h^3}{h^2}-0=-h$. Del mismo modo: $\frac{\partial f}{\partial y}(h,0)=\frac{h^3}{h^2}-0=h$; $\frac{\partial f}{\partial x}(h,0)=0$; $\frac{\partial f}{\partial y}(0,h)=0$.
4. **$\frac{\partial^2 f}{\partial x^2}(0,0)$** = parcial en $x$ de $\frac{\partial f}{\partial x}$: $\lim_{h\to0}\frac{\frac{\partial f}{\partial x}(h,0)-\frac{\partial f}{\partial x}(0,0)}{h}=\lim_{h\to0}\frac{0-0}{h}=0$.
5. **$\frac{\partial^2 f}{\partial y^2}(0,0)$:** $\lim_{h\to0}\frac{\frac{\partial f}{\partial y}(0,h)-0}{h}=0$.
6. **$\frac{\partial^2 f}{\partial y\partial x}(0,0)$** = parcial en $y$ de $\frac{\partial f}{\partial x}$ (U p. 176): $\lim_{h\to0}\frac{\frac{\partial f}{\partial x}(0,h)-\frac{\partial f}{\partial x}(0,0)}{h}=\lim_{h\to0}\frac{-h-0}{h}=-1$.
7. **$\frac{\partial^2 f}{\partial x\partial y}(0,0)$** = parcial en $x$ de $\frac{\partial f}{\partial y}$: $\lim_{h\to0}\frac{\frac{\partial f}{\partial y}(h,0)-0}{h}=\lim_{h\to0}\frac{h}{h}=1$.
8. **Resultado:** $Hf(0,0)=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ (fila 1: $\frac{\partial^2 f}{\partial x^2},\frac{\partial^2 f}{\partial x\partial y}$; fila 2: $\frac{\partial^2 f}{\partial y\partial x},\frac{\partial^2 f}{\partial y^2}$). **Las cruzadas no coinciden.**

**Receta.** Segunda parcial en un punto especial = definición aplicada a la parcial primera: para «$\partial y$ de $\partial_x f$» se necesitan los valores de $\partial_x f$ sobre el eje $y$, $(0,h)$.

**Error típico.** Suponer que las cruzadas son siempre iguales (eso exige las hipótesis de Schwarz) o confundir el orden de derivación.

sympy: $f_x(0,y)=-y$, $f_y(x,0)=x$, $f_x(x,0)=0$, $f_y(0,y)=0$; cruzadas $-1$ y $1$.

---

### Ejercicio 4.39 (E pp. 162-163)

> ¿Por qué pueden no coincidir las derivadas parciales segundas cruzadas en el ejercicio anterior pese a que existe un resultado en esa dirección?

**Idea en una frase.** El teorema de Schwarz tiene hipótesis; si una falla, no garantiza nada, y aquí falla la continuidad de la cruzada en el origen.

1. **Qué dice Schwarz** (Teorema 4.1, U p. 178): parciales primeras continuas en un abierto $D$, $\frac{\partial^2 f}{\partial x\partial y}$ existente en $D$ y **continua en $(a,b)$** $\Rightarrow$ las cruzadas coinciden en $(a,b)$.
2. **Contrarrecíproco:** como en 4.38 las cruzadas en $(0,0)$ son distintas ($1\neq-1$), alguna hipótesis tiene que fallar.
3. **Cuál falla (comprobación).** Fuera del origen, sympy da
$\dfrac{\partial^2 f}{\partial x\partial y}=\dfrac{\partial^2 f}{\partial y\partial x}=\dfrac{(x^2-y^2)(x^4+10x^2y^2+y^4)}{(x^2+y^2)^3}.$
Por el eje $x$ ($y=0$) vale $\frac{x^6}{x^6}=1$; por el eje $y$ ($x=0$) vale $\frac{-y^6}{y^6}=-1$. Dos caminos con límites distintos: **no existe el límite** en $(0,0)$, así que la cruzada **no es continua** en el origen.
4. **Conclusión:** no se cumple la hipótesis de continuidad de la cruzada; el teorema no se aplica y las cruzadas pueden ser distintas (y lo son).

**Receta.** Antes de usar un teorema, comprobar **todas** sus hipótesis; si las conclusiones fallan, alguna hipótesis falla.

**Error típico.** Leer Schwarz como «las cruzadas siempre coinciden».

sympy: cruzada fuera del origen como arriba; $1$ por $y=0$, $-1$ por $x=0$.

---

### Ejercicio 4.41 (E p. 163)

> Utilizando la definición, calcula la derivada direccional de $f$ en $(1,-1,2)$ en la dirección del vector unitario $\frac{\bar u}{\|\bar u\|}$, donde $\bar u=(0,1,1)$ y $f(x,y,z)=xy-z$.

**Idea en una frase.** Normalizar el vector, moverse $h$ veces por él desde el punto y aplicar el límite de la Def. 4.10.

1. **Normalizar** (la Def. 4.10 exige vector unitario): $\|\bar u\|=\sqrt{0+1+1}=\sqrt2$, $v=\big(0,\tfrac1{\sqrt2},\tfrac1{\sqrt2}\big)$.
2. **Punto desplazado:** $(1,\ -1+\tfrac{h}{\sqrt2},\ 2+\tfrac{h}{\sqrt2})$.
3. **Evaluar $f$:** $1\cdot\big(-1+\tfrac h{\sqrt2}\big)-\big(2+\tfrac h{\sqrt2}\big)=-3$.
4. **Valor en el punto:** $f(1,-1,2)=-1-2=-3$.
5. **Cociente:** $\frac{-3-(-3)}{h}=0$ para todo $h\ne0$, así que $D_vf(1,-1,2)=\lim_{h\to0}0=0$.
6. **Comprobación con el Teorema 4.2** (polinomio, parciales continuas): $\nabla f=(y,x,-1)=(-1,1,-1)$; $\nabla f\cdot v=0+\tfrac1{\sqrt2}-\tfrac1{\sqrt2}=0$.

*Interpretación:* en esa dirección $f$ es constante (se avanza por la superficie de nivel $f=-3$).

**Receta.** Definición: $D_vf(p)=\lim_{h\to0}\frac{f(p+hv)-f(p)}{h}$ con $v$ unitario.

**Error típico.** Usar $\bar u$ sin normalizar.

sympy: cociente $=0$.

---

### Ejercicio 4.40 (E p. 163)

> De una función de tres variables $f$ se sabe que tiene derivadas parciales continuas en todo $\mathbb{R}^3$ y que $\nabla f(1,\pi,\sqrt7)=(\sqrt8,3,\sqrt5)$. ¿Es cierto que su derivada direccional en la dirección de $(\sqrt2,3,\sqrt5)$ en el punto $(1,\pi,\sqrt7)$ es menor que $\pi$?

**Idea en una frase.** Parciales continuas permiten usar $D_vf=\nabla f\cdot v$; solo hay que **normalizar** el vector antes.

1. **Hipótesis del Teorema 4.2** (U p. 180): parciales continuas en todo $\mathbb{R}^3$. Se cumple.
2. **Normalizar:** $\|(\sqrt2,3,\sqrt5)\|=\sqrt{2+9+5}=\sqrt{16}=4$; $v=\frac14(\sqrt2,3,\sqrt5)$.
3. **Producto escalar:** $(\sqrt8,3,\sqrt5)\cdot(\sqrt2,3,\sqrt5)=\sqrt{16}+9+5=4+9+5=18$.
4. **Derivada:** $D_vf=\frac{18}{4}=\frac92=4{,}5$.
5. **Comparar:** $4{,}5>\pi\approx3{,}1416$. **No es cierto.**

**Receta.** $D_vf=\nabla f\cdot\frac{w}{\|w\|}$: dividir por la norma del vector dado.

**Error típico.** No normalizar: daría $18$ (la conclusión no cambiaría aquí, pero el valor sería falso).

sympy: norma $4$, $D_vf=9/2$.

---

### Ejercicio 4.42 (E p. 164)

> Para la función $f$ dada por $f(x,y)=x\cos(x+y)$, indica el ángulo formado por el vector $(1,1)$ y la dirección de máximo crecimiento de $f$ en $(0,0)$. a) $\frac\pi2$ radianes. b) $\frac\pi4$ radianes. c) $\frac\pi8$ radianes. d) Ninguna de las anteriores.

**Idea en una frase.** La dirección de máximo crecimiento es la del gradiente; el ángulo sale del producto escalar.

1. **Hipótesis del Teorema 4.3:** $f$ es producto y composición de funciones con derivadas continuas; sus parciales son continuas en todo $\mathbb{R}^2$.
2. **Parciales:** $\frac{\partial f}{\partial x}=\cos(x+y)-x\operatorname{sen}(x+y)$ (producto); $\frac{\partial f}{\partial y}=-x\operatorname{sen}(x+y)$ ($x$ es una constante que multiplica).
3. **En $(0,0)$:** $\nabla f(0,0)=(1,0)$. Por el Teorema 4.3 (U p. 182), $f$ crece más deprisa en la dirección $(1,0)$.
4. **Ángulo** (U §4.1): $\cos\alpha=\frac{(1,0)\cdot(1,1)}{\|(1,0)\|\,\|(1,1)\|}=\frac{1}{\sqrt2}$, así que $\alpha=\frac\pi4$.
5. **Respuesta: b).**

**Receta.** Máximo crecimiento $\to\nabla f$; ángulo entre $u$ y $w$: $\arccos\frac{u\cdot w}{\|u\|\|w\|}$.

**Error típico.** Olvidar el término $-x\operatorname{sen}(x+y)$ de la regla del producto (aquí se anula en $(0,0)$, pero no en general).

sympy: $\nabla f(0,0)=(1,0)$; ángulo $\pi/4$.

---

### Ejercicio 4.43 (E pp. 164-165)

> Indica la dirección de máximo crecimiento en el punto $(1,1)$ de $f$ dada por
> $$f(x,y)=\begin{cases}\dfrac{x^2}{x^2+y^2},&(x,y)\ne(0,0),\\[4pt] 0,&(x,y)=(0,0).\end{cases}$$
> a) $\left(\frac{\sqrt2}2,-\frac{\sqrt2}2\right)$. b) $\left(\frac{\sqrt2}2,\frac{\sqrt2}2\right)$. c) $\left(-\frac{\sqrt2}2,-\frac{\sqrt2}2\right)$. d) Ninguna de las anteriores.

**Idea en una frase.** El punto $(1,1)$ es «normal» (lejos del origen): gradiente con reglas, y se normaliza.

1. **Hipótesis del Teorema 4.3:** en $\mathbb{R}^2\setminus\{(0,0)\}$, $f$ es un cociente de polinomios con denominador no nulo; sus parciales son cocientes de polinomios, continuas cerca de $(1,1)$. (Lo que pase en el origen no importa aquí.)
2. **Parciales** (regla del cociente): $\frac{\partial f}{\partial x}=\frac{2x(x^2+y^2)-x^2\cdot2x}{(x^2+y^2)^2}=\frac{2xy^2}{(x^2+y^2)^2}$; $\frac{\partial f}{\partial y}=\frac{-2x^2y}{(x^2+y^2)^2}$.
3. **En $(1,1)$:** $\nabla f(1,1)=\left(\frac24,-\frac24\right)=\left(\frac12,-\frac12\right)$.
4. **Normalizar:** $\|\nabla f(1,1)\|=\sqrt{\frac14+\frac14}=\frac{1}{\sqrt2}$; dirección $\sqrt2\left(\frac12,-\frac12\right)=\left(\frac{\sqrt2}2,-\frac{\sqrt2}2\right)$.
5. **Respuesta: a).** (La tasa máxima es $\|\nabla f(1,1)\|=\frac{\sqrt2}{2}$.)

*Comprobación de sentido común:* $f$ es la proporción de $x^2$ en $x^2+y^2$; crece si aumenta $x$ y disminuye $y$, es decir, hacia «$+x,-y$».

**Receta.** Dirección de máximo crecimiento $=\nabla f/\|\nabla f\|$ (vector unitario).

**Error típico.** Dar $\nabla f$ sin normalizar (llevaría a marcar d) «ninguna») o cambiar un signo al derivar el cociente: la dirección de máximo **de**crecimiento sería $\left(-\frac{\sqrt2}2,\frac{\sqrt2}2\right)$, que no es ninguna de las opciones.

sympy: $\nabla f(1,1)=(1/2,-1/2)$, unitario $(\sqrt2/2,-\sqrt2/2)$.

---

### Ejercicio 4.44 (E p. 165)

> Calcula la ecuación de la recta tangente en el punto $(1,2,2)$ de la curva intersección de la gráfica de $f(x,y)=x^2y$ con un plano paralelo al eje $z$ y al vector $(1,1,0)$.

**Idea en una frase.** El plano es vertical con dirección horizontal $(1,1)$: la pendiente de la curva en ese plano es la derivada direccional según $\frac{(1,1)}{\sqrt2}$.

1. **Comprobar el punto:** $f(1,2)=1\cdot2=2$; $(1,2,2)$ está en la gráfica.
2. **El plano:** pasa por $(1,2,2)$ y contiene las direcciones $(0,0,1)$ y $(1,1,0)$. Es vertical y su dirección horizontal es $(1,1)$; unitario: $v=\left(\frac1{\sqrt2},\frac1{\sqrt2}\right)$.
3. **Vector director** (U p. 180): $(v_1,v_2,D_vf(1,2))$.
4. **Gradiente:** $\nabla f=(2xy,x^2)$; $\nabla f(1,2)=(4,1)$ (parciales continuas: polinomio).
5. **Derivada direccional** (Teorema 4.2): $D_vf(1,2)=(4,1)\cdot\left(\frac1{\sqrt2},\frac1{\sqrt2}\right)=\frac5{\sqrt2}$.
6. **Director:** $\left(\frac1{\sqrt2},\frac1{\sqrt2},\frac5{\sqrt2}\right)$; multiplicando por $\sqrt2$, $(1,1,5)$.
7. **Recta:** $(x,y,z)=(1,2,2)+\lambda(1,1,5)$, $\lambda\in\mathbb{R}$.

*Comprobación directa, solo con una variable:* los puntos del plano son $(1+t,2+t,z)$; la curva es $t\mapsto\big(1+t,\,2+t,\,(1+t)^2(2+t)\big)$. Derivando en $t=0$: $\big(1,1,\ 2(1+t)(2+t)+(1+t)^2\big|_{t=0}\big)=(1,1,5)$. Coincide.

**Receta.** Tangente a la curva corte con un plano vertical de dirección $w$: director $\big(\hat w,\ D_{\hat w}f\big)$ con $\hat w=w/\|w\|$ (o, equivalentemente, $(w,\ \nabla f\cdot w)$ sin normalizar).

**Error típico.** Mezclar un vector sin normalizar en las dos primeras componentes con la derivada direccional normalizada en la tercera: $(1,1,\frac5{\sqrt2})$ no es tangente.

sympy: $\nabla f(1,2)=(4,1)$, $D_vf=5\sqrt2/2$.

---

## 2. Preguntas de examen (X)

Las preguntas se ordenan por subsección: gradiente (4.3) → Hessiana (4.4) → máximo crecimiento (4.5) → preguntas mixtas que usan además material del Tema 5 (marcadas). Las de mayor interés para este tema llevan ★.

---

### ★ X p. 130 (I. Electrónica Industrial y Automática, examen B sin fecha, P4, 1 punto)

> Calcule el gradiente en $(2,3)$ de la función dada por $f(x,y)=\ln(xy)$.

Es el mismo enunciado que **E 4.31**: $\nabla f(x,y)=\left(\frac{y}{xy},\frac{x}{xy}\right)=\left(\frac1x,\frac1y\right)$ y $\nabla f(2,3)=\left(\frac12,\frac13\right)$.

**Receta.** Gradiente en un punto: parciales con las otras variables constantes y sustituir.

---

### ★ X p. 152 (Feb 2019, 1ª semana, I. Electrónica Industrial y Automática, Ej. 6, 3 puntos)

> Dada la función $f:\mathbb{R}^2\to\mathbb{R}$ dada por $f(x,y)=xy(5x-15+y)$ se pide: Calcular $\nabla f(2,-3)$ (1 punto). Determinar los puntos críticos de $f$ (2 puntos).

**Idea en una frase.** Desarrollar el polinomio, derivar, y para los críticos resolver $\nabla f=0$ separando casos (un producto es $0$ si lo es algún factor).

1. **Desarrollar:** $f=5x^2y-15xy+xy^2$.
2. **Parciales:** $\frac{\partial f}{\partial x}=10xy-15y+y^2=y(10x+y-15)$; $\frac{\partial f}{\partial y}=5x^2-15x+2xy=x(5x+2y-15)$.
3. **Gradiente en $(2,-3)$:** $\frac{\partial f}{\partial x}=-3(20-3-15)=-3\cdot2=-6$; $\frac{\partial f}{\partial y}=2(10-6-15)=2\cdot(-11)=-22$. $\nabla f(2,-3)=(-6,-22)$.
4. **Puntos críticos** = puntos donde $\nabla f=(0,0)$ (U p. 173, como en E 4.32): $y(10x+y-15)=0$ y $x(5x+2y-15)=0$.
5. **Caso $y=0$:** la segunda queda $x(5x-15)=0$: $x=0$ o $x=3$. Puntos $(0,0)$ y $(3,0)$.
6. **Caso $10x+y=15$ (con $y\ne0$):** si $x=0$, $y=15$: punto $(0,15)$. Si $5x+2y=15$: de la primera $y=15-10x$; sustituyendo, $5x+30-20x=15$, $x=1$, $y=5$: punto $(1,5)$.
7. **Resultado:** $(0,0)$, $(3,0)$, $(0,15)$, $(1,5)$.

**Receta.** Sistema $\nabla f=0$ con factores: «$A\cdot B=0\iff A=0$ o $B=0$» y combinar los casos de las dos ecuaciones (cuatro combinaciones).

**Error típico.** Dividir por $x$ o por $y$ y perder las soluciones con $x=0$ o $y=0$.

sympy: $\nabla f(2,-3)=(-6,-22)$; críticos $\{(0,0),(3,0),(0,15),(1,5)\}$.

---

### ★ X p. 143 (Sept 2018, I. Electrónica Industrial y Automática, Ej. 6, 3 puntos)

> Para la función dada por $f(x,y)=\ln(36-x^2-y^2)$: Determine y dibuje su dominio (1 punto). Calcule el gradiente de $f$ en el punto $(1,5)$ (1 punto). Calcule $f\circ g$ donde $g(\rho,\theta)=(\rho\cos\theta,\rho\operatorname{sen}\theta)$ (1 punto).

**Idea en una frase.** Logaritmo $\Rightarrow$ argumento positivo (un disco); gradiente con la regla de la cadena; la composición es pasar a polares.

1. **Dominio** (Tema 4.2): $36-x^2-y^2>0\iff x^2+y^2<36$: **disco abierto** de centro $(0,0)$ y radio $6$ (sin la circunferencia frontera).
2. **Parciales:** $\frac{\partial f}{\partial x}=\frac{-2x}{36-x^2-y^2}$, $\frac{\partial f}{\partial y}=\frac{-2y}{36-x^2-y^2}$.
3. **En $(1,5)$** (está en el dominio: $1+25=26<36$; denominador $36-26=10$): $\nabla f(1,5)=\left(\frac{-2}{10},\frac{-10}{10}\right)=\left(-\frac15,-1\right)$.
4. **Composición:** $(f\circ g)(\rho,\theta)=f(\rho\cos\theta,\rho\operatorname{sen}\theta)=\ln(36-\rho^2\cos^2\theta-\rho^2\operatorname{sen}^2\theta)=\ln(36-\rho^2)$ (porque $\cos^2\theta+\operatorname{sen}^2\theta=1$), para $0\le\rho<6$.

**Receta.** $\frac{\partial}{\partial x}\ln(u)=\frac{u_x}{u}$; comprobar siempre que el punto está en el dominio.

sympy: $\nabla f(1,5)=(-1/5,-1)$; $f\circ g=\ln(36-\rho^2)$.

---

### ★ X pp. 148-149 (Feb 2019, 2ª semana, I. Electrónica Industrial y Automática, Ej. 6, 3 puntos)

> Sean $f(x,y)=\ln(4-x^2-y^2)$ y $g(x,y)=\sqrt{x^2+y^2-1}$: Calcule el dominio de $h(x,y)=f(x,y)+g(x,y)$ (1 punto). Calcule los gradientes de $f$ y $g$ en el punto $\left(0,\frac32\right)$ (1.5 puntos). Calcule el producto escalar de los vectores gradientes del apartado anterior (0.5 puntos).

**Idea en una frase.** El dominio de una suma es la intersección de los dominios; los gradientes, con la regla de la cadena.

1. **Dominio de $f$:** $4-x^2-y^2>0\iff x^2+y^2<4$. **De $g$:** $x^2+y^2-1\ge0\iff x^2+y^2\ge1$.
2. **Dominio de $h$** (deben tener sentido los dos sumandos): $\{(x,y): 1\le x^2+y^2<4\}$, una **corona**: incluye la circunferencia de radio $1$ y excluye la de radio $2$.
3. **Gradiente de $f$:** $\left(\frac{-2x}{4-x^2-y^2},\frac{-2y}{4-x^2-y^2}\right)$. En $\left(0,\frac32\right)$: denominador $4-\frac94=\frac74$; $\nabla f=\left(0,\frac{-3}{7/4}\right)=\left(0,-\frac{12}7\right)$.
4. **Gradiente de $g$:** $\frac{\partial}{\partial x}\sqrt u=\frac{u_x}{2\sqrt u}$, así que $\nabla g=\left(\frac{x}{\sqrt{x^2+y^2-1}},\frac{y}{\sqrt{x^2+y^2-1}}\right)$. En $\left(0,\frac32\right)$: $\sqrt{\frac94-1}=\frac{\sqrt5}2$; $\nabla g=\left(0,\frac{3/2}{\sqrt5/2}\right)=\left(0,\frac3{\sqrt5}\right)=\left(0,\frac{3\sqrt5}5\right)$.
5. **Producto escalar:** $0\cdot0+\left(-\frac{12}7\right)\cdot\frac{3\sqrt5}5=-\frac{36\sqrt5}{35}$.

**Receta.** Dominio de $f+g$ = $\operatorname{Dom}f\cap\operatorname{Dom}g$; $\nabla$ componente a componente.

sympy: $\nabla f=(0,-12/7)$, $\nabla g=(0,3\sqrt5/5)$, producto $-36\sqrt5/35$.

---

### ★ X p. 142 (Sept 2018, I. Electrónica Industrial y Automática, P4, 1 punto)

> Calcule la matriz Hessiana de la función dada por $f(x,y)=y\operatorname{sen}(x)-y^3e^x+2$.

**Idea en una frase.** Derivar dos veces; las cruzadas coinciden (Schwarz) y basta calcular una.

1. **Primeras:** $\frac{\partial f}{\partial x}=y\cos x-y^3e^x$; $\frac{\partial f}{\partial y}=\operatorname{sen}x-3y^2e^x$.
2. **Puras:** $\frac{\partial^2 f}{\partial x^2}=-y\operatorname{sen}x-y^3e^x$; $\frac{\partial^2 f}{\partial y^2}=-6ye^x$.
3. **Cruzada:** $\frac{\partial}{\partial y}\big(y\cos x-y^3e^x\big)=\cos x-3y^2e^x$, y $\frac{\partial}{\partial x}\big(\operatorname{sen}x-3y^2e^x\big)=\cos x-3y^2e^x$: iguales (son continuas, Teorema 4.1).
4. **Hessiana:** $Hf(x,y)=\begin{pmatrix}-y\operatorname{sen}x-y^3e^x&\cos x-3y^2e^x\\ \cos x-3y^2e^x&-6ye^x\end{pmatrix}$.

**Receta.** Hessiana = tabla de segundas; calcular las dos cruzadas es una buena comprobación.

sympy: coincide.

---

### ★ X p. 144 (Feb 2018, 1ª semana, I. Electrónica Industrial y Automática, P4, 1 punto)

> Calcule la matriz Hessiana en el punto $(2,1,\pi)$ de la función dada por $f(x,y,z)=x^2+e^x+5y^2-z^3-\cos(z)$.

**Idea en una frase.** Cada sumando depende de una sola variable: Hessiana diagonal (como E 4.36).

1. **Primeras:** $\frac{\partial f}{\partial x}=2x+e^x$, $\frac{\partial f}{\partial y}=10y$, $\frac{\partial f}{\partial z}=-3z^2+\operatorname{sen}z$.
2. **Puras:** $2+e^x$, $10$, $-6z+\cos z$.
3. **Cruzadas:** cada parcial primera depende de una sola variable, así que todas las cruzadas son $0$.
4. **En $(2,1,\pi)$:** $\cos\pi=-1$. $Hf(2,1,\pi)=\begin{pmatrix}2+e^2&0&0\\0&10&0\\0&0&-6\pi-1\end{pmatrix}$.

sympy: $\operatorname{diag}(2+e^2,10,-6\pi-1)$.

---

### ★ X pp. 130-131 (I. Electrónica Industrial y Automática, examen B sin fecha, Ej. 6, 3 puntos)

> Para la función dada por $f(x,y)=\begin{cases}\dfrac{x^2}{x^2+y^2},&(x,y)\ne(0,0),\\ 0,&(x,y)=(0,0).\end{cases}$ Estudie su continuidad. Estudie las asíntotas de la función $G(z)=f(\pi,z)$. Calcule la dirección de máximo crecimiento de $f$ en el punto $(1,1)$.

**Idea en una frase.** Continuidad: fuera del origen por operaciones, en el origen un camino lo descarta; asíntotas: función de una variable; máximo crecimiento: gradiente normalizado (E 4.43).

1. **Continuidad fuera del origen** (U pp. 166-167): cociente de polinomios con denominador $\ne0$: continua.
2. **En el origen:** por el camino $y=0$, $f(x,0)=\frac{x^2}{x^2}=1\to1\ne0=f(0,0)$. **No es continua** en $(0,0)$ (basta un camino cuyo límite no es $f(0,0)$).
3. **$G(z)=f(\pi,z)=\frac{\pi^2}{\pi^2+z^2}$** (como $(\pi,z)\ne(0,0)$, se usa la fórmula). Denominador $\ge\pi^2>0$: dominio $\mathbb{R}$ y $G$ continua, **sin asíntotas verticales**.
4. **Horizontales:** $\lim_{z\to\pm\infty}\frac{\pi^2}{\pi^2+z^2}=0$: la recta de altura $0$ (eje horizontal del plano $zy$) es asíntota horizontal en $+\infty$ y en $-\infty$; por eso **no hay oblicuas**.
5. **Máximo crecimiento en $(1,1)$:** como en E 4.43, $\nabla f(1,1)=\left(\frac12,-\frac12\right)$ y la dirección es $\left(\frac{\sqrt2}2,-\frac{\sqrt2}2\right)$ (parciales continuas cerca de $(1,1)$, Teorema 4.3).

**Receta.** Fijar una variable da una función de una variable (para asíntotas, monotonía…); máximo crecimiento $=\nabla f/\|\nabla f\|$.

sympy: límite por $y=0$ igual a $1$; $\lim_{z\to\infty}G=0$; gradiente $(1/2,-1/2)$.

---

### X p. 121 (Examen 4 «elaborado con exámenes de asignaturas similares», Ej. 6; enunciado p. 119) — usa extremos (Tema 5), pero se resuelve con una desigualdad

> Calcúlense los máximos y mínimos de $f(x,y)=5+x^2y^2$.

**Idea en una frase.** $x^2y^2\ge0$, así que $f\ge5$, con igualdad exactamente en los ejes.

1. **Parciales:** $\frac{\partial f}{\partial x}=2xy^2$, $\frac{\partial f}{\partial y}=2x^2y$.
2. **Puntos críticos:** $2xy^2=0$ y $2x^2y=0$ se cumplen a la vez si y solo si $x=0$ o $y=0$: todos los puntos de los **ejes**.
3. **Mínimo:** $x^2y^2\ge0$ siempre, luego $f(x,y)\ge5$; y $f=5$ justo cuando $x=0$ o $y=0$. Cada punto de los ejes es **mínimo absoluto** (valor $5$), y por tanto también relativo.
4. **Máximo:** $f(t,t)=5+t^4\to+\infty$: no hay máximo absoluto. Tampoco relativo: los únicos candidatos (puntos críticos) son los de los ejes, que son mínimos, y cerca de cada uno hay puntos con $f>5$.

**Receta.** Antes de usar criterios del Tema 5, mirar si una desigualdad evidente ($\text{cuadrado}\ge0$) da directamente el mínimo.

sympy: $\nabla f=(2xy^2,\,2x^2y)$.

---

### X p. 136 (Feb 2017, 2ª semana, I. Electrónica Industrial y Automática, Ej. 6, 3 puntos) — **la clasificación usa el criterio de la Hessiana del Tema 5**

> Sea $f:\mathbb{R}^2\to\mathbb{R}$ la función dada por $f(x,y)=4xy-2y^2-x^3+1$. Estudiar los extremos relativos de $f$.

**Idea en una frase.** Puntos críticos con $\nabla f=0$ (este tema); su tipo, con el signo del determinante de la Hessiana (Tema 5).

1. **Parciales:** $\frac{\partial f}{\partial x}=4y-3x^2$, $\frac{\partial f}{\partial y}=4x-4y$.
2. **Críticos:** de la segunda, $y=x$; en la primera, $4x-3x^2=x(4-3x)=0$: $x=0$ o $x=\frac43$. Puntos $(0,0)$ y $\left(\frac43,\frac43\right)$.
3. **Hessiana** (U p. 177): $Hf(x,y)=\begin{pmatrix}-6x&4\\4&-4\end{pmatrix}$, $\det Hf=24x-16$.
4. *(Tema 5)* **$(0,0)$:** $\det=-16<0$: **punto de silla**.
5. *(Tema 5)* **$\left(\frac43,\frac43\right)$:** $\det=32-16=16>0$ y $\frac{\partial^2 f}{\partial x^2}=-8<0$: **máximo relativo**, con $f\left(\frac43,\frac43\right)=\frac{59}{27}$.

**Receta.** Extremos: (1) $\nabla f=0$; (2) Hessiana en cada punto; (3) criterio del determinante (Tema 5).

sympy: críticos $(0,0)$, $(4/3,4/3)$; $\det$: $-16$ y $16$, $f_{xx}=-8$.

---

### X p. 140 (Feb 2018, 2ª semana, I. Electrónica Industrial y Automática, P3, 1 punto) — **usa la noción de extremo relativo (Tema 5)**

> Razone si la siguiente afirmación es verdadera o falsa: Sea $f:\mathbb{R}^2\to\mathbb{R}$ una función diferenciable en todo $\mathbb{R}^2$. Si $\nabla f(a,b)=\left(\frac{\partial f}{\partial x}(a,b),\frac{\partial f}{\partial y}(a,b)\right)=(0,0)$, entonces el punto $(a,b)$ es un extremo relativo (esto es, un mínimo o un máximo relativo).

**Idea en una frase.** Basta un contraejemplo: una «silla de montar» tiene gradiente nulo y no es extremo.

1. **Candidato:** $f(x,y)=x^2-y^2$ (polinomio, diferenciable en todo $\mathbb{R}^2$).
2. **Gradiente:** $\nabla f=(2x,-2y)$; $\nabla f(0,0)=(0,0)$.
3. **No es extremo:** $f(0,0)=0$, pero $f(t,0)=t^2>0$ y $f(0,t)=-t^2<0$ para $t\ne0$ tan pequeño como se quiera: cerca de $(0,0)$ hay valores mayores y menores que $f(0,0)$.
4. **Respuesta: falsa.** (Otro contraejemplo: $f(x,y)=x^3$ en $(0,0)$.)

**Receta.** Para refutar «$P\Rightarrow Q$», un ejemplo con $P$ y sin $Q$. $\nabla f=0$ es necesario, no suficiente, para extremo.

sympy: $\nabla(x^2-y^2)(0,0)=(0,0)$.

---

### X p. 127 (I. Electrónica Industrial y Automática, examen A sin fecha, P4, 1 punto) — **el plano tangente es del Tema 5; aquí solo el gradiente**

> Calcule la ecuación del plano tangente a la gráfica de la función $f(x,y)=x^2+xy$ en el punto $(1,2,3)$.

**Idea en una frase.** La fórmula del plano (que da el propio examen) solo necesita el gradiente en $(1,2)$.

1. **Fórmula** (Tema 5): $z-f(a,b)=\nabla f(a,b)\cdot(x-a,\,y-b)$.
2. **Comprobar el punto:** $f(1,2)=1+2=3$.
3. **Gradiente:** $\nabla f=(2x+y,\ x)$; $\nabla f(1,2)=(4,1)$.
4. **Plano:** $z-3=4(x-1)+(y-2)\iff 4x+y-z=3$.

sympy: $\nabla f(1,2)=(4,1)$.

---

### X p. 133 (Sept 2017, I. Electrónica Industrial y Automática, P4, 1 punto) — **plano tangente (Tema 5)**

> Calcule la ecuación del plano tangente a la gráfica de la función $f(x,y)=e^x(3\operatorname{sen}y+2)$ en el punto $\left(0,\frac\pi2,5\right)$.

1. **Comprobar el punto:** $f\left(0,\frac\pi2\right)=1\cdot(3+2)=5$.
2. **Parciales:** $\frac{\partial f}{\partial x}=e^x(3\operatorname{sen}y+2)$ ($3\operatorname{sen}y+2$ es constante en $x$); $\frac{\partial f}{\partial y}=3e^x\cos y$.
3. **Gradiente:** $\nabla f\left(0,\frac\pi2\right)=(5,\ 3\cos\frac\pi2)=(5,0)$.
4. **Plano:** $z=5+5(x-0)+0\cdot\left(y-\frac\pi2\right)=5+5x$.

sympy: $f=5$, $\nabla f=(5,0)$.

---

### X p. 138 (Feb 2017, 1ª semana, I. Electrónica Industrial y Automática, Ej. 6, 3 puntos) — **plano tangente (Tema 5)**

> Sea $f:\mathbb{R}^2\to\mathbb{R}$ la función dada por $f(x,y)=\begin{cases}\dfrac{x^2y^3}{x^4+y^2}&\text{si }(x,y)\ne(0,0),\\ 1&\text{si }(x,y)=(0,0).\end{cases}$ Estudiar la continuidad de $f$ en el punto $(0,0)$ (1.5 puntos). Obtener la ecuación del plano tangente a la gráfica de $f$ en el punto $\left(1,1,\frac12\right)$ (1.5 puntos).

**Idea en una frase.** El límite en el origen es $0$ (se prueba acotando), que no es $f(0,0)=1$; el plano solo pide el gradiente en $(1,1)$.

1. **Valor esperado:** por rectas $y=mx$, $\frac{m^3x^5}{x^4+m^2x^2}=\frac{m^3x^3}{x^2+m^2}\to0$. Las rectas sugieren límite $0$ (sin probarlo).
2. **Prueba (acotación).** Como $(x^2-|y|)^2\ge0$, se tiene $x^4+y^2\ge2x^2|y|$, es decir, $\frac{x^2|y|}{x^4+y^2}\le\frac12$. Entonces
$|f(x,y)|=\frac{x^2|y|}{x^4+y^2}\cdot y^2\le\frac{y^2}{2}\xrightarrow[(x,y)\to(0,0)]{}0.$
Por el emparedado (U p. 163), $\lim_{(x,y)\to(0,0)}f(x,y)=0$.
3. **Conclusión:** $0\ne1=f(0,0)$: $f$ **no es continua** en $(0,0)$.
4. **Comprobar el punto:** $f(1,1)=\frac{1}{2}$.
5. **Parciales** (cociente): $\frac{\partial f}{\partial x}=\frac{2xy^3(x^4+y^2)-x^2y^3\cdot4x^3}{(x^4+y^2)^2}$, $\frac{\partial f}{\partial y}=\frac{3x^2y^2(x^4+y^2)-x^2y^3\cdot2y}{(x^4+y^2)^2}$. En $(1,1)$: $\frac{2\cdot2-4}{4}=0$ y $\frac{3\cdot2-2}{4}=1$. $\nabla f(1,1)=(0,1)$.
6. **Plano** (Tema 5): $z=\frac12+0\cdot(x-1)+1\cdot(y-1)=y-\frac12$.

**Receta.** Para probar que un límite doble vale $0$, acotar $|f|$ por algo que tiende a $0$; la desigualdad $a^2+b^2\ge2|ab|$ es la clave cuando aparecen sumas como $x^4+y^2$.

sympy: $f(1,1)=1/2$, $\nabla f(1,1)=(0,1)$; cota $|f|\le y^2/2$ comprobada.

---

### X pp. 124-125 (Examen 5 «elaborado con exámenes de asignaturas similares», Ej. 6; enunciado p. 122) — **la diferenciabilidad es del Tema 5**

> Estudiar la continuidad, derivabilidad y diferenciabilidad de la función $f(x,y)=\begin{cases}\dfrac{x^3+xy^2+3y^4}{x^2+y^2}&\forall(x,y)\ne(0,0)\\ 0&(0,0)\end{cases}$

**Idea en una frase.** Fuera del origen todo es cociente de polinomios; en el origen, polares para el límite y la definición para las parciales.

1. **Fuera del origen:** cociente de polinomios con denominador $\ne0$: continua, con parciales (por la regla del cociente) continuas.
2. **Continuidad en $(0,0)$:** en polares, $F(\rho,\theta)=\frac{\rho^3\cos^3\theta+\rho^3\cos\theta\operatorname{sen}^2\theta+3\rho^4\operatorname{sen}^4\theta}{\rho^2}=\rho\cos\theta\,(\cos^2\theta+\operatorname{sen}^2\theta)+3\rho^2\operatorname{sen}^4\theta=\rho\cos\theta+3\rho^2\operatorname{sen}^4\theta$. Acotación sin $\theta$: $|F|\le\rho+3\rho^2\to0$. Límite $0=f(0,0)$: **continua**.
3. **Parciales en $(0,0)$** (definición): $f(t,0)=\frac{t^3}{t^2}=t$, así que $\frac{\partial f}{\partial x}(0,0)=\lim_{t\to0}\frac{t-0}{t}=1$. $f(0,t)=\frac{3t^4}{t^2}=3t^2$, así que $\frac{\partial f}{\partial y}(0,0)=\lim_{t\to0}\frac{3t^2}{t}=0$.
4. *(Tema 5)* **Diferenciabilidad en $(0,0)$:** hay que ver si $\lim_{(h,k)\to(0,0)}\frac{f(h,k)-f(0,0)-1\cdot h-0\cdot k}{\sqrt{h^2+k^2}}=0$. Como $f(h,k)-h=\frac{3k^4}{h^2+k^2}$, el cociente es $\frac{3k^4}{(h^2+k^2)^{3/2}}$; en polares, $3\rho\operatorname{sen}^4\theta$, acotado por $3\rho\to0$. **Diferenciable.**

**Receta.** Punto especial: (1) límite (polares) frente al valor; (2) parciales por definición mirando $f$ en los ejes; (3) (Tema 5) límite del resto entre la distancia.

sympy: polar $\rho\cos\theta+3\rho^2\operatorname{sen}^4\theta$; parciales $1$ y $0$; resto en polares $3\rho\operatorname{sen}^4\theta$.

---

*No hay en X preguntas de derivada direccional por la definición; la única de máximo crecimiento es la de X pp. 130-131.*

---

## 3. Ejemplos propios (dificultad creciente)

### Propio 1 — Gradiente con regla de la cadena (fácil)

> Calcula $\nabla f(1,0)$ para $f(x,y)=x^3y^2+e^{xy}$.

1. $\frac{\partial f}{\partial x}=3x^2y^2+y\,e^{xy}$ (la derivada interior de $xy$ respecto de $x$ es $y$).
2. $\frac{\partial f}{\partial y}=2x^3y+x\,e^{xy}$.
3. En $(1,0)$: $\frac{\partial f}{\partial x}=0+0=0$; $\frac{\partial f}{\partial y}=0+1\cdot e^0=1$. $\nabla f(1,0)=(0,1)$.

sympy: $(0,1)$.

### Propio 2 — Hessiana, derivada direccional y máximo crecimiento (medio)

> Sea $f(x,y)=xe^y+y^2$. (a) Calcula $Hf(1,0)$. (b) Calcula la derivada de $f$ en $(1,0)$ en la dirección de $(3,4)$. (c) ¿Cuál es la mayor derivada direccional en $(1,0)$ y en qué dirección?

1. **Primeras:** $f_x=e^y$, $f_y=xe^y+2y$. $\nabla f(1,0)=(1,1)$.
2. **Segundas:** $f_{xx}=0$, $\frac{\partial^2 f}{\partial y\partial x}=\frac{\partial^2 f}{\partial x\partial y}=e^y$, $f_{yy}=xe^y+2$. $Hf(1,0)=\begin{pmatrix}0&1\\1&3\end{pmatrix}$.
3. **(b)** Normalizar: $\|(3,4)\|=5$, $v=\left(\frac35,\frac45\right)$. Parciales continuas $\Rightarrow$ Teorema 4.2: $D_vf(1,0)=(1,1)\cdot\left(\frac35,\frac45\right)=\frac75$.
4. **(c)** Teorema 4.3: máximo $\|\nabla f(1,0)\|=\sqrt2$ en la dirección $\left(\frac1{\sqrt2},\frac1{\sqrt2}\right)$. Comprobación: $\frac75=1{,}4\le\sqrt2\approx1{,}414$.

sympy: $Hf(1,0)=\begin{pmatrix}0&1\\1&3\end{pmatrix}$, $D_vf=7/5$, $\|\nabla f\|=\sqrt2$.

### Propio 3 — Parciales que existen sin continuidad (medio-difícil)

> Sea $f(x,y)=\frac{xy}{x^2+y^2}$ si $(x,y)\ne(0,0)$, $f(0,0)=0$. (a) Calcula $\nabla f(0,0)$. (b) ¿Es $f$ continua en $(0,0)$? (c) ¿Existe la derivada direccional en $(0,0)$ según $v=\left(\frac1{\sqrt2},\frac1{\sqrt2}\right)$?

1. **(a)** $f(h,0)=0$ y $f(0,h)=0$, así que ambas parciales en el origen valen $\lim_{h\to0}\frac{0}{h}=0$: $\nabla f(0,0)=(0,0)$.
2. **(b)** Por $y=mx$: $f(x,mx)=\frac{m}{1+m^2}$, que depende de $m$ (p. ej. $0$ con $m=0$, $\frac12$ con $m=1$). No existe el límite: **no es continua**.
3. **(c)** $f\left(\frac h{\sqrt2},\frac h{\sqrt2}\right)=\frac{h^2/2}{h^2}=\frac12$, luego el cociente es $\frac{1/2-0}{h}$, que no tiene límite finito ($\to\pm\infty$). **No existe** $D_vf(0,0)$.
4. **Moraleja:** aquí $\nabla f(0,0)\cdot v=0$, pero $D_vf(0,0)$ no existe: el Teorema 4.2 no se aplica porque las parciales no son continuas en el origen (si lo fueran, $f$ sería continua). Tener las dos parciales no da las demás direcciones.

sympy: $f(x,mx)=m/(1+m^2)$; cociente direccional $\to\infty$.

### Propio 4 — Todas las direccionales existen pero no son $\nabla f\cdot v$ (difícil)

> Sea $f(x,y)=\frac{x^2y}{x^2+y^2}$ si $(x,y)\ne(0,0)$, $f(0,0)=0$. Calcula $D_vf(0,0)$ para todo vector unitario $v=(a,b)$ y compáralo con $\nabla f(0,0)\cdot v$.

1. **Definición** (U p. 179): $f(ha,hb)=\frac{h^3a^2b}{h^2(a^2+b^2)}=h\,a^2b$ (porque $a^2+b^2=1$). Cociente: $\frac{ha^2b-0}{h}=a^2b$. Así $D_vf(0,0)=a^2b$ para **toda** dirección.
2. **Parciales:** con $v=(1,0)$, $a^2b=0$; con $v=(0,1)$, $0$. $\nabla f(0,0)=(0,0)$, y $\nabla f(0,0)\cdot v=0$.
3. **Comparar** con $v=\left(\frac1{\sqrt2},\frac1{\sqrt2}\right)$: $D_vf(0,0)=\frac12\cdot\frac1{\sqrt2}=\frac{\sqrt2}4\ne0$.
4. **Moraleja:** la fórmula $D_vf=\nabla f\cdot v$ necesita la hipótesis del Teorema 4.2 (parciales continuas en el punto); aquí falla, y la fórmula da un valor equivocado aunque **todas** las direccionales existan. (Además, $f$ es continua en el origen, porque $|f|\le|y|$.)

sympy: $D_vf(0,0)=a^2b$; para $v=(1,1)/\sqrt2$, $\sqrt2/4$.

---

## Notas internas (no pasar al HTML)

- X p. 121 (Examen 4, Ej. 6): la solución impresa escribe $\frac{\partial f}{\partial y}=2xy^2$; lo correcto es $2x^2y$ (la conclusión no cambia). Arriba se escribe lo correcto.
- X p. 138 (Feb 2017 1ª, Ej. 6): la solución impresa deduce el límite $0$ solo con rectas $y=mx$, lo que no basta; arriba se prueba con la cota $|f|\le y^2/2$.
- X p. 140 (Feb 2018 2ª, P3): la solución impresa solo remite a «texto base página 267»; el contraejemplo $x^2-y^2$ es propio.
- X p. 136: la solución impresa no da el valor del máximo; $f(4/3,4/3)=59/27$ calculado aquí.
- E 4.39: E dice que falla la continuidad de $\frac{\partial^2 f}{\partial y\partial x}$; por la simetría de la fórmula fuera del origen fallan las dos cruzadas (se ha comprobado y se explica arriba con la del enunciado de U).
- No se ha incluido X Examen 3 Ej. 6 (PDF 116-118, $4x^3/(x^2+y^2)$, continuidad y diferenciabilidad) porque el dossier lo deja fuera del índice del tema 4 y no se ha verificado en imagen; encaja mejor en Tema 5.1.
