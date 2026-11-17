r"""Tema 6.2 (Teoremas fundamentales del Cálculo): primer teorema (derivar funciones definidas por una integral, límites
variables, monotonía y extremos), regla de Barrow y su hipótesis de continuidad, valor medio integral; recalculados con sympy.

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
u = sp.Symbol('u', real=True)
xp = sp.Symbol('x', positive=True)
tp = sp.Symbol('t', positive=True)
h = sp.Symbol('h', positive=True)
EJ = pathlib.Path(__file__).resolve().parents[2] / 'contenido' / 'tema_6_2' / 'ejercicios'


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


def deriva_integral(f, a, b):
    """d/dx ∫_{a(x)}^{b(x)} f(t) dt por la fórmula de E 6.15."""
    return sp.simplify(f.subs(t, b) * sp.diff(b, x) - f.subs(t, a) * sp.diff(a, x))


def comprobaciones(c):
    # ---- Ejercicios del libro (E 6.11-6.16)
    F, C = x, sp.Integer(1)  # f = 1, F = x
    c('ej-6-11', "con f=1, F=x, C=1: (F+C)'=f (a); (f+C)'=0≠F (b); (1+C)'=0≠x (c)",
      lista([sp.diff(F + C, x), sp.diff(1 + C, x), integral(t, 0, x, t)], [1, 0, x ** 2 / 2]), 1, r"Respuesta: a).")
    Fu = sp.integrate(sp.sin(sp.log(tp)), (tp, 0, xp))
    H = Fu.subs(xp, sp.exp(x))
    H1 = sp.simplify(sp.diff(H, x))
    H2 = sp.diff(H1, x)
    c('ej-6-12', "H'=eˣsen x; H''(3π/4)=0, H'''(3π/4)=−√2e^{3π/4}; H''(π)<0; ∫₀¹sen(ln t)=−1/2",
      lista([sp.simplify(H1 - sp.exp(x) * sp.sin(x)), sp.simplify(H2.subs(x, 3 * pi / 4)), sp.simplify(sp.diff(H2, x).subs(x, 3 * pi / 4)),
             sp.sign(H2.subs(x, pi)), Fu.subs(xp, 1), r(H2.subs(x, 3 * pi / 4 - R(1, 10)), 2), r(H2.subs(x, 3 * pi / 4 + R(1, 10)), 2)],
            [0, 0, -sp.sqrt(2) * sp.exp(3 * pi / 4), -1, R(-1, 2), R('1.35'), R('-1.65')]), 1,
      r"H'''\!\left(\frac{3\pi}4\right)=-\sqrt2\,e^{3\pi/4}\lt0")
    F13 = integral(t * sp.sin(t), 0, x, t)
    c('ej-6-13', "F'=x sen x; F''(7π)=−7π; F(7π)=7π < F(9π)=9π",
      lista([sp.diff(F13, x) - x * sp.sin(x), sp.diff(F13, x, 2).subs(x, 7 * pi), F13.subs(x, 7 * pi), F13.subs(x, 9 * pi)],
            [0, -7 * pi, 7 * pi, 9 * pi]), 1, r"F''(7\pi)=-7\pi\lt0")
    c('ej-6-14', 'd/dx ∫ₓ¹t² = −x²', lista([sp.diff(integral(t ** 2, x, 1, t), x), deriva_integral(t ** 2, x, sp.Integer(1))],
                                          [-x ** 2, -x ** 2]), 1, r"G'(x)=-x^2")
    d15 = sp.exp(x) * sp.cos(sp.exp(x)) - 2 * x * sp.cos(x ** 2)
    c('ej-6-15', "d/dx ∫_{x²}^{eˣ}cos t = eˣcos(eˣ) − 2x cos(x²)",
      lista([sp.diff(integral(sp.cos(t), x ** 2, sp.exp(x), t), x) - d15, deriva_integral(sp.cos(t), x ** 2, sp.exp(x)) - d15], [0, 0]), 1,
      r"e^x\cos(e^x)-2x\cos(x^2)")
    c('ej-6-16', '∫₂³dx/(x−1)=ln 2; 1∈[0,2] (no continua)', lista([integral(1 / (x - 1), 2, 3), si((0 < 1 < 2))], [sp.log(2), 1]), 1,
      r"\int_2^3\frac{dx}{x-1}=\ln2-\ln1=\ln2")
    # ---- Ejemplos propios
    G1 = integral(1 / (1 + t ** 2), x, x ** 2, t)
    N1 = sp.Integral(sp.sin(t ** 2), (t, 0, x))
    c('p1', "G'(x)=2x/(1+x⁴)−1/(1+x²), G'(1)=1/2; límite 1/3",
      lista([sp.simplify(sp.diff(G1, x) - (2 * x / (1 + x ** 4) - 1 / (1 + x ** 2))), sp.diff(G1, x).subs(x, 1),
             sp.limit(sp.integrate(sp.sin(t ** 2), (t, 0, x)) / x ** 3, x, 0), sp.limit(sp.diff(N1, x).doit() / (3 * x ** 2), x, 0)],
            [0, R(1, 2), R(1, 3), R(1, 3)]), 1, r"G'(1)=\frac22-\frac12=\frac12")
    c('p2', '∫₁⁴(3√x−2/x²)=25/2; ∫_ε¹dx/x² = 1/ε − 1 → ∞',
      lista([integral(3 * sp.sqrt(x) - 2 / x ** 2, 1, 4), sp.limit(sp.integrate(1 / tp ** 2, (tp, h, 1)), h, 0, '+')], [R(25, 2), sp.oo]), 1,
      r"\frac{33}2-4=\frac{25}2")
    m2 = integral(sp.sin(x), 0, pi) / pi
    c('p3', 'valor medio 3 (c=√3) y 2/π (c≈0,690 y 2,451)',
      lista([integral(x ** 2, 0, 3) / 3, sp.solve(sp.Eq(xp ** 2, 3), xp)[0], m2, r(sp.asin(m2), 3), r(pi - sp.asin(m2), 3)],
            [3, sp.sqrt(3), 2 / pi, R('0.690'), R('2.451')]), 1, r"c_2=\pi-\arcsin\frac2\pi\approx2{,}451")
    fp4 = sp.Piecewise((x ** 2, x <= 1), (2 - x, True))
    c('p4', '∫|x²−2x| = 4 (tres trozos de 4/3); sin |·|: 4/3; a trozos: 5/6',
      lista([integral(x ** 2 - 2 * x, -1, 0), -integral(x ** 2 - 2 * x, 0, 2), integral(x ** 2 - 2 * x, 2, 3), integral(sp.Abs(x ** 2 - 2 * x), -1, 3),
             integral(x ** 2 - 2 * x, -1, 3), integral(fp4, 0, 2)], [R(4, 3), R(4, 3), R(4, 3), 4, R(4, 3), R(5, 6)]), 1,
      r"\frac13+\frac12=\frac56")
    # ---- Exámenes
    c('x1', "F''(7π) = −7π < 0 → B", lista([sp.diff(t * sp.sin(t), t).subs(t, 7 * pi)], [-7 * pi]), 1, r"F''(7\pi)=-7\pi\lt0")
    s = sp.Symbol('s', real=True)
    F2 = integral(sp.exp(-s), 0, x, s)
    c('x2', "F=1−e^{−x}, F'=e^{−x}>0 con f=e^{−x} decreciente",
      lista([F2, sp.diff(sp.exp(-x), x), sp.diff(F2, x)], [1 - sp.exp(-x), -sp.exp(-x), sp.exp(-x)]), 1, r"F(x)=\int_0^xe^{-s}\,ds=1-e^{-x}")
    F3 = integral(-sp.exp(-t), 0, x, t)
    c('x3', "F=e^{−x}−1 decreciente con f=−e^{−x} creciente",
      lista([F3, sp.diff(-sp.exp(-x), x), sp.diff(F3, x), integral(-1 / tp ** 2, 1, xp, tp)], [sp.exp(-x) - 1, sp.exp(-x), -sp.exp(-x), 1 / xp - 1]), 1,
      r"F(x)=\int_0^x(-e^{-t})\,dt=e^{-x}-1")
    F4 = R(3, 4) * sp.sin(x) ** R(4, 3)
    c('x4', "F=¾ sen^{4/3}x es primitiva; ∫₀^π = 0 → A",
      lista([sp.simplify(sp.diff(F4, x) - sp.cos(x) * sp.sin(x) ** R(1, 3)), F4.subs(x, pi) - F4.subs(x, 0),
             sp.Integral(sp.cos(x) * sp.cbrt(sp.sin(x)), (x, 0, pi)).evalf() < 1e-12], [0, 0, True]), 1,
      r"\int_0^\pi=F(\pi)-F(0)=\frac34\cdot0-\frac34\cdot0=0")
    I5 = integral(sp.tan(x), 0, pi / 4)
    c('x5', '∫₀^{π/4} tg x = ln2/2 = ln4/4 → A y B', lista([I5, sp.log(4) / 4, r(I5, 4)], [sp.log(2) / 2, sp.log(2) / 2, R('0.3466')]), 1,
      r"\int_0^{\pi/4}\operatorname{tg}x\,dx=-\ln\frac{\sqrt2}2+\ln1=\ln\sqrt2=\frac{\ln2}2")
    e = sp.Symbol('e', positive=True)
    c('x6', '∫_ε^{π/2} cos/√sen = 2 − 2√sen ε → 2 → C',
      lista([sp.simplify(sp.diff(2 * sp.sqrt(sp.sin(x)), x) - sp.cos(x) / sp.sqrt(sp.sin(x))),
             sp.limit(2 - 2 * sp.sqrt(sp.sin(e)), e, 0, '+'), r(sp.Integral(sp.cos(x) / sp.sqrt(sp.sin(x)), (x, 0, pi / 2)).evalf(), 6)],
            [0, 2, 2]), 1, r"\lim_{\varepsilon\to0^+}\left(2-2\sqrt{\operatorname{sen}\varepsilon}\right)=2")
    # ---- Práctica «Ahora hazlo tú» (respuesta final = «Resultado: …»)
    Ga1 = integral(t ** 3 - 4 * t, x, 3, t)
    Fa2 = lambda v: sp.Piecewise((0, v <= 0), (v, True))  # noqa: E731
    Ga2 = integral(sp.Abs(t), -1, x, t)
    Gp = sp.Piecewise(((1 - x ** 2) / 2, x <= 0), ((1 + x ** 2) / 2, True))
    Hb1 = deriva_integral(1 / (1 + t ** 3), sp.Integer(0), x ** 2)
    Kb1 = sp.integrate(1 / tp, (tp, 1, xp ** 3))
    Gb2 = sp.integrate(1 / tp, (tp, xp, 3 * xp))
    Jb2 = integral(t ** 2 - 2 * t, x, x + 2, t)
    fc1 = (x - 2) / (1 + x ** 2)
    Fc1 = integral(fc1.subs(x, t), 0, x, t)
    Fc2 = sp.integrate(sp.log(tp) / tp, (tp, 1, xp))
    Fc2pp = sp.diff(sp.log(xp) / xp, xp)
    Nd2 = sp.integrate(sp.atan(tp), (tp, 0, xp ** 2))
    Nd2b = sp.integrate(sp.exp(t ** 2), (t, 0, xp))
    Ff1 = x ** 3 / 3 - x
    ff2 = sp.Piecewise((sp.exp(x), x <= 0), (1 - x, True))
    a = sp.Symbol('a', real=True)
    P = {
        'pr-a1': (lista([sp.diff(Ga1, x), sp.diff(Ga1, x).subs(x, 1), sp.sqrt(1 + 0 ** 4), integral(sp.sqrt(1 + t ** 4), 2, 2, t)],
                        [4 * x - x ** 3, 3, 1, 0]), 1,
                  r"Resultado: $F'(x)=\sqrt{1+x^4}$, $F'(0)=1$, $F(2)=0$; $G'(x)=4x-x^3$, $G'(1)=3$"),
        'pr-a2': (lista([sp.limit((Fa2(-h) - Fa2(0)) / (-h), h, 0), sp.limit((Fa2(h) - Fa2(0)) / h, h, 0), sp.limit(Fa2(h), h, 0),
                         integral(1, 0, xp), sp.simplify(Ga2 - Gp).subs(x, R(-1, 2)), sp.simplify(Ga2 - Gp).subs(x, R(3, 2)),
                         sp.limit((Gp.subs(x, h) - Gp.subs(x, 0)) / h, h, 0), sp.limit((Gp.subs(x, -h) - Gp.subs(x, 0)) / (-h), h, 0)],
                        [0, 1, 0, xp, 0, 0, 0, 0]), 1,
                  r"Resultado: $F(x)=0$ si $x\le0$ y $F(x)=x$ si $x&gt;0$; $F$ es continua pero no derivable en $0$ y $F'=f$ en todo $x\ne0$; $G'(x)=|x|$ para todo $x$, $G'(0)=0$"),
        'pr-b1': (lista([Hb1 - 2 * x / (1 + x ** 6), Hb1.subs(x, 1), Kb1 - 3 * sp.log(xp), sp.diff(Kb1, xp)], [0, 1, 0, 3 / xp]), 1,
                  r"Resultado: $H'(x)=\frac{2x}{1+x^6}$, $H'(1)=1$; $K'(x)=\frac3x$ (y $K(x)=3\ln x$)"),
        'pr-b2': (lista([Gb2, sp.diff(Gb2, xp), sp.expand(Jb2), sp.diff(Jb2, x), sp.solve(sp.diff(Jb2, x), x), Jb2.subs(x, 0)],
                        [sp.log(3), 0, 2 * x ** 2 - R(4, 3), 4 * x, [0], R(-4, 3)]), 1,
                  r"Resultado: $G'(x)=0$ y $G(x)=\ln3$ para todo $x&gt;0$; $J'(x)=4x$, mínimo en $x=0$ con $J(0)=-\frac43$"),
        'pr-c1': (lista([sp.diff(Fc1, x) - fc1, sp.solve(fc1, x), sp.sign(fc1.subs(x, 0)), sp.sign(fc1.subs(x, 3)), Fc1.subs(x, 2),
                         r(Fc1.subs(x, 2), 3), sp.limit(Fc1, x, sp.oo)],
                        [0, [2], -1, 1, sp.log(5) / 2 - 2 * sp.atan(2), R('-1.410'), sp.oo]), 1,
                  r"Resultado: $F$ decrece en $(-\infty,2]$ y crece en $[2,\infty)$; mínimo absoluto en $x=2$, $F(2)=\frac12\ln5-2\operatorname{arctg}2\approx-1{,}410$; no tiene máximo absoluto"),
        'pr-c2': (lista([Fc2, sp.simplify(Fc2pp - (1 - sp.log(xp)) / xp ** 2), sp.solve(Fc2pp, xp), sp.sign(Fc2pp.subs(xp, 2)),
                         sp.sign(Fc2pp.subs(xp, 4)), Fc2.subs(xp, E_), Fc2.subs(xp, 1)],
                        [sp.log(xp) ** 2 / 2, 0, [E_], 1, -1, R(1, 2), 0]), 1,
                  r"Resultado: decrece en $(0,1]$, crece en $[1,\infty)$, mínimo absoluto en $x=1$ con $F(1)=0$; convexa en $(0,e]$, cóncava en $[e,\infty)$, inflexión en $x=e$; $F(x)=\frac{(\ln x)^2}2$"),
        'pr-d1': (lista([sp.limit(sp.integrate(sp.cos(t ** 2), (t, 0, x)) / x, x, 0), sp.limit(integral(sp.exp(t) - 1, 0, x, t) / x ** 2, x, 0)],
                        [1, R(1, 2)]), 1, r"Resultado: a) $1$; b) $\frac12$"),
        'pr-d2': (lista([sp.limit(Nd2 / xp ** 4, xp, 0), sp.limit(xp * sp.exp(-xp ** 2) * Nd2b, xp, sp.oo),
                         sp.simplify(sp.diff(sp.exp(xp ** 2) / xp, xp) - sp.exp(xp ** 2) * (2 * xp ** 2 - 1) / xp ** 2)], [R(1, 2), R(1, 2), 0]), 1,
                  r"Resultado: a) $\frac12$; b) $\frac12$"),
        'pr-e1': (lista([integral(3 * x ** 2 - 4 * x + 1, -1, 2), integral(sp.sin(x), 0, pi / 3), integral(sp.exp(2 * x), 0, 1), r((E_ ** 2 - 1) / 2, 3)],
                        [6, R(1, 2), (E_ ** 2 - 1) / 2, R('3.195')]), 1, r"Resultado: a) $6$; b) $\frac12$; c) $\frac{e^2-1}2$"),
        'pr-e2': (lista([integral(x / (1 + x ** 2), 0, 1), integral(x * sp.exp(-x ** 2), 0, 1), integral(sp.cos(x) ** 2, 0, pi),
                         r((1 - sp.exp(-1)) / 2, 3)], [sp.log(2) / 2, (1 - sp.exp(-1)) / 2, pi / 2, R('0.316')]), 1,
                  r"Resultado: a) $\frac{\ln2}2$; b) $\frac{1-e^{-1}}2$; c) $\frac\pi2$"),
        'pr-f1': (lista([integral(x ** 2 - 1, 0, 2), Ff1.subs(x, 1) - Ff1.subs(x, 0), Ff1.subs(x, 2) - Ff1.subs(x, 1),
                         integral(1 - x ** 2, 0, 1) + integral(x ** 2 - 1, 1, 2)], [R(2, 3), R(-2, 3), R(4, 3), 2]), 1,
                  r"Resultado: $\int_0^2(x^2-1)\,dx=\frac23$; área $=2$"),
        'pr-f2': (lista([sp.cos(pi / 2), si((0 < pi / 2 < pi)), sp.simplify(sp.diff(sp.atan(x / 2) / 2, x) - 1 / (4 + x ** 2)),
                         integral(1 / (4 + x ** 2), -2, 2), sp.exp(0) - (1 - 0), integral(ff2, -1, 2), integral(1 - x, 0, 2)],
                        [0, 1, 0, pi / 4, 0, 1 - sp.exp(-1), 0]), 1,
                  r"Resultado: a) no es correcto ($x=\frac\pi2$ está en $[0,\pi]$); b) $\frac\pi4$; c) $1-e^{-1}$"),
        'pr-g1': (lista([sp.diff(x ** 2 - 2 * x - 3, x), sorted(sp.solve(a ** 2 - 2 * a - 3, a)), sp.expand(integral(2 * t - 2, 3, x, t)),
                         sp.expand(integral(2 * t - 2, -1, x, t))], [2 * x - 2, [-1, 3], x ** 2 - 2 * x - 3, x ** 2 - 2 * x - 3]), 1,
                  r"Resultado: $f(x)=2x-2$; $a=3$ o $a=-1$"),
        'pr-g2': (lista([sp.simplify(1 + 2 * integral(sp.exp(2 * t), 0, x, t) - sp.exp(2 * x)),
                         sp.simplify(integral(t * (2 * sp.sin(t) + t * sp.cos(t)), 0, x, t) - x ** 2 * sp.sin(x)),
                         sp.limit(2 * sp.sin(x) + x * sp.cos(x), x, 0)], [0, 0, 0]), 1,
                  r"Resultado: a) $f(x)=e^{2x}$ (la única); b) $f(x)=2\operatorname{sen}x+x\cos x$"),
    }
    for eid, (val, esp, txt) in P.items():
        if (EJ / f'{eid}.html').exists() or (EJ / f'{eid}.solucion.html').exists():
            c(eid, 'resultado de la práctica', val, esp, txt)
    return P
