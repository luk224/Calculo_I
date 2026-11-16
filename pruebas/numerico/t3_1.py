r"""Tema 3.1 (Teorema de Taylor): derivadas sucesivas, polinomios de Taylor, restos de Lagrange y aproximaciones recalculados con sympy.

`comprobaciones(c)`: c(ejercicio, descripción, valor_sympy, esperado, trozo_latex)
  - valor_sympy: lo que calcula sympy (derivadas, polinomios desarrollados, límites, cotas redondeadas a los decimales
    que da la página);  esperado: lo que afirma la página;
  - trozo_latex: cadena que debe aparecer en `ejercicios/<ejercicio>.html` (o `.solucion.html`), comparada sin etiquetas,
    espacios, \, \; \! ni \displaystyle y con \dfrac/\tfrac = \frac.
Las comprobaciones de la práctica «Ahora hazlo tú» (pr-*) solo se activan cuando el ejercicio existe en `contenido/`.
"""
import pathlib

import sympy as sp

x = sp.symbols('x', real=True)
h = sp.symbols('h', real=True)
e, ln, sen, cos = sp.exp, sp.log, sp.sin, sp.cos
pi = sp.pi
EJ = pathlib.Path(__file__).resolve().parents[2] / 'contenido' / 'tema_3_1' / 'ejercicios'
R = sp.Rational


def T(f, x0, n):
    """Polinomio de Taylor de orden n de f centrado en x0 (desarrollado en potencias de x)."""
    x0 = sp.sympify(x0)
    return sp.expand(sum(sp.diff(f, x, k).subs(x, x0) / sp.factorial(k) * (x - x0) ** k for k in range(n + 1)))


def D(f, k, x0):
    """f^{(k}(x0) simplificada."""
    return sp.simplify(sp.diff(f, x, k).subs(x, x0))


def r(v, d):
    """v redondeado a d decimales, como racional exacto."""
    return R(str(round(float(v), d)))


def nmin(cota, eps, desde=0):
    """Menor natural n con cota(n) < eps."""
    n = desde
    while not cota(n) < eps:
        n += 1
    return sp.Integer(n)


def lista(vals, esperados):
    """1 si cada valor coincide con el esperado (para comparar varias derivadas a la vez), 0 si no."""
    return sp.Integer(int(all(sp.simplify(sp.sympify(a) - b) == 0 for a, b in zip(vals, esperados))))


def iguales(a, b):
    return sp.Integer(1) if sp.simplify(sp.expand(a - b)) == 0 else sp.Integer(0)


def comprobaciones(c):
    # ---- Ejercicios del libro (E 3.1-3.14)
    u = x ** 2 + pi / 5
    c('ej-3-1', "f''' de sen(x²+π/5)", sp.simplify(sp.diff(sen(u), x, 3) - (-12 * x * sen(u) - 8 * x ** 3 * cos(u))), 0,
      r"-8x^3\cos")
    c('ej-3-2', 'f^(4 de 3x²-x+1', sp.diff(3 * x ** 2 - x + 1, x, 4), 0, r"$f^{(4}=0$")
    xp = sp.symbols('x', positive=True)
    c('ej-3-3', "f''=-x^{-3/2}/4 para x>0 (respuesta d)", sp.simplify(sp.diff(sp.sqrt(xp), xp, 2) + xp ** R(-3, 2) / 4), 0,
      r"Respuesta: d)")
    c('ej-3-4', 'cociente incremental en 0', sp.limit(((h ** 2 - 1) / h - 0) / h, h, 0), -sp.oo, r"1-\frac1{h^2}\to-\infty")
    c('ej-3-5', "pendiente de f' en (0,1)", sp.diff(x, x), 1, r"$f''=1$")
    f6 = (e(x) - 1) / x
    c('ej-3-6', "f'(0)", sp.limit((f6.subs(x, h) - 1) / h, h, 0), R(1, 2), r"$f'(0)=\frac12$")
    c('ej-3-6', "f''(0)", sp.limit((sp.diff(f6, x).subs(x, h) - R(1, 2)) / h, h, 0), R(1, 3), r"$f''(0)=\frac13$")
    c('ej-3-7', 'p1 de cos en 0', T(cos(x), 0, 1), 1, r"$p_1(x)=1$")
    c('ej-3-8', 'c) desarrollado en potencias de x', sp.expand(2 * x + 3 * (x + 3) ** 2), 27 + 20 * x + 3 * x ** 2, r"27+20x+3x^2")
    c('ej-3-9', 'p3 de ln(x²+1)', T(ln(x ** 2 + 1), 0, 3), x ** 2, r"\boxed{x^2}")
    c('ej-3-10', 'x³-x²+x-2 en potencias de x-1', iguales(T(x ** 3 - x ** 2 + x - 2, 1, 3), -1 + 2 * (x - 1) + 2 * (x - 1) ** 2 + (x - 1) ** 3), 1,
      r"P(x)=-1+2(x-1)+2(x-1)^2+(x-1)^3")
    c('ej-3-11', 'p1 de x² en 0', T(x ** 2, 0, 1), 0, r"$p_1=0\ne x^2$")
    c('ej-3-12', 'p3 de ln(cos x)', T(ln(cos(x)), 0, 3), -x ** 2 / 2, r"p_3(x)=-\tfrac12x^2")
    c('ej-3-12', 'cota (3-2cos²1)/(12cos⁴1)', r((3 - 2 * cos(1) ** 2) / (12 * cos(1) ** 4), 3), R('2.363'), r"2{,}363")
    c('ej-3-12', 'f^(4 de ln(cos x)', sp.simplify(sp.diff(ln(cos(x)), x, 4) + 2 * (3 - 2 * cos(x) ** 2) / cos(x) ** 4), 0,
      r"-2\,\dfrac{3-2\cos^2x}{\cos^4x}")
    pe = e(-1) * (1 + (x + 1) + (x + 1) ** 2 / 2 + (x + 1) ** 3 / 6)
    c('ej-3-13', 'p3 de x+e^x en -1', iguales(T(x + e(x), -1, 3), (e(-1) - 1) + (1 + e(-1)) * (x + 1) + e(-1) / 2 * (x + 1) ** 2
                                                + e(-1) / 6 * (x + 1) ** 3) * iguales(T(e(x), -1, 3), pe), 1,
      r"(e^{-1}-1)+(1+e^{-1})(x+1)")
    c('ej-3-13', 'p3 de (x+1)e^x en -1', iguales(T((x + 1) * e(x), -1, 3), e(-1) * ((x + 1) + (x + 1) ** 2 + (x + 1) ** 3 / 2)), 1,
      r"p_3^h(x)=e^{-1}\big((x+1)+(x+1)^2+\tfrac{(x+1)^3}{2}\big)")
    c('ej-3-14', 'x máximo con x⁴/4 ≤ 10^-4', sp.root(R(4, 10 ** 4), 4), sp.sqrt(2) / 10, r"=\frac{\sqrt2}{10}")
    c('ej-3-14', 'p3 de ln(1+x)', T(ln(1 + x), 0, 3), x - x ** 2 / 2 + x ** 3 / 3, r"p_3(x)=x-\frac{x^2}2+\frac{x^3}3")
    # ---- Ejemplos propios y de U
    c('a1-f-n-de-xe-x-f-cil', "f^(5 de xe^x", sp.simplify(sp.diff(x * e(x), x, 5) - (x + 5) * e(x)), 0, r"f^{(n}(x)=(x+n)e^x")
    c('a2-f-n-de-frac1-1-x-medio', 'f^(4 de 1/(1+x)', sp.simplify(sp.diff(1 / (1 + x), x, 4) - 24 / (1 + x) ** 5), 0,
      r"\dfrac{(-1)^n\,n!}{(1+x)^{n+1}}")
    c('a3-continua-derivada-continua-', "g'(h)/h por la derecha", sp.limit(2 * sp.Abs(h) / h, h, 0, '+'), 2, r"\to2$")
    c('a3-continua-derivada-continua-', "g'(h)/h por la izquierda", sp.limit(2 * sp.Abs(h) / h, h, 0, '-'), -2, r"\to-2$")
    c('b0-taylor-de-orden-2-de-x-en-0', '|h|/h por la izquierda', sp.limit(sp.Abs(h) / h, h, 0, '-'), -1, r"$-1$ por la izquierda")
    c('b1-mac-laurin-de-orden-4-de-co', 'p4 de cos', T(cos(x), 0, 4), 1 - x ** 2 / 2 + x ** 4 / 24, r"p_4(x)=1-\frac{x^2}{2}+\frac{x^4}{24}")
    c('b2-taylor-de-orden-2-de-sqrt-x', 'p2 de √x en 4', iguales(T(sp.sqrt(x), 4, 2), 2 + (x - 4) / 4 - (x - 4) ** 2 / 64), 1,
      r"p_2(x)=2+\frac{x-4}{4}-\frac{(x-4)^2}{64}")
    c('b3-mac-laurin-de-e-x-operatorn', 'p3 de e^x sen x', T(e(x) * sen(x), 0, 3), x + x ** 2 + x ** 3 / 3, r"p_3(x)=x+x^2+\frac{x^3}{3}")
    c('b3-mac-laurin-de-e-x-operatorn', 'p4 de e^{-x²}', T(e(-x ** 2), 0, 4), 1 - x ** 2 + x ** 4 / 2, r"e^{-x^2}=1-x^2+\frac{x^4}2")
    c('c0-el-truco-de-u-ej-3-10-usar-', 'cota de R4(1/2) para sen', r(R(1, 2) ** 5 / 120, 5), R('0.00026'), r"0{,}00026")
    c('c1-e-0-1-con-p-3-y-cota-f-cil', 'p3(0,1) de e^x', r(T(e(x), 0, 3).subs(x, R(1, 10)), 7), R('1.1051667'), r"1{,}1051667")
    c('c1-e-0-1-con-p-3-y-cota-f-cil', 'cota 2·10^-4/24', r(R(2, 10 ** 4) / 24, 7), R('0.0000083'), r"8{,}3\cdot10^{-6}")
    c('c2-sqrt-4-1-con-el-p-2-de-b2-y', 'p2(4,1) de √x', T(sp.sqrt(x), 4, 2).subs(x, R(41, 10)), R('2.02484375'), r"2{,}02484375")
    c('c2-sqrt-4-1-con-el-p-2-de-b2-y', "f''' de √x", sp.simplify(sp.diff(sp.sqrt(xp), xp, 3) - R(3, 8) * xp ** R(-5, 2)), 0,
      r"f'''(x)=\frac{3}{8x^{5/2}}")
    c('c3-qu-orden-hace-falta-para-sq', 'n mínimo y p4(1/2)',
      nmin(lambda n: 2 / (sp.factorial(n + 1) * 2 ** (n + 1)), R(1, 1000)) + T(e(x), 0, 4).subs(x, R(1, 2)), 4 + R(211, 128),
      r"p_4(\frac12)=\frac{211}{128}")
    c('c4-para-qu-x-ge0-vale-cos-x-ap', '(24·10^-4)^{1/4}', r(sp.root(R(24, 10 ** 4), 4), 4), R('0.2213'), r"0\le x&lt;0{,}2213")
    # ---- Exámenes
    c('ex-1', '(n+1)! con n=3', sp.factorial(4), 24, r"\frac{f^{(4}(c)}{24}\,x^4")
    c('ex-2', 'p2(π²) frente a f(π²)=1', ((x - pi ** 2) ** 2 + 2 * pi ** 2 + 1).subs(x, pi ** 2), 2 * pi ** 2 + 1,
      r"$2\pi^2+1\ne1$")
    c('ex-3', 'p3 de sen(πx) en 1/2', iguales(T(sen(pi * x), R(1, 2), 3), 1 - pi ** 2 / 2 * (x - R(1, 2)) ** 2), 1,
      r"p_3(x)=1-\dfrac{\pi^2}{2}\left(x-\tfrac12\right)^2")
    p4 = (x - pi) ** 2 + (x - pi) ** 3 / 4
    c('ex-4', "f(π), f''(π), f'''(π), f^(4(π)", lista([D(p4, k, pi) for k in (0, 2, 3, 4)], [0, 2, R(3, 2), 0]), 1,
      r"f'''(\pi)=\frac32")
    c('ex-5', 'p3 de (3x-1)e^x en -1', iguales(T((3 * x - 1) * e(x), -1, 3),
                                              e(-1) * (-4 - (x + 1) + (x + 1) ** 2 + R(5, 6) * (x + 1) ** 3)), 1,
      r"p_3(x)=e^{-1}\left[-4-(x+1)+(x+1)^2+\frac56(x+1)^3\right]")
    c('ex-6', 'n mínimo y p3(1/4) de cos',
      nmin(lambda n: R(1, 4) ** (n + 1) / sp.factorial(n + 1), R(2, 1000)) + T(cos(x), 0, 3).subs(x, R(1, 4)), 3 + R(31, 32),
      r"=\frac{31}{32}=0{,}96875")
    # ---- Práctica «Ahora hazlo tú» (respuesta final = «Resultado: …»)
    lnx1 = ln(1 + x)
    P = {
        'pr-a1': (iguales(T(1 / x, 2, 3), R(1, 2) - (x - 2) / 4 + (x - 2) ** 2 / 8 - (x - 2) ** 3 / 16), 1,
                  r"Resultado: $p_3(x)=\frac12-\frac{x-2}{4}+\frac{(x-2)^2}{8}-\frac{(x-2)^3}{16}$"),
        'pr-a2': (T(sp.tan(x), 0, 4), x + x ** 3 / 3,
                  r"Resultado: $p_4(x)=x+\frac{x^3}{3}$ (orden $4$, grado $3$)"),
        'pr-b1': (lista([D(3 - (x - 2) + 5 * (x - 2) ** 3, k, 2) for k in range(4)]
                         + [(3 - (x - 2) + 5 * (x - 2) ** 3).subs(x, R(21, 10))], [3, -1, 0, 30, R('2.905')]), 1,
                  r"Resultado: $f(2)=3$, $f'(2)=-1$, $f''(2)=0$, $f'''(2)=30$; $f(2{,}1)\approx p_3(2{,}1)=2{,}905$"),
        'pr-b2': (iguales(T(x ** 4 - 3 * x ** 2 + 2, 1, 2), -2 * (x - 1) + 3 * (x - 1) ** 2)
                  * iguales(T(x ** 4 - 3 * x ** 2 + 2, 1, 4), -2 * (x - 1) + 3 * (x - 1) ** 2 + 4 * (x - 1) ** 3 + (x - 1) ** 4), 1,
                  r"Resultado: $p_2(x)=-2(x-1)+3(x-1)^2$; $p_4(x)=-2(x-1)+3(x-1)^2+4(x-1)^3+(x-1)^4=P(x)$"),
        'pr-c1': (T(sen(x ** 2), 0, 6) + D(sen(x ** 2), 6, 0), x ** 2 - x ** 6 / 6 - 120,
                  r"Resultado: $p_6(x)=x^2-\frac{x^6}{6}$; $f^{(6}(0)=-120$"),
        'pr-c2': (T(e(x) * cos(x), 0, 4) + D(e(x) * cos(x), 4, 0), 1 + x - x ** 3 / 3 - x ** 4 / 6 - 4,
                  r"Resultado: $p_4(x)=1+x-\frac{x^3}{3}-\frac{x^4}{6}$; $f^{(4}(0)=-4$"),
        'pr-d1': (T(e(x), 0, 2).subs(x, -R(1, 5)) + R(8, 1000) / 6, R('0.82') + R(1, 750),
                  r"Resultado: $e^{-0{,}2}\approx0{,}82$, con error $&lt;\frac{1}{750}\approx0{,}0013$"),
        'pr-d2': (T(sp.cbrt(x), 27, 2).subs(x, 28) + R(10, 27) / 3 ** 8 / 6, R(6641, 2187) + R(5, 531441),
                  r"Resultado: $\sqrt[3]{28}\approx\frac{6641}{2187}\approx3{,}036580$, con error $&lt;\frac{5}{531441}\approx9{,}4\cdot10^{-6}$"),
        'pr-e1': (nmin(lambda n: 3 / sp.factorial(n + 1), R(1, 1000)) + T(e(x), 0, 6).subs(x, 1), 6 + R(1957, 720),
                  r"Resultado: $n=6$; $e\approx\frac{1957}{720}\approx2{,}71806$"),
        'pr-e2': (nmin(lambda n: R(1, 4) ** (n + 1) / (n + 1), R(1, 1000), 1) + T(lnx1, 0, 3).subs(x, -R(1, 5)), 3 - R(167, 750),
                  r"Resultado: $n=3$; $\ln0{,}8\approx-\frac{167}{750}\approx-0{,}22267$"),
        'pr-f1': (sp.limit((x - sen(x)) / x ** 3, x, 0), R(1, 6), r"Resultado: $\frac16$"),
        'pr-f2': (sp.limit((e(x ** 2) - cos(x) - R(3, 2) * x ** 2) / x ** 4, x, 0), R(11, 24), r"Resultado: $\frac{11}{24}$"),
        'pr-g1': (r(sp.root(R(6, 1000), 3), 4), R('0.1817'),
                  r"Resultado: $|x|&lt;\sqrt[3]{0{,}006}\approx0{,}1817$"),
        'pr-g2': (sp.simplify(R(10, 9) ** R(3, 2) / 800) + sp.sqrt(R(8, 100)), sp.sqrt(10) / 2160 + sp.sqrt(2) / 5,
                  r"Resultado: en $[-0{,}1;0{,}1]$ el error es $&lt;\frac{\sqrt{10}}{2160}\approx0{,}0015$; para $x\ge0$ basta $0\le x&lt;\frac{\sqrt2}{5}\approx0{,}283$"),
    }
    for eid, (val, esp, txt) in P.items():
        if (EJ / f'{eid}.html').exists() or (EJ / f'{eid}.solucion.html').exists():
            c(eid, 'resultado de la práctica', val, esp, txt)
