r"""Tema 4.2 (Funciones de varias variables): dominio, imagen, curvas y superficies de nivel, límites dobles
(reiterados, rectas, curvas, polares, emparedado) y continuidad, recalculados con sympy.

`comprobaciones(c)`: c(ejercicio, descripción, valor_sympy, esperado, trozo_latex)
  - valor_sympy: lo que calcula sympy;  esperado: lo que afirma la página;
  - trozo_latex: cadena que debe aparecer en `ejercicios/<ejercicio>.html` (o `.solucion.html`), comparada sin etiquetas,
    espacios, \, \; \! ni \displaystyle y con \dfrac/\tfrac = \frac.
Las comprobaciones de la práctica «Ahora hazlo tú» (pr-*) solo se activan cuando el ejercicio existe en `contenido/`.
Polares de U p.165: x = a + ρ cos θ, y = b + ρ sen θ; caso 2 = cota |F − l| ≤ h(ρ) → 0 con h sin θ.
"""
import pathlib

import sympy as sp

R = sp.Rational
pi = sp.pi
x, y, z, t, m, k, C = sp.symbols('x y z t m k C', real=True)
rho = sp.symbols('rho', positive=True)
th = sp.symbols('theta', real=True)
EJ = pathlib.Path(__file__).resolve().parents[2] / 'contenido' / 'tema_4_2' / 'ejercicios'


def _igual(p, q):
    p, q = sp.sympify(p), sp.sympify(q)
    if p == q:
        return True
    return sp.simplify(p - q) == 0


def lista(vals, esperados):
    return sp.Integer(int(len(vals) == len(esperados) and all(_igual(p, q) for p, q in zip(vals, esperados))))


def r(v, d):
    return R(str(round(float(v), d)))


def pol(f, a=0, b=0):
    """F(ρ, θ) = f(a + ρ cos θ, b + ρ sen θ), simplificada."""
    return sp.simplify(sp.trigsimp(f.subs({x: a + rho * sp.cos(th), y: b + rho * sp.sin(th)}, simultaneous=True)))


def cota(F, h, l=0, n=73):
    """|F − l| ≤ h(ρ) en una rejilla de θ ∈ [0, 2π] y ρ ∈ {1, 1/2, …, 1/1000} (comprobación numérica de la cota sin θ)."""
    fF = sp.lambdify((rho, th), F - l, 'math')
    fh = sp.lambdify(rho, h, 'math')
    import math
    ok = all(abs(fF(rr, 2 * math.pi * j / (n - 1))) <= fh(rr) + 1e-12
             for rr in (1, 0.5, 0.1, 0.01, 0.001) for j in range(n))
    return sp.Integer(int(ok))


def todos(cond, puntos):
    return sp.Integer(int(all(bool(cond(*p)) for p in puntos)))


def reiterados(f, a=0, b=0):
    """[lim_{y→b} lim_{x→a} f, lim_{x→a} lim_{y→b} f]."""
    return [sp.limit(sp.limit(f, x, a), y, b), sp.limit(sp.limit(f, y, b), x, a)]


def comprobaciones(c):
    # ---- Ejercicios del libro (E 4.9-4.24)
    P = R(1, 10) * R(82, 1000) * x / y
    c('ej-4-9', 'P(273,2) = 1,1193 atm', P.subs({x: 273, y: 2}), R('1.1193'), r"=\dfrac{2{,}2386}{2}=1{,}1193")
    c('ej-4-10', 'P(T,2)=1 ⇒ T ≈ 243,9; corte 0,0041 T', lista([r(sp.solve(P.subs(y, 2) - 1, x)[0], 1), sp.expand(P.subs(y, 2) / x)], [R('243.9'), R('0.0041')]), 1,
      r"T=\dfrac2{0{,}0082}\approx243{,}9")
    c('ej-4-11', 'cada punto de la gráfica tiene 3 coordenadas', len((x, y, x ** 2 + y ** 2)), 3, r"Respuesta: c).")
    c('ej-4-12', 'sobre (0,0) la esfera tiene dos puntos', len(sp.solve(z ** 2 - 1, z)), 2, r"Respuesta: no.")
    f13 = x ** 2 - y ** 3
    c('ej-4-13', 'f(1,1)=f(8,4)=0, (0,1) fuera; y³≤x² ⇔ y≤x^(2/3) en una rejilla',
      lista([f13.subs({x: 1, y: 1}), f13.subs({x: 8, y: 4}), f13.subs({x: 0, y: 1}),
             todos(lambda a, b: (b ** 3 <= a ** 2) == (b <= sp.real_root(a ** 2, 3)), [(R(i, 4), R(j, 4)) for i in range(-12, 13) for j in range(-12, 13)])],
            [0, 0, -1, 1]), 1, r"y\le\sqrt[3]{x^2}=x^{2/3}")
    c('ej-4-14', 'xy en (2,1), (-1,-3), (1,1/2)', lista([2 * 1, (-1) * (-3), 1 * R(1, 2)], [2, 3, R(1, 2)]), 1, r"=\{(x,y):xy\ge1\}")
    f15 = sp.cos(x * z + sp.log(y))
    c('ej-4-15', 'f(x,1,1) = cos x: 1 en 0 y −1 en π', lista([f15.subs({y: 1, z: 1}), f15.subs({x: 0, y: 1, z: 1}), f15.subs({x: pi, y: 1, z: 1})], [sp.cos(x), 1, -1]), 1,
      r"imagen $[-1,1]$")
    # 4.16: modelo elíptico f = x²/16 + y²/4 (niveles crecientes hacia fuera): signo de la derivada en cada dirección
    g16 = x ** 2 / 16 + y ** 2 / 4
    dd = lambda p, v: sp.sign((sp.Matrix([g16.diff(x), g16.diff(y)]).subs({x: p[0], y: p[1]})).dot(sp.Matrix(v)))  # noqa: E731
    c('ej-4-16', 'modelo elíptico: crece, se mantiene, decrece, crece', lista([dd((0, 2), (0, 1)), dd((4, 0), (0, 1)), dd((4, -1), (-1, 0)), dd((4, -1), (1, -2))], [1, 0, -1, 1]), 1,
      r"crece, se mantiene, decrece, crece.")
    c('ej-4-17', 'nivel 8: y = ±√3 x', lista(sorted(sp.solve((x ** 2 - y ** 2 / 3 + 8 - 8).subs(x, 1), y)), [-sp.sqrt(3), sp.sqrt(3)]), 1, r"y=\pm\sqrt3\,x")
    c('ej-4-18', 'x²−y=C ⇔ y=x²−C', sp.solve(x ** 2 - y - C, y)[0], x ** 2 - C, r"y=x^2-C")
    c('ej-4-19', 'reiterados 0 y 1', lista(reiterados((x ** 2 + y ** 3) / (x ** 2 + y ** 2)), [0, 1]), 1, r"$1\ne0$")
    f20 = x * y / (x ** 2 + y ** 2)
    c('ej-4-20', 'reiterados 0, recta y=x da 1/2', lista(reiterados(f20) + [sp.simplify(f20.subs(y, x))], [0, 0, R(1, 2)]), 1, r"f(x,x)=\frac{x^2}{2x^2}=\frac12")
    c('ej-4-21', 'h(0,−5)=0; mínimos de 3+x²y² y 3+x²+y⁴', lista([sp.sqrt((x ** 2 * y).subs({x: 0, y: -5})), (3 + x ** 2 * y ** 2).subs({x: 0, y: 0}), (3 + x ** 2 + y ** 4).subs({x: 0, y: 0})], [0, 3, 3]), 1,
      r"h(0,-5)=0")
    F22 = pol((x ** 2 + y ** 2) * sp.sin(1 / (x ** 2 + y ** 2)))
    c('ej-4-22', 'F = ρ² sen(1/ρ²) → 0, |F| ≤ ρ²', lista([sp.simplify(F22 - rho ** 2 * sp.sin(rho ** -2)), sp.limit(rho ** 2 * sp.sin(rho ** -2), rho, 0), cota(F22, rho ** 2)], [0, 0, 1]), 1,
      r"\le\rho^2=:h(\rho)\to0")
    c('ej-4-23', 'por x=y² vale 1; por rectas 0', lista([sp.simplify((y ** 2 / x).subs(x, y ** 2)), sp.limit((y ** 2 / x).subs(y, m * x), x, 0)], [1, 0]), 1,
      r"f(y^2,y)=\dfrac{y^2}{y^2}=1\to1")
    f24 = (x ** 2 - y ** 2) / (x ** 2 + y ** 2)
    c('ej-4-24', 'ejes: −1 y 1; polares cos 2θ', lista([sp.simplify(f24.subs(x, 0)), sp.simplify(f24.subs(y, 0)), sp.simplify(pol(f24) - sp.cos(2 * th))], [-1, 1, 0]), 1,
      r"f(0,y)=\dfrac{-y^2}{y^2}=-1\to-1")
    # ---- Ejemplos propios
    c('p1', 'corte parábola-circunferencia y = (−1+√17)/2', lista([max(sp.solve(y + y ** 2 - 4, y)), r((-1 + sp.sqrt(17)) / 2, 2)], [(-1 + sp.sqrt(17)) / 2, R('1.56')]), 1,
      r"y=\frac{-1+\sqrt{17}}2\approx1{,}56")
    c('p2', 'x²+4y² = 4 en (±2,0), (0,±1); g(x,1)=x', lista([(x ** 2 + 4 * y ** 2).subs({x: 2, y: 0}), (x ** 2 + 4 * y ** 2).subs({x: 0, y: 1}), (x * y).subs(y, 1)], [4, 4, x]), 1,
      r"pasa por $(\pm2,0)$ y $(0,\pm1)$")
    f3 = x * y ** 2 / (x ** 2 + y ** 4)
    c('p3', 'reiterados 0, rectas 0, x=y² da 1/2', lista(reiterados(f3) + [sp.limit(f3.subs(y, m * x), x, 0), sp.simplify(f3.subs(x, y ** 2))], [0, 0, 0, R(1, 2)]), 1,
      r"f(y^2,y)=\dfrac{y^4}{y^4+y^4}=\dfrac12")
    F4 = pol((x - 1) * y ** 2 / ((x - 1) ** 2 + y ** 2), 1, 0)
    c('p4', 'F = ρ cos θ sen²θ, |F| ≤ ρ ⇒ c = 0', lista([sp.simplify(F4 - rho * sp.cos(th) * sp.sin(th) ** 2), cota(F4, rho)], [0, 1]), 1, r"<b>Respuesta: $c=0$.</b>")
    F5 = pol(x ** 3 / (x ** 2 + 2 * y ** 2))
    c('p5', 'F = ρcos³θ/(1+sen²θ), |F| ≤ ρ', lista([sp.simplify(F5 - rho * sp.cos(th) ** 3 / (1 + sp.sin(th) ** 2)), cota(F5, rho)], [0, 1]), 1,
      r"F(\rho,\theta)=\dfrac{\rho\cos^3\theta}{1+\operatorname{sen}^2\theta}")
    # ---- Exámenes
    c('x1', 'h(1,0)=ln 3; (2,0) fuera', lista([(sp.log(4 - x ** 2 - y ** 2) + sp.sqrt(x ** 2 + y ** 2 - 1)).subs({x: 1, y: 0}), 4 - 2 ** 2], [sp.log(3), 0]), 1,
      r"D=\{1\le x^2+y^2&lt;4\}")
    f2 = x * sp.log(y) + y * sp.log(x)
    c('x2', 'f(x,1)=ln x; f(e^c,1)=c', lista([sp.simplify(f2.subs(y, 1)), sp.simplify(f2.subs(y, 1).subs(x, sp.exp(C)))], [sp.log(x), C]), 1,
      r"f(x,1)=x\ln1+1\cdot\ln x=\ln x")
    c('x3', 'radios √((C+4)/2): 1, 2, 3', lista([sp.sqrt(R(cc + 4, 2)) for cc in (-2, 4, 14)], [1, 2, 3]), 1, r"$C=14$: radio $3$")
    c('x4', 'ejes: −1 y 1', lista([sp.simplify(f24.subs(x, 0)), sp.simplify(f24.subs(y, 0))], [-1, 1]), 1, r"Por $x=0$: $f(0,y)=-1\to-1$")
    f5 = sp.atan(x * y / (x ** 2 + y ** 2))
    c('x5', 'por y=mx: arctg(m/(1+m²)); m=1 ≈ 0,4636', lista([sp.simplify(f5.subs(y, m * x) - sp.atan(m / (1 + m ** 2))), r(sp.atan(R(1, 2)), 4)], [0, R('0.4636')]), 1,
      r"\operatorname{arctg}\frac12\approx0{,}4636")
    F6 = pol((x ** 3 + y ** 4) / (x ** 2 + y ** 2))
    c('x6', 'F = ρcos³θ + ρ²sen⁴θ, |F| ≤ ρ+ρ²', lista([sp.simplify(F6 - rho * sp.cos(th) ** 3 - rho ** 2 * sp.sin(th) ** 4), cota(F6, rho + rho ** 2)], [0, 1]), 1,
      r"F(\rho,\theta)=\dfrac{\rho^3\cos^3\theta+\rho^4\operatorname{sen}^4\theta}{\rho^2}=\rho\cos^3\theta+\rho^2\operatorname{sen}^4\theta")
    f7 = x ** 2 * y ** 3 / (x ** 4 + y ** 2)
    c('x7', 'por y=mx: m³x³/(x²+m²) → 0 ≠ 1', lista([sp.simplify(f7.subs(y, m * x) - m ** 3 * x ** 3 / (x ** 2 + m ** 2)), sp.limit(f7.subs(y, m * x), x, 0), cota(pol(f7), rho ** 3)], [0, 0, 1]), 1,
      r"f(x,mx)=\dfrac{m^3x^5}{x^4+m^2x^2}=\dfrac{m^3x^3}{x^2+m^2}\to0")
    # ---- Práctica «Ahora hazlo tú» (respuesta final = «Resultado: …»)
    da1 = lambda a, b: bool(a + b >= 0) and bool(a != b)  # noqa: E731
    da2 = lambda a, b: bool(-1 <= a + b) and bool(a + b <= 1) and bool(a * b >= 0)  # noqa: E731
    tri = lambda a, b: (bool(a >= 0) and bool(b >= 0) and bool(a + b <= 1)) or (bool(a <= 0) and bool(b <= 0) and bool(a + b >= -1))  # noqa: E731
    rejilla = [(R(i, 10), R(j, 10)) for i in range(-20, 21) for j in range(-20, 21)]
    fb1 = 1 + sp.sqrt(4 - x ** 2 - y ** 2)
    fb2 = (x + y) / sp.sqrt(x ** 2 + y ** 2)
    Fb2 = pol(fb2)
    fc2 = 2 * y / (x ** 2 + y ** 2)
    kk = sp.symbols('kk', nonzero=True, real=True)
    fd1 = sp.sqrt(x ** 2 + y ** 2 + z ** 2)
    fd2 = sp.log(z - x ** 2 - y ** 2)
    fe1 = (x ** 2 - x * y) / (x ** 2 + y ** 2)
    fe2 = x ** 2 * y / (x ** 4 + y ** 2)
    Ff1 = pol((x ** 4 + y ** 4) / (x ** 2 + y ** 2))
    Fg1 = pol(x * y / sp.sqrt(x ** 2 + y ** 2))
    b = sp.symbols('b', real=True)
    tg2 = [(R(i, 7), R(j, 3)) for i in range(-6, 7) if i != 0 for j in range(-6, 7)]
    P = {
        'pr-a1': (lista([sp.Integer(int(da1(2, -2))), (sp.sqrt(x + y) / (x - y)).subs({x: 2, y: -2}),
                         sp.Integer(int(da1(1, 1))), sp.Integer(int(da1(0, 0))), sp.Integer(int(da1(-2, 1)))], [1, 0, 0, 0, 0]), 1,
                  r"Resultado: $D=\{(x,y):\ x+y\ge0,\ x\ne y\}$; solo $(2,-2)$ está en $D$"),
        'pr-a2': (lista([todos(lambda a, b: da2(a, b) == tri(a, b), rejilla), sp.Integer(int(da2(0, 0))), sp.Integer(int(da2(R(1, 2), R(1, 2)))),
                         sp.Integer(int(da2(1, 1))), sp.Integer(int(da2(1, R(-1, 2)))), (sp.asin(x + y) + sp.sqrt(x * y)).subs({x: R(1, 2), y: R(1, 2)})],
                        [1, 1, 1, 0, 0, pi / 2 + R(1, 2)]), 1,
                  r"Resultado: $D$ = triángulo de vértices $(0,0),(1,0),(0,1)$ $\cup$ triángulo de vértices $(0,0),(-1,0),(0,-1)$ (cerrados); están $(0,0)$ y $\left(\frac12,\frac12\right)$"),
        'pr-b1': (lista([fb1.subs({x: 0, y: 0}), fb1.subs({x: 2, y: 0}), fb1.subs({x: sp.sqrt(3), y: 0}),
                         sp.minimum(1 + sp.sqrt(4 - t ** 2), t, sp.Interval(0, 2)), sp.maximum(1 + sp.sqrt(4 - t ** 2), t, sp.Interval(0, 2))], [3, 1, 2, 1, 3]), 1,
                  r"Resultado: dominio $x^2+y^2\le4$; imagen $[1,3]$"),
        'pr-b2': (lista([sp.simplify(Fb2 - sp.cos(th) - sp.sin(th)), sp.simplify(sp.expand_trig(sp.sqrt(2) * sp.sin(th + pi / 4)) - sp.cos(th) - sp.sin(th)),
                         sp.maximum(sp.cos(th) + sp.sin(th), th, sp.Interval(0, 2 * pi)), sp.minimum(sp.cos(th) + sp.sin(th), th, sp.Interval(0, 2 * pi)),
                         fb2.subs({x: 1, y: 1}), fb2.subs({x: -1, y: -1}), fb2.subs({x: 1, y: -1}), fb2.subs({x: 1, y: 0})],
                        [0, 0, sp.sqrt(2), -sp.sqrt(2), sp.sqrt(2), -sp.sqrt(2), 0, 1]), 1,
                  r"Resultado: $D=\mathbb R^2\setminus\{(0,0)\}$; imagen $[-\sqrt2,\sqrt2]$"),
        'pr-c1': (lista([(y / x).subs({x: 2, y: 6}), sp.simplify((y / x).subs(y, k * x)), (y / x).subs({x: 1, y: k})], [3, k, k]), 1,
                  r"Resultado: la curva de nivel $k$ es la recta $y=kx$ sin el origen; por $(2,6)$ pasa la de nivel $3$; imagen $\mathbb R$"),
        'pr-c2': (lista([sp.expand(kk * (x ** 2 + y ** 2) - 2 * y - kk * (x ** 2 + (y - 1 / kk) ** 2 - 1 / kk ** 2)), fc2.subs({x: 1, y: 1}), fc2.subs({x: 0, y: -1}),
                         sp.simplify(fc2.subs({x: 0, y: 2 / kk})), fc2.subs({x: 1, y: 0}), sp.simplify((x ** 2 + (y - 1 / kk) ** 2 - 1 / kk ** 2).subs({x: 0, y: 0}))],
                        [0, 1, -2, kk, 0, 0]), 1,
                  r"Resultado: $k\ne0$: circunferencia $x^2+\left(y-\frac1k\right)^2=\frac1{k^2}$ sin el origen; $k=0$: el eje $x$ sin el origen; imagen $\mathbb R$"),
        'pr-d1': (lista([fd1.subs({x: 2, y: 3, z: 6}), sp.simplify(fd1.subs({x: rho, y: 0, z: 0}))], [7, rho]), 1,
                  r"Resultado: $D=\mathbb R^3$; imagen $[0,\infty)$; superficies de nivel: esferas $x^2+y^2+z^2=k^2$ ($k>0$); por $(2,3,6)$ pasa la de nivel $7$"),
        'pr-d2': (lista([fd2.subs({x: 1, y: 1, z: 3}), sp.simplify(fd2.subs({x: 0, y: 0, z: sp.exp(C)})), sp.solve(fd2 - k, z)[0]], [0, C, x ** 2 + y ** 2 + sp.exp(k)]), 1,
                  r"Resultado: $D=\{(x,y,z):z>x^2+y^2\}$; imagen $\mathbb R$; superficie de nivel $k$: el paraboloide $z=x^2+y^2+e^k$; por $(1,1,3)$ pasa la de nivel $0$"),
        'pr-e1': (lista([sp.simplify(fe1.subs(y, m * x) - (1 - m) / (1 + m ** 2)), ((1 - m) / (1 + m ** 2)).subs(m, 0), ((1 - m) / (1 + m ** 2)).subs(m, 1)] + reiterados(fe1),
                        [0, 1, 0, 0, 1]), 1,
                  r"Resultado: por $y=mx$ sale $\frac{1-m}{1+m^2}$, que depende de $m$: el límite no existe"),
        'pr-e2': (lista(reiterados(fe2) + [sp.simplify(fe2.subs(y, m * x) - m * x / (x ** 2 + m ** 2)), sp.limit(fe2.subs(y, m * x), x, 0),
                                           sp.simplify(fe2.subs(y, x ** 2)), sp.simplify(fe2.subs(y, k * x ** 2) - k / (1 + k ** 2))],
                        [0, 0, 0, 0, R(1, 2), 0]), 1,
                  r"Resultado: rectas y reiterados dan $0$, pero por $y=x^2$ sale $\frac12$: el límite no existe"),
        'pr-f1': (lista([sp.simplify(Ff1 - rho ** 2 * (sp.cos(th) ** 4 + sp.sin(th) ** 4)), cota(Ff1, rho ** 2), sp.expand((x ** 2 + y ** 2) ** 2 - x ** 4 - y ** 4),
                         sp.maximum(sp.cos(th) ** 4 + sp.sin(th) ** 4, th, sp.Interval(0, 2 * pi))], [0, 1, 2 * x ** 2 * y ** 2, 1]), 1,
                  r"Resultado: $\displaystyle\lim_{(x,y)\to(0,0)}\frac{x^4+y^4}{x^2+y^2}=0$ (cota $|F|\le\rho^2$)"),
        'pr-f2': (lista([sp.simplify(pol(sp.sin(x ** 2 + y ** 2) / (x ** 2 + y ** 2)) - sp.sin(rho ** 2) / rho ** 2), sp.limit(sp.sin(rho ** 2) / rho ** 2, rho, 0),
                         sp.simplify(pol(sp.sin(x ** 2 + y ** 2) / (x ** 2 + 2 * y ** 2)) - sp.sin(rho ** 2) / (rho ** 2 * (1 + sp.sin(th) ** 2))),
                         sp.limit(sp.sin(x ** 2) / x ** 2, x, 0), sp.limit(sp.sin(y ** 2) / (2 * y ** 2), y, 0)], [0, 1, 0, 1, R(1, 2)]), 1,
                  r"Resultado: a) el límite vale $1$; b) no existe (por el eje $x$ sale $1$ y por el eje $y$ sale $\frac12$)"),
        'pr-g1': (lista([sp.simplify(Fg1 - rho * sp.cos(th) * sp.sin(th)), cota(Fg1, rho), cota(Fg1, rho / 2)], [0, 1, 1]), 1,
                  r"Resultado: $f$ es continua en $\mathbb R^2$ ($|F|\le\rho\to0=f(0,0)$)"),
        'pr-g2': (lista([todos(lambda a, bb: abs(sp.sin(a * bb) / a) <= abs(bb) + R(1, 10 ** 12), tg2), sp.limit(sp.sin(x * b) / x, x, 0),
                         todos(lambda a, bb: sp.simplify(bb * sp.sin(a * bb) / (a * bb) - sp.sin(a * bb) / a) == 0, [(p, q) for p, q in tg2 if q != 0])],
                        [1, b, 1]), 1,
                  r"Resultado: $f$ es continua en todo $\mathbb R^2$ (en el eje $y$, $\lim_{(x,y)\to(0,b)}f=b=f(0,b)$)"),
    }
    for eid, (val, esp, txt) in P.items():
        if (EJ / f'{eid}.html').exists() or (EJ / f'{eid}.solucion.html').exists():
            c(eid, 'resultado de la práctica', val, esp, txt)
