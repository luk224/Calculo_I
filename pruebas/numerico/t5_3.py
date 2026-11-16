r"""Tema 5.3 (Teorema de la función implícita): hipótesis del teorema, derivación implícita (primera y segunda),
pendiente de curvas de nivel y superficies z = g(x, y), recalculados con sympy.

`comprobaciones(c)`: c(ejercicio, descripción, valor_sympy, esperado, trozo_latex)
  - valor_sympy: lo que calcula sympy;  esperado: lo que afirma la página;
  - trozo_latex: cadena que debe aparecer en `ejercicios/<ejercicio>.html` (o `.solucion.html`), comparada sin etiquetas,
    espacios, \, \; \! ni \displaystyle y con \dfrac/\tfrac = \frac.
Las comprobaciones de la práctica «Ahora hazlo tú» (pr-*) solo se activan cuando el ejercicio existe en `contenido/`.
Teorema (U p.206): f(a,b)=0, f_y(a,b)≠0 ⇒ y=g(x) con g' = −f_x/f_y.  Varias variables (U p.211): ∂z/∂x_j = −f_{x_j}/f_z.
"""
import pathlib

import sympy as sp

R = sp.Rational
pi = sp.pi
E_ = sp.E
x, y, z, a = sp.symbols('x y z a', real=True)
EJ = pathlib.Path(__file__).resolve().parents[2] / 'contenido' / 'tema_5_3' / 'ejercicios'


def _igual(p, q):
    p, q = sp.sympify(p), sp.sympify(q)
    if p == q:
        return True
    return sp.simplify(p - q) == 0


def lista(vals, esperados):
    return sp.Integer(int(len(vals) == len(esperados) and all(_igual(p, q) for p, q in zip(vals, esperados))))


def r(val, d):
    return R(str(round(float(val), d)))


def en(e, punto, vs=(x, y)):
    return sp.simplify(sp.sympify(e).subs(dict(zip(vs, punto))))


def grad(f, punto, vs=(x, y)):
    return [en(sp.diff(f, s), punto, vs) for s in vs]


def dy(F, punto, num=x, den=y, vs=(x, y)):
    """Derivada implícita −F_num/F_den en el punto (por defecto dy/dx)."""
    return en(-sp.diff(F, num) / sp.diff(F, den), punto, vs)


_X = sp.Symbol('X')
_Y = sp.Function('Y')(_X)
_W = sp.Symbol('W')


def derivadas_implicitas(F, punto):
    """(y', y'') en el punto, derivando dos veces F(x, y(x)) = 0 (como en U p.207)."""
    Ex = F.subs({x: _X, y: _Y}, simultaneous=True)
    yp = sp.solve(sp.diff(Ex, _X), sp.diff(_Y, _X))[0]
    e2 = sp.diff(Ex, _X, 2).subs(sp.diff(_Y, _X, 2), _W).subs(sp.diff(_Y, _X), yp)
    ypp = sp.solve(e2, _W)[0]
    s = lambda e: sp.simplify(e.subs(_Y, punto[1]).subs(_X, punto[0]))  # noqa: E731
    return s(yp), s(ypp)


def raiz_real(pol, cerca):
    rs = [complex(q) for q in sp.Poly(pol, y).nroots()]
    rs = [q.real for q in rs if abs(q.imag) < 1e-12]
    return min(rs, key=lambda q: abs(q - cerca))


def comprobaciones(c):
    # ---- Ejercicios del libro (E 5.23-5.27)
    f23 = x ** 2 - x * y ** 2 + y ** 2 - 1
    c('ej-5-23', 'solo (0,1): f=0 y f_y≠0; (2,1) fuera; (−1,0) f_y=0',
      lista([en(f23, (0, 1)), en(sp.diff(f23, y), (0, 1)), en(f23, (2, 1)), en(f23, (-1, 0)), en(sp.diff(f23, y), (-1, 0))], [0, 2, 2, 0, 0]), 1,
      r"Respuesta: a).")
    f24 = x ** 4 + x ** 2 * y ** 3 - y ** 2 - 1
    # x = g(y): intercambiar papeles (derivar respecto de y)
    g24 = derivadas_implicitas(f24.subs({x: y, y: x}, simultaneous=True), (1, 1))
    c('ej-5-24', "∇f(1,1)=(6,1); g'(1)=−1/6; g''(1)=−43/108", lista(grad(f24, (1, 1)) + list(g24), [6, 1, R(-1, 6), R(-43, 108)]), 1,
      r"Respuestas: $g'(1)=-\frac16$, $g''(1)=-\frac{43}{108}$.")
    f25 = 3 * x * y - x ** 3 + sp.cos(pi * y) - 1
    c('ej-5-25', "f(1,1)=0; f_y=3 (sí y=g(x), g'=0); f_x=0 (no garantiza x)",
      lista([en(f25, (1, 1))] + grad(f25, (1, 1))[::-1] + [dy(f25, (1, 1))], [0, 3, 0, 0]), 1, r"-\frac03=0")
    f26 = y * sp.exp(x) - x ** 2
    c('ej-5-26', 'nivel 1, pendiente −1', lista([en(f26, (0, 1)), dy(f26 - 1, (0, 1))], [1, -1]), 1, r"Respuesta: $-1$.")
    f27 = 1 - sp.exp(x ** 7 + y ** 2 - x * z - 1)
    asol = sp.solve(sp.Eq(f27.subs({x: 1, y: 0, z: a}), 0), a)
    P27 = (1, 0, 0)
    c('ej-5-27', 'a=0; f_z=1; g_x=7, g_y=0',
      lista(asol + [en(sp.diff(f27, z), P27, (x, y, z)), dy(f27, P27, x, z, (x, y, z)), dy(f27, P27, y, z, (x, y, z))], [0, 1, 7, 0]), 1,
      r"Respuestas: $a=0$, $\frac{\partial g}{\partial x}(1,0)=7$, $\frac{\partial g}{\partial y}(1,0)=0$.")
    # ---- Ejemplos propios
    fp1 = x ** 2 + x * y + y ** 2 - 7
    hor = sp.solve([fp1, sp.diff(fp1, x)], [x, y], dict=True)
    ver = sp.solve([fp1, sp.diff(fp1, y)], [x, y], dict=True)
    s21 = sp.sqrt(21)
    c('p1', "y'(1)=−4/5; horizontales ±(√21/3, −2√21/3); verticales ±(2√21/3, −√21/3)",
      lista([dy(fp1, (1, 2)), sp.Integer(int({(sp.simplify(d[x]), sp.simplify(d[y])) for d in hor} == {(s21 / 3, -2 * s21 / 3), (-s21 / 3, 2 * s21 / 3)})),
             sp.Integer(int({(sp.simplify(d[x]), sp.simplify(d[y])) for d in ver} == {(2 * s21 / 3, -s21 / 3), (-2 * s21 / 3, s21 / 3)}))], [R(-4, 5), 1, 1]), 1,
      r"\pm\left(\frac{\sqrt{21}}3,-\frac{2\sqrt{21}}3\right)")
    fp2 = z ** 3 + x * z - y
    P2 = (0, 1, 1)
    zx, zy = dy(fp2, P2, x, z, (x, y, z)), dy(fp2, P2, y, z, (x, y, z))
    aprox = 1 + zx * R(1, 10) + zy * R(-1, 10)
    real = sp.nsolve(z ** 3 + R(1, 10) * z - R(9, 10), z, 1)
    c('p2', 'z_x=−1/3, z_y=1/3; aprox 0,9333; real 0,93098', lista([zx, zy, r(aprox, 4), r(real, 5)], [R(-1, 3), R(1, 3), R('0.9333'), R('0.93098')]), 1,
      r"z\approx0{,}93098")
    c('p3', "y'(0)=−1/e, y''(0)=1/e²", lista(list(derivadas_implicitas(sp.exp(y) + x * y - E_, (0, 1))), [-1 / E_, E_ ** -2]), 1,
      r"y''(0)=\frac1{e^2}")
    fp4 = x ** 3 + y ** 3 - 3 * x * y
    sing = [s for s in sp.solve([sp.diff(fp4, x), sp.diff(fp4, y)], [x, y]) if all(v.is_real for v in s) and fp4.subs({x: s[0], y: s[1]}) == 0]
    c('p4', "singular solo (0,0); y'=−1, y''=−32/3 en (3/2,3/2)",
      lista([sp.Integer(int(sing == [(0, 0)]))] + list(derivadas_implicitas(fp4, (R(3, 2), R(3, 2)))), [1, -1, R(-32, 3)]), 1, r"=-\dfrac{32}3")
    # ---- Exámenes
    fx1 = x ** 2 + y ** 2 - 9
    c('x1', 'f(3,0)=0, f_y(3,0)=0 (falso); f_x(3,0)=6', lista([en(fx1, (3, 0))] + grad(fx1, (3, 0))[::-1], [0, 0, 6]), 1,
      r"\frac{\partial f}{\partial y}(3,0)=0")
    c('x2', "g'(1)=−1/6, g''(1)=−43/108 (= E 5.24)", lista(list(g24), [R(-1, 6), R(-43, 108)]), 1, r"g''(1)=-\frac{43}{108}")
    # ---- Práctica «Ahora hazlo tú» (respuesta final = «Resultado: …»)
    fa1 = y ** 3 - 3 * y + x ** 2 - 2
    pts_a1 = [(2, 1), (0, -1), (1, 0), (0, 2)]
    fa2 = x ** 3 + a * x * y + y ** 3 - a - 2
    G = fa2.subs(a, -3)
    sq = R(1, 2) * ((x - y) ** 2 + (x - 1) ** 2 + (y - 1) ** 2)
    fb1 = y ** 2 - 2 * y + x ** 3 - x + 1
    fb2 = y ** 2 - x ** 3 - x ** 2

    def conj(sist):
        return {(sp.simplify(p), sp.simplify(q)) for p, q in sp.solve(sist, [x, y])}
    s3 = sp.sqrt(3)
    fc2 = sp.log(x ** 2 + y ** 2) - sp.atan(y / x)
    fe1 = x ** 2 * y - y ** 3 + 2 * x
    fx_, fy_ = x ** 2 - y ** 2, x * y
    m1 = sp.simplify(-sp.diff(fx_, x) / sp.diff(fx_, y))
    m2 = sp.simplify(-sp.diff(fy_, x) / sp.diff(fy_, y))
    ff1 = x ** 2 + 2 * y ** 2 + z ** 3 - 4
    gf1 = sp.cbrt(4 - x ** 2 - 2 * y ** 2)
    ff2 = sp.exp(x * z) + y * z ** 2 - 2
    PF = (0, 1, 1)
    gzx, gzy = dy(ff2, PF, x, z, (x, y, z)), dy(ff2, PF, y, z, (x, y, z))
    pl = sp.expand(2 * (1 + gzx * x + gzy * (y - 1)))  # 2z = …  ⇒  x + y + 2z = 3
    fg1 = y ** 5 + y - x
    pV, V, T, Rg = sp.symbols('p V T R', positive=True)
    Fx, Fy, Fz = sp.symbols('F_x F_y F_z', nonzero=True)
    gas = sp.simplify((sp.diff(Rg * T / V, V) * sp.diff(Rg * T / pV, T) * sp.diff(pV * V / Rg, pV)).subs(pV, Rg * T / V))
    P = {
        'pr-a1': (lista([en(fa1, p) for p in pts_a1] + [en(sp.diff(fa1, y), p) for p in pts_a1] + [dy(fa1, (0, 2))],
                        [0, 0, -1, 0, 0, 0, -3, 9, 0]), 1,
                  r"Resultado: solo en d) $(0,2)$ (allí $f=0$ y $f_y=9\ne0$)"),
        'pr-a2': (lista([sp.expand(en(fa2, (1, 1))), en(sp.diff(fa2, y), (1, 1)), dy(fa2, (1, 1)), sp.expand(G - (x + y + 1) * sq),
                         sp.Integer(int(sp.solve([G, sp.diff(G, x), sp.diff(G, y)], [x, y]) == [(1, 1)]))], [0, a + 3, -1, 0, 1]), 1,
                  r"Resultado: $a\ne-3$, con $g'(1)=-1$ para todo $a\ne-3$; con $a=-3$, cerca de $(1,1)$ la curva es solo el punto $(1,1)$"),
        'pr-b1': (lista([en(fb1, (1, 1))] + grad(fb1, (1, 1)) + [dy(fb1, (1, 1), y, x)], [0, 2, 0, 0]), 1,
                  r"Resultado: $y=g(x)$ no lo garantiza ($f_y(1,1)=0$); $x=h(y)$ sí ($f_x(1,1)=2\ne0$), con $h'(1)=0$"),
        'pr-b2': (lista([sp.Integer(int(conj([fb2, sp.diff(fb2, y)]) == {(0, 0), (-1, 0)})),
                         sp.Integer(int(conj([fb2, sp.diff(fb2, x)]) == {(0, 0), (R(-2, 3), 2 * s3 / 9), (R(-2, 3), -2 * s3 / 9)})),
                         en(sp.diff(fb2, x), (-1, 0)), dy(fb2, (-1, 0), y, x)], [1, 1, -1, 0]), 1,
                  r"Resultado: a) $(0,0)$ y $(-1,0)$; b) $(0,0)$ y $\left(-\frac23,\pm\frac{2\sqrt3}9\right)$; c) solo $(0,0)$; d) $x=h(y)$ con $h'(0)=0$"),
        'pr-c1': (lista([en(x ** 2 * y + y ** 3 - 10, (1, 2)), dy(x ** 2 * y + y ** 3 - 10, (1, 2))], [0, R(-4, 13)]), 1,
                  r"Resultado: $y'(1)=-\frac4{13}$; tangente $y=2-\frac4{13}(x-1)$"),
        'pr-c2': (lista([en(fc2, (1, 0)), en(sp.diff(fc2, y), (1, 0)), sp.simplify(-sp.diff(fc2, x) / sp.diff(fc2, y) - (2 * x + y) / (x - 2 * y)), dy(fc2, (1, 0))],
                        [0, -1, 0, 2]), 1,
                  r"Resultado: $y'=\frac{2x+y}{x-2y}$; $y'(1)=2$; tangente $y=2x-2$"),
        'pr-d1': (lista(list(derivadas_implicitas(x ** 3 + y ** 3 - 9, (1, 2))), [R(-1, 4), R(-9, 16)]), 1,
                  r"Resultado: $y'(1)=-\frac14$, $y''(1)=-\frac9{16}$"),
        'pr-d2': (lista(list(derivadas_implicitas(y ** 3 + x * y + x ** 2 - 3, (1, 1)))
                        + [sp.Integer(int(all(raiz_real(y ** 3 + q * y + q ** 2 - 3, 1) < 1 - 0.75 * (q - 1) for q in (0.9, 0.95, 1.05, 1.1))))],
                        [R(-3, 4), R(-31, 32), 1]), 1,
                  r"Resultado: $y'(1)=-\frac34$, $y''(1)=-\frac{31}{32}$; la curva queda por debajo de su tangente cerca de $(1,1)$"),
        'pr-e1': (lista([en(fe1, (1, 1))] + grad(fe1, (1, 1)) + [dy(fe1, (1, 1))], [2, 4, -2, 2]), 1,
                  r"Resultado: pendiente $2$; tangente $y=2x-1$"),
        'pr-e2': (lista([m1 - x / y, m2 + y / x, sp.simplify(m1 * m2), m1.subs({x: 2, y: 1}), m2.subs({x: 2, y: 1})], [0, 0, -1, 2, R(-1, 2)]), 1,
                  r"Resultado: $m_1=\frac ab$, $m_2=-\frac ba$, $m_1m_2=-1$; en $(2,1)$: $2$ y $-\frac12$"),
        'pr-f1': (lista([en(ff1, (1, 1, 1), (x, y, z)), dy(ff1, (1, 1, 1), x, z, (x, y, z)), dy(ff1, (1, 1, 1), y, z, (x, y, z))] + grad(gf1, (1, 1)),
                        [0, R(-2, 3), R(-4, 3), R(-2, 3), R(-4, 3)]), 1,
                  r"Resultado: $\frac{\partial g}{\partial x}(1,1)=-\frac23$, $\frac{\partial g}{\partial y}(1,1)=-\frac43$"),
        'pr-f2': (lista([en(ff2, PF, (x, y, z))] + grad(ff2, PF, (x, y, z)) + [gzx, gzy, dy(ff2, PF, y, x, (x, y, z)), sp.expand(pl + x + y)],
                        [0, 1, 1, 2, R(-1, 2), R(-1, 2), -1, 3]), 1,
                  r"Resultado: $g_x(0,1)=g_y(0,1)=-\frac12$; $\frac{\partial h}{\partial y}(1,1)=-1$; plano $x+y+2z=3$"),
        'pr-g1': (lista([en(fg1, (2, 1)), dy(fg1, (2, 1)), r(1 + R(6, 100) / 6, 2), r(raiz_real(y ** 5 + y - R(206, 100), 1), 5)],
                        [0, R(1, 6), R('1.01'), R('1.00984')]), 1,
                  r"Resultado: $g'(2)=\frac16$; $g(2{,}06)\approx1{,}01$ (valor real $\approx1{,}00984$)"),
        'pr-g2': (lista([sp.simplify((-Fy / Fx) * (-Fz / Fy) * (-Fx / Fz)), gas], [-1, -1]), 1,
                  r"Resultado: $\frac{\partial x}{\partial y}\cdot\frac{\partial y}{\partial z}\cdot\frac{\partial z}{\partial x}=-1$ (no $1$); con $pV=RT$: $-\frac{RT}{pV}=-1$"),
    }
    for eid, (val, esp, txt) in P.items():
        if (EJ / f'{eid}.html').exists() or (EJ / f'{eid}.solucion.html').exists():
            c(eid, 'resultado de la práctica', val, esp, txt)
