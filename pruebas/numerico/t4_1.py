r"""Tema 4.1 (El espacio ℝⁿ): producto escalar, norma, distancia, ángulo, conjuntos del plano (interior, frontera,
abierto/cerrado) y coordenadas polares, cilíndricas y esféricas, recalculados con sympy.

`comprobaciones(c)`: c(ejercicio, descripción, valor_sympy, esperado, trozo_latex)
  - valor_sympy: lo que calcula sympy;  esperado: lo que afirma la página;
  - trozo_latex: cadena que debe aparecer en `ejercicios/<ejercicio>.html` (o `.solucion.html`), comparada sin etiquetas,
    espacios, \, \; \! ni \displaystyle y con \dfrac/\tfrac = \frac.
Las comprobaciones de la práctica «Ahora hazlo tú» (pr-*) solo se activan cuando el ejercicio existe en `contenido/`.
Convenios de U §4.1.3: θ ∈ [0, 2π); en esféricas φ ∈ [−π/2, π/2] (latitud) y z = ρ sen φ.
"""
import pathlib

import sympy as sp

R = sp.Rational
pi = sp.pi
s2, s3 = sp.sqrt(2), sp.sqrt(3)
EJ = pathlib.Path(__file__).resolve().parents[2] / 'contenido' / 'tema_4_1' / 'ejercicios'


def V(*c):
    return sp.Matrix([sp.sympify(t) for t in c])


def dot(u, v):
    return sp.simplify(u.dot(v))


def norma(u):
    return sp.sqrt(sp.simplify(u.dot(u)))


def angulo(u, v):
    return sp.acos(sp.nsimplify(dot(u, v) / (norma(u) * norma(v))))


def theta(x, y):
    """Ángulo polar en [0, 2π) (regla de cuadrantes de U p.148)."""
    t = sp.atan2(y, x)
    return sp.simplify(t + 2 * pi) if bool(t < 0) else sp.simplify(t)


def polares(x, y):
    return [sp.sqrt(x ** 2 + y ** 2), theta(x, y)]


def cilindricas(x, y, z):
    return polares(x, y) + [sp.sympify(z)]


def esfericas(x, y, z):
    r = sp.sqrt(x ** 2 + y ** 2 + z ** 2)
    return [sp.simplify(r), theta(x, y), sp.asin(sp.simplify(z / r))]


def de_cil(r, t, z):
    return [sp.simplify(r * sp.cos(t)), sp.simplify(r * sp.sin(t)), sp.sympify(z)]


def de_esf(r, t, f):
    return [sp.simplify(r * sp.cos(f) * sp.cos(t)), sp.simplify(r * sp.cos(f) * sp.sin(t)), sp.simplify(r * sp.sin(f))]


def _igual(p, q):
    p, q = sp.sympify(p), sp.sympify(q)
    if p == q:
        return True
    if isinstance(p, sp.Set) or isinstance(q, sp.Set):
        return False
    return sp.simplify(p - q) == 0


def lista(vals, esperados):
    return sp.Integer(int(len(vals) == len(esperados) and all(_igual(p, q) for p, q in zip(vals, esperados))))


def r(v, d):
    return R(str(round(float(v), d)))


def tipo_punto(pert, P, rad=R(1, 1000), n=24):
    """'i' interior, 'e' exterior, 'f' frontera: mira el punto y n puntos de un círculo pequeño a su alrededor."""
    a, b = P
    pts = [(a, b)] + [(a + rad * sp.cos(2 * pi * k / n), b + rad * sp.sin(2 * pi * k / n)) for k in range(n)]
    dentro = [bool(pert(sp.N(x, 30), sp.N(y, 30))) for x, y in pts]
    return 'i' if all(dentro) else ('e' if not any(dentro) else 'f')


def comprobaciones(c):
    # ---- Ejercicios del libro (E 4.1-4.8)
    c('ej-4-1', 'el producto escalar de dos vectores es un número', sp.Integer(int(dot(V(1, 2), V(3, 4)).is_number)), 1,
      r"$\mathbb R^2$ con $\mathbb R^3$.")
    c('ej-4-2', 'contraejemplo: (u·v)w = (0,1)', lista(list(dot(V(1, 0), V(1, 0)) * V(0, 1)), [0, 1]), 1, r"$1\cdot(0,1)=(0,1)$")
    c('ej-4-3', '(0,1,2)·(-3,-4,2)', dot(V(0, 1, 2), V(-3, -4, 2)), 0, r"0-4+4=0")
    u, v = V(-1, 1), V(2, 3)
    c('ej-4-4', 'normas, suma y 3u', lista([norma(u), norma(v), norma(u + v), norma(3 * u)], [s2, sp.sqrt(13), sp.sqrt(17), 3 * s2]), 1,
      r"$\|\bar u+\bar v\|=\sqrt{1+16}=\sqrt{17}\approx4{,}123$")
    disco = lambda x, y: x ** 2 + y ** 2 <= 4  # noqa: E731
    c('ej-4-5', 'frontera (2,0), interior (1,0), exterior (3,0)', lista([tipo_punto(disco, (2, 0)), tipo_punto(disco, (1, 0)), tipo_punto(disco, (3, 0))],
                                                                       ['f', 'i', 'e']), 1, r"$C$ es <b>cerrado</b>")
    c('ej-4-6', 'polares de (-1,1) y ángulo con (2,3)', lista(polares(-1, 1) + [sp.cos(angulo(u, v)), r(angulo(u, v), 4)], [s2, 3 * pi / 4, 1 / sp.sqrt(26), R('1.3734')]), 1,
      r"$(\rho,\theta)=(\sqrt2,3\pi/4)$")
    c('ej-4-7', 'cilíndricas de (1,1,1)', lista(cilindricas(1, 1, 1), [s2, pi / 4, 1]), 1, r"$\rho=\sqrt{1+1}=\sqrt2$")
    c('ej-4-8', 'cil./esf. de (1,2,-1) y vueltas', lista(cilindricas(1, 2, -1) + esfericas(1, 2, -1) + de_cil(1, pi, 0) + de_esf(1, pi / 2, 0),
                                                       [sp.sqrt(5), sp.atan(2), -1, sp.sqrt(6), sp.atan(2), sp.asin(-1 / sp.sqrt(6)), -1, 0, 0, 0, 1, 0]), 1,
      r"Cartesianas: $(0,1,0)$")
    # ---- Ejemplos propios
    a, b = V(1, 2, 2), V(2, -1, 2)
    c('p1', 'a·b, normas, ángulo y |a+b|', lista([dot(a, b), norma(a), norma(b), sp.cos(angulo(a, b)), norma(a + b)], [4, 3, 3, R(4, 9), sp.sqrt(26)]), 1,
      r"$\cos\alpha=\frac4{9}$")
    corona = lambda x, y: (1 < x ** 2 + y ** 2) & (x ** 2 + y ** 2 <= 4)  # noqa: E731
    c('p2', 'corona: (2,0) y (1,0) frontera, (3/2,0) interior', lista([tipo_punto(corona, (2, 0)), tipo_punto(corona, (1, 0)), tipo_punto(corona, (R(3, 2), 0)),
                                                                      bool(corona(2, 0)), bool(corona(1, 0))], ['f', 'f', 'i', True, False]), 1, r"<b>Cerrado: no.</b>")
    x, y, z = sp.symbols('x y z', real=True)
    g = x ** 2 + y ** 2 + z ** 2 - 2 * z
    c('p3', 'g en los cinco puntos', lista([g.subs({x: p[0], y: p[1], z: p[2]}) for p in ((0, 0, 0), (1, 1, 1), (0, 0, 3), (2, 0, 1), (0, 0, 5))]
                                           + [sp.expand(x ** 2 + y ** 2 + (z - 1) ** 2 - 1 - g)], [0, 1, 3, 3, 15, 0]), 1, r"$(0,0,5)$: $g=15$, exterior")
    c('p4', 'polares, cilíndricas y esféricas', lista(polares(-1, -s3) + polares(0, -3) + cilindricas(-s3, -1, 2) + esfericas(-s3, -1, 2) + de_esf(2 * s2, 7 * pi / 6, pi / 4),
                                                    [2, 4 * pi / 3, 3, 3 * pi / 2, 2, 7 * pi / 6, 2, 2 * s2, 7 * pi / 6, pi / 4, -s3, -1, 2]), 1,
      r"Esféricas $(2\sqrt2,7\pi/6,\pi/4)$")
    # ---- Exámenes
    c('x1', 'ortogonales', dot(V(0, 1, 2), V(-3, -4, 2)), 0, r"producto escalar $=0$")
    c('x2', 'ejemplos (2,2√3) → (4,π/3); (2,7π/4) → (√2,−√2)', lista(polares(2, 2 * s3) + de_cil(2, 7 * pi / 4, 0)[:2], [4, pi / 3, s2, -s2]), 1,
      r"$(\rho,\theta)=(2,7\pi/4)\mapsto(\sqrt2,-\sqrt2)$")
    p, q = V(1, 2, 3, 4), V(-1, -2, -3, -4)
    c('x3', 'producto escalar −30 y normas √30', lista([dot(p, q), norma(p), norma(q)], [-30, sp.sqrt(30), sp.sqrt(30)]), 1, r"=-1-4-9-16=-30")
    c('x4', 'distancia √41', norma(V(1, 3, 5) - V(1, -1, 0)), sp.sqrt(41), r"$\sqrt{0+16+25}=\sqrt{41}\approx6{,}403$")
    c('x5', 'distancia 3√3', norma(V(4, 2, 0) - V(1, -1, 3)), 3 * s3, r"$d=\sqrt{9+9+9}=\sqrt{27}=3\sqrt3\approx5{,}196$")
    c('x6', 'distancia 1 y ángulo arccos(1/√15)', lista([norma(V(1, 0, -1) - V(2, 0, -1)), sp.cos(angulo(V(0, 1, 2), V(1, -1, 1))), r(angulo(V(0, 1, 2), V(1, -1, 1)), 4)],
                                                        [1, 1 / sp.sqrt(15), R('1.3096')]), 1, r"\cos\alpha=\frac1{\sqrt5\sqrt3}=\frac1{\sqrt{15}}\approx0{,}2582")
    p, q = V(1, 2, 0, 1), V(-1, -2, 3, 0)
    c('x7', 'producto escalar −5, normas √6 y √14', lista([dot(p, q), norma(p), norma(q)], [-5, sp.sqrt(6), sp.sqrt(14)]), 1, r"=-1-4+0+0=-5")
    # ---- Práctica «Ahora hazlo tú» (respuesta final = «Resultado: …»)
    ua1, va1 = V(2, -1, 3), V(1, 4, -2)
    xa2 = sp.symbols('xa2', real=True)
    ub1, vb1 = V(1, 0, 1), V(0, 1, 1)
    k = sp.symbols('k', real=True)
    ub2, vb2 = V(0, 2, -1), V(3, 0, 4)
    wc1 = V(3, -4, 12)
    uc2, vc2 = V(1, 2, -2), V(4, 0, 3)
    d1 = lambda x, y: (x + 1) ** 2 + (y - 2) ** 2 >= 4  # noqa: E731
    d2 = lambda x, y: (x > 0) & (y >= 0) & (x ** 2 + y ** 2 < 4)  # noqa: E731
    th = sp.symbols('theta', real=True)
    rho = sp.symbols('rho', positive=True)
    xe = rho * sp.cos(th)
    ye = rho * sp.sin(th)
    ph = sp.symbols('varphi', real=True)
    P = {
        'pr-a1': (lista([dot(ua1, va1), norma(ua1), norma(va1), norma(va1 - ua1)], [-8, sp.sqrt(14), sp.sqrt(21), sp.sqrt(51)]), 1,
                  r"Resultado: $\bar u\cdot\bar v=-8$; $\|\bar u\|=\sqrt{14}$, $\|\bar v\|=\sqrt{21}$; $d(\bar u,\bar v)=\sqrt{51}$"),
        'pr-a2': (lista(sorted(sp.solve(norma(V(xa2, 0, 0) - V(1, 2, 2)) ** 2 - 9, xa2)), [0, 2]), 1,
                  r"Resultado: $(0,0,0)$ y $(2,0,0)$"),
        'pr-b1': (lista([dot(ub1, vb1), sp.cos(angulo(ub1, vb1)), angulo(ub1, vb1)], [1, R(1, 2), pi / 3]), 1,
                  r"Resultado: $\cos\alpha=\frac12$, $\alpha=\frac\pi3$ ($60^\circ$)"),
        'pr-b2': (lista(sp.solve(dot(V(k, 2, -1), V(3, k, 4)), k) + [dot(ub2, vb2), sp.cos(angulo(ub2, vb2)), r(angulo(ub2, vb2), 3)],
                        [R(4, 5), -4, -4 / (5 * sp.sqrt(5)), R('1.937')]), 1,
                  r"Resultado: $k=\frac45$; con $k=0$, $\cos\alpha=-\frac4{5\sqrt5}$ y $\alpha\approx1{,}937$ rad (obtuso)"),
        'pr-c1': (lista([norma(wc1)] + list(wc1 / norma(wc1)) + list(-5 * wc1 / norma(wc1)) + [norma(-5 * wc1 / norma(wc1))],
                        [13, R(3, 13), R(-4, 13), R(12, 13), R(-15, 13), R(20, 13), R(-60, 13), 5]), 1,
                  r"Resultado: unitario $\frac1{13}(3,-4,12)$; de norma $5$ y sentido contrario $\left(-\frac{15}{13},\frac{20}{13},-\frac{60}{13}\right)$"),
        'pr-c2': (lista([norma(uc2), norma(vc2), dot(uc2, vc2), norma(uc2 + vc2), norma(uc2 - vc2), sp.sqrt(9 + 25 + 2 * (-2)), sp.sqrt(9 + 25 - 2 * (-2))],
                        [3, 5, -2, sp.sqrt(30), sp.sqrt(38), sp.sqrt(30), sp.sqrt(38)]), 1,
                  r"Resultado: $\|\bar u+\bar v\|=\sqrt{30}\approx5{,}48$ y $\|\bar u-\bar v\|=\sqrt{38}\approx6{,}16$, los dos $\le8$"),
        'pr-d1': (lista([tipo_punto(d1, (-1, 2)), tipo_punto(d1, (1, 2)), tipo_punto(d1, (2, 2)), tipo_punto(d1, (-1, 4)), bool(d1(1, 2))], ['e', 'f', 'i', 'f', True]), 1,
                  r"Resultado: cerrado, no abierto y no acotado; frontera: la circunferencia $(x+1)^2+(y-2)^2=4$"),
        'pr-d2': (lista([tipo_punto(d2, (0, 1)), tipo_punto(d2, (1, 0)), tipo_punto(d2, (s2, s2)), tipo_punto(d2, (1, 1)), tipo_punto(d2, (0, 0)),
                         bool(d2(0, 1)), bool(d2(1, 0)), bool(d2(s2, s2))], ['f', 'f', 'f', 'i', 'f', False, True, False]), 1,
                  r"Resultado: ni abierto ni cerrado; acotado"),
        'pr-e1': (lista(polares(-2, 2) + polares(s3, -1) + [r(theta(-2, 2), 4)], [2 * s2, 3 * pi / 4, 2, 11 * pi / 6, R('2.3562')]), 1,
                  r"Resultado: $(-2,2)\to\left(2\sqrt2,\frac{3\pi}4\right)$; $(\sqrt3,-1)\to\left(2,\frac{11\pi}6\right)$"),
        'pr-e2': (lista([sp.simplify((xe ** 2 + ye ** 2 - 4 * xe) / rho - (rho - 4 * sp.cos(th)))] + polares(2, 2) + [4 * sp.cos(pi / 4)]
                        + de_cil(2 * s3, 7 * pi / 6, 0)[:2] + [(-3) ** 2 + s3 ** 2 - 4 * (-3)],
                        [0, 2 * s2, pi / 4, 2 * s2, -3, -s3, 24]), 1,
                  r"Resultado: $\rho=4\cos\theta$, circunferencia de centro $(2,0)$ y radio $2$; $(2,2)$ está en ella y $(-3,-\sqrt3)$ no"),
        'pr-f1': (lista(cilindricas(-1, -1, 3) + de_cil(4, 5 * pi / 6, -2), [s2, 5 * pi / 4, 3, -2 * s3, 2, -2]), 1,
                  r"Resultado: $(-1,-1,3)\to\left(\sqrt2,\frac{5\pi}4,3\right)$; $\left(4,\frac{5\pi}6,-2\right)\to(-2\sqrt3,2,-2)$"),
        'pr-f2': (lista([sp.simplify(sp.sqrt(xe ** 2 + ye ** 2) - rho), sp.simplify(xe ** 2 + ye ** 2 - rho ** 2)] + cilindricas(0, 1, 2) + [theta(-1, 0)],
                        [0, 0, 1, pi / 2, 2, pi]), 1,
                  r"Resultado: cono $z=\rho$; paraboloide $z=\rho^2$; sólido $0\le\rho\le2$, $0\le\theta\le\pi$, $0\le z\le3$"),
        'pr-g1': (lista(esfericas(0, 2, -2) + de_esf(2, pi, pi / 3), [2 * s2, pi / 2, -pi / 4, -1, 0, s3]), 1,
                  r"Resultado: $(0,2,-2)\to\left(2\sqrt2,\frac\pi2,-\frac\pi4\right)$; $\left(2,\pi,\frac\pi3\right)\to(-1,0,\sqrt3)$"),
        'pr-g2': (lista(cilindricas(-1, s3, 2) + esfericas(-1, s3, 2) + de_esf(2 * s2, 2 * pi / 3, pi / 4)
                        + [sp.simplify((rho ** 2 - 2 * rho * sp.sin(ph)) / rho - (rho - 2 * sp.sin(ph)))],
                        [2, 2 * pi / 3, 2, 2 * s2, 2 * pi / 3, pi / 4, -1, s3, 2, 0]), 1,
                  r"Resultado: cilíndricas $\left(2,\frac{2\pi}3,2\right)$; esféricas $\left(2\sqrt2,\frac{2\pi}3,\frac\pi4\right)$; la esfera es $\rho=2\operatorname{sen}\varphi$"),
    }
    for eid, (val, esp, txt) in P.items():
        if (EJ / f'{eid}.html').exists() or (EJ / f'{eid}.solucion.html').exists():
            c(eid, 'resultado de la práctica', val, esp, txt)
