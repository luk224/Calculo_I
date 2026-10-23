# Soluciones Tema 6.5 — Integrales impropias

Resolución paso a paso de los ejemplos 6.36-6.45 de U (§6.5.2, pp. 272-278), de los ejercicios de **E** 6.42-6.48 (E pp. 246-252; 6.49-6.51 solo enunciado y resultado, fuera de examen), de las 8 preguntas de exámenes **X** sobre impropias, de 4 tipos de pregunta que no aparecen en X pero pueden caer, de los ítems 9-10 de la autoevaluación de U (p. 282) y de 4 ejemplos propios. Todo se ha comprobado con sympy y mpmath (script `v65.py`, carpeta `r65/` del scratchpad). Las definiciones 6.9 y 6.10, el criterio de comparación y el recuadro de comparación por límite se han leído **como imagen** (U PDF 270-276 = pp. impresas 272-278); los enunciados de E (pp. 246-254) y de X (pp. 25, 46-47, 73, 81, 93-94, 105, 115-116, 150) también.

Páginas: U impresa (= PDF + 2); E impresa = PDF; X = página del PDF de exámenes. Convocatorias de X tomadas de `indice_examenes_*.md` y de la cabecera de la página.

**Alcance:** de U §6.5 solo entra en examen §6.5.2 (integrales impropias, pp. 271-278). §6.5.3 (sucesiones funcionales e integración, pp. 279-280) y la integración término a término de series de potencias (pp. 280-281) van **fuera de examen** (bloque colapsado), igual que E 6.49-6.51.

## 0. Herramientas de teoría que se usan

| Clave | Enunciado (como en U) | Dónde |
|---|---|---|
| **Motivación** | «Al trabajar con integrales hemos considerado funciones acotadas sobre intervalos acotados. Pero a menudo se necesita integrar sobre intervalos no acotados o funciones no acotadas.» | U §6.5.1, p. 271 |
| **1ª especie** Def. 6.9 | Si $f:[a,\infty)\to\mathbb R$ es una función **continua y acotada**, la integral impropia de primera especie en $[a,\infty)$ es $$\int_a^\infty f(x)\,dx=\lim_{M\to\infty}\int_a^M f(x)\,dx.$$ Si el límite es un número real, se dice que es **convergente** y, en otro caso, **divergente**. | U p. 272 |
| **Extensiones** | En $(-\infty,b]$: $\int_{-\infty}^bf=\lim_{M\to-\infty}\int_M^bf$. En $\mathbb R$: $\int_{-\infty}^{\infty}f=\int_{-\infty}^cf+\int_c^{\infty}f$ para un número real $c$; «es convergente si ambas lo son y es divergente si alguna lo es». | U p. 274 |
| **Condición necesaria** | Una condición necesaria para la convergencia de $\int_a^{+\infty}f$ es que $\lim_{x\to\infty}f(x)=0$, **siempre que el límite exista**. | U recuadro p. 274 |
| **2ª especie** Def. 6.10 | Si $f:(a,b]\to\mathbb R$ es una función **continua y no acotada**, la integral impropia de segunda especie es $$\int_a^bf(x)\,dx=\lim_{c\to a^+}\int_c^bf(x)\,dx.$$ Convergente si el límite es un número real; divergente en otro caso. Análogo en $[a,b)$: $\int_a^bf=\lim_{c\to b^-}\int_a^cf$. | U pp. 275-276 |
| **Asíntota interior** | Si $f$ tiene una asíntota vertical $x=c$ con $c\in[a,b]$, «la integral se divide en dos integrales de segunda especie» (y, como en $\mathbb R$, converge solo si convergen las dos). | U p. 276 (Ej. 6.42) |
| **Precaución** | «Antes de resolver una integral definida hay que comprobar la continuidad del integrando. Si no lo hacemos así, podemos llegar a resultados falsos al haber aplicado el teorema fundamental sin cumplirse alguna hipótesis.» | U recuadro p. 276 |
| **3ª especie** | «Aquellas donde uno de los extremos del intervalo de integración es $\infty$ o $-\infty$ y la función a integrar no está acotada. […] para resolverla la dividimos en la suma de una integral de cada especie.» | U margen p. 275 |
| **Comparación** (1ª especie) | Sean $0\le f(x)\le g(x)$ continuas para $x\in[a,\infty)$. Si $\int_a^\infty g$ converge, entonces también converge $\int_a^\infty f$. Si $\int_a^\infty f$ diverge, entonces también diverge $\int_a^\infty g$. (Nota al pie: es necesario que $f$ y $g$ tengan valores mayores que 0; en otro caso hay que tomar valor absoluto y otras definiciones.) | U p. 277 (Ej. 6.43) |
| **Comparación** (2ª especie) | «El criterio de comparación estudiado tiene un equivalente obvio para integrales de segunda especie»: con $0\le f\le g$ en $(a,b]$, si $\int_a^bg$ converge, converge $\int_a^bf$; si $\int_a^bf$ diverge, diverge $\int_a^bg$. | U p. 278 (Ej. 6.44) |
| **Comparación mediante límite** | Sean $f(x)\ge0$ y $g(x)>0$ continuas para $x\in[a,\infty)$, y $\lim_{x\to\infty}\frac{f(x)}{g(x)}=l$. **(i)** Si $l\in(0,\infty)$, $\int_a^\infty f$ y $\int_a^\infty g$ son ambas convergentes o ambas divergentes. **(ii)** Si $l=0$ y $\int_a^\infty g$ converge, también converge $\int_a^\infty f$. **(iii)** Si $l=\infty$ y $\int_a^\infty g$ diverge, también diverge $\int_a^\infty f$. Margen: se extiende a 2ª especie con la impropiedad en $a$ cambiando $\lim_{x\to\infty}$ por $\lim_{x\to a^+}$. | U recuadro p. 278 (Ej. 6.45) |

**Herramientas de temas anteriores:** Regla de Barrow (U Teor. 6.2, p. 244); técnicas de primitivas (U §6.3: tabla p. 248, cambio de variable pp. 249-251, partes pp. 251-254, racionales pp. 255-258); límite en el infinito (U p. 47); L'Hôpital, también para $\frac\infty\infty$ (U §2.3.2, p. 82) y para $0\cdot\infty$ (U p. 84); Prop. 2.3: si $\lim_{x\to\infty}f(x)=l$, entonces $\lim_{n\to\infty}f(n)=l$ (U p. 85).

**Qué hace «impropia» una integral $\int_a^bf$** (las dos causas de U):
1. Un **límite de integración infinito** ($a=-\infty$ o $b=\infty$) → **1ª especie** (Def. 6.9).
2. La **función no acotada** en algún punto del intervalo de integración (asíntota vertical en un extremo o en un punto interior) → **2ª especie** (Def. 6.10).
3. Las dos a la vez → **3ª especie** (margen p. 275): se parte en una de cada.

Un punto donde $f$ **no está definida pero tiene límite finito** (p. ej. $\frac{\mathrm{sen}\,x}{x}$ en $0$) **no** es causa de impropiedad: $f$ sigue acotada cerca de él.

---

### Receta general del tema

> **Paso 1. Clasificar la especie.** Mira (a) los límites de integración: ¿alguno es $\pm\infty$? → 1ª especie; (b) el integrando en $[a,b]$: ¿se anula algún denominador, hay $\ln$ en $0$, una raíz par de algo que se anula en el denominador…? Calcula el límite de $f$ en ese punto: si es $\pm\infty$, $f$ **no está acotada** → 2ª especie. Si pasan las dos cosas → 3ª especie. Si no pasa ninguna, es una integral ordinaria: Barrow directamente.
>
> **Paso 2. Partir en los puntos problemáticos.** Cada trozo debe tener **un solo problema y en un extremo**: $\int_{-\infty}^{\infty}=\int_{-\infty}^{c}+\int_c^{\infty}$; asíntota interior en $c$: $\int_a^b=\int_a^c+\int_c^b$; 3ª especie en $(0,\infty)$: $\int_0^1+\int_1^\infty$. La integral total converge **solo si convergen todos los trozos**; basta que uno diverja para que diverja.
>
> **Paso 3a. Si se pide el valor: límite de la primitiva.** Calcula una primitiva $F$, aplica Barrow en el intervalo «recortado» ($[a,M]$, $[c,b]$…) y toma el límite: $\int_a^\infty f=\lim_{M\to\infty}\big(F(M)-F(a)\big)$, $\int_a^bf=\lim_{c\to a^+}\big(F(b)-F(c)\big)$. Si el límite es un número real: converge y ese es su valor; si es $\pm\infty$ o no existe: diverge.
>
> **Paso 3b. Si solo se pide el carácter (o no hay primitiva): comparar.** Comprueba que el integrando tiene **signo constante** (si es $\le0$, trabaja con $-f$). Busca su comportamiento dominante en el punto problemático y compáralo con una integral de referencia ($\frac1{x^p}$, $e^{-kx}$; tabla de abajo): con desigualdad (U p. 277) o con el límite del cociente (U p. 278).

### Integrales de referencia (para comparar)

| Integral | Converge si… (valor) | Diverge si… | Fuente |
|---|---|---|---|
| $\displaystyle\int_1^\infty\frac{dx}{x^p}$ | $p>1$ (vale $\frac1{p-1}$) | $p\le1$ | U Ej. 6.38, p. 273 (y 6.36-6.37) |
| $\displaystyle\int_0^1\frac{dx}{x^p}$ | $p<1$ (vale $\frac1{1-p}$) | $p\ge1$ | U Ej. 6.41, p. 275 |
| $\displaystyle\int_0^\infty\frac{dx}{x^p}$ | nunca (siempre falla uno de los dos trozos) | todo $p$ | propio (Propio 4) |
| $\displaystyle\int_0^\infty e^{-kx}\,dx$ | $k>0$ (vale $\frac1k$) | $k\le0$ | U Ej. 6.39, pp. 273-274 |
| $\displaystyle\int_{-\infty}^{\infty}\frac{dx}{1+x^2}$ | converge, vale $\pi$ | — | U Ej. 6.40, p. 274 |
| $\displaystyle\int_0^1\ln x\,dx$ | converge, vale $-1$ | — | E 6.46, p. 248 |

Regla mnemotécnica: **en el infinito hace falta que $f$ baje deprisa ($p>1$); cerca de $0$ basta que suba despacio ($p<1$); $p=1$ ($\frac1x$) diverge en los dos sitios.**

Dos consecuencias sencillas que se usan siempre:
- **Desplazar el punto problemático.** Con el cambio $t=x-a$ (U p. 251), $\int_a^{b}\frac{dx}{(x-a)^p}$ ($b>a$) se comporta como $\int_0^{b-a}\frac{dt}{t^p}$: converge si y solo si $p<1$. Igual si la asíntota está en el extremo derecho: $\int_a^b\frac{dx}{(b-x)^p}$.
- **Cambiar el extremo «bueno» no cambia el carácter.** $\int_a^\infty f$ y $\int_{a'}^\infty f$ difieren en $\int_a^{a'}f$, que es una integral ordinaria (un número): o convergen las dos o divergen las dos. Por eso $\int_2^\infty\frac{dx}{x^2}$ converge igual que $\int_1^\infty\frac{dx}{x^2}$.

### Cómo elegir $g$ al comparar

- **En $\pm\infty$: quedarse con lo que crece más deprisa.** En polinomios y raíces, la mayor potencia: $\sqrt{x^4+x^2+1}\approx x^2$, $\sqrt{x^3+1}\approx x^{3/2}$, $\frac{2x+1}{x^3-5}\approx\frac2{x^2}$. Se toma $g=\frac1{x^q}$ con esa potencia $q$; el cociente $f/g$ tiende a un número $l\in(0,\infty)$ y se aplica el caso (i).
- **Exponenciales.** $e^{-x}$ baja más deprisa que cualquier potencia: $\lim_{x\to\infty}x^ne^{-x}=0$ (L'Hôpital $n$ veces, U p. 82). Para $f=x^ne^{-x}$ (o $e^{-x^2}$) se compara con $g=\frac1{x^2}$: el límite es $0$ y $\int_1^\infty\frac{dx}{x^2}$ converge → caso (ii).
- **Logaritmos.** $\ln x$ crece más despacio que cualquier potencia: $\frac1{\ln x}$ es «más grande» que $\frac1x$ en el infinito (límite $\infty$ con $g=\frac1x$ → caso (iii), diverge); $\frac{\ln x}{x^2}$ es «más pequeña» que $\frac1{x^{3/2}}$ (límite $0$ → caso (ii), converge).
- **Cerca de $0^+$: quedarse con la menor potencia** (es la que manda cuando $x$ es pequeño): $x^3+x^2+x\approx x$, $x(1+x)\approx x$. Y las equivalencias que se obtienen con L'Hôpital: $\mathrm{sen}\,x\approx x$, $e^x-1\approx x$, $\ln(1+x)\approx x$, $1-\cos x\approx\frac{x^2}2$ (cada cociente tiende a $1$).
- **Si el criterio «no decide»** (caso $l=0$ con $\int g$ divergente, o $l=\infty$ con $\int g$ convergente), se prueba con otra $g$ (E 6.47).
- **Signo:** los dos criterios de U piden $f\ge0$ (y $g>0$). Si $f\le0$ en todo el intervalo, se estudia $-f$. Si $f$ cambia de signo infinitas veces ($\mathrm{sen}\,x$, $\cos x$), estos criterios no se pueden aplicar tal cual.

---

## 1. Ejemplos de U (§6.5.2, pp. 272-278)

### Ejemplos 6.36-6.38 (U pp. 272-273): $\int_1^\infty\frac{dx}{x^p}$

> 6.36: ¿Es finita el área bajo la gráfica de $\frac1{x^2}$ entre $x=1$ y $x=\infty$? 6.37: Estudie si la integral impropia $\int_1^\infty\frac1x\,dx$ es convergente. 6.38: Para un número real $p$, estudie si $\int_1^\infty\frac1{x^p}\,dx$ es convergente.

**Antes de calcular**
- **Qué me piden:** decidir si $\lim_{M\to\infty}\int_1^M\frac{dx}{x^p}$ es un número real, según $p$.
- **Cómo lo pienso:** el área hasta $M$ siempre es finita; la pregunta es si se «estabiliza» al crecer $M$. Depende de lo deprisa que baje $\frac1{x^p}$.
- **Qué uso:** Def. 6.9 (U p. 272): $\frac1{x^p}$ es continua y acotada en $[1,\infty)$ si $p\ge0$ (vale como mucho $1$); Barrow (U p. 244).
- **Por dónde empiezo:** separar $p=1$ (la primitiva es un logaritmo) de $p\ne1$ (es una potencia).

1. **$p=2$ (Ej. 6.36):** $\int_1^M\frac{dx}{x^2}=\big[-\frac1x\big]_1^M=1-\frac1M$. Para $M=10,100,1000$ da $0{,}9;\ 0{,}99;\ 0{,}999$. Límite: $\lim_{M\to\infty}\big(1-\frac1M\big)=1$. **Converge y vale 1.**
2. **$p=1$ (Ej. 6.37):** $\int_1^M\frac{dx}{x}=\ln M-\ln1=\ln M\to\infty$. **Diverge.** (Aunque $\frac1x\to0$, no baja lo bastante deprisa.)
3. **$p\ne1$:** $\int_1^M x^{-p}dx=\Big[\frac{x^{1-p}}{1-p}\Big]_1^M=\frac1{1-p}\big(M^{1-p}-1\big)$.
4. **Signo del exponente $1-p$:** si $p<1$, $1-p>0$ y $M^{1-p}\to\infty$: **diverge**. Si $p>1$, $1-p<0$, $M^{1-p}=\frac1{M^{p-1}}\to0$ y el límite es $\frac{-1}{1-p}=\frac1{p-1}$: **converge**.
5. **Conclusión:** $\int_1^\infty\frac{dx}{x^p}$ converge $\iff p>1$, con valor $\frac1{p-1}$.

**Receta.** Integral «modelo» con parámetro: primitiva con el parámetro, separar el caso en que la primitiva cambia de forma ($p=1$), y estudiar el límite según el signo del exponente.

**Error típico.** Pensar que basta $\lim_{x\to\infty}f(x)=0$ para que converja: $\frac1x\to0$ y diverge.

sympy: $\int_1^\infty x^{-2}=1$, $\int_1^\infty x^{-1}=\infty$, $\int_1^\infty x^{-5/2}=\frac23=\frac1{3/2}$.

---

### Ejemplo 6.39 (U pp. 273-274): $\int_0^\infty e^{-kx}dx$

> Estudie si la integral $\int_0^\infty e^{-kx}dx$ es convergente.

**Antes de calcular**
- **Qué me piden:** el carácter según $k$.
- **Cómo lo pienso:** $e^{-kx}$ baja a $0$ si $k>0$ (muy deprisa), es constante si $k=0$ y crece si $k<0$.
- **Qué uso:** Def. 6.9 (U p. 272).
- **Por dónde empiezo:** el caso $k=0$ aparte (el integrando es $1$).

1. **$k=0$:** $\int_0^M1\,dx=M\to\infty$: diverge.
2. **$k\ne0$:** $\int_0^Me^{-kx}dx=\Big[-\frac1ke^{-kx}\Big]_0^M=\frac1k\big(1-e^{-kM}\big)$.
3. **$k>0$:** $e^{-kM}\to0$, el límite es $\frac1k$: **converge y vale $\frac1k$**.
4. **$k<0$:** $-kM\to+\infty$, $e^{-kM}\to\infty$: **diverge**. (Aquí, además, $e^{-kx}$ no está acotada en $[0,\infty)$.)

**Receta.** $\int_0^\infty e^{-kx}dx=\frac1k$ si $k>0$. Es la otra integral de referencia para comparar.

**Error típico.** Olvidar el signo: con $k>0$ la primitiva es $-\frac1ke^{-kx}$, y $F(\infty)-F(0)=0-(-\frac1k)=\frac1k>0$ (un área de algo positivo no puede salir negativa).

sympy: $\int_0^\infty e^{-kx}dx=\frac1k$ ($k>0$).

---

### Ejemplo 6.40 (U p. 274): $\int_{-\infty}^{\infty}\frac{dx}{1+x^2}$

> ¿Es convergente $\int_{-\infty}^{\infty}\frac1{1+x^2}dx$?

**Antes de calcular**
- **Qué me piden:** carácter y valor de una impropia con los dos extremos infinitos.
- **Cómo lo pienso:** son **dos** problemas ($-\infty$ y $+\infty$): se parte en un punto $c$ y se estudia cada trozo por separado.
- **Qué uso:** extensión a $\mathbb R$ (U p. 274); $\int\frac{dx}{1+x^2}=\mathrm{arctg}\,x$ (tabla U p. 248).
- **Por dónde empiezo:** $c=0$; el integrando es continuo en $\mathbb R$ y $0<\frac1{1+x^2}\le1$ (acotado).

1. **Partir:** $I=\int_{-\infty}^0\frac{dx}{1+x^2}+\int_0^{\infty}\frac{dx}{1+x^2}$.
2. **Trozo derecho:** $\lim_{N\to\infty}\big(\mathrm{arctg}\,N-\mathrm{arctg}\,0\big)=\frac\pi2$.
3. **Trozo izquierdo:** $\lim_{M\to-\infty}\big(\mathrm{arctg}\,0-\mathrm{arctg}\,M\big)=0-\big(-\frac\pi2\big)=\frac\pi2$.
4. **Ambos convergen**, luego $I$ converge y $I=\frac\pi2+\frac\pi2=\pi$.

**Receta.** Dos extremos infinitos = dos límites **independientes** ($M$ y $N$ con letras distintas).

**Error típico.** Calcular $\lim_{M\to\infty}\int_{-M}^Mf$ (un solo límite simétrico). Para $f(x)=x$ eso da $0$, pero $\int_0^\infty x\,dx$ diverge, así que $\int_{-\infty}^{\infty}x\,dx$ **diverge** según la definición de U.

sympy: $\pi$.

---

### Ejemplos 6.41-6.42 (U pp. 275-276): segunda especie

> 6.41: Estudie la convergencia de $\int_0^1\frac1{x^p}dx$ para $p\in\mathbb R$. 6.42: Calcule la integral $\int_{-1}^1\frac1{x^2}dx$.

**Antes de calcular**
- **Qué me piden:** el carácter de $\int_0^1\frac{dx}{x^p}$ según $p$, y una integral con el problema en el **interior** del intervalo.
- **Cómo lo pienso:** si $p>0$, $\frac1{x^p}\to\infty$ cuando $x\to0^+$: el área es la de una «pared» infinitamente alta pero cada vez más estrecha; converge si sube despacio.
- **Qué uso:** Def. 6.10 (U p. 275); asíntota interior (U p. 276).
- **Por dónde empiezo:** si $p\le0$, $\frac1{x^p}=x^{-p}$ es continua en $[0,1]$: no es impropia.

1. **$p\le0$:** $\int_0^1x^kdx$ con $k=-p\ge0$, integral ordinaria.
2. **$p=1$:** $\int_c^1\frac{dx}x=-\ln c\to+\infty$ cuando $c\to0^+$: **diverge**.
3. **$p>0$, $p\ne1$:** $\int_c^1x^{-p}dx=\frac1{1-p}\big(1-c^{1-p}\big)$. Si $p<1$: $c^{1-p}\to0$ y el límite es $\frac1{1-p}$: **converge**. Si $p>1$: $c^{1-p}=\frac1{c^{p-1}}\to\infty$: **diverge**.
4. **Otra vía (U p. 275):** con $t=\frac1x$, $\int_0^1\frac{dx}{x^p}=\int_1^\infty\frac{dt}{t^{2-p}}$, que converge $\iff2-p>1\iff p<1$ (Ej. 6.38). Así una de 2ª especie se convierte en una de 1ª.
5. **Ej. 6.42.** $\frac1{x^2}$ no está definida en $x=0\in[-1,1]$ y $\lim_{x\to0}\frac1{x^2}=\infty$: asíntota interior. Se parte: $\int_{-1}^1=\int_{-1}^0+\int_0^1$.
6. **Trozo derecho:** $\lim_{c\to0^+}\big[-\frac1x\big]_c^1=\lim_{c\to0^+}\big(-1+\frac1c\big)=\infty$: diverge. (Ya bastaría: si un trozo diverge, la integral diverge.) El izquierdo también: $\lim_{c\to0^-}\big(-\frac1c-1\big)=\infty$.
7. **Conclusión: diverge.** Aplicar Barrow «a ciegas» daría $\big[-\frac1x\big]_{-1}^1=-1-1=-2$, un número **negativo** para el área de una función positiva: es falso porque $\frac1{x^2}$ no es continua en $[-1,1]$ y Barrow no se puede usar (recuadro U p. 276).

**Receta.** Antes de Barrow, buscar ceros del denominador **dentro** de $[a,b]$; si los hay, partir allí y hacer un límite lateral en cada trozo.

**Error típico.** El $-2$ del paso 7.

sympy: $\int_0^1x^{-1/2}=2$, $\int_0^1x^{-3/4}=4$; $\lim_{c\to0^+}\int_c^1x^{-2}=\infty$.

---

### Ejemplos 6.43-6.44 (U pp. 277-278): comparación

> 6.43: Estudie si la integral $\int_1^\infty\frac1{\sqrt{x^4+x^2+1}}dx$ es convergente. 6.44: Estudie si la integral $\int_0^1\frac1{\sqrt[4]{x^3+x^2+x}}dx$ es convergente.

**Antes de calcular**
- **Qué me piden:** solo el carácter (no hay primitiva sencilla).
- **Cómo lo pienso:** en el infinito $\sqrt{x^4+x^2+1}\approx x^2$, así que $f\approx\frac1{x^2}$; cerca de $0$, $x^3+x^2+x\approx x$ y $f\approx\frac1{x^{1/4}}$. Pero para una **desigualdad** sirve cualquier sumando positivo del radicando.
- **Qué uso:** comparación (U p. 277) y su versión de 2ª especie (U p. 278); Ej. 6.38 y 6.41.
- **Por dónde empiezo:** quitar sumandos positivos del denominador hace la fracción **más grande**.

1. **6.43, signo y continuidad:** $f(x)=\frac1{\sqrt{x^4+x^2+1}}>0$ y continua en $[1,\infty)$.
2. **Desigualdad:** $x^4+x^2+1\ge x^4\Rightarrow\sqrt{x^4+x^2+1}\ge x^2\Rightarrow f(x)\le\frac1{x^2}$.
3. **Referencia:** $\int_1^\infty\frac{dx}{x^2}$ converge ($p=2>1$). Por comparación, **converge** (su valor, $\approx0{,}8429$, es menor que $1$).
4. **6.44, por qué es impropia:** el denominador se anula en $x=0$ y $f\to\infty$ cuando $x\to0^+$: 2ª especie.
5. **Desigualdad en $(0,1)$:** $x^3+x^2+x\ge x^3\Rightarrow f(x)\le\frac1{\sqrt[4]{x^3}}=\frac1{x^{3/4}}$.
6. **Referencia:** $\int_0^1\frac{dx}{x^{3/4}}$ converge ($p=\frac34<1$). Por comparación, **converge** ($\approx1{,}1882\le4$).
7. **Comentario:** en 6.44 la mejor comparación sería con $\frac1{x^{1/4}}$ (el término que domina cerca de $0$ es $x$, no $x^3$); pero a U le basta una $g$ **mayor** cuya integral converja, aunque sea una cota «floja».

**Receta.** Para probar convergencia: acotar $f$ **por encima** por una referencia convergente (quitando sumandos positivos del denominador). Para probar divergencia: acotar **por debajo** por una referencia divergente.

**Error típico.** Usar la desigualdad al revés: $f\ge g$ con $\int g$ convergente **no dice nada**.

mpmath: $0{,}842875$ y $1{,}188159$.

---

### Ejemplo 6.45 (U p. 278): comparación mediante límite

> Estudie si la integral $\int_0^\infty\frac1{e^x+1}dx$ es convergente.

**Antes de calcular**
- **Qué me piden:** el carácter.
- **Cómo lo pienso:** para $x$ grande, $e^x+1\approx e^x$, luego $f\approx e^{-x}$.
- **Qué uso:** comparación mediante límite (U p. 278), Ej. 6.39 con $k=1$.
- **Por dónde empiezo:** $f=\frac1{e^x+1}\ge0$, $g=e^{-x}>0$, continuas en $[0,\infty)$.

1. **Límite:** $\lim_{x\to\infty}\frac{f}{g}=\lim_{x\to\infty}\frac{e^x}{e^x+1}=\lim_{x\to\infty}\frac1{1+e^{-x}}=1$.
2. **$l=1\in(0,\infty)$:** las dos tienen el mismo carácter; $\int_0^\infty e^{-x}dx=1$ converge, luego **converge**.
3. **(Extra: valor.)** Multiplicando por $e^{-x}$: $\frac{e^{-x}}{1+e^{-x}}=-\frac{(1+e^{-x})'}{1+e^{-x}}$, primitiva $-\ln(1+e^{-x})$; valor $0-(-\ln2)=\ln2\approx0{,}693$.

**Receta.** Si $\frac fg\to l\in(0,\infty)$, $f$ y $g$ «se parecen» en el infinito y sus integrales tienen el mismo carácter.

**Error típico.** Calcular $\lim_{x\to0}\frac fg$ (en el punto que no es el problemático) en lugar de $\lim_{x\to\infty}\frac fg$.

sympy: $\int_0^\infty\frac{dx}{e^x+1}=\ln2$.

---

## 2. Ejercicios de E (de fácil a difícil; numeración conservada)

Orden propuesto: 6.42 y 6.45 (clasificar) → 6.43 (1ª especie por definición) → 6.46 (2ª especie por definición) → 6.44 (por qué hay que mirar todos los $M$) → 6.47 (comparación por límite) → 6.48 (función Gamma: 3ª especie, comparación y partes).

---

### Ejercicio 6.42 (E p. 246)

> Si la función $f$ es una función continua y acotada en todo $\mathbb R$, ¿es posible hablar de integrales impropias de primera y segunda especie para ella?

**Antes de calcular**
- **Qué me piden:** decidir qué especies pueden aparecer con una $f$ continua y acotada en todo $\mathbb R$.
- **Cómo lo pienso:** cada especie tiene su «causa»: 1ª = intervalo no acotado; 2ª = función no acotada.
- **Qué uso:** Def. 6.9 (U p. 272), extensiones (U p. 274) y Def. 6.10 (U p. 275).

1. **1ª especie: sí.** El dominio es todo $\mathbb R$, así que tiene sentido $\int_a^\infty f$, $\int_{-\infty}^bf$ o $\int_{-\infty}^\infty f$, por ejemplo $\int_{-\infty}^{-3}f(x)\,dx$. (Que converjan o no depende de $f$: $\int_0^\infty\cos x\,dx$ diverge; $\int_0^\infty\frac{dx}{1+x^2}$ converge.)
2. **2ª especie: no.** La Def. 6.10 exige que $f$ **no esté acotada** en el intervalo. Como $f$ es acotada en todo $\mathbb R$, en cualquier $[a,b]$ es continua y acotada: $\int_a^bf$ es una integral ordinaria.
3. **3ª especie: tampoco** (necesitaría también $f$ no acotada).

**Receta.** 1ª especie ⇔ algún límite infinito; 2ª especie ⇔ $f$ no acotada en el intervalo. Se comprueban por separado.

**Error típico.** Creer que «impropia» significa «divergente»: es una forma de definir la integral; luego puede converger o no.

---

### Ejercicio 6.45 (E p. 248)

> ¿En una integral impropia de segunda especie el intervalo de integración está acotado?

**Antes de calcular**
- **Qué me piden:** sí o no, razonado con la definición.
- **Qué uso:** Def. 6.10 (U p. 275) y margen sobre la 3ª especie (U p. 275).

1. **Sí.** La Def. 6.10 se plantea para $f:(a,b]\to\mathbb R$ (o $[a,b)$) con $a,b$ números reales: el intervalo es **acotado** y lo que falla es que $f$ no está acotada.
2. Si además un extremo fuese $\pm\infty$, sería de **3ª especie** (U margen p. 275), y se parte en una de 1ª y otra de 2ª.

**Receta.** 2ª especie pura = intervalo acotado + función no acotada.

**Error típico.** Llamar «de 2ª especie» a $\int_0^\infty\ln x\,dx$: tiene las dos causas, es de 3ª especie (autoevaluación U p. 282, ítem 9; ver §3c).

---

### Ejercicio 6.43 (E p. 247)

> Utilizando la definición, calcula la integral impropia $\int_0^{+\infty}xe^{-x^2}dx$.

**Antes de calcular**
- **Qué me piden:** el valor (o la divergencia) usando el límite de la Def. 6.9.
- **Cómo lo pienso:** $x$ es (salvo el factor $-2$) la derivada de $-x^2$: la primitiva es inmediata. La exponencial baja tan deprisa que el área total será finita.
- **Qué uso:** Def. 6.9 (U p. 272); tabla de inmediatas, fila $\int e^ff'=e^f$ (U p. 248).
- **Por dónde empiezo:** comprobar que es de 1ª especie: $xe^{-x^2}$ es continua en $[0,\infty)$ y acotada (es $\ge0$, vale $0$ en $0$ y tiende a $0$ en el infinito; su máximo es $\frac1{\sqrt{2e}}\approx0{,}43$ en $x=\frac1{\sqrt2}$).

1. **Definición:** $\int_0^{+\infty}xe^{-x^2}dx=\lim_{M\to+\infty}\int_0^Mxe^{-x^2}dx$.
2. **Primitiva:** $\int xe^{-x^2}dx=-\frac12\int(-2x)e^{-x^2}dx=-\frac12e^{-x^2}$.
3. **Barrow en $[0,M]$** (ahí $f$ es continua): $\Big[-\frac12e^{-x^2}\Big]_0^M=-\frac12e^{-M^2}+\frac12$.
4. **Límite:** $e^{-M^2}\to0$, luego el límite es $\frac12$.
5. **Conclusión:** converge y vale $\frac12$.

**Receta.** 1ª especie con primitiva conocida: Barrow en $[a,M]$ y límite $M\to\infty$.

**Error típico.** Escribir directamente «$F(\infty)$» sin el límite, o poner la primitiva $-2e^{-x^2}$ (multiplicar en lugar de dividir por $-2$).

sympy: $\frac12$.

---

### Ejercicio 6.46 (E pp. 248-249)

> Utilizando la definición calcula la integral impropia $\int_0^1\ln x\,dx$.

**Antes de calcular**
- **Qué me piden:** el valor por la definición de 2ª especie.
- **Cómo lo pienso:** $\ln x\to-\infty$ cuando $x\to0^+$ (asíntota vertical en $0$): el «área» está por debajo del eje y es una pared infinitamente profunda pero estrecha.
- **Qué uso:** Def. 6.10 (U p. 275); primitiva de $\ln x$ por partes (U p. 252); L'Hôpital para $0\cdot\infty$ (U pp. 82-84).
- **Por dónde empiezo:** $\ln x$ es continua en $(0,1]$ y $\lim_{x\to0^+}\ln x=-\infty$: no acotada → 2ª especie con el problema en $a=0$.

1. **Definición:** $\int_0^1\ln x\,dx=\lim_{c\to0^+}\int_c^1\ln x\,dx$.
2. **Primitiva (partes, $u=\ln x$, $v'=1$):** $\int\ln x\,dx=x\ln x-\int x\cdot\frac1x\,dx=x\ln x-x$.
3. **Barrow en $[c,1]$:** $(1\cdot\ln1-1)-(c\ln c-c)=-1-c\ln c+c$.
4. **Límite delicado:** $c\ln c$ es $0\cdot(-\infty)$. Se escribe como cociente: $c\ln c=\frac{\ln c}{1/c}$ (tipo $\frac{-\infty}{\infty}$) y L'Hôpital: $\lim_{c\to0^+}\frac{1/c}{-1/c^2}=\lim_{c\to0^+}(-c)=0$.
5. **Resultado:** $\lim_{c\to0^+}(-1-c\ln c+c)=-1-0+0=-1$. **Converge y vale $-1$.**
6. **Comprobación de sentido:** $\ln x<0$ en $(0,1)$, así que el resultado debe ser negativo ✓.

**Receta.** 2ª especie: Barrow en $[c,b]$ y $c\to a^+$; los límites $0\cdot\infty$ se pasan a cociente para L'Hôpital.

**Error típico.** Decir que $c\ln c\to0\cdot(-\infty)=-\infty$ o $=0$ «porque sí»: es una indeterminación y hay que resolverla.

sympy: $-1$; $\lim_{c\to0^+}c\ln c=0$.

---

### Ejercicio 6.44 (E pp. 247-248)

> Para la sucesión de término general $a_n=\int_0^n\cos(2\pi x)\,dx$: 1. Comprueba que la sucesión converge a cero, es decir, se verifica $\lim_{n\to+\infty}\int_0^n\cos(2\pi x)\,dx=0$. 2. ¿Garantiza el apartado anterior que $\int_0^{+\infty}\cos(2\pi x)\,dx$ converge?

**Antes de calcular**
- **Qué me piden:** un límite de una **sucesión** y decidir si de él se deduce la convergencia de la impropia.
- **Cómo lo pienso:** la Def. 6.9 pide el límite de la **función** $F(M)=\int_0^M\cos(2\pi x)dx$ cuando $M$ recorre **todos** los reales grandes, no solo los enteros. $\cos(2\pi x)$ tiene periodo $1$: en cada periodo el área positiva y la negativa se compensan, pero entre dos enteros el área acumulada sube y baja.
- **Qué uso:** Def. 6.9 (U p. 272); límite en el infinito (U p. 47); Prop. 2.3 (U p. 85: si $\lim_{x\to\infty}F(x)=l$, entonces $\lim_{n\to\infty}F(n)=l$; **el recíproco no es cierto**).
- **Por dónde empiezo:** la primitiva $\frac{\mathrm{sen}(2\pi x)}{2\pi}$.

1. **Apartado 1:** $a_n=\Big[\frac{\mathrm{sen}(2\pi x)}{2\pi}\Big]_0^n=\frac{\mathrm{sen}(2\pi n)-\mathrm{sen}\,0}{2\pi}=0$ para todo $n$, porque $2\pi n$ es un múltiplo de $2\pi$. Una sucesión constante $0$ tiene límite $0$.
2. **Apartado 2, la función que importa:** $F(M)=\int_0^M\cos(2\pi x)dx=\frac{\mathrm{sen}(2\pi M)}{2\pi}$.
3. **Probar con valores no enteros:** $M=k+\frac14$ ($k$ entero): $F=\frac{\mathrm{sen}(2\pi k+\frac\pi2)}{2\pi}=\frac1{2\pi}\approx0{,}159$. Con $M=k+\frac34$: $F=-\frac1{2\pi}$. Con $M=k$: $F=0$.
4. **No hay límite:** si $F(M)$ tendiera a un número $L$, para $M$ suficientemente grande (sea entero o no) $F(M)$ estaría tan cerca de $L$ como se quiera (definición de límite en el infinito, U p. 47). Pero hay valores de $M$ tan grandes como se quiera con $F(M)=0$ y otros con $F(M)=\frac1{2\pi}$: $L$ no puede estar a la vez cerca de los dos. $F(M)$ **oscila** entre $-\frac1{2\pi}$ y $\frac1{2\pi}$.
5. **Conclusión:** $\int_0^{+\infty}\cos(2\pi x)dx$ **diverge** (diverger incluye «el límite no existe», no solo «vale $\infty$»). El apartado 1 **no** lo garantiza: los enteros son «momentos de suerte» en los que el área acumulada vuelve a $0$.
6. **¿Y la condición necesaria (U p. 274)?** Aquí $\lim_{x\to\infty}\cos(2\pi x)$ no existe, así que esa condición no se puede aplicar ni a favor ni en contra; hay que ir a la definición.

**Receta.** Para la convergencia de $\int_a^\infty f$ hay que estudiar $\lim_{M\to\infty}F(M)$ con $M$ **real**. Para probar que **no** existe, basta encontrar dos formas de hacer crecer $M$ con resultados distintos.

**Error típico.** Calcular solo $\lim_{n\to\infty}F(n)$ con $n$ natural y concluir que converge.

sympy: $a_n=0$; $F(M)=\frac{\mathrm{sen}(2\pi M)}{2\pi}$; $\frac1{2\pi}\approx0{,}159155$.

---

### Ejercicio 6.47 (E pp. 249-250)

> Utiliza el *criterio de comparación mediante límites* (y la pista al margen) para estudiar si son convergentes o divergentes las integrales impropias $\int_1^{+\infty}\frac1{\ln(x+1)}dx$ y $\int_1^{+\infty}e^{-x^2}dx$.
>
> (Pista al margen: para cualquier $a>0$, la integral impropia $\int_a^{+\infty}\frac{dx}x$ es divergente y la integral impropia $\int_a^{+\infty}\frac{dx}{x^2}$ es convergente.)

**Antes de calcular**
- **Qué me piden:** el carácter de dos integrales sin primitiva elemental, con el límite del cociente.
- **Cómo lo pienso:** $\ln(x+1)$ crece más despacio que $x$, así que $\frac1{\ln(x+1)}$ baja **más despacio** que $\frac1x$ (que ya diverge) → diverge. $e^{-x^2}$ baja muchísimo más deprisa que $\frac1{x^2}$ → converge.
- **Qué uso:** comparación mediante límite (U p. 278), casos (iii) y (ii); L'Hôpital (U p. 82); Ej. 6.38.
- **Por dónde empiezo:** comprobar hipótesis: en $[1,\infty)$ ambas son continuas y positivas ($\ln(x+1)\ge\ln2>0$), y $g=\frac1x$, $g=\frac1{x^2}$ son $>0$.

1. **Primera, $g=\frac1x$:** $\lim_{x\to\infty}\frac{1/\ln(x+1)}{1/x}=\lim_{x\to\infty}\frac{x}{\ln(x+1)}$, tipo $\frac\infty\infty$. L'Hôpital: $\lim_{x\to\infty}\frac1{1/(x+1)}=\lim_{x\to\infty}(x+1)=+\infty$.
2. **Caso (iii):** $l=\infty$ y $\int_1^\infty\frac{dx}x$ diverge ⇒ $\int_1^{+\infty}\frac{dx}{\ln(x+1)}$ **diverge**.
3. **(Alternativa con desigualdad):** $\ln(1+x)\le x$ para $x>0$, luego $\frac1{\ln(x+1)}\ge\frac1x$, y la de abajo ya diverge (U p. 277).
4. **Segunda, primer intento con $g=\frac1x$:** $\lim_{x\to\infty}\frac{e^{-x^2}}{1/x}=\lim_{x\to\infty}\frac{x}{e^{x^2}}=\lim_{x\to\infty}\frac1{2xe^{x^2}}=0$. Pero $l=0$ con $\int g$ **divergente** no es ninguno de los tres casos: **el criterio no decide**.
5. **Segundo intento con $g=\frac1{x^2}$:** $\lim_{x\to\infty}\frac{x^2}{e^{x^2}}=\lim_{x\to\infty}\frac{2x}{2xe^{x^2}}=\lim_{x\to\infty}\frac1{e^{x^2}}=0$.
6. **Caso (ii):** $l=0$ y $\int_1^\infty\frac{dx}{x^2}$ converge ⇒ $\int_1^{+\infty}e^{-x^2}dx$ **converge** (vale $\approx0{,}1394$, pero no se puede calcular con primitivas elementales).

**Receta.** Con $l=0$ hay que comparar con una $g$ **convergente**; con $l=\infty$, con una $g$ **divergente**. Si sale el caso equivocado, probar con otra potencia.

**Error típico.** Concluir «diverge» en el paso 4 porque $\int\frac{dx}x$ diverge: con $l=0$ solo se transmite la convergencia.

sympy/mpmath: límites $\infty$, $0$, $0$; $\int_1^\infty e^{-x^2}dx=0{,}139403$; $\int_1^{1000}\frac{dx}{\ln(x+1)}\approx176{,}7$ (sigue creciendo).

---

### Ejercicio 6.48 (E pp. 250-252)

> Demuestra que para $p>0$ la siguiente integral impropia converge: $\Gamma(p)=\int_0^{+\infty}e^{-x}x^{p-1}dx$. Probar que para cada $p>0$ se tiene $\Gamma(p+1)=p\Gamma(p)$. Probar que $\Gamma(1)=1$ y deducir que para todo $n\in\mathbb N$ se tiene que $\Gamma(n+1)=n!$.

**Antes de calcular**
- **Qué me piden:** (a) convergencia para todo $p>0$; (b) la fórmula $\Gamma(p+1)=p\Gamma(p)$; (c) $\Gamma(1)=1$ y $\Gamma(n+1)=n!$.
- **Cómo lo pienso:** hay dos posibles problemas: el $+\infty$ (siempre) y el $0$ (solo si $p-1<0$, porque $x^{p-1}=\frac1{x^{1-p}}$ explota). Se parte en $1$ y cada trozo se compara con una referencia: cerca de $0$, $e^{-x}\approx1$ y $f\approx\frac1{x^{1-p}}$; en el infinito manda $e^{-x}$.
- **Qué uso:** 3ª especie: partir (U p. 275); comparación (U p. 277-278); Ej. 6.38, 6.39, 6.41; partes en la definida (U p. 254); L'Hôpital (U p. 82).
- **Por dónde empiezo:** $\Gamma(p)=\int_0^1e^{-x}x^{p-1}dx+\int_1^{\infty}e^{-x}x^{p-1}dx$.

**(a) Convergencia.**
1. **Signo:** $f(x)=e^{-x}x^{p-1}>0$ en $(0,\infty)$ y continua: se pueden usar los criterios de comparación.
2. **Trozo $[0,1]$.** Si $p\ge1$, $x^{p-1}$ es continua en $[0,1]$ (vale $1$ si $p=1$; $0$ en $x=0$ si $p>1$): integral ordinaria. Si $0<p<1$, $f(x)\to\infty$ cuando $x\to0^+$: 2ª especie.
3. **Comparación en $(0,1]$ (caso $0<p<1$):** como $0<e^{-x}\le1$, se tiene $0<f(x)\le x^{p-1}=\frac1{x^{1-p}}$. Y $\int_0^1\frac{dx}{x^{1-p}}$ converge porque el exponente $1-p<1$ (Ej. 6.41; aquí se usa $p>0$). ⇒ $\int_0^1f$ **converge**. (Con el límite: $\lim_{x\to0^+}\frac{f}{x^{p-1}}=\lim_{x\to0^+}e^{-x}=1\in(0,\infty)$, misma conclusión.)
4. **Trozo $[1,\infty)$.** $f$ es continua y acotada en $[1,\infty)$ (tiende a $0$). Con $g=\frac1{x^2}$: $\lim_{x\to\infty}\frac{f}{g}=\lim_{x\to\infty}\frac{x^{p+1}}{e^x}=0$ (si $p+1\le0$ es inmediato; si no, L'Hôpital repetido hasta que el exponente de $x$ sea $\le0$, mientras el denominador sigue siendo $e^x$).
5. **Caso (ii):** $l=0$ y $\int_1^\infty\frac{dx}{x^2}$ converge ⇒ $\int_1^\infty f$ **converge**.
6. **Conclusión:** los dos trozos convergen, luego $\Gamma(p)$ converge para todo $p>0$.

**(b) $\Gamma(p+1)=p\,\Gamma(p)$.**
7. **Planteamiento:** $\Gamma(p+1)=\int_0^\infty e^{-x}x^p\,dx$. Se trabaja en $[c,M]$ con $0<c<M$ (allí todo es continuo) y al final $c\to0^+$, $M\to\infty$.
8. **Partes** con $u=x^p$, $v'=e^{-x}$ ($u'=px^{p-1}$, $v=-e^{-x}$): $$\int_c^Me^{-x}x^p\,dx=\Big[-x^pe^{-x}\Big]_c^M+p\int_c^Me^{-x}x^{p-1}dx=-M^pe^{-M}+c^pe^{-c}+p\int_c^Me^{-x}x^{p-1}dx.$$
9. **Límites:** $M^pe^{-M}=\frac{M^p}{e^M}\to0$ (L'Hôpital, como en el paso 4); $c^pe^{-c}\to0\cdot1=0$ porque $p>0$; y $\int_c^Me^{-x}x^{p-1}dx\to\Gamma(p)$ por (a).
10. **Resultado:** $\Gamma(p+1)=0+0+p\,\Gamma(p)$.

**(c) $\Gamma(1)$ y factoriales.**
11. $\Gamma(1)=\int_0^\infty e^{-x}dx=1$ (Ej. 6.39 con $k=1$).
12. **Bajando de uno en uno con (b):** $\Gamma(n+1)=n\Gamma(n)=n(n-1)\Gamma(n-1)=\dots=n(n-1)\cdots2\cdot1\cdot\Gamma(1)=n!$. Ejemplos: $\Gamma(2)=1$, $\Gamma(3)=2$, $\Gamma(5)=24=4!$.
13. **(Cultura.)** $\Gamma$ extiende el factorial a cualquier $p>0$; por ejemplo $\Gamma(\frac12)=\sqrt\pi$. Está muy relacionada con la función Beta, $\beta(p,q)=\frac{\Gamma(p)\Gamma(q)}{\Gamma(p+q)}=\int_0^1x^{p-1}(1-x)^{q-1}dx$.

**Receta.** Integral con dos problemas: partir en un punto intermedio, y en cada trozo comparar con la referencia adecuada ($\frac1{x^q}$ cerca de $0$; $\frac1{x^2}$ en el infinito si hay una exponencial que decrece).

**Error típico.** Estudiar solo el infinito y olvidar el $0$ cuando $p<1$; o hacer partes en $[0,M]$ directamente cuando $\int_0^Me^{-x}x^{p-1}dx$ todavía es impropia.

sympy: $\Gamma(\frac12)=\sqrt\pi$, $\Gamma(1)=\Gamma(2)=1$, $\Gamma(5)=24$; $\frac{\int_0^\infty e^{-x}x^p}{\int_0^\infty e^{-x}x^{p-1}}=p$; $\lim_{x\to0^+}e^{-x}=1$; $\lim_{x\to\infty}x^{p+1}e^{-x}=0$.

---

### Fuera de examen: E 6.49-6.51 (para `details.fuera`)

Usan U §6.5.3 (convergencia uniforme e integración, pp. 279-280) y la integración término a término de series de potencias (Prop. 6.1, pp. 280-281). **No entran en examen.**

- **Ejercicio 6.49 (E pp. 252-253).** Calcula, para $n\in\mathbb N$, $\lim_{n\to+\infty}\int_2^3\frac{\cos n+\mathrm{sen}(nx)}{x^n}dx$. **Resultado: $0$.** En $[2,3]$, $\big|\frac{\cos n+\mathrm{sen}(nx)}{x^n}\big|\le\frac2{2^n}\to0$: convergencia uniforme a $0$, y se puede pasar el límite dentro de la integral.
- **Ejercicio 6.50 (E p. 253).** Dada la sucesión funcional $\{f_n\}$ donde $f_n(x)=\cos(nx)$, $x\in[0,2\pi]$, ¿puede existir $\lim_{n\to+\infty}\int_0^{2\pi}f_n(x)\,dx$ pese a no ser uniformemente convergente $\{f_n\}$? **Sí:** $\int_0^{2\pi}\cos(nx)dx=\frac{\mathrm{sen}(2\pi n)}n=0$ para todo $n$, límite $0$, aunque $\{f_n\}$ ni siquiera converge puntualmente (en $x=\frac\pi2$: $0,-1,0,1,\dots$).
- **Ejercicio 6.51 (E p. 254).** Calcula una primitiva de la función $f$ dada por $f(x)=\sum_{n=0}^{+\infty}\frac{2^n}{n!}x^n$. **Resultado:** radio de convergencia $\infty$; integrando término a término, $\int f=\sum_{n=0}^\infty\frac{2^n}{(n+1)!}x^{n+1}=\frac12f(x)-\frac12$; como $f(x)=e^{2x}$, es $\frac12e^{2x}-\frac12$.

---

## 3. Así lo preguntan en el examen (X)

Orden: clasificar sin calcular (pp. 25, 73, 81) → ¿es impropia? con una que no lo es (p. 105) → 1ª especie con valor (pp. 46-47, 150) → 2ª especie «escondida» (pp. 115-116) → 3ª especie divergente (pp. 93-94). **En X no hay preguntas de convergencia por comparación**: para eso, §3b.

---

### X p. 25 (Septiembre 2012, original, Ingeniería Mecánica, Modelo A, Pregunta corta 2)

> (1 PUNTO) Sean $a$ y $b$ dos números reales del intervalo $(-10,10)$. Razone si la integral $\int_a^bf(x)\,dx$ puede ser impropia.

**Antes de calcular**
- **Qué me piden:** decidir qué tipo de impropiedad es posible con límites de integración finitos.
- **Cómo lo pienso:** las causas son dos: límite infinito (imposible aquí) o $f$ no acotada (posible, no sabemos nada de $f$).
- **Qué uso:** Def. 6.9 y 6.10 (U pp. 272, 275).

1. **1ª especie: no.** $a$ y $b$ son números reales (están en $(-10,10)$): el intervalo de integración es acotado.
2. **2ª especie: sí puede.** Si $f$ no está acotada en $[a,b]$. Ejemplo: $a=0$, $b=1$, $f(x)=\frac1{\sqrt x}$: $\int_0^1\frac{dx}{\sqrt x}$ es impropia de 2ª especie (y converge, vale $2$); con $a=-1$, $b=1$, $f(x)=\frac1{x^2}$ es de 2ª especie con asíntota interior (y diverge).
3. **Respuesta:** sí, puede ser impropia, pero solo de **segunda especie**.

**Receta.** Límites finitos ⇒ solo puede haber 2ª especie, y solo si $f$ no está acotada en $[a,b]$.

**Error típico.** Contestar «no, porque el intervalo es acotado» olvidando la otra causa.

---

### X p. 73 (Septiembre 2016, Grado en Ingeniería Mecánica, Modelo B, Pregunta corta 3)

> (1 PUNTO) Clasifique la integral impropia siguiente: $\int_0^\infty e^{-x}dx$. Explique por qué es de ese tipo.

**Antes de calcular**
- **Qué me piden:** la especie y su justificación.
- **Qué uso:** Def. 6.9 (U p. 272); Ej. 6.39 (U pp. 273-274).

1. **Función:** $e^{-x}$ es continua en $[0,\infty)$ y $0<e^{-x}\le1$: está **acotada**. No hay 2ª especie.
2. **Intervalo:** $[0,\infty)$ no está acotado. Es de **primera especie**.
3. **(Si piden el valor):** $\lim_{M\to\infty}\big(1-e^{-M}\big)=1$: converge y vale $1$.

**Receta.** Clasificar = mirar intervalo (¿infinito?) y función (¿acotada?) por separado y decirlo con esas palabras.

**Error típico.** Decir solo «es de primera especie» sin explicar las dos comprobaciones (piden el porqué).

sympy: $1$.

---

### X p. 81 (Febrero 2017, Grado en Ingeniería Mecánica, Modelo B, Pregunta corta 3)

> (1 PUNTO) Dada la integral $\int_1^\infty\frac1{x^p}dx$ indique si para $p>1$ es impropia de primera y/o de segunda especie. Razone la respuesta.

**Antes de calcular**
- **Qué me piden:** decidir qué causas de impropiedad hay para $p>1$.
- **Cómo lo pienso:** el único punto donde $\frac1{x^p}$ explota es $x=0$, que **no** está en $[1,\infty)$.
- **Qué uso:** Def. 6.9 y 6.10 (U pp. 272, 275).

1. **Función:** para $x\ge1$ y $p>1$, $x^p\ge1$, luego $0<\frac1{x^p}\le1$: acotada y continua en $[1,\infty)$. **No** es de 2ª especie.
2. **Intervalo:** el límite superior es $\infty$: **es de 1ª especie** (solo de 1ª).
3. **(Además):** converge y vale $\frac1{p-1}$ (U Ej. 6.38).

**Receta.** Una asíntota vertical solo cuenta si está **dentro** del intervalo de integración.

**Error típico.** Decir «de 2ª especie porque $\frac1{x^p}$ tiene una asíntota en $0$»: $0\notin[1,\infty)$.

---

### X p. 105 (Ingeniería Electrónica, examen 3, sin fecha, Ejercicio 5)

> (3 PUNTOS) Dada la integral $\int_1^e\frac{\ln x}{x}dx$: Razone si es una integral impropia. Aproxime el valor de la integral utilizando la Fórmula del Trapecio. Calcule el valor real de la integral. Razone si la aproximación por la Fórmula del Trapecio puede ser irracional cuando la integral que aproxima tiene valor racional.

**Antes de calcular**
- **Qué me piden:** clasificar, aproximar con el trapecio, calcular el valor exacto y una reflexión.
- **Cómo lo pienso:** el único punto «peligroso» de $\frac{\ln x}x$ es $x=0$, fuera de $[1,e]$.
- **Qué uso:** Def. 6.9-6.10 (U pp. 272, 275); trapecio (U Def. 6.5, p. 267); tabla, fila $\int f^af'$ (U p. 248); Barrow (U p. 244).
- **Por dónde empiezo:** $\frac{\ln x}x$ es continua en $[1,e]$ (denominador $\ge1$).

1. **¿Impropia? No:** el intervalo $[1,e]$ es acotado y $\frac{\ln x}{x}$ es continua en él, luego acotada (Weierstrass). Integral ordinaria.
2. **Trapecio:** $f(1)=0$, $f(e)=\frac1e$: $\int_1^e\frac{\ln x}xdx\approx\frac{0+\frac1e}{2}(e-1)=\frac12-\frac1{2e}\approx0{,}3161$.
3. **Valor exacto:** $\frac{\ln x}{x}=\ln x\cdot(\ln x)'$, primitiva $\frac{(\ln x)^2}2$. Barrow: $\frac{1^2}2-\frac{0^2}2=\frac12$.
4. **Reflexión:** sí puede: el valor exacto $\frac12$ es racional y la aproximación $\frac12-\frac1{2e}$ es irracional (porque $e$ lo es).

**Receta.** «¿Es impropia?» se contesta siempre con las dos comprobaciones; si las dos fallan, Barrow directamente.

**Error típico.** Ver un $\ln$ o una fracción y declarar impropia sin mirar si el punto malo está en el intervalo.

sympy: $\frac12$; trapecio $0{,}316060$.

---

### X pp. 46-47 (Septiembre 2014, Modelo A, Ejercicio 5, apartado c)

> Sea $f(x)=\frac{2}{x(x-1)}$ […] c) Estúdiese si la integral $\int_{-\infty}^{-1}f(x)\,dx=\int_{-\infty}^{-1}\frac{2}{x(x-1)}dx$ es impropia. En caso de que lo sea, indíquese de qué especie. (En el apartado a) se pedía la primitiva: $\int\frac2{x(x-1)}dx=2\ln\lvert x-1\rvert-2\ln\lvert x\rvert+C$.)

**Antes de calcular**
- **Qué me piden:** clasificar (y, como extra, el valor).
- **Cómo lo pienso:** los ceros del denominador, $0$ y $1$, quedan fuera de $(-\infty,-1]$; el único problema es el $-\infty$.
- **Qué uso:** Def. 6.9 y extensión a $(-\infty,b]$ (U pp. 272, 274); fracciones simples (U p. 255).
- **Por dónde empiezo:** el signo y el tamaño de $x(x-1)$ para $x\le-1$.

1. **Función acotada:** para $x\le-1$, $x<0$ y $x-1<0$, luego $x(x-1)>0$; además $x(x-1)\ge(-1)(-2)=2$ (crece al alejarse de $-1$). Así $0<f(x)\le\frac22=1$: continua y acotada. No hay 2ª especie.
2. **Intervalo no acotado** (límite $-\infty$): **1ª especie**, única causa.
3. **Valor (extra):** $F(x)=2\ln\lvert x-1\rvert-2\ln\lvert x\rvert=2\ln\Big\lvert\frac{x-1}{x}\Big\rvert$. $F(-1)=2\ln2$; cuando $M\to-\infty$, $\frac{M-1}{M}\to1$ y $F(M)\to2\ln1=0$.
4. **Conclusión:** $\int_{-\infty}^{-1}f=\lim_{M\to-\infty}\big(F(-1)-F(M)\big)=2\ln2\approx1{,}386$: converge.

**Receta.** En racionales, localizar las raíces del denominador y ver si caen en el intervalo; juntar los logaritmos en uno solo antes de tomar el límite ($\infty-\infty$ desaparece).

**Error típico.** Calcular $\lim_{M\to-\infty}2\ln\lvert M-1\rvert$ y $\lim_{M\to-\infty}2\ln\lvert M\rvert$ por separado ($\infty-\infty$).

sympy: $2\ln2$.

---

### X p. 150 (Febrero 2019, 1ª semana, I. Electrónica Industrial y Automática, Pregunta corta 2)

> (1 PUNTO) Decida si la siguiente integral impropia es de primera o de segunda especie, y calcule su valor: $\int_0^{+\infty}\frac{x}{\sqrt{e^x}}dx$.

**Antes de calcular**
- **Qué me piden:** la especie y el valor.
- **Cómo lo pienso:** $\frac{x}{\sqrt{e^x}}=xe^{-x/2}$: una potencia por una exponencial decreciente, que gana. Es como $\Gamma(2)$ con $x/2$.
- **Qué uso:** Def. 6.9 (U p. 272); partes (U p. 252); L'Hôpital (U p. 82).
- **Por dónde empiezo:** reescribir $\sqrt{e^x}=e^{x/2}$.

1. **Clasificación:** $f(x)=xe^{-x/2}$ es continua en $[0,\infty)$, $\ge0$ y tiende a $0$ en el infinito; tiene un máximo ($\frac2e$ en $x=2$), así que está acotada. Intervalo no acotado: **1ª especie**.
2. **Primitiva por partes** ($u=x$, $v'=e^{-x/2}$, $v=-2e^{-x/2}$): $\int xe^{-x/2}dx=-2xe^{-x/2}+\int2e^{-x/2}dx=-2xe^{-x/2}-4e^{-x/2}=(-2x-4)e^{-x/2}$.
3. **Barrow en $[0,M]$:** $(-2M-4)e^{-M/2}-(-4)=4-\frac{2M+4}{e^{M/2}}$.
4. **Límite:** $\frac{2M+4}{e^{M/2}}$ es $\frac\infty\infty$; L'Hôpital: $\frac{2}{\frac12e^{M/2}}\to0$.
5. **Valor:** $4$. Converge.

**Receta.** Polinomio × exponencial decreciente: partes (derivando el polinomio) y el límite final siempre da $0$ en el infinito.

**Error típico.** Signo en $v$: $\int e^{-x/2}dx=-2e^{-x/2}$, no $-\frac12e^{-x/2}$.

sympy: $4$; $\frac{d}{dx}\big[(-2x-4)e^{-x/2}\big]=xe^{-x/2}$ ✓.

---

### X pp. 115-116 (Examen 3 elaborado con exámenes de asignaturas similares, Ejercicio 3)

> Señale el valor de $\int_0^{\frac\pi2}\frac{\cos x}{\sqrt{\mathrm{sen}\,x}}dx$: A) 0; B) $\frac\pi4$; C) 2; D) Ninguno de los anteriores.

**Antes de calcular**
- **Qué me piden:** el valor (test).
- **Cómo lo pienso:** en $x=0$, $\mathrm{sen}\,x=0$ y el denominador se anula: hay una asíntota vertical en el extremo izquierdo, **es impropia de 2ª especie**, aunque el enunciado no lo diga.
- **Qué uso:** Def. 6.10 (U p. 275); tabla, fila $\int f^af'$ con $f=\mathrm{sen}\,x$, $a=-\frac12$ (U p. 248).
- **Por dónde empiezo:** $\lim_{x\to0^+}\frac{\cos x}{\sqrt{\mathrm{sen}\,x}}=\frac{1}{0^+}=+\infty$.

1. **Clasificación:** $f$ continua en $(0,\frac\pi2]$, no acotada cerca de $0$: 2ª especie.
2. **Primitiva:** $\int(\mathrm{sen}\,x)^{-1/2}\cos x\,dx=\frac{(\mathrm{sen}\,x)^{1/2}}{1/2}=2\sqrt{\mathrm{sen}\,x}$.
3. **Definición:** $\lim_{c\to0^+}\Big[2\sqrt{\mathrm{sen}\,x}\Big]_c^{\pi/2}=\lim_{c\to0^+}\big(2-2\sqrt{\mathrm{sen}\,c}\big)=2$.
4. **Respuesta C) 2.** Converge.
5. **¿Por qué «Barrow a ciegas» da lo mismo aquí?** Porque la primitiva $2\sqrt{\mathrm{sen}\,x}$ es continua en $0$ (vale $0$): el límite coincide con $F(0)$. Cuando la primitiva se va a infinito (como $-\frac1x$ en U Ej. 6.42), no.

**Receta.** Si la primitiva tiene límite finito en el punto problemático, la impropia converge y su valor es «$F(b)-F(a)$» con ese límite; pero hay que escribir el límite.

**Error típico.** No detectar la impropiedad (el integrando «parece» inofensivo porque el intervalo es acotado).

sympy: $2$; $\lim_{x\to0^+}f=\infty$.

---

### X pp. 93-94 (Febrero 2018, Grado en Ingeniería Mecánica, Modelo B, Ejercicio 5, apartado c)

> Sea $f$ la función dada por $f(x)=\frac{2}{x(x+2)}$. […] (c) (0.75 puntos) Estudie si la integral $\int_{-\infty}^{-2}f(x)\,dx=\int_{-\infty}^{-2}\frac{2}{x(x+2)}dx$ es impropia. En caso de que lo sea, indique de qué especie o especies. (En el apartado a) se obtenía la primitiva $\int\frac{2}{x(x+2)}dx=-\ln\lvert x+2\rvert+\ln\lvert x\rvert+C$.)

**Antes de calcular**
- **Qué me piden:** clasificar (y, como extra, estudiar si converge).
- **Cómo lo pienso:** dos problemas: el $-\infty$ y la raíz $x=-2$ del denominador, que es justo el extremo derecho.
- **Qué uso:** Def. 6.9 y 6.10 (U pp. 272, 275); 3ª especie (U margen p. 275).
- **Por dónde empiezo:** $\lim_{x\to-2^-}\frac{2}{x(x+2)}$: $x\to-2$, $x+2\to0^-$, $x(x+2)\to(-2)(0^-)=0^+$, luego $f\to+\infty$.

1. **Clasificación:** límite $-\infty$ (1ª especie) **y** $f$ no acotada en $-2$ (2ª especie): es de **primera y segunda especie** a la vez (de 3ª especie).
2. **Partir** en un punto intermedio, p. ej. $-3$: $\int_{-\infty}^{-2}=\int_{-\infty}^{-3}+\int_{-3}^{-2}$.
3. **Trozo de 2ª especie:** con $F(x)=\ln\lvert x\rvert-\ln\lvert x+2\rvert$: $\lim_{c\to-2^-}\big(F(c)-F(-3)\big)=\lim_{c\to-2^-}\big(\ln\lvert c\rvert-\ln\lvert c+2\rvert\big)-\ln3=\ln2-(-\infty)-\ln3=+\infty$. **Diverge.**
4. **Conclusión:** como un trozo diverge, $\int_{-\infty}^{-2}f$ **diverge** (el otro trozo converge, vale $\ln3$, pero da igual).

**Receta.** 3ª especie: partir, y en cuanto un trozo diverja, la integral diverge.

**Error típico.** Usar Barrow con la primitiva en $[-\infty,-2]$ como si nada: $F(-2)$ no existe.

sympy: $\lim_{x\to-2^-}\big(\ln\lvert x\rvert-\ln\lvert x+2\rvert\big)=\infty$; $\lim_{x\to-\infty}F=0$.

---

## 3b. Tipos de pregunta que no aparecen en X (y pueden caer)

Resueltos solo con los criterios de U (comparación y comparación por límite, pp. 277-278) y las integrales de referencia.

### Tipo A — Convergencia por comparación en el infinito: $\int_1^\infty\frac{dx}{\sqrt{x^3+1}}$ [propio]

**Antes de calcular**
- **Qué me piden:** el carácter (no hay primitiva elemental).
- **Cómo lo pienso:** $\sqrt{x^3+1}\approx x^{3/2}$; $\frac1{x^{3/2}}$ tiene exponente $>1$: converge.
- **Qué uso:** comparación (U p. 277); Ej. 6.38.
- **Por dónde empiezo:** $f>0$, continua y acotada ($\le\frac1{\sqrt2}$) en $[1,\infty)$: 1ª especie.

1. **Desigualdad:** $x^3+1\ge x^3\Rightarrow\frac1{\sqrt{x^3+1}}\le\frac1{x^{3/2}}$.
2. **Referencia:** $\int_1^\infty\frac{dx}{x^{3/2}}$ converge ($p=\frac32>1$) y vale $2$.
3. **Conclusión:** converge (y su valor es menor que $2$; numéricamente $\approx1{,}8948$).

**Receta.** Grado del denominador − grado del numerador (contando raíces como fracciones) $>1$ ⇒ converge en el infinito.

**Error típico.** Comparar con $\frac1{x^3}$ (olvidar la raíz): $\frac1{\sqrt{x^3+1}}\le\frac1{x^3}$ es **falso** para $x>1$.

mpmath: $1{,}89476$.

### Tipo B — Comparación de 2ª especie: $\int_0^1\frac{dx}{\sqrt{x(1+x)}}$ [propio]

**Antes de calcular**
- **Qué me piden:** el carácter (y el valor, si se puede).
- **Cómo lo pienso:** cerca de $0$, $x(1+x)\approx x$ y $f\approx\frac1{\sqrt x}$: exponente $\frac12<1$, converge.
- **Qué uso:** comparación de 2ª especie (U p. 278); Ej. 6.41.
- **Por dónde empiezo:** $f\to+\infty$ cuando $x\to0^+$: 2ª especie en $0$.

1. **Desigualdad en $(0,1]$:** $1+x\ge1\Rightarrow x(1+x)\ge x\Rightarrow f(x)\le\frac1{\sqrt x}$.
2. **Referencia:** $\int_0^1\frac{dx}{\sqrt x}=2$ converge. ⇒ **converge**.
3. **(Valor, para quien quiera):** con $t=\sqrt x$ ($x=t^2$, $dx=2t\,dt$): $\int\frac{2t\,dt}{t\sqrt{1+t^2}}=2\int\frac{dt}{\sqrt{1+t^2}}=2\ln\big(t+\sqrt{1+t^2}\big)$. Valor $2\ln(1+\sqrt2)\approx1{,}7627<2$ ✓.

**Receta.** Cerca de $0$, quedarse con la **menor** potencia de $x$ en cada factor.

**Error típico.** Tomar el término de mayor grado ($x^2$) como en el infinito: $\frac1{\sqrt{x^2}}=\frac1x$, cuya integral diverge, y concluir mal (además la desigualdad $f\le\frac1x$ es cierta pero no sirve: compara con algo divergente por arriba).

sympy: $2\,\mathrm{arccosh}\sqrt2=2\ln(1+\sqrt2)=1{,}76275$.

### Tipo C — Un punto que **no** es problema: $\int_0^\infty\frac{\mathrm{sen}^2x}{x^2}dx$ [propio]

**Antes de calcular**
- **Qué me piden:** clasificar y estudiar la convergencia.
- **Cómo lo pienso:** en $x=0$ el cociente no está definido, pero $\frac{\mathrm{sen}\,x}{x}\to1$: la función está acotada cerca de $0$. El único problema es el infinito, y ahí $0\le\frac{\mathrm{sen}^2x}{x^2}\le\frac1{x^2}$.
- **Qué uso:** Def. 6.9 (U p. 272); comparación (U p. 277); $\lim_{x\to0}\frac{\mathrm{sen}\,x}{x}=1$ (L'Hôpital, U p. 82).
- **Por dónde empiezo:** partir en $1$.

1. **En $0$:** $\lim_{x\to0^+}\frac{\mathrm{sen}^2x}{x^2}=1^2=1$. Definiendo $f(0)=1$, $f$ es continua en $[0,1]$: $\int_0^1f$ es una integral **ordinaria** (no es de 2ª especie: la función está acotada).
2. **En $[1,\infty)$:** $f\ge0$ (es un cuadrado entre un cuadrado) y $\mathrm{sen}^2x\le1\Rightarrow f(x)\le\frac1{x^2}$.
3. **Referencia:** $\int_1^\infty\frac{dx}{x^2}$ converge. ⇒ $\int_1^\infty f$ converge.
4. **Conclusión:** impropia **solo de 1ª especie** y **convergente**. (Su valor, $\frac\pi2$, no se puede obtener con primitivas elementales; no se pide.)

**Receta.** Ante un denominador que se anula, calcular el **límite** de $f$ en ese punto: si es finito, no hay 2ª especie.

**Error típico.** Clasificarla como de 3ª especie por el $x^2$ del denominador. Y otro: intentar la condición necesaria «$f\to0$» como prueba de convergencia (solo sirve para probar divergencia).

sympy: $\lim_{x\to0}f=1$; $\int_0^\infty f=\frac\pi2$.

### Tipo D — Comparación por límite en $0^+$: $\int_0^1\frac{dx}{\mathrm{sen}\,x}$ frente a $\int_0^1\frac{dx}{\sqrt{\mathrm{sen}\,x}}$ [propio]

**Antes de calcular**
- **Qué me piden:** el carácter de las dos.
- **Cómo lo pienso:** cerca de $0$, $\mathrm{sen}\,x\approx x$: la primera se parece a $\frac1x$ (diverge) y la segunda a $\frac1{\sqrt x}$ (converge).
- **Qué uso:** comparación mediante límite extendida a 2ª especie (U margen p. 278: $\lim_{x\to a^+}\frac fg$); Ej. 6.41.
- **Por dónde empiezo:** en $(0,1]$, $\mathrm{sen}\,x>0$ (porque $1<\pi$): ambas son positivas y continuas, y explotan en $0^+$.

1. **Primera, $g=\frac1x$:** $\lim_{x\to0^+}\frac{1/\mathrm{sen}\,x}{1/x}=\lim_{x\to0^+}\frac{x}{\mathrm{sen}\,x}=1\in(0,\infty)$.
2. Mismo carácter que $\int_0^1\frac{dx}x$, que diverge ⇒ $\int_0^1\frac{dx}{\mathrm{sen}\,x}$ **diverge**.
3. **Segunda, $g=\frac1{\sqrt x}$:** $\lim_{x\to0^+}\sqrt{\frac{x}{\mathrm{sen}\,x}}=1$. Mismo carácter que $\int_0^1\frac{dx}{\sqrt x}$, que converge ⇒ **converge** ($\approx2{,}0348$).

**Receta.** Cerca de $0$, sustituir cada función por su equivalente ($\mathrm{sen}\,x\approx x$, $e^x-1\approx x$, $\ln(1+x)\approx x$, $1-\cos x\approx\frac{x^2}2$) para elegir $g=\frac1{x^q}$; luego comprobar el límite del cociente.

**Error típico.** Calcular el límite del cociente en $x\to\infty$ (copiando el recuadro) cuando el problema está en $0^+$.

sympy: ambos límites $1$; mpmath $\int_0^1\frac{dx}{\sqrt{\mathrm{sen}\,x}}=2{,}03481$.

---

## 3c. Autoevaluación de U (p. 282), ítems de impropias

> 9. La integral impropia $\int_0^\infty\ln(x)\,dx$ es de segunda especie.

**Falso.** Tiene las dos causas: límite $\infty$ y $\ln x\to-\infty$ cuando $x\to0^+$. Es de **3ª especie** (U margen p. 275). Partiendo en $1$: $\int_0^1\ln x=-1$ converge (E 6.46), pero $\int_1^M\ln x\,dx=M\ln M-M+1\to\infty$ diverge; luego la integral **diverge**.

> 10. Si $f$ es una función continua decreciente en $[1,\infty)$ y $\lim_{x\to\infty}f(x)=0$, entonces $\int_1^\infty f(x)\,dx$ es convergente.

**Falso.** Contraejemplo: $f(x)=\frac1x$ es continua, decreciente, tiende a $0$, y $\int_1^\infty\frac{dx}x$ diverge (U Ej. 6.37). La condición $f\to0$ es **necesaria** (U p. 274), no suficiente.

---

## 4. Ejemplos propios (dificultad creciente)

### Propio 1 — $\int_1^\infty\frac{dx}{x(x+1)}$ (fácil) [propio]

> Calcula $\int_1^\infty\frac{dx}{x(x+1)}$ usando la definición.

**Antes de calcular**
- **Qué me piden:** el valor.
- **Cómo lo pienso:** $\frac1{x(x+1)}\approx\frac1{x^2}$ en el infinito: converge. Es racional: fracciones simples.
- **Qué uso:** Def. 6.9 (U p. 272); fracciones simples (U p. 255).
- **Por dónde empiezo:** raíces del denominador $0$ y $-1$, fuera de $[1,\infty)$; $0<f\le\frac12$: 1ª especie.

1. **Fracciones simples:** $\frac1{x(x+1)}=\frac1x-\frac1{x+1}$.
2. **Primitiva:** $\ln x-\ln(x+1)=\ln\frac{x}{x+1}$ (en $[1,\infty)$ no hacen falta valores absolutos).
3. **Barrow en $[1,M]$:** $\ln\frac{M}{M+1}-\ln\frac12$.
4. **Límite:** $\frac{M}{M+1}\to1$, $\ln1=0$; resultado $-\ln\frac12=\ln2\approx0{,}693$.

**Receta.** Juntar los logaritmos en uno solo antes del límite.

**Error típico.** Separar $\lim_{M\to\infty}\ln M-\lim_{M\to\infty}\ln(M+1)=\infty-\infty$ y declarar «diverge».

sympy: $\ln2$.

---

### Propio 2 — $\int_2^\infty\frac{dx}{x(\ln x)^q}$: la frontera fina (medio) [propio]

> Estudia, según el valor de $q>0$, la convergencia de $\int_2^\infty\frac{dx}{x(\ln x)^q}$, y calcula su valor cuando converja.

**Antes de calcular**
- **Qué me piden:** el carácter según $q$ y el valor.
- **Cómo lo pienso:** el integrando baja un poco más deprisa que $\frac1x$ (dividido por una potencia de $\ln x$, que crece muy despacio). Comparar con $\frac1x$ o $\frac1{x^2}$ no decide: hay que hacer la integral.
- **Qué uso:** Def. 6.9 (U p. 272); tabla, fila $\int f^af'$ con $f=\ln x$ (U p. 248); Ej. 6.37-6.38.
- **Por dónde empiezo:** $\frac1x$ es la derivada de $\ln x$: cambio $t=\ln x$.

1. **Cambio** $t=\ln x$, $dt=\frac{dx}x$; $x=2\to t=\ln2$; $x=M\to t=\ln M\to\infty$: $\int_2^M\frac{dx}{x(\ln x)^q}=\int_{\ln2}^{\ln M}\frac{dt}{t^q}$.
2. **Es la integral modelo** $\int\frac{dt}{t^q}$ desde $\ln2>0$ hasta infinito: converge $\iff q>1$ (Ej. 6.38 y el cambio de extremo «bueno»).
3. **$q=1$:** $\big[\ln t\big]_{\ln2}^{\ln M}=\ln(\ln M)-\ln(\ln2)\to\infty$: diverge (muy despacio: para $M=10^{100}$ solo vale $\approx5{,}8$).
4. **$q>1$:** $\Big[\frac{t^{1-q}}{1-q}\Big]_{\ln2}^{\ln M}\to0-\frac{(\ln2)^{1-q}}{1-q}=\frac{(\ln2)^{1-q}}{q-1}$. Ej.: $q=2$: $\frac1{\ln2}\approx1{,}443$.
5. **$0<q<1$:** $(\ln M)^{1-q}\to\infty$: diverge.

**Receta.** Si aparece $\frac{f'}{f^q}$, el cambio $t=f(x)$ convierte la integral en una de referencia.

**Error típico.** Comparar con $\frac1x$ «porque se parece» y concluir divergente para todo $q$; o pensar que una integral que «crece tan despacio» converge.

sympy: $q=2$: $\frac1{\ln2}$; $q=\frac32$: $\frac2{\sqrt{\ln2}}$; $q=1$: $\infty$.

---

### Propio 3 — Asíntota interior: $\int_{-1}^1\frac{dx}{\sqrt[3]x}$ frente a $\int_{-1}^1\frac{dx}{x}$ (medio-difícil) [propio]

> (a) Estudia $\int_{-1}^1\frac{dx}{\sqrt[3]x}$ ($\sqrt[3]x$ es la raíz cúbica real, definida también para $x<0$). (b) Estudia $\int_{-1}^1\frac{dx}x$. (c) ¿Por qué no basta decir «la función es impar, la integral vale $0$»?

**Antes de calcular**
- **Qué me piden:** el carácter de dos integrales con una asíntota en $x=0$, interior al intervalo.
- **Cómo lo pienso:** hay que partir en $0$ y estudiar cada mitad **por separado** (U p. 276). La simetría solo sirve si las dos mitades convergen.
- **Qué uso:** Def. 6.10 y asíntota interior (U pp. 275-276); Ej. 6.41.
- **Por dónde empiezo:** $\lim_{x\to0^\pm}\frac1{\sqrt[3]x}=\pm\infty$ y $\lim_{x\to0^\pm}\frac1x=\pm\infty$: ambas no acotadas.

1. **(a) Partir:** $\int_{-1}^1=\int_{-1}^0+\int_0^1$. Primitiva de $x^{-1/3}$: $\frac32x^{2/3}=\frac32\sqrt[3]{x^2}$ (válida y continua en todo $\mathbb R$).
2. **(a) Trozo derecho:** $\lim_{c\to0^+}\big(\frac32-\frac32c^{2/3}\big)=\frac32$: converge ($p=\frac13<1$).
3. **(a) Trozo izquierdo:** $\lim_{c\to0^-}\int_{-1}^c x^{-1/3}dx=\lim_{c\to0^-}\big(\frac32\sqrt[3]{c^2}-\frac32\sqrt[3]{1}\big)=0-\frac32=-\frac32$: converge.
4. **(a) Conclusión:** las dos mitades convergen ⇒ **converge** y vale $\frac32-\frac32=0$.
5. **(b) Trozo derecho:** $\lim_{c\to0^+}\int_c^1\frac{dx}x=\lim_{c\to0^+}(-\ln c)=+\infty$: diverge. ⇒ $\int_{-1}^1\frac{dx}x$ **diverge** (no hace falta mirar la otra mitad).
6. **(c)** En (b), $\frac1x$ es impar y «el área de la izquierda cancela la de la derecha», pero son **dos áreas infinitas**: $\infty-\infty$ no es $0$. La definición de U exige que cada trozo converja por separado; si no, diverge. En (a) la simetría sí da el valor $0$, porque cada mitad es finita.

**Receta.** Asíntota interior: partir, calcular cada mitad con su propio límite lateral, y solo si las dos son números sumarlas.

**Error típico.** Usar un único límite simétrico, $\lim_{\varepsilon\to0^+}\Big(\int_{-1}^{-\varepsilon}+\int_\varepsilon^1\Big)\frac{dx}x=0$, y concluir que (b) vale $0$. Ese límite no es la definición.

mpmath: (a) $0$ (mitades $\pm\frac32$); sympy (b) $\int_0^1\frac{dx}x=\infty$.

---

### Propio 4 — Tercera especie: $\int_0^\infty\frac{dx}{\sqrt x\,(1+x)}$ y por qué $\int_0^\infty\frac{dx}{x^p}$ nunca converge (difícil) [propio]

> (a) Clasifica y calcula $\int_0^\infty\frac{dx}{\sqrt x\,(1+x)}$. (b) Demuestra que $\int_0^\infty\frac{dx}{x^p}$ diverge para todo $p$.

**Antes de calcular**
- **Qué me piden:** una de 3ª especie con valor, y un resultado general.
- **Cómo lo pienso:** en $0$, $f\approx\frac1{\sqrt x}$ (sube despacio, bien); en el infinito, $f\approx\frac1{x^{3/2}}$ (baja deprisa, bien). Pero $\frac1{x^p}$ no puede estar bien en los dos sitios: en $0$ necesita $p<1$ y en el infinito $p>1$.
- **Qué uso:** 3ª especie (U margen p. 275); comparación (U pp. 277-278); Ej. 6.38 y 6.41; cambio de variable (U p. 251).
- **Por dónde empiezo:** partir en $1$.

1. **(a) Clasificación:** límite $\infty$ y $f\to\infty$ cuando $x\to0^+$: **3ª especie**. $\int_0^\infty=\int_0^1+\int_1^\infty$.
2. **(a) Carácter de $\int_0^1$:** $1+x\ge1\Rightarrow f\le\frac1{\sqrt x}$, y $\int_0^1\frac{dx}{\sqrt x}$ converge ⇒ converge.
3. **(a) Carácter de $\int_1^\infty$:** $1+x\ge x\Rightarrow f\le\frac1{\sqrt x\cdot x}=\frac1{x^{3/2}}$, y $\int_1^\infty\frac{dx}{x^{3/2}}$ converge ⇒ converge (además $f\le\frac12$ en $[1,\infty)$: acotada).
4. **(a) Valor:** con $t=\sqrt x$ ($dx=2t\,dt$): $\int\frac{2t\,dt}{t(1+t^2)}=2\,\mathrm{arctg}\,t=2\,\mathrm{arctg}\sqrt x$. Entonces $\int_0^1f=\lim_{c\to0^+}\big(2\,\mathrm{arctg}1-2\,\mathrm{arctg}\sqrt c\big)=\frac\pi2$ y $\int_1^\infty f=\lim_{M\to\infty}\big(2\,\mathrm{arctg}\sqrt M-\frac\pi2\big)=\pi-\frac\pi2=\frac\pi2$. Total: $\pi$.
5. **(b)** $\int_0^\infty\frac{dx}{x^p}=\int_0^1+\int_1^\infty$. Si $p\le1$, $\int_1^\infty$ diverge (Ej. 6.38). Si $p\ge1$, $\int_0^1$ diverge (Ej. 6.41). Todo $p$ cae en algún caso (y $p=1$ en los dos): siempre diverge algún trozo, luego **siempre diverge**. (Para $p\le0$ ni siquiera es de 3ª especie: solo de 1ª, y diverge.)

**Receta.** 3ª especie: un trozo con cada problema; en cada uno, la referencia $\frac1{x^q}$ con la desigualdad que toca ($q<1$ cerca de $0$, $q>1$ en el infinito).

**Error típico.** Comparar toda la integral con una sola $\frac1{x^q}$ en $(0,\infty)$: esa referencia **siempre diverge** (apartado b), así que no sirve para probar convergencia.

sympy: $\int_0^1f=\int_1^\infty f=\frac\pi2$, total $\pi$.

---

## 5. Chuleta rápida del tema

- **1ª especie** (U Def. 6.9, p. 272): $\int_a^\infty f=\lim_{M\to\infty}\int_a^Mf$, $f$ continua y acotada. **2ª especie** (U Def. 6.10, p. 275): $\int_a^bf=\lim_{c\to a^+}\int_c^bf$, $f$ continua no acotada en $(a,b]$. **3ª especie** (U p. 275): las dos causas; se parte.
- **Converge** = el límite es un número real; **diverge** = es $\pm\infty$ **o no existe** (E 6.44).
- **Partir:** en $\mathbb R$, en asíntotas interiores y en 3ª especie; converge solo si convergen **todos** los trozos (con límites **independientes**).
- **Referencias:** $\int_1^\infty\frac{dx}{x^p}$ converge $\iff p>1$ ($\frac1{p-1}$); $\int_0^1\frac{dx}{x^p}$ converge $\iff p<1$ ($\frac1{1-p}$); $\int_0^\infty e^{-kx}dx=\frac1k$ ($k>0$); $\int_{-\infty}^\infty\frac{dx}{1+x^2}=\pi$; $\int_0^1\ln x\,dx=-1$; $\int_0^\infty\frac{dx}{x^p}$ diverge siempre.
- **Comparación** (U p. 277): $0\le f\le g$: $\int g$ conv ⇒ $\int f$ conv; $\int f$ div ⇒ $\int g$ div. **Por límite** (U p. 278): $\frac fg\to l\in(0,\infty)$ ⇒ mismo carácter; $l=0$ + $\int g$ conv ⇒ conv; $l=\infty$ + $\int g$ div ⇒ div. En $0^+$: igual con $\lim_{x\to a^+}$.
- **Condición necesaria** (U p. 274): si $\lim_{x\to\infty}f$ existe y no es $0$, diverge. Si es $0$, **no** se sabe ($\frac1x$).
- **Errores frecuentes:** Barrow sin ver la asíntota interior ($\int_{-1}^1\frac{dx}{x^2}=-2$, falso); creer que $f$ no acotada solo importa en los extremos; tomar un único límite simétrico ($\int_{-\infty}^\infty x\,dx$, $\int_{-1}^1\frac{dx}x$); comparar con funciones que cambian de signo o con la desigualdad al revés; usar $l=0$ con $g$ divergente; calcular el límite del cociente en el punto que no es el problemático; separar logaritmos y obtener $\infty-\infty$; llamar «impropia» a una integral cuyo punto malo está fuera del intervalo o cuya función tiene límite finito en él.
