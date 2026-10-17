# Soluciones Tema 4.1 — El espacio $\mathbb{R}^n$

Resolución paso a paso de los ejercicios de **E** de la sección 4.1 (Ejercicios 4.1-4.8, E pp. 136-141), de las preguntas de examen **X** sobre $\mathbb{R}^n$ (X pp. 1, 13, 22-23, 53, 70, 89, 139) y de 4 ejemplos propios. Todos los cálculos se han comprobado con sympy (salidas resumidas al final de cada bloque). Se han leído como imagen (PyMuPDF) E p. 139 y X pp. 13, 22, 23, 89 y 139.

Páginas: U impresa (= PDF + 2); E impresa = PDF; X = página PDF de `Examenes-resueltos-Calculo.pdf`.

## 0. Herramientas de teoría que se usan

| Clave | Enunciado (resumido) | Dónde |
|---|---|---|
| $\mathbb{R}^n$, operaciones | $\bar x=(x_1,\dots,x_n)$. Suma componente a componente: $\bar x+\bar y=(x_1+y_1,\dots,x_n+y_n)$. Producto por un número: $\lambda\bar x=(\lambda x_1,\dots,\lambda x_n)$. Base canónica $e_1,\dots,e_n$. | U §4.1.2, pp. 142-143 |
| **Def. 4.1** | Producto escalar $\bar x\cdot\bar y=x_1y_1+\dots+x_ny_n$ (**es un número**). Norma $\|\bar x\|=\sqrt{\bar x\cdot\bar x}=\sqrt{x_1^2+\dots+x_n^2}$ («longitud»). Unitario: norma 1. | U §4.1.2, p. 143 |
| Distancia | $d(\bar x,\bar y)=\|\bar y-\bar x\|=\sqrt{(y_1-x_1)^2+\dots+(y_n-x_n)^2}$. | U p. 143 |
| Discos / bolas | Disco abierto de centro $(a,b)$ y radio $r$: $\{(x,y): d((a,b),(x,y))<r\}$; cerrado con $\le$. En $\mathbb{R}^3$ o $\mathbb{R}^n$: bola, definiciones semejantes. | U pp. 145-146 |
| Interior, frontera | $(a,b)$ **interior** a $C$ si **existe** un disco abierto centrado en $(a,b)$ contenido en $C$. $(a,b)$ **frontera** de $C$ si **todo** disco abierto centrado en $(a,b)$ tiene puntos de $C$ y puntos fuera de $C$. | U pp. 145-146 |
| Abierto, cerrado, acotado | **Abierto**: vacío o todos sus puntos interiores. **Cerrado**: contiene a su frontera. **Acotado**: cabe en un disco. | U p. 146 |
| **Def. 4.2** | Ángulo $\alpha\in[0,\pi]$ entre $\bar x,\bar y$ no nulos: $\cos\alpha=\dfrac{\bar x\cdot\bar y}{\|\bar x\|\,\|\bar y\|}$. **Ortogonales** $\iff$ $\bar x\cdot\bar y=0$. | U p. 147 |
| Polares | $(x,y)\neq(0,0)$: $x=\rho\cos\theta$, $y=\rho\operatorname{sen}\theta$; $\rho=\sqrt{x^2+y^2}>0$, $\operatorname{tg}\theta=y/x$, $\theta\in[0,2\pi)$. Si $x=0$: $\theta=\pi/2$ ($y>0$) o $3\pi/2$ ($y<0$). | U §4.1.3, p. 148 |
| Cilíndricas | $(\rho,\theta,z)$: $x=\rho\cos\theta$, $y=\rho\operatorname{sen}\theta$, $z=z$. | U p. 149 |
| Esféricas | $(\rho,\theta,\phi)$, $\rho>0$, $\theta\in[0,2\pi)$, $\phi\in[-\pi/2,\pi/2]$: $x=\rho\cos\phi\cos\theta$, $y=\rho\cos\phi\operatorname{sen}\theta$, $z=\rho\operatorname{sen}\phi$; $\rho=\sqrt{x^2+y^2+z^2}$, $\operatorname{sen}\phi=z/\rho$. | U pp. 150-151 |

**Propiedades que U da por sabidas «del Álgebra» (p. 143) pero no enuncia** (marcar como *propia* o citar el margen de E):

- **Desigualdad triangular:** $\|\bar u+\bar v\|\le\|\bar u\|+\|\bar v\|$. La enuncia **E** en el margen de p. 137 (Ejercicio 4.4). Análogo en $\mathbb{R}$: $|a+b|\le|a|+|b|$ (S App. A, p. A8). Consecuencia que se usa en 4.5: $\|\bar q\|\ge\|\bar p\|-\|\bar p-\bar q\|$.
- **Homogeneidad:** $\|\lambda\bar u\|=|\lambda|\,\|\bar u\|$ (se comprueba en E 4.4.2). Ojo al **valor absoluto**.
- Cauchy-Schwarz, $|\bar u\cdot\bar v|\le\|\bar u\|\|\bar v\|$, es lo que garantiza que el cociente de la Def. 4.2 está en $[-1,1]$; no aparece ni en U ni en E: solo como comentario *propio*.

**Aviso sobre U (omisión).** U dice que las cilíndricas valen para $\mathbb{R}^3\setminus\{(0,0,0)\}$ (p. 149), pero en todo el **eje $z$** (puntos $(0,0,z)$) es $\rho=0$ y el ángulo $\theta$ no está determinado; lo mismo pasa con $\theta$ en esféricas. La unicidad de $(\rho,\theta,z)$ o $(\rho,\theta,\phi)$ solo se tiene fuera del eje $z$. En los ejercicios no aparece ningún punto del eje $z$, así que no afecta a los resultados.

**La trampa del ángulo $\theta$ (aparece en 4.6, 4.8 y en los propios).** La calculadora da $\arctan(y/x)\in(-\pi/2,\pi/2)$, que solo es el ángulo correcto en el primer cuadrante. Regla segura, con $\theta_0=\arctan|y/x|\in[0,\pi/2)$:

| Signos | Cuadrante | $\theta$ |
|---|---|---|
| $x>0,\ y\ge0$ | I | $\theta_0$ |
| $x<0,\ y\ge0$ | II | $\pi-\theta_0$ |
| $x<0,\ y<0$ | III | $\pi+\theta_0$ |
| $x>0,\ y<0$ | IV | $2\pi-\theta_0$ |
| $x=0$ | eje $y$ | $\pi/2$ si $y>0$; $3\pi/2$ si $y<0$ |

---

## 1. Ejercicios de E (orden de dificultad creciente; numeración conservada)

Orden propuesto para aprender: **4.1 → 4.2 → 4.3 → 4.4 → 4.6 → 4.7 → 4.8 → 4.5** (el 4.5, de abiertos/cerrados/frontera, es el más conceptual).

---

### Ejercicio 4.1 (E p. 136)

> ¿Se pueden multiplicar escalarmente tres vectores? ¿Y un vector de $\mathbb{R}^2$ con uno de $\mathbb{R}^3$?

**Idea en una frase.** El producto escalar toma **dos vectores del mismo $\mathbb{R}^n$** y devuelve **un número**; cualquier otra cosa no encaja en la definición.

1. **Qué dice la definición.** Def. 4.1 (U p. 143): $\bar x\cdot\bar y=x_1y_1+\dots+x_ny_n$ con $\bar x,\bar y\in\mathbb{R}^n$. Hay **dos** vectores y los dos tienen **el mismo número $n$** de componentes, porque se multiplican «la primera con la primera, la segunda con la segunda…».
2. **Tres vectores.** Si intentamos $(\bar u\cdot\bar v)\cdot\bar w$: el primer paréntesis ya es un **número** $\lambda$. Lo que queda, $\lambda\,\bar w$, no es un producto escalar (no son dos vectores), sino el producto de un número por un vector (que da un vector, ver 4.2). Así que **no** existe un «producto escalar de tres vectores».
3. **$\mathbb{R}^2$ con $\mathbb{R}^3$.** Por ejemplo $(1,2)$ y $(3,4,5)$: la tercera componente $5$ no tiene pareja con la que multiplicarse. La definición no se aplica: **no**.

**Respuesta:** no en ambos casos.

**Receta.** Antes de operar, mirar el *tipo* de cada objeto: vector·vector (mismo $n$) $\to$ número; número·vector $\to$ vector; nada más.

**Error típico.** Rellenar con ceros el vector corto ($(1,2)\to(1,2,0)$) y «multiplicar»: eso es otra cosa (identificar $\mathbb{R}^2$ con un plano de $\mathbb{R}^3$), no el producto escalar de la Def. 4.1.

Fuente: E Ej. 4.1 p. 136; U §4.1.2 Def. 4.1 p. 143.

---

### Ejercicio 4.2 (E p. 136)

> El vector $(\bar u\cdot\bar v)\,\bar w$, con $\bar u,\bar v,\bar w\in\mathbb{R}^n$ verifica:
> a) Es nulo o paralelo al vector $\bar w$. b) Es nulo o paralelo al vector $\bar v$. c) Es nulo o paralelo al vector $\bar u$. d) Esa expresión no da lugar a un vector.

**Idea en una frase.** Lo de dentro del paréntesis es un número $\lambda$, y «número por $\bar w$» es $\bar w$ estirado, encogido o dado la vuelta: paralelo a $\bar w$, o el vector cero.

1. **Tipo del paréntesis.** $\bar u\cdot\bar v$ es un producto escalar (Def. 4.1, U p. 143): un número. Llamémoslo $\lambda=\bar u\cdot\bar v$.
2. **Tipo del total.** $\lambda\bar w=(\lambda w_1,\dots,\lambda w_n)$ es producto por escalar (U p. 143): **es un vector** de $\mathbb{R}^n$. Descarta la d).
3. **Cuándo es el vector nulo.** $\lambda\bar w=\bar 0$ si $\lambda=0$ (es decir, $\bar u$ y $\bar v$ ortogonales) o si $\bar w=\bar 0$.
4. **Si no es nulo,** es un múltiplo no nulo de $\bar w$, y eso es exactamente «paralelo a $\bar w$» (mismo sentido si $\lambda>0$, opuesto si $\lambda<0$).
5. **Por qué no b) ni c).** Un contraejemplo basta: $\bar u=\bar v=(1,0)$, $\bar w=(0,1)$ da $(\bar u\cdot\bar v)\bar w=1\cdot(0,1)=(0,1)$, que no es nulo ni paralelo a $(1,0)$.

**Respuesta: a).**

*Matiz sobre E.* La solución escribe «siempre es paralelo al vector $\bar w$» y justo después corrige con el caso nulo; lo exacto es «nulo o paralelo», como dice la opción a).

**Receta.** En una expresión con varios productos, ir de dentro afuera anotando qué sale en cada paso (número o vector); un número por un vector es siempre «nulo o paralelo» a ese vector.

**Error típico.** Leer $(\bar u\cdot\bar v)\bar w$ como «algo entre los tres vectores» y elegir d); o decir «paralelo a $\bar w$» olvidando el caso $\bar u\cdot\bar v=0$.

Fuente: E Ej. 4.2 p. 136; U §4.1.2 p. 143.

---

### Ejercicio 4.3 (E p. 136) — también X p. 1 (Feb 2010)

> ¿Son ortogonales los vectores $(0,1,2)$ y $(-3,-4,2)$?

**Idea en una frase.** Ortogonal = producto escalar cero; basta multiplicar componente a componente y sumar.

1. **Criterio.** Def. 4.2 (U p. 147): dos vectores son ortogonales si y solo si su producto escalar es $0$. (Si los dos son no nulos, $\cos\alpha=0$, o sea $\alpha=\pi/2$.)
2. **Cálculo** (Def. 4.1): $(0,1,2)\cdot(-3,-4,2)=0\cdot(-3)+1\cdot(-4)+2\cdot2=0-4+4=0.$
3. **Conclusión.** Sí, son ortogonales.

**Lo que hay que escribir en el examen:** la fórmula del producto escalar, la cuenta $0-4+4=0$ y la frase «como el producto escalar es 0, son ortogonales».

**Receta.** Para saber si son ortogonales, calcular $\bar u\cdot\bar v$ y comprobar si es 0.

**Error típico.** Multiplicar las componentes y dar el vector $(0,-4,4)$ como resultado (eso no es el producto escalar: falta **sumar**).

Fuente: E Ej. 4.3 p. 136; U Def. 4.1 p. 143 y Def. 4.2 p. 147. sympy: `0`.

---

### Ejercicio 4.4 (E pp. 136-137)

> Dados $\bar u=(-1,1)$ y $\bar v=(2,3)$ se pide:
> 1. Calcular $\bar u+\bar v$, $\|\bar u\|$, $\|\bar v\|$ y $\|\bar u+\bar v\|$. ¿Se cumple $\|\bar u\|+\|\bar v\|=\|\bar u+\bar v\|$? ¿Contradice esto que cumpla la desigualdad triangular?
> 2. Calcular $3\bar u$ y $\|3\bar u\|$. ¿Se cumple $\|3\bar u\|=3\|\bar u\|$?
> 3. Representar gráficamente $\bar u$, $\bar v$, $\bar u+\bar v$ y $3\bar u$.

**Idea en una frase.** La longitud de la suma no es la suma de longitudes (un lado de un triángulo es más corto que los otros dos juntos), pero multiplicar por 3 sí multiplica la longitud por 3.

**Apartado 1.**

1. **Suma** (componente a componente, U p. 143): $\bar u+\bar v=(-1+2,\,1+3)=(1,4)$.
2. **Normas** (Def. 4.1, U p. 143; norma = raíz de la suma de los cuadrados de las componentes):
   $\|\bar u\|=\sqrt{(-1)^2+1^2}=\sqrt2\approx1{,}414$, $\quad\|\bar v\|=\sqrt{2^2+3^2}=\sqrt{13}\approx3{,}606$, $\quad\|\bar u+\bar v\|=\sqrt{1^2+4^2}=\sqrt{17}\approx4{,}123$.
3. **Igualdad.** $\|\bar u\|+\|\bar v\|=\sqrt2+\sqrt{13}\approx5{,}020\neq4{,}123\approx\|\bar u+\bar v\|$. **No** se cumple.
   (Sin calculadora: si fuese $\sqrt2+\sqrt{13}=\sqrt{17}$, elevando al cuadrado $15+2\sqrt{26}=17$, o sea $\sqrt{26}=1$, falso.)
4. **Desigualdad triangular.** La desigualdad triangular (margen de E p. 137) dice $\|\bar u+\bar v\|\le\|\bar u\|+\|\bar v\|$: **menor o igual**, no igual. Aquí $4{,}12\le5{,}02$: se cumple, con desigualdad estricta. **No hay contradicción.**
   *Por qué es estricta:* en el paralelogramo de la figura, $\bar u$, $\bar v$ y $\bar u+\bar v$ son los lados de un triángulo, y un lado es más corto que la suma de los otros dos. La igualdad solo ocurre si $\bar u$ y $\bar v$ apuntan en el mismo sentido (triángulo «aplastado»); $(-1,1)$ y $(2,3)$ no lo hacen.

**Apartado 2.**

5. $3\bar u=(3\cdot(-1),\,3\cdot1)=(-3,3)$ (producto por escalar, U p. 143).
6. $\|3\bar u\|=\sqrt{(-3)^2+3^2}=\sqrt{18}=\sqrt{9\cdot2}=3\sqrt2=3\|\bar u\|$. **Sí** se cumple.
   *Por qué en general:* $\|\lambda\bar u\|=\sqrt{\lambda^2u_1^2+\dots+\lambda^2u_n^2}=\sqrt{\lambda^2}\,\|\bar u\|=|\lambda|\,\|\bar u\|$. Con $\lambda=3>0$, $|3|=3$.

**Apartado 3.** Se dibujan flechas desde el origen hasta $(-1,1)$, $(2,3)$, $(1,4)$ y $(-3,3)$. Se ve que $\bar u+\bar v$ es la diagonal del paralelogramo de lados $\bar u$ y $\bar v$, y que $3\bar u$ está sobre la misma recta que $\bar u$, con el mismo sentido y triple de largo (figura en E p. 137).

**Receta.** Norma = $\sqrt{\text{suma de cuadrados}}$. Recordar: $\|\bar u+\bar v\|\le\|\bar u\|+\|\bar v\|$ (en general $<$) y $\|\lambda\bar u\|=|\lambda|\|\bar u\|$.

**Errores típicos.** (i) Creer que $\|\bar u+\bar v\|=\|\bar u\|+\|\bar v\|$ («la norma es lineal»): falso. (ii) Escribir $\|-3\bar u\|=-3\|\bar u\|$: una norma nunca es negativa; es $|-3|\,\|\bar u\|=3\sqrt2$. (iii) Escribir $\sqrt{(-1)^2+1^2}=\sqrt{-1+1}$ (el cuadrado de $-1$ es $+1$).

Fuente: E Ej. 4.4 pp. 136-137 (desigualdad triangular en el margen de p. 137); U §4.1.2 p. 143 (y U Ej. 4.1 p. 144, mismo tipo de cuentas). sympy: $\bar u+\bar v=(1,4)$; $\sqrt2,\sqrt{13},\sqrt{17}$; $5{,}0198$ frente a $4{,}1231$; $\|3\bar u\|=3\sqrt2$.

---

### Ejercicio 4.6 (E p. 140)

> Dados $\bar u=(-1,1)$ y $\bar v=(2,3)$, se pide:
> 1. Expresar $\bar u$ en coordenadas polares.
> 2. Determinar el ángulo que forman $\bar u$ y $\bar v$.

**Idea en una frase.** Polares = (distancia al origen, ángulo con el eje $x$ positivo), eligiendo el ángulo por el cuadrante; el ángulo entre dos vectores sale del producto escalar.

**Apartado 1** (U §4.1.3, p. 148).

1. **Radio:** $\rho=\sqrt{x^2+y^2}=\sqrt{(-1)^2+1^2}=\sqrt2$.
2. **Tangente:** $\operatorname{tg}\theta=y/x=1/(-1)=-1$.
3. **Cuadrante:** $x=-1<0$, $y=1>0$: **segundo cuadrante**, $\theta\in(\pi/2,\pi)$.
4. **Ángulo:** en $[0,2\pi)$ hay dos ángulos con tangente $-1$: $3\pi/4$ (II) y $7\pi/4$ (IV). Como estamos en el II, $\theta=3\pi/4$. (Con la tabla del §0: $\theta_0=\arctan1=\pi/4$, $\theta=\pi-\pi/4=3\pi/4$.)
5. **Comprobación** (siempre conviene): $\sqrt2\cos(3\pi/4)=\sqrt2\cdot(-\tfrac{\sqrt2}{2})=-1$ ✓, $\sqrt2\operatorname{sen}(3\pi/4)=1$ ✓.

**Resultado:** $(\rho,\theta)=(\sqrt2,\,3\pi/4)$.

**Apartado 2** (Def. 4.2, U p. 147).

6. **Producto escalar:** $\bar u\cdot\bar v=(-1)\cdot2+1\cdot3=1$.
7. **Normas** (de 4.4): $\|\bar u\|=\sqrt2$, $\|\bar v\|=\sqrt{13}$.
8. **Coseno:** $\cos\alpha=\dfrac{1}{\sqrt2\sqrt{13}}=\dfrac1{\sqrt{26}}\approx0{,}1961$.
9. **Ángulo:** $\alpha=\arccos\frac1{\sqrt{26}}\approx1{,}3734$ rad $\approx78{,}69^\circ$. Aquí no hay que elegir cuadrante: $\arccos$ devuelve un valor en $[0,\pi]$ (U p. 147), que es justo el rango del ángulo entre vectores. Como $\cos\alpha>0$, el ángulo es agudo.

**Receta.** Polares: $\rho=\sqrt{x^2+y^2}$, $\theta$ por la tangente **y** el cuadrante (comprobar sustituyendo). Ángulo entre vectores: $\alpha=\arccos\frac{\bar u\cdot\bar v}{\|\bar u\|\|\bar v\|}$.

**Errores típicos.** (i) $\theta=\arctan(-1)=-\pi/4$: no está en $[0,2\pi)$ y además es el cuarto cuadrante; el punto está en el segundo. (ii) Calculadora en grados cuando se piden radianes (E p. 141: «siempre expresamos los ángulos en radianes»). (iii) Confundir el ángulo polar de $\bar u$ ($3\pi/4$, con el eje $x$) con el ángulo entre $\bar u$ y $\bar v$.

Fuente: E Ej. 4.6 p. 140; U §4.1.3 p. 148 (polares, como U Ej. 4.4 p. 149) y Def. 4.2 p. 147. sympy: `atan2(1,-1)=3*pi/4`; $\alpha=1{,}37340$ rad $=78{,}690^\circ$.

---

### Ejercicio 4.7 (E p. 140)

> Si las coordenadas cartesianas de un punto son $(1,1,1)$, ¿cuáles son sus coordenadas cilíndricas?

**Idea en una frase.** Cilíndricas = polares de $(x,y)$ + la misma $z$.

1. **Fórmulas** (U p. 149): $\rho=\sqrt{x^2+y^2}$, $\operatorname{tg}\theta=y/x$ (con el cuadrante), $z=z$.
2. $\rho=\sqrt{1+1}=\sqrt2$.
3. $\operatorname{tg}\theta=1/1=1$, con $x>0$, $y>0$ (primer cuadrante): $\theta=\pi/4$.
4. $z=1$.
5. **Comprobación:** $\sqrt2\cos\frac\pi4=1$, $\sqrt2\operatorname{sen}\frac\pi4=1$ ✓.

**Resultado:** $(\rho,\theta,z)=(\sqrt2,\,\pi/4,\,1)$.

**Receta.** De cartesianas a cilíndricas: trabajar solo con $(x,y)$ como en polares y copiar $z$.

**Error típico.** Poner $\rho=\sqrt{x^2+y^2+z^2}=\sqrt3$: esa es la $\rho$ de **esféricas** (distancia al origen); en cilíndricas $\rho$ es la distancia al **eje $z$**.

Fuente: E Ej. 4.7 p. 140; U §4.1.3 p. 149.

---

### Ejercicio 4.8 (E p. 141)

> 1. Dado $(1,2,-1)$ en coordenadas cartesianas, se pide determinar sus coordenadas cilíndricas y esféricas.
> 2. Dado $(1,\pi,0)$ en coordenadas cilíndricas, se pide determinar sus coordenadas cartesianas.
> 3. Dado $(1,\pi/2,0)$ en coordenadas esféricas, se pide determinar sus coordenadas cartesianas.

**Idea en una frase.** Ir hacia cartesianas es solo sustituir en las fórmulas; salir de cartesianas exige elegir bien los ángulos ($\theta$ por el cuadrante, $\phi$ por el signo de $z$).

**Apartado 1.** Punto $(x,y,z)=(1,2,-1)$.

*Cilíndricas* (U p. 149):
1. $\rho=\sqrt{1^2+2^2}=\sqrt5$.
2. $\operatorname{tg}\theta=2/1=2$; $x>0$, $y>0$ (primer cuadrante), así que vale el valor de la calculadora: $\theta=\arctan2\approx1{,}1071$ rad.
3. $z=-1$. **Cilíndricas:** $(\sqrt5,\ \arctan2,\ -1)\approx(2{,}2361;\ 1{,}1071;\ -1)$.

*Esféricas* (U pp. 150-151):
4. $\rho=\sqrt{x^2+y^2+z^2}=\sqrt{1+4+1}=\sqrt6$ (ahora es la distancia al origen).
5. $\theta$ es **el mismo** que en cilíndricas (U p. 150: se calcula «con las indicaciones dadas en las coordenadas cilíndricas»): $\theta=\arctan2\approx1{,}1071$.
6. $\operatorname{sen}\phi=z/\rho=-1/\sqrt6$. Como $\phi\in[-\pi/2,\pi/2]$ y en ese intervalo el seno toma cada valor una sola vez, $\phi=\arcsen(-1/\sqrt6)\approx-0{,}4205$ rad. Es negativo porque el punto está **por debajo** del plano $xy$ ($z<0$).
7. **Comprobación:** $\cos\phi=\sqrt{1-1/6}=\sqrt{5/6}$ (positivo en $[-\pi/2,\pi/2]$), así que $\rho\cos\phi=\sqrt6\sqrt{5/6}=\sqrt5$, y $\sqrt5\cos\theta=1$, $\sqrt5\operatorname{sen}\theta=2$ ✓; $z=\sqrt6\cdot(-1/\sqrt6)=-1$ ✓.

**Esféricas:** $(\sqrt6,\ \arctan2,\ \arcsen(-1/\sqrt6))\approx(2{,}4495;\ 1{,}1071;\ -0{,}4205)$.

**Apartado 2.** Cilíndricas $(\rho,\theta,z)=(1,\pi,0)$:
8. $x=1\cdot\cos\pi=-1$, $y=1\cdot\operatorname{sen}\pi=0$, $z=0$. **Cartesianas:** $(-1,0,0)$. (Ángulo $\pi$ = semieje $x$ negativo, a distancia 1 del eje $z$.)

**Apartado 3.** Esféricas $(\rho,\theta,\phi)=(1,\pi/2,0)$:
9. $x=1\cdot\cos0\cdot\cos\frac\pi2=0$, $y=1\cdot\cos0\cdot\operatorname{sen}\frac\pi2=1$, $z=1\cdot\operatorname{sen}0=0$. **Cartesianas:** $(0,1,0)$. ($\phi=0$: en el plano $xy$; $\theta=\pi/2$: semieje $y$ positivo.)

**Receta.** Cartesianas a cilíndricas/esféricas: $\theta$ con tangente + cuadrante; $\rho$ cilíndrica $=\sqrt{x^2+y^2}$, $\rho$ esférica $=\sqrt{x^2+y^2+z^2}$; $\phi=\arcsen(z/\rho)$. Al revés: sustituir.

**Errores típicos.** (i) Usar la convención de otros libros, en la que el ángulo esférico se mide desde el eje $z$ ($z=\rho\cos\phi$, $\phi\in[0,\pi]$). **En U**, $\phi$ se mide desde el plano $xy$ y $z=\rho\operatorname{sen}\phi$: en el examen manda U. (ii) Usar la misma $\rho$ en cilíndricas y esféricas.

Fuente: E Ej. 4.8 p. 141 (E escribe $\varphi$); U §4.1.3 pp. 149-152 (mismo tipo que U Ej. 4.6-4.8). sympy: $\sqrt5$, `atan(2)=1.10715`, $\sqrt6$, $-0{,}42053$; $(-1,0,0)$; $(0,1,0)$.

---

### Ejercicio 4.5 (E pp. 138-139)

> Dado el conjunto $C=\{(x,y)\in\mathbb{R}^2: x^2+y^2\le4\}$ se pide:
> 1. Representarlo gráficamente.
> 2. Determinar y representar su frontera.
> 3. Razonar si es un conjunto abierto o cerrado.

**Idea en una frase.** $C$ es el disco de radio 2 **con** su borde; la frontera es la circunferencia del borde y, como $C$ la contiene, $C$ es cerrado.

**Apartado 1.**
1. $x^2+y^2=d\big((0,0),(x,y)\big)^2$ (distancia, U p. 143). Así, $x^2+y^2\le4$ significa «distancia al origen $\le2$». Es el **disco cerrado** de centro $(0,0)$ y radio 2 (U p. 145): el círculo relleno, borde incluido (se dibuja con borde continuo).

**Apartado 2.** Afirmación: la frontera es la circunferencia $S=\{x^2+y^2=4\}$. Hay que ver dos cosas: que los puntos de $S$ son frontera y que los demás no.

2. **Cada punto de $S$ es frontera.** *Ejemplo concreto:* $P=(2,0)$ y un disco de radio $r=0{,}1$ centrado en él. Contiene a $P$, que es de $C$ ($4\le4$), y también a $(2{,}05;\,0)$, que no es de $C$ ($4{,}2025>4$). Lo mismo con cualquier $r$: $(2+r/2,\,0)$ está a distancia $r/2<r$ de $P$ y fuera de $C$.
   *En general:* si $\|P\|=2$, cualquier disco de radio $r$ centrado en $P$ contiene $P\in C$ y el punto $Q=(1+\tfrac r4)P$, que dista $\|Q-P\|=\tfrac r4\|P\|=\tfrac r2<r$ de $P$ y tiene $\|Q\|=2+\tfrac r2>2$, o sea $Q\notin C$. Por la definición de punto frontera (U p. 146), $P$ es frontera. (Esta es la demostración analítica que E «deja para el lector».)
3. **Un punto de dentro ($\|P''\|<2$) no es frontera: es interior.** *Ejemplo:* $P''=(1,0)$ y disco de radio $\delta=2-1=1$: si $Q$ está a distancia $<1$ de $(1,0)$, entonces $\|Q\|<1+1=2$, luego $Q\in C$. *En general,* con $s=\|P''\|<2$ y $\delta=2-s>0$: si $\|Q-P''\|<\delta$, la desigualdad triangular da $\|Q\|\le\|P''\|+\|Q-P''\|<s+(2-s)=2$. Todo el disco está en $C$; no tiene puntos de fuera, así que **no** es frontera (es interior, U p. 145).
4. **Un punto de fuera ($\|P'\|>2$) no es frontera.** Con $s=\|P'\|>2$ y $\delta=s-2$: si $\|Q-P'\|<\delta$, entonces $\|Q\|\ge\|P'\|-\|P'-Q\|>s-(s-2)=2$, así que $Q\notin C$. El disco no tiene puntos de $C$: no es frontera.
5. **Conclusión:** frontera $=S=\{(x,y):x^2+y^2=4\}$ (dibujo: solo la circunferencia; por ejemplo $(2,0)$ y $(\sqrt2,\sqrt2)$ están en ella).

**Apartado 3.**
6. **Cerrado:** por definición (U p. 146), $C$ es cerrado si contiene a su frontera. Todos los puntos de $S$ cumplen $x^2+y^2=4\le4$: están en $C$. **$C$ es cerrado.**
7. **No es abierto** (no se pide explícitamente, pero la pregunta es «abierto o cerrado»): $(2,0)\in C$ y no es interior (paso 2: todo disco centrado en él se sale de $C$).

**Errata en E (p. 139, verificada en la imagen).** El texto dice «elegimos dos que no estén en la circunferencia: $P'\in C$ y $P''\notin C$. Entonces podemos elegir un círculo centrado en $P'$ de tal forma que sus intersección con $C$ sea el conjunto vacío. Y podemos elegir otro círculo centrado en $P''$ que esté totalmente incluido en el conjunto $C$». Las pertenencias están **intercambiadas**: un disco centrado en un punto de $C$ siempre corta a $C$ (contiene al propio centro). Debe decir **$P'\notin C$ y $P''\in C$**, que es además lo que muestra la figura de esa misma página ($P''$ dentro del disco, $P'$ fuera).

**Receta.** (1) Traducir la desigualdad a «distancia al centro $\le$ / $<$ radio». (2) Frontera = puntos con distancia **igual** al radio (todo disco centrado en ellos tiene puntos dentro y fuera; los puntos de dentro o de fuera tienen un disco de radio «distancia al borde» que no lo cruza). (3) Con $\le$ contiene el borde: cerrado; con $<$: abierto.

**Errores típicos.** (i) Pensar que «abierto» y «cerrado» son contrarios: hay conjuntos que no son ni una cosa ni otra (Ejemplo propio 2) y conjuntos que son ambas ($\mathbb{R}^2$ y $\emptyset$; U p. 146). (ii) Decir que la frontera de $C$ es «el exterior» o «todo lo que no es $C$». (iii) Dibujar el disco con borde discontinuo (eso indica que el borde **no** está incluido).

Fuente: E Ej. 4.5 pp. 138-139; U §4.1.2 pp. 145-146 (como U Ej. 4.3 p. 147, que es la versión abierta con «<»).

---

## 2. Así lo preguntan en el examen (X)

Las preguntas cortas de $\mathbb{R}^n$ (1 punto) son siempre del mismo tipo: **producto escalar y normas**, **distancia**, **ángulo/ortogonalidad** y **teoría de polares**. En X no hay preguntas sueltas de abiertos/cerrados/frontera: ese tipo se practica con E 4.5, y reaparece como paso intermedio en preguntas de extremos absolutos de temas posteriores (justificar que el conjunto es cerrado y acotado: X p. 25, Sept 2012, $x^2+y^2=1$; X p. 97, Sept 2018, $1\le x^2+y^2\le4$).

---

### X p. 1 (Feb 2010, 1ª sem., Ing. Eléctrica, P4, 1 punto)

> ¿Son ortogonales los vectores $(0,1,2)$ y $(-3,-4,2)$? Justifíquese la respuesta.

Es **idéntico al Ejercicio 4.3** de E (ver arriba). $(0,1,2)\cdot(-3,-4,2)=0-4+4=0$, luego **son ortogonales** (Def. 4.2, U p. 147). La solución de X es correcta.

**Receta.** Ortogonalidad = producto escalar nulo; la «justificación» es nombrar el criterio.

---

### X p. 13 (Feb 2011, 2ª sem., Mecánica, Modelo B, P4, 1 punto)

> Describa brevemente las coordenadas polares en $\mathbb{R}^2$. Indique también cómo se cambia de coordenadas polares a cartesianas y viceversa.

**Errata de X (verificada en la imagen).** La solución impresa solo dice «Vea la página 194 del libro "Cálculo para Ingenieros"». En la edición oficial actual de U (2023), la p. 194 es de §5.2 (regla de la cadena); las polares están en **U §4.1.3, pp. 148-149**. (La referencia era de otra edición.) Damos aquí la respuesta completa.

**Idea en una frase.** En vez de «cuánto a la derecha y cuánto arriba» $(x,y)$, se dice «a qué distancia del origen y en qué dirección» $(\rho,\theta)$.

**Respuesta modelo (lo que hay que escribir):**

1. **Descripción.** Todo punto $(x,y)\in\mathbb{R}^2\setminus\{(0,0)\}$ queda determinado de forma única por un radio $\rho>0$ y un ángulo $\theta\in[0,2\pi)$: $\rho$ es la distancia del punto al origen, $\rho=\|(x,y)\|$, y $\theta$ es el ángulo que forma el vector $(x,y)$ con el semieje $x$ positivo, medido en sentido antihorario (U p. 148).
2. **De polares a cartesianas:** $x=\rho\cos\theta,\quad y=\rho\operatorname{sen}\theta.$ (Trigonometría en el triángulo rectángulo de hipotenusa $\rho$.)
3. **De cartesianas a polares:** $\rho=\sqrt{x^2+y^2}$; $\operatorname{tg}\theta=y/x$ si $x\neq0$, eligiendo de los dos ángulos de $[0,2\pi)$ con esa tangente el del cuadrante que indican los signos de $x$ e $y$; si $x=0$, $\theta=\pi/2$ ($y>0$) o $\theta=3\pi/2$ ($y<0$).
4. **Ejemplos** (de U p. 149, para rematar): $(2,2\sqrt3)$ da $\rho=4$, $\operatorname{tg}\theta=\sqrt3$, primer cuadrante, $\theta=\pi/3$. Y $(\rho,\theta)=(2,7\pi/4)$ da $(x,y)=(\sqrt2,-\sqrt2)$.

**Receta.** Pregunta de teoría = definición (qué son $\rho$ y $\theta$ y sus rangos) + las dos fórmulas de cambio + el aviso del cuadrante + un ejemplo.

**Error típico.** Dar $\theta=\arctan(y/x)$ sin más (falla en los cuadrantes II, III y IV, y para $x=0$), u olvidar que el origen no tiene ángulo definido.

---

### X pp. 22-23 (Feb 2012, 2ª sem., Mecánica, Modelo B, P4, 1 punto)

> Calcule el producto escalar de $(1,2,3,4)$ y $(-1,-2,-3,-4)$ y la norma de estos dos vectores.

**Idea en una frase.** Las fórmulas de $\mathbb{R}^2$ y $\mathbb{R}^3$ valen igual en $\mathbb{R}^4$: multiplicar y sumar; raíz de la suma de cuadrados.

1. **Producto escalar** (Def. 4.1): $1\cdot(-1)+2\cdot(-2)+3\cdot(-3)+4\cdot(-4)=-1-4-9-16=-30$.
2. **Norma del primero:** $\sqrt{1+4+9+16}=\sqrt{30}$.
3. **Norma del segundo:** $\sqrt{(-1)^2+(-2)^2+(-3)^2+(-4)^2}=\sqrt{30}$ (también: es el primero por $-1$, y $\|-\bar x\|=|-1|\,\|\bar x\|$).
4. *Comentario:* $\bar x\cdot\bar y=-30=-\|\bar x\|\|\bar y\|$, así que $\cos\alpha=-1$ y $\alpha=\pi$: vectores opuestos, como debe ser.

X da los mismos resultados (correctos).

**Receta.** En $\mathbb{R}^n$, mismas fórmulas, más sumandos. Un producto escalar **puede ser negativo**; una norma **no**.

**Error típico.** Escribir $\|(-1,-2,-3,-4)\|=-\sqrt{30}$.

---

### X p. 53 (Sept 2015, Modelo A, P4, 1 punto)

> Calcular la distancia euclídea entre los puntos $(1,-1,0)$ y $(1,3,5)$.

1. **Fórmula** (U p. 143): $d(\bar x,\bar y)=\|\bar y-\bar x\|$.
2. **Diferencia:** $(1,3,5)-(1,-1,0)=(0,4,5)$ (X resta al revés y obtiene $(0,-4,-5)$; da igual porque $\|-\bar w\|=\|\bar w\|$).
3. **Norma:** $\sqrt{0^2+4^2+5^2}=\sqrt{41}\approx6{,}403$.

**Resultado:** $d=\sqrt{41}$ (X: correcto).

**Receta.** Distancia = norma de la resta (en cualquier orden).

**Error típico.** Restar mal un negativo: $3-(-1)=4$, no $2$.

---

### X p. 70 (Sept 2016, Modelo A, P4, 1 punto)

> Calcule la distancia entre los elementos $(4,2,0)$ y $(1,-1,3)\in\mathbb{R}^3$.

1. Diferencia: $(4,2,0)-(1,-1,3)=(3,3,-3)$.
2. $d=\sqrt{3^2+3^2+(-3)^2}=\sqrt{27}=3\sqrt3\approx5{,}196$.

X da $\sqrt{27}$ (correcto; conviene simplificar a $3\sqrt3$).

**Receta y error típico:** como en X p. 53; además, $\sqrt{27}=\sqrt{9\cdot3}=3\sqrt3$.

---

### X p. 89 (Feb 2018, Modelo A, P4, 1 punto)

> Calcule la distancia entre los puntos $(1,0,-1)$ y $(2,0,-1)$ con la métrica euclídea. Determine el ángulo que forman los vectores $(0,1,2)$ y $(1,-1,1)$.

**Idea en una frase.** Dos cuentas independientes: norma de una resta, y $\arccos$ del producto escalar dividido entre el producto de normas.

1. **Distancia:** $(1,0,-1)-(2,0,-1)=(-1,0,0)$; $d=\sqrt{(-1)^2+0+0}=1$. (Los puntos solo difieren en la $x$, en una unidad.)
2. **Producto escalar:** $(0,1,2)\cdot(1,-1,1)=0-1+2=1$.
3. **Normas:** $\|(0,1,2)\|=\sqrt5$, $\|(1,-1,1)\|=\sqrt3$.
4. **Coseno** (Def. 4.2): $\cos\alpha=\dfrac1{\sqrt5\sqrt3}=\dfrac1{\sqrt{15}}\approx0{,}2582$.
5. **Ángulo:** $\alpha=\arccos\dfrac1{\sqrt{15}}\approx\mathbf{1{,}3096}$ **rad** $\approx75{,}04^\circ$.

**Errata de X (verificada en la imagen y con sympy).** La solución impresa termina con «$\alpha=1.209$ radianes». Es incorrecto: $\cos(1{,}209)\approx0{,}354\neq0{,}258\approx1/\sqrt{15}$. El valor correcto es $\alpha=\arccos(1/\sqrt{15})\approx1{,}3096$ rad. Todo lo anterior de la solución de X, incluido $\cos\alpha=1/\sqrt{15}$, es correcto. (El enunciado impreso, además, ha perdido el símbolo del ángulo: «el ángulo  que forman».)

**Receta.** Ángulo: $\cos\alpha=\frac{\bar u\cdot\bar v}{\|\bar u\|\|\bar v\|}$ y $\alpha=\arccos(\dots)\in[0,\pi]$, en radianes; **comprobar** calculando el coseno del resultado.

**Error típico.** Teclear mal la calculadora (o usarla en grados) y no comprobar. Dejarlo en «$\alpha=\arccos(1/\sqrt{15})$» es una respuesta exacta válida.

sympy: $d=1$; $\bar u\cdot\bar v=1$; $\sqrt5,\sqrt3$; $\alpha=1{,}309639$ rad $=75{,}037^\circ$; $\cos(1{,}209)=0{,}35395$; $1/\sqrt{15}=0{,}25820$.

---

### X p. 139 (Sept 2018, Modelo B, Mecánica, P4, 1 punto) — **sin solución en X**

> Calcule el producto escalar de $(1,2,0,1)$ y $(-1,-2,3,0)$ y la norma de estos dos vectores.

1. **Producto escalar:** $1\cdot(-1)+2\cdot(-2)+0\cdot3+1\cdot0=-1-4+0+0=-5$.
2. $\|(1,2,0,1)\|=\sqrt{1+4+0+1}=\sqrt6\approx2{,}449$.
3. $\|(-1,-2,3,0)\|=\sqrt{1+4+9+0}=\sqrt{14}\approx3{,}742$.
4. *(Extra)* $\cos\alpha=-5/\sqrt{84}\approx-0{,}546$, $\alpha\approx2{,}148$ rad: ángulo obtuso, coherente con el signo negativo.

**Receta:** como X pp. 22-23. **Error típico:** saltarse los sumandos con un $0$ y desordenar las parejas de componentes.

sympy: $-5$, $\sqrt6$, $\sqrt{14}$, $\alpha=2{,}14784$.

---

## 3. Ejemplos propios (dificultad creciente)

### Propio 1 — Producto escalar, norma, unitario y ángulo en $\mathbb{R}^3$ (fácil)

> Sean $\bar a=(1,2,2)$ y $\bar b=(2,-1,2)$. Calcula $\bar a\cdot\bar b$, $\|\bar a\|$, $\|\bar b\|$, un vector unitario en la dirección de $\bar a$, el ángulo que forman, y comprueba la desigualdad triangular.

**Idea en una frase.** Todo sale de la Def. 4.1 y la Def. 4.2.

1. $\bar a\cdot\bar b=1\cdot2+2\cdot(-1)+2\cdot2=2-2+4=4$.
2. $\|\bar a\|=\sqrt{1+4+4}=3$; $\|\bar b\|=\sqrt{4+1+4}=3$.
3. **Unitario:** dividir por la norma, $\bar a/\|\bar a\|=(\tfrac13,\tfrac23,\tfrac23)$; su norma es $\sqrt{\tfrac19+\tfrac49+\tfrac49}=1$ ✓. (Por la homogeneidad, $\|\tfrac13\bar a\|=\tfrac13\cdot3=1$.)
4. $\cos\alpha=\tfrac4{3\cdot3}=\tfrac49$, $\alpha=\arccos\tfrac49\approx1{,}1102$ rad $\approx63{,}61^\circ$ (agudo, porque $\bar a\cdot\bar b>0$).
5. $\bar a+\bar b=(3,1,4)$, $\|\bar a+\bar b\|=\sqrt{26}\approx5{,}10\le6=\|\bar a\|+\|\bar b\|$ ✓.

**Receta.** Unitario = vector dividido por su norma. Signo del producto escalar: $>0$ agudo, $=0$ recto, $<0$ obtuso.

**Error típico.** Calcular el unitario dividiendo por la suma de componentes ($1+2+2=5$) en vez de por la norma.

Fuente: propia (sobre U Def. 4.1 p. 143 y Def. 4.2 p. 147). sympy: $4$, $3$, $3$, $(1/3,2/3,2/3)$, $\arccos(4/9)=1{,}11024$, $\sqrt{26}$.

---

### Propio 2 — Una corona: ni abierta ni cerrada (medio)

> $A=\{(x,y)\in\mathbb{R}^2: 1<x^2+y^2\le4\}$. Describe $A$, halla su frontera y decide si es abierto, cerrado y acotado.

**Idea en una frase.** Es el anillo entre las circunferencias de radio 1 (excluida) y 2 (incluida): tiene un borde que no le pertenece y otro que sí.

1. $1<x^2+y^2\le4$ equivale a $1<\|(x,y)\|\le2$: puntos a distancia del origen mayor que 1 y como mucho 2 (corona circular; borde interior discontinuo, exterior continuo).
2. **Frontera:** las dos circunferencias $\{x^2+y^2=1\}\cup\{x^2+y^2=4\}$, con el mismo razonamiento que en E 4.5 (en cada una, todo disco centrado en el punto tiene puntos con distancia al origen a ambos lados del radio, unos en $A$ y otros no). Un punto con $1<\|P\|<2$ es interior: el disco de radio $\delta=\min(\|P\|-1,\,2-\|P\|)$ queda dentro de $A$ (desigualdad triangular, como en 4.5). *Ejemplo:* $P=(1{,}5;\,0)$, $\delta=\min(0{,}5;\,0{,}5)=0{,}5$.
3. **Abierto: no.** $(2,0)\in A$ ($4\le4$) pero es punto frontera, no interior.
4. **Cerrado: no.** $(1,0)$ es frontera y **no** está en $A$ (no cumple $1<1$); $A$ no contiene a su frontera.
5. **Acotado: sí,** $A$ está dentro del disco de centro $(0,0)$ y radio 3 (U p. 146).

**Receta.** Cada desigualdad aporta un trozo de frontera; «$<$» deja ese trozo fuera, «$\le$» lo mete. Si hay de las dos clases, el conjunto no es ni abierto ni cerrado.

**Error típico.** Concluir «no es abierto, luego es cerrado».

Fuente: propia (sobre U pp. 145-146).

---

### Propio 3 — Reconocer una bola en $\mathbb{R}^3$ completando cuadrados (medio-difícil)

> $B=\{(x,y,z)\in\mathbb{R}^3: x^2+y^2+z^2-2z<3\}$. Demuestra que es una bola abierta (centro y radio) y clasifica los puntos $(0,0,0)$, $(1,1,1)$, $(0,0,3)$, $(2,0,1)$ y $(0,0,5)$ en interiores a $B$, frontera de $B$ o exteriores.

**Idea en una frase.** Completar el cuadrado en $z$ para que aparezca «distancia al centro».

1. $z^2-2z=(z-1)^2-1$, luego la condición es $x^2+y^2+(z-1)^2-1<3$, es decir $x^2+y^2+(z-1)^2<4$, o sea $d\big((x,y,z),(0,0,1)\big)<2$: **bola abierta** de centro $(0,0,1)$ y radio $2$ (U p. 146, bolas en $\mathbb{R}^3$). Es un conjunto **abierto** (como U Ej. 4.3 en $\mathbb{R}^2$) y acotado.
2. Frontera: la esfera $x^2+y^2+(z-1)^2=4$.
3. Evaluando $g=x^2+y^2+z^2-2z$ (interior si $g<3$, frontera si $g=3$, exterior si $g>3$):
   - $(0,0,0)$: $g=0<3$, interior (dista 1 del centro).
   - $(1,1,1)$: $g=1+1+1-2=1<3$, interior.
   - $(0,0,3)$: $g=9-6=3$, **frontera** (y no pertenece a $B$).
   - $(2,0,1)$: $g=4+1-2=3$, frontera.
   - $(0,0,5)$: $g=25-10=15>3$, exterior.

**Receta.** Completar cuadrados: $z^2-2kz=(z-k)^2-k^2$. Luego leer centro y radio de $\|\bar x-\bar c\|<r$.

**Error típico.** Olvidar el $-1$ al completar el cuadrado y obtener radio $\sqrt3$.

Fuente: propia (sobre U pp. 145-147). sympy: $x^2+y^2+(z-1)^2-4\equiv x^2+y^2+z^2-2z-3$; valores de $g$: $0,1,3,3,15$.

---

### Propio 4 — Conversiones con el cuadrante «trampa» (difícil)

> a) Pasa a polares $(-1,-\sqrt3)$ y $(0,-3)$. b) Pasa $(-\sqrt3,-1,2)$ a cilíndricas y esféricas y comprueba el resultado volviendo a cartesianas. c) Escribe en cilíndricas el cilindro $x^2+y^2=9$ y en esféricas la esfera $x^2+y^2+z^2=4$.

**Idea en una frase.** La calculadora no sabe en qué cuadrante estás: hay que decírselo con los signos de $x$ e $y$.

**a)**
1. $(-1,-\sqrt3)$: $\rho=\sqrt{1+3}=2$; $\operatorname{tg}\theta=\sqrt3$. La calculadora da $\pi/3$, pero $x<0$, $y<0$ es el **tercer** cuadrante: $\theta=\pi+\pi/3=4\pi/3$. Comprobación: $2\cos\frac{4\pi}3=-1$, $2\operatorname{sen}\frac{4\pi}3=-\sqrt3$ ✓. Polares $(2,4\pi/3)$.
2. $(0,-3)$: $x=0$, no se puede dividir; regla de U p. 148: como $y<0$, $\theta=3\pi/2$; $\rho=3$. Polares $(3,3\pi/2)$.

**b)**
3. **Cilíndricas:** $\rho=\sqrt{3+1}=2$; $\operatorname{tg}\theta=\frac{-1}{-\sqrt3}=\frac1{\sqrt3}$, $\theta_0=\pi/6$; tercer cuadrante: $\theta=\pi+\pi/6=7\pi/6$; $z=2$. Cilíndricas $(2,7\pi/6,2)$.
4. **Esféricas:** $\rho=\sqrt{3+1+4}=\sqrt8=2\sqrt2$; $\theta=7\pi/6$; $\operatorname{sen}\phi=\frac{2}{2\sqrt2}=\frac{\sqrt2}2$ con $\phi\in[-\pi/2,\pi/2]$, así que $\phi=\pi/4$. Esféricas $(2\sqrt2,7\pi/6,\pi/4)$.
5. **Vuelta:** $x=2\sqrt2\cos\frac\pi4\cos\frac{7\pi}6=2\sqrt2\cdot\frac{\sqrt2}2\cdot(-\frac{\sqrt3}2)=-\sqrt3$ ✓; $y=2\operatorname{sen}\frac{7\pi}6=2\cdot(-\frac12)=-1$ ✓; $z=2\sqrt2\cdot\frac{\sqrt2}2=2$ ✓.

**c)**
6. $x^2+y^2=\rho^2\cos^2\theta+\rho^2\operatorname{sen}^2\theta=\rho^2$; el cilindro es $\rho=3$ (con $\theta$ y $z$ libres). Por eso U dice que las cilíndricas son «muy convenientes para representar cilindros» (p. 149).
7. $x^2+y^2+z^2=\rho^2\cos^2\phi(\cos^2\theta+\operatorname{sen}^2\theta)+\rho^2\operatorname{sen}^2\phi=\rho^2$; la esfera es $\rho=2$.

**Receta.** $\theta$: tangente, ángulo de referencia $\theta_0$, ajustar por cuadrante y comprobar sustituyendo. Superficies: sustituir $x,y,z$ y simplificar con $\cos^2+\operatorname{sen}^2=1$.

**Error típico.** Dar $\theta=\pi/3$ para $(-1,-\sqrt3)$: ese ángulo corresponde al punto $(1,\sqrt3)$, el opuesto.

Fuente: propia (sobre U §4.1.3 pp. 148-151). sympy: atan2 da $4\pi/3$ y $3\pi/2$ (módulo $2\pi$); $(2,7\pi/6)$, $\rho=2\sqrt2$, $\phi=\pi/4$; vuelta $(-\sqrt3,-1,2)$.

---

## 4. Resumen de erratas y avisos

| Dónde | Qué dice | Correcto |
|---|---|---|
| **E 4.5, p. 139** | «$P'\in C$ y $P''\notin C$… un círculo centrado en $P'$ con intersección vacía con $C$… otro centrado en $P''$ incluido en $C$» | Pertenencias intercambiadas: **$P'\notin C$, $P''\in C$** (así lo dibuja la figura). |
| E 4.2, p. 136 | «siempre es paralelo al vector $\bar w$» | Impreciso: «nulo o paralelo» (el propio texto lo matiza después; la respuesta a) es correcta). |
| **X p. 13** (Feb 2011) | Solución: «Vea la página 194 del libro» | En U (ed. 2023) las polares están en **§4.1.3, pp. 148-149**; la p. 194 es §5.2. Se da la respuesta completa. |
| **X p. 89** (Feb 2018) | $\alpha=1.209$ rad | $\alpha=\arccos(1/\sqrt{15})\approx$ **1,3096 rad** ($75{,}04^\circ$). |
| X p. 139 (Sept 2018) | Sin solución | $-5$, $\sqrt6$, $\sqrt{14}$. |
| U pp. 149-150 | Cilíndricas/esféricas «en $\mathbb{R}^3\setminus\{(0,0,0)\}$» | En todo el eje $z$ el ángulo $\theta$ no está determinado (omisión; no afecta a los ejercicios). |
| U p. 143 | «sus propiedades… conocidas del Álgebra» | No enuncia la desigualdad triangular, $\|\lambda\bar u\|=|\lambda|\|\bar u\|$ ni Cauchy-Schwarz; la triangular está en el margen de E p. 137. |

E 4.1, 4.3, 4.4, 4.6, 4.7 y 4.8: resultados correctos (sympy). X pp. 1, 22-23, 53, 70: correctos.
