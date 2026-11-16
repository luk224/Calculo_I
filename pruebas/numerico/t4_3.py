r"""Tema 4.3 (Derivadas parciales, gradiente, orden superior y direccional): parciales por las reglas y por la
definición, gradiente, puntos críticos, rectas tangentes a cortes y a curvas de nivel, Hessiana, Schwarz,
derivada direccional y dirección de máximo crecimiento, recalculados con sympy.

`comprobaciones(c)`: c(ejercicio, descripción, valor_sympy, esperado, trozo_latex)
  - valor_sympy: lo que calcula sympy;  esperado: lo que afirma la página;
  - trozo_latex: cadena que debe aparecer en `ejercicios/<ejercicio>.html` (o `.solucion.html`), comparada sin etiquetas,
    espacios, \, \; \! ni \displaystyle y con \dfrac/\tfrac = \frac.
Las comprobaciones de la práctica «Ahora hazlo tú» (pr-*) solo se activan cuando el ejercicio existe en `contenido/`.
Convenio de U p.176: ∂²f/∂y∂x = ∂/∂y(∂f/∂x); Hf = [[f_xx, ∂²f/∂x∂y], [∂²f/∂y∂x, f_yy]].
"""
import pathlib

import sympy as sp

R = sp.Rational
pi = sp.pi
x, y, z, t, s, h, m = sp.symbols('x y z t s h m', real=True)
a, b = sp.symbols('a b', real=True)
rho = sp.symbols('rho', positive=True)
th = sp.symbols('theta', real=True)
s2, s5 = sp.sqrt(2), sp.sqrt(5)
EJ = pathlib.Path(__file__).resolve().parents[2] / 'contenido' / 'tema_4_3' / 'ejercicios'


def _igual(p, q):
    p, q = sp.sympify(p), sp.sympify(q)
    if p == q:
        return True
    if isinstance(p, sp.Set) or isinstance(q, sp.Set):
        return False
    return sp.simplify(p - q) == 0


def lista(vals, esperados):
    vals, esperados = list(vals), list(esperados)
    return sp.Integer(int(len(vals) == len(esperados) and all(_igual(p, q) for p, q in zip(vals, esperados))))


def r(v, d):
    return R(str(round(float(v), d)))


def grad(f, vs=(x, y), punto=None):
    g = [sp.diff(f, v) for v in vs]
    return [sp.simplify(e.subs(dict(zip(vs, punto)))) for e in g] if punto is not None else [sp.simplify(e) for e in g]


def hess(f, vs=(x, y), punto=None):
    """Hf con la convención de U: fila i, columna j = ∂/∂x_i (∂f/∂x_j)."""
    H = sp.Matrix(len(vs), len(vs), lambda i, j: sp.diff(f, vs[j], vs[i]))
    return H.subs(dict(zip(vs, punto))) if punto is not None else H.applyfunc(sp.simplify)


def plano(H):
    return list(H)


def criticos(f, vs=(x, y)):
    return sorted([tuple(sp.Tuple(*[d[v] for v in vs])) for d in sp.solve(grad(f, vs), vs, dict=True)], key=str)


def unit(*w):
    w = sp.Matrix(w)
    return w / sp.sqrt(w.dot(w))


def dir_def(f, p, v, vs=(x, y), f0=None):
    """Derivada direccional por la definición (Def. 4.10): lim_{h→0} (f(p+hv) − f(p))/h (f0 = f(p) si f va a trozos)."""
    fp = f.subs(dict(zip(vs, [pi_ + h * vi for pi_, vi in zip(p, v)])), simultaneous=True)
    f0 = f.subs(dict(zip(vs, p)), simultaneous=True) if f0 is None else f0
    return sp.limit(sp.simplify((fp - f0) / h), h, 0)


def comprobaciones(c):
    # ---- Ejercicios del libro (E 4.25-4.44)
    pr = sp.Function('f')
    c('ej-4-25', 'modelo con ∂f/∂p > 0 y ∂f/∂c < 0 (signos)', sp.Integer(1), 1, r"\frac{\partial f}{\partial p}>0")
    c('ej-4-26', 'el gradiente de f(x,y,z) tiene 3 componentes', len(grad(pr(x, y, z), (x, y, z))), 3, r"Respuesta: b).")
    F = sp.integrate(s * sp.exp(s), (s, 0, y))
    f = x * F
    c('ej-4-27', 'gradiente por partes y por el TFC', lista(grad(f) + [sp.diff(F, y)], [1 + (y - 1) * sp.exp(y), x * y * sp.exp(y), y * sp.exp(y)]), 1,
      r"$\nabla f(x,y)=\big(1+(y-1)e^y,\ xye^y\big)$")
    f = y * sp.tan(sp.exp(x)) + sp.cos(x + y) ** 2
    c('ej-4-28', '∇f(0,0) = (0, tg 1)', lista(grad(f, punto=(0, 0)), [0, sp.tan(1)]), 1, r"$\nabla f(0,0)=(0,\operatorname{tg}1)$")
    f = sp.exp(x - y) * sp.cos(x) + (y - 1) ** 3
    g = grad(f, punto=(0, 0))
    c('ej-4-29', '∇f(0,0) = (1,2) y (−2,1)·∇f = 0', lista(g + [-2 * g[0] + 1 * g[1]], [1, 2, 0]), 1, r"$\nabla f(0,0)=(1,\ -1+3)=(1,2)$")
    f = x ** 2 + y ** 2
    c('ej-4-30', 'f(1,2) = 5, f_y(1,2) = 4', lista([f.subs({x: 1, y: 2}), sp.diff(f, y).subs({x: 1, y: 2})], [5, 4]), 1,
      r"$(x,y,z)=(1,2,5)+\lambda(0,1,4)$")
    c('ej-4-31', '∇ln(xy)(2,3)', lista(grad(sp.log(x * y), punto=(2, 3)), [R(1, 2), R(1, 3)]), 1, r"$\nabla f(2,3)=\big(\frac12,\frac13\big)$")
    c('ej-4-32', 'único punto crítico (0,0,1)', lista(criticos(x ** 2 + y ** 3 + z ** 2 - 2 * z, (x, y, z)), [(0, 0, 1)]), 1, r"solo el punto $(0,0,1)$")
    f = x ** 2 * y ** 2 / (x ** 2 + y ** 2)
    fx = 2 * x * y ** 4 / (x ** 2 + y ** 2) ** 2
    c('ej-4-33', 'f_x fuera del origen y en el origen (f(h,0) = 0)', lista([sp.simplify(sp.diff(f, x) - fx), sp.simplify(f.subs({x: h, y: 0}))], [0, 0]), 1,
      r"\frac{2xy^4}{(x^2+y^2)^2}")
    Fp = sp.simplify(fx.subs({x: rho * sp.cos(th), y: rho * sp.sin(th)}))
    c('ej-4-34', 'f_x en polares = 2ρ cos θ sen⁴θ', sp.simplify(Fp - 2 * rho * sp.cos(th) * sp.sin(th) ** 4), 0,
      r"$F(\rho,\theta)=2\rho\cos\theta\operatorname{sen}^4\theta$")
    u = sp.sin(x - t)
    c('ej-4-35', 'u_tt = u_xx = −sen(x−t)', lista([sp.diff(u, t, 2), sp.diff(u, x, 2)], [-sp.sin(x - t), -sp.sin(x - t)]), 1,
      r"ambas valen $-\operatorname{sen}(x-t)$")
    c('ej-4-36', 'Hessiana en (0,1,0)', lista(plano(hess(sp.cos(x) + y ** 2 / 2, (x, y, z), (0, 1, 0))), [-1, 0, 0, 0, 1, 0, 0, 0, 0]), 1,
      r"$Hf(0,1,0)=\begin{pmatrix}-1&0&0\\0&1&0\\0&0&0\end{pmatrix}$")
    c('ej-4-37', '∇f(1,0) y Hf(1,0) de x²y', lista(grad(x ** 2 * y, punto=(1, 0)) + plano(hess(x ** 2 * y, punto=(1, 0))), [0, 1, 0, 2, 2, 0]), 1,
      r"$Hf(1,0)=\begin{pmatrix}0&2\\2&0\end{pmatrix}$")
    f = (x ** 3 * y - x * y ** 3) / (x ** 2 + y ** 2)
    fx, fy = sp.diff(f, x), sp.diff(f, y)
    # ∂²f/∂y∂x(0,0) = lim (f_x(0,h) − 0)/h ; ∂²f/∂x∂y(0,0) = lim (f_y(h,0) − 0)/h
    c('ej-4-38', 'cruzadas en el origen −1 y 1', lista([sp.limit(sp.simplify(fx.subs({x: 0, y: h})) / h, h, 0),
                                                       sp.limit(sp.simplify(fy.subs({x: h, y: 0})) / h, h, 0),
                                                       sp.limit(sp.simplify(fx.subs({x: h, y: 0})) / h, h, 0)], [-1, 1, 0]), 1,
      r"$Hf(0,0)=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$")
    fxy = sp.diff(f, y, x)
    c('ej-4-39', 'cruzada fuera del origen y límites 1 y −1 por los ejes',
      lista([sp.simplify(fxy - (x ** 2 - y ** 2) * (x ** 4 + 10 * x ** 2 * y ** 2 + y ** 4) / (x ** 2 + y ** 2) ** 3),
             sp.simplify(fxy.subs(y, 0)), sp.simplify(fxy.subs(x, 0))], [0, 1, -1]), 1,
      r"\frac{(x^2-y^2)(x^4+10x^2y^2+y^4)}{(x^2+y^2)^3}")
    c('ej-4-40', 'D_v f = 9/2 > π', lista([(sp.Matrix([sp.sqrt(8), 3, s5]).T * unit(s2, 3, s5))[0], sp.Integer(int(bool(R(9, 2) > pi)))], [R(9, 2), 1]), 1,
      r"$D_vf=\frac{18}4=\frac92=4{,}5$")
    c('ej-4-41', 'D_v f(1,−1,2) = 0 por la definición', dir_def(x * y - z, (1, -1, 2), list(unit(0, 1, 1)), (x, y, z)), 0,
      r"$D_vf(1,-1,2)=\lim_{h\to0}0=0$")
    g = sp.Matrix(grad(x * sp.cos(x + y), punto=(0, 0)))
    c('ej-4-42', 'ángulo π/4', sp.acos(sp.simplify(g.dot(sp.Matrix([1, 1])) / (g.norm() * s2))), pi / 4, r"$\alpha=\frac\pi4$")
    g = sp.Matrix(grad(x ** 2 / (x ** 2 + y ** 2), punto=(1, 1)))
    c('ej-4-43', 'dirección (√2/2, −√2/2)', lista(list(g) + list(g / g.norm()), [R(1, 2), R(-1, 2), s2 / 2, -s2 / 2]), 1,
      r"$\sqrt2\big(\frac12,-\frac12\big)=\big(\frac{\sqrt2}2,-\frac{\sqrt2}2\big)$")
    cur = sp.Matrix([1 + t, 2 + t, (1 + t) ** 2 * (2 + t)])
    c('ej-4-44', 'director (1,1,5)', lista(list(cur.diff(t).subs(t, 0)) + [dir_def(x ** 2 * y, (1, 2), list(unit(1, 1)))], [1, 1, 5, 5 / s2]), 1,
      r"$(x,y,z)=(1,2,2)+\lambda(1,1,5)$")
    # ---- Ejemplos propios
    c('p1', '∇f(1,0) = (0,1)', lista(grad(x ** 3 * y ** 2 + sp.exp(x * y), punto=(1, 0)), [0, 1]), 1, r"$\nabla f(1,0)=(0,1)$")
    f = x * sp.exp(y) + y ** 2
    gp = sp.Matrix(grad(f, punto=(1, 0)))
    c('p2', 'Hf(1,0), D_v = 7/5 y máximo √2', lista(plano(hess(f, punto=(1, 0))) + [gp.dot(unit(3, 4)), gp.norm()], [0, 1, 1, 3, R(7, 5), s2]), 1,
      r"$Hf(1,0)=\begin{pmatrix}0&1\\1&3\end{pmatrix}$")
    f = x * y / (x ** 2 + y ** 2)
    c('p3', 'f(x,mx) = m/(1+m²) y f(h/√2,h/√2) = 1/2', lista([sp.simplify(f.subs(y, m * x)), sp.simplify(f.subs({x: h / s2, y: h / s2}))],
                                                            [m / (1 + m ** 2), R(1, 2)]), 1, r"$f(x,mx)=\frac m{1+m^2}$")
    f = x ** 2 * y / (x ** 2 + y ** 2)
    c('p4', 'D_v f(0,0) = a²b (v = (cos θ, sen θ)) y √2/4', lista([sp.simplify(f.subs({x: h * sp.cos(th), y: h * sp.sin(th)}) / h),
                                              dir_def(f, (0, 0), [1 / s2, 1 / s2], f0=0)], [sp.cos(th) ** 2 * sp.sin(th), s2 / 4]), 1,
      r"$D_vf(0,0)=\frac12\cdot\frac1{\sqrt2}=\frac{\sqrt2}4\ne0$")
    # ---- Exámenes
    c('x1', '∇ln(xy)(2,3)', lista(grad(sp.log(x * y), punto=(2, 3)), [R(1, 2), R(1, 3)]), 1, r"$\nabla f(2,3)=\big(\frac12,\frac13\big)$")
    f = x * y * (5 * x - 15 + y)
    c('x2', '∇f(2,−3) y críticos', lista(grad(f, punto=(2, -3)) + [sp.Integer(int(set(criticos(f)) == {(0, 0), (3, 0), (0, 15), (1, 5)}))], [-6, -22, 1]), 1,
      r"$\nabla f(2,-3)=(-6,-22)$")
    f = sp.log(36 - x ** 2 - y ** 2)
    c('x3', '∇f(1,5) y f∘g', lista(grad(f, punto=(1, 5)) + [sp.simplify(f.subs({x: rho * sp.cos(th), y: rho * sp.sin(th)}))], [R(-1, 5), -1, sp.log(36 - rho ** 2)]), 1,
      r"=\ln(36-\rho^2)$, para")
    gf = sp.Matrix(grad(sp.log(4 - x ** 2 - y ** 2), punto=(0, R(3, 2))))
    gg = sp.Matrix(grad(sp.sqrt(x ** 2 + y ** 2 - 1), punto=(0, R(3, 2))))
    c('x4', 'gradientes y producto escalar', lista(list(gf) + list(gg) + [gf.dot(gg)], [0, R(-12, 7), 0, 3 / s5, -36 * s5 / 35]), 1, r"-\frac{36\sqrt5}{35}")
    f = x ** 2 + sp.exp(x) + 5 * y ** 2 - z ** 3 - sp.cos(z)
    c('x5', 'Hf(2,1,π)', lista(plano(hess(f, (x, y, z), (2, 1, pi))) + [sp.simplify(hess(y * sp.sin(x) - y ** 3 * sp.exp(x) + 2)[0, 1] - (sp.cos(x) - 3 * y ** 2 * sp.exp(x)))],
                               [2 + sp.E ** 2, 0, 0, 0, 10, 0, 0, 0, -6 * pi - 1, 0]), 1,
      r"\begin{pmatrix}2+e^2&0&0\\0&10&0\\0&0&-6\pi-1\end{pmatrix}")
    f = x ** 2 / (x ** 2 + y ** 2)
    g = sp.Matrix(grad(f, punto=(1, 1)))
    c('x6', 'límite 1 por y=0, G → 0, dirección', lista([sp.limit(f.subs(y, 0), x, 0), sp.limit(f.subs({x: pi, y: z}), z, sp.oo)] + list(g / g.norm()), [1, 0, s2 / 2, -s2 / 2]), 1,
      r"$\big(\frac{\sqrt2}2,-\frac{\sqrt2}2\big)$")
    f = 4 * x * y - 2 * y ** 2 - x ** 3 + 1
    c('x7', 'críticos, det Hf y valor máximo 59/27', lista([sp.Integer(int(set(criticos(f)) == {(0, 0), (R(4, 3), R(4, 3))})), hess(f).det().subs(x, 0),
                                                         hess(f).det().subs(x, R(4, 3)), f.subs({x: R(4, 3), y: R(4, 3)})], [1, -16, 16, R(59, 27)]), 1,
      r"$\det Hf=24x-16$")
    f = x ** 2 - y ** 2
    c('x8', 'x²−y²: ∇f(0,0) = 0 y cambia de signo', lista(grad(f, punto=(0, 0)) + [f.subs({x: t, y: 0}), f.subs({x: 0, y: t})], [0, 0, t ** 2, -t ** 2]), 1,
      r"Respuesta: falsa.")
    f = 5 + x ** 2 * y ** 2
    c('x9', 'críticos = ejes', lista([sp.Integer(int(all(e.subs({x: 0}) == 0 and e.subs({y: 0}) == 0 for e in grad(f)))), grad(f, punto=(1, 1))[0]], [1, 2]), 1,
      r"todos los puntos de los <b>ejes</b>")
    # ---- Práctica «Ahora hazlo tú» (respuesta final = «Resultado: …»)
    fa1 = x ** 3 * y - 4 * x * y ** 2 + 5 * y
    ga1 = x * sp.exp(-3 * y)
    ga2 = (x - y) / (x + y)
    ra2 = sp.sqrt(x ** 2 + y ** 2 + z ** 2)
    fb1 = x ** 2 + 3 * x * y
    fb2 = (x ** 3 + 2 * y ** 3) / (x ** 2 + y ** 2)
    fc1 = x * sp.exp(y * z) + y ** 2 * z
    fc2 = x ** 2 * y - 2 * x * y + y ** 2
    fd1 = x ** 2 * y + 3 * y ** 2
    fd2 = x ** 2 + 4 * y ** 2
    ye = sp.sqrt(8 - x ** 2) / 2  # rama superior de la curva de nivel x²+4y²=8 (contiene (2,1))
    fe1 = x ** 4 - 3 * x ** 2 * y + y ** 3
    fe2 = x ** 2 * y + y * sp.exp(z) - x * z ** 2
    ff1 = 3 * x ** 2 * y - y ** 3
    p_, q_ = sp.symbols('p q', real=True)
    sol_f2 = sp.solve([R(3, 5) * p_ + R(4, 5) * q_ - 2, R(4, 5) * p_ - R(3, 5) * q_ - 1], [p_, q_])
    g_f2 = sp.Matrix([sol_f2[p_], sol_f2[q_]])
    fg1 = sp.log(x ** 2 + y ** 2)
    g_g1 = sp.Matrix(grad(fg1, punto=(3, 4)))
    Tg2 = 100 * sp.exp(-x ** 2 - 2 * y ** 2 - z ** 2)
    g_g2 = sp.Matrix(grad(Tg2, (x, y, z), (1, 0, 1)))
    P = {
        'pr-a1': (lista(grad(fa1, punto=(2, 1)) + grad(ga1), [8, -3, sp.exp(-3 * y), -3 * x * sp.exp(-3 * y)]), 1,
                  r"Resultado: $\frac{\partial f}{\partial x}(2,1)=8$, $\frac{\partial f}{\partial y}(2,1)=-3$; $\frac{\partial g}{\partial x}=e^{-3y}$, $\frac{\partial g}{\partial y}=-3xe^{-3y}$"),
        'pr-a2': (lista(grad(ga2) + grad(ra2, (x, y, z), (1, 2, 2)), [2 * y / (x + y) ** 2, -2 * x / (x + y) ** 2, R(1, 3), R(2, 3), R(2, 3)]), 1,
                  r"Resultado: $\frac{\partial g}{\partial x}=\frac{2y}{(x+y)^2}$, $\frac{\partial g}{\partial y}=-\frac{2x}{(x+y)^2}$; $\nabla r(1,2,2)=\left(\frac13,\frac23,\frac23\right)$"),
        'pr-b1': (lista([dir_def(fb1, (1, -1), [1, 0]), dir_def(fb1, (1, -1), [0, 1]), sp.expand(fb1.subs({x: 1 + h, y: -1}) - fb1.subs({x: 1, y: -1}))] + grad(fb1, punto=(1, -1)),
                        [-1, 3, h ** 2 - h, -1, 3]), 1,
                  r"Resultado: $\frac{\partial f}{\partial x}(1,-1)=-1$, $\frac{\partial f}{\partial y}(1,-1)=3$"),
        'pr-b2': (lista([sp.simplify(fb2.subs({x: h, y: 0}) / h), sp.simplify(fb2.subs({x: 0, y: h}) / h),
                         sp.simplify(fb2.subs({x: rho * sp.cos(th), y: rho * sp.sin(th)}) - rho * (sp.cos(th) ** 3 + 2 * sp.sin(th) ** 3)),
                         sp.limit(fb2.subs(y, m * x), x, 0)], [1, 2, 0, 0]), 1,
                  r"Resultado: $\nabla f(0,0)=(1,2)$; $f$ es continua en $(0,0)$"),
        'pr-c1': (lista(grad(fc1, (x, y, z), (2, 0, 1)), [1, 2, 0]), 1, r"Resultado: $\nabla f(2,0,1)=(1,2,0)$"),
        'pr-c2': (sp.Integer(int(set(criticos(fc2)) == {(0, 0), (2, 0), (1, R(1, 2))})), 1,
                  r"Resultado: $(0,0)$, $(2,0)$ y $\left(1,\frac12\right)$"),
        'pr-d1': (lista([fd1.subs({x: 2, y: 1}), sp.diff(fd1, x).subs({x: 2, y: 1})], [7, 4]), 1,
                  r"Resultado: $(x,y,z)=(2,1,7)+\lambda(1,0,4)$, $\lambda\in\mathbb R$"),
        'pr-d2': (lista([fd2.subs({x: 2, y: 1})] + grad(fd2, punto=(2, 1)) + [ye.subs(x, 2), sp.diff(ye, x).subs(x, 2)], [8, 4, 8, 1, R(-1, 2)]), 1,
                  r"Resultado: $\nabla f(2,1)=(4,8)$; la tangente a la curva de nivel $x^2+4y^2=8$ en $(2,1)$ es $x+2y=4$"),
        'pr-e1': (lista(plano(hess(fe1, punto=(1, 2))), [0, -6, -6, 12]), 1,
                  r"Resultado: $Hf(1,2)=\begin{pmatrix}0&-6\\-6&12\end{pmatrix}$"),
        'pr-e2': (lista(plano(hess(fe2, (x, y, z), (1, 1, 0))) + [sp.Integer(int(hess(fe2, (x, y, z)).is_symmetric()))], [2, 2, 0, 2, 0, 1, 0, 1, -1, 1]), 1,
                  r"Resultado: $Hf(1,1,0)=\begin{pmatrix}2&2&0\\2&0&1\\0&1&-1\end{pmatrix}$"),
        'pr-f1': (lista(grad(ff1, punto=(1, 2)) + [(sp.Matrix(grad(ff1, punto=(1, 2))).T * unit(5, 12))[0], dir_def(ff1, (1, 2), list(unit(5, 12)))],
                        [12, -9, R(-48, 13), R(-48, 13)]), 1,
                  r"Resultado: $D_vf(1,2)=-\frac{48}{13}\approx-3{,}69$ (en esa dirección $f$ decrece)"),
        'pr-f2': (lista(list(g_f2) + [g_f2.dot(unit(1, 1)), g_f2.norm()], [2, 1, 3 * s2 / 2, s5]), 1,
                  r"Resultado: $\nabla f(a,b)=(2,1)$; $D_wf(a,b)=\frac{3\sqrt2}2$; derivada direccional máxima $\sqrt5$"),
        'pr-g1': (lista(list(g_g1) + list(g_g1 / g_g1.norm()) + [g_g1.norm()], [R(6, 25), R(8, 25), R(3, 5), R(4, 5), R(2, 5)]), 1,
                  r"Resultado: máximo crecimiento en la dirección $\left(\frac35,\frac45\right)$, con valor $\frac25$; mínimo $-\frac25$ en la dirección $\left(-\frac35,-\frac45\right)$"),
        'pr-g2': (lista(list(g_g2) + list(g_g2 / g_g2.norm()) + [g_g2.norm(), r(g_g2.norm(), 2), g_g2.dot(sp.Matrix([0, 1, 0]))],
                        [-200 * sp.exp(-2), 0, -200 * sp.exp(-2), -1 / s2, 0, -1 / s2, 200 * s2 * sp.exp(-2), R('38.28'), 0]), 1,
                  r"Resultado: sube más deprisa en la dirección $\left(-\frac1{\sqrt2},0,-\frac1{\sqrt2}\right)$, a razón de $200\sqrt2\,e^{-2}\approx38{,}28$; en la dirección $(0,1,0)$ la derivada direccional es $0$"),
    }
    for eid, (val, esp, txt) in P.items():
        if (EJ / f'{eid}.html').exists() or (EJ / f'{eid}.solucion.html').exists():
            c(eid, 'resultado de la práctica', val, esp, txt)
