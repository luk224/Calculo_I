r"""Tema 2.4 (Newton y punto fijo): iteraciones, cotas de error y números de iteraciones recalculados con sympy.

`comprobaciones(c)`: c(ejercicio, descripción, valor_sympy, esperado, trozo_latex)
  - valor_sympy: lo que calcula sympy (iterados redondeados a los decimales que da la página, número de iteraciones,
    valores exactos);  esperado: lo que afirma la página;
  - trozo_latex: cadena que debe aparecer en `ejercicios/<ejercicio>.html` (o `.solucion.html`), comparada sin etiquetas,
    espacios, \, \; \! ni \displaystyle y con \dfrac/\tfrac = \frac.
Las comprobaciones de la práctica «Ahora hazlo tú» (pr-*) solo se activan cuando el ejercicio existe en `contenido/`.
"""
import pathlib

import sympy as sp

x = sp.symbols('x', real=True)
e, ln, sen, cos = sp.exp, sp.log, sp.sin, sp.cos
EJ = pathlib.Path(__file__).resolve().parents[2] / 'contenido' / 'tema_2_4' / 'ejercicios'
PREC = 40


def newton(f, x0, n, exacto=False):
    """Lista [x0, x1, …, xn] de Newton para f(x)=0 (exacta con fracciones si exacto=True)."""
    N = x - f / sp.diff(f, x)
    xs = [sp.sympify(x0) if exacto else sp.Float(x0, PREC)]
    for _ in range(n):
        v = N.subs(x, xs[-1])
        xs.append(sp.simplify(v) if exacto else sp.N(v, PREC))
    return xs


def fijo(g, x0, n):
    """Lista [x0, …, xn] de x_{k+1}=g(x_k) (con 40 cifras)."""
    xs = [sp.Float(x0, PREC)]
    for _ in range(n):
        xs.append(sp.N(g.subs(x, xs[-1]), PREC))
    return xs


def r(v, d):
    """v redondeado a d decimales, como racional exacto (para comparar con lo escrito en la página)."""
    return sp.Rational(str(round(float(v), d)))


def nmin(cota, eps, desde=1):
    """Menor natural n con cota(n) < eps."""
    n = desde
    while not cota(n) < eps:
        n += 1
    return sp.Integer(n)


def teor23(k, l):
    """Cota del Teorema 2.3 de U: n -> k^n/(1-k)·(b-a)."""
    return lambda n: k ** n / (1 - k) * l


def biseccion(f, a, b, n):
    """Puntos medios c1..cn de la bisección (U p.54) en [a,b] con fracciones."""
    cs = []
    for _ in range(n):
        c = (a + b) / 2
        cs.append(c)
        if f.subs(x, a) * f.subs(x, c) < 0:
            b = c
        else:
            a = c
    return cs


def comprobaciones(c):
    # ---- Ejercicios del libro (E 2.34-2.38)
    s5 = newton(x ** 2 - 5, 2, 4, exacto=True)
    c('ej-2-34', 'x4 exacto de Newton para x²-5', s5[4], sp.Rational(5374978561, 2403763488),
      r"x_4=\frac{5374978561}{2403763488}")
    c('ej-2-35', 'x3 de Newton para x²', newton(x ** 2, sp.Rational(2, 5), 3, exacto=True)[3],
      sp.Rational(1, 20), r"$x_3=0.05$")
    c('ej-2-36', 'x3 desde x0=0.5', r(newton(e(-x) - x, 0.5, 3)[3], 12), sp.Rational('0.567143290410'),
      r"0.567143290410")
    c('ej-2-36', 'x3 desde x0=5', r(newton(e(-x) - x, 5, 3)[3], 12), sp.Rational('0.566534509041'),
      r"0.566534509041")
    c('ej-2-37', 'k=0.8, error<0.1', nmin(teor23(sp.Rational(4, 5), 2), sp.Rational(1, 10)), 21,
      r"El primer natural es $n=21$")
    c('ej-2-37', 'k=0.2, error<0.1', nmin(teor23(sp.Rational(1, 5), 2), sp.Rational(1, 10)), 3,
      r"sale $n=3$")
    c('ej-2-38', 'x4 de e^{-x} desde 1', r(fijo(e(-x), 1, 4)[4], 4), sp.Rational('0.6062'),
      r"$x_4\approx0.6062$")
    c('ej-2-38', 'iteraciones garantizadas para 0.01', nmin(teor23(e(-sp.Rational(1, 10)), sp.Rational(19, 10)),
                                                                                    sp.Rational(1, 100)), 76, r"o sea $76$ iteraciones")
    # ---- Ejemplos propios
    c('ej-p1', 'x1 y x3 para x³-10', r(newton(x ** 3 - 10, 2, 3)[3], 12) + newton(x ** 3 - 10, 2, 1, True)[1],
      sp.Rational('2.154434692237') + sp.Rational(13, 6), r"2.154434692237")
    c('ej-p2', 'x4 para x³-x-1 desde 1.5', r(newton(x ** 3 - x - 1, 1.5, 4)[4], 12), sp.Rational('1.324717957245'),
      r"1.324717957245")
    c('ej-p3', 'ciclo 0,1,0 y x4 desde -2',
      sum(newton(x ** 3 - 2 * x + 2, 0, 2, True)) + r(newton(x ** 3 - 2 * x + 2, -2, 4)[4], 12),
      1 + sp.Rational('-1.769292354239'), r"-1.769292354239")
    c('ej-p4', 'k=0.5, [0,1], error<10^-3', nmin(teor23(sp.Rational(1, 2), 1), sp.Rational(1, 1000)), 11,
      r"luego $n=11$")
    c('ej-p5', 'k=sen 1, error<0.01', nmin(teor23(sen(1), 1), sp.Rational(1, 100)), 38, r"luego $n=38$")
    c('ej-p6', 'k=1/(3·4^{1/3}), error<10^-6',
      nmin(teor23(1 / (3 * sp.cbrt(4)), 1), sp.Rational(1, 10 ** 6)), 10, r"o sea $n=10$")
    # ---- Exámenes
    c('ex-1', 'bisección en [-1,1], error<0.15', nmin(lambda n: sp.Rational(2, 2 ** n), sp.Rational(15, 100)), 4,
      r"$n=4$ iteraciones")
    c('ex-2', 'x2 exacto para e^x+2x-4', sp.simplify(newton(e(x) + 2 * x - 4, 0, 2, True)[2] - 4 / (sp.E + 2)), 0,
      r"x_2=\dfrac{4}{e+2}\approx0.8477")
    c('ex-3', 'x5 de 1-1/(x²+2)', r(fijo(1 - 1 / (x ** 2 + 2), 0, 5)[5], 4), sp.Rational('0.5697'),
      r"$x_5\approx0.5697$")
    c('ex-4', 'raíz de x-2^{-x}', r(newton(x - 2 ** (-x), 0, 3)[3], 3), sp.Rational('0.641'),
      r"la raíz es $0.641$")
    g5 = sen(x) / 2 + 1
    c('ex-5', 'x4 y cota π/8', r(fijo(g5, 2, 4)[4], 4) + teor23(sp.Rational(1, 2), sp.pi)(4),
      sp.Rational('1.4987') + sp.pi / 8, r"(c) error $&lt;\pi/8\approx0.39$")
    g6 = cos(x ** 2) * sen(x + 1) / 2
    c('ex-6', 'n con k=1/2 en [0,1/2] y x4',
      nmin(lambda n: sp.Rational(1, 2 ** n), sp.Rational(1, 10)) + r(fijo(g6, 0, 4)[4], 5) - sp.Rational('0.48449'), 4,
      r"$n=4$ iteraciones; solución aproximada $0.48449$")
    # ---- Práctica «Ahora hazlo tú» (respuesta final = «Resultado: …»)
    lnx = ln(x)
    d1 = [sp.Integer(0)]
    for _ in range(3):
        d1.append((d1[-1] ** 2 + 2) / 5)
    P = {
        'pr-a1': (newton(x ** 3 + 2 * x - 5, 1, 2, True)[2] + r(newton(x ** 3 + 2 * x - 5, 1, 2)[2], 5),
                  sp.Rational(1311, 985) + sp.Rational('1.33096'),
                  r"Resultado: $x_1=\frac75=1.4$, $x_2=\frac{1311}{985}\approx1.33096$"),
        'pr-a2': (sp.expand(x * (2 - 7 * x) - (x - (1 / x - 7) / sp.diff(1 / x - 7, x)))
                  + newton(1 / x - 7, sp.Rational(1, 10), 3, True)[3], sp.Rational('0.14284777'),
                  r"Resultado: $x_{n+1}=x_n(2-7x_n)$; $x_1=0.13$, $x_2=0.1417$, $x_3=0.14284777$"),
        'pr-b1': (r(newton(x ** 4 - x - 10, 2, 3)[3], 5) + sum(
            1 for i in (1, 2, 3) if abs(newton(x ** 4 - x - 10, 2, 3)[i] - newton(x ** 4 - x - 10, 2, 3)[i - 1])
            / abs(newton(x ** 4 - x - 10, 2, 3)[i]) >= sp.Rational(1, 1000)),
                  sp.Rational('1.85558') + 2, r"Resultado: se para en $n=3$, $x_3\approx1.85558$"),
        'pr-b2': (r(newton(x - 2 * sen(x), 2, 3)[3], 6) + r(newton(x - 2 * sen(x), 1, 1)[1], 2),
                  sp.Rational('1.895494') + sp.Rational('-7.47'),
                  r"Resultado: $x_3\approx1.895494$ (se para en $n=3$); desde $x_0=1$ sale $x_1\approx-7.47$"),
        'pr-c1': (sp.diff(x ** 2 - 4 * x + 3, x).subs(x, 2) + newton(x ** 2 - 4 * x + 3, 0, 3, True)[3], sp.Rational(3279, 3280),
                  r"Resultado: $f'(2)=0$; $x_1=\frac34$, $x_2=\frac{39}{40}$, $x_3=\frac{3279}{3280}\to1$"),
        'pr-c2': (r(newton(sp.atan(x), 0.5, 1)[1], 4) + r(newton(sp.atan(x), 1.5, 2)[2], 2),
                  sp.Rational('-0.0796') + sp.Rational('2.32'),
                  r"Resultado: desde $0.5$ converge a $0$ ($x_1\approx-0.0796$); desde $1.5$ diverge ($x_1\approx-1.69$, $x_2\approx2.32$, $x_3\approx-5.11$)"),
        'pr-d1': (d1[3] + teor23(sp.Rational(2, 5), 1)(3) + sp.solve(x ** 2 - 5 * x + 2, x)[0],
                  sp.Rational(34166, 78125) + sp.Rational(8, 75) + (5 - sp.sqrt(17)) / 2,
                  r"Resultado: $x_3=\frac{34166}{78125}\approx0.437325$; $\tilde x=\frac{5-\sqrt{17}}2\approx0.438447$; cota $\frac{8}{75}$"),
        'pr-d2': (r(sp.nsolve(e(x) / 3 - x, 0.6), 4) + r(sp.nsolve(e(x) / 3 - x, 1.5), 4) + r(e(2) / 3, 2),
                  sp.Rational('0.6191') + sp.Rational('1.5121') + sp.Rational('2.46'),
                  r"Resultado: en $[0,1]$ se cumple el Teorema 2.2 con $k=\frac e3$ (punto fijo $\approx0.6191$); en $[0,2]$ no ($g(2)\approx2.46$; hay otro punto fijo, $\approx1.5121$)"),
        'pr-e1': (nmin(teor23(sp.Rational(3, 5), 2), sp.Rational(1, 100)), 13, r"Resultado: $n=13$"),
        'pr-e2': (nmin(teor23(sp.cbrt(6) / 18, 1), sp.Rational(1, 10 ** 6)) + r(fijo(sp.cbrt(x + 5), 1, 3)[3], 6),
                  7 + sp.Rational('1.903422'), r"Resultado: $n=7$; $x_3\approx1.903422$"),
        'pr-f1': (sum(biseccion(x ** 3 - 2 * x - 5, sp.Integer(2), sp.Integer(3), 3))
                  + nmin(lambda n: sp.Rational(1, 2 ** n), sp.Rational(1, 1000)),
                  sp.Rational(5, 2) + sp.Rational(9, 4) + sp.Rational(17, 8) + 10,
                  r"Resultado: $c_1=2.5$, $c_2=2.25$, $c_3=2.125$; $n=10$ iteraciones"),
        'pr-f2': (r(newton(lnx - x + 2, 0.2, 3)[3], 4) + r(newton(lnx - x + 2, 3, 2)[2], 4) + r(newton(lnx - x + 2, 0.5, 1)[1], 3),
                  sp.Rational('0.1586') + sp.Rational('3.1462') + sp.Rational('-0.307'),
                  r"Resultado: dos raíces, $\approx0.1586$ y $\approx3.1462$; desde $x_0=0.5$ Newton se sale del dominio ($x_1\approx-0.307$)"),
        'pr-g1': (newton(x ** 2 - 3, 2, 3, True)[3] + sp.Rational(1, 6) ** 3 / sp.Rational(5, 6) / 2,
                  sp.Rational(18817, 10864) + sp.Rational(1, 360),
                  r"Resultado: $k=\frac16$; $x_3=\frac{18817}{10864}$, con error $&lt;\frac1{360}$"),
        'pr-g2': (nmin(teor23(sp.Rational(2, 3), 1), sp.Rational(1, 1000)) + nmin(teor23(sp.Rational(62, 343), sp.Rational(1, 5)),
                                                                              sp.Rational(1, 1000)),
                  20 + 4, r"Resultado: en $[1,2]$, $k=\frac23$ y $n=20$; en $[1.2,1.4]$, $k=\frac{62}{343}$ y $n=4$"),
    }
    for eid, (val, esp, txt) in P.items():
        if (EJ / f'{eid}.html').exists() or (EJ / f'{eid}.solucion.html').exists():
            c(eid, 'resultado de la práctica', val, esp, txt)
