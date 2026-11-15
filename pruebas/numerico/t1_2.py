"""Tema 1.2 (sucesiones): cada resultado se recalcula con sympy y se comprueba que la solución de la página lo escribe.

`comprobaciones(c)`: c(ejercicio, descripción, valor_sympy, esperado, trozo_latex)
  - valor_sympy: lo que calcula sympy;  esperado: lo que afirma la página (exacto o redondeado como en la página);
  - trozo_latex: cadena que debe aparecer en `ejercicios/<ejercicio>.html` (o `.solucion.html`), comparada sin etiquetas,
    espacios ni \\displaystyle y con \\dfrac/\\tfrac = \\frac.
Las sumas de n términos (sympy no siempre calcula su límite) se comprueban por sus cotas del emparedado o por el
cociente de incrementos de Stolz, más un valor numérico.
Las comprobaciones de la práctica «Ahora hazlo tú» (pr-*) solo se activan cuando el ejercicio existe en `contenido/`.
"""
import pathlib

import sympy as sp

n = sp.symbols('n', positive=True, integer=True)
x = sp.symbols('x', real=True)
oo = sp.oo
EJ = pathlib.Path(__file__).resolve().parents[2] / 'contenido' / 'tema_1_2' / 'ejercicios'


def L(f):
    """Límite cuando n → ∞."""
    return sp.limit(f, n, oo)


def si(cond):
    """Comprobación lógica: 1 si se cumple (se compara con esperado = 1)."""
    return sp.Integer(1 if bool(cond) else 0)


def r(v, k=4):
    """Redondeo a k decimales (como se escribe en la página)."""
    return sp.Rational(str(round(float(v), k)))


def recurrencia(a1, g, m):
    """Términos a_1..a_m de a_{n+1} = g(a_n) (exactos)."""
    t = [sp.nsimplify(a1)]
    for _ in range(m - 1):
        t.append(sp.nsimplify(g(t[-1])))
    return t


def comprobaciones(c):
    # ---- Ejercicios del libro (E 1.6-1.16)
    c('ej-1-6', 'x_n=1/n², y_n=n: producto → 0', L(n * (1 / n ** 2)), 0, r'x_ny_n=\frac n{n^2}=\frac1n\to0')
    c('ej-1-6', 'x_n→1, y_n=n: producto → ∞', L((1 + 1 / n) * n), oo, r'el producto tiende a $+\infty$')
    c('ej-1-7', 'n/√(n³+4)', L(n / sp.sqrt(n ** 3 + 4)), 0, r'$\lim_{n\to\infty} a_n=0$')
    c('ej-1-8', 'cociente con exponenciales', L((sp.exp(n + 3 / n) + 5) / (2 * sp.exp(n))), sp.Rational(1, 2), r'\lim_{n\to\infty} x_n=\frac12+0=\boxed{\tfrac12}')
    c('ej-1-9', 'cociente con dos raíces', L(sp.sqrt(16 * n ** 4 - 4) / (n * sp.sqrt(4 * n ** 2 + 5))), 2, r'\lim_{n\to\infty} a_n=\boxed2')
    c('ej-1-10', 'conjugado', L(sp.sqrt(n ** 2 + 4 * n + 8) - n), 2, r'\frac4{1+1}=\boxed2')
    c('ej-1-11', 'pan inferior', L(n / sp.sqrt(n ** 2 + n)), 1, r'a_n=\dfrac1{\sqrt{1+1/n}}\to1')
    c('ej-1-11', 'pan superior', L(n / sp.sqrt(n ** 2 + 1)), 1, r'c_n=\dfrac1{\sqrt{1+1/n^2}}\to1')
    c('ej-1-11', 'b_10 numérico', r(sum(1 / sp.sqrt(100 + k) for k in range(1, 11))), sp.Rational('0.9739'), r'b_{10}\approx0{,}9739')
    a, b = sp.symbols('a b', real=True)
    l12 = L(((a - b) + 1 / n) / (sp.sqrt(1 + a / n + 1 / n ** 2) + sp.sqrt(1 + b / n)))
    c('ej-1-12', 'límite (a-b)/2', l12, (a - b) / 2, r'\frac{a-b}{1+1}=\frac{a-b}2')
    c('ej-1-12', 'ejemplo a=5, b=1', L(sp.sqrt(n ** 2 + 5 * n + 1) - sp.sqrt(n ** 2 + n)), 2, r'\boxed{a-b=4}')
    c('ej-1-13', '1^∞', L(((5 * n + 2) / (5 * n + 3)) ** (3 * n + 1)), sp.exp(-sp.Rational(3, 5)), r'\boxed{e^{-3/5}}')
    c('ej-1-14', 'base → 1/2, exponente → ∞', L(((n ** 4 - n + 1) / (2 * n ** 4 - n + 2)) ** (n ** 2 / (n + 1))), 0, r'$\lim_{n\to\infty} a_n=\boxed0$')
    c('ej-1-15', 'raíz n-ésima de n', L(n ** (1 / n)), 1, r'\lim_{n\to\infty}\sqrt[n]n=e^0=\boxed1')
    c('ej-1-15', 'Stolz: ln(1+1/n) → 0', L(sp.log(1 + 1 / n)), 0, r'\ln\!\left(1+\tfrac1n\right)\to\ln1=0')
    c('ej-1-16', 'cociente de Stolz', L((n + 2) ** (n + 1) / ((2 * n + 1) * (n + 1) ** n)), sp.E / 2, r'\boxed{\dfrac e2}')
    s100 = sum(sp.Rational(k + 1) ** k / sp.Rational(k) ** (k - 1) for k in range(1, 101)) / 100 ** 2
    c('ej-1-16', 's_100 numérico', r(s100, 5), sp.Rational('1.35967'), r's_{100}\approx1{,}35967')
    # ---- Ejemplos propios A-E
    c('ej-a1', 'P1', L((3 * n ** 2 - n + 2) / (5 * n ** 2 + 4)), sp.Rational(3, 5), r'\to\dfrac35')
    c('ej-a2', 'P2', L(sp.sqrt(9 * n ** 2 + n) / (2 * n + 1)), sp.Rational(3, 2), r'\to\dfrac32')
    c('ej-a3', 'P3', L((2 ** n + 3 ** n) / (3 ** (n + 1) + 1)), sp.Rational(1, 3), r'\dfrac{0+1}{3+0}=\dfrac13')
    c('ej-b1', 'P4', L(sp.sqrt(n ** 2 + n) - n), sp.Rational(1, 2), r'\dfrac1{\sqrt{1+1/n}+1}=\dfrac12')
    c('ej-b2', 'P5', L(sp.sqrt(n) * (sp.sqrt(n + 1) - sp.sqrt(n))), sp.Rational(1, 2), r'\lim_{n\to\infty}\sqrt n\,(\sqrt{n+1}-\sqrt n)')
    c('ej-b3', 'P6: c=10', L(sp.sqrt(n ** 2 + 10 * n) - n), 5, r'luego $c=10$')
    c('ej-b3', 'P6: segundo límite', L(sp.sqrt(n ** 2 + 3 * n) - sp.sqrt(n ** 2 - n)), 2, r'=\dfrac{3-(-1)}2=2')
    c('ej-c1', 'P7', L(sp.sin(n) / n), 0, r'\lim_{n\to\infty}\dfrac{\operatorname{sen}n}n=0')
    c('ej-c2', 'P8 cota inferior', L(n ** 2 / (n ** 2 + n)), 1, r'\frac{n^2}{n^2+n}\le b_n\le\frac{n^2}{n^2+1}')
    c('ej-c2', 'P8 cota superior', L(n ** 2 / (n ** 2 + 1)), 1, r'las dos cotas tienden a 1')
    c('ej-c3', 'P9', L(3 * 2 ** (1 / n)), 3, r'\lim_{n\to\infty}\sqrt[n]{2^n+3^n}=3')
    c('ej-d1', 'P10', L((1 + 2 / n) ** n), sp.exp(2), r'es $e^2$')
    c('ej-d2', 'P11', L(((n + 3) / (n - 1)) ** (2 * n)), sp.exp(8), r'el límite es $e^8$')
    c('ej-d3', 'P12', L(((n ** 2 + 1) / (n ** 2 - n)) ** n), sp.E, r'el límite es $e$')
    c('ej-d4', 'P13 base → 2', L(((2 * n + 1) / (n + 3)) ** n), oo, r'\left(\frac{2n+1}{n+3}\right)^n=+\infty')
    c('ej-d4', 'P13 base → 1/3', L(((n + 1) / (3 * n)) ** sp.sqrt(n)), 0, r'\left(\frac{n+1}{3n}\right)^{\sqrt n}=0')
    c('ej-e1', 'P14 (Stolz)', L((n + 1) ** 2 / ((n + 1) ** 3 - n ** 3)), sp.Rational(1, 3), r'\dfrac{(n+1)^2}{3n^2+3n+1}\to\dfrac13')
    c('ej-e1', 'P14 (suma de 1..n)', L(n * (n + 1) / 2 / n ** 2), sp.Rational(1, 2), r'\dfrac{1+2+\cdots+n}{n^2}\to\dfrac12')
    c('ej-e2', 'P15', L(sp.log(n) / sp.sqrt(n)), 0, r'\lim_{n\to\infty}\dfrac{\ln n}{\sqrt n}=0')
    c('ej-e3', 'P16 (Stolz)', L((n + 1) ** (1 / (n + 1))), 1, r'\sqrt[n+1]{n+1}\to1')
    # ---- Exámenes
    c('ex-1', '(-1)^n acotada (|a_n| ≤ 1) y sin límite', si(max(abs((-1) ** k) for k in range(1, 50)) == 1 and L((-1) ** (2 * n)) != L((-1) ** (2 * n + 1))), 1, r'Respuesta: B.')
    c('ex-2', 'cociente con raíces', L((sp.sqrt(n ** 2 + 1) - sp.sqrt(9 * n ** 2 + 2)) / (3 * n - 2 + sp.sqrt(4 * n ** 2 - 3))), -sp.Rational(2, 5), r'\frac{1-3}{3+2}=\boxed{-\tfrac25}')
    c('ex-3', 'conjugado', L(sp.sqrt(n ** 2 - 2 * n) - sp.sqrt(n ** 2 + 4)), -1, r'\frac{-2}{1+1}=\boxed{-1}')
    c('ex-4', 'cota 1/n → 0', L(1 / n), 0, r'Respuesta: B) 0.')
    c('ex-5', 'exponente y_n(x_n-1)', L(n ** 2 / (n + 2) * ((n ** 2 + n + 1) / (n ** 2 - n - 1) - 1)), 2, r'\frac{2n^3+n^2}{n^3+n^2-3n-2}\to2')
    c('ex-5', '1^∞ → e²', L(((n ** 2 + n + 1) / (n ** 2 - n - 1)) ** (n ** 2 / (n + 2))), sp.exp(2), r'\boxed{e^{2}}')
    c('ex-5', 'contraste: base → 1/16', L(((n ** 2 + 2 * n) / (16 * n ** 2 + 4 * n - 7)) ** n), 0, r'El límite es <b>0</b>')
    c('ex-6', 'a = π/3: |cos a| < 1 → 0', L(sp.cos(sp.pi / 3) ** n), 0, r'el límite es <b>0</b>')
    c('ex-6', 'a = 2π: cos a = 1 → 1', L(sp.cos(2 * sp.pi) ** n), 1, r'el límite es <b>1</b>')
    # ---- Práctica «Ahora hazlo tú» (respuesta final = «Resultado: …»)
    g1 = recurrencia(1, lambda t: sp.sqrt(2 * t + 3), 5)
    g2 = recurrencia(2, lambda t: (t + 2 / t) / 2, 4)
    P = {
        'pr-a1': (L((2 * n + 1) ** 3 / (4 * n ** 3 - n ** 2 + 7)), 2, r'Resultado: $2$'),
        'pr-a2': (L((sp.cbrt(27 * n ** 3 + n ** 2) - sp.sqrt(n)) / (sp.sqrt(n ** 2 + 1) + n)), sp.Rational(3, 2), r'Resultado: $\frac32$'),
        'pr-b1': (L(sp.sqrt(4 * n ** 2 + n) - 2 * n), sp.Rational(1, 4), r'Resultado: $\frac14$'),
        'pr-b2': (L(sp.cbrt(n ** 3 + 3 * n ** 2) - n), 1, r'Resultado: $1$'),
        'pr-c1': (L((2 * n + sp.cos(n ** 2)) / (3 * n - sp.sin(n))), sp.Rational(2, 3), r'Resultado: $\frac23$'),
        'pr-c2': (L(n * (n + 1) / 2 / (n ** 2 + 1)) + L(n * (n + 1) / 2 / (n ** 2 + n)), 1, r'Resultado: $\frac12$'),
        'pr-d1': (L(((3 * n - 1) / (3 * n + 2)) ** n), sp.exp(-1), r'Resultado: $e^{-1}=\frac1e$'),
        'pr-d2': (si([L((1 + 1 / n ** sp.Rational(1, 2)) ** n), L((1 + 1 / n) ** n), L((1 + 1 / n ** 2) ** n)] == [oo, sp.E, 1]), 1,
                  r'Resultado: $+\infty$ si $0&lt;p&lt;1$; $e$ si $p=1$; $1$ si $p&gt;1$'),
        'pr-e1': (L(2 ** (n + 1) / (2 ** (n + 1) - 2 ** n)), 2, r'Resultado: $2$'),
        'pr-e2': (L(((n + 1) ** 2 + sp.sqrt(n + 1) * n ** sp.Rational(3, 2)) / (3 * n ** 2 + 3 * n + 1)), sp.Rational(2, 3), r'Resultado: $\frac23$'),
        'pr-f1': (L((3 * n + 1) / (n + 2)) + 10 * si(sp.simplify((3 * (n + 1) + 1) / (n + 3) - (3 * n + 1) / (n + 2) - 5 / ((n + 2) * (n + 3))) == 0), 13,
                  r'Resultado: creciente, $\frac43\le a_n&lt;3$ y $\lim_{n\to\infty}a_n=3$'),
        'pr-f2': (L(n / 2 ** n), 0, r'Resultado: decreciente, $0&lt;b_n\le\frac12$ y $\lim_{n\to\infty}b_n=0$'),
        'pr-g1': (max(sp.solve(x ** 2 - 2 * x - 3, x)) + 10 * si(all(g1[k] < g1[k + 1] < 3 for k in range(4))), 13, r'Resultado: $\lim_{n\to\infty}a_n=3$'),
        'pr-g2': (max(sp.solve(x ** 2 - 2, x)) + 10 * si(g2[1:] == [sp.Rational(3, 2), sp.Rational(17, 12), sp.Rational(577, 408)]), sp.sqrt(2) + 10, r'Resultado: $\lim_{n\to\infty}a_n=\sqrt2$'),
    }
    if (EJ / 'pr-e2.html').exists():
        c('pr-e2', 'cociente de incrementos en n=1000', r(((1001) ** 2 + sp.sqrt(1001) * sp.Integer(1000) ** sp.Rational(3, 2)) / (3 * 1000 ** 2 + 3 * 1000 + 1), 4), sp.Rational('0.6668'), r'\approx0{,}6668')
    for eid, (val, esp, txt) in P.items():
        if (EJ / f'{eid}.html').exists() or (EJ / f'{eid}.solucion.html').exists():
            c(eid, 'resultado de la práctica', val, esp, txt)
