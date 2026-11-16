r"""Tema 5.2 (Regla de la cadena. Teorema del valor medio): reglas de la diferencial, regla de la cadena
(caminos y producto de matrices) y teorema del valor medio, recalculados con sympy.

`comprobaciones(c)`: c(ejercicio, descripción, valor_sympy, esperado, trozo_latex)
  - valor_sympy: lo que calcula sympy;  esperado: lo que afirma la página;
  - trozo_latex: cadena que debe aparecer en `ejercicios/<ejercicio>.html` (o `.solucion.html`), comparada sin etiquetas,
    espacios, \, \; \! ni \displaystyle y con \dfrac/\tfrac = \frac.
Las comprobaciones de la práctica «Ahora hazlo tú» (pr-*) solo se activan cuando el ejercicio existe en `contenido/`.
Cadena (U pp.196-200): ∇(f(g,h))(ā) = ∇f(g(ā),h(ā)) · [∇g(ā); ∇h(ā)].  TVM (U p.202): f(ā) − f(b̄) = ∇f(c̄)·(ā − b̄).
"""
import pathlib

import sympy as sp

R = sp.Rational
pi = sp.pi
E_ = sp.E
x, y, z, t, u, v = sp.symbols('x y z t u v', real=True)
EJ = pathlib.Path(__file__).resolve().parents[2] / 'contenido' / 'tema_5_2' / 'ejercicios'


def _igual(p, q):
    p, q = sp.sympify(p), sp.sympify(q)
    if p == q:
        return True
    return sp.simplify(p - q) == 0


def lista(vals, esperados):
    return sp.Integer(int(len(vals) == len(esperados) and all(_igual(p, q) for p, q in zip(vals, esperados))))


def r(val, d):
    return R(str(round(float(val), d)))


def grad(f, punto, vs=(x, y)):
    return [sp.simplify(sp.diff(f, s).subs(dict(zip(vs, punto)))) for s in vs]


def compon(f, sust):
    """f con las variables sustituidas a la vez (composición)."""
    return f.subs(sust, simultaneous=True)


def cadena(f, vs_f, inter, vs_fin, punto):
    """∇f(punto imagen) · matriz de las intermedias (fila 1×n)."""
    pf = dict(zip(vs_fin, punto))
    img = [g.subs(pf) for g in inter]
    gf = sp.Matrix([[sp.diff(f, s) for s in vs_f]]).subs(dict(zip(vs_f, img)))
    J = sp.Matrix(inter).jacobian(list(vs_fin)).subs(pf)
    return [sp.simplify(e) for e in gf * J]


def comprobaciones(c):
    # ---- Ejercicios del libro (E 5.13-5.22)
    c('ej-5-13', '∇(xy)(2,3) = (3,2) = g∇f + f∇g', lista([3 * 1 + 2 * 0, 3 * 0 + 2 * 1] + grad(x * y, (2, 3)), [3, 2, 3, 2]), 1, r"Respuesta: c).")
    gs = [1 + 2, 9 + 5]
    gp = [2 * 1 + 9 * 2, 2 * 9 + 9 * 5]
    gq = [R(2 * 1 - 9 * 2, 4), R(2 * 9 - 9 * 5, 4)]
    c('ej-5-14', 'gradientes (3,14), (20,63), (−4,−27/4)', lista(gs + gp + gq, [3, 14, 20, 63, -4, R(-27, 4)]), 1, r"z=\tfrac92-4(x-1)-\tfrac{27}4(y-2)")
    f15 = x * (1 - y ** 2) - y
    F15 = compon(f15, {x: sp.exp(2 * t), y: 1 / t})
    c('ej-5-15', "F'(t) por sustitución = por la cadena", lista([sp.simplify(sp.diff(F15, t) - (2 * sp.exp(2 * t) * (1 - 1 / t ** 2 + 1 / t ** 3) + 1 / t ** 2))], [0]), 1,
      r"2e^{2t}\left(1-\frac1{t^2}+\frac1{t^3}\right)+\frac1{t^2}")
    F16 = x ** 2 + sp.cos(sp.exp(-x))
    c('ej-5-16', 'd/dx f(x,e^{−x}) = 2x + e^{−x} sen(e^{−x})', sp.simplify(sp.diff(F16, x) - (2 * x + sp.exp(-x) * sp.sin(sp.exp(-x)))), 0,
      r"=2x+e^{-x}\operatorname{sen}(e^{-x})")
    f = sp.Function('f')
    z17 = f(u - 2 * v, 2 * v - u)
    c('ej-5-17', '2 z_u + z_v = 0 con f genérica', sp.simplify(2 * sp.diff(z17, u) + sp.diff(z17, v)), 0, r"2(f_x-f_y)+(-2f_x+2f_y)=0")
    c('ej-5-18', 'gradiente (1,0)', lista(cadena(x - y ** 2, (x, y), [u + u * v, sp.tan(u)], (u, v), (0, 0)), [1, 0]), 1, r"Respuesta: $(1,0)$.")
    c('ej-5-19', 'gradiente (cos 1 + 2e², 3)', lista(cadena(3 * x + y + z ** 2, (x, y, z), [u * v, sp.sin(u) + 3, sp.exp(u)], (u, v), (1, 0)), [sp.cos(1) + 2 * E_ ** 2, 3]), 1,
      r"Respuesta: $(\cos1+2e^2,\,3)$.")
    c('ej-5-20', 'TVM con gradiente nulo (demostración, sin cálculo)', sp.Integer(1), 1, r"$f(\bar a)=f(\bar b)$ para todo par de puntos de $A$")
    c('ej-5-21', '∇(−x−y) = (−1,−1)', lista(grad(-x - y, (0, 0)), [-1, -1]), 1, r"$\nabla f=(-1,-1)$")
    f22 = x ** 2 - y ** 3
    c('ej-5-22', 'f(−2,1)=3, f(−1,2)=−7, f(1/2,1/2)=1/8, f(2,1)=3', lista([f22.subs({x: -2, y: 1}), f22.subs({x: -1, y: 2}), f22.subs({x: R(1, 2), y: R(1, 2)}), f22.subs({x: 2, y: 1})], [3, -7, R(1, 8), 3]), 1,
      r"$f(-2,1)=3$ y $f(-1,2)=-7$")
    # ---- Ejemplos propios
    rh, th = sp.symbols('rho theta', positive=True)
    zp1 = compon(x ** 2 + x * y, {x: rh * sp.cos(th), y: rh * sp.sin(th)})
    c('p1', 'z_ρ = 4, z_θ = −4 en (2, π/4)', lista([sp.simplify(sp.diff(zp1, s).subs({rh: 2, th: pi / 4})) for s in (rh, th)], [4, -4]), 1, r"=3+1=4")
    c('p2', 'matriz [[30,21],[3,2]]', lista(cadena(x ** 2 * y, (x, y), [u + v, u * v], (u, v), (1, 2)) + cadena(x + y, (x, y), [u + v, u * v], (u, v), (1, 2)), [30, 21, 3, 2]), 1,
      r"=\begin{pmatrix}30&21\\3&2\end{pmatrix}")
    c('p3', 'z_ρ² + z_θ²/ρ² = f_x² + f_y² (con f = x²+xy: 20)', lista([sp.simplify((sp.diff(zp1, rh) ** 2 + sp.diff(zp1, th) ** 2 / rh ** 2).subs({rh: 2, th: pi / 4}))], [20]), 1, r"=20")
    c('p4', '|f(1,1;0,9) − f(1,1)| ≈ 0,0993 ≤ 0,2', lista([r(abs(sp.sin(R(11, 10)) * sp.cos(R(9, 10)) - sp.sin(1) * sp.cos(1)), 4)], [R('0.0993')]), 1, r"\approx0{,}0993")
    # ---- Exámenes
    c('x1', '∇(x²e^{x+y})(1,−1) = (3,1)', lista(grad(x ** 2 * sp.exp(x + y), (1, -1)), [3, 1]), 1, r"\nabla f(1,-1)=(2+1,\,1)=(3,1)")
    c('x2', '∇f(1,0) = (−1,0)', lista(grad((x + y ** 3) * sp.cos(pi * x ** 2), (1, 0)), [-1, 0]), 1, r"(-1,0)")
    f3 = y * sp.tan(sp.exp(x)) + sp.cos(x + y) ** 2
    c('x3', 'gradiente general', lista([sp.simplify(sp.diff(f3, x) - (y * sp.exp(x) / sp.cos(sp.exp(x)) ** 2 - 2 * sp.cos(x + y) * sp.sin(x + y))),
                                         sp.simplify(sp.diff(f3, y) - (sp.tan(sp.exp(x)) - 2 * sp.cos(x + y) * sp.sin(x + y)))], [0, 0]), 1,
      r"\operatorname{tg}e^x-2\cos(x+y)\operatorname{sen}(x+y)")
    g4 = grad(x ** 2 * y, (1, 1))
    f4 = grad(sp.log(x ** 2 * y), (1, 1))
    c('x4', '∇g = ∇f = (2,1), cos = 1', lista(g4 + f4 + [sp.Matrix(g4).dot(sp.Matrix(f4)) / (sp.Matrix(g4).norm() * sp.Matrix(f4).norm())], [2, 1, 2, 1, 1]), 1, r"=\dfrac55=1")
    f5 = sp.log(36 - x ** 2 - y ** 2)
    c('x5', '∇f(1,5) = (−1/5,−1); f∘g = ln(36 − ρ²)', lista(grad(f5, (1, 5)) + [sp.simplify(compon(f5, {x: rh * sp.cos(th), y: rh * sp.sin(th)}) - sp.log(36 - rh ** 2))], [R(-1, 5), -1, 0]), 1,
      r"\left(-\frac15,-1\right)")
    f6 = x ** 3 + y ** 3 + x + y
    c('x6', 'ejemplo f(−1,−2) = −12 < f(0,0) = 0', lista([f6.subs({x: -1, y: -2}), f6.subs({x: 0, y: 0})], [-12, 0]), 1, r"$f(-1,-2)=-12$")
    c('x7', "g'(0) = 2 f(0) f'(0) cos 0 = −4", sp.Integer(2 * 1 * (-2) * 1), -4, r"g'(0)=2\cdot1\cdot(-2)\cdot1=-4")
    gp2 = sp.symbols('gp2')
    c('x8', "f'(x) = g(2x) + 2x g'(2x): 2 = −1 + 2g'(2)", sp.solve(sp.Eq(2, -1 + 2 * gp2), gp2)[0], R(3, 2), r"g'(2)=\frac32")
    c('x9', "g'(π/2) = sen(f(0)) f'(0) sen(π/2) = 0", sp.sin(pi) * 2 * sp.sin(pi / 2), 0, r"=2\operatorname{sen}\pi=0")
    c('x10', "g'(√2) = cos(π)·3·10√2 = −30√2", sp.cos(pi) * 3 * 10 * sp.sqrt(2), -30 * sp.sqrt(2), r"=-30\sqrt2")
    c('x11', 'enunciado de teoría (sin cálculo)', sp.Integer(1), 1, r"continua en el cerrado y derivable en el abierto")
    # ---- Práctica «Ahora hazlo tú» (respuesta final = «Resultado: …»)
    Fa1 = (x ** 2 + y) * sp.exp(x * y)
    # a2: datos f(1,1)=2, g(1,1)=−1, ∇f=(3,−1), ∇g=(1,2); también con funciones concretas que los cumplen
    fa, ga = 2 + 3 * (x - 1) - (y - 1), -1 + (x - 1) + 2 * (y - 1)
    ha = fa ** 2 / ga
    gha = grad(ha, (1, 1))
    Fb1 = compon(x ** 2 * y - y ** 3, {x: sp.cos(t), y: sp.sin(t)})
    Xb, Yb = 10 + 2 * t, 6 - 3 * t
    Dp = sp.simplify(sp.diff(sp.sqrt(Xb ** 2 + Yb ** 2), t).subs(t, 0))
    Zc1 = compon(sp.exp(x) * sp.sin(y), {x: u * v, y: u + v})
    wc2 = f(x - y, y - z, z - x)
    Fd1 = compon(x ** 2 * y + y, {x: u - v, y: u * v ** 2})
    Jd2 = sp.Matrix([compon(x * y + z, {x: u + v, y: u - v, z: u * v}), compon(x - z ** 2, {x: u + v, y: u - v, z: u * v})]).jacobian([u, v]).subs({u: 1, v: 1})
    Jd2p = (sp.Matrix([x * y + z, x - z ** 2]).jacobian([x, y, z]).subs({x: 2, y: 0, z: 1})
            * sp.Matrix([u + v, u - v, u * v]).jacobian([u, v]).subs({u: 1, v: 1}))
    s = sp.symbols('s')
    se1 = sp.solve(sp.Eq(2, sp.Matrix([s, 2 * s]).dot(sp.Matrix([2, 1]))), s)[0]
    fe2x = sp.diff(sp.log(1 + x ** 2 + y ** 2), x)
    fx_l = sp.lambdify((x, y), fe2x, 'math')
    cota_e2 = all(abs(fx_l(p, q)) <= 1 + 1e-12 for p in [i / 4 - 5 for i in range(41)] for q in [i / 4 - 5 for i in range(41)])
    rr = sp.symbols('rr', nonnegative=True)
    ff1 = x ** 3 + 3 * x + sp.atan(y)
    df1 = ff1.subs({x: 1, y: 2}) - ff1.subs({x: 0, y: 1})
    xy = lambda p, q: (x * y).subs({x: p, y: q})  # noqa: E731
    gg1 = x ** 2 * y + 3
    P = {
        'pr-a1': (lista(grad(Fa1, (1, 0)), [2, 2]), 1, r"Resultado: $\nabla(fg)(1,0)=(2,2)$"),
        'pr-a2': (lista([ha.subs({x: 1, y: 1})] + grad(fa, (1, 1)) + grad(ga, (1, 1)) + gha + [sp.expand(-4 + gha[0] * (x - 1) + gha[1] * (y - 1))],
                        [-4, 3, -1, 1, 2, -16, -4, -16 * x - 4 * y + 16]), 1,
                  r"Resultado: $\nabla h(1,1)=(-16,-4)$; plano tangente $z=-16x-4y+16$"),
        'pr-b1': (sp.simplify(sp.diff(Fb1, t).subs(t, pi / 4)), -sp.sqrt(2), r"Resultado: $F'\!\left(\frac\pi4\right)=-\sqrt2$"),
        'pr-b2': (lista([sp.diff(Xb * Yb, t).subs(t, 0), Dp, r(Dp, 3), sp.sqrt(Xb ** 2 + Yb ** 2).subs(t, 0)], [-18, 1 / sp.sqrt(34), R('0.171'), 2 * sp.sqrt(34)]), 1,
                  r"Resultado: $\frac{dA}{dt}=-18$ cm²/s (disminuye); $\frac{dD}{dt}=\frac1{\sqrt{34}}\approx0{,}171$ cm/s (aumenta)"),
        'pr-c1': (lista([sp.simplify(sp.diff(Zc1, q).subs({u: 1, v: 0})) for q in (u, v)] + cadena(sp.exp(x) * sp.sin(y), (x, y), [u * v, u + v], (u, v), (1, 0)),
                        [sp.cos(1), sp.sin(1) + sp.cos(1), sp.cos(1), sp.sin(1) + sp.cos(1)]), 1,
                  r"Resultado: $\frac{\partial z}{\partial u}(1,0)=\cos1$; $\frac{\partial z}{\partial v}(1,0)=\operatorname{sen}1+\cos1$"),
        'pr-c2': (lista([sp.simplify(sum(sp.diff(wc2, q) for q in (x, y, z))), sp.expand(sum(sp.diff((x - y) * (y - z), q) for q in (x, y, z)))], [0, 0]), 1,
                  r"Resultado: $w_x=f_r-f_q$, $w_y=f_s-f_r$, $w_z=f_q-f_s$; la suma es $0$"),
        'pr-d1': (lista([sp.diff(Fd1, q).subs({u: 2, v: 1}) for q in (u, v)] + cadena(x ** 2 * y + y, (x, y), [u - v, u * v ** 2], (u, v), (2, 1)), [6, 4, 6, 4]), 1,
                  r"Resultado: $\nabla\big(f(g,h)\big)(2,1)=(6,4)$"),
        'pr-d2': (lista(list(Jd2) + list(Jd2p), [3, -1, -1, -1, 3, -1, -1, -1]), 1,
                  r"Resultado: $\begin{pmatrix}3&-1\\-1&-1\end{pmatrix}$"),
        'pr-e1': (lista([se1, 2 * se1, se1, xy(2, 1) - xy(0, 0)], [R(1, 2), 1, R(1, 2), 2]), 1, r"Resultado: $(c,d)=\left(1,\frac12\right)$"),
        'pr-e2': (lista([sp.maximum(2 * rr / (1 + rr ** 2), rr, sp.Interval(0, sp.oo)), sp.Integer(int(cota_e2)), r(sp.log(R(3, 2)), 3)], [1, 1, R('0.405')]), 1,
                  r"Resultado: $|f_x|,|f_y|\le1$; $|f(\bar a)-f(\bar b)|\le|a_1-b_1|+|a_2-b_2|$; cota $1$ frente al valor $\ln\frac32\approx0{,}405$"),
        'pr-f1': (lista([sp.Integer(1 if bool(df1 > 0) else 0), r(df1, 2)], [1, R('4.32')]), 1,
                  r"Resultado: $f(1,2)>f(0,1)$ (las dos parciales son positivas en $\mathbb R^2$)"),
        'pr-f2': (lista([xy(1, 1), xy(2, 3), xy(-2, -2), xy(-1, -1), xy(-2, 1), xy(-1, 3), xy(-1, R(11, 10))], [1, 6, 4, 1, -2, -3, R(-11, 10)]), 1,
                  r"Resultado: a) crece; b) decrece; c) no hay respuesta única (según el vector, sube o baja)"),
        'pr-g1': (lista([sp.diff(gg1, x) - 2 * x * y, sp.diff(gg1, y) - x ** 2, gg1.subs({x: 1, y: 1}), gg1.subs({x: 2, y: -1})], [0, 0, 4, -1]), 1,
                  r"Resultado: $g(x,y)=x^2y+3$ y $g(2,-1)=-1$"),
        'pr-g2': (lista([sp.Integer(1) - sp.Integer(-1), sp.Matrix([0, 0]).dot(sp.Matrix([2, 0]))], [2, 0]), 1,
                  r"Resultado: $\nabla f=(0,0)$ en $D$ pero $f$ no es constante ($f(1,0)=1$, $f(-1,0)=-1$); no contradice E 5.20 porque $D$ no es convexo"),
    }
    for eid, (val, esp, txt) in P.items():
        if (EJ / f'{eid}.html').exists() or (EJ / f'{eid}.solucion.html').exists():
            c(eid, 'resultado de la práctica', val, esp, txt)
