# Unidad 3.3 — Interpolación polinómica

**Ejercicios:** E 3.21-3.28 (E pp. 107-113; página impresa = PDF). Todos son de examen.
**Teoría:** U §3.3 «Interpolación polinómica», pp. 119-124 (PDF 117-122). Apartados: 3.3.1 Motivación p. 119; Orientaciones y objetivos p. 120; 3.3.2 Interpolación pp. 120-121 (sistema lineal, existencia y unicidad, Ej. 3.16 pp. 121-122); diferencias divididas p. 123 (Ej. 3.17); forma de Newton p. 124 (Ej. 3.18) y «añadir un nodo» p. 124.
**Herramientas previas de U:** teorema de Rolle (U §2.5.2 p. 95) y resto de Lagrange de Taylor (U Prop. 3.2 y Def. 3.3 p. 111), solo para la fórmula del error. Para los problemas de examen que mezclan Simpson: trapecio (U Def. 6.5 y 6.6 p. 267) y Simpson (U Def. 6.7 y 6.8 p. 268), que son del **Tema 6** pero se basan en este tema.
**Verificación:** todos los resultados están comprobados con sympy en aritmética exacta (fracciones), con un script de diferencias divididas y con `sympy.interpolate`.

## Orden de estudio recomendado (se mantiene la numeración de E)

| Bloque | Ejercicios (orden de estudio) | Herramienta de U |
|---|---|---|
| A. Qué es el interpolador: grado y unicidad (sin cuentas) | 3.21 → 3.22 → 3.23 → 3.26 | U §3.3.2 pp. 120-121 |
| B. Calcular el interpolador por diferencias divididas | propio P1 → 3.24 → 3.25 → X p. 5 → X p. 119 | U p. 123 (tabla) y p. 124 (forma de Newton) |
| C. Añadir un nodo sin repetir | propio P2 → 3.27 → 3.28 | U p. 124 («al añadir un nuevo nodo…») |
| D. Cuánto se equivoca el interpolador (forma de Lagrange del error, **P**) | propio P3 → propio P4 | No está en U/S/L: propia, vía Rolle (U p. 95) |
| E. Examen: interpolación + trapecio/Simpson | X pp. 101/107 → X pp. 65-66 → X p. 85 → X p. 100 → X p. 151 | U pp. 267-268 (Tema 6) |

**Notación (la de U).** Datos $(x_k,f_k)$, $k=0,\dots,n$; los $x_k$ son los **nodos**. El **polinomio interpolador** $p_n$ es el de grado $\le n$ con $p_n(x_k)=f_k$ para todo $k$ (U pp. 120-121). Diferencias divididas (U p. 123):
$$f[x_k]=f_k,\qquad f[x_k,x_{k+1}]=\frac{f_{k+1}-f_k}{x_{k+1}-x_k},\qquad f[x_k,\dots,x_{k+m}]=\frac{f[x_{k+1},\dots,x_{k+m}]-f[x_k,\dots,x_{k+m-1}]}{x_{k+m}-x_k}.$$
Forma de Newton (U p. 124): $p_n(x)=f[x_0]+f[x_0,x_1](x-x_0)+f[x_0,x_1,x_2](x-x_0)(x-x_1)+\dots+f[x_0,\dots,x_n](x-x_0)\cdots(x-x_{n-1})$.

**Cómo se lee la tabla** (U Ej. 3.17 p. 123). Cada columna se calcula con la anterior: «la de abajo menos la de arriba», dividido entre la diferencia de los nodos **de los extremos** que abarca. Para el polinomio se usa solo la **diagonal superior** (la primera fila de cada columna).

---

# BLOQUE A — Qué es el interpolador: grado y unicidad

**Idea.** Con $n+1$ datos hay $n+1$ incógnitas $a_0,\dots,a_n$ (U p. 121), así que el interpolador tiene grado **como mucho** $n$. Y es **único** (U p. 121). Estas dos frases resuelven 3.21, 3.22, 3.23 y 3.26 sin hacer cuentas.

**Unicidad (U la afirma en p. 121 y no la demuestra; argumento propio, P).** Si $p$ y $q$ tienen grado $\le n$ y coinciden en los $n+1$ nodos, la diferencia $d=p-q$ tiene grado $\le n$ y se anula en $n+1$ puntos distintos. Un polinomio no nulo de grado $\le n$ tiene como mucho $n$ raíces (teorema del factor: cada raíz $r$ da un factor $(x-r)$, y no caben más de $n$ factores). Por tanto $d\equiv0$ y $p=q$.

**Consecuencia práctica (la usaremos mucho).** Si encontramos **de cualquier forma** (a ojo, porque los puntos están alineados, etc.) un polinomio de grado $\le n$ que pasa por los $n+1$ datos, **ese es** el interpolador. No hay otro.

## Ejercicio 3.21 (E p. 107)

> Razona si es cierto o falso que el polinomio interpolador que pasa por 9 puntos debe ser un polinomio exactamente de grado 8.

**Idea en una frase.** «Grado 8» es el **máximo**, no lo obligatorio: si los 9 puntos están en una recta, el interpolador es esa recta.

**Solución.**
1. **Grado máximo.** Con 9 datos, $n+1=9$, así que $n=8$: buscamos $p_8(x)=a_0+a_1x+\dots+a_8x^8$, con 9 incógnitas y 9 ecuaciones (U p. 121). U lo dice así: «el grado de $p_n(x)$ así construido es $n$ como máximo».
2. **Puede salir $a_8=0$.** Nada obliga a que el coeficiente de $x^8$ sea distinto de 0: depende de los datos.
3. **Contraejemplo** (el de E). Los puntos $(a,2a)$, $a=1,\dots,9$, es decir, $(1,2),(2,4),\dots,(9,18)$.
4. **Un candidato.** El polinomio $q(x)=2x$ pasa por todos: $q(a)=2a$. Su grado es $1\le8$.
5. **Es el interpolador.** Por la unicidad (Bloque A), el interpolador de grado $\le8$ es único, y $q$ ya cumple las condiciones. Luego $p_8(x)=2x$, de grado 1.
6. **Respuesta: falso.** Comprobado con sympy: el polinomio de Newton con esos 9 datos es $2x$.

**Receta.** Para refutar «el interpolador tiene grado exactamente $n$»: dar puntos sobre una recta (o sobre un polinomio de grado menor) y usar la unicidad.
**Error típico.** Confundir «grado $\le n$» con «grado $n$». El propio U escribe en el Ej. 3.18 (p. 124) «Su grado es 3, porque tenemos 4 datos»: es verdad en ese ejemplo **porque** la última diferencia, $\frac1{12}$, no es 0. Con 4 datos lo seguro es «grado $\le3$».
**Teoría:** U §3.3.2 pp. 120-121.

## Ejercicio 3.22 (E p. 107)

> Razona si es cierto o falso que si se interpolan $n$ puntos tomados de la gráfica de un polinomio de grado $n$ el resultado va a ser un polinomio de grado $n$.

**Idea en una frase.** Con $n$ puntos el interpolador tiene grado **como mucho $n-1$**, así que **nunca** puede tener grado $n$: la afirmación es falsa siempre, no solo en un ejemplo.

**Solución.**
1. **Cuántos datos.** Hay $n$ puntos. En la notación de U los índices van de $0$ a $n-1$.
2. **Grado máximo.** El interpolador de $n$ datos tiene $n$ coeficientes $a_0,\dots,a_{n-1}$: su grado es $\le n-1$ (U p. 121).
3. **Conclusión.** Un polinomio de grado $\le n-1$ no es de grado $n$. **Falso**, para cualquier elección de los $n$ puntos.
4. **Por qué no se recupera el polinomio original.** El polinomio original $P$ (grado $n$) pasa por los $n$ puntos, pero tiene grado $n$, no $\le n-1$: no es «el» interpolador de esos datos. Para recuperarlo harían falta $n+1$ puntos (entonces sí, por unicidad, el interpolador sería $P$).
5. **Ejemplo concreto.** $P(x)=x^2$ ($n=2$) y los 2 puntos $(-1,1)$ y $(1,1)$. El interpolador es la constante $1$ (grado 0), no $x^2$.

**Matiz sobre la solución de E (p. 107).** E responde «es falso, el grado será menor o igual que $n$» y da un contraejemplo (las $n$ raíces de $P$ dan $p\equiv0$). La conclusión «falso» es correcta, pero la cota es imprecisa: con $n$ puntos el grado es $\le n-1$, y eso hace la afirmación **siempre** falsa. Además, el contraejemplo de E necesita que $P$ tenga $n$ raíces reales distintas, cosa que no todo polinomio cumple ($x^2+1$ no tiene ninguna); el argumento del paso 2 no necesita nada.
**Receta.** Contar: $m$ datos $\Rightarrow$ grado $\le m-1$. Para recuperar un polinomio de grado $n$ hacen falta $n+1$ puntos de su gráfica.
**Error típico.** Pensar que «los puntos vienen de un polinomio de grado $n$, así que sale ese polinomio». Solo si hay al menos $n+1$ puntos.
**Teoría:** U §3.3.2 pp. 120-121.

## Ejercicio 3.23 (E p. 107)

> Dados los siguientes datos: $f(1)=1$, $f(3)=2$, $f(4)=-1$, $f(5)=0$, ¿puede haber más de un polinomio interpolador de grado 3 o menor que coincida con $f$ en 1, 3, 4 y 5?

**Idea en una frase.** No: es el teorema de unicidad. Muchas **funciones** pasan por esos 4 puntos, pero solo **un polinomio de grado $\le3$**.

**Solución.**
1. **Datos.** 4 nodos distintos (1, 3, 4, 5), así que $n=3$.
2. **Teorema.** El interpolador de grado $\le n$ existe y es único (U p. 121; argumento en el Bloque A).
3. **Respuesta: no.** Solo hay uno.
4. **Matiz.** Si se permite grado 4 o más, sí hay infinitos: por ejemplo $p_3(x)+c\,(x-1)(x-3)(x-4)(x-5)$ para cualquier $c$, porque el producto se anula en los cuatro nodos.
5. **(Para practicar, no se pedía.)** Diferencias divididas: $f[x_0,x_1]=\frac12$, $f[x_1,x_2]=-3$, $f[x_2,x_3]=1$; $f[x_0,x_1,x_2]=-\frac76$, $f[x_1,x_2,x_3]=2$; $f[x_0,\dots,x_3]=\frac{19}{24}$. Por tanto
   $$p_3(x)=1+\tfrac12(x-1)-\tfrac76(x-1)(x-3)+\tfrac{19}{24}(x-1)(x-3)(x-4)=\tfrac{19}{24}x^3-\tfrac{15}{2}x^2+\tfrac{485}{24}x-\tfrac{25}{2}.$$
   Verificado con sympy (Newton y `interpolate` dan lo mismo, y $p_3$ vale $1,2,-1,0$ en $1,3,4,5$).

**Receta.** «¿Puede haber más de uno?» → unicidad, si el grado está limitado a $\le n$ con $n+1$ nodos distintos. Si el grado no está limitado, hay infinitos.
**Error típico.** Contestar «sí, porque hay muchas funciones que pasan por esos puntos»: eso es cierto para funciones, no para polinomios de grado $\le3$.
**Teoría:** U §3.3.2 p. 121.

## Ejercicio 3.26 (E p. 110)

> El polinomio interpolador que pasa por los puntos de la gráfica de $f(x)=\cos 2x$ en los puntos: $x=0$, $x=\pi$, $x=2\pi$, ¿es el polinomio idénticamente nulo?

**Idea en una frase.** El interpolador depende **solo de los valores en los nodos**, y en los tres $\cos2x$ vale $1$: el interpolador es la constante $1$, no el $0$.

**Solución.**
1. **Valores en los nodos.** $f(0)=\cos0=1$, $f(\pi)=\cos2\pi=1$, $f(2\pi)=\cos4\pi=1$ (el coseno vale 1 en los múltiplos de $2\pi$).
2. **Un candidato.** $q(x)=1$ pasa por $(0,1)$, $(\pi,1)$, $(2\pi,1)$ y tiene grado $0\le2$.
3. **Es el interpolador**, por unicidad (U p. 121). Con la tabla: todas las diferencias de orden 1 y 2 son 0 (numeradores $1-1=0$), y Newton da $p_2(x)=1$.
4. **Respuesta: no.** $p_2(x)=1$ no es el polinomio nulo (por ejemplo, $p_2(0)=1\neq0$).

**Receta.** Antes de calcular nada, evaluar $f$ en los nodos. Si los valores son iguales, el interpolador es esa constante; si están alineados, es esa recta.
**Error típico.** Pensar en los ceros de la función: $\cos2x$ se anula en $\frac\pi4,\frac{3\pi}4,\dots$, pero esos no son los nodos. Si los nodos fueran ceros de $f$, entonces sí saldría $p\equiv0$ (como en el contraejemplo de E 3.22).
**Teoría:** U §3.3.2 p. 121.

---

# BLOQUE B — Calcular el interpolador con diferencias divididas

**Idea.** La forma de Newton construye el polinomio **por capas**: una constante que acierta en $x_0$; se le suma una recta que no estropea $x_0$ (lleva el factor $(x-x_0)$) y acierta en $x_1$; se le suma una parábola que no estropea $x_0,x_1$ (lleva $(x-x_0)(x-x_1)$) y acierta en $x_2$; etc. Los coeficientes de cada capa son las diferencias divididas de la diagonal superior (U p. 124). Así explica U el Ej. 3.16 (pp. 121-122): $p_2(x)=3x+15-\frac12x(x-1)$ es la recta $p_1$ más una corrección que se anula en $0$ y en $1$.

## Ejemplo propio P1 (sencillo): el mismo polinomio por sistema lineal y por Newton

> Halla el polinomio interpolador de $(-1,4)$, $(1,0)$, $(2,1)$: (a) resolviendo el sistema lineal de U p. 121; (b) con diferencias divididas. Comprueba que salen iguales.

**Idea en una frase.** Son dos caminos al **mismo** polinomio (por unicidad); Newton evita resolver el sistema.

**(a) Sistema lineal.**
1. **Incógnitas:** 3 datos, así que $p_2(x)=a_0+a_1x+a_2x^2$.
2. **Una ecuación por dato** (U p. 121): $a_0-a_1+a_2=4$, $a_0+a_1+a_2=0$, $a_0+2a_1+4a_2=1$.
3. **Restar las dos primeras:** $2a_1=-4$, luego $a_1=-2$.
4. **Sustituir $a_1=-2$:** la segunda da $a_0+a_2=2$; la tercera, $a_0+4a_2=5$.
5. **Restar estas dos:** $3a_2=3$, $a_2=1$, y $a_0=1$. Resultado: $p_2(x)=1-2x+x^2$.

**(b) Diferencias divididas.**
6. **Orden 1:** $\frac{0-4}{1-(-1)}=-2$ y $\frac{1-0}{2-1}=1$. **Orden 2:** $\frac{1-(-2)}{2-(-1)}=1$.
7. **Newton:** $p_2(x)=4-2(x+1)+1\cdot(x+1)(x-1)=4-2x-2+x^2-1=x^2-2x+1$.
8. **Iguales:** $p_2(x)=(x-1)^2$ por los dos caminos. Verificado con sympy (`solve` y Newton).

**Receta.** Con 2 o 3 datos el sistema es viable. Con 4 o más, Newton es más rápido y menos propenso a errores (U p. 121: «la resolución de este sistema … puede ser una tarea ardua»).

## Ejercicio 3.24 (E p. 108)

> Determina, mediante diferencias divididas, el polinomio de grado 3 que interpola los siguientes datos: $k=0,1,2,3$; $x_k=1,5,8,10$; $f(x_k)=3,11,38,56$.

**Idea en una frase.** Tabla de diferencias (columna a columna), diagonal superior y forma de Newton.

**Solución.**
1. **Orden 0** (U p. 123): $f[x_k]=f(x_k)$: $3,\ 11,\ 38,\ 56$.
2. **Orden 1** (cociente incremental entre nodos **vecinos**):
   - $f[x_0,x_1]=\frac{11-3}{5-1}=\frac84=2$,
   - $f[x_1,x_2]=\frac{38-11}{8-5}=\frac{27}{3}=9$,
   - $f[x_2,x_3]=\frac{56-38}{10-8}=\frac{18}2=9$.
3. **Orden 2** (resta de la columna anterior, dividida entre los nodos de los **extremos** que abarca):
   - $f[x_0,x_1,x_2]=\frac{9-2}{8-1}=\frac77=1$ (abarca de $x_0=1$ a $x_2=8$),
   - $f[x_1,x_2,x_3]=\frac{9-9}{10-5}=0$ (abarca de $x_1=5$ a $x_3=10$).
4. **Orden 3:** $f[x_0,\dots,x_3]=\frac{0-1}{10-1}=-\frac19$ (abarca de $1$ a $10$).
5. **La tabla:**

   | $x_k$ | $f[x_k]$ | orden 1 | orden 2 | orden 3 |
   |---|---|---|---|---|
   | 1 | **3** | **2** | **1** | $\mathbf{-\frac19}$ |
   | 5 | 11 | 9 | 0 | |
   | 8 | 38 | 9 | | |
   | 10 | 56 | | | |

6. **Forma de Newton** (U p. 124), con la diagonal superior (en negrita):
   $$\boxed{p_3(x)=3+2(x-1)+1\cdot(x-1)(x-5)-\tfrac19(x-1)(x-5)(x-8).}$$
   Esta ya es una respuesta completa: es un polinomio de grado 3.
7. **(Solo si se pide en potencias de $x$.)** $(x-1)(x-5)=x^2-6x+5$ y $(x-1)(x-5)(x-8)=x^3-14x^2+53x-40$. Sumando:
   $$p_3(x)=-\tfrac19x^3+\tfrac{23}9x^2-\tfrac{89}9x+\tfrac{94}9.$$
8. **Comprobación** (la recomienda U p. 120): $p_3(1)=3$, $p_3(5)=11$, $p_3(8)=38$, $p_3(10)=56$. Verificado con sympy. **E no tiene erratas** en este ejercicio.

**Receta.** (1) Columna de orden 0 = valores. (2) Cada nueva casilla = (casilla de la columna anterior de abajo − la de arriba) / ($x$ del extremo inferior − $x$ del extremo superior del grupo). (3) Polinomio = diagonal superior por los productos $(x-x_0)(x-x_1)\cdots$, con tantos factores como el orden. (4) Comprobar en dos o tres nodos.
**Error típico.** En el orden 2 o 3, dividir entre la diferencia de nodos **vecinos** ($8-5$) en vez de entre los **extremos** ($8-1$). Otro: poner en el término de orden $m$ el factor $(x-x_m)$, que no va (el último factor es $(x-x_{m-1})$).
**Teoría:** U p. 123 (definiciones, Ej. 3.17) y p. 124 (Ej. 3.18). Es literalmente X p. 57 (Feb. 2015, Modelo B, Ej. 5), con la misma solución.

## Ejercicio 3.25 (E pp. 109-110)

> Hemos medido la velocidad de un coche al frenar, tras haber pasado 1 segundo, a los 2 segundos y a los 4 segundos (variable $t$). Los valores obtenidos aparecen en la tabla siguiente: $t$ (s): 0, 1, 2, 4; $v$ (km/h): 210, 180, 160, 140.
> 1) Determina el polinomio interpolador que aproxima los datos mediante diferencias divididas considerando únicamente los instantes inicial y final.
> 2) Determina el polinomio interpolador que aproxima los datos mediante diferencias divididas considerando todos los datos.
> 3) Aproxima la velocidad transcurridos 3 segundos desde que comience el frenado mediante ambos polinomios.

(El texto nombra los instantes 1, 2 y 4 s, pero la tabla incluye también $t=0$ con 210 km/h, que es el «instante inicial» del apartado 1. Se sigue la tabla, como E.)

**Idea en una frase.** Con 2 nodos sale una recta; con 4, una cúbica. Las dos se evalúan en $t=3$ y dan valores distintos.

**Solución.**
1. **Apartado 1: nodos $t_0=0$, $t_1=4$.** $f[t_0,t_1]=\frac{140-210}{4-0}=-\frac{70}4=-\frac{35}2$.
2. **Recta:** $p_1(t)=210-\frac{35}2(t-0)=210-\frac{35}2t$. Es la recta que une $(0,210)$ y $(4,140)$, como en U Ej. 3.16 (p. 122).
3. **Apartado 2: orden 1** con $0,1,2,4$: $\frac{180-210}{1-0}=-30$, $\frac{160-180}{2-1}=-20$, $\frac{140-160}{4-2}=-10$.
4. **Orden 2:** $\frac{-20-(-30)}{2-0}=\frac{10}2=5$ y $\frac{-10-(-20)}{4-1}=\frac{10}3$.
5. **Orden 3:** $\frac{\frac{10}3-5}{4-0}=\frac{-5/3}{4}=-\frac5{12}$.
6. **Cúbica** (diagonal superior $210,-30,5,-\frac5{12}$):
   $$p_3(t)=210-30t+5t(t-1)-\tfrac5{12}t(t-1)(t-2).$$
   Desarrollada: $-\frac5{12}t^3+\frac{25}4t^2-\frac{215}6t+210$ (sympy; comprobada en los 4 nodos).
7. **Apartado 3, recta:** $p_1(3)=210-\frac{105}2=\frac{315}2=157{,}5$ km/h.
8. **Apartado 3, cúbica:** se sustituye en la forma de Newton (más fácil que desarrollar): $210-90+5\cdot3\cdot2-\frac5{12}\cdot3\cdot2\cdot1=210-90+30-\frac52=\frac{295}2=147{,}5$ km/h.
9. **Lectura.** La recta ignora que el coche frena cada vez menos (las diferencias de orden 1 pasan de $-30$ a $-10$); la cúbica sí lo recoge. Coincide con E.

**Receta.** Si se pide comparar interpoladores con más y menos nodos: una tabla para cada conjunto de nodos y evaluar **en la forma de Newton**, sin desarrollar.
**Error típico.** Usar en el apartado 1 los nodos $1$ y $4$ porque el enunciado «empieza en 1 segundo». El instante inicial de la tabla es $t=0$.
**Teoría:** U p. 122 (recta, Ej. 3.16), p. 123 y p. 124.

---

# BLOQUE C — Añadir un nodo sin empezar de nuevo

**Idea (U p. 124).** $p_n(x)=p_{n-1}(x)+f[x_0,\dots,x_n](x-x_0)\cdots(x-x_{n-1})$. Al añadir un dato nuevo, el polinomio viejo se conserva y solo se suma **un término**, cuyo coeficiente sale de las diferencias nuevas (las que contienen el nodo nuevo).

**Propiedad que U no enuncia (P, verificada con sympy): las diferencias divididas no dependen del orden de los nodos.** $f[x_0,\dots,x_m]$ es el coeficiente de $x^m$ del interpolador de esos $m+1$ datos (en la forma de Newton solo el último término tiene $x^m$), y ese polinomio es único sea cual sea el orden en que se listen los datos. Por eso los nodos **no tienen por qué estar ordenados** en la tabla, y un nodo nuevo se puede poner siempre **al final** de la lista.

## Ejemplo propio P2 (sencillo-medio): añadir un dato a P1

> A los datos de P1 se añade $(3,8)$. Halla $p_3$ aprovechando $p_2(x)=(x-1)^2$.

1. **Nodo nuevo al final:** $x_3=3$, $f_3=8$.
2. **Diferencias nuevas** (solo las que contienen $x_3$): $f[x_2,x_3]=\frac{8-1}{3-2}=7$; $f[x_1,x_2,x_3]=\frac{7-1}{3-1}=3$; $f[x_0,\dots,x_3]=\frac{3-1}{3-(-1)}=\frac12$. Son 3 cuentas; las otras 3 de la tabla se reutilizan.
3. **Término nuevo:** $\frac12(x+1)(x-1)(x-2)$, que se anula en los nodos viejos (no estropea lo ya conseguido).
4. **Resultado:** $p_3(x)=(x-1)^2+\frac12(x+1)(x-1)(x-2)=\frac12x^3-\frac52x+2$. Comprobación: $p_3(3)=\frac{27}2-\frac{15}2+2=8$. Verificado con sympy.

**Receta.** Añadir un nodo = calcular la nueva diagonal inferior (tantas diferencias como nodos había) + sumar un término.

## Ejercicio 3.27 (E pp. 110-112)

> Los datos a 1 de enero de los años 2004 a 2008 del INE referentes a población de España son: 2004: 43197684; 2005: 44108530; 2006: 44708964; 2007: 45200737; 2008: 46157822.
> 1) Con estos datos, y utilizando interpolación ¿estima la población de España el 1 de julio de 2007?
> 2) Si conocemos el dato adicional de que la población el 1 de enero de 2009 es 46745809, ¿cuál sería la población estimada de España el 1 de julio de 2007?

**Idea en una frase.** Tabla con 5 nodos (los años), evaluar en $x=2007{,}5$ con la forma de Newton sin desarrollar, y para el apartado 2 añadir un nodo y un término.

**Solución.**
1. **Datos.** $x_k=2004,\dots,2008$ (5 nodos, $n=4$). El 1 de julio de 2007 es la mitad del año: $x=2007{,}5$.
2. **Denominadores.** Los nodos están a distancia 1: en orden 1 se divide entre 1, en orden 2 entre 2, en orden 3 entre 3 y en orden 4 entre 4.
3. **Orden 1:** $910846$, $600434$, $491773$, $957085$ (restas de poblaciones consecutivas).
4. **Orden 2:** $\frac{600434-910846}2=-155206$; $\frac{491773-600434}2=-\frac{108661}2=-54330{,}5$; $\frac{957085-491773}2=232656$.
5. **Orden 3:** $\frac{-54330{,}5+155206}3=\frac{201751}6\approx33625{,}17$; $\frac{232656+54330{,}5}3=\frac{573973}6\approx95662{,}17$. (En `ejercicios.txt` aparecen como «33625.1Û6»: es $33625{,}1\overline{6}$, un decimal periódico.)
6. **Orden 4:** $\frac{573973/6-201751/6}4=\frac{372222/6}{4}=\frac{62037}4=15509{,}25$.
7. **Polinomio de Newton:**
   $$p_4(x)=43197684+910846(x-2004)-155206(x-2004)(x-2005)+\tfrac{201751}6(x-2004)(x-2005)(x-2006)+\tfrac{62037}4(x-2004)\cdots(x-2007).$$
8. **Evaluar en 2007,5.** Los factores valen $x-2004=3{,}5$, $x-2005=2{,}5$, $x-2006=1{,}5$, $x-2007=0{,}5$. Término a término: $43197684+3187961-1358052{,}5+441330{,}31+101779{,}45=45\,570\,702{,}27$. Se redondea a **45 570 702 personas**. Coincide con E (sympy, aritmética exacta).
9. **Apartado 2: nodo nuevo $x_5=2009$**, al final. Diferencias nuevas (las que contienen 2009): $587987$; $-184549$; $-\frac{417205}3\approx-139068{,}33$; $-\frac{469461}8=-58682{,}625$; y $f[x_0,\dots,x_5]=-\frac{118707}8=-14838{,}375$. Son 5 cuentas.
10. **Término nuevo:** $p_5(x)=p_4(x)-14838{,}375\,(x-2004)(x-2005)(x-2006)(x-2007)(x-2008)$.
11. **Evaluar.** El producto en 2007,5 es $3{,}5\cdot2{,}5\cdot1{,}5\cdot0{,}5\cdot(-0{,}5)=-3{,}28125$ (el último factor es negativo porque $2007{,}5<2008$). Término: $-14838{,}375\cdot(-3{,}28125)=+48688{,}42$. Total: $45\,619\,390{,}68\approx$ **45 619 391 personas**. Coincide con E.

**Receta.** Con nodos equiespaciados a distancia $h$, el denominador de orden $m$ es $m\cdot h$. Para estimar en un punto, evaluar la forma de Newton término a término (sin desarrollar). Al añadir un nodo, calcular solo la diagonal nueva y sumar un término.
**Error típico.** Desarrollar el polinomio con números de 8 cifras: es largo y acumula errores de redondeo. Y olvidar el signo del factor $(x-2008)$ cuando $x<2008$.
**Teoría:** U p. 123 y p. 124 (forma de Newton y «al añadir un nuevo nodo»).

## Ejercicio 3.28 (E p. 113)

> Supón que en el ejercicio anterior en lugar de proporcionarte el dato de la población en 2009 te dan el dato de la población en 2003. A partir de la tabla de diferencias divididas de los años 2004 a 2008. ¿Cuántas diferencias divididas de orden mayor o igual que 1 debes calcular para estimar la población en 2007.5? ¿Y si te proporcionasen la población en 2005.5?

**Idea en una frase.** Se reutiliza toda diferencia cuyo grupo de nodos **no** contiene el nuevo; las que lo contienen hay que calcularlas.

**Solución (con la tabla ordenada, como E).**
1. **Cuántas hay en total.** Con 6 nodos ordenados, las diferencias de orden $\ge1$ son $5+4+3+2+1=15$ (una por cada grupo de nodos consecutivos de tamaño $\ge2$).
2. **Nodo 2003 (un extremo).** Queda arriba de la tabla. Los grupos consecutivos que no lo contienen son exactamente los de la tabla vieja: $4+3+2+1=10$ reutilizables. Nuevas: $15-10=$ **5**.
3. **Nodo 2005,5 (en medio).** Queda entre 2005 y 2006 y «parte» la tabla. Sin él solo quedan los grupos consecutivos dentro de $\{2004,2005\}$ (1 grupo) y dentro de $\{2006,2007,2008\}$ (3 grupos): **4** reutilizables. Nuevas: $15-4=$ **11**. Coincide con E.

**Matiz que E omite (P, verificado con sympy).** Como las diferencias divididas no dependen del orden de los nodos (Bloque C), **no hace falta** meter 2005,5 en su sitio: se puede añadir **al final** de la lista ($x_5=2005{,}5$). Entonces solo hay que calcular $f[x_4,x_5]$, $f[x_3,x_4,x_5]$, $f[x_2,\dots,x_5]$, $f[x_1,\dots,x_5]$ y $f[x_0,\dots,x_5]$: **5 nuevas, igual que con 2003 o 2009**, y $p_5=p_4+f[x_0,\dots,x_5](x-2004)\cdots(x-2008)$. Comprobado con sympy: con los datos de E 3.27, la diferencia de orden 5 vale $-\frac{118707}8$ tanto con los nodos en orden como desordenados. La respuesta de E (11) es correcta **si se exige la tabla ordenada**; el mínimo es 5.

**Receta.** Nuevas = las que contienen el nodo nuevo. Si se puede elegir, poner el nodo nuevo al final: siempre son tantas como nodos había.
**Error típico.** Recalcular la tabla entera.
**Teoría:** U p. 124 («basta con calcular las diferencias que nos faltan (que son las diferencias donde está $x_n$)»).

---

# BLOQUE D — Cuánto se equivoca el interpolador (forma de Lagrange del error) — **P**

> **Aviso de fuente.** Esta fórmula **no está en U §3.3, ni en S ni en L** (dossier, §5). El cronograma la cita en las «notas adicionales» del módulo III, que no están en el repositorio. Aquí va marcada como **propia (P)** y razonada con herramientas de U (Rolle, p. 95). Es la «hermana» del resto de Lagrange de Taylor (U Prop. 3.2 p. 111).

**Enunciado (P).** Sea $f$ con derivada $(n+1)$-ésima en un intervalo $I$ que contiene los nodos distintos $x_0,\dots,x_n$ y el punto $x$. Sea $p_n$ el interpolador. Entonces existe $\xi\in I$ (entre el menor y el mayor de $x,x_0,\dots,x_n$) tal que
$$\boxed{f(x)-p_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}\,(x-x_0)(x-x_1)\cdots(x-x_n).}$$
Si $|f^{(n+1)}|\le M$ en $I$, entonces $|f(x)-p_n(x)|\le\frac{M}{(n+1)!}\,|x-x_0|\cdots|x-x_n|$.

**Comparación con Taylor (U p. 111).** Taylor: $\frac{f^{(n+1)}(c)}{(n+1)!}(x-x_0)^{n+1}$, con toda la información concentrada en un punto. Interpolación: el mismo $\frac{f^{(n+1)}}{(n+1)!}$, pero la potencia se reparte entre los $n+1$ nodos. Por eso el interpolador es exacto en los nodos (el producto vale 0) y aproxima en todo el intervalo, que es lo que U pide en p. 120.

**Por qué es cierta (esquema con Rolle, P).**
1. **Si $x$ es un nodo,** los dos lados valen 0. Supongamos que no lo es.
2. **Llamamos** $w(t)=(t-x_0)\cdots(t-x_n)$ y elegimos el número $K$ para que $f(x)-p_n(x)=K\,w(x)$ (se puede, porque $w(x)\neq0$). Hay que ver que $K=\frac{f^{(n+1)}(\xi)}{(n+1)!}$ para algún $\xi$.
3. **Función auxiliar:** $g(t)=f(t)-p_n(t)-K\,w(t)$. Se anula en los $n+1$ nodos (allí $f=p_n$ y $w=0$) y en $t=x$ (por la elección de $K$): **$n+2$ ceros** distintos.
4. **Rolle (U p. 95)** entre cada dos ceros consecutivos: $g'$ tiene al menos $n+1$ ceros. Otra vez: $g''$ tiene al menos $n$ ceros. Y así sucesivamente: tras $n+1$ pasos, $g^{(n+1)}$ tiene al menos **un** cero, $\xi$.
5. **Derivamos $n+1$ veces:** $p_n^{(n+1)}=0$ (tiene grado $\le n$) y $w^{(n+1)}=(n+1)!$ (porque $w=t^{n+1}+\dots$). Así $g^{(n+1)}(t)=f^{(n+1)}(t)-K\,(n+1)!$.
6. **En $\xi$:** $0=f^{(n+1)}(\xi)-K\,(n+1)!$, luego $K=\frac{f^{(n+1)}(\xi)}{(n+1)!}$.

**Caso particular.** Si $f$ es un polinomio de grado $\le n$, $f^{(n+1)}=0$ y el error es 0: el interpolador **es** $f$ (otra forma de ver la unicidad y E 3.21).

## Ejemplo propio P3 (medio): cota de error con $e^x$

> Interpola $f(x)=e^x$ en $0,\frac12,1$; aproxima $e^{1/4}$ y acota el error con la forma de Lagrange.

**Idea en una frase.** El error es $\frac{f'''(\xi)}{3!}$ por el producto de las distancias a los 3 nodos; se acota $f'''=e^\xi$ entre su mínimo y su máximo en $[0,1]$.
1. **Tabla** (valores $1$; $e^{1/2}\approx1{,}6487213$; $e\approx2{,}7182818$): orden 1: $\frac{1{,}6487213-1}{0{,}5}=1{,}2974425$ y $\frac{2{,}7182818-1{,}6487213}{0{,}5}=2{,}1391211$; orden 2: $\frac{2{,}1391211-1{,}2974425}{1-0}=0{,}8416786$.
2. **Newton:** $p_2(x)=1+1{,}2974425\,x+0{,}8416786\,x\left(x-\frac12\right)$.
3. **Aproximación:** $p_2(\frac14)=1+0{,}3243606-0{,}0526049=1{,}2717557$.
4. **Fórmula del error** ($n=2$, tres nodos): $e^{1/4}-p_2(\frac14)=\frac{e^{\xi}}{3!}\left(\tfrac14-0\right)\left(\tfrac14-\tfrac12\right)\left(\tfrac14-1\right)=\frac{e^\xi}{6}\cdot\frac{3}{64}$, con $\xi\in(0,1)$.
5. **Acotar $f'''(\xi)=e^\xi$:** en $[0,1]$, $1\le e^\xi\le e$ (la exponencial es creciente).
6. **Cota:** $0{,}0078\approx\frac16\cdot\frac3{64}\le e^{1/4}-p_2(\tfrac14)\le\frac{e}{6}\cdot\frac3{64}\approx0{,}0212$. Además el error es **positivo**: el interpolador se queda por debajo.
7. **Comprobación:** $e^{1/4}=1{,}2840254$; error real $0{,}0122697$, dentro de $[0{,}0078;\ 0{,}0212]$. Verificado con sympy.
8. **(Cota en todo $[0,1]$.)** El máximo de $|x(x-\frac12)(x-1)|$ en $[0,1]$ es $\frac{\sqrt3}{36}\approx0{,}0481$ (en $x=\frac12\pm\frac{\sqrt3}6$, donde se anula la derivada). Luego $|e^x-p_2(x)|\le\frac{e}{6}\cdot0{,}0481\approx0{,}0218$ para todo $x\in[0,1]$.

**Receta.** Error en un punto: (1) contar nodos: $n+1$; (2) $M$ = máximo de $|f^{(n+1)}|$ en el intervalo que contiene nodos y punto; (3) cota $=\frac{M}{(n+1)!}\prod|x-x_i|$.
**Error típico.** Usar $(x-x_0)^{n+1}$ (la de Taylor) en lugar del producto de las distancias a **todos** los nodos.

## Ejemplo propio P4 (difícil): la cota de Lagrange frente al redondeo de los datos (X p. 119)

> En X p. 119 (ver más abajo) se interpola $\ln x$ en $1{,}3;\ 1{,}4;\ 1{,}5;\ 1{,}6$ con los valores **redondeados a 4 decimales** y se estima $\ln1{,}47\approx0{,}3853$. ¿Qué error garantiza la forma de Lagrange? ¿Por qué el error real es mayor?

**Idea en una frase.** La fórmula de Lagrange mide el error del método con datos exactos; aquí domina otro error, el del redondeo de los datos.
1. **Qué derivada:** 4 nodos, $n=3$, se necesita $f^{(4)}$. Derivando: $f'=\frac1x$, $f''=-\frac1{x^2}$, $f'''=\frac2{x^3}$, $f^{(4)}=-\frac6{x^4}$.
2. **Cota de $|f^{(4)}|$ en $[1{,}3;\,1{,}6]$:** $\frac6{x^4}$ es decreciente, así que el máximo está en $1{,}3$: $M=\frac6{1{,}3^4}\approx2{,}1008$.
3. **Producto:** $|1{,}47-1{,}3|\cdot|1{,}47-1{,}4|\cdot|1{,}47-1{,}5|\cdot|1{,}47-1{,}6|=0{,}17\cdot0{,}07\cdot0{,}03\cdot0{,}13=4{,}641\cdot10^{-5}$.
4. **Cota:** $\frac{2{,}1008}{4!}\cdot4{,}641\cdot10^{-5}\approx4{,}06\cdot10^{-6}$. Es el error **si los datos fueran exactos**. Con los $\ln x_k$ exactos el error real es $2{,}6\cdot10^{-6}$ (sympy), dentro de la cota.
5. **Pero X usa datos redondeados** (error $\le5\cdot10^{-5}$ en cada uno). Ese error se propaga: $p_3(1{,}47)$ es una combinación de los cuatro datos con pesos $-0{,}0455$; $0{,}3315$; $0{,}7735$; $-0{,}0595$ (sympy), cuya suma de valores absolutos es $1{,}21$. El redondeo puede mover el resultado hasta $1{,}21\cdot5\cdot10^{-5}\approx6\cdot10^{-5}$.
6. **Conclusión:** el error real de X, $|0{,}385262-0{,}385300|\approx3{,}7\cdot10^{-5}$, lo explica el **redondeo de los datos**, no la interpolación. Por eso no tiene sentido dar más de 4 cifras: $\ln1{,}47\approx0{,}3853$.

**Receta.** La cota de Lagrange mide el error del **método**. Si los datos vienen redondeados, hay que sumar el error de los datos; en la práctica, no dar más cifras que los datos.

---

# Así lo preguntan en el examen (X; página = PDF, leída como imagen con PyMuPDF)

## X p. 5 (Feb. 2010, 2.ª semana, Ing. Eléctrica, Ej. 5, 3 puntos)

> Determine, por diferencias divididas, el polinomio de grado 3 que aproxima los siguientes datos: $k=0,1,2,3$; $x_k=-2,0,1,3$; $f(x_k)=0,2,3,5$.

**Idea en una frase.** Las tres pendientes salen iguales: los puntos están en una recta y el «polinomio de grado 3» es en realidad $x+2$.
1. **Orden 1:** $\frac{2-0}{0-(-2)}=1$, $\frac{3-2}{1-0}=1$, $\frac{5-3}{3-1}=1$.
2. **Orden 2:** $\frac{1-1}{1-(-2)}=0$ y $\frac{1-1}{3-0}=0$. **Orden 3:** $\frac{0-0}{3-(-2)}=0$.
3. **Newton:** $p_3(x)=0+1\cdot(x+2)+0+0=x+2$.
4. **Comprobación:** $x+2$ vale $0,2,3,5$ en $-2,0,1,3$. Coincide con X; verificado con sympy. **Sin erratas.**

**Receta.** Si una columna de diferencias es toda ceros, las siguientes también, y el grado es menor que el esperado (es E 3.21 en la práctica).
**Error típico.** Pensar que la respuesta está mal porque «pedían grado 3». El interpolador de 4 datos tiene grado $\le3$.

## X p. 57 (Feb. 2015, Modelo B, Ej. 5, 3 puntos)

Es **idéntico** a E 3.24 (mismos datos y misma solución, $p_3(x)=-\frac19x^3+\frac{23}9x^2-\frac{89}9x+\frac{94}9$). Ver el Ejercicio 3.24. Sin erratas.

## X p. 101 («Electrónica 2», I. Electrónica Industrial y Automática, pregunta corta 3, 1 punto) y X p. 107 («Electrónica 4», Ej. 5, 3 puntos) — **con errata y con hueco**

> (p. 101) De una función $f$ se sabe que $f(0)=1$, $f(2)=3$ y $f(4)=2$. Aproxime el valor de $f(8)$ utilizando el polinomio interpolador.
> (p. 107) Mismos datos. • Aproxime el valor de $f(1)$ utilizando el polinomio interpolador. • Aproxime el valor de $\int_0^4 f(x)\,dx$ mediante la fórmula de Simpson. • Compruebe que obtiene el mismo resultado que en el apartado anterior si integra el polinomio interpolador entre 0 y 4.

**Idea en una frase.** Tres datos, parábola por Newton, y se evalúa; Simpson es exactamente integrar esa parábola.
1. **Orden 1:** $\frac{3-1}{2-0}=1$ y $\frac{2-3}{4-2}=-\frac12$. **Orden 2:** $\frac{-\frac12-1}{4-0}=-\frac38$.
2. **Polinomio:** $p(x)=1+x-\frac38x(x-2)=-\frac38x^2+\frac74x+1$.
3. **(p. 101)** $f(8)\approx p(8)=1+8-\frac38\cdot8\cdot6=9-18=-9$.
4. **(p. 107, primer punto)** $f(1)\approx p(1)=1+1-\frac38\cdot1\cdot(-1)=2+\frac38=\frac{19}8=2{,}375$.
5. **Simpson** (U Def. 6.7 p. 268): $\frac{4-0}6\left(f(0)+4f(2)+f(4)\right)=\frac46(1+12+2)=10$.
6. **Integrar el interpolador:** $\int_0^4\left(-\frac38x^2+\frac74x+1\right)dx=-\frac38\cdot\frac{64}3+\frac74\cdot8+4=-8+14+4=10$. Iguales, porque Simpson se obtiene **integrando el interpolador de grado 2** en $a,\frac{a+b}2,b$ (U p. 267, final). Verificado con sympy.

**Errata de X p. 101.** La última línea dice «El valor aproximado de $f(3)$ viene dado por $p(8)$»: debe decir **$f(8)$**. El número, $-9$, es correcto.
**Hueco de X p. 107.** La solución impresa **no da** el valor de $f(1)$ pedido en el primer apartado. Es $p(1)=\frac{19}8$.
**Receta.** Interpolar y evaluar. Para Simpson con 3 nodos equiespaciados: o la fórmula, o integrar la parábola interpoladora (salen iguales).
**Error típico (p. 101).** Fiarse de $p(8)=-9$: es una **extrapolación** (8 está muy fuera de $[0,4]$). La forma de Lagrange del error (Bloque D) lo explica: el producto de distancias $|8-0|\,|8-2|\,|8-4|=192$ es enorme, frente a $|1-0|\,|1-2|\,|1-4|=3$ en $x=1$. Que salga negativo cuando los datos están entre 1 y 3 es una señal de alarma.

## X pp. 65-66 (Feb. 2016, Modelo B, Ej. 5, 3 puntos) — **con erratas**; y X pp. 122-124 (Examen 5, Ej. 5), el mismo problema — **con un error de cálculo**

> (p. 65) Se consideran los siguientes valores de una función: $x=1,2,3$; $f(x)=31,26,43$. (a) Calcule $\int_1^3f(x)\,dx$ por la regla del trapecio. (b) Calcule $\int_1^3f(x)\,dx$ por la regla de Simpson con 3 nodos igualmente espaciados. (c) La función $g(x)=11x^2-38x+58$ verifica $f(1)=g(1)$, $f(2)=g(2)$, $f(3)=g(3)$. Calcule $\int_1^3g(x)\,dx$ y compárelo con los valores obtenidos en los apartados anteriores. Justifique a qué se debe la diferencia.

**Idea en una frase.** El trapecio integra la poligonal (rectas entre datos); Simpson integra la parábola interpoladora, y $g$ **es** esa parábola: por eso $\int g$ coincide con Simpson.
1. **(a) Trapecio compuesto** con los 3 nodos, $h=1$ (U Def. 6.6 p. 267): $\frac h2(f_0+2f_1+f_2)=\frac12(31+52+43)=63$.
2. **(b) Simpson** (U Def. 6.7 p. 268): $\frac{3-1}6(31+4\cdot26+43)=\frac{178}3\approx59{,}333$.
3. **(c) ¿Es $g$ el interpolador?** $g(1)=11-38+58=31$, $g(2)=44-76+58=26$, $g(3)=99-114+58=43$: sí, y como tiene grado 2, por unicidad es **el** interpolador. (Con Newton: orden 1: $-5$ y $17$; orden 2: $11$; $p_2=31-5(x-1)+11(x-1)(x-2)=11x^2-38x+58$.)
4. **Integral:** $\int_1^3g=\left[\frac{11}3x^3-19x^2+58x\right]_1^3=\frac{178}3$.
5. **Justificación:** Simpson es la integral exacta de la parábola que interpola en $a,\frac{a+b}2,b$; $g$ es esa parábola; luego $\int g$ = Simpson. El trapecio usa rectas y da otra cosa (63). Todo verificado con sympy.

**Erratas de X pp. 65-66.** En (a) y (b) escribe «$f(0)=31$, $f(1)=26$, $f(3)=43$»; los nodos son $1,2,3$: debe ser $f(1)=31$, $f(2)=26$, $f(3)=43$. Los resultados (63 y $\frac{178}3$) son correctos.
**Error de X p. 123 (Examen 5, Ej. 5; no estaba en el dossier).** Es el mismo problema sin el apartado (c). En el trapecio sustituye $f(x_1)=31$ en lugar de $26$: $\frac{3-1}2\left(\frac{31+43}2+31\right)=68$. **Lo correcto es 63.** La comparación del apartado 3 (p. 124, «aplicando la regla del trapecio obtenemos 68») arrastra el error. Repite además la errata «$f(0)=31$, $f(1)=26$» en p. 123 y p. 124.
**Receta.** «¿Por qué coincide con Simpson?» → porque Simpson integra el interpolador de grado 2, y por unicidad la parábola dada es ese interpolador.

## X p. 85 (Sept. 2017, Modelo A, Grado en Ing. Mecánica, pregunta corta 3, 1 punto) — **con erratas**

> Sea $f$ una función continua tal que $f(0)=1$, $f(1)=-2$, $f(2)=0$. Aproxime el valor de la integral $I=\int_0^2f(x)\,dx$ con el método de Simpson.

1. **Simpson** (U Def. 6.7 p. 268) con $a=0$, $\frac{a+b}2=1$, $b=2$: $I\approx(2-0)\frac{1+4(-2)+0}6=\frac{2\cdot(-7)}6=-\frac73$.
2. **Comprobación vía interpolación:** el interpolador es $p_2(x)=\frac52x^2-\frac{11}2x+1$ y $\int_0^2p_2=-\frac73$ (sympy).

**Erratas de X p. 85.** (i) La nota dice «En el enunciado ponía $f(3)=0$ y era una errata, debía ser $f(3)=0$»: es contradictoria; lo que quiere decir es «debía ser $f(2)=0$», que es lo que se usa. (ii) La última línea escribe $\int_1^2f$ en lugar de $\int_0^2f$. El resultado $-\frac73$ es correcto.

## X p. 100 («Electrónica 1», I. Electrónica Industrial y Automática, Ej. 5, 3 puntos) — **solución impresa sin números**

> Encuentre una función $f$ cuya gráfica pase por los puntos $(0,15)$, $(1,18)$, $(2,20)$ y $(4,23)$. Aproxime $\int_0^2f(x)\,dx$ utilizando el método del trapecio y el método de Simpson. (No hay una errata, se trata de la integral entre 0 y 2.)

**Idea en una frase.** Son los datos de U Ej. 3.17-3.18: la función pedida es el interpolador $p_3$; las integrales se hacen con los datos en $0,1,2$.
1. **Función** (U Ej. 3.18 p. 124): $p_3(x)=15+3x-\frac12x(x-1)+\frac1{12}x(x-1)(x-2)=\frac1{12}x^3-\frac34x^2+\frac{11}3x+15$.
2. **Trapecio simple** (U Def. 6.5 p. 267): $\frac{2-0}2(15+20)=35$. **Compuesto** con $h=1$ (Def. 6.6): $\frac12(15+2\cdot18+20)=\frac{71}2=35{,}5$. (X admite cualquiera de los dos.)
3. **Simpson** en $0,1,2$: $\frac{2}6(15+4\cdot18+20)=\frac{107}3\approx35{,}667$.
4. **Comparación (propia):** $\int_0^2p_3=\frac{107}3$, igual que Simpson: Simpson es exacto para polinomios de grado $\le3$ (su cota de error, U Teor. 6.4 p. 270, lleva $f^{(4)}$, que es 0 para una cúbica). Verificado con sympy.

**Omisión de X.** La solución impresa solo dice que el polinomio es el de U Ej. 3.18 y que la integral se aproxima «sin más que sustituir los datos»; no da ningún valor. Los números de arriba son cálculo propio.

## X pp. 119-121 (Examen 4 «elaborado con exámenes de asignaturas similares», Ej. 5)

> Determínese un polinomio de grado 3 que aproxime a $f(x)=\ln x$ a partir de los valores de la función $\ln x$ en los nodos 1,3; 1,4; 1,5 y 1,6. Para ello, utilícense diferencias divididas y 4 cifras significativas. A partir de este polinomio, estímese el valor de $\ln 1{,}47$.

**Idea en una frase.** Igual que E 3.24, pero con decimales: tabla, Newton y evaluar **sin desarrollar** para no acumular redondeos.
1. **Datos (4 decimales):** $\ln1{,}3=0{,}2624$; $\ln1{,}4=0{,}3365$; $\ln1{,}5=0{,}4055$; $\ln1{,}6=0{,}4700$.
2. **Orden 1** (dividir entre $0{,}1$): $0{,}741$; $0{,}690$; $0{,}645$.
3. **Orden 2** (entre $0{,}2$): $\frac{0{,}690-0{,}741}{0{,}2}=-0{,}255$; $\frac{0{,}645-0{,}690}{0{,}2}=-0{,}225$.
4. **Orden 3** (entre $0{,}3$): $\frac{-0{,}225+0{,}255}{0{,}3}=0{,}1$.
5. **Newton:** $p_3(x)=0{,}2624+0{,}741(x-1{,}3)-0{,}255(x-1{,}3)(x-1{,}4)+0{,}1(x-1{,}3)(x-1{,}4)(x-1{,}5)$.
6. **Evaluar en 1,47** (factores $0{,}17$; $0{,}07$; $-0{,}03$): $0{,}2624+0{,}12597-0{,}0030345-0{,}0000357=0{,}3852998\approx$ **0,3853**.
7. **Comprobación:** $\ln1{,}47=0{,}385262$. Diferencias verificadas con sympy. Sobre el tamaño del error, ver el ejemplo propio P4.

**Detalles de X (no cambian el resultado).** (i) p. 120: los rangos de $k$ están desplazados: $x_{k+1}-x_k=0{,}1$ es para $k=0,1,2$ (X pone $0,\dots,3$); $x_{k+2}-x_k=0{,}2$ para $k=0,1$ (X: $0,\dots,2$); $x_{k+3}-x_k=0{,}3$ solo para $k=0$ (X: $0,1$). (ii) p. 121: redondea $0{,}741\cdot0{,}17=0{,}12597$ a $0{,}1260$ y obtiene $0{,}3853293$; sin ese redondeo sale $0{,}3852998$. Con 4 cifras, ambos son $0{,}3853$. (iii) X desarrolla también el polinomio ($\approx0{,}1x^3-0{,}675x^2+2{,}017x-1{,}438$; sympy da $2{,}0165$ en el término en $x$) y avisa, con razón, de que evaluar esa forma introduce más redondeo.
**Receta.** Con decimales: evaluar la forma de Newton directamente y redondear solo al final.

## X p. 151 (Feb. 2019, 1.ª semana, Ej. 5, 3 puntos) — **con erratas menores**

> De una función $f$ se sabe que $f(1)=2$, $f(3)=3$, $f(4)=2$ y $f(8)=10$. • Aproxime el valor de $f(2)$ utilizando el polinomio interpolador. (1.5 PUNTOS) • Usando el valor de $f(2)$ obtenido en el apartado anterior, aproxime el valor de $\int_1^4f(x)\,dx$ mediante la fórmula compuesta de Simpson en dos subintervalos. (1.5 PUNTOS)

**Idea en una frase.** (a) Nodos no equiespaciados: cada división usa su propio denominador. (b) Con el interpolador se conoce $f$ «en cualquier punto» de $[1,4]$ y se aplica Simpson compuesta.

**Apartado (a).**
1. **Orden 1:** $\frac{3-2}{3-1}=\frac12$; $\frac{2-3}{4-3}=-1$; $\frac{10-2}{8-4}=2$.
2. **Orden 2:** $\frac{-1-\frac12}{4-1}=-\frac12$; $\frac{2-(-1)}{8-3}=\frac35$.
3. **Orden 3:** $\frac{\frac35+\frac12}{8-1}=\frac{11/10}{7}=\frac{11}{70}$.
4. **Newton:** $p(x)=2+\frac12(x-1)-\frac12(x-1)(x-3)+\frac{11}{70}(x-1)(x-3)(x-4)$.
5. **En $x=2$** (factores $1$, $-1$, $-2$): $2+\frac12+\frac12+\frac{11}{70}\cdot2=3+\frac{11}{35}=\frac{116}{35}\approx$ **3,3143**.

**Apartado (b)** (X avisa de que el enunciado tiene una errata: debería decir «usando el polinomio interpolador»; se admitieron todos los planteamientos razonables.)
6. **Simpson compuesta, 2 subintervalos** de $[1,4]$ (U Def. 6.8 p. 268): $h=\frac{4-1}2=\frac32$; nodos $1,\ \frac74,\ \frac52,\ \frac{13}4,\ 4$ (extremos y puntos medios).
7. **Fórmula:** $\frac h6\left(p(1)+4p(\tfrac74)+2p(\tfrac52)+4p(\tfrac{13}4)+p(4)\right)=\frac{2409}{280}\approx$ **8,6036**. Coincide con el 8,6035 de X (truncado).
8. **Observación (propia):** es **exactamente** $\int_1^4p(x)\,dx=\frac{2409}{280}$, porque Simpson es exacto para cúbicas (U Teor. 6.4 p. 270: $f^{(4)}=0$). Otra lectura que X admite: Simpson simple en $1,2,3$ (con $p(2)$) + trapecio en $[3,4]$, que da $\frac{601}{70}\approx8{,}5857$. Todo verificado con sympy.

**Erratas de X p. 151.** (i) En el desarrollo de $p(x)$ aparece «$+[x_0,x_1,x_2,x_3](x-x_0)\ldots$»: falta la $f$, es $f[x_0,x_1,x_2,x_3]$. (ii) $\frac{116}{35}=3{,}31428\ldots$ se redondea a $3{,}3143$ (X escribe $3{,}3142$, truncando). (iii) Errata del enunciado del apartado (b), reconocida por X.
**X p. 152 (revisada).** Contiene solo el Ej. 6 de ese examen (gradiente y puntos críticos de $f(x,y)=xy(5x-15+y)$, Temas 4-5), **no** interpolación. La Simpson compuesta del Ej. 5 termina en la p. 151. Verificado con sympy: $\nabla f(2,-3)=(-6,-22)$ y puntos críticos $(0,0),(3,0),(0,15),(1,5)$, como X. Sin erratas.
**Receta.** Nodos no equiespaciados: el denominador es siempre $x_{\text{último}}-x_{\text{primero}}$ del grupo. Si un apartado necesita valores de $f$ que no se tienen, se sacan del interpolador.

---

## (a) Teoría necesaria (U; páginas impresas verificadas en `ingenieros.txt`)

- **U §3.3.1** Motivación, p. 119. **Orientaciones y objetivos**, p. 120 (dibujar los datos; comprobar el resultado).
- **U §3.3.2** Interpolación, pp. 120-121: datos $(x_k,f_k)$, nodos, $p_n$ con $p_n(x_k)=f_k$ (p. 120); sistema lineal de $n+1$ ecuaciones, «el grado … es $n$ como máximo», existencia y unicidad sin demostración (p. 121). **Ej. 3.16** (recta y parábola), pp. 121-122.
- **Diferencias divididas**, p. 123 (órdenes 0, 1 y $m$; tabla). **Ej. 3.17**, p. 123.
- **Forma de Newton**, p. 124. **Ej. 3.18** ($p_3=\frac1{12}x^3-\frac34x^2+\frac{11}3x+15$), p. 124. **Añadir un nodo**: $p_n=p_{n-1}+f[x_0,\dots,x_n](x-x_0)\cdots(x-x_{n-1})$, p. 124.
- **Rolle**, U §2.5.2 p. 95; **resto de Lagrange de Taylor**, U Prop. 3.2 y Def. 3.3 p. 111 (para el Bloque D).
- **Tema 6 (para X):** trapecio, Def. 6.5 p. 267; trapecio compuesto, Def. 6.6 p. 267; Simpson «por un polinomio de grado dos (parábola) que pasa por» $a,\frac{a+b}2,b$, p. 267, y Def. 6.7 p. 268; Simpson compuesta, Def. 6.8 p. 268; cotas de error, Teor. 6.3 p. 269 y Teor. 6.4 p. 270.

## (b) Huecos de U y dónde suplirlos

| Hueco | Dónde |
|---|---|
| Demostración de la unicidad | U la remite a un libro externo (p. 121, nota 1). Argumento propio en el Bloque A (teorema del factor). |
| Fórmula del error de interpolación (forma de Lagrange) | No está en U, S ni L. Bloque D (P), con demostración vía Rolle (U p. 95). Pendiente: cotejar con las «notas adicionales» del módulo III cuando estén disponibles. |
| Las diferencias divididas no dependen del orden de los nodos | No está en U. Bloque C (P), verificado con sympy. Útil para E 3.28. |
| Grado exacto del interpolador | U p. 124 dice «Su grado es 3, porque tenemos 4 datos»; lo preciso es «grado $\le3$; es 3 porque $f[x_0,\dots,x_3]=\frac1{12}\neq0$». |

## (c) Erratas, omisiones y avisos

**E:**
1. **E 3.22 (p. 107):** «el grado será menor o igual que $n$» es impreciso: con $n$ puntos el grado es $\le n-1$, y por eso la afirmación es **siempre** falsa. El contraejemplo de E supone además que el polinomio tiene $n$ raíces reales.
2. **E 3.28 (p. 113):** la respuesta «11» para el nodo 2005,5 supone la tabla ordenada. Como las diferencias divididas no dependen del orden, añadiendo el nodo al final bastan **5** (verificado con sympy).
3. **E 3.25 (p. 109):** el texto menciona 1, 2 y 4 s, pero la tabla incluye $t=0$ (se sigue la tabla, como E).
4. **E 3.27 (pp. 111-112):** «33625.1Û6» y «95662.1Û6» son la extracción de $33625{,}1\overline6$ y $95662{,}1\overline6$ ($\frac{201751}6$ y $\frac{573973}6$). No es errata del libro.
5. E 3.21, 3.23, 3.24, 3.26 y 3.27: correctos (verificados).

**X:**
1. **X pp. 65-66:** «$f(0)=31$, $f(1)=26$» en lugar de $f(1)=31$, $f(2)=26$ (resultados correctos).
2. **X p. 123 (nuevo, no estaba en el dossier):** trapecio $=68$ por sustituir $f(x_1)=31$; **lo correcto es 63**. Arrastrado en la comparación de p. 124.
3. **X p. 85:** nota contradictoria («$f(3)=0$ … debía ser $f(3)=0$»; quiere decir $f(2)=0$) y $\int_1^2$ en lugar de $\int_0^2$. Resultado $-\frac73$ correcto.
4. **X p. 101:** «$f(3)$» en lugar de $f(8)$. $p(8)=-9$ correcto, pero es una extrapolación poco fiable.
5. **X p. 107:** no da $f(1)$ ($=\frac{19}8$).
6. **X p. 100:** no da ningún valor numérico (trapecio 35 o 35,5; Simpson $\frac{107}3$).
7. **X pp. 120-121:** rangos de $k$ desplazados en una unidad; redondeo intermedio ($0{,}3853293$ frente a $0{,}3852998$); ambos dan $0{,}3853$.
8. **X p. 151:** falta la $f$ en $f[x_0,x_1,x_2,x_3]$; $\frac{116}{35}\approx3{,}3143$ (no $3{,}3142$). Simpson compuesta $\frac{2409}{280}\approx8{,}6036$, correcta (y igual a $\int_1^4p$).
9. **X p. 152:** no es de interpolación (Ej. 6, gradiente y puntos críticos); correcta.

## (d) Figuras

| Libro | Pág. PDF (impresa) | Contenido | Uso |
|---|---|---|---|
| U | 122 (124) | Gráfica de $p_3$ del Ej. 3.18 con los cuatro datos | Bloque B |
| E | 109 (109) | Figura 3.4: los cuatro puntos de E 3.24 y su interpolador | Ej. 3.24 |
| X | 66 (66) | Trapecio (poligonal) frente a Simpson (parábola) con los datos 31, 26, 43 | X pp. 65-66 (solo uso personal) |
