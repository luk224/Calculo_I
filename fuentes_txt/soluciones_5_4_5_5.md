# Soluciones Temas 5.4 y 5.5: Valores extremos y extremos condicionados (Lagrange)

Resolución paso a paso de los ejercicios de **E** de extremos y multiplicadores de Lagrange (Ejercicios 5.28-5.48, E pp. 191-212), de los ejemplos de U que enseñan un método distinto (Ej. 5.17-5.18, 5.20-5.22, 5.24 y 5.26, U pp. 216-232), de 6 preguntas de examen **X** y de 4 ejemplos propios. Todos los cálculos (puntos críticos, Hessianas, sistemas de Lagrange, valores) se han comprobado con sympy (script `v545.py` en el scratchpad de la sesión). Las páginas de X se han leído como imagen (pp. 9, 33-34, 83-84, 94-95, 97, 134).

Páginas: U impresa (= PDF + 2); E impresa = PDF; X = página PDF de `Examenes-resueltos-Calculo.pdf`.

## 0. Herramientas de teoría que se usan

| Clave | Enunciado (resumido) | Dónde |
|---|---|---|
| Extremo absoluto | $f$ alcanza un **máximo absoluto** en $(a,b)$ si $f(x,y)\le f(a,b)$ para todo $(x,y)\in D$; **mínimo absoluto** si $f(x,y)\ge f(a,b)$ para todo $(x,y)\in D$. | U Def. 5.7-5.9, p. 213 |
| Extremo relativo | Igual, pero solo para los $(x,y)$ de un disco abierto alrededor de $(a,b)$ (dentro de $D$). Todo extremo absoluto es relativo. | U Def. 5.10-5.12, p. 214 |
| Punto crítico | $(a,b)$ con $\frac{\partial f}{\partial x}(a,b)=\frac{\partial f}{\partial y}(a,b)=0$, es decir $\nabla f(a,b)=(0,0)$. En $n$ variables, $\nabla f=\bar 0$. | U Def. 5.13, p. 216 |
| **Condición necesaria** | $f$ diferenciable en $D$ abierto. Si $f$ alcanza un extremo relativo en $(a,b)\in D$, entonces $\nabla f(a,b)=\bar 0$. (El recíproco es falso.) | U p. 218 |
| Punto de silla | Punto crítico que **no** es extremo relativo: en cualquier disco alrededor hay puntos con valor mayor y puntos con valor menor. Modelo: $3x^2-y^2$ en $(0,0)$. | U p. 219, Ej. 5.19 |
| **Condición suficiente (Hessiana)** | En un punto crítico, $H f(a,b)=\begin{pmatrix} r & s\\ t & u\end{pmatrix}=\begin{pmatrix} f_{xx} & f_{xy}\\ f_{yx} & f_{yy}\end{pmatrix}(a,b)$, $d=\det Hf(a,b)$: $d>0,\ r>0\Rightarrow$ mínimo relativo; $d>0,\ r<0\Rightarrow$ máximo relativo; $d<0\Rightarrow$ punto de silla; $d=0$ (o $d>0$ con $r=0$) $\Rightarrow$ caso dudoso. Puede usarse $u$ en lugar de $r$. | U p. 220-221 |
| **Teorema de los valores extremos** | Si $f$ es continua en $S\subset\mathbb{R}^n$ **cerrado y acotado**, alcanza el máximo y el mínimo absolutos en $S$. Además se alcanzan en la frontera de $S$ o en un punto crítico del interior de $S$. | U p. 222 |
| Procedimiento en un compacto | (1) Puntos críticos de $f$ en el interior. (2) Candidatos de la frontera. (3) Evaluar $f$ en todos: el mayor valor es el máximo absoluto, el menor el mínimo absoluto. | U p. 222 |
| **Teorema de Lagrange** | $f,g$ continuas con parciales continuas. Si $f$ tiene un extremo relativo en $(a,b)$ sobre la curva $g(x,y)=0$ y $\nabla g(a,b)\neq\bar 0$, existe $\lambda$ con $\nabla f(a,b)=-\lambda\nabla g(a,b)$. Equivale a que $(a,b,\lambda)$ sea punto crítico de $F(x,y,\lambda)=f(x,y)+\lambda g(x,y)$. Vale igual en $\mathbb{R}^n$. | U pp. 226 y 228 |
| Método de los multiplicadores | (1) $F=f+\lambda g$. (2) Resolver $\nabla F=\bar 0$ (la última ecuación, $\frac{\partial F}{\partial\lambda}=0$, es la propia restricción $g=0$). (3) Si el conjunto $g=0$ es cerrado y acotado, evaluar $f$ en los puntos obtenidos: mayor = máximo, menor = mínimo. (4) Alternativa: si de $g=0$ se despeja $y=h(x)$, estudiar $f(x,h(x))$ (una variable). | U p. 228 |
| Despejar en la restricción | Ej. 5.22: en la frontera se despeja una variable (teorema de la función implícita) y se reduce a una variable; los puntos donde no se puede despejar se estudian aparte. | U pp. 224-225 |

**Herramientas de temas anteriores que aparecen:** derivadas parciales y gradiente (U §4.3, pp. 168-173); plano tangente $z=f(a,b)+\nabla f(a,b)\cdot(x-a,y-b)$ (U (5.2), p. 189); extremos de una variable con $f'$ y $f''$ (U §3.4, pp. 125-134); $e^t>0$ para todo $t$; «un producto es cero si y solo si lo es algún factor».

---

### Receta general del tema

> **Extremos relativos de $f(x,y)$ en un abierto (sin restricciones):**
> 1. Calcular $f_x$, $f_y$ e igualarlas a $0$. Resolver el sistema **por casos** (sacar factor común; «producto = 0 ⇒ algún factor = 0»). Así salen los **puntos críticos**: los únicos candidatos.
> 2. Calcular $f_{xx}$, $f_{xy}$, $f_{yy}$ y, en **cada** punto crítico, $d=f_{xx}f_{yy}-f_{xy}^2$ y $r=f_{xx}$.
> 3. Clasificar: $d<0$ silla; $d>0$ y $r>0$ mínimo; $d>0$ y $r<0$ máximo; $d=0$ dudoso (mirar el signo de $f-f(a,b)$ a mano).
>
> **Extremos absolutos en un conjunto cerrado y acotado $S$:** teorema de los valores extremos ⇒ existen. Candidatos = críticos del interior + candidatos de la frontera (Lagrange, o parametrizar cada trozo de la frontera, + «esquinas»). Se evalúa $f$ en todos y se comparan. **No hace falta la Hessiana.**
>
> **Extremos de $f$ con una restricción $g=0$ (Lagrange):** $F=f+\lambda g$; resolver $F_x=0$, $F_y=0$ ($F_z=0$), $g=0$; comprobar $\nabla g\neq\bar 0$ en la restricción; si la restricción es cerrada y acotada, comparar valores de $f$. Si no lo es, decidir con el sentido del problema o despejando y pasando a una variable.

---

## 1. Ejemplos de U que enseñan un método

### U Ej. 5.17 y 5.20 (pp. 216-217 y 221-222): puntos críticos con una exponencial y clasificación

> Determine los puntos críticos de $f(x,y)=(x^2+2y^2)\,e^{1-(x^2+y^2)}$ y clasifíquelos.

**Antes de calcular**
- *Qué me piden:* los puntos con $\nabla f=\bar 0$ y si en cada uno hay máximo, mínimo o silla.
- *Cómo lo pienso:* la exponencial nunca vale $0$, así que «sobra» en las ecuaciones; queda un sistema de dos productos igualados a cero que se resuelve por casos.
- *Qué uso:* Def. 5.13 (U p. 216) y condición suficiente con la Hessiana (U p. 220).
- *Por dónde empiezo:* derivar con la regla del producto y sacar factor común $e^{1-(x^2+y^2)}$.

1. **Derivadas** (producto: derivada del polinomio por la exponencial más polinomio por la derivada de la exponencial, que es $-2x\,e^{\dots}$ o $-2y\,e^{\dots}$):
$f_x=2x(1-x^2-2y^2)\,e^{1-(x^2+y^2)}$, $\quad f_y=2y(2-x^2-2y^2)\,e^{1-(x^2+y^2)}$.
2. **Quitar la exponencial:** como $e^{t}>0$ siempre, $f_x=0\iff x(1-x^2-2y^2)=0$ y $f_y=0\iff y(2-x^2-2y^2)=0$.
3. **Casos** (cada ecuación es un producto igual a $0$):
   - $x=0,\ y=0$: punto $(0,0)$.
   - $x=0,\ y\ne0$: la 2ª da $2-2y^2=0$, $y=\pm1$: puntos $(0,\pm1)$.
   - $y=0,\ x\ne0$: la 1ª da $1-x^2=0$, $x=\pm1$: puntos $(\pm1,0)$.
   - $x\ne0,\ y\ne0$: habría que tener a la vez $x^2+2y^2=1$ y $x^2+2y^2=2$: imposible.
4. **Hessiana en cada punto** (sympy): $Hf(0,0)=\begin{pmatrix}2e&0\\0&4e\end{pmatrix}$, $d=8e^2>0$, $r=2e>0$: **mínimo relativo**. $Hf(\pm1,0)=\begin{pmatrix}-4&0\\0&2\end{pmatrix}$, $d=-8<0$: **silla**. $Hf(0,\pm1)=\begin{pmatrix}-2&0\\0&-8\end{pmatrix}$, $d=16>0$, $r=-2<0$: **máximo relativo**.

**Receta.** Si todas las derivadas llevan un factor que nunca se anula (exponencial), se quita; el resto se resuelve por casos «este factor $=0$ / este otro $=0$».

### U Ej. 5.18 (p. 217): infinitos puntos críticos

> $f(x,y)=\dfrac{x^2y^2}{x^2+y^2}$ si $(x,y)\neq(0,0)$, $f(0,0)=0$.

1. Fuera del origen: $f_x=\dfrac{2xy^4}{(x^2+y^2)^2}$, $f_y=\dfrac{2x^4y}{(x^2+y^2)^2}$.
2. El denominador es positivo; se anulan las dos si y solo si $x=0$ o $y=0$: **todos los puntos de los ejes** son críticos.
3. **Para entenderlo:** en los ejes $f=0$ y en el resto $f>0$, así que todos son mínimos relativos (no estrictos). La Hessiana no hace falta: basta mirar el signo.

**Receta.** Los puntos críticos no tienen por qué ser aislados; si $f\ge0$ y se anula en ellos, son mínimos sin más cuentas.

### U Ej. 5.21, 5.22 y 5.24 (pp. 223-225 y 229): el mismo problema por dos caminos

> Extremos absolutos de $f(x,y)=x^2+2y^2$ en el disco $S=\{x^2+y^2\le1\}$.

**Antes de calcular**
- *Qué me piden:* el máximo y el mínimo de $f$ en el disco cerrado.
- *Cómo lo pienso:* el disco es cerrado y acotado: los extremos existen y están en un crítico del interior o en la circunferencia.
- *Qué uso:* teorema de los valores extremos (U p. 222); en la frontera, despejar (U p. 224) o Lagrange (U p. 228).
- *Por dónde empiezo:* $\nabla f=(2x,4y)=\bar 0$.

1. **Interior** (Ej. 5.21): $\nabla f=(2x,4y)=\bar 0\iff(x,y)=(0,0)$, con $f(0,0)=0$.
2. **Frontera despejando** (Ej. 5.22): en $x^2+y^2=1$ se tiene $y^2=1-x^2$, luego $f=x^2+2(1-x^2)=2-x^2$ para $x\in(-1,1)$. $F'(x)=-2x=0\iff x=0$, $y=\pm1$. Donde no se puede despejar $y$ ($\frac{\partial g}{\partial y}=2y=0$): $(\pm1,0)$, se añaden a mano.
3. **Frontera con Lagrange** (Ej. 5.24): $F=x^2+2y^2+\lambda(x^2+y^2-1)$: $2x(1+\lambda)=0$, $2y(2+\lambda)=0$, $x^2+y^2=1$. Casos: $\lambda=-1\Rightarrow y=0,\ x=\pm1$; $\lambda=-2\Rightarrow x=0,\ y=\pm1$. Mismos candidatos, sin tener que «añadir a mano» nada.
4. **Comparar:** $f(0,0)=0$, $f(\pm1,0)=1$, $f(0,\pm1)=2$. **Mínimo absoluto $0$ en $(0,0)$; máximo absoluto $2$ en $(0,\pm1)$.** (Sobre la circunferencia sola: mínimo condicionado $1$ en $(\pm1,0)$.)

**Receta.** Lagrange evita el problema de «dónde no se puede despejar»; despejar evita el $\lambda$. Los dos dan los mismos candidatos.

### U Ej. 5.26 (pp. 231-232): Lagrange en tres variables, con $\lambda=0$

> Tres números no negativos con suma $9$ y producto máximo.

1. $F=xyz+\lambda(x+y+z-9)$: $yz+\lambda=0$, $xz+\lambda=0$, $xy+\lambda=0$, $x+y+z=9$.
2. **Caso $\lambda=0$:** $yz=xz=xy=0$: al menos dos son $0$, y la suma da $(9,0,0)$, $(0,9,0)$, $(0,0,9)$, con producto $0$.
3. **Caso $\lambda\ne0$:** ninguno es $0$; de $yz=xz$ sale $x=y$, de $xz=xy$ sale $y=z$: $x=y=z=3$, $\lambda=-9$.
4. El triángulo $\{x+y+z=9,\ x,y,z\ge0\}$ es cerrado y acotado: **máximo $27$ en $(3,3,3)$**.

**Receta.** En los sistemas de Lagrange hay que mirar siempre el caso $\lambda=0$ por separado (no se puede dividir entre $\lambda$).

---

## 2. Ejercicios de E (orden de dificultad creciente; numeración conservada)

Orden propuesto para aprender:
- **Sin derivadas, solo signo o teorema:** 5.28 → 5.38 → 5.33.
- **Hallar puntos críticos:** 5.29 → 5.30 → 5.35.
- **Clasificar con la Hessiana:** 5.31 → 5.32 → 5.37 → 5.36 → 5.34.
- **Lagrange:** 5.44 → 5.39 → 5.42 → 5.40 → 5.46 → 5.47.
- **Absolutos en un compacto (interior + frontera):** 5.41 → 5.43 → 5.48.
- **Optimización reducida a una variable:** 5.45.

---

### Ejercicio 5.28 (E p. 191)

> ¿Alcanza la función $f(x,y)=y^2x^2+y^2+4\,\mathrm{sen}^2x$ los valores mínimo y máximo absolutos en $\mathbb{R}^2$?

**Antes de calcular**
- *Qué me piden:* decidir si existe un punto donde $f$ es la menor de todas y otro donde es la mayor.
- *Cómo lo pienso:* los tres sumandos son cuadrados (o múltiplos positivos de cuadrados): $f\ge0$. Si llega a valer $0$, ese es el mínimo. Para el máximo, buscar una recta por la que $f$ crezca sin límite.
- *Qué uso:* Def. 5.7-5.8 de máximo y mínimo absoluto (U p. 213).
- *Por dónde empiezo:* ver cuándo vale $0$ cada sumando.

1. **Signo:** $y^2x^2\ge0$, $y^2\ge0$, $4\,\mathrm{sen}^2x\ge0$. Luego $f(x,y)\ge0$ para todo $(x,y)$.
2. **¿Cuándo vale $0$?** Una suma de números $\ge0$ es $0$ solo si cada sumando es $0$: $y^2=0\Rightarrow y=0$; $\mathrm{sen}\,x=0\Rightarrow x=k\pi$, $k\in\mathbb{Z}$ (el primer sumando ya es $0$ con $y=0$).
3. **Mínimo absoluto:** $f(k\pi,0)=0\le f(x,y)$ para todo $(x,y)$: por la Def. 5.8, $f$ alcanza el mínimo absoluto $0$ en todos los puntos $(k\pi,0)$, $k\in\mathbb{Z}$ (infinitos puntos).
4. **Máximo absoluto:** sobre el eje $x=0$, $f(0,y)=y^2$, que supera cualquier número $M$ (basta $y=\sqrt{M}+1$). Si hubiera máximo $f(a,b)$, tomando $M=f(a,b)$ habría un punto con valor mayor: contradicción. **No hay máximo absoluto.**

**Receta.** Antes de derivar, mirar el signo: si $f\ge0$ y se anula en algún punto, ahí está el mínimo absoluto. Para negar el máximo, encontrar una recta en la que $f\to+\infty$.

**Error típico.** Concluir «no hay máximo porque $\mathbb{R}^2$ no es acotado»: el teorema de los valores extremos da una condición **suficiente**; si no se cumple, no se puede concluir nada sin más (p. ej. $e^{-x^2-y^2}$ sí tiene máximo en $\mathbb{R}^2$).

---

### Ejercicio 5.38 (E p. 200)

> La función $f(x,y)=x^2y$ está definida sobre el conjunto $S=\{(x,y)\in\mathbb{R}^2:x^2+y^2\le1\}$. ¿Alcanza el máximo absoluto en este conjunto? Justifica la respuesta.

**Antes de calcular**
- *Qué me piden:* solo **si existe** el máximo, no cuánto vale.
- *Cómo lo pienso:* es exactamente la situación del teorema de los valores extremos: función continua sobre un disco cerrado.
- *Qué uso:* teorema de los valores extremos (U p. 222).
- *Por dónde empiezo:* comprobar las tres hipótesis.

1. **$f$ es continua:** es un polinomio.
2. **$S$ es cerrado:** contiene su frontera, la circunferencia $x^2+y^2=1$ (el «$\le$» la incluye).
3. **$S$ es acotado:** está dentro del disco de radio $1$ (todo punto cumple $\|(x,y)\|\le1$).
4. Por el teorema de los valores extremos, **sí**: $f$ alcanza en $S$ el máximo y el mínimo absolutos.

**Para ir más allá (no se pide):** en el interior, $\nabla f=(2xy,x^2)=\bar0$ solo en $x=0$, donde $f=0$. En la frontera, $x^2=1-y^2$ y $f=(1-y^2)y$; su derivada $1-3y^2$ se anula en $y=\pm\frac1{\sqrt3}$. El máximo es $f=\frac23\cdot\frac{1}{\sqrt3}=\frac{2\sqrt3}{9}$ en $\left(\pm\sqrt{2/3},\,1/\sqrt3\right)$ y el mínimo $-\frac{2\sqrt3}9$ en $\left(\pm\sqrt{2/3},\,-1/\sqrt3\right)$ (sympy).

**Receta.** «¿Alcanza…?» en un conjunto ⇒ comprobar continua + cerrado + acotado y citar el teorema.

**Error típico.** Contestar calculando puntos críticos del interior y decir «no hay máximo porque en el interior no hay extremos»: el máximo puede estar en la frontera.

---

### Ejercicio 5.33 (E p. 195)

> La función de dos variables dada por $f(x,y)=x^2\,\mathrm{sen}^2y$ verifica:
> a) Alcanza en $(0,0)$ un mínimo relativo. b) Alcanza en $(0,0)$ un máximo relativo. c) Tiene en $(0,0)$ un punto de silla. d) Ninguna de las opciones anteriores.

**Antes de calcular**
- *Qué me piden:* qué tipo de punto es $(0,0)$.
- *Cómo lo pienso:* la Hessiana puede no decidir (todo es «muy plano» en el origen); pero $f$ es un producto de cuadrados: nunca es negativa.
- *Qué uso:* condición suficiente (U p. 220); si es dudosa, la Def. 5.11 de mínimo relativo (U p. 214).
- *Por dónde empiezo:* comprobar que $(0,0)$ es crítico.

1. **Gradiente:** $f_x=2x\,\mathrm{sen}^2y$, $f_y=2x^2\,\mathrm{sen}\,y\cos y=x^2\,\mathrm{sen}\,2y$. En $(0,0)$ ambas valen $0$: es punto crítico.
2. **Hessiana:** $Hf(x,y)=\begin{pmatrix}2\,\mathrm{sen}^2y & 4x\,\mathrm{sen}\,y\cos y\\ 4x\,\mathrm{sen}\,y\cos y & 2x^2\cos 2y\end{pmatrix}$; en $(0,0)$ es la matriz nula, $d=0$: **caso dudoso**, el criterio no dice nada.
3. **Mirar el signo:** $f(0,0)=0$ y $f(x,y)=x^2\,\mathrm{sen}^2y\ge0$ siempre (producto de dos cuadrados).
4. Entonces $f(x,y)\ge f(0,0)$ para todo $(x,y)$: mínimo absoluto, y por tanto relativo. **Respuesta a).**

**Receta.** Si $d=0$, comparar $f(x,y)$ con $f(a,b)$ cerca del punto: si $f-f(a,b)\ge0$ es mínimo; si $\le0$, máximo; si toma los dos signos, silla.

**Error típico.** Elegir d) («no se puede saber») porque la Hessiana es nula. «Dudoso» significa que **el criterio** no decide, no que el punto no sea extremo.

---

### Ejercicio 5.29 (E pp. 191-192)

> Localiza los puntos en los que la función dada por $f(x,y)=x^3+y^3+xy$ puede alcanzar los extremos relativos.

**Antes de calcular**
- *Qué me piden:* los candidatos, es decir, los puntos críticos (no clasificarlos).
- *Cómo lo pienso:* $f$ es un polinomio, diferenciable en todo $\mathbb{R}^2$ (abierto): los extremos relativos solo pueden estar donde $\nabla f=\bar0$.
- *Qué uso:* condición necesaria de extremo (U p. 218).
- *Por dónde empiezo:* despejar $y$ en $f_x=0$, que queda «limpio».

1. $f_x=3x^2+y$, $f_y=3y^2+x$. Sistema: $3x^2+y=0$, $3y^2+x=0$.
2. De la 1ª, $y=-3x^2$. Se sustituye en la 2ª: $3\cdot9x^4+x=0\iff x(27x^3+1)=0$.
3. Producto nulo: $x=0$ o $27x^3=-1\iff x^3=-\frac1{27}\iff x=-\frac13$ (raíz cúbica real única).
4. Se vuelve a $y=-3x^2$: $x=0\Rightarrow y=0$; $x=-\frac13\Rightarrow y=-3\cdot\frac19=-\frac13$.
5. **Puntos críticos:** $(0,0)$ y $\left(-\frac13,-\frac13\right)$.

**Para ir más allá:** $Hf=\begin{pmatrix}6x&1\\1&6y\end{pmatrix}$; en $(0,0)$, $d=-1$: silla; en $\left(-\frac13,-\frac13\right)$, $d=4-1=3>0$, $r=-2<0$: máximo relativo.

**Receta.** Sistema polinómico: despejar en la ecuación más sencilla, sustituir, factorizar la ecuación de una variable y volver atrás con cada raíz.

**Error típico.** Dividir entre $x$ en $27x^4+x=0$ y perder la solución $x=0$.

---

### Ejercicio 5.30 (E pp. 192-193)

> Determina los puntos críticos de la función dada por $f(x,y)=xy\,(x^2+y^2)$.

**Antes de calcular**
- *Qué me piden:* los puntos con $\nabla f=\bar0$.
- *Cómo lo pienso:* las dos derivadas salen con un factor $y$ y otro $x$; lo que queda son sumas de cuadrados, que solo se anulan en el origen.
- *Qué uso:* Def. 5.13 (U p. 216).
- *Por dónde empiezo:* desarrollar $f=x^3y+xy^3$ y derivar.

1. $f=x^3y+xy^3$, así que $f_x=3x^2y+y^3=y(3x^2+y^2)$ y $f_y=x^3+3xy^2=x(x^2+3y^2)$.
2. **Si $x=0$:** la 1ª queda $y\cdot y^2=y^3=0$, luego $y=0$.
3. **Si $y=0$:** la 2ª queda $x^3=0$, luego $x=0$.
4. **Si $x\ne0$ e $y\ne0$:** tendría que ser $3x^2+y^2=0$, pero es suma de cuadrados con $x\ne0$: es $>0$. Imposible.
5. **Único punto crítico: $(0,0)$.**

**Para entenderlo:** $f(0,0)=0$ y $f$ tiene el signo de $xy$: positiva en el 1.er y 3.er cuadrantes y negativa en los otros dos. Es un punto de silla (la Hessiana es nula: el criterio no decide; se ve por el signo).

**Receta.** Sacar factor común y separar casos; «suma de cuadrados $=0$» solo si cada uno es $0$.

**Error típico.** Olvidar algún caso o dar por soluciones $(x,0)$ sin comprobar la otra ecuación.

---

### Ejercicio 5.35 (E pp. 197-198)

> Sea $f:\mathbb{R}^2\to\mathbb{R}$, $f(x,y)=x(1-\cos y)+y(1-\cos x)+xy$. Calcula $\nabla f(\pi,0)$; ¿es $(\pi,0)$ un punto crítico? Estudia si en $(0,0)$ la función $f$ alcanza un extremo relativo.

**Antes de calcular**
- *Qué me piden:* un gradiente en un punto, y clasificar el origen.
- *Cómo lo pienso:* el origen será crítico; la Hessiana dirá su tipo. El término $xy$ (silla clásica) hace sospechar que es silla.
- *Qué uso:* Def. 5.13 (U p. 216) y condición suficiente (U p. 220).
- *Por dónde empiezo:* derivar término a término.

1. $f_x=(1-\cos y)+y\,\mathrm{sen}\,x+y$, $\quad f_y=x\,\mathrm{sen}\,y+(1-\cos x)+x$.
2. **En $(\pi,0)$:** $f_x=0+0+0=0$; $f_y=0+(1-\cos\pi)+\pi=2+\pi$. $\nabla f(\pi,0)=(0,\,2+\pi)\ne\bar0$: **no es crítico**.
3. **En $(0,0)$:** $f_x=0$, $f_y=0$: sí es crítico.
4. **Derivadas segundas:** $f_{xx}=y\cos x$, $f_{xy}=\mathrm{sen}\,y+\mathrm{sen}\,x+1$, $f_{yy}=x\cos y$. En $(0,0)$: $Hf(0,0)=\begin{pmatrix}0&1\\1&0\end{pmatrix}$.
5. $d=0\cdot0-1\cdot1=-1<0$: **punto de silla**, no hay extremo relativo en $(0,0)$.

**Para entenderlo:** cerca del origen $1-\cos t\approx\frac{t^2}{2}$, así que $f\approx xy$: positiva en la diagonal $y=x$ y negativa en $y=-x$.

**Receta.** Si $d<0$ ya no hace falta mirar $r$: silla.

**Error típico.** Ver $r=0$ y decir «caso dudoso». Lo primero es mirar $d$: si $d<0$ es silla, valga lo que valga $r$.

---

### Ejercicio 5.31 (E pp. 193-194)

> Sea $f(x,y)=x^3+y^2-xy$. Estudia si la función alcanza sus extremos relativos en los puntos $(0,0)$, $(1,-1)$ y $\left(\frac16,\frac1{12}\right)$ y, en caso de que así sea, razona si son máximos o mínimos. ¿Es alguno de estos puntos un extremo absoluto de $f$ en $\mathbb{R}^2$? ¿Se alcanzan en $\mathbb{R}^2$ extremos absolutos?

**Antes de calcular**
- *Qué me piden:* (1) cuáles de los tres puntos son críticos; (2) clasificarlos; (3) decidir si hay extremos absolutos.
- *Cómo lo pienso:* un punto no crítico no puede ser extremo (condición necesaria). A los críticos, Hessiana. Para lo absoluto: un $x^3$ «suelto» hace que $f$ no esté acotada.
- *Qué uso:* condición necesaria (U p. 218), condición suficiente (U p. 220), Def. 5.7-5.8 (U p. 213).
- *Por dónde empiezo:* hallar todos los puntos críticos.

1. $f_x=3x^2-y$, $f_y=2y-x$.
2. De $f_y=0$: $x=2y$. En $f_x=0$: $12y^2-y=y(12y-1)=0$, $y=0$ o $y=\frac1{12}$. Puntos críticos: $(0,0)$ y $\left(\frac16,\frac1{12}\right)$.
3. **$(1,-1)$:** $\nabla f(1,-1)=(3+1,\,-2-1)=(4,-3)\ne\bar0$. Por la condición necesaria, **no es extremo relativo**.
4. **Hessiana:** $f_{xx}=6x$, $f_{xy}=-1$, $f_{yy}=2$.
5. **$(0,0)$:** $Hf=\begin{pmatrix}0&-1\\-1&2\end{pmatrix}$, $d=-1<0$: **silla**.
6. **$\left(\frac16,\frac1{12}\right)$:** $Hf=\begin{pmatrix}1&-1\\-1&2\end{pmatrix}$, $d=2-1=1>0$ y $r=1>0$: **mínimo relativo**, con $f=\frac1{216}+\frac1{144}-\frac1{72}=-\frac1{432}$.
7. **¿Absoluto?** $f(-1,0)=-1<-\frac1{432}$: hay un valor menor, así que el mínimo relativo no es absoluto.
8. **Sin extremos absolutos:** sobre el eje $y=0$, $f(x,0)=x^3$, que toma valores tan grandes y tan negativos como se quiera ($x\to\pm\infty$). Ningún valor puede ser el mayor ni el menor.

**Receta.** «¿Es extremo en estos puntos?» ⇒ primero gradiente en cada punto (descartar los no críticos), después Hessiana. «¿Absoluto?» ⇒ buscar un punto con valor mejor, o una recta donde $f$ no esté acotada.

**Error típico.** Clasificar $(1,-1)$ con la Hessiana sin comprobar que es crítico: el criterio solo vale en puntos críticos.

---

### Ejercicio 5.32 (E pp. 194-195)

> Determina los puntos críticos, y estudia si se alcanza algún extremo en ellos, para la función dada por $f(x,y)=y+x^2y^2-x^2+y^2$.

**Antes de calcular**
- *Qué me piden:* críticos y su clasificación.
- *Cómo lo pienso:* $f_x$ factoriza como $2x(y^2-1)$: dos casos, $x=0$ o $y=\pm1$; cada uno se lleva a $f_y=0$.
- *Qué uso:* Def. 5.13 (U p. 216), condición suficiente (U p. 220).
- *Por dónde empiezo:* derivar y sacar factor común.

1. $f_x=2xy^2-2x=2x(y^2-1)$, $\quad f_y=1+2x^2y+2y=1+2y(x^2+1)$.
2. **Caso $x=0$:** $f_y=1+2y=0\Rightarrow y=-\frac12$. Punto $\left(0,-\frac12\right)$.
3. **Caso $y=1$:** $f_y=1+2(x^2+1)\ge3>0$: sin solución.
4. **Caso $y=-1$:** $f_y=1-2(x^2+1)=-1-2x^2\le-1<0$: sin solución.
5. Único crítico: $\left(0,-\frac12\right)$.
6. **Hessiana:** $f_{xx}=2y^2-2$, $f_{xy}=4xy$, $f_{yy}=2x^2+2$. En el punto: $f_{xx}=\frac12-2=-\frac32$, $f_{xy}=0$, $f_{yy}=2$.
7. $d=-\frac32\cdot2-0=-3<0$: **punto de silla**; $f$ no alcanza extremos relativos.

**Receta.** Factorizar la derivada más sencilla y llevar cada caso a la otra ecuación; si en un caso la otra ecuación es «positivo $=0$», ese caso no da puntos.

**Error típico.** Olvidar que $y^2=1$ da **dos** casos ($y=1$ e $y=-1$).

---

### Ejercicio 5.37 (E pp. 199-200)

> Se quieren instalar tres segmentos de cable que conecten cada uno de los puntos $A=(0,0)$, $B=(4,0)$ y $C=(1,3)$ con un punto $P=(x,y)$. Los segmentos tienen longitudes $d_1$, $d_2$ y $d_3$, respectivamente. Se busca que la suma de las tres longitudes al cuadrado, $d_1^2+d_2^2+d_3^2$, sea mínima. ¿Cuáles son las coordenadas de $P$?

**Antes de calcular**
- *Qué me piden:* el punto $P$ que minimiza una función de dos variables.
- *Cómo lo pienso:* al elevar al cuadrado desaparecen las raíces: queda un polinomio de grado 2 («paraboloide»), con un único mínimo.
- *Qué uso:* puntos críticos (U p. 216) y Hessiana (U p. 220).
- *Por dónde empiezo:* escribir $f(x,y)$ con la fórmula de la distancia.

1. $d_1^2=x^2+y^2$, $d_2^2=(x-4)^2+y^2$, $d_3^2=(x-1)^2+(y-3)^2$.
2. Suma: $f(x,y)=3x^2+3y^2-10x-6y+26$.
3. $f_x=6x-10=0\Rightarrow x=\frac53$; $f_y=6y-6=0\Rightarrow y=1$.
4. $Hf=\begin{pmatrix}6&0\\0&6\end{pmatrix}$ en todo punto: $d=36>0$, $r=6>0$: **mínimo**. $P=\left(\frac53,1\right)$, con $f=\frac{44}3$.

**Para entenderlo:** $\left(\frac53,1\right)=\left(\frac{0+4+1}3,\frac{0+0+3}3\right)$ es el **baricentro** del triángulo $ABC$. Además, como $f=3\left(x-\frac53\right)^2+3(y-1)^2+\frac{44}{3}$, el mínimo es absoluto.

**Receta.** Problema geométrico: escribir la magnitud en función de las coordenadas, simplificar (cuadrados en lugar de raíces) y aplicar crítico + Hessiana.

**Error típico.** Minimizar $d_1+d_2+d_3$ (con raíces) en lugar de la suma de cuadrados que pide el enunciado.

---

### Ejercicio 5.36 (E pp. 198-199)

> Se van a introducir dos tipos de componentes electrónicos en el mercado, A y B. Si $x$ es el precio de A e $y$ el de B, durante el primer mes se venderán $12-4x+3y$ miles de unidades de A y $15+x-10y$ miles de unidades de B. Si el precio de fabricación de A es 1 euro y el de B es 0.9 euros, ¿qué precio deberían tener para maximizar las ganancias?

**Antes de calcular**
- *Qué me piden:* los precios $(x,y)$ que hacen máxima la ganancia.
- *Cómo lo pienso:* ganancia = (beneficio por unidad) × (unidades vendidas), sumado en A y B. Sale un polinomio de grado 2 con un solo punto crítico.
- *Qué uso:* puntos críticos (U p. 216) y Hessiana (U p. 220).
- *Por dónde empiezo:* escribir la función ganancia.

1. **Modelo:** beneficio por unidad $x-1$ (A) e $y-0.9$ (B). Ganancia (en miles de euros):
$f(x,y)=(x-1)(12-4x+3y)+(y-0.9)(15+x-10y)=-4x^2+4xy-10y^2+15.1x+21y-25.5$.
2. $f_x=15.1-8x+4y$, $\quad f_y=4x+21-20y$.
3. De $f_y=0$: $x=5y-\frac{21}4$. En $f_x=0$: $15.1-40y+42+4y=0\iff57.1=36y\iff y=\frac{571}{360}\approx1.5861$.
4. $x=5\cdot\frac{571}{360}-\frac{21}{4}=\frac{193}{72}\approx2.6806$.
5. **Hessiana** (constante): $\begin{pmatrix}-8&4\\4&-20\end{pmatrix}$, $d=160-16=144>0$, $r=-8<0$: **máximo**.
6. **Respuesta:** A a $2.68$ € y B a $1.59$ € (ganancia $\approx11.39$ miles de euros, sympy).

**Receta.** Problemas de economía: escribir «beneficio unitario × cantidad», desarrollar, y crítico + Hessiana. Con un polinomio de grado 2 la Hessiana es constante.

**Error típico.** Tomar como ganancia «precio × cantidad» (ingresos) sin restar el coste de fabricación.

---

### Ejercicio 5.34 (E pp. 196-197)

> Para la función $f(x,y)=\dfrac{x^2+3y^2}{(x^2+y^2+1)^2}$ calcula:
> a) La ecuación del plano tangente a la gráfica de $f$ en el punto $(-1,0,f(-1,0))$.
> b) Los puntos críticos de la función.
> c) La expresión de la función en coordenadas polares.

**Antes de calcular**
- *Qué me piden:* un plano tangente, los puntos críticos y un cambio a polares.
- *Cómo lo pienso:* las derivadas de un cociente llevan un denominador siempre positivo; los críticos salen del numerador, por casos. Si el gradiente es nulo en $(-1,0)$, el plano tangente es horizontal.
- *Qué uso:* plano tangente (U (5.2), p. 189); Def. 5.13 (U p. 216).
- *Por dónde empiezo:* derivar con la regla del cociente y simplificar el factor $(x^2+y^2+1)$.

1. **Derivadas** (cociente; se simplifica un factor $x^2+y^2+1$):
$f_x=\dfrac{x\,(2-2x^2-10y^2)}{(x^2+y^2+1)^3}$, $\quad f_y=\dfrac{2y\,(3+x^2-3y^2)}{(x^2+y^2+1)^3}$.
2. **a)** $f(-1,0)=\frac{1}{4}$; $f_x(-1,0)=\frac{-1\cdot0}{8}=0$, $f_y(-1,0)=0$. Plano: $z=\frac14+0\cdot(x+1)+0\cdot y$, es decir **$z=\frac14$**.
3. **b)** El denominador es $>0$: hay que resolver $x(2-2x^2-10y^2)=0$ y $y(3+x^2-3y^2)=0$.
   - $x=0$: la 2ª da $y=0$ o $3=3y^2$: $(0,0)$, $(0,\pm1)$.
   - $y=0$: la 1ª da $x=0$ o $2=2x^2$: $(\pm1,0)$.
   - $x\ne0$, $y\ne0$: $x^2+5y^2=1$ y $x^2-3y^2=-3$; restando, $8y^2=4$, $y^2=\frac12$, y entonces $x^2=1-\frac52<0$: imposible.
   - **Críticos:** $(0,0)$, $(\pm1,0)$, $(0,\pm1)$.
4. **c)** Con $x=\rho\cos\theta$, $y=\rho\,\mathrm{sen}\,\theta$: $x^2+y^2=\rho^2$ y $x^2+3y^2=\rho^2+2\rho^2\mathrm{sen}^2\theta$. Luego $f=\dfrac{\rho^2\,(1+2\,\mathrm{sen}^2\theta)}{(\rho^2+1)^2}$.

**Para ir más allá (sympy):** $Hf(0,0)=\mathrm{diag}(2,6)$: mínimo ($f=0$); $Hf(\pm1,0)=\mathrm{diag}\!\left(-\frac12,1\right)$: silla; $Hf(0,\pm1)=\mathrm{diag}\!\left(-1,-\frac32\right)$: máximo ($f=\frac34$). El punto $(-1,0)$ del apartado a) es crítico; por eso el plano tangente es horizontal.

**Receta.** Plano tangente horizontal ⇔ punto crítico. En un cociente, los críticos son los ceros del numerador de las derivadas.

**Error típico.** No simplificar el factor común del denominador y perderse en el sistema.

---

### Ejercicio 5.44 (E p. 206)

> Sea $f(x,y)=x^2+y$. Calcula mediante el método de los multiplicadores de Lagrange los puntos críticos de $f$ cuando nos restringimos a los $(x,y)$ tales que $2x-y=0$.

**Antes de calcular**
- *Qué me piden:* los puntos críticos condicionados (candidatos) de $f$ sobre la recta $y=2x$.
- *Cómo lo pienso:* se construye $F=f+\lambda g$ y se buscan sus puntos críticos; el sistema es lineal.
- *Qué uso:* teorema y método de Lagrange (U pp. 226 y 228).
- *Por dónde empiezo:* $g(x,y)=2x-y$, $F=x^2+y+\lambda(2x-y)$.

1. $\nabla g=(2,-1)\ne\bar0$ en todo punto: el teorema se puede aplicar en toda la recta.
2. $F_x=2x+2\lambda=0$, $F_y=1-\lambda=0$, $F_\lambda=2x-y=0$.
3. De la 2ª, $\lambda=1$. En la 1ª, $x=-1$. En la 3ª, $y=-2$.
4. **Único punto crítico: $(-1,-2)$** ($\lambda=1$).

**Para entenderlo (comprobación despejando, U p. 228 paso 4):** sobre la recta $y=2x$, $f(x,2x)=x^2+2x=(x+1)^2-1$, que tiene mínimo $-1$ en $x=-1$ y no tiene máximo. Así que $(-1,-2)$ es el **mínimo condicionado** (absoluto sobre la recta).

**Receta.** Lagrange con una restricción lineal: el sistema suele resolverse empezando por la ecuación que da $\lambda$ directamente.

**Error típico.** Olvidar la tercera ecuación ($g=0$) y quedarse con una recta de soluciones.

---

### Ejercicio 5.39 (E p. 201)

> Sea $f(x,y)=x^2-y^2$ y el conjunto $C=\{(x,y):x+y=0\}$. Discute la veracidad de las siguientes afirmaciones relativas a $f$ y la restricción dada por $C$:
> a) En $(1,-1)$ se alcanza un mínimo condicionado. b) En $(1,-1)$ se alcanza un máximo condicionado. c) En $(1,-1)$ hay un punto de silla. d) Ninguna de las anteriores.

**Antes de calcular**
- *Qué me piden:* qué tipo de punto es $(1,-1)$ para $f$ restringida a la recta $y=-x$.
- *Cómo lo pienso:* sobre esa recta $x^2=y^2$: $f$ vale siempre $0$. Una función constante tiene máximo y mínimo en todos sus puntos.
- *Qué uso:* método de Lagrange (U p. 228) y Def. 5.10-5.11 (U p. 214) aplicadas sobre $C$.
- *Por dónde empiezo:* comprobar que $(1,-1)$ es crítico de $F$.

1. $F=x^2-y^2+\lambda(x+y)$: $F_x=2x+\lambda$, $F_y=-2y+\lambda$, $F_\lambda=x+y$.
2. En $(1,-1)$: $2+\lambda=0$ y $2+\lambda=0$ con $\lambda=-2$; $x+y=0$ ✓. Es punto crítico condicionado (de hecho todos los puntos de $C$ lo son, con $\lambda=-2x$).
3. **Sobre $C$:** $f(x,-x)=x^2-x^2=0$. $f$ es constante en $C$.
4. Entonces $f(x,y)\le f(1,-1)$ **y** $f(x,y)\ge f(1,-1)$ para todo $(x,y)\in C$: hay **a la vez** mínimo y máximo condicionado. **Verdaderas a) y b)**; c) y d) falsas.

**Receta.** Si la restricción permite sustituir ($y=-x$), sustituir y estudiar la función de una variable: ahí se ve la naturaleza del punto.

**Error típico.** Responder c) porque $x^2-y^2$ tiene una silla en el plano: la pregunta es sobre la recta, no sobre todo $\mathbb{R}^2$.

---

### Ejercicio 5.42 (E pp. 203-204)

> Sabiendo que la función $f(x,y)=x-y$ alcanza en el conjunto $S=\{(x,y)\in\mathbb{R}^2:x^2+y^2=1\}$ extremos absolutos condicionados, determina en qué puntos los alcanza.

**Antes de calcular**
- *Qué me piden:* dónde está el máximo y dónde el mínimo de $x-y$ en la circunferencia unidad.
- *Cómo lo pienso:* se sabe que existen (la circunferencia es cerrada y acotada). Lagrange da pocos candidatos; se comparan valores.
- *Qué uso:* método de Lagrange (U p. 228).
- *Por dónde empiezo:* $F=x-y+\lambda(x^2+y^2-1)$.

1. $\nabla g=(2x,2y)\ne\bar0$ en la circunferencia (solo se anula en el origen, que no está en ella).
2. $F_x=1+2\lambda x=0$, $F_y=-1+2\lambda y=0$, $x^2+y^2=1$.
3. $\lambda\ne0$ (si no, $1=0$). Despejando: $x=-\frac{1}{2\lambda}$, $y=\frac1{2\lambda}$.
4. En la restricción: $\frac{1}{4\lambda^2}+\frac1{4\lambda^2}=1\iff\lambda^2=\frac12\iff\lambda=\pm\frac{\sqrt2}2$.
5. $\lambda=-\frac{\sqrt2}2$: $\left(\frac{\sqrt2}2,-\frac{\sqrt2}2\right)$, $f=\sqrt2$. $\quad\lambda=\frac{\sqrt2}2$: $\left(-\frac{\sqrt2}2,\frac{\sqrt2}2\right)$, $f=-\sqrt2$.
6. **Máximo $\sqrt2$ en $\left(\frac{\sqrt2}2,-\frac{\sqrt2}2\right)$; mínimo $-\sqrt2$ en $\left(-\frac{\sqrt2}2,\frac{\sqrt2}2\right)$.**

**Para entenderlo:** las rectas $x-y=c$ (curvas de nivel) son paralelas; las extremas que tocan la circunferencia son tangentes a ella (U Fig. 5.13, p. 227).

**Receta.** Con $f$ lineal: despejar $x$ e $y$ en función de $\lambda$, meterlos en la restricción para hallar $\lambda$ y volver.

**Error típico.** Dividir por $\lambda$ sin comprobar antes que $\lambda\ne0$.

---

### Ejercicio 5.40 (E pp. 202-203)

> Utilizando el método de los multiplicadores de Lagrange, calcula las dimensiones de una lata cilíndrica cerrada (con ambas tapas) de volumen 300 ml candidatas a maximizar o minimizar su superficie.

**Antes de calcular**
- *Qué me piden:* radio $r$ y altura $h$ candidatos a extremo de la superficie con volumen fijo.
- *Cómo lo pienso:* función a optimizar = superficie; restricción = volumen. Las dos tapas son círculos, el lateral un rectángulo de base $2\pi r$.
- *Qué uso:* método de Lagrange (U p. 228); para clasificar, una variable (U §3.4).
- *Por dónde empiezo:* $f(r,h)=2\pi r^2+2\pi rh$, $g(r,h)=\pi r^2h-300$, con $r,h>0$.

1. $F=2\pi r^2+2\pi rh+\lambda(\pi r^2h-300)$.
2. $F_r=4\pi r+2\pi h+2\lambda\pi rh=0$; $F_h=2\pi r+\lambda\pi r^2=0$; $F_\lambda=\pi r^2h-300=0$.
3. Como $r>0$, se divide la 2ª entre $\pi r$: $2+\lambda r=0$, $\lambda=-\frac2r$.
4. La 1ª, dividida entre $2\pi$: $2r+h+\lambda rh=0$. Con $\lambda r=-2$: $2r+h-2h=0$, es decir **$h=2r$** (la altura es igual al diámetro).
5. En la restricción: $\pi r^2\cdot2r=300\iff r^3=\frac{150}\pi\iff r=\sqrt[3]{150/\pi}\approx3.628$ cm, y $h=2r\approx7.256$ cm.
6. **¿Máximo o mínimo?** Despejando $h=\frac{300}{\pi r^2}$: $A(r)=2\pi r^2+\frac{600}{r}$, $r>0$. $A'(r)=4\pi r-\frac{600}{r^2}=0\iff r^3=\frac{150}{\pi}$ (el mismo punto), y $A''(r)=4\pi+\frac{1200}{r^3}>0$: **mínimo**. Superficie mínima $\approx248.08$ cm². No hay máximo: $A(r)\to+\infty$ si $r\to0^+$ o $r\to+\infty$.

**Receta.** Optimización geométrica con una ligadura: $f$ = lo que se optimiza, $g$ = la condición fija; usar que las variables son positivas para dividir. Para clasificar, despejar y pasar a una variable.

**Error típico.** Olvidar una de las dos tapas ($\pi r^2$ en lugar de $2\pi r^2$), o creer que Lagrange dice por sí solo si es máximo o mínimo (la restricción aquí no es acotada).

---

### Ejercicio 5.46 (E pp. 208-209)

> Halla los puntos críticos de la función $f:\mathbb{R}^3\to\mathbb{R}$ dada por $f(x,y,z)=x+y+z$, sujetos a la condición $x^2+2y^2+3z^2=1$. ¿Puedes determinar si en alguno de ellos se alcanza un extremo absoluto condicionado?

**Antes de calcular**
- *Qué me piden:* candidatos de Lagrange en $\mathbb{R}^3$ y si son máximo/mínimo absoluto.
- *Cómo lo pienso:* como en 5.42 pero con tres variables: cada coordenada se despeja en función de $\lambda$. La restricción es un elipsoide: cerrado y acotado.
- *Qué uso:* Lagrange en $\mathbb{R}^n$ (U p. 228) y teorema de los valores extremos (U p. 222).
- *Por dónde empiezo:* $F=x+y+z+\lambda(x^2+2y^2+3z^2-1)$.

1. $\nabla g=(2x,4y,6z)\ne\bar0$ en el elipsoide (solo se anula en el origen).
2. $F_x=1+2\lambda x=0$, $F_y=1+4\lambda y=0$, $F_z=1+6\lambda z=0$, $x^2+2y^2+3z^2=1$.
3. $\lambda\ne0$ (si no, $1=0$): $x=-\frac1{2\lambda}$, $y=-\frac1{4\lambda}$, $z=-\frac1{6\lambda}$.
4. En la restricción: $\frac1{4\lambda^2}+\frac2{16\lambda^2}+\frac3{36\lambda^2}=\frac{1}{\lambda^2}\left(\frac14+\frac18+\frac1{12}\right)=\frac{11}{24\lambda^2}=1$, luego $\lambda=\pm\sqrt{\frac{11}{24}}=\pm\frac{\sqrt{66}}{12}$.
5. $\lambda=-\frac{\sqrt{66}}{12}$: $P_1=\left(\frac{\sqrt{66}}{11},\frac{\sqrt{66}}{22},\frac{\sqrt{66}}{33}\right)$, $f(P_1)=\sqrt{66}\left(\frac{6+3+2}{66}\right)=\frac{\sqrt{66}}{6}\approx1.354$.
   $\lambda=+\frac{\sqrt{66}}{12}$: $P_2=-P_1$, $f(P_2)=-\frac{\sqrt{66}}6$.
6. El elipsoide es cerrado y acotado y $f$ es continua: hay máximo y mínimo absolutos, y están entre los candidatos. **Máximo $\frac{\sqrt{66}}6$ en $P_1$; mínimo $-\frac{\sqrt{66}}6$ en $P_2$.**

**Receta.** Lagrange en $\mathbb{R}^3$: igual que en $\mathbb{R}^2$, con una ecuación más. Si la restricción es una superficie cerrada y acotada (esfera, elipsoide), basta comparar valores.

**Error típico.** Errores de fracciones al sustituir: conviene sacar $\frac1{\lambda^2}$ factor común antes de sumar.

---

### Ejercicio 5.47 (E pp. 209-211)

> Sabiendo que hay una distancia mínima entre el punto $(0,0,0)$ y la superficie dada por $z=xy+4$, determínala.

**Antes de calcular**
- *Qué me piden:* la menor distancia del origen a los puntos de la superficie.
- *Cómo lo pienso:* minimizar la distancia es lo mismo que minimizar su cuadrado ($t\mapsto t^2$ es creciente para $t\ge0$), que no tiene raíz. Restricción: estar en la superficie.
- *Qué uso:* Lagrange en $\mathbb{R}^3$ (U p. 228).
- *Por dónde empiezo:* $f=x^2+y^2+z^2$, $g=xy+4-z$.

1. $\nabla g=(y,x,-1)$: nunca es nulo (tercera componente $-1$).
2. $F=x^2+y^2+z^2+\lambda(xy+4-z)$: $2x+\lambda y=0$, $2y+\lambda x=0$, $2z-\lambda=0$, $xy+4-z=0$.
3. **Caso $x=0$:** la 1ª da $\lambda y=0$, la 2ª $2y=0$, luego $y=0$; la 4ª, $z=4$; $\lambda=8$. Punto $(0,0,4)$, $f=16$.
4. **Caso $x\ne0$:** de la 2ª, $y=-\frac{\lambda x}{2}$; en la 1ª: $2x-\frac{\lambda^2x}{2}=0$, y dividiendo entre $x\ne0$: $\lambda^2=4$.
   - $\lambda=2$: $y=-x$, $z=1$; la 4ª: $-x^2+4-1=0$, $x=\pm\sqrt3$. Puntos $(\sqrt3,-\sqrt3,1)$ y $(-\sqrt3,\sqrt3,1)$, $f=3+3+1=7$.
   - $\lambda=-2$: $y=x$, $z=-1$; la 4ª: $x^2+5=0$: sin solución real.
5. Se sabe que hay mínimo y está entre los candidatos: el menor valor de $f$ es $7$. **Distancia mínima $\sqrt7$**, en $(\sqrt3,-\sqrt3,1)$ y $(-\sqrt3,\sqrt3,1)$.

**Receta.** Distancia de un punto a una curva o superficie: minimizar el **cuadrado** de la distancia con Lagrange; al final, sacar la raíz.

**Error típico.** Quedarse con $(0,0,4)$ porque «es el punto más cercano a la vista» (el más bajo sobre el eje $z$): hay puntos de la silla más cerca del origen. O dar $7$ como distancia en lugar de $\sqrt7$.

---

### Ejercicio 5.41 (E p. 203)

> Describe qué procedimiento seguirías para determinar los extremos absolutos de $f(x,y)=y^2\,\mathrm{sen}^2(x+y)-x^2$ en $x^2+y^2\le1$.

**Antes de calcular**
- *Qué me piden:* el **plan**, no las cuentas.
- *Cómo lo pienso:* disco cerrado y acotado + función continua ⇒ los extremos existen y están en el interior (puntos críticos) o en la circunferencia (Lagrange).
- *Qué uso:* teorema de los valores extremos y procedimiento (U p. 222), Lagrange (U p. 228).
- *Por dónde empiezo:* justificar la existencia.

1. **Existencia:** $f$ es continua (producto y composición de funciones elementales) y $S=\{x^2+y^2\le1\}$ es cerrado y acotado: por el teorema de los valores extremos, $f$ alcanza máximo y mínimo absolutos en $S$.
2. **Interior** $x^2+y^2<1$: resolver $f_x=0$, $f_y=0$ y quedarse con las soluciones del interior.
3. **Frontera** $x^2+y^2=1$: Lagrange con $F=f+\lambda(x^2+y^2-1)$ (o parametrizar $x=\cos t$, $y=\mathrm{sen}\,t$, $t\in[0,2\pi]$ y estudiar una función de una variable).
4. **Comparar:** evaluar $f$ en todos los candidatos; el mayor valor es el máximo absoluto y el menor, el mínimo.
5. **No hace falta la Hessiana**: no se trata de clasificar extremos relativos sino de comparar valores.

**Receta.** Ver la receta general: existencia → interior → frontera → tabla de valores.

**Error típico.** Calcular solo los puntos críticos del interior (olvidando la frontera), o clasificar con la Hessiana y dar un mínimo relativo como absoluto.

---

### Ejercicio 5.43 (E pp. 204-205)

> La temperatura de una placa circular de ecuación $x^2+y^2\le4$ está dada por la función $T(x,y)=e^{x^2}+e^{y^2}$. ¿Cuáles son la temperatura máxima y mínima que se alcanzan?

**Antes de calcular**
- *Qué me piden:* el máximo y el mínimo absolutos de $T$ en el disco de radio $2$.
- *Cómo lo pienso:* $e^{x^2}$ crece al alejarse $x$ de $0$, y $e^{y^2}$ igual con $y$: el mínimo estará en el centro. En el borde, como $e^{t}$ crece cada vez más deprisa, conviene «gastar» todo el radio en una sola variable: $e^{4}+e^{0}$.
- *Qué uso:* teorema de los valores extremos (U p. 222), Lagrange (U p. 228).
- *Por dónde empiezo:* puntos críticos del interior.

1. **Existencia:** $T$ continua, disco cerrado y acotado.
2. **Interior:** $T_x=2xe^{x^2}$, $T_y=2ye^{y^2}$. Como $e^{t}>0$: $x=0$, $y=0$. Candidato $(0,0)$, $T=2$.
3. **Frontera** con $F=e^{x^2}+e^{y^2}+\lambda(x^2+y^2-4)$:
$2x(e^{x^2}+\lambda)=0$, $\ 2y(e^{y^2}+\lambda)=0$, $\ x^2+y^2=4$.
   - $x=0$: $y^2=4$, puntos $(0,\pm2)$.
   - $y=0$: puntos $(\pm2,0)$.
   - $x\ne0$, $y\ne0$: $\lambda=-e^{x^2}=-e^{y^2}$, luego $e^{x^2}=e^{y^2}$, $x^2=y^2$ (la exponencial es inyectiva), y con $x^2+y^2=4$: $x^2=y^2=2$. Puntos $(\pm\sqrt2,\pm\sqrt2)$.
4. **Tabla:** $T(0,0)=2$; $T(0,\pm2)=T(\pm2,0)=1+e^4\approx55.60$; $T(\pm\sqrt2,\pm\sqrt2)=2e^2\approx14.78$.
5. **Mínimo $2$ en $(0,0)$; máximo $1+e^4$ en $(0,\pm2)$ y $(\pm2,0)$.**

**Receta.** Ver receta general. Al resolver Lagrange, «producto $=0$» da casos; en el caso «ningún factor simple es $0$», igualar las dos expresiones de $\lambda$.

**Error típico.** Olvidar los casos $x=0$ o $y=0$ al dividir entre $x$ o $y$, y quedarse solo con $(\pm\sqrt2,\pm\sqrt2)$ (que no dan el máximo).

---

### Ejercicio 5.48 (E pp. 211-212)

> Sea $f:\mathbb{R}^2\to\mathbb{R}$ tal que $f(x,y)=x^2-xy+y^2$. Encontrar los valores máximos y mínimos que alcanza $f$ en el conjunto $A=\{(x,y):|x|\le1,\ |y|\le1\}$.

**Antes de calcular**
- *Qué me piden:* máximo y mínimo absolutos en el cuadrado $[-1,1]\times[-1,1]$.
- *Cómo lo pienso:* la frontera no es una curva «lisa»: son 4 lados y 4 vértices. Cada lado es un segmento donde $f$ es una función de una variable.
- *Qué uso:* teorema de los valores extremos y procedimiento (U p. 222); extremos de una variable en un intervalo (U §3.4).
- *Por dónde empiezo:* puntos críticos del interior.

1. **Existencia:** polinomio (continuo) en un cuadrado cerrado y acotado.
2. **Interior:** $f_x=2x-y=0$, $f_y=-x+2y=0$: solo $(0,0)$, $f=0$. (Hessiana $\begin{pmatrix}2&-1\\-1&2\end{pmatrix}$, $d=3>0$, $r=2>0$: mínimo relativo; no es necesario para lo absoluto.)
3. **Lado $x=1$:** $\varphi(y)=1-y+y^2$, $\varphi'(y)=2y-1=0\Rightarrow y=\frac12$: punto $\left(1,\frac12\right)$, $f=\frac34$.
4. **Lado $x=-1$:** $1+y+y^2$, derivada $2y+1=0$: $\left(-1,-\frac12\right)$, $f=\frac34$.
5. **Lado $y=1$:** $x^2-x+1$: $\left(\frac12,1\right)$, $f=\frac34$. **Lado $y=-1$:** $x^2+x+1$: $\left(-\frac12,-1\right)$, $f=\frac34$.
6. **Vértices** (extremos de los intervalos de cada lado): $f(1,1)=f(-1,-1)=1$; $f(-1,1)=f(1,-1)=1+1+1=3$.
7. **Tabla y conclusión:** valores $0,\ \frac34,\ 1,\ 3$. **Mínimo $0$ en $(0,0)$; máximo $3$ en $(-1,1)$ y $(1,-1)$.**

**Receta.** Frontera poligonal: parametrizar cada lado como función de una variable en un intervalo cerrado; candidatos = ceros de su derivada dentro del intervalo + extremos del intervalo (vértices).

**Error típico.** Olvidar los vértices: aquí el máximo está precisamente en dos de ellos.

---

### Ejercicio 5.45 (E pp. 206-208)

> Se quiere instalar una tubería entre dos puntos, A y B, situados en los puntos de coordenadas $(0,0)$ y $(300,100)$, de las dos riberas de un río cuyo curso ocupa la región entre el eje $x$ y la recta $y=100$. El coste de la instalación de la tubería bajo el río es el triple que el coste de la instalación en tierra. ¿Cuál debe ser el trazado para que el coste de la instalación sea mínimo si la tubería debe ser recta al cruzar el río y seguir las riberas?

**Antes de calcular**
- *Qué me piden:* dónde cruzar a la otra orilla para que el coste sea mínimo.
- *Cómo lo pienso:* se cruza en línea recta desde A hasta $P=(x,100)$ y luego se va por la orilla hasta B. El coste depende de una sola variable, $x\in[0,300]$; el coste por metro $k$ es un factor que no cambia dónde está el mínimo.
- *Qué uso:* extremos de una variable en un intervalo cerrado (U §3.4).
- *Por dónde empiezo:* escribir el coste.

1. **Longitudes:** bajo el río, de $(0,0)$ a $(x,100)$: $\sqrt{x^2+100^2}$; por tierra, de $(x,100)$ a $(300,100)$: $300-x$.
2. **Coste:** $k(300-x)+3k\sqrt{x^2+100^2}=k\,h(x)$ con $h(x)=300-x+3\sqrt{x^2+100^2}$. Como $k>0$, minimizar el coste es minimizar $h$.
3. $h'(x)=-1+\dfrac{3x}{\sqrt{x^2+100^2}}=0\iff3x=\sqrt{x^2+100^2}$ (con $x\ge0$) $\iff9x^2=x^2+10\,000\iff x^2=1250\iff x=25\sqrt2\approx35.36$.
4. $h''(x)=\dfrac{3\cdot100^2}{(x^2+100^2)^{3/2}}>0$: mínimo relativo.
5. **Extremos del intervalo:** $h(0)=600$, $h(300)=300\sqrt{10}\approx948.7$, $h(25\sqrt2)=300+200\sqrt2\approx582.8$. El menor es el de $x=25\sqrt2$.
6. **Trazado:** cruzar en línea recta de A a $P=(25\sqrt2,100)\approx(35.4,\,100)$ y seguir por la orilla hasta B.

**Receta.** Si el problema depende de una sola variable, no hace falta Lagrange: función de una variable en un intervalo cerrado, críticos + extremos del intervalo.

**Error típico.** Elevar al cuadrado $3x=\sqrt{\dots}$ sin recordar que exige $x\ge0$, y aceptar la raíz negativa $x=-25\sqrt2$.

---

## 3. Preguntas de examen (X)

Selección variada: Hessiana (Feb 2018), absolutos en un compacto (Feb 2017), existencia (Sept 2018), Lagrange en la circunferencia (Sept 2017), distancia a una elipse (examen escaneado, p. 9) y optimización geométrica en $\mathbb{R}^3$ (Feb 2013). Otras de este tema en X que repiten métodos ya vistos: Feb 2011 2ª sem. y Feb 2014 A ($x^3+y^2-xy$, igual que E 5.31), Feb 2015 A (igual que E 5.44), Feb 2016 B (igual que E 5.43), Sept 2010 y Feb 2012 2ª sem. (como E 5.42).

---

### ★ X pp. 94-95 (Febrero 2018, Modelo B, Grado en Ing. Mecánica, Ej. 6, 3 puntos)

> Sea $f:\mathbb{R}^2\to\mathbb{R}$ la función definida por $f(x,y)=x^3+y^2-3xy$. Se pide:
> (a) (1 punto) Estudiar si los puntos $(0,0)$, $\left(\frac16,\frac1{12}\right)$ y $\left(\frac32,\frac94\right)$ son extremos relativos de la función.
> (b) (1.25 puntos) En caso de que lo sean, razonar si son máximos o mínimos relativos.
> (c) (0.75 puntos) ¿Es alguno de estos puntos un extremo absoluto de $f$ en $\mathbb{R}^2$? ¿Alcanza la función un máximo o un mínimo absoluto? (Indicación: considere el valor de la función en los ejes de coordenadas.)

**Antes de calcular**
- *Qué me piden:* lo mismo que E 5.31 con otra función: descartar los no críticos, clasificar los críticos y discutir lo absoluto.
- *Cómo lo pienso:* un punto que no anula el gradiente no puede ser extremo; a los críticos, Hessiana; el término $x^3$ impide que haya extremos absolutos.
- *Qué uso:* condición necesaria (U p. 218), condición suficiente (U p. 220).
- *Por dónde empiezo:* $\nabla f=(3x^2-3y,\ 2y-3x)$.

**Lo que hay que escribir en el examen:**
1. $f$ es un polinomio (clase $C^\infty$): sus extremos relativos están entre los puntos con $\nabla f=(3x^2-3y,\,2y-3x)=(0,0)$.
2. Sistema: $y=x^2$ e $y=\frac32x$, luego $x^2=\frac32x$, $x\left(x-\frac32\right)=0$: puntos críticos $(0,0)$ y $\left(\frac32,\frac94\right)$.
3. $\nabla f\left(\frac16,\frac1{12}\right)=\left(\frac1{12}-\frac14,\ \frac16-\frac12\right)=\left(-\frac16,-\frac13\right)\ne(0,0)$: **no es extremo relativo**.
4. $f_{xx}=6x$, $f_{xy}=-3$, $f_{yy}=2$.
5. $(0,0)$: $Hf=\begin{pmatrix}0&-3\\-3&2\end{pmatrix}$, $d=-9<0$: **punto de silla**, no es extremo.
6. $\left(\frac32,\frac94\right)$: $Hf=\begin{pmatrix}9&-3\\-3&2\end{pmatrix}$, $d=18-9=9>0$, $r=9>0$: **mínimo relativo**, con $f\left(\frac32,\frac94\right)=\frac{27}8+\frac{81}{16}-\frac{81}8=-\frac{27}{16}$.
7. (c) En el eje $y=0$: $f(x,0)=x^3$, que tiende a $+\infty$ si $x\to+\infty$ y a $-\infty$ si $x\to-\infty$. $f$ no está acotada ni superior ni inferiormente: **no hay máximo ni mínimo absolutos**; el mínimo relativo no es absoluto (p. ej. $f(-2,0)=-8<-\frac{27}{16}$).

**Explicaciones (no hace falta escribirlas):** las cuentas del paso 6, con denominador $16$: $\frac{54}{16}+\frac{81}{16}-\frac{162}{16}=-\frac{27}{16}$.

**Receta.** Ver E 5.31: gradiente en los puntos dados → Hessiana en los críticos → recta donde $f$ no está acotada.

**Error típico.** Aplicar la Hessiana a $\left(\frac16,\frac1{12}\right)$ (no es crítico) y sacar una conclusión.

sympy: críticos $(0,0)$, $\left(\frac32,\frac94\right)$; $d=-9$ y $9$; $f\left(\frac32,\frac94\right)=-\frac{27}{16}$; $\nabla f\left(\frac16,\frac1{12}\right)=\left(-\frac16,-\frac13\right)$.

---

### ★ X pp. 83-84 (Febrero 2017, Modelo B, Grado en Ing. Mecánica, Ej. 6, 3 puntos)

> Sea $f:[0,1]\times[0,1]\to\mathbb{R}$ la función dada por $f(x,y)=(x^2-x)(y^2-y)$.
> a) Determine en qué puntos se pueden alcanzar los extremos relativos de esta función en $(0,1)\times(0,1)$. Observación: para determinar las derivadas parciales, no desarrolle los paréntesis, y observe que un producto es $0$ si y solo si lo es uno de los factores.
> b) Determine dónde alcanza $f$ sus extremos absolutos en el conjunto $[0,1]\times[0,1]$. Observe que $f(0,y)=f(1,y)=f(x,0)=f(x,1)=0$.

**Antes de calcular**
- *Qué me piden:* candidatos del interior del cuadrado y después máximo/mínimo absolutos en el cuadrado cerrado.
- *Cómo lo pienso:* en $(0,1)$ los factores $x^2-x=x(x-1)$ e $y^2-y$ son negativos, así que $f>0$ dentro y $f=0$ en el borde. Mínimo en todo el borde; máximo dentro.
- *Qué uso:* condición necesaria (U p. 218), teorema de los valores extremos (U p. 222).
- *Por dónde empiezo:* $f_x=(2x-1)(y^2-y)$, $f_y=(x^2-x)(2y-1)$.

**Lo que hay que escribir en el examen:**
1. (a) $f$ es polinomio; en el abierto $(0,1)^2$ los extremos relativos están donde $f_x=(2x-1)(y^2-y)=0$ y $f_y=(x^2-x)(2y-1)=0$.
2. En $(0,1)^2$, $y^2-y=y(y-1)\ne0$, así que la 1ª obliga a $x=\frac12$. Igual, $x^2-x\ne0$ y la 2ª obliga a $y=\frac12$.
3. Único candidato: $\left(\frac12,\frac12\right)$, con $f=\left(-\frac14\right)\left(-\frac14\right)=\frac1{16}$.
4. (b) $f$ continua en el cuadrado cerrado y acotado $[0,1]^2$: por el teorema de los valores extremos alcanza máximo y mínimo absolutos, en la frontera o en un crítico del interior.
5. En la frontera $f=0$ (uno de los dos factores vale $0$). En el interior solo está $\left(\frac12,\frac12\right)$ con $f=\frac1{16}$.
6. **Máximo absoluto $\frac1{16}$ en $\left(\frac12,\frac12\right)$; mínimo absoluto $0$ en todos los puntos de la frontera.**

**Explicaciones (no hace falta escribirlas):**
- Comprobación del máximo sin Hessiana: dentro del cuadrado $f>0$ (producto de dos negativos) y el único candidato interior tiene el mayor valor de la tabla.
- Con Hessiana: $Hf\left(\frac12,\frac12\right)=\mathrm{diag}\!\left(-\frac12,-\frac12\right)$, $d=\frac14>0$, $r<0$: máximo relativo (sympy).

**Receta.** Absolutos en un rectángulo: críticos interiores + frontera; si $f$ vale constante en la frontera, la tabla tiene solo dos filas.

**Error típico.** Resolver $f_x=f_y=0$ en todo $\mathbb{R}^2$ y dar como candidatos interiores $(0,0)$, $(1,1)$… que están en la frontera.

sympy: críticos en $\mathbb{R}^2$: $(0,0),(0,1),(1,0),(1,1)$ (sillas, en la frontera) y $\left(\frac12,\frac12\right)$ con $f=\frac1{16}$.

---

### ★ X p. 97 (Septiembre 2018, Modelo A, Grado en Ing. Mecánica, P4, 1 punto)

> La función $f(x,y)=x^2y^3$ está definida sobre el conjunto $S=\{(x,y)\in\mathbb{R}^2:1\le x^2+y^2\le4\}$. ¿Alcanza el máximo absoluto en este conjunto? Justifique la respuesta.

**Antes de calcular**
- *Qué me piden:* solo si existe el máximo.
- *Cómo lo pienso:* es una corona circular con los dos bordes incluidos: cerrada y acotada.
- *Qué uso:* teorema de los valores extremos (U p. 222).
- *Por dónde empiezo:* comprobar hipótesis.

**Lo que hay que escribir en el examen:**
1. $f$ es un polinomio, luego continua.
2. $S$ es cerrado (las desigualdades $\le$ incluyen las dos circunferencias $x^2+y^2=1$ y $x^2+y^2=4$, que forman su frontera) y acotado (contenido en el disco de radio $2$).
3. Por el teorema de los valores extremos, **sí**: $f$ alcanza el máximo (y el mínimo) absoluto en $S$.

**Receta.** Ver E 5.38. Lo único que cambia es reconocer que una corona con «$\le$» en los dos lados es cerrada.

**Error típico.** Pensar que «tiene un agujero» impide aplicar el teorema: el agujero no importa; lo que importa es que $S$ contenga su frontera y esté acotado. (Si fuera $1<x^2+y^2\le4$, no sería cerrado y el teorema no se podría aplicar.)

---

### ★ X p. 134 (Septiembre 2017, Ej. 6, 3 puntos)

> Utilice el método de los multiplicadores de Lagrange para determinar y clasificar los extremos de la función $f(x,y)=xy$, sujeta a la condición $x^2+y^2=1$.

**Antes de calcular**
- *Qué me piden:* candidatos de Lagrange y decir cuáles son máximo y mínimo.
- *Cómo lo pienso:* la circunferencia es cerrada y acotada: basta comparar valores. Por simetría, el producto es máximo en la diagonal $y=x$ y mínimo en $y=-x$.
- *Qué uso:* método de Lagrange (U p. 228) y teorema de los valores extremos (U p. 222).
- *Por dónde empiezo:* $F=xy+\lambda(x^2+y^2-1)$.

**Lo que hay que escribir en el examen:**
1. $f$ y $g=x^2+y^2-1$ son continuas con parciales continuas; $\nabla g=(2x,2y)\ne\bar0$ en la circunferencia.
2. $F_x=y+2\lambda x=0$, $F_y=x+2\lambda y=0$, $x^2+y^2=1$.
3. Si $\lambda=0$: $x=y=0$, que no cumple la restricción. Luego $\lambda\ne0$.
4. Multiplicando la 1ª por $y$ y la 2ª por $x$: $y^2=-2\lambda xy=x^2$. Entonces $x^2=y^2=\frac12$.
5. Candidatos: $\left(\pm\frac{\sqrt2}2,\pm\frac{\sqrt2}2\right)$ (los cuatro). Con $y=x$: $\lambda=-\frac12$; con $y=-x$: $\lambda=\frac12$.
6. La circunferencia es cerrada y acotada: $f$ alcanza máximo y mínimo absolutos entre los candidatos.
7. $f=\frac12$ en $\left(\frac{\sqrt2}2,\frac{\sqrt2}2\right)$ y $\left(-\frac{\sqrt2}2,-\frac{\sqrt2}2\right)$: **máximo**. $f=-\frac12$ en $\left(\frac{\sqrt2}2,-\frac{\sqrt2}2\right)$ y $\left(-\frac{\sqrt2}2,\frac{\sqrt2}2\right)$: **mínimo**.

**Explicaciones (no hace falta escribirlas):** el paso 4 es «despejar $\lambda$ en las dos ecuaciones e igualar»: $-\frac{y}{2x}=-\frac{x}{2y}$ (se puede dividir porque, con $\lambda\ne0$, si $x=0$ la 1ª da $y=0$, imposible).

**Receta.** Sistema de Lagrange simétrico: despejar $\lambda$ en dos ecuaciones e igualar, para obtener una relación entre $x$ e $y$ sin $\lambda$; luego la restricción.

**Error típico.** Quedarse solo con $x=y$ (de $x^2=y^2$ salen $y=x$ e $y=-x$).

sympy: los cuatro puntos con $\lambda=\mp\frac12$ y $f=\pm\frac12$.

---

### ★ X p. 9 (examen escaneado de la serie de 2010, sin cabecera, P1, 3 puntos)

> Hállese la distancia mínima y máxima del origen de coordenadas a la elipse $5x^2+6xy+5y^2=8$.

**Antes de calcular**
- *Qué me piden:* el punto de la elipse más cercano y el más lejano al origen, y esas distancias.
- *Cómo lo pienso:* como en E 5.47, se optimiza el cuadrado de la distancia $x^2+y^2$. La elipse está girada $45^\circ$ (por el término $6xy$): sus ejes son las diagonales $y=x$ e $y=-x$, y ahí estarán los extremos.
- *Qué uso:* Lagrange (U p. 228), teorema de los valores extremos (U p. 222).
- *Por dónde empiezo:* $f=x^2+y^2$, $g=5x^2+6xy+5y^2-8$.

**Lo que hay que escribir en el examen:**
1. La elipse es cerrada y acotada y $f$ es continua: hay distancia máxima y mínima. $\nabla g=(10x+6y,\,6x+10y)$ solo se anula en $(0,0)$, que no está en la elipse.
2. $F=x^2+y^2+\lambda(5x^2+6xy+5y^2-8)$: $2x+\lambda(10x+6y)=0$, $2y+\lambda(6x+10y)=0$, $g=0$.
3. Restando las dos primeras: $2(x-y)+\lambda(4x-4y)=0\iff(x-y)(2+4\lambda)=0$. Dos casos: $y=x$ o $\lambda=-\frac12$.
4. **$y=x$:** $5x^2+6x^2+5x^2=16x^2=8$, $x=\pm\frac{\sqrt2}2$. Puntos $\pm\left(\frac{\sqrt2}2,\frac{\sqrt2}2\right)$, $f=1$.
5. **$\lambda=-\frac12$:** la 1ª queda $2x-5x-3y=0$, es decir $y=-x$; en $g$: $5x^2-6x^2+5x^2=4x^2=8$, $x=\pm\sqrt2$. Puntos $\pm(\sqrt2,-\sqrt2)$, $f=4$.
6. **Distancia mínima $\sqrt1=1$** en $\pm\left(\frac{\sqrt2}2,\frac{\sqrt2}2\right)$; **distancia máxima $\sqrt4=2$** en $\pm(\sqrt2,-\sqrt2)$.

**Explicaciones (no hace falta escribirlas):** el truco del paso 3 (restar las ecuaciones) funciona porque el sistema es simétrico al cambiar $x$ por $y$. Comprobación geométrica: en la diagonal $y=x$ la elipse está «estrecha» (semieje $1$) y en $y=-x$, «ancha» (semieje $2$).

**Receta.** Distancia máxima/mínima a una curva cerrada: Lagrange sobre $x^2+y^2$; existencia por el teorema de los valores extremos; raíz cuadrada al final.

**Error típico.** Dar $1$ y $4$ como distancias (son los cuadrados de las distancias).

sympy: candidatos $\pm\left(\frac{\sqrt2}2,\frac{\sqrt2}2\right)$ ($\lambda=-\frac18$, $f=1$) y $\pm(\sqrt2,-\sqrt2)$ ($\lambda=-\frac12$, $f=4$).

---

### ★ X pp. 33-34 (Febrero 2013, 1ª semana, Ing. Mecánica, Modelo A, Ej. 6)

> Determínense las dimensiones de un paralelepípedo rectangular de volumen $1\,\mathrm{m}^3$ dado, de tal forma que su área sea mínima o máxima.

**Antes de calcular**
- *Qué me piden:* las aristas $x,y,z>0$ con $xyz=1$ que hacen extremo el área $2xy+2xz+2yz$.
- *Cómo lo pienso:* por simetría el candidato será el cubo. El área puede crecer sin límite (una caja muy larga y muy fina), así que solo habrá mínimo.
- *Qué uso:* Lagrange en $\mathbb{R}^3$ (U p. 228), o despejar una variable y usar puntos críticos y Hessiana (U pp. 216, 220).
- *Por dónde empiezo:* $A=2xy+2xz+2yz$ con $g=xyz-1$.

**Lo que hay que escribir en el examen (vía Lagrange):**
1. $F=2xy+2xz+2yz+\lambda(xyz-1)$, con $x,y,z>0$.
2. $F_x=2y+2z+\lambda yz=0$, $F_y=2x+2z+\lambda xz=0$, $F_z=2x+2y+\lambda xy=0$, $xyz=1$.
3. Multiplicando la 1ª por $x$, la 2ª por $y$ y la 3ª por $z$ y usando $xyz=1$: $2xy+2xz=-\lambda$, $2xy+2yz=-\lambda$, $2xz+2yz=-\lambda$.
4. Restando la 1ª y la 2ª: $2z(x-y)=0$, y como $z>0$, $x=y$. Restando la 2ª y la 3ª: $2x(y-z)=0$, $y=z$.
5. $x=y=z$ y $x^3=1$: **$x=y=z=1$ m** (un cubo), $\lambda=-4$, área $6\,\mathrm{m}^2$.
6. **Naturaleza:** despejando $x=\frac1{yz}$, $A(y,z)=\frac2z+\frac2y+2yz$ ($y,z>0$). En $(1,1)$: $A_y=-\frac2{y^2}+2z=0$, $A_z=-\frac2{z^2}+2y=0$ ✓; $HA(1,1)=\begin{pmatrix}4&2\\2&4\end{pmatrix}$, $d=12>0$, $r=4>0$: **mínimo**.
7. **No hay máximo:** con $x=y=n$, $z=\frac1{n^2}$, el volumen es $1$ y el área es $2n^2+\frac4n\to+\infty$.

**Explicaciones (no hace falta escribirlas):** el paso 3 es un truco útil cuando la restricción es un producto: al multiplicar cada ecuación por «su» variable aparece $xyz$, que vale $1$.

**Receta.** Optimización de cajas: Lagrange con $g$ = volumen, multiplicar cada ecuación por su variable y restar; clasificar despejando una variable y usando la Hessiana de dos variables.

**Error típico.** Decir que el cubo da «área mínima o máxima» sin decidir: es mínima, y máxima no existe.

sympy: Lagrange da solo $(1,1,1)$ con $\lambda=-4$, $A=6$; $\det HA(1,1)=12$.

---

## 4. Ejemplos propios (dificultad creciente)

### Propio 1: un mínimo con la Hessiana (fácil)

> Halla y clasifica los puntos críticos de $f(x,y)=x^2+xy+y^2-3x$.

1. $f_x=2x+y-3=0$, $f_y=x+2y=0$. De la 2ª, $x=-2y$; en la 1ª, $-3y-3=0$, $y=-1$, $x=2$.
2. $Hf=\begin{pmatrix}2&1\\1&2\end{pmatrix}$, $d=3>0$, $r=2>0$: **mínimo relativo** en $(2,-1)$, con $f(2,-1)=4-2+1-6=-3$.

**Receta.** Polinomio de grado 2: un único crítico (sistema lineal) y Hessiana constante.

sympy ✓.

### Propio 2: silla y dos mínimos (medio)

> Halla y clasifica los puntos críticos de $f(x,y)=x^4+y^4-4xy$.

1. $f_x=4x^3-4y=0\Rightarrow y=x^3$; $f_y=4y^3-4x=0\Rightarrow x=y^3=x^9$.
2. $x^9-x=x(x^8-1)=0$: $x=0$ o $x=\pm1$ (raíces reales de $x^8=1$). Puntos $(0,0)$, $(1,1)$, $(-1,-1)$.
3. $Hf=\begin{pmatrix}12x^2&-4\\-4&12y^2\end{pmatrix}$.
4. $(0,0)$: $d=-16<0$, **silla**. $(\pm1,\pm1)$: $d=144-16=128>0$, $r=12>0$, **mínimos relativos** con $f=-2$.

**Para entenderlo:** como $x^4+y^4\to\infty$ más rápido que $4xy$, los dos mínimos son además absolutos.

sympy ✓.

### Propio 3: Lagrange en una elipse (medio-difícil)

> Halla el rectángulo de área máxima, con lados paralelos a los ejes, inscrito en la elipse $\frac{x^2}4+y^2=1$.

1. Si $(x,y)$ es el vértice del primer cuadrante, el área es $f=4xy$ con $x,y>0$ y $g=\frac{x^2}4+y^2-1=0$.
2. $F=4xy+\lambda\left(\frac{x^2}4+y^2-1\right)$: $4y+\frac{\lambda x}2=0$, $4x+2\lambda y=0$.
3. De la 1ª, $\lambda=-\frac{8y}x$; en la 2ª: $4x-\frac{16y^2}x=0\Rightarrow x^2=4y^2$.
4. En la elipse: $\frac{4y^2}4+y^2=2y^2=1$, $y=\frac{\sqrt2}2$, $x=\sqrt2$.
5. Área $4\cdot\sqrt2\cdot\frac{\sqrt2}2=4$. Es máximo: la elipse es cerrada y acotada, $f=4xy$ alcanza máximo en ella, y el máximo está entre los candidatos de Lagrange (en los otros candidatos, $f=-4$).
6. **Rectángulo de lados $2\sqrt2\times\sqrt2$, área $4$.**

sympy: candidatos $(\pm\sqrt2,\pm\frac{\sqrt2}2)$, $f=\pm4$.

### Propio 4: absolutos en un disco (difícil)

> Halla el máximo y el mínimo absolutos de $f(x,y)=x^2+y^2-2x$ en el disco $x^2+y^2\le4$.

1. **Existencia:** polinomio en un disco cerrado y acotado.
2. **Interior:** $f_x=2x-2=0$, $f_y=2y=0$: $(1,0)$, con $x^2+y^2=1<4$ (sí es interior). $f(1,0)=-1$.
3. **Frontera** $x^2+y^2=4$: sustituyendo, $f=4-2x$ con $x\in[-2,2]$. Es decreciente en $x$: máximo $8$ en $x=-2$ (punto $(-2,0)$), mínimo $0$ en $x=2$ (punto $(2,0)$).
   (Con Lagrange: $2x-2+2\lambda x=0$, $2y+2\lambda y=0$; si $y\neq0$, $\lambda=-1$ y la 1ª da $-2=0$, imposible; luego $y=0$, $x=\pm2$.)
4. **Tabla:** $f(1,0)=-1$, $f(2,0)=0$, $f(-2,0)=8$. **Mínimo $-1$ en $(1,0)$; máximo $8$ en $(-2,0)$.**

**Para entenderlo:** $f=(x-1)^2+y^2-1$: es «la distancia al cuadrado al punto $(1,0)$, menos 1». El punto del disco más cercano a $(1,0)$ es él mismo; el más lejano, $(-2,0)$.

**Receta.** En la frontera, si la restricción permite sustituir $x^2+y^2$ por una constante, $f$ se convierte en una función de una variable en un intervalo cerrado.

sympy: críticos y Lagrange coinciden.

---

## Notas internas (no pasar al HTML)

- **E 5.30 (p. 192):** las dos derivadas del desarrollo aparecen rotuladas «$\partial f/\partial x$»; la segunda es $\partial f/\partial y$. Enunciado leído como $f=xy(x^2+y^2)$ por las derivadas.
- **E 5.32 (p. 194):** la frase «Pero si x = 0, entonces debe ser y = ±1» debe leerse «si $x\ne0$» (pérdida de la barra en la extracción o errata).
- **E 5.37 (p. 199):** en la figura las etiquetas de B y C están intercambiadas respecto al enunciado.
- **E 5.45 (p. 207):** dice «para comprobar que son menores que $h(25\sqrt2)$»; debe ser «mayores».
- **E 5.47 (p. 210):** la conclusión repite el mismo punto «$(\sqrt3,-\sqrt3,1)$ y $(\sqrt3,-\sqrt3,1)$»; el segundo es $(-\sqrt3,\sqrt3,1)$.
- **E 5.40:** E deja abierta la clasificación; aquí se completa (mínimo, área $\approx248.08$ cm², sin máximo).
- **E 5.48 (p. 212):** valores $f(P_5)\dots f(P_8)=\frac34$ (la extracción los rompe).
- **X pp. 94-95 (Feb 2018 B):** la solución impresa da $f\left(\frac32,\frac94\right)=-\frac{27}8$; el valor correcto es $-\frac{27}{16}$ (sympy). No cambia la conclusión.
- **X pp. 83-84 (Feb 2017 B):** la indicación impresa escribe «$f(y,0)$» donde debe ser $f(x,1)$; aquí se ha escrito la forma correcta en el enunciado.
- **X pp. 33-34 (Feb 2013):** la solución impresa no decide entre mínimo y máximo («mínima o máxima»); aquí se justifica mínimo y se prueba que no hay máximo. La puntuación del ejercicio no aparece en la página.
- **X p. 9:** página escaneada sin cabecera ni solución impresa (va tras el examen de Septiembre 2010, Eléctrica, y antes de Feb 2011 Mecánica A); solución propia verificada con sympy. Citarla como «X p. 9 (examen de 2010, sin cabecera)».
- **X p. 97 (Sept 2018 A):** la solución impresa cita «página 268 del libro de teoría» (edición anterior); en U actual el teorema está en p. 222.
- **U Teorema de Lagrange (pp. 226, 228):** en el `.txt` falta la barra de $\ne$ en «$\nabla g(a,b)\ne0$»; la hipótesis es $\nabla g\neq\bar0$.
- **U Ej. 5.20:** la matriz en $(\pm1,0)$ es $\mathrm{diag}(-4,2)$ (verificado con sympy).
