# Así lo preguntan en el examen: Tema 2.5 (Rolle, valor medio, funciones monótonas)

Fuente: **X** = *Exámenes resueltos de Cálculo* (`E:\UNED\CALCULO\Examenes-resueltos-Calculo.pdf`); se cita la página PDF. Todas las páginas se han leído **renderizadas como imagen** (PyMuPDF, 110 dpi), no del `.txt`.
Notación y resultados del tema (los mismos que en `temas/tema_2_5_rolle_valor_medio.html`):
- Teorema de Rolle (U p.95), Teorema del valor medio, TVM (U p.96), Teorema 2.4 de funciones constantes (U p.97), Definición 2.5 de monotonía y Proposición 2.4, «signo de $f'$ ⇒ monotonía» (U p.98), $x^3$ es estrictamente creciente aunque $f'(0)=0$ (U p.99), Bolzano (U §1.4, p.52).
- En U, «creciente» admite tramos planos ($\le$) y «estrictamente creciente» no ($<$).

Filas del índice con tema 2.5 o cercano (`indice_examenes_1..4.md`): X p.13, p.35, p.101, p.109-110, p.107, p.135, p.137; cercanas: p.22 y p.126 (Bolzano, unicidad), p.147 (Bolzano), p.86 (TVM en varias variables, tema 5: se omite). La p.109-110 ($f=e^{2x^2-x}$) es **el mismo ejercicio que E 2.48**, ya resuelto en el tema, así que no se repite. La p.107 (derivada de $F(x)=\int_0^x f$) necesita el Tema 6 y también se omite.

Orden: de fácil a difícil. Hay 6 problemas (el 5 junta dos preguntas V/F breves).

---

## Problema 1. Enunciar el TVM y explicar su interpretación geométrica

**Fuente:** `X p.137 (Febrero 2017, 1ª semana, I. Electrónica Industrial y Automática, pregunta corta 3, 1 punto)`.

**Enunciado.** Enuncie el Teorema del Valor Medio (para funciones de una variable) y explique la interpretación geométrica de este resultado.

**Solución impresa:** solo «Ver texto base (páginas 94 y 95)». Esas páginas corresponden a una edición anterior de U; en la edición de 2023 el TVM está en **U p.96**.

**Solución paso a paso.**
1. **Enunciado (U p.96).** Sea $f:[a,b]\to\mathbb R$ **continua en $[a,b]$** y **derivable en $(a,b)$**. Entonces existe al menos un $c\in(a,b)$ tal que
   $$f'(c)=\frac{f(b)-f(a)}{b-a}.$$
   Hay que escribir las dos hipótesis: sin ellas el enunciado es falso. Por ejemplo, $|x|$ en $[-1,2]$ es continua pero no derivable en $0$: la cuerda tiene pendiente $\tfrac13$ y $f'$ solo vale $\pm1$.
2. **Qué es cada lado.** El cociente $\dfrac{f(b)-f(a)}{b-a}$ es la pendiente de la **cuerda** (recta secante) que une $A=(a,f(a))$ con $B=(b,f(b))$. El número $f'(c)$ es la pendiente de la **recta tangente** a la gráfica en $(c,f(c))$.
3. **Interpretación geométrica.** Hay al menos un punto interior de la gráfica en el que la tangente es **paralela a la cuerda $AB$**, ya que dos rectas son paralelas si tienen la misma pendiente.
4. **Interpretación física (opcional, pero ayuda).** Si $f(t)$ es la posición en el instante $t$, el cociente es la velocidad media en $[a,b]$. El teorema dice que en algún instante $c$ la velocidad instantánea $f'(c)$ coincide con la media.
5. **Relación con Rolle (opcional).** Si además $f(a)=f(b)$, la cuerda es horizontal y se obtiene Rolle: $f'(c)=0$. Recíprocamente, el TVM se demuestra aplicando Rolle a $h(x)=f(x)-f(a)-\frac{f(b)-f(a)}{b-a}(x-a)$, es decir, a $f$ menos la recta de la cuerda (U pp.96-97).

**Receta.** Para «enuncie y explique», escribe las hipótesis (continua en el cerrado y derivable en el abierto), la fórmula con $c\in(a,b)$ abierto y la frase «tangente paralela a la cuerda», con un dibujo.
**Parte del tema que usa:** §3 del resumen (TVM, U p.96).
**Verificación:** no hay nada que calcular. El contraejemplo $|x|$ en $[-1,2]$ se comprueba a mano: pendiente $(2-1)/3=1/3$.
**Avisos:** la página que cita la solución impresa (94-95) es de una edición antigua de U; en la actual es p.96.

---

## Problema 2. Aplicar Rolle para encontrar una tangente horizontal

**Fuente:** `X p.135 (Febrero 2017, 2ª semana, I. Electrónica Industrial y Automática, pregunta corta 4, 1 punto)`.

**Enunciado.** Enuncie el Teorema de Rolle. Úselo para demostrar que, dada la función $f:[-2,0]\to\mathbb R$, $f(x)=e^{(x+1)^2}$, existe algún $c\in[-2,0]$ tal que la recta tangente a la gráfica de $f$ en $(c,f(c))$ es paralela al eje $x$.

**Solución paso a paso.**
1. **Enunciado (U p.95).** Si $f:[a,b]\to\mathbb R$ es continua en $[a,b]$, derivable en $(a,b)$ y $f(a)=f(b)$, entonces existe $c\in(a,b)$ con $f'(c)=0$.
2. **Traducir lo que se pide.** La tangente en $(c,f(c))$ es $y=f(c)+f'(c)(x-c)$. Es paralela al eje $x$ (horizontal) si y solo si su pendiente es $0$, es decir, $f'(c)=0$. Así que basta encontrar un $c$ con $f'(c)=0$, y eso es justo lo que da Rolle.
3. **Continuidad en $[-2,0]$.** $f=\exp\circ g$ con $g(x)=(x+1)^2$, que es un polinomio. La composición de funciones continuas es continua, así que $f$ es continua en todo $\mathbb R$ y, en particular, en $[-2,0]$.
4. **Derivabilidad en $(-2,0)$.** Por la regla de la cadena, $f$ es derivable en $\mathbb R$ y $f'(x)=2(x+1)\,e^{(x+1)^2}$.
5. **Mismo valor en los extremos.** $f(-2)=e^{(-1)^2}=e$ y $f(0)=e^{1^2}=e$. Coinciden.
6. **Aplicar Rolle.** Se cumplen las tres hipótesis, así que existe $c\in(-2,0)$ con $f'(c)=0$, y en ese punto la tangente es horizontal.
7. **(Comprobación, no se pide.)** Como $e^{(x+1)^2}>0$, $f'(c)=0\iff c+1=0\iff c=-1\in(-2,0)$. La tangente es $y=f(-1)=e^0=1$.

**Receta.** «Tangente paralela al eje $x$» significa $f'(c)=0$. Comprueba las tres hipótesis de Rolle (la continuidad y la derivabilidad salen de las reglas de composición) y calcula $f(a)=f(b)$.
**Parte del tema que usa:** §2 del resumen (Rolle, U p.95), igual que E 2.39.
**Verificación (sympy):** $f(0)=f(-2)=e$; $f'(x)=2(x+1)e^{(x+1)^2}$; `solve(f'(x)=0)` da $[-1]$.
**Avisos:**
- El enunciado y la solución impresa escriben $c\in[-2,0]$ (cerrado). Rolle garantiza más: $c\in(-2,0)$ (abierto). No es un error, porque lo que se pide es más débil, pero en el examen conviene escribir el abierto.
- La solución impresa remite a «ejercicio 87 del libro de problemas», que es la numeración de un libro antiguo. El análogo en E es el **Ej. 2.39** (E p.76).
- **Error típico:** decir «paralela al eje $y$», que sería una tangente vertical (ver E 2.39).

---

## Problema 3. Intervalos de crecimiento de $x^2e^{1-x}$

**Fuente:** `X p.101 (sin fecha; I. Electrónica Industrial y Automática, examen «Electrónica 2» del índice, pregunta corta 2, 1 punto)`.

**Enunciado.** Calcule los intervalos de crecimiento y decrecimiento de la función dada por $f(x)=x^2e^{(1-x)}$.

**Solución paso a paso** (receta «intervalos de monotonía» del tema).
1. **Dominio y derivabilidad.** $f$ es producto de un polinomio y de $e^{1-x}$, ambos derivables en $\mathbb R$, así que $f$ es derivable en $\mathbb R$. No hay puntos sin derivada que separar.
2. **Derivar** (producto y cadena, $(e^{1-x})'=-e^{1-x}$):
   $$f'(x)=2x\,e^{1-x}-x^2e^{1-x}=x(2-x)\,e^{1-x}.$$
3. **Quitar el factor de signo fijo.** $e^{1-x}>0$ para todo $x$, así que el signo de $f'$ es el de $x(2-x)$.
4. **Ceros:** $x=0$ y $x=2$. Dividen $\mathbb R$ en $(-\infty,0)$, $(0,2)$ y $(2,\infty)$.
5. **Signo en cada intervalo** (con un punto de prueba):
   - $x=-1$: $(-1)\cdot 3<0$, así que $f'<0$ en $(-\infty,0)$;
   - $x=1$: $1\cdot 1>0$, así que $f'>0$ en $(0,2)$;
   - $x=3$: $3\cdot(-1)<0$, así que $f'<0$ en $(2,\infty)$.
6. **Aplicar la Prop. 2.4 (U p.98).** $f$ es **estrictamente decreciente en $(-\infty,0)$ y en $(2,\infty)$**, y **estrictamente creciente en $(0,2)$**. Como $f$ es continua, se pueden incluir los extremos: estrictamente decreciente en $(-\infty,0]$ y en $[2,\infty)$, estrictamente creciente en $[0,2]$ (variante de Larson, Teorema 3.5, del tema).
7. **(Extra, Tema 3.)** En $0$ la función pasa de bajar a subir: mínimo relativo, con $f(0)=0$. En $2$ pasa de subir a bajar: máximo relativo, con $f(2)=4/e$ (U Prop. 3.5).
8. **Cuidado al redactar:** no escribas «decreciente en $(-\infty,0)\cup(2,\infty)$». Ser decreciente en cada intervalo **no** implica ser decreciente en la unión (error típico de E 2.44), y aquí de hecho es falso: $-0{,}1<3$ y, sin embargo, $f(-0{,}1)=0{,}01\,e^{1{,}1}\approx0{,}030<f(3)=9e^{-2}\approx1{,}218$. Lo correcto es nombrar cada intervalo por separado.

**Receta.** Deriva y factoriza, quita las exponenciales (siempre positivas), haz la tabla de signos con los ceros y aplica la Prop. 2.4 en cada intervalo por separado.
**Parte del tema que usa:** §5 del resumen (Prop. 2.4, U p.98). Mismo método que el ejemplo de U $xe^{1-x}$ (U pp.99-100) y E 2.48.
**Verificación (sympy):** `factor(diff(x**2*exp(1-x)))` da $-x(x-2)e^{1-x}$, con ceros $\{0,2\}$; $f(2)=4e^{-1}$.
**Avisos (errata en la solución impresa):** la solución impresa dice «$f'(x)$ será *negativa* si $x$ es menor que *1* o mayor que 2 y *negativa* si $x$ está entre 0 y 2». Hay dos erratas: debe decir «menor que **0**» y, en el segundo caso, «**positiva**». La conclusión impresa (estrictamente creciente en $(0,2)$, estrictamente decreciente en $(-\infty,0)$ y $(2,\infty)$) sí es correcta.

---

## Problema 4. Monotonía de $x^3e^x$: un cero de $f'$ que no cambia de signo

**Fuente:** `X p.13 (Febrero 2011, 2ª semana, Ingeniería Mecánica, Modelo B, pregunta corta 2, 1 punto)`. Pregunta gemela más fácil: `X p.35 (Febrero 2013, 2ª semana, Ingeniería Mecánica, Modelo B, pregunta corta 1)`, «¿Dónde es creciente $f(x)=xe^x$?». Allí $f'(x)=(1+x)e^x$, así que es creciente (de hecho estrictamente) en $[-1,\infty)$.

**Enunciado.** Determine los intervalos de crecimiento y decrecimiento de la función dada por $f(x)=x^3e^x$.

**Solución paso a paso.**
1. **Derivabilidad.** Es producto de un polinomio por $e^x$, así que es derivable en $\mathbb R$.
2. **Derivar y factorizar:** $f'(x)=3x^2e^x+x^3e^x=x^2(x+3)\,e^x$.
3. **Factores de signo fijo.** $e^x>0$ y $x^2\ge0$, y $x^2$ solo se anula en $x=0$. Por tanto, para $x\ne0$, el signo de $f'$ es el de $x+3$.
4. **Ceros de $f'$:** $x=-3$ (simple: $f'$ **cambia** de signo) y $x=0$ (doble: $f'$ **no cambia** de signo, porque es $>0$ a ambos lados).
5. **Tabla de signos:**
   - en $(-\infty,-3)$: $f'<0$ (en $x=-4$: $16\cdot(-1)\cdot e^{-4}<0$);
   - en $(-3,0)$: $f'>0$ (en $x=-1$: $1\cdot2\cdot e^{-1}>0$);
   - en $(0,\infty)$: $f'>0$.
6. **Prop. 2.4 (U p.98) en cada intervalo.** $f$ es estrictamente decreciente en $(-\infty,-3)$ y estrictamente creciente en $(-3,0)$ y en $(0,\infty)$.
7. **Unir los trozos a través de $x=0$.** Aquí la Prop. 2.4 no basta tal cual, porque $f'(0)=0$. Se razona como U hace con $x^3$ (U p.99), o con la variante de Larson del tema. Como $f$ es continua, es estrictamente creciente en $[-3,0]$ y en $[0,\infty)$. Si $-3\le a<0<b$, entonces $f(a)<f(0)<f(b)$. Por tanto $f$ es **estrictamente creciente en $[-3,\infty)$** y **estrictamente decreciente en $(-\infty,-3]$**.
8. **(Extra.)** Hay un mínimo relativo (y absoluto) en $x=-3$, con $f(-3)=-27e^{-3}\approx-1{,}344$. En $x=0$ la tangente es horizontal, pero **no hay extremo** (punto de silla, como en $x^3$).

**Receta.** En la tabla de signos, un factor al cuadrado ($x^2$, $(x-a)^2$) no cambia el signo: su cero no separa la monotonía. Si $f'$ tiene el mismo signo a ambos lados de un cero aislado, los dos intervalos se unen.
**Parte del tema que usa:** §5 del resumen (Prop. 2.4; ejemplo de $x^3$, U p.99; variante de Larson; ejemplo B3 $x+\operatorname{sen}x$).
**Verificación (sympy):** `factor(diff(x**3*exp(x)))` da $x^2(x+3)e^x$; signos en $x=-4,-1,1$: $-,+,+$; $f(-3)\approx-1{,}3443$.
**Avisos:**
- La solución impresa da «creciente en $(-3,\infty)$ y decreciente en $(-\infty,-3)$». Es correcta y no parte el intervalo en $0$, que es lo que se quiere, pero no justifica por qué el cero de $f'$ en $x=0$ no rompe el crecimiento. La clave es su frase «$x^2e^x\ge0$», y conviene decirla explícitamente con el argumento del paso 7.
- En X p.35, la frase «es creciente cuando su derivada es mayor o igual que 0» usa una equivalencia: «$\Leftarrow$» es la Prop. 2.4, y «$\Rightarrow$» está en el error típico del tema (U pp.98-99). En un intervalo y con $f$ derivable, es correcta.

---

## Problema 5. Bolzano: ni da unicidad, ni sirve sin continuidad (dos V/F)

**Fuentes:**
- (a) `X p.22 (Febrero 2012, 2ª semana, Ingeniería Mecánica, Modelo B, pregunta corta 1, 1 punto)`.
- (b) `X p.126 (sin fecha; I. Electrónica Industrial y Automática, pregunta corta 2, 1 punto)`.

**Enunciados.**
(a) Sea $f:[-1,1]\to\mathbb R$ una función continua tal que $f(-1)=-3$ y $f(1)=3$. Razone si es cierto que la ecuación $f(x)=0$ tiene una única solución en el intervalo $[-1,1]$. Apóyese en la gráfica de una función con estas características si lo considera necesario.
(b) Razone la veracidad o falsedad de la siguiente afirmación: «Si $f:\mathbb R\to\mathbb R$ es estrictamente creciente y $f(-1)<0<f(1)$, entonces existe al menos una solución de la ecuación $f(x)=0$.»

**Solución paso a paso.**
1. **(a) Existencia.** $f$ es continua en $[-1,1]$ y $f(-1)f(1)=-9<0$. Por Bolzano (U p.52) existe al menos un $c\in(-1,1)$ con $f(c)=0$.
2. **(a) Unicidad: falsa.** Bolzano solo garantiza «al menos una». Contraejemplo de la solución impresa: $f(x)=3\operatorname{sen}\frac{5\pi x}{2}$. Es continua, $f(-1)=3\operatorname{sen}(-\tfrac{5\pi}2)=-3$ y $f(1)=3\operatorname{sen}\tfrac{5\pi}2=3$, pero se anula en $0$ y en $\tfrac25$ (de hecho en $0,\pm\tfrac25,\pm\tfrac45$: cinco soluciones). Uno polinómico: $p(x)=\tfrac32(5x^3-3x)$ cumple $p(\pm1)=\pm3$ y se anula en $0$ y $\pm\sqrt{3/5}$.
3. **(a) Qué habría que añadir para tener unicidad.** Que $f$ sea **estrictamente monótona** en $[-1,1]$. Si lo es, es inyectiva ($a<b\Rightarrow f(a)<f(b)$, luego $f(a)\ne f(b)$) y no puede anularse dos veces. Con $f$ derivable basta con $f'>0$ en $(-1,1)$ (Prop. 2.4, U p.98). Otra forma, con Rolle (U p.95): si hubiera dos ceros $r_1<r_2$, habría un $c\in(r_1,r_2)$ con $f'(c)=0$.
4. **(b) Falsa: la monotonía no sustituye a la continuidad.** Contraejemplo impreso: $f(x)=x$ si $x<0$ y $f(x)=x+1$ si $x\ge0$.
   - Es estrictamente creciente: dentro de cada trozo es $x$ o $x+1$. Si $a<0\le b$, entonces $f(a)=a<0<1\le b+1=f(b)$.
   - Cumple $f(-1)=-1<0<2=f(1)$.
   - No se anula: si $x<0$, $f(x)=x<0$; si $x\ge0$, $f(x)=x+1\ge1$.
   - El fallo está en que **no es continua en $0$** (el límite por la izquierda es $0$ y $f(0)=1$), y Bolzano exige continuidad.
5. **Conclusión conjunta.** Continuidad + cambio de signo da **existencia** (Bolzano). Estricta monotonía da **a lo sumo una** solución. Las dos juntas dan **exactamente una**.

**Receta.** «¿Única solución?»: existencia con Bolzano (comprueba la continuidad) y unicidad con estricta monotonía ($f'>0$ o $f'<0$) o con Rolle (dos ceros de $f$ darían un cero de $f'$). Para refutar, basta una gráfica que oscile o que salte.
**Parte del tema que usa:** Bolzano (U §1.4 p.52, prerrequisito del tema), Def. 2.5 y Prop. 2.4 (U p.98), receta «tantas raíces como ceros de $f'$» (ejemplo A3 del tema).
**Verificación (sympy):** $3\operatorname{sen}(5\pi x/2)$ vale $-3$ en $-1$ y $3$ en $1$, y se anula en $\{-\tfrac45,-\tfrac25,0,\tfrac25,\tfrac45\}\subset[-1,1]$. Para $p$: $p(\pm1)=\pm3$ y raíces $0,\pm\sqrt{0{,}6}$.
**Avisos:** la solución impresa de (a) cita «página 51 del libro Cálculo para Ingenieros» (edición antigua); en la de 2023 Bolzano está en U p.52. Ninguna de las dos preguntas es de §2.5 por sí sola: se incluyen porque el paso «unicidad = estricta monotonía o Rolle» es justo lo que aporta el tema. Si el redactor prefiere no salirse de §2.5, el Problema 5 puede ir como recuadro dentro del 6.

---

## Problema 6. Bolzano + monotonía: ¿cuántas soluciones tiene $e^x-x=2$?

**Fuente:** `X p.147 (Febrero 2019, 2ª semana, I. Electrónica Industrial y Automática, pregunta corta 4, 1 punto)`. El enunciado original solo pide la existencia; los pasos 4-7 son una **ampliación propia** que usa el tema 2.5 (y es como se pregunta el «número de raíces»).

**Enunciado (original).** Enuncie el Teorema de Bolzano y aplíquelo para demostrar que la ecuación $e^x-x=2$ tiene al menos una solución en el intervalo $[1,2]$.
**Ampliación (propia).** Demuestre que esa solución es única en $[1,2]$ y que la ecuación tiene exactamente dos soluciones reales.

**Solución paso a paso.**
1. **Pasar a la forma $f(x)=0$.** Sea $f(x)=e^x-x-2$. Resolver $e^x-x=2$ es resolver $f(x)=0$.
2. **Bolzano (U p.52).** Si $f:[a,b]\to\mathbb R$ es continua y $f(a)f(b)<0$, existe $c\in(a,b)$ con $f(c)=0$.
3. **Hipótesis.** $f$ es suma de funciones continuas, luego continua en $\mathbb R$. Además $f(1)=e-3\approx-0{,}28<0$ y $f(2)=e^2-4\approx3{,}39>0$. Por tanto existe $c\in(1,2)$ con $e^c-c=2$. Esto es lo que pedía el examen.
4. **Unicidad en $[1,2]$ (propia).** $f'(x)=e^x-1$. Si $x>0$, entonces $e^x>e^0=1$, porque la exponencial es estrictamente creciente. Así $f'>0$ en $(0,\infty)\supset[1,2]$, y por la Prop. 2.4 (U p.98) $f$ es estrictamente creciente en $[1,2]$: no puede anularse dos veces. La raíz es única: $c\approx1{,}1462$.
5. **Estudio en todo $\mathbb R$.** $f'(x)<0$ si $x<0$ y $f'(x)>0$ si $x>0$. Por la Prop. 2.4 y la continuidad en $0$ (como en el Problema 4), $f$ es estrictamente decreciente en $(-\infty,0]$ y estrictamente creciente en $[0,\infty)$. En cada uno de esos dos intervalos hay **como mucho una** raíz.
6. **Existencia de la segunda raíz.** $f(0)=1-0-2=-1<0$ y $f(-2)=e^{-2}+2-2=e^{-2}>0$. Por Bolzano hay una raíz en $(-2,0)$: $\approx-1{,}8414$.
7. **Conclusión.** Hay exactamente **dos** soluciones reales, una en $(-2,0)$ y otra en $(1,2)$. Otra forma, con Rolle (U p.95): si hubiera tres raíces $r_1<r_2<r_3$, Rolle en $[r_1,r_2]$ y en $[r_2,r_3]$ daría dos ceros distintos de $f'$, pero $f'(x)=e^x-1=0$ solo en $x=0$.

**Receta.** Para contar soluciones: (1) escribe $f(x)=0$; (2) estudia el signo de $f'$ para partir $\mathbb R$ en intervalos de estricta monotonía (en cada uno hay a lo sumo una raíz); (3) en cada intervalo, busca un cambio de signo para que Bolzano dé la existencia.
**Parte del tema que usa:** Prop. 2.4 (U p.98), Rolle (U p.95), receta «tantas raíces como ceros de $f'$» (ejemplo A3 del tema); Bolzano (U p.52) como prerrequisito.
**Verificación (sympy):** $f(1)\approx-0{,}2817$, $f(2)\approx3{,}3891$, $f(-2)\approx0{,}1353$ y $f(0)=-1$. Con nsolve salen $1{,}146193$ y $-1{,}841406$, y solve da exactamente dos raíces, $-2-W_0(-e^{-2})$ y $-2-W_{-1}(-e^{-2})$ ($W$ es la función de Lambert).
**Avisos:** la solución impresa concluye «existe al menos un $c\in[1,2]$»; Bolzano da el abierto $(1,2)$, que es más fuerte. En la misma página, la pregunta 3 (Taylor en $\sqrt3$) dice «derivadas en $x=2$» y llama $p_3$ a un polinomio de orden 2: son erratas ajenas a este tema.

---

## Tipos de pregunta del tema que caen en examen y no hay en el PDF

En X, el tema 2.5 apenas aparece, solo en preguntas cortas de 1 punto: enunciar Rolle o el TVM, aplicar Rolle a una función concreta y estudiar la monotonía por el signo de $f'$. **No hay** en el PDF, aunque el tema los enseña y E los trabaja (E 2.40-2.42, 2.45-2.47, 2.49):
- **Desigualdades con el TVM** (p. ej. $|\operatorname{sen}a-\operatorname{sen}b|\le|a-b|$, $\ln(1+x)<x$): en el tema solo hay ejemplos propios y de S.
- **Hallar el $c$ del TVM** para una función concreta (tipo Larson, $5-4/x$ en $[1,4]$).
- **Probar que una expresión es constante** porque su derivada es $0$ (Teorema 2.4, tipo E 2.45 d).
- **V/F sobre las hipótesis de Rolle o del TVM** con funciones a trozos o con $|\cdot|$ (tipo E 2.42, 2.49).
- **Número exacto de raíces de un polinomio** (tipo $x^3+3x+1=0$): en X solo aparece aquí como ampliación propia del Problema 6.
- El TVM en **varias variables** sí aparece en X (p.86, Septiembre 2017, Modelo A, P4), pero es del Tema 5.
