r"""Tema 6.4 (Integración numérica): rectángulos, trapecio y Simpson (simples y compuestos, convención de U: Simpson
compuesta en n subintervalos con nodos cada h/2 y factor h/6), datos en tabla, cotas del error (Teor. 6.3 y 6.4 de U) y
número de subintervalos; recalculados con sympy.

`comprobaciones(c)`: c(ejercicio, descripción, valor_sympy, esperado, trozo_latex)
  - valor_sympy: lo que calcula sympy;  esperado: lo que afirma la página;
  - trozo_latex: cadena que debe aparecer en `ejercicios/<ejercicio>.html` (o `.solucion.html`), comparada sin etiquetas,
    espacios, \, \; \! ni \displaystyle y con \dfrac/\tfrac = \frac.
Las comprobaciones de la práctica «Ahora hazlo tú» (pr-*) solo se activan cuando el ejercicio existe en `contenido/`.
"""
import math
import pathlib

import sympy as sp

R = sp.Rational
pi = sp.pi
E_ = sp.E
x = sp.Symbol('x', real=True)
EJ = pathlib.Path(__file__).resolve().parents[2] / 'contenido' / 'tema_6_4' / 'ejercicios'


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


def cerca(val, ref, tol):
    return si(abs(float(val) - float(ref)) < tol)


def integral(f, a, b):
    return sp.integrate(f, (x, a, b))


def _nodos(a, b, n):
    a, b = sp.sympify(a), sp.sympify(b)
    h = (b - a) / n
    return [a + k * h for k in range(n + 1)], h


def _v(f, t):
    return f.subs(x, t) if isinstance(f, sp.Basic) else f(t)


def izq(f, a, b, n):
    """Rectángulo izquierdo compuesto (U Def. 6.4)."""
    xs, h = _nodos(a, b, n)
    return h * sum(_v(f, t) for t in xs[:-1])


def der(f, a, b, n):
    xs, h = _nodos(a, b, n)
    return h * sum(_v(f, t) for t in xs[1:])


def cen(f, a, b, n):
    xs, h = _nodos(a, b, n)
    return h * sum(_v(f, (xs[k] + xs[k + 1]) / 2) for k in range(n))


def trap(f, a, b, n):
    """Trapecio compuesto (U Def. 6.6): h/2 (E + 2C)."""
    xs, h = _nodos(a, b, n)
    v = [_v(f, t) for t in xs]
    return h / 2 * (v[0] + v[-1] + 2 * sum(v[1:-1]))


def simp(f, a, b, n):
    """Simpson compuesta (U Def. 6.8): n subintervalos, nodos cada h/2, factor h/6."""
    xs, h2 = _nodos(a, b, 2 * n)
    h = 2 * h2
    v = [_v(f, t) for t in xs]
    return h / 6 * (v[0] + v[-1] + 2 * sum(v[2:-1:2]) + 4 * sum(v[1::2]))


def tabla_trap(ys, h):
    return R(h) / 2 * (ys[0] + ys[-1] + 2 * sum(ys[1:-1]))


def tabla_simp(ys, h):
    """Simpson compuesta sobre 2n+1 datos; h = longitud de cada subintervalo (dos pasos de la tabla)."""
    return R(h) / 6 * (ys[0] + ys[-1] + 2 * sum(ys[2:-1:2]) + 4 * sum(ys[1::2]))


def m_trap(ba, M2, tol):
    return math.ceil(math.sqrt(float(ba ** 3 * M2 / (12 * tol))) - 1e-12)


def m_simp(ba, M4, tol):
    return math.ceil((float(ba ** 5 * M4 / (2880 * tol))) ** 0.25 - 1e-12)


def interp(xs, ys):
    return sp.expand(sp.interpolate(list(zip(xs, ys)), x))


def comprobaciones(c):
    # ---- Ejercicios del libro (E 6.36-6.41)
    c('e636', 'e^{-x²} no tiene primitiva elemental (sympy la expresa con erf)',
      si(sp.integrate(sp.exp(-x ** 2), x).has(sp.erf)), 1, r"e^{-x^2}")
    c('e637', 'trapecio (42+41)/2·3 = 124,5', R(42 + 41, 2) * 3, R(249, 2), r"=41{,}5\cdot3=124{,}5")
    f38 = sp.Piecewise((3 + x, x <= 1), (4 * x, True))
    c('e638', '∫=22; trapecio n=4 → 22 (n par: exacto); n=3 → 68/3; n=1 → 28',
      lista([integral(3 + x, -1, 1) + integral(4 * x, 1, 3), trap(f38, -1, 3, 4), trap(f38, -1, 3, 2), trap(f38, -1, 3, 6),
             trap(f38, -1, 3, 3), trap(f38, -1, 3, 1)], [22, 22, 22, 22, R(68, 3), 28]), 1, r"\frac{44}2=22")
    c('e639', 'finca: 100/2·(280 + 2·525) = 66 500 m²', tabla_trap([130, 120, 125, 140, 140, 150], 100), 66500, r"=50\cdot1330=66\,500")
    c('e640', '∫₀^π cos con trapecio n=4 = 0 = exacto', lista([trap(sp.cos(x), 0, pi, 4), integral(sp.cos(x), 0, pi)], [0, 0]), 1,
      r"\frac{\pi/4}2\,(0+2\cdot0)=0")
    d41 = [40, 42, 41, 42, 41]
    c('e641', 'der. 164; der. comp. 166; trap. 162; trap. comp. 331/2; Simpson 490/3; Simpson comp. (n=2) 499/3',
      lista([41 * 4, sum(d41[1:]), R(40 + 41, 2) * 4, tabla_trap(d41, 1), R(40 + 4 * 41 + 41, 6) * 4, tabla_simp(d41, 2)],
            [164, 166, 162, R(331, 2), R(490, 3), R(499, 3)]), 1, r"\frac13\cdot499=\frac{499}3")
    # ---- Ejemplos propios
    f1 = x ** 2
    c('p1', 'x² en [0,1]: M=1/4, T=1/2, S=1/3; n=2: 5/16, 3/8, 1/3; S=(T+2M)/3',
      lista([cen(f1, 0, 1, 1), trap(f1, 0, 1, 1), simp(f1, 0, 1, 1), cen(f1, 0, 1, 2), trap(f1, 0, 1, 2), simp(f1, 0, 1, 2),
             (trap(f1, 0, 1, 1) + 2 * cen(f1, 0, 1, 1)) / 3],
            [R(1, 4), R(1, 2), R(1, 3), R(5, 16), R(3, 8), R(1, 3), R(1, 3)]), 1, r"\frac14\big(0+2\cdot\frac14+1\big)=\frac38")
    c('p2', 'Simpson: x³ en [0,2] da 4 (exacto); x⁴ en [0,1] da 5/24, error 1/120 = cota',
      lista([simp(x ** 3, 0, 2, 1), integral(x ** 3, 0, 2), simp(x ** 4, 0, 1, 1), simp(x ** 4, 0, 1, 1) - R(1, 5), R(24, 2880)],
            [4, 4, R(5, 24), R(1, 120), R(1, 120)]), 1, r"\frac{24}{2880}=\frac1{120}")
    c('p3', '1/x en [1,2], tol 1e-4: trapecio m=41 (≥40,82), Simpson m=4 (≥3,02)',
      lista([m_trap(1, 2, R(1, 10 ** 4)), m_simp(1, 24, R(1, 10 ** 4)), r(sp.sqrt(R(2, 12) * 10 ** 4), 2), r((R(24, 2880) * 10 ** 4) ** R(1, 4), 2)],
            [41, 4, R('40.82'), R('3.02')]), 1, r"m\ge40{,}82")
    f4 = sp.exp(-x ** 2)
    d4 = sp.diff(f4, x, 4)
    c('p4', 'e^{-x²}: M₄=12 (f⁽⁴⁾(0)); trapecio m=409, Simpson m=9 (≥8,03); S₉≈0,7468242',
      lista([d4.subs(x, 0), si(abs(d4.subs(x, 1)) < 12), m_trap(1, 2, R(1, 10 ** 6)), m_simp(1, 12, R(1, 10 ** 6)),
             r((R(12, 2880) * 10 ** 6) ** R(1, 4), 2), r(simp(f4, 0, 1, 9), 7)],
            [12, 1, 409, 9, R('8.03'), R('0.7468242')]), 1, r"m\ge8{,}03")
    # ---- Exámenes
    c('x1', 'trapecio con 1,2,−1,−3,0: −3/2', tabla_trap([1, 2, -1, -3, 0], 1), R(-3, 2), r"\frac12(-3)=-\frac32")
    c('x2', 'trapecio n=2: π(1+√2)/8 ≈ 0,9481; Simpson π(1+2√2)/12 ≈ 1,0023; exacto 1',
      lista([trap(sp.cos(x), 0, pi / 2, 2), simp(sp.cos(x), 0, pi / 2, 1), r(simp(sp.cos(x), 0, pi / 2, 1), 4),
             r(trap(sp.cos(x), 0, pi / 2, 2), 4), integral(sp.cos(x), 0, pi / 2)],
            [pi * (1 + sp.sqrt(2)) / 8, pi * (1 + 2 * sp.sqrt(2)) / 12, R('1.0023'), R('0.9481'), 1]), 1,
      r"\frac\pi{12}\big(1+2\sqrt2\big)\approx1{,}0023")
    f3 = x / (x ** 2 + 1) ** 2
    c('x3', 'exacto 1/4; trapecio n=2 89/400; Simpson 51/200',
      lista([integral(f3, 0, 1), trap(f3, 0, 1, 2), simp(f3, 0, 1, 1)], [R(1, 4), R(89, 400), R(51, 200)]), 1, r"=\frac{51}{200}=0{,}255")
    g = 11 * x ** 2 - 38 * x + 58
    c('x4', 'trapecio 63; Simpson 178/3 = ∫g; g pasa por los datos',
      lista([tabla_trap([31, 26, 43], 1), tabla_simp([31, 26, 43], 2), integral(g, 1, 3), [g.subs(x, k) for k in (1, 2, 3)]],
            [63, R(178, 3), R(178, 3), [31, 26, 43]]), 1, r"102-\frac{128}3=\frac{178}3")
    p5 = interp([0, 2, 4], [1, 3, 2])
    c('x5', 'p(1)=19/8; Simpson 10 = ∫₀⁴p',
      lista([p5 - (-R(3, 8) * x ** 2 + R(7, 4) * x + 1), p5.subs(x, 1), tabla_simp([1, 3, 2], 4), integral(p5, 0, 4)], [0, R(19, 8), 10, 10]), 1,
      r"=-8+14+4=10")
    f6 = x ** 2 * sp.sin(x)
    c('x6', 'exacto π²−4; Simpson π³/6 ≈ 5,1677',
      lista([integral(f6, 0, pi), simp(f6, 0, pi, 1), r(simp(f6, 0, pi, 1), 4)], [pi ** 2 - 4, pi ** 3 / 6, R('5.1677')]), 1,
      r"\frac{\pi^3}6\approx5{,}1677")
    f7 = sp.sin(x) ** 4 * sp.cos(x) ** 3
    c('x7', 'Simpson compuesta n=3 ≈ 0,05689; exacto 2/35',
      lista([r(simp(f7, 0, pi / 2, 3), 5), integral(f7, 0, pi / 2)], [R('0.05689'), R(2, 35)]), 1, r"\frac\pi{36}\cdot0{,}65190\approx0{,}05689")
    f8 = 1 / sp.sqrt(-x ** 2 + 8 * x - 7)
    c('x8', 'trapecio n=5 ≈ 0,6808; exacto 2 arcsen(1/3) ≈ 0,6797',
      lista([r(trap(f8, 3, 5, 5), 4), r(sp.Integral(f8, (x, 3, 5)).evalf(), 4), r(2 * sp.asin(R(1, 3)), 4)],
            [R('0.6808'), R('0.6797'), R('0.6797')]), 1, r"0{,}2\cdot3{,}40427\approx0{,}6808")
    p9 = interp([1, 3, 4, 8], [2, 3, 2, 10])
    c('x9', 'p(2)=116/35; Simpson compuesta n=2 sobre p = ∫₁⁴p = 2409/280',
      lista([p9.subs(x, 2), simp(p9, 1, 4, 2), integral(p9, 1, 4)], [R(116, 35), R(2409, 280), R(2409, 280)]), 1,
      r"=\frac{2409}{280}\approx8{,}6036")
    xs10, ys10 = [0, 1, 3, 7], [2, 0, -1, 4]
    c('x10', 'trapecio tramo a tramo (no equiespaciado): 1 − 1 + 6 = 6',
      sum(R(ys10[k] + ys10[k + 1], 2) * (xs10[k + 1] - xs10[k]) for k in range(3)), 6, r"=1-1+6=6")
    # ---- Práctica «Ahora hazlo tú» (respuesta final = «Resultado: …»)
    fa1 = x ** 2 + 1
    fa2 = 4 / (1 + x ** 2)
    La, Ra, Ta, Ma = izq(fa2, 0, 1, 4), der(fa2, 0, 1, 4), trap(fa2, 0, 1, 4), cen(fa2, 0, 1, 4)
    T2, T4, S2 = trap(sp.exp(x), 0, 1, 2), trap(sp.exp(x), 0, 1, 4), simp(sp.exp(x), 0, 1, 2)
    fc1 = 1 / (1 + x ** 2)
    fc2 = x * sp.sin(x)
    vd1 = [0, 12, 20, 25, 28, 30, 31]
    yd2 = [R(1), R('1.4'), R('1.6'), R('1.5'), R('1.2'), R('0.8')]
    fe2 = sp.exp(x ** 2)
    Ie2 = sp.Integral(fe2, (x, 0, 1)).evalf(20)
    fg1 = 2 * x ** 3 - x ** 2 + 1
    A, B, C = sp.symbols('A B C')
    sg2 = sp.solve([A + B + C - 2, B + 2 * C - 2, B + 4 * C - R(8, 3)], [A, B, C])
    qg2 = lambda p: sg2[A] * p.subs(x, 0) + sg2[B] * p.subs(x, 1) + sg2[C] * p.subs(x, 2)  # noqa: E731
    P = {
        'pr-a1': (lista([izq(fa1, 0, 2, 4), der(fa1, 0, 2, 4), cen(fa1, 0, 2, 4), integral(fa1, 0, 2),
                         izq(fa1, 0, 2, 4) - R(14, 3), der(fa1, 0, 2, 4) - R(14, 3), cen(fa1, 0, 2, 4) - R(14, 3)],
                        [R(15, 4), R(23, 4), R(37, 8), R(14, 3), R(-11, 12), R(13, 12), R(-1, 24)]), 1,
                  r"Resultado: izquierdo $\frac{15}4$, derecho $\frac{23}4$, central $\frac{37}8$; exacto $\frac{14}3$ (el central es el más cercano)"),
        'pr-a2': (lista([integral(fa2, 0, 1), r(La, 4), r(Ra, 4), (La + Ra) / 2 - Ta, r(Ta, 4), r(Ma, 4), si(Ra < pi < La),
                         r(Ta - pi, 4), r(Ma - pi, 4)],
                        [pi, R('3.3812'), R('2.8812'), 0, R('3.1312'), R('3.1468'), 1, R('-0.0104'), R('0.0052')]), 1,
                  r"Resultado: $I=\pi$; $I_{\text{izq}}\approx3{,}3812$, $I_{\text{der}}\approx2{,}8812$, luego $2{,}8812&lt;I&lt;3{,}3812$; $T_4=\frac{I_{\text{izq}}+I_{\text{der}}}2\approx3{,}1312$; $I_{\text{cen}}\approx3{,}1468$"),
        'pr-b1': (lista([trap(1 / x, 1, 3, 4), integral(1 / x, 1, 3), r(trap(1 / x, 1, 3, 4) - sp.log(3), 4), si(sp.diff(1 / x, x, 2).subs(x, 3) > 0)],
                        [R(67, 60), sp.log(3), R('0.0181'), 1]), 1,
                  r"Resultado: $T_4=\frac{67}{60}\approx1{,}1167$; exacto $\ln3\approx1{,}0986$; error $\approx0{,}0181$ (por exceso)"),
        'pr-b2': (lista([r(T2, 4), r(T4, 4), r(T2 - E_ + 1, 4), r(T4 - E_ + 1, 4), r((T2 - E_ + 1) / (T4 - E_ + 1), 0),
                         sp.expand((4 * T4 - T2) / 3 - S2), r(S2, 6), integral(sp.exp(x), 0, 1)],
                        [R('1.7539'), R('1.7272'), R('0.0356'), R('0.0089'), 4, 0, R('1.718319'), E_ - 1]), 1,
                  r"Resultado: $T_2\approx1{,}7539$, $T_4\approx1{,}7272$; errores $\approx0{,}0356$ y $\approx0{,}0089$ (cociente $\approx4$); $\frac{4T_4-T_2}3\approx1{,}718319=S_2$; exacto $e-1\approx1{,}718282$"),
        'pr-c1': (lista([simp(fc1, 0, 1, 1), simp(fc1, 0, 1, 2), integral(fc1, 0, 1), r(simp(fc1, 0, 1, 2), 6)],
                        [R(47, 60), R(8011, 10200), pi / 4, R('0.785392')]), 1,
                  r"Resultado: $S_1=\frac{47}{60}\approx0{,}78333$; $S_2=\frac{8011}{10200}\approx0{,}785392$; exacto $\frac\pi4\approx0{,}785398$"),
        'pr-c2': (lista([integral(fc2, 0, pi), simp(fc2, 0, pi, 1), simp(fc2, 0, pi, 2), r(simp(fc2, 0, pi, 1), 4), r(simp(fc2, 0, pi, 2), 4),
                         r((simp(fc2, 0, pi, 1) - pi) / (simp(fc2, 0, pi, 2) - pi), 0)],
                        [pi, pi ** 2 / 3, pi ** 2 * (1 + 2 * sp.sqrt(2)) / 12, R('3.2899'), R('3.1488'), 21]), 1,
                  r"Resultado: exacto $\pi$; $S_1=\frac{\pi^2}3\approx3{,}2899$; $S_2=\frac{\pi^2(1+2\sqrt2)}{12}\approx3{,}1488$; el error se divide entre $\approx21$"),
        'pr-d1': (lista([tabla_trap(vd1, 10), tabla_simp(vd1, 20)], [1305, R(3950, 3)]), 1,
                  r"Resultado: trapecio $1305$ m; Simpson compuesta ($n=3$) $\frac{3950}3\approx1316{,}7$ m"),
        'pr-d2': (lista([tabla_trap(yd2, R(1, 2)), si(len(yd2) % 2 == 0), tabla_simp(yd2[:5], 1), tabla_trap(yd2[4:], R(1, 2)),
                         tabla_simp(yd2[:5], 1) + tabla_trap(yd2[4:], R(1, 2))],
                        [R(33, 10), 1, R(17, 6), R(1, 2), R(10, 3)]), 1,
                  r"Resultado: a) $3{,}3$; b) no: hay $6$ nodos (número par); c) $\frac{17}6+\frac12=\frac{10}3\approx3{,}3333$"),
        'pr-e1': (lista([pi ** 3 / (12 * 4 ** 2), pi ** 5 / (2880 * 4 ** 4), r(pi ** 3 / 192, 4), r(pi ** 5 / 737280 * 10 ** 4, 2),
                         si(abs(trap(sp.sin(x), 0, pi, 4) - 2) < pi ** 3 / 192), si(abs(simp(sp.sin(x), 0, pi, 4) - 2) < pi ** 5 / 737280)],
                        [pi ** 3 / 192, pi ** 5 / 737280, R('0.1615'), R('4.15'), 1, 1]), 1,
                  r"Resultado: trapecio $\varepsilon\le\frac{\pi^3}{192}\approx0{,}1615$; Simpson $\varepsilon\le\frac{\pi^5}{737280}\approx4{,}15\cdot10^{-4}$"),
        'pr-e2': (lista([sp.factor(sp.diff(fe2, x, 2)), sp.factor(sp.diff(fe2, x, 4)), sp.diff(fe2, x, 2).subs(x, 1), sp.diff(fe2, x, 4).subs(x, 1),
                         6 * E_ / (12 * 100), 76 * E_ / (2880 * 625), r(E_ / 200, 4), r(19 * E_ / 450000 * 10 ** 4, 2),
                         si(abs(trap(fe2, 0, 1, 10) - Ie2) < E_ / 200), si(abs(simp(fe2, 0, 1, 5) - Ie2) < 19 * E_ / 450000)],
                        [2 * (2 * x ** 2 + 1) * sp.exp(x ** 2), 4 * (4 * x ** 4 + 12 * x ** 2 + 3) * sp.exp(x ** 2), 6 * E_, 76 * E_,
                         E_ / 200, 19 * E_ / 450000, R('0.0136'), R('1.15'), 1, 1]), 1,
                  r"Resultado: $M_2=6e$, $M_4=76e$; trapecio ($n=10$) $\varepsilon\le\frac e{200}\approx0{,}0136$; Simpson ($n=5$) $\varepsilon\le\frac{19e}{450000}\approx1{,}15\cdot10^{-4}$; los dos usan $11$ nodos"),
        'pr-f1': (lista([m_trap(1, 1, R(1, 10 ** 3)), m_simp(1, 1, R(1, 10 ** 6)), 2 * 5 + 1,
                         si(abs(trap(sp.cos(x), 0, 1, 10) - sp.sin(1)) < R(1, 10 ** 3)), si(abs(simp(sp.cos(x), 0, 1, 5) - sp.sin(1)) < R(1, 10 ** 6))],
                        [10, 5, 11, 1, 1]), 1,
                  r"Resultado: trapecio $m=10$ ($11$ nodos); Simpson $m=5$ ($11$ nodos)"),
        'pr-f2': (lista([m_trap(2, 1, R(1, 10 ** 4)), m_simp(2, 6, R(1, 10 ** 4)), si(R(8, 12 * 81 ** 2) > R(1, 10 ** 4)),
                         si(R(192, 2880 * 5 ** 4) > R(1, 10 ** 4)), integral(sp.log(x), 1, 3), sp.diff(sp.log(x), x, 2).subs(x, 1),
                         sp.diff(sp.log(x), x, 4).subs(x, 1)],
                        [82, 6, 1, 1, 3 * sp.log(3) - 2, -1, -6]), 1,
                  r"Resultado: $M_2=1$, $M_4=6$; trapecio $m=82$ subintervalos; Simpson $m=6$ subintervalos"),
        'pr-g1': (lista([integral(fg1, -1, 1), trap(fg1, -1, 1, 1), cen(fg1, -1, 1, 1), simp(fg1, -1, 1, 1), sp.diff(fg1, x, 4),
                         (trap(fg1, -1, 1, 1) + 2 * cen(fg1, -1, 1, 1)) / 3],
                        [R(4, 3), 0, 2, R(4, 3), 0, R(4, 3)]), 1,
                  r"Resultado: exacto $\frac43$; trapecio $0$; punto medio $2$; Simpson $\frac43$ (exacto, porque $f^{(4)}=0$)"),
        'pr-g2': (lista([sg2[A], sg2[B], sg2[C], qg2(x ** 3), integral(x ** 3, 0, 2), qg2(x ** 4), integral(x ** 4, 0, 2),
                         qg2(x ** 4) - integral(x ** 4, 0, 2), R(2 ** 5, 2880) * 24],
                        [R(1, 3), R(4, 3), R(1, 3), 4, 4, R(20, 3), R(32, 5), R(4, 15), R(4, 15)]), 1,
                  r"Resultado: $A=C=\frac13$, $B=\frac43$ (Simpson); exacta para $x^3$ ($4=4$); para $x^4$ da $\frac{20}3\ne\frac{32}5$ (error $\frac4{15}$, igual a la cota)"),
    }
    for eid, (val, esp, txt) in P.items():
        if (EJ / f'{eid}.html').exists() or (EJ / f'{eid}.solucion.html').exists():
            c(eid, 'resultado de la práctica', val, esp, txt)
    return P
