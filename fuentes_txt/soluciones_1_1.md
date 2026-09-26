# Soluciones — Tema 1.1 El espacio ℝ

**Fuentes.** Ejercicios: libro **E** (*Libro de ejercicios Cálculo 24-25*, `ejercicios.txt`; página impresa = PDF). Teoría: libro **U** (*Cálculo para Ingenieros*, `ingenieros.txt`; página impresa = PDF + 2). Todas las páginas citadas se han comprobado en los `.txt`. Todos los cálculos se han verificado con sympy 1.14 (scripts en el scratchpad de la sesión).

## 0. Alcance y notas de verificación

**Ejercicios de E que dependen solo de §1.1:** **1.1, 1.2, 1.3, 1.4 y 1.5** (E pp. 6-10). Las sucesiones empiezan en el **Ejercicio 1.6** (E p. 10), que trata de la convergencia de $\{x_n y_n\}$ y ya es materia de §1.2. El Ejercicio 1.4 habla de «sucesión», pero solo pide el supremo y el ínfimo de un conjunto, así que es de §1.1. Hasta E p. 50 no hay más ejercicios de supremo o ínfimo que dependan solo de §1.1: el 1.37 (p. 37) usa supremo e ínfimo, pero de la imagen de una función, con límites y Weierstrass (§1.4).

**Mapa de la teoría de U §1.1 (verificado):**

| Contenido | U, página impresa |
|---|---|
| ℕ, ℤ, ℚ, ℝ, irracionales $\mathbb I$ | §1.1.2, pp. 12-13 |
| Recta real, orden, Ejemplo 1.1 | p. 14 |
| Propiedades del orden (1-7), Ejemplo 1.2 | p. 15 |
| Def. 1.1 (valor absoluto), Def. 1.2 (distancia) | p. 15 |
| Teorema 1.1 (propiedades de $\lvert\cdot\rvert$), Ejemplo 1.3 (contraejemplo) | p. 16 |
| Intervalos (definiciones) | pp. 16-17 |
| Centro $\frac{a+b}{2}$, radio $\frac{b-a}{2}$, $(c-r,c+r)=\{\lvert x-c\rvert<r\}$, Ejemplo 1.4 | p. 17 |
| Ejemplo 1.5; Def. 1.3 (cota superior); Ejemplo 1.6 | p. 18 |
| Ejemplo 1.7 (ℕ no tiene cotas superiores); Defs. 1.4, 1.5, 1.6 (acotado); Ejemplo 1.8 | p. 19 |
| Ejemplo 1.9; Def. 1.7 (supremo); Def. 1.8 (ínfimo); unicidad; Ejemplos 1.10, 1.11 | p. 20 |
| Ejemplos 1.12, 1.13; **Axioma del supremo**; versión para el ínfimo | p. 21 |

**Incidencias en las fuentes y en el dossier previo:**

1. **§1.1 de U termina en la p. 21, no en la p. 20.** El Axioma del supremo y los Ejemplos 1.12 y 1.13 están en la p. 21. §1.2 empieza en la p. 22.
2. **U no define máximo ni mínimo, no enuncia la propiedad arquimediana ni la densidad, y no da la caracterización ε del supremo.** CLAUDE.md dice que están en §1.1, pero no aparecen en el texto. Lo más cercano es el **Ejemplo 1.7 (p. 19)**: ℕ no está acotado superiormente, que en la práctica funciona como propiedad arquimediana. En este documento, lo que no está en U se marca como **(propia)**.
3. **El dossier previo cita mal una página:** el Ejercicio 1.4 está en **E pp. 8-9**, no en las pp. 9-10.
4. **Símbolos perdidos en la extracción del texto (seguramente no son erratas del libro).** `pdftotext` elimina la barra de los símbolos negados, y pasa igual en U: «$q = 0$» por $q\neq0$ (p. 12), «$A=\emptyset$» por $A\neq\emptyset$ (p. 21). Por eso en E:
   - 1.1 (p. 6), última línea: «$I_1\ \ I_2$» debe leerse $I_1\not\subset I_2$.
   - 1.2 (p. 7): «$-y+4 = |y+4|$» debe leerse $-y+4\neq|y+4|$. También «$x\in(-|y+4|,|y+4|)$» debe leerse $x\notin(\dots)$.
   - 1.5 (p. 10): «Observa que C 2/3 µF…» tiene un símbolo perdido.

   Conviene confirmarlo en el PDF.
5. **Erratas o imprecisiones reales de E** (se detallan en cada ejercicio):
   - **1.2:** para $y<0$ escribe $x\in(-y,y)$, que es un intervalo **vacío**; debe ser $(y,-y)=(-|y|,|y|)$. Además escribe $|x|>|y+4|$ donde debería ser $|x|\ge|y+4|$. Por último, para $y=0$ dice que «la pregunta no tiene sentido» (y escribe $x<0$ en vez de $|x|<0$). En realidad la implicación es **cierta por vacuidad**.
   - **1.4:** el razonamiento por reducción al absurdo escribe «$c\ge \frac1m>0$ (basta tomar $m\ge 1/c$)». Así no hay contradicción. Hace falta la desigualdad **estricta** $\frac1m<c$, es decir, tomar $m>1/c$.
   - **1.5:** justifica que $2/3$ y $28/11$ son el ínfimo y el supremo «porque se obtienen a partir de los ínfimos y supremos de $C_1$ y $C_2$». Ese argumento no basta: combinando desigualdades se obtienen **cotas**, no necesariamente las óptimas. Hay que comprobar que esos valores **se alcanzan**, y se alcanzan, así que son mínimo y máximo.
   - **1.3:** da el supremo y el ínfimo sin justificarlos. Aquí se justifican.
6. **En U (p. 21)**, la fórmula del Axioma del supremo («si $A\subset\mathbb R$ y $A\neq\emptyset$, entonces $\sup A\in\mathbb R$») omite la hipótesis «acotado superiormente», que sí está en el enunciado en palabras. La versión para el ínfimo omite «$A\neq\emptyset$». Hay que usar siempre las dos hipótesis.

---

## Ejercicio 1.1 (E p. 6)

> Sean $I_1$ e $I_2$ los intervalos dados por
> $$I_1=(-3,5],\qquad I_2=\{x\in\mathbb R:\ |x-3|<4\}.$$
> Elige la o las opciones correctas:
> a) Los dos intervalos tienen el mismo radio.
> b) El centro de $I_1$ es menor que el centro de $I_2$.
> c) Se cumple $I_1\subset I_2$.
> d) Ninguna de las anteriores.

**Solución**

1. **Traducir $I_2$ a extremos.** Por U p. 17, $\{x:|x-c|<r\}=(c-r,c+r)$, porque $|x-c|$ es la distancia de $x$ a $c$ (Def. 1.2, p. 15). Aquí $c=3$ y $r=4$, luego $I_2=(3-4,3+4)=(-1,7)$. Comprobación directa: $|x-3|<4 \iff -4<x-3<4 \iff -1<x<7$, sumando 3 a cada miembro (propiedad 5 del orden, U p. 15).
2. **Centro y radio de $I_1=(-3,5]$.** Con las fórmulas de U p. 17 (valen para cualquier intervalo de extremos $a<b$, abierto, cerrado o semiabierto): $c_1=\frac{-3+5}{2}=1$ y $r_1=\frac{5-(-3)}{2}=4$.
3. **Opción a).** $r_1=4=r_2$. **Correcta.**
4. **Opción b).** $c_1=1<3=c_2$. **Correcta.**
5. **Opción c).** Para refutar una inclusión basta un punto de $I_1$ que no esté en $I_2$ (un contraejemplo, U Ejemplo 1.3, p. 16). Tomamos $x=-2$: está en $I_1$ porque $-3<-2\le5$, pero $|-2-3|=5\not<4$, así que no está en $I_2$. Por tanto $I_1\not\subset I_2$. De hecho $I_1\setminus I_2=(-3,-1]$ (verificado con sympy). **Falsa.**
6. **Opción d).** Falsa, porque a) y b) son correctas.

**Respuesta:** a) y b).

**Receta.** Pasa todos los intervalos a la misma forma: extremos $(a,b)$ o centro y radio $(c,r)$, con $c=\frac{a+b}2$, $r=\frac{b-a}2$ y $|x-c|<r\iff x\in(c-r,c+r)$. Después compara números. Para negar una inclusión, busca un punto concreto que esté en uno y no en el otro.

**Error típico.** Leer $|x-3|<4$ como $(-4,4)$ o como $(3,7)$, es decir, olvidar que $c$ es el centro y $r$ el radio. Otro error es pensar que dos intervalos con el mismo radio y centros cercanos tienen que estar uno dentro del otro.

---

## Ejercicio 1.2 (E pp. 7-8)

> Sean $x$ e $y$ dos números reales tales que $|x|<|y|$. ¿Debe ser $|x|<|y+4|$?

**Solución**

1. **Entender la pregunta.** «¿Debe ser…?» pregunta si la implicación $|x|<|y|\Rightarrow|x|<|y+4|$ es cierta **para todos** los $x,y$. Para responder «no» basta **un contraejemplo** (U Ejemplo 1.3, p. 16). Para responder «sí» habría que demostrarlo en general.
2. **Lectura geométrica.** $|x|<|y|$ significa que $x$ está en el intervalo de centro 0 y radio $|y|$, $(-|y|,|y|)$ (U p. 17). La pregunta es entonces si $(-|y|,|y|)\subset(-|y+4|,|y+4|)$, y eso depende de si $|y|\le|y+4|$.
3. **Caso $y>0$.** Por la Def. 1.1 (U p. 15), $|y|=y$. Como $y+4>0$, también $|y+4|=y+4$. Además $y<y+4$ (propiedad 5 del orden, p. 15). Por transitividad (propiedad 4), $|x|<|y|=y<y+4=|y+4|$. En este caso **sí** se cumple.
4. **Caso $y=0$.** Ningún $x$ cumple $|x|<0$, porque $|x|\ge0$. La hipótesis nunca se da y la implicación es cierta **por vacuidad** (E dice que «no tiene sentido», lo cual es impreciso).
5. **Caso $y<0$.** Ahora $|y|=-y$, y el signo de $y+4$ puede ser cualquiera. Si $y+4<0$ (es decir, $y<-4$), entonces $|y+4|=-(y+4)=-y-4<-y=|y|$: el segundo intervalo es **más pequeño** y la implicación puede fallar.
6. **Contraejemplo (el de E).** $y=-6$, $x=-5$. Entonces $|x|=5<6=|y|$, así que se cumple la hipótesis. Pero $|y+4|=|-2|=2<5=|x|$, así que no se cumple $|x|<|y+4|$. **Respuesta: no, en general no.**
7. **Ampliación (propia).** ¿Para qué $y$ vale la implicación con cualquier $x$? Hace falta $|y|\le|y+4|$. Como ambos lados son $\ge0$, podemos elevar al cuadrado: $y^2\le y^2+8y+16\iff y\ge-2$. Por tanto la implicación vale para todo $x$ si y solo si $y\ge-2$ (verificado con sympy: `solveset(|y|<=|y+4|) = [-2, oo)`). Para $y<-2$ siempre hay contraejemplos: cualquier $x$ con $|y+4|\le|x|<|y|$.

**Erratas de E en este ejercicio:**
- Para $y<0$ escribe $x\in(-y,y)$, que es vacío porque $-y>y$. Debe ser $(y,-y)=(-|y|,|y|)$.
- «o lo que es lo mismo $|x|>|y+4|$» debería ser $|x|\ge|y+4|$ (equivale a $x\notin(-|y+4|,|y+4|)$).

**Receta.** Ante «¿debe cumplirse…?» con valores absolutos: (1) quita los valores absolutos distinguiendo casos por el signo de lo que hay dentro (Def. 1.1); (2) si un caso da problemas, fabrica un contraejemplo numérico concreto y compruébalo. Para comparar $|u|$ con $|v|$, puedes elevar al cuadrado, porque ambos son $\ge0$.

**Error típico.** Suponer que las desigualdades se «trasladan» dentro del valor absoluto: $y<y+4$ **no** implica $|y|<|y+4|$ (compara con U Ejemplo 1.3: $x<y\not\Rightarrow|x|<|y|$). Otro error es dar como respuesta «sí» porque se ha probado solo un caso ($y>0$).

---

## Ejercicio 1.3 (E p. 8)

> Dado el conjunto $A=\{x\in\mathbb R:\ 0<x^2<1\}$, se pide elegir la opción correcta:
> a) $\inf A=0$.
> b) $A$ tiene supremo pero no tiene ínfimo.
> c) $A$ está acotado.
> d) Ninguna de las anteriores.

**Solución**

1. **Reescribir la condición con valor absoluto.** Por la Def. 1.1 (U p. 15), $|x|=\sqrt{x^2}$, luego $x^2=|x|^2$.
   - $0<x^2\iff x\neq0\iff 0<|x|$ (Teorema 1.1.1, U p. 16: $|x|=0\iff x=0$).
   - $x^2<1\iff|x|^2<1\iff|x|<1$, porque para $t\ge0$ se tiene $t^2<1\iff t<1$.

   Por tanto $A=\{x:\ 0<|x|<1\}$.
2. **Pasar a intervalos.** $|x|<1\iff x\in(-1,1)$ (U p. 17, con $c=0$ y $r=1$). Quitando el 0: $A=(-1,0)\cup(0,1)$ (verificado con sympy).
3. **Cotas.** Todo $a\in A$ cumple $-1<a<1$, así que $1$ es cota superior y $-1$ es cota inferior (Defs. 1.3 y 1.5, U pp. 18-19). Por tanto $A$ está **acotado** (Def. 1.6, p. 19).
4. **$\sup A=1$ (Def. 1.7, U p. 20).** (i) 1 es cota superior (paso 3). (ii) Supongamos que $c<1$ también fuera cota superior. Como $\tfrac12\in A$, tendría que ser $c\ge\tfrac12>0$. Entonces el punto medio $a=\frac{c+1}{2}$ cumple $c<a<1$ y $a>0$, luego $a\in A$ y $a>c$, lo que contradice que $c$ sea cota superior. Así, toda cota superior es $\ge1$, y 1 es la menor. Como $1\notin A$, es supremo pero **no máximo**.
5. **$\inf A=-1$.** Se razona igual por simetría ($x\in A\iff -x\in A$). Compara con U Ejemplo 1.10 (p. 20): $(-1,1)$ tiene supremo 1 e ínfimo $-1$. Quitar el 0, que está en el interior, no cambia los extremos.
6. **Revisar las opciones.**
   - a) Falsa: $\inf A=-1$. De hecho 0 ni siquiera es cota inferior, porque $-\tfrac12\in A$ y $-\tfrac12<0$.
   - b) Falsa: tiene ínfimo.
   - c) **Correcta.**
   - d) Falsa.

**Respuesta:** c).

**Receta.** Convierte la condición del conjunto en intervalos (pasando por $|x|$ cuando aparece $x^2$). Después lee el supremo y el ínfimo: el supremo de una unión finita de intervalos es el mayor de los extremos derechos y el ínfimo el menor de los extremos izquierdos. «Agujeros» interiores como el $\{0\}$ no afectan.

**Error típico.** Ver «$0<x^2$» y concluir que $\inf A=0$, confundiendo $x^2$ con $x$. También es un error olvidar los $x$ negativos al despejar $x^2<1$ (escribir solo $x<1$).

---

## Ejercicio 1.4 (E pp. 8-9)

> Sea $S$ el conjunto dado por
> $$S=\left\{1,\ \frac12,\ \frac13,\ \dots,\ \frac1n,\ \dots\right\}.$$
> Se pide encontrar su ínfimo y su supremo. ¿Están en $S$?

**Solución**

1. **Describir el conjunto.** $S=\{\frac1n:\ n\in\mathbb N\}$ con $\mathbb N=\{1,2,3,\dots\}$ (U p. 12). Sus primeros elementos son $1,\frac12,\frac13,\dots$ y parecen decrecer hacia 0. Hay que **demostrarlo** con las definiciones.
2. **1 es cota superior.** Para $n\in\mathbb N$ se tiene $n\ge1$. Multiplicando por $\frac1n>0$ (propiedad 6 del orden, U p. 15): $1\ge\frac1n$. Por tanto $\frac1n\le1$ para todo $n$ (Def. 1.3, p. 18).
3. **$\sup S=1$ y está en $S$.** Si $c$ es cualquier cota superior, como $1\in S$ (con $n=1$), debe ser $1\le c$. Esto es justo la condición (ii) de la Def. 1.7 (p. 20). Luego $\sup S=1\in S$. **Idea general:** si una cota superior pertenece al conjunto, es automáticamente el supremo, y además es el **máximo** (propia).
4. **0 es cota inferior.** $n>0\Rightarrow\frac1n>0$, luego $\frac1n\ge0$ para todo $n$ (Def. 1.5, p. 19).
5. **0 es la mayor cota inferior (reducción al absurdo).** Supongamos que $c>0$ fuera cota inferior de $S$. Por U Ejemplo 1.7 (p. 19), ℕ no está acotado superiormente, así que el número $\frac1c$ no es cota superior de ℕ: existe $m\in\mathbb N$ con $m>\frac1c$. Multiplicando por $\frac{c}{m}>0$ (propiedad 6) se obtiene $c>\frac1m$. Pero $\frac1m\in S$ y es **estrictamente** menor que $c$, lo que contradice que $c$ sea cota inferior. Por tanto ninguna cota inferior es $>0$, y $\inf S=0$ (Def. 1.8, p. 20).
6. **$0\notin S$.** $\frac1n=0$ no tiene solución, porque $\frac1n>0$. Por tanto 0 es ínfimo pero **no mínimo**.

**Respuesta:** $\sup S=1\in S$ (es el máximo) e $\inf S=0\notin S$ (no hay mínimo).

**Errata de E.** Escribe «$c\ge\frac1m>0$ (basta tomar $m\ge 1/c$)». Con $m\ge\frac1c$ solo se garantiza $\frac1m\le c$, y que un elemento sea $\le c$ no contradice que $c$ sea cota inferior (podría ser $\frac1m=c$). Hay que tomar $m>\frac1c$ para obtener $\frac1m<c$ estricto.

**Receta.** Para probar $\inf A=s$: (i) comprueba que $s\le a$ para todo $a\in A$; (ii) supón que existe una cota inferior $c>s$ y encuentra un elemento de $A$ **menor que $c$**. Para hallarlo suele bastar el Ejemplo 1.7 (existe $m\in\mathbb N$ mayor que cualquier número dado). Por último, mira si $s\in A$ para decidir si es mínimo.

**Error típico.** Decir que $\inf S=0$ «porque $\frac1n$ tiende a 0» sin demostrar que ningún $c>0$ es cota inferior. Otro error es afirmar que $0\in S$, o que $S$ tiene mínimo.

---

## Ejercicio 1.5 (E p. 10)

> Tenemos dos condensadores, $C_1$ y $C_2$, conectados en serie. La capacidad equivalente $C$ de la asociación verifica
> $$\frac1C=\frac1{C_1}+\frac1{C_2}.$$
> Los dos condensadores tienen capacidad variable y la capacidad de $C_1$ varía entre 2 y 4 microfaradios (µF) y la de $C_2$ entre 1 y 7 µF. Se pide encontrar entre qué valores se encuentra la capacidad del condensador equivalente $C$.

**Solución** (se interpreta «varía entre» como $C_1\in[2,4]$ y $C_2\in[1,7]$).

1. **Datos como desigualdades.** $2\le C_1\le4$ y $1\le C_2\le7$. Todas las cantidades son positivas.
2. **Invertir, lo que da la vuelta a las desigualdades entre positivos.** Si $0<a\le b$, al multiplicar por $\frac1{ab}>0$ (propiedad 6 del orden, U p. 15) queda $\frac1b\le\frac1a$. Por tanto $\frac14\le\frac1{C_1}\le\frac12$ y $\frac17\le\frac1{C_2}\le1$.
3. **Sumar desigualdades.** Por U Ejemplo 1.2 (p. 15), $x\le y$ y $z\le w$ implican $x+z\le y+w$:
   $$\frac{11}{28}=\frac14+\frac17\ \le\ \frac1C\ \le\ \frac12+1=\frac32.$$
4. **Invertir otra vez (paso 2).** $\frac23\le C\le\frac{28}{11}$. Así, $\frac23$ µF es una cota inferior y $\frac{28}{11}\approx2{,}545$ µF una cota superior de los valores de $C$.
5. **¿Son las mejores cotas? Comprobar que se alcanzan** (este paso falta en E).
   - Con $C_1=2$ y $C_2=1$: $\frac1C=\frac12+1=\frac32$, luego $C=\frac23$.
   - Con $C_1=4$ y $C_2=7$: $\frac1C=\frac14+\frac17=\frac{11}{28}$, luego $C=\frac{28}{11}$.

   Una cota que pertenece al conjunto es su ínfimo (o supremo), y además su mínimo (o máximo), como en el Ejercicio 1.4, paso 3. Verificado con sympy: $C=\frac{C_1C_2}{C_1+C_2}$ y $\partial C/\partial C_1=\frac{C_2^2}{(C_1+C_2)^2}>0$, así que $C$ crece con cada capacidad. Un barrido de la malla da mínimo $2/3$ y máximo $28/11$.

**Respuesta:** $\frac23\ \mu F\le C\le\frac{28}{11}\ \mu F$. El valor $\frac23$ es el ínfimo (y mínimo) y $\frac{28}{11}$ el supremo (y máximo). Si los intervalos de $C_1$ y $C_2$ fueran abiertos, esos valores seguirían siendo el ínfimo y el supremo, pero no se alcanzarían.

**Receta.** Para acotar una expresión de variables acotadas: escribe cada variable como desigualdad, transforma paso a paso (sumar conserva el sentido; invertir positivos lo cambia; multiplicar por un negativo lo cambia) y combina. Después **comprueba si las cotas se alcanzan** con valores concretos; si se alcanzan, son el ínfimo y el supremo.

**Error típico.** Invertir sin dar la vuelta a la desigualdad (escribir $\frac12\le\frac1{C_1}\le\frac14$). Otro error es creer que cualquier cota obtenida combinando desigualdades es ya el supremo o el ínfimo: si una misma variable aparece en varios sitios, las cotas pueden no alcanzarse.

---

## Ejemplos propios (verificados con sympy)

### Ejemplo propio 1 (fácil): del valor absoluto al intervalo y al revés

**Enunciado (propio).** (a) Escribe $\{x\in\mathbb R:\ |2x-5|\le3\}$ como intervalo y da su centro y radio. (b) Escribe $(-7,3)$ con valor absoluto.

**Solución.**
1. (a) Saca el coeficiente de $x$: $|2x-5|=2\,|x-\tfrac52|$, porque $|ab|=|a||b|$ se deduce de $|t|=\sqrt{t^2}$ (Def. 1.1). Entonces $|2x-5|\le3\iff|x-\tfrac52|\le\tfrac32$.
2. Por U p. 17 esto es $[\tfrac52-\tfrac32,\tfrac52+\tfrac32]=[1,4]$, con centro $\tfrac52$ y radio $\tfrac32$ (sympy: `Interval(1, 4)`).
3. (b) $c=\frac{-7+3}{2}=-2$ y $r=\frac{3-(-7)}{2}=5$. Por tanto $(-7,3)=\{x:\ |x+2|<5\}$ (sympy: `Interval.open(-7, 3)`).

### Ejemplo propio 2 (medio): suma de dos valores absolutos, supremo e ínfimo

**Enunciado (propio).** Sea $A=\{x\in\mathbb R:\ |x-1|+|x+2|<5\}$. Halla $\sup A$ e $\inf A$. ¿Tiene máximo o mínimo?

**Solución.**
1. Los puntos críticos son donde cambian de signo los contenidos: $x=-2$ y $x=1$. Se estudian tres casos (Def. 1.1):
   - $x<-2$: $-(x-1)-(x+2)=-2x-1<5\iff x>-3$, lo que da $(-3,-2)$.
   - $-2\le x\le1$: $-(x-1)+(x+2)=3<5$, siempre cierto, lo que da $[-2,1]$.
   - $x>1$: $(x-1)+(x+2)=2x+1<5\iff x<2$, lo que da $(1,2)$.
2. Uniendo los casos, $A=(-3,2)$ (sympy: `Interval.open(-3, 2)`).
3. Por U Ejemplo 1.10 (p. 20, el mismo argumento que para $(-1,1)$), $\sup A=2$ e $\inf A=-3$. En $x=2$ y $x=-3$ la suma vale exactamente 5, así que esos puntos no están en $A$. Por tanto **no** hay máximo ni mínimo.
4. **Idea geométrica:** $|x-1|+|x+2|$ es la suma de las distancias de $x$ a $1$ y a $-2$. Nunca baja de 3, que es la distancia entre ellos, y vale 5 a $1$ unidad por fuera de cada punto.

### Ejemplo propio 3 (difícil): supremo no alcanzado con la caracterización ε

**Enunciado (propio).** Sea $B=\left\{\dfrac{2n-1}{n+1}:\ n\in\mathbb N\right\}$. Demuestra que $\sup B=2$, que $\inf B=\min B=\tfrac12$ y que $B$ no tiene máximo.

**Solución.**
1. **Reescribir** para ver la estructura: $\frac{2n-1}{n+1}=2-\frac{3}{n+1}$ (sympy lo confirma). Los primeros términos son $\frac12, 1, \frac54, \frac75, \frac32,\dots$
2. **Mínimo.** $b_{n+1}-b_n=\frac{3}{(n+1)(n+2)}>0$ (sympy), así que los términos crecen y el menor es $b_1=\frac12$. Como $\frac12\in B$ y es cota inferior, $\inf B=\min B=\tfrac12$.
3. **2 es cota superior.** $\frac{3}{n+1}>0\Rightarrow b_n<2$ para todo $n$. En particular $2\notin B$, luego no hay máximo **si** 2 es el supremo.
4. **2 es la menor cota superior (caracterización ε, propia; ver Método 6).** Sea $\varepsilon>0$. Buscamos $n$ con $b_n>2-\varepsilon$, es decir, $\frac3{n+1}<\varepsilon\iff n+1>\frac3\varepsilon$. Por U Ejemplo 1.7 (p. 19) existe $n\in\mathbb N$ con $n>\frac3\varepsilon$, y entonces $n+1>\frac3\varepsilon$. Así, $2-\varepsilon$ no es cota superior para ningún $\varepsilon>0$, y ninguna cota superior puede ser menor que 2. Por tanto $\sup B=2$ (Def. 1.7).
5. **Comprobación numérica.** Para $\varepsilon=0{,}01$ basta $n=300$: $b_{300}=\frac{599}{301}\approx1{,}99003>1{,}99$ (verificado con fracciones exactas).

---

## Métodos del tema

1. **Pasar entre $|x-c|<r$ y $(c-r,c+r)$** (U p. 17).
   - De valor absoluto a intervalo: $|x-c|<r\iff c-r<x<c+r$, y con $\le$ se obtiene el intervalo cerrado $[c-r,c+r]$. Si aparece $|ax-b|$ con $a\neq0$, divide primero: $|ax-b|<r\iff|x-\frac ba|<\frac r{|a|}$.
   - De intervalo a valor absoluto: dado $(a,b)$, toma $c=\frac{a+b}2$ y $r=\frac{b-a}2$, y escribe $\{x:\ |x-c|<r\}$.
   - $|x-c|>r$ es el **complementario**: $(-\infty,c-r)\cup(c+r,\infty)$.
2. **Resolver desigualdades con valores absolutos por casos.** Marca los puntos donde se anula cada $|\cdot|$, estudia cada trozo con la Def. 1.1 (U p. 15) y une los resultados (Ejemplo propio 2). Para comparar $|u|$ y $|v|$, eleva al cuadrado: $|u|\le|v|\iff u^2\le v^2$ (Ejercicio 1.2, paso 7).
3. **Refutar con un contraejemplo** (U Ejemplo 1.3, p. 16). Una afirmación «para todo» se refuta con **un** caso concreto, comprobado con números (Ejercicios 1.1c y 1.2). Una afirmación general no se demuestra con ejemplos.
4. **Hallar el supremo o el ínfimo con la definición** (Defs. 1.7 y 1.8, U p. 20):
   1. Describe el conjunto (intervalos, o la fórmula de sus elementos) y **conjetura** el valor $s$.
   2. Demuestra que $s$ es cota: $a\le s$ para todo $a\in A$ (o $a\ge s$ para el ínfimo).
   3. Demuestra que es la mejor cota: supón que $c<s$ es cota superior (o $c>s$ cota inferior) y encuentra un $a\in A$ que la supere (punto medio, o $\frac1m$ con $m$ grande). Eso es una contradicción.
   4. Decide si $s\in A$ (Ejercicios 1.3 y 1.4).
5. **Atajo: una cota que pertenece al conjunto.** Si $s$ es cota superior y $s\in A$, entonces $s=\sup A=\max A$; con el ínfimo, igual. **Máximo** = supremo que pertenece al conjunto; **mínimo** = ínfimo que pertenece al conjunto (propia: U no los define en §1.1). Se usa en los Ejercicios 1.4 y 1.5 y en el Ejemplo propio 3.
6. **Demostrar $\sup A=s$ con la caracterización ε** (propia, equivalente a la Def. 1.7):
   $$s=\sup A\iff\begin{cases}a\le s\ \ \forall a\in A,\\ \forall\varepsilon>0\ \exists a\in A:\ a>s-\varepsilon.\end{cases}$$
   *Por qué funciona:* cualquier $c<s$ se escribe como $c=s-\varepsilon$ con $\varepsilon=s-c>0$. La segunda condición dice que $c$ no es cota superior, que es lo que exige la condición (ii) de la Def. 1.7. Para el ínfimo: $a\ge s$ para todo $a$, y para todo $\varepsilon>0$ existe $a\in A$ con $a<s+\varepsilon$.
   *Cómo se aplica:* dado $\varepsilon$, despeja qué hace falta (típicamente «$n>\text{algo}(\varepsilon)$») y justifica que existe un tal $n$ con U Ejemplo 1.7 (Ejemplo propio 3).
7. **«Propiedad arquimediana» a partir de U Ejemplo 1.7 (p. 19).** Como ℕ no tiene cotas superiores, para cada número real $K$ existe $m\in\mathbb N$ con $m>K$. Con $K=\frac1c$ se obtiene: para todo $c>0$ existe $m$ con $\frac1m<c$. Es la herramienta que prueba $\inf\{\frac1n\}=0$.
8. **Acotar expresiones de variables acotadas** (Ejercicio 1.5). Traduce cada dato a desigualdades y opera con las propiedades del orden (U p. 15):
   - sumar desigualdades del mismo sentido (Ejemplo 1.2);
   - multiplicar por un positivo conserva el sentido; por un negativo lo invierte;
   - invertir entre positivos lo invierte.

   Después **comprueba si las cotas se alcanzan** antes de llamarlas ínfimo y supremo.
9. **Supremo e ínfimo de intervalos y uniones.** Los intervalos $(a,b)$, $[a,b]$, $(a,b]$ y $[a,b)$ tienen $\inf=a$ y $\sup=b$ (U Ejemplo 1.10, p. 20), y son acotados (U p. 20). En una unión finita de intervalos, el supremo es el mayor extremo derecho y el ínfimo el menor extremo izquierdo. Las semirrectas $(a,\infty)$ no tienen supremo (no están acotadas superiormente).
10. **Existencia: el Axioma del supremo** (U p. 21). Si $A\neq\emptyset$ y está acotado superiormente, $\sup A$ existe en ℝ; análogamente para el ínfimo. Hay que comprobar **las dos** hipótesis. En ℚ puede fallar: $\{x\in\mathbb Q: x^2\le7\}$ no tiene supremo en ℚ (U Ejemplo 1.11, p. 20, y p. 21).
