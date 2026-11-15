"""Ejecuta todas las pruebas del proyecto.

  python3 pruebas/ejecutar.py            # todas
  python3 pruebas/ejecutar.py --rapido   # lo mismo, sin las que necesiten navegador (hoy no hay ninguna: reservado)
"""
import pathlib
import sys
import unittest

AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent))
sys.path.insert(0, str(AQUI))

if __name__ == '__main__':
    rapido = '--rapido' in sys.argv
    suite = unittest.TestSuite()
    for f in sorted(AQUI.glob('test_*.py')):
        if rapido and f.stem == 'test_navegador':
            continue
        suite.addTests(unittest.defaultTestLoader.loadTestsFromName('pruebas.' + f.stem))
    r = unittest.TextTestRunner(verbosity=1).run(suite)
    sys.exit(0 if r.wasSuccessful() else 1)
