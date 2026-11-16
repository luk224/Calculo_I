r"""Tema 3.3 (Interpolación polinómica): tablas de diferencias divididas, polinomios de Newton, valores estimados,
integrales por trapecio/Simpson y cotas de error de Lagrange recalculados con sympy.

`comprobaciones(c)`: c(ejercicio, descripción, valor_sympy, esperado, trozo_latex)
  - valor_sympy: lo que calcula sympy;  esperado: lo que afirma la página;
  - trozo_latex: cadena que debe aparecer en `ejercicios/<ejercicio>.html` (o `.solucion.html`), comparada sin etiquetas,
    espacios, \, \; \! ni \displaystyle y con \dfrac/\tfrac = \frac.
Las comprobaciones de la práctica «Ahora hazlo tú» (pr-*) solo se activan cuando el ejercicio existe en `contenido/`.
"""
import pathlib

import sympy as sp

x = sp.symbols('x')
R = sp.Rational
pi = sp.pi
EJ = pathlib.Path(__file__).resolve().parents[2] / 'contenido' / 'tema_3_3' / 'ejercicios'


def I(xs, ys):
    """Polinomio interpolador desarrollado."""
    return sp.expand(sp.interpolate(list(zip(xs, ys)), x))


def diag(xs, ys):
    """Diagonal superior de la tabla de diferencias divididas (en el orden dado de los nodos)."""
    col, d = list(ys), [sp.sympify(ys[0])]
    for m in range(1, len(xs)):
        col = [sp.simplify((col[k + 1] - col[k]) / (xs[k + m] - xs[k])) for k in range(len(col) - 1)]
        d.append(col[0])
    return d


def lista(vals, esperados):
    return sp.Integer(int(len(vals) == len(esperados) and all(sp.simplify(sp.sympify(a) - b) == 0 for a, b in zip(vals, esperados))))


def iguales(a, b):
    return sp.Integer(1) if sp.simplify(sp.expand(a - b)) == 0 else sp.Integer(0)


def r(v, d):
    return R(str(round(float(v), d)))


def comprobaciones(c):
    # ---- Ejercicios del libro (E 3.21-3.28)
    c('ej-3-21', 'interpolador de (a,2a), a=1..9', I(list(range(1, 10)), [2 * a for a in range(1, 10)]), 2 * x, r"p_8(x)=2x")
    c('ej-3-22', 'interpolador de x² en ±1', I([-1, 1], [1, 1]), 1, r"la constante $1$, no $x^2$")
    c('ej-3-23', 'p3 por (1,1),(3,2),(4,-1),(5,0)', iguales(I([1, 3, 4, 5], [1, 2, -1, 0]), R(19, 24) * x ** 3 - R(15, 2) * x ** 2 + R(485, 24) * x - R(25, 2)), 1,
      r"=\frac{19}{24}x^3-\frac{15}2x^2+\frac{485}{24}x-\frac{25}2")
    c('ej-3-24', 'p3 por (1,3),(5,11),(8,38),(10,56)', iguales(I([1, 5, 8, 10], [3, 11, 38, 56]), -x ** 3 / 9 + R(23, 9) * x ** 2 - R(89, 9) * x + R(94, 9)), 1,
      r"p_3(x)=-\tfrac19x^3+\tfrac{23}9x^2-\tfrac{89}9x+\tfrac{94}9")
    c('ej-3-25', 'recta y cúbica en t=3', I([0, 4], [210, 140]).subs(x, 3) + I([0, 1, 2, 4], [210, 180, 160, 140]).subs(x, 3), R(315, 2) + R(295, 2),
      r"=210-90+30-\frac52=147{,}5")
    c('ej-3-26', 'interpolador de cos2x en 0,π,2π', I([0, pi, 2 * pi], [sp.cos(0), sp.cos(2 * pi), sp.cos(4 * pi)]), 1, r"p_2(x)=1$ no es el polinomio nulo")
    pob = [43197684, 44108530, 44708964, 45200737, 46157822]
    c('ej-3-27', 'p4(2007,5) redondeado', sp.floor(I(list(range(2004, 2009)), pob).subs(x, R(4015, 2))), 45570702, r"45\,570\,702{,}27")
    c('ej-3-28', 'diferencias nuevas: 2003 y 2005,5', sp.Integer(15 - 10) * 100 + (15 - 4), 511, r"$15-4=$ 11")
    # ---- Exámenes
    c('ex-1', 'interpolador de (-2,0),(0,2),(1,3),(3,5)', I([-2, 0, 1, 3], [0, 2, 3, 5]), x + 2, r"$x+2$ vale $0,2,3,5$")
    c('ex-2', 'mismo que E 3.24', iguales(I([1, 5, 8, 10], [3, 11, 38, 56]), -x ** 3 / 9 + R(23, 9) * x ** 2 - R(89, 9) * x + R(94, 9)), 1,
      r"=-\tfrac19x^3+\tfrac{23}9x^2-\tfrac{89}9x+\tfrac{94}9")
    p = I([0, 2, 4], [1, 3, 2])
    c('ex-3', 'p(8), p(1), Simpson e ∫p', lista([p.subs(x, 8), p.subs(x, 1), R(4, 6) * (1 + 12 + 2), sp.integrate(p, (x, 0, 4))], [-9, R(19, 8), 10, 10]), 1,
      r"p(1)=1+1-\frac38\cdot1\cdot(-1)=\frac{19}8=2{,}375")
    g = 11 * x ** 2 - 38 * x + 58
    c('ex-4', 'trapecio, Simpson, ∫g', lista([R(1, 2) * (31 + 52 + 43), R(2, 6) * (31 + 4 * 26 + 43), sp.integrate(g, (x, 1, 3)), iguales(I([1, 2, 3], [31, 26, 43]), g)],
                                           [63, R(178, 3), R(178, 3), 1]), 1, r"\frac{178}3\approx59{,}333")
    c('ex-5', 'Simpson en [0,2]', sp.integrate(I([0, 1, 2], [1, -2, 0]), (x, 0, 2)), R(-7, 3), r"-\frac73")
    p6 = I([0, 1, 2, 4], [15, 18, 20, 23])
    c('ex-6', 'p3, trapecio compuesto y Simpson', lista([iguales(p6, x ** 3 / 12 - R(3, 4) * x ** 2 + R(11, 3) * x + 15), R(1, 2) * (15 + 36 + 20), R(2, 6) * (15 + 72 + 20),
                                                        sp.integrate(p6, (x, 0, 2))], [1, R(71, 2), R(107, 3), R(107, 3)]), 1, r"\frac{107}3\approx35{,}667")
    vals = [R('0.2624'), R('0.3365'), R('0.4055'), R('0.4700')]
    xs7 = [R('1.3'), R('1.4'), R('1.5'), R('1.6')]
    c('ex-7', 'diagonal y p3(1,47) con 4 decimales', lista(diag(xs7, vals) + [r(I(xs7, vals).subs(x, R('1.47')), 4)], [R('0.2624'), R('0.741'), R('-0.255'), R('0.1'), R('0.3853')]), 1,
      r"0{,}3853")
    p8 = I([1, 3, 4, 8], [2, 3, 2, 10])
    c('ex-8', 'p(2) y Simpson compuesta en [1,4] (= ∫p)', lista([p8.subs(x, 2), sp.integrate(p8, (x, 1, 4))], [R(116, 35), R(2409, 280)]), 1,
      r"\frac{116}{35}\approx\mathbf{3{,}3143}")
    # ---- Ejemplos propios
    c('p1', 'interpolador de (-1,4),(1,0),(2,1)', I([-1, 1, 2], [4, 0, 1]), (x - 1) ** 2, r"$p_2(x)=(x-1)^2$ por los dos caminos")
    c('p2', 'con (3,8)', I([-1, 1, 2, 3], [4, 0, 1, 8]), x ** 3 / 2 - R(5, 2) * x + 2, r"=\frac12x^3-\frac52x+2")
    pe = I([0, R(1, 2), 1], [1, sp.exp(R(1, 2)), sp.E])
    c('p3', 'p2(1/4) de e^x', r(pe.subs(x, R(1, 4)), 7), R('1.2717557'), r"=1{,}2717557")
    w = R('0.17') * R('0.07') * R('0.03') * R('0.13')
    c('p4', 'cota de Lagrange para ln 1,47', r(6 / R('1.3') ** 4 / 24 * w, 8), R('0.00000406'), r"\approx4{,}06\cdot10^{-6}")
    # ---- Práctica «Ahora hazlo tú» (respuesta final = «Resultado: …»)
    a = sp.symbols('a')
    P = {
        'pr-a1': (I([0, 1, 2], [1, 3, 7]), x ** 2 + x + 1, r"Resultado: $p_2(x)=x^2+x+1$"),
        'pr-a2': (lista(sp.solve(diag([0, 1, 2, 3], [1, a, 5, 10])[3], a) + [I([0, 1, 2, 3], [1, 2, 5, 10])], [2, x ** 2 + 1]), 1,
                  r"Resultado: $a=2$; $p(x)=x^2+1$"),
        'pr-b1': (lista(diag([0, 1, 3], [2, 3, 11]) + [I([0, 1, 3], [2, 3, 11])], [2, 1, 1, x ** 2 + 2]), 1,
                  r"Resultado: $p_2(x)=2+x+x(x-1)=x^2+2$"),
        'pr-b2': (lista(diag([-1, 0, 2, 3], [-2, 1, 1, 10]) + [I([-1, 0, 2, 3], [-2, 1, 1, 10])], [-2, 3, -1, 1, x ** 3 - 2 * x ** 2 + 1]), 1,
                  r"Resultado: $p_3(x)=-2+3(x+1)-(x+1)x+(x+1)x(x-2)=x^3-2x^2+1$"),
        'pr-c1': (I([1, 2, 4], [4, 7, 19]).subs(x, 3), 12, r"Resultado: $f(3)\approx p_2(3)=12$"),
        'pr-c2': (lista([I([1, 4, 9], [1, 2, 3]).subs(x, 5), I([1, 4, 9], [1, 2, 3]).subs(x, 16)], [R(34, 15), 3]), 1,
                  r"Resultado: $\sqrt5\approx\frac{34}{15}\approx2{,}2667$; $p_2(16)=3\ne4$ (extrapolar falla)"),
        'pr-d1': (lista(diag([0, 1, 3, 2], [2, 3, 11, 4]) + [I([0, 1, 3, 2], [2, 3, 11, 4])], [2, 1, 1, 1, x ** 3 - 3 * x ** 2 + 3 * x + 2]), 1,
                  r"Resultado: $p_3(x)=x^2+2+x(x-1)(x-3)=x^3-3x^2+3x+2$"),
        'pr-d2': (lista([diag([1, 2, 4, 5], [4, 7, 19, 25])[3], I([1, 2, 4, 5], [4, 7, 19, 25]).subs(x, 3)], [R(-1, 4), R(25, 2)]), 1,
                  r"Resultado: $f(3)\approx p_3(3)=12{,}5$; $3$ diferencias nuevas"),
        'pr-e1': (lista([I([1, 2], [1, R(1, 2)]).subs(x, R(3, 2)), sp.diff(1 / x, x, 2).subs(x, 1) / 2 * R(-1, 4), sp.diff(1 / x, x, 2).subs(x, 2) / 2 * R(-1, 4),
                         R(2, 3) - R(3, 4)], [R(3, 4), R(-1, 4), R(-1, 32), R(-1, 12)]), 1,
                  r"Resultado: $p_1(1{,}5)=0{,}75$; $-0{,}25\le f(1{,}5)-p_1(1{,}5)\le-0{,}03125$ (error real $-\frac1{12}$)"),
        'pr-e2': (lista([I([0, pi / 6, pi / 2], [0, R(1, 2), 1]).subs(x, pi / 4), r(pi ** 3 / 1152, 4), sp.Integer(1 if bool(sp.sqrt(2) / 2 - R(11, 16) < pi ** 3 / 1152) else 0)],
                        [R(11, 16), R('0.0269'), 1]), 1,
                  r"Resultado: $\operatorname{sen}\frac\pi4\approx\frac{11}{16}=0{,}6875$, con $0&lt;\text{error}&lt;\frac{\pi^3}{1152}\approx0{,}0269$"),
        'pr-f1': (r(sp.E / 800, 4), R('0.0034'), r"Resultado: $|e^x-p_1(x)|\le\frac{e\cdot0{,}01}{8}\approx0{,}0034$"),
        'pr-f2': (lista([r(sp.sqrt(R(8, 10 ** 6)), 6), sp.ceiling((pi / 2) / sp.sqrt(R(8, 10 ** 6)))], [R('0.002828'), 556]), 1,
                  r"Resultado: $h&lt;\sqrt8\cdot10^{-3}\approx0{,}002828$; $N=556$ subintervalos"),
        'pr-g1': (diag([0, 2, 7], [1, 3, 113])[2], 3, r"Resultado: $f[x_0,x_1,x_2]=3$ para cualesquiera nodos"),
        'pr-g2': (lista(diag([1, 2, 4, 5], [1, 8, 64, 125])[2:], [7, 1]), 1, r"Resultado: $f[1,2,4,5]=1$; $f[1,2,4]=1+2+4=7$"),
    }
    for eid, (val, esp, txt) in P.items():
        if (EJ / f'{eid}.html').exists() or (EJ / f'{eid}.solucion.html').exists():
            c(eid, 'resultado de la práctica', val, esp, txt)
