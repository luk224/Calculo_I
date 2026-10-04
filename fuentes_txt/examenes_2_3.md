# Problemas de examen real: tema 2.3 Regla de L'Hôpital (indeterminaciones)

Fuente **X** = `E:\UNED\CALCULO\Examenes-resueltos-Calculo.pdf` (páginas = página PDF). Enunciados y soluciones impresas comprobados **viendo la página renderizada**. Cálculos verificados con sympy (`limit`, `diff`).
Notación y recetas del resumen `temas/tema_2_3_lhopital.html` (regla: U §2.3.2 p.82; formas $0\cdot\infty$, $\infty-\infty$, potencias: U pp.83-85; Prop. 2.2: U p.85).

Orden: de fácil a difícil, un tipo distinto en cada uno ($\tfrac00$ doble, $\tfrac\infty\infty$ con exponenciales, $\infty-\infty$, $0^0$, $1^\infty$, regla dentro de un problema de continuidad/derivabilidad).

---

## Problema 1. $\tfrac00$: aplicar la regla dos veces

**Fuente:** `X p.88 (Febrero 2018, Grado Ing. Mecánica, cód. 68031029, Modelo A, pregunta corta 2, 1 punto)`

**Enunciado.** Calcule el límite
$$\lim_{x\to0}\frac{e^x-x-1}{x^2}.$$

**Solución.**
1. **Sustituir primero.** Numerador: $e^0-0-1=0$; denominador: $0^2=0$. Es $\tfrac00$: se cumple la condición 1 de la lista de comprobación (U §2.3.2 p.82).
2. **Condiciones de la regla.** $f(x)=e^x-x-1$ y $g(x)=x^2$ son derivables en todo $\mathbb R$; $g'(x)=2x\neq0$ para $x\neq0$ (que sea $0$ en el propio $0$ no importa).
3. **Derivar arriba y abajo por separado** (no la regla del cociente): $\dfrac{f'(x)}{g'(x)}=\dfrac{e^x-1}{2x}$. Al sustituir vuelve a salir $\tfrac00$, así que todavía no sabemos si existe este límite.
4. **Segunda aplicación.** $e^x-1$ y $2x$ son derivables, $(2x)'=2\neq0$, y es $\tfrac00$:
$$\lim_{x\to0}\frac{e^x-1}{2x}=\lim_{x\to0}\frac{e^x}{2}=\frac12 .$$
5. **Subir la cadena.** Como el último límite existe ($=\tfrac12$), la regla garantiza que el del paso 3 vale $\tfrac12$, y por tanto también el original:
$$\lim_{x\to0}\frac{e^x-x-1}{x^2}=\frac12 .$$

**Receta.** Repite la regla mientras siga saliendo $\tfrac00$ o $\tfrac\infty\infty$, comprobando en cada paso que la derivada del denominador no se anula cerca del punto.

**Parte del tema.** Enunciado de la regla y «aplicarla más de una vez» (U §2.3.2 pp.82-83, Ej. 2.9 p.83).

**Verificación.** sympy: `limit((exp(x)-x-1)/x**2, x, 0)` $=1/2$.

**Avisos.** Solución impresa correcta. Justifica la condición con «$x^2$ y $2x$ no se anulan cerca de $0$»; lo exacto es que no se anulen las **derivadas del denominador** ($2x$ y $2$) en un entorno perforado de $0$, que también es cierto. *Alternativa con Taylor en el tema 3.1:* $e^x=1+x+\tfrac{x^2}2+o(x^2)$.

---

## Problema 2. $\tfrac\infty\infty$ con exponenciales (la trampa de «da vueltas»)

**Fuente:** `X p.10 (Febrero 2011, 1ª semana, Ing. Mecánica, Modelo A, pregunta corta 2, 1 punto)`

**Enunciado.** Calcule el valor del siguiente límite:
$$\lim_{x\to\infty}\frac{x+e^x}{2x+e^x}.$$

**Solución (con la regla, como el solucionario).**
1. **Tipo.** $x+e^x\to+\infty$ y $2x+e^x\to+\infty$: es $\tfrac\infty\infty$.
2. **Condiciones.** Numerador y denominador derivables en $\mathbb R$; $g'(x)=2+e^x>0$ siempre.
3. **Primera aplicación:** $\dfrac{1+e^x}{2+e^x}$, de nuevo $\tfrac\infty\infty$, y $(2+e^x)'=e^x\neq0$.
4. **Segunda aplicación:** $\dfrac{e^x}{e^x}=1$ para todo $x$, luego su límite es $1$.
5. Subiendo la cadena (cada límite existe porque existe el siguiente): $\displaystyle\lim_{x\to\infty}\frac{x+e^x}{2x+e^x}=1$.

**Solución alternativa (más segura, receta del tema para exponenciales).** Dividir arriba y abajo por el término dominante $e^x$:
$$\frac{x+e^x}{2x+e^x}=\frac{x/e^x+1}{2x/e^x+1}\longrightarrow\frac{0+1}{0+1}=1,$$
porque $\lim_{x\to\infty}x/e^x=\lim 1/e^x=0$ (regla, tipo $\tfrac\infty\infty$: «la exponencial gana siempre»).

**Receta.** Cociente de sumas con exponenciales en $\pm\infty$: divide por la exponencial dominante; usa la regla solo para los cocientes «potencia/exponencial» que queden.

**Parte del tema.** Regla para $\tfrac\infty\infty$ en $x\to\infty$ (U §2.3.2 p.82, nota al margen) y error típico «la regla da vueltas» (S §4.4 pp.304-305).

**Verificación.** sympy: `limit((x+exp(x))/(2*x+exp(x)), x, oo)` $=1$.

**Avisos (imprecisión del solucionario).** Escribe «el **numerador** no se anula si $x$ tiende a $\infty$» como condición de la regla. La hipótesis correcta es que **la derivada del denominador**, $g'(x)=2+e^x$, no se anule cerca de $\infty$ (lo cual se cumple). Aquí la regla funciona porque en el segundo paso $e^x/e^x$ se simplifica; en variantes como $\frac{e^x+e^{-x}}{e^x-e^{-x}}$ la regla da vueltas y hay que dividir.

---

## Problema 3. $\infty-\infty$: restar y aplicar la regla

**Fuente:** `X p.104 (examen sin fecha, I. Electrónica Industrial y Automática, pregunta corta 1, 1 punto)`

**Enunciado.** Calcule el límite
$$\lim_{x\to0}\left(\frac1x-\frac1{1-\cos x}\right).$$

**Solución.**
1. **Qué tipo es.** Por la derecha: $\frac1x\to+\infty$ y $\frac1{1-\cos x}\to+\infty$ ($1-\cos x>0$ para $0<|x|<2\pi$), así que es $\infty-\infty$. Por la izquierda: $\frac1x\to-\infty$, y queda $-\infty-(+\infty)=-\infty$, que **no** es indeterminado.
2. **Hacer la resta** (denominador común), como indica U p.83:
$$\frac1x-\frac1{1-\cos x}=\frac{1-\cos x-x}{x(1-\cos x)} .$$
En $x\to0$ es $\tfrac00$.
3. **Condiciones.** $f(x)=1-\cos x-x$ y $g(x)=x(1-\cos x)$ son derivables; $g'(x)=(1-\cos x)+x\operatorname{sen}x$. Para $0<|x|<\pi$: $1-\cos x>0$ y $x\operatorname{sen}x>0$ ($x$ y $\operatorname{sen}x$ tienen el mismo signo), luego $g'(x)>0$: no se anula cerca de $0$.
4. **Derivar:**
$$\frac{f'(x)}{g'(x)}=\frac{\operatorname{sen}x-1}{(1-\cos x)+x\operatorname{sen}x}.$$
Numerador $\to-1$; denominador $\to0$ **por valores positivos** (paso 3). Es «$\frac{-1}{0^+}$», que no es indeterminado: tiende a $-\infty$ por ambos lados.
5. **Conclusión.** La regla vale también si $\ell=-\infty$ (U p.82, $\ell\in\overline{\mathbb R}$):
$$\lim_{x\to0}\left(\frac1x-\frac1{1-\cos x}\right)=-\infty .$$

**Receta.** $\infty-\infty$: junta en una sola fracción, aplica la regla al $\tfrac00$ resultante y, si sale «número$/0$», estudia el **signo** del $0$.

**Parte del tema.** $\infty-\infty$ (U §2.3.2 p.83, Ej. 2.10 pp.83-84); regla con límite infinito.

**Verificación.** sympy: límites laterales en $0^+$ y $0^-$ ambos $-\infty$; $g'(x)=x\operatorname{sen}x-\cos x+1$ comprobado con `diff`.

**Avisos.** Solución impresa correcta (justifica el signo con «$x\operatorname{sen}x$ no toma valores negativos»). No comenta que por la izquierda no hay indeterminación; el resultado no cambia. Intuición: $\frac1{1-\cos x}\approx\frac2{x^2}$ crece mucho más rápido que $\frac1x$.

---

## Problema 4. $0^0$: exponencial y $0\cdot\infty$

**Fuente:** `X p.8 (Septiembre 2010, Grado Ing. Eléctrica, cód. 63011021, ejercicio 5, 3 puntos)`

**Enunciado.** Calcule
$$\lim_{x\to0^+}x^{x^2}.$$

**Solución.**
1. **Tipo.** Base $x\to0^+$, exponente $x^2\to0$: es $0^0$, indeterminado. La función solo tiene sentido para $x>0$ (por eso el límite es lateral).
2. **Pasar a exponencial.** Para $x>0$, $x^{x^2}=e^{x^2\ln x}$ (definición de potencia de base positiva). Como $e^t$ es continua (U Prop. 1.14, p.51), basta calcular $L=\lim_{x\to0^+}x^2\ln x$, y el resultado será $e^L$.
3. **El exponente es $0\cdot(-\infty)$.** Pasarlo a cociente poniendo **abajo la potencia** (su inversa se deriva fácil; la del logaritmo, no):
$$x^2\ln x=\frac{\ln x}{1/x^2}=\frac{\ln x}{x^{-2}},\qquad \text{tipo }\frac{-\infty}{+\infty}.$$
4. **Regla.** $(\ln x)'=\frac1x$, $(x^{-2})'=-2x^{-3}\neq0$ para $x>0$:
$$\lim_{x\to0^+}\frac{1/x}{-2/x^3}=\lim_{x\to0^+}\left(-\frac{x^2}{2}\right)=0 .$$
Simplificar antes de pasar al límite evita derivar otra vez.
5. **Volver.** $L=0$, luego $\displaystyle\lim_{x\to0^+}x^{x^2}=e^0=1$.

**Receta.** $f^g$ con $0^0$, $\infty^0$ o $1^\infty$: escribe $f^g=e^{g\ln f}$, calcula $L=\lim g\ln f$ (será $0\cdot\infty$, que se pasa a cociente) y el resultado es $e^L$.

**Parte del tema.** Formas $0\cdot\infty$ y potencias indeterminadas (U §2.3.2 pp.84-85, Ej. 2.11 y 2.12 p.84).

**Verificación.** sympy: `limit(x**2*log(x), x, 0, "+")` $=0$; `limit(x**(x**2), x, 0, "+")` $=1$.

**Avisos (laguna lógica del solucionario).** Escribe «suponemos que tiene límite y es $l$» y toma $\ln l=\lim\ln x^{x^2}$: así da por supuesto que el límite existe y es positivo, que es justo lo que hay que demostrar. Es más riguroso el paso 2 ($x^{x^2}=e^{x^2\ln x}$ y continuidad de la exponencial), que demuestra la existencia. Además, el solucionario remite a la «página 260» de un libro de ejercicios antiguo (no corresponde a E 24-25).

---

## Problema 5. $1^\infty$ en $x\to\infty$

**Fuente:** `X p.132 (Septiembre 2017, I. Electrónica Industrial y Automática, pregunta corta 1, 1 punto)`

**Enunciado.** Calcule el límite
$$\lim_{x\to\infty}\left(\frac{x-1}{x+2}\right)^x .$$

**Solución (con la regla).**
1. **Tipo.** $\frac{x-1}{x+2}\to1$ (dividir arriba y abajo por $x$) y el exponente $x\to\infty$: es $1^\infty$. Para $x>1$ la base es positiva.
2. **Exponencial.** $\left(\frac{x-1}{x+2}\right)^x=e^{\,x\ln\frac{x-1}{x+2}}$. Hay que hallar $L=\lim_{x\to\infty}x\ln\frac{x-1}{x+2}$, que es $\infty\cdot0$.
3. **A cociente:** $x\ln\frac{x-1}{x+2}=\dfrac{\ln(x-1)-\ln(x+2)}{1/x}$, tipo $\tfrac00$ (separar el logaritmo simplifica la derivada).
4. **Regla.** Numerador: $\frac1{x-1}-\frac1{x+2}=\frac{3}{(x-1)(x+2)}$; denominador: $-\frac1{x^2}\neq0$. Cociente:
$$\frac{3/((x-1)(x+2))}{-1/x^2}=\frac{-3x^2}{x^2+x-2}\longrightarrow-3 .$$
5. **Resultado:** $\displaystyle\lim_{x\to\infty}\left(\frac{x-1}{x+2}\right)^x=e^{-3}$.

**Solución del solucionario (Prop. 2.2, número $e$).** $\frac{x-1}{x+2}=1+\frac{-3}{x+2}=1+\frac1{(x+2)/(-3)}$; con $f(x)=\frac{x+2}{-3}\to-\infty$ se fuerza el exponente, $x=f(x)\cdot\frac{-3x}{x+2}$, y
$$\left[\left(1+\tfrac1{f(x)}\right)^{f(x)}\right]^{\frac{-3x}{x+2}}\to e^{\lim\frac{-3x}{x+2}}=e^{-3}.$$
Atajo equivalente del tema: $e^{\lim g(f-1)}$ con $g(f-1)=x\cdot\frac{-3}{x+2}\to-3$.

**Receta.** $1^\infty$: $e^{L}$ con $L=\lim g\ln f$ (o el atajo $L=\lim g\,(f-1)$).

**Parte del tema.** Potencias $1^\infty$ con logaritmos (U p.85) y Proposición 2.2 (U p.85).

**Verificación.** sympy: `limit(x*log((x-1)/(x+2)), x, oo)` $=-3$; `limit(((x-1)/(x+2))**x, x, oo)` $=e^{-3}$.

**Avisos.** Resultado impreso correcto. El último paso del solucionario (base y exponente variables a la vez: $(\dots)^{a(x)}\to e^{\lim a(x)}$) se justifica escribiendo $e^{a(x)\ln b(x)}$ y usando la continuidad de la exponencial; el solucionario no lo dice.

---

## Problema 6. La regla dentro de un problema de continuidad y derivabilidad

**Fuente:** `X pp.86-87 (Septiembre 2017, Grado Ing. Mecánica, cód. 68031029, Modelo A, ejercicio 5, 3 puntos: (a) 1, (b) 0.75, (c) 1.25)`

**Enunciado.** Dada la función
$$f(x)=\begin{cases}\dfrac{x}{e^x-1} & \text{si } x\neq0,\ 1 & \text{si } x=0.\end{cases}$$
(a) (1 punto) Demuestre que es continua en $\mathbb R$. (b) (0.75 puntos) Demuestre que tiene derivada continua en $\mathbb R-\{0\}$. (c) (1.25 puntos) Demuestre que la derivada es continua en $x=0$.

**Solución.**
1. **(a) Fuera de $0$.** Si $x\neq0$, $e^x\neq1$, así que $f$ es cociente de funciones continuas con denominador no nulo: continua.
2. **(a) En $0$.** Hay que ver $\lim_{x\to0}f(x)=f(0)=1$. Es $\tfrac00$; $(e^x-1)'=e^x\neq0$; regla:
$$\lim_{x\to0}\frac{x}{e^x-1}=\lim_{x\to0}\frac1{e^x}=1=f(0).$$
Luego $f$ es continua en $\mathbb R$.
3. **(b)** Para $x\neq0$, por la regla del cociente (U §2.2):
$$f'(x)=\frac{(e^x-1)-xe^x}{(e^x-1)^2},$$
cociente de continuas con denominador $\neq0$ si $x\neq0$: $f'$ es continua en $\mathbb R-\{0\}$.
4. **(c) Existencia de $f'(0)$ por la definición** (la fórmula de (b) no vale en $0$):
$$f'(0)=\lim_{h\to0}\frac{f(h)-f(0)}{h}=\lim_{h\to0}\frac{\frac{h}{e^h-1}-1}{h}=\lim_{h\to0}\frac{h-e^h+1}{h(e^h-1)}\quad\left(\tfrac00\right).$$
5. **Regla (1ª vez).** Numerador derivado: $1-e^h$; denominador derivado: $(e^h-1)+he^h$. Sigue $\tfrac00$. La derivada de ese denominador, $(2+h)e^h$, es $>0$ para $h>-2$, así que $(e^h-1)+he^h$ es estrictamente creciente allí y solo se anula en $h=0$: la condición «$g'\neq0$ cerca de $0$» se cumple.
6. **Regla (2ª vez).**
$$\lim_{h\to0}\frac{-e^h}{e^h+e^h+he^h}=\lim_{h\to0}\frac{-1}{2+h}=-\frac12 .$$
Por tanto $f'(0)=-\tfrac12$.
7. **(c) Continuidad de $f'$ en $0$:** falta $\lim_{x\to0}f'(x)=-\tfrac12$. Con $N=e^x-1-xe^x$, $D=(e^x-1)^2$ (tipo $\tfrac00$): $N'=-xe^x$, $D'=2(e^x-1)e^x\neq0$ si $x\neq0$. Entonces
$$\frac{N'}{D'}=\frac{-xe^x}{2(e^x-1)e^x}=-\frac12\cdot\frac{x}{e^x-1}\longrightarrow-\frac12\cdot1=-\frac12,$$
usando el límite del paso 2. Así $\lim_{x\to0}f'(x)=f'(0)$: $f'$ es continua en $0$.

**Receta.** Función a trozos con $\tfrac00$ en el punto de unión: continuidad = un límite con la regla; $f'(a)$ = **definición** (cociente incremental, otra vez con la regla); continuidad de $f'$ = calcular $\lim f'(x)$ y compararlo con $f'(a)$.

**Parte del tema.** Regla para $\tfrac00$ aplicada varias veces y «simplificar tras derivar» (U §2.3.2 pp.82-83); usa además derivada por definición (U §2.1) y regla del cociente (U §2.2).

**Verificación.** sympy: $\lim_{x\to0}f=1$; $f'(x)$ de `diff` coincide con (b); $\lim_{x\to0}\frac{f(x)-1}{x}=-\tfrac12$; $\lim_{x\to0}f'(x)=-\tfrac12$.

**Avisos.** Resultados impresos correctos. En el último límite el solucionario pasa de $\frac{-xe^x}{2(e^x-1)e^x}$ a $\frac{-1}{2e^x}$ sin decirlo: ha simplificado $e^x$ y aplicado la regla otra vez. Tampoco comprueba la condición sobre la derivada del denominador (paso 5). *Alternativa con Taylor en el tema 3.1:* $\frac{x}{e^x-1}=1-\frac x2+O(x^2)$ da directamente $f'(0)=-\tfrac12$.

---

## Otros problemas de examen del tema (no desarrollados, por repetir tipo)
- `X p.137` (Feb. 2017, 1ª sem., I. Electrónica, P1, 1 punto): $\lim_{x\to0}\frac{x-\operatorname{sen}x}{x^3}=\frac16$ (regla tres veces; alternativa con Taylor en el 3.1).
- `X p.140` (Feb. 2018, 2ª sem., I. Electrónica, P1, 1 punto): $\lim_{x\to\infty}\frac{\ln 5x^2}{3+7\ln x}=\frac27$ (el solucionario usa propiedades del logaritmo; con la regla: $\frac{2/x}{7/x}=\frac27$).
- `X p.7` (Sept. 2010, Eléctrica, P1, 1 punto): extender $\frac{\operatorname{sen}x}{x}$ por continuidad en $0$ (es U Ej. 2.8).
- `X p.81` (Feb. 2017, Mecánica, Modelo B, P1): $\lim_{x\to0^+}\frac{5+\cos(e^{-x^2})}{\ln x}=0$. **No** es indeterminado (acotado$/\infty$): ejemplo de cuándo NO usar la regla.

## Tipos de pregunta del tema que caen en examen y no hay en el PDF
- $\infty^0$ (p. ej. $\lim_{x\to\infty}x^{1/x}$): no aparece en ningún examen del PDF.
- Límite **con parámetro** (hallar $a$ para que un límite resuelto con la regla sea finito o tenga un valor dado): no hay ninguno (el de Feb. 2014 Modelo A, ej. 5, es de continuidad sin indeterminación).
- Límite de **sucesión** resuelto pasando a variable real y aplicando la regla (U Prop. 2.3): en el PDF las sucesiones $1^\infty$ se resuelven con el número $e$ (p. ej. `X p.101`), no con L'Hôpital.
- Producto $0\cdot\infty$ «puro» (no dentro de una potencia), del tipo $\lim_{x\to0^+}x\ln x$: solo aparece como paso intermedio (Problema 4).
