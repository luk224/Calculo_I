"""Integridad de `contenido/tema_X_Y/`: referencias, huérfanos, exámenes requeridos, nº de ejercicios y página sin retoques a mano."""
import json
import re
import sys
import unittest

sys.path.insert(0, __import__('pathlib').Path(__file__).resolve().parent.as_posix())
from comun import RAIZ, TEMAS, leer, temas_datos  # noqa: E402
import tema_datos  # noqa: E402


def refs(bloques):
    for b in bloques:
        if b['t'] == 'ej':
            yield 'ej', b['ref']
        elif b['t'] == 'parte':
            yield 'parte', b['archivo']
        elif b['t'] == 'cont':
            yield from refs(b['hijos'])


class Contenido(unittest.TestCase):
    def test_hay_temas(self):
        self.assertTrue(temas_datos(), 'no hay ningún contenido/tema_X_Y/tema.json')

    def test_referencias_y_huerfanos(self):
        for clave, d, t in temas_datos():
            with self.subTest(tema=clave):
                self.assertEqual(d.name, tema_datos.clave_dir(clave))
                partes, ejs = set(), set()
                for tipo, r in refs(t['bloques']):
                    if tipo == 'parte':
                        partes.add(r)
                        self.assertTrue((d / 'partes' / r).exists(), f'falta parte {r}')
                    else:
                        ejs.add(r)
                        self.assertTrue((d / 'ejercicios' / f'{r}.json').exists(), f'falta ejercicio {r}')
                for p in (d / 'partes').glob('*.html'):
                    self.assertIn(p.name, partes, f'fragmento huérfano: {p.name}')
                for j in (d / 'ejercicios').glob('*.json'):
                    self.assertIn(j.stem, ejs, f'ejercicio huérfano: {j.name}')
                tema_datos.Generador(clave)  # ids de ejercicio únicos
                self.assertEqual(len(ejs), sum(1 for _ in (d / 'ejercicios').glob('*.json')))
                self.assertEqual(len(list(refs(t['bloques']))), len(set(refs(t['bloques']))), 'bloque repetido')

    def test_examenes_requeridos_presentes(self):
        for clave, d, t in temas_datos():
            with self.subTest(tema=clave):
                self.assertTrue(t['examenes_requeridos'], 'el tema no registra exámenes requeridos')
                for eid in t['examenes_requeridos']:
                    j = d / 'ejercicios' / f'{eid}.json'
                    self.assertTrue(j.exists(), f'examen requerido ausente: {eid}')
                    m = json.loads(j.read_text(encoding='utf8'))
                    self.assertEqual(m['tipo'], 'examen', eid)
                    self.assertTrue(m['src']['l'] == 'X' and m['src']['ref'].startswith(('X p.', 'X pp.')), eid)
                # todos los exámenes presentes están registrados
                reales = {json.loads(j.read_text(encoding='utf8'))['id'] for j in (d / 'ejercicios').glob('*.json')
                          if json.loads(j.read_text(encoding='utf8'))['tipo'] == 'examen'}
                self.assertEqual(reales, set(t['examenes_requeridos']), 'examen sin registrar en tema.json')

    def test_numero_de_ejercicios_no_baja(self):
        for clave, d, t in temas_datos():
            with self.subTest(tema=clave):
                hoy = {}
                for j in (d / 'ejercicios').glob('*.json'):
                    k = json.loads(j.read_text(encoding='utf8'))['tipo']
                    hoy[k] = hoy.get(k, 0) + 1
                for k, n in t['num_ejercicios'].items():
                    self.assertGreaterEqual(hoy.get(k, 0), n, f'bajan los ejercicios de tipo «{k}»: {hoy.get(k, 0)} < {n} (si es deliberado, actualiza num_ejercicios)')
                # en la página: cada ejercicio aparece una vez
                pagina = leer(TEMAS / t['archivo'])
                self.assertEqual(len(re.findall(r'<(?:article class="ejer"|details class="(?:sol|pr)")', pagina)) - len(re.findall(r'<article class="ejer"[^>]*>.*?<details class="sol"', pagina, re.S)),
                                 sum(hoy.values()))

    def test_pagina_generada_sin_retoques_a_mano(self):
        for clave, d, t in temas_datos():
            with self.subTest(tema=clave):
                ok, msg = tema_datos.equivale(clave)
                self.assertTrue(ok, 'la página difiere de lo que genera contenido/ (¿editada a mano? regenera con herramientas/construir.py)\n' + msg)
                self.assertIn('GENERADO desde contenido/', leer(TEMAS / t['archivo'])[:300])
