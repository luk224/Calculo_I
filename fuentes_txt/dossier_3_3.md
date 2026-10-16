# Dossier Tema 3.3: Interpolación polinómica

**Fuentes**: U = *Cálculo para Ingenieros* (`ingenieros.txt`), §3.3, pp. 119-124 impresas (PDF 117-122; impresa = PDF + 2). S = *Cálculo de una variable* (Stewart, `stewart.txt`), cap. 11, §11.10. L = *Cálculo Tomo 1* (Larson, `larson.txt`), cap. 9, §9.7 (impresa = PDF − 17). E = libro de ejercicios (`ejercicios.txt`, impresa = PDF). X = *Exámenes resueltos* (`Examenes-resueltos-Calculo.pdf`, página PDF, leída como imagen con PyMuPDF).

**Alcance de examen**: §3.3 completo (interpolación, diferencias divididas de Newton, tabla de diferencias). Lo confirman 9 preguntas de X (ver §4). No hay partes «fuera de examen» en este tema.

**Notación**: U escribe el polinomio interpolador como $p_n$, los nodos como $x_k$, los datos como $f_k$ y las diferencias divididas como $f[x_k,\dots,x_{k+m}]$. Las tildes de U se han restaurado (el texto extraído las pierde). Los cálculos están comprobados con sympy en aritmética exacta.

**Aviso importante**: la **forma de Lagrange del error de interpolación** (citada en las notas adicionales del cronograma para este módulo) **no aparece en U §3.3**, ni en S ni en L, y las notas adicionales **no están en el repositorio**. Ver §5.

---

## 1. LIBRO OFICIAL (U), §3.3

### 3.3.1 Motivación (p. 119)

Texto (p. 119): «A menudo vamos a necesitar trabajar con una función cuya expresión no conocemos o vamos a necesitar una expresión más sencilla de una función. […] Estos problemas se resuelven aproximadamente mediante interpolación, que es el proceso por el que se determina una función que vale exactamente los valores dados.»

Texto (p. 119): «Lo más sencillo es aproximar por la poligonal que pasa por todos los datos. Pero si queremos encontrar una curva suave, fácil de construir y de evaluar, lo mejor es buscar un polinomio. Entonces hablamos de interpolación polinómica.»

Cuadro «Splines» (p. 121, margen): si los datos no son suaves y se aumenta el grado, el polinomio puede oscilar entre datos; una alternativa son los splines (polinomios a trozos con condiciones de derivabilidad en los nodos). **No entra en examen** (no aparece en X ni en E).

### Orientaciones y objetivos (p. 120)

Texto (p. 120): «Antes de resolver un problema, es conveniente que se representen gráficamente los datos para poder anticipar qué tipo de polinomio vamos a obtener. Además, es conveniente que se compruebe que el resultado, ya que el proceso de interpolación supone realizar diversas operaciones y es fácil equivocarse.»

Objetivos (p. 120): «… el estudiante podrá elaborar una tabla de diferencias a partir de un conjunto de datos y construir un polinomio de interpolación a partir de unos datos dados.»

### 3.3.2 Interpolación (pp. 120-121)

Texto (p. 120): «Pero este resultado no nos vale para la interpolación, no sólo porque hace falta conocer el valor de f y sus derivadas en x a priori, sino también porque sólo es una buena aproximación cerca de a. Y queremos que aproxime bien en todo un intervalo.»

Datos (p. 120): «En general, disponemos de una colección de datos $(x_k, f_k)$ para $k = 0,\dots,n$. Los números $x_k$ se llaman nodos y $f_k$ representa el valor de la función $f(x)$ […] en $x_k$. Buscamos un polinomio de grado $n$, $p_n(x) = a_0 + a_1x + \dots + a_nx^n$, de forma que $p_n(x_k) = f_k$ para $k = 0,\dots,n$.»

Texto (p. 121): «El polinomio $p_n(x)$ se llama polinomio de interpolación o polinomio interpolador.»

Sistema lineal (p. 121): las $n+1$ condiciones dan un sistema de $n+1$ ecuaciones lineales con $n+1$ incógnitas $a_i$. Texto: «Se puede resolver mediante distintos métodos, que se estudian en la asignatura de Álgebra. El grado de $p_n(x)$ así construido es $n$ como máximo. Sin embargo, la resolución de este sistema de ecuaciones puede ser una tarea ardua por la regla de Cramer […], por lo que estudiaremos otra forma de determinar el polinomio de interpolación.»

Existencia y unicidad (p. 121): «Una característica importante de este polinomio es que existe y es único. La demostración de que es único es muy sencilla [nota 1: Rodríguez Marín, Perán Mazón y Gil Cid, *Fundamentos de Matemáticas. Matemáticas II*]. Para demostrar que el polinomio existe vamos a construirlo. Utilizaremos el método más popular, el de diferencias divididas de Newton, por sus ventajas frente a otros métodos.» (Nota 2: el método «está estrechamente relacionado con el método de eliminación Gaussiana».)

### Ejemplo 3.16 (pp. 121-122): recta y parábola

Datos (p. 121): $x_k = 0, 1$; $f_k = 15, 18$ (temperatura de una habitación al encender la calefacción y tras 1 hora).

Texto (p. 121): «De forma general, la ecuación de la recta que pasa por $(x_0,f_0)$ y pendiente $m$ es: $p_1(x) - f_0 = m\,(x - x_0)$.»

Resultado (p. 122): $p_1(x) = f_0 + \dfrac{f_1 - f_0}{x_1 - x_0}(x - x_0) = 15 + \dfrac{18-15}{1-0}(x-0) = 3x + 15$.

Texto (p. 122): «Si $f(x)$ es la función que describe la temperatura exacta, entonces $m$ es una aproximación a su derivada, en analogía con el polinomio de Taylor de orden 1.»

Tercer dato $(x_2, f_2) = (2, 20)$ y $p_2$ (p. 122): $p_2(x) = 3x + 15 - \tfrac12 x(x-1)$. Texto: «El último término se determina con el nuevo dato $(x_2,f_2)$. Además, $-\tfrac12$ es una aproximación a la derivada segunda de $f$. Se deja como actividad al lector que compruebe que el polinomio $p_2(x)$ es el polinomio de interpolación de los datos dados.» (Comprobado con sympy: $p_2(0)=15$, $p_2(1)=18$, $p_2(2)=20$.)

### 3.3.3 (sin número en U) Diferencias divididas (pp. 123-124)

Orden 0 (p. 123): «Se definen las diferencias divididas de orden 0 como el valor de la función en $x_k$: $f[x_k] = f_k$.»

Orden 1 (p. 123): $f[x_k, x_{k+1}] = \dfrac{f[x_{k+1}] - f[x_k]}{x_{k+1} - x_k} = \dfrac{f_{k+1}-f_k}{x_{k+1}-x_k}$.

Orden m (p. 123): «La diferencia dividida de orden $m$ se define de forma recursiva: $f[x_k,\dots,x_{k+m}] = \dfrac{f[x_{k+1},\dots,x_{k+m}] - f[x_k,\dots,x_{k+m-1}]}{x_{k+m}-x_k}$.» Texto: «Geométricamente, son una aproximación de la derivada de orden $m$ de la función $f(x)$.»

Texto (p. 123): «La forma más sencilla de calcular las diferencias divididas es en una tabla, conocida como tabla de diferencias.»

### Ejemplo 3.17 (p. 123): tabla de diferencias

Datos (p. 123): $x_k = 0, 1, 2, 4$; $f_k = 15, 18, 20, 23$ (temperatura a distintas horas).

Tabla (reconstruida con las fórmulas de U; el texto extraído está desordenado, ver §5). La **diagonal superior** (15, 3, −1/2, 1/12) es la que usa Newton:

| $x_k$ | $f[x_k]$ | $f[x_k,x_{k+1}]$ | $f[x_k,x_{k+1},x_{k+2}]$ | $f[x_k,\dots,x_{k+3}]$ |
|---|---|---|---|---|
| 0 | 15 | $\frac{18-15}{1-0}=3$ | $\frac{2-3}{2-0}=-\frac12$ | $\frac{-\frac16+\frac12}{4-0}=\frac1{12}$ |
| 1 | 18 | $\frac{20-18}{2-1}=2$ | $\frac{\frac32-2}{4-1}=-\frac16$ | |
| 2 | 20 | $\frac{23-20}{4-2}=\frac32$ | | |
| 4 | 23 | | | |

### Ejemplo 3.18 (p. 124): polinomio por Newton

Texto (p. 124): «El polinomio de interpolación por Newton se calcula a partir de las diferencias divididas mediante: $p_n(x) = f[x_0] + f[x_0,x_1](x-x_0) + f[x_0,x_1,x_2](x-x_0)(x-x_1) + \dots + f[x_0,\dots,x_n](x-x_0)(x-x_1)\cdots(x-x_{n-1})$.»

Resultado (p. 124): $p_3(x) = \dfrac{1}{12}x^3 - \dfrac34 x^2 + \dfrac{11}{3}x + 15$ (verificado: $p_3(4) = 23$).

Texto (p. 124): «Obsérvese que elegimos las diferencias de la diagonal superior.» La figura de la p. 124 muestra la gráfica de $p_3$ con los cuatro puntos.

Ampliación con un nodo nuevo (p. 124): «Con este método, el polinomio de grado $n$ se obtiene a partir del polinomio de grado $n-1$, $p_{n-1}$: $p_n(x) = p_{n-1}(x) + f[x_0,\dots,x_n](x-x_0)\cdots(x-x_{n-1})$. Por eso, al añadir un nuevo nodo no hace falta empezar todo el proceso de nuevo, basta con calcular las diferencias que nos faltan (que son las diferencias donde está $x_n$) y añadir este nuevo término.» (Idea de E 3.27-3.28.)

Grado (p. 124): «Su grado es 3, porque tenemos 4 datos.»

### Lo que U NO trae en §3.3

- No da la **fórmula del error** $f - p_n$ para la interpolación (ni su forma de Lagrange).
- No da la **forma de Lagrange del polinomio** (base de polinomios $\ell_k$); solo Newton.
- No demuestra la **unicidad** («muy sencilla», remite a un libro externo).
- No trata nodos equiespaciados (diferencias finitas) ni interpolación inversa.

---

## 2. Apartados equivalentes en S y L

Ni Stewart ni Larson tratan la interpolación polinómica por diferencias divididas (búsqueda en `stewart.txt` y `larson.txt` de «interpol», «diferencias divididas» y «Lagrange»; «Newton» sale solo como método de Newton-Raphson, que no es este tema). Lo más cercano es el **polinomio de Taylor y su residuo**, que sirve para entender el error de aproximación.

### S, §11.10 «Series de Taylor y de Maclaurin», pp. 755-756

- **p. 755** (cabecera «SECCIÓN 11.10 … 755»). Definición de polinomio de Taylor. Texto (con acentos restaurados): «Observe que $T_n$ es una polinomial de grado $n$ llamado polinomio de Taylor de $n$-ésimo grado de $f$ en $a$.» Intuición: $T_n$ se construye con derivadas en un solo punto, por eso aproxima bien cerca de $a$ y no en todo un intervalo (la idea que U contrapone en p. 120).
- **p. 756** (cabecera «756 CAPÍTULO 11»). Desigualdad de Taylor y forma de Lagrange del residuo. Texto: «Otra fórmula, que se llama forma de Lagrange del término del residuo, establece que hay un número $z$ entre $x$ y $a$ tal que $R_n(x) = \dfrac{f^{(n+1)}(z)}{(n+1)!}(x-a)^{n+1}$.» Y: «Esta versión es una generalización del teorema del valor medio (que es el caso $n = 0$).»
  - Desigualdad de Taylor (p. 756; fórmula reconstruida del texto con símbolos perdidos, comprobar en el PDF): si $|f^{(n+1)}(x)| \le M$ para $|x-a|\le d$, entonces $|R_n(x)| \le \dfrac{M}{(n+1)!}|x-a|^{n+1}$.

### L, §9.7 «Polinomios de Taylor y aproximaciones», p. 642

- **p. 642** (cabecera «642 Capítulo 9 Series infinitas»; PDF 659). Subsección «Residuo de un polinomio de Taylor». Texto: «Una técnica de aproximación es de poco valor sin una idea de su precisión.» Define el residuo $R_n(x) = f(x) - P_n(x)$ y el «error asociado» $|R_n(x)|$. Texto: «El siguiente teorema presenta un procedimiento general para estimar el residuo asociado con un polinomio de Taylor. […] el residuo dado en el teorema se llama forma de Lagrange del residuo.»
- **Teorema 9.19 (Teorema de Taylor)**, p. 642: «Si una función $f$ es derivable hasta el orden $n + 1$ en un intervalo $I$ que contiene a $c$, entonces, para cada $x$ en $I$, existe $z$ entre $x$ y $c$ tal que» $f(x) = P_n(x) + R_n(x)$, con $R_n(x) = \dfrac{f^{(n+1)}(z)}{(n+1)!}(x-c)^{n+1}$ (fórmula reconstruida del texto con símbolos perdidos).
- Texto (p. 642): «Al aplicar el teorema de Taylor, no se debe esperar poder encontrar el valor exacto de $z$. […] Se está tratando de encontrar los límites para $f^{(n+1)}(z)$ de los que se puede decir qué tan grande es el residuo $R_n(x)$.»

**Nota para el redactor**: S y L dan el error de Taylor, no el de interpolación. Si la forma de Lagrange del error de interpolación se incluye en el tema (notas adicionales), habrá que tomarla de esas notas; no está verificada aquí.

---

## 3. Ejercicios del libro de ejercicios (E), 3.21-3.28

Mapa: E 3.21-3.28 = U §3.3 (interpolación). Impresa = PDF (E). Enunciados literales (tildes restauradas; la negrita del libro no se ha conservado). Soluciones: las del libro, comprobadas con sympy.

### Ejercicio 3.21 (E p. 107) → U §3.3.2 (grado y unicidad)

Enunciado: «Razona si es cierto o falso que el polinomio interpolador que pasa por 9 puntos debe ser un polinomio exactamente de grado 8.»

Solución del libro (p. 107): «Es cierto que al tener 9 puntos, el grado del polinomio va a ser como máximo 8. Pero puede ser menor.» Contraejemplo: puntos $(a, 2a)$, $a = 1,\dots,9$; el interpolador es $2x$ (grado 1). **Respuesta: falso.**
Método: contraejemplo con puntos alineados.

### Ejercicio 3.22 (E p. 107) → U §3.3.2

Enunciado: «Razona si es cierto o falso que si se interpolan $n$ puntos tomados de la gráfica de un polinomio de grado $n$ el resultado va a ser un polinomio de grado $n$.»

Solución del libro (p. 107): «Es falso, el grado será menor o igual que $n$.» Contraejemplo: polinomio con $n$ raíces $x_1,\dots,x_n$; sus cortes con el eje $x$ dan $p\equiv0$ (grado 0).
Método: contraejemplo con raíces (puntos sobre el eje $x$).

### Ejercicio 3.23 (E p. 107) → U §3.3.2 (unicidad)

Enunciado: «Dados los siguientes datos: $f(1) = 1$, $f(3) = 2$, $f(4) = -1$, $f(5) = 0$, ¿puede haber más de un polinomio interpolador de grado 3 o menor que coincida con $f$ en 1, 3, 4 y 5?»

Solución del libro (p. 107): «No. Aunque haya más de una función que pase por estos puntos, el polinomio interpolador de grado menor o igual que 3 es único.»
Método: teorema de unicidad (no hace falta calcularlo).

### Ejercicio 3.24 (E p. 108) → U Ej. 3.18 (p. 124), diferencias divididas

Enunciado: «Determina, mediante diferencias divididas, el polinomio de grado 3 que interpola los siguientes datos: $k = 0,1,2,3$; $x_k = 1, 5, 8, 10$; $f(x_k) = 3, 11, 38, 56$.»

Solución del libro (p. 108): $f[x_0]=3$; $f[x_0,x_1]=2$, $f[x_1,x_2]=9$, $f[x_2,x_3]=9$; $f[x_0,x_1,x_2]=1$, $f[x_1,x_2,x_3]=0$; $f[x_0..x_3]=-\tfrac19$. Polinomio: $p_3(x)=3+2(x-1)+(x-1)(x-5)-\tfrac19(x-1)(x-5)(x-8)$, que desarrollado es $-\tfrac19x^3+\tfrac{23}9x^2-\tfrac{89}9x+\tfrac{94}9$.
Comprobación (sympy): coincide con $f$ en $1,5,8,10$ y la expansión es correcta. **Sin erratas.**
Método: tabla de diferencias divididas + forma de Newton; expandir solo si se pide centrado en 0.

### Ejercicio 3.25 (E pp. 109-110) → U §3.3.3 y Ej. 3.18

Enunciado (literal): «Hemos medido la velocidad de un coche al frenar, tras haber pasado 1 segundo, a los 2 segundos y a los 4 segundos (variable $t$). Los valores obtenidos aparecen en la tabla siguiente: $t$ (s): 0, 1, 2, 4; $v$ (km/h): 210, 180, 160, 140.
1) Determina el polinomio interpolador que aproxima los datos mediante diferencias divididas considerando únicamente los instantes inicial y final.
2) Determina el polinomio interpolador que aproxima los datos mediante diferencias divididas considerando todos los datos.
3) Aproxima la velocidad transcurridos 3 segundos desde que comience el frenado mediante ambos polinomios.»

Solución del libro (pp. 109-110): (1) $p_1(t) = 210 - \tfrac{35}{2}t$. (2) $f[t_0,t_1]=-30$, $f[t_1,t_2]=-20$, $f[t_2,t_3]=-10$; $f[t_0,t_1,t_2]=5$, $f[t_1,t_2,t_3]=\tfrac{10}{3}$; $f[t_0..t_3]=-\tfrac5{12}$; $p_3(t)=210-30t+5t(t-1)-\tfrac5{12}t(t-1)(t-2)$. (3) $p_1(3)=157{,}5$ km/h; $p_3(3)=147{,}5$ km/h.
Comprobación (sympy): $p_1(3)=315/2$; $p_3(t)=-\tfrac5{12}t^3+\tfrac{25}4t^2-\tfrac{215}6t+210$ y $p_3(3)=295/2=147{,}5$. **Coinciden.**
Método: diferencias con 2 nodos (recta) y con 4 nodos (cúbica); evaluar en $t=3$.
**Aviso de enunciado**: el texto dice «tras haber pasado 1 segundo, a los 2 segundos y a los 4 segundos», pero la tabla incluye $t=0$ (210 km/h), que es el que usa el apartado 1 (verificado en la imagen de E p. 109). Se ha seguido la tabla.

### Ejercicio 3.26 (E p. 110) → U §3.3.2 (existencia y unicidad)

Enunciado: «El polinomio interpolador que pasa por los puntos de la gráfica de $f(x) = \cos 2x$ en los puntos: $x = 0$, $x = \pi$, $x = 2\pi$, ¿es el polinomio idénticamente nulo?»

Solución del libro (p. 110): $f(0)=f(\pi)=f(2\pi)=1$; el interpolador es $p_2(x)=1$. **Respuesta: no.**
Comprobación: $\cos 0 = \cos 2\pi = \cos 4\pi = 1$ ✓.
Método: evaluar la función en los nodos; con esos valores el interpolador es constante.

### Ejercicio 3.27 (E pp. 110-112) → U §3.3.3 (tabla y añadir nodos)

Enunciado (literal): «Los datos a 1 de enero de los años 2004 a 2008 del INE referentes a población de España son: 2004: 43197684; 2005: 44108530; 2006: 44708964; 2007: 45200737; 2008: 46157822.
1) Con estos datos, y utilizando interpolación ¿estima la población de España el 1 de julio de 2007?
2) Si conocemos el dato adicional de que la población el 1 de enero de 2009 es 46745809, ¿cuál sería la población estimada de España el 1 de julio de 2007?»

Solución del libro (pp. 110-112): (1) polinomio de grado 4 con $f[x_0,x_1]=910846$, $f[x_0,x_1,x_2]=-155206$, $f[x_0..x_3]=\tfrac{201751}{6}\approx33625{,}17$, $f[x_0..x_4]=\tfrac{62037}{4}=15509{,}25$; $p_4(2007{,}5)\approx45\,570\,702$ (redondeado, porque es un número de personas). (2) Se añade el nodo 2009 y se calculan 5 diferencias nuevas; $f[x_0..x_5]=-14838{,}375$; $p_5(2007{,}5)\approx45\,619\,391$.
Comprobación (sympy, exacta): $p_4(2007{,}5)=45\,570\,702{,}27$ ✓; $p_5(2007{,}5)=45\,619\,390{,}68$ ✓; la diferencia de orden 5 es $-118707/8=-14838{,}375$ ✓; $p_5-p_4=-14838{,}375\,(x-2004)\cdots(x-2008)$ ✓.
Método: tabla de diferencias con $x$ = año; evaluar en $2007{,}5$ con la forma de Newton sin desarrollar; añadir un nodo = calcular solo las diferencias que contienen el nodo nuevo.
Nota de cálculo: el libro toma $x - 2004$ (años desde 2004), así que $2007{,}5$ corresponde a $x-2004 = 3{,}5$.

### Ejercicio 3.28 (E p. 113) → U §3.3.3 (qué diferencias se calculan)

Enunciado (literal): «Supón que en el ejercicio anterior en lugar de proporcionarte el dato de la población en 2009 te dan el dato de la población en 2003. A partir de la tabla de diferencias divididas de los años 2004 a 2008. ¿Cuántas diferencias divididas de orden mayor o igual que 1 debes calcular para estimar la población en 2007.5? ¿Y si te proporcionasen la población en 2005.5?»

Solución del libro (p. 113): con el dato 2003 (nodo en un extremo): **5** diferencias nuevas, aprovechando **10** de la tabla. Con el dato 2005,5 (nodo intermedio): **11** nuevas, aprovechando **4**.
Comprobación (conteo, sin sympy): con 6 nodos hay 15 diferencias de orden ≥ 1 (rangos contiguos de longitud ≥ 2). Si el nodo nuevo está en un extremo, los 10 rangos que no lo contienen son los del conjunto antiguo: 5 nuevas y 10 reutilizables ✓. Si está entre 2005 y 2006, los rangos que no lo contienen son 4 ([0,1], [3,4], [4,5], [3,5]): 4 reutilizables y 11 nuevas ✓. **Coinciden con el libro.**
Método: contar qué diferencias contienen el nodo nuevo (las demás se reutilizan).

---

## 4. Preguntas de examen (X) sobre interpolación

Localizadas en `fuentes_txt/indice_examenes_1..4.md` (etiqueta «3.3» o «3.3 interpolación») y comprobadas en el PDF renderizado (PyMuPDF, 110 dpi, leídas como imagen). Páginas PDF.

### X p. 5 · Feb 2010, 2.ª semana, Ing. Eléctrica, Ej. 5 (3 puntos) — **verificado**
Enunciado: «Determine, por diferencias divididas, el polinomio de grado 3 que aproxima los siguientes datos: $x_k = -2, 0, 1, 3$; $f(x_k) = 0, 2, 3, 5$.»
Solución impresa: $f[x_0,x_1]=f[x_1,x_2]=f[x_2,x_3]=1$; de orden 2 y 3, todo 0; $p_3(x)=x+2$.
Comprobación (sympy): $p_3(x)=x+2$ ✓. **Sin erratas.**
Receta: si las diferencias de orden 2 y 3 son nulas, los datos están alineados y el polinomio es de grado 1.

### X p. 57 · Feb 2015, Modelo B, Ej. 5 — **verificado**
Enunciado: polinomio de grado 3 por diferencias divididas para $(1,3)$, $(5,11)$, $(8,38)$, $(10,56)$. (Igual que E 3.24.)
Solución impresa: $f[x_0,x_1]=2$, $f[x_1,x_2]=9$, $f[x_2,x_3]=9$; $f[x_0..x_2]=1$, $f[x_1..x_3]=0$; $f[x_0..x_3]=-\tfrac19$; $p_3(x)=3+2(x-1)+(x-1)(x-5)-\tfrac19(x-1)(x-5)(x-8)=-\tfrac19x^3+\tfrac{23}9x^2-\tfrac{89}9x+\tfrac{94}9$. Comprobado ✓.

### X pp. 65-66 · Feb 2016, Modelo B, Ej. 5 (3 puntos) — **verificado, con erratas de rotulado**
Enunciado (p. 65): «Se consideran los siguientes valores de una función: $x = 1, 2, 3$; $f(x) = 31, 26, 43$. (a) Calcule $\int_1^3 f$ por la regla del trapecio. (b) Calcule $\int_1^3 f$ por la regla de Simpson con 3 nodos igualmente espaciados. (c) La función $g(x) = 11x^2 - 38x + 58$ verifica $f(1)=g(1)$, $f(2)=g(2)$, $f(3)=g(3)$. Calcule $\int_1^3 g$ y compárelo con los valores obtenidos en los apartados anteriores. Justifique a qué se debe la diferencia.»
Solución impresa: (a) $\frac{3-1}{2}\left(\frac{31+43}{2}+26\right)=63$ ✓. (b) $\frac{3-1}{6}(31+4\cdot26+43)=\frac{178}{3}\approx59{,}333$ ✓. (c) $\int_1^3 g=\frac{178}3\approx59{,}333$ ✓ (verificado: $g(1)=31$, $g(2)=26$, $g(3)=43$).
Justificación impresa (p. 66): el trapecio aproxima por segmentos (grado 1); Simpson aproxima por un polinomio de grado 2; como $g$ es de grado 2 y coincide con los datos, coincide con Simpson.
**Erratas**: en (a) y (b) de la solución se escribe «$f(0)=31$, $f(1)=26$, $f(3)=43$»; los nodos son $1,2,3$, así que debe ser $f(1)=31$, $f(2)=26$, $f(3)=43$. Los resultados numéricos son correctos.

### X p. 85 · Sep 2017, Modelo A, pregunta corta 3 (1 punto) — relacionada (Simpson = interpolación de grado 2) — **verificado**
Enunciado: «Sea $f$ una función continua tal que $f(0) = 1$, $f(1) = -2$, $f(2) = 0$. Aproxime el valor de la integral $I = \int_0^2 f(x)\,dx$ con el método de Simpson.»
Nota impresa: «En el enunciado ponía $f(3)=0$ y era una errata, debía ser $f(3)=0$.» (**Redacción contradictoria**: la solución usa $f(2)=0$, que es lo coherente con el enunciado.)
Solución impresa: «Simpson se basa en la interpolación en tres puntos igualmente espaciados.» $I\approx(2-0)\dfrac{f(0)+4f(1)+f(2)}{6}=2\cdot\dfrac{1-8+0}{6}=-\dfrac73$ ✓.
**Erratas**: la línea de Simpson escribe $\int_1^2 f$ en lugar de $\int_0^2 f$.

### X p. 100 · Electrónica 1, Ej. 5 (3 puntos) — **enunciado verificado; solución impresa sin valores numéricos**
Enunciado: «Encuentre una función $f$ cuya gráfica pase por los puntos $(0,15)$, $(1,18)$, $(2,20)$ y $(4,23)$. Aproxime $\int_0^2 f(x)\,dx$ utilizando el método del trapecio y el método de Simpson.»
Solución impresa (p. 100): «Son los datos del Ejemplo 3.17 del texto base, así que el polinomio es el que aparece en el Ejemplo 3.18.» No da las integrales.
**Cálculo propio (no es solución impresa)**: $p_3(x)=\tfrac1{12}x^3-\tfrac34x^2+\tfrac{11}3x+15$; $\int_0^2 p_3 = \tfrac{107}3\approx35{,}67$. Trapecio simple: $\tfrac{2}{2}(15+20)=35$. Trapecio compuesto ($h=1$, nodos 0, 1, 2): $\tfrac12(15+2\cdot18+20)=\tfrac{71}2=35{,}5$. Simpson en $0,1,2$: $\tfrac26(15+4\cdot18+20)=\tfrac{107}3\approx35{,}67$.

### X p. 101 · Electrónica 2, pregunta corta 3 (1 punto) — **verificado, con errata**
Enunciado: «De una función $f$ se sabe que $f(0)=1$, $f(2)=3$ y $f(4)=2$. Aproxime el valor de $f(8)$ utilizando el polinomio interpolador.»
Solución impresa: $f[x_0,x_1]=1$, $f[x_1,x_2]=-\tfrac12$, $f[x_0,x_1,x_2]=-\tfrac38$; $p(x)=1+x-\tfrac38x(x-2)$; «El valor aproximado de $f(3)$ viene dado por $p(8)=1+8-18=-9$.»
Comprobación (sympy): $p(8)=-9$ ✓; $p(0)=1$, $p(2)=3$, $p(4)=2$ ✓.
**Errata**: en la última línea pone «$f(3)$» en lugar de $f(8)$.

### X p. 107 · Electrónica 4, Ej. 5 (3 puntos) — **verificado; solución impresa incompleta**
Enunciado (p. 107): «De una función $f$ se sabe que $f(0)=1$, $f(2)=3$ y $f(4)=2$. (a) Aproxime el valor de $f(1)$ utilizando el polinomio interpolador. (b) Aproxime el valor de $\int_0^4 f(x)\,dx$ mediante la fórmula de Simpson. (c) Compruebe que obtiene el mismo resultado que en el apartado anterior si integra el polinomio interpolador entre 0 y 4.»
Solución impresa: $p(x)=1+x-\tfrac38x(x-2)$; (b) Simpson $\frac{4-0}{6}(1+4\cdot3+2)=10$ ✓; (c) $\int_0^4p=10$ ✓.
**Hueco**: la solución impresa **no da el valor de $f(1)$** pedido en (a). Cálculo propio: $p(1)=1+1-\tfrac38\cdot1\cdot(-1)=\tfrac{19}8=2{,}375$.

### X pp. 119-121 · Examen 4, Ej. 5 (3 puntos) — **verificado**
Enunciado (p. 119): «Determínese un polinomio de grado 3 que aproxime a $f(x)=\ln x$ a partir de los valores de la función $\ln x$ en los nodos 1,3; 1,4; 1,5 y 1,6. Para ello, utilícense diferencias divididas y 4 cifras significativas. A partir de este polinomio, estímese el valor de $\ln 1{,}47$.»
Solución impresa (pp. 120-121): $f[x_0,x_1]=0{,}741$, $f[x_1,x_2]=0{,}69$, $f[x_2,x_3]=0{,}645$; $f[x_0,x_1,x_2]=-0{,}255$, $f[x_1,x_2,x_3]=-0{,}225$; $f[x_0..x_3]=0{,}1$; $p_3(x)\approx0{,}1x^3-0{,}675x^2+2{,}017x-1{,}438$; $p_3(1{,}47)=0{,}3853293\approx0{,}3853$ (calculado con la forma de Newton sin desarrollar, p. 121).
Comprobación (sympy): diferencias ✓; $p_3(1{,}47)=0{,}385300$ frente a $\ln 1{,}47=0{,}385262$: error $\approx 4\cdot10^{-5}$ (el libro no da cota de error).

### X p. 151 · Feb 2019, 1.ª semana, Ej. 5 (3 puntos) — **verificado, con erratas menores**
Enunciado (p. 151): «Datos $f(1)=2$, $f(3)=3$, $f(4)=2$, $f(8)=10$. (a) Aproxime $f(2)$ con el polinomio interpolador (1,5 puntos). (b) Usando el valor de $f(2)$ obtenido, aproxime $\int_1^4 f$ con la fórmula compuesta de Simpson en dos subintervalos (1,5 puntos).»
Solución impresa (p. 151): $f[x_0,x_1]=\tfrac12$, $f[x_1,x_2]=-1$, $f[x_2,x_3]=2$; $f[x_0,x_1,x_2]=-\tfrac12$, $f[x_1,x_2,x_3]=\tfrac35$; $f[x_0..x_3]=\tfrac{11}{70}$; $p(x)=2+\tfrac12(x-1)-\tfrac12(x-1)(x-3)+\tfrac{11}{70}(x-1)(x-3)(x-4)$; $f(2)\approx p(2)=\tfrac{116}{35}\approx3{,}3142$.
Comprobación (sympy): diferencias ✓; $p(2)=\tfrac{116}{35}=3{,}31428\ldots$, es decir **$\approx 3{,}3143$** (el libro trunca a 3,3142).
**Erratas**: (i) en el desarrollo, el término de $f[x_0,\dots,x_3]$ aparece sin la $f$ («$+[x_0,x_1,x_2,x_3]\ldots$»); (ii) $116/35\approx3{,}3143$ (no 3,3142).
Nota (p. 151): el enunciado del apartado (b) tiene una errata («Usando el valor de $f(2)$ obtenido»); el libro admite cualquier planteamiento razonable. La Simpson compuesta de la p. 152 es integración numérica (§6): no revisada en detalle.

---

## 5. Faltas o dudas

1. **Forma de Lagrange del error de interpolación** (cronograma, «notas adicionales» del módulo III): **no localizada**. No está en U §3.3 (pp. 119-124), ni en S (§11.10), ni en L (§9.7). Las notas adicionales no están en `fuentes_txt/` ni en `E:\UNED\CALCULO` (búsqueda de «nota», «landau» y «adicional» sin resultados). Hace falta el documento para verificar enunciado y página.
2. **Equivalentes en S/L**: no hay tratamiento de interpolación polinómica en Stewart ni en Larson. Solo se cita el residuo de Taylor (S p. 756; L p. 642) como analogía.
3. **U §3.3 incompleto**: la unicidad se afirma sin demostración («muy sencilla», remite a un libro externo, p. 121); no hay fórmula del error de interpolación; no hay forma de Lagrange del polinomio.
4. **Tabla de U (Ej. 3.17, p. 123)**: el texto extraído está desordenado; se ha reconstruido con las fórmulas y verificado con sympy. Candidatas a recorte para el HTML (`herramientas/extraer_figura.py`): la figura de la p. 124 (gráfica de $p_3$) y la Figura 3.4 de E p. 109 (cuatro puntos y su polinomio interpolador).
5. **E 3.25**: el enunciado menciona los instantes 1, 2 y 4 s, pero la tabla incluye $t=0$. Se ha seguido la tabla (verificado en la imagen de E p. 109).
6. **E 3.27 (solución impresa)**: «33625.1Û6» es el fraccionario $201751/6$ mal extraído del texto; verificado.
7. **X p. 66**: rotulado erróneo de los nodos en (a) y (b) (ver §4).
8. **X p. 85**: nota contradictoria sobre $f(2)$/$f(3)$ y $\int_1^2$ en lugar de $\int_0^2$ (ver §4).
9. **X p. 100**: la solución impresa no da números; los valores de §4 son cálculo propio.
10. **X p. 107**: falta el valor de $f(1)$ en la solución impresa; $p(1)=19/8$ es cálculo propio.
11. **X p. 101**: «$f(3)$» en lugar de $f(8)$ en la solución.
12. **X p. 151**: $116/35\approx3{,}3143$ (impreso 3,3142); falta una $f$ en el desarrollo; la Simpson compuesta de la p. 152 no está revisada.
13. **Páginas de X vistas como imagen**: 5, 57, 65, 66, 85, 100, 101, 107, 119, 120, 121 y 151. La p. 152 no se ha visto.
14. **Índice de X**: `indice_examenes_3.md` atribuye a X p. 119 el rango «119-121 (continúa fuera del rango)»; se confirma que el enunciado está en p. 119 y la solución en pp. 120-121.
15. Las páginas de U y E citadas se han comprobado en el texto extraído; las de S y L, con la cabecera de página (S: pp. 755-756; L: p. 642).
