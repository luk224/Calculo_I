"""Tema 1.4 (límites y continuidad): cada resultado se recalcula con sympy y se comprueba que la solución de la página lo escribe.

`comprobaciones(c)`: c(ejercicio, descripción, valor_sympy, esperado, trozo_latex)
  - valor_sympy: lo que calcula sympy;  esperado: lo que afirma la página (exacto o redondeado como en la página);
  - trozo_latex: cadena que debe aparecer en `ejercicios/<ejercicio>.html` (o `.solucion.html`), comparada sin etiquetas,
    espacios ni \\displaystyle y con \\dfrac/\\tfrac = \\frac.
Las comprobaciones de la práctica «Ahora hazlo tú» (pr-*) solo se activan cuando el ejercicio existe en `contenido/`.
"""
import pathlib

import sympy as sp

x = sp.symbols('x', real=True)
xp = sp.symbols('x', positive=True)
oo = sp.oo
EJ = pathlib.Path(__file__).resolve().parents[2] / 'contenido' / 'tema_1_4' / 'ejercicios'


def L(f, v, p, dir='+-'):
    return sp.limit(f, v, p, dir)


def si(cond):
    """Comprobación lógica: 1 si se cumple (se compara con esperado = 1)."""
    return sp.Integer(1 if bool(cond) else 0)


def r(v, k=4):
    """Redondeo a k decimales (como se escribe en la página)."""
    return sp.Rational(str(round(float(v), k)))


def raiz(f, x0):
    return sp.nsolve(f, x, x0)


def biseccion(f, a, b, n):
    """Puntos medios c_1..c_n del método de bisección (exactos)."""
    a, b, cs = sp.nsimplify(a), sp.nsimplify(b), []
    for _ in range(n):
        c = (a + b) / 2
        cs.append(c)
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return cs


def iteraciones(longitud, eps):
    """Menor n con longitud/2^n < eps."""
    n = 0
    while sp.nsimplify(longitud) / 2 ** n >= sp.nsimplify(eps):
        n += 1
    return n


def comprobaciones(c):
    # ---- Ejercicios del libro (E 1.23-1.41)
    c('ej-1-23', 'cos x/x en 0+', L(sp.cos(x) / x, x, 0, '+'), oo, r'\lim_{x\to0^+}\frac{\cos x}x=+\infty')
    c('ej-1-23', 'cos x/x en 0-', L(sp.cos(x) / x, x, 0, '-'), -oo, r'\lim_{x\to0^-}\frac{\cos x}x=-\infty')
    c('ej-1-24', '0/0 polinomios', L((x ** 2 - x) / (x ** 2 + 2 * x - 3), x, 1), sp.Rational(1, 4), r'\lim_{x\to1}f(x)=\frac1{1+3}=\frac14')
    dom = sp.calculus.util.continuous_domain(sp.sin(sp.sqrt(x / (x - 1) ** 6)), x, sp.S.Reals)
    c('ej-1-25', 'dominio [0,1)∪(1,∞)', si(dom == sp.Union(sp.Interval.Ropen(0, 1), sp.Interval.open(1, oo))), 1, r'[0,1)\cup(1,+\infty)')
    c('ej-1-26', 'cociente de logaritmos', L(sp.log(xp) / sp.log(4 * xp ** 4), xp, oo), sp.Rational(1, 4), r'el límite es $\frac14$')
    c('ej-1-27', '1^∞', L(((xp + 1) / (xp - 1)) ** xp, xp, oo), sp.E ** 2, r'Resultado: $e^2')
    f28 = (x ** 2 + 1) / (x ** 2 - 1)
    c('ej-1-28', 'horizontal y=1', L(f28, x, oo), 1, r'Respuesta: a) y c)')
    c('ej-1-28', 'vertical x=1 por la derecha', L(f28, x, 1, '+'), oo, r'Luego $x=1$ y $x=-1$ son asíntotas verticales')
    f29 = (x ** 3 + 2 * x ** 2 - 1) / (x ** 2 - 4)
    c('ej-1-29', 'pendiente m', L(f29 / x, x, oo), 1, r'$m=1$, $b=2$')
    c('ej-1-29', 'ordenada b', L(f29 - x, x, -oo), 2, r'La asíntota oblicua es $y=x+2$')
    c('ej-1-29', 'resto de la división', sp.rem(x ** 3 + 2 * x ** 2 - 1, x ** 2 - 4, x), 4 * x + 7, r'(x+2)(x^2-4)+(4x+7)')
    g30 = (x ** 2 + 1) / (x - 1)
    c('ej-1-30', 'horizontal y=0 en -∞', L(1 / (x - 1), x, -oo), 0, r'$y=0$ es asíntota horizontal')
    c('ej-1-30', 'oblicua: b', L(g30 - x, x, oo), 1, r'$y=x+1$ es asíntota oblicua')
    c('ej-1-31', 'acotada por 0', L(x * sp.cos(1 / x), x, 0), 0, r'Redefinición: $f(0)=0$')
    c('ej-1-32', 'k = límite', L((x ** 3 - 8) / (x - 2), x, 2), 12, r'$k=12$')
    c('ej-1-33', 'límite en -1', L(sp.exp(-1 / (1 + x) ** 2), x, -1), 0, r'\lim_{x\to-1}f(x)=0')
    c('ej-1-33', 'f(-1) distinto del límite', si(sp.exp(-sp.Rational(1, 4)) != 0), 1, r'$f(-1)=e^{-1/4}\approx0{,}7788\neq0$')
    gf = sp.exp(-1 / (1 + sp.Abs(x)) ** 2)
    c('ej-1-34', 'g∘f continua en 0', L(gf, x, 0), gf.subs(x, 0), r'$(g\circ f)(x)=e^{-\frac1{(1+|x|)^2}}$')
    p35 = 2 * x ** 5 - 7 * x ** 2 + 3  # ejemplo de grado impar con a_n>0
    c('ej-1-35', 'grado impar: p→+∞ en +∞', L(p35, x, oo), oo, r'\lim_{x\to+\infty}p=+\infty')
    c('ej-1-35', 'grado impar: p→-∞ en -∞', L(p35, x, -oo), -oo, r'\lim_{x\to-\infty}p=-\infty')
    h36 = 4 * x ** 4 / (x ** 2 + x + 1) - sp.cos(x)
    c('ej-1-36', 'h(1) > 0', r(h36.subs(x, 1), 3), sp.Rational('0.793'), r'h(1)\approx0{,}793')
    c('ej-1-36', 'punto de corte', r(raiz(h36, 0.8)), sp.Rational('0.8075'), r'c\approx0{,}8075')
    f37 = sp.exp(-xp) / xp
    c('ej-1-37', 'límite en 0+', L(f37, xp, 0, '+'), oo, r'\lim_{x\to0^+}f=+\infty')
    c('ej-1-37', 'límite en +∞', L(f37, xp, oo), 0, r'\lim_{x\to+\infty}f=0')
    f38 = (x + 2) / (x ** 5 + 1)
    c('ej-1-38', 'f(3)', f38.subs(x, 3), sp.Rational(5, 244), r'f(3)=\frac5{244}')
    c('ej-1-38', 'x0 con f=1/2', r(raiz(f38 - sp.Rational(1, 2), 1.4)), sp.Rational('1.4236'), r'x_0\approx1{,}4236')

    def f39(t):
        return -1 if t <= sp.Rational(3, 10) else (1 if t <= sp.Rational(6, 10) else t - sp.Rational(8, 10))
    c('ej-1-39', 'bisección atrapada en el salto (12 it.)', r(biseccion(f39, 0, 1, 12)[-1], 5), sp.Rational('0.30005'), r'c\approx0{,}30005')
    c40 = biseccion(lambda t: t ** 3 - 3, 0, 4, 3)
    c('ej-1-40', 'c_3', c40[-1], sp.Rational(3, 2), r'Aproximación: $c_3=1{,}5$')
    c('ej-1-40', 'error real', r(abs(c40[-1] - sp.cbrt(3))), sp.Rational('0.0578'), r'\approx0{,}0578')
    c('ej-1-41', 'iteraciones para 0,11', iteraciones(1, '0.11'), 4, r'Respuesta: d) 4')
    # ---- Ejemplos propios (A1-E3)
    c('ej-a1', '0/0 polinomios', L((x ** 2 - 4) / (x ** 2 - 3 * x + 2), x, 2), 4, r'\frac{2+2}{2-1}=4')
    c('ej-a3', 'conjugado', L((sp.sqrt(1 + x) - 1) / x, x, 0), sp.Rational(1, 2), r'\frac1{1+1}=\frac12')
    c('ej-a4', '1^∞', L(((xp + 2) / (xp - 3)) ** (2 * xp + 1), xp, oo), sp.exp(10), r'=e^{10}')
    c('ej-a4', 'logaritmos', L(sp.log(xp ** 2 + 1) / sp.log(xp), xp, oo), 2, r'\to2')
    fb1 = (2 * x + 1) / (x - 3)
    c('ej-b1', 'horizontal', L(fb1, x, oo), 2, r'Horizontal $y=2$')
    c('ej-b1', 'vertical 3-', L(fb1, x, 3, '-'), -oo, r'en $3^-$ el denominador $\to0^-$ y $f\to-\infty$')
    fb2 = (x ** 2 - 3 * x) / (x + 1)
    c('ej-b2', 'pendiente', L(fb2 / x, x, oo), 1, r'=1$')
    c('ej-b2', 'ordenada', L(fb2 - x, x, -oo), -4, r'$y=x-4$')
    fb3 = sp.sqrt(x ** 2 + 1) + x
    c('ej-b3', 'horizontal en -∞', L(fb3, x, -oo), 0, r'Horizontal $y=0$')
    c('ej-b3', 'pendiente en +∞', L(fb3 / x, x, oo), 2, r'Oblicua $y=2x$')
    c('ej-c1', 'parámetro', sp.solve(sp.Symbol('a') + 1 - 5)[0], 4, r'$a=4$')
    c('ej-c2', 'emparedado', L(x ** 2 * sp.sin(1 / x), x, 0), 0, r'$f(0)=0$')
    fc3 = (x ** 2 - 1) / sp.Abs(x - 1)
    c('ej-c3', 'lateral derecho', L(fc3, x, 1, '+'), 2, r'$f=\frac{(x-1)(x+1)}{x-1}=x+1\to2$')
    c('ej-c3', 'lateral izquierdo', L(fc3, x, 1, '-'), -2, r'=-(x+1)\to-2$')
    c('ej-d1', 'raíz', r(raiz(x ** 3 + x - 1, 0.7)), sp.Rational('0.6823'), r'0{,}6823')
    p = x ** 5 - 3 * x + 1
    c('ej-d3', 'tres cambios de signo', si([p.subs(x, k) for k in (-2, -1, 0, 1, 2)] == [-25, 3, 1, -1, 27]), 1, r'$p(-2)=-25$, $p(-1)=3$, $p(0)=1$, $p(1)=-1$, $p(2)=27$')
    c('ej-d3', 'número de raíces reales', len(sp.real_roots(sp.Poly(p, x))), 3, r'al menos 3 raíces reales')
    c('ej-e1', 'c_3', biseccion(lambda t: t ** 2 - 2, 1, 2, 3)[-1], sp.Rational(11, 8), r'$c_3=1{,}375$')
    c('ej-e2', 'iteraciones 10^-3', iteraciones(1, '0.001'), 10, r'$n=10$')
    ce3 = biseccion(lambda t: sp.cos(t) - t, 0, 1, 4)
    c('ej-e3', 'c_4', ce3[-1], sp.Rational(11, 16), r'$c_4=0{,}6875$')
    c('ej-e3', 'raíz', r(raiz(sp.cos(x) - x, 0.7), 5), sp.Rational('0.73909'), r'0{,}73909')
    # ---- Exámenes
    c('ex-1', 'lateral izquierdo', L((2 - x) / (x - 1), x, 0, '-'), -2, r'\lim_{x\to0^-}f=\frac2{-1}=-2')
    c('ex-1', 'lateral derecho', L(sp.exp(x), x, 0, '+'), 1, r'\lim_{x\to0^+}f=e^0=1')
    q = 3 * x * (4 * x ** 2 - 3)
    c('ex-2', 'f(±1)=±3', si(q.subs(x, 1) == 3 and q.subs(x, -1) == -3), 1, r'$f(\pm1)=\pm3$')
    c('ex-2', 'tres soluciones', len(sp.solve(q, x)), 3, r'tres soluciones')
    f3 = sp.log((sp.E * x) ** 2 + 1)
    c('ex-3', 'f(1)', r(f3.subs(x, 1), 3), sp.Rational('2.127'), r'\approx2{,}127')
    c('ex-3', 'x0 exacto', sp.simplify(f3.subs(x, sp.sqrt(sp.E - 1) / sp.E)), 1, r'x_0=\frac{\sqrt{e-1}}e')
    c('ex-4', 'acotada / -∞', L((5 + sp.cos(sp.exp(-xp ** 2))) / sp.log(xp), xp, 0, '+'), 0, r'El límite vale $0$')
    c('ex-5', '1^∞', L(((xp - 1) / (xp + 2)) ** xp, xp, oo), sp.exp(-3), r'e^{-3}')
    f6 = (x ** 3 + x ** 2 + 1) / (x ** 2 + 4)
    c('ex-6', 'pendiente', L(f6 / x, x, -oo), 1, r'=1$ (los términos de mayor grado)')
    c('ex-6', 'ordenada', L(f6 - x, x, oo), 1, r'La asíntota oblicua es $y=x+1$')
    c7 = biseccion(lambda t: t ** 3 + 2 * t ** 2 - 1, 0, 1, 3)
    c('ex-7', 'número de pasos', iteraciones(1, '0.2'), 3, r'3 pasos')
    c('ex-7', 'c_3', c7[-1], sp.Rational(5, 8), r'$\bar x\approx0{,}625$')
    c('ex-7', 'f(c_3)', (x ** 3 + 2 * x ** 2 - 1).subs(x, c7[-1]), sp.Rational('0.025390625'), r'0{,}025390625')
    c('ex-7', 'variante: 4 iteraciones', iteraciones(2, '0.15'), 4, r'4 iteraciones')
    # ---- Práctica «Ahora hazlo tú» (respuesta final = «Resultado: …»)
    a, b = sp.symbols('a b')
    f_c2 = sp.solve([sp.Eq(a + 1, b), sp.Eq(1 + b, L(a * (x ** 2 - 1) / (x - 1), x, 1))], [a, b])
    cf2 = biseccion(lambda t: t ** 3 + t - 5, 1, 2, 4)
    P = {
        'pr-a1': (L((x ** 2 - 9) / (x ** 2 - x - 6), x, 3), sp.Rational(6, 5), r'Resultado: $\frac65$'),
        'pr-a2': (L((sp.sqrt(x + 9) - 3) / (sp.sqrt(x + 4) - 2), x, 0), sp.Rational(2, 3), r'Resultado: $\frac23$'),
        'pr-b1': (L((1 - 3 * x) / (x + 2), x, oo), -3, r'Resultado: vertical $x=-2$ y horizontal $y=-3$'),
        'pr-b2': (L(sp.sqrt(x ** 2 + 3 * x) + x, x, -oo), -sp.Rational(3, 2), r'Resultado: $y=x+\frac32$ en $+\infty$ e $y=-x-\frac32$ en $-\infty$'),
        'pr-c1': (sp.solve(2 * a + 1 - (4 - a), a)[0], 1, r'Resultado: $a=1$'),
        'pr-c2': (f_c2[a] + 10 * f_c2[b], 2 + 30, r'Resultado: $a=2$, $b=3$'),
        'pr-d1': (L((x ** 2 - 4 * x + 3) / (x ** 2 - 1), x, 1), -1, r'Resultado: evitable en $x=1$ (límite $-1$) e infinita en $x=-1$'),
        'pr-d2': (L(1 / (1 + sp.exp(1 / x)), x, 0, '-') - L(1 / (1 + sp.exp(1 / x)), x, 0, '+'), 1, r'Resultado: salto en $x=0$ (laterales $1$ y $0$)'),
        'pr-e1': (r(raiz(sp.exp(x) + x - 3, 0.8), 3), sp.Rational('0.792'), r'Resultado: existe $c\in(0,1)$ con $e^c=3-c$ ($c\approx0{,}792$)'),
        'pr-e2': (r(raiz(sp.exp(-x) - x, 0.5), 3), sp.Rational('0.567'), r'Resultado: existe $c\in[0,1]$ con $f(c)=c$'),
        'pr-f1': (iteraciones(2, '0.01'), 8, r'Resultado: $n=8$'),
        'pr-f2': (cf2[-1], sp.Rational(25, 16), r'Resultado: $c_4=1{,}5625$, error menor que $\frac1{16}$; para $10^{-3}$, $n=10$'),
    }
    for eid, (val, esp, txt) in P.items():
        if (EJ / f'{eid}.html').exists() or (EJ / f'{eid}.solucion.html').exists():
            c(eid, 'resultado de la práctica', val, esp, txt)
