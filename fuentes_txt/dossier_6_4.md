# Dossier Tema 6.4: Integración numérica

Páginas: U impresa = PDF + 2; E impresa = PDF; S = cabecera impresa de `stewart.txt`; L impresa = PDF − 17. Verificadas por el agente de fuentes en los .txt y en imagen (X). Los símbolos del texto extraído de U están degradados: las fórmulas de abajo están reconstruidas y comprobadas numéricamente; **el resolutor/redactor debe confirmar en imagen (render de la página PDF de U) las fórmulas de Teor. 6.3, 6.4 y Def. 6.8 (pp. 268-270) y el Ej. 6.32 (p. 267).**

## 0. Rangos de U §6.4 (pp. 263-270; §6.5 empieza en p. 271)
| Apartado | Pág. | Contenido |
|---|---|---|
| 6.4.1 Motivación | 263 | aproximar ∫ cuando no hay primitiva o solo se conocen valores de f |
| 6.4.2 Idea | 264 | se apoya en: (1) integral = área; (2) aditividad ∫ₐᵇ = ∫ₐᶜ + ∫꜀ᵇ. Fórmulas simples y luego dividir el intervalo |
| Rectángulos | 264-266 | Def. 6.3 (simples), Ej. 6.29 (p.265), Def. 6.4 (compuestas), Ej. 6.30 (p.266) |
| Trapecio | 266-267 | idea (recta por (a,f(a)),(b,f(b))), Def. 6.5, Ej. 6.31, Def. 6.6 (compuesta), Ej. 6.32 |
| Simpson | 268-269 | Def. 6.7 (simple), Def. 6.8 (compuesta), Ej. 6.33 (pp. 268-269) |
| Errores | 269-270 | Teor. 6.3 (trapecio, p.269), Ej. 6.34 (pp.269-270), Teor. 6.4 (Simpson, p.270), Ej. 6.35 (p.270) |

## 1. U (fórmulas y citas)
- p.263: «…en muchos casos no es posible calcular una primitiva de f a la que aplicar la Regla de Barrow o porque solamente conocemos los valores de f en ciertos puntos del intervalo [a, b].»
- Def. 6.3 (p.264) rectángulos: izq. f(a)(b−a); der. f(b)(b−a); central f((a+b)/2)(b−a).
- Def. 6.4 (p.266): n subintervalos, h=(b−a)/n, xₖ=a+kh. Izq.: h·Σₖ₌₀ⁿ⁻¹ f(xₖ); der.: h·Σₖ₌₁ⁿ f(xₖ); central: h·Σₖ₌₀ⁿ⁻¹ f((xₖ+xₖ₊₁)/2).
- Def. 6.5 (p.267) trapecio: ∫ₐᵇ f ≈ (f(a)+f(b))/2·(b−a) (área de un trapecio de altura b−a y bases f(a), f(b)).
- Def. 6.6 (p.267) compuesto: ≈ (h/2)(f₀ + 2f₁ + … + 2fₙ₋₁ + fₙ); regla mnemotécnica «(h/2)(Extremos + 2·Centrales)».
- Def. 6.7 (p.268) Simpson: ≈ (b−a)/6·(f(a) + 4f((a+b)/2) + f(b)) (parábola por los tres puntos).
- Def. 6.8 (p.268) Simpson compuesta: en U, **n = número de subintervalos de longitud h=(b−a)/n, a cada uno se le aplica Simpson** (nodos xₖ=a+kh/2, k=0..2n): ≈ (h/6)(f₀ + 4f₁ + 2f₂ + 4f₃ + … + 2f₂ₙ₋₂ + 4f₂ₙ₋₁ + f₂ₙ); regla «(h/6)(Extremos + 2·Pares + 4·Impares)». (En S y L, n = número de pedazos, par, y la fórmula es (Δx/3)[1,4,2,…,4,1]; la cota 2880m⁴ de U equivale a 180n⁴ con n=2m. En el HTML explicar con la convención de U sin contrastar fuentes.)
- Teor. 6.3 (p.269): error trapecio compuesto en m subintervalos: ε ≤ (b−a)³·M₂/(12m²), con |f″|≤M₂ en [a,b].
- Teor. 6.4 (p.270): error Simpson compuesta en m subintervalos: ε ≤ (b−a)⁵·M₄/(2880m⁴), con |f⁽⁴⁾|≤M₄.
- Ejemplos: 6.29 (p.265): ∫₁^{5/2}(x³−3,3x²+3x)dx, exacta 1,303125; izq. 1,05, der. 3,75, central 0,75. 6.30 (p.266) con 3 subintervalos: 0,975; 1,875; 1,242. 6.31 (p.267): trapecio 2,4. 6.32 (p.267): trapecio con 2 subintervalos 1,5773 (≈1,577). 6.33 (pp.268-269): tabla x=1;1,1;…;1,6, f=2;2,2;2,3;2,1;2,4;2,3;1,9; Simpson simple (f(1)+4f(1,3)+f(1,6))/6·0,6 = 1,23; compuesta con 3 subintervalos 1,3233 (con sus datos). 6.34 (pp.269-270): ∫₀¹e^{−x²}dx, f″=2e^{−x²}(2x²−1), |f″|≤2; m=10: ε≤1/600; m=20: ε≤1/2400. 6.35 (p.270): |f⁽⁴⁾|≤50, ∫₀²f con error<0,0001: 2⁵·50/(2880m⁴)≤10⁻⁴ ⇔ m≥8,6334 → 9 subintervalos.

## 2. S y L
- **S §7.7 Integración aproximada pp. 507-516**: punto medio/izq./der. p.507; trapecio T_n p.508 (Ej. 1 ∫₁²1/x, n=5: T₅≈0,695635, M₅≈0,691908, ln2≈0,693147); cotas |E_T|≤K(b−a)³/(12n²), |E_M|≤K(b−a)³/(24n²) p.510 (Ej. 2 n=41 trapecio, 29 punto medio); Simpson S_n=(Δx/3)[1,4,2,…,4,1] p.512-513 (Ej. 4 p.513); |E_S|≤K(b−a)⁵/(180n⁴) p.514; Ej. 6 p.515 (n=8).
- **L §4.6 pp. 305-311**: Teor. 4.17 trapecio p.306 (Ej. 1 ∫₀^π sen x, n=4→1,896, n=8→1,974); Teor. 4.18 (Simpson exacta en cuadráticas) p.307; Teor. 4.19 Simpson p.308 (Ej. 2 → 2,005; 2,0003); Teor. 4.20 errores p.309; Ej. 3 pp.309-310.

## 3. E (Ej. 6.36-6.41, pp. 242-246; 6.42 ya es §6.5)
| E | Pág. | Enunciado (resumen; leer completo en ejercicios.txt) | Resultado |
|---|---|---|---|
| 6.36 | 242 | ¿La integración numérica solo es útil si no se conoce la expresión de f? | No: puede no haber primitiva elemental o ser muy difícil |
| 6.37 | 242-243 | f(0)=42, f(3)=41: ¿trapecio? ¿Simpson? | trapecio 124,5; Simpson no (falta f(1,5)) |
| 6.38 | 243 | f=3+x (x≤1), 4x (x>1): ¿∫₋₁³ exacta con trapecio compuesto en nº par de subintervalos iguales? | Sí (x=1 es nodo; con 4 subint. T=22=exacto) |
| 6.39 | 244 | finca entre tres caminos y un río, puntos (0,130),(100,120),(200,125),(300,140),(400,140),(500,150): área con trapecio compuesto | 66 500 m² |
| 6.40 | 244-245 | ∫₀^π cos x, trapecio con 4 intervalos, comparar con el real | 0 (= real) |
| 6.41 | 245-246 | f(−1)=40,f(0)=42,f(1)=41,f(2)=42,f(3)=41: ∫₋₁³ con rectángulo derecho, trapecio y Simpson, simples y compuestos | 164 y 166; 162 y 165,5; 163,33… y 166,33… |

## 4. X (exámenes): trapecio / Simpson / error (p. = página PDF de X; convocatoria en fuentes_txt/indice_examenes_*.md)
Valores verificados por el agente: p.7 ∫₀^{2π}1/(2+cos x), trapecio 3 nodos = 4π/3 (real 2π/√3) · p.13 (Feb 2011, 2ª sem.) trapecio con f(−1..3)=1,2,−1,−3,0 → −3/2 · p.23 ∫₀^π cos²x sen x trapecio 4 int. = π√2/8 (real 2/3) · p.25 ∫₋₁¹e^{x²} trapecio 2 subint. = e+1 · p.36 ∫₀^{π/2}cos x: trapecio 2 int. π(1+√2)/8≈0,9481, Simpson π(1+2√2)/12≈1,0023 · p.38 trapecio con f(0)=2,f(1)=0,f(3)=−1,f(7)=4 → 6 · p.46-47 (Sept 2014) Simpson simple ∫₋₃⁻¹ 2/(x(x−1)) con nodos −3,−2,−1 = 5/6 (real 2ln(3/2)≈0,8109) · p.50-51 Simpson 3 nodos de ∫₀^{2π}dx/(2+cos x) = 14π/9 · p.65-66 (Feb 2016) f(1)=31,f(2)=26,f(3)=43: trapecio 63, Simpson 178/3, ∫g con g=11x²−38x+58 = 178/3 (Simpson exacto en parábolas) · p.69 ∫₀¹e^{x³} trapecio 2 subint. = (1+2e^{1/8}+e)/4≈1,4961 · p.78-79 (Feb 2017) ∫₀¹x/(x²+1)² = 1/4; trapecio 2 subint. 89/400; Simpson 3 nodos 51/200 · p.85 Simpson f(0)=1,f(1)=−2,f(2)=0 → −7/3 · p.93-94 (Feb 2018) Simpson con nodos 0,1,2 de 2/(x(x+2)): no se puede (f(0) no definida) · p.100 (Electrónica 1) polinomio por (0,15),(1,18),(2,20),(4,23); trapecio 35,5; Simpson 107/3 · p.103 eˣcos x trapecio ∫₀^{π/2}: π/4, real ≈1,9052 · p.105 ∫₁ᵉ ln x/x trapecio ½−1/(2e), real ½ · p.107 f(0)=1,f(2)=3,f(4)=2: interpolación y Simpson ∫₀⁴=10 · p.109-111 trapecio de ∫₃⁵dx/√(−x²+8x−7) con 5 subint. ≈0,6808 (real 2arcsen(1/3)≈0,6797) · p.112-114 tabla x=1,0…1,4, f=0,232;0,157;0,648;0,698;0,834 trapecio 0,2036 · p.130 ∫₁³(2x+3)/(x²+3x+2): Simpson ≈1,2056, exacta ln20−ln6≈1,2040 · p.133-134 ∫₃⁵x/(x²+3x+2) trapecio 4 subint. ≈0,267573 (exacta 0,267479) · p.136 (Feb 2017, 2ª sem.) ∫₀^πx²sen x Simpson = π³/6≈5,1677 (exacta π²−4) · p.137-138 (Feb 2017, 1ª sem.) ∫₃⁵(5x+3)/(x²+2x+3) trapecio 2 subint. ≈1,7203 (exacta ≈1,71479) · p.139 ∫₀^π sen²x cos x: trapecio 4 int. = 0, Simpson = 0, exacta 0 · p.141 (Feb 2018, 2ª sem.) ∫₀^{π/2}sen⁴x cos³x Simpson compuesta en 3 subint. ≈0,05689 (exacta 2/35) · p.143 (Sept 2018, Electrónica) ∫₁³x/(1+√x) trapecio 2 subint. ≈1,6275 · p.151 (Feb 2019, 1ª sem.) f(1)=2,f(3)=3,f(4)=2,f(8)=10: p(2)=116/35, Simpson compuesta 2 subint. de ∫₁⁴ ≈8,6036 (no hay preguntas de cota de error en X).
Aviso para quien resuelva: en p.122-124 (Examen 5, Ej. 5) el trapecio correcto es 63; la solución impresa da 68 (no copiarla; no mencionar la discrepancia en el HTML). Enunciado de p.38 con f(1)=0 (imagen); p.85 es ∫₀².
