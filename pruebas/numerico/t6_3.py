r"""Tema 6.3 (Cálculo de integrales): inmediatas, cambio de variable, partes, fracciones simples, Hermite,
trigonométricas y raíces; primitivas comprobadas derivando y valores de las definidas recalculados con sympy.

`comprobaciones(c)`: c(ejercicio, descripción, valor_sympy, esperado, trozo_latex)
  - valor_sympy: lo que calcula sympy;  esperado: lo que afirma la página;
  - trozo_latex: cadena que debe aparecer en `ejercicios/<ejercicio>.html` (o `.solucion.html`), comparada sin etiquetas,
    espacios, \, \; \! ni \displaystyle y con \dfrac/\tfrac = \frac.
Las comprobaciones de la práctica «Ahora hazlo tú» (pr-*) solo se activan cuando el ejercicio existe en `contenido/`.
"""
import pathlib

import sympy as sp

R = sp.Rational
pi = sp.pi
E_ = sp.E
x = sp.Symbol('x', real=True)
t = sp.Symbol('t', real=True)
ln, sen, cos, tg, atan, asin, sqrt, exp, Abs = sp.log, sp.sin, sp.cos, sp.tan, sp.atan, sp.asin, sp.sqrt, sp.exp, sp.Abs
EJ = pathlib.Path(__file__).resolve().parents[2] / 'contenido' / 'tema_6_3' / 'ejercicios'


def _igual(p, q):
    p, q = sp.sympify(p), sp.sympify(q)
    if p == q:
        return True
    return sp.simplify(p - q) == 0


def lista(vals, esperados):
    return si((len(vals) == len(esperados) and all(_igual(p, q) for p, q in zip(vals, esperados))))


def si(cond):
    return sp.Integer(1 if bool(cond) else 0)


def r(val, d):
    return R(str(round(float(val), d)))


def integral(f, a, b, v=x):
    return sp.integrate(f, (v, a, b))


def num(f, a, b):
    return sp.Integral(f, (x, a, b)).evalf(30)


def prim(F, f, puntos):
    """1 si F' = f (comprobado en varios puntos del dominio con 25 cifras; vale con valores absolutos y raíces)."""
    dF = sp.diff(F, x)
    difs = [sp.N((dF - f).subs(x, p), 25) for p in puntos]
    return si(all(d.is_number and not d.has(sp.nan, sp.zoo) and abs(d) < 1e-15 for d in difs))


PTS = [R(3, 2), R(11, 5), R(37, 10), R(23, 4)]           # puntos positivos lejos de raíces de los ejemplos
PTS_T = [R(1, 5), R(7, 10), R(-3, 10), R(13, 10)]  # puntos donde las trigonométricas están definidas


def comprobaciones(c):
    # ---- Ejercicios del libro (E 6.17-6.35)
    c('ej-6-17', 'primitivas: (ln x)²/2; (1/3)ln|x³−3x+7|; −(2/3)cos√(x³)',
      lista([prim(ln(x) ** 2 / 2, ln(x) / x, PTS), prim(ln(Abs(x ** 3 - 3 * x + 7)) / 3, (x ** 2 - 1) / (x ** 3 - 3 * x + 7), PTS + [-3]),
             prim(-R(2, 3) * cos(sqrt(x ** 3)), sen(sqrt(x ** 3)) / sqrt(x ** 3) * x ** 2, PTS), (x ** 3 - 3 * x + 7).subs(x, -3)],
            [1, 1, 1, -11]), 1, r"=\frac13\ln\lvert x^3-3x+7\rvert+C")
    c('ej-6-17', 'tercera primitiva', 1, 1, r"=-\frac23\cos\sqrt{x^3}+C")
    c('ej-6-18', '∫xeˣ = (x−1)eˣ con u=x; con u=eˣ aparece ∫x²eˣ/2',
      lista([prim((x - 1) * exp(x), x * exp(x), PTS)], [1]), 1, r"=(x-1)e^x+C")
    c('ej-6-19', '∫xeˣ/(x+1)² = eˣ/(x+1)', prim(exp(x) / (x + 1), x * exp(x) / (x + 1) ** 2, PTS), 1, r"I=\dfrac{e^x}{x+1}+C")
    c('ej-6-20', 'apart = 1/(x+1) + 5/(x+1)² − 3/(x+1)³',
      sp.apart((x ** 2 + 7 * x + 3) / (x + 1) ** 3) - (1 / (x + 1) + 5 / (x + 1) ** 2 - 3 / (x + 1) ** 3), 0,
      r"f(x)=\dfrac1{x+1}+\dfrac5{(x+1)^2}-\dfrac3{(x+1)^3}")
    c('ej-6-21', 'A=3/2, B=−1/2', lista([sp.apart((x + 2) / (x ** 2 - 1)) - (R(3, 2) / (x - 1) - R(1, 2) / (x + 1)),
                                       prim(R(3, 2) * ln(Abs(x - 1)) - R(1, 2) * ln(Abs(x + 1)), (x + 2) / (x ** 2 - 1), PTS + [R(1, 2), -3])],
                                      [0, 1]), 1, r"=\frac32\ln\lvert x-1\rvert-\frac12\ln\lvert x+1\rvert+C")
    f22 = (x ** 3 + 3 * x ** 2 - 28 * x - 33) / (x ** 2 - x - 20)
    c('ej-6-22', 'f = x+4+(−4x+47)/(x²−x−20) = x+4+3/(x−5)−7/(x+4); b) correcta',
      lista([sp.simplify(f22 - (x + 4 + (-4 * x + 47) / (x ** 2 - x - 20))), sp.apart(f22) - (x + 4 + 3 / (x - 5) - 7 / (x + 4)),
             prim(x ** 2 / 2 + 4 * x + 3 * ln(Abs(x - 5)) - 7 * ln(Abs(x + 4)), f22, PTS + [7])], [0, 0, 1]), 1,
      r"f(x)=x+4+\dfrac{-4x+47}{x^2-x-20}")
    a, b, cc, e = sp.symbols('a b c e')
    sol23 = sp.solve(sp.Poly(sp.expand((a * x + b) * (x ** 2 + 1) + sp.together(sp.diff((cc * x + e) / (x ** 2 + 1), x) * (x ** 2 + 1) ** 2)
                                       - 8 * x ** 3), x).coeffs(), [a, b, cc, e])
    c('ej-6-23', 'Hermite: a=8, b=c=0, e=4; ∫ = 4ln(x²+1)+4/(x²+1)',
      lista([sol23[a], sol23[b], sol23[cc], sol23[e], prim(4 * ln(x ** 2 + 1) + 4 / (x ** 2 + 1), 8 * x ** 3 / (x ** 2 + 1) ** 2, PTS)],
            [8, 0, 0, 4, 1]), 1, r"f=\dfrac{8x}{x^2+1}+\dfrac{d}{dx}\Big(\dfrac4{x^2+1}\Big)")
    c('ej-6-24', 'primitiva por Hermite',
      prim(ln(Abs(x)) + ln(x ** 2 + 1) + atan(x) + x / (x ** 2 + 1), (3 * x ** 4 + 4 * x ** 2 + 2 * x + 1) / (x * (x ** 2 + 1) ** 2), PTS + [-2]), 1,
      r"I=\ln\lvert x\rvert+\ln(x^2+1)+\operatorname{arctg}x+\dfrac x{x^2+1}+C")
    F25 = (-4 * x + 1) / (3 * (x ** 2 + x + 1)) + 4 * ln(Abs(x + 1)) - 2 * ln(x ** 2 + x + 1) + 4 * sqrt(3) / 9 * atan((2 * x + 1) / sqrt(3))
    c('ej-6-25', 'A=−4/3, B=1/3, C=4, D=−4, E=−4/3 y primitiva',
      prim(F25, (2 * x ** 2 - x + 1) / ((x ** 2 + x + 1) ** 2 * (x + 1)), PTS + [-3]), 1,
      r"\frac{-4x+1}{3(x^2+x+1)}+4\ln\lvert x+1\rvert-2\ln(x^2+x+1)+\frac{4\sqrt3}9\operatorname{arctg}\frac{2x+1}{\sqrt3}+C")
    T = tg(x / 2)
    F26 = -ln(Abs(T - 1 - sqrt(2))) / sqrt(2) + ln(Abs(T - 1 + sqrt(2))) / sqrt(2)
    tt = sp.Symbol('tt')
    c('ej-6-26', 'con t=tg(x/2) queda ∫−2/(t²−2t−1); c) es primitiva',
      lista([sp.simplify((1 / (2 * tt / (1 + tt ** 2) + (1 - tt ** 2) / (1 + tt ** 2)) * 2 / (1 + tt ** 2)) - (-2 / (tt ** 2 - 2 * tt - 1))),
             prim(F26, 1 / (sen(x) + cos(x)), [R(1, 5), R(7, 10), R(13, 10), R(-1, 2)])], [0, 1]), 1,
      r"Respuesta: b) y c).")
    c('ej-6-27', 'I = (1/4)ln(1+sen²(2x+1))',
      lista([sp.apart(tt / ((1 + 2 * tt ** 2) * (1 + tt ** 2)), tt) - (2 * tt / (1 + 2 * tt ** 2) - tt / (1 + tt ** 2)),
             prim(ln(1 + sen(2 * x + 1) ** 2) / 4, tg(2 * x + 1) / (1 + 2 * tg(2 * x + 1) ** 2), [R(1, 10), R(-1, 5), R(3, 10), 1])], [0, 1]), 1,
      r"I=\frac14\ln\big(1+\operatorname{sen}^2(2x+1)\big)+C")
    s6 = x ** R(1, 6)
    F28 = 6 * (-s6 ** 8 / 8 + s6 ** 7 / 7 + x / 6 - s6 ** 5 / 5 + sqrt(x) / 3 - s6 + atan(s6))
    c('ej-6-28', 'división y primitiva con x=t⁶',
      lista([sp.expand((t ** 2 + 1) * (-t ** 7 + t ** 6 + t ** 5 - t ** 4 + t ** 2 - 1) + 1 - (-t ** 9 + t ** 8 + t ** 5)),
             prim(F28, (1 + sqrt(x) - x ** R(2, 3)) / (1 + x ** R(1, 3)), PTS)], [0, 1]), 1,
      r"-t^9+t^8+t^5=(t^2+1)(-t^7+t^6+t^5-t^4+t^2-1)+1")
    F29 = ln(Abs((sqrt(x + 1) + sqrt(x - 1)) / (sqrt(x + 1) - sqrt(x - 1)))) + sqrt(x ** 2 - 1)
    c('ej-6-29', 'dx/dt = −4t/(t²−1)²; primitiva en x>1',
      lista([sp.simplify(sp.diff((t ** 2 + 1) / (t ** 2 - 1), t) + 4 * t / (t ** 2 - 1) ** 2), prim(F29, sqrt((x + 1) / (x - 1)), PTS)], [0, 1]), 1,
      r"+\sqrt{x^2-1}+C")
    c('ej-6-30', '∫₀¹ arcsen(x/2)/√(4−x²) = π²/72', integral(asin(x / 2) / sqrt(4 - x ** 2), 0, 1), pi ** 2 / 72, r"=\dfrac{\pi^2}{72}")
    F31 = asin((2 * x - 1) / sqrt(3)) / 2
    f31 = 1 / sqrt(3 - (2 * x - 1) ** 2)
    c('ej-6-31', '∫ = π/6 (primitiva ½·arcsen((2x−1)/√3), Barrow y cuadratura)',
      lista([prim(F31, f31, [R(3, 5), R(9, 10), R(6, 5)]), F31.subs(x, R(5, 4)) - F31.subs(x, R(1, 2)),
             si(abs(sp.N(num(f31, R(1, 2), R(5, 4)) - pi / 6)) < 1e-15)], [1, pi / 6, 1]), 1, r"\frac12\cdot\frac\pi3=\frac\pi6")
    c('ej-6-32', '∫₀^{π/2} cos²2x = π/4', integral(cos(2 * x) ** 2, 0, pi / 2), pi / 4, r"=\dfrac\pi4")
    c('ej-6-33', '(e⁴−e²)/2 ≈ 23,6', lista([integral(exp(2 * x), 1, 2), r(integral(exp(2 * x), 1, 2), 1)], [(E_ ** 4 - E_ ** 2) / 2, R('23.6')]), 1,
      r"=\dfrac{e^4-e^2}2\approx23{,}6")
    c('ej-6-34', 'áreas 1/12, 1/3, 5/12', lista([integral(x ** 2 - x ** 3, 0, 1), integral(sqrt(x) - x ** 2, 0, 1), integral(sqrt(x) - x ** 3, 0, 1)],
                                                [R(1, 12), R(1, 3), R(5, 12)]), 1, r"\frac23-\frac14=\frac5{12}")
    d35 = cos(pi * x) - sen(pi * x)
    c('ej-6-35', 'cortes −3/4, 1/4; área 4√2/π ≈ 1,80',
      lista([-integral(d35, -1, R(-3, 4)) + integral(d35, R(-3, 4), R(1, 4)) - integral(d35, R(1, 4), 1),
             r(4 * sqrt(2) / pi, 2), integral(d35, -1, 1)], [4 * sqrt(2) / pi, R('1.80'), 0]), 1, r"=\dfrac{4\sqrt2}\pi\approx1{,}80")
    # ---- Ejemplos propios
    c('p1', '∫x²cos x y ∫₀^{π/2} = π²/4−2 ≈ 0,467',
      lista([prim(x ** 2 * sen(x) + 2 * x * cos(x) - 2 * sen(x), x ** 2 * cos(x), PTS), integral(x ** 2 * cos(x), 0, pi / 2),
             r(pi ** 2 / 4 - 2, 3)], [1, pi ** 2 / 4 - 2, R('0.467')]), 1, r"\dfrac{\pi^2}4-2\approx0{,}467")
    c('p2', 'A=1, B=−1, C=0 y primitiva',
      lista([sp.apart((3 * x + 5) / ((x - 1) * (x ** 2 + 2 * x + 5))) - (1 / (x - 1) - x / (x ** 2 + 2 * x + 5)),
             prim(ln(Abs(x - 1)) - ln(x ** 2 + 2 * x + 5) / 2 + atan((x + 1) / 2) / 2, (3 * x + 5) / ((x - 1) * (x ** 2 + 2 * x + 5)), PTS + [-2])],
            [0, 1]), 1, r"=\ln\lvert x-1\rvert-\frac12\ln(x^2+2x+5)+\frac12\operatorname{arctg}\frac{x+1}2+C")
    c('p3', '∫₀³ x/√(x+1) = 8/3', lista([integral(x / sqrt(x + 1), 0, 3), integral(2 * (t ** 2 - 1), 1, 2, t)], [R(8, 3), R(8, 3)]), 1,
      r"2\Big(\frac23+\frac23\Big)=\dfrac83")
    c('p4', 'primitiva de sen⁵x cos²x; ∫₀^π sen²x = π/2',
      lista([prim(-cos(x) ** 3 / 3 + 2 * cos(x) ** 5 / 5 - cos(x) ** 7 / 7, sen(x) ** 5 * cos(x) ** 2, PTS_T),
             prim(x / 2 - sen(2 * x) / 4, sen(x) ** 2, PTS_T), integral(sen(x) ** 2, 0, pi)], [1, 1, pi / 2]), 1,
      r"-\frac{\cos^3x}3+\frac{2\cos^5x}5-\frac{\cos^7x}7+C")
    c('p4', 'definida', integral(sen(x) ** 2, 0, pi), pi / 2, r"=\dfrac\pi2")
    # ---- Exámenes
    c('x1', 'primitiva con u=1+x³', prim((1 + x ** 3) ** R(8, 3) / 8 - (1 + x ** 3) ** R(5, 3) / 5, x ** 5 * ((1 + x ** 3) ** 2) ** R(1, 3), PTS), 1,
      r"I=\dfrac18(1+x^3)^{8/3}-\dfrac15(1+x^3)^{5/3}+K")
    v2 = integral((5 * x + 3) / (x ** 2 + 2 * x + 3), 3, 5)
    F2 = R(5, 2) * ln(x ** 2 + 2 * x + 3) - sqrt(2) * atan((x + 1) / sqrt(2))
    c('x2', 'F(5)−F(3) ≈ 1,7148', lista([prim(F2, (5 * x + 3) / (x ** 2 + 2 * x + 3), PTS), si(abs(sp.N(v2 - (F2.subs(x, 5) - F2.subs(x, 3)), 25)) < 1e-15),
                                          r(v2, 4)], [1, 1, R('1.7148')]), 1,
      r"\approx1{,}7148")
    c('x3', '∫₋₂⁰(3+4x)e^{−x} = −7−e² ≈ −14,39', lista([integral((3 + 4 * x) * exp(-x), -2, 0), r(-7 - E_ ** 2, 2)], [-7 - E_ ** 2, R('-14.39')]), 1,
      r"-7-e^2\approx-14{,}39")
    c('x4', '∫₀^{π²} sen√x = 2π', lista([si(abs(sp.N(num(sen(sqrt(x)), 0, pi ** 2) - 2 * pi)) < 1e-15), integral(2 * t * sen(t), 0, pi, t)], [1, 2 * pi]), 1, r"=2\pi")
    c('x5', '∫₀^{π/2} sen⁴x cos³x = 2/35', integral(sen(x) ** 4 * cos(x) ** 3, 0, pi / 2), R(2, 35), r"=\dfrac2{35}")
    c('x6', 'primitiva con x=t²', prim(2 * (x ** R(3, 2) / 3 - x / 2 + sqrt(x) - ln(1 + sqrt(x))), x / (1 + sqrt(x)), PTS), 1,
      r"2\Big(\frac{x^{3/2}}3-\frac x2+\sqrt x-\ln(1+\sqrt x)\Big)+C")
    c('x7', 'primitiva con t=tg(x/2)', prim(ln(Abs((3 + tg(x / 2)) / (3 - tg(x / 2)))) / 3, 1 / (4 + 5 * cos(x)), PTS_T), 1,
      r"\frac13\ln\left\lvert\frac{3+\operatorname{tg}\frac x2}{3-\operatorname{tg}\frac x2}\right\rvert+C")
    # ---- Práctica «Ahora hazlo tú» (respuesta final = «Resultado: …»)
    hc = sp.symbols('ha hb hc hd')
    eqs = sp.Poly(sp.expand(sp.together(sp.diff((hc[0] * x + hc[1]) / (x ** 2 + 1), x) * (x ** 2 + 1) ** 2)
                            + (hc[2] * x + hc[3]) * (x ** 2 + 1) - (x ** 3 + 2)), x).coeffs()
    sh = sp.solve(eqs, hc)
    Fe2 = (2 * x + 1) / (2 * (x ** 2 + 1)) + ln(x ** 2 + 1) / 2 + atan(x)
    Fg2 = 2 * sqrt(x) - 3 * x ** R(1, 3) + 6 * x ** R(1, 6) - 6 * ln(1 + x ** R(1, 6))
    fg2 = 1 / (sqrt(x) + x ** R(1, 3))
    xr = sp.Symbol('xr', positive=True)
    P = {
        'pr-a1': (lista([prim(ln(x ** 2 + 3 * x + 5), (2 * x + 3) / (x ** 2 + 3 * x + 5), PTS + [-2]), sp.discriminant(x ** 2 + 3 * x + 5, x),
                         prim((x ** 3 + 1) ** 5 / 15, x ** 2 * (x ** 3 + 1) ** 4, PTS), prim(exp(tg(x)), exp(tg(x)) / cos(x) ** 2, PTS_T)],
                        [1, -11, 1, 1]), 1,
                  r"Resultado: a) $\ln(x^2+3x+5)+C$; b) $\frac{(x^3+1)^5}{15}+C$; c) $e^{\operatorname{tg}x}+C$"),
        'pr-a2': (lista([prim(ln(Abs(ln(x))), 1 / (x * ln(x)), PTS), prim(asin(2 * x / 3) / 2, 1 / sqrt(9 - 4 * x ** 2), [R(1, 5), R(-1, 2), 1, R(7, 5)]),
                         prim(-ln(Abs(cos(x))), tg(x), PTS_T + [2]), integral(tg(x), 0, pi / 4), r(ln(2) / 2, 3)],
                        [1, 1, 1, ln(2) / 2, R('0.347')]), 1,
                  r"Resultado: a) $\ln\lvert\ln x\rvert+C$; b) $\frac12\operatorname{arcsen}\frac{2x}3+C$; c) $-\ln\lvert\cos x\rvert+C$ y $\int_0^{\pi/4}\operatorname{tg}x\,dx=\frac12\ln2\approx0{,}347$"),
        'pr-b1': (lista([integral(x * (1 + x ** 2) ** 3, 0, 1), integral(t ** 3 / 2, 1, 2, t), prim(atan(exp(x)), exp(x) / (1 + exp(2 * x)), PTS + [-1])],
                        [R(15, 8), R(15, 8), 1]), 1,
                  r"Resultado: a) $\frac{15}8$; b) $\operatorname{arctg}e^x+C$"),
        'pr-b2': (lista([integral(2 * t ** 2 / (1 + t ** 2), 0, 1, t), si(abs(sp.N(num(sqrt(exp(x) - 1), 0, ln(2)) - (2 - pi / 2))) < 1e-15),
                         r(2 - pi / 2, 3), sp.diff(ln(1 + t ** 2), t)],
                        [2 - pi / 2, 1, R('0.429'), 2 * t / (1 + t ** 2)]), 1,
                  r"Resultado: $\int_0^{\ln2}\sqrt{e^x-1}\,dx=2-\frac\pi2\approx0{,}429$"),
        'pr-c1': (lista([prim(x ** 2 / 2 * ln(x) - x ** 2 / 4, x * ln(x), PTS), integral(x * cos(x), 0, pi)], [1, -2]), 1,
                  r"Resultado: a) $\frac{x^2}2\ln x-\frac{x^2}4+C$; b) $\int_0^\pi x\cos x\,dx=-2$"),
        'pr-c2': (lista([prim(x * atan(x) - ln(1 + x ** 2) / 2, atan(x), PTS + [-1]), integral(atan(x), 0, 1), r(pi / 4 - ln(2) / 2, 3),
                         prim(exp(2 * x) * (2 * sen(x) - cos(x)) / 5, exp(2 * x) * sen(x), PTS + [-1])],
                        [1, pi / 4 - ln(2) / 2, R('0.439'), 1]), 1,
                  r"Resultado: a) $x\operatorname{arctg}x-\frac12\ln(1+x^2)+C$; b) $\frac\pi4-\frac12\ln2\approx0{,}439$; c) $\frac{e^{2x}(2\operatorname{sen}x-\cos x)}5+C$"),
        'pr-d1': (lista([sp.apart((5 * x - 1) / (x ** 2 - x - 2)) - (3 / (x - 2) + 2 / (x + 1)),
                         prim(3 * ln(Abs(x - 2)) + 2 * ln(Abs(x + 1)), (5 * x - 1) / (x ** 2 - x - 2), PTS + [-3, R(1, 2)]),
                         integral((5 * x - 1) / (x ** 2 - x - 2), 3, 4), r(ln(R(25, 2)), 3)], [0, 1, ln(R(25, 2)), R('2.526')]), 1,
                  r"Resultado: $3\ln\lvert x-2\rvert+2\ln\lvert x+1\rvert+C$; $\int_3^4\frac{5x-1}{x^2-x-2}dx=\ln\frac{25}2\approx2{,}526$"),
        'pr-d2': (lista([sp.apart((x ** 3 + x + 2) / (x * (x - 1) ** 2)) - (1 + 2 / x + 4 / (x - 1) ** 2),
                         prim(x + 2 * ln(Abs(x)) - 4 / (x - 1), (x ** 3 + x + 2) / (x * (x - 1) ** 2), PTS + [-2, R(1, 2)]),
                         integral((x ** 3 + x + 2) / (x * (x - 1) ** 2), 2, 3), r(3 + 2 * ln(R(3, 2)), 3)],
                        [0, 1, 3 + 2 * ln(R(3, 2)), R('3.811')]), 1,
                  r"Resultado: $x+2\ln\lvert x\rvert-\frac4{x-1}+C$; $\int_2^3\frac{x^3+x+2}{x(x-1)^2}dx=3+2\ln\frac32\approx3{,}811$"),
        'pr-e1': (lista([prim(ln(x ** 2 + 4 * x + 8) + atan((x + 2) / 2) / 2, (2 * x + 5) / (x ** 2 + 4 * x + 8), PTS + [-2, -5]),
                         integral((2 * x + 5) / (x ** 2 + 4 * x + 8), -2, 0), r(ln(2) + pi / 8, 3)], [1, ln(2) + pi / 8, R('1.086')]), 1,
                  r"Resultado: $\ln(x^2+4x+8)+\frac12\operatorname{arctg}\frac{x+2}2+C$; $\int_{-2}^0\frac{2x+5}{x^2+4x+8}dx=\ln2+\frac\pi8\approx1{,}086$"),
        'pr-e2': (lista([sh[hc[0]], sh[hc[1]], sh[hc[2]], sh[hc[3]], prim(Fe2, (x ** 3 + 2) / (x ** 2 + 1) ** 2, PTS + [-1]),
                         integral((x ** 3 + 2) / (x ** 2 + 1) ** 2, 0, 1), r(R(1, 4) + ln(2) / 2 + pi / 4, 3)],
                        [1, R(1, 2), 1, 1, 1, R(1, 4) + ln(2) / 2 + pi / 4, R('1.382')]), 1,
                  r"Resultado: $\frac{2x+1}{2(x^2+1)}+\frac12\ln(x^2+1)+\operatorname{arctg}x+C$; $\int_0^1\frac{x^3+2}{(x^2+1)^2}dx=\frac14+\frac12\ln2+\frac\pi4\approx1{,}382$"),
        'pr-f1': (lista([prim(sen(x) - sen(x) ** 3 / 3, cos(x) ** 3, PTS_T), integral(cos(x) ** 3, 0, pi / 2), prim(tg(x) - x, tg(x) ** 2, PTS_T)],
                        [1, R(2, 3), 1]), 1,
                  r"Resultado: a) $\operatorname{sen}x-\frac{\operatorname{sen}^3x}3+C$ y $\int_0^{\pi/2}\cos^3x\,dx=\frac23$; b) $\operatorname{tg}x-x+C$"),
        'pr-f2': (lista([prim(2 / sqrt(3) * atan(tg(x / 2) / sqrt(3)), 1 / (2 + cos(x)), PTS_T + [R(5, 2), R(-29, 10)]),
                         integral(2 / (t ** 2 + 3), 0, 1, t), r(pi / (3 * sqrt(3)), 3),
                         si(abs(sp.N(num(1 / (2 + cos(x)), 0, pi / 2) - pi / (3 * sqrt(3)))) < 1e-15), si((pi / 6 < pi / (3 * sqrt(3)) < pi / 4))],
                        [1, pi / (3 * sqrt(3)), R('0.605'), 1, 1]), 1,
                  r"Resultado: $\frac2{\sqrt3}\operatorname{arctg}\frac{\operatorname{tg}(x/2)}{\sqrt3}+C$ en $(-\pi,\pi)$; $\int_0^{\pi/2}\frac{dx}{2+\cos x}=\frac\pi{3\sqrt3}\approx0{,}605$"),
        'pr-g1': (lista([integral(1 / (1 + sqrt(xr)), 0, 4, xr), integral(2 * t / (1 + t), 0, 2, t), r(4 - 2 * ln(3), 3),
                         prim(2 * sqrt(x) - 2 * ln(1 + sqrt(x)), 1 / (1 + sqrt(x)), PTS)], [4 - 2 * ln(3), 4 - 2 * ln(3), R('1.803'), 1]), 1,
                  r"Resultado: $\int_0^4\frac{dx}{1+\sqrt x}=4-2\ln3\approx1{,}803$ (primitiva $2\sqrt x-2\ln(1+\sqrt x)+C$)"),
        'pr-g2': (lista([sp.apart(6 * t ** 3 / (t + 1), t) - (6 * t ** 2 - 6 * t + 6 - 6 / (t + 1)), prim(Fg2, fg2, PTS),
                         Fg2.subs(x, 64) - Fg2.subs(x, 1), si(abs(sp.N(num(fg2, 1, 64) - (11 - 6 * ln(R(3, 2))))) < 1e-15), r(11 - 6 * ln(R(3, 2)), 3)],
                        [0, 1, 11 - 6 * ln(R(3, 2)), 1, R('8.567')]), 1,
                  r"Resultado: $2\sqrt x-3\sqrt[3]x+6\sqrt[6]x-6\ln\left(1+\sqrt[6]x\right)+C$; $\int_1^{64}\frac{dx}{\sqrt x+\sqrt[3]x}=11-6\ln\frac32\approx8{,}567$"),
    }
    for eid, (val, esp, txt) in P.items():
        if (EJ / f'{eid}.html').exists() or (EJ / f'{eid}.solucion.html').exists():
            c(eid, 'resultado de la práctica', val, esp, txt)
    return P
