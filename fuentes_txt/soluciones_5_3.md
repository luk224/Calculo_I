# Soluciones Tema 5.3: Teorema de la función implícita

Resolución paso a paso de los ejercicios de **E** de la sección 5.3 de U (Ejercicios 5.23-5.27, E pp. 186-191), de los ejemplos de U que conviene rehacer (Ej. 5.10-5.14, U pp. 205-212), de las dos preguntas de examen **X** sobre función implícita (X pp. 30-31 y 150-151) y de 4 ejemplos propios. Todos los cálculos se han comprobado con sympy (script `v53.py` en el scratchpad de la sesión), y las derivadas implícitas además numéricamente (resolviendo la ecuación con `nsolve` y derivando por diferencias finitas). Se han leído como imagen X pp. 29, 30, 150; E pp. 186-191 en texto (limpio) y comprobadas con el dossier, que vio E pp. 186 y 190 en imagen.

Páginas: U impresa (= PDF + 2); E impresa = PDF; X = página PDF de `Examenes-resueltos-Calculo.pdf`.

## 0. Herramientas de teoría que se usan

| Clave | Enunciado (resumido) | Dónde |
|---|---|---|
| Ecuación implícita / explícita | Implícita: $f(x_1,\dots,x_n)=0$ (no dice cómo despejar). Explícita: una variable escrita en función de las otras, $y=y(x_1,\dots,x_{n-1})$. Pasar de explícita a implícita es inmediato: $f=y-y(x_1,\dots)=0$. | U §5.3.2, p. 205; Ej. 5.10 p. 205 |
| **Teorema de la función implícita (dos variables)** | $f:D\subset\mathbb{R}^2\to\mathbb{R}$ continua con parciales continuas en el abierto $D$; $(a,b)\in D$ con **(1)** $f(a,b)=0$ y **(2)** $\frac{\partial f}{\partial y}(a,b)\ne0$. Entonces hay intervalos abiertos $U\ni a$, $V\ni b$ y una **única** $g:U\to V$ con $f(x,g(x))=0$ para $x\in U$; además $g(a)=b$, $g$ tiene derivada continua y $\dfrac{dy}{dx}=-\dfrac{\partial f/\partial x}{\partial f/\partial y}$. | U p. 206 |
| Cambio de papeles | Si en lugar de (2) se tiene $\frac{\partial f}{\partial x}(a,b)\ne0$, se puede despejar $x=g(y)$ y $\dfrac{dx}{dy}=-\dfrac{\partial f/\partial y}{\partial f/\partial x}$. | U p. 206; Ej. 5.11 pp. 206-207 |
| **Derivación implícita** | Si $f(x,y(x))=0$ cerca de $a$, se deriva con la regla de la cadena: $\frac{\partial f}{\partial x}+\frac{\partial f}{\partial y}\,y'(x)=0$, y se despeja $y'$. Se puede repetir para $y''$, $y'''$… | U p. 207; Ej. 5.12 pp. 207-210 |
| Pendiente de una curva de nivel | La curva de nivel $f(x,y)=k$ tiene en $(a,b)$ recta tangente de pendiente $-\frac{\partial f/\partial x}{\partial f/\partial y}(a,b)$: menos el cociente de las componentes del gradiente. | U p. 210; Ej. 5.13 p. 210 |
| Gradiente y curvas de nivel | Propiedad 4.1: $\nabla f(a,b)$ es perpendicular a la curva de nivel que pasa por $(a,b)$. | U p. 174 |
| **Teorema de la función implícita ($n+1$ variables)** | $f(x_1,\dots,x_n,z)$ continua con parciales continuas en un abierto $D\subset\mathbb{R}^{n+1}$; $f(a_1,\dots,a_n,b)=0$ y $\frac{\partial f}{\partial z}(a_1,\dots,a_n,b)\ne0$. Entonces hay una bola $U$ de $(a_1,\dots,a_n)$, un intervalo $V\ni b$ y una única $g:U\to V$ con parciales continuas tal que $f(x_1,\dots,x_n,g(x_1,\dots,x_n))=0$ en $U$, y $\dfrac{\partial z}{\partial x_j}=-\dfrac{\partial f/\partial x_j}{\partial f/\partial z}$. Vale para cualquier variable en lugar de $z$. | U p. 211; Ej. 5.14 pp. 211-212 |

**Herramientas de temas anteriores que aparecen:**
- Regla de la cadena con una variable final: $\frac{d}{dx}f(x,y(x))=\frac{\partial f}{\partial x}+\frac{\partial f}{\partial y}\,y'(x)$ (U p. 196; con $g(x)=x$, Ej. 5.7 p. 199).
- Derivadas parciales y gradiente (U §4.3, pp. 168-173). Recta tangente $y=b+m(x-a)$; plano tangente $z=c+\frac{\partial z}{\partial x}(x-a)+\frac{\partial z}{\partial y}(y-b)$ (U (5.2), p. 189).
- Polinomios, exponenciales, senos y cosenos, y sus sumas, productos y composiciones, son continuos con parciales continuas en todo su dominio: así se comprueba la hipótesis de regularidad del teorema.
- Regla del producto y de la cadena de una variable (U §2.2, p. 79), para la derivación implícita sucesiva.

---

### Receta general del tema

> **¿Define $f(x,y)=0$ a $y$ como función de $x$ cerca de $(a,b)$?** (pregunta «el teorema garantiza…»)
> 1. **Pasarlo todo a un lado**: escribir la ecuación como $f(x,y)=0$ (p. ej. $x^2+y^2=9\to f=x^2+y^2-9$).
> 2. **Regularidad**: $f$ continua con parciales continuas cerca del punto (funciones elementales: una frase basta).
> 3. **Condición 1**: $f(a,b)=0$ (el punto está en la curva).
> 4. **Condición 2**: la parcial respecto a **la variable que se quiere despejar** no se anula en el punto: $\frac{\partial f}{\partial y}(a,b)\ne0$ para $y=g(x)$; $\frac{\partial f}{\partial x}(a,b)\ne0$ para $x=g(y)$; $\frac{\partial f}{\partial z}\ne0$ para $z=g(x,y)$.
> 5. Si falla 3, el punto ni siquiera está en la curva. Si falla 4, **el teorema no garantiza nada** (no dice que sea imposible).
>
> **Derivar la función implícita:** fórmula $\;y'=-\dfrac{f_x}{f_y}\;$ (o $z_x=-f_x/f_z$, $z_y=-f_y/f_z$) evaluada en el punto; o bien derivar la ecuación con $y=y(x)$ dentro y despejar. Para $y''$: derivar **otra vez** la ecuación ya derivada y sustituir el punto y el $y'$ ya calculado.

---

## 1. Ejemplos de U (para entender el teorema antes de los ejercicios)

### U Ej. 5.10 (p. 205): de explícita a implícita

> La parábola $y=x^2$ en forma implícita.

1. Basta pasar todo a un lado: $f(x,y)=x^2-y=0$.
2. **Por qué es útil:** el teorema siempre trabaja con «$f=0$». El camino contrario (despejar) es el difícil, y es el que estudia el teorema.

### U Ej. 5.11 (pp. 204-207): la circunferencia $x^2+y^2=1$

> ¿Dónde se puede despejar $y$ en función de $x$ en $x^2+y^2-1=0$? ¿Y $x$ en función de $y$?

**Idea en una frase.** Se puede despejar $y$ donde la curva «no es vertical», y eso lo detecta $\frac{\partial f}{\partial y}\ne0$.

1. $f(x,y)=x^2+y^2-1$: polinomio, así que es continua con parciales continuas en $\mathbb{R}^2$.
2. $\frac{\partial f}{\partial y}=2y$. Se anula solo si $y=0$, es decir, en los puntos $(1,0)$ y $(-1,0)$ de la circunferencia.
3. **En $\left(\frac{\sqrt2}2,\frac{\sqrt2}2\right)$**: $f=\frac12+\frac12-1=0$ y $\frac{\partial f}{\partial y}=\sqrt2\ne0$: hay $y=g(x)$; aquí se conoce, $y=\sqrt{1-x^2}$. En $\left(\frac{\sqrt2}2,-\frac{\sqrt2}2\right)$, igual con $y=-\sqrt{1-x^2}$.
4. **En $(1,0)$** la condición 2 falla, y de hecho es imposible: a la izquierda de $x=1$ hay dos valores de $y$ ($\pm\sqrt{1-x^2}$) y a la derecha ninguno.
5. **Cambio de papeles:** $\frac{\partial f}{\partial x}(1,0)=2\ne0$, así que cerca de $(1,0)$ sí se despeja $x=g(y)$, que es $x=\sqrt{1-y^2}$.
6. **Derivada implícita** (U p. 207): $y'=-\frac{2x}{2y}=-\frac xy$ donde $y\ne0$; $x'(y)=-\frac yx$ donde $x\ne0$. Comprobación: $\left(\sqrt{1-x^2}\right)'=\frac{-x}{\sqrt{1-x^2}}=-\frac xy$. ✓
7. **Respuesta al «ejercicio» que deja U:** se puede despejar $x$ en todos los puntos de la circunferencia salvo $(0,1)$ y $(0,-1)$.

### U Ej. 5.13 (p. 210): pendiente de una curva de nivel

> La gráfica de $f(x,y)=x^2+3xy-y^2$ define curvas de nivel $f(x,y)=k$. Una de ellas contiene al punto $(1,0)$. Calcule la pendiente de la recta tangente en $(1,0)$ a esa curva.

1. **Qué curva:** $f(1,0)=1$, así que es $f(x,y)=1$, es decir $F(x,y)=x^2+3xy-y^2-1=0$.
2. **Hipótesis:** $F$ polinomio; $F(1,0)=0$; $\frac{\partial F}{\partial y}=3x-2y$ vale $3\ne0$ en $(1,0)$. Hay $y=y(x)$ cerca de $x=1$, con $y(1)=0$.
3. $\frac{\partial F}{\partial x}=2x+3y$ vale $2$ en $(1,0)$.
4. **Pendiente:** $y'(1)=-\frac{2}{3}$. Recta tangente: $y=-\frac23(x-1)$.

### U Ej. 5.12 (pp. 207-210): folium de Descartes $x^3+y^3-3xy=0$ (derivada segunda)

**Idea en una frase.** Es el modelo de «derivar implícitamente dos veces»: se deriva la ecuación, se despeja $y'$, y se deriva $y'$ (que depende de $x$ y de $y(x)$).

1. $f_x=3x^2-3y$, $f_y=3y^2-3x$.
2. **Dónde se despeja $y$:** hace falta $f_y\ne0$, es decir $x\ne y^2$. Sustituyendo $x=y^2$ en la ecuación: $y^6+y^3-3y^3=y^3(y^3-2)=0$, luego $y=0$ o $y=\sqrt[3]2$. Los puntos de la curva con $f_y=0$ son $(0,0)$ y $(\sqrt[3]4,\sqrt[3]2)$; en todos los demás se despeja $y$.
3. **Dónde se despeja $x$:** por simetría ($x\leftrightarrow y$), salvo en $(0,0)$ y $(\sqrt[3]2,\sqrt[3]4)$. Solo en $(0,0)$ se anulan las dos parciales.
4. **Derivada primera** (derivar la ecuación con $y=y(x)$, U p. 209): $3x^2+3y^2y'-3y-3xy'=0$, luego
$$y'=\frac{y-x^2}{y^2-x}.$$
5. **Derivada segunda:** derivar el cociente (regla del cociente; $y$ es función de $x$) y sustituir $y'$. Tras simplificar sale (U p. 210)
$$y''=-\frac{2\left(xy+xy^4+x^4y-3x^2y^2\right)}{(y^2-x)^3}.$$
6. **Simplificación usando la propia curva** (útil en examen): $xy^4+x^4y=xy(x^3+y^3)=xy\cdot3xy=3x^2y^2$, así que en los puntos del folium el numerador es $2xy$ y
$$y''=-\frac{2xy}{(y^2-x)^3}.$$

sympy: la expresión de U coincide con la derivada segunda implícita (diferencia $0$); con la parametrización $x=\frac{3t}{1+t^3}$, $y=\frac{3t^2}{1+t^3}$ en $t=\frac12,\,2,\,-\frac25$, las dos formas de $y''$ coinciden. Puntos con $f=f_y=0$ reales: $(0,0)$, $(2^{2/3},2^{1/3})$.

### U Ej. 5.14 (pp. 211-212): una superficie $z=g(x,y)$

> $x^2-xy+3z^2=3$ cerca de $(0,1,1)$.

1. $f(x,y,z)=x^2-xy+3z^2-3$; $f(0,1,1)=0-0+3-3=0$.
2. $f_x=2x-y$, $f_y=-x$, $f_z=6z$; $f_z(0,1,1)=6\ne0$: existe $z=g(x,y)$ en un disco centrado en $(0,1)$, con $g(0,1)=1$.
3. **Derivadas:** $z_x(0,1)=-\frac{f_x}{f_z}=-\frac{-1}{6}=\frac16$; $z_y(0,1)=-\frac{f_y}{f_z}=-\frac{0}{6}=0$.
4. **Comprobación** (aquí se puede despejar, eligiendo la raíz positiva porque $z=1>0$): $z=\sqrt{1-\frac{x^2-xy}3}$; derivando, $z_x(0,1)=\frac16$, $z_y(0,1)=0$. ✓

---

## 2. Ejercicios de E (orden de dificultad creciente; numeración conservada)

Orden propuesto para aprender: **5.23 → 5.25** (comprobar las condiciones del teorema) **→ 5.26** (pendiente con $-f_x/f_y$) **→ 5.27** (tres variables) **→ 5.24** (derivada segunda implícita).

---

### Ejercicio 5.23 (E p. 186)

> El teorema de la función implícita garantiza que la ecuación $x^2-xy^2+y^2=1$ define a $y$ como función implícita de $x$ cerca de:
> a) $(0,1)$. b) $(2,1)$. c) $(-1,0)$. d) Ninguna de las anteriores.

**Idea en una frase.** Para cada punto se comprueban las dos condiciones: está en la curva ($f=0$) y $\frac{\partial f}{\partial y}\ne0$.

1. **Escribir $f=0$:** $f(x,y)=x^2-xy^2+y^2-1$. Es un polinomio: continua con parciales continuas en $\mathbb{R}^2$ (hipótesis de U p. 206).
2. **Parcial respecto a $y$** (la variable que se quiere despejar): $\frac{\partial f}{\partial y}=-2xy+2y=2y(1-x)$.
3. **Punto $(0,1)$:** $f(0,1)=0-0+1-1=0$ ✓; $\frac{\partial f}{\partial y}(0,1)=2\cdot1\cdot(1-0)=2\ne0$ ✓. Se cumplen las dos.
4. **Punto $(2,1)$:** $f(2,1)=4-2+1-1=2\ne0$. El punto **no está en la curva**: el teorema no se puede ni plantear (da igual que $\frac{\partial f}{\partial y}(2,1)=-2\ne0$).
5. **Punto $(-1,0)$:** $f(-1,0)=1-0+0-1=0$ ✓, pero $\frac{\partial f}{\partial y}(-1,0)=2\cdot0\cdot2=0$ ✗.
6. **Respuesta: a).**

**Receta.** Tabla de dos columnas por punto: «$f(a,b)=0$?» y «$\frac{\partial f}{\partial(\text{variable a despejar})}(a,b)\ne0$?». Solo vale el punto con dos «sí».

**Error típico.** Olvidar la condición $f(a,b)=0$ y dar por bueno $(2,1)$ porque su parcial no se anula.

sympy: $f$ en los tres puntos: $0,\ 2,\ 0$; $\frac{\partial f}{\partial y}$: $2,\ -2,\ 0$.

---

### Ejercicio 5.25 (E pp. 188-189)

> Sea la ecuación $3xy-x^3+\cos(\pi y)=1$. Justifica si el teorema de la función implícita garantiza que esta ecuación define a $y$ como función implícita de $x$ cerca de $(1,1)$. ¿Lo garantiza para $x$ como función implícita de $y$?

**Idea en una frase.** Mismo punto, dos preguntas: para $y=g(x)$ se mira $\frac{\partial f}{\partial y}$; para $x=g(y)$ se mira $\frac{\partial f}{\partial x}$.

1. **Escribir $f=0$** (pasar el $1$ a la izquierda): $f(x,y)=3xy-x^3+\cos(\pi y)-1$. Suma de un polinomio y un coseno: continua con parciales continuas en $\mathbb{R}^2$.
2. **El punto está en la curva:** $f(1,1)=3-1+\cos\pi-1=3-1-1-1=0$ ✓.
3. **¿$y$ en función de $x$?** $\frac{\partial f}{\partial y}=3x-\pi\operatorname{sen}(\pi y)$; en $(1,1)$: $3-\pi\operatorname{sen}\pi=3\ne0$ ✓. **Sí**: el teorema (U p. 206) garantiza $y=g(x)$ cerca de $x=1$, con $g(1)=1$ (y de paso $g'(1)=-\frac{f_x}{f_y}=-\frac03=0$).
4. **¿$x$ en función de $y$?** $\frac{\partial f}{\partial x}=3y-3x^2$; en $(1,1)$: $3-3=0$ ✗. **El teorema no lo garantiza.**
5. **Qué significa «no lo garantiza»:** el teorema solo da una condición suficiente; con $\frac{\partial f}{\partial x}=0$ no concluye nada. Para saber qué pasa de verdad hay que mirar la curva. En este ejemplo, cerca de $(1,1)$ la curva se parece a la parábola $y-1\approx(x-1)^2$ (desarrollando: $f(1+h,1+k)\approx3k-3h^2$): para $y$ un poco mayor que $1$ hay **dos** valores de $x$ y para $y<1$ **ninguno**, así que aquí efectivamente no se puede escribir $x=g(y)$. (Esto es un complemento; en el examen basta con el paso 4.)

**Receta.** «¿Puedo despejar la variable $v$?» ⇔ «¿$\frac{\partial f}{\partial v}\ne0$ en el punto?» (además de $f=0$). Si la parcial es $0$, la respuesta correcta es «el teorema no lo garantiza», no «es imposible».

**Error típico.** Confundir qué parcial se mira: para despejar $x$ hay que mirar la parcial **respecto a $x$**.

sympy: $f(1,1)=0$, $f_y(1,1)=3$, $f_x(1,1)=0$; $f(x,1)=-(x-1)^2(x+2)$; numéricamente, para $y=0{,}99$ no hay ninguna solución $x\in[0{,}8;\,1{,}2]$ y para $y=1{,}01$ hay dos.

---

### Ejercicio 5.26 (E pp. 189-190)

> Sea $f$ la función dada por $f(x,y)=ye^x-x^2$. ¿Cuál es la pendiente de la recta tangente a la curva de nivel que pasa por $(0,1)$ en ese mismo punto?

**Idea en una frase.** La pendiente de una curva de nivel es $-\frac{f_x}{f_y}$; se puede ver con el teorema de la función implícita o con «gradiente perpendicular a la curva».

**Paso previo: qué curva de nivel.** $f(0,1)=1\cdot e^0-0=1$, así que es la curva $ye^x-x^2=1$.

**Método 1: teorema de la función implícita** (U p. 206 y p. 210).
1. $F(x,y)=ye^x-x^2-1$: continua con parciales continuas (polinomios y exponencial). $F(0,1)=0$ ✓.
2. $\frac{\partial F}{\partial y}=e^x$; en $(0,1)$ vale $1\ne0$ ✓. Cerca de $(0,1)$ la curva es la gráfica de una función $y=y(x)$ con $y(0)=1$.
3. La pendiente de la tangente a una gráfica es la derivada: $y'(0)=-\frac{F_x(0,1)}{F_y(0,1)}$.
4. $\frac{\partial F}{\partial x}=ye^x-2x$; en $(0,1)$ vale $1$.
5. **Pendiente:** $y'(0)=-\frac11=-1$. Recta tangente: $y=1-x$.

**Método 2: gradiente perpendicular** (U Propiedad 4.1, p. 174).
1. $\nabla f=(ye^x-2x,\ e^x)$; $\nabla f(0,1)=(1,1)$.
2. La tangente es perpendicular a $(1,1)$; un vector perpendicular es $(1,-1)$ (su producto escalar con $(1,1)$ es $0$).
3. Con vector director $(1,-1)$, la pendiente es $\frac{-1}{1}=-1$.

**Receta.** Pendiente de la curva de nivel en $(a,b)$: $m=-\dfrac{\partial f/\partial x}{\partial f/\partial y}(a,b)$ (no hace falta restar la constante $k$: no cambia las derivadas).

**Error típico.** Olvidar el signo menos, o calcular $\frac{f_y}{f_x}$ (al revés).

sympy: $-\frac{F_x}{F_y}(0,1)=-1$.

---

### Ejercicio 5.27 (E pp. 190-191)

> Se considera la función $f:\mathbb{R}^3\to\mathbb{R}$ definida por $f(x,y,z)=1-e^{(x^7+y^2-xz-1)}$.
> 1. Encuentra el valor de $a$ tal que cerca del punto $(1,0,a)$ la ecuación $f(x,y,z)=0$ defina implícitamente una función $z=g(x,y)$.
> 2. Calcula $\frac{\partial g}{\partial x}(1,0)$ y $\frac{\partial g}{\partial y}(1,0)$.

**Idea en una frase.** El teorema en tres variables (U p. 211): $f=0$ en el punto y $\frac{\partial f}{\partial z}\ne0$; luego $g_x=-\frac{f_x}{f_z}$, $g_y=-\frac{f_y}{f_z}$.

1. **Regularidad:** $f$ es composición de una exponencial con un polinomio: continua con parciales continuas en $\mathbb{R}^3$, para cualquier $a$.
2. **Condición $f(1,0,a)=0$:** el exponente vale $1+0-a-1=-a$, así que $1-e^{-a}=0\iff e^{-a}=1\iff a=0$. Único candidato: el punto $(1,0,0)$.
3. **Condición $\frac{\partial f}{\partial z}\ne0$:** por la regla de la cadena, $\frac{\partial f}{\partial z}=-e^{(\dots)}\cdot(-x)=x\,e^{(x^7+y^2-xz-1)}$. En $(1,0,0)$: $1\cdot e^0=1\ne0$ ✓. **Respuesta 1: $a=0$.**
4. **Las otras parciales** (regla de la cadena): $\frac{\partial f}{\partial x}=-(7x^6-z)\,e^{(\dots)}$, $\frac{\partial f}{\partial y}=-2y\,e^{(\dots)}$. En $(1,0,0)$: $f_x=-7$, $f_y=0$.
5. **Fórmula del teorema** (U p. 211):
$$\frac{\partial g}{\partial x}(1,0)=-\frac{f_x}{f_z}=-\frac{-7}{1}=7,\qquad \frac{\partial g}{\partial y}(1,0)=-\frac{f_y}{f_z}=-\frac01=0.$$
6. **Otra forma (derivar la ecuación):** como $e^{s}>0$, $f=0\iff x^7+y^2-xz-1=0$. Con $z=g(x,y)$ y derivando respecto a $x$: $7x^6-g-x\,g_x=0$; en $(1,0)$ con $g=0$: $7-0-g_x=0$, $g_x=7$. Respecto a $y$: $2y-x\,g_y=0$, luego $g_y(1,0)=0$. ✓
7. **Comprobación despejando** (aquí se puede, para $x\ne0$): $z=\frac{x^7+y^2-1}{x}$, con $z_x=\frac{6x^7-y^2+1}{x^2}$, que en $(1,0)$ vale $7$, y $z_y=\frac{2y}{x}=0$. ✓

**Receta.** Superficie $f(x,y,z)=0$: (1) imponer $f(\text{punto})=0$ para hallar el dato que falta; (2) comprobar $f_z\ne0$; (3) $z_x=-f_x/f_z$, $z_y=-f_y/f_z$ en el punto.

**Error típico.** Al derivar respecto a $x$ con $z=g(x,y)$ dentro, olvidar que el término $xz$ es un producto: su derivada es $z+x\,z_x$, no $x\,z_x$.

sympy: $a=0$; $f_z(1,0,0)=1$; $g_x(1,0)=7$, $g_y(1,0)=0$; la forma explícita da lo mismo y anula $f$.

---

### Ejercicio 5.24 (E pp. 187-188)

> Dada la ecuación $x^4+x^2y^3-y^2=1$.
> 1. Muestra que define a $x$ como función implícita de $y$ cerca de $(1,1)$.
> 2. Calcula $g'(1)$ y $g''(1)$, en donde $x=g(y)$ cerca de $(1,1)$.

**Idea en una frase.** Aquí la variable que se despeja es $x$ (la independiente es $y$): se mira $\frac{\partial f}{\partial x}$, y luego se deriva dos veces la identidad $f(g(y),y)=0$ respecto a $y$.

**Apartado 1.**
1. $f(x,y)=x^4+x^2y^3-y^2-1$ (polinomio: continua con parciales continuas en $\mathbb{R}^2$).
2. $f(1,1)=1+1-1-1=0$ ✓.
3. $\nabla f=(4x^3+2xy^3,\ 3x^2y^2-2y)$; $\nabla f(1,1)=(6,1)$.
4. $\frac{\partial f}{\partial x}(1,1)=6\ne0$ ✓. Por el teorema con los papeles cambiados (U p. 206) hay intervalos $U\ni1$ (de $y$), $V\ni1$ (de $x$) y una única $g:U\to V$ con $f(g(y),y)=0$ y $g(1)=1$.

**Apartado 2: $g'(1)$.**
5. **Fórmula directa:** $g'(1)=\frac{dx}{dy}(1)=-\frac{f_y(1,1)}{f_x(1,1)}=-\frac16$.
6. **Por derivación implícita** (necesario para $g''$): en $g(y)^4+g(y)^2y^3-y^2-1=0$ se deriva respecto a $y$ (cadena en $g^4$, producto en $g^2y^3$):
$$4g^3g'+2g\,g'\,y^3+3g^2y^2-2y=0.\qquad(\ast)$$
7. En $y=1$, $g=1$: $4g'+2g'+3-2=0$, así que $6g'(1)+1=0$ y $g'(1)=-\frac16$ (coincide).

**Apartado 2: $g''(1)$.**
8. **Derivar $(\ast)$ otra vez respecto a $y$**, término a término (producto de varios factores, todos dependen de $y$ salvo los números):
   - $\left(4g^3g'\right)'=12g^2(g')^2+4g^3g''$.
   - $\left(2g\,g'\,y^3\right)'=2(g')^2y^3+2g\,g''\,y^3+6g\,g'\,y^2$.
   - $\left(3g^2y^2\right)'=6g\,g'\,y^2+6g^2y$.
   - $(-2y)'=-2$.
   Sumando: $12g^2(g')^2+4g^3g''+2(g')^2y^3+2g\,g''\,y^3+12g\,g'\,y^2+6g^2y-2=0$.
9. **Sustituir $y=1$, $g=1$, $g'=-\frac16$** (así la única incógnita es $g''$):
   - $12\cdot\frac1{36}=\frac13$; $\ 2\cdot\frac1{36}=\frac1{18}$; $\ 12\cdot\left(-\frac16\right)=-2$; $\ 6-2=4$.
   - Queda $\frac13+\frac1{18}-2+4+6g''(1)=0$, es decir $6g''(1)+\frac{43}{18}=0$.
10. **Despejar:** $g''(1)=-\frac{43}{108}$.

**Receta.** Derivada segunda implícita: (1) derivar la ecuación con $x=g(y)$ dentro → ecuación $(\ast)$; (2) evaluar y despejar $g'$; (3) derivar $(\ast)$ **antes** de evaluar; (4) evaluar con el $g'$ ya conocido y despejar $g''$.

**Error típico.** Evaluar $(\ast)$ en el punto y **después** derivar (se deriva una constante y sale $0=0$); o tratar $g'$ como constante al derivar por segunda vez (olvidando los términos con $g''$).

sympy: $\nabla f(1,1)=(6,1)$; $g'(1)=-\frac16$; segunda ecuación en el punto: $14(g')^2+12g'+6g''+4=0$, de donde $g''(1)=-\frac{43}{108}\approx-0{,}39815$. Numérico (resolviendo $x$ para $y=1\pm10^{-4}$): $g'(1)\approx-0{,}1666667$, $g''(1)\approx-0{,}398148$.

---

## 3. Preguntas de examen (X)

Solo hay dos preguntas de examen de función implícita en X; las dos piden exactamente lo de E 5.23-5.25 y E 5.24.

---

### ★ X p. 150-151 (Feb 2019, 1ª semana, I. Electrónica Industrial y Automática, P4, 1 punto)

> Razone si la siguiente afirmación es verdadera o falsa: el teorema de la función implícita para funciones de dos variables garantiza que la ecuación $x^2+y^2=9$ define a $y$ como función implícita de $x$ cerca de $(3,0)$.

**Idea en una frase.** $(3,0)$ es el punto «más a la derecha» de la circunferencia: allí la tangente es vertical y $\frac{\partial f}{\partial y}=0$.

**Lo que hay que escribir en el examen:**
1. Sea $f(x,y)=x^2+y^2-9$, polinomio: continua con parciales continuas en $\mathbb{R}^2$.
2. $f(3,0)=9+0-9=0$: el punto está en la curva.
3. $\frac{\partial f}{\partial y}(x,y)=2y$, y $\frac{\partial f}{\partial y}(3,0)=0$. No se cumple la hipótesis $\frac{\partial f}{\partial y}(a,b)\ne0$ del teorema (U p. 206).
4. **Falso:** el teorema no garantiza que $y$ sea función implícita de $x$ cerca de $(3,0)$.

**Para entenderlo (no hace falta escribirlo):**
- De hecho es imposible: para $x$ un poco menor que $3$ hay dos valores $y=\pm\sqrt{9-x^2}$, y para $x>3$ ninguno.
- En cambio, $\frac{\partial f}{\partial x}(3,0)=6\ne0$: cerca de $(3,0)$ sí se puede despejar $x=\sqrt{9-y^2}$.

**Receta.** V/F de función implícita: escribir $f$, comprobar $f(a,b)=0$ y la parcial de la variable que se despeja; si se anula, «falso: el teorema no lo garantiza».

**Error típico.** Contestar «verdadero» porque el punto está en la curva (solo se ha comprobado la condición 1).

sympy: $f(3,0)=0$, $f_y(3,0)=0$, $f_x(3,0)=6$.

---

### ★ X pp. 30-31 (Sept 2012, reserva, Ing. Mecánica, Modelo A, Ej. 6, 3 puntos)

> Dada la ecuación $x^4+x^2y^3-y^2=1$,
> (a) Demuestre que define a $x$ como función implícita de $y$ en un entorno de $(1,1)$.
> (b) Si $x=g(y)$, calcule $g'(1)$ y $g''(1)$.

**Idea en una frase.** Es el Ejercicio 5.24 de E: la variable que se despeja es $x$, así que la condición es $\frac{\partial f}{\partial x}(1,1)\ne0$; después se deriva dos veces $f(g(y),y)=0$.

**Lo que hay que escribir en el examen:**

(a)
1. $f(x,y)=x^4+x^2y^3-y^2-1$: polinomio, continua con parciales continuas en $\mathbb{R}^2$.
2. $f(1,1)=0$.
3. $\nabla f(x,y)=(4x^3+2xy^3,\ 3x^2y^2-2y)$, $\nabla f(1,1)=(6,1)$; en particular $\frac{\partial f}{\partial x}(1,1)=6\ne0$.
4. Por el teorema de la función implícita (con los papeles de $x$ e $y$ cambiados, U p. 206), existen un intervalo abierto $U$ con $1\in U$, un intervalo abierto $V$ con $1\in V$ y una única $g:U\to V$ con derivada continua tal que $f(g(y),y)=0$ para $y\in U$ y $g(1)=1$. Además
$$g'(y)=\frac{dx}{dy}=-\frac{\partial f/\partial y}{\partial f/\partial x}(g(y),y).$$

(b)
5. $g'(1)=-\frac{f_y(1,1)}{f_x(1,1)}=-\frac16$.
6. Derivando $g^4+g^2y^3-y^2-1=0$ respecto a $y$: $4g^3g'+2gg'y^3+3g^2y^2-2y=0$.
7. Derivando otra vez: $12g^2(g')^2+4g^3g''+2(g')^2y^3+2gg''y^3+12gg'y^2+6g^2y-2=0$.
8. En $y=1$, $g=1$, $g'=-\frac16$: $\frac13+4g''+\frac1{18}+2g''-2+6-2=0\Rightarrow 6g''(1)=-\frac{43}{18}\Rightarrow g''(1)=-\frac{43}{108}$.

**Explicaciones (no hace falta escribirlas):**
- En el paso 7, cada término de la línea del paso 6 es un producto de factores que dependen de $y$ ($g$, $g'$, $y^3$…): se usa la regla del producto con todos ellos. Detalle término a término en E 5.24, paso 8.
- Comprobación rápida de la cuenta del paso 8: $12\cdot\frac1{36}=\frac13$, $2\cdot\frac1{36}=\frac1{18}$, $12\cdot\left(-\frac16\right)=-2$; los números sueltos suman $\frac13+\frac1{18}-2+6-2=\frac{43}{18}$.

**Receta.** Ver E 5.24: derivar antes de evaluar; evaluar con el $g'$ ya hallado; despejar $g''$.

**Error típico.** Usar la fórmula $g'=-f_x/f_y$ (la de $y=g(x)$) cuando lo que se despeja es $x$: daría $-6$ en lugar de $-\frac16$.

sympy: $g'(1)=-\frac16$, $g''(1)=-\frac{43}{108}$ (y numéricamente igual).

---

## 4. Ejemplos propios (dificultad creciente)

### Propio 1: recta tangente a una curva implícita y puntos con tangente horizontal (fácil)

> Para la elipse $x^2+xy+y^2=7$: (a) comprueba que define $y=y(x)$ cerca de $(1,2)$ y halla la recta tangente allí; (b) ¿en qué puntos la tangente es horizontal?

1. $F(x,y)=x^2+xy+y^2-7$; $F(1,2)=1+2+4-7=0$ ✓.
2. $F_x=2x+y$, $F_y=x+2y$. En $(1,2)$: $F_x=4$, $F_y=5\ne0$ ✓ (U p. 206).
3. **Pendiente:** $y'(1)=-\frac45$. **Recta tangente:** $y=2-\frac45(x-1)$.
4. **(b) Tangente horizontal** significa $y'=0$, es decir $F_x=0$ con $F_y\ne0$: $y=-2x$. Sustituyendo en la elipse: $x^2-2x^2+4x^2=3x^2=7$, $x=\pm\sqrt{7/3}$. Puntos: $\left(\frac{\sqrt{21}}3,-\frac{2\sqrt{21}}3\right)$ y $\left(-\frac{\sqrt{21}}3,\frac{2\sqrt{21}}3\right)$ (allí $F_y=x+2y=\mp\sqrt{21}\ne0$, así que la fórmula vale).
5. **Lectura:** donde $F_y=0$ (es decir, $x=-2y$) la tangente es vertical y no se puede despejar $y$: son los puntos $\pm\left(\frac{2\sqrt{21}}3,-\frac{\sqrt{21}}3\right)$.

**Receta.** Tangente horizontal: $F_x=0$ (y $F_y\ne0$). Tangente vertical: $F_y=0$ (y $F_x\ne0$). Cada condición se resuelve junto con la ecuación de la curva.

sympy: $y'(1)=-\frac45$; puntos con $F=F_x=0$: $\pm\left(\frac{\sqrt{21}}3,-\frac{2\sqrt{21}}3\right)$; con $F=F_y=0$: $\pm\left(\frac{2\sqrt{21}}3,-\frac{\sqrt{21}}3\right)$.

### Propio 2: derivadas parciales de $z(x,y)$ implícita y plano tangente (medio)

> La ecuación $z^3+xz-y=0$ define $z=z(x,y)$ cerca de $(0,1,1)$. (a) Compruébalo. (b) Calcula $z_x(0,1)$ y $z_y(0,1)$. (c) Usa el plano tangente para aproximar $z(0{,}1;\,0{,}9)$.

1. **(a)** $f(x,y,z)=z^3+xz-y$ (polinomio). $f(0,1,1)=1+0-1=0$ ✓; $f_z=3z^2+x$, $f_z(0,1,1)=3\ne0$ ✓ (U p. 211). Hay $z=z(x,y)$ con $z(0,1)=1$.
2. **(b)** $f_x=z$, $f_y=-1$. En el punto: $f_x=1$, $f_y=-1$.
$$z_x(0,1)=-\frac{1}{3}=-\frac13,\qquad z_y(0,1)=-\frac{-1}{3}=\frac13.$$
3. **(c) Plano tangente** (U (5.2), p. 189): $z\approx1-\frac13(x-0)+\frac13(y-1)$. En $(0{,}1;\,0{,}9)$: $z\approx1-\frac{0{,}1}3-\frac{0{,}1}3=0{,}9333$.
4. **Comparación:** resolviendo numéricamente $z^3+0{,}1z-0{,}9=0$ cerca de $1$ sale $z\approx0{,}93098$: error $\approx0{,}0024$.

**Receta.** Superficie implícita: $z_x=-f_x/f_z$, $z_y=-f_y/f_z$, y con ellas el plano tangente $z\approx z_0+z_x(x-x_0)+z_y(y-y_0)$, sin despejar $z$ (aquí despejar exigiría resolver una cúbica).

sympy: $z_x=-\frac13$, $z_y=\frac13$; raíz real $0{,}930980$; aproximación lineal $0{,}933333$.

### Propio 3: derivada segunda de $y(x)$ implícita (medio-difícil)

> La ecuación $e^y+xy=e$ define $y=y(x)$ cerca de $(0,1)$. Calcula $y'(0)$ e $y''(0)$.

1. **Hipótesis:** $F=e^y+xy-e$; $F(0,1)=e+0-e=0$ ✓; $F_y=e^y+x$, $F_y(0,1)=e\ne0$ ✓.
2. **Derivar la ecuación** con $y=y(x)$ (cadena en $e^y$, producto en $xy$): $e^yy'+y+xy'=0.\quad(\ast)$
3. **En $x=0$, $y=1$:** $e\,y'+1+0=0\Rightarrow y'(0)=-\frac1e$.
4. **Derivar $(\ast)$ otra vez** (cada término es un producto): $\left(e^yy'\right)'=e^y(y')^2+e^yy''$; $(y)'=y'$; $(xy')'=y'+xy''$. Queda
$$e^y(y')^2+e^yy''+2y'+xy''=0.$$
5. **En $x=0$, $y=1$, $y'=-\frac1e$:** $e\cdot\frac1{e^2}+e\,y''-\frac2e+0=0\Rightarrow e\,y''=\frac1e\Rightarrow y''(0)=\frac1{e^2}$.
6. **Lectura:** $y'(0)<0$ y $y''(0)>0$: cerca de $x=0$ la curva baja y es convexa (U §3.5).

**Receta.** La misma que E 5.24: derivar, evaluar, despejar $y'$; derivar la ecuación derivada (no la evaluada), evaluar con $y'$ y despejar $y''$.

sympy: $y'(0)=-e^{-1}\approx-0{,}367879$, $y''(0)=e^{-2}\approx0{,}135335$; numérico con diferencias finitas: $-0{,}367879$ y $0{,}135335$.

### Propio 4: hallar el parámetro y decidir qué variable se despeja (difícil)

> Sea $F(x,y)=x^3+y^3-3xy$ (folium de Descartes, U Ej. 5.12). (a) ¿En qué puntos de la curva $F=0$ **no** se puede despejar ninguna de las dos variables con el teorema? (b) En el punto $\left(\frac32,\frac32\right)$, halla $y'$ e $y''$ y la recta tangente.

1. **(a)** Hay que resolver $F=0$, $F_x=3x^2-3y=0$, $F_y=3y^2-3x=0$. De $F_x=0$: $y=x^2$; en $F_y=0$: $x^4=x$, luego $x=0$ o $x=1$. $(0,0)$: $F=0$ ✓. $(1,1)$: $F=1+1-3=-1\ne0$, no está en la curva. Solo **$(0,0)$**.
2. **(b) Comprobar el punto:** $F\left(\frac32,\frac32\right)=\frac{27}8+\frac{27}8-\frac{27}4=0$ ✓. $F_y=3\cdot\frac94-\frac92=\frac94\ne0$ ✓.
3. **$y'$:** con la fórmula de U, $y'=\frac{y-x^2}{y^2-x}=\frac{\frac32-\frac94}{\frac94-\frac32}=\frac{-3/4}{3/4}=-1$. Tangente: $y=\frac32-(x-\frac32)$, es decir $x+y=3$.
4. **$y''$:** con la forma simplificada (válida sobre la curva, ver U Ej. 5.12 arriba), $y''=-\frac{2xy}{(y^2-x)^3}=-\frac{2\cdot\frac94}{\left(\frac34\right)^3}=-\frac{9/2}{27/64}=-\frac{32}{3}$.
5. **Lectura:** el punto $\left(\frac32,\frac32\right)$ es la «punta» del lazo, sobre la recta $y=x$; $y''<0$: allí el lazo se curva hacia abajo respecto a su tangente $x+y=3$.

sympy: único punto real con $F=F_x=F_y=0$: $(0,0)$; en $\left(\frac32,\frac32\right)$: $y'=-1$, $y''=-\frac{32}3$ (verificado con la fórmula de U y con la simplificada).

---

## Notas internas (no pasar al HTML)

- **E 5.23, solución impresa:** en el apartado $(2,1)$ aparece «$\frac{\partial f}{\partial y}(-1,0)=0$» y en el $(-1,0)$ «$\frac{\partial f}{\partial y}(0,1)=0$»: las parciales están cambiadas de punto. Lo correcto (arriba): $f_y(0,1)=2$, $f_y(2,1)=-2$, $f_y(-1,0)=0$. Además el texto extraído muestra «$f(2,1)=0$» y «$\frac{\partial f}{\partial y}(0,1)=0$» porque pdftotext pierde la barra de $\ne$. Conclusión a) correcta.
- **X p. 30, apartado (a):** escribe $\frac{dg}{dy}=\frac{dx}{dy}=\frac{\partial f/\partial y}{\partial f/\partial x}$ sin el signo menos, y $g:V\to U$ con «$U$ que contiene a 1, $V$ de 1» (nombres cruzados respecto a «para todo $x\in U$, $y\in V$»). Arriba se escribe la fórmula con el signo y la notación coherente. El resultado de (b) del impreso ($-\frac16$, $-\frac{43}{108}$) es correcto.
- **X p. 30:** la cabecera del examen (Sept 2012, reserva, Mecánica, Modelo A) no está en las pp. 29-30; se toma del índice `indice_examenes_1.md`.
- **E 5.24, 5.25, 5.26, 5.27:** en el texto extraído aparecen «$=0$» donde la imagen tiene $\ne0$ (pdftotext pierde la barra). Los valores son los de arriba.
- **E 5.25:** el complemento del paso 5 (la curva no admite $x=g(y)$ cerca de $(1,1)$) es propio, comprobado numéricamente; el libro solo dice «no está garantizado… pero esto no significa que no sea posible».
- **U Ej. 5.12:** la simplificación $y''=-\frac{2xy}{(y^2-x)^3}$ sobre la curva es propia (usa $x^3+y^3=3xy$); verificada con sympy y la parametrización.
- **Propio 4 (b):** $y''\left(\frac32\right)=-\frac{32}3$ comprobado con sympy de tres formas: fórmula de U, forma simplificada $-\frac{2xy}{(y^2-x)^3}$ y derivación implícita directa.
- U no desarrolla sistemas de ecuaciones implícitas (solo la nota 3 de p. 211, $f:\mathbb{R}^{n+m}\to\mathbb{R}^m$); no hay ejercicios de E ni X de sistemas.
