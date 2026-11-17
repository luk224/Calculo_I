r"""Tema 6.1 (Definición de integral de Riemann): particiones y finura, sumas de Riemann, integrales por la definición,
áreas con signo, propiedades (U p.240), acotaciones y primitivas (Def. 6.2), recalculados con sympy.

`comprobaciones(c)`: c(ejercicio, descripción, valor_sympy, esperado, trozo_latex)
  - valor_sympy: lo que calcula sympy;  esperado: lo que afirma la página;
  - trozo_latex: cadena que debe aparecer en `ejercicios/<ejercicio>.html` (o `.solucion.html`), comparada sin etiquetas,
    espacios, \, \; \! ni \displaystyle y con \dfrac/\tfrac = \frac.
Las comprobaciones de la práctica «Ahora hazlo tú» (pr-*) solo se activan cuando el ejercicio existe en `contenido/`.
"""
import pathlib

import sympy as sp

R = sp.Rational
pi = sp.pi
E_ = sp.E
x = sp.Symbol('x', real=True)
n, i = sp.symbols('n i', positive=True, integer=True)
EJ = pathlib.Path(__file__).resolve().parents[2] / 'contenido' / 'tema_6_1' / 'ejercicios'


def _igual(p, q):
    p, q = sp.sympify(p), sp.sympify(q)
    if p == q:
        return True
    return sp.simplify(p - q) == 0


def lista(vals, esperados):
    return si((len(vals) == len(esperados) and all(_igual(p, q) for p, q in zip(vals, esperados))))


def si(cond):
    return sp.Integer(1 if bool(cond) else 0)


def r(val, d):
    return R(str(round(float(val), d)))


def finura(P):
    return max(b - a for a, b in zip(P, P[1:]))


def es_particion(P, a, b):
    return si((P[0] == a and P[-1] == b and all(p < q for p, q in zip(P, P[1:]))))


def suma(f, P, c):
    """Suma de Riemann con partición P y representantes c (lista de puntos)."""
    return sp.nsimplify(sum(f.subs(x, ci) * (q - p) for ci, p, q in zip(c, P, P[1:])))


def izq(P):
    return P[:-1]


def der(P):
    return P[1:]


def med(P):
    return [(p + q) / 2 for p, q in zip(P, P[1:])]


def suma_n(f, a, b, extremo='der'):
    """S_n con partición equiespaciada de [a,b] en n trozos (simbólica en n)."""
    dx = (b - a) / n
    ci = a + i * dx if extremo == 'der' else a + (i - 1) * dx
    return sp.simplify(sp.summation(f.subs(x, ci) * dx, (i, 1, n)))


def integral(f, a, b):
    return sp.integrate(f, (x, a, b))


def comprobaciones(c):
    # ---- Ejercicios del libro (E 6.1-6.10)
    P1 = [1, 2, 3, 5, 6]
    c('ej-6-1', 'finura de {1,2,3,5,6} = 2', lista([es_particion(P1, 1, 6), finura(P1), len(P1) - 1], [1, 2, 4]), 1,
      r"\|P\|=\max\{1,1,2,1\}=\boxed{2}")
    P2 = [0, 3] + [3 + R(k, 98) for k in range(1, 99)]
    Q2 = [R(k, 98) for k in range(99)] + [4]
    c('ej-6-2', '100 puntos, finura 3 (las dos construcciones)',
      lista([len(P2), es_particion(P2, 0, 4), finura(P2), len(Q2), es_particion(Q2, 0, 4), finura(Q2)], [100, 1, 3, 100, 1, 3]), 1,
      r"$2+98=100$")
    c('ej-6-3', 'finura ≤ 2π ≈ 6,2832 < 7', lista([r(2 * pi, 4), si((2 * pi < 7))], [R('6.2832'), 1]), 1,
      r"\|P\|\le2\pi\approx6{,}2832")
    c('ej-6-4', 'toda suma de Riemann de la función nula vale 0; I = I + I ⇒ I = 0',
      lista([suma_n(sp.Integer(0) * x, 0, 1), sp.solve(sp.Eq(sp.Symbol('I'), 2 * sp.Symbol('I')))[0]], [0, 0]), 1, r"I=I+I")
    a, b = 0, 1
    c('ej-6-5', 'b) con f=1, g=−1: 0 frente a 2(b−a); d) con f=g=1: 0 frente a 2(b−a)',
      lista([integral(sp.Abs(1 - 1), a, b), 2 * (b - a), integral(sp.Abs(1 - 1), a, b), integral(1, a, b) - integral(1, b, a)], [0, 2, 0, 2]), 1,
      r"Respuesta: b) y d)")
    c('ej-6-6', '∫₀¹x² = 1/3 ≠ (1/2)(1/2) = 1/4', lista([integral(x ** 2, 0, 1), integral(x, 0, 1) ** 2], [R(1, 3), R(1, 4)]), 1,
      r"\frac13\ne\frac14")
    c('ej-6-7', 'cotas −2·2 = −4 y 4·2 = 8', lista([integral(-2, -1, 1), integral(4, -1, 1)], [-4, 8]), 1,
      r"-4\le\int_{-1}^1f\le8")
    c('ej-6-8', 'aditividad ⇒ 0; ejemplo sen(4/3(x+π)) con integral 0 en [−π,π/2]',
      lista([si((-pi < pi / 2 < E_)), integral(sp.sin(R(4, 3) * (x + pi)), -pi, pi / 2)], [1, 0]), 1,
      r"\int_{-\pi}^{\frac\pi2}f=0")
    c('ej-6-9', 'sen x en [0,π]: μ = 2/π ≈ 0,64 (no entre f(0)=f(π)=0)',
      lista([integral(sp.sin(x), 0, pi) / pi, r(2 / pi, 2)], [2 / pi, R('0.64')]), 1, r"\mu=\frac2\pi\approx0{,}64")
    C = sp.Integer(1)
    c('ej-6-10', "con f=1, F=x, C=1: F'=f (a); f'=0≠F+C (b), ≠F (c); F'=1≠f+C=2 (d)",
      lista([sp.diff(x, x), sp.diff(sp.Integer(1), x), (x + C).subs(x, 0), 1 + C], [1, 0, 1, 2]), 1, r"Respuesta: a).")
    # ---- Ejemplos propios
    Sa = suma_n(3 * x + 1, 0, 1)
    Sb_der, Sb_izq = suma_n(x ** 2, 0, 1), suma_n(x ** 2, 0, 1, 'izq')
    c('p1', '∫₀¹(3x+1)=5/2 con S_n=(5n+3)/(2n); ∫₀¹x²=1/3; n=10: 0,285 y 0,385',
      lista([Sa - (5 * n + 3) / (2 * n), sp.limit(Sa, n, sp.oo), sp.limit(Sb_der, n, sp.oo), Sb_der - (n + 1) * (2 * n + 1) / (6 * n ** 2),
             Sb_izq - (n - 1) * (2 * n - 1) / (6 * n ** 2), Sb_izq.subs(n, 10), Sb_der.subs(n, 10)],
            [0, R(5, 2), R(1, 3), 0, 0, R('0.285'), R('0.385')]), 1, r"\frac{5n+3}{2n}")
    g2 = x + sp.sqrt(4 - x ** 2)
    c('p2', '2π, −2π y variante 2π−4', lista([integral(g2, -2, 2), integral(g2, 2, -2), integral(sp.sqrt(4 - x ** 2) - 1, -2, 2)],
                                           [2 * pi, -2 * pi, 2 * pi - 4]), 1, r"=0+2\pi=2\pi")
    f3 = sp.exp(-x ** 2)
    cot = []
    for k in (1, 2, 4):
        P = [R(j, k) for j in range(k + 1)]
        cot += [r(suma(f3, P, der(P)).evalf(), 4), r(suma(f3, P, izq(P)).evalf(), 4)]
    I3 = sp.Integral(f3, (x, 0, 1)).evalf()
    c3 = sp.nsolve(sp.exp(-x ** 2) - I3, x, 0.5)
    c('p3', 'horquillas [0,3679;1], [0,5733;0,8894], [0,6640;0,8220]; I≈0,7468; c≈0,54',
      lista(cot + [r(I3, 4), r(c3, 2)], [R('0.3679'), 1, R('0.5733'), R('0.8894'), R('0.6640'), R('0.8220'), R('0.7468'), R('0.54')]), 1,
      r"0{,}6640\le I\le0{,}8220")
    f4 = x ** 2
    P4 = [-1, 0, R(1, 2), 2]
    P4b = [-1, 0, R(1, 2), 1, 2]
    m = [0, 0, R(1, 4)]
    M = [1, R(1, 4), 4]
    mb = [0, 0, R(1, 4), 1]
    Mb = [1, R(1, 4), 1, 4]
    def sm(v, P): return sum(vi * (q - p) for vi, p, q in zip(v, P, P[1:]))  # noqa: E301,E704
    c('p4', "‖P‖=3/2; s=3/8, S=57/8; s'=9/8, S'=45/8; medios 21/8; exacto 3",
      lista([finura(P4), sm(m, P4), sm(M, P4), sm(mb, P4b), sm(Mb, P4b), suma(f4, P4, med(P4)), integral(f4, -1, 2),
             si((all(sp.minimum(f4, x, sp.Interval(p, q)) == mm and sp.maximum(f4, x, sp.Interval(p, q)) == MM
                                for p, q, mm, MM in zip(P4b, P4b[1:], mb, Mb))))],
            [R(3, 2), R(3, 8), R(57, 8), R(9, 8), R(45, 8), R(21, 8), 3, 1]), 1,
      r"s(P')=0+0+\frac14\cdot\frac12+1\cdot1=\frac98")
    # ---- Exámenes
    s = sp.Symbol('s', positive=True)
    F1 = sp.integrate(1 / (s + 1), (s, 0, x))
    c('x1', "f=1/(s+1) decreciente; F=ln(1+x), F'=1/(x+1)>0",
      lista([sp.diff(1 / (s + 1), s), F1, sp.diff(sp.log(1 + x), x)], [-1 / (s + 1) ** 2, sp.log(1 + x), 1 / (x + 1)]), 1,
      r"F(x)=\ln(1+x)")
    t = sp.Symbol('t', real=True)
    F2 = sp.integrate(t * sp.sin(t), (t, 0, x))
    c('x2', "F''(7π)=−7π; F(7π)=7π; signo de F' a ambos lados",
      lista([sp.diff(x * sp.sin(x), x).subs(x, 7 * pi), F2.subs(x, 7 * pi), sp.sign((x * sp.sin(x)).subs(x, 6.5 * pi)),
             sp.sign((x * sp.sin(x)).subs(x, 7.5 * pi))], [-7 * pi, 7 * pi, 1, -1]), 1,
      r"F''(7\pi)=0+7\pi\cos7\pi=-7\pi\lt0")
    F3 = sp.integrate(t - 1, (t, 0, x))
    c('x3', 'F=x²/2−x; F(1/2)=−3/8 > F(1)=−1/2', lista([F3, F3.subs(x, R(1, 2)), F3.subs(x, 1)], [x ** 2 / 2 - x, R(-3, 8), R(-1, 2)]), 1,
      r"F\left(\frac12\right)=-\frac38\gt F(1)=-\frac12")
    c('x4', 'áreas 1/12, 1/3, 5/12 → B',
      lista([integral(x ** 2 - x ** 3, 0, 1), integral(sp.sqrt(x) - x ** 2, 0, 1), integral(sp.sqrt(x) - x ** 3, 0, 1)],
            [R(1, 12), R(1, 3), R(5, 12)]), 1, r"\int_0^1(\sqrt x-x^3)\,dx=\frac23-\frac14=\frac5{12}")
    # ---- Práctica «Ahora hazlo tú» (respuesta final = «Resultado: …»)
    Pa1 = [-2, R(-3, 2), 0, 1, 3]
    cc = sp.Symbol('c', real=True)
    sol_a1 = sp.solve([cc - 1 <= R(3, 2), 3 - cc <= R(3, 2)], cc)
    Qn = lambda k: [R(j, 2 * k) for j in range(k + 1)] + [1]  # noqa: E731
    ln_ = sp.Symbol('n', positive=True)
    fin_a2 = 2 - 2 ** ((ln_ - 1) / ln_)
    Pa2_4 = [2 ** R(j, 4) for j in range(5)]
    fb1 = x ** 2 + 1
    Pb1 = [R(j, 2) for j in range(5)]
    fb2 = 1 / x
    Pb2 = [1, R(3, 2), 2, 3]
    Sc1, Sc1i = suma_n(1 - x, -1, 3), suma_n(1 - x, -1, 3, 'izq')
    Sc2 = suma_n(x ** 2, 1, 3)
    xr = sp.Symbol('xr', real=True)
    dd2 = sp.integrate(sp.sqrt(9 - xr ** 2), (xr, -3, 3)) - sp.integrate(sp.Abs(xr), (xr, -3, 3))
    # simetría: con partición equiespaciada simétrica y puntos medios, la suma de x³ es exactamente 0
    sim = [sum((-3 + (2 * j - 1) * R(3, k)) ** 3 * R(6, k) for j in range(1, k + 1)) for k in (2, 5, 10)]
    A, B = sp.symbols('A B')
    sAB = sp.solve([A + B - 5, A - 2 * B + 1], [A, B])
    ff2 = x * sp.exp(-x)
    If2 = integral(ff2, 0, 3)
    low2 = 0 * 1 + ff2.subs(x, 2) + ff2.subs(x, 3)
    upp2 = ff2.subs(x, 1) + ff2.subs(x, 1) + ff2.subs(x, 2)
    fg1 = x * sp.exp(x)
    cand = [x * sp.exp(x) - sp.exp(x), x * sp.exp(x) - sp.exp(x) + 5, x ** 2 * sp.exp(x) / 2, x * sp.exp(x)]
    P = {
        'pr-a1': (lista([es_particion(Pa1, -2, 3), len(Pa1) - 1, finura(Pa1), si((sol_a1 == sp.And(R(3, 2) <= cc, cc <= R(5, 2)))),
                         finura(sorted(Pa1 + [2])), sp.ceiling(5 / R(1, 10))], [1, 4, 2, 1, R(3, 2), 50]), 1,
                  r"Resultado: $n=4$, $\|P\|=2$; añadiendo un punto $c\in\left[\frac32,\frac52\right]$ (por ejemplo $c=2$) la finura pasa a ser $\frac32$; equiespaciada con finura $\le\frac1{10}$: $n\ge50$"),
        'pr-a2': (lista([es_particion(Pa2_4, 1, 2), sp.nsimplify(finura([sp.nsimplify(p) for p in Pa2_4])) - (2 - 2 ** R(3, 4)), r(2 - 2 ** R(3, 4), 4),
                         sp.limit(fin_a2, ln_, sp.oo), finura(Qn(3)), finura(Qn(50)), len(Qn(50)) - 1],
                        [1, 0, R('0.3182'), 0, R(1, 2), R(1, 2), 51]), 1,
                  r"Resultado: $\|P_n\|=2-2^{(n-1)/n}$ ($\approx0{,}3182$ para $n=4$), que tiende a $0$; $\|Q_n\|=\frac12$ para todo $n$ aunque $n\to\infty$"),
        'pr-b1': (lista([suma(fb1, Pb1, izq(Pb1)), suma(fb1, Pb1, der(Pb1)), suma(fb1, Pb1, med(Pb1)), integral(fb1, 0, 2), r(R(14, 3), 3)],
                        [R(15, 4), R(23, 4), R(37, 8), R(14, 3), R('4.667')]), 1,
                  r"Resultado: izquierdo $3{,}75$; derecho $5{,}75$; punto medio $4{,}625$ (valor exacto $\frac{14}3\approx4{,}667$)"),
        'pr-b2': (lista([finura(Pb2), suma(fb2, Pb2, med(Pb2)), r(R(38, 35), 4), suma(fb2, Pb2, der(Pb2)), suma(fb2, Pb2, izq(Pb2)),
                         integral(fb2, 1, 3), r(sp.log(3), 4)], [1, R(38, 35), R('1.0857'), R(11, 12), R(4, 3), sp.log(3), R('1.0986')]), 1,
                  r"Resultado: $\|P\|=1$; con puntos medios $\frac{38}{35}\approx1{,}0857$; $\frac{11}{12}\le\int_1^3\frac{dx}x\le\frac43$ (el valor es $\ln3\approx1{,}0986$)"),
        'pr-c1': (lista([Sc1, Sc1i, sp.limit(Sc1, n, sp.oo), integral(1 - x, -1, 3)], [-8 / n, 8 / n, 0, 0]), 1,
                  r"Resultado: $S_n=-\frac8n$; $\int_{-1}^3(1-x)\,dx=0$"),
        'pr-c2': (lista([Sc2 - (2 + 4 * (n + 1) / n + 4 * (n + 1) * (2 * n + 1) / (3 * n ** 2)), Sc2.subs(n, 1), sp.limit(Sc2, n, sp.oo),
                         integral(x ** 2, 1, 3), integral(x ** 2, 0, 3) - integral(x ** 2, 0, 1)], [0, 18, R(26, 3), R(26, 3), R(26, 3)]), 1,
                  r"Resultado: $S_n=2+\frac{4(n+1)}n+\frac{4(n+1)(2n+1)}{3n^2}$; $\int_1^3x^2\,dx=\frac{26}3$"),
        'pr-d1': (lista([integral(x - 3, 0, 3), integral(x - 3, 3, 4), integral(x - 3, 0, 4), integral(sp.Abs(x - 3), 0, 4)],
                        [R(-9, 2), R(1, 2), -4, 5]), 1,
                  r"Resultado: $\int_0^4(x-3)\,dx=-4$; área encerrada con el eje: $5$"),
        'pr-d2': (lista([dd2, r(dd2, 3), integral(x ** 3 + 2, -3, 3)] + sim, [9 * pi / 2 - 9, R('5.137'), 12, 0, 0, 0]), 1,
                  r"Resultado: a) $\frac{9\pi}2-9\approx5{,}137$; b) $12$"),
        'pr-e1': (lista([-1 - 3, 1 + 3, 2 * (-1) - 3 * 4], [-4, 4, -14]), 1,
                  r"Resultado: $\int_2^5f=-4$; $\int_5^2f=4$; $\int_0^5(2f-3g)=-14$"),
        'pr-e2': (lista([sAB[A], sAB[B], 2 * sAB[A] - sAB[B] + 3, integral(2 * x / 3, 0, 3), integral(4 * x / 9, 0, 3),
                         integral(1 * R(2, 3), 0, 3), integral(2 * x / 3 * 4 * x / 9, 0, 3)], [3, 2, 7, 3, 2, 2, R(8, 3)]), 1,
                  r"Resultado: a) $\int_0^3f=3$, $\int_0^3g=2$; b) $7$; c) no se puede: con $f=1$, $g=\frac23$ sale $2$ y con $f=\frac{2x}3$, $g=\frac{4x}9$ sale $\frac83$"),
        'pr-f1': (lista([sp.sqrt(1 + 0 ** 3) * 2, sp.sqrt(1 + 2 ** 3) * 2, si((2 < sp.Integral(sp.sqrt(1 + x ** 3), (x, 0, 2)).evalf() < 6)),
                         r(sp.Integral(sp.sqrt(1 + x ** 3), (x, 0, 2)).evalf(), 3)], [2, 6, 1, R('3.241')]), 1,
                  r"Resultado: $2\le\int_0^2\sqrt{1+x^3}\,dx\le6$ (valor real $\approx3{,}241$)"),
        'pr-f2': (lista([sp.solve(sp.diff(ff2, x), x), 3 * ff2.subs(x, 1), r(3 / E_, 3), low2, upp2, r(low2, 3), r(upp2, 3), If2, r(If2, 3)],
                        [[1], 3 / E_, R('1.104'), 2 * sp.exp(-2) + 3 * sp.exp(-3), 2 / E_ + 2 * sp.exp(-2), R('0.42'), R('1.006'), 1 - 4 * sp.exp(-3), R('0.801')]), 1,
                  r"Resultado: a) $0\le I\le\frac3e\approx1{,}104$; b) $2e^{-2}+3e^{-3}\le I\le\frac2e+2e^{-2}$, es decir, $0{,}420\le I\le1{,}006$ (valor real $1-4e^{-3}\approx0{,}801$)"),
        'pr-g1': (lista([sp.simplify(sp.diff(F, x) - fg1) for F in cand], [0, 0, x ** 2 * sp.exp(x) / 2, sp.exp(x)]), 1,
                  r"Resultado: son primitivas a) y b); c) y d) no"),
        'pr-g2': (lista([sp.simplify(sp.diff(sp.atan(x), x) - 1 / (1 + x ** 2)), sp.simplify(sp.diff(-sp.atan(1 / x), x) - 1 / (1 + x ** 2)),
                         sp.atan(1) + sp.atan(1), sp.atan(-1) + sp.atan(-1), sp.atan(1) - pi / 4],
                        [0, 0, pi / 2, -pi / 2, 0]), 1,
                  r"Resultado: $\operatorname{arctg}x-\left(-\operatorname{arctg}\frac1x\right)=\frac\pi2$ en $(0,\infty)$ (y $-\frac\pi2$ en $(-\infty,0)$); primitiva con $H(1)=0$: $H(x)=\operatorname{arctg}x-\frac\pi4$"),
    }
    for eid, (val, esp, txt) in P.items():
        if (EJ / f'{eid}.html').exists() or (EJ / f'{eid}.solucion.html').exists():
            c(eid, 'resultado de la práctica', val, esp, txt)
    return P
