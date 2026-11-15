"""Utilidades comunes de las pruebas."""
import json
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
TEMAS = RAIZ / 'temas'
CONTENIDO = RAIZ / 'contenido'
sys.path.insert(0, str(RAIZ / 'herramientas'))


def leer(p):
    return pathlib.Path(p).read_text(encoding='utf8').replace('\r\n', '\n')


def temas_datos():
    """[(clave, carpeta, tema.json cargado)] de los temas migrados a `contenido/`."""
    out = []
    for tj in sorted(CONTENIDO.glob('tema_*/tema.json')):
        out.append((json.loads(tj.read_text(encoding='utf8'))['clave'], tj.parent, json.loads(tj.read_text(encoding='utf8'))))
    return out


def paginas():
    """Todas las páginas de `temas/` (migradas o no): [Path]."""
    return sorted(TEMAS.glob('tema_*.html'))


def sin_svg(t):
    return re.sub(r'<(script|style)\b.*?</\1>', '', re.sub(r'<svg\b.*?</svg>', '<svg/>', t, flags=re.S), flags=re.S)
