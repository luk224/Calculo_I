# Soluciones Tema 6.2 — Teoremas fundamentales del Cálculo

Resolución paso a paso de los ejercicios de **E** de la sección 6.2 de U (Ejercicios 6.11-6.16, E pp. 218-223), de 6 preguntas de exámenes **X** y de 4 ejemplos propios. Todos los cálculos se han comprobado con sympy (scripts `v62.py` y `p62.py` en el scratchpad). Los enunciados de X se han leído como imagen (render de las pp. 107, 109, 110, 112, 113, 115, 116, 119 y 144); los de E, en `ejercicios.txt` (pp. 218-223).

Páginas: U impresa (= PDF + 2); E impresa = PDF; X = página del PDF de exámenes; L impresa = PDF − 17.

## 0. Herramientas de teoría que se usan

| Clave | Enunciado (resumido) | Dónde |
|---|---|---|
| **Def. 6.2 (primitiva)** | $F$ es primitiva de $f$ en $(a,b)$ si $F'(x)=f(x)$ para todo $x\in(a,b)$. Todas las primitivas son $F+k$, $k\in\mathbb R$; se escribe $\int f(x)\,dx=F(x)+C$. | U p. 241 |
| **Teorema 6.1 (TFC, 1ª parte)** | Si $f:[a,b]\to\mathbb R$ es continua, $F(x)=\int_a^x f(t)\,dt$ es derivable y $F'(x)=f(x)$ para todo $x\in(a,b)$. «Se elimina el signo integral y se sustituye $t$ por $x$» (Ej. 6.6). | U p. 243 (Ej. 6.6 y 6.7, p. 244) |
| **Límite inferior variable** | $\int_x^c f(t)\,dt=-\int_c^x f(t)\,dt$, luego $\dfrac{d}{dx}\int_x^c f(t)\,dt=-f(x)$. | U Ej. 6.7, p. 244; propiedad (P6) p. 240 |
| **Teorema 6.2 (TFC, 2ª parte, regla de Barrow)** | Si $f$ es **continua en $[a,b]$** y $F$ es **cualquier** primitiva de $f$, $\displaystyle\int_a^b f(x)\,dx=F(x)\Big|_a^b=F(b)-F(a)$. | U p. 244 (Ej. 6.8, p. 245) |
| **TVM integral** | Si $f$ es continua en $[a,b]$, existe $c\in[a,b]$ con $\int_a^b f(x)\,dx=f(c)(b-a)$. Al número $\frac1{b-a}\int_a^b f$ se le llama **valor medio** de $f$ en $[a,b]$ (L §4.4, p. 281). | U p. 244 (margen); demostración en E 6.9 |
| Propiedades de la integral | (P5) aditividad $\int_a^b=\int_a^c+\int_c^b$; (P6) $\int_a^b f=-\int_b^a f$; monotonía. | U p. 240 |
| Integral impropia de 2ª especie | Si $f:(a,b]\to\mathbb R$ es continua y no acotada, $\int_a^b f=\lim_{\varepsilon\to0^+}\int_{a+\varepsilon}^b f$. | U Def. 6.10, p. 275 |

**Herramientas de temas anteriores:**
- **Regla de la cadena** (U §2.2, p. 79): $(g\circ f)'(a)=g'(f(a))\,f'(a)$.
- **Monotonía por el signo de la derivada** (U Prop. 2.4, p. 98): $f'>0$ en un intervalo ⇒ estrictamente creciente; $f'<0$ ⇒ estrictamente decreciente.
- **Criterio de la 2ª derivada** (U Prop. 3.7, p. 131): si $f'(c)=0$ y $f''(c)<0$, máximo relativo en $c$; si $f''(c)>0$, mínimo relativo.
- **Convexidad y punto de inflexión** (U Prop. 3.10, p. 136; Def. 3.10 y Prop. 3.11-3.12, p. 137): $f''\ge0$ ⇒ convexa; $f''\le0$ ⇒ cóncava; si $f''(c)=0$ y $f'''(c)\ne0$, hay inflexión en $c$ (de convexa a cóncava si $f'''(c)<0$).
- **L'Hôpital** (U §2.3, p. 82), solo en el Propio 1 b).

---

### Receta general del tema

> **Derivar una función definida por una integral** $G(x)=\int_{a(x)}^{b(x)}f(t)\,dt$ con $f$ continua:
> $$G'(x)=f\big(b(x)\big)\,b'(x)-f\big(a(x)\big)\,a'(x).$$
> «Integrando evaluado en el límite de arriba por su derivada, menos integrando evaluado en el límite de abajo por su derivada». Casos: límite de arriba $x$ ⇒ $G'=f(x)$; límite de abajo $x$ ⇒ $G'=-f(x)$; límite constante ⇒ ese término es $0$.
>
> **Calcular una integral definida con Barrow**:
> 1. **Comprobar** que el integrando es continuo en todo $[a,b]$ (si no, Barrow no se puede usar).
> 2. Buscar una primitiva $F$ y **comprobarla derivando**.
> 3. Calcular $F(b)-F(a)$ (la constante $C$ no hace falta: se cancela).
>
> **Estudiar monotonía/extremos de $F(x)=\int_a^x f(t)\,dt$**: $F'=f$ (TFC1), así que $F$ crece donde $f>0$ y decrece donde $f<0$; sus puntos críticos son los ceros de $f$, y $F''=f'$.

---

## 1. Ejercicios de E (orden de dificultad creciente; numeración conservada)

Orden propuesto para aprender: **6.11** (qué es una primitiva) **→ 6.14** (límite inferior variable) **→ 6.16** (cuándo se puede usar Barrow) **→ 6.13** (monotonía y extremos de $\int_0^x$) **→ 6.12** (TFC1 + regla de la cadena + inflexión) **→ 6.15** (fórmula general con los dos límites variables).

---

### Ejercicio 6.11 (E pp. 218-219)

> Sea $F:\mathbb R\to\mathbb R$ una primitiva de una función continua $f:\mathbb R\to\mathbb R$ y $C\in\mathbb R$ una constante. Señale la opción correcta:
> a) $\dfrac{d}{dx}\big(F(x)+C\big)=f(x)$, $\forall x\in\mathbb R$. b) $\dfrac{d}{dx}\big(f(x)+C\big)=F(x)$, $\forall x\in\mathbb R$. c) $\displaystyle\int F(x)\,dx=f(x)+C$, $\forall x\in\mathbb R$. d) Ninguna de las anteriores.

**Antes de calcular**
- **Qué me piden:** decidir cuál de tres igualdades sobre $f$, su primitiva $F$ y una constante $C$ es siempre cierta.
- **Cómo lo pienso:** «$F$ es primitiva de $f$» quiere decir una sola cosa: derivando $F$ sale $f$. Cada opción se traduce a «¿qué se deriva y qué sale?» y se comprueba.
- **Qué uso:** Def. 6.2 de primitiva (U p. 241): $F'=f$; la derivada de una constante es $0$ (U p. 79, tabla).
- **Por dónde empiezo:** derivar $F(x)+C$ en a).

1. **Traducir la hipótesis.** Por la Def. 6.2 (U p. 241), $F'(x)=f(x)$ para todo $x$.
2. **a) Verdadera.** La derivada de una suma es la suma de derivadas y la de una constante es $0$:
   $$\frac{d}{dx}\big(F(x)+C\big)=F'(x)+0=f(x).$$
   Es decir, $F+C$ es **otra** primitiva de $f$: por eso se escribe $\int f=F+C$.
3. **Ejemplo para probar las demás:** $f(x)=1$ (continua), $F(x)=x$ (primitiva, pues $F'=1$), $C=1$.
4. **b) Falsa.** Primero, nada garantiza que $f$ sea derivable (solo se sabe que es continua; por ejemplo $f(x)=|x|$ no es derivable en $0$), así que la expresión puede no tener sentido. Y aunque lo sea: con el ejemplo, $\frac{d}{dx}(1+1)=0\ne x=F(x)$ para $x\ne0$.
5. **c) Falsa.** c) dice que las primitivas de $F$ son $f+C$, es decir, que $(f+C)'=F$. Con el ejemplo: las primitivas de $F(x)=x$ son $\frac{x^2}2+C$, no $1+C$ (derivando $1+C$ sale $0\ne x$).
6. **d) Falsa**, porque a) es correcta. **Respuesta: a).**

**Receta.** Traducir cada afirmación sobre primitivas a «derivada de la primitiva = integrando» y probar con $f=1$, $F=x$.

**Error típico.** Invertir los papeles (creer que $f$ es la «primitiva» de $F$) o pensar que la constante cambia la derivada: $F+C$ y $F$ tienen la misma derivada.

sympy: $\frac{d}{dx}(x+5)=1$.

---

### Ejercicio 6.14 (E pp. 220-221)

> Calcula el valor de $\displaystyle\frac{d}{dx}\left(\int_x^1 t^2\,dt\right)$.

**Antes de calcular**
- **Qué me piden:** la derivada respecto de $x$ de una integral cuyo **límite inferior** es $x$.
- **Cómo lo pienso:** el TFC1 solo dice cómo derivar si la $x$ está **arriba**. Le doy la vuelta a la integral (cambia el signo) y la $x$ queda arriba.
- **Qué uso:** cambio de orden de los límites (P6, U p. 240), TFC1 (U Teor. 6.1, p. 243) y U Ej. 6.7 (p. 244).
- **Por dónde empiezo:** escribir $\int_x^1=-\int_1^x$.

1. **Comprobar la hipótesis del TFC1.** $f(t)=t^2$ es continua en todo $\mathbb R$, así que el TFC1 se puede aplicar en cualquier intervalo $[1,x]$ o $[x,1]$.
2. **Intercambiar los límites** (P6, U p. 240: intercambiar los límites cambia el signo):
   $$\int_x^1 t^2\,dt=-\int_1^x t^2\,dt.$$
3. **Derivar con el TFC1.** Ahora $x$ está en el límite superior y el inferior ($1$) es fijo. La derivada de una constante por una función es la constante por la derivada:
   $$\frac{d}{dx}\left(-\int_1^x t^2\,dt\right)=-\frac{d}{dx}\int_1^x t^2\,dt=-x^2.$$
4. **Resultado: $-x^2$.**
5. **Comprobación con Barrow.** $\int_x^1 t^2\,dt=\left[\frac{t^3}3\right]_x^1=\frac13-\frac{x^3}3$, cuya derivada es $-x^2$. Coincide.

**Receta.** Si la $x$ está en el límite **inferior**, intercambiar los límites (sale un signo menos) y aplicar el TFC1: $\frac{d}{dx}\int_x^c f(t)\,dt=-f(x)$.

**Error típico.** Contestar $x^2$ (olvidar el signo) o $\frac13-\frac{x^3}3$ (calcular la integral y no derivarla).

sympy: `diff(integrate(t**2,(t,x,1)),x)` $=-x^2$.

---

### Ejercicio 6.16 (E pp. 222-223)

> Se sabe que $\displaystyle\int\frac{1}{x-1}\,dx=\ln|x-1|+C$ en $\mathbb R\setminus\{1\}$. ¿Qué opción es verdadera?
> a) No hay relación entre la integral definida y la indefinida.
> b) Utilizando Barrow resulta $\displaystyle\int_0^2\frac1{x-1}\,dx=0$.
> c) Utilizando Barrow resulta $\displaystyle\int_2^3\frac1{x-1}\,dx=\ln2$.

**Antes de calcular**
- **Qué me piden:** decidir en qué casos se puede usar la regla de Barrow con la primitiva $\ln|x-1|$.
- **Cómo lo pienso:** Barrow tiene una hipótesis: el integrando continuo en **todo** el intervalo $[a,b]$. Si el intervalo contiene el punto donde $\frac1{x-1}$ «explota» ($x=1$), no se puede usar, aunque la cuenta «salga».
- **Qué uso:** regla de Barrow (U Teor. 6.2, p. 244), con su hipótesis de continuidad.
- **Por dónde empiezo:** mirar si $x=1$ está en $[0,2]$ y en $[2,3]$.

1. **a) Falsa.** La regla de Barrow (U Teor. 6.2, p. 244) es precisamente la relación entre ambas: la integral definida se calcula con una primitiva (integral indefinida).
2. **Hipótesis de Barrow en b).** $f(x)=\frac1{x-1}$ no está definida en $x=1$, y $1\in[0,2]$. Por tanto $f$ **no** es continua en $[0,2]$ y **no se puede aplicar Barrow**.
3. **Por qué la cuenta de b) engaña.** Si se aplicara a ciegas: $\ln|2-1|-\ln|0-1|=0-0=0$. Pero cerca de $x=1$ la función no está acotada (por ejemplo $f(1{,}001)=1000$, $f(0{,}999)=-1000$), así que no es integrable en $[0,2]$ y esa integral no tiene sentido como integral de Riemann. Un resultado numérico no prueba nada si la hipótesis del teorema falla.
4. **Hipótesis de Barrow en c).** En $[2,3]$ se tiene $x-1\in[1,2]$, nunca $0$: $f$ es continua en $[2,3]$. Barrow se puede aplicar.
5. **Cálculo de c).** Con la primitiva $F(x)=\ln|x-1|$ (se puede tomar $C=0$: U p. 245, cualquier primitiva vale):
   $$\int_2^3\frac{dx}{x-1}=\ln|3-1|-\ln|2-1|=\ln2-\ln1=\ln2.$$
6. **Respuesta: c).**

**Receta.** Antes de aplicar Barrow, buscar los puntos donde el integrando no está definido (denominador $0$, logaritmo de $0$, raíz de negativo…) y comprobar que **ninguno** está en $[a,b]$.

**Error típico.** Aplicar Barrow «porque se conoce la primitiva» sin mirar el intervalo: con $\int_{-1}^1\frac{dx}{x^2}$ saldría $-2$, un número negativo para una función positiva (ver Propio 2).

sympy: $\int_2^3\frac{dx}{x-1}=\ln2$; en $[0,2]$ sympy no da valor (integral divergente).

---

### Ejercicio 6.13 (E p. 220)

> Dada la función $F(x)=\displaystyle\int_0^x t\,\mathrm{sen}\,t\,dt$ definida en $I=[0,\infty)$, señala la opción correcta.
> a) $F$ alcanza un máximo en $x=7\pi$. b) $F$ es creciente en $I$. c) $F$ alcanza un mínimo en $x=7\pi$. d) $F$ es decreciente en $I$.

**Antes de calcular**
- **Qué me piden:** estudiar la monotonía de $F$ y qué pasa en $x=7\pi$.
- **Cómo lo pienso:** no hace falta calcular la integral: el TFC1 da $F'$ directamente, y con $F'$ y $F''$ se estudian crecimiento y extremos como en el Tema 3.
- **Qué uso:** TFC1 (U Teor. 6.1, p. 243); monotonía por el signo de $F'$ (U Prop. 2.4, p. 98); criterio de la 2ª derivada (U Prop. 3.7, p. 131).
- **Por dónde empiezo:** $F'(x)=x\,\mathrm{sen}\,x$.

1. **Derivar con el TFC1.** $f(t)=t\,\mathrm{sen}\,t$ es continua en $\mathbb R$, luego (U Teor. 6.1, p. 243)
   $$F'(x)=x\,\mathrm{sen}\,x.$$
2. **Descartar b) y d).** Para $x>0$ el signo de $F'$ es el de $\mathrm{sen}\,x$, que cambia: $F'>0$ en $(0,\pi)$ y $F'<0$ en $(\pi,2\pi)$. Así que $F$ crece en $(0,\pi)$ y decrece en $(\pi,2\pi)$ (U Prop. 2.4, p. 98): no es ni creciente ni decreciente en $I$.
3. **Puntos críticos.** $F'(x)=0\iff x=0$ o $\mathrm{sen}\,x=0\iff x=k\pi$, $k=0,1,2,\dots$ En particular, $7\pi$ es punto crítico.
4. **Segunda derivada** (derivada de un producto):
   $$F''(x)=\mathrm{sen}\,x+x\cos x.$$
5. **Evaluar en $7\pi$.** $\mathrm{sen}(7\pi)=0$ y $\cos(7\pi)=\cos\pi=-1$ (7 es impar), luego $F''(7\pi)=0+7\pi(-1)=-7\pi<0$.
6. **Concluir** (U Prop. 3.7, p. 131): $F'(7\pi)=0$ y $F''(7\pi)<0$ ⇒ $F$ alcanza un **máximo relativo** en $x=7\pi$. Comprobación con el signo: justo antes de $7\pi$, $\mathrm{sen}\,x>0$ ($F$ sube); justo después, $\mathrm{sen}\,x<0$ ($F$ baja).
7. **Respuesta: a).** (Es un máximo relativo, no absoluto: con Barrow, $F(x)=\mathrm{sen}\,x-x\cos x$, y $F(7\pi)=7\pi<F(9\pi)=9\pi$.)

**Receta.** Para $F(x)=\int_a^x f(t)\,dt$: $F'=f$ y $F''=f'$. Puntos críticos = ceros de $f$; se clasifican con el signo de $f$ alrededor o con $f'$.

**Error típico.** Intentar calcular la integral (aquí requiere integración por partes, §6.3) cuando solo se necesita su derivada; o equivocarse con $\cos(7\pi)$ (vale $-1$, no $1$).

sympy: $F(x)=\mathrm{sen}\,x-x\cos x$, $F'=x\,\mathrm{sen}\,x$, $F''(7\pi)=-7\pi$; $F'(7\pi\mp0{,}1)\approx\pm2{,}2$.

---

### Ejercicio 6.12 (E pp. 219-220)

> Sea $H=F\circ G$ con $F(x)=\displaystyle\int_0^x\mathrm{sen}(\ln t)\,dt$ y $G(x)=e^x$. Señala la opción correcta:
> a) $H$ es creciente en $\mathbb R$. b) $H$ tiene un punto de inflexión en $x=\frac{3\pi}4$. c) $H$ es cóncava en $\mathbb R$. d) $H$ alcanza un mínimo en $\pi$.

**Antes de calcular**
- **Qué me piden:** estudiar crecimiento, concavidad, inflexión y extremos de $H(x)=F(e^x)$.
- **Cómo lo pienso:** $H$ es una composición; su derivada sale con la regla de la cadena, y la derivada de $F$ la da el TFC1. Con $H'$, $H''$ y $H'''$ se revisan las cuatro opciones.
- **Qué uso:** regla de la cadena (U p. 79); TFC1 (U Teor. 6.1, p. 243); U Prop. 2.4 (p. 98), Prop. 3.7 (p. 131), Prop. 3.10-3.12 (pp. 136-137).
- **Por dónde empiezo:** $H'(x)=F'(e^x)\cdot e^x$.

1. **Derivada de $F$.** El integrando $\mathrm{sen}(\ln t)$ es continuo para $t>0$ (en $t=0$ no está definido, pero está acotado entre $-1$ y $1$). Para $u>0$ se escribe
   $$F(u)=\int_0^1\mathrm{sen}(\ln t)\,dt+\int_1^u\mathrm{sen}(\ln t)\,dt.$$
   El primer sumando es un número fijo (vale $-\tfrac12$; es una integral impropia convergente, U §6.5, pero su valor no importa porque al derivar da $0$). Al segundo se le aplica el TFC1. Por tanto $F'(u)=\mathrm{sen}(\ln u)$ para todo $u>0$.
2. **Regla de la cadena** (U p. 79). Como $G(x)=e^x>0$ siempre, se puede usar el paso 1 con $u=e^x$:
   $$H'(x)=F'(e^x)\cdot(e^x)'=\mathrm{sen}(\ln e^x)\,e^x=e^x\,\mathrm{sen}\,x,$$
   porque $\ln e^x=x$.
3. **a) Falsa.** $e^x>0$, así que el signo de $H'$ es el de $\mathrm{sen}\,x$, que cambia (por ejemplo $H'<0$ en $(\pi,2\pi)$): $H$ no es creciente en $\mathbb R$.
4. **Segunda derivada** (producto):
   $$H''(x)=e^x\,\mathrm{sen}\,x+e^x\cos x=e^x(\mathrm{sen}\,x+\cos x).$$
5. **d) Falsa.** $H'(\pi)=e^\pi\,\mathrm{sen}\,\pi=0$ (punto crítico), pero $H''(\pi)=e^\pi(0-1)=-e^\pi<0$: en $\pi$ hay un **máximo** relativo (U Prop. 3.7, p. 131), no un mínimo.
6. **c) Falsa.** $H''(0)=e^0(0+1)=1>0$ y $H''(\pi)<0$: $H''$ cambia de signo, así que $H$ no es cóncava en todo $\mathbb R$ (U Prop. 3.10, p. 136).
7. **b) Verdadera.** En $x=\frac{3\pi}4$: $\mathrm{sen}\frac{3\pi}4=\frac{\sqrt2}2$ y $\cos\frac{3\pi}4=-\frac{\sqrt2}2$, luego $H''\!\left(\frac{3\pi}4\right)=0$. Tercera derivada:
   $$H'''(x)=e^x(\mathrm{sen}\,x+\cos x)+e^x(\cos x-\mathrm{sen}\,x)=2e^x\cos x,$$
   y $H'''\!\left(\frac{3\pi}4\right)=2e^{3\pi/4}\left(-\frac{\sqrt2}2\right)=-\sqrt2\,e^{3\pi/4}<0$. Por U Prop. 3.12 (p. 137), la primera derivada no nula tras la segunda es de orden 3 (impar): **hay inflexión**, y como es negativa, $H$ pasa de convexa a cóncava. (Comprobación con el signo: $H''\!\left(\frac{3\pi}4-0{,}1\right)\approx1{,}35>0$ y $H''\!\left(\frac{3\pi}4+0{,}1\right)\approx-1{,}65<0$.)
8. **Respuesta: b).**

**Receta.** Si $H(x)=F(g(x))$ con $F(u)=\int_a^u f(t)\,dt$: $H'(x)=f(g(x))\,g'(x)$ (TFC1 + regla de la cadena). Después se trabaja con $H'$ como con cualquier función.

**Error típico.** Escribir $H'(x)=\mathrm{sen}(\ln e^x)$ olvidando multiplicar por $(e^x)'=e^x$; o dar por buena la inflexión solo con $H''=0$ sin comprobar el cambio de signo (o $H'''\ne0$).

sympy: $H'=e^x\,\mathrm{sen}\,x$; $H''=\sqrt2\,e^x\,\mathrm{sen}(x+\frac\pi4)$, que se anula en $\frac{3\pi}4$; $H'''\!\left(\frac{3\pi}4\right)=-\sqrt2\,e^{3\pi/4}$; $H''(\pi)=-e^\pi$; $\int_0^1\mathrm{sen}(\ln t)\,dt=-\frac12$.

---

### Ejercicio 6.15 (E p. 221)

> Sea $f:\mathbb R\to\mathbb R$ una función integrable en $\mathbb R$. Sean $a:\mathbb R\to\mathbb R$ y $b:\mathbb R\to\mathbb R$ funciones derivables en $\mathbb R$. Demuestra que
> $$\frac{d}{dx}\left(\int_{a(x)}^{b(x)}f(t)\,dt\right)=f(b(x))\,b'(x)-f(a(x))\,a'(x).$$
> Aplica el resultado para calcular el valor de $\displaystyle\frac{d}{dx}\left(\int_{x^2}^{e^x}\cos t\,dt\right)$.

**Antes de calcular**
- **Qué me piden:** probar la fórmula general para derivar una integral con los dos límites variables y aplicarla a un caso.
- **Cómo lo pienso:** partir la integral en un punto fijo $c$; así quedan dos integrales con un solo límite variable cada una, que ya sé derivar (TFC1, cambio de orden y regla de la cadena).
- **Qué uso:** aditividad (P5) y cambio de orden (P6) (U p. 240); TFC1 (U Teor. 6.1, p. 243); regla de la cadena (U p. 79). Para usar el TFC1 hace falta $f$ **continua**, así que se trabaja con $f$ continua.
- **Por dónde empiezo:** definir $\Phi(u)=\int_c^u f(t)\,dt$.

**Demostración.**
1. **Una función auxiliar.** Se fija un número $c\in\mathbb R$ (por ejemplo $c=0$) y se define $\Phi(u)=\int_c^u f(t)\,dt$. Como $f$ es continua, por el TFC1 (U p. 243), $\Phi'(u)=f(u)$ para todo $u$.
2. **Escribir la integral con $\Phi$.** Por aditividad (P5) y cambio de orden (P6) (U p. 240):
   $$\int_{a(x)}^{b(x)}f(t)\,dt=\int_{a(x)}^{c}f(t)\,dt+\int_c^{b(x)}f(t)\,dt=-\int_c^{a(x)}f(t)\,dt+\int_c^{b(x)}f(t)\,dt=\Phi(b(x))-\Phi(a(x)).$$
   (Las propiedades valen para cualquier orden de los extremos, por eso no importa dónde caiga $c$.)
3. **Derivar con la regla de la cadena** (U p. 79). $\Phi(b(x))$ es la composición de $\Phi$ con $b$: su derivada es $\Phi'(b(x))\,b'(x)=f(b(x))\,b'(x)$. Igual para $a$:
   $$\frac{d}{dx}\int_{a(x)}^{b(x)}f(t)\,dt=f(b(x))\,b'(x)-f(a(x))\,a'(x).\qquad\blacksquare$$
4. **Casos particulares** (para ver que no es nada nuevo): con $a(x)=c$ constante y $b(x)=x$ sale $f(x)$ (TFC1); con $a(x)=x$, $b(x)=c$ sale $-f(x)$ (E 6.14).

**Aplicación.**
5. **Identificar las piezas.** $f(t)=\cos t$ (continua en $\mathbb R$), $b(x)=e^x$, $b'(x)=e^x$, $a(x)=x^2$, $a'(x)=2x$.
6. **Sustituir en la fórmula:**
   $$\frac{d}{dx}\int_{x^2}^{e^x}\cos t\,dt=\cos(e^x)\,e^x-\cos(x^2)\cdot2x=e^x\cos(e^x)-2x\cos(x^2).$$
7. **Comprobación con Barrow.** $\int_{x^2}^{e^x}\cos t\,dt=\mathrm{sen}(e^x)-\mathrm{sen}(x^2)$; derivando con la regla de la cadena se obtiene lo mismo.

**Receta.** $\dfrac{d}{dx}\displaystyle\int_{a(x)}^{b(x)}f=f(\text{arriba})\cdot(\text{arriba})'-f(\text{abajo})\cdot(\text{abajo})'$. Se demuestra partiendo la integral en un punto fijo.

**Error típico.** Olvidar los factores $b'(x)$ y $a'(x)$ (contestar $\cos(e^x)-\cos(x^2)$) o el signo menos del límite inferior.

sympy: $\frac{d}{dx}\int_{x^2}^{e^x}\cos t\,dt-\big(e^x\cos(e^x)-2x\cos(x^2)\big)=0$.

---

## 2. Así lo preguntan en el examen (X)

Orden: **X p. 109-110** (igual que E 6.13) **→ X p. 107 → X p. 144** (V/F de monotonía de $F$) **→ X p. 119 → X p. 112-113** (Barrow directo) **→ X p. 115-116** (Barrow con integrando no acotado en un extremo).

---

### X p. 109-110 (Examen 1 «elaborado con exámenes de asignaturas similares», Ejercicio 4)

> Dada la función $F(x)=\displaystyle\int_0^x t\,\mathrm{sen}\,t\,dt$ definida en $[0,\infty)$ señale la opción correcta: **A)** $F$ es creciente; **B)** $F$ tiene un máximo en $x=7\pi$; **C)** $F$ es decreciente; **D)** Ninguna de las anteriores.

**Antes de calcular**
- **Qué me piden:** lo mismo que en E 6.13: monotonía de $F$ y tipo de punto en $7\pi$.
- **Cómo lo pienso:** $F'=$ integrando (TFC1); signo de $F'$ para la monotonía y $F''$ para clasificar.
- **Qué uso:** TFC1 (U Teor. 6.1, p. 243); U Prop. 2.4 (p. 98) y Prop. 3.7 (p. 131).
- **Por dónde empiezo:** $F'(x)=x\,\mathrm{sen}\,x$.

1. **TFC1:** $F'(x)=x\,\mathrm{sen}\,x$ ($t\,\mathrm{sen}\,t$ es continua).
2. **A) y C) falsas:** el signo de $F'$ en $x>0$ es el de $\mathrm{sen}\,x$, que cambia (positivo en $(0,\pi)$, negativo en $(\pi,2\pi)$).
3. **$7\pi$ es crítico:** $F'(7\pi)=7\pi\,\mathrm{sen}(7\pi)=0$.
4. **Clasificar:** $F''(x)=\mathrm{sen}\,x+x\cos x$, $F''(7\pi)=-7\pi<0$ ⇒ máximo relativo.
5. **Respuesta: B).** Lo que se escribe en el examen: «$F'(x)=x\,\mathrm{sen}\,x$ por el TFC; cambia de signo, luego A y C falsas; $F'(7\pi)=0$, $F''(7\pi)=-7\pi<0$: máximo en $7\pi$. Respuesta B.»

**Receta.** Igual que E 6.13: $F'=f$, $F''=f'$.

**Error típico.** Elegir A) pensando que «la integral de algo que empieza positivo es creciente».

sympy: $F''(7\pi)=-7\pi$.

---

### X p. 107 (Examen de Electrónica, pregunta corta 4)

> (1 PUNTO) Razone la veracidad o falsedad de la siguiente afirmación: «Si $f$ es derivable y decreciente en $(0,\infty)$, entonces $F$ es decreciente en $(0,\infty)$, donde $F(x)=\int_0^x f(s)\,ds$.»

**Antes de calcular**
- **Qué me piden:** decidir si «$f$ decreciente ⇒ $F$ decreciente» y justificarlo.
- **Cómo lo pienso:** la monotonía de $F$ depende del **signo** de $F'=f$, no de si $f$ sube o baja. Una $f$ que baja pero sigue siendo positiva hace que $F$ **crezca**.
- **Qué uso:** TFC1 (U Teor. 6.1, p. 243); U Prop. 2.4 (p. 98).
- **Por dónde empiezo:** $F'(x)=f(x)$ y buscar una $f$ decreciente y positiva.

1. **Derivada de $F$.** $f$ es derivable, luego continua; por el TFC1, $F'(x)=f(x)$.
2. **Qué decide la monotonía de $F$.** Por U Prop. 2.4 (p. 98), $F$ decrece donde $F'=f<0$ y crece donde $f>0$. Que $f$ sea decreciente no dice nada sobre su signo.
3. **Contraejemplo.** $f(x)=e^{-x}$:
   - es derivable y decreciente en $(0,\infty)$, porque $f'(x)=-e^{-x}<0$;
   - es positiva y continua en $[0,\infty)$, así que $F(x)=\int_0^x e^{-s}\,ds$ existe, y por Barrow $F(x)=1-e^{-x}$;
   - $F'(x)=e^{-x}>0$: $F$ es **estrictamente creciente**, no decreciente.
4. **Conclusión: la afirmación es falsa.**
5. **Otra forma de verlo (con límite inferior $1$).** La idea «$f=\frac1x$ baja pero es positiva» también sirve si la integral empieza en $1$: $\int_1^x\frac{dt}t=\ln x$ es creciente aunque $\frac1x$ sea decreciente. Con límite inferior $0$ **no** puede usarse $\frac1x$, porque no está acotada cerca de $0$ y $\int_0^x\frac{dt}t$ no existe (diverge). Por eso, para el enunciado tal como está, el contraejemplo es $e^{-x}$.

**Receta.** En un V/F sobre la monotonía de $F(x)=\int_a^x f$: traducir a «signo de $f$». Si la hipótesis habla de la monotonía de $f$ y no de su signo, buscar un contraejemplo con $f$ que tenga el signo «contrario» al esperado ($e^{-x}$ es decreciente y positiva; $-e^{-x}$ es creciente y negativa) y que sea continua en el intervalo de integración, extremo incluido.

**Error típico.** Confundir «$f$ decreciente» con «$f$ negativa»; o proponer un contraejemplo cuya integral desde $0$ no existe.

sympy: $\int_0^x e^{-s}ds=1-e^{-x}$; $\int_1^x\frac{dt}t=\ln x$; $\int_0^x\frac{dt}t=\infty$.

---

### X p. 144 (Febrero 2018, 1ª semana, I. Electrónica Industrial y Automática, pregunta corta 3)

> (1 PUNTO) Razone la veracidad o falsedad de la siguiente afirmación: «Si $f$ es continua y creciente en $(0,\infty)$, entonces la función $F(x)=\int_0^x f(t)\,dt$ es creciente en $(0,\infty)$».

**Antes de calcular**
- **Qué me piden:** decidir si «$f$ creciente ⇒ $F$ creciente».
- **Cómo lo pienso:** es el espejo del anterior: $F$ crece donde $f>0$. Una $f$ creciente pero negativa hace que $F$ **decrezca**.
- **Qué uso:** TFC1 (U Teor. 6.1, p. 243); U Prop. 2.4 (p. 98).
- **Por dónde empiezo:** buscar una $f$ creciente y negativa, continua también en $0$.

1. **TFC1:** $F'(x)=f(x)$, así que $F$ crece donde $f>0$ y decrece donde $f<0$ (U Prop. 2.4, p. 98).
2. **Contraejemplo.** $f(x)=-e^{-x}$:
   - es continua y creciente en $(0,\infty)$: $f'(x)=e^{-x}>0$;
   - es negativa, y continua también en $0$, así que $F(x)=\int_0^x(-e^{-t})\,dt=e^{-x}-1$ existe;
   - $F'(x)=-e^{-x}<0$: $F$ es **estrictamente decreciente**.
3. **Conclusión: la afirmación es falsa.**
4. **Otra forma de verlo (con límite inferior $1$).** $f(t)=-\frac1{t^2}$ es creciente y negativa en $(0,\infty)$; con la integral desde $1$, $\int_1^x\left(-\frac1{t^2}\right)dt=\frac1x-1$, que es decreciente. Desde $0$ no sirve: $-\frac1{t^2}$ no está acotada cerca de $0$ y la integral no existe.

**Receta.** La que se ha visto en X p. 107: monotonía de $F$ = signo de $f$; el contraejemplo debe ser integrable desde el límite inferior que da el enunciado.

**Error típico.** Pensar que $F$ «hereda» la monotonía de $f$. Lo que hereda $F$ de la monotonía de $f$ es la **convexidad** ($F''=f'\ge0$ ⇒ $F$ convexa, U Prop. 3.10, p. 136), no el crecimiento.

sympy: $\int_0^x(-e^{-t})dt=e^{-x}-1$; $\int_1^x(-t^{-2})dt=\frac1x-1$.

---

### X p. 119 (Examen 4 «elaborado con exámenes de asignaturas similares», Ejercicio 4)

> Señale el valor de $\displaystyle\int_0^\pi\cos x\,\sqrt[3]{\mathrm{sen}\,x}\,dx$: **A)** $0$; **B)** $1$; **C)** $\pi$; **D)** Ninguna de las anteriores.

**Antes de calcular**
- **Qué me piden:** el valor de una integral definida.
- **Cómo lo pienso:** el integrando es «potencia de $\mathrm{sen}\,x$ por la derivada de $\mathrm{sen}\,x$»: su primitiva es la potencia siguiente dividida por el nuevo exponente. Luego Barrow.
- **Qué uso:** Barrow (U Teor. 6.2, p. 244); regla de la cadena (U p. 79) para comprobar la primitiva.
- **Por dónde empiezo:** proponer $F(x)=\frac34(\mathrm{sen}\,x)^{4/3}$ y derivarla.

1. **Continuidad.** $\sqrt[3]{\ }$ está definida y es continua en todo $\mathbb R$ (también en $0$ y en negativos), y $\cos x$, $\mathrm{sen}\,x$ son continuas: el integrando es continuo en $[0,\pi]$. Barrow es aplicable.
2. **Primitiva.** $\cos x\,(\mathrm{sen}\,x)^{1/3}$ tiene la forma $u^{1/3}u'$ con $u=\mathrm{sen}\,x$. Se propone $F(x)=\frac34(\mathrm{sen}\,x)^{4/3}$ y se comprueba derivando con la regla de la cadena:
   $$F'(x)=\frac34\cdot\frac43(\mathrm{sen}\,x)^{1/3}\cos x=\cos x\,\sqrt[3]{\mathrm{sen}\,x}.\ \checkmark$$
3. **Barrow:** $F(\pi)-F(0)=\frac34(\mathrm{sen}\,\pi)^{4/3}-\frac34(\mathrm{sen}\,0)^{4/3}=0-0=0$.
4. **Por qué sale $0$ (comprobación de sentido).** En $[0,\frac\pi2]$ el integrando es $\ge0$ y en $[\frac\pi2,\pi]$ es $\le0$ (porque $\cos x\le0$ y $\mathrm{sen}\,x\ge0$); por la simetría $x\mapsto\pi-x$ (cambia el signo de $\cos$ y deja igual el $\mathrm{sen}$) las dos áreas son iguales y se cancelan.
5. **Respuesta: A).**

**Receta.** Integrando de la forma $u^r\,u'$ ($r\ne-1$): primitiva $\frac{u^{r+1}}{r+1}$; comprobar derivando y aplicar Barrow.

**Error típico.** Confundir el valor de la integral (área con signo, aquí $0$) con el área total (que sería $2\cdot\frac34=\frac32$).

sympy: $F'=\cos x\,\sqrt[3]{\mathrm{sen}\,x}$; $F(\pi)-F(0)=0$; integración numérica $\approx0$.

---

### X p. 112-113 (Examen 2 «elaborado con exámenes de asignaturas similares», Ejercicio 3)

> Señale el área comprendida entre la gráfica de $\mathrm{tg}\,x$; las rectas $x=0$, $x=\frac\pi4$; y el eje $x$: **A)** $\frac{\ln2}2$; **B)** $\frac{\ln4}4$; **C)** $\frac{\pi^2}4$; **D)** Ninguna de las anteriores.

**Antes de calcular**
- **Qué me piden:** un área bajo una curva entre $x=0$ y $x=\frac\pi4$.
- **Cómo lo pienso:** si la función es $\ge0$ en el intervalo, el área es directamente la integral. $\mathrm{tg}\,x=\frac{\mathrm{sen}\,x}{\cos x}$ es «menos la derivada del denominador entre el denominador»: su primitiva es $-\ln|\cos x|$.
- **Qué uso:** integral como área (U §6.1, p. 238); Barrow (U Teor. 6.2, p. 244); regla de la cadena para comprobar la primitiva (U p. 79).
- **Por dónde empiezo:** comprobar el signo y la continuidad de $\mathrm{tg}\,x$ en $[0,\frac\pi4]$.

1. **Signo y continuidad.** En $[0,\frac\pi4]$, $\cos x\ge\frac{\sqrt2}2>0$ y $\mathrm{sen}\,x\ge0$: $\mathrm{tg}\,x$ es continua y $\ge0$. El área pedida es $\int_0^{\pi/4}\mathrm{tg}\,x\,dx$.
2. **Primitiva.** $F(x)=-\ln(\cos x)$ (en el intervalo $\cos x>0$, no hace falta valor absoluto). Comprobación: $F'(x)=-\frac{-\mathrm{sen}\,x}{\cos x}=\mathrm{tg}\,x$. ✓
3. **Barrow:**
   $$\int_0^{\pi/4}\mathrm{tg}\,x\,dx=-\ln\cos\frac\pi4+\ln\cos0=-\ln\frac{\sqrt2}2+\ln1=\ln\frac2{\sqrt2}=\ln\sqrt2=\frac{\ln2}2.$$
4. **Mirar todas las opciones.** $\frac{\ln4}4=\frac{\ln2^2}4=\frac{2\ln2}4=\frac{\ln2}2$: **B) es el mismo número** que A). C) $\frac{\pi^2}4\approx2{,}47$ no puede ser, porque en $[0,\frac\pi4]$ se tiene $0\le\mathrm{tg}\,x\le1$ y el área es $\le\frac\pi4\approx0{,}785$.
5. **Respuesta: A) y B)** (las dos valen $\frac{\ln2}2\approx0{,}347$).

**Receta.** Área bajo $f\ge0$ = $\int_a^b f$ con Barrow. Para $\frac{u'}{u}$ la primitiva es $\ln|u|$. Tras obtener el número, **simplificar todas las opciones** antes de descartar alguna (los logaritmos pueden aparecer escritos de varias formas).

**Error típico.** Olvidar el signo: la primitiva de $\mathrm{tg}\,x$ es $-\ln|\cos x|$, no $\ln|\cos x|$ (saldría un área negativa).

sympy: $\int_0^{\pi/4}\mathrm{tg}\,x\,dx=-\ln\frac{\sqrt2}2=\frac{\ln2}2\approx0{,}3466$; $\frac{\ln4}4-\frac{\ln2}2=0$.

---

### X p. 115-116 (Examen 3 «elaborado con exámenes de asignaturas similares», Ejercicio 3)

> Señale el valor de $\displaystyle\int_0^{\pi/2}\frac{\cos x}{\sqrt{\mathrm{sen}\,x}}\,dx$: A) $0$; B) $\frac\pi4$; C) $2$; D) Ninguno de los anteriores.

**Antes de calcular**
- **Qué me piden:** el valor de la integral.
- **Cómo lo pienso:** es otra vez «potencia de $\mathrm{sen}\,x$ por su derivada» ($(\mathrm{sen}\,x)^{-1/2}\cos x$), con primitiva $2\sqrt{\mathrm{sen}\,x}$. Pero en $x=0$ el denominador vale $0$: el integrando no está acotado y Barrow no se aplica directamente en $[0,\frac\pi2]$. Se aplica en $[\varepsilon,\frac\pi2]$ y se hace $\varepsilon\to0^+$.
- **Qué uso:** Barrow (U Teor. 6.2, p. 244) en $[\varepsilon,\frac\pi2]$; integral impropia de 2ª especie (U Def. 6.10, p. 275).
- **Por dónde empiezo:** comprobar la primitiva derivando.

1. **Dónde falla la continuidad.** En $(0,\frac\pi2]$, $\mathrm{sen}\,x>0$ y el integrando es continuo. En $x=0$, $\mathrm{sen}\,0=0$: el integrando no está definido y crece sin límite al acercarse a $0$ (por ejemplo, en $x=0{,}0001$ vale $\approx100$). Es una integral impropia de 2ª especie (U Def. 6.10, p. 275): $\int_0^{\pi/2}=\lim_{\varepsilon\to0^+}\int_\varepsilon^{\pi/2}$.
2. **Primitiva.** $F(x)=2\sqrt{\mathrm{sen}\,x}=2(\mathrm{sen}\,x)^{1/2}$. Comprobación con la regla de la cadena: $F'(x)=2\cdot\frac12(\mathrm{sen}\,x)^{-1/2}\cos x=\frac{\cos x}{\sqrt{\mathrm{sen}\,x}}$. ✓
3. **Barrow en $[\varepsilon,\frac\pi2]$** (ahí sí es continuo):
   $$\int_\varepsilon^{\pi/2}\frac{\cos x}{\sqrt{\mathrm{sen}\,x}}\,dx=2\sqrt{\mathrm{sen}\frac\pi2}-2\sqrt{\mathrm{sen}\,\varepsilon}=2-2\sqrt{\mathrm{sen}\,\varepsilon}.$$
4. **Límite.** Cuando $\varepsilon\to0^+$, $\mathrm{sen}\,\varepsilon\to0$, así que $2-2\sqrt{\mathrm{sen}\,\varepsilon}\to2$. La integral es convergente y vale $2$.
5. **Respuesta: C).** (Como $F$ es continua en $[0,\frac\pi2]$, el resultado coincide con $F(\frac\pi2)-F(0)=2-0$; pero el razonamiento correcto pasa por el límite, igual que en E 6.16 había que mirar la continuidad.)

**Receta.** Si el integrando no está acotado en un extremo del intervalo, integrar hasta $\varepsilon$ con Barrow y tomar el límite. Si la primitiva tiene límite finito en ese extremo, la integral converge y vale ese límite.

**Error típico.** Aplicar Barrow sin mirar el extremo $x=0$. Aquí la cuenta saldría bien, pero el mismo descuido en $\int_{-1}^1\frac{dx}{x^2}$ da $-2$, que es falso (Propio 2).

sympy: $\int_0^{\pi/2}\frac{\cos x}{\sqrt{\mathrm{sen}\,x}}dx=2$; $\lim_{\varepsilon\to0^+}2\sqrt{\mathrm{sen}\,\varepsilon}=0$.

---

## 3. Ejemplos propios (dificultad creciente)

### Propio 1 — Derivar una integral con límites variables y un límite con TFC1 (fácil-medio) [propio]

> a) Calcula $G'(x)$ para $G(x)=\displaystyle\int_x^{x^2}\frac{dt}{1+t^2}$ y el valor $G'(1)$.
> b) Calcula $\displaystyle\lim_{x\to0}\frac{1}{x^3}\int_0^x\mathrm{sen}(t^2)\,dt$.

**Antes de calcular**
- **Qué me piden:** en a), la derivada de una integral con los dos límites variables; en b), un límite $\frac00$ en el que el numerador es una integral.
- **Cómo lo pienso:** a) es la fórmula de E 6.15. En b) no se sabe calcular $\int\mathrm{sen}(t^2)\,dt$ con funciones elementales, pero no hace falta: L'Hôpital pide derivar el numerador, y eso lo da el TFC1.
- **Qué uso:** E 6.15 / TFC1 (U Teor. 6.1, p. 243); regla de la cadena (U p. 79); L'Hôpital (U §2.3, p. 82).
- **Por dónde empiezo:** identificar $f(t)=\frac1{1+t^2}$, $b(x)=x^2$, $a(x)=x$.

a)
1. $f(t)=\frac1{1+t^2}$ es continua en $\mathbb R$ (el denominador nunca es $0$).
2. Fórmula de E 6.15 con $b(x)=x^2$, $b'(x)=2x$, $a(x)=x$, $a'(x)=1$:
   $$G'(x)=\frac{1}{1+(x^2)^2}\cdot2x-\frac1{1+x^2}\cdot1=\frac{2x}{1+x^4}-\frac1{1+x^2}.$$
3. $G'(1)=\frac22-\frac12=\frac12$.
4. Comprobación con Barrow: $G(x)=\mathrm{arctg}(x^2)-\mathrm{arctg}\,x$; derivando sale lo mismo.

b)
5. **Tipo de límite.** Numerador: $N(x)=\int_0^x\mathrm{sen}(t^2)\,dt\to\int_0^0=0$ (P0, U p. 240; $N$ es continua por ser derivable). Denominador $x^3\to0$. Es $\frac00$.
6. **L'Hôpital** (U §2.3, p. 82). Por el TFC1, $N'(x)=\mathrm{sen}(x^2)$; y $(x^3)'=3x^2$:
   $$\lim_{x\to0}\frac{N(x)}{x^3}=\lim_{x\to0}\frac{\mathrm{sen}(x^2)}{3x^2}.$$
7. Con $u=x^2\to0$ y el límite fundamental $\lim_{u\to0}\frac{\mathrm{sen}\,u}u=1$: el límite es $\frac13$.

**Receta.** Integral con límite variable en un límite $\frac00$: L'Hôpital + TFC1 (la derivada del numerador es el integrando evaluado en $x$).

**Error típico.** En a), escribir $\frac1{1+x^2}$ para el límite superior (evaluar en $x$ en vez de en $x^2$) u olvidar el factor $2x$.

sympy: $G'(x)-\left(\frac{2x}{1+x^4}-\frac1{1+x^2}\right)=0$, $G'(1)=\frac12$; límite b) $=\frac13$.

---

### Propio 2 — Regla de Barrow y su hipótesis (medio) [propio]

> a) Calcula $\displaystyle\int_1^4\left(3\sqrt x-\frac{2}{x^2}\right)dx$.
> b) ¿Es correcto escribir $\displaystyle\int_{-1}^1\frac{dx}{x^2}=\left[-\frac1x\right]_{-1}^1=-2$?

**Antes de calcular**
- **Qué me piden:** una integral con Barrow y decidir si otra «cuenta» es válida.
- **Cómo lo pienso:** primero miro si el integrando es continuo en el intervalo. En a) sí ($x\ge1$); en b) no ($x=0$ está dentro). Además, en b) el resultado es negativo para una función positiva: imposible por monotonía.
- **Qué uso:** Barrow (U Teor. 6.2, p. 244); monotonía de la integral (U p. 240).
- **Por dónde empiezo:** escribir $3\sqrt x=3x^{1/2}$ y $\frac2{x^2}=2x^{-2}$.

a)
1. **Continuidad.** En $[1,4]$, $\sqrt x$ y $\frac1{x^2}$ son continuas (no hay $x=0$).
2. **Primitiva** de cada término con $\int x^r\,dx=\frac{x^{r+1}}{r+1}$ ($r\ne-1$):
   $3x^{1/2}\to3\cdot\frac{x^{3/2}}{3/2}=2x^{3/2}$; $\ -2x^{-2}\to-2\cdot\frac{x^{-1}}{-1}=\frac2x$. Así $F(x)=2x^{3/2}+\frac2x$. Comprobación: $F'(x)=3x^{1/2}-\frac2{x^2}$ ✓.
3. **Barrow:** $F(4)=2\cdot8+\frac12=\frac{33}2$, $F(1)=2+2=4$; resultado $\frac{33}2-4=\frac{25}2$.

b)
4. **No es correcto.** $\frac1{x^2}$ no está definida en $x=0\in[-1,1]$: no es continua en $[-1,1]$ y Barrow no se puede usar.
5. **Señal de alarma.** $\frac1{x^2}>0$, y por monotonía (U p. 240) la integral de una función positiva no puede ser $-2$. De hecho, cerca de $0$ la función no está acotada y la integral (impropia, U §6.5) diverge: $\int_\varepsilon^1\frac{dx}{x^2}=\frac1\varepsilon-1\to\infty$.

**Receta.** Barrow = (1) continuidad en $[a,b]$, (2) primitiva comprobada derivando, (3) $F(b)-F(a)$. Si el signo del resultado contradice el del integrando, hay un error de hipótesis.

**Error típico.** Aplicar Barrow a una función con un punto «prohibido» dentro del intervalo.

sympy: a) $\frac{25}2$; b) $\int_{-1}^1x^{-2}dx=\infty$.

---

### Propio 3 — Valor medio de una función (medio-difícil) [propio]

> Halla el valor medio $\frac1{b-a}\int_a^b f$ y todos los puntos $c\in[a,b]$ del teorema del valor medio integral para:
> a) $f(x)=x^2$ en $[0,3]$; b) $f(x)=\mathrm{sen}\,x$ en $[0,\pi]$.

**Antes de calcular**
- **Qué me piden:** la «altura media» de $f$ y dónde la alcanza $f$.
- **Cómo lo pienso:** el TVM integral dice que hay un rectángulo de base $b-a$ y altura $f(c)$ con la misma área que la de bajo la gráfica. Calculo esa altura con Barrow y resuelvo $f(c)=$ altura dentro del intervalo.
- **Qué uso:** TVM integral (U p. 244, margen; E 6.9); Barrow (U Teor. 6.2, p. 244); valor medio (L §4.4, p. 281).
- **Por dónde empiezo:** calcular $\int_a^b f$.

a)
1. $\int_0^3x^2\,dx=\left[\frac{x^3}3\right]_0^3=9$.
2. Valor medio: $\frac9{3-0}=3$.
3. $c^2=3\iff c=\pm\sqrt3$; solo $c=\sqrt3\approx1{,}73$ está en $[0,3]$.

b)
4. $\int_0^\pi\mathrm{sen}\,x\,dx=[-\cos x]_0^\pi=-(-1)+1=2$.
5. Valor medio: $\frac2\pi\approx0{,}637$.
6. $\mathrm{sen}\,c=\frac2\pi$ en $[0,\pi]$: como $0<\frac2\pi<1$, hay **dos** soluciones, $c_1=\arcsin\frac2\pi\approx0{,}690$ y $c_2=\pi-\arcsin\frac2\pi\approx2{,}451$ (el seno es simétrico respecto de $\frac\pi2$).

**Receta.** Valor medio $=\frac1{b-a}\int_a^bf$; los $c$ del TVM son las soluciones de $f(c)=$ valor medio **dentro** de $[a,b]$. El teorema garantiza al menos uno; puede haber varios.

**Error típico.** Olvidar dividir por $b-a$, quedarse con soluciones fuera del intervalo ($-\sqrt3$) o creer que $c$ es único.

sympy: a) $3$; b) $\frac2\pi$, $c_1\approx0{,}6901$, $c_2\approx2{,}4515$.

---

### Propio 4 — Integral con valor absoluto y función definida a trozos (difícil) [propio]

> a) Calcula $\displaystyle\int_{-1}^3\left|x^2-2x\right|dx$ y compárala con $\displaystyle\int_{-1}^3(x^2-2x)\,dx$.
> b) Calcula $\displaystyle\int_0^2 f(x)\,dx$ con $f(x)=\begin{cases}x^2,&0\le x\le1,\\2-x,&1<x\le2.\end{cases}$

**Antes de calcular**
- **Qué me piden:** integrales en las que la expresión cambia según el trozo del intervalo.
- **Cómo lo pienso:** el valor absoluto cambia de fórmula donde lo de dentro cambia de signo: parto el intervalo en esos puntos (aditividad) y en cada trozo quito el valor absoluto con el signo adecuado. En b) parto en $x=1$.
- **Qué uso:** aditividad (P5, U p. 240); Barrow (U Teor. 6.2, p. 244) en cada trozo.
- **Por dónde empiezo:** resolver $x^2-2x=0$.

a)
1. **Ceros y signo.** $x^2-2x=x(x-2)=0\iff x=0$ o $x=2$. Probando un punto de cada trozo: en $x=-\frac12$ vale $\frac54>0$; en $x=1$ vale $-1<0$; en $x=\frac52$ vale $\frac54>0$. Luego
   $|x^2-2x|=x^2-2x$ en $[-1,0]$ y $[2,3]$, y $|x^2-2x|=-(x^2-2x)$ en $[0,2]$.
2. **Partir** (P5) y usar la primitiva $F(x)=\frac{x^3}3-x^2$ de $x^2-2x$:
   - $\int_{-1}^0(x^2-2x)\,dx=F(0)-F(-1)=0-\left(-\frac13-1\right)=\frac43$;
   - $\int_0^2-(x^2-2x)\,dx=-(F(2)-F(0))=-\left(\frac83-4\right)=\frac43$;
   - $\int_2^3(x^2-2x)\,dx=F(3)-F(2)=0-\left(-\frac43\right)=\frac43$.
3. **Sumar:** $\int_{-1}^3|x^2-2x|\,dx=\frac43+\frac43+\frac43=4$.
4. **Sin valor absoluto:** $\int_{-1}^3(x^2-2x)\,dx=F(3)-F(-1)=0+\frac43=\frac43$. Es distinto porque aquí el trozo de $[0,2]$ (bajo el eje) **resta**: $\frac43-\frac43+\frac43$. La integral con $|\cdot|$ es el área total; sin él, el área con signo.

b)
5. **Continuidad.** Por la izquierda de $1$, $f\to1^2=1$; por la derecha, $2-1=1$; y $f(1)=1$. $f$ es continua en $[0,2]$, así que es integrable y en cada trozo se puede usar Barrow.
6. **Partir en $x=1$:** $\int_0^1x^2\,dx=\frac13$; $\int_1^2(2-x)\,dx=\left[2x-\frac{x^2}2\right]_1^2=2-\frac32=\frac12$.
7. **Sumar:** $\frac13+\frac12=\frac56$.

**Receta.** Valor absoluto o función a trozos: (1) puntos donde cambia la fórmula (ceros de lo de dentro del $|\cdot|$, o puntos de corte de la definición); (2) partir con la aditividad; (3) en cada trozo, fórmula sin $|\cdot|$ y Barrow; (4) sumar.

**Error típico.** Calcular $\left|\int_{-1}^3(x^2-2x)\,dx\right|=\frac43$ en lugar de $\int_{-1}^3|x^2-2x|\,dx=4$: el valor absoluto no «sale» de la integral.

sympy: a) $4$ (trozos $\frac43,-\frac43,\frac43$ antes de cambiar el signo), sin valor absoluto $\frac43$; b) $\frac56$.
