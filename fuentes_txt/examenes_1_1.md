# Problemas de examen real — Tema 1.1 El espacio ℝ

Fuente **X** = `E:\UNED\CALCULO\Examenes-resueltos-Calculo.pdf` (se cita la página **PDF**). Enunciados y soluciones impresas comprobados sobre la página renderizada.
Selección (de fácil a difícil, sin repetir tipo): todos se resuelven con lo de U §1.1 (orden, valor absoluto, intervalos, cotas, supremo/ínfimo) más conocimientos de bachillerato (signo de un producto, monotonía de la raíz y de la exponencial). Notación y recetas del resumen `temas/tema_1_1_espacio_R.html` (receta «demostrar que sup A = s», «traductores» del valor absoluto, tabla de intervalos).

Filas del índice con tema 1.1 o con desigualdades: X p.16, p.56, p.88, p.122-123, p.135, p.69. Todas se usan (p.56 como variante de p.16, por ser del mismo tipo).

---

## Problema 1. Ínfimo y supremo de $\{x: 0\le x^3<1\}$ (potencia impar)

**Fuente:** `X p.88 (Febrero 2018, Grado en Ing. Mecánica, Modelo A, pregunta corta 1, 1 punto)`.

**Enunciado.** Determine el ínfimo y el supremo del conjunto $A=\{x\in\mathbb R:\ 0\le x^3<1\}$. Razone la respuesta.

**Solución.**
1. **Traducir el conjunto a un intervalo.** Antes de buscar cotas conviene saber *qué números* hay en $A$; las condiciones son sobre $x^3$, no sobre $x$.
2. **La potencia cúbica conserva el orden.** Para $a,b\in\mathbb R$: $b^3-a^3=(b-a)(a^2+ab+b^2)$ y $a^2+ab+b^2=\left(a+\tfrac b2\right)^2+\tfrac34 b^2>0$ salvo si $a=b=0$. Por tanto, si $a<b$ el segundo factor es $>0$ y $b^3-a^3$ tiene el signo de $b-a$: $a<b\iff a^3<b^3$ (y lo mismo con $\le$).
3. Aplicando el paso 2 con $0=0^3$ y $1=1^3$: $0\le x^3\iff 0\le x$ y $x^3<1\iff x<1$. Luego $A=[0,1)$.
4. **Ínfimo.** $0\le x$ para todo $x\in A$, así que $0$ es cota inferior, y $0\in A$. Una cota inferior que pertenece al conjunto es el mínimo y, por tanto, el ínfimo (atajo del tema): $\inf A=\min A=0$.
5. **Supremo: conjetura $s=1$.** (a) Es cota superior: todo $x\in A$ cumple $x<1$. (b) Es la menor: sea $c<1$. Si $c<0$, $0\in A$ y $0>c$; si $0\le c<1$, el punto medio $a=\frac{c+1}2$ cumple $c<a<1$ y $a\ge0$, luego $a\in A$ y $a>c$. En ambos casos $c$ no es cota superior. Así $\sup A=1$ (definición de supremo, U Def. 1.7, p.20).
6. **¿Máximo?** $1\notin A$ ($1^3=1\not<1$), luego $A$ no tiene máximo.

**Resultado:** $\inf A=\min A=0$, $\sup A=1$ (sin máximo). Coincide con la solución impresa.

**Receta:** reescribe el conjunto como intervalo (usando que $x\mapsto x^3$ conserva el orden) y lee ínf/sup en la tabla de intervalos, justificando «es cota» y «es la menor».

**Parte del tema:** orden en ℝ y sus propiedades (U §1.1, pp.14-15); cotas (U Defs. 1.3-1.6, pp.18-19), supremo e ínfimo (U Defs. 1.7-1.8, p.20); tabla de intervalos (U Ej. 1.10, p.20).

**Verificación:** sympy `solve_univariate_inequality` da $[0,1)$, ínf $0\in A$, sup $1\notin A$; factorización $b^3-a^3=(b-a)(a^2+ab+b^2)$ comprobada.

**Avisos:** la solución impresa no justifica la equivalencia $x^3<1\iff x<1$ ni que $1$ sea la *menor* cota, aunque el enunciado pide «razone»; en examen conviene escribir los pasos 2 y 5. Tampoco menciona que $0$ es mínimo y que no hay máximo (no se pide, pero suma claridad).

---

## Problema 2. Ínfimo y supremo de $\{x: 0<x^2<1\}$ (conjunto con un «agujero»)

**Fuente:** `X p.16 (Septiembre 2011, Ing. Mecánica, preguntas cortas, nº 1, 1 punto)`.

**Enunciado.** Calcule el ínfimo y el supremo del conjunto $A=\{x\in\mathbb R:\ 0<x^2<1\}$.

**Solución.**
1. **Traducir a valor absoluto.** $x^2=|x|^2$ (porque $|x|=\pm x$). Así las condiciones pasan a ser sobre $u=|x|\ge0$.
2. **$0<x^2\iff x\ne0$:** un cuadrado es $\ge0$ y vale $0$ solo si $x=0$.
3. **$x^2<1\iff|x|<1$:** con $u=|x|\ge0$, $u^2-1=(u-1)(u+1)$ y $u+1>0$, así que $u^2<1\iff u-1<0\iff u<1$.
4. **Traductor del valor absoluto** ($|x|<a\iff -a<x<a$, con $a=1$): $|x|<1\iff -1<x<1$. Junto con $x\neq0$: $A=(-1,0)\cup(0,1)$.
5. **Supremo $=1$.** Cota: todo $x\in A$ cumple $x<1$. La menor: si $c<1$, tomar $a=\max\left\{\tfrac12,\tfrac{c+1}2\right\}$; entonces $a\in(0,1)\subset A$ y $a>c$, luego $c$ no es cota. $1\notin A$: no hay máximo.
6. **Ínfimo $=-1$**, simétrico: cota inferior porque $x>-1$; si $c>-1$, $a=\min\left\{-\tfrac12,\tfrac{c-1}2\right\}\in(-1,0)\subset A$ y $a<c$. $-1\notin A$: no hay mínimo.
7. El «agujero» en $0$ no influye: el sup/ínf de una unión finita de intervalos son el mayor extremo derecho y el menor extremo izquierdo (tabla del tema).

**Resultado:** $\inf A=-1$, $\sup A=1$; ni mínimo ni máximo. Coincide con la solución impresa.

**Variante del mismo tipo:** `X p.56 (Febrero 2015, Grado en Ing. Mecánica, Modelo B, pregunta corta 1, 1 punto)`: $A=\{x\in\mathbb R:\ 0\le|x|\le1\}$. Como $|x|\ge0$ siempre, la condición es solo $|x|\le1\iff-1\le x\le1$, $A=[-1,1]$, $\inf A=\min A=-1$, $\sup A=\max A=1$ (solución impresa correcta; tampoco menciona que aquí sí son mínimo y máximo).

**Receta:** si la condición depende de $x^2$ o de $|x|$, pasa a $|x|$, usa el traductor $|x|<a\iff -a<x<a$ y quita los puntos excluidos; luego sup/ínf = extremos exteriores del conjunto.

**Parte del tema:** valor absoluto (U Def. 1.1, p.15: $|x|=\sqrt{x^2}$; propiedades, Teorema 1.1, p.16) y «traductores» del resumen, intervalos (U pp.16-17), supremo/ínfimo (U Defs. 1.7-1.8, p.20).

**Verificación:** sympy: $A=(-1,0)\cup(0,1)$, ínf $-1$, sup $1$; variante: $[-1,1]$.

**Avisos:** ninguna errata. El error típico es escribir $A=(-1,1)$ olvidando que $0<x^2$ excluye $x=0$ (no cambia sup/ínf, pero el conjunto queda mal), o «$x^2<1\iff x<1$» (falso: $x=-2$ cumple $x<1$ pero $x^2=4$).

---

## Problema 3. Pregunta tipo test con exponencial: $A=\{x: 1/e^x<1\}$

**Fuente:** `X p.122 (enunciado) y p.123 (solución) («Examen 5 elaborado con exámenes de asignaturas similares», sin fecha ni puntuación; Ejercicio 2, tipo test)`.

**Enunciado.** Dado el conjunto $A=\left\{x\in\mathbb R:\ \dfrac1{e^x}<1\right\}$ señale la respuesta correcta: **A)** No tiene supremo ni ínfimo; **B)** $\inf A=0$; **C)** $\sup A=0$; **D)** $A$ es acotado.

**Solución.**
1. **Quitar el denominador.** $e^x>0$ para todo $x$, y multiplicar por un positivo conserva la desigualdad: $\frac1{e^x}<1\iff 1<e^x$.
2. **Monotonía de la exponencial** (bachillerato): $x\mapsto e^x$ es estrictamente creciente y $e^0=1$, luego $e^x>1=e^0\iff x>0$. Así $A=(0,+\infty)$.
3. **Ínfimo.** $0$ es cota inferior ($x>0$ en $A$). Es la mayor: si $c>0$, $a=\frac c2\in A$ y $a<c$, luego $c$ no es cota inferior. $\inf A=0$, y $0\notin A$ (no hay mínimo).
4. **No hay supremo.** Dado cualquier $M\in\mathbb R$, el número $a=\max\{M,0\}+1$ está en $A$ y $a>M$; ningún $M$ es cota superior, así que $A$ no está acotado superiormente y no tiene supremo en ℝ.
5. **Descartar opciones.** A) falsa (sí hay ínfimo). C) falsa ($0$ ni siquiera es cota superior: $1\in A$). D) falsa (paso 4). **B) correcta.**

**Resultado:** B. Coincide con la solución impresa.

**Receta:** en un test de sup/ínf, primero escribe el conjunto como intervalo despejando con operaciones que conservan el orden (multiplicar por positivos, aplicar $\ln$ o $e^{(\cdot)}$) y después comprueba cada opción contra la tabla de intervalos.

**Parte del tema:** propiedades del orden (U p.15), cotas y conjunto acotado (U Defs. 1.3-1.6, pp.18-19), ínfimo (U Def. 1.8, p.20), semirrectas sin supremo (U Ej. 1.12-1.13, p.21).

**Verificación:** sympy: solución de $1/e^x<1$ = $(0,\infty)$, ínf $0$, sup $\infty$.

**Avisos:** la solución impresa dice «la función $1/e^x$ es decreciente. Además $1/e^0=1$» sin explicar cómo se pasa de ahí a $x>0$; es correcto (si $g$ es decreciente y $g(0)=1$, $g(x)<1\iff x>0$, por ser estrictamente decreciente). Remite a un libro externo («Ejercicios resueltos de Matemáticas I», ej. 211), no a U.

---

## Problema 4. Inecuación cuadrática: dominio de $f(x)=\sqrt{2x^2-6}$

**Fuente:** `X p.135 (Febrero 2017, segunda semana, Grado en Ing. Electrónica Industrial y Automática, pregunta corta 1, 1 punto)`.

**Enunciado.** Sea $f$ la función definida por $f(x)=\sqrt{2x^2-6}$. Determine el dominio de la función $f$.

**Solución.**
1. **Qué se exige.** La raíz cuadrada real solo está definida para radicandos $\ge0$: dominio $=\{x\in\mathbb R:\ 2x^2-6\ge0\}$. Es una inecuación, que es lo que se practica en 1.1.
2. **Despejar.** Sumar $6$ conserva el sentido (propiedad 5 del orden) y dividir por $2>0$ también (propiedad 6, multiplicando por $\tfrac12>0$): $2x^2-6\ge0\iff x^2\ge3$.
3. **Pasar a valor absoluto.** $x^2=|x|^2$ y $3=(\sqrt3)^2$; para $u,v\ge0$, $u^2\ge v^2\iff u\ge v$ (porque $u^2-v^2=(u-v)(u+v)$ con $u+v>0$ salvo $u=v=0$). Luego $x^2\ge3\iff|x|\ge\sqrt3$.
4. **Traductor** «$|x|\ge a\iff x\ge a$ o $x\le-a$» ($a=\sqrt3>0$): $x\le-\sqrt3$ o $x\ge\sqrt3$.
5. **Dominio:** $(-\infty,-\sqrt3]\cup[\sqrt3,+\infty)$. Comprobación rápida: $x=\pm\sqrt3$ da radicando $0$ (vale); $x=0$ da $-6$ (no vale); $x=-2$ da $2$ (vale).

**Resultado:** $\operatorname{Dom} f=(-\infty,-\sqrt3]\cup[\sqrt3,+\infty)$. Coincide con la solución impresa.

**Receta:** para $x^2\ge a$ (con $a>0$) pasa a $|x|\ge\sqrt a$ y usa el traductor: salen **dos** semirrectas; los extremos entran si la desigualdad es $\ge$.

**Parte del tema:** propiedades del orden (U p.15), valor absoluto (U Def. 1.1, p.15) y «traductores» del resumen, intervalos y semirrectas (U pp.16-17). La palabra «dominio» es de U §1.4 (p.42 y ss.), pero aquí solo se usa «radicando $\ge0$» (bachillerato).

**Verificación:** sympy: $\{2x^2-6\ge0\}=(-\infty,-\sqrt3]\cup[\sqrt3,\infty)$.

**Avisos (errata menor):** en el «Fallo recurrente» impreso pone «Olvidar que $x=-\sqrt3$ y $x=-\sqrt3$ pertenecen también al dominio…»: el valor aparece repetido; se entiende «$x=-\sqrt3$ y $x=\sqrt3$» (los extremos). Los errores que señala son reales: quedarse solo con $[\sqrt3,\infty)$ (escribir $x\ge\sqrt3$ en vez de $|x|\ge\sqrt3$) o dejar los extremos abiertos.

---

## Problema 5. Inecuación racional: dominio de $f(x)=\sqrt{\dfrac{2-x}{(x+1)^2}}$

**Fuente:** `X p.69 (Septiembre 2016, Grado en Ing. Mecánica, Modelo A, pregunta corta 1, 1 punto)`.

**Enunciado.** Determine el dominio de definición de $f(x)=\sqrt{\dfrac{2-x}{(x+1)^2}}$.

**Solución.**
1. **Condiciones.** Hacen falta dos cosas: que el cociente exista, $(x+1)^2\ne0\iff x\ne-1$; y que el radicando sea $\ge0$: $\frac{2-x}{(x+1)^2}\ge0$.
2. **Signo del denominador.** Si $x\ne-1$, $(x+1)^2>0$ (cuadrado de un número no nulo).
3. **Multiplicar por un positivo conserva el sentido** (propiedad 6 del orden). Multiplicando por $(x+1)^2>0$ (y, de vuelta, por $1/(x+1)^2>0$): $\frac{2-x}{(x+1)^2}\ge0\iff 2-x\ge0\iff x\le2$. Ojo: es $\ge$, no $>$, porque $\sqrt0=0$ existe.
4. **Unir condiciones:** $x\le2$ y $x\ne-1$: $\operatorname{Dom}f=(-\infty,-1)\cup(-1,2]$.
5. **Comprobación:** $x=2$: $\sqrt{0/9}=0$ (vale); $x=-1$: división por $0$ (no vale); $x=3$: $\sqrt{-1/16}$ (no vale); $x=-5$: $\sqrt{7/16}$ (vale).

**Resultado:** $(-\infty,-1)\cup(-1,2]$, que es lo mismo que el impreso «$(-\infty,2]-\{-1\}$».

**Receta:** en un cociente, separa «denominador $\ne0$» de «signo»; si el denominador es un cuadrado, es positivo donde existe y el signo lo decide solo el numerador.

**Parte del tema:** propiedades del orden (multiplicar por un positivo, U p.15), intervalos y uniones de intervalos (U pp.16-17). (Como en el Problema 4, «dominio» es vocabulario de U §1.4.)

**Verificación:** sympy `solve_univariate_inequality` y `continuous_domain` dan $(-\infty,-1)\cup(-1,2]$.

**Aviso (errata en la solución impresa):** el razonamiento dice «hace falta numerador mayor que 0: $2-x>0\iff x<2$», lo que excluiría $x=2$; sin embargo el resultado final $(-\infty,2]-\{-1\}$ incluye el $2$ (y es el correcto). Debe leerse «numerador mayor **o igual** que 0: $2-x\ge0\iff x\le2$».

---

## Tipos de pregunta del tema que caen en examen y no hay en el PDF X

En X solo aparecen preguntas cortas (1 punto) de «reescribir el conjunto como intervalo y leer ínf/sup» y, clasificadas en 1.4, inecuaciones para hallar dominios. No hay ejemplos de:
- Supremo/ínfimo de conjuntos definidos **por una sucesión** ($\{1/n\}$, $\{(-1)^n+1/n\}$, $\{\frac{n}{n+1}\}$), que exigen la propiedad arquimediana o la caracterización con $\varepsilon$ (E Ej. 1.4; resumen, ejemplo propio 3).
- Conjuntos de **racionales** con sup/ínf irracional y el axioma del supremo en ℚ (U Ej. 1.11, p.20; U p.21).
- **Desigualdades con varios valores absolutos** por casos ($|x-1|+|x+2|<5$, $|x-a|<|x-b|$) (E Ej. 1.2).
- **Acotar expresiones** de variables acotadas (sup/ínf de $\{x-y\}$, $\{1/x\}$…) (E Ej. 1.5).
- Paso intervalo ↔ $|x-c|<r$ (centro y radio) (U Ej. 1.4-1.5, pp.17-18; E Ej. 1.1).
- Distinguir explícitamente **máximo/mínimo** de sup/ínf (X nunca lo pide, aunque conviene decirlo en la respuesta).
