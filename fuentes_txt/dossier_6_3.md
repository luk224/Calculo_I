# Dossier Tema 6.3: Cálculo de integrales

Páginas: U impresa = PDF + 2; E impresa = PDF; S = cabecera; L impresa = PDF − 17. Verificado en `ingenieros.txt` y en render (U pp. 248, 249, 250, 255; E pp. 223, 231-232, 234, 237-238; X ver tabla). Resultados comprobados con sympy/mpmath por el agente de fuentes. El resolutor debe leer los enunciados completos en `ejercicios.txt` (E) y en la imagen (X: PDF `Examenes-resueltos-Calculo.pdf`, página PDF = página de `examenes.txt`; renderizar con PyMuPDF o pdftoppm).

## 0. Rangos de U §6.3 (pp. 246-262)

| Apartado | Pág. impresa | Contenido |
|---|---|---|
| 6.3.1 Motivación / 6.3.2 inicio | 246 | «misión imposible», se remite al Curso 0 |
| Propiedades de la integral indefinida | 247 | ∫cf = c∫f, ∫(f+g) = ∫f+∫g; Ej. 6.9 |
| Tabla de integrales inmediatas | 248 | 11 filas (abajo); Ej. 6.10 |
| Ej. 6.11-6.14 | 249 | ∫eˣcos(eˣ); ∫4x/√(1−4x⁴) = arcsen 2x²; ∫7x/(x²+3); ∫1/x = ln|x| |
| Cambio de variable | 249-251 | ∫f(x)dx = ∫f(g(t))g′(t)dt; Ej. 6.15, 6.16 (p. 250); en definidas hay que deshacer el cambio o cambiar límites (p. 251), Ej. 6.17 (∫₀^{π²} sen√x dx = ∫₀^π 2t sen t dt) |
| Integración por partes | 251-254 | ∫uv′ = uv − ∫u′v (p. 252); Ej. 6.18 (ln x), 6.19 (x²eˣ), 6.20 (eˣcos x, se despeja), 6.21 (recurrencia cosⁿ), 6.22 (definida) |
| Racionales | 255-258 | grado p < grado q (si no, dividir); descomposición en fracciones simples; Ruffini; Ej. 6.23, 6.24; integrales de fracciones simples p. 257 (ln|x−a|, (x−a)^{−n+1}/(−n+1), ln + arctg para irreducible de grado 2) |
| Método de Hermite | 259-261 | p/q = d/dx(f/g) + p₁/q₁; Ej. 6.25: ∫dx/((x+1)(x²+1)²) |
| Trigonométricas | 261-262 | t = tg(x/2): sen x = 2t/(1+t²), cos x = (1−t²)/(1+t²), dx = 2dt/(1+t²); Ej. 6.26; senⁿcosᵐ con sen² = (1−cos2x)/2, cos² = (1+cos2x)/2; Ej. 6.27 (∫cos²sen² = x/8 − sen4x/32) |

### Tabla de integrales inmediatas (U p. 248; f = f(x), a, k constantes)
1. ∫a dx = ax + k · 2. ∫f^a f′ = f^{a+1}/(a+1) + k (a ≠ −1) · 3. ∫f′/f = ln|f| + k · 4. ∫e^f f′ = e^f + k · 5. ∫a^f f′ = a^f/ln a + k · 6. ∫cos f · f′ = sen f + k · 7. ∫sen f · f′ = −cos f + k · 8. ∫f′/cos²f = ∫(1+tg²f)f′ = tg f + k · 9. ∫f′/(1+f²) = arctg f + k · 10. ∫f′/√(1−f²) = arcsen f + k · 11. ∫−f′/√(1−f²) = arccos f + k.

Cita de U p. 249: «Cuando la integral es un logaritmo, escribimos el valor absoluto de su argumento». Cita p. 250: «…si se puede descomponer en dos partes y una es la derivada de la otra, ahí tenemos el cambio de variable.» Cita p. 252: «Es importante elegir u y v de forma que la nueva integral sea más sencilla que la original…». Cita p. 259 (Hermite): «No es frecuente que el denominador sea la potencia de un polinomio irreducible de segundo grado, pero si nos lo encontramos, es mejor aplicar el Método de Hermite» (p. 258).

## 1. Ejemplos de U (resultados)
6.9: ∫(3x²−2x+5) = x³−x²+5x+k · 6.10: ∫3cos²x sen x = −cos³x+k · 6.15: ∫2/((−3x+2)²+1) = −(2/3)arctg(−3x+2)+k · 6.16: ∫cos x√(1+sen x) = (2/3)(1+sen x)^{3/2}+k · 6.18: x ln x − x + k · 6.19: x²eˣ − 2xeˣ + 2eˣ + k · 6.20: ½(eˣcos x + eˣsen x)+k · 6.23: (2x³+13x−30)/((x+2)(x−1)²(x²+4)) = −1/(x+2) + 2/(x−1) − 1/(x−1)² + (−x−1)/(x²+4) · 6.24: ∫ = −ln|x+2| + 2ln|x−1| + 1/(x−1) − ½ln(x²+4) − ½arctg(x/2)+k · 6.25: (1/4)(x+1)/(x²+1) + (1/4)ln|x+1| − (1/8)ln(x²+1) + (1/2)arctg x + k · 6.26: ∫(1+sen²x)/(1+cos x) = tg(x/2) − sen x + x + k · 6.27: x/8 − sen(4x)/32 + k.

## 2. S y L
- **S §5.5 Sustitución pp. 407-413** (regla p. 408, página inferida de las cabeceras 407/409); **§7.1 Partes pp. 464-469** (obj. p. 465, Ej. 2 ln x p. 465); **§7.2 Trigonométricas pp. 471-477** (cosⁿ, p. 471); **§7.3 Sustitución trigonométrica pp. 478-483** (Ej. 1 p. 479, solo contexto); **§7.4 Fracciones parciales pp. 485-493** (división previa p. 485, casos pp. 487-491).
- **L §4.5 Sustitución pp. 292-304** (Teor. 4.13 p. 293; Teor. 4.15 definidas p. 298); **§8.2 Partes pp. 515-523** (Teor. 8.1 p. 515; repetición Ej. 4 p. 518); **§8.3 Trigonométricas pp. 524-532**; **§8.5 Fracciones parciales pp. 542-550**.

## 3. E (Ej. 6.17-6.35, pp. 223-241). Ej. 6.36 (p. 242) ya es §6.4.
| E | Pág. | Enunciado (resumen; leer completo en ejercicios.txt) | Resultado |
|---|---|---|---|
| 6.17 | 223 | ∫(ln x)/x; ∫(x²−1)/(x³−3x+7); ∫sen(√x³)/√x³·x² | (ln x)²/2; ⅓ln|x³−3x+7|; −⅔cos√(x³) (+C) |
| 6.18 | 224 | ∫xeˣ por partes: ¿qué u y v′? | a) u=x, v′=eˣ; (x−1)eˣ |
| 6.19 | 225 | ∫xeˣ/(x+1)² por partes | −xeˣ/(x+1) + eˣ + C |
| 6.20 | 225 | descomponer (x²+7x+3)/(x+1)³ | 1/(x+1) + 5/(x+1)² − 3/(x+1)³ |
| 6.21 | 226-227 | ∫(x+2)/(x²−1) | (3/2)ln|x−1| − ½ln|x+1| + C |
| 6.22 | 227-228 | f=(x³+3x²−28x−33)/(x²−x−20): afirmación correcta (hay que dividir) | b) x²/2+4x+3ln|x−5|−7ln|x+4|+C |
| 6.23 | 229 | f=8x³/(x²+1)²: ¿método? | b) Hermite: 8x/(x²+1) + d/dx(4/(x²+1)) |
| 6.24 | 230 | ∫(3x⁴+4x²+2x+1)/(x(x²+1)²) (Hermite) | ln|x|+ln(x²+1)+arctg x + x/(x²+1) + C |
| 6.25 | 231-232 | ∫(2x²−x+1)/((x²+x+1)²(x+1)) (Hermite) | (−4x+1)/(3(x²+x+1)) + 4ln|x+1| − 2ln(x²+x+1) + (4√3/9)arctg((2x+1)/√3) + C |
| 6.26 | 232-233 | ∫dx/(sen x+cos x): ¿cambio? | b) t=tg(x/2) y c) ln en t (−1/√2 ln|t−1−√2| + 1/√2 ln|t−1+√2|) |
| 6.27 | 233-234 | ∫tg(2x+1)/(1+2tg²(2x+1)) (t = tg(2x+1)) | ¼ln(1+sen²(2x+1)) + C |
| 6.28 | 234-235 | ∫(1+√x−∛x²)/(1+∛x) (t⁶=x) | 6(−t⁸/8+t⁷/7+t⁶/6−t⁵/5+t³/3−t+arctg t)+C, t=x^{1/6} |
| 6.29 | 235-237 | ∫√((x+1)/(x−1)) con (x+1)/(x−1)=t² | ln|(√(x+1)+√(x−1))/(√(x+1)−√(x−1))| + √(x²−1) + C |
| 6.30 | 237 | ∫₀¹ arcsen(x/2)/√(4−x²) | b) π²/72 |
| 6.31 | 238 | ∫_{1/2}^{5/4} dx/√(3−(2x−1)²) | d) π/6 |
| 6.32 | 238-239 | ∫₀^{π/2} cos²(2x) | π/4 |
| 6.33 | 239-240 | área bajo e^{2x} entre x=1 y 2 | (e⁴−e²)/2 |
| 6.34 | 240-241 | áreas entre x², x³, √x | b): f–g=1/12, f–h=1/3, h–g=5/12 |
| 6.35 | 241-242 | área entre cos πx y sen πx en [−1,1] | a) 4√2/π |

(En E 6.25 el integrando impreso en la solución difiere del enunciado; usar el del enunciado, que es el que cumple el resultado. No mencionarlo en el HTML.)

## 4. X (exámenes) de integrales y primitivas (página PDF X; método)
p.1 ∫₀¹3x/(3x²+1)² = 3/8 (tabla 2) · p.6 ∫₀¹e^{−2x}ln(1+e^{2x}) ≈ 0,4858 (cambio+partes) · p.9 ∫x³/(x²−2x+1) = x²/2+2x+3ln|x−1|−1/(x−1)+C (división, sin solución impresa) · p.11 ∫x⁶/(x²+1) = x⁵/5−x³/3+x−arctg x+C (Feb 2011, Mecánica A, Ej. 5) · p.19-20 ∫₋₂⁰(3+4x)e^{−x} = −e²−7 (partes) · p.29 ∫₀¹x/(x²+1)³ = 3/16 · p.33 ∫xeˣ · p.38 ∫x⁵∛((1+x³)²) = (1/8)(1+x³)^{8/3} − (1/5)(1+x³)^{5/3}+K · p.47 ∫2/(x(x−1)) = 2ln|x−1|−2ln|x|+C · p.56 ∫e^{2x}cos x = (1/5)e^{2x}(sen x+2cos x)+C · p.59 ∫ln x · p.81 ∫x³e^{x²} = ½(x²−1)e^{x²}+C · p.88 ∫x⁴/(x²+1) = x³/3−x+arctg x+C · p.93-94 ∫2/(x(x+2)) = ln|x|−ln|x+2|+C · p.105 ∫₁ᵉ(ln x)/x = 1/2 · p.119 primitiva de (x+1)/(x²−3x) = −⅓ln|x|+(4/3)ln|x−3|+C (opción C) · p.128 ∫₀^{π²}sen√x = 2π · p.130 ∫₁³(2x+3)/(x²+3x+2) = ln(10/3) · p.133-134 ∫₃⁵x/(x²+3x+2) = ln(98/75) · p.136 ∫₀^π x²sen x = π²−4 · p.139 ∫₀^π sen²x cos x = 0 · p.141 ∫₀^{π/2}sen⁴x cos³x = 2/35 · p.143 ∫x/(1+√x) = 2(x^{3/2}/3 − x/2 + √x − ln(1+√x))+C (x=t²) · p.148 ∫dx/(4+5cos x) = ⅓ln|(3+tg(x/2))/(3−tg(x/2))|+C.
Convocatorias exactas: ver `fuentes_txt/indice_examenes_*.md`; las pp. 9, 16, 29, 33, 43, 88, 130 no tienen cabecera visible: tomar la convocatoria del índice. Los apartados de trapecio/Simpson/impropias de esas mismas preguntas son de 6.4 y 6.5: se omiten aquí.
