r"""Tema 3.4 (Optimización. Extremos relativos y absolutos): puntos críticos, tablas de valores en intervalos cerrados,
criterios de la 1.ª/2.ª derivada y de orden superior, límites en los bordes y problemas de optimización, recalculados con sympy.

`comprobaciones(c)`: c(ejercicio, descripción, valor_sympy, esperado, trozo_latex)
  - valor_sympy: lo que calcula sympy;  esperado: lo que afirma la página;
  - trozo_latex: cadena que debe aparecer en `ejercicios/<ejercicio>.html` (o `.solucion.html`), comparada sin etiquetas,
    espacios, \, \; \! ni \displaystyle y con \dfrac/\tfrac = \frac.
Las comprobaciones de la práctica «Ahora hazlo tú» (pr-*) solo se activan cuando el ejercicio existe en `contenido/`.
"""
import pathlib

import sympy as sp

x = sp.symbols('x', real=True)
t = sp.symbols('t', real=True)
R = sp.Rational
pi = sp.pi
EJ = pathlib.Path(__file__).resolve().parents[2] / 'contenido' / 'tema_3_4' / 'ejercicios'


def crit(f, a=-sp.oo, b=sp.oo, v=x):
    """Ceros de f' en el intervalo abierto (a, b), ordenados."""
    return sorted(sp.solveset(sp.diff(f, v), v, sp.Interval.open(a, b)))


def _igual(p, q):
    p, q = sp.sympify(p), sp.sympify(q)
    if p == q:
        return True
    if isinstance(p, sp.Set) or isinstance(q, sp.Set) or sp.oo in (abs(p), abs(q)):
        return False
    return sp.simplify(p - q) == 0


def lista(vals, esperados):
    return sp.Integer(int(len(vals) == len(esperados) and all(_igual(p, q) for p, q in zip(vals, esperados))))


def vals(f, pts, v=x):
    return [sp.simplify(f.subs(v, p)) for p in pts]


def cbrt(z):
    """Raíz cúbica real (también de negativos)."""
    return sp.sign(z) * sp.Abs(z) ** R(1, 3)


def r(v, d):
    return R(str(round(float(v), d)))


def comprobaciones(c):
    # ---- Ejercicios del libro (E 3.29-3.38 y 3.44)
    c('ej-3-29', "f' tipo x³: cambia de − a + en 0 (mínimo)", lista([sp.sign((x ** 3).subs(x, -1)), sp.sign((x ** 3).subs(x, 1))], [-1, 1]), 1, r"Respuesta: a).")
    a, b, cc = sp.symbols('a b c')
    c('ej-3-30', "discriminante de f' y contraejemplo 2x³+6x", lista([sp.expand(sp.discriminant(3 * a * x ** 2 + 2 * b * x + cc, x)), sp.solveset(6 * x ** 2 + 6, x, sp.S.Reals)],
                                                               [4 * b ** 2 - 12 * a * cc, sp.S.EmptySet]), 1, r"$4b^2-12ac>0$")
    s = t ** 4 - 8 * t ** 3 + 18 * t ** 2
    v = sp.diff(s, t)
    c('ej-3-31', 'críticos de v y v(1), v(3)', lista(crit(v, 0, sp.oo, t) + vals(v, [1, 3], t), [1, 3, 16, 0]), 1, r"máximo relativo, $v(1)=16$ m/s")
    f = (1 - x ** 2) / (x + 3)
    x1 = -3 + 2 * sp.sqrt(2)
    c('ej-3-32', 'crítico y valores en [-1,1]', lista(crit(f, -1, 1) + vals(f, [-1, x1, 1]) + [sp.diff(f, x, 2).subs(x, x1)], [x1, 0, 6 - 4 * sp.sqrt(2), 0, -sp.sqrt(2) / 2]), 1,
      r"$f(x_1)=6-2\sqrt8=6-4\sqrt2\approx0{,}343$")
    A, B, C, D = sp.symbols('A B C D')
    S = A * t ** 3 + B * t ** 2 + C * t + D
    sol = sp.solve([S.subs(t, 0), S.subs(t, 1) - 10, sp.diff(S, t).subs(t, 0), sp.diff(S, t).subs(t, 5)], [A, B, C, D])
    S = S.subs(sol)
    c('ej-3-33', 'coeficientes y s(5), s(6)', lista([sol[A], sol[B], S.subs(t, 5), S.subs(t, 6)], [R(-20, 13), R(150, 13), R(1250, 13), R(1080, 13)]), 1,
      r"$s(5)=\frac{1250}{13}\approx96{,}15$")
    h = sp.symbols('h')
    c('ej-3-34', 'derivadas laterales de |x-1| en 1', lista([sp.limit((sp.Abs(1 + h - 1)) / h, h, 0, '-'), sp.limit(sp.Abs(h) / h, h, 0, '+')], [-1, 1]), 1,
      r"$|x-1|\ge0=f(1)$")
    c('ej-3-35', 'límite lateral de x^{-1/3} en 0+', sp.limit(x ** R(-1, 3), x, 0, '+'), sp.oo, r"\lim_{x\to0^+}x^{-1/3}=+\infty")
    fp = (x + 2) * (x - 1) ** 2  # modelo de f': corta en -2, toca en 1
    c('ej-3-36', "modelo de f': cambio de signo solo en -2", lista([sp.sign(fp.subs(x, -3)), sp.sign(fp.subs(x, 0)), sp.sign(fp.subs(x, 2))], [-1, 1, 1]), 1,
      r"a) correcta, b) falsa")
    V = (40 - 2 * x) ** 2 * x
    c('ej-3-37', 'crítico interior y volumen máximo', lista(crit(V, 0, 20) + [V.subs(x, R(20, 3))], [R(20, 3), R(128000, 27)]), 1, r"\tfrac{128000}{27}\approx4740{,}7")
    c('ej-3-38', 'área máxima con perímetro 100', lista(crit(x * (50 - x), 0, 50) + [625], [25, (x * (50 - x)).subs(x, 25)]), 1, r"$a=b=25$ cm")
    c('ej-3-44', "f''(1) de (x-1)²", sp.diff((x - 1) ** 2, x, 2).subs(x, 1), 2, r"$f''(1)=2>0$")
    # ---- Ejemplos propios
    f = x ** 3 - 3 * x + 1
    c('p1', 'tabla en [-2,3]', lista(crit(f, -2, 3) + vals(f, [-2, -1, 1, 3]), [-1, 1, -1, 3, -1, 19]), 1, r"Máximo absoluto $19$ en $x=3$")
    f = x * sp.exp(-x ** 2 / 2)
    c('p2', "críticos, f''(1) y f(1)", lista(crit(f) + [sp.diff(f, x, 2).subs(x, 1), f.subs(x, 1)], [-1, 1, -2 * sp.exp(R(-1, 2)), sp.exp(R(-1, 2))]), 1,
      r"$f''(1)=-2e^{-1/2}&lt;0$")
    f = x ** 5 - 5 * x ** 4
    c('p3', "críticos, f⁽⁴⁾(0) y f(4)", lista(crit(f) + [sp.diff(f, x, 2).subs(x, 0), sp.diff(f, x, 3).subs(x, 0), sp.diff(f, x, 4).subs(x, 0), f.subs(x, 4)],
                                              [0, 4, 0, 0, -120, -256]), 1, r"$f^{(4)}(0)=-120\ne0$")
    rr = sp.symbols('r', positive=True)
    Ar = 2 * pi * rr ** 2 + 2000 / rr
    r0 = sp.solve(sp.diff(Ar, rr), rr)[0]
    c('p4', 'radio óptimo y superficie mínima', lista([r(r0, 2), r(Ar.subs(rr, r0), 1), sp.simplify(1000 / (pi * r0 ** 2) / r0)], [R('5.42'), R('553.6'), 2]), 1,
      r"Superficie mínima $\approx553{,}6$ cm²")
    # ---- Exámenes
    f = (1 - x ** 2) / (x + 3)
    c('x1', "f''(x1) = -√2/2", sp.simplify(sp.diff(f, x, 2).subs(x, x1)), -sp.sqrt(2) / 2, r"$f''(x_1)=-\frac{\sqrt2}2&lt;0$")
    c('x2', 'mínimo de |x-1|', lista([sp.solveset(sp.Abs(x - 1), x, sp.S.Reals)], [sp.FiniteSet(1)]), 1, r"$|x-1|=0\iff x=1$")
    c('x3', 'x³cos(x+1) continua en [-π,π]', sp.Integer(int(sp.calculus.util.continuous_domain(x ** 3 * sp.cos(x + 1), x, sp.Interval(-pi, pi)) == sp.Interval(-pi, pi))), 1,
      r"Verdadero.")
    f = x ** 3 - 3 * x ** 2 - 9 * x + 2
    c('x4', 'críticos -1 y 3', lista(crit(f) + vals(f, [-1, 3]), [-1, 3, 7, -25]), 1, r"$f'(x)=3x^2-6x-9=3(x+1)(x-3)$")
    c('x5', 'producto máximo con suma 9', lista(crit(x * (9 - x), 0, 9) + [(x * (9 - x)).subs(x, R(9, 2))], [R(9, 2), R(81, 4)]), 1, r"producto $\tfrac{81}4=20{,}25$")
    f = x * sp.exp(-x)
    c('x6', 'tabla en [0,2]', lista(crit(f, 0, 2) + vals(f, [0, 1, 2]), [1, 0, sp.exp(-1), 2 * sp.exp(-2)]), 1, r"$f(0)=0$, $f(1)=1/e$, $f(2)=2/e^2$")
    f = x ** 4 - 2 * x ** 3
    c('x7', "f''(0)=0, f'''(0)=-12, mínimo en 3/2", lista([sp.diff(f, x, 2).subs(x, 0), sp.diff(f, x, 3).subs(x, 0), f.subs(x, R(3, 2))], [0, -12, R(-27, 16)]), 1,
      r"C) correcta (punto de silla en $0$)")
    c('x8', 'producto máximo con suma -15', lista(crit(x * (-15 - x), -15, 0) + [(x * (-15 - x)).subs(x, R(-15, 2))], [R(-15, 2), R(225, 4)]), 1,
      r"producto $\tfrac{225}4=56{,}25$")
    # ---- Práctica «Ahora hazlo tú» (respuesta final = «Resultado: …»)
    fa1 = 2 * x ** 3 - 3 * x ** 2 - 12 * x
    fa2 = x - 2 * sp.sin(x)
    fb1 = sp.Abs(x ** 2 - 4)
    gb2 = lambda z: cbrt(z) ** 2 * (z - 5)  # noqa: E731
    hc2 = lambda z: cbrt(z ** 2 - 1) ** 2  # noqa: E731
    fc1 = (x - 2) ** 2 * (x + 1)
    fd1 = sp.sin(x) + sp.cos(x)
    fd2 = sp.exp(x) - x - x ** 2 / 2
    gd2 = sp.cos(x) + x ** 2 / 2
    fe1 = x + 1 / x
    fe2 = sp.log(x) / x
    Af1 = x * (120 - 2 * x)
    Df2 = (x - 3) ** 2 + x ** 4
    aa, bb = sp.symbols('a b')
    Fg1 = x ** 3 + aa * x ** 2 + bb * x
    sg1 = sp.solve([Fg1.subs(x, 1) + 2, sp.diff(Fg1, x).subs(x, 1)], [aa, bb])
    Fg2 = x ** 2 * sp.exp(aa * x)
    ag2 = sp.solve(sp.diff(Fg2, x).subs(x, 1), aa)
    P = {
        'pr-a1': (lista(crit(fa1, -2, 3) + vals(fa1, [-2, -1, 2, 3]), [-1, 2, -4, 7, -20, -9]), 1,
                  r"Resultado: máximo absoluto $7$ en $x=-1$; mínimo absoluto $-20$ en $x=2$"),
        'pr-a2': (lista(crit(fa2, 0, pi) + vals(fa2, [0, pi / 3, pi]) + [r(fa2.subs(x, pi / 3), 3)], [pi / 3, 0, pi / 3 - sp.sqrt(3), pi, R('-0.685')]), 1,
                  r"Resultado: mínimo absoluto $\frac\pi3-\sqrt3\approx-0{,}685$ en $x=\frac\pi3$; máximo absoluto $\pi$ en $x=\pi$"),
        'pr-b1': (lista(vals(fb1, [-3, -2, 0, 1]) + [sp.diff(x ** 2 - 4, x).subs(x, -2), sp.diff(4 - x ** 2, x).subs(x, -2)], [5, 0, 4, 3, -4, 4]), 1,
                  r"Resultado: máximo absoluto $5$ en $x=-3$; mínimo absoluto $0$ en $x=-2$"),
        'pr-b2': (lista([gb2(sp.Integer(k)) for k in (-1, 0, 2, 4)] + [r(gb2(sp.Integer(2)), 2), r(gb2(sp.Integer(4)), 2)],
                        [-6, 0, -3 * 2 ** R(2, 3), -2 * 2 ** R(1, 3), R('-4.76'), R('-2.52')]), 1,
                  r"Resultado: máximo absoluto $0$ en $x=0$ (no derivable); mínimo absoluto $-6$ en $x=-1$"),
        'pr-c1': (lista([sp.factor(sp.diff(fc1, x)) - 3 * x * (x - 2)] + vals(fc1, [0, 2]), [0, 4, 0]), 1,
                  r"Resultado: máximo relativo $f(0)=4$; mínimo relativo $f(2)=0$"),
        'pr-c2': (lista([hc2(sp.Integer(k)) for k in (-1, 0, 1)] + [sp.Integer(int(all(bool(hc2(sp.Rational(q)) > 0) for q in ('-1.1', '-0.9', '0.9', '1.1')) and bool(hc2(R(1, 10)) < 1) and bool(hc2(R(-1, 10)) < 1)))],
                        [0, 1, 0, 1]), 1,
                  r"Resultado: mínimos relativos y absolutos $0$ en $x=\pm1$; máximo relativo (no absoluto) $1$ en $x=0$"),
        'pr-d1': (lista(crit(fd1, 0, 2 * pi) + [sp.diff(fd1, x, 2).subs(x, pi / 4), sp.diff(fd1, x, 2).subs(x, 5 * pi / 4)] + vals(fd1, [pi / 4, 5 * pi / 4]),
                        [pi / 4, 5 * pi / 4, -sp.sqrt(2), sp.sqrt(2), sp.sqrt(2), -sp.sqrt(2)]), 1,
                  r"Resultado: máximo relativo $\sqrt2$ en $x=\frac\pi4$; mínimo relativo $-\sqrt2$ en $x=\frac{5\pi}4$"),
        'pr-d2': (lista([sp.diff(fd2, x, k).subs(x, 0) for k in (1, 2, 3)] + [sp.diff(gd2, x, k).subs(x, 0) for k in (1, 2, 3, 4)] + [gd2.subs(x, 0)],
                        [0, 0, 1, 0, 0, 0, 1, 1]), 1,
                  r"Resultado: $f$ tiene un punto de silla en $0$ ($f'''(0)=1$); $g$ tiene un mínimo relativo $g(0)=1$ ($g^{(4)}(0)=1>0$)"),
        'pr-e1': (lista(crit(fe1, 0, sp.oo) + [sp.limit(fe1, x, 0, '+'), sp.limit(fe1, x, sp.oo), fe1.subs(x, 1)], [1, sp.oo, sp.oo, 2]), 1,
                  r"Resultado: mínimo absoluto $2$ en $x=1$; no tiene máximo absoluto"),
        'pr-e2': (lista(crit(fe2, 0, sp.oo) + [sp.limit(fe2, x, 0, '+'), sp.limit(fe2, x, sp.oo), fe2.subs(x, sp.E)], [sp.E, -sp.oo, 0, sp.exp(-1)]), 1,
                  r"Resultado: máximo absoluto $\frac1e$ en $x=e$; no tiene mínimo absoluto"),
        'pr-f1': (lista(crit(Af1, 0, 60) + vals(Af1, [0, 30, 60]) + [120 - 2 * 30], [30, 0, 1800, 0, 60]), 1,
                  r"Resultado: lados perpendiculares de $30$ m y lado paralelo de $60$ m; área máxima $1800$ m²"),
        'pr-f2': (lista(crit(Df2) + [sp.discriminant(2 * x ** 2 + 2 * x + 3, x), sp.sqrt(Df2.subs(x, 1))], [1, -20, sp.sqrt(5)]), 1,
                  r"Resultado: el punto $(1,1)$, a distancia mínima $\sqrt5$"),
        'pr-g1': (lista([sg1[aa], sg1[bb], sp.diff(Fg1.subs(sg1), x, 2).subs(x, 1)], [0, -3, 6]), 1,
                  r"Resultado: $a=0$, $b=-3$; mínimo relativo en $x=1$"),
        'pr-g2': (lista(ag2 + crit(Fg2.subs(aa, -2)) + vals(Fg2.subs(aa, -2), [0, 1]), [-2, 0, 1, 0, sp.exp(-2)]), 1,
                  r"Resultado: $a=-2$; mínimo relativo $f(0)=0$ y máximo relativo $f(1)=e^{-2}$"),
    }
    for eid, (val, esp, txt) in P.items():
        if (EJ / f'{eid}.html').exists() or (EJ / f'{eid}.solucion.html').exists():
            c(eid, 'resultado de la práctica', val, esp, txt)
