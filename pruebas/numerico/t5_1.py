r"""Tema 5.1 (Diferencial de una función. Función diferenciable. Plano tangente): parciales, cociente de
diferenciabilidad Q, planos tangentes, diferenciales y aproximaciones, recalculados con sympy.

`comprobaciones(c)`: c(ejercicio, descripción, valor_sympy, esperado, trozo_latex)
  - valor_sympy: lo que calcula sympy;  esperado: lo que afirma la página;
  - trozo_latex: cadena que debe aparecer en `ejercicios/<ejercicio>.html` (o `.solucion.html`), comparada sin etiquetas,
    espacios, \, \; \! ni \displaystyle y con \dfrac/\tfrac = \frac.
Las comprobaciones de la práctica «Ahora hazlo tú» (pr-*) solo se activan cuando el ejercicio existe en `contenido/`.
Cociente de U Def. 5.1 (p.189): Q = [f(a+h,b+k) − f(a,b) − ∇f(a,b)·(h,k)] / √(h²+k²); polares h = ρ cos θ, k = ρ sen θ.
"""
import math
import pathlib

import sympy as sp

R = sp.Rational
pi = sp.pi
E_ = sp.E
x, y, z, h, k, t, a, b = sp.symbols('x y z h k t a b', real=True)
rho = sp.symbols('rho', positive=True)
th = sp.symbols('theta', real=True)
EJ = pathlib.Path(__file__).resolve().parents[2] / 'contenido' / 'tema_5_1' / 'ejercicios'


def _igual(p, q):
    p, q = sp.sympify(p), sp.sympify(q)
    if p == q:
        return True
    return sp.simplify(p - q) == 0


def lista(vals, esperados):
    return sp.Integer(int(len(vals) == len(esperados) and all(_igual(p, q) for p, q in zip(vals, esperados))))


def r(v, d):
    return R(str(round(float(v), d)))


def grad(f, punto, vs=(x, y)):
    return [sp.simplify(sp.diff(f, v).subs(dict(zip(vs, punto)))) for v in vs]


def pol(F):
    """F(h,k) en polares h = ρ cos θ, k = ρ sen θ, simplificada."""
    return sp.simplify(sp.trigsimp(F.subs({h: rho * sp.cos(th), k: rho * sp.sin(th)}, simultaneous=True)))


def cociente(f, f0, gr, a0=0, b0=0):
    """Q(h,k) de la Def. 5.1 en (a0,b0) con f(a0,b0) = f0 y gradiente gr (f es la fórmula fuera del punto)."""
    return (f.subs({x: a0 + h, y: b0 + k}, simultaneous=True) - f0 - gr[0] * h - gr[1] * k) / sp.sqrt(h ** 2 + k ** 2)


def cota(F, g, n=73, var='polar'):
    """|F| ≤ g en una rejilla: var='polar' → F(ρ,θ), g(ρ); var='hk' → F(h,k), g(h,k) (puntos ≠ (0,0))."""
    if var == 'polar':
        fF, fg = sp.lambdify((rho, th), F, 'math'), sp.lambdify(rho, g, 'math')
        ok = all(abs(fF(rr, 2 * math.pi * j / (n - 1))) <= fg(rr) + 1e-12
                 for rr in (1, 0.5, 0.1, 0.01, 0.001) for j in range(n))
    else:
        fF, fg = sp.lambdify((h, k), F, 'math'), sp.lambdify((h, k), g, 'math')
        vals = [s * 10 ** -e for e in (1, 2, 3) for s in (1, -1, 0.37, -0.73)] + [0.0]
        ok = all(abs(fF(p, q)) <= fg(p, q) + 1e-12 for p in vals for q in vals if (p, q) != (0.0, 0.0))
    return sp.Integer(int(ok))


def lim_lat(e, v):
    return [sp.limit(e, v, 0, '+'), sp.limit(e, v, 0, '-')]


def comprobaciones(c):
    # ---- Ejercicios del libro (E 5.1-5.12)
    f1 = sp.atan(x * y / (x ** 2 + y ** 2))
    c('ej-5-1', 'parciales 0 en el origen; por y=x vale arctg(1/2)', lista([f1.subs(y, 0), f1.subs(x, 0), sp.simplify(f1.subs(y, x))], [0, 0, sp.atan(R(1, 2))]), 1,
      r"f(x,x)=\operatorname{arctg}\frac12\ne0")
    f2 = sp.cos(y) - y * x ** 2
    c('ej-5-2', 'f(0,0)=1, ∇f(0,0)=(0,0)', lista([f2.subs({x: 0, y: 0})] + grad(f2, (0, 0)), [1, 0, 0]), 1, r"z=1+(0,0)\cdot(x,y)=1")
    f3 = x ** 2 + y ** 3 + sp.exp(x + y)
    g3 = grad(f3, (1, -1))
    c('ej-5-3', 'plano z = 2 + 3x + 4y', sp.expand(f3.subs({x: 1, y: -1}) + g3[0] * (x - 1) + g3[1] * (y + 1)), 2 + 3 * x + 4 * y, r"\boxed{z=2+3x+4y}")
    f4 = x * sp.exp(y) + y * sp.cos(x * y) ** 2
    c('ej-5-4', 'f_x y f_y', lista([sp.diff(f4, x) - (sp.exp(y) - y ** 2 * sp.sin(2 * x * y)), sp.diff(f4, y) - (x * sp.exp(y) + sp.cos(x * y) ** 2 - x * y * sp.sin(2 * x * y))], [0, 0]), 1,
      r"f_y=xe^y+\cos^2(xy)-xy\operatorname{sen}(2xy)")
    f5 = (x ** 2 + y ** 2) * sp.sin(1 / (x ** 2 + y ** 2))
    fx5 = sp.diff(f5, x)
    c('ej-5-5', 'Q = ρ sen(1/ρ²), |Q| ≤ ρ; f_x(x_n,0) = −2/x_n', lista([sp.simplify(pol(cociente(f5, 0, [0, 0])) - rho * sp.sin(rho ** -2)), cota(pol(cociente(f5, 0, [0, 0])), rho),
                                                                   sp.simplify(fx5.subs({x: 1 / sp.sqrt(2 * 3 * pi), y: 0}) + 2 * sp.sqrt(2 * 3 * pi))], [0, 1, 0]), 1,
      r"Q=\rho\operatorname{sen}\frac1{\rho^2}")
    Q6 = pol(cociente(x * sp.Abs(y), 0, [0, 0]))
    c('ej-5-6', 'Q = ρ cos θ |sen θ|, |Q| ≤ ρ', lista([sp.simplify(Q6 - rho * sp.cos(th) * sp.Abs(sp.sin(th))), cota(Q6, rho)], [0, 1]), 1,
      r"Q=\rho\cos\theta|\operatorname{sen}\theta|")
    f7 = 4 * x ** 3 / (x ** 2 + y ** 2)
    Q7 = pol(cociente(f7, 0, [4, 0]))
    c('ej-5-7', 'Q = −4 cos θ sen²θ: 0 y −√2', lista([sp.simplify(Q7 + 4 * sp.cos(th) * sp.sin(th) ** 2), Q7.subs(th, 0), sp.simplify(Q7.subs(th, pi / 4))], [0, 0, -sp.sqrt(2)]), 1,
      r"=-\sqrt2")
    c('ej-5-8', 'contrarrecíproco del Teorema 5.1 (sin cálculo)', sp.Integer(1), 1, r"no diferenciable en $(1,2,3)$; continua en $(3,2,1)$")
    f9 = y * sp.sin(1 / x) + x
    t9 = sp.symbols('t9', positive=True)
    Q9t = sp.simplify(cociente(f9, 0, [1, 0]).subs({h: t9, k: t9}))
    c('ej-5-9', 'Q(t,t) = sen(1/t)/√2 (t > 0): 0 y 1/√2 en dos sucesiones', lista([sp.simplify(Q9t - sp.sin(1 / t9) / sp.sqrt(2)),
                                                                         sp.simplify(Q9t.subs(t9, 1 / (5 * pi))), sp.simplify(Q9t.subs(t9, 1 / (pi / 2 + 10 * pi)))], [0, 0, 1 / sp.sqrt(2)]), 1,
      r"\frac1{\sqrt2}\operatorname{sen}\frac1t")
    u = sp.symbols('u', positive=True)
    G = u / sp.log(1 - u) + 1
    c('ej-5-10', 'lim u/ln(1−u) = −1; lim G(u)/u = 1/2', lista([sp.limit(u / sp.log(1 - u), u, 0, '+'), sp.limit(G / u, u, 0, '+')], [-1, R(1, 2)]), 1,
      r"\frac{G(u)}u\to\frac{-1/2}{-1}=\frac12")
    Q11 = pol(cociente(x * y / (x ** 2 + y ** 2) ** R(1, 4), 0, [0, 0]))
    c('ej-5-11', 'Q = √ρ cos θ sen θ, |Q| ≤ √ρ', lista([sp.simplify(Q11 - sp.sqrt(rho) * sp.cos(th) * sp.sin(th)), cota(Q11, sp.sqrt(rho))], [0, 1]), 1,
      r"=\sqrt\rho\cos\theta\operatorname{sen}\theta")
    c('ej-5-12', 'f + xy = x² + y²; |h|/h → ±1', lista([sp.expand(x ** 2 - x * y + y ** 2 + x * y)] + lim_lat(sp.sqrt(h ** 2) / h, h), [x ** 2 + y ** 2, 1, -1]), 1,
      r"\frac{\sqrt{h^2}}h=\frac{|h|}h")
    # ---- Ejemplos propios
    fp1 = sp.sqrt(x ** 2 + y ** 2)
    gp1 = grad(fp1, (3, 4))
    c('p1', 'aproximación 4,988; exacto 4,98812…', lista([5 + gp1[0] * R(2, 100) + gp1[1] * R(-3, 100), r(sp.sqrt(R('3.02') ** 2 + R('3.97') ** 2), 5)], [R('4.988'), R('4.98812')]), 1,
      r"=5+0{,}012-0{,}024=4{,}988")
    Qp2 = pol(cociente(x * y / sp.sqrt(x ** 2 + y ** 2), 0, [0, 0]))
    c('p2', 'Q = cos θ sen θ: 0 y 1/2', lista([sp.simplify(Qp2 - sp.cos(th) * sp.sin(th)), Qp2.subs(th, 0), sp.simplify(Qp2.subs(th, pi / 4))], [0, 0, R(1, 2)]), 1,
      r"=\cos\theta\operatorname{sen}\theta=\frac12\operatorname{sen}2\theta")
    fp3 = x ** 2 * sp.sin(1 / x) + y ** 2
    c('p3', 'f_x = 2x sen(1/x) − cos(1/x); vale −1 en 1/(2nπ)', lista([sp.simplify(sp.diff(fp3, x) - (2 * x * sp.sin(1 / x) - sp.cos(1 / x))), sp.diff(fp3, x).subs({x: 1 / (6 * pi), y: 0}),
                                                                   sp.limit(h * sp.sin(1 / h), h, 0)], [0, -1, 0]), 1,
      r"f_x=2x\operatorname{sen}\frac1x-\cos\frac1x")
    Qp4 = pol(cociente(sp.Abs(x * y), 0, [0, 0]))
    c('p4', 'α = 1: Q = ρ|cos θ sen θ|; α = 1/2: 1/√2 en θ = π/4', lista([sp.simplify(Qp4 - rho * sp.Abs(sp.cos(th) * sp.sin(th))),
                                                                        sp.simplify(pol(cociente(sp.sqrt(sp.Abs(x * y)), 0, [0, 0])).subs(th, pi / 4))], [0, 1 / sp.sqrt(2)]), 1,
      r"Q=\rho^{2\alpha-1}|\cos\theta\operatorname{sen}\theta|^\alpha")
    # ---- Exámenes
    fx1 = (x + sp.sin(y)) ** 2
    gx1 = grad(fx1, (a, b))
    c('x1', 'Df(a,b)(x,y) = 2(a+sen b)(x + y cos b)', sp.simplify(gx1[0] * x + gx1[1] * y - 2 * (a + sp.sin(b)) * (x + y * sp.cos(b))), 0,
      r"=2(a+\operatorname{sen}b)(x+y\cos b)")
    c('x2', 'enunciado de teoría (sin cálculo)', sp.Integer(1), 1,
      r"si $f$ admite derivadas parciales en un entorno de $(a,b)$ y estas son continuas en $(a,b)$")
    fx3 = x ** 2 + x * y
    g = grad(fx3, (1, 2))
    c('x3', 'plano 4x + y − z = 3', sp.expand(4 * x + y - (fx3.subs({x: 1, y: 2}) + g[0] * (x - 1) + g[1] * (y - 2))), 3, r"\boxed{4x+y-z=3}")
    fx4 = sp.exp(x) * (3 * sp.sin(y) + 2)
    g = grad(fx4, (0, pi / 2))
    c('x4', 'plano z = 5 + 5x', sp.expand(fx4.subs({x: 0, y: pi / 2}) + g[0] * x + g[1] * (y - pi / 2)), 5 + 5 * x, r"\boxed{z=5+5x}")
    fx5 = y * sp.tan(sp.sin(x))
    c('x5', 'f_x = y cos x / cos²(sen x), f_y = tg(sen x)', lista([sp.simplify(sp.diff(fx5, x) - y * sp.cos(x) / sp.cos(sp.sin(x)) ** 2), sp.diff(fx5, y)], [0, sp.tan(sp.sin(x))]), 1,
      r"f_x=\frac{y\cos x}{\cos^2(\operatorname{sen}x)}")
    c('x6', 'f(x,mx) = arctg(m/(1+m²)); f_x', lista([sp.simplify(f1.subs(y, 2 * x)), sp.simplify(sp.diff(f1, x) - y * (y ** 2 - x ** 2) / ((x ** 2 + y ** 2) ** 2 + x ** 2 * y ** 2))],
                                                   [sp.atan(R(2, 5)), 0]), 1,
      r"f_x=\dfrac{y(y^2-x^2)}{(x^2+y^2)^2+x^2y^2}")
    fx7 = (x ** 2 - y ** 2) / sp.cbrt(x ** 3 + y ** 3)
    Q7t = sp.simplify(cociente(fx7, 0, [1, -1]).subs({h: t, k: 2 * t}))
    tp = sp.symbols('tp', positive=True)
    Q7t = sp.simplify(Q7t.subs(t, tp))
    c('x7', 'Q(t,2t) = (1 − ∛3)/√5 ≈ −0,198', lista([sp.simplify(Q7t - (1 - sp.cbrt(3)) / sp.sqrt(5)), r(Q7t, 3)], [0, R('-0.198')]), 1,
      r"\frac{1-\sqrt[3]3}{\sqrt5}\approx-0{,}198")
    fx8 = x ** 2 * y ** 2 / (x ** 2 + 2 * y ** 2)
    c('x8', 'f_x y f_y fuera del origen', lista([sp.simplify(sp.diff(fx8, x) - 4 * x * y ** 4 / (x ** 2 + 2 * y ** 2) ** 2), sp.simplify(sp.diff(fx8, y) - 2 * x ** 4 * y / (x ** 2 + 2 * y ** 2) ** 2)], [0, 0]), 1,
      r"f_x=\dfrac{4xy^4}{(x^2+2y^2)^2}")
    fx9 = y ** 3 * sp.sin(1 / (x ** 2 + 2 * y ** 2))
    c('x9', '|Q| ≤ |k|³/ρ ≤ ρ²', cota(cociente(fx9, 0, [0, 0]), (h ** 2 + k ** 2), var='hk'), 1,
      r"|Q|\le\frac{|k|^3}\rho\le\frac{\rho^3}\rho=\rho^2\to0")
    fx10 = (x ** 3 + x * y ** 2 + 3 * y ** 4) / (x ** 2 + y ** 2)
    Q10 = pol(cociente(fx10, 0, [1, 0]))
    c('x10', 'Q = 3ρ sen⁴θ', lista([sp.simplify(Q10 - 3 * rho * sp.sin(th) ** 4), sp.limit(fx10.subs(y, 0) / x, x, 0), sp.limit(fx10.subs(x, 0) / y, y, 0)], [0, 1, 0]), 1,
      r"Q=3\rho\operatorname{sen}^4\theta")
    fx11 = x ** 2 * y ** 3 / (x ** 4 + y ** 2)
    g = grad(fx11, (1, 1))
    c('x11', 'f(1,1)=1/2, ∇=(0,1): z = y − 1/2', lista([fx11.subs({x: 1, y: 1}), sp.expand(R(1, 2) + g[0] * (x - 1) + g[1] * (y - 1))], [R(1, 2), y - R(1, 2)]), 1,
      r"\boxed{z=y-\frac12}")
    # ---- Práctica «Ahora hazlo tú» (respuesta final = «Resultado: …»)
    fa1 = x ** 3 * y - 2 * x * y ** 2 + 1
    ga1 = grad(fa1, (1, 1))
    fa2 = x * sp.log(x * y)
    ga2 = grad(fa2, (1, E_))
    fb1 = x ** 2 * y + sp.sin(x * y)
    gb1 = grad(fb1, (1, 0))
    fb2 = x * y * z + sp.log(1 + x ** 2 + z ** 2)
    gb2 = grad(fb2, (1, 2, 0), (x, y, z))
    rr, HH = sp.symbols('r H', positive=True)
    V = pi * rr ** 2 * HH
    dV = (sp.diff(V, rr) * R(1, 10) + sp.diff(V, HH) * R(1, 5)).subs({rr: 10, HH: 20})
    V0 = V.subs({rr: 10, HH: 20})
    fd1 = (x + y) ** 2 / (x ** 2 + y ** 2)
    Qd2 = (sp.real_root(h, 3) * sp.cos(pi / 2 + k)) / sp.sqrt(h ** 2 + k ** 2)
    Qe1 = pol(cociente(x ** 3 * y / (x ** 2 + y ** 2), 0, [0, 0]))
    fe2 = sp.exp(x) + x ** 2 * y ** 2 / (x ** 2 + y ** 2)
    Qe2 = cociente(fe2, 1, [1, 0])
    Qf1 = pol(cociente(x ** 2 * y / (x ** 2 + y ** 2), 0, [0, 0]))
    Qf2t = sp.simplify((sp.cbrt(2) * t - 2 * t) / (sp.sqrt(2) * t))
    fg1 = sp.log(x ** 2 + y ** 2) + x / y
    ap = sp.symbols('ap', positive=True)
    P = {
        'pr-a1': (lista([fa1.subs({x: 1, y: 1})] + ga1 + [sp.expand(fa1.subs({x: 1, y: 1}) + ga1[0] * (x - 1) + ga1[1] * (y - 1))], [0, 1, -3, x - 3 * y + 2]), 1,
                  r"Resultado: $z=x-3y+2$"),
        'pr-a2': (lista([sp.simplify(fa2.subs({x: 1, y: E_}))] + ga2 + [sp.expand(1 + ga2[0] * (x - 1) + ga2[1] * (y - E_)), sp.expand(1 + ga2[0] * (0 - 1) + ga2[1] * (0 - E_))],
                        [1, 2, 1 / E_, 2 * x + y / E_ - 2, -2]), 1,
                  r"Resultado: a) no ($f(1,e)=1$); b) $z=2x+\frac ye-2$; c) en $(0,0,-2)$"),
        'pr-b1': (lista([sp.diff(fb1, x) - (2 * x * y + y * sp.cos(x * y)), sp.diff(fb1, y) - (x ** 2 + x * sp.cos(x * y))] + gb1 + [gb1[0] * 3 + gb1[1] * (-1)], [0, 0, 0, 2, -2]), 1,
                  r"Resultado: $Df(a,b)(x,y)=\big(2ab+b\cos(ab)\big)x+\big(a^2+a\cos(ab)\big)y$; $Df(1,0)(x,y)=2y$ y $Df(1,0)(3,-1)=-2$"),
        'pr-b2': (lista([fb2.subs({x: 1, y: 2, z: 0})] + gb2, [sp.log(2), 1, 0, 2]), 1,
                  r"Resultado: $Df(1,2,0)(x,y,z)=x+2z$; espacio tangente $w=\ln2+(x-1)+2z$"),
        'pr-c1': (lista([1 + 3 * R(2, 100) + 2 * R(-3, 100), r(R('1.02') ** 3 * R('0.97') ** 2, 5), R('1.02') ** 3, R('0.97') ** 2], [1, R('0.99849'), R('1.061208'), R('0.9409')]), 1,
                  r"Resultado: $1{,}02^3\cdot0{,}97^2\approx1$ (valor exacto $0{,}99849\ldots$)"),
        'pr-c2': (lista([dV, r(dV, 1), V0, dV / V0, sp.expand(V.subs({rr: R('10.1'), HH: R('20.2')}) - V0)], [60 * pi, R('188.5'), 2000 * pi, R(3, 100), R('60.602') * pi]), 1,
                  r"Resultado: error máximo $\approx60\pi\approx188{,}5$ cm³; error relativo $\approx3\,\%$"),
        'pr-d1': (lista([sp.simplify(fd1.subs(y, -x)), sp.simplify(fd1.subs(y, 0)), sp.simplify(fd1.subs(x, 0))], [0, 1, 1]), 1,
                  r"Resultado: sí tiene parciales ($\nabla f(0,0)=(0,0)$), pero no es continua (por $y=-x$ tiende a $0\ne1$) y por tanto no es diferenciable en $(0,0)$"),
        'pr-d2': (lista([sp.limit(sp.cbrt(tp) / tp, tp, 0, '+'), sp.simplify(sp.cos(pi / 2 + k) + sp.sin(k)),
                         cota(Qd2, sp.Abs(h) ** R(1, 3), var='hk')], [sp.oo, 0, 1]), 1,
                  r"Resultado: no es diferenciable en $(0,0)$ (no existe $f_x(0,0)$); sí lo es en $\left(0,\frac\pi2\right)$, con $|Q|\le\sqrt[3]{|h|}\to0$ y plano tangente $z=0$"),
        'pr-e1': (lista([sp.simplify(Qe1 - rho * sp.cos(th) ** 3 * sp.sin(th)), cota(Qe1, rho)], [0, 1]), 1,
                  r"Resultado: $Q=\rho\cos^3\theta\operatorname{sen}\theta$, $|Q|\le\rho\to0$: diferenciable en $(0,0)$, plano tangente $z=0$"),
        'pr-e2': (lista([sp.limit((sp.exp(h) - 1) / h, h, 0), sp.limit((sp.exp(h) - 1 - h) / h, h, 0),
                         sp.simplify(pol(Qe2 - (sp.exp(h) - 1 - h) / sp.sqrt(h ** 2 + k ** 2)) - rho * sp.cos(th) ** 2 * sp.sin(th) ** 2),
                         cota(Qe2, sp.Abs(sp.exp(h) - 1 - h) / sp.Max(sp.Abs(h), R(1, 10 ** 9)) + sp.sqrt(h ** 2 + k ** 2), var='hk')], [1, 0, 0, 1]), 1,
                  r"Resultado: diferenciable en $(0,0)$; $\nabla f(0,0)=(1,0)$ y plano tangente $z=1+x$"),
        'pr-f1': (lista([sp.simplify(Qf1 - sp.cos(th) ** 2 * sp.sin(th)), Qf1.subs(th, 0), sp.simplify(Qf1.subs(th, pi / 4))], [0, 0, sp.sqrt(2) / 4]), 1,
                  r"Resultado: continua y con $\nabla f(0,0)=(0,0)$, pero $Q=\cos^2\theta\operatorname{sen}\theta$ (vale $0$ y $\frac{\sqrt2}4$ según la dirección): no es diferenciable en $(0,0)$"),
        'pr-f2': (lista([sp.simplify(sp.cbrt(tp ** 3) / tp), sp.simplify(sp.cbrt(2) / sp.sqrt(2) - 2 ** R(-1, 6)), r(2 ** R(-1, 6), 3), sp.simplify(2 / sp.sqrt(2)),
                         sp.simplify(Qf2t - (sp.cbrt(2) - 2) / sp.sqrt(2)), r(Qf2t, 3)], [1, 0, R('0.891'), sp.sqrt(2), 0, R('-0.523')]), 1,
                  r"Resultado: $\nabla f(0,0)=(1,1)$; $D_{\bar v}f(0,0)=2^{-1/6}\approx0{,}891\ne\sqrt2=\nabla f(0,0)\cdot\bar v$; no es diferenciable en $(0,0)$"),
        'pr-g1': (lista(grad(fg1, (1, 1)), [2, 0]), 1,
                  r"Resultado: $D=\{(x,y):y\ne0\}$; $f$ es diferenciable en todo $D$; $Df(1,1)(x,y)=2x$"),
        'pr-g2': (lista(lim_lat(sp.Abs((ap + t) ** 2 - ap ** 2) / t, t) + lim_lat(sp.Abs((ap + t) ** 2 - (-ap) ** 2) / t, t)
                        + [cota(sp.Abs(h ** 2 - k ** 2) / sp.sqrt(h ** 2 + k ** 2), sp.sqrt(h ** 2 + k ** 2), var='hk')],
                        [2 * ap, -2 * ap, 2 * ap, -2 * ap, 1]), 1,
                  r"Resultado: $f$ es diferenciable en $\mathbb R^2$ salvo en los puntos de las rectas $y=x$ e $y=-x$ distintos del origen; en $(0,0)$ sí es diferenciable"),
    }
    for eid, (val, esp, txt) in P.items():
        if (EJ / f'{eid}.html').exists() or (EJ / f'{eid}.solucion.html').exists():
            c(eid, 'resultado de la práctica', val, esp, txt)
