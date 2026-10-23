# Ejemplos interactivos con three.js — catálogo por tema

Estado: **infraestructura montada** (octubre 2026: `assets/three/`, `assets/interactivos.js|css`, `assets/escenas/`, página `pruebas/interactivo_demo.html`); probada en navegador (funciona); falta el primer interactivo real. Ningún tema usa todavía three.js (el del 2.1 es SVG+JS propio). Revisados los 20 temas hechos (1.1–5.3). Regla vigente para los temas nuevos: ver `CLAUDE.md`, regla 12.

## 1. Criterio: cuándo merece la pena

Un interactivo se añade solo si **mueve un parámetro y deja ver algo que la figura estática no enseña**. Prioridad:

- **Alta:** concepto 3D (superficies, planos tangentes, gradiente, curvas de nivel) o dinámico donde el estudiante «ve» el teorema al arrastrar (Rolle/TVM, Taylor, Newton).
- **Media:** definiciones ε-δ / ε-N, interpolación, implícita, sólidos de revolución.
- **Baja / no hacer:** temas puramente algebraicos (reglas de derivación, orden en ℝ, tablas de criterios). Ahí el SVG o el recorte del libro bastan.

three.js es el motor porque la mitad del curso (Temas 4-6) es 3D. En 2D se usa la misma infraestructura con `OrthographicCamera` (un solo motor, un solo estilo). Un interactivo **nunca sustituye** al ejercicio resuelto ni a la figura del libro; se coloca justo después de la explicación del concepto, y no entra en la chuleta.

## 2. Infraestructura común (a crear una vez)

```
assets/three/three.bundle.js    three + OrbitControls en un único script clásico (global THREE), vendorizado
assets/interactivos.js          helpers: escena, ejes, malla de superficie z=f(x,y), curvas de nivel, sliders, tema claro/oscuro
assets/interactivos.css         marco .interactivo, sliders, leyenda, versión impresa
assets/img/int_<nombre>.png     captura estática (se muestra al imprimir y como fallback)
```

Decisiones técnicas (para que no se rompa lo que ya funciona):

1. **Offline y sin módulos ES.** Los `import` de módulos fallan al abrir un HTML por `file://`. Se genera una vez un bundle clásico (esbuild/IIFE, `window.THREE`) y se copia a `assets/three/`, igual que KaTeX. Sin CDN.
2. **Carga perezosa:** el script de three solo se descarga y el `<canvas>` solo se crea cuando la figura entra en pantalla (`IntersectionObserver`). Los temas pesan ~100 KB y no deben ralentizarse.
3. **Marcado en el tema:**
   ```html
   <figure class="interactivo" data-escena="plano-tangente" data-params='{"f":"x*x+y*y"}'>
     <noscript><img src="../assets/img/int_plano_tangente.png" alt="…"></noscript>
     <figcaption>Arrastra para girar; mueve el punto con los sliders. <span class="src" …></span></figcaption>
   </figure>
   ```
   Con `src="propia"` si no hay equivalente en los libros (o la figura del libro en que se inspira).
4. **Tema claro/oscuro:** los colores se leen de las variables CSS (`getComputedStyle`) y se repintan al cambiar `data-theme`.
5. **Impresión/PDF:** `@media print` oculta el canvas y muestra la captura estática (`break-inside: avoid`). `exportar_pdf.py` no ejecuta WebGL de forma fiable.
6. **Móvil y accesibilidad:** táctil con `OrbitControls`; sliders con `<input type="range">` y etiqueta; `prefers-reduced-motion` desactiva animaciones automáticas; descripción textual en `aria-label`; si no hay WebGL se ve la captura.
7. **Matemáticas en etiquetas:** KaTeX en HTML superpuesto (no texto dentro del canvas).
8. **Rigor:** la función dibujada y los valores mostrados (pendiente, polinomio, gradiente) se calculan con las mismas fórmulas del tema; se contrastan con sympy antes de publicar. Mismo criterio de «sin erratas» (regla 8 bis).
9. **Rendimiento:** una escena por figura, máx. 2-3 por tema, `devicePixelRatio ≤ 2`, parar el render cuando el canvas sale de pantalla.

## 3. Catálogo por tema (ya hechos)

Leyenda: ★★★ imprescindible · ★★ útil · ★ opcional · — no.

### Módulo I — El paso al límite
| Tema | Prio. | Interactivo propuesto (ubicación) |
|---|---|---|
| 1.1 Espacio ℝ | — | Nada. Opcional ★: recta real con zoom para ver densidad de ℚ (§ Propiedad arquimediana y densidad). |
| 1.2 Sucesiones | ★★ | **Tubo ε-N:** slider de ε dibuja la banda $(L-\varepsilon,L+\varepsilon)$ y marca el primer $N$ desde el que todos los términos caen dentro (§ Límite de una sucesión). Elegir entre $1/n$, $(-1)^n/n$, $\sqrt[n]{n}$. Segundo: sucesión monótona acotada que «se aprieta» (§ Monótonas). |
| 1.3 Series | ★★ | **Sumas parciales vs. suma:** términos $a_n$ como barras y $S_n$ como curva que converge/diverge; selector geométrica / armónica / $1/n^2$ / alternada (§ Serie, suma parcial). Segundo ★: criterio de comparación con áreas bajo $1/x^p$. |
| 1.4 Límites y continuidad | ★★ | **ε-δ en una función:** arrastrar δ y ver si la gráfica queda dentro de la banda de ε (§ Límite de una función). **Bisección:** botón «paso» que parte el intervalo (§ Bisección). |

### Módulo II — Funciones derivables
| Tema | Prio. | Interactivo propuesto |
|---|---|---|
| 2.1 Derivada | ★★★ | **Secantes → tangente:** slider de $h\to0$; la pendiente de la secante se acerca a $f'(a)$ y se ve cuándo no existe (lateral distinto, |x|, cúspide) (§ Interpretación geométrica; § Derivadas laterales). |
| 2.2 Reglas | ★ | Solo opcional: $f$ y $f'$ superpuestas, para ver que $f'$ es «la pendiente de f». |
| 2.3 L'Hôpital | ★ | Cociente de dos curvas que valen 0 en $a$: zoom hacia $a$ muestra que el cociente de valores ≈ cociente de pendientes (§ La regla de L'Hôpital). |
| 2.4 Newton y punto fijo | ★★★ | **Newton paso a paso** (tangente → corte con el eje) y **telaraña de punto fijo** con $g'(x^*)$ variable: se ve cuándo converge, oscila o diverge (§§ Newton, Punto fijo). |
| 2.5 Rolle y valor medio | ★★★ | **TVM:** secante entre $a,b$ y tangente que se mueve con $c$; los $c$ válidos se iluminan. Rolle como caso $f(a)=f(b)$ y contraejemplos (sin continuidad / sin derivabilidad) (§§ Rolle, valor medio). |

### Módulo III — Aplicaciones de la derivada
| Tema | Prio. | Interactivo propuesto |
|---|---|---|
| 3.1 Taylor | ★★★ | **Polinomio de Taylor de grado $n$** (slider $n$, centro $a$) frente a $f$ ($e^x$, $\sin x$, $\ln(1+x)$) y banda del resto de Lagrange (§ Polinomio de Taylor; § Resto). |
| 3.2 Series de Taylor | ★★ | **Radio de convergencia:** $1/(1+x^2)$ — la serie diverge fuera de $(-1,1)$ aunque $f$ sea suave; se ven las sumas parciales explotar (§ Radio de convergencia). |
| 3.3 Interpolación | ★★★ | **Nodos arrastrables:** el polinomio interpolador se recalcula; fenómeno de Runge con nodos equiespaciados frente a otros; muestra del error de Lagrange (§§ Qué es interpolar, Cuánto se equivoca). |
| 3.4 Optimización | ★★ | Problemas con forma 3D: caja/lata de volumen fijo que cambia de dimensiones mientras una gráfica $A(x)$ marca el mínimo (§ Problemas de optimización). Puntos críticos: tangente horizontal sobre la gráfica (★). |
| 3.5 Concavidad | ★★ | Tangente que se desliza: queda por debajo/encima de la curva según $f''$; marca de inflexión (§ Cómo decidirlo con derivadas, § Puntos de inflexión). |

### Módulo IV — Funciones de varias variables
| Tema | Prio. | Interactivo propuesto |
|---|---|---|
| 4.1 Espacio $\mathbb R^n$ | ★★★ | **Vectores 3D:** dos vectores arrastrables → producto escalar, norma, ángulo. **Coordenadas polares/cilíndricas/esféricas:** sliders $(r,\theta,\varphi)$ mueven un punto y muestran $(x,y,z)$ (§§ Producto escalar, Coordenadas). Discos abiertos/cerrados (★). |
| 4.2 Funciones de varias variables | ★★★ | **Superficie $z=f(x,y)$ + curvas de nivel** (cortes con planos $z=c$ que bajan hasta el plano XY). **Límites por caminos:** elegir recta/parábola de aproximación y ver los valores distintos de $\frac{xy}{x^2+y^2}$ en el origen (§§ Gráfica y curvas de nivel, Límite). |
| 4.3 Derivadas parciales | ★★★ | **Cortes $x=x_0$, $y=y_0$ de la superficie** con su tangente (= parciales). **Gradiente:** flecha en el plano de nivel, ortogonal a la curva de nivel y dirección de máximo crecimiento; derivada direccional con un slider de ángulo (§§ Derivada parcial, Gradiente, Derivada direccional). |

### Módulo V — Aplicaciones de la diferencial
| Tema | Prio. | Interactivo propuesto |
|---|---|---|
| 5.1 Diferencial | ★★★ | **Plano tangente** en un punto arrastrable; zoom hacia el punto muestra que superficie y plano se confunden. Contraejemplo de función con parciales pero no diferenciable (plano «falso» que no aproxima) (§§ Idea, Función diferenciable y plano tangente). |
| 5.2 Cadena y valor medio | ★★ | **Curva $\gamma(t)$ sobre la superficie:** $\frac{d}{dt}f(\gamma(t))=\nabla f\cdot\gamma'$ con el gradiente y el vector velocidad dibujados (§ Regla de la cadena). TVM en dos variables: segmento y punto intermedio (★). |
| 5.3 Función implícita | ★★ | **Curva de nivel $F(x,y)=c$** con su tangente de pendiente $-F_x/F_y$; marcar puntos donde $F_y=0$ y la curva no es gráfica (§§ Teorema, Pendiente de una curva de nivel). |

## 4. Previsión para los temas que faltan (se hacen al crearlos)

| Tema | Prio. | Interactivo |
|---|---|---|
| 5.4 Extremos en varias variables | ★★★ | Superficies con máximo, mínimo y **punto de silla** con el plano tangente horizontal; signo de la Hessiana → forma local. |
| 5.5 Extremos condicionados / Lagrange | ★★★ | Curvas de nivel de $f$ tangentes a la restricción $g=0$ ($\nabla f\parallel\nabla g$); el punto sobre la restricción se mueve y se ve el valor de $f$. |
| 6.1-6.2 Riemann y teoremas fundamentales | ★★ | Sumas de Riemann (inferior/superior/punto medio) con slider de particiones; el área acumulada $F(x)=\int_a^x f$ y su derivada (TFC). |
| 6.3-6.4 Técnicas y numérica | ★ | Trapecios/Simpson comparados con el área exacta. |
| 6.5 Integrales impropias | ★★ | Área hasta $b\to\infty$ para $1/x^p$: se ve cuándo se estabiliza. |
| Sólidos de revolución (si aparecen en 6.x) | ★★★ | Girar una región alrededor de un eje: discos/arandelas/capas. |

## 5. Orden de implementación sugerido

1. Infraestructura (§2) con **una** escena de prueba: plano tangente (5.1).
2. Los ★★★ de los temas ya hechos: 4.2, 4.3, 5.1, 2.5, 2.4, 3.1, 3.3, 2.1, 4.1.
3. Los ★★ cuando haya tiempo de repaso.
4. Los temas nuevos los incluyen desde el redactor (regla 12 de `CLAUDE.md`).

Cada tema retocado se publica con su commit propio (`CLAUDE.md` §4b).

## 6. Pendiente de decidir

- Si se quiere conservar el uso offline por `file://` (por eso el bundle clásico) o basta con GitHub Pages (permitiría `importmap` + módulos).
- Tamaño admisible del bundle (three + OrbitControls minificado ≈ 0,7 MB; con carga perezosa solo se paga en los temas con interactivos).
- Licencia: three.js es MIT (incluir `LICENSE` en `assets/three/`).


## 6. Infraestructura montada (cómo se usa)

- **three r147** (`assets/three/three.min.js` + `OrbitControls.js`, clásicos, MIT; licencia en `LICENSE-three.txt`). Se eligió r147 porque es la última con builds clásicos y sin necesidad de bundler (no hay node/npm en el equipo).
- **Motor:** `assets/interactivos.js` (carga perezosa, render bajo demanda, tema claro/oscuro, WebGL ausente → mensaje). Helpers: `ejes`, `superficie`, `curva`; en el contexto de cada escena: `slider`, `lectura`, `alCambiarTema`.
- **Escenas:** una por fichero en `assets/escenas/<nombre>.js`, registrada con `Interactivos.registrar(nombre, function(ctx){…})`. La escena `demo-superficie` sirve de plantilla.
- **En el tema:** `<link rel="stylesheet" href="../assets/interactivos.css">`, `<script defer src="../assets/interactivos.js">` y `<figure class="interactivo" data-escena="…" data-params='{…}'>` con `<figcaption>` y su `src`.
- **Impresión:** en `@media print` se oculta el lienzo y se muestra `.int-static` (añadir `<img class="int-static" src="../assets/img/int_<nombre>.png">`; la captura aún se hace a mano).
- **Herramientas:** sympy 1.14 instalado en el usuario (`~/.local`, sin pip) para verificar valores.
- **Pendiente:** primera escena real (propuesta: 4.2 o 4.3), flujo para generar las capturas estáticas.

### Escenas hechas (octubre 2026)
- `coordenadas` en el tema 4.1 (polares, cilíndricas y esféricas con φ desde el plano xy como en U; Ej. 4.8 comprobado); `vectores` en el tema 4.1 (u, v con sliders: u·v, normas, ángulo con arco, proyección; helper `H.flecha`; u=(2,1,1), v=(1,2,0) → 4, 43,09°, comprobado); `gradiente` en el tema 4.3 (curva de nivel, flecha del gradiente y de v, plano vertical con la derivada direccional; Ej. 4.29 da 0,707; H.nivel compartido con superficie-nivel); `parciales` en el tema 4.3 (cortes y=b, x=a de la superficie con sus tangentes; helper `H.tubo`; parciales analíticas comprobadas); `superficie-nivel` en el tema 4.2 (primer 3D: superficie, plano z=c, traza y curva de nivel por marching squares; funciones x²+y²+1, x²−y², campana, paraboloide elíptico); `radio-convergencia` en el tema 3.2 (sumas parciales de 1/(1+x²), 1/(1−x), ln(1+x), eˣ, sen x con rectas x=±R; coeficientes y S₁₀ comprobados con sympy/Python); `concavidad` en el tema 3.5 (tangente deslizante, inflexiones por bisección sobre f″; funciones x³, x⁴/4−x², sen x, x⁴ comprobadas con sympy); `interpolacion` en el tema 3.3 (nodos arrastrables vía `ctx.arrastre`, Runge con nodos equiespaciados y de Chebyshev; errores 1,9156 y 0,109 con 11 nodos, comprobados con sympy/Python); `taylor` en el tema 3.1 (grado n, centro a y resto en un punto; eˣ, sen, cos, ln(1+x); valores de las derivadas comprobados con sympy); `secante-tangente` en el tema 2.1 (sustituye al SVG+JS inicial); `newton` y `telarana` en el tema 2.4; `tvm` (con `"modo":"rolle"` para Rolle) en el 2.5. Son 2D (`data-params {"dim":2}`: cámara ortográfica, sin giro), con helpers `cinta`, `punto`, `grafica`, `ejes2D` y, en el contexto, `vista` y `selector`.
- Valores comprobados con sympy (raíces, puntos fijos, ciclo 0↔1 de x³−2x+2, Newton de ∛x → −2x). Probadas en Chromium headless (WebGL por software).
- Falta la captura estática (`.int-static`) para el PDF.
- **Zoom y desplazamiento en 2D** (motor): rueda del ratón, pellizco táctil, arrastrar para mover, doble clic o botón «Restablecer vista». El grosor de líneas, trazos y puntos se mantiene en píxeles al hacer zoom (`reescalar(f)` en `cinta` y `punto`; todo objeto 2D nuevo debe definirlo). Se puede acercar hasta ×25 y alejar hasta ×4 (las escenas dibujan una región 4 veces más ancha y alta que la vista inicial: usar `W(v)` como en `newton.js`); el movimiento queda dentro de lo dibujado.
