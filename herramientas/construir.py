"""Regenera todo lo generado desde `contenido/`: las páginas de `temas/` de cada tema migrado.

  python3 herramientas/construir.py            # regenera las páginas
  python3 herramientas/construir.py --probar   # regenera y ejecuta las pruebas rápidas
"""
import pathlib
import subprocess
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
H = RAIZ / 'herramientas'


def correr(*args):
    r = subprocess.run([sys.executable, *map(str, args)], cwd=RAIZ)
    if r.returncode:
        sys.exit(r.returncode)


def main():
    import json
    for d in sorted((RAIZ / 'contenido').glob('tema_*')):
        clave = json.loads((d / 'tema.json').read_text(encoding='utf8'))['clave']
        correr(H / 'tema_datos.py', 'generar', clave)
    if '--probar' in sys.argv:
        correr(RAIZ / 'pruebas' / 'ejecutar.py', '--rapido')


if __name__ == '__main__':
    main()
