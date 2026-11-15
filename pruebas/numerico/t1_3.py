"""Tema 1.3 (series numéricas): cada resultado se recalcula con sympy y se comprueba que la solución de la página lo escribe.

`comprobaciones(c)`: c(ejercicio, descripción, valor_sympy, esperado, trozo_latex)
  - valor_sympy: lo que calcula sympy;  esperado: lo que afirma la página (exacto o redondeado como en la página);
  - trozo_latex: cadena que debe aparecer en `ejercicios/<ejercicio>.html` (o `.solucion.html`), comparada sin etiquetas,
    espacios ni \\displaystyle y con \\dfrac/\\tfrac = \\frac.
Las sumas numéricas de series (sympy no tiene forma cerrada) se calculan con mpmath (`nsum`) o sumando en coma flotante
hasta que la cola es despreciable frente al redondeo que escribe la página.
Las comprobaciones de la práctica «Ahora hazlo tú» (pr-*) solo se activan cuando el ejercicio existe en `contenido/`.
"""
import math
import pathlib

import mpmath as mp
import sympy as sp

n = sp.symbols('n', positive=True, integer=True)
oo = sp.oo
EJ = pathlib.Path(__file__).resolve().parents[2] / 'contenido' / 'tema_1_3' / 'ejercicios'


def L(f):
    """Límite cuando n → ∞."""
    return sp.limit(f, n, oo)


def S(f, a=1):
    """Suma exacta de la serie desde n = a."""
    return sp.summation(f, (n, a, oo))


def si(cond):
    """Comprobación lógica: 1 si se cumple (se compara con esperado = 1)."""
    return sp.Integer(1 if bool(cond) else 0)


def r(v, k=4):
    """Redondeo a k decimales (como se escribe en la página)."""
    return sp.Rational(str(round(float(v), k)))


def comprobaciones(c):
    # ---- Ejercicios del libro (E 1.17-1.22)
    c('ej-1-17', 'a_n + b_n = 1/n - 1/n = 0', sp.simplify(1 / n - 1 / n), 0, r'a_n+b_n=\frac1n-\frac1n=0')
    s18 = sum(1 / (3 + math.cos(k) + k ** 2.5) for k in range(1, 100001))
    c('ej-1-18', 'suma numérica de la serie', r(s18), sp.Rational('0.4949'), r'\sum a_n\approx0{,}4949')
    c('ej-1-18', 'serie mayorante ζ(5/2)', r(sp.zeta(sp.Rational(5, 2))), sp.Rational('1.3415'), r'\sum1/n^{5/2}\approx1{,}3415')
    s19 = math.fsum(1 / (k ** 0.5 + k ** (2 / 3)) for k in range(1, 10 ** 6 + 1))
    c('ej-1-19', 's_{10^6} (diverge)', r(s19, 1), sp.Rational('253.5'), r's_{10^6}\approx253{,}5')
    c('ej-1-19', 'minorante 1/(2n^{2/3})', si(all(sp.sqrt(j) + sp.cbrt(j) ** 2 <= 2 * sp.cbrt(j) ** 2 for j in range(1, 200))), 1, r'\ge\frac1{2n^{2/3}}')
    c('ej-1-20', 'cociente → e/2', L((1 + 1 / n) ** n * (n + 1) / (2 * n + 1)), sp.E / 2, r'\frac e2\approx1{,}359&gt;1')
    s21 = math.fsum(math.exp(math.log(k) ** 2 - k * math.log(math.log(k))) for k in range(2, 400))
    c('ej-1-21', 'suma numérica', r(s21, 2), sp.Rational('10.54'), r'\approx10{,}54')
    c('ej-1-21', 'raíz: (ln n)²/n → 0', L(sp.log(n) ** 2 / n), 0, r'\ell=0\in[0,1)')
    s22 = math.fsum((-1) ** k * math.exp(k) / (math.exp(2 * k) + 1) for k in range(1, 60))
    a22 = math.fsum(math.exp(k) / (math.exp(2 * k) + 1) for k in range(1, 60))
    c('ej-1-22', 'suma con signos', r(s22), sp.Rational('-0.2274'), r'\sum a_n\approx-0{,}2274')
    c('ej-1-22', 'suma de |a_n|', r(a22), sp.Rational('0.5356'), r'\sum|a_n|\approx0{,}5356')
    c('ej-1-22', 'mayorante geométrica', S(sp.exp(-n)), 1 / (sp.E - 1), r'\frac1{e-1}\approx0{,}5820')
    # ---- Ejemplos propios
    c('ej-a1', 'término → 1/2', L(n / (2 * n + 5)), sp.Rational(1, 2), r'\to\dfrac12\ne0')
    c('ej-a2', 'geométrica', S(3 / 2 ** n), 3, r'\dfrac{3/2}{1-1/2}=3')
    c('ej-b1', 'suma', r(mp.nsum(lambda k: (k + 1) / (k ** 3 + 2), [1, mp.inf])), sp.Rational('1.4247'), r'\approx1{,}4247')
    c('ej-b3', 'cociente → 1/e', L((n / (n + 1)) ** n), sp.exp(-1), r'\to\dfrac1e&lt;1')
    c('ej-b3', 'suma', r(mp.nsum(lambda k: mp.factorial(k) / k ** k, [1, mp.inf])), sp.Rational('1.8799'), r'\approx1{,}8799')
    c('ej-b4', 'suma', r(mp.nsum(lambda k: (k / (k + 1)) ** (k ** 2), [1, mp.inf])), sp.Rational('0.8174'), r'\approx0{,}8174')
    c('ej-c1', 'suma', r(mp.nsum(lambda k: (-1) ** k * k / (k ** 2 + 1), [1, mp.inf])), sp.Rational('-0.2696'), r'\approx-0{,}2696')
    c('ej-b2', 'minorante 1/(2√n)', si(all(sp.sqrt(j) + 1 <= 2 * sp.sqrt(j) for j in range(1, 200))), 1, r'a_n\ge\dfrac1{2\sqrt n}')
    c('ej-b4', 'raíz → 1/e', L((n / (n + 1)) ** n), sp.exp(-1), r'\sqrt[n]{a_n}=\Big(\dfrac n{n+1}\Big)^n\to\dfrac1e&lt;1')
    c('ej-c2', '|a_2| < |a_3|', si(1 / (sp.sqrt(2) + 1) < 1 / (sp.sqrt(3) - 1)), 1, r'|a_2|\approx0{,}414&lt;|a_3|\approx1{,}366')
    # ---- Exámenes
    c('ex-1', 'signos de (-1)^n alternan', si(all((-1) ** k * (-1) ** (k + 1) < 0 for k in range(1, 20))), 1, r'$a_n=(-1)^nb_n$')
    c('ex-2', 'cociente → 1/4', L(((n + 1) ** 2 / 4 ** (n + 1)) / (n ** 2 / 4 ** n)), sp.Rational(1, 4), r'\frac14(1+\frac1n)^2\to\frac14&lt;1')
    c('ex-3', 'suma = 3ζ(3)/4', r(S((-1) ** (n - 1) / n ** 3)), sp.Rational('0.9015'), r'\approx0{,}9015')
    c('ex-4', 'suma = (1-√2)ζ(1/2)', r((1 - sp.sqrt(2)) * sp.zeta(sp.Rational(1, 2)), 3), sp.Rational('0.605'), r'\approx0{,}605')
    k = sp.symbols('k', positive=True, integer=True)
    c('ex-5', 'cociente (n+1)/(n+1-k) → 1', L(sp.combsimp(sp.binomial(n + 1, k) / sp.binomial(n, k))), 1, r'=\frac{n+1}{n+1-k}\to1')
    c('ex-6', 'contraejemplo D: Σ1/n diverge, Σ1/n² = π²/6', si(S(1 / n) == oo and S(1 / n ** 2) == sp.pi ** 2 / 6), 1, r'<b>Resultado:</b> C.')
    # ---- Práctica «Ahora hazlo tú» (respuesta final = «Resultado: …»)
    P = {
        'pr-a1': (S(2 ** (n + 1) / 5 ** n, 2), sp.Rational(8, 15), r'Resultado: converge y su suma es $\frac8{15}$'),
        'pr-a2': (S((2 ** n + (-1) ** n) / 3 ** n), sp.Rational(7, 4), r'Resultado: $\frac74$'),
        'pr-b1': (S(1 / ((2 * n - 1) * (2 * n + 1))), sp.Rational(1, 2), r'Resultado: $\frac12$'),
        'pr-b2': (sp.log(sp.Rational(1, 2)) - L(sp.log(n / (n + 1))), -sp.log(2), r'Resultado: $-\ln2$'),
        'pr-c1': (L(sp.sqrt(n ** 2 + 1) / (2 * n)), sp.Rational(1, 2), r'Resultado: diverge (el término tiende a $\frac12\neq0$)'),
        'pr-c2': (L(((n - 2) / (n + 1)) ** n), sp.exp(-3), r'Resultado: diverge (el término tiende a $e^{-3}\neq0$)'),
        'pr-d1': (S(sp.Rational(1, 3) ** n), sp.Rational(1, 2), r'Resultado: converge'),
        'pr-d2': (L(sp.log(n) / n) + si(math.log(3) >= 1), 1, r'Resultado: (a) diverge; (b) converge'),
        'pr-e1': (L(3 / (n + 1)), 0, r'Resultado: converge (el cociente tiende a $0$)'),
        'pr-e2': (L(2 / (1 + 1 / n) ** n), 2 / sp.E, r'Resultado: converge (el cociente tiende a $\frac2e&lt;1$)'),
        'pr-f1': (L(n / (2 * n + 1)), sp.Rational(1, 2), r'Resultado: converge (la raíz tiende a $\frac12$)'),
        'pr-f2': (L((1 + 1 / n) ** n / 3), sp.E / 3, r'Resultado: converge (la raíz tiende a $\frac e3&lt;1$)'),
        'pr-g1': (L(((n + 1) / 2 ** (n + 1)) / (n / 2 ** n)), sp.Rational(1, 2), r'Resultado: absolutamente convergente'),
        'pr-g2': (L(sp.sqrt(n + 1) - 1) + 10 * si(sp.simplify(sp.radsimp(1 / (sp.sqrt(n) + sp.sqrt(n + 1))) - (sp.sqrt(n + 1) - sp.sqrt(n))) == 0), oo,
                  r'Resultado: condicionalmente convergente'),
    }
    for eid, (val, esp, txt) in P.items():
        if (EJ / f'{eid}.html').exists() or (EJ / f'{eid}.solucion.html').exists():
            c(eid, 'resultado de la práctica', val, esp, txt)
