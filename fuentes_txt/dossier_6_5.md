# Dossier Tema 6.5: Paso al límite en integración (solo integrales impropias en examen)

Páginas: U impresa = PDF + 2; E impresa = PDF; S = cabecera impresa; L impresa = PDF − 17. Verificadas por el agente de fuentes (U pp. 272-278 y 282, L pp. 569-574 y X en imagen).

## 0. Rangos de U §6.5 (pp. 271-282)
| Apartado | Pág. | Contenido | Examen |
|---|---|---|---|
| 6.5.1 Motivación | 271 | integrar en intervalos no acotados o funciones no acotadas | contexto |
| 6.5.2 Impropias de 1ª especie | 271-274 | Def. 6.9 (p.272); Ej. 6.36 (p.272), 6.37-6.38 (p.273), 6.39 (pp.273-274), 6.40 (p.274); extensiones a (−∞,b] y ℝ; condición necesaria (recuadro p.274) | SÍ |
| Impropias de 2ª especie | 275-276 | Def. 6.10 (p.275); Ej. 6.41 (p.275), 6.42 (p.276); asíntota interior; recuadro de precaución (p.276); margen p.275: 3ª especie | SÍ |
| Convergencia/divergencia | 277-278 | criterio de comparación (p.277), Ej. 6.43 (p.277), 2ª especie por comparación sin enunciar + Ej. 6.44 (p.278), comparación por límite (recuadro p.278), Ej. 6.45 (p.278) | SÍ |
| 6.5.3 Sucesiones funcionales | 279-280 | convergencia uniforme e integrabilidad, Ej. 6.46 | FUERA (colapsado en `details.fuera`) |
| Series de potencias término a término | 280-281 | Prop. 6.1, Ej. 6.47 | FUERA |
| Autoevaluación | 281-282 | solo ítems 9 y 10 son de impropias | parcial |

## 1. U (citas)
- p.271: «Al trabajar con integrales hemos considerado funciones acotadas sobre intervalos acotados. Pero a menudo se necesita integrar sobre intervalos no acotados o funciones no acotadas.»
- **Def. 6.9 (p.272), 1ª especie:** f:[a,∞)→ℝ continua y acotada; ∫ₐ^∞ f = lím_{M→∞} ∫ₐᴹ f; convergente si el límite es real, divergente si no. Extensiones (p.274): (−∞,b] análogo; en ℝ se parte en un c: «Es convergente si ambas lo son y es divergente si alguna lo es.» Recuadro p.274: condición necesaria lím_{x→∞} f(x)=0 «siempre que el límite exista».
- Ej. 6.36 (p.272): ∫₁^∞ dx/x² = 1. Ej. 6.37 (p.273): ∫₁^∞ dx/x diverge (ln M). Ej. 6.38 (p.273): ∫₁^∞ dx/x^p: converge si p>1 (valor 1/(p−1)), diverge si p≤1. Ej. 6.39 (pp.273-274): ∫₀^∞ e^{−kx}dx: k>0 converge (1/k); k≤0 diverge. Ej. 6.40 (p.274): ∫_{−∞}^{∞} dx/(1+x²) = π (partiendo en 0).
- **Def. 6.10 (p.275), 2ª especie:** f:(a,b]→ℝ continua y no acotada; ∫ₐᵇ f = lím_{c→a⁺} ∫꜀ᵇ f (análogo si la asíntota está en b). Margen p.275: «integrales de tercera especie: … uno de los extremos … es ∞ o −∞ y la función … no está acotada … la dividimos en la suma de una integral de cada especie.»
- Ej. 6.41 (p.275): ∫₀¹ dx/x^p: converge si p<1 (valor 1/(1−p)), diverge si p≥1 (usa t=1/x). Ej. 6.42 (p.276): ∫₋₁¹ dx/x² diverge (se parte en 0; Barrow a ciegas daría −2). Asíntota interior c∈[a,b]: se divide en dos integrales de 2ª especie. Recuadro p.276: «Antes de resolver una integral definida hay que comprobar la continuidad del integrando…».
- **Criterio de comparación (p.277):** 0≤f≤g continuas en [a,∞): si ∫g converge, converge ∫f; si ∫f diverge, diverge ∫g. Nota: f y g han de ser >0. Ej. 6.43: ∫₁^∞ dx/√(x⁴+x²+1) ≤ ∫₁^∞ dx/x²: converge. p.278: criterio análogo para 2ª especie (no enunciado); Ej. 6.44: ∫₀¹ dx/∛(x³+x²+x) ≤ ∫₀¹ dx/x^{3/4}: converge.
- **Comparación por límite (recuadro p.278):** f≥0, g>0 continuas en [a,∞), lím_{x→∞} f/g = l: l∈(0,∞) ⇒ ambas convergen o ambas divergen; l=0 y ∫g converge ⇒ ∫f converge; l=∞ y ∫g diverge ⇒ ∫f diverge. Ej. 6.45: ∫₀^∞ dx/(eˣ+1) con g=e^{−x}: límite 1, converge.
- (La convergencia absoluta de integrales impropias no está en U §6.5: no atribuirla a U.)

## 2. S y L
- **S §7.8 Integrales impropias, pp. 519-528** (inicio p.519 por el índice): Def. 1 intervalos infinitos p.520 (Ej. 1 ∫₁^∞ dx/x diverge p.520; Ej. 2 ∫_{−∞}^0 xeˣ = −1 p.521); Ej. 3 ∫dx/(1+x²)=π p.522; Ej. 4 ∫₁^∞ dx/x^p converge ⇔ p>1, pp.522-523; Tipo 2 (integrandos discontinuos) Def. 3 p.523; Ej. 5 ∫₂⁵dx/√(x−2)=2√3 p.524; Ej. 7 ∫₀³dx/(x−1) diverge (advertencia) p.524; Ej. 8 ∫₀¹ ln x = −1 p.525; teorema de comparación p.525; Ej. 9 ∫₀^∞ e^{−x²} p.526.
- **L §8.8 pp. 568-574**: definiciones p.568; Ej. 1 ∫₁^∞dx/x diverge, Ej. 2 p.569; Def. discontinuidades infinitas p.571; Ej. 6 ∫₀¹dx/∛x = 3/2 p.572; Ej. 8 ∫₋₁²dx/x³ diverge («evaluación incorrecta») p.572; Ej. 9 ∫₀^∞dx/(√x(x+1)) = π p.573; Teor. 8.5 (∫₁^∞dx/x^p) p.574.

## 3. E (Tema 6 acaba en p.254)
| E | Pág. | Enunciado (resumen; leer completo en ejercicios.txt) | Resultado |
|---|---|---|---|
| 6.42 | 246 | f continua y acotada en ℝ: ¿hay impropias de 1ª y 2ª especie? | 1ª sí (dominio ℝ), 2ª no (f acotada) |
| 6.43 | 247 | ∫₀^{+∞} x e^{−x²} dx por definición | 1/2 |
| 6.44 | 247-248 | aₙ=∫₀ⁿ cos(2πx)dx: 1) lím aₙ=0; 2) ¿garantiza que ∫₀^{+∞} converge? | 1) aₙ=sen(2πn)/(2π)=0; 2) no: ∫₀^M oscila entre ±1/(2π), diverge |
| 6.45 | 248 | ¿En una impropia de 2ª especie el intervalo está acotado? | Sí |
| 6.46 | 248-249 | ∫₀¹ ln x dx por definición | −1 |
| 6.47 | 249-250 | comparación por límite: ∫₁^{+∞}dx/ln(x+1); ∫₁^{+∞}e^{−x²}dx | la 1ª diverge (g=1/x, límite ∞); la 2ª converge (g=1/x², límite 0) |
| 6.48 | 250-252 | Γ(p)=∫₀^{+∞}e^{−x}x^{p−1}dx converge para p>0; Γ(p+1)=pΓ(p); Γ(1)=1; Γ(n+1)=n! | separar [0,1] y [1,∞); partes |
| 6.49-6.51 | 252-254 | **FUERA DE EXAMEN** (paso al límite bajo la integral / series de potencias) | 6.49: 0; 6.50: 0; 6.51: F=½f−½ con f=e^{2x}… (no resolver; solo listar en el bloque `fuera`) |

## 4. X (impropias; p. = página PDF; convocatoria en fuentes_txt/indice_examenes_*.md)
1. p.25 (Sept 2012, Mecánica, Mod. A, PC2): «Sean a y b del intervalo (−10,10). Razone si ∫ₐᵇ f puede ser impropia.» Sí, de 2ª especie (f no acotada en [a,b]).
2. p.47 (Sept 2014, Mod. A, Ej. 5c): ¿es impropia ∫_{−∞}^{−1} 2/(x(x−1)) dx? Sí, 1ª especie (única causa: límite infinito; la función está acotada en el intervalo). Valor: 2 ln 2 (converge).
3. p.73 (Sept 2016, Mod. B, P3): clasificar ∫₀^∞ e^{−x}dx: 1ª especie (función acotada, intervalo no). Valor 1.
4. p.81 (Feb 2017, Mod. B, P3 corta): ∫₁^∞ 1/x^p dx para p>1: 1ª especie solamente (0<1/x^p<1).
5. p.94 (Feb 2018, Mod. B, Ej. 5c): ∫_{−∞}^{−2} 2/(x(x+2)) dx: de 1ª y 2ª especie (límite infinito y f no acotada en −2); la integral diverge (primitiva ln|x|−ln|x+2| → +∞ en −2⁻).
6. p.105 (Electrónica 3, Ej. 5a): ∫₁ᵉ (ln x)/x dx: NO es impropia (continua en [1,e]); valor 1/2.
7. p.115 (Examen 3, Ej. 3): ∫₀^{π/2} cos x/√(sen x) dx = 2 (impropia de 2ª especie en 0 que Barrow a ciegas resuelve bien).
8. p.150 (Feb 2019, 1ª sem., P2): clasificar y calcular ∫₀^{+∞} x/√(eˣ) dx: 1ª especie; primitiva (−2x−4)e^{−x/2}; valor 4.
No hay en X preguntas de comparación/convergencia con criterios: indicarlo en el HTML.
