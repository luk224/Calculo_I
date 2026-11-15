"""Tema 1.1 (el espacio ℝ): cada resultado se recalcula con sympy y se comprueba que la solución de la página lo escribe.

`comprobaciones(c)`: c(ejercicio, descripción, valor_sympy, esperado, trozo_latex)
  - valor_sympy: lo que calcula sympy;  esperado: lo que afirma la página;
  - trozo_latex: cadena que debe aparecer en `ejercicios/<ejercicio>.html` (o `.solucion.html`), comparada sin etiquetas,
    espacios ni \\displaystyle y con \\dfrac/\\tfrac = \\frac (los «<» van como `&lt;`, igual que en el HTML).
Las comprobaciones de la práctica «Ahora hazlo tú» (pr-*) solo se activan cuando el ejercicio existe en `contenido/`.
"""
import pathlib

import sympy as sp

x = sp.symbols('x', real=True)
n = sp.symbols('n', positive=True, integer=True)
oo = sp.oo
R = sp.Rational
Iv = sp.Interval
EJ = pathlib.Path(__file__).resolve().parents[2] / 'contenido' / 'tema_1_1' / 'ejercicios'


def si(cond):
    """Comprobación lógica: 1 si se cumple (se compara con esperado = 1)."""
    return sp.Integer(1 if bool(cond) else 0)


def sol(desig):
    """Conjunto solución real de una desigualdad en x."""
    return sp.solve_univariate_inequality(desig, x, relational=False)


def dominio(f):
    return sp.calculus.util.continuous_domain(f, x, sp.S.Reals)


def comprobaciones(c):
    # ---- Ejercicios del libro (E 1.1-1.5)
    c('ej-1-1', 'I2 = (-1,7)', si(sol(sp.Abs(x - 3) < 4) == Iv.open(-1, 7)), 1, r'I_2=(-1,7)')
    c('ej-1-1', 'centro de I1', R(-3 + 5, 2), 1, r'$c_1=\frac{-3+5}2=1$')
    c('ej-1-1', 'mismo radio', si(R(5 - (-3), 2) == 4), 1, r'Respuesta: a) y b).')
    y0, x0 = -6, -5
    c('ej-1-2', 'contraejemplo', si(abs(x0) < abs(y0) and not abs(x0) < abs(y0 + 4)), 1, r'$y=-6$, $x=-5$')
    c('ej-1-2', '|y|≤|y+4| ⇔ y≥-2', si(sol(sp.Abs(x) <= sp.Abs(x + 4)) == Iv(-2, oo)), 1, r'y\ge-2')
    A3 = sp.Union(Iv.open(-1, 0), Iv.open(0, 1))
    c('ej-1-3', 'A = (-1,0)∪(0,1)', si(sol(x ** 2 < 1).intersect(sol(x ** 2 > 0)) == A3), 1, r'A=(-1,0)\cup(0,1)')
    c('ej-1-3', 'sup A', A3.sup, 1, r'Respuesta: c).')
    c('ej-1-4', 'inf 1/n', sp.limit(1 / n, n, oo), 0, r'$\inf S=0\notin S$')
    c('ej-1-4', 'sup = 1', max(R(1, k) for k in range(1, 50)), 1, r'$\sup S=1\in S$ (máximo)')
    Cs = [1 / (1 / R(a) + 1 / R(b)) for a in (2, 4) for b in (1, 7)]
    c('ej-1-5', 'mínimo de C', min(Cs), R(2, 3), r'\frac23\ \mu F\le C\le\frac{28}{11}')
    c('ej-1-5', 'máximo de C', max(Cs), R(28, 11), r'\frac1C=\frac14+\frac17=\frac{11}{28}')
    # ---- Ejemplos propios
    c('ej-a1', '|2x-5|≤3', si(sol(sp.Abs(2 * x - 5) <= 3) == Iv(1, 4)), 1, r'=[1,4]$, con centro $\tfrac52$ y radio $\tfrac32$')
    c('ej-a1', '(-7,3) con |·|', si(sol(sp.Abs(x + 2) < 5) == Iv.open(-7, 3)), 1, r'(-7,3)=\{x:\ |x+2|&lt;5\}')
    c('ej-a2', 'suma de |·|', si(sol(sp.Abs(x - 1) + sp.Abs(x + 2) < 5) == Iv.open(-3, 2)), 1, r'$A=(-3,2)$')
    b = (2 * n - 1) / (n + 1)
    c('ej-a3', 'sup = límite', sp.limit(b, n, oo), 2, r'$\sup B=2$')
    c('ej-a3', 'crecimiento', sp.simplify(b.subs(n, n + 1) - b), 3 / ((n + 1) * (n + 2)), r'b_{n+1}-b_n=\frac3{(n+1)(n+2)}')
    c('ej-a3', 'b_300', b.subs(n, 300), R(599, 301), r'b_{300}=\frac{599}{301}')
    # ---- Exámenes
    c('ex-1', 'A = [0,1)', si(sol(x ** 3 >= 0).intersect(sol(x ** 3 < 1)) == Iv.Ropen(0, 1)), 1, r'A=[0,1)')
    c('ex-2', 'A = (-1,0)∪(0,1)', si(sol(x ** 2 < 1).intersect(sol(x ** 2 > 0)) == A3), 1, r'$A=(-1,0)\cup(0,1)$')
    c('ex-2', 'variante |x|≤1', si(sol(sp.Abs(x) <= 1) == Iv(-1, 1)), 1, r'$A=[-1,1]$')
    c('ex-3', 'A = (0,∞)', si(sol(sp.exp(-x) < 1) == Iv.open(0, oo)), 1, r'A=(0,+\infty)')
    c('ex-4', 'dominio √(2x²-6)', si(dominio(sp.sqrt(2 * x ** 2 - 6)) == sp.Union(Iv(-oo, -sp.sqrt(3)), Iv(sp.sqrt(3), oo))), 1, r'(-\infty,-\sqrt3]\cup[\sqrt3,+\infty)')
    c('ex-5', 'dominio √((2-x)/(x+1)²)', si(dominio(sp.sqrt((2 - x) / (x + 1) ** 2)) == sp.Union(Iv.open(-oo, -1), Iv.Lopen(-1, 2))), 1, r'(-\infty,-1)\cup(-1,2]')
    # ---- Práctica «Ahora hazlo tú» (respuesta final = «Resultado: …»)
    I, J = sol(sp.Abs(x + 1) < 3), sol(sp.Abs(x - 2) <= 2)
    E = (x + 1) / (x + 3)
    f2 = [(-1) ** k + R(1, k) for k in range(1, 200)]
    P = {
        'pr-a1': (si(I.intersect(J) == Iv.Ropen(0, 2) and I.union(J) == Iv.Lopen(-4, 4)), 1,
                  r'Resultado: $I\cap J=[0,2)$ (centro $1$, radio $1$) e $I\cup J=(-4,4]$'),
        'pr-a2': (si(min(3 - 1, 6 - 3) == 2 and max(3 - 1, 6 - 3) == 3), 1, r'Resultado: (a) $r=2$; (b) $R=3$'),
        'pr-b1': (si(sol(sp.Abs(x - 2) < sp.Abs(x + 4)) == Iv.open(-1, oo)), 1, r'Resultado: $(-1,+\infty)$'),
        'pr-b2': (si(sol(sp.Abs(x ** 2 - 4) < 3) == sp.Union(Iv.open(-sp.sqrt(7), -1), Iv.open(1, sp.sqrt(7)))), 1,
                  r'Resultado: $(-\sqrt7,-1)\cup(1,\sqrt7)$'),
        'pr-c1': (si(dominio(sp.sqrt((x + 3) / (x - 1))) == sp.Union(Iv(-oo, -3), Iv.open(1, oo))), 1,
                  r'Resultado: $\operatorname{Dom}f=(-\infty,-3]\cup(1,+\infty)$'),
        'pr-c2': (si(sol(3 / (x - 1) >= x + 1) == sp.Union(Iv(-oo, -2), Iv.Lopen(1, 2))), 1, r'Resultado: $(-\infty,-2]\cup(1,2]$'),
        'pr-d1': (si(-1 < 2 and not (R(1, -1) > R(1, 2))), 1, r'Resultado: (a) sí; (b) no (contraejemplo $x=-1$, $y=2$)'),
        'pr-d2': (sp.maximum(sp.Abs(x ** 2 - 1), x, Iv(R(1, 2), R(3, 2))), R(5, 4), r'Resultado: sí; de hecho $|x^2-1|&lt;\frac54$'),
        'pr-e1': (si((sol(sp.Abs(x - 1) < 2).union(sp.FiniteSet(4))).sup == 4 and sol(sp.Abs(x - 1) < 2).inf == -1), 1,
                  r'Resultado: $\sup A=\max A=4$; $\inf A=-1$, sin mínimo'),
        'pr-e2': (si(sol(x ** 3 < x) == sp.Union(Iv.open(-oo, -1), Iv.open(0, 1))), 1,
                  r'Resultado: $A=(-\infty,-1)\cup(0,1)$; $\sup A=1$ (sin máximo)'),
        'pr-f1': (sp.limit(1 + 3 / n, n, oo) + 10 * (1 + R(3, 1)), 1 + 40, r'Resultado: $\sup B=\max B=4$; $\inf B=1$, sin mínimo'),
        'pr-f2': (max(f2), R(3, 2), r'Resultado: $\sup C=\max C=\frac32$; $\inf C=-1$, sin mínimo'),
        'pr-g1': (si(min(a - 2 * bb for a in (1, 3) for bb in (-2, 1)) == -1 and max(a - 2 * bb for a in (1, 3) for bb in (-2, 1)) == 7), 1,
                  r'Resultado: $-1\le z\le7$, con mínimo $-1$ y máximo $7$'),
        'pr-g2': (sp.minimum(E, x, Iv(0, 2)) + 10 * sp.maximum(E, x, Iv(0, 2)), R(1, 3) + 6, r'Resultado: (a) $\frac15\le E\le1$ (no óptimas); (b) $\min E=\frac13$, $\max E=\frac35$'),
    }
    for eid, (val, esp, txt) in P.items():
        if (EJ / f'{eid}.html').exists() or (EJ / f'{eid}.solucion.html').exists():
            c(eid, 'resultado de la práctica', val, esp, txt)
