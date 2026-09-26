# Soluciones — Tema 2.3 Límites y derivación: regla de L'Hôpital

Ejercicios de **E** 2.24–2.33 (E pp. 66–72, impresa = PDF). Teoría: **U §2.3**, pp. 81–85 (impresa = PDF + 2).
Todos los enunciados se han comprobado sobre la imagen del PDF de E (el `.txt` los desfigura) y todos los resultados se han verificado con sympy (`limit`).

**Orden de estudio recomendado (de fácil a difícil), conservando la numeración:**

| Orden | Ejercicio | Tipo de indeterminación | Resultado |
|---|---|---|---|
| 1 | 2.26 | $0/0$ (polinomios) | $-3/4$ |
| 2 | 2.25 | $0/0$ (con raíz y logaritmo) | $-1$ |
| 3 | 2.28 | $\infty/\infty$ lateral | $0$ |
| 4 | 2.30 | $0\cdot\infty$ | $0$ |
| 5 | 2.27 | $\infty/\infty$ donde L'Hôpital «da vueltas» | $1$ |
| 6 | 2.31 | $0^0$ | $1$ |
| 7 | 2.29 | $\infty^0$ (test) | $1$ (opción b) |
| 8 | 2.24 | $1^\infty$ | $\sqrt e$ |
| 9 | 2.32 | $\infty/\infty$ reiterado $n$ veces | $0$ |
| 10 | 2.33 | $0/0$ en una **sucesión** | $1$ |

**Regla de L'Hôpital tal como la usaremos** (U §2.3.2, p. 82, completada con S p. 302 / L p. 558): sean $f,g$ derivables cerca de $a$ (salvo quizá en $a$), con $g'(x)\neq 0$ cerca de $a$ (salvo quizá en $a$). Si $\lim_{x\to a}f=\lim_{x\to a}g=0$, o bien $\lim f=\pm\infty$ y $\lim g=\pm\infty$, **y existe** $\lim_{x\to a}\frac{f'(x)}{g'(x)}=\ell\in\overline{\mathbb R}$, entonces $\lim_{x\to a}\frac{f(x)}{g(x)}=\ell$. Vale también para $a=\pm\infty$, $a^+$, $a^-$ (nota al margen de U p. 82).

Antes de cada aplicación hay que comprobar **tres cosas**: (i) que es un cociente de tipo $0/0$ o $\infty/\infty$; (ii) que $f,g$ son derivables y $g'\neq0$ cerca del punto; (iii) que el límite del cociente de derivadas existe (o es $\pm\infty$).

---

## Ejercicio 2.26 (E p. 67; solución p. 68)

> **Calcula el valor de** $\displaystyle\lim_{x\to-1}\frac{x^5+x^4-x^2+1}{x^4-1}$.

**Solución.**

1. **Sustituir primero.** Numerador en $x=-1$: $-1+1-1+1=0$. Denominador: $1-1=0$. Como los polinomios son continuos (U Prop. 1.13, p. 51), ambos límites valen $0$: indeterminación $\tfrac00$. No se puede usar el cociente de límites (U Prop. 1.11, p. 46 exige límite del denominador $\neq0$).
2. **Comprobar las hipótesis de L'Hôpital** (U p. 82). $f(x)=x^5+x^4-x^2+1$ y $g(x)=x^4-1$ son polinomios, luego derivables en todo $\mathbb R$ (tabla de derivadas, U p. 79). $g'(x)=4x^3$ solo se anula en $x=0$, así que $g'(x)\neq0$ en un entorno de $-1$ (por ejemplo en $(-2,0)$).
3. **Derivar** (regla de la potencia, U p. 79): $f'(x)=5x^4+4x^3-2x$, $g'(x)=4x^3$.
4. **Límite del cociente de derivadas.** Es un cociente de polinomios con denominador $4(-1)^3=-4\neq0$, así que basta sustituir:
$$\lim_{x\to-1}\frac{5x^4+4x^3-2x}{4x^3}=\frac{5-4+2}{-4}=-\frac34 .$$
5. **Conclusión.** Como este límite existe, L'Hôpital da $\displaystyle\lim_{x\to-1}\frac{x^5+x^4-x^2+1}{x^4-1}=-\frac34$.
6. **Comprobación sin L'Hôpital** (lo que sugiere E). Si $x=-1$ anula ambos polinomios, $(x+1)$ divide a los dos (regla de Ruffini): $x^5+x^4-x^2+1=(x+1)(x^4-x+1)$ y $x^4-1=(x+1)(x-1)(x^2+1)$. Para $x\neq-1$ se simplifica y $\lim_{x\to-1}\frac{x^4-x+1}{(x-1)(x^2+1)}=\frac{1+1+1}{(-2)(2)}=-\frac34$. Coincide.

**Receta.** Cociente de polinomios con $0/0$ en $x=a$: o factorizas $(x-a)$ por Ruffini y simplificas, o derivas arriba y abajo una vez y sustituyes; ambos caminos deben coincidir.

**Error típico.** Aplicar la regla del cociente $\left(\frac fg\right)'$ en vez de derivar numerador y denominador **por separado**.

**Teoría:** U §2.3.2 p. 82 (regla); U §2.2.2 p. 79 (tabla de derivadas).

---

## Ejercicio 2.25 (E p. 67)

> **Calcula el valor de** $\displaystyle\lim_{x\to0}\frac{\ln(1+x)-x}{1-\sqrt{1-x^2}}$.

**Solución.**

1. **Tipo.** Numerador: $\ln 1-0=0$. Denominador: $1-\sqrt1=0$. Ambas funciones son continuas en $0$ (composición de continuas, U Prop. 1.14 p. 51), luego tenemos $\tfrac00$.
2. **Hipótesis.** En $(-1,1)$ las dos funciones son derivables (regla de la cadena, U p. 79). Derivadas:
   - $f'(x)=\dfrac{1}{1+x}-1=\dfrac{1-(1+x)}{1+x}=\dfrac{-x}{1+x}$ (derivada de $\ln u$, tabla U pp. 80–81).
   - $g'(x)=-\dfrac{1}{2\sqrt{1-x^2}}\cdot(-2x)=\dfrac{x}{\sqrt{1-x^2}}$ (derivada de $u^{1/2}$ con $u=1-x^2$).

   $g'(x)=0$ solo en $x=0$; por tanto $g'(x)\neq0$ en $(-1,1)\setminus\{0\}$, que es lo que exige U («esta última condición no excluye que $g'(a)$ pueda ser 0», p. 82).
3. **Simplificar antes de pasar al límite.** Para $x\neq0$, $x\in(-1,1)$:
$$\frac{f'(x)}{g'(x)}=\frac{-x}{1+x}\cdot\frac{\sqrt{1-x^2}}{x}=-\frac{\sqrt{1-x^2}}{1+x}.$$
   Podemos cancelar $x$ porque en el límite $x\to0$ nunca se toma $x=0$.
4. **Límite.** La última función es continua en $0$ y vale $-\frac{1}{1}=-1$.
5. **Conclusión.** $\displaystyle\lim_{x\to0}\frac{\ln(1+x)-x}{1-\sqrt{1-x^2}}=-1$.

**Receta.** Tras derivar, **simplifica** el cociente de derivadas antes de sustituir: muchas veces el factor que producía el $0/0$ se cancela y ya no hace falta derivar otra vez.

**Error típico.** Volver a aplicar L'Hôpital sin simplificar (sale una expresión mucho más larga) o decir «$g'(0)=0$, luego no se puede aplicar»: lo que importa es $g'\neq0$ **cerca** de $0$, no en $0$.

**Teoría:** U §2.3.2 p. 82; tabla de derivadas compuestas U pp. 80–81.

---

## Ejercicio 2.28 (E p. 68; solución p. 69)

> **Calcula el valor del límite** $\displaystyle\lim_{x\to\frac{\pi}{2}^-}\frac{2-\ln(\cos x)}{2+\operatorname{tg} x}$.

**Solución.**

1. **Dominio.** Para $x\in(0,\pi/2)$ es $\cos x>0$, así que $\ln(\cos x)$ está definido: tiene sentido el límite **por la izquierda**.
2. **Tipo.** Cuando $x\to\frac\pi2^-$, $\cos x\to0^+$, luego $\ln(\cos x)\to-\infty$ y el **numerador** $2-\ln(\cos x)\to+\infty$. Además $\operatorname{tg}x=\frac{\operatorname{sen}x}{\cos x}\to\frac{1}{0^+}=+\infty$, y el denominador $\to+\infty$. Indeterminación $\frac{+\infty}{+\infty}$ (**no** $\frac{-\infty}{+\infty}$ como dice E: ver erratas).
3. **Hipótesis.** Ambas funciones son derivables en $(0,\pi/2)$. Derivadas:
   - $f'(x)=-\dfrac{1}{\cos x}\cdot(-\operatorname{sen}x)=\dfrac{\operatorname{sen}x}{\cos x}$ (regla de la cadena con $\ln u$, U pp. 80–81).
   - $g'(x)=\dfrac{1}{\cos^2x}$ (U p. 80), que nunca se anula.
4. **Cociente de derivadas.** Dividir entre $\frac1{\cos^2x}$ es multiplicar por $\cos^2x$:
$$\frac{f'(x)}{g'(x)}=\frac{\operatorname{sen}x}{\cos x}\cdot\cos^2x=\operatorname{sen}x\cos x\;\longrightarrow\;1\cdot0=0 .$$
5. **Conclusión.** El límite vale $0$.

*Interpretación:* el numerador crece como $-\ln(\cos x)$ (logarítmicamente) y el denominador como $1/\cos x$ (como una potencia): gana el denominador.

**Receta.** En un límite lateral hacia un punto donde algo se anula, determina primero el **signo** de lo que tiende a $0$ ($0^+$ o $0^-$) para saber si cada trozo va a $+\infty$ o a $-\infty$.

**Error típico.** Equivocar el signo: $\ln(\cos x)\to-\infty$, pero hay un signo menos delante, así que el numerador va a $+\infty$.

**Teoría:** U §2.3.2 p. 82 (y nota al margen: válida para $a^-$); derivada de $\operatorname{tg}$ U p. 80.

---

## Ejercicio 2.30 (E p. 70)

> **Calcula el valor de** $\displaystyle\lim_{x\to0^+}x\ln x$.

**Solución.**

1. **Tipo.** $x\to0^+$ y $\ln x\to-\infty$: producto $0\cdot(-\infty)$. L'Hôpital **no** se aplica a productos (U p. 84: «Las indeterminaciones del tipo $\pm\infty\cdot0$ no aparecen citadas en la Regla»).
2. **Convertir en cociente** (U p. 84: $f\cdot g=\frac{f}{1/g}$). Elegimos pasar al denominador el factor $x$, cuya inversa $1/x$ se deriva fácil:
$$x\ln x=\frac{\ln x}{1/x},$$
   que es de tipo $\frac{-\infty}{+\infty}$.
3. **Hipótesis.** $\ln x$ y $1/x$ son derivables en $(0,\infty)$; $(1/x)'=-1/x^2\neq0$.
4. **L'Hôpital:**
$$\lim_{x\to0^+}\frac{\ln x}{1/x}=\lim_{x\to0^+}\frac{1/x}{-1/x^2}=\lim_{x\to0^+}(-x)=0 .$$
5. **Conclusión.** $\lim_{x\to0^+}x\ln x=0$.
6. **La otra elección (mala).** $x\ln x=\frac{x}{1/\ln x}$ es $\frac00$, pero al derivar sale $\lim(-x(\ln x)^2)$, más complicado que el de partida (E p. 70 lo muestra).

**Receta.** $0\cdot\infty$: escribe $fg=\dfrac{g}{1/f}$ poniendo **en el denominador el factor cuya inversa se deriva fácil** (normalmente la potencia $x^k$, nunca el logaritmo).

**Error típico.** Pensar «$0$ por lo que sea es $0$». Aquí sale $0$, pero $x\cdot\frac1x=1$ también es de tipo $0\cdot\infty$ y vale $1$.

**Teoría:** U §2.3.2 p. 84 (fórmula para $0\cdot\infty$ y Ejemplo 2.11). Es exactamente S §4.4 Ej. 6, p. 305.

---

## Ejercicio 2.27 (E p. 68)

> **Calcula el valor del límite** $\displaystyle\lim_{x\to+\infty}\frac{\operatorname{sen}x+e^x}{\cos x+e^x}$.

**Solución.**

1. **Tipo.** $e^x\to+\infty$ y $\operatorname{sen}x,\cos x\in[-1,1]$; así $\operatorname{sen}x+e^x\ge e^x-1\to+\infty$, y lo mismo el denominador: $\frac{+\infty}{+\infty}$.
2. **Intento con L'Hôpital.** Las hipótesis se cumplen ($g'(x)=-\operatorname{sen}x+e^x\ge e^x-1>0$ para $x>0$), pero
$$\frac{f'}{g'}=\frac{\cos x+e^x}{-\operatorname{sen}x+e^x},\qquad \frac{f''}{g''}=\frac{-\operatorname{sen}x+e^x}{-\cos x+e^x},\ \dots$$
   Tras cuatro derivaciones volvemos al cociente de partida: el método da vueltas y **no simplifica nada**.
3. **Otro camino: dividir por el término dominante** $e^x$ (numerador y denominador):
$$\frac{\operatorname{sen}x+e^x}{\cos x+e^x}=\frac{\operatorname{sen}x\cdot e^{-x}+1}{\cos x\cdot e^{-x}+1}.$$
4. **Límites de cada trozo.** $e^{-x}\to0$ y $\operatorname{sen}x$, $\cos x$ están acotadas, luego $\operatorname{sen}x\,e^{-x}\to0$ y $\cos x\,e^{-x}\to0$ («cero por acotada», U Prop. 1.10 p. 45, aplicada en $+\infty$).
5. **Álgebra de límites** (U Prop. 1.11 p. 46; el denominador tiende a $1\neq0$):
$$\lim_{x\to+\infty}\frac{\operatorname{sen}x\,e^{-x}+1}{\cos x\,e^{-x}+1}=\frac{0+1}{0+1}=1 .$$

**Receta.** Si al derivar reaparece la misma estructura (senos/cosenos que rotan, exponenciales que se reproducen), abandona L'Hôpital y **divide por el término dominante**.

**Error típico.** Concluir que «el límite no existe» porque L'Hôpital no termina. La regla solo informa si sabes calcular $\lim f'/g'$; si no, hay que buscar otro método.

**Teoría:** U Prop. 1.10 p. 45 y Prop. 1.11 p. 46. Advertencia de uso de la regla: S §4.4 p. 305 («debe tener en cuenta otros métodos antes de utilizar la regla»).

---

## Ejercicio 2.31 (E p. 70)

> **Calcula el valor de** $\displaystyle\lim_{x\to0^+}x^{x^2}$.

**Solución.**

1. **Tipo.** Base $x\to0^+$, exponente $x^2\to0$: $0^0$, indeterminado (la base empuja hacia $0$ y el exponente hacia «potencia $0$», que da $1$).
2. **Escribir como exponencial.** Para $x>0$, $x^{x^2}=e^{\ln\left(x^{x^2}\right)}=e^{x^2\ln x}$ (identidad $e^{\ln b}=b$ y «el logaritmo baja exponentes», como en E p. 66).
3. **Límite del exponente**, de tipo $0\cdot(-\infty)$; lo pasamos a cociente como en 2.30:
$$\lim_{x\to0^+}x^2\ln x=\lim_{x\to0^+}\frac{\ln x}{1/x^2}\overset{\text{L'H}}{=}\lim_{x\to0^+}\frac{1/x}{-2/x^3}=\lim_{x\to0^+}\left(-\frac{x^2}{2}\right)=0 .$$
   (Hipótesis: $\frac{-\infty}{+\infty}$, derivables en $(0,\infty)$, $(x^{-2})'=-2x^{-3}\neq0$.)
4. **Volver a la potencia.** Como $\exp$ es continua en $0$ (U Prop. 1.14 p. 51), $\lim e^{x^2\ln x}=e^{0}=1$.

**Receta.** $f^g$ con $0^0$, $\infty^0$ o $1^\infty$: escribe $f^g=e^{g\ln f}$, calcula $L=\lim g\ln f$ (será $0\cdot\infty$) y el resultado es $e^L$ (con $e^{+\infty}=+\infty$, $e^{-\infty}=0$).

**Error típico.** Quedarse en el límite del exponente y responder $0$ en lugar de $e^0=1$ (el propio U lo avisa en el recuadro de p. 85).

**Teoría:** U §2.3.2 pp. 84–85 (Ejemplo 2.12 y recuadro «Ojo»). U solo menciona explícitamente $\infty^0$ y $1^\infty$; el tipo $0^0$ está en S §4.4 p. 306 (Ej. 9, $x^x$, p. 307) y L §8.7 Ej. 6, p. 562.

---

## Ejercicio 2.29 (E p. 69)

> **Señala el valor del límite siguiente** $\displaystyle\lim_{x\to+\infty}x^{\frac{1}{x+1}}$: **a)** $0$. **b)** $1$. **c)** $e$. **d)** $e^e$.

**Solución.**

1. **Tipo.** Base $\to+\infty$, exponente $\frac1{x+1}\to0$: $\infty^0$.
2. **Exponencial.** Para $x>0$: $x^{\frac1{x+1}}=e^{\frac{\ln x}{x+1}}$.
3. **Exponente**, tipo $\frac{+\infty}{+\infty}$; hipótesis: derivables en $(0,\infty)$ y $(x+1)'=1\neq0$:
$$\lim_{x\to+\infty}\frac{\ln x}{x+1}\overset{\text{L'H}}{=}\lim_{x\to+\infty}\frac{1/x}{1}=0 .$$
4. **Continuidad de exp:** el límite es $e^0=1$. **Respuesta b).**
5. *Descarte rápido de opciones (útil en el test):* para $x>1$ la base es $>1$ y el exponente positivo, luego $x^{1/(x+1)}>1$: la a) es imposible; y como el exponente de $e$ tiende a $0$, no puede salir $e$ ni $e^e$.

**Receta.** Igual que 2.31: $\infty^0\Rightarrow e^{\lim g\ln f}$; «logaritmo entre potencia de $x$» tiende siempre a $0$.

**Error típico.** Escribir «$\ln l=\ln\lim\ldots$» sin haber probado que el límite $l$ existe y es positivo (ver erratas); con la forma $e^{g\ln f}$ no hace falta suponer nada.

**Teoría:** U Ejemplo 2.12 p. 84 (mismo tipo: $\lim x^{1/x}=1$).

---

## Ejercicio 2.24 (E p. 66)

> **Calcula el valor de** $\displaystyle\lim_{x\to+\infty}\left(\frac{\ln x^2+1}{2\ln x}\right)^{\ln x}$.

Aquí $\ln x^2+1$ significa $\ln(x^2)+1$ (así lo usa la solución de E; ver erratas).

**Solución (camino 1: el «número $e$», U Prop. 2.2).**

1. **Tipo.** Como $\ln(x^2)=2\ln x$ para $x>0$, la base es $\frac{2\ln x+1}{2\ln x}=1+\frac{1}{2\ln x}\to1$, y el exponente $\ln x\to+\infty$: tipo $1^{+\infty}$.
2. **Ajustar a la forma de la Proposición 2.2** (U p. 85): si $f(x)\to\pm\infty$, entonces $\left(1+\frac1{f(x)}\right)^{f(x)}\to e$. Tomamos $f(x)=\ln x^2=2\ln x\to+\infty$. El exponente que tenemos es $\ln x=\frac12\ln x^2$:
$$\left(1+\frac1{\ln x^2}\right)^{\ln x}=\left[\left(1+\frac1{\ln x^2}\right)^{\ln x^2}\right]^{1/2}$$
   (propiedad $(b^c)^d=b^{cd}$, válida para base $b>0$).
3. **Límite.** Lo de dentro tiende a $e$ por la Prop. 2.2; la función $t\mapsto t^{1/2}$ es continua en $e$ (U Prop. 1.14 p. 51), así que el límite es $e^{1/2}=\sqrt e$.

**Solución (camino 2: logaritmos y L'Hôpital, la «Nota» de E pp. 66–67).**

1. Escribimos la expresión como $e^{h(x)}$ con $h(x)=\ln x\cdot\ln\left(1+\frac1{\ln x^2}\right)$, de tipo $+\infty\cdot0$.
2. Cociente: $h(x)=\dfrac{\ln\left(1+\frac1{\ln x^2}\right)}{1/\ln x}$, tipo $\frac00$.
3. Derivadas (regla de la cadena): numerador $\dfrac{1}{1+\frac1{\ln x^2}}\cdot\left(-\dfrac{1}{(\ln x^2)^2}\cdot\dfrac{2}{x}\right)$; denominador $-\dfrac{1}{(\ln x)^2}\cdot\dfrac1x\neq0$.
4. Cociente de derivadas, usando $(\ln x^2)^2=4(\ln x)^2$:
$$\frac{2(\ln x)^2}{(\ln x^2)^2}\cdot\frac{1}{1+\frac1{\ln x^2}}=\frac{1}{2\left(1+\frac1{\ln x^2}\right)}\to\frac12 .$$
5. Por continuidad de $\exp$: límite $=e^{1/2}=\sqrt e$.

**Receta.** $1^\infty$: escribe la base como $1+\frac1{f}$ y fuerza el exponente a ser $f\cdot(\text{algo})$; entonces el límite es $e^{\lim(\text{algo})}$. Atajo equivalente (consecuencia del método del logaritmo): si $f\to1$ y $g\to\infty$, $\lim f^g=e^{\lim g\,(f-1)}$; aquí $g(f-1)=\ln x\cdot\frac{1}{2\ln x}=\frac12$.

**Error típico.** Decir «$1^\infty=1$». La base no es $1$, solo tiende a $1$, y el exponente amplifica la diferencia.

**Teoría:** U Prop. 2.2 y Ejemplo 2.13, p. 85; U p. 85 (el tipo $1^\infty$ con logaritmos lleva a $0\cdot\infty$).

---

## Ejercicio 2.32 (E p. 70; solución p. 71)

> **Calcula para $n\in\mathbb N$ y $a>1$ el límite** $\displaystyle\lim_{x\to+\infty}\frac{x^n}{a^x}$.

**Solución.**

1. **Qué es la variable.** $n$ está fijo; la variable es $x$.
2. **Tipo.** $a^x=e^{x\ln a}$ con $\ln a>0$ (porque $a>1$), luego $a^x\to+\infty$; y $x^n\to+\infty$: tipo $\frac{+\infty}{+\infty}$.
3. **Una aplicación de L'Hôpital.** $(x^n)'=nx^{n-1}$ y $(a^x)'=a^x\ln a\neq0$ (tabla U p. 79):
$$\lim_{x\to+\infty}\frac{x^n}{a^x}=\frac{n}{\ln a}\lim_{x\to+\infty}\frac{x^{n-1}}{a^x},$$
   siempre que el límite de la derecha exista.
4. **Razonamiento por inducción** (lo que E hace con «aplicamos L'Hôpital $n$ veces»). Llamemos $L_k=\lim_{x\to+\infty}\frac{x^k}{a^x}$.
   - $k=0$: $L_0=\lim\frac1{a^x}=0$ (inverso de algo que tiende a $+\infty$).
   - Si $L_{k-1}=0$ con $k\ge1$, entonces $\frac{x^k}{a^x}$ es $\frac\infty\infty$, se cumplen las hipótesis y, por el paso 3, $L_k=\frac{k}{\ln a}L_{k-1}=0$.

   Luego $L_n=0$ para todo $n\in\mathbb N$. Equivalentemente, tras $n$ derivaciones queda $\dfrac{n!}{a^x(\ln a)^n}\to0$ (constante entre algo que tiende a $+\infty$).
5. **La pregunta final de E ($0<a<1$).** Entonces $a^x\to0^+$ y ya **no hay indeterminación**: $\frac{x^n}{a^x}=x^n\left(\frac1a\right)^x$ es producto de dos funciones que tienden a $+\infty$, luego el límite es $+\infty$. (E deja la pregunta sin responder.)

**Receta.** Potencia frente a exponencial de base $>1$: deriva hasta que la potencia se convierta en constante (el grado baja en 1 cada vez; la exponencial se reproduce). Resultado: **la exponencial gana siempre**.

**Error típico.** Derivar respecto de $n$, o tratar $a^x$ como si fuese $x^a$ (su derivada es $a^x\ln a$, no $x\,a^{x-1}$).

**Teoría:** U §2.3.2 p. 82 y Ejemplo 2.9 p. 83 (aplicación reiterada); derivada de $a^x$ en la tabla de U p. 79. Caso $n=2$, $a=e$: L §8.7 Ej. 3, p. 560.

---

## Ejercicio 2.33 (E p. 71; solución p. 72)

> **Utilizando la Regla de l'Hôpital calcula el valor del límite de la sucesión** $\left\{\dfrac{\ln\frac{n+1}{n}}{\ln\frac{n+2}{n+1}}\right\}$ **cuando $n$ tiende a $+\infty$.**

**Solución.**

1. **Por qué no se deriva la sucesión.** Una sucesión solo está definida en $\mathbb N$; no tiene sentido derivar respecto de $n$. Pasamos a una función de variable real con **U Prop. 2.3 (p. 85)**: si $\lim_{x\to\infty}f(x)=l\in\overline{\mathbb R}$, entonces $\lim_{n\to\infty}f(n)=l$.
2. **Función asociada:** $f(x)=\dfrac{\ln\frac{x+1}{x}}{\ln\frac{x+2}{x+1}}$, $x>0$.
3. **Tipo.** $\frac{x+1}{x}\to1$ y $\frac{x+2}{x+1}\to1$; por continuidad del logaritmo, numerador y denominador tienden a $\ln1=0$: $\frac00$.
4. **Derivadas** (conviene escribir $\ln\frac{x+1}{x}=\ln(x+1)-\ln x$):
   - $\big(\ln(x+1)-\ln x\big)'=\dfrac1{x+1}-\dfrac1x=\dfrac{-1}{x(x+1)}$.
   - $\big(\ln(x+2)-\ln(x+1)\big)'=\dfrac1{x+2}-\dfrac1{x+1}=\dfrac{-1}{(x+1)(x+2)}$, que no se anula nunca.
5. **Cociente de derivadas:**
$$\frac{-1/(x(x+1))}{-1/((x+1)(x+2))}=\frac{(x+1)(x+2)}{x(x+1)}=\frac{x+2}{x}=1+\frac2x\to1 .$$
6. **Conclusión.** $\lim_{x\to\infty}f(x)=1$ y, por la Prop. 2.3, $\displaystyle\lim_{n\to\infty}\frac{\ln\frac{n+1}{n}}{\ln\frac{n+2}{n+1}}=1$. (Comprobación numérica: para $n=1000$ el término vale $1{,}0010$.)

**Receta.** Límite de sucesión con $0/0$ o $\infty/\infty$ «difícil»: cambia $n$ por $x\in\mathbb R$, aplica L'Hôpital a la función y vuelve a la sucesión con U Prop. 2.3.

**Error típico.** Usar la implicación al revés: que $f(n)\to l$ **no** implica que $f(x)\to l$ (por ejemplo, $\operatorname{sen}(\pi n)=0$ para todo $n$, pero $\operatorname{sen}(\pi x)$ no tiene límite en $+\infty$).

**Teoría:** U Prop. 2.3 y Ejemplo 2.14, p. 85; L Teorema 9.1 p. 585 y Ej. 6 p. 588.

---

## Ejemplos propios (dificultad creciente)

### Propio 1 (fácil, $0/0$ con dos derivaciones)
$\displaystyle\lim_{x\to0}\frac{e^x-1-x}{x^2}$.

1. En $0$: $\frac{1-1-0}{0}$, tipo $\frac00$. Funciones derivables, $(x^2)'=2x\neq0$ si $x\neq0$.
2. L'Hôpital: $\lim\frac{e^x-1}{2x}$, otra vez $\frac00$; $(2x)'=2\neq0$.
3. L'Hôpital: $\lim\frac{e^x}{2}=\frac12$. **Resultado: $\frac12$** (sympy: $1/2$).

### Propio 2 (medio, $\infty-\infty$)
$\displaystyle\lim_{x\to0}\left(\frac1x-\frac1{e^x-1}\right)$.

1. Por la derecha es $+\infty-(+\infty)$ (y por la izquierda $-\infty-(-\infty)$). Restamos (U p. 83: «pueden desaparecer o transformarse … si realizamos la resta»): $\dfrac{e^x-1-x}{x(e^x-1)}$, tipo $\frac00$.
2. Derivadas: numerador $e^x-1$; denominador $h(x)=e^x-1+xe^x$. Como $h'(x)=(2+x)e^x>0$ cerca de $0$, $h$ es estrictamente creciente allí y solo se anula en $0$: hipótesis OK.
3. $\lim\frac{e^x-1}{e^x-1+xe^x}$ sigue siendo $\frac00$; derivamos otra vez: $\lim\frac{e^x}{(2+x)e^x}=\lim\frac1{2+x}=\frac12$. **Resultado: $\frac12$** (sympy: $1/2$).

### Propio 3 (medio-alto, $1^\infty$)
$\displaystyle\lim_{x\to0}(\cos x)^{1/x^2}$.

1. Base $\to1$, exponente $\to+\infty$: $1^\infty$. Cerca de $0$, $\cos x>0$, luego $(\cos x)^{1/x^2}=e^{\ln(\cos x)/x^2}$.
2. Exponente: $\frac{\ln\cos x}{x^2}$ es $\frac00$. L'Hôpital: $\frac{-\operatorname{tg}x}{2x}=-\frac12\cdot\frac{\operatorname{sen}x}{x}\cdot\frac1{\cos x}\to-\frac12$ (usando $\frac{\operatorname{sen}x}{x}\to1$, U Ej. 2.8, pp. 82–83).
3. **Resultado: $e^{-1/2}=1/\sqrt e$** (sympy: $e^{-1/2}$).

### Propio 4 (difícil, sucesión)
Para $a>0$: $\displaystyle\lim_{n\to\infty}n\left(a^{1/n}-1\right)$.

1. Función: $f(x)=x(a^{1/x}-1)=\dfrac{a^{1/x}-1}{1/x}$; como $a^{1/x}=e^{(\ln a)/x}\to e^0=1$, es $\frac00$.
2. Derivadas: numerador $a^{1/x}\ln a\cdot\left(-\frac1{x^2}\right)$; denominador $-\frac1{x^2}\neq0$. Cociente: $a^{1/x}\ln a\to\ln a$.
3. Por U Prop. 2.3: **$\lim_n n(a^{1/n}-1)=\ln a$** (sympy: $\log a$; numéricamente, con $a=2$ y $n=1000$: $0{,}69339\approx\ln2=0{,}69315$).

---

## (a) Teoría necesaria (verificada sobre el PDF de U)

| Resultado | Enunciado | U, página impresa |
|---|---|---|
| Regla de L'Hôpital | $f,g$ con el mismo dominio, derivables, $g'(x)\neq0$ cerca de $a$ (puede ser $g'(a)=0$). Si $\lim f=\lim g=0$ o $\lim f=\pm\infty$ y $\lim g=\pm\infty$, entonces $\lim\frac fg=\lim\frac{f'}{g'}=\ell$, $\ell\in\overline{\mathbb R}$. Al margen: vale sustituyendo $a$ por $\infty$, $-\infty$, $a^+$ o $a^-$. | §2.3.2, **p. 82** |
| Uso básico | $\lim\frac{\operatorname{sen}x}{x}=1$ (Ej. 2.8) | pp. 82–83 |
| Aplicación reiterada | $\lim\frac{1+e^{x^2}}{x^3}=\infty$ (Ej. 2.9) | p. 83 |
| $\infty-\infty$ | «realizamos la resta» y queda $\frac00$ o $\frac\infty\infty$ (Ej. 2.10) | pp. 83–84 |
| $\pm\infty\cdot0$ | $\lim f\cdot g=\lim\frac{f}{1/g}$ (Ej. 2.11) | p. 84 |
| $\infty^0$ | «utilizar logaritmos primero» (Ej. 2.12: $\lim x^{1/x}=1$) | p. 84 |
| Error típico | olvidar deshacer el logaritmo y dar $0$ en vez de $1$ | p. 85 |
| $1^\infty$ | con logaritmos se llega a $0\cdot\infty$; Prop. 2.2: $f\to\pm\infty\Rightarrow\left(1+\frac1f\right)^f\to e$ (Ej. 2.13) | p. 85 |
| Sucesiones | Prop. 2.3: $\lim_{x\to\infty}f(x)=l\in\overline{\mathbb R}\Rightarrow\lim_n f(n)=l$ (Ej. 2.14) | p. 85 |
| Apoyos previos | Prop. 1.10 (cero por acotada) p. 45; Prop. 1.11 (álgebra de límites) p. 46; Prop. 1.13–1.14 (continuidad de suma, producto, cociente y composición) p. 51; Prop. 2.1, regla de la cadena y tabla de derivadas p. 79; derivada de $\operatorname{tg}$ p. 80; tabla de derivadas compuestas pp. 80–81 | |

**Aviso sobre el enunciado de U (p. 82).** Tal como está escrito («Si … Entonces $\lim\frac fg=\lim\frac{f'}{g'}=\ell$») parece afirmar que el límite de $f'/g'$ siempre existe. La hipótesis correcta es «**si existe** $\lim\frac{f'}{g'}=\ell$» (así en S p. 302 y en L Teorema 8.4, p. 558). Además, `pdftotext` pierde la barra de $\neq$ en «$g'(x)\neq0$» y la de $\overline{\mathbb R}$ en «$\ell\in\overline{\mathbb R}$» (p. 82) y en la Prop. 2.3 (p. 85): en `ingenieros.txt` aparecen como «$g'(x)=0$» y «$\ell\in\mathbb R$».

**Cómo transformar cada tipo (resumen):**
- $\frac00$, $\frac\infty\infty$: L'Hôpital directamente (comprobando hipótesis).
- $0\cdot\infty$: $fg=\frac{f}{1/g}$ o $\frac{g}{1/f}$ (poner abajo el factor cuya inversa se deriva fácil).
- $\infty-\infty$: denominador común, racionalizar o sacar factor común.
- $0^0$, $\infty^0$, $1^\infty$: $f^g=e^{g\ln f}$; calcular $L=\lim g\ln f$ ($0\cdot\infty$); resultado $e^L$. Para $1^\infty$, también U Prop. 2.2.
- Sucesión: pasar a $f(x)$ y usar U Prop. 2.3.
- **No** son indeterminaciones: $\frac{c}{0^+}=\pm\infty$ si $c\neq0$, $0^{+\infty}=0$, $\infty^{\infty}=\infty$, $\infty+\infty=\infty$, $\frac{c}{\infty}=0$ (L p. 563; S margen p. 306). Aplicar L'Hôpital en esos casos da resultados falsos.

## (b) Huecos de U y dónde suplirlos

| Hueco en U | Dónde está | Página impresa |
|---|---|---|
| Por qué funciona la regla (intuición: cociente de rectas tangentes) | S §4.4, figura 1 | S p. 302 |
| Hipótesis «si existe $\lim f'/g'$» bien escrita | S §4.4 (recuadro); L Teorema 8.4 | S p. 302; L p. 558 |
| Demostración (teorema del valor medio de Cauchy) | L Teorema 8.3 (demostración en el apéndice A); S Apéndice F | L p. 558; S p. A46 |
| No aplicar L'Hôpital si no hay indeterminación | S §4.4 Ej. 5 y comentario; L «uso incorrecto» | S pp. 304–305; L p. 563 |
| Tipo $0^0$ (U solo cita $\infty^0$ y $1^\infty$) y método $y=e^{\ln y}$ sin suponer que el límite existe | S «Potencias indeterminadas», Ej. 8–9 ($x^x$); L Ej. 5 ($1^\infty$) y Ej. 6 ($0^0$) | S pp. 306–307; L pp. 561–562 |
| $x\ln x$ con las dos elecciones de cociente (= E 2.30) | S §4.4 Ej. 6 y Nota | S p. 305 |
| $\infty-\infty$ con más ejemplos | S Ej. 7; L Ej. 7 | S p. 306; L p. 563 |
| Aplicación reiterada potencia/exponencial (= E 2.32 con $n=2$, $a=e$) | L §8.7 Ej. 3 | L p. 560 |
| Lista de formas **determinadas** | L §8.7; S margen | L p. 563; S p. 306 |
| L'Hôpital en sucesiones (más ejemplos) | L Teorema 9.1 y Ej. 6 | L pp. 585, 588 |
| Inicio de las secciones | S §4.4 empieza en p. 301; L §8.7 empieza en p. 557 | |

## (c) Erratas y omisiones de E

1. **Ej. 2.28 (p. 69): tipo de indeterminación mal escrito.** E dice «del tipo $\frac{-\infty}{+\infty}$». Como $\ln(\cos x)\to-\infty$, el numerador $2-\ln(\cos x)\to+\infty$: es $\frac{+\infty}{+\infty}$. El resultado $0$ es correcto.
2. **Ej. 2.24 (pp. 66–67): notación ambigua y cita.** $\ln x^2+1$ debe leerse $\ln(x^2)+1$ (la solución usa $\frac{\ln x^2+1}{\ln x^2}=1+\frac1{\ln x^2}$). Si se leyera $\ln(x^2+1)$, el límite sería $1$, no $\sqrt e$ (comprobado con sympy). En la «Nota», E remite al «ejemplo 2.12» de U para $1^{\pm\infty}$, pero el Ej. 2.12 (U p. 84) es de tipo $\infty^0$; el comentario sobre $1^\infty$ con logaritmos está en U p. 85. Los paréntesis dobles $\ln\big((1+\frac1{\ln x^2})\big)$ de p. 67 son solo tipográficos.
3. **Ej. 2.29 y 2.31 (pp. 69–70), igual que U Ej. 2.12: falta de rigor.** Escriben «$\lim=l$» con $l\in[0,+\infty]$ y toman $\ln l$. Eso supone que el límite existe y que $0<l<\infty$ (si $l=0$ o $l=+\infty$, $\ln l$ no es un número real). Lo correcto: $f^g=e^{g\ln f}$; si $g\ln f\to L$, por continuidad de $\exp$ el límite es $e^L$, sin suponer nada (S p. 307).
4. **Ej. 2.25 (p. 67): hipótesis mal dicha.** «La derivada del denominador cerca de cero no se anula»: $g'(x)=\frac{x}{\sqrt{1-x^2}}$ sí se anula en $x=0$. Lo que se cumple, y lo que exige U, es $g'(x)\neq0$ para $x\neq0$ cercano a $0$. El resultado $-1$ es correcto.
5. **Ej. 2.27 (p. 68): matiz.** «La Regla de l'Hôpital no es infalible»: en realidad las hipótesis se cumplen y $\lim\frac{f'}{g'}$ existe (vale $1$); lo que ocurre es que derivar no simplifica y el cálculo da vueltas. La regla no falla, pero aquí no sirve para calcular el límite.
6. **Ej. 2.32 (pp. 70–71): omisiones.** (i) «Aplicar l'Hôpital $n$ veces» se justifica mejor por inducción (cada paso intermedio es $\frac\infty\infty$ porque $x^{n-k}\to\infty$ para $k<n$). (ii) La pregunta final «¿qué ocurriría si $0<a<1$?» queda sin responder: el límite es $+\infty$ y no hay indeterminación.
7. Ejercicios **2.26, 2.30 y 2.33**: correctos. (En 2.33 las derivadas intermedias de p. 72 son correctas: el cociente se simplifica a $\frac{x+2}{x}$.)

*Verificación:* todos los límites de este documento (2.24–2.33, la lectura alternativa de 2.24, el caso $0<a<1$ de 2.32 y los propios 1–4) se han comprobado con `sympy.limit`.
