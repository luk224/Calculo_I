"""Tema 2.1 (la derivada): cada resultado se recalcula con sympy y se comprueba que la solución de la página lo escribe.

`comprobaciones(c)`: c(ejercicio, descripción, valor_sympy, esperado, trozo_latex)
  - valor_sympy: lo que calcula sympy;  esperado: lo que afirma la página (exacto o redondeado como en la página);
  - trozo_latex: cadena que debe aparecer en `ejercicios/<ejercicio>.html` (o `.solucion.html`), comparada sin etiquetas,
    espacios ni \\displaystyle y con \\dfrac/\\tfrac = \\frac.
Las preguntas de verdadero/falso se comprueban con su contraejemplo o su caso concreto (función `si`).
Las comprobaciones de la práctica «Ahora hazlo tú» (pr-*) solo se activan cuando el ejercicio existe en `contenido/`.
"""
import pathlib

import sympy as sp

h = sp.symbols('h', real=True)
x = sp.symbols('x', real=True)
a, b, k, m = sp.symbols('a b c m', real=True)  # k es la «c» de los enunciados
oo = sp.oo
EJ = pathlib.Path(__file__).resolve().parents[2] / 'contenido' / 'tema_2_1' / 'ejercicios'


def D(f, x0, lado=None):
    """Derivada por la definición en x0 (lado '+' o '-' para las laterales)."""
    q = (f(x0 + h) - f(x0)) / h
    return sp.limit(q, h, 0) if lado is None else sp.limit(q, h, 0, lado)


def si(cond):
    """Comprobación lógica: 1 si se cumple (se compara con esperado = 1)."""
    return sp.Integer(1 if bool(cond) else 0)


def r(v, k=2):
    """Redondeo a k decimales (como se escribe en la página)."""
    return sp.Rational(str(round(float(v), k)))


def comprobaciones(c):
    absx = lambda t: sp.Abs(t)  # noqa: E731
    # ---- Ejercicios del libro (E 2.1, 2.2, 2.6-2.9, 2.14, 2.17-2.23)
    c('ej-2-1', 'f\'(a) es un número (ej. x² en 3)', si(D(lambda t: t ** 2, 3).is_real), 1, r'<b>Respuesta: b).</b>')
    c('ej-2-2', 'velocidad media 3 km en 13/240 h', 3 / (sp.Rational(3) + sp.Rational(1, 4)) * 60, sp.Rational(720, 13), r'\dfrac{3}{13/240}=\dfrac{720}{13}')
    c('ej-2-2', 'redondeo', r(sp.Rational(720, 13)), sp.Rational('55.38'), r'\approx55{,}38')
    c('ej-2-6', 'normal ⟂ tangente', (-m) * 1 + 1 * m, 0, r"$-f'(a)+f'(a)=0$")
    f27 = -x ** 3 / 3 - x ** 2 - 1
    c('ej-2-7', 'ceros de f\'', si(set(sp.solve(sp.diff(f27, x), x)) == {0, -2}), 1, r'x=0$ o $x=-2$')
    c('ej-2-7', 'f(-2)', f27.subs(x, -2), -sp.Rational(7, 3), r'$(0,-1)$ y $\left(-2,-\frac73\right)$')
    c('ej-2-8', 'f\'(x)=1', sp.solve(sp.diff(f27, x) - 1, x)[0], -1, r'(x+1)^2=0\iff x=-1')
    c('ej-2-8', 'f(-1)', f27.subs(x, -1), -sp.Rational(5, 3), r'\left(-1,-\frac53\right)')
    c('ej-2-9', 'f\'(1/2)', (sp.sin(sp.pi * x) * sp.exp(2 * x ** 2 - x)).subs(x, sp.Rational(1, 2)), 1, r'=1\cdot e^0=1')
    c('ej-2-14', 'ejemplo f=x-1/2: L0·L1<0 y raíz en (0,1)',
      si(sp.limit(x - sp.Rational(1, 2), x, 0, '+') * sp.limit(x - sp.Rational(1, 2), x, 1, '-') < 0 and sp.solve(x - sp.Rational(1, 2), x) == [sp.Rational(1, 2)]), 1,
      r'<b>Respuesta: verdadera</b>')
    c('ej-2-17', '|x| (laterales distintas) es continua en 0', sp.limit(absx(x), x, 0), 0, r'<b>Respuesta: verdadera.</b>')
    c('ej-2-18', '|x|: laterales 1 y -1', si(D(absx, 0, '+') == 1 and D(absx, 0, '-') == -1), 1, r'<b>Respuesta: falsa.</b>')
    c('ej-2-19', 'f\'(0+)', D(absx, 0, '+'), 1, r"$f'(0^+)=1$")
    c('ej-2-19', 'f\'(0-)', D(absx, 0, '-'), -1, r"$f'(0^-)=-1$")
    c('ej-2-20', '|x³| en 0', D(lambda t: sp.Abs(t ** 3), 0), 0, r'<b>Respuesta: b).</b>')
    c('ej-2-20', '|2 sen x|: laterales ±2', si(D(lambda t: sp.Abs(2 * sp.sin(t)), 0, '+') == 2 and D(lambda t: sp.Abs(2 * sp.sin(t)), 0, '-') == -2), 1, r'=\pm2\cos0=\pm2')
    c('ej-2-20', '√|x|: lateral derecha +∞', D(lambda t: sp.sqrt(sp.Abs(t)), 0, '+'), oo, r'\frac1{\sqrt h}\to+\infty')
    c('ej-2-21', 'contraejemplo |x-2| en 1', D(lambda t: sp.Abs(t - 2), 1), -1, r"$|f|'(1)=-1$")
    c('ej-2-22', 'c) con f=x²: |f|\'(0)=0', D(lambda t: sp.Abs(t ** 2), 0), 0, r'<b>Respuesta: c).</b>')
    c('ej-2-23', 'f\'(0-)', D(lambda t: 2 * t + sp.sin(t), 0, '-'), 3, r'=2+1=3')
    c('ej-2-23', 'f\'(0+) con a=-3, b=-7π', sp.diff(sp.sin(-3 * x - 7 * sp.pi), x).subs(x, 0), 3, r'$(-1)^{-7}(-3)=3$')
    # ---- Ejemplos propios
    c('ej-a1', '√x en 4', D(sp.sqrt, 4), sp.Rational(1, 4), r'\xrightarrow[h\to0]{}\dfrac14')
    c('ej-a1', 'normal: ordenada en el origen', 2 - (-4) * 4, 18, r'$y=-4x+18$')
    sol2 = sp.solve([a + b, 2 * a + b - 1], [a, b])
    c('ej-a2', 'sistema', si(sol2 == {a: 1, b: -1} and D(sp.log, 1, '+') == 1), 1, r'$a=1$, $b=-1$')

    def malos(p):
        """Ceros del polinomio p donde p' ≠ 0: puntos donde |p| no es derivable."""
        return {z for z in sp.solve(p, x) if sp.diff(p, x).subs(x, z) != 0}
    c('ej-a3', '|x³-x|', si(malos(x ** 3 - x) == {-1, 0, 1}), 1, r'$F$ es derivable en $\mathbb R\setminus\{-1,0,1\}$')
    c('ej-a3', '|x³-x²|', si(malos(x ** 3 - x ** 2) == {1}), 1, r'$G$ es derivable en $\mathbb R\setminus\{1\}$')
    # ---- Exámenes
    tg = 1 + (x - sp.E) / sp.E
    c('ex-1', 'tangente en x=0', tg.subs(x, 0), 0, r'el punto $(0,0)$')
    c('ex-1', 'tangente simplificada y = x/e', sp.simplify(tg - x / sp.E), 0, r'=\frac xe$')
    c('ex-2', 'x²: laterales iguales y continua', si(D(lambda t: t ** 2, 0, '+') == D(lambda t: t ** 2, 0, '-') and sp.limit(x ** 2, x, 0) == 0), 1, r'es continua en $a$. Verdadera.')
    c('ex-3', '|x² sen x| en 0', D(lambda t: sp.Abs(t ** 2 * sp.sin(t)), 0), 0, r"con $f'(0)=0$")
    c('ex-3', 'cociente = h|sen h| (h<0 y h>0)', si(all(sp.simplify(sp.Abs(hv ** 2 * sp.sin(hv)) / hv - hv * sp.Abs(sp.sin(hv))) == 0 for hv in (sp.Rational(1, 3), -sp.Rational(1, 3)))), 1, r'=h\,|\operatorname{sen}h|')
    f4 = a * sp.exp(x) / (2 + x)
    c('ex-4', 'f\'(x)', sp.simplify(sp.diff(f4, x) - a * (1 + x) * sp.exp(x) / (2 + x) ** 2), 0, r'=\dfrac{a(1+x)e^x}{(2+x)^2}')
    c('ex-4', 'f\'(0)=1', sp.solve(sp.diff(f4, x).subs(x, 0) - 1, a)[0], 4, r'$a=4$')
    sol5 = sp.solve([a * sp.cos(0) - 2, sp.diff(a * sp.cos(x), x).subs(x, 0) - b], [a, b])
    c('ex-5', 'a, b', si(sol5 == {a: 2, b: 0}), 1, r'Resultado: $a=2$, $b=0$')
    c('ex-6', 'continuidad n=1', sp.limit(x * sp.sin(1 / x), x, 0), 0, r'$|f(x)|\le|x|^n$')
    c('ex-6', 'sen(1/h) toma 1 y -1 en h→0', si(sp.sin(1 / (1 / (sp.pi / 2 + 2 * 50 * sp.pi))) == 1 and sp.sin(1 / (1 / (3 * sp.pi / 2 + 2 * 50 * sp.pi))) == -1), 1, r'$\operatorname{sen}\frac1h=-1$')
    c('ex-6', 'n=2: derivable con f\'(0)=0', D(lambda t: t ** 2 * sp.sin(1 / t) if t != 0 else 0, 0), 0, r"derivable en $0$ con $f'(0)=0$")
    # ---- Práctica «Ahora hazlo tú» (respuesta final = «Resultado: …»)
    p = sp.symbols('p', positive=True)
    lat = lambda q: (sp.limit(sp.Abs(h) ** q / h, h, 0, '+'), sp.limit(sp.Abs(h) ** q / h, h, 0, '-'))  # noqa: E731
    P = {
        'pr-a1': (D(lambda t: t ** 2 - 3 * t, 2), 1, r"Resultado: $f'(2)=1$"),
        'pr-a2': (D(lambda t: 1 / sp.sqrt(t), 1), -sp.Rational(1, 2), r"Resultado: $f'(1)=-\frac12$"),
        'pr-b1': ((9 + 6 - 3) / sp.Integer(2) + 10 * D(lambda t: t ** 2 + 2 * t, 1), 46, r"Resultado: $v_m=6$ m/s y $s'(1)=4$ m/s"),
        'pr-b2': (si(sp.simplify((5 * (2 + h) ** 2 - 20) / h) == 20 + 5 * h and D(lambda t: 5 * t ** 2, 2) == 20
                     and sp.solve(5 * h - sp.Rational(1, 10), h) == [sp.Rational(1, 50)]), 1,
                  r"Resultado: $v_m=20+5h$, $s'(2)=20$ m/s; error menor que $0{,}1$ si $0&lt;h&lt;0{,}02$"),
        'pr-c1': (si((x ** 3 - 2 * x).subs(x, 1) == -1 and sp.diff(x ** 3 - 2 * x, x).subs(x, 1) == 1), 1, r'Resultado: tangente $y=x-2$; normal $y=-x$'),
        'pr-c2': (si({sp.expand(a0 ** 2 + 2 * a0 * (x - a0)) for a0 in sp.solve(a ** 2 - 2 * a - 3, a)} == {6 * x - 9, -2 * x - 1}), 1,
                  r'Resultado: $y=6x-9$ (tangente en $(3,9)$) e $y=-2x-1$ (tangente en $(-1,1)$)'),
        'pr-d1': (si({(v, (x ** 3 - 3 * x + 1).subs(x, v)) for v in sp.solve(3 * x ** 2 - 3 - 9, x)} == {(2, 3), (-2, -1)}), 1, r'Resultado: $(2,3)$ y $(-2,-1)$'),
        'pr-d2': (sp.solve(1 / x - 1, x)[0] + 10 * sp.solve(k + sp.log(1) - 1, k)[0], 11, r'Resultado: $c=1$, tangente en el punto $(1,1)$'),
        'pr-e1': (si(D(lambda t: t ** 2, 1, '-') == 2 and D(lambda t: 2 * t - 1, 1, '+') == 2), 1, r"Resultado: derivable en $1$, con $f'(1^-)=f'(1^+)=f'(1)=2$"),
        'pr-e2': (sp.limit(sp.exp(-1 / h), h, 0, '+') + sp.limit(x * sp.exp(-1 / x), x, 0, '+'), 0, r"Resultado: derivable en $0$, con $f'(0)=0$"),
        'pr-f1': (si(sp.limit((h + 1) / h, h, 0, '-') == -oo and sp.limit(h ** 2 / h, h, 0, '+') == 0), 1,
                  r"Resultado: no es derivable en $0$ (no es continua; $f'(0^-)=-\infty$, $f'(0^+)=0$)"),
        'pr-f2': (si(lat(sp.Rational(1, 2)) == (oo, -oo) and lat(1) == (1, -1) and lat(sp.Rational(3, 2)) == (0, 0) and lat(2) == (0, 0)
                     and sp.limit(sp.Abs(x) ** p, x, 0) == 0), 1,
                  r"Resultado: continua para todo $p&gt;0$; derivable en $0$ si y solo si $p&gt;1$ (y entonces $f'(0)=0$)"),
        'pr-g1': (si(sp.solve([a + b - 1, a - D(lambda t: t ** 3, 1, '+')], [a, b]) == {a: 3, b: -2}), 1, r'Resultado: $a=3$, $b=-2$'),
        'pr-g2': (si(sp.solve([1 + b + k - 2, 2 + b - sp.diff(2 / x, x).subs(x, 1)], [b, k]) == {b: -4, k: 5}
                     and sp.expand(2 + sp.diff(2 / x, x).subs(x, 1) * (x - 1)) == -2 * x + 4), 1, r'Resultado: $b=-4$, $c=5$; tangente $y=-2x+4$'),
    }
    for eid, (val, esp, txt) in P.items():
        if (EJ / f'{eid}.html').exists() or (EJ / f'{eid}.solucion.html').exists():
            c(eid, 'resultado de la práctica', val, esp, txt)
