# Soluciones Tema 4.2 — Funciones de varias variables (dominio, imagen, gráfica, curvas de nivel, límites y continuidad)

Resolución paso a paso de los ejercicios de **E** de la sección 4.2 (Ejercicios 4.9-4.24, E pp. 142-153), de las preguntas de examen **X** sobre funciones de varias variables (dominio, curvas de nivel, límites, continuidad) y de 4 ejemplos propios. Todos los cálculos se han comprobado con sympy (salidas resumidas al final de cada bloque). Se han leído como imagen (PyMuPDF) E pp. 144-153 (la figura de 4.16 ampliada a 300 ppp) y X pp. 4, 16, 33, 39, 45, 65, 98, 122-125, 130-131, 137-138, 140, 143, 148.

Páginas: U impresa (= PDF + 2); E impresa = PDF; X = página PDF de `Examenes-resueltos-Calculo.pdf`.

## 0. Herramientas de teoría que se usan

| Clave | Enunciado (resumido) | Dónde |
|---|---|---|
| **Def. 4.3** | Función de dos variables $f:D\subset\mathbb{R}^2\to\mathbb{R}$: a cada $(x,y)\in D$ le asigna **un único** número $f(x,y)$. $D$ = dominio; $f(D)$ = imagen. **Convenio:** si no se dice el dominio, es el mayor conjunto donde la expresión tiene sentido. | U §4.2.2, p. 153 |
| Cómo se busca el dominio | Lo mismo que en una variable: raíz par $\Rightarrow$ argumento $\ge0$; logaritmo $\Rightarrow$ argumento $>0$; denominador $\neq0$; arcoseno/arcocoseno $\Rightarrow$ argumento en $[-1,1]$. | U p. 153 (margen) |
| Gráfica | $\{(x,y,z)\in\mathbb{R}^3:(x,y)\in D,\ z=f(x,y)\}$. Su proyección sobre el plano $xy$ es el dominio; sobre el eje $z$, la imagen. | U p. 155 |
| Curvas de nivel | Curva de nivel $k$: $\{(x,y)\in D: f(x,y)=k\}$ (= proyección sobre el plano $xy$ del corte de la gráfica con el plano $z=k$, la «traza»). En tres variables: superficies de nivel. | U p. 155; Ej. 4.11 pp. 155-156 |
| **Def. 4.4** | $\lim_{(x,y)\to(a,b)}f(x,y)=l$ si para todo $\varepsilon>0$ existe $\delta>0$ tal que $0<d((a,b),(x,y))<\delta$ y $(x,y)\in D$ $\Rightarrow$ $|f(x,y)-l|<\varepsilon$. Idea: **por cualquier camino** hacia $(a,b)$, $f$ se acerca a $l$. | U §4.2.3, p. 159 |
| Álgebra de límites | Límite de $cf$, $f+g$, $fg$, $f/g$ (si el límite de $g$ es $m\neq0$). | U p. 160 |
| **Condiciones necesarias** | Si existe el límite $l$: (i) los **límites reiterados** $\lim_{y\to b}\lim_{x\to a}f$ y $\lim_{x\to a}\lim_{y\to b}f$ coinciden (con $l$, si existen); (ii) los límites por **rectas** $y=mx+k$ (y $x=m'y+k'$) por $(a,b)$ valen $l$; (iii) los límites por **curvas** $y=g(x)$ con $g(a)=b$ (o $x=h(y)$) valen $l$. **Si coinciden, NO se puede afirmar que el límite exista.** | U pp. 161-162 |
| **Regla del emparedado** | Si $g\le f\le h$ en un disco centrado en $(a,b)$ y $\lim_{(x,y)\to(a,b)}g=\lim_{(x,y)\to(a,b)}h=l$, entonces $\lim_{(x,y)\to(a,b)}f=l$. | U p. 163 |
| **Propiedad** «infinitésimo $\times$ acotada» | Si $\lim_{(x,y)\to(a,b)}f=0$ y $g$ está acotada cerca de $(a,b)$, entonces $\lim_{(x,y)\to(a,b)}fg=0$. | U p. 165 |
| **Polares** | $x=a+\rho\cos\theta$, $y=b+\rho\operatorname{sen}\theta$, $F(\rho,\theta)=f(a+\rho\cos\theta,b+\rho\operatorname{sen}\theta)$. (1) Si $\lim_{\rho\to0}F$ **depende de $\theta$**, no existe el límite. (2) Si $|F(\rho,\theta)-l|\le h(\rho)$ con $h(\rho)\to0$ (**$h$ sin $\theta$**), el límite es $l$. (3) En otro caso, no se concluye nada. | U p. 165 |
| **Def. 4.5-4.7** | $f$ continua en $(a,b)\in D$ si $\lim_{(x,y)\to(a,b)}f(x,y)=f(a,b)$; discontinua si no; continua en $A$ si lo es en cada punto de $A$. | U p. 166 |
| Propiedades de continuidad | Suma, producto, cociente (donde el denominador $\neq0$) y composición de continuas son continuas. Polinomios en $x,y$ continuos en $\mathbb{R}^2$; racionales donde no se anula el denominador; exponenciales, raíces, logaritmos y trigonométricas, donde estén definidas. | U pp. 166-167 |

**Dos hechos de una variable que se usan sin cesar** (de temas anteriores): $|\operatorname{sen}u|\le1$, $|\cos u|\le1$; y $\operatorname{arctg}$ es continua y estrictamente creciente.

---

### Receta general: cómo estudiar $\lim_{(x,y)\to(a,b)}f(x,y)$

> **Paso 1 — Sustituir.** Si $f$ es continua en $(a,b)$ (polinomio, cociente con denominador $\neq0$ en $(a,b)$, composición de elementales definidas allí), el límite es $f(a,b)$ y se acabó (U pp. 166-167).
>
> **Paso 2 — Si sale $\tfrac00$ (u otra indeterminación): intentar REFUTAR** (demostrar que **no existe**) con caminos, de más fácil a más listo:
> (a) los dos **ejes** o los **reiterados**; (b) el haz de **rectas** $y-b=m(x-a)$; (c) **curvas** $y-b=m(x-a)^k$ o $x-a=m(y-b)^k$ elegidas para que **numerador y denominador tengan el mismo grado** (por ejemplo, si aparece $x^2+y^4$, probar $x=y^2$). Si **dos caminos dan valores distintos** (o un camino da un valor que depende de $m$) $\Rightarrow$ **no existe** (U pp. 161-163).
>
> **Paso 3 — Si todos los caminos probados dan el mismo valor $l$: intentar PROBAR** que el límite es $l$. Se acota $|f(x,y)-l|$ por algo que tiende a $0$:
> (a) **polares** centradas en $(a,b)$: buscar $|F(\rho,\theta)-l|\le h(\rho)\to0$ **sin $\theta$** (usar $|\cos\theta|,|\operatorname{sen}\theta|\le1$);
> (b) **emparedado** con desigualdades como $x^2\le x^2+y^2$, $\dfrac{x^2}{x^2+y^2}\le1$, $|y|\le\sqrt{x^2+y^2}$;
> (c) **infinitésimo $\times$ acotada** (U pp. 163-165).
>
> **Continuidad en un punto «especial»** (donde la fórmula cambia): continua $\iff$ el límite existe **y** vale $f(a,b)$. Basta un camino cuyo límite sea distinto de $f(a,b)$ para concluir **discontinua**.

**Por qué los caminos solo sirven para refutar.** Hay infinitos caminos hacia $(a,b)$; comprobar unos cuantos (aunque sean infinitas rectas) no los cubre todos. Ejemplo de U (Ej. 4.16, pp. 162-163): $\dfrac{x^3y}{x^6+y^2}$ da $0$ por todas las rectas y $\tfrac12$ por $y=x^3$.

---

## 1. Ejercicios de E (orden de dificultad creciente; numeración conservada)

Orden propuesto para aprender: **4.11 → 4.12 → 4.9 → 4.10** (qué es una función de dos variables) **→ 4.15 → 4.13 → 4.14** (dominio e imagen) **→ 4.18 → 4.17 → 4.16** (curvas de nivel) **→ 4.20 → 4.19 → 4.24 → 4.21 → 4.22 → 4.23** (límites y continuidad).

---

### Ejercicio 4.11 (E p. 144)

> Indica la opción correcta sobre la gráfica de $f:D\subset\mathbb{R}^2\to\mathbb{R}$: a) Es un conjunto de $\mathbb{R}$. b) Es un conjunto de $\mathbb{R}^2$. c) Es un conjunto de $\mathbb{R}^3$. d) Ninguna de las anteriores.

**Idea en una frase.** Cada punto de la gráfica lleva las **dos** coordenadas de entrada y **una** de salida: tres números.

1. **Definición** (U p. 155): gráfica $=\{(x,y,z): (x,y)\in D,\ z=f(x,y)\}$.
2. **Contar coordenadas:** cada elemento es una terna $(x,y,z)$, es decir, un punto de $\mathbb{R}^3$.
3. **Respuesta: c).** (Igual que en una variable la gráfica de $y=f(x)$ es un conjunto de pares $(x,f(x))$, de $\mathbb{R}^2$.)

**Receta.** Gráfica de $f:\mathbb{R}^n\to\mathbb{R}$ $\subset\mathbb{R}^{n+1}$ (entradas + salida).

**Error típico.** Confundir gráfica con dominio ($\subset\mathbb{R}^2$) o con imagen ($\subset\mathbb{R}$).

---

### Ejercicio 4.12 (E p. 144)

> ¿Puede tener la gráfica de una función $f:D\subset\mathbb{R}^2\to\mathbb{R}$ forma de balón?

**Idea en una frase.** Encima de cada punto del dominio la gráfica tiene **un solo** punto; un balón tiene dos (arriba y abajo).

1. **Qué exige la Def. 4.3** (U p. 153): a cada $(x,y)\in D$ le corresponde **un único** $f(x,y)$.
2. **Una esfera** $x^2+y^2+z^2=1$: sobre $(0,0)$ están los puntos $(0,0,1)$ y $(0,0,-1)$, que pedirían $f(0,0)=1$ y $f(0,0)=-1$ a la vez. Imposible.
3. **Respuesta: no.** «Prueba de la recta vertical» en $\mathbb{R}^3$: toda recta vertical corta a la gráfica como mucho una vez. Es lo mismo que en una variable impide que una circunferencia sea la gráfica de $y=f(x)$.
4. *Comentario:* la mitad superior sí puede serlo: $z=\sqrt{1-x^2-y^2}$ en el disco $x^2+y^2\le1$ (y la inferior con el signo $-$).

**Receta.** Para saber si una superficie es una gráfica $z=f(x,y)$: ¿alguna recta vertical la corta dos veces? Si sí, no lo es.

**Error típico.** Pensar que «función» es cualquier ecuación en $x,y,z$.

---

### Ejercicio 4.9 (E p. 142)

> La ley de los gases ideales describe la relación entre la presión $P$, la temperatura $T$ y el volumen $V$ de un gas ideal como $PV=nRT$, donde $n$ es el número de moles de gas y $R=0.082\ \text{atm·l/K·mol}$ es la constante universal de los gases ideales. Podemos escribir la presión del gas (en atmósferas) como función de las variables $T$ (en grados Kelvin) y $V$ (en litros), para $V>0$, como $P(T,V)=\dfrac{nRT}{V}$. ¿Cuál es el valor de $P(273,2)$ si $n=0.1$ y qué significa?

**Idea en una frase.** Evaluar una función de dos variables es sustituir **cada** variable por su valor.

1. **Sustituir** $n=0.1$, $R=0.082$, $T=273$, $V=2$: $P(273,2)=\dfrac{0.1\cdot0.082\cdot273}{2}=\dfrac{2.2386}{2}=1.1193$ atm.
2. **Significado:** es la presión que ejercen $0.1$ moles de gas ideal encerrados en $2$ litros a $273$ K ($\approx0\,^\circ$C).

**Receta.** $f(a,b)$: sustituir $x=a$, $y=b$ (en el orden de las variables) y operar.

**Error típico.** Cambiar el orden: $P(273,2)$ es $T=273$, $V=2$, no al revés.

sympy: $1.1193$.

---

### Ejercicio 4.10 (E pp. 142-143)

> Con los datos del ejercicio anterior se pide: 1. Reformular y contestar la siguiente pregunta: «¿para qué valor de $T$ se cumple $P(T,2)=1$?» 2. ¿Qué significado tiene la función $P(T,2)$? Describe cómo se comporta esta función. 3. ¿Qué significado tiene la función $P(273,V)$? Describe cómo se comporta esta función. 4. Representar la curva de nivel $P(T,V)=1$. ¿Qué verifican los elementos de esta curva?

**Idea en una frase.** Fijar una variable convierte la función de dos variables en una función de **una** variable (un «corte» de la gráfica); fijar el **valor** de $P$ da una curva de nivel.

1. **Apartado 1.** Pregunta reformulada: «¿a qué temperatura $0.1$ moles ocupan $2$ litros a $1$ atm?». Se resuelve la ecuación de una incógnita
$\dfrac{0.1\cdot0.082\cdot T}{2}=1\iff T=\dfrac{2}{0.0082}\approx243.9\ \text{K}.$
2. **Apartado 2.** Con $V=2$ fijo: $P(T,2)=\dfrac{0.0082}{2}T=0.0041\,T$. Es una **recta por el origen** (función lineal, creciente): a volumen fijo, la presión es **proporcional** a la temperatura.
3. **Apartado 3.** Con $T=273$ fijo: $P(273,V)=\dfrac{2.2386}{V}$, $V>0$. Es una **hipérbola**: decreciente, $\lim_{V\to+\infty}P(273,V)=0$ (mucho volumen, poca presión) y $\lim_{V\to0^+}P(273,V)=+\infty$.
4. **Apartado 4.** Curva de nivel $1$ (U p. 155): puntos $(T,V)$ con $P(T,V)=1$, es decir $\dfrac{0.0082\,T}{V}=1\iff V=0.0082\,T$ (con $T,V>0$). Es una **semirrecta** (sin el origen, porque $V>0$). Sus puntos son los pares (temperatura, volumen) en los que $0.1$ moles ejercen exactamente $1$ atm. Comprobación: $(243.9,\,2)$ está en ella ($0.0082\cdot243.9\approx2$), coherente con el apartado 1.

E: correcto.

**Receta.** Fijar **una variable** $\to$ función de una variable (corte). Fijar el **valor de $f$** $\to$ curva de nivel $f=k$ en el plano de las variables.

**Error típico.** Confundir «$P(T,2)$» (función de $T$) con «$P=2$» (curva de nivel).

sympy: $T=243.90$; pendiente $0.0041$; $0.1\cdot0.082\cdot273=2.2386$; curva $V=0.0082\,T$.

---

### Ejercicio 4.15 (E pp. 146-147)

> Determina el dominio y la imagen de la función dada por $f(x,y,z)=\cos(xz+\ln y)$.

**Idea en una frase.** El coseno acepta cualquier número; solo el logaritmo pone condiciones. Y el coseno de «algo que recorre todos los reales» recorre $[-1,1]$.

1. **Dominio** (convenio de U p. 153): $\cos$ y $xz$ están definidos siempre; $\ln y$ exige $y>0$. Así $D=\{(x,y,z)\in\mathbb{R}^3: y>0\}$ (un semiespacio).
2. **Imagen, cota:** $-1\le\cos u\le1$ para todo $u$, luego $f(D)\subset[-1,1]$.
3. **Imagen, se alcanza todo:** tomando puntos $(x,1,1)\in D$ queda $f(x,1,1)=\cos(x+0)=\cos x$, que, con $x\in[0,\pi]$, toma todos los valores entre $\cos0=1$ y $\cos\pi=-1$ (es continua: teorema de los valores intermedios). Así $[-1,1]\subset f(D)$.
4. **Resultado:** $D=\{y>0\}$, imagen $[-1,1]$.

E: correcto (usa los mismos puntos $(x,1,1)$).

**Receta (imagen).** Dos mitades: (i) **cota** ($f(D)\subset I$) y (ii) **se alcanza** (encontrar una «recta» de puntos del dominio en la que $f$ se reduce a una función de una variable que recorre $I$).

**Error típico.** Dar solo la mitad (i): saber que $|\cos|\le1$ no prueba que se alcancen todos los valores.

---

### Ejercicio 4.13 (E pp. 144-145)

> Sea $f$ la función dada por $f(x,y)=\sqrt{x^2-y^3}$. ¿Cuál es su dominio? Pedimos dar su expresión analítica y representarlo gráficamente.

**Idea en una frase.** Raíz cuadrada $\Rightarrow$ argumento **mayor o igual** que $0$; luego se despeja $y$ con la raíz cúbica, que conserva el orden.

1. **Condición** (U p. 153): $x^2-y^3\ge0\iff y^3\le x^2$.
2. **Despejar $y$.** La raíz cúbica $u\mapsto\sqrt[3]{u}$ está definida para todo $u$ (también negativos) y es **estrictamente creciente**, así que conserva las desigualdades: $y^3\le x^2\iff y\le\sqrt[3]{x^2}=x^{2/3}$.
3. **Dominio:** $D=\{(x,y)\in\mathbb{R}^2: y\le x^{2/3}\}$: los puntos **sobre o por debajo** de la curva $y=x^{2/3}$ (curva con un «pico» en el origen, simétrica respecto al eje $y$, con $y\ge0$). Por ejemplo, todo el semiplano $y\le0$ está en $D$.
4. **Comprobación con puntos:** $(1,1)$: $1-1=0\ge0$, está en $D$ (sobre la curva) y $f(1,1)=0$. $(8,4)$: $64-64=0$, también. $(0,1)$: $0-1<0$, no está.

**Errata de E (verificada en la imagen de pp. 144-145).** E escribe la condición como $x^2>y^3$ y el dominio con $y^3<x^2$, $y<x^{2/3}$ (desigualdades **estrictas**). Es incorrecto: $\sqrt0=0$ existe, y los puntos de la curva $y=x^{2/3}$ (como $(1,1)$) pertenecen al dominio. Lo correcto es $\ge$ / $\le$. (E dice justo antes «su argumento debe ser positivo o 0», que es lo correcto, y luego escribe $>$.)

**Receta.** Raíz par: $\ge0$. Despejar usando funciones crecientes (conservan el sentido de $\le$). Dibujar la curva frontera, decidir de qué lado está la región probando un punto, y si el borde entra ($\le$) o no ($<$).

**Error típico.** Poner $>0$ en una raíz (es el logaritmo el que pide $>0$).

sympy: $f(1,1)=0$; $8^2-4^3=0$.

---

### Ejercicio 4.14 (E pp. 145-146)

> Sea $f$ la función dada por $f(x,y)=\sqrt{\ln(xy)}$. ¿Cuál es su dominio?

**Idea en una frase.** Dos condiciones encadenadas: el logaritmo pide $xy>0$ y la raíz pide $\ln(xy)\ge0$, es decir $xy\ge1$; luego se dibuja $xy\ge1$ separando signos.

1. **Logaritmo:** $xy>0$ $\iff$ $x,y$ del mismo signo y ninguno nulo (cuadrantes I y III **sin** los ejes).
2. **Raíz:** $\ln(xy)\ge0\iff xy\ge e^0=1$ (porque $\ln$ es creciente y $\ln1=0$). Esta condición ya implica la anterior ($xy\ge1>0$), así que basta con $xy\ge1$.
3. **Caso $x>0$ (entonces $y>0$):** dividir por $x>0$ **no** cambia el sentido: $y\ge\dfrac1x$. Región por encima de la rama de hipérbola del primer cuadrante, incluida la curva.
4. **Caso $x<0$ (entonces $y<0$):** dividir por $x<0$ **cambia** el sentido: $y\le\dfrac1x$. Región por debajo de la rama del tercer cuadrante, incluida la curva.
5. **Dominio:** $D=\{(x,y): x>0,\ y\ge\tfrac1x\}\cup\{(x,y): x<0,\ y\le\tfrac1x\}=\{(x,y): xy\ge1\}$.
6. **Comprobación:** $(2,1)$: $xy=2\ge1$ ✓. $(-1,-3)$: $3\ge1$ ✓. $(1,\tfrac12)$: $\tfrac12<1$ ✗ ($\ln\tfrac12<0$).

**Errata menor de E.** La primera condición se escribe «$xy\ge0\iff x,y\ge0$ o $x,y\le0$», que incluye los ejes, donde $\ln(xy)=\ln0$ no existe (E mismo dice antes que «el argumento del logaritmo debe ser positivo»). Debe ser $xy>0$ (sin ejes). No afecta al resultado final, porque la segunda condición $xy\ge1$ ya los excluye; el dominio y la figura finales de E son correctos.

**Receta.** Funciones anidadas: condición de la de **fuera** aplicada a la de dentro ($\ln(\dots)\ge0$) **y** condición de la de dentro ($\dots>0$). Al dividir una desigualdad por una variable, separar casos según su signo.

**Error típico.** Dividir $xy\ge1$ entre $x$ sin mirar el signo y dar $y\ge1/x$ también en el tercer cuadrante (eso daría puntos como $(-1,0)$, que no están en el dominio).

---

### Ejercicio 4.18 (E p. 149)

> Determina las curvas de nivel de la función $f$ dada por $f(x,y)=x^2-y$. ¿Qué tipo de curvas son?

**Idea en una frase.** Igualar $f$ a una constante y despejar: aquí se despeja $y$ y sale una parábola para cada valor.

1. **Curva de nivel $C$** (U p. 155): $x^2-y=C$, $C\in\mathbb{R}$.
2. **Despejar:** $y=x^2-C$. Para cada $C$ es la parábola $y=x^2$ **trasladada verticalmente** $-C$ unidades (vértice $(0,-C)$).
3. **Todas son parábolas** (no hay casos especiales: para todo $C$ la ecuación tiene solución). Imagen de $f$: $\mathbb{R}$ (p. ej. $f(0,y)=-y$ toma cualquier valor).

E: correcto.

**Receta.** Curvas de nivel: $f(x,y)=C$, despejar y reconocer la curva; revisar si para algún $C$ la curva es vacía, un punto o se degenera.

**Error típico.** Dibujar la gráfica de $f$ (una superficie) en lugar de curvas en el plano $xy$.

---

### Ejercicio 4.17 (E p. 148)

> Sea $f$ la función dada por $f(x,y)=x^2-\dfrac{y^2}{3}+8$. Se pide determinar las curvas de nivel. ¿Qué tipo de curvas son?

**Idea en una frase.** $f=C$ da $x^2-\frac{y^2}{3}=C-8$; según el signo de $C-8$ salen hipérbolas «horizontales», «verticales» o, si $C=8$, **dos rectas**.

1. **Ecuación:** $x^2-\dfrac{y^2}{3}+8=C\iff x^2-\dfrac{y^2}{3}=C'$, con $C'=C-8$.
2. **$C'>0$ ($C>8$):** dividiendo por $C'$, $\dfrac{x^2}{C'}-\dfrac{y^2}{3C'}=1$: **hipérbola** que corta al eje $x$ en $(\pm\sqrt{C'},0)$ y no corta al eje $y$ (se abre a izquierda y derecha).
3. **$C'<0$ ($C<8$):** $\dfrac{y^2}{3|C'|}-\dfrac{x^2}{|C'|}=1$: **hipérbola** que corta al eje $y$ en $(0,\pm\sqrt{3|C'|})$ (se abre arriba y abajo). Es la de trazo discontinuo de E ($C'=-1.5$).
4. **$C'=0$ ($C=8$):** $x^2=\dfrac{y^2}{3}\iff y=\pm\sqrt3\,x$: **dos rectas** que se cortan en el origen (las asíntotas comunes de todas las hipérbolas). En ese nivel está el punto $(0,0)$, donde $f(0,0)=8$.
5. **Resultado:** hipérbolas para $C\neq8$; par de rectas $y=\pm\sqrt3x$ para $C=8$. (La gráfica es una «silla de montar».)

**Omisión de E.** Dice que «estas curvas son hipérbolas» y dibuja $C'=0.25,\ 1.5,\ -1.5$, pero no trata el caso $C'=0$, en el que la curva de nivel **no** es una hipérbola sino las dos rectas $y=\pm\sqrt3x$; tampoco explica que, según el signo de $C'$, la hipérbola corta a un eje o al otro.

**Receta.** Pasar la constante al otro lado y estudiar su **signo**: $>0$, $<0$ y $=0$ dan tipos de curva distintos; el caso $=0$ suele ser degenerado (punto, rectas o vacío).

**Error típico.** Olvidar el caso $C'=0$, o dividir por $C'$ sin haber excluido $C'=0$.

sympy: `solve(x**2-y**2/3, y)` $\to y=\pm\sqrt3x$.

---

### Ejercicio 4.16 (E pp. 147-148)

> En la siguiente figura se representan 6 curvas de nivel de una función $f$, que son los conjuntos $\{(x,y): f(x,y)=k,\ k=1,\dots,6\}$ que podemos distinguir por las etiquetas que se han puesto en ellas. [Figura: elipses concéntricas centradas en el origen; la etiqueta 1 en la más interior y la 6 en la más exterior.] A partir de ella, estima si la función crece, decrece o se mantiene prácticamente sin cambios en los siguientes puntos (señalados en la figura) y direcciones: 1. Punto $(0,2)$ y dirección $\mathbf{j}=(0,1)$, 2. Punto $(4,0)$ y dirección $\mathbf{j}=(0,1)$, 3. Punto $(4,-1)$, dirección $-\mathbf{i}$, donde $\mathbf{i}=(1,0)$, 4. Punto $(4,-1)$, dirección $\mathbf{i}-2\mathbf{j}$.

**Idea en una frase.** Como en un mapa topográfico: los niveles **aumentan hacia fuera** (1 dentro, 6 fuera), así que alejarse del centro es «subir» y acercarse es «bajar»; moverse a lo largo de una curva es no cambiar de altura.

1. **Leer la figura** (ampliada en la imagen de E p. 147): las curvas son elipses con centro $(0,0)$; la etiqueta $1$ está en la elipse interior y la $6$ en la exterior. Por tanto **$f$ crece al alejarse del origen** (cruzando elipses hacia fuera).
2. **Punto $(0,2)$, dirección $(0,1)$:** desde el punto más alto de su elipse (nivel 4 según E) se sube verticalmente, es decir, **hacia fuera** y perpendicular a la curva: **crece**.
3. **Punto $(4,0)$, dirección $(0,1)$:** $(4,0)$ está en el extremo derecho de una elipse, donde la tangente es **vertical**. Moverse en dirección $(0,1)$ es moverse **tangente** a la curva de nivel: **prácticamente sin cambios** (la variación «de primer orden» es nula; de hecho, sobre la recta $x=4$ la función tiene un mínimo en $y=0$, porque al subir o bajar se sale ligeramente hacia elipses exteriores).
4. **Punto $(4,-1)$, dirección $-\mathbf{i}=(-1,0)$:** hacia la izquierda, es decir, **hacia el centro**, cruzando a niveles menores: **decrece**.
5. **Punto $(4,-1)$, dirección $\mathbf{i}-2\mathbf{j}=(1,-2)$:** hacia la derecha y hacia abajo, **alejándose** del centro: **crece**.

E da las mismas respuestas (crece, se mantiene, decrece, crece). **Imprecisión de E** en el apartado 2: dice que es «un punto donde pasa de crecer a decrecer o al revés»; sobre la recta vertical $x=4$ lo que ocurre es que pasa de **decrecer a crecer** (mínimo en $y=0$). Su comentario de que en dirección $\mathbf{j}+k\mathbf{i}$ ($k>0$) crece y en $\mathbf{j}-k\mathbf{i}$ decrece es correcto (la primera apunta hacia fuera, la segunda hacia dentro). Este ejercicio anticipa el **gradiente** (§4.3): la dirección perpendicular a la curva de nivel es la de máxima variación.

**Receta.** Ver hacia dónde aumentan las etiquetas. Dirección que cruza hacia niveles mayores: crece; hacia menores: decrece; tangente a la curva: (casi) constante.

**Error típico.** Leer la figura como si fuera la gráfica (confundir «estar más arriba en el dibujo» con «valor mayor de $f$»).

---

### Ejercicio 4.20 (E p. 150)

> Razona si es cierto que cualquier función $f:D\subset\mathbb{R}^2\to\mathbb{R}$ tiene límite en $(x_0,y_0)\in\mathbb{R}^2$ si los límites reiterados existen y coinciden, es decir, si: $\lim_{y\to y_0}\big(\lim_{x\to x_0}f(x,y)\big)=\lim_{x\to x_0}\big(\lim_{y\to y_0}f(x,y)\big)$.

**Idea en una frase.** Los reiterados son, en el fondo, acercarse «por los ejes»; otros caminos pueden dar otro valor.

1. **Qué dice la teoría** (U p. 161): si el límite existe, los reiterados (si existen) coinciden con él. Es una condición **necesaria**, no **suficiente**.
2. **Contraejemplo** (no lo da E): $f(x,y)=\dfrac{xy}{x^2+y^2}$ en $(0,0)$.
   - Reiterado 1: con $y\neq0$ fijo, $\lim_{x\to0}\frac{xy}{x^2+y^2}=\frac0{y^2}=0$; luego $\lim_{y\to0}0=0$.
   - Reiterado 2: por simetría, también $0$.
   - Camino $y=x$: $f(x,x)=\dfrac{x^2}{2x^2}=\dfrac12\to\dfrac12\neq0$.
   Dos caminos con límites distintos $\Rightarrow$ no existe el límite, aunque los reiterados coinciden.
3. **Respuesta: falso.**

**Omisión de E.** Responde «No es cierto» con la frase de la teoría, sin contraejemplo. En un V/F de examen conviene dar uno (como el anterior, o el Ej. 4.16 de U, p. 162).

**Receta.** En un «verdadero/falso» que dice «si pasa A, entonces existe el límite», buscar un contraejemplo concreto: $xy/(x^2+y^2)$ es el comodín.

**Error típico.** Creer que, porque los reiterados (o todas las rectas) dan lo mismo, el límite existe.

sympy: reiterados $0,0$; por $y=x$, $1/2$.

---

### Ejercicio 4.19 (E pp. 149-150)

> Estudia si existe el límite siguiente $\displaystyle\lim_{(x,y)\to(0,0)}\frac{x^2+y^3}{x^2+y^2}$.

**Idea en una frase.** Sustituir da $\frac00$; probamos a refutar con los reiterados y salen valores distintos.

1. **Paso 1 (sustituir):** $\frac{0}{0}$, indeterminado. Hay que estudiar caminos.
2. **Reiterado «primero $y$»:** con $x\neq0$ fijo, $\lim_{y\to0}\frac{x^2+y^3}{x^2+y^2}=\frac{x^2}{x^2}=1$ (el denominador no se anula: es una función continua de $y$). Luego $\lim_{x\to0}1=1$.
3. **Reiterado «primero $x$»:** con $y\neq0$ fijo, $\lim_{x\to0}\frac{x^2+y^3}{x^2+y^2}=\frac{y^3}{y^2}=y$. Luego $\lim_{y\to0}y=0$.
4. **Conclusión:** $1\neq0$; por la condición necesaria de U p. 161, **el límite no existe**.
5. *Alternativa con rectas* (útil si los reiterados coincidieran): $y=mx$ da $\dfrac{x^2+m^3x^3}{x^2(1+m^2)}=\dfrac{1+m^3x}{1+m^2}\to\dfrac1{1+m^2}$, que depende de $m$.

E resuelve igual (correcto). Es exactamente la pregunta X p. 4 (Feb 2010).

**Receta.** Reiterados: congelar una variable (≠ valor límite), hacer el límite en la otra, y luego el de la congelada. Si difieren, no hay límite.

**Error típico.** Sustituir a la vez $x=0$, $y=0$ en el paso interior (eso da $\frac00$ otra vez): en el límite interior la otra variable es una constante **no nula**.

sympy: reiterados $1$ y $0$; por rectas $1/(1+m^2)$.

---

### Ejercicio 4.24 (E p. 153)

> Sea $f$ la función dada por $f(x,y)=\dfrac{x^2-y^2}{x^2+y^2}$ si $(x,y)\neq(0,0)$, $f(0,0)=0$. ¿Es una función continua?

**Idea en una frase.** Fuera del origen no hay problema (cociente de polinomios); en el origen, los dos ejes dan $1$ y $-1$.

1. **En $(x,y)\neq(0,0)$:** $f$ es **cociente** de polinomios (continuos) con denominador $x^2+y^2\neq0$: continua (U p. 166).
2. **En $(0,0)$, eje $y$** ($x=0$, $y\neq0$): $f(0,y)=\dfrac{-y^2}{y^2}=-1\to-1$.
3. **Eje $x$** ($y=0$, $x\neq0$): $f(x,0)=\dfrac{x^2}{x^2}=1\to1$.
4. **Conclusión:** dos caminos con límites distintos $\Rightarrow$ no existe $\lim_{(x,y)\to(0,0)}f(x,y)$ $\Rightarrow$ $f$ **no es continua en $(0,0)$** (Def. 4.5). Es continua en $\mathbb{R}^2\setminus\{(0,0)\}$.
5. *En polares:* $F(\rho,\theta)=\cos^2\theta-\operatorname{sen}^2\theta=\cos2\theta$, que depende de $\theta$ (caso 1 de U p. 165).

**Errata de redacción de E.** «Luego **el producto** resulta ser también una función continua» debe decir «**el cociente**».

**Receta.** Continuidad de una función definida «a trozos» en un punto: (i) fuera del punto, propiedades; (ii) en el punto, ¿existe el límite y vale $f(a,b)$?

**Error típico.** Concluir «discontinua» sin decir en qué puntos: la respuesta completa es «continua en $\mathbb{R}^2\setminus\{(0,0)\}$, discontinua en $(0,0)$».

sympy: ejes $-1$ y $1$; polar $\cos2\theta$.

---

### Ejercicio 4.21 (E pp. 150-151)

> Para las funciones dadas por las siguientes expresiones $f(x,y)=y\operatorname{sen}(x^2+1)$, $g(x,y)=\dfrac{\ln(3+x^2y^2)}{3+x^2+y^4}$, $h(x,y)=\sqrt{x^2y}$, se pide determinar su dominio y estudiar cuáles son continuas.

**Idea en una frase.** Las tres están construidas con operaciones y composiciones de funciones elementales, así que son continuas **en todo su dominio**; el trabajo es hallar el dominio.

1. **$f$, dominio:** $y$, $x^2+1$ y $\operatorname{sen}$ están definidos para todo número: $D_f=\mathbb{R}^2$.
2. **$f$, continuidad:** $x^2+1$ es polinomio (continua); $\operatorname{sen}$ es continua; la composición $\operatorname{sen}(x^2+1)$ es continua; el producto por $y$ (polinomio) es continuo. **$f$ continua en $\mathbb{R}^2$.**
3. **$g$, dominio:** el argumento del logaritmo cumple $3+x^2y^2\ge3>0$ siempre; el denominador $3+x^2+y^4\ge3>0$ nunca se anula. $D_g=\mathbb{R}^2$.
4. **$g$, continuidad:** $3+x^2y^2$ es polinomio; $\ln$ continua en $(0,\infty)$; composición continua; cociente de continuas con denominador $\neq0$: **$g$ continua en $\mathbb{R}^2$.**
5. **$h$, dominio:** raíz cuadrada $\Rightarrow x^2y\ge0$. Como $x^2\ge0$: si $x\neq0$, $x^2>0$ y la condición es $y\ge0$; si $x=0$, $x^2y=0\ge0$ **para cualquier $y$**. Así
$D_h=\{(x,y): y\ge0\}\cup\{(0,y): y\in\mathbb{R}\}$
(semiplano superior **más** el eje $y$ entero). Por ejemplo, $(0,-5)\in D_h$ y $h(0,-5)=\sqrt0=0$.
6. **$h$, continuidad:** $x^2y$ polinomio y $\sqrt{\cdot}$ continua en $[0,\infty)$: $h$ es continua en todo $D_h$. (En los puntos $(0,y)$ con $y<0$, los únicos puntos de $D_h$ cercanos están en el eje $y$, donde $h=0$; la Def. 4.4 solo mira puntos **del dominio**, y el límite es $0=h(0,y)$.)

**Errata de E (verificada en la imagen de p. 151).** E da $D=\{(x,y)\in\mathbb{R}^2: y\ge0\}$ para $h$. Le falta la semirrecta $\{x=0,\ y<0\}$, donde $x^2y=0$ y la raíz sí existe.

**Receta.** En dominios con productos dentro de una raíz, **no dividir** por un factor que pueda ser $0$: separar el caso en que ese factor se anula.

**Error típico.** «Simplificar» $x^2y\ge0$ a $y\ge0$ dividiendo por $x^2$ sin considerar $x=0$.

---

### Ejercicio 4.22 (E pp. 151-152)

> Sea $f$ la función dada por $f(x,y)=(x^2+y^2)\operatorname{sen}\dfrac{1}{x^2+y^2}$ si $(x,y)\neq(0,0)$, $f(0,0)=0$. Se pide estudiar su continuidad.

**Idea en una frase.** «Algo que tiende a $0$» ($x^2+y^2$) por «algo acotado» ($\operatorname{sen}$) tiende a $0$, que es justamente $f(0,0)$.

1. **Fuera del origen:** $x^2+y^2$ y $\frac1{x^2+y^2}$ son continuas (cociente con denominador $\neq0$), $\operatorname{sen}$ es continua, y producto y composición conservan la continuidad (U p. 166). **Continua en $\mathbb{R}^2\setminus\{(0,0)\}$.**
2. **En el origen hay que ver si $\lim_{(x,y)\to(0,0)}f(x,y)=0=f(0,0)$.** Sustituir da «$0\cdot\operatorname{sen}(\infty)$»: sin sentido; hay que acotar.
3. **Polares** (U p. 165): $x^2+y^2=\rho^2$, así que $F(\rho,\theta)=\rho^2\operatorname{sen}\dfrac1{\rho^2}$ (ni siquiera depende de $\theta$).
4. **Acotar:** $|F(\rho,\theta)-0|=\rho^2\left|\operatorname{sen}\dfrac1{\rho^2}\right|\le\rho^2=:h(\rho)$, y $h(\rho)\to0$. Por el caso 2 de U p. 165, $\lim_{(x,y)\to(0,0)}f(x,y)=0$.
   *(Equivalente, sin polares: $\lim_{(x,y)\to(0,0)}(x^2+y^2)=0$ y $\operatorname{sen}\frac1{x^2+y^2}$ está acotada por $1$; por la propiedad «infinitésimo $\times$ acotada», U p. 165.)*
5. **Conclusión:** el límite vale $0=f(0,0)$: **$f$ es continua en todo $\mathbb{R}^2$.**

E resuelve igual (correcto).

**Receta.** Si aparece $\operatorname{sen}(\text{algo que explota})$ o $\cos(\dots)$ multiplicado por algo que tiende a $0$: «infinitésimo $\times$ acotada».

**Error típico.** Intentar calcular el límite de $\operatorname{sen}\frac1{x^2+y^2}$ (no existe) y concluir que el producto no tiene límite.

sympy: $F=\rho^2\operatorname{sen}(1/\rho^2)$; límite $0$.

---

### Ejercicio 4.23 (E p. 152)

> Sea $f$ la función dada por $f(x,y)=\dfrac{y^2}{x}$ si $x\neq0$, $f(x,y)=0$ si $x=0$. Se pide estudiar su continuidad en el origen.

**Idea en una frase.** Todas las rectas dan $0$, pero la parábola $x=y^2$ (que iguala los grados de numerador y denominador) da $1\neq0$.

1. **Qué hay que ver:** continua en $(0,0)$ $\iff$ $\lim_{(x,y)\to(0,0)}f(x,y)=f(0,0)=0$.
2. **Rectas $y=mx$** ($x\neq0$): $f(x,mx)=\dfrac{m^2x^2}{x}=m^2x\to0$, para todo $m$.
3. **Eje $y$** ($x=0$, que no es de la forma $y=mx$): $f(0,y)=0\to0$.
4. **Todas las rectas dan $0$, pero eso no prueba nada** (U p. 162). Buscamos una curva que haga $y^2$ y $x$ «del mismo tamaño»: $x=y^2$. Entonces $f(y^2,y)=\dfrac{y^2}{y^2}=1\to1$.
5. **Conclusión:** por la curva $x=y^2$ el límite es $1\neq0=f(0,0)$, así que **$f$ no es continua en $(0,0)$** (y además el límite no existe: tendría que valer $0$ por las rectas y $1$ por la parábola).
6. *Más aún:* por $x=y^2/k$ ($k\neq0$) se obtiene $f=k$: acercándose por parábolas se consigue **cualquier** valor.

E resuelve igual (correcto). En el `.txt` la definición aparece como «$x=0$, $x=0$» por la pérdida del símbolo $\neq$ en la extracción; en el PDF pone $x\neq0$.

**Receta (elegir la curva).** Si en el cociente aparece $y^p$ frente a $x^q$, probar $x=y^{p/q}$ o $y=x^{q/p}$ para que todo quede con la misma potencia y se simplifique.

**Error típico.** Quedarse en las rectas y afirmar «límite $0$, continua».

sympy: rectas $0$; $x=y^2\Rightarrow1$; $x=y^2/k\Rightarrow k$.

---

## 2. Preguntas de examen (X)

**Seleccionadas para el HTML (7, de fácil a difícil, marcadas ★):** X p. 148 (dominio, corona) · X p. 140 (dominio e imagen) · X p. 137 (curvas de nivel) · X p. 33 (límite que no existe por los ejes) · X p. 45 / p. 98 (arcotangente: no existe por rectas) · X p. 65 (límite por polares) · X p. 138 (continuidad con $f(0,0)=1$).
**Complementarias:** X p. 143 (dominio, disco), X p. 4 (= E 4.19), X p. 16 (V/F caminos y continuidad), X p. 39 (continuidad con seno), X pp. 130-131 (= U Ej. 4.21), X pp. 122-125 (Examen 5, continuidad por polares).
**Otras del dossier no resueltas aquí** (no se pidieron o no se han leído en imagen): Sept 2010 P3a (p. 9), Feb 2011 Ej. 6 (pp. 11-12, análoga a X p. 39), Sept 2012 PC4 (p. 29), Electrónica 2 Ej. 5 (p. 102, $\sqrt{x^2+y^2}$), Electrónica 3 P3 (p. 104), Examen 2 Ej. 5 (p. 113, igual que U Ej. 4.20).

---

### ★ X p. 148 (Feb 2019, 2ª semana, I. Electrónica Industrial y Automática, Ej. 6, primer apartado, 1 punto)

> Sean $f(x,y)=\ln(4-x^2-y^2)$ y $g(x,y)=\sqrt{x^2+y^2-1}$: Calcule el dominio de $h(x,y)=f(x,y)+g(x,y)$.

**Idea en una frase.** La suma existe donde existen **las dos**: intersección de «dentro del círculo de radio 2 (sin borde)» y «fuera del de radio 1 (con borde)».

1. **Dominio de $f$:** logaritmo $\Rightarrow4-x^2-y^2>0\iff x^2+y^2<4$: disco abierto de centro $(0,0)$ y radio $2$.
2. **Dominio de $g$:** raíz $\Rightarrow x^2+y^2-1\ge0\iff x^2+y^2\ge1$: puntos a distancia $\ge1$ del origen (exterior del disco de radio 1, con la circunferencia).
3. **Dominio de $h=f+g$:** la intersección, $D=\{(x,y): 1\le x^2+y^2<4\}$: una **corona circular** que **incluye** la circunferencia interior (radio 1) y **no incluye** la exterior (radio 2).
4. **Comprobación:** $(1,0)$: $h=\ln3+0$ ✓. $(2,0)$: $\ln0$ ✗. $(0,\tfrac32)$: $\ln(1.75)+\sqrt{1.25}$ ✓.

X da lo mismo (correcto).

**Receta.** Dominio de suma/producto = intersección de dominios. Expresiones con $x^2+y^2$ = condiciones sobre la distancia al origen (discos, coronas). Decir siempre qué bordes entran.

**Error típico.** Poner $\le4$ (el logaritmo de $0$ no existe) o $>1$ (la raíz de $0$ sí existe).

---

### ★ X p. 140 (Feb 2018, 2ª semana, I. Electrónica Industrial y Automática, P4, 1 punto)

> Determinar el dominio y la imagen de la función $f(x,y)=x\ln y+y\ln x$.

**Idea en una frase.** Cada logaritmo pide su variable positiva; para la imagen basta encontrar una recta del dominio en la que $f$ sea el propio $\ln x$.

1. **Dominio:** $\ln y$ exige $y>0$ y $\ln x$ exige $x>0$: $D=\{(x,y): x>0,\ y>0\}$ (primer cuadrante abierto, sin ejes).
2. **Imagen:** tomemos los puntos $(x,1)$ con $x>0$ (están en $D$). Ahí $f(x,1)=x\ln1+1\cdot\ln x=\ln x$. Cuando $x$ recorre $(0,\infty)$, $\ln x$ recorre **todo** $\mathbb{R}$ (por ejemplo, $f(e^c,1)=c$ para cualquier $c$). Así $f(D)\supset\mathbb{R}$, es decir, **imagen $=\mathbb{R}$**.

**Comentario sobre la solución de X.** Llega al resultado correcto, pero la justificación de la imagen («la imagen del logaritmo es $(-\infty,\infty)$, por tanto…») es insuficiente: que cada sumando pueda tomar todos los valores no implica, por sí solo, que la expresión $x\ln y+y\ln x$ los tome. El argumento con $f(x,1)=\ln x$ lo demuestra.

**Receta.** Imagen: restringir $f$ a una recta sencilla del dominio ($y=1$, $x=1$, $y=x$…) donde quede una función conocida de una variable.

**Error típico.** Dar el dominio con $\ge$ (los ejes no entran: $\ln0$ no existe).

sympy: $f(x,1)=\ln x$.

---

### ★ X p. 137 (Feb 2017, 1ª semana, I. Electrónica Industrial y Automática, P4, 1 punto)

> Sea $f:\mathbb{R}^2\to\mathbb{R}$ la función dada por $f(x,y)=2x^2+2y^2-4$. Dibuje sus curvas de nivel.

**Idea en una frase.** $f=C$ es $x^2+y^2=\frac{C+4}2$: circunferencias centradas en el origen, salvo cuando el segundo miembro es $0$ (un punto) o negativo (nada).

1. **Curva de nivel $C$:** $2x^2+2y^2-4=C\iff x^2+y^2=\dfrac{C+4}{2}$.
2. **$C>-4$:** circunferencia de centro $(0,0)$ y radio $\sqrt{\dfrac{C+4}{2}}$. Por ejemplo $C=-2$: radio $1$; $C=4$: radio $2$; $C=14$: radio $3$.
3. **$C=-4$:** $x^2+y^2=0\iff(x,y)=(0,0)$: un **punto** (el mínimo de $f$).
4. **$C<-4$:** $x^2+y^2<0$ es imposible: **vacía**.
5. **Dibujo:** circunferencias concéntricas; los radios crecen como $\sqrt{C+4}$, así que **a igual salto de $C$ las curvas se van juntando** (la gráfica, un paraboloide, se hace más empinada). Imagen de $f$: $[-4,\infty)$.

**Omisión de X.** Dice solo «$x^2+y^2=C'$: familia de circunferencias», sin decir que $C'=\frac{C+4}2$ y sin los casos $C=-4$ (un punto) y $C<-4$ (vacío). En examen se deben indicar.

**Receta.** Como en U Ej. 4.11 (p. 156): despejar $x^2+y^2=$ (expresión en $C$) y discutir su signo: $>0$ circunferencia, $=0$ punto, $<0$ vacío.

**Error típico.** Escribir «radio $C$» o «radio $C+4$» en lugar de $\sqrt{(C+4)/2}$.

---

### ★ X p. 33 (Feb 2013, 1ª semana, Mecánica, Modelo A, PC4)

> Estúdiese si existe el siguiente límite: $\displaystyle\lim_{(x,y)\to(0,0)}\frac{x^2-y^2}{x^2+y^2}$.

**Idea en una frase.** Por el eje $x$ vale siempre $1$ y por el eje $y$ vale siempre $-1$: no puede tener límite.

1. **Sustituir:** $\frac00$.
2. **Eje $y$** ($x=0$, $y\neq0$): $f(0,y)=\dfrac{-y^2}{y^2}=-1\to-1$.
3. **Eje $x$** ($y=0$, $x\neq0$): $f(x,0)=\dfrac{x^2}{x^2}=1\to1$.
4. **No existe** (dos caminos, dos valores; U p. 161).

Es la misma función que E 4.24. **Errata de X:** llama «límites laterales» a los límites a lo largo de los ejes; «laterales» se usa en una variable ($x\to a^\pm$). Lo correcto: «límites a lo largo de los ejes».

**Receta.** Probar primero los ejes: es lo más rápido y a menudo basta.

**Error típico.** Calcular un solo eje y concluir.

---

### ★ X p. 45 (Feb 2014, Mecánica, Modelo B, Ej. 6 a)) = X p. 98 (Sept 2018, Mecánica, Modelo A, Ej. 6 a))

> Sea $f$ la función dada por $f(x,y)=\operatorname{arctg}\dfrac{xy}{x^2+y^2}$ si $(x,y)\neq(0,0)$, $f(0,0)=0$. Estudiar la continuidad de la función en $\mathbb{R}^2$.

**Idea en una frase.** Por la recta $y=mx$ el cociente vale la constante $\frac{m}{1+m^2}$, que cambia con $m$; el arcotangente no lo arregla.

1. **Fuera del origen:** $\frac{xy}{x^2+y^2}$ es cociente de polinomios con denominador $\neq0$ (continua) y $\operatorname{arctg}$ es continua en $\mathbb{R}$; la composición es continua. **Continua en $\mathbb{R}^2\setminus\{(0,0)\}$.**
2. **Origen, rectas $y=mx$** ($x\neq0$): $\dfrac{x\cdot mx}{x^2+m^2x^2}=\dfrac{m}{1+m^2}$ (constante), luego $f(x,mx)=\operatorname{arctg}\dfrac{m}{1+m^2}$ para todo $x\neq0$ y su límite es ese mismo número.
3. **Depende de $m$:** $m=0$ da $\operatorname{arctg}0=0$; $m=1$ da $\operatorname{arctg}\frac12\approx0.4636$. Distintos (el arcotangente es estrictamente creciente: valores distintos dentro dan valores distintos fuera).
4. **Conclusión:** no existe $\lim_{(x,y)\to(0,0)}f(x,y)$ $\Rightarrow$ $f$ **no es continua en $(0,0)$**. Continua en $\mathbb{R}^2\setminus\{(0,0)\}$.
5. *En polares:* $F=\operatorname{arctg}\dfrac{\operatorname{sen}2\theta}{2}$, depende de $\theta$ (caso 1).

X resuelve igual (correcto). **Aviso:** `indice_examenes_3.md` l. 98 registra erróneamente esta pregunta (p. 98) como «continua»; la solución impresa dice claramente **no continua**. *(Fuera de §4.2: en el apartado b) de X p. 45 la segunda derivada parcial aparece rotulada $\partial f/\partial x$ en vez de $\partial f/\partial y$; en X p. 98 está bien.)*

**Receta.** Si $f=\varphi(\text{cociente})$ con $\varphi$ continua y estrictamente monótona (arctg, exp…), basta estudiar el cociente: si su límite depende del camino, el de $f$ también.

**Error típico.** Creer que, como $\operatorname{arctg}$ está acotada, el límite es $0$ (acotada sí, pero no multiplicada por nada que tienda a $0$).

sympy: $\lim_{x\to0}f(x,mx)=\operatorname{arctg}\frac{m}{1+m^2}$; polar $\operatorname{arctg}(\operatorname{sen}2\theta/2)$.

---

### ★ X p. 65 (Feb 2016, Mecánica, Modelo B, P4, 1 punto)

> Calcule el límite $\displaystyle\lim_{(x,y)\to(0,0)}\frac{x^3+y^4}{x^2+y^2}$.

**Idea en una frase.** En polares el denominador es $\rho^2$ y el numerador tiene al menos $\rho^3$: sobra al menos un $\rho$, que tiende a $0$.

1. **Sustituir:** $\frac00$. Los caminos (eje $x$: $f=x\to0$; eje $y$: $f=y^2\to0$; rectas: $\to0$) sugieren $l=0$. Hay que **probarlo**.
2. **Polares** $x=\rho\cos\theta$, $y=\rho\operatorname{sen}\theta$ (U p. 165): $x^2+y^2=\rho^2$ y
$F(\rho,\theta)=\dfrac{\rho^3\cos^3\theta+\rho^4\operatorname{sen}^4\theta}{\rho^2}=\rho\cos^3\theta+\rho^2\operatorname{sen}^4\theta.$
3. **Acotar sin $\theta$:** como $|\cos\theta|\le1$ y $|\operatorname{sen}\theta|\le1$: $|F(\rho,\theta)-0|\le\rho+\rho^2=:h(\rho)\to0$.
4. **Conclusión** (caso 2 de U p. 165): $\displaystyle\lim_{(x,y)\to(0,0)}\frac{x^3+y^4}{x^2+y^2}=0$.

X da lo mismo (correcto); su frase «$\cos^3\theta+\rho\operatorname{sen}^4\theta$ está acotado» es cierta para $\rho\le1$ (cota $1+\rho\le2$); con la $h(\rho)$ explícita queda más claro.

**Receta.** Polares: simplificar $\rho^2$ del denominador, acotar senos y cosenos por $1$, y comprobar que queda una $h(\rho)$ **sin $\theta$** que tiende a $0$.

**Error típico.** Escribir «$\lim_{\rho\to0}\rho\cos^3\theta=0$» para un $\theta$ fijo y darlo por probado sin la cota uniforme (ver el Propio 3: puede fallar).

sympy: $F=\rho(\cos^3\theta+\rho\operatorname{sen}^4\theta)$.

---

### ★ X p. 138 (Feb 2017, 1ª semana, I. Electrónica Industrial y Automática, Ej. 6, primer apartado, 1.5 puntos)

> Sea $f:\mathbb{R}^2\to\mathbb{R}$ la función dada por $f(x,y)=\dfrac{x^2y^3}{x^4+y^2}$ si $(x,y)\neq(0,0)$, $f(0,0)=1$. Estudiar la continuidad de $f$ en el punto $(0,0)$.

**Idea en una frase.** Cerca del origen $f$ se acerca a $0$ por cualquier camino, pero la función vale $1$ en el origen: hay un «salto» de valor.

1. **Lo que hay que comparar:** continua en $(0,0)$ $\iff\lim_{(x,y)\to(0,0)}f(x,y)=f(0,0)=1$.
2. **Rectas $y=mx$:** $f(x,mx)=\dfrac{m^3x^5}{x^4+m^2x^2}=\dfrac{m^3x^3}{x^2+m^2}\to0$ (para $m\neq0$ el denominador tiende a $m^2\neq0$; para $m=0$, $f(x,0)=0$). Eje $y$: $f(0,y)=0$.
3. **Basta para la discontinuidad.** Si el límite existiera, debería valer lo mismo que por las rectas, $0$; y $0\neq1$. Si no existiera, tampoco sería continua. **En los dos casos, $f$ no es continua en $(0,0)$.** (Este es el razonamiento de X, válido aunque breve.)
4. *Extra (no necesario, pero aclara):* el límite **sí existe y vale 0**. Como $\dfrac{y^2}{x^4+y^2}\le1$,
$|f(x,y)|=x^2|y|\cdot\dfrac{y^2}{x^4+y^2}\le x^2|y|\to0,$
y por el emparedado (U p. 163) $\lim_{(x,y)\to(0,0)}f(x,y)=0$. Si se redefiniera $f(0,0)=0$, sería continua.

X: correcto en el resultado. Escribe «$\lim_{(x,mx)\to(0,0)}$», notación poco habitual (mejor $\lim_{x\to0}f(x,mx)$).

**Receta.** Para **refutar** la continuidad no hace falta saber si el límite existe: basta **un** camino cuyo límite no sea $f(a,b)$.

**Error típico.** Concluir «continua» porque «todas las rectas dan lo mismo», sin mirar el valor $f(0,0)$ que da el enunciado.

sympy: rectas $0$; $y=x^2\Rightarrow f=x^4/2\to0$; $x^2y-f=\dfrac{x^6y}{x^4+y^2}$ (confirma la cota).

---

### X p. 143 (Sept 2018, I. Electrónica Industrial y Automática, Ej. 6, primer apartado, 1 punto) — complementaria

> Para la función dada por $f(x,y)=\ln(36-x^2-y^2)$, determine y dibuje su dominio.

1. Logaritmo: $36-x^2-y^2>0\iff x^2+y^2<36$.
2. $D=\{(x,y): x^2+y^2<36\}$: **disco abierto** de centro $(0,0)$ y radio $6$ (sin la circunferencia).

X dice «un círculo, sin incluir su frontera»: correcto en el fondo; en la terminología de U (pp. 145-146) es un «disco abierto».

**Receta / error típico:** como X p. 148; no incluir el borde, porque $\ln0$ no existe.

---

### X p. 4 (Feb 2010, 2ª semana, Ing. Eléctrica, PC3, 1 punto) — complementaria

> Razone por qué no existe el límite $\displaystyle\lim_{(x,y)\to(0,0)}\frac{x^2+y^3}{x^2+y^2}$.

Idéntica a **E 4.19**: reiterados $1$ y $0$ $\Rightarrow$ no existe. X: correcto.

---

### X p. 16 (Sept 2011, Mecánica, PC3, 1 punto) — complementaria

> Sea $f:\mathbb{R}^2\to\mathbb{R}$ una función definida en una bola centrada en un punto $(a,b)$. Razone si es cierto o falso que si en $(a,b)$ existen y son iguales los límites a lo largo de todos los caminos entonces podemos asegurar que $f$ es continua en este punto.

**Idea en una frase.** Aunque el límite exista, la continuidad exige además que **coincida con el valor** $f(a,b)$.

1. **Falso.** Continuidad (Def. 4.5) = existe el límite **y** vale $f(a,b)$.
2. **Contraejemplo (X):** $f(x,y)=x^2+y$ si $(x,y)\neq(0,0)$, $f(0,0)=1$. Por cualquier camino, $x^2+y\to0$ (es un polinomio, continuo), así que el límite existe y vale $0$; pero $f(0,0)=1\neq0$: no es continua.

X: correcto. **Matiz:** si de verdad los límites coinciden por **todos** los caminos, el límite existe; lo que falla es la igualdad con $f(a,b)$. (No confundir con «todas las rectas», que no basta ni para la existencia.)

**Receta.** V/F de continuidad: recordar las **dos** condiciones (existe el límite / vale $f(a,b)$) y romper la que no se garantiza.

---

### X p. 39 (Sept 2013, Mecánica y Electrónica, Modelo A, P6) — complementaria

> Estúdiese la continuidad de la función $f(x,y)=x^2\operatorname{sen}\left(\dfrac{1}{x^2+y^2}\right)$ si $(x,y)\neq(0,0)$, $f(0,0)=0$.

1. **Fuera del origen:** continua (producto de polinomio y composición de $\operatorname{sen}$ con una racional de denominador $\neq0$).
2. **Origen:** $0\le|f(x,y)|\le x^2$ porque $|\operatorname{sen}(\cdot)|\le1$; y $x^2\to0$. Por el emparedado (U p. 163), $|f|\to0$, luego $f\to0=f(0,0)$.
3. **Continua en $\mathbb{R}^2$.**

X: correcto. Su frase «continua si $(x,y)\neq(0,0)$ donde el argumento del seno no está definido» está mal construida: debe entenderse «continua en $(x,y)\neq(0,0)$; el único punto donde el argumento del seno no está definido es $(0,0)$». También usa, sin decirlo, que $|g|\to0\Rightarrow g\to0$ (porque $-|g|\le g\le|g|$, como hace U al final del Ej. 4.17, p. 164). Es del mismo tipo que E 4.22 y X pp. 11-12 (Feb 2011).

---

### X pp. 130-131 (I. Electrónica Industrial y Automática, examen B sin fecha, Ej. 6, primer apartado) — complementaria

> Para la función dada por $f(x,y)=\dfrac{x^2}{x^2+y^2}$ si $(x,y)\neq(0,0)$, $f(0,0)=0$: Estudie su continuidad.

1. Continua en $\mathbb{R}^2\setminus\{(0,0)\}$ (cociente de polinomios, denominador $\neq0$).
2. Camino $y=0$: $f(x,0)=1\to1\neq0=f(0,0)$. **No continua en $(0,0)$.**

X: correcto (es U Ej. 4.21, p. 167). Basta un camino porque se compara con $f(0,0)$, como en X p. 138. (Los otros apartados, asíntotas de $G(z)=f(\pi,z)$ y gradiente, son de §1.4 y §4.3.)

---

### X pp. 122-125 (Examen 5, «elaborado con exámenes de asignaturas similares», Ej. 6, solo continuidad) — complementaria

> Estudiar la continuidad, derivabilidad y diferenciabilidad de la función $f(x,y)=\dfrac{x^3+xy^2+3y^4}{x^2+y^2}$ si $(x,y)\neq(0,0)$, $f(0,0)=0$. [Aquí solo la continuidad; derivabilidad y diferenciabilidad son de §4.3 y Tema 5.]

1. **Fuera del origen:** continua (cociente de polinomios, denominador $\neq0$).
2. **Caminos (para intuir):** reiterados $\lim_{x\to0}x=0$ y $\lim_{y\to0}3y^2=0$; rectas $\dfrac{x+m^2x+3m^4x^2}{1+m^2}\to0$. Candidato $l=0$.
3. **Polares:** el numerador es $\rho^3\cos^3\theta+\rho^3\cos\theta\operatorname{sen}^2\theta+3\rho^4\operatorname{sen}^4\theta=\rho^3\cos\theta(\cos^2\theta+\operatorname{sen}^2\theta)+3\rho^4\operatorname{sen}^4\theta$, luego $F(\rho,\theta)=\rho\cos\theta+3\rho^2\operatorname{sen}^4\theta$.
4. **Cota sin $\theta$:** $|F|\le\rho+3\rho^2\to0$. Límite $0=f(0,0)$: **continua en $\mathbb{R}^2$.**

X: resultado correcto. Al final escribe «$\lim_{\rho\to0}\rho\cos^3\theta+\rho\cos\theta\sin^2\theta+3\rho^2\sin^4\theta=0$» sin paréntesis y sin dar la cota independiente de $\theta$ (paso 4), que es lo que exige U p. 165. *(Fuera de §4.2: en el Ej. 5 de este mismo examen, X p. 123, la regla del trapecio da $68$ porque se suma $31$ en lugar de $f(2)=26$; lo correcto es $\frac{3-1}{2}\big(\frac{31+43}{2}+26\big)=63$, como en X p. 65.)*

sympy: $F=\rho(\cos\theta+3\rho\operatorname{sen}^4\theta)$; reiterados $0,0$.

---

## 3. Ejemplos propios (dificultad creciente)

### Propio 1 — Dominio con raíz y logaritmo (fácil-medio)

> Halla y dibuja el dominio de $f(x,y)=\sqrt{y-x^2}+\ln(4-x^2-y^2)$. Variante: ¿qué cambia si la función es $g(x,y)=\dfrac{\sqrt{y-x^2}}{\ln(4-x^2-y^2)}$?

**Idea en una frase.** Cada pieza impone una condición y el dominio es la intersección; si el logaritmo está en un denominador, además no puede valer $0$.

1. **Raíz:** $y-x^2\ge0\iff y\ge x^2$: sobre o por encima de la parábola $y=x^2$ (con la parábola).
2. **Logaritmo:** $4-x^2-y^2>0\iff x^2+y^2<4$: disco abierto de radio $2$ (sin la circunferencia).
3. **Dominio de $f$:** $D_f=\{(x,y): y\ge x^2,\ x^2+y^2<4\}$. Es la «gota» limitada abajo por la parábola (incluida) y arriba por la circunferencia (excluida). Se cortan donde $y=x^2$ y $x^2+y^2=4$: $y+y^2=4$, $y=\frac{-1+\sqrt{17}}2\approx1.56$, $x\approx\pm1.25$ (esos dos puntos **no** están en $D_f$, porque están en la circunferencia).
4. **Comprobación:** $(0,1)$: $1\ge0$ y $1<4$ ✓. $(1.5,1.5)$: $1.5-2.25<0$ ✗. $(0,2)$: $4-4=0$ ✗ ($\ln0$).
5. **Variante $g$:** además, denominador $\neq0$: $\ln(4-x^2-y^2)\neq0\iff4-x^2-y^2\neq1\iff x^2+y^2\neq3$. Hay que **quitar** de $D_f$ el arco de la circunferencia de radio $\sqrt3$ que está dentro de la región (por ejemplo, el punto $(0,\sqrt3)$, que sí estaba en $D_f$).

**Receta.** Lista de condiciones (raíz $\ge0$, log $>0$, denominador $\neq0$) $\to$ intersección $\to$ dibujar fronteras y decidir qué bordes entran.

**Error típico.** Olvidar la condición «denominador $\neq0$» cuando el denominador es un logaritmo ($\ln u=0$ para $u=1$).

Fuente: propia (sobre U Def. 4.3 y margen, p. 153). sympy: intersección $(\pm1.250,\ 1.562)$; la circunferencia $x^2+y^2=3$ corta a la parábola en $y=\frac{-1+\sqrt{13}}2$.

---

### Propio 2 — Curvas de nivel (medio)

> Describe las curvas de nivel de (a) $f(x,y)=x^2+4y^2$ y (b) $g(x,y)=xy$. Indica la imagen de cada función.

**Idea en una frase.** (a) elipses que se reducen a un punto en $k=0$; (b) hipérbolas que degeneran en los ejes en $k=0$.

1. **(a) Nivel $k$:** $x^2+4y^2=k$.
   - $k<0$: vacía (suma de cuadrados $\ge0$).
   - $k=0$: solo $(0,0)$.
   - $k>0$: $\dfrac{x^2}{k}+\dfrac{y^2}{k/4}=1$, **elipse** de semiejes $\sqrt k$ (en $x$) y $\frac{\sqrt k}{2}$ (en $y$). Ej.: $k=4$ pasa por $(\pm2,0)$ y $(0,\pm1)$.
   - Imagen de $f$: $[0,\infty)$ (no negativa, y $f(x,0)=x^2$ toma todo valor $\ge0$).
2. **(b) Nivel $k$:** $xy=k$.
   - $k\neq0$: $y=\dfrac kx$, **hipérbola** equilátera; ramas en los cuadrantes I y III si $k>0$, en II y IV si $k<0$.
   - $k=0$: $xy=0\iff x=0$ o $y=0$: los **dos ejes**.
   - Imagen de $g$: $\mathbb{R}$ ($g(x,1)=x$).
3. *Lectura:* en (a), como en E 4.16, las elipses crecen hacia fuera: $f$ aumenta al alejarse del origen. En (b) el signo de $g$ cambia al cruzar los ejes (silla).

**Receta.** $f=k$; casos según $k$ (vacía / punto o degenerada / curva); reconocer la cónica dividiendo para dejar «$=1$».

**Error típico.** Dar «circunferencias» en (a): el $4$ delante de $y^2$ achata la curva.

Fuente: propia (sobre U p. 155 y Ej. 4.11 pp. 155-156).

---

### Propio 3 — Límite que no existe aunque fallen las rectas y engañen las polares (medio-difícil)

> Estudia $\displaystyle\lim_{(x,y)\to(0,0)}\frac{xy^2}{x^2+y^4}$.

**Idea en una frase.** Rectas y reiterados dan $0$, pero la parábola $x=y^2$ da $\frac12$; y las polares, aplicadas «a la ligera», harían creer que el límite es $0$.

1. **Sustituir:** $\frac00$.
2. **Reiterados:** con $y\neq0$ fijo, $\lim_{x\to0}\frac{xy^2}{x^2+y^4}=\frac0{y^4}=0$; con $x\neq0$ fijo, $\lim_{y\to0}\frac{xy^2}{x^2+y^4}=\frac0{x^2}=0$. Ambos $0$.
3. **Rectas $y=mx$:** $\dfrac{m^2x^3}{x^2+m^4x^4}=\dfrac{m^2x}{1+m^4x^2}\to0$. Todas $0$. Aún no se sabe nada.
4. **Curva que iguala grados:** en el denominador compiten $x^2$ e $y^4$; con $x=y^2$ los dos son $y^4$: $f(y^2,y)=\dfrac{y^4}{y^4+y^4}=\dfrac12\to\dfrac12$.
5. **Conclusión:** $\frac12\neq0$ $\Rightarrow$ **no existe** el límite. (Con $x=-y^2$ sale $-\frac12$.)
6. **Trampa de las polares:** $F(\rho,\theta)=\dfrac{\rho\cos\theta\operatorname{sen}^2\theta}{\cos^2\theta+\rho^2\operatorname{sen}^4\theta}$. Para cada $\theta$ **fijo** con $\cos\theta\neq0$, $F\to0$ (el denominador tiende a $\cos^2\theta\neq0$); y si $\cos\theta=0$, $F=0$. ¡Todos los «rayos» dan $0$! Pero **no** hay una cota $|F|\le h(\rho)$ sin $\theta$: cuando $\cos\theta$ es muy pequeño el denominador también lo es. Estamos en el **caso 3** de U p. 165: las polares no permiten concluir, y el paso 4 demuestra que el límite no existe.

**Receta.** Polares solo **prueban** el límite si la cota final no depende de $\theta$. Si el denominador conserva un término en $\theta$ que puede anularse, desconfiar y buscar curvas.

**Error típico.** «$\lim_{\rho\to0}F=0$ para todo $\theta$, luego el límite es 0». Falso: eso equivale a probar solo las rectas.

Fuente: propia (análogo a U Ej. 4.16, pp. 162-163, y criterio de polares U p. 165). sympy: reiterados $0,0$; rectas $0$; $x=y^2\Rightarrow\frac12$; $x=-y^2\Rightarrow-\frac12$; $F$ como arriba.

---

### Propio 4 — Límite que existe en un punto distinto del origen; continuidad (difícil)

> Sea $f(x,y)=\dfrac{(x-1)\,y^2}{(x-1)^2+y^2}$ si $(x,y)\neq(1,0)$, $f(1,0)=c$. ¿Para qué valor de $c$ es $f$ continua en $\mathbb{R}^2$?

**Idea en una frase.** Centrar las polares en $(1,0)$; el cociente $\frac{y^2}{(x-1)^2+y^2}$ está entre $0$ y $1$ y el factor $(x-1)$ tiende a $0$.

1. **Fuera de $(1,0)$:** cociente de polinomios con denominador $(x-1)^2+y^2\neq0$: continua.
2. **Límite en $(1,0)$, caminos (para intuir):** recta $x=1$: $f(1,y)=0$; rectas $y=m(x-1)$: $\dfrac{m^2(x-1)^3}{(1+m^2)(x-1)^2}=\dfrac{m^2(x-1)}{1+m^2}\to0$. Candidato $l=0$.
3. **Probarlo con polares centradas en $(1,0)$** (U p. 165, con $a=1$, $b=0$): $x=1+\rho\cos\theta$, $y=\rho\operatorname{sen}\theta$. Denominador $\rho^2$; numerador $\rho^3\cos\theta\operatorname{sen}^2\theta$. Así $F(\rho,\theta)=\rho\cos\theta\operatorname{sen}^2\theta$ y $|F-0|\le\rho\to0$ (cota sin $\theta$). Límite $=0$.
4. *Alternativa (emparedado):* $\dfrac{y^2}{(x-1)^2+y^2}\le1$, luego $|f(x,y)|\le|x-1|\to0$.
5. **Continuidad:** $f$ es continua en $(1,0)$ $\iff c=0$. **Respuesta: $c=0$**; para cualquier otro $c$, $f$ es continua en $\mathbb{R}^2\setminus\{(1,0)\}$ y discontinua en $(1,0)$.

**Receta.** Si el punto no es el origen, trasladar: polares $x=a+\rho\cos\theta$, $y=b+\rho\operatorname{sen}\theta$ (o renombrar $u=x-a$, $v=y-b$) y razonar como en el origen.

**Error típico.** Usar $x=\rho\cos\theta$, $y=\rho\operatorname{sen}\theta$ (centradas en el origen) para un límite en $(1,0)$: con eso $\rho\to0$ significa acercarse a $(0,0)$, no a $(1,0)$.

Fuente: propia (sobre U p. 165 y Def. 4.5 p. 166). sympy: $F=\rho\cos\theta\operatorname{sen}^2\theta$; rectas $\to0$.

---

## 4. Resumen de erratas y omisiones detectadas

**En E (todas verificadas en la imagen del PDF):**
- **4.13** (pp. 144-145): desigualdades estrictas ($x^2>y^3$, $y<x^{2/3}$); deben ser $\ge$ / $\le$ (la curva $y=x^{2/3}$ pertenece al dominio; p. ej. $(1,1)$).
- **4.14** (p. 145): «$xy\ge0$» debe ser «$xy>0$» (resultado final correcto).
- **4.16** (p. 148): «pasa de crecer a decrecer o al revés»: sobre $x=4$ hay un mínimo en $y=0$ (pasa de decrecer a crecer). Imprecisión menor.
- **4.17** (p. 148): «son hipérbolas» omite el nivel $C=8$ ($C'=0$): par de rectas $y=\pm\sqrt3x$; tampoco distingue hipérbolas que cortan al eje $x$ ($C>8$) o al eje $y$ ($C<8$).
- **4.20** (p. 150): falta contraejemplo (p. ej. $xy/(x^2+y^2)$).
- **4.21** (p. 151): $\operatorname{dom}h=\{y\ge0\}\cup\{x=0\}$, no solo $\{y\ge0\}$.
- **4.24** (p. 153): «el producto» $\to$ «el cociente».

**En X:**
- p. 33 (Feb 2013): «límites laterales» $\to$ límites a lo largo de los ejes.
- p. 39 (Sept 2013): frase mal construida sobre dónde está definido el seno (resultado correcto).
- p. 45 (Feb 2014 B, apdo. b, fuera de §4.2): segunda derivada parcial rotulada $\partial f/\partial x$ (debe ser $\partial f/\partial y$).
- p. 98: correcta (no continua); el error está en `indice_examenes_3.md` l. 98.
- p. 123 (Examen 5, Ej. 5, fuera de §4.2): trapecio $=68$ por sumar $31$ en lugar de $f(2)=26$; correcto $63$.
- p. 125 (Examen 5): límite polar sin paréntesis y sin cota independiente de $\theta$.
- p. 137 (Feb 2017 P4): faltan $C=-4$ (punto) y $C<-4$ (vacío), y la relación $C'=(C+4)/2$.
- p. 138 (Feb 2017 Ej. 6): razonamiento por rectas válido para la discontinuidad, pero no dice que el límite existe (existe y vale $0$).
- p. 140 (Feb 2018 P4): justificación de la imagen insuficiente (usar $f(x,1)=\ln x$).
- p. 143 (Sept 2018 Electr.): «círculo sin frontera» = disco abierto (terminología).
