"""Tema 2.5 (Rolle, valor medio y funciones monótonas): cada resultado se recalcula con sympy y se comprueba que la solución
de la página lo escribe.

`comprobaciones(c)`: c(ejercicio, descripción, valor_sympy, esperado, trozo_latex)
  - valor_sympy: lo que calcula sympy (diferencias que deben ser 0, el punto c pedido, o 1/0 para comprobaciones lógicas con `si`);
  - trozo_latex: cadena que debe aparecer en `ejercicios/<ejercicio>.html` (o `.solucion.html`), comparada sin etiquetas,
    espacios, \\, \; \\! ni \\displaystyle y con \\dfrac/\\tfrac = \\frac.
En los ejercicios de «elige la opción» se comprueba con sympy el contraejemplo o el dato que decide la respuesta.
Las comprobaciones de la práctica «Ahora hazlo tú» (pr-*) solo se activan cuando el ejercicio existe en `contenido/`.
"""
import pathlib

import sympy as sp

x = sp.symbols('x', real=True)
xp = sp.symbols('x', positive=True)
h = sp.symbols('h', real=True)
sen, cos, ln, e, pi = sp.sin, sp.cos, sp.log, sp.exp, sp.pi
EJ = pathlib.Path(__file__).resolve().parents[2] / 'contenido' / 'tema_2_5' / 'ejercicios'


def dif(f, g, v=x):
    """f' - g simplificado (0 si la derivada de la página es correcta)."""
    return sp.simplify(sp.diff(f, v) - g)


def si(cond):
    """Comprobación lógica: 1 si se cumple (se compara con esperado = 1)."""
    return sp.Integer(1 if bool(cond) else 0)


def ceros(f, a, b):
    """Ceros de f en el abierto (a, b)."""
    return sp.solveset(f, x, sp.Interval.open(a, b))


def comprobaciones(c):
    # ---- Ejercicios del libro (E 2.39-2.51)
    c('ej-2-39', 'Rolle con 1-x² en [-1,1]: c=0', si(ceros(sp.diff(1 - x ** 2, x), -1, 1) == sp.FiniteSet(0)), 1,
      r"Respuesta: b).")
    r40 = ceros(sp.diff(x * (x - 1) * (x + 2), x), -2, 1)
    c('ej-2-40', 'tangentes horizontales de x(x-1)(x+2)',
      si(r40 == sp.FiniteSet((-1 - sp.sqrt(7)) / 3, (-1 + sp.sqrt(7)) / 3)), 1, r"x=\frac{-1\pm\sqrt7}{3}")
    c('ej-2-41', 'f=-x: pendiente de la cuerda en [0,1]', (-1) - 0, -1, r"$f(x)=-x$")
    f42 = sp.Abs(x - sp.Rational(1, 2))
    c('ej-2-42', '|x-1/2|: f(1)-f(0)=0', f42.subs(x, 1) - f42.subs(x, 0), 0,
      r"f(1)-f(0)=\tfrac12-\tfrac12=0")
    c('ej-2-43', 'x·x no es creciente', si((-1) ** 2 > 0 ** 2), 1, r"$(-1)^2&gt;0^2$")
    c('ej-2-44', '-cos x: f(0)<f(π)', si(-cos(0) < -cos(pi)) + sp.simplify(sp.diff(-cos(x), x) - sen(x)), 1,
      r"f(0)=-1\lt1=f(\pi)")
    ch, sh = (e(x) + e(-x)) / 2, (e(x) - e(-x)) / 2
    c('ej-2-45', 'cosh²-senh²=1', sp.simplify(ch ** 2 - sh ** 2), 1, r"g(0)=1^2-0^2=1")
    c('ej-2-46', 'sen(πx) > 0 en (0,1) y < 0 en (1,2)',
      si(sen(pi * sp.Rational(1, 2)) > 0 and sen(pi * sp.Rational(3, 2)) < 0), 1, r"Respuesta: d).")
    c('ej-2-47', 'mínimo de ln(x²+2) = ln 2 > 0', sp.minimum(ln(x ** 2 + 2), x), ln(2), r"\ln(x^2+2)\ge\ln2")
    c('ej-2-48', 'f\' de e^{2x²-x}', dif(e(2 * x ** 2 - x), e(2 * x ** 2 - x) * (4 * x - 1)), 0,
      r"f'(x)=e^{2x^2-x}(4x-1)")
    c('ej-2-49', 'límite por la izquierda en 1', sp.limit(x - 2, x, 1, '-'), -1, r"\lim_{x\to1^-}(x-2)=-1")
    c('ej-2-50', '(x³+1)/x = x²+1/x', sp.simplify((x ** 3 + 1) / x - (x ** 2 + 1 / x)), 0,
      r"f(x)=x^2+\dfrac1x")
    c('ej-2-51', 'ceros de cos x + cos 2x en (0,2π)',
      si(ceros(cos(x) + cos(2 * x), 0, 2 * pi) == sp.FiniteSet(pi / 3, pi, 5 * pi / 3)), 1,
      r"x\in\{\tfrac\pi3,\pi,\tfrac{5\pi}3\}")
    # ---- Exámenes
    c('ex-1', 'TVM con x³ en [0,3] (ejemplo): c=√3',
      list(ceros(sp.diff(x ** 3, x) - sp.Integer(27 - 0) / 3, 0, 3))[0], sp.sqrt(3), r"f'(c)=\dfrac{f(b)-f(a)}{b-a}")
    f2 = e((x + 1) ** 2)
    c('ex-2', 'f(-2)=f(0)=e y c=-1',
      list(ceros(sp.diff(f2, x), -2, 0))[0] + (f2.subs(x, -2) - sp.E) + (f2.subs(x, 0) - sp.E), -1, r"f(-2)=e^{(-1)^2}=e")
    c('ex-3', 'f\' de x²e^{1-x}', dif(x ** 2 * e(1 - x), x * (2 - x) * e(1 - x)), 0,
      r"f'(x)=x(2-x)\,e^{1-x}")
    c('ex-4', 'f\' de x³e^x', dif(x ** 3 * e(x), x ** 2 * (x + 3) * e(x)), 0, r"x^2(x+3)\,e^x")
    p5 = sp.Rational(3, 2) * (5 * x ** 3 - 3 * x)
    c('ex-5', 'p(-1)=-3, p(1)=3 y tres ceros',
      si(p5.subs(x, -1) == -3 and p5.subs(x, 1) == 3 and sp.solveset(p5, x, sp.S.Reals)
         == sp.FiniteSet(0, sp.sqrt(sp.Rational(3, 5)), -sp.sqrt(sp.Rational(3, 5)))), 1, r"p(x)=\tfrac32(5x^3-3x)")
    f6 = e(x) - x - 2
    c('ex-6', 'f(1)=e-3<0, f(2)=e²-4>0', si(f6.subs(x, 1) < 0 and f6.subs(x, 2) > 0), 1, r"f(1)=e-3\lt0")
    c('ex-6', 'raíz en [1,2] ≈ 1,146', sp.Rational(str(round(float(sp.nsolve(f6, x, 1.1)), 3))),
      sp.Rational(1146, 1000), r"f'(x)=e^x-1")
    # ---- Práctica «Ahora hazlo tú» (respuesta final = «Resultado: …»)
    fa1 = sen(x) + cos(x)
    pb2 = x ** 3 - 12 * x + 1
    fe2 = ln(xp) / xp
    F = sp.atan(x) + sp.atan(1 / x)
    H = sen(x) - x + x ** 3 / 6
    P = {
        'pr-a1': (list(ceros(sp.diff(fa1, x), 0, pi / 2))[0] + (fa1.subs(x, 0) - fa1.subs(x, pi / 2)), pi / 4,
                  r"Resultado: $c=\frac\pi4$"),
        'pr-a2': (si(sp.limit(sp.cbrt(h ** 2) / h, h, 0, '+') == sp.oo and not sp.solve(sp.diff(xp ** sp.Rational(2, 3), xp), xp)), 1,
                  r"Resultado: $f(-1)=f(1)=1$ pero no existe $c$ con $f'(c)=0$: falla la derivabilidad en $x=0$"),
        'pr-b1': (si(len(sp.real_roots(x ** 5 + x - 1)) == 1 and 0 < float(sp.real_roots(x ** 5 + x - 1)[0]) < 1), 1,
                  r"Resultado: exactamente una raíz real, en $(0,1)$ ($\approx0{,}755$)"),
        'pr-b2': (si([sp.sign(pb2.subs(x, v)) for v in (-4, -3, 0, 1, 4)] == [-1, 1, 1, -1, 1] and len(sp.real_roots(pb2)) == 3), 1,
                  r"Resultado: exactamente tres raíces reales, en $(-4,-3)$, $(0,1)$ y $(1,4)$"),
        'pr-c1': (list(ceros(3 * x ** 2 - 9, 0, 3))[0], sp.sqrt(3), r"Resultado: $c=\sqrt3$"),
        'pr-c2': (sp.solve(sp.Eq(1 / (2 * sp.sqrt(xp)), sp.Rational(1, 2)), xp)[0], 1, r"Resultado: $c=1$"),
        'pr-d1': (si(10 < sp.sqrt(101) < sp.Rational(201, 20)), 1, r"Resultado: $10&lt;\sqrt{101}&lt;10{,}05$"),
        'pr-d2': (si(all(sp.Rational(1, n + 1) < ln(1 + sp.Rational(1, n)) < sp.Rational(1, n) for n in range(1, 30))), 1,
                  r"Resultado: $\dfrac{b-a}{b}&lt;\ln\dfrac ba&lt;\dfrac{b-a}{a}$; con $b=n+1$, $a=n$: "
                  r"$\dfrac1{n+1}&lt;\ln\left(1+\dfrac1n\right)&lt;\dfrac1n$"),
        'pr-e1': (si(sp.factor(sp.diff(x ** 4 - 8 * x ** 2, x)) == 4 * x * (x - 2) * (x + 2)
                     and [sp.sign(sp.diff(x ** 4 - 8 * x ** 2, x).subs(x, v)) for v in (-3, -1, 1, 3)] == [-1, 1, -1, 1]), 1,
                  r"Resultado: decreciente en $(-\infty,-2)$ y $(0,2)$; creciente en $(-2,0)$ y $(2,+\infty)$"),
        'pr-e2': (dif(fe2, (1 - ln(xp)) / xp ** 2, xp) + si(sp.pi ** sp.E < sp.E ** sp.pi), 1,
                  r"Resultado: crece en $(0,e)$, decrece en $(e,+\infty)$; $\pi^e&lt;e^\pi$"),
        'pr-f1': (sp.minimum(e(x) - 1 - x, x), 0,
                  r"Resultado: $e^x\ge1+x$ para todo $x\in\mathbb R$, con igualdad solo en $x=0$"),
        'pr-f2': (sp.simplify(sp.diff(H, x, 2) - (x - sen(x))) + si(all(H.subs(x, sp.Rational(k, 4)) > 0 for k in range(1, 60))), 1,
                  r"Resultado: $\operatorname{sen}x&gt;x-\dfrac{x^3}6$ para todo $x&gt;0$"),
        'pr-g1': (sp.simplify(sp.diff(F, x)) + F.subs(x, 1) - F.subs(x, -1), pi,
                  r"Resultado: $\operatorname{arctg}x+\operatorname{arctg}\dfrac1x=\dfrac\pi2$ si $x&gt;0$ (y $-\dfrac\pi2$ si $x&lt;0$)"),
        'pr-g2': (sp.simplify(sp.diff(3 * e(x ** 2), x) - 2 * x * 3 * e(x ** 2)) + 3 * e(0), 3, r"Resultado: $f(x)=3e^{x^2}$"),
    }
    for eid, (val, esp, txt) in P.items():
        if (EJ / f'{eid}.html').exists() or (EJ / f'{eid}.solucion.html').exists():
            c(eid, 'resultado de la práctica', val, esp, txt)
