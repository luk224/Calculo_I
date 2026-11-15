"""Tema 2.2 (reglas de derivación): cada derivada se recalcula con sympy y se comprueba que la solución de la página la escribe.

`comprobaciones(c)`: c(ejercicio, descripción, valor_sympy, esperado, trozo_latex)
  - valor_sympy: lo que calcula sympy (normalmente la diferencia entre la derivada de sympy y la de la página, que debe ser 0,
    o el valor numérico pedido);  esperado: lo que afirma la página;
  - trozo_latex: cadena que debe aparecer en `ejercicios/<ejercicio>.html` (o `.solucion.html`), comparada sin etiquetas,
    espacios, \\, \\; \\! ni \\displaystyle y con \\dfrac/\\tfrac = \\frac.
Con funciones «desconocidas» (f, g dadas solo por sus datos en un punto) se usa una función concreta que cumple esos datos:
la cadena solo depende de ellos.
Las comprobaciones de la práctica «Ahora hazlo tú» (pr-*) solo se activan cuando el ejercicio existe en `contenido/`.
"""
import pathlib

import sympy as sp

x = sp.symbols('x', real=True)
xp = sp.symbols('x', positive=True)
h = sp.symbols('h', real=True)
a = sp.symbols('a', positive=True)
sen, cos, tg, ln, e = sp.sin, sp.cos, sp.tan, sp.log, sp.exp
EJ = pathlib.Path(__file__).resolve().parents[2] / 'contenido' / 'tema_2_2' / 'ejercicios'


def dif(f, g, v=x):
    """f' - g simplificado (0 si la derivada de la página es correcta)."""
    return sp.simplify(sp.diff(f, v) - g)


def num(f, g, v, pts):
    """Máximo de |f' - g| en unos puntos (para expresiones con raíces que sympy no simplifica); se redondea a 10 decimales."""
    d = sp.diff(f, v)
    return sp.Rational(str(round(max(abs(float((d - g).subs(v, p))) for p in pts), 10)))


def si(cond):
    """Comprobación lógica: 1 si se cumple (se compara con esperado = 1)."""
    return sp.Integer(1 if bool(cond) else 0)


def comprobaciones(c):
    # ---- Ejercicios del libro (E 2.3-2.5, 2.10-2.13, 2.15, 2.16)
    c('ej-2-3', '(sen x cos x)\' = cos 2x', dif(sen(x) * cos(x), cos(2 * x)), 0,
      r"f'(x)=\cos^2x-\operatorname{sen}^2x=\cos2x")
    c('ej-2-3', '(sec x)\' = sec x tg x', dif(1 / cos(x), tg(x) / cos(x)), 0,
      r"g'(x)=\sec x\operatorname{tg}x")
    c('ej-2-4', 'sen((1+cos x)^2)', dif(sen((1 + cos(x)) ** 2), -2 * sen(x) * (1 + cos(x)) * cos((1 + cos(x)) ** 2)), 0,
      r"h'(x)=-2\operatorname{sen}x(1+\cos x)\cos\big((1+\cos x)^2\big)")
    G = e(x ** 2) + (x + 1) * ln(x ** 2)
    c('ej-2-5', 'sen(e^{x²}+(x+1)ln x²)', dif(sen(G), cos(G) * (2 * x * e(x ** 2) + ln(x ** 2) + 2 + 2 / x)), 0,
      r"\Big(2xe^{x^2}+\ln x^2+2+\frac2x\Big)")
    c('ej-2-10', 'g\' = e^{x/(x+1)}/(x+1)²', dif(e(x / (x + 1)), e(x / (x + 1)) / (x + 1) ** 2), 0,
      r"=\frac{e^{\frac x{x+1}}}{(x+1)^2}")
    c('ej-2-10', 'f\' (x>0)', dif(sp.sqrt(2 + sp.cbrt(xp)), 1 / (6 * sp.sqrt(2 + sp.cbrt(xp)) * sp.cbrt(xp ** 2)), xp), 0,
      r"\operatorname{dom}f'=(-8,0)\cup(0,+\infty)")
    c('ej-2-11', 'cotg x³', dif(sp.cot(x ** 3), -3 * x ** 2 / sen(x ** 3) ** 2), 0, r"Correcta: a).")
    gg = lambda t: 3 * t  # noqa: E731  (cualquier g con g'(2)=3)
    c('ej-2-12', 'f\'(1) = 6a', sp.diff(gg(2 * xp ** a), xp).subs(xp, 1), 6 * a, r"$f'(1)=6a$")
    c('ej-2-13', 'arccos √x', num(sp.acos(sp.sqrt(xp)), -1 / (2 * sp.sqrt(xp - xp ** 2)), xp,
                                                         [sp.Rational(k, 10) for k in range(1, 10)]), 0,
      r"f'(x)=\frac{-1}{2\sqrt{x-x^2}}")
    f15 = x ** 5 + x ** 3 + x
    c('ej-2-15', 'f(1)=3, 1/f\'(1)', 1 / sp.diff(f15, x).subs(x, 1) + (f15.subs(x, 1) - 3), sp.Rational(1, 9),
      r"=\frac1{f'(1)}=\frac1{5+3+1}=\frac19")
    c('ej-2-16', 'x^{1/x}', dif(xp ** (1 / xp), xp ** (1 / xp) * (1 - ln(xp)) / xp ** 2, xp), 0,
      r"f'(x)=x^{1/x}\frac{1-\ln x}{x^2}")
    # ---- Exámenes
    c('ex-1', 'x² e^{cos x}', dif(x ** 2 * e(cos(x)), e(cos(x)) * (2 * x - x ** 2 * sen(x))), 0,
      r"f'(x)=e^{\cos x}\bigl(2x-x^2\operatorname{sen}x\bigr)")
    c('ex-2', 'sen[cos²(2/x)]', dif(sen(cos(2 / x) ** 2), 4 / x ** 2 * cos(2 / x) * sen(2 / x) * cos(cos(2 / x) ** 2)), 0,
      r"f'(x)=\frac{4}{x^2}\cos\frac2x\operatorname{sen}\frac2x\cos\Bigl[\cos^2\frac2x\Bigr]")
    c('ex-3', 'arctg√(x²-1) - sen² 3x (x>1)',
      num(sp.atan(sp.sqrt(xp ** 2 - 1)) - sen(3 * xp) ** 2, 1 / (xp * sp.sqrt(xp ** 2 - 1)) - 6 * sen(3 * xp) * cos(3 * xp), xp,
          [sp.Rational(k, 4) for k in range(5, 20)]), 0,
      r"f'(x)=\frac{1}{x\sqrt{x^2-1}}-6\operatorname{sen}3x\cos3x")
    f4 = lambda t: sp.pi + 3 * (t - 2)  # noqa: E731  (f(2)=π, f'(2)=3)
    c('ex-4', 'g\'(√2)', sp.diff(sen(f4(5 * x ** 2 - 8)), x).subs(x, sp.sqrt(2)), -30 * sp.sqrt(2),
      r"g'(\sqrt2)=-30\sqrt2")
    G5 = sp.symbols('G')
    c('ex-5', '2 = -1 + 2g\'(2)', sp.solve(sp.Eq(2, -1 + 2 * G5), G5)[0], sp.Rational(3, 2),
      r"g'(2)=\frac32")
    c('ex-6', 'f\'\'', sp.simplify(sp.diff(1 / (x ** 2 + 2 * x + 1) + cos(e(x)), x, 2)
                                                         - (6 / (x + 1) ** 4 - e(x) * sen(e(x)) - e(2 * x) * cos(e(x)))), 0,
      r"f''(x)=\frac{6}{(x+1)^4}-e^x\operatorname{sen}(e^x)-e^{2x}\cos(e^x)")
    # ---- Práctica «Ahora hazlo tú» (respuesta final = «Resultado: …»)
    fd2 = x + e(x)
    fe2 = ln(xp) ** xp
    P = {
        'pr-a1': (dif((x ** 2 + 1) / (x - 2), (x ** 2 - 4 * x - 1) / (x - 2) ** 2), 0,
                  r"Resultado: $f'(x)=\dfrac{x^2-4x-1}{(x-2)^2}$, $x\neq2$"),
        'pr-a2': (dif(x * e(x) / (x + 1), e(x) * (x ** 2 + x + 1) / (x + 1) ** 2), 0,
                  r"Resultado: $f'(x)=\dfrac{e^x(x^2+x+1)}{(x+1)^2}$, $x\neq-1$"),
        'pr-b1': (dif(sp.sqrt(x ** 2 + 4 * x + 5), (x + 2) / sp.sqrt(x ** 2 + 4 * x + 5)), 0,
                  r"Resultado: $f'(x)=\dfrac{x+2}{\sqrt{x^2+4x+5}}$ en todo $\mathbb R$"),
        'pr-b2': (dif(ln(cos(3 * x) ** 2), -6 * tg(3 * x)), 0, r"Resultado: $f'(x)=-6\operatorname{tg}3x$, para $\cos3x\neq0$"),
        'pr-c1': (dif(x * tg(x), tg(x) + x / cos(x) ** 2), 0, r"Resultado: $f'(x)=\operatorname{tg}x+\dfrac{x}{\cos^2x}$"),
        'pr-c2': (dif(sp.sec(x) ** 2 - tg(x) ** 2, 0), 0, r"Resultado: $f'(x)=0$ (la función es constante, $f(x)=1$)"),
        'pr-d1': (dif(sp.asin(2 * x), 2 / sp.sqrt(1 - 4 * x ** 2)), 0,
                  r"Resultado: $\operatorname{dom}f=\left[-\frac12,\frac12\right]$; $f'(x)=\dfrac{2}{\sqrt{1-4x^2}}$ en $\left(-\frac12,\frac12\right)$"),
        'pr-d2': (1 / sp.diff(fd2, x).subs(x, 0) + (fd2.subs(x, 0) - 1), sp.Rational(1, 2), r"Resultado: $(f^{-1})'(1)=\frac12$"),
        'pr-e1': (dif(xp ** sen(xp), xp ** sen(xp) * (cos(xp) * ln(xp) + sen(xp) / xp), xp), 0,
                  r"Resultado: $f'(x)=x^{\operatorname{sen}x}\left(\cos x\ln x+\dfrac{\operatorname{sen}x}{x}\right)$"),
        'pr-e2': (dif(fe2, fe2 * (ln(ln(xp)) + 1 / ln(xp)), xp) + sp.diff(fe2, xp).subs(xp, sp.E), 1,
                  r"Resultado: $f'(x)=(\ln x)^x\left(\ln(\ln x)+\dfrac1{\ln x}\right)$; $f'(e)=1$"),
        'pr-f1': (sp.diff(4 * (x ** 2 + 1), x).subs(x, 2), 16, r"Resultado: $h'(2)=16$"),
        'pr-f2': (sp.diff(ln(2 + 3 * (e(x) - 1)), x).subs(x, 0), sp.Rational(3, 2), r"Resultado: $h'(0)=\frac32$"),
        'pr-g1': (sp.limit(sp.cbrt(h) / h, h, 0, '+'), sp.oo,
                  r"Resultado: $f'(x)=\dfrac1{3\sqrt[3]{(x-1)^2}}$ para $x\neq1$; no es derivable en $x=1$"),
        'pr-g2': (sp.limit(sp.Abs(h) ** sp.Rational(4, 3) / h, h, 0, '+') + sp.limit(sp.Abs(h) ** sp.Rational(4, 3) / h, h, 0, '-')
                  + dif(xp ** sp.Rational(4, 3), sp.Rational(4, 3) * sp.cbrt(xp), xp), 0,
                  r"Resultado: sí es derivable en $0$, con $f'(0)=0$; $f'(x)=\frac43\sqrt[3]x$ en todo $\mathbb R$"),
    }
    for eid, (val, esp, txt) in P.items():
        if (EJ / f'{eid}.html').exists() or (EJ / f'{eid}.solucion.html').exists():
            c(eid, 'resultado de la práctica', val, esp, txt)
