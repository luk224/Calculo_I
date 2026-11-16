r"""Tema 3.5 (Concavidad y convexidad): signo de f'', puntos de inflexión (cambio de signo y Prop. 3.12), lectura de f' y f'',
asíntotas y estudio completo de funciones, desigualdades por convexidad, recalculados con sympy.

`comprobaciones(c)`: c(ejercicio, descripción, valor_sympy, esperado, trozo_latex)
  - valor_sympy: lo que calcula sympy;  esperado: lo que afirma la página;
  - trozo_latex: cadena que debe aparecer en `ejercicios/<ejercicio>.html` (o `.solucion.html`), comparada sin etiquetas,
    espacios, \, \; \! ni \displaystyle y con \dfrac/\tfrac = \frac.
Las comprobaciones de la práctica «Ahora hazlo tú» (pr-*) solo se activan cuando el ejercicio existe en `contenido/`.
"""
import pathlib

import sympy as sp

x = sp.symbols('x', real=True)
R = sp.Rational
pi = sp.pi
E = sp.E
EJ = pathlib.Path(__file__).resolve().parents[2] / 'contenido' / 'tema_3_5' / 'ejercicios'


def d(f, n=1):
    return sp.simplify(sp.diff(f, x, n))


def ceros(expr, dom=sp.S.Reals):
    """Ceros reales de expr en dom, ordenados."""
    return sorted(sp.solveset(sp.simplify(expr), x, dom), key=lambda z: float(z))


def _igual(p, q):
    p, q = sp.sympify(p), sp.sympify(q)
    if p == q:
        return True
    if isinstance(p, sp.Set) or isinstance(q, sp.Set) or sp.oo in (abs(p), abs(q)):
        return False
    return sp.simplify(p - q) == 0


def lista(vals, esperados):
    return sp.Integer(int(len(vals) == len(esperados) and all(_igual(p, q) for p, q in zip(vals, esperados))))


def signos(expr, pts):
    """Signos de expr en los puntos de prueba."""
    return [sp.sign(sp.N(expr.subs(x, p))) for p in pts]


def r(v, dd):
    return R(str(round(float(v), dd)))


def comprobaciones(c):
    # ---- Ejercicios del libro (E 3.30, 3.36, 3.39-3.43, 3.45-3.48)
    a, b, cc, dd = sp.symbols('a b c d')
    cub = a * x ** 3 + b * x ** 2 + cc * x + dd
    c('ej-3-30', "cero de f''=6ax+2b y f'''=6a", lista(sp.solve(sp.diff(cub, x, 2), x) + [sp.diff(cub, x, 3)], [-b / (3 * a), 6 * a]), 1, r"$x_0=-\frac b{3a}$")
    fp = (x ** 3 - 3 * x + 2) / 2  # modelo de f': máximo 2 en -1, mínimo 0 en 1
    c('ej-3-36', "modelo de f': extremos en ±1 ⇒ f''(±1)=0", lista(ceros(sp.diff(fp, x)) + [fp.subs(x, -1), fp.subs(x, 1)], [-1, 1, 2, 0]), 1,
      r"$f''(-1)=0$ y $f''(1)=0$")
    f = 3 * x ** 5 - 5 * x ** 4 - 20 * x ** 3 + 2 * x - 1
    c('ej-3-39', "f''=60x(x-2)(x+1), inflexiones y f'''", lista([sp.expand(d(f, 2) - 60 * x * (x - 2) * (x + 1))] + [f.subs(x, v) for v in (-1, 0, 2)] + [d(f, 3).subs(x, v) for v in (-1, 0, 2)],
                                                        [0, 9, -1, -141, 180, -120, 360]), 1, r"$f''(x)=60\,x\,(x-2)(x+1)$")
    h = sp.symbols('h')
    c('ej-3-40', "f'' a trozos y derivadas laterales en 4", lista([d(-x ** 2 + 4 * x, 2), d(x ** 2 - 4 * x, 2), sp.limit((h * sp.Abs(h - 4) - 0) / (h - 4), h, 4, '-'),
                                                                  sp.limit((h * sp.Abs(h - 4)) / (h - 4), h, 4, '+')], [-2, 2, -4, 4]), 1, r"$f'(4^-)=-4$, $f'(4^+)=4$")
    xp = sp.symbols('xp', positive=True)
    c('ej-3-41', "f'' de √x y cuerda en 0", lista([sp.simplify(sp.diff(sp.sqrt(xp), xp, 2) + 1 / (4 * xp ** R(3, 2))), sp.sqrt(sp.Abs(0)), (sp.sqrt(1) + sp.sqrt(1)) / 2], [0, 0, 1]), 1,
      r"$f''(x)=-\frac1{4x^{3/2}}&lt;0$")
    fp = x ** 2 * (x - 1) ** 2  # modelo de f' (≥0, baja-sube-baja-sube)
    c('ej-3-42', "modelo de f': cambios de monotonía en 0, 1/2, 1", lista(ceros(sp.diff(fp, x)) + signos(sp.diff(fp, x), [-1, R(1, 4), R(3, 4), 2]), [0, R(1, 2), 1, -1, 1, -1, 1]), 1,
      r"c) correcta")
    f = 1 / (1 - x)
    c('ej-3-43', "f''=2/(1-x)^3 y asíntota en 1", lista([sp.simplify(d(f, 2) - 2 / (1 - x) ** 3), sp.limit(f, x, 1, '-'), sp.limit(f, x, 1, '+')], [0, sp.oo, -sp.oo]), 1,
      r"$f''(x)=\frac2{(1-x)^3}$")
    c('ej-3-45', 'pendientes de cuerdas de x² en [0,1],[1,2],[2,3]', lista([(x ** 2).subs(x, k + 1) - (x ** 2).subs(x, k) for k in (0, 1, 2)], [1, 3, 5]), 1, r"$\frac{9-4}{1}=5$")
    f = x ** 2 / (x - 1)
    m = sp.limit(f / x, x, sp.oo)
    c('ej-3-46', "f'', extremos y asíntota oblicua", lista([sp.simplify(d(f, 2) - 2 / (x - 1) ** 3)] + ceros(d(f)) + [f.subs(x, 2), m, sp.limit(f - m * x, x, sp.oo), sp.limit(f - x, x, -sp.oo)],
                                                       [0, 0, 2, 4, 1, 1, 1]), 1, r"<b>$y=x+1$</b> en $\pm\infty$")
    c('ej-3-47', "c) f''(-x³)=-6x y f'' de arctg", lista([d(-x ** 3, 2), sp.simplify(d(sp.atan(x), 2) + 2 * x / (1 + x ** 2) ** 2), d(-(x - 2) ** 2)], [-6 * x, 0, -2 * (x - 2)]), 1,
      r"$f''(x)=-6x$")
    fd = -x / 2 - sp.atan(x)
    c('ej-3-48', 'asíntotas y curvatura', lista([sp.limit(-sp.atan(x), x, -sp.oo), sp.limit(fd / x, x, sp.oo), sp.limit(fd + x / 2, x, sp.oo), sp.simplify(d(fd, 2) - 2 * x / (1 + x ** 2) ** 2)],
                                                [pi / 2, R(-1, 2), -pi / 2, 0]), 1, r"$y=-\tfrac x2-\tfrac\pi2$")
    # ---- Ejemplos propios
    f = sp.log(1 + x ** 2)
    c('p1', "f'' y f'''(1)", lista([sp.simplify(d(f, 2) - 2 * (1 - x ** 2) / (1 + x ** 2) ** 2), d(f, 3).subs(x, 1), f.subs(x, 1)], [0, -1, sp.log(2)]), 1, r"$f'''(1)=-1&lt;0$")
    f = x ** 4 - 4 * x ** 3 + 6 * x ** 2 + x
    g = x ** 5 - 5 * x ** 4 + 10 * x ** 3 - 10 * x ** 2
    c('p2', "f''=12(x-1)², g''=20(x-1)³", lista([sp.expand(d(f, 2) - 12 * (x - 1) ** 2), sp.expand(d(g, 2) - 20 * (x - 1) ** 3), d(f, 4).subs(x, 1), d(g, 5), f.subs(x, 1), g.subs(x, 1)],
                                                 [0, 0, 24, 120, 4, -4]), 1, r"$g''(x)=20x^3-60x^2+60x-20=20(x-1)^3$")
    c('p3', 'sen concavo en [0,π/2] y ejemplo numérico', lista([d(sp.sin(x), 2) + sp.sin(x), sp.sin(pi / 6), r((sp.sqrt(3) + sp.sqrt(11)) / 2, 3), r(sp.sqrt(7), 3)],
                                                                [0, R(1, 2), R('2.524'), R('2.646')]), 1, r"$\operatorname{sen}x\ge\frac{2x}\pi$")
    f = x ** 3 / (x ** 2 - 1)
    c('p4', "f', f'', extremos y f'''(0)", lista([sp.simplify(d(f) - x ** 2 * (x ** 2 - 3) / (x ** 2 - 1) ** 2), sp.simplify(d(f, 2) - 2 * x * (x ** 2 + 3) / (x ** 2 - 1) ** 3),
                                                 sp.simplify(f.subs(x, sp.sqrt(3))), d(f, 3).subs(x, 0), sp.limit(f - x, x, sp.oo)], [0, 0, 3 * sp.sqrt(3) / 2, -6, 0]), 1,
      r"$f'''(0)=-6&lt;0$")
    # ---- Exámenes
    c('x1', "modelo f''=x²-4: inflexiones ±2", lista(ceros(x ** 2 - 4) + signos(x ** 2 - 4, [-3, 0, 3]), [-2, 2, 1, -1, 1]), 1, r"$x=-2$ y $x=2$")
    c('x2', "modelo f''=x(x²-1): inflexiones -1, 0, 1", lista(ceros(x * (x ** 2 - 1)) + signos(x * (x ** 2 - 1), [R(-3, 2), R(-1, 2), R(1, 2), R(3, 2)]), [-1, 0, 1, -1, 1, -1, 1]), 1,
      r"inflexiones en $x=-1,0,1$")
    c('x3', "modelo f''=x(x-1)(x-2): signos −,+,−,+", lista(signos(x * (x - 1) * (x - 2), [-1, R(1, 2), R(3, 2), 3]), [-1, 1, -1, 1]), 1, r"$f''\le0$ en $[a,x_0]$ y en $[x_1,x_2]$")
    f = x ** 4 - 2 * x
    c('x4', "f''=12x² y f⁽⁴⁾(0)=24", lista([d(f, 2), d(f, 3).subs(x, 0), d(f, 4)], [12 * x ** 2, 0, 24]), 1, r"$f''(x)=12x^2\ge0$")
    f = x * sp.exp(x)
    c('x5', "f''=(x+2)eˣ e inflexión", lista([sp.simplify(d(f, 2) - (x + 2) * sp.exp(x)), f.subs(x, -2), r(f.subs(x, -2), 3)], [0, -2 * sp.exp(-2), R('-0.271')]), 1,
      r"$f''(x)=e^x+(1+x)e^x=(x+2)e^x$")
    f = x ** 2 / (x + 1)
    c('x6', "f''=2/(x+1)³", lista([sp.simplify(d(f, 2) - 2 / (x + 1) ** 3), sp.simplify(d(f) - x * (x + 2) / (x + 1) ** 2)], [0, 0]), 1, r"=\frac2{(x+1)^3}")
    f = 1 / (x ** 2 + 4)
    it = [sp.Integer(0)]
    for _ in range(3):
        it.append(f.subs(x, it[-1]))
    c('x7', "f'', inflexiones e iteraciones", lista([sp.simplify(d(f, 2) - (6 * x ** 2 - 8) / (x ** 2 + 4) ** 3)] + ceros(6 * x ** 2 - 8) + [f.subs(x, 2 / sp.sqrt(3))] + it[1:],
                                                    [0, -2 / sp.sqrt(3), 2 / sp.sqrt(3), R(3, 16), R(1, 4), R(16, 65), R(4225, 17156)]), 1,
      r"=\frac{6x^2-8}{(x^2+4)^3}")
    f = (3 * x - 1) * sp.exp(x)
    c('x8', "derivadas, extremo, inflexión y Taylor en -1", lista([sp.simplify(d(f, k) - (3 * x - 1 + 3 * k) * sp.exp(x)) for k in (1, 2, 3)]
                                                                 + [f.subs(x, R(-2, 3)), d(f, 3).subs(x, R(-5, 3))] + [d(f, k).subs(x, -1) for k in range(4)],
                                                                 [0, 0, 0, -3 * sp.exp(R(-2, 3)), 3 * sp.exp(R(-5, 3)), -4 / E, -1 / E, 2 / E, 5 / E]), 1,
      r"$f'''(-\tfrac53)=3e^{-5/3}\neq0$")
    f2, f3 = sp.exp(x ** 2), sp.exp(x ** 3)
    c('x9', "f'' para k=2 y k=3 e inflexiones", lista([sp.simplify(d(f2, 2) - (4 * x ** 2 + 2) * f2), sp.simplify(d(f3, 2) - 3 * x * (3 * x ** 3 + 2) * f3)] + ceros(3 * x * (3 * x ** 3 + 2))
                                                     + [r(-sp.cbrt(R(2, 3)), 3)], [0, 0, -sp.cbrt(R(2, 3)), 0, R('-0.874')]), 1,
      r"$f''=(6x+9x^4)e^{x^3}=3x(3x^3+2)e^{x^3}$")
    fd = x / 2 + sp.atan(x)
    c('x10', 'curvatura y asíntotas', lista([sp.simplify(d(sp.atan(x), 2) + 2 * x / (1 + x ** 2) ** 2), sp.limit(sp.atan(x), x, -sp.oo), sp.limit(fd / x, x, sp.oo), sp.limit(fd - x / 2, x, sp.oo)],
                                            [0, -pi / 2, R(1, 2), pi / 2]), 1, r"$y=\tfrac x2+\tfrac\pi2$")
    # ---- Práctica «Ahora hazlo tú» (respuesta final = «Resultado: …»)
    xp = sp.symbols('xp', positive=True)
    k = sp.symbols('k', real=True)
    fa1 = x ** 4 - 6 * x ** 2 + 5
    fa2 = xp ** 2 * sp.log(xp)
    fb2 = sp.exp(x) + sp.exp(-x) - x ** 2
    fc1 = (x - 1) ** 2 * (x + 2)   # f'
    fc2 = x * sp.exp(-x)           # f'
    fd1 = (2 * x ** 2 + 1) / (x + 2)
    fd2 = sp.sqrt(x ** 2 + 2 * x)
    fe1 = (x ** 2 - 1) / x ** 2
    fe2 = x ** 2 * sp.exp(-x)
    gf2 = x - 1 - sp.log(x)
    aa, bb = sp.symbols('a b')
    Fg1 = aa * x ** 3 + bb * x ** 2
    sg1 = sp.solve([sp.diff(Fg1, x, 2).subs(x, 1), Fg1.subs(x, 1) - 2], [aa, bb])
    fg2 = sp.diff(x ** 4 + k * x ** 3 + 6 * x ** 2, x, 2)
    P = {
        'pr-a1': (lista([sp.factor(d(fa1, 2)) - 12 * (x - 1) * (x + 1)] + ceros(d(fa1, 2)) + [fa1.subs(x, -1), fa1.subs(x, 1), d(fa1, 3).subs(x, -1), d(fa1, 3).subs(x, 1)],
                        [0, -1, 1, 0, 0, -24, 24]), 1,
                  r"Resultado: convexa en $(-\infty,-1]$ y en $[1,\infty)$; cóncava en $[-1,1]$; inflexiones $(-1,0)$ y $(1,0)$"),
        'pr-a2': (lista([sp.simplify(sp.diff(fa2, xp, 2) - (2 * sp.log(xp) + 3))] + list(sp.solveset(2 * sp.log(xp) + 3, xp, sp.Interval.open(0, sp.oo)))
                        + [sp.simplify(fa2.subs(xp, sp.exp(R(-3, 2)))), r(sp.exp(R(-3, 2)), 3)], [0, sp.exp(R(-3, 2)), -R(3, 2) * sp.exp(-3), R('0.223')]), 1,
                  r"Resultado: cóncava en $(0,e^{-3/2}]$, convexa en $[e^{-3/2},\infty)$; inflexión en $x=e^{-3/2}\approx0{,}223$"),
        'pr-b1': (lista([sp.diff(xp ** R(1, 3), xp, 2).subs(xp, 1), sp.diff(-(xp ** R(1, 3)), xp, 2).subs(xp, 1), sp.limit(xp ** R(1, 3) / xp, xp, 0, '+')],
                        [R(-2, 9), R(2, 9), sp.oo]), 1,  # x<0: f(x)=-(-x)^{1/3}, luego f''(x)=-g''(-x) con g(u)=u^{1/3}: f''(-1)=-g''(1)
                  r"Resultado: convexa en $(-\infty,0]$, cóncava en $[0,\infty)$; inflexión en $(0,0)$ aunque $f''(0)$ no existe"),
        'pr-b2': (lista([d(fb2, n).subs(x, 0) for n in (2, 3, 4)] + [sp.simplify(d(fb2, 2) - (sp.exp(x / 2) - sp.exp(-x / 2)) ** 2)], [0, 0, 2, 0]), 1,
                  r"Resultado: convexa en $\mathbb R$; no hay inflexión en $x=0$ aunque $f''(0)=0$"),
        'pr-c1': (lista([sp.expand(sp.diff(fc1, x) - 3 * (x - 1) * (x + 1))] + ceros(fc1) + signos(fc1, [-3, -1, 2]), [0, -2, 1, -1, 1, 1]), 1,
                  r"Resultado: cóncava en $[-1,1]$, convexa en $(-\infty,-1]$ y en $[1,\infty)$; inflexiones en $x=\pm1$; mínimo relativo en $x=-2$"),
        'pr-c2': (lista([sp.simplify(sp.diff(fc2, x) - (1 - x) * sp.exp(-x))] + ceros(sp.diff(fc2, x)) + ceros(fc2) + signos(fc2, [-1, 1]), [0, 1, 0, -1, 1]), 1,
                  r"Resultado: convexa en $(-\infty,1]$, cóncava en $[1,\infty)$; inflexión en $x=1$; mínimo relativo en $x=0$"),
        'pr-d1': (lista([sp.limit(fd1, x, -2, '-'), sp.limit(fd1, x, -2, '+'), sp.limit(fd1 / x, x, sp.oo), sp.limit(fd1 - 2 * x, x, sp.oo), sp.limit(fd1 / x, x, -sp.oo),
                         sp.limit(fd1 - 2 * x, x, -sp.oo), sp.simplify(fd1 - (2 * x - 4) - 9 / (x + 2))], [-sp.oo, sp.oo, 2, -4, 2, -4, 0]), 1,
                  r"Resultado: asíntota vertical $x=-2$ y oblicua $y=2x-4$ (en $+\infty$ y en $-\infty$)"),
        'pr-d2': (lista([sp.limit(fd2 / x, x, sp.oo), sp.limit(fd2 - x, x, sp.oo), sp.limit(fd2 / x, x, -sp.oo), sp.limit(fd2 + x, x, -sp.oo), sp.limit(fd2, x, sp.oo)],
                        [1, 1, -1, -1, sp.oo]), 1,
                  r"Resultado: $y=x+1$ en $+\infty$ e $y=-x-1$ en $-\infty$; sin asíntotas verticales ni horizontales"),
        'pr-e1': (lista([sp.simplify(d(fe1) - 2 / x ** 3), sp.simplify(d(fe1, 2) + 6 / x ** 4), sp.limit(fe1, x, 0), sp.limit(fe1, x, sp.oo), sp.limit(fe1, x, -sp.oo)] + ceros(fe1),
                        [0, 0, -sp.oo, 1, 1, -1, 1]), 1,
                  r"Resultado: asíntotas $x=0$ e $y=1$; decreciente en $(-\infty,0)$, creciente en $(0,\infty)$; sin extremos; cóncava en $(-\infty,0)$ y en $(0,\infty)$; sin inflexiones"),
        'pr-e2': (lista(ceros(d(fe2)) + [fe2.subs(x, 2)] + ceros(d(fe2, 2)) + [sp.limit(fe2, x, sp.oo), sp.limit(fe2 / x, x, -sp.oo), r(fe2.subs(x, 2), 3)],
                        [0, 2, 4 * sp.exp(-2), 2 - sp.sqrt(2), 2 + sp.sqrt(2), 0, -sp.oo, R('0.541')]), 1,
                  r"Resultado: mínimo $(0,0)$, máximo relativo $(2,4e^{-2})$; inflexiones en $x=2\pm\sqrt2$; asíntota $y=0$ en $+\infty$"),
        'pr-f1': (lista([sp.diff(sp.log(xp), xp, 2) + 1 / xp ** 2, sp.sqrt(2 * 8), R(2 + 8, 2)], [0, 4, 5]), 1,
                  r"Resultado: $\sqrt{ab}\le\frac{a+b}2$ para $a,b>0$"),
        'pr-f2': (lista(ceros(d(gf2), sp.Interval.open(0, sp.oo)) + [d(gf2, 2).subs(x, 1), gf2.subs(x, 1), sp.Integer(int(bool(sp.log(R(11, 10)) < R(1, 10))))], [1, 1, 0, 1]), 1,
                  r"Resultado: $\ln x\le x-1$ para todo $x>0$, con igualdad solo en $x=1$; por ejemplo, $\ln1{,}1\le0{,}1$"),
        'pr-g1': (lista([sg1[aa], sg1[bb], sp.diff(Fg1.subs(sg1), x, 3)] + signos(sp.diff(Fg1.subs(sg1), x, 2), [0, 2]), [-1, 3, -6, 1, -1]), 1,
                  r"Resultado: $a=-1$, $b=3$; $f(x)=-x^3+3x^2$ pasa de convexa a cóncava en $(1,2)$"),
        'pr-g2': (lista([sp.expand(sp.discriminant(fg2, x))] + sorted(sp.solve(sp.discriminant(fg2, x), k)) + [sp.factor(fg2.subs(k, 4)), fg2.subs(k, 5).subs(x, -1)],
                        [36 * k ** 2 - 576, -4, 4, 12 * (x + 1) ** 2, -6]), 1,
                  r"Resultado: $f$ es convexa en $\mathbb R$ si y solo si $-4\le k\le4$"),
    }
    for eid, (val, esp, txt) in P.items():
        if (EJ / f'{eid}.html').exists() or (EJ / f'{eid}.solucion.html').exists():
            c(eid, 'resultado de la práctica', val, esp, txt)
