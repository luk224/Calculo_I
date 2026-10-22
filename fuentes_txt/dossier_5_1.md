# Dossier 5.1 «Diferencial de una función. Función diferenciable. Plano tangente» (U §5.1, pp.186-193)
Páginas: U impresa = PDF+2; E impresa = PDF; X = página PDF de Examenes-resueltos-Calculo.pdf. S y L NO tienen apartado de varias variables (solo una variable: S §3.10 pp.250-251 linealización; L §3.9 p.231 y p.237). El tema depende de U, E y X.

## 1. U §5.1 (p.185 intro del Tema 5; §5.1 pp.186-193; §5.2 empieza en p.194)
- 5.1.1 Motivación p.186: derivabilidad ⇒ continuidad en una variable. Objetivos: diferencial como generalización de la derivada; relación con derivada según un vector.
- Idea del plano pp.186-188: parciales dan vectores tangentes (1,0,∂f/∂x), (0,1,∂f/∂y) (Fig. 5.1 p.187). **(5.1) p.188**: z = f(a,b)+∇f(a,b)·(x−a,y−b). Advertencia p.188: que existan parciales NO basta para que exista el plano tangente (Ej. 4.24).
- **Def. 5.1 p.189**: f diferenciable en (a,b) si lím_{(h,k)→(0,0)} [f(a+h,b+k) − f(a,b) − ∇f(a,b)·(h,k)] / ‖(h,k)‖ = 0. **(5.2) p.189** plano tangente: z = f(a,b)+∇f(a,b)·(x−a,y−b).
- **Ej. 5.1 pp.189-190**: f=e^{−1/(x²+y²)}, f(0,0)=0, diferenciable en (0,0): ∇f(0,0)=(0,0); polares: lím_{ρ→0} e^{−1/ρ²}/ρ=0.
- **Def. 5.2 p.190** (n variables): igual con h̄=(h₁,…,hₙ), ‖h̄‖.
- **Teorema 5.1 p.191**: si f es diferenciable en un punto, admite parciales y es continua en él.
- **Ej. 5.2 p.191**: f=xy+1 si x>0, f=x−y si x≤0 (discontinua en (0,0) ⇒ no diferenciable); g=x+|y| (no existe ∂g/∂y(0,0): laterales 1 y −1) ⇒ no diferenciable.
- **Condición suficiente p.192**: si f admite parciales cerca de a y son continuas en a ⇒ diferenciable en a. «Regular» = continua con parciales continuas.
- **Ej. 5.3 p.192**: f=sen(1/(x²+y²)) diferenciable en todo su dominio ℝ²∖{0}.
- Observación pp.192-193: para n>2 no se habla de plano tangente; espacio tangente (5.3) p.193: x_{n+1}=f(a)+∇f(a)·(x−a).
- **Def. 5.3 p.193** diferencial: Df(a)(x)=∇f(a)·x (aplicación lineal; la matriz es el gradiente). **Ej. 5.4 p.193**: f=x²+y en (1,2): Df(1,2)(x,y)=2x+y. **Def. 5.4 p.193**: diferenciable en A.
- Reglas de la diferencial (suma, producto, cociente) y Ej. 5.5: §5.2.2 pp.194-195 (fuera de 5.1).
- Relación con direccionales: U Teorema 4.2 p.180 (parciales continuas ⇒ D_v f=∇f·v). Que diferenciable ⇒ D_v f=∇f·v es consecuencia propia.

## 2. E 5.1-5.12 (pp.168-179), 5.13-5.14 son de §5.2.2
- 5.1 (p.168): parciales ⇒ ¿diferenciable y plano tangente? No se puede asegurar.
- 5.2 (p.168): f=cos y − yx², plano tangente en (0,0,1): z=1 (a, b).
- 5.3 (p.169): f=x²+y³+e^{x+y} en (1,−1,1): z=2+3x+4y.
- 5.4 (p.170): diferencial de f=x e^y + y cos²(xy) en (a,b): (e^b − b² sen 2ab)x + (a e^b + cos²(ab) − ab sen 2ab)y.
- 5.5 (pp.170-171): (x²+y²)sen(1/(x²+y²)), f(0,0)=0: parciales 0; diferenciable; parciales NO continuas en (0,0).
- 5.6 (pp.172-173): f=x|y| diferenciable en (0,0) (definición; no hay parciales en un entorno).
- 5.7 (pp.173-174): f=4x³/(x²+y²), f(0,0)=0: continua; f_x(0,0)=4, f_y(0,0)=0; no diferenciable ((f−4h)/ρ → −4cosθ sen²θ).
- 5.8 (pp.174-175): f:ℝ³→ℝ discontinua en (1,2,3), diferenciable en (3,2,1): no diferenciable en (1,2,3); continua en (3,2,1).
- 5.9 (pp.175-176): f=y sen(1/x)+x (x≠0), 0 si x=0: continua en 0; f_x(0,0)=1, f_y(0,0)=0; no diferenciable (en h=k no hay límite) ⇒ sin plano tangente.
- 5.10 (pp.176-177): (x²+y²)/ln(1−x²−y²) en x²+y²<1, f(0,0)=−1: continua y diferenciable en 0.
- 5.11 (p.178): xy/(x²+y²)^{1/4}, f(0,0)=0: parciales 0; diferenciable (√ρ cosθ senθ→0).
- 5.12 (p.179): f=x²−xy+y², g=(f+xy)/√(x²+y²), g(0,0)=0: g=√(x²+y²) fuera de 0; no existe ∂g/∂x(0,0) (lím |h|/h) ⇒ no diferenciable en 0.
- (5.13 pp.179-180: ∇(fg)=g∇f+f∇g; 5.14 pp.180-181: planos tangentes de f+g, fg, f/g — §5.2.2.)
- Notas internas (no al HTML): erratas en 5.5 (falta 1/ρ), 5.6 (condición suficiente mal aplicada), 5.14.

## 3. X (páginas PDF; todas verificadas en imagen por el agente de fuentes)
- Diferencial de (x+sen y)²: pp.35 (Feb 2013 2ª, Mec. B PC4), 44 (Feb 2014 B P4), 57 (Feb 2015 B P4). Df(a,b)(x,y)=2(a+sen b)(x+cos b·y).
- p.60 (Feb 2016 A P4): condición suficiente de diferenciabilidad.
- Diferenciabilidad: p.2-3 (Feb 2010 1ª Eléctrica Ej.6, x³/(x²+2y²)); pp.17-18 (Sept 2011 Mecánica Ej.6, = E 5.12); pp.20-21 (Feb 2012 1ª Mec. A Ej.6, = E 5.7); pp.26-27 (Sept 2012 Mec. A Ej.6, = E 5.10); pp.54-55 (Sept 2015 A Ej.6, (x²−y²)/∛(x³+y³)); pp.61-63 (Feb 2016 A Ej.6, x²y²/(x²+2y²)); pp.71-72 (Sept 2016 A Ej.6, y³ sen(1/(x²+2y²)): SÍ diferenciable); pp.79-80 (Feb 2017 A Ej.6, (x⁴+3xy³)/(x⁵+y⁴)); pp.90-92 (Feb 2018 A Ej.6, x³/(x²+2y²)); p.98 (Sept 2018 A Ej.6, arctg(xy/(x²+y²))); pp.115, 117-118 (Examen 3 Ej.6, = E 5.7); pp.122, 124-125 (Examen 5 Ej.6, (x³+xy²+3y⁴)/(x²+y²)).
- Plano tangente: p.127 (Electrónica A P4, x²+xy en (1,2,3): 4x+y−z=3); p.133 (Sept 2017 Electr. P4, eˣ(3 sen y+2) en (0,π/2,5): z=5+5x); p.138 (Feb 2017 1ª Ej.6: f=x²y³/(x⁴+y²), f(0,0)=1: discontinua en 0 (eje x → 0); en (1,1) plano z=y−1/2); p.100 (Electrónica I Ej.6: cos x − xy², plano z=1 en (0,0,1) + Hessiana y extremos); p.9 (P3b: diferencial de y·tg(sen x), sin solución impresa); p.140 (V/F gradiente nulo ⇒ extremo).
- Errores en soluciones impresas (notas internas): p.18 (∂g/∂x(0,0)=1, debe no existir), p.21 (signo), p.63 (denominador), p.72 (concluye mal: sí diferenciable), p.138.
