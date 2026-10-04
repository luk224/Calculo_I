# Problemas de examen real: Tema 2.2 Reglas de derivación

Fuente **X** = `E:\UNED\CALCULO\Examenes-resueltos-Calculo.pdf` (páginas = páginas PDF). Todos los enunciados y soluciones se han leído en la página renderizada del PDF, no en el `.txt`.

Filtrado de `indice_examenes_1..4.md`: filas con tema 2.2 → X p.25, 46, 52, 64, 96, 123, 139, 144. Las de «recta tangente» (p.4, 56, 106, 113) están clasificadas como 2.1 (solo usan $f'$ de un polinomio o de $\ln x$) y las de función implícita (p.30, 150) son de varias variables (5.x): se descartan.
Se eligen 6, de fácil a difícil y sin repetir tipo. Los tres problemas «$g=\text{(exterior)}(f(\text{interior}))$ con $f$ desconocida» (p.25, 123, 144) son del mismo tipo: se resuelve el de p.144 y los otros dos se dan como variantes.

Notación como en el tema: $\operatorname{sen}$, $\operatorname{arctg}$; «receta» = método reutilizable.

---

## Problema 1. Producto y cadena: $f(x)=x^2e^{\cos x}$

**Fuente:** `X p.96 (Septiembre 2018, Grado en Ing. Mecánica, Modelo A, pregunta corta 2, 1 punto)`.

**Enunciado.** Determine la derivada de la función
$$f(x)=x^2e^{\cos x}.$$

**Solución.**
1. **Última operación.** $f$ es un *producto* de $u(x)=x^2$ y $v(x)=e^{\cos x}$, así que manda la regla del producto: $f'=u'v+uv'$.
2. $u'(x)=2x$ (tabla: $(x^n)'=nx^{n-1}$).
3. $v(x)=e^{\cos x}$ es una *composición*: exterior $e^{(\cdot)}$, interior $\cos x$. Por la regla de la cadena, $v'(x)=e^{\cos x}\cdot(\cos x)'=e^{\cos x}(-\operatorname{sen}x)$.
4. Juntando: $f'(x)=2x\,e^{\cos x}+x^2e^{\cos x}(-\operatorname{sen}x)$.
5. Sacando factor común $e^{\cos x}$ (que nunca se anula):
$$\boxed{f'(x)=e^{\cos x}\,\bigl(2x-x^2\operatorname{sen}x\bigr)},\qquad x\in\mathbb R.$$
6. Dominio: $f$ es producto y composición de funciones derivables en todo $\mathbb R$, luego es derivable en todo $\mathbb R$.

**Receta.** Identifica la última operación (aquí producto); deriva cada factor por separado y, si un factor es una composición, aplica la cadena dentro.

**Parte del tema:** §3 regla del producto, §5 regla de la cadena, §6 tabla ($e^x$, $\cos$).

**Verificación:** sympy: la diferencia entre `diff(f)` y $e^{\cos x}(2x-x^2\operatorname{sen}x)$ simplifica a 0.

**Avisos:** coincide con la solución impresa. Error típico: olvidar el signo de $(\cos x)'=-\operatorname{sen}x$.

---

## Problema 2. Multicapa: $\operatorname{sen}\bigl[\cos^2(2/x)\bigr]$

**Fuente:** `X p.52 (Septiembre 2015, Grado en Ing. Mecánica, Modelo A, pregunta corta 2, 1 punto)`.

**Enunciado.** Calcular la derivada de la función $\operatorname{sen}\left[\cos^2\left(\dfrac{2}{x}\right)\right]$.

**Solución.**
1. **Dominio.** $2/x$ exige $x\neq0$; el resto ($\cos$, cuadrado, $\operatorname{sen}$) está definido en todo $\mathbb R$. Dominio: $\mathbb R\setminus\{0\}$, y ahí todas las capas son derivables.
2. **Capas** (de fuera hacia dentro), escribiendo $t=2/x$:
   - capa 1: $\operatorname{sen}(w)$, con $w=\cos^2 t$;
   - capa 2: $w=z^2$, con $z=\cos t$;
   - capa 3: $z=\cos t$;
   - capa 4: $t=2/x=2x^{-1}$.
   Cuatro capas, cuatro factores.
3. Derivada de cada capa, evaluada en lo que tiene dentro:
   - $(\operatorname{sen}w)'=\cos w=\cos\bigl[\cos^2(2/x)\bigr]$;
   - $(z^2)'=2z=2\cos(2/x)$;
   - $(\cos t)'=-\operatorname{sen}t=-\operatorname{sen}(2/x)$;
   - $(2x^{-1})'=-2x^{-2}=-\dfrac{2}{x^2}$.
4. Multiplicar (regla de la cadena repetida):
$$f'(x)=\cos\!\Bigl[\cos^2\tfrac2x\Bigr]\cdot2\cos\tfrac2x\cdot\Bigl(-\operatorname{sen}\tfrac2x\Bigr)\cdot\Bigl(-\tfrac{2}{x^2}\Bigr).$$
5. Los dos signos menos se cancelan y $2\cdot2=4$:
$$\boxed{f'(x)=\frac{4}{x^2}\cos\frac2x\,\operatorname{sen}\frac2x\,\cos\!\Bigl[\cos^2\frac2x\Bigr]},\qquad x\neq0.$$
   (Opcional: $2\operatorname{sen}a\cos a=\operatorname{sen}2a$ da $f'(x)=\frac{2}{x^2}\operatorname{sen}\frac4x\cos[\cos^2\frac2x]$.)

**Receta.** Con varias composiciones, escribe explícitamente las capas y multiplica una derivada por capa, cada una evaluada en lo que tiene dentro: $n$ capas, $n$ factores.

**Parte del tema:** §5 regla de la cadena (varias capas), §6 tabla; receta «capas» del tema.

**Verificación:** sympy: la diferencia con la fórmula impresa simplifica a 0.

**Avisos:** coincide con la impresa (que no indica el dominio $x\neq0$). Errores típicos: leer $\cos^2(2/x)$ como $\cos(\cos(2/x))$; perder la capa $2/x$ o su signo.

---

## Problema 3. Trigonométrica inversa + cadena: $\operatorname{arctg}\sqrt{x^2-1}-\operatorname{sen}^2 3x$

**Fuente:** `X p.46 (Septiembre 2014, Grado en Ing. Mecánica, Modelo A, pregunta corta 2, 1 punto)`.

**Enunciado.** Calcular la derivada de $f(x)=\operatorname{arctg}\sqrt{x^2-1}-\operatorname{sen}^2 3x$.

**Solución.**
1. **Dominio.** La raíz exige $x^2-1\ge0$, es decir $|x|\ge1$; $\operatorname{arctg}$ y $\operatorname{sen}^2 3x$ están definidas en todo $\mathbb R$. Dominio de $f$: $(-\infty,-1]\cup[1,\infty)$.
2. **Dónde vale la fórmula.** $\sqrt{u}$ solo es derivable para $u>0$ (su derivada $\frac1{2\sqrt u}$ no existe en $u=0$). La fórmula que obtengamos vale, pues, para $|x|>1$; en $x=\pm1$ la pendiente tiende a $\pm\infty$ (tangente vertical) y $f$ no es derivable.
3. **Primer sumando**, tres capas: $\operatorname{arctg}(s)$, $s=\sqrt u$, $u=x^2-1$.
   - $(\operatorname{arctg}s)'=\dfrac1{1+s^2}=\dfrac1{1+(x^2-1)}=\dfrac1{x^2}$;
   - $(\sqrt u)'=\dfrac1{2\sqrt u}=\dfrac1{2\sqrt{x^2-1}}$;
   - $(x^2-1)'=2x$.
   Producto: $\dfrac1{x^2}\cdot\dfrac{2x}{2\sqrt{x^2-1}}=\dfrac{1}{x\sqrt{x^2-1}}$.
4. **Segundo sumando**, tres capas: $w^2$, $w=\operatorname{sen}v$, $v=3x$:
   $(\operatorname{sen}^2 3x)'=2\operatorname{sen}3x\cdot\cos3x\cdot3=6\operatorname{sen}3x\cos3x\;(=3\operatorname{sen}6x)$.
5. Resta (la derivada de una diferencia es la diferencia de derivadas):
$$\boxed{f'(x)=\frac{1}{x\sqrt{x^2-1}}-6\operatorname{sen}3x\cos3x},\qquad |x|>1.$$
6. **Control del signo.** Al simplificar $\frac{2x}{2x^2}=\frac1x$ se conserva el signo de $x$: para $x<-1$ el primer término es negativo. Tiene sentido: si $x$ crece desde $-3$ hacia $-1$, $x^2-1$ disminuye y $\operatorname{arctg}\sqrt{x^2-1}$ decrece. Por eso **no** se puede escribir $\frac{1}{\sqrt{x^4-x^2}}$ (siempre positivo).

**Receta.** Separa sumandos; en cada uno, capas de fuera a dentro, usando $(\operatorname{arctg}u)'=\frac{u'}{1+u^2}$ y $(\sqrt u)'=\frac{u'}{2\sqrt u}$; simplifica $1+(\sqrt{\cdot})^2$ antes de multiplicar.

**Parte del tema:** §8 derivada de la arcotangente (función inversa), §5 cadena, §6 tabla, §10 dominio de $f'$ (puntos donde la fórmula falla).

**Verificación:** sympy: la diferencia con la fórmula impresa es 0 simbólicamente; además, numéricamente en $x=2,-2,1.5,-3$ (error $<10^{-15}$), lo que confirma que $\frac1{x\sqrt{x^2-1}}$ vale también para $x<-1$.

**Avisos:** el resultado impreso es correcto, pero (a) en el paso intermedio la tipografía muestra $\sqrt{x^2-1}^{\,2}$ (que es $x^2-1$); (b) la solución impresa **no indica el dominio** ni que $f$ no es derivable en $x=\pm1$. Error típico: escribir $\frac{1}{\sqrt{x^4-x^2}}$, que pierde el signo para $x<-1$.

---

## Problema 4. Cadena con función desconocida: $g(x)=\operatorname{sen}\bigl(f(5x^2-8)\bigr)$

**Fuente:** `X p.144 (Febrero 2018, Primera Semana, I. Electrónica Industrial y Automática, pregunta corta 2, 1 punto)`.

**Enunciado.** Sabiendo que $f$ es derivable y verifica $f(2)=\pi$ y $f'(2)=3$, calcular $g'(\sqrt2)$ siendo $g(x)=\operatorname{sen}\bigl(f(5x^2-8)\bigr)$.

**Solución.**
1. **Capas** de $g$: exterior $\operatorname{sen}$; media $f$; interior $u(x)=5x^2-8$. Las tres son derivables (la de $f$ es hipótesis), así que $g$ es derivable y la cadena se aplica.
2. **Cadena en general** (sin sustituir todavía):
$$g'(x)=\cos\bigl(f(5x^2-8)\bigr)\cdot f'(5x^2-8)\cdot10x.$$
3. **Evaluar el interior en el punto.** $u(\sqrt2)=5\cdot2-8=2$: justo el punto donde conocemos $f$ y $f'$ (señal de que vamos bien).
4. Sustituir: $g'(\sqrt2)=\cos\bigl(f(2)\bigr)\cdot f'(2)\cdot10\sqrt2=\cos\pi\cdot3\cdot10\sqrt2$.
5. Como $\cos\pi=-1$:
$$\boxed{g'(\sqrt2)=-30\sqrt2}.$$

**Receta.** Con una $f$ «desconocida» dentro de una composición: aplica la cadena en general, sustituye el punto y comprueba que el argumento de $f$ y de $f'$ es justo el punto donde te dan los datos.

**Parte del tema:** §5 regla de la cadena (receta «función desconocida»).

**Verificación:** sympy con $F$ simbólica: $g'(\sqrt2)=10\sqrt2\cos(F(2))F'(2)$; con $F(2)=\pi$, $F'(2)=3$ da $-30\sqrt2$.

**Avisos:** coincide con la impresa (que escribe «$(g(\sqrt2))'$» por $g'(\sqrt2)$: abuso de notación; la derivada de la constante $g(\sqrt2)$ sería 0). Error típico: escribir $f'(\sqrt2)$ en lugar de $f'(u(\sqrt2))=f'(2)$.

**Variantes del mismo tipo en X (para practicar):**
- `X p.25 (Septiembre 2012 original, Ing. Mecánica, Modelo A, pregunta corta 1, 1 punto)`: $f(0)=1$, $f'(0)=-2$, $g(x)=f^2(\operatorname{sen}x)$. Entonces $g'(x)=2f(\operatorname{sen}x)\,f'(\operatorname{sen}x)\cos x$ y $g'(0)=2\cdot1\cdot(-2)\cdot1=-4$. Coincide con la impresa. (Ojo: $f^2(\operatorname{sen}x)$ significa $[f(\operatorname{sen}x)]^2$, no $f(f(\operatorname{sen}x))$.)
- `X p.122 (enunciado) y p.123 (solución) («Examen 5», recopilación de asignaturas similares, ejercicio 4, test)`: $f(0)=\pi$, $f'(0)=2$, $g(x)=\cos\bigl(f(\cos x)\bigr)$. Entonces $g'(x)=-\operatorname{sen}\bigl(f(\cos x)\bigr)\,f'(\cos x)\,(-\operatorname{sen}x)=\operatorname{sen}\bigl(f(\cos x)\bigr)\,f'(\cos x)\operatorname{sen}x$ y $g'(\pi/2)=\operatorname{sen}\pi\cdot2\cdot1=0$: opción A. Coincide (la impresa tiene un paréntesis sin cerrar, errata tipográfica sin consecuencias). Verificado con sympy.

---

## Problema 5. Problema «al revés»: hallar $g'(2)$ a partir de $f(x)=x\,g(2x)$

**Fuente:** `X p.64 (Febrero 2016, Grado en Ing. Mecánica, Modelo B, pregunta corta 2, 1 punto)`.

**Enunciado.** Se sabe que $f$ y $g$ son funciones derivables, $g(2)=-1$, $f'(1)=2$ y que $f(x)=x\,g(2x)$. Calcule $g'(2)$. *Indicación:* aplique la regla de la cadena.

**Solución.**
1. **Última operación.** $f$ es el *producto* de $x$ por $g(2x)$; y $g(2x)$ es una composición (exterior $g$, interior $2x$).
2. **Derivar en general.** Producto: $f'(x)=1\cdot g(2x)+x\cdot\bigl(g(2x)\bigr)'$. Cadena: $\bigl(g(2x)\bigr)'=g'(2x)\cdot2$. Por tanto
$$f'(x)=g(2x)+2x\,g'(2x).$$
3. **Elegir el punto.** Queremos $g'(2)$, es decir $2x=2$, o sea $x=1$; y en $x=1$ conocemos $f'(1)$. Sustituimos $x=1$:
$$f'(1)=g(2)+2\,g'(2)\quad\Longrightarrow\quad 2=-1+2g'(2).$$
4. **Despejar:** $2g'(2)=3$, luego $\boxed{g'(2)=\tfrac32}$.

**Receta.** Deriva la relación en general (producto + cadena), elige el $x$ que hace que el argumento de la función desconocida sea el pedido, sustituye los datos y despeja.

**Parte del tema:** §3 producto, §5 cadena (receta «función desconocida»).

**Verificación:** sympy con $G$ simbólica: $f'(1)=G(2)+2G'(2)$; con $G(2)=-1$, $f'(1)=2$ resulta $G'(2)=3/2$.

**Avisos:** coincide con la impresa. Error típico: olvidar el factor 2 de la derivada interior y obtener $g'(2)=3$.

---

## Problema 6. Derivada segunda: $f(x)=\dfrac1{x^2+2x+1}+\cos(e^x)$

**Fuente:** `X p.139 (Septiembre 2018, Grado en Ing. Mecánica, Modelo B, pregunta corta 2, 1 punto)`. **El PDF no trae la solución** (el apartado «Solución:» está vacío).

**Enunciado.** Sea $f$ la función definida por
$$f(x)=\frac{1}{x^2+2x+1}+\cos(e^x).$$
¿Cuál es su derivada segunda?

**Solución.**
1. **Simplificar antes de derivar.** $x^2+2x+1=(x+1)^2$ (cuadrado de un binomio), así que $\dfrac1{x^2+2x+1}=(x+1)^{-2}$. Dominio: $x\neq-1$. Escribirlo como potencia evita aplicar dos veces la regla del cociente.
2. **Derivada primera, primer sumando** (cadena con interior $x+1$, de derivada 1): $\bigl((x+1)^{-2}\bigr)'=-2(x+1)^{-3}$.
3. **Derivada primera, segundo sumando** (cadena: exterior $\cos$, interior $e^x$): $\bigl(\cos e^x\bigr)'=-\operatorname{sen}(e^x)\cdot e^x$.
4. Por tanto $f'(x)=-2(x+1)^{-3}-e^x\operatorname{sen}(e^x)$.
5. **Derivada segunda** = derivada de $f'$ (definición de derivada segunda, U §3.1 p.104):
   - $\bigl(-2(x+1)^{-3}\bigr)'=6(x+1)^{-4}$;
   - $e^x\operatorname{sen}(e^x)$ es un *producto*: $\bigl(e^x\operatorname{sen}(e^x)\bigr)'=e^x\operatorname{sen}(e^x)+e^x\cdot\cos(e^x)\cdot e^x=e^x\operatorname{sen}(e^x)+e^{2x}\cos(e^x)$.
6. Restando:
$$\boxed{f''(x)=\frac{6}{(x+1)^4}-e^x\operatorname{sen}(e^x)-e^{2x}\cos(e^x)},\qquad x\neq-1.$$

**Receta.** Simplifica primero (factoriza el denominador y pásalo a potencia negativa); deriva una vez y, para la segunda, vuelve a mirar la última operación de cada término de $f'$ (aquí aparece un producto nuevo, $e^x\operatorname{sen}(e^x)$).

**Parte del tema:** §5 cadena, §3 producto, §6 tabla. La derivada segunda se define en U §3.1 p.104 (el tema 2.2 no la trata explícitamente; basta saber que es «derivar otra vez»).

**Verificación:** sympy: la diferencia entre `diff(f,x,2)` y la fórmula del recuadro simplifica a 0.

**Avisos:** sin solución impresa; la solución anterior es propia. Error típico: derivar $e^x\operatorname{sen}(e^x)$ como si fuera solo $e^x\cos(e^x)e^x$ (olvidar la regla del producto).

---

## Tipos de pregunta del tema que caen en examen y no hay en el PDF X

En el PDF de exámenes resueltos **no aparece ningún problema** de:
- **Derivada de la función inversa** en un punto, $(f^{-1})'(y_0)=1/f'(x_0)$ (p. ej. $f(x)=x^3+x$, $(f^{-1})'(2)=\tfrac14$), ni deducción de $(\arcsen)'$, $(\arccos)'$ (§8 del tema).
- **Derivación logarítmica** ($x^x$, $(\operatorname{sen}x)^{x}$…) (§9).
- **Derivación implícita en una variable** (tangente a una curva $F(x,y)=0$, p. ej. $x^2+y^2=9$): en X solo aparece como teorema de la función implícita en varias variables (p.30, p.150; tema 5.x).
- **Derivadas de $\operatorname{tg}$, $\sec$, $\operatorname{cotg}$** como pregunta propia (§7).
- **Dominio de $f'$ / puntos donde la fórmula falla** como pregunta explícita (§10); aparece implícitamente en el problema 3 ($x=\pm1$) y en preguntas de 2.1 tipo «¿es derivable $|x^2\operatorname{sen}x|$ en 0?» (X p.22, 69, 93).
- **Recta tangente**: sí sale en X, pero clasificada como 2.1 (X p.4, 56, 106, 113), con derivadas inmediatas.

Conviene cubrir estos tipos con los ejercicios de E del tema 2.2 (E 2.3-2.5, 2.10-2.13, 2.15-2.16) y ejemplos propios.
