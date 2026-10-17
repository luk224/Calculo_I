# Dossier 4.2 «Funciones de varias variables» (U §4.2, pp. 152-167)
Páginas: U impresa = PDF+2; E impresa = PDF; X = página PDF de Examenes-resueltos-Calculo.pdf. S y L NO tienen apartado equivalente (solo una variable): el tema depende de U, E y X.

## 1. U §4.2 (empieza al pie de p.152; §4.3 empieza en p.168)
- 4.2.1 Motivación p.152: T(x,y) temperatura de placa; T(x,y,t) tres variables. Objetivos p.153: f: D⊂Rⁿ→R extiende una variable; entender límite en dos variables; calcularlo.
- **Def. 4.3 p.153**: f: D⊂R²→R asigna a cada (x,y)∈D un único real f(x,y). D dominio, f(D) imagen. Convenio: sin dominio explícito, el mayor conjunto donde tenga sentido la expresión.
- Ej. 4.9 p.153: f=2x²+3y⁴, dominio R², imagen [0,∞). Ej. 4.10 pp.153-154: f=1+x²−y (f(1,1)=1, f(−3,0)=√10, f(t,t²)=1); dominio {y≤1+x²} (Fig. 4.9 p.154); imagen [0,∞).
- Notación p.154: z=f(x,y); variables independientes x,y; dependiente z. Se extiende a n variables.
- **Gráfica p.155**: {(x,y,z)∈R³ : (x,y)∈D, z=f(x,y)}. Proyección sobre xy = dominio; sobre eje z = imagen.
- **Curvas de nivel p.155**: {f(x,y)=k} (curva de contorno, Fig. 4.10); en tres variables, superficies de nivel. Trazas = intersecciones con z=k.
- Ej. 4.11 pp.155-157: f=x²+y²+1: k<1 vacía, k=1 punto (0,0), k>1 circunferencias de radio √(k−1); cortes x=c parábolas; gráfica paraboloide (Fig. 4.11 p.156).
- Operaciones/composición pp.157-158: Ej. 4.12 (x²y)/(e^{xy}); Ej. 4.13 g∘f=cos(x²−y²+xy); Ej. 4.14 h∘g con g(ρ,θ)=(ρcosθ,ρsenθ).
- 4.2.3 Límite. Idea p.159: infinitos caminos (Fig. 4.12). **Def. 4.4 p.159** (ε-δ con 0<d((a,b),(x,y))<δ ⇒ |f−l|<ε; Fig. 4.13 p.160). Álgebra de límites p.160 (suma, producto, cociente con m≠0).
- p.161: límites reiterados deben coincidir; también por rectas y=mx+k o curvas y=g(x); si coinciden NO se puede afirmar que exista el límite (solo condición necesaria).
- Ej. 4.15 p.162 (Fig. 4.14): f=y−x+½xy+1 en (1,1), límite 3/2. Ej. 4.16 pp.162-163: x³y/(x⁶+y²) en (0,0): reiterados 0 y 0, rectas 0, pero y=x³ da 1/2 ⇒ no existe.
- **Regla del emparedado p.163**. Ej. 4.17 pp.163-164: x²y/(x²+y⁴)→0 (|f|≤|y|).
- **Propiedad p.165**: infinitésimo × acotada → 0. **Polares p.165**: F(ρ,θ)=f(a+ρcosθ,b+ρsenθ): (1) si el límite en ρ→0 depende de θ, no existe; (2) si |F−l|≤h(ρ)→0, límite l; (3) otro caso: no se concluye. Ej. 4.18 p.165: x³/(x²+y²)→0 (F=ρcos³θ).
- **Continuidad**: Def. 4.5 p.166 (lím f = f(a,b)); Def. 4.6 discontinua; Def. 4.7 continua en A. Propiedades p.166 (suma, producto, cociente, composición; elementales donde estén definidas).
- Ej. 4.19 p.167: e^{x²+y} continua en R². Ej. 4.20 p.167: x³/(x²+y²), f(0,0)=0, continua. Ej. 4.21 p.167: x²/(x²+y²), f(0,0)=0, discontinua en 0 (x=0→0, y=0→1, y=x→1/2); continua en R²\{0}.

## 2. E §4.2 = E 4.9-4.24 (§4.3 empieza en E 4.25, p.153). Enunciados completos en fuentes_txt/ejercicios.txt (líneas ~8005-8700); leer imagen si la extracción falla
- 4.9 (p.142) gases ideales P(T,V)=nRT/V, P(273,2) con n=0,1 → 1,1193 atm. 4.10 (pp.142-143): fijar variable; P(T,2)=1 ⇒ T=243,9 K; P(T,2)=0,0041T; P(273,V)=2,2386/V; curva de nivel P=1 recta V=0,0082T.
- 4.11 (p.144) gráfica ⊂ R³ (c). 4.12 (p.144) ¿gráfica en forma de balón? No (unicidad de imagen).
- 4.13 (pp.144-145) dominio de √(x²−y³). **Errata**: el libro escribe x²>y³; debe ser ≥: dominio {y≤x^{2/3}}.
- 4.14 (pp.145-146) dominio √(ln(xy)): xy≥1: {x,y>0,y≥1/x}∪{x,y<0,y≤1/x}. Errata menor: primera línea pone xy≥0, debe ser xy>0.
- 4.15 (pp.146-147) f(x,y,z)=cos(xz+ln y): dominio {y>0}, imagen [−1,1]. 4.16 (pp.147-148) leer curvas de nivel en figura: 1 crece; 2 se mantiene; 3 decrece; 4 crece (anticipa gradiente).
- 4.17 (p.148) x²−y²/3+8: hipérbolas (C'=0 → dos rectas y=±√3x, no tratado). 4.18 (p.149) x²−y: parábolas y=x²−C.
- 4.19 (pp.149-150) lím (x²+y³)/(x²+y²) en 0: reiterados 1 y 0 ⇒ no existe. 4.20 (p.150) reiterados iguales no bastan (contraejemplo propio xy/(x²+y²)).
- 4.21 (pp.150-151) dominio y continuidad de y sen(x²+1), ln(3+x²y²)/(3+x²+y⁴), √(x²y). **Errata**: dom h = {y≥0}∪{x=0}, el libro dice {y≥0}.
- 4.22 (pp.151-152) (x²+y²)sen(1/(x²+y²)), f(0,0)=0: continua (|f|≤ρ²). 4.23 (p.152) y²/x, 0 si x=0: no continua (rectas →0, x=y² →1). 4.24 (p.153) (x²−y²)/(x²+y²): no continua (ejes: −1 y 1). Errata redacción: «el producto» → «el cociente».

## 3. X relacionadas (PDF verificado en imagen por el agente)
Feb 2010 2ª sem PC3 (p.4) = E 4.19. Sept 2010 P3a (p.9) lím [x(y−1),(1+x)^{1/x}]: SIN solución en PDF, propia (0,e). Feb 2011 1ª sem Mec A Ej.6 (pp.11-12) x²sen(1/(x²+y²)) continua. Sept 2011 PC3 (p.16) V/F caminos ⇒ continua: Falso, contraejemplo x²+y... (f(0,0)=1). Sept 2012 PC4 (p.29, convocatoria según índice) lím ln(x²+1)cos(y²eˣ)=0. Feb 2013 1ª sem PC4 (p.33) (x²−y²)/(x²+y²) no existe (errata: «laterales»=a lo largo de ejes). Sept 2013 P6 (p.39) x²sen(1/(x²+y²)). Feb 2014 Mod B Ej.6 (p.45) arctg(xy/(x²+y²)) discontinua. Feb 2016 Mod B P4 (p.65) lím (x³+y⁴)/(x²+y²)=0 polares. Sept 2018 Mod A Ej.6 (p.98) arctg(xy/(x²+y²)): NO continua en 0 (indice_examenes_3.md l.98 erróneo). Electrónica 2 Ej.5 (p.102) √(x²+y²): dominio, imagen [0,∞), circunferencias. Electrónica 3 P3 (p.104) reiterados de (x−1)/(y²+x−1) en (1,0): 1 y 0. Electrónica B Ej.6 (pp.130-131) x²/(x²+y²) discontinua. Feb 2017 1ª sem P4 (p.137) curvas de nivel 2x²+2y²−4 (falta C=−4 punto, C<−4 vacío). Feb 2017 1ª sem Ej.6 (p.138) x²y³/(x⁴+y²), f(0,0)=1 discontinua. Feb 2018 2ª sem P4 (p.140) dominio e imagen x ln y+y ln x (imagen ℝ por f(x,1)=ln x; el libro lo justifica mal). Sept 2018 Electr. Ej.6 (p.143) ln(36−x²−y²) dominio disco abierto de radio 6 (el libro dice «círculo sin frontera»). Feb 2019 2ª sem Ej.6 (pp.148-149) dominio {1≤x²+y²<4}. Examen 5 Ej.6 (PDF 122, 124-125) (x³+xy²+3y⁴)/(x²+y²): continuidad (parte de §4.2; parciales/diferenciabilidad son 4.3/5.x). Examen 2 Ej.5 (p.113) x³/(x²+y²).
Erratas menores en X: p.102 «C positivo»→C≥0; p.104 f no definida en (1,0).
No leídos (solo índice): Feb 2010 1ª sem Ej.6 (PDF 2-3), Feb 2012 1ª Ej.6 (20-21), Sept 2012 Ej.6 (26-27), Sept 2014 Ej.6 (47-48), Sept 2015 Ej.6 (54-55), Feb 2015 B Ej.6 (57-58), Feb 2016 A Ej.6 (61-63), Sept 2016 Ej.6 (71-72), Feb 2017 A Ej.6 (79-80), Feb 2018 A Ej.6 (90-92), Examen 3 Ej.6 (117-118).

## 4. Dudas
Figuras U Fig. 4.9-4.14 (pp.154,155,157,159,160,162) sin recortar (Fig. 4.14 omite el «+1» en el pie). E 4.16 figura p.147 sin verificar píxel a píxel. No copiar erratas al HTML.
