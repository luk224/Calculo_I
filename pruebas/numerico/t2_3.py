"""Tema 2.3 (L'Hôpital): cada límite se recalcula con sympy y se comprueba que la solución de la página escribe ese resultado.

`comprobaciones(c)`: c(ejercicio, descripción, valor_sympy, esperado, trozo_latex)
  - valor_sympy: lo que calcula sympy (límite);  esperado: lo que afirma la página (exacto);
  - trozo_latex: cadena que debe aparecer en `ejercicios/<ejercicio>.solucion.html` (o `.html` en las de práctica), comparada sin espacios ni
    \\displaystyle y con \\dfrac/\\tfrac = \\frac.
"""
import sympy as sp

x = sp.symbols('x', real=True)
xp = sp.symbols('x', positive=True)
n = sp.symbols('n', positive=True, integer=True)
a = sp.symbols('a', positive=True)
oo = sp.oo


def L(f, v, p, dir='+-'):
    return sp.limit(f, v, p, dir)


def comprobaciones(c):
    # ---- Ejercicios del libro (E 2.24-2.33)
    c('ej-2-24', '1^∞ con logaritmos', L(((2 * sp.log(xp) + 1) / (2 * sp.log(xp))) ** sp.log(xp), xp, oo), sp.sqrt(sp.E), r'\sqrt e')
    c('ej-2-25', '0/0 con raíz y log', L((sp.log(1 + x) - x) / (1 - sp.sqrt(1 - x ** 2)), x, 0), -1, r'-1')
    c('ej-2-26', '0/0 polinomios', L((x ** 5 + x ** 4 - x ** 2 + 1) / (x ** 4 - 1), x, -1), sp.Rational(-3, 4), r'-\frac34')
    c('ej-2-27', 'L\'Hôpital da vueltas', L((sp.sin(x) + sp.exp(x)) / (sp.cos(x) + sp.exp(x)), x, oo), 1, r'\frac{0+1}{0+1}')
    c('ej-2-28', '∞/∞ lateral', L((2 - sp.log(sp.cos(x))) / (2 + sp.tan(x)), x, sp.pi / 2, '-'), 0, r'El límite vale $0$')
    c('ej-2-29', '∞^0 (test)', L(xp ** (1 / (xp + 1)), xp, oo), 1, r'Respuesta b)')
    c('ej-2-30', '0·∞', L(xp * sp.log(xp), xp, 0, '+'), 0, r'=0$')
    c('ej-2-31', '0^0', L(xp ** (xp ** 2), xp, 0, '+'), 1, r'e^0=1')
    k = 3
    c('ej-2-32', 'x^n/a^x (n=3, a=2)', L(xp ** k / 2 ** xp, xp, oo), 0, r'\to0$')
    c('ej-2-33', 'sucesión con logaritmos', L(sp.log((n + 1) / n) / sp.log((n + 2) / (n + 1)), n, oo), 1, r'es $1$')
    # ---- Propios
    c('ej-p1', '0/0', L((sp.exp(x) - 1 - x) / x ** 2, x, 0), sp.Rational(1, 2), r'\frac12')
    c('ej-p2', '∞-∞', L(1 / x - 1 / (sp.exp(x) - 1), x, 0), sp.Rational(1, 2), r'Resultado:$\frac12$')
    c('ej-p3', '1^∞', L(sp.cos(x) ** (1 / x ** 2), x, 0), sp.exp(-sp.Rational(1, 2)), r'e^{-1/2}')
    c('ej-p4', 'sucesión n(a^{1/n}-1)', L(n * (2 ** (1 / n) - 1), n, oo), sp.log(2), r'\ln2')
    # ---- Exámenes
    c('ex-1', 'Feb. 2018: 0/0', L((sp.exp(x) - x - 1) / x ** 2, x, 0), sp.Rational(1, 2), r'El límite vale $\frac12$')
    c('ex-2', 'Feb. 2011: ∞/∞', L((x + sp.exp(x)) / (2 * x + sp.exp(x)), x, oo), 1, r'El límite vale $1$')
    c('ex-3', 'Electrónica: ∞-∞', L(1 / x - 1 / (1 - sp.cos(x)), x, 0), -oo, r'El límite vale $-\infty$')
    c('ex-4', 'Sept. 2010: 0^0', L(xp ** (xp ** 2), xp, 0, '+'), 1, r'e^{0}=1')
    c('ex-5', '1^∞', L(((xp - 1) / (xp + 2)) ** xp, xp, oo), sp.exp(-3), r'e^{L}=e^{-3}')
    # ex-6: f(x)=x/(e^x-1), f(0)=1: continuidad de f y de f' en 0
    f = x / (sp.exp(x) - 1)
    fp = sp.diff(f, x)
    c('ex-6', 'f continua en 0: lím f = f(0) = 1', L(f, x, 0), 1, r'f(0)=1')
    c('ex-6', "f'(0) por la definición", L((f - 1) / x, x, 0), -sp.Rational(1, 2), r'-\tfrac12')
    c('ex-6', "lím f'(x) en 0 = f'(0)", L(fp, x, 0), -sp.Rational(1, 2), r'-\tfrac12')
    # ---- Práctica (respuesta final = «Resultado: …»)
    P = {
        'pr-a1': (L(sp.sin(3 * x) / sp.log(1 + x), x, 0), 3, r'Resultado:$3$'),
        'pr-a2': (L((x - sp.atan(x)) / x ** 3, x, 0), sp.Rational(1, 3), r'Resultado:$\frac13$'),
        'pr-b1': (L(sp.log(xp) ** 2 / xp, xp, oo), 0, r'Resultado:$0$'),
        'pr-b2': (L(sp.log(xp) / sp.log(sp.sin(xp)), xp, 0, '+'), 1, r'Resultado:$1$'),
        'pr-c1': (L(xp * sp.sin(2 / xp), xp, oo), 2, r'Resultado:$2$'),
        'pr-c2': (L(xp * (sp.pi / 2 - sp.atan(xp)), xp, oo), 1, r'Resultado:$1$'),
        'pr-d1': (L(1 / sp.sin(x) - 1 / sp.tan(x), x, 0), 0, r'Resultado:$0$'),
        'pr-d2': (L(xp / (xp - 1) - 1 / sp.log(xp), xp, 1), sp.Rational(1, 2), r'Resultado:$\frac12$'),
        'pr-e1': (L((1 + sp.sin(x)) ** (1 / x), x, 0), sp.E, r'Resultado:$e$'),
        'pr-e2': (L((1 + x ** 2) ** (1 / (1 - sp.cos(x))), x, 0), sp.E ** 2, r'Resultado:$e^2$'),
        'pr-f1': (L(xp ** sp.sin(xp), xp, 0, '+'), 1, r'Resultado:$1$'),
        'pr-f2': (L((sp.exp(xp) + xp) ** (1 / xp), xp, oo), sp.E, r'Resultado:$e$'),
        'pr-g1': (L(sp.log(n) / sp.log(n + 1), n, oo), 1, r'Resultado:$1$'),
        'pr-g2': (L(n ** 2 * (1 - sp.cos(1 / n)), n, oo), sp.Rational(1, 2), r'Resultado:$\frac12$'),
    }
    for eid, (val, esp, txt) in P.items():
        c(eid, 'resultado de la práctica', val, esp, txt)
