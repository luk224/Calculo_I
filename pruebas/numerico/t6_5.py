r"""Tema 6.5 (Integrales impropias): definición por límites (primera, segunda y tercera especie), integral de referencia
$\frac1{x^p}$, criterios de comparación directa y por límite; valores y límites recalculados con sympy (y mpmath cuando no
hay primitiva elemental).

`comprobaciones(c)`: c(ejercicio, descripción, valor_sympy, esperado, trozo_latex)
  - valor_sympy: lo que calcula sympy;  esperado: lo que afirma la página;
  - trozo_latex: cadena que debe aparecer en `ejercicios/<ejercicio>.html` (o `.solucion.html`), comparada sin etiquetas,
    espacios, \, \; \! ni \displaystyle y con \dfrac/\tfrac = \frac.
Las comprobaciones de la práctica «Ahora hazlo tú» (pr-*) solo se activan cuando el ejercicio existe en `contenido/`.
"""
import pathlib

import mpmath as mp
import sympy as sp

R = sp.Rational
pi = sp.pi
E_ = sp.E
oo = sp.oo
x = sp.Symbol('x', positive=True)       # casi todas las integrales viven en (0, ∞)
y = sp.Symbol('y', real=True)           # para intervalos con negativos
t = sp.Symbol('t', positive=True)
c_ = sp.Symbol('c', positive=True)
M = sp.Symbol('M', positive=True)
p_ = sp.Symbol('p', positive=True)
ln, sen, cos, tg, atan, sqrt, exp = sp.log, sp.sin, sp.cos, sp.tan, sp.atan, sp.sqrt, sp.exp
EJ = pathlib.Path(__file__).resolve().parents[2] / 'contenido' / 'tema_6_5' / 'ejercicios'


def _igual(p, q):
    p, q = sp.sympify(p), sp.sympify(q)
    if p == q:
        return True
    if p.has(oo, -oo, sp.zoo) or q.has(oo, -oo, sp.zoo):
        return False
    return sp.simplify(p - q) == 0


def lista(vals, esperados):
    return si(len(vals) == len(esperados) and all(_igual(p, q) for p, q in zip(vals, esperados)))


def si(cond):
    return sp.Integer(1 if bool(cond) else 0)


def r(val, d):
    return R(str(round(float(val), d)))


def integral(f, a, b, v=x):
    return sp.integrate(f, (v, a, b))


def quad(f, a, b):
    """Valor numérico con mpmath (integrales sin primitiva elemental)."""
    mp.mp.dps = 30
    return mp.quad(sp.lambdify(x, f, 'mpmath'), [a, b] if b != mp.inf else [a, 1, mp.inf])


def lim(f, punto, lado='+', v=x):
    return sp.limit(f, v, punto, lado)


def comprobaciones(c):
    # ---- Ejercicios del libro (E 6.42-6.48)
    c('e642', 'continua y acotada en R: ∫₀^∞ dx/(1+x²) = π/2 converge; ∫₀^M cos x = sen M oscila',
      lista([integral(1 / (1 + x ** 2), 0, oo), integral(cos(x), 0, M), integral(cos(x), 0, 2 * pi), integral(cos(x), 0, pi / 2)],
            [pi / 2, sen(M), 0, 1]), 1, r"\int_0^\infty\frac{dx}{1+x^2}")
    c('e643', '∫₀^∞ x e^{−x²} = 1/2', lista([integral(x * exp(-x ** 2), 0, oo), lim(R(1, 2) - exp(-M ** 2) / 2, oo, '-', M)], [R(1, 2), R(1, 2)]), 1,
      r"converge y vale $\frac12$")
    k = sp.Symbol('k', integer=True)
    c('e644', 'a_n = 0; F(k+1/4) = 1/(2π) ≈ 0,159, F(k+3/4) = −1/(2π)',
      lista([sp.simplify(sen(2 * pi * k) / (2 * pi)), sp.simplify(sen(2 * pi * (k + R(1, 4))) / (2 * pi)), sp.simplify(sen(2 * pi * (k + R(3, 4))) / (2 * pi)),
             r(1 / (2 * pi), 3)], [0, 1 / (2 * pi), -1 / (2 * pi), R('0.159')]), 1, r"=\frac1{2\pi}\approx0{,}159")
    c('e645', 'segunda especie: intervalo acotado (a, b reales) y f no acotada, p. ej. 1/x en (0,1]',
      lista([lim(1 / x, 0), integral(1 / sqrt(x), 0, 1)], [oo, 2]), 1, r"$f:(a,b]\to\mathbb R$")
    c('e646', '∫₀¹ ln x = −1; c·ln c → 0', lista([integral(ln(x), 0, 1), lim(c_ * ln(c_), 0, '+', c_), integral(ln(x), c_, 1, x)],
                                              [-1, 0, -1 - c_ * ln(c_) + c_]), 1, r"\lim_{c\to0^+}(-1-c\ln c+c)=-1")
    c('e647', 'x/ln(x+1) → ∞ (diverge); x²e^{−x²} → 0 (converge, ≈0,1394)',
      lista([lim(x / ln(x + 1), oo, '-'), lim(x * exp(-x ** 2), oo, '-'), lim(x ** 2 * exp(-x ** 2), oo, '-'), r(quad(exp(-x ** 2), 1, mp.inf), 4)],
            [oo, 0, 0, R('0.1394')]), 1, r"\approx0{,}1394")
    G = lambda q: integral(exp(-x) * x ** (q - 1), 0, oo)  # noqa: E731
    c('e648', 'Γ(1/2)=√π, Γ(1)=1, Γ(5/2)=(3/2)Γ(3/2), Γ(5)=24, x^{p+1}e^{−x}→0',
      lista([G(R(1, 2)), G(1), G(R(5, 2)) - R(3, 2) * G(R(3, 2)), G(5), G(2), G(3), lim(x ** R(7, 2) * exp(-x), oo, '-')],
            [sqrt(pi), 1, 0, 24, 1, 2, 0]), 1, r"\Gamma(5)=24=4!")
    # ---- Ejemplos propios y tipos
    c('p1', '∫₁^∞ dx/(x(x+1)) = ln 2 ≈ 0,693', lista([integral(1 / (x * (x + 1)), 1, oo), r(ln(2), 3)], [ln(2), R('0.693')]), 1,
      r"-\ln\frac12=\ln2\approx0{,}693")
    c('p2', 'q=2: 1/ln 2 ≈ 1,443; q=1 en M=10¹⁰⁰: ≈5,8',
      lista([integral(1 / (x * ln(x) ** 2), 2, oo), r(1 / ln(2), 3), r(ln(ln(sp.Integer(10) ** 100)) - ln(ln(2)), 1),
             integral(1 / t ** 2, ln(2), oo, t)], [1 / ln(2), R('1.443'), R('5.8'), 1 / ln(2)]), 1, r"\frac1{\ln2}\approx1{,}443")
    c('p3', '∫₀¹ x^{−1/3} = 3/2, mitad izquierda −3/2; ∫₀¹ dx/x = ∞',
      lista([integral(x ** R(-1, 3), 0, 1), -integral(t ** R(-1, 3), 0, 1, t), integral(1 / x, 0, 1)], [R(3, 2), R(-3, 2), oo]), 1,
      r"\frac32-\frac32=0")
    c('p4', '∫₀^∞ dx/(√x(1+x)) = π (π/2 + π/2)',
      lista([integral(1 / (sqrt(x) * (1 + x)), 0, oo), integral(1 / (sqrt(x) * (1 + x)), 0, 1), integral(1 / (sqrt(x) * (1 + x)), 1, oo)],
            [pi, pi / 2, pi / 2]), 1, r"Total: $\pi$")
    c('ta', '∫₁^∞ dx/√(x³+1) ≈ 1,8948 < 2 = ∫₁^∞ x^{−3/2}',
      lista([r(quad(1 / sqrt(x ** 3 + 1), 1, mp.inf), 4), integral(x ** R(-3, 2), 1, oo)], [R('1.8948'), 2]), 1, r"\approx1{,}8948")
    c('tb', '∫₀¹ dx/√(x(1+x)) = 2 ln(1+√2) ≈ 1,7627',
      lista([integral(2 / sqrt(1 + t ** 2), 0, 1, t), r(quad(1 / sqrt(x * (1 + x)), 0, 1), 4), r(2 * ln(1 + sqrt(2)), 4)],
            [2 * ln(1 + sqrt(2)), R('1.7627'), R('1.7627')]), 1, r"2\ln(1+\sqrt2)\approx1{,}7627")
    c('tc', 'sen²x/x² → 1 en 0; ∫₀^∞ = π/2', lista([lim(sen(x) ** 2 / x ** 2, 0), integral(sen(x) ** 2 / x ** 2, 0, oo)], [1, pi / 2]), 1,
      r"Su valor, $\frac\pi2$")
    c('td', 'x/sen x → 1; ∫₀¹ dx/√(sen x) ≈ 2,0348',
      lista([lim(x / sen(x), 0), r(quad(1 / sqrt(sen(x)), 0, 1), 4), integral(1 / x, 0, 1)], [1, R('2.0348'), oo]), 1, r"\approx2{,}0348")
    c('auto', '∫₁^M ln x = M ln M − M + 1 → ∞; ∫₁^∞ dx/x = ∞',
      lista([sp.expand(integral(ln(x), 1, M)), lim(M * ln(M) - M + 1, oo, '-', M), integral(1 / x, 1, oo)], [M * ln(M) - M + 1, oo, oo]), 1,
      r"M\ln M-M+1\to\infty")
    # ---- Exámenes
    c('x1', 'límites finitos: solo segunda especie; ∫₀¹ dx/√x = 2, ∫₋₁¹ dx/x² diverge',
      lista([integral(1 / sqrt(x), 0, 1), integral(1 / y ** 2, 0, 1, y)], [2, oo]), 1, r"(converge, vale $2$)")
    c('x2', '∫₀^∞ e^{−x} = 1', integral(exp(-x), 0, oo), 1, r"\lim_{M\to\infty}\big(1-e^{-M}\big)=1")
    c('x3', 'no impropia; trapecio 1/2 − 1/(2e) ≈ 0,3161; exacto 1/2',
      lista([integral(ln(x) / x, 1, E_), (E_ - 1) / 2 * (0 + 1 / E_), r(R(1, 2) - 1 / (2 * E_), 4)],
            [R(1, 2), R(1, 2) - 1 / (2 * E_), R('0.3161')]), 1, r"\frac12-\frac1{2e}\approx0{,}3161")
    c('x4', '∫_{−∞}^{−1} 2/(x(x−1)) = 2 ln 2 ≈ 1,386',
      lista([integral(2 / (y * (y - 1)), -oo, -1, y), r(2 * ln(2), 3)], [2 * ln(2), R('1.386')]), 1, r"=2\ln2\approx1{,}386")
    c('x5', '∫₀^∞ x e^{−x/2} = 4', lista([integral(x * exp(-x / 2), 0, oo), sp.simplify(sp.diff((-2 * x - 4) * exp(-x / 2), x) - x * exp(-x / 2))], [4, 0]), 1,
      r"Valor:</b> $4$")
    F6 = ln(sp.Abs(y)) - ln(sp.Abs(y + 2))
    c('x6', 'tercera especie: el trozo [−3,−2) diverge (+∞); el otro vale ln 3',
      lista([lim(F6 - F6.subs(y, -3), -2, '-', y), integral(2 / (y * (y + 2)), -oo, -3, y),
             [sp.N((sp.diff(F6, y) - 2 / (y * (y + 2))).subs(y, v), 20) for v in (-3, -5, R(-5, 2))]], [oo, ln(3), [0, 0, 0]]), 1, r"el límite es $+\infty$")
    # ---- Práctica «Ahora hazlo tú» (respuesta final = «Resultado: …»)
    P = {
        'pr-a1': (lista([sp.solve(y ** 2 - 1, y), sp.solve(y - 1, y), lim(sen(x) / x, 0), lim(1 / (x * sqrt(x - 1)), 1, '+')],
                        [[-1, 1], [1], 1, oo]), 1,
                  r"Resultado: a) primera especie; b) segunda especie (asíntota interior en $x=1$); c) no es impropia; d) tercera especie"),
        'pr-a2': (lista([sp.solve(y ** 2 - 4 * y + 3, y), lim(1 / (y ** 2 - 4 * y + 3), 1, '-', y), lim((1 - cos(x)) / x ** 2, 0),
                         lim(ln(x) / (1 + x ** 2), 0), lim(tg(y), pi / 2, '-', y)], [[1, 3], oo, R(1, 2), -oo, oo]), 1,
                  r"Resultado: a) si $0&lt;a&lt;1$ no es impropia; si $a\ge1$, segunda especie; b) no es impropia ($f\to\frac12$); c) tercera especie"),
        'pr-b1': (lista([integral(1 / (2 * x + 1) ** 2, 1, oo), lim(1 / sp.Integer(6) - 1 / (2 * (2 * M + 1)), oo, '-', M),
                         integral(1 / (x ** 2 + 4), 0, oo)], [R(1, 6), R(1, 6), pi / 4]), 1,
                  r"Resultado: a) $\frac16$; b) $\frac\pi4$"),
        'pr-b2': (lista([integral(1 / (y ** 2 + 2 * y + 5), -oo, oo, y), integral(1 / (y ** 2 + 2 * y + 5), -oo, -1, y),
                         integral(exp(-x) * sen(x), 0, oo),
                         sp.simplify(sp.diff(-exp(-x) * (sen(x) + cos(x)) / 2, x) - exp(-x) * sen(x))], [pi / 2, pi / 4, R(1, 2), 0]), 1,
                  r"Resultado: a) $\frac\pi2$; b) $\frac12$"),
        'pr-c1': (lista([integral(1 / sqrt(4 - y), 0, 4, y), lim(4 - 2 * sqrt(4 - y), 4, '-', y), integral(1 / (x - 1) ** 2, 1, 2),
                         lim(1 / (c_ - 1) - 1, 1, '+', c_)], [4, 4, oo, oo]), 1,
                  r"Resultado: a) $4$; b) diverge ($+\infty$)"),
        'pr-c2': (lista([integral(1 / sqrt(1 - x ** 2), 0, 1), sp.simplify(sp.diff(2 * sqrt(x) * ln(x) - 4 * sqrt(x), x) - ln(x) / sqrt(x)),
                         lim(2 * sqrt(c_) * ln(c_), 0, '+', c_), r(quad(ln(x) / sqrt(x), 0, 1), 6)], [pi / 2, 0, 0, -4]), 1,
                  r"Resultado: a) $\frac\pi2$; b) $-4$"),
        'pr-d1': (lista([integral(x ** R(-4, 3), 1, oo), integral(x ** R(-4, 3), 0, 1), integral(x ** R(-1, 3), 0, 8)], [3, oo, 6]), 1,
                  r"Resultado: a) converge (vale $3$); b) diverge; c) converge (vale $6$)"),
        'pr-d2': (lista([integral(1 / t ** R(3, 2), 1, oo, t), 1 / (R(3, 2) - 1), integral(1 / t ** R(1, 2), 0, 1, t), 1 / (1 - R(1, 2)),
                         integral(1 / (x - 1) ** 3, 2, oo), integral(1 / sqrt(x - 1), 1, 2), integral(1 / t, 1, oo, t), integral(1 / t, 0, 1, t)],
                        [2, 2, 2, 2, R(1, 2), 2, oo, oo]), 1,
                  r"Resultado: $\int_2^\infty\frac{dx}{(x-1)^p}$ converge $\iff p&gt;1$ (vale $\frac1{p-1}$); $\int_1^2\frac{dx}{(x-1)^p}$ converge $\iff p&lt;1$ (vale $\frac1{1-p}$); $\int_2^\infty\frac{dx}{(x-1)^3}=\frac12$ y $\int_1^2\frac{dx}{\sqrt{x-1}}=2$"),
        'pr-e1': (lista([integral(x ** -3, 1, oo), si(sp.N(quad(1 / (x ** 3 + x + 1), 1, mp.inf)) < R(1, 2)), integral(1 / x, 1, oo),
                         si(all(2 + cos(v) >= 1 for v in [0, 1, 2, 3, pi]))], [R(1, 2), 1, oo, 1]), 1,
                  r"Resultado: a) converge; b) diverge"),
        'pr-e2': (lista([integral(ln(x) / x ** 3, 1, oo), integral(x ** -2, 1, oo), integral(1 / x ** 2, 0, 1), si(cos(1) > 0),
                         sp.diff(x - ln(x), x)], [R(1, 4), 1, oo, 1, 1 - 1 / x]), 1,
                  r"Resultado: a) converge (vale $\frac14$); b) diverge"),
        'pr-f1': (lista([lim((x + 3) / (x ** 3 + 2 * x ** 2 + 5) / x ** -2, oo, '-'), lim(sqrt(x) / (x + 1) / (1 / sqrt(x)), oo, '-'),
                         integral(x ** -2, 1, oo), integral(1 / sqrt(x), 1, oo)], [1, 1, 1, oo]), 1,
                  r"Resultado: a) converge; b) diverge"),
        'pr-f2': (lista([lim(1 / (exp(x) - 1) / (1 / x), 0), integral(1 / x, 0, 1), lim(sen(1 / x ** 2) / x ** -2, oo, '-'), integral(x ** -2, 1, oo),
                         si(1 < pi)], [1, oo, 1, 1, 1]), 1,
                  r"Resultado: a) diverge; b) converge"),
        'pr-g1': (lista([integral((y - 1) ** R(-2, 3), 1, 3, y), integral(1 / sp.cbrt((1 - y) ** 2), 0, 1, y),
                         3 * sp.cbrt(2) + 3, r(3 + 3 * sp.cbrt(2), 3), r(quad(1 / sp.cbrt((1 - x) ** 2), 0, 1) + quad(1 / sp.cbrt((x - 1) ** 2), 1, 3), 6)],
                        [3 * sp.cbrt(2), 3, 3 + 3 * 2 ** R(1, 3), R('6.780'), r(3 + 3 * sp.cbrt(2), 6)]), 1,
                  r"Resultado: converge y vale $3+3\sqrt[3]2\approx6{,}780$"),
        'pr-g2': (lista([integral(exp(-sqrt(x)) / sqrt(x), 0, oo), integral(2 * exp(-t), 0, oo, t), integral(exp(-sqrt(x)) / sqrt(x), 0, 1),
                         integral(1 / sqrt(x), 0, 1), integral(y / (1 + y ** 2), 0, oo, y)], [2, 2, 2 - 2 / E_, 2, oo]), 1,
                  r"Resultado: a) converge y vale $2$; b) diverge (cada mitad diverge)"),
    }
    for eid, (val, esp, txt) in P.items():
        if (EJ / f'{eid}.html').exists() or (EJ / f'{eid}.solucion.html').exists():
            c(eid, 'resultado de la práctica', val, esp, txt)
    return P
