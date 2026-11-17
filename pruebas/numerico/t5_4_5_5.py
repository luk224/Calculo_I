r"""Temas 5.4-5.5 (Valores extremos. Extremos condicionados, multiplicadores de Lagrange), recalculados con sympy.

`comprobaciones(c)`: c(ejercicio, descripción, valor_sympy, esperado, trozo_latex)
  - valor_sympy: lo que calcula sympy;  esperado: lo que afirma la página;
  - trozo_latex: cadena que debe aparecer en `ejercicios/<ejercicio>.html` (o `.solucion.html`), comparada sin etiquetas,
    espacios, \, \; \! ni \displaystyle y con \dfrac/\tfrac = \frac.
Las comprobaciones de la práctica «Ahora hazlo tú» (pr-*) solo se activan cuando el ejercicio existe en `contenido/`.
Condición necesaria (U p.218): ∇f = 0.  Condición suficiente (U p.220): d = |Hf|, r = f_xx.
Teorema de los valores extremos (U p.222).  Lagrange (U p.228): ∇F = 0 con F = f + λ g.
El fichero se llama t5_4_5_5.py porque la carpeta es contenido/tema_5_4_5_5 (clave «5.4-5.5»).
"""
import pathlib

import sympy as sp

R = sp.Rational
pi = sp.pi
E_ = sp.E
x, y, z, t, lam = sp.symbols('x y z t lambda', real=True)
EJ = pathlib.Path(__file__).resolve().parents[2] / 'contenido' / 'tema_5_4_5_5' / 'ejercicios'


def _igual(p, q):
    p, q = sp.sympify(p), sp.sympify(q)
    if p == q:
        return True
    return sp.simplify(p - q) == 0


def lista(vals, esperados):
    return sp.Integer(int(len(vals) == len(esperados) and all(_igual(p, q) for p, q in zip(vals, esperados))))


def conjunto(sols, esperados):
    """Mismo conjunto de puntos (tuplas), sin importar el orden."""
    a = {tuple(sp.nsimplify(sp.simplify(e)) for e in s) for s in sols}
    b = {tuple(sp.nsimplify(e) for e in s) for s in esperados}
    return sp.Integer(int(a == b))


def r(val, d):
    return R(str(round(float(val), d)))


def criticos(f, vs=(x, y)):
    """Puntos críticos reales de f (lista de tuplas)."""
    sols = sp.solve([sp.diff(f, v) for v in vs], list(vs), dict=True)
    out = []
    for s in sols:
        p = tuple(sp.simplify(s.get(v, v)) for v in vs)
        if all(e.is_real for e in p):
            out.append(p)
    return out


def hd(f, p, vs=(x, y)):
    """(d, r) de la condición suficiente (U p.220) en el punto p."""
    H = sp.hessian(f, vs).subs(dict(zip(vs, p)))
    return [sp.simplify(H.det()), sp.simplify(H[0, 0])]


def lagrange(f, g, vs=(x, y)):
    """Soluciones reales (x, y[, z]) del sistema ∇(f + λg) = 0, g = 0."""
    F = f + lam * g
    sols = sp.solve([sp.diff(F, v) for v in vs] + [g], list(vs) + [lam], dict=True)
    out = []
    for s in sols:
        p = tuple(sp.simplify(s[v]) for v in vs)
        if all(e.is_real for e in p):
            out.append(p)
    return out


def val(f, p, vs=(x, y)):
    return sp.simplify(f.subs(dict(zip(vs, p))))


def comprobaciones(c):
    # ---- Ejercicios del libro (E 5.28-5.48)
    f28 = y ** 2 * x ** 2 + y ** 2 + 4 * sp.sin(x) ** 2
    c('ej-5-28', 'f(kπ,0) = 0 (mínimo, f ≥ 0); f(0,y) = y² no acotada', lista([val(f28, (pi, 0)), val(f28, (-2 * pi, 0)), sp.simplify(f28.subs(x, 0) - y ** 2)], [0, 0, 0]), 1,
      r"$f(k\pi,0)=0\le f(x,y)$")
    f29 = x ** 3 + y ** 3 + x * y
    c('ej-5-29', 'críticos (0,0), (−1/3,−1/3); d = −1 y 3', lista([conjunto(criticos(f29), [(0, 0), (R(-1, 3), R(-1, 3))])] + hd(f29, (0, 0))[:1] + hd(f29, (R(-1, 3), R(-1, 3))), [1, -1, 3, -2]), 1,
      r"$(0,0)$ y $\left(-\frac13,-\frac13\right)$")
    f30 = x * y * (x ** 2 + y ** 2)
    c('ej-5-30', 'único crítico real (0,0)', conjunto(criticos(f30), [(0, 0)]), 1, r"Único punto crítico: $(0,0)$")
    f31 = x ** 3 + y ** 2 - x * y
    c('ej-5-31', '(1,−1) no crítico; (0,0) silla; (1/6,1/12) mínimo −1/432; f(−1,0) = −1',
      lista([sp.diff(f31, x).subs({x: 1, y: -1}), hd(f31, (0, 0))[0]] + hd(f31, (R(1, 6), R(1, 12))) + [val(f31, (R(1, 6), R(1, 12))), val(f31, (-1, 0))], [4, -1, 1, 1, R(-1, 432), -1]), 1,
      r"-\frac1{432}")
    f32 = y + x ** 2 * y ** 2 - x ** 2 + y ** 2
    c('ej-5-32', 'único crítico (0,−1/2), d = −3', lista([conjunto(criticos(f32), [(0, R(-1, 2))]), hd(f32, (0, R(-1, 2)))[0]], [1, -3]), 1, r"d=-\frac32\cdot2-0=-3")
    f33 = x ** 2 * sp.sin(y) ** 2
    c('ej-5-33', 'Hessiana nula en (0,0) (dudoso); f ≥ 0 = f(0,0): mínimo', lista([sp.hessian(f33, (x, y)).subs({x: 0, y: 0}) == sp.zeros(2, 2)], [True]), 1, r"Respuesta a)")
    f34 = (x ** 2 + 3 * y ** 2) / (x ** 2 + y ** 2 + 1) ** 2
    c('ej-5-34', 'críticos (0,0), (±1,0), (0,±1); plano z = 1/4; f(0,±1) = 3/4',
      lista([conjunto(criticos(f34), [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]), val(f34, (-1, 0)), val(f34, (0, 1))] + hd(f34, (0, 1)) + hd(f34, (-1, 0))[:1],
            [1, R(1, 4), R(3, 4), R(3, 2), -1, R(-1, 2)]), 1, r"z=\frac14")
    f35 = x * (1 - sp.cos(y)) + y * (1 - sp.cos(x)) + x * y
    c('ej-5-35', '∇f(π,0) = (0, 2+π); d(0,0) = −1', lista([sp.diff(f35, x).subs({x: pi, y: 0}), sp.diff(f35, y).subs({x: pi, y: 0}), hd(f35, (0, 0))[0]], [0, 2 + pi, -1]), 1,
      r"\nabla f(\pi,0)=(0,\,2+\pi)")
    f36 = (x - 1) * (12 - 4 * x + 3 * y) + (y - R(9, 10)) * (15 + x - 10 * y)
    p36 = criticos(f36)[0]
    c('ej-5-36', 'x = 193/72, y = 571/360, d = 144, ganancia ≈ 11,39', lista(list(p36) + hd(f36, p36) + [r(val(f36, p36), 2)], [R(193, 72), R(571, 360), 144, -8, R('11.39')]), 1,
      r"y=\frac{571}{360}")
    f37 = x ** 2 + y ** 2 + (x - 4) ** 2 + y ** 2 + (x - 1) ** 2 + (y - 3) ** 2
    c('ej-5-37', 'P = (5/3,1), f = 44/3', lista(list(criticos(f37)[0]) + [val(f37, (R(5, 3), 1))], [R(5, 3), 1, R(44, 3)]), 1, r"$P=\left(\frac53,1\right)$")
    h38 = (1 - y ** 2) * y
    c('ej-5-38', 'máximo de x²y en el disco: 2√3/9 (frontera)', lista([sp.maximum(h38, y, sp.Interval(-1, 1)), sp.minimum(h38, y, sp.Interval(-1, 1))], [2 * sp.sqrt(3) / 9, -2 * sp.sqrt(3) / 9]), 1,
      r"\frac{2\sqrt3}9")
    c('ej-5-39', 'f(x,−x) = 0: constante sobre la recta', sp.expand((x ** 2 - y ** 2).subs(y, -x)), 0, r"f(x,-x)=x^2-x^2=0")
    rr = sp.symbols('r', positive=True)
    A40 = 2 * pi * rr ** 2 + 600 / rr
    r40 = sp.solve(sp.diff(A40, rr), rr)[0]
    c('ej-5-40', 'r = (150/π)^{1/3} ≈ 3,628; h = 2r; S ≈ 248,08', lista([sp.simplify(r40 ** 3 - 150 / pi), r(r40, 3), r(A40.subs(rr, r40), 2), sp.simplify(300 / (pi * r40 ** 2) - 2 * r40)], [0, R('3.628'), R('248.08'), 0]), 1,
      r"r^3=\frac{150}\pi")
    c('ej-5-41', 'procedimiento (interior + frontera con Lagrange); sin cálculo final', sp.Integer(1), 1, r"F=f+\lambda(x^2+y^2-1)")
    L42 = lagrange(x - y, x ** 2 + y ** 2 - 1)
    c('ej-5-42', 'máximo √2, mínimo −√2', lista([max(val(x - y, p) for p in L42), min(val(x - y, p) for p in L42)], [sp.sqrt(2), -sp.sqrt(2)]), 1,
      r"Máximo $\sqrt2$ en $\left(\frac{\sqrt2}2,-\frac{\sqrt2}2\right)$")
    T = sp.exp(x ** 2) + sp.exp(y ** 2)
    L43 = lagrange(T, x ** 2 + y ** 2 - 4)
    v43 = [val(T, p) for p in L43] + [val(T, (0, 0))]
    c('ej-5-43', 'mínimo 2, máximo 1 + e⁴ ≈ 55,60; 2e² ≈ 14,78', lista([min(v43, key=float), max(v43, key=float), r(1 + E_ ** 4, 2), r(2 * E_ ** 2, 2)], [2, 1 + E_ ** 4, R('55.60'), R('14.78')]), 1,
      r"T(\pm\sqrt2,\pm\sqrt2)=2e^2\approx14.78")
    c('ej-5-44', 'único crítico (−1,−2), λ = 1', conjunto(lagrange(x ** 2 + y, 2 * x - y), [(-1, -2)]), 1, r"$(-1,-2)$ ($\lambda=1$)")
    xs = sp.symbols('xs', nonnegative=True)
    h45 = 300 - xs + 3 * sp.sqrt(xs ** 2 + 100 ** 2)
    c('ej-5-45', 'x = 25√2, h = 300 + 200√2 ≈ 582,8; h(0) = 600; h(300) = 300√10',
      lista([sp.solve(sp.diff(h45, xs), xs)[0], sp.simplify(h45.subs(xs, 25 * sp.sqrt(2))), r(300 + 200 * sp.sqrt(2), 1), h45.subs(xs, 0), sp.simplify(h45.subs(xs, 300))],
            [25 * sp.sqrt(2), 300 + 200 * sp.sqrt(2), R('582.8'), 600, 300 * sp.sqrt(10)]), 1, r"h(25\sqrt2)=300+200\sqrt2\approx582.8")
    L46 = lagrange(x + y + z, x ** 2 + 2 * y ** 2 + 3 * z ** 2 - 1, (x, y, z))
    v46 = [val(x + y + z, p, (x, y, z)) for p in L46]
    c('ej-5-46', 'máximo √66/6 ≈ 1,354, mínimo −√66/6', lista([max(v46, key=float), min(v46, key=float), r(sp.sqrt(66) / 6, 3)], [sp.sqrt(66) / 6, -sp.sqrt(66) / 6, R('1.354')]), 1,
      r"\frac{\sqrt{66}}6\approx1.354")
    L47 = lagrange(x ** 2 + y ** 2 + z ** 2, x * y + 4 - z, (x, y, z))
    c('ej-5-47', 'candidatos (0,0,4) [16] y (±√3,∓√3,1) [7]: distancia √7',
      lista([conjunto(L47, [(0, 0, 4), (sp.sqrt(3), -sp.sqrt(3), 1), (-sp.sqrt(3), sp.sqrt(3), 1)]), sp.sqrt(min(val(x ** 2 + y ** 2 + z ** 2, p, (x, y, z)) for p in L47))], [1, sp.sqrt(7)]), 1,
      r"Distancia mínima $\sqrt7$")
    f48 = x ** 2 - x * y + y ** 2
    cand48 = [(0, 0), (1, R(1, 2)), (-1, R(-1, 2)), (R(1, 2), 1), (R(-1, 2), -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    v48 = [val(f48, p) for p in cand48]
    c('ej-5-48', 'mínimo 0 en (0,0); máximo 3 en (−1,1), (1,−1); 3/4 en los lados', lista([min(v48), max(v48), val(f48, (1, R(1, 2)))], [0, 3, R(3, 4)]), 1,
      r"Mínimo $0$ en $(0,0)$; máximo $3$ en $(-1,1)$ y $(1,-1)$")
    # ---- Ejemplos propios
    fp1 = x ** 2 + x * y + y ** 2 - 3 * x
    c('p1', 'mínimo en (2,−1), f = −3', lista(list(criticos(fp1)[0]) + hd(fp1, (2, -1)) + [val(fp1, (2, -1))], [2, -1, 3, 2, -3]), 1, r"$f(2,-1)=4-2+1-6=-3$")
    fp2 = x ** 4 + y ** 4 - 4 * x * y
    c('p2', 'críticos (0,0) silla, (±1,±1) mínimos −2; identidad de f + 2',
      lista([conjunto(criticos(fp2), [(0, 0), (1, 1), (-1, -1)]), hd(fp2, (0, 0))[0]] + hd(fp2, (1, 1)) + [val(fp2, (1, 1)), sp.expand(fp2 + 2 - (x ** 2 - y ** 2) ** 2 - 2 * (x * y - 1) ** 2)],
            [1, -16, 128, 12, -2, 0]), 1, r"(x^2-y^2)^2+2(xy-1)^2\ge0")
    Lp3 = lagrange(4 * x * y, x ** 2 / 4 + y ** 2 - 1)
    c('p3', 'área máxima 4 en (√2, √2/2)', lista([max(val(4 * x * y, p) for p in Lp3)] + [conjunto([p for p in Lp3 if p[0] > 0 and p[1] > 0], [(sp.sqrt(2), sp.sqrt(2) / 2)])], [4, 1]), 1,
      r"$4\cdot\sqrt2\cdot\frac{\sqrt2}2=4$")
    fp4 = x ** 2 + y ** 2 - 2 * x
    vp4 = [val(fp4, p) for p in criticos(fp4) + lagrange(fp4, x ** 2 + y ** 2 - 4)]
    c('p4', 'mínimo −1 en (1,0); máximo 8 en (−2,0)', lista([min(vp4), max(vp4)], [-1, 8]), 1, r"Mínimo $-1$ en $(1,0)$; máximo $8$ en $(-2,0)$")
    c('p5', 'Lagrange sin solución; ∇g = 0 en (0,0), mínimo 0', lista([len(lagrange(x, y ** 2 - x ** 3)), sp.Integer(len(sp.solve([-3 * x ** 2, 2 * y], [x, y], dict=True)))], [0, 1]), 1,
      r"mínimo $0$ en $(0,0)$")
    # ---- Exámenes
    fx1 = x ** 3 + y ** 2 - 3 * x * y
    c('x1', 'críticos (0,0) silla, (3/2,9/4) mínimo −27/16; (1/6,1/12) no crítico',
      lista([conjunto(criticos(fx1), [(0, 0), (R(3, 2), R(9, 4))]), hd(fx1, (0, 0))[0]] + hd(fx1, (R(3, 2), R(9, 4))) + [val(fx1, (R(3, 2), R(9, 4))), sp.diff(fx1, x).subs({x: R(1, 6), y: R(1, 12)}), sp.diff(fx1, y).subs({x: R(1, 6), y: R(1, 12)})],
            [1, -9, 9, 9, R(-27, 16), R(-1, 6), R(-1, 3)]), 1, r"-\frac{27}{16}")
    fx2 = (x ** 2 - x) * (y ** 2 - y)
    c('x2', 'máximo 1/16 en (1/2,1/2); 0 en la frontera', lista([val(fx2, (R(1, 2), R(1, 2)))] + hd(fx2, (R(1, 2), R(1, 2))) + [fx2.subs(x, 0), fx2.subs(y, 1)], [R(1, 16), R(1, 4), R(-1, 2), 0, 0]), 1,
      r"Máximo absoluto $\frac1{16}$ en $\left(\frac12,\frac12\right)$")
    c('x3', 'corona cerrada y acotada + f continua: teorema de los valores extremos', sp.Integer(1), 1, r"Por el teorema de los valores extremos, sí")
    Lx4 = lagrange(x * y, x ** 2 + y ** 2 - 1)
    c('x4', 'cuatro candidatos; máximo 1/2, mínimo −1/2', lista([sp.Integer(len(Lx4)), max(val(x * y, p) for p in Lx4), min(val(x * y, p) for p in Lx4)], [4, R(1, 2), R(-1, 2)]), 1,
      r"$f=\frac12$ en $\left(\frac{\sqrt2}2,\frac{\sqrt2}2\right)$")
    Lx5 = lagrange(x ** 2 + y ** 2, 5 * x ** 2 + 6 * x * y + 5 * y ** 2 - 8)
    vx5 = [val(x ** 2 + y ** 2, p) for p in Lx5]
    c('x5', 'distancias mínima 1 y máxima 2', lista([sp.sqrt(min(vx5)), sp.sqrt(max(vx5))], [1, 2]), 1, r"distancia máxima $\sqrt4=2$ en $\pm(\sqrt2,-\sqrt2)$")
    xp, yp, zp = sp.symbols('xp yp zp', positive=True)
    Ax6 = 2 * xp * yp + 2 * xp * zp + 2 * yp * zp
    sx6 = sp.solve([sp.diff(Ax6 + lam * (xp * yp * zp - 1), v) for v in (xp, yp, zp)] + [xp * yp * zp - 1], [xp, yp, zp, lam], dict=True)
    A2 = 2 / zp + 2 / yp + 2 * yp * zp
    c('x6', 'cubo de arista 1, λ = −4, área 6; HA(1,1) = [[4,2],[2,4]]',
      lista([sp.Integer(len(sx6)), sx6[0][xp], sx6[0][lam], Ax6.subs({xp: 1, yp: 1, zp: 1})] + hd(A2, (1, 1), (yp, zp)), [1, 1, -4, 6, 12, 4]), 1,
      r"$x=y=z=1$ m (un cubo), $\lambda=-4$, área $6\ \mathrm{m}^2$")
    # ---- Práctica «Ahora hazlo tú» (respuesta final = «Resultado: …»)
    fa1 = x ** 3 - 3 * x + y ** 2 - 2 * y
    fa2 = x * y * sp.exp(-(x ** 2 + y ** 2) / 2)
    fb1 = x ** 2 - y ** 4
    fb2 = (y - x ** 2) * (y - 3 * x ** 2)
    m_ = sp.symbols('m', real=True)
    s_ = sp.symbols('s', nonnegative=True)
    hc2 = s_ * sp.exp(-s_)
    fd1 = x ** 2 + y ** 2 - x - y
    vd1 = [val(fd1, p) for p in [(R(1, 2), R(1, 2)), (R(1, 2), 0), (0, R(1, 2)), (1, 1), (0, 0), (2, 0), (0, 2)]]
    fd2 = x ** 2 + 2 * y ** 2 - x
    vd2 = [val(fd2, p) for p in criticos(fd2) + lagrange(fd2, x ** 2 + y ** 2 - 1)]
    Le2 = lagrange(x + y, x * y - 4)
    he2 = x + 4 / x
    Lf1 = lagrange(x ** 2 + y ** 2 + z ** 2, x + 2 * y + 2 * z - 9, (x, y, z))
    Lf2 = [p for p in lagrange(8 * x * y * z, x ** 2 / 4 + y ** 2 + z ** 2 / 9 - 1, (x, y, z)) if all(e > 0 for e in p)]
    Ag1 = x * y + 64 / y + 64 / x
    mm, bb = sp.symbols('m b', real=True)
    Eg2 = sum((mm * xi + bb - yi) ** 2 for xi, yi in [(0, 1), (1, 3), (2, 4)])
    P = {
        'pr-a1': (lista([conjunto(criticos(fa1), [(1, 1), (-1, 1)])] + hd(fa1, (1, 1)) + [val(fa1, (1, 1)), hd(fa1, (-1, 1))[0]], [1, 12, 6, -3, -12]), 1,
                  r"Resultado: mínimo relativo en $(1,1)$ con $f=-3$; punto de silla en $(-1,1)$"),
        'pr-a2': (lista([conjunto(criticos(fa2), [(0, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]), hd(fa2, (0, 0))[0]] + hd(fa2, (1, 1)) + hd(fa2, (1, -1)) + [val(fa2, (1, 1)), val(fa2, (-1, 1))],
                        [1, -1, 4 * sp.exp(-2), -2 * sp.exp(-1), 4 * sp.exp(-2), 2 * sp.exp(-1), sp.exp(-1), -sp.exp(-1)]), 1,
                  r"Resultado: silla en $(0,0)$; máximos $e^{-1}$ en $(1,1)$ y $(-1,-1)$; mínimos $-e^{-1}$ en $(1,-1)$ y $(-1,1)$"),
        'pr-b1': (lista([conjunto(criticos(fb1), [(0, 0)])] + hd(fb1, (0, 0)) + [fb1.subs(y, 0), fb1.subs(x, 0)], [1, 0, 2, x ** 2, -y ** 4]), 1,
                  r"Resultado: $d=0$ (dudoso); $(0,0)$ es un punto de silla ($f(x,0)=x^2>0$, $f(0,y)=-y^4&lt;0$)"),
        'pr-b2': (lista([conjunto(criticos(fb2), [(0, 0)])] + hd(fb2, (0, 0)) + [sp.expand(fb2.subs(y, 2 * x ** 2)), sp.expand(fb2.subs(y, 0)), sp.expand(fb2.subs({x: t, y: m_ * t})), sp.expand(fb2.subs(x, 0))],
                        [1, 0, 0, -x ** 4, 3 * x ** 4, m_ ** 2 * t ** 2 - 4 * m_ * t ** 3 + 3 * t ** 4, y ** 2]), 1,
                  r"Resultado: único crítico $(0,0)$ con $d=0$; mínimo sobre cada recta por el origen, pero silla: $f(x,2x^2)=-x^4&lt;0$ y $f(x,0)=3x^4>0$"),
        'pr-c1': (lista([val(x + y, (0, 0)), val(x + y, (1, 1)), sp.diff(x + y, x), sp.diff(x + y, y), sp.limit(t, t, sp.oo)], [0, 2, 1, 1, sp.oo]), 1,
                  r"Resultado: a) mínimo $0$ en $(0,0)$ y máximo $2$ en $(1,1)$; b) ni máximo ni mínimo; c) mínimo $0$ en $(0,0)$, sin máximo"),
        'pr-c2': (lista([sp.solve(sp.diff(hc2, s_), s_)[0], sp.maximum(hc2, s_, sp.Interval(0, sp.oo)), sp.minimum(hc2, s_, sp.Interval(0, sp.oo)),
                         sp.simplify(sp.diff((x ** 2 + y ** 2) * sp.exp(-(x ** 2 + y ** 2)), x) - 2 * x * (1 - x ** 2 - y ** 2) * sp.exp(-(x ** 2 + y ** 2)))],
                        [1, sp.exp(-1), 0, 0]), 1,
                  r"Resultado: mínimo absoluto $0$ en $(0,0)$; máximo absoluto $e^{-1}$ en todos los puntos de $x^2+y^2=1$"),
        'pr-d1': (lista([conjunto(criticos(fd1), [(R(1, 2), R(1, 2))]), min(vd1), max(vd1), sp.factor(fd1.subs(y, 2 - x))] + vd1, [1, R(-1, 2), 2, 2 * (x - 1) ** 2, R(-1, 2), R(-1, 4), R(-1, 4), 0, 0, 2, 2]), 1,
                  r"Resultado: mínimo $-\frac12$ en $\left(\frac12,\frac12\right)$; máximo $2$ en $(2,0)$ y $(0,2)$"),
        'pr-d2': (lista([min(vd2), max(vd2), val(fd2, (R(-1, 2), sp.sqrt(3) / 2)), val(fd2, (1, 0)), val(fd2, (-1, 0))], [R(-1, 4), R(9, 4), R(9, 4), 0, 2]), 1,
                  r"Resultado: mínimo $-\frac14$ en $\left(\frac12,0\right)$; máximo $\frac94$ en $\left(-\frac12,\pm\frac{\sqrt3}2\right)$"),
        'pr-e1': (lista([conjunto(lagrange(x ** 2 + y ** 2, x + 2 * y - 5), [(1, 2)]), sp.expand((x ** 2 + y ** 2).subs(x, 5 - 2 * y) - 5 * (y - 2) ** 2), sp.sqrt(5) / 1, R(5) / sp.sqrt(5)],
                        [1, 5, sp.sqrt(5), sp.sqrt(5)]), 1, r"Resultado: el punto $(1,2)$; distancia mínima $\sqrt5$"),
        'pr-e2': (lista([conjunto(Le2, [(2, 2), (-2, -2)]), val(x + y, (2, 2)), val(x + y, (-2, -2)), sp.diff(he2, x, 2).subs(x, 2), sp.diff(he2, x, 2).subs(x, -2), sp.limit(he2, x, sp.oo), sp.limit(he2, x, -sp.oo)],
                        [1, 4, -4, 1, -1, sp.oo, -sp.oo]), 1,
                  r"Resultado: mínimo relativo condicionado $4$ en $(2,2)$; máximo relativo condicionado $-4$ en $(-2,-2)$; sin extremos absolutos"),
        'pr-f1': (lista([conjunto(Lf1, [(1, 2, 2)]), sp.sqrt(val(x ** 2 + y ** 2 + z ** 2, (1, 2, 2), (x, y, z)))] + hd((9 - 2 * y - 2 * z) ** 2 + y ** 2 + z ** 2, (2, 2), (y, z)), [1, 3, 36, 10]), 1,
                  r"Resultado: el punto $(1,2,2)$; distancia mínima $3$"),
        'pr-f2': (lista([conjunto(Lf2, [(2 / sp.sqrt(3), 1 / sp.sqrt(3), sp.sqrt(3))]), val(8 * x * y * z, Lf2[0], (x, y, z)), r(16 * sp.sqrt(3) / 3, 2), 2 * Lf2[0][0], 2 * Lf2[0][1], 2 * Lf2[0][2]],
                        [1, 16 * sp.sqrt(3) / 3, R('9.24'), 4 / sp.sqrt(3), 2 / sp.sqrt(3), 2 * sp.sqrt(3)]), 1,
                  r"Resultado: caja de $\frac4{\sqrt3}\times\frac2{\sqrt3}\times2\sqrt3$; volumen máximo $\frac{16\sqrt3}3\approx9{,}24$"),
        'pr-g1': (lista([conjunto([p for p in criticos(Ag1) if p[0] > 0], [(4, 4)])] + hd(Ag1, (4, 4)) + [val(Ag1, (4, 4)), R(32, 16)], [1, 3, 2, 48, 2]), 1,
                  r"Resultado: base $4\times4$ dm y altura $2$ dm; material mínimo $48\ \mathrm{dm}^2$"),
        'pr-g2': (lista(list(criticos(Eg2, (mm, bb))[0]) + hd(Eg2, (R(3, 2), R(7, 6)), (mm, bb)) + [val(Eg2, (R(3, 2), R(7, 6)), (mm, bb))], [R(3, 2), R(7, 6), 24, 10, R(1, 6)]), 1,
                  r"Resultado: $y=\frac32x+\frac76$; error mínimo $E=\frac16$"),
    }
    for eid, (v, esp, txt) in P.items():
        if (EJ / f'{eid}.html').exists() or (EJ / f'{eid}.solucion.html').exists():
            c(eid, 'resultado de la práctica', v, esp, txt)

