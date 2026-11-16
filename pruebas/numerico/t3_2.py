"""Tema 3.2 (series de Taylor y funciones analíticas): cada resultado se recalcula con sympy y se comprueba que la solución
de la página lo escribe.

`comprobaciones(c)`: c(ejercicio, descripción, valor_sympy, esperado, trozo_latex)
  - valor_sympy: lo que calcula sympy (límites de cocientes/raíces, coeficientes, derivadas en el centro, sumas, o 1/0 con `si`);
  - trozo_latex: cadena que debe aparecer en `ejercicios/<ejercicio>.html` (o `.solucion.html`), comparada sin etiquetas,
    espacios, \\, \\; \\! ni \\displaystyle y con \\dfrac/\\tfrac = \\frac.
Las comprobaciones de la práctica «Ahora hazlo tú» (pr-*) solo se activan cuando el ejercicio existe en `contenido/`.
"""
import pathlib

import sympy as sp

x = sp.symbols('x', real=True)
n = sp.symbols('n', positive=True, integer=True)
k = sp.symbols('k', integer=True, nonnegative=True)
sen, cos, ln, e, pi, fac = sp.sin, sp.cos, sp.log, sp.exp, sp.pi, sp.factorial
EJ = pathlib.Path(__file__).resolve().parents[2] / 'contenido' / 'tema_3_2' / 'ejercicios'


def si(cond):
    """Comprobación lógica: 1 si se cumple (se compara con esperado = 1)."""
    return sp.Integer(1 if bool(cond) else 0)


def cociente(a):
    """lim |a_{n+1}/a_n| (el radio es su inverso)."""
    return sp.limit(sp.Abs(sp.combsimp(a.subs(n, n + 1) / a)), n, sp.oo)


def serie(f, x0, orden=12):
    return sp.series(f, x, x0, orden).removeO()


def igual_serie(f, x0, g, orden=12):
    """La serie de f en x0 coincide con g (suma finita) hasta el orden dado."""
    return si(sp.expand(serie(f, x0, orden) - g) == 0)


def dn0(f, m):
    return sp.diff(f, x, m).subs(x, 0)


def comprobaciones(c):
    # ---- Ejercicios del libro (E 3.17-3.20)
    c('ej-3-17', 'radio de la serie de derivadas de sum e^{-n}x^n', 1 / cociente((n + 1) * e(-(n + 1))), sp.E, r"$R=e$")
    c('ej-3-18', '1/(1-x)^2 = sum (m+1)x^m', igual_serie(1 / (1 - x) ** 2, 0, sum((m + 1) * x ** m for m in range(12))), 1,
      r"\frac1{(1-x)^2}=\sum_{m=0}^{\infty}(m+1)x^m")
    c('ej-3-19', 'serie de e^x', igual_serie(e(x), 0, sum(x ** m / fac(m) for m in range(12))), 1,
      r"\sum_{n=0}^\infty\frac{x^n}{n!}=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots")
    kk = 3
    c('ej-3-20', '(1+x)^{-3} = sum (-1)^n C(n+2,n) x^n y radio 1',
      igual_serie((1 + x) ** -kk, 0, sum((-1) ** m * sp.binomial(kk + m - 1, m) * x ** m for m in range(12)))
      * cociente(sp.binomial(kk + n - 1, n)), 1, r"(-1)^n\binom{k+n-1}{n}x^n")
    # ---- Exámenes
    c('ex-1b', 'radio de sum e^{-n}x^n', 1 / cociente(e(-n)), sp.E, r"$R=e$")
    c('ex-1', 'radio de sum x^n/2^n', 1 / cociente(1 / 2 ** n), 2, r"R=\frac1{1/2}=2")
    c('ex-2', 'radio infinito de sum 2^n/n! (x-1/2)^n', cociente(2 ** n / fac(n)), 0, r"x_0=\frac12")
    c('ex-3', 'raíz de (1+1/n)^{2n^2} -> e^2', sp.limit((1 + 1 / n) ** (2 * n), n, sp.oo), sp.E ** 2, r"R=\frac1{e^2}")
    c('ex-4', 'cociente ln(n+2)/ln(n+1) -> 1', sp.limit(ln(n + 2) / ln(n + 1), n, sp.oo), 1, r"$(-2,0)$")
    c('ex-5', 'sum n x^{n-1} = 1/(1-x)^2 (radio 1)', cociente(n), 1, r"Respuesta C")
    c('ex-6', 'serie de e^{pi x}', igual_serie(e(pi * x), 0, sum(pi ** m * x ** m / fac(m) for m in range(12))), 1,
      r"\sum_{n=0}^\infty\frac{\pi^n}{n!}x^n")
    c('ex-7', 'p_3(1/4)=31/32 y cota 1/6144 < 0.002 < 1/384',
      serie(cos(x), 0, 4).subs(x, sp.Rational(1, 4)) + si(sp.Rational(1, 6144) < sp.Rational(2, 1000) < sp.Rational(1, 384)) - 1,
      sp.Rational(31, 32), r"\frac{31}{32}")
    c('p1', 'radio 2 de sum (x-3)^n/(n2^n)', 1 / cociente(1 / (n * 2 ** n)), 2, r"$[1,5)$")
    c('p2', 'derivada n-ésima de e^{2x} en 1 (n=5)', sp.diff(e(2 * x), x, 5).subs(x, 1), 32 * sp.E ** 2, r"f^{(n}(1)=2^ne^2")
    c('p3', 'f^{(8}(0) de x^2 cos x^3', dn0(x ** 2 * cos(x ** 3), 8), -20160, r"f^{(8}(0)=-\frac{8!}{2}=-20160")
    c('p4', 'sum n/2^n = 2', sp.summation(k / 2 ** k, (k, 1, sp.oo)), 2, r"\frac{1/2}{1/4}=2")
    # ---- Práctica «Ahora hazlo tú» (respuesta final = «Resultado: …»)
    P = {
        'pr-a1': (igual_serie(sen(x), pi, sum((-1) ** (j + 1) * (x - pi) ** (2 * j + 1) / fac(2 * j + 1) for j in range(6)))
                  * si(cociente(1 / fac(2 * n + 1)) == 0), 1,
                  r"Resultado: $\operatorname{sen}x=\sum_{n=0}^\infty\frac{(-1)^{n+1}}{(2n+1)!}(x-\pi)^{2n+1}$, con $R=\infty$"),
        'pr-a2': (igual_serie(ln(x), 1, sum((-1) ** (j + 1) * (x - 1) ** j / j for j in range(1, 12))) * cociente(1 / n), 1,
                  r"Resultado: $\ln x=\sum_{n=1}^\infty\frac{(-1)^{n+1}}{n}(x-1)^n$, con $R=1$ e intervalo de convergencia $(0,2]$"),
        'pr-b1': (igual_serie(1 / (2 - x), 0, sum(x ** j / 2 ** (j + 1) for j in range(12))) * 1 / cociente(1 / 2 ** (n + 1)), 2,
                  r"Resultado: $\frac1{2-x}=\sum_{n=0}^\infty\frac{x^n}{2^{n+1}}$ para $|x|&lt;2$ (intervalo $(-2,2)$)"),
        'pr-b2': (igual_serie(sen(x) ** 2, 0, sum((-1) ** (j + 1) * 2 ** (2 * j - 1) * x ** (2 * j) / fac(2 * j) for j in range(1, 6)))
                  * dn0(sen(x) ** 2, 4), -8,
                  r"Resultado: $\operatorname{sen}^2x=\sum_{n=1}^\infty\frac{(-1)^{n+1}2^{2n-1}}{(2n)!}x^{2n}$ para todo $x$, y $f^{(4}(0)=-8$"),
        'pr-c1': (dn0(e(x ** 2), 6) + dn0(e(x ** 2), 5), 120, r"Resultado: $f^{(5}(0)=0$ y $f^{(6}(0)=120$"),
        'pr-c2': (dn0(x ** 3 * e(x), 10) * si(all(dn0(x ** 3 * e(x), m) == m * (m - 1) * (m - 2) for m in range(3, 12))), 720,
                  r"Resultado: $f^{(n}(0)=n(n-1)(n-2)$ para $n\ge3$; $f^{(10}(0)=720$"),
        'pr-d1': (1 / cociente(n / 5 ** n), 5, r"Resultado: centro $1$, $R=5$, intervalo de convergencia $(-4,6)$"),
        'pr-d2': (1 / cociente(1 / (sp.sqrt(n) * 3 ** n)), 3, r"Resultado: centro $-1$, $R=3$, intervalo de convergencia $(-4,2]$"),
        'pr-e1': (cociente(n ** 2 / fac(n)), 0, r"Resultado: $R=\infty$ (converge para todo $x\in\mathbb R$)"),
        'pr-e2': (1 / sp.limit(n / (2 * n + 1), n, sp.oo) + si(sp.limit((2 * n / (2 * n + 1)) ** n, n, sp.oo) == e(-sp.Rational(1, 2))) - 1,
                  2, r"Resultado: $R=2$, intervalo de convergencia $(-2,2)$"),
        'pr-f1': (sp.summation(k / 3 ** (k - 1), (k, 1, sp.oo)), sp.Rational(9, 4),
                  r"Resultado: $\sum_{n=1}^\infty\frac{n}{3^{n-1}}=\frac94$"),
        'pr-f2': (sp.summation(k * (k - 1) / 2 ** k, (k, 2, sp.oo)), 4, r"Resultado: $\sum_{n=2}^\infty\frac{n(n-1)}{2^n}=4$"),
        'pr-g1': (sp.summation((-1) ** k * pi ** (2 * k) / (4 ** k * fac(2 * k)), (k, 0, sp.oo)), 0,
                  r"Resultado: la suma es $\cos\frac\pi2=0$"),
        'pr-g2': (sp.summation(1 / (k * 2 ** k), (k, 1, sp.oo)), ln(2), r"Resultado: $\sum_{n=1}^\infty\frac{1}{n\,2^n}=\ln2$"),
        'pr-h1': (sp.limit(sp.Abs(sp.Rational(7, 2)) ** (n + 1) / fac(n + 1), n, sp.oo), 0,
                  r"Resultado: $|R_n(x)|\le\frac{|x|^{n+1}}{(n+1)!}\to0$ para todo $x$, luego la serie suma $\operatorname{sen}x$ en todo $\mathbb R$"),
        'pr-h2': (sum(sp.Rational(1, fac(j)) for j in range(7)) + si(sp.Rational(3, 720) > sp.Rational(1, 1000) > sp.Rational(3, 5040)
                                                                     and sp.E - sp.Rational(1957, 720) < sp.Rational(3, 5040)) - 1,
                  sp.Rational(1957, 720),
                  r"Resultado: basta $n=6$ (siete términos): $e\approx\frac{1957}{720}\approx2{,}71806$, con error $&lt;\frac3{7!}&lt;0{,}001$"),
    }
    for eid, (val, esp, txt) in P.items():
        if (EJ / f'{eid}.html').exists() or (EJ / f'{eid}.solucion.html').exists():
            c(eid, 'resultado de la práctica', val, esp, txt)
