"""Estructura y reglas de redacción de TODAS las páginas de `temas/` (migradas o no)."""
import json
import re
import sys
import unittest

sys.path.insert(0, __import__('pathlib').Path(__file__).resolve().parent.as_posix())
from comun import leer, paginas, sin_svg  # noqa: E402

ERRATAS = re.compile(r'errata|(?:la oficial|el libro|el solucionario|la soluci[oó]n oficial)\s*(?:se equivoca|omite)|aviso sobre el libro|c[oó]mo lo cuenta|tabla\s+lay|lay\s*↔|\bX escribe\b', re.I)


def visible(t):
    return re.sub(r'<[^>]+>', ' ', sin_svg(t))


class Paginas(unittest.TestCase):
    def test_hay_paginas(self):
        self.assertTrue(paginas())

    def test_etiquetas_balanceadas(self):
        for p in paginas():
            t = sin_svg(leer(p))
            with self.subTest(pagina=p.name):
                for tag in ('div', 'details', 'section', 'figure', 'table', 'ul', 'ol', 'span', 'main', 'article', 'header', 'footer', 'summary', 'p'):
                    self.assertEqual(len(re.findall(rf'<{tag}\b', t)), len(re.findall(rf'</{tag}>', t)), f'<{tag}> sin equilibrar')
                self.assertEqual(len(re.findall(r'<h1\b', t)), 1)

    def test_ids_unicos_y_enlaces_internos(self):
        for p in paginas():
            t = leer(p)
            ids = re.findall(r'\sid="([^"]+)"', sin_svg(t))
            with self.subTest(pagina=p.name):
                dup = sorted({i for i in ids if ids.count(i) > 1})
                self.assertFalse(dup, f'ids repetidos: {dup}')
                for h in re.findall(r'href="#([^"]+)"', t):
                    self.assertIn(h, ids, f'enlace roto #{h}')

    def test_json_de_las_graficas(self):
        for p in paginas():
            t = leer(p)
            with self.subTest(pagina=p.name):
                import html
                for g in re.findall(r"<figure class=\"graf\"[^>]*data-g='([^']*)'", t):
                    d = json.loads(html.unescape(g))
                    self.assertIsInstance(d, dict)
                    self.assertTrue(d.get('c') or d.get('p'), 'gráfica sin curvas ni puntos')

    def test_limites_con_subindice(self):
        for p in paginas():
            t = leer(p)
            with self.subTest(pagina=p.name):
                malos = re.findall(r'.{25}\\lim(?![_a-zA-Z]|\\limits_).{10}', t)
                self.assertFalse(malos, f'\\lim sin subíndice: {malos[:3]}')

    def test_sin_erratas_ni_comparativas_entre_fuentes(self):
        for p in paginas():
            with self.subTest(pagina=p.name):
                m = ERRATAS.search(visible(leer(p)))
                self.assertIsNone(m, f'regla 8 bis: «{m and m.group(0)}»')

    def test_citas_bien_formadas(self):
        for p in paginas():
            t = sin_svg(leer(p))
            with self.subTest(pagina=p.name):
                for l, ref in re.findall(r'<span class="src" data-l="([^"]*)" data-ref="([^"]*)"', t):
                    self.assertIn(l, 'UESLXP', f'clave de fuente desconocida «{l}»')
                    self.assertTrue(ref.strip(), 'cita vacía')

    def test_formulas_katex_delimitadas(self):
        """Un `$` suelto estropea el resto de la página: nº par de `$` (sin contar `\\$`)."""
        for p in paginas():
            t = re.sub(r'<(script|style)\b.*?</\1>', '', leer(p), flags=re.S)
            t = re.sub(r'<!--.*?-->', '', t, flags=re.S)
            t = re.sub(r"data-g='[^']*'", '', t)
            with self.subTest(pagina=p.name):
                self.assertEqual(len(re.findall(r'(?<!\\)\$', t)) % 2, 0, '`$` sin cerrar')
