"""Contenido de un tema como datos (`contenido/tema_X_Y/`) <-> página HTML (`temas/`).

  python3 herramientas/tema_datos.py migrar temas/tema_2_3_lhopital.html 2.3   # HTML -> contenido/tema_2_3/ (una sola vez por tema)
  python3 herramientas/tema_datos.py generar 2.3                               # contenido/tema_2_3/ -> temas/<archivo>.html
  python3 herramientas/tema_datos.py equivale 2.3 [pagina.html]                # la página regenerada == la publicada (tras normalizar espacios)

La clave de tema es «X.Y» (p. ej. 2.3); para 5.4-5.5 se usa «5.4-5.5». Carpeta: `contenido/tema_5_4_5_5/`.

Estructura de `contenido/tema_X_Y/`:
  tema.json        metadatos (archivo, títulos, cabecera, chips, `head`, pie), `examenes_requeridos`,
                   `num_ejercicios` y `bloques` (el orden de la página, un bloque por línea)
  estilo.css       el <style> propio del tema (si lo tiene)
  leyenda.html     la leyenda de fuentes de la cabecera
  partes/*.html    fragmentos tal cual (teoría, cajas, figuras, tablas, interactivos, quiz, chuleta…)
  ejercicios/      un ejercicio por id:
                     <id>.json              metadatos (forma, tipo E/propio/examen/practica, nivel, minimo, extra, título, fuente…)
                     <id>.enunciado.html + <id>.solucion.html     (forma «tarjeta»: article.ejer)
                     <id>.html              cuerpo (formas «details» —details.sol— y «practica» —details.pr—)
Tipos de bloque en `bloques`:
  {"t":"c","texto":"<!-- … -->"}       comentario HTML     {"t":"h2","attrs":…,"n":…,"html":…}   encabezado de sección
  {"t":"parte","archivo":"…"}          fragmento            {"t":"ej","ref":"<id>"}              ejercicio
  {"t":"cont","abre":"<div …>","cierra":"</div>","hijos":[…]}   contenedor con bloques dentro (p. ej. div.pract)
Los HTML de `temas/` están generados: no se editan a mano.
"""
import json
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
AVISO = '<!-- GENERADO desde contenido/{dir}/ con herramientas/tema_datos.py; no editar a mano -->'
AVISO_RE = re.compile(r'<!-- GENERADO desde [^>]*-->\s*')

TOP = '''</head>
<body>
<div class="topbar"><div class="in">
  <a href="../index.html">← Índice de temas</a>
  <span><button id="btn-sol" type="button">Mostrar soluciones</button> <button id="btn-tema" type="button">Claro / oscuro</button></span>
</div></div>

<div class="layout">
<nav class="side-toc" aria-label="Índice del tema"><b>En esta página</b></nav>
<main>
'''
POST = '''</main>
</div>
</body>
</html>
'''
NIVELES = {1: '★ Básico', 2: '★★ Medio', 3: '★★★ Difícil'}
TIPO_DE_FUENTE = {'E': 'E', 'P': 'propio', 'X': 'examen'}   # otras fuentes (U, S, L): «ejemplo» de un libro
SRC_RE = re.compile(r'<span class="src" data-l="(\w)" data-ref="([^"]*)">([^<]*)</span>')
ABRE = re.compile(r'<!--.*?-->|<(\w+)([^>]*)>', re.S)
VACIOS = {'br', 'hr', 'img', 'meta', 'link', 'input'}
BLOQUE = ('div p details summary article header footer h1 h2 h3 h4 h5 h6 li ul ol table tr td th thead tbody figure figcaption '
          'section dl dt dd main nav script style link meta br title head body html').split()


# ---------------------------------------------------------------- utilidades
def clave_dir(clave):
    return 'tema_' + re.sub(r'[.\-]', '_', clave)


def src_html(d):
    return f'<span class="src" data-l="{d["l"]}" data-ref="{d["ref"]}">{d["txt"]}</span>'


def src_dict(m):
    return {'l': m.group(1), 'ref': m.group(2), 'txt': m.group(3)}


def norm(s):
    """Normaliza espacios: runs -> un espacio; se quitan los de alrededor de etiquetas de bloque (no cambian el render)."""
    s = AVISO_RE.sub('', s)
    s = re.sub(r'\s+', ' ', s)
    t = '|'.join(BLOQUE)
    s = re.sub(r'\s*(</?(?:%s)\b[^>]*>)\s*' % t, r'\1', s)
    s = re.sub(r'\s*(<!--.*?-->)\s*', r'\1', s)
    return s.strip()


def top_level(s):
    """Divide un fragmento en elementos de primer nivel: ('comentario'|'texto'|etiqueta, cadena completa, apertura)."""
    out, pos = [], 0
    while True:
        m = ABRE.search(s, pos)
        if not m:
            if s[pos:].strip():
                out.append(('texto', s[pos:].strip(), ''))
            return out
        if s[pos:m.start()].strip():
            out.append(('texto', s[pos:m.start()].strip(), ''))
        if m.group(0).startswith('<!--'):
            out.append(('comentario', m.group(0), '')); pos = m.end(); continue
        tag = m.group(1)
        if tag in VACIOS:
            out.append((tag, m.group(0), m.group(0))); pos = m.end(); continue
        depth, i = 1, m.end()
        tok = re.compile(r'<(/?)' + tag + r'\b[^>]*>')
        while depth:
            t = tok.search(s, i)
            assert t, 'sin cierre de ' + tag + ': ' + s[m.start():m.start() + 80]
            depth += -1 if t.group(1) else 1
            i = t.end()
        out.append((tag, s[m.start():i], m.group(0)))
        pos = i


def slug(t):
    return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')


def leer_json(p):
    return json.loads(pathlib.Path(p).read_text(encoding='utf8'))


def escribir(p, s):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s.strip() + '\n', encoding='utf8')


def volcar_tema(meta):
    """JSON legible: un bloque por línea."""
    bl = meta.pop('bloques')
    txt = json.dumps(meta, ensure_ascii=False, indent=1)
    meta['bloques'] = bl
    lineas = ',\n'.join('  ' + json.dumps(b, ensure_ascii=False) for b in bl)
    return txt[:-2] + ',\n "bloques": [\n' + lineas + '\n ]\n}\n'


# ---------------------------------------------------------------- HTML -> datos
class Migrador:
    def __init__(self, clave):
        self.clave = clave
        self.dir = RAIZ / 'contenido' / clave_dir(clave)
        self.sec, self.n = 'inicio', 0
        self.ids = set()
        self.cuenta = {'E': 0, 'propio': 0, 'examen': 0, 'practica': 0, 'ejemplo': 0}
        self.examenes = []

    # -- ejercicios
    def _id_libre(self, base):
        base = base or 'ej'
        i, k = base, 2
        while i in self.ids:
            i = f'{base}-{k}'; k += 1
        self.ids.add(i)
        return i

    def _tarjeta(self, outer, abre):
        m = re.fullmatch(r'<article class="ejer"(?: id="([\w-]+)")?( data-extra)?>', abre)
        assert m, abre
        inner = outer[len(abre):-len('</article>')].strip()
        h = re.match(r'<header class="ejer-cab"><span class="nv n([123])">([^<]*)</span>(<span class="nv min">Mínimo</span>)?'
                     r'<span class="tit">(.*?)</span> (<span class="src".*?</span>)</header>\s*', inner, re.S)
        assert h, inner[:200]
        assert NIVELES[int(h.group(1))] == h.group(2), h.group(2)
        src = SRC_RE.fullmatch(h.group(5)); assert src, h.group(5)
        resto = inner[h.end():]
        el = top_level(resto)
        assert [e[0] for e in el] == ['div', 'details'], [e[0] for e in el]
        en = re.fullmatch(r'<div class="ejer-enun">(.*)</div>', el[0][1], re.S); assert en
        so = re.fullmatch(r'<details class="sol"><summary>(.*?)</summary>(.*)</details>', el[1][1], re.S); assert so
        eid = self._id_libre(m.group(1) or slug(re.sub(r'<[^>]+>|\$', '', h.group(4)))[:30])
        tipo = TIPO_DE_FUENTE[src.group(1)]
        meta = {'id': eid, 'forma': 'tarjeta', 'tipo': tipo, 'nivel': int(h.group(1)), 'minimo': bool(h.group(3)),
                'extra': bool(m.group(2)), 'titulo': h.group(4), 'src': src_dict(src), 'resumen_sol': so.group(1)}
        if not m.group(1):
            meta['sin_id'] = True
        e = self.dir / 'ejercicios'
        escribir(e / f'{eid}.json', json.dumps(meta, ensure_ascii=False, indent=1))
        escribir(e / f'{eid}.enunciado.html', en.group(1))
        escribir(e / f'{eid}.solucion.html', so.group(2))
        self._registra(tipo, eid)
        return {'t': 'ej', 'ref': eid}

    def _practica(self, outer, abre):
        m = re.fullmatch(r'<details class="pr"(?: id="([\w-]+)")?( data-extra)?>', abre)
        assert m, abre
        s = re.fullmatch(r'<details class="pr"[^>]*><summary><span class="nv n([123])">([^<]*)</span> (.*?) (<span class="src".*?</span>)</summary>(.*)</details>', outer, re.S)
        assert s, outer[:200]
        assert NIVELES[int(s.group(1))] == s.group(2)
        src = SRC_RE.fullmatch(s.group(4)); assert src
        eid = self._id_libre(m.group(1) or 'pr')
        meta = {'id': eid, 'forma': 'practica', 'tipo': 'practica', 'nivel': int(s.group(1)), 'extra': bool(m.group(2)),
                'titulo': s.group(3), 'src': src_dict(src)}
        if not m.group(1):
            meta['sin_id'] = True
        e = self.dir / 'ejercicios'
        escribir(e / f'{eid}.json', json.dumps(meta, ensure_ascii=False, indent=1))
        escribir(e / f'{eid}.html', s.group(5))
        self._registra('practica', eid)
        return {'t': 'ej', 'ref': eid}

    def _details(self, outer, abre):
        m = re.fullmatch(r'<details class="sol"(?: id="([\w-]+)")?( data-extra)?>', abre)
        assert m, abre
        s = re.fullmatch(r'<details class="sol"[^>]*>\s*<summary>(.*?) ((?:<span class="src"[^>]*>[^<]*</span>\s*)+)</summary>(.*)</details>', outer, re.S)
        assert s, outer[:200]
        srcs = [SRC_RE.fullmatch(x) for x in re.findall(r'<span class="src"[^>]*>[^<]*</span>', s.group(2))]
        assert all(srcs), s.group(2)
        eid = self._id_libre(m.group(1) or slug(re.sub(r'<[^>]+>|\$', '', s.group(1)))[:30])
        tipo = TIPO_DE_FUENTE.get(srcs[0].group(1), 'ejemplo')
        meta = {'id': eid, 'forma': 'details', 'tipo': tipo, 'extra': bool(m.group(2)), 'titulo': s.group(1), 'src': src_dict(srcs[0])}
        if len(srcs) > 1:
            meta['src_mas'] = [src_dict(x) for x in srcs[1:]]
        if not m.group(1):
            meta['sin_id'] = True
        e = self.dir / 'ejercicios'
        escribir(e / f'{eid}.json', json.dumps(meta, ensure_ascii=False, indent=1))
        escribir(e / f'{eid}.html', s.group(3))
        self._registra(tipo, eid)
        return {'t': 'ej', 'ref': eid}

    def _registra(self, tipo, eid):
        self.cuenta[tipo] += 1
        if tipo == 'examen':
            self.examenes.append(eid)

    # -- bloques
    def _parte(self, outer, tag, clase):
        self.n += 1
        nombre = f'{self.sec}-{self.n:02d}-{slug(clase or tag)}.html'
        escribir(self.dir / 'partes' / nombre, outer)
        return {'t': 'parte', 'archivo': nombre}

    def bloques(self, html):
        out = []
        for tag, outer, abre in top_level(html):
            cls = (re.search(r'class="([^"]*)"', abre) or [None, ''])[1] if abre else ''
            if tag == 'comentario':
                out.append({'t': 'c', 'texto': outer})
            elif tag == 'h2':
                m = re.fullmatch(r'<h2([^>]*)><span class="n">(.*?)</span>(.*)</h2>', outer, re.S)
                assert m, outer[:100]
                idm = re.search(r'id="([\w-]+)"', m.group(1))
                self.sec = idm.group(1) if idm else self.sec
                self.n = 0
                out.append({'t': 'h2', 'attrs': m.group(1), 'n': m.group(2), 'html': m.group(3)})
            elif tag == 'article' and cls == 'ejer':
                out.append(self._tarjeta(outer, abre))
            elif tag == 'details' and cls == 'sol':
                out.append(self._details(outer, abre))
            elif tag == 'details' and cls == 'pr':
                out.append(self._practica(outer, abre))
            elif tag == 'div' and cls == 'pract':
                inner = outer[len(abre):-len('</div>')]
                out.append({'t': 'cont', 'abre': abre, 'cierra': '</div>', 'hijos': self.bloques(inner)})
            else:
                out.append(self._parte(outer, tag, cls))
        return out

    def migrar(self, ruta):
        s = pathlib.Path(ruta).read_text(encoding='utf8')
        s = AVISO_RE.sub('', s)
        i_head = s.index('</head>')
        cabeza, resto = s[:i_head], s[i_head:]
        assert resto.startswith(TOP), 'la parte superior del cuerpo no es la estándar'
        assert resto.endswith(POST), 'el final de la página no es el estándar'
        main = resto[len(TOP):-len(POST)]
        hm = re.match(r'<!DOCTYPE html>\s*<html([^>]*)>\s*<head>\s*<meta charset="utf-8">\n(.*)', cabeza, re.S)
        assert hm, cabeza[:100]
        lineas = hm.group(2)
        titulo_pagina = re.search(r'<title>(.*?)</title>', lineas).group(1)
        lineas = lineas.replace(f'<title>{titulo_pagina}</title>', '{{titulo}}')
        estilos = re.findall(r'<style>.*?</style>', lineas, re.S)
        assert len(estilos) <= 1
        if estilos:
            lineas = lineas.replace(estilos[0], '{{estilo}}')
            escribir(self.dir / 'estilo.css', re.fullmatch(r'<style>(.*)</style>', estilos[0], re.S).group(1))
        meta = {'clave': self.clave, 'archivo': pathlib.Path(ruta).name, 'html_attrs': hm.group(1),
                'titulo_pagina': titulo_pagina, 'head': lineas.strip('\n').split('\n')}
        # cabecera (hero) y pie
        el = top_level(main)
        assert el[0][0] == 'header' and 'class="hero"' in el[0][2], el[0][:2]
        assert el[-1][0] == 'footer', el[-1][:2]
        h = re.fullmatch(r'<header class="hero">\s*<div class="kick">(.*?)</div>\s*<h1>(.*?)</h1>\s*<p>(.*?)</p>\s*'
                         r'<div class="chips">(.*?)</div>\s*(<div class="legend">.*?</div>)?\s*</header>', el[0][1], re.S)
        assert h, el[0][1][:300]
        chips = re.findall(r'<span[^>]*>.*?</span>', h.group(4), re.S)
        assert ''.join(chips) == h.group(4).strip()
        meta.update({'kick': h.group(1), 'titulo': h.group(2), 'descripcion': h.group(3), 'chips': chips,
                     'pie': re.fullmatch(r'<footer>(.*)</footer>', el[-1][1], re.S).group(1)})
        if h.group(5):
            escribir(self.dir / 'leyenda.html', h.group(5))
        cuerpo = main[main.index(el[0][1]) + len(el[0][1]):main.rindex(el[-1][1])]
        meta['bloques'] = self.bloques(cuerpo)
        meta['examenes_requeridos'] = self.examenes
        meta['num_ejercicios'] = {k: v for k, v in self.cuenta.items() if v}
        escribir(self.dir / 'tema.json', volcar_tema(meta))
        return meta


# ---------------------------------------------------------------- datos -> HTML
class Generador:
    def __init__(self, clave):
        self.clave = clave
        self.dirname = clave_dir(clave)
        self.dir = RAIZ / 'contenido' / self.dirname
        self.t = leer_json(self.dir / 'tema.json')

    def leer(self, *p):
        return (self.dir.joinpath(*p)).read_text(encoding='utf8').strip()

    def ejercicio(self, eid):
        m = leer_json(self.dir / 'ejercicios' / f'{eid}.json')
        idattr = '' if m.get('sin_id') else f' id="{m["id"]}"'
        extra = ' data-extra' if m.get('extra') else ''
        src = src_html(m['src']) + ''.join(' ' + src_html(x) for x in m.get('src_mas', []))
        f = m['forma']
        if f == 'tarjeta':
            cab = (f'<header class="ejer-cab"><span class="nv n{m["nivel"]}">{NIVELES[m["nivel"]]}</span>'
                   + ('<span class="nv min">Mínimo</span>' if m.get('minimo') else '')
                   + f'<span class="tit">{m["titulo"]}</span> {src}</header>')
            return (f'<article class="ejer"{idattr}{extra}>\n{cab}\n<div class="ejer-enun">{self.leer("ejercicios", eid + ".enunciado.html")}</div>\n'
                    f'<details class="sol"><summary>{m["resumen_sol"]}</summary>\n{self.leer("ejercicios", eid + ".solucion.html")}\n</details>\n</article>\n')
        if f == 'practica':
            return (f'<details class="pr"{idattr}{extra}><summary><span class="nv n{m["nivel"]}">{NIVELES[m["nivel"]]}</span> {m["titulo"]} {src}</summary>\n'
                    f'{self.leer("ejercicios", eid + ".html")}\n</details>\n')
        if f == 'details':
            return f'<details class="sol"{idattr}{extra}><summary>{m["titulo"]} {src}</summary>\n{self.leer("ejercicios", eid + ".html")}\n</details>\n'
        raise ValueError(f)

    def bloque(self, b):
        t = b['t']
        if t == 'c':
            return b['texto'] + '\n'
        if t == 'h2':
            return f'<h2{b["attrs"]}><span class="n">{b["n"]}</span>{b["html"]}</h2>\n'
        if t == 'parte':
            return self.leer('partes', b['archivo']) + '\n'
        if t == 'ej':
            return self.ejercicio(b['ref'])
        if t == 'cont':
            return b['abre'] + '\n' + ''.join(self.bloque(x) for x in b['hijos']) + b['cierra'] + '\n'
        raise ValueError(t)

    def pagina(self):
        t = self.t
        estilo = self.leer('estilo.css') if (self.dir / 'estilo.css').exists() else None
        cab = ['<!DOCTYPE html>', AVISO.format(dir=self.dirname), f'<html{t["html_attrs"]}>', '<head>', '<meta charset="utf-8">']
        for l in t['head']:
            if l == '{{titulo}}':
                l = f'<title>{t["titulo_pagina"]}</title>'
            elif l == '{{estilo}}':
                l = f'<style>\n{estilo}\n</style>'
            cab.append(l)
        chips = ''.join(t['chips'])
        ley = (self.dir / 'leyenda.html')
        hero = ('<header class="hero">\n  <div class="kick">' + t['kick'] + '</div>\n  <h1>' + t['titulo'] + '</h1>\n  <p>' + t['descripcion']
                + '</p>\n  <div class="chips">' + chips + '</div>\n' + ('  ' + ley.read_text(encoding='utf8').strip() + '\n' if ley.exists() else '') + '</header>\n')
        cuerpo = ''.join(self.bloque(b) for b in t['bloques'])
        return '\n'.join(cab) + '\n' + TOP + '\n' + hero + '\n' + cuerpo + '\n<footer>' + t['pie'] + '</footer>\n' + POST

    def escribir(self):
        p = RAIZ / 'temas' / self.t['archivo']
        p.write_text(self.pagina(), encoding='utf8')
        return p


def equivale(clave, ruta=None):
    g = Generador(clave)
    ref = pathlib.Path(ruta) if ruta else RAIZ / 'temas' / g.t['archivo']
    a, b = norm(g.pagina()), norm(ref.read_text(encoding='utf8'))
    if a == b:
        return True, ''
    n = min(len(a), len(b))
    i = next((k for k in range(n) if a[k] != b[k]), n)
    return False, f'DIFERENCIA en {i}\n generada: {a[max(0, i - 100):i + 140]}\n publicada: {b[max(0, i - 100):i + 140]}'


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    cmd = sys.argv[1]
    if cmd == 'migrar':
        ruta, clave = sys.argv[2], sys.argv[3]
        mg = Migrador(clave)
        meta = mg.migrar(ruta)
        print('OK datos en', mg.dir.relative_to(RAIZ), '·', meta['num_ejercicios'], '·', len(meta['bloques']), 'bloques')
        ok, msg = equivale(clave, ruta)
        print('equivale:', 'OK' if ok else msg)
        sys.exit(0 if ok else 1)
    elif cmd == 'generar':
        print('OK', Generador(sys.argv[2]).escribir().relative_to(RAIZ))
    elif cmd == 'equivale':
        ok, msg = equivale(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
        print('OK la página regenerada equivale a la publicada' if ok else msg)
        sys.exit(0 if ok else 1)
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main()
