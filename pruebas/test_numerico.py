"""Resultados de los ejercicios recalculados con sympy (`pruebas/numerico/tX_Y.py`) y buscados en la solución de la página.

Cada fichero define `comprobaciones(c)`; c(ejercicio, descripción, valor_sympy, esperado, trozo_latex).
Falla si sympy no da lo esperado o si la solución escrita en `contenido/` no contiene ese resultado.
Un tema migrado sin fichero numérico solo avisa (lista en `test_cobertura_numerica`).
"""
import importlib.util
import pathlib
import re
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import sympy as sp  # noqa: E402
from comun import CONTENIDO, leer, temas_datos  # noqa: E402

NUM = pathlib.Path(__file__).resolve().parent / 'numerico'


def canon(t):
    t = re.sub(r'<[^>]+>', '', t)
    t = re.sub(r'\\(?:displaystyle|,|;|!|:|\s)|\s|&nbsp;|\u00a0', '', t)
    return t.replace(r'\dfrac', r'\frac').replace(r'\tfrac', r'\frac')


def cargar(ruta):
    spec = importlib.util.spec_from_file_location(ruta.stem, ruta)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def iguales(a, b):
    a, b = sp.sympify(a), sp.sympify(b)
    if a in (sp.oo, -sp.oo) or b in (sp.oo, -sp.oo):
        return a == b
    return sp.simplify(a - b) == 0


class Numerico(unittest.TestCase):
    def test_resultados_de_los_ejercicios(self):
        for ruta in sorted(NUM.glob('t*.py')):
            clave = ruta.stem[1:].replace('_', '.')
            carpeta = CONTENIDO / ('tema_' + ruta.stem[1:])
            self.assertTrue(carpeta.exists(), f'{ruta.name}: no existe {carpeta.name}')
            casos = []
            cargar(ruta).comprobaciones(lambda *a: casos.append(a))
            self.assertTrue(casos)
            for ej, desc, val, esperado, latex in casos:
                with self.subTest(tema=clave, ejercicio=ej, dato=desc):
                    self.assertTrue(iguales(val, esperado), f'sympy da {val}, la página dice {esperado}')
                    e = carpeta / 'ejercicios'
                    ficheros = [e / f'{ej}.solucion.html', e / f'{ej}.html']
                    f = next((x for x in ficheros if x.exists()), None)
                    self.assertIsNotNone(f, f'falta el ejercicio {ej}')
                    self.assertIn(canon(latex), canon(leer(f)), f'{ej}: «{latex}» no aparece en la solución')

    def test_cobertura_numerica(self):
        """Todos los ejercicios de un tema con fichero numérico deben tener al menos una comprobación (salvo los de teoría pura)."""
        for ruta in sorted(NUM.glob('t*.py')):
            carpeta = CONTENIDO / ('tema_' + ruta.stem[1:])
            casos = []
            cargar(ruta).comprobaciones(lambda *a: casos.append(a))
            con = {c[0] for c in casos}
            for j in sorted((carpeta / 'ejercicios').glob('*.json')):
                with self.subTest(ejercicio=j.stem, tema=ruta.stem):
                    self.assertIn(j.stem, con, f'{j.stem} sin comprobación numérica')

    def test_temas_sin_fichero_numerico_informados(self):
        """Informativo: no falla (los temas aún sin pruebas numéricas se irán añadiendo)."""
        faltan = [c for c, d, _ in temas_datos() if not (NUM / ('t' + d.name[5:] + '.py')).exists()]
        if faltan:
            print('\n[aviso] temas migrados sin pruebas numéricas:', faltan)
