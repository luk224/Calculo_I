#!/usr/bin/env python3
"""Genera prioridades.html («¿Por dónde empiezo?») a partir de:
  - fuentes_txt/indice_examenes_1..4.md  (una fila = una pregunta o apartado de examen de Examenes-resueltos-Calculo.pdf)
  - la cabecera «⏱ ~N h» de cada temas/tema_*.html
  - datos/dependencias.json (orden del cronograma y dependencias orientativas)
Uso:  python3 herramientas/prioridades.py

REGLAS DE MAPEO (columna «tema» del índice -> unidad de resumen 1.1 ... 6.5; 5.4 y 5.5 van juntos como «5.4-5.5»):
 1. Se excluyen las filas «fuera de examen», las de §1.5 (sucesiones/series de funciones) y «otro (Maxima)».
 2. Cada fila cuenta UNA vez, en el tema PRINCIPAL = el primer código que aparece en la cadena («1.4 / 2.1 / 2.3» -> 1.4;
    «3.4/3.5» -> 3.4). Los demás códigos son «aparece como herramienta» (columna aparte, no suma al total).
 3. Códigos genéricos (4.x, 5.x, 6.x) se asignan a una unidad por palabras clave del texto de la cadena y del enunciado:
    4.x: plano tangente/diferenciabilidad -> 5.1; gradiente, parciales, direccional, hessiana, derivadas segundas -> 4.3;
         producto escalar, normas, distancia, ángulo, ortogonal, polares, Rⁿ -> 4.1; resto (dominio, curvas de nivel,
         límites, continuidad) -> 4.2.
    5.x: implícita -> 5.3; cadena/valor medio/TVM -> 5.2; diferencial/diferenciabilidad/plano tangente -> 5.1;
         resto (extremos, Lagrange, hessiana, clasificación) -> 5.4-5.5.
    6.x: «teorema fundamental» -> 6.2; técnicas/racional/cambio de variable -> 6.3; impropia -> 6.5;
         trapecio/Simpson/numérica/error -> 6.4; suma de Riemann -> 6.1; resto (primitivas, áreas) -> 6.3.
 3b. MAPEO MANUAL (prioridad sobre las reglas anteriores): datos/mapeo_examenes.json, hecho leyendo cada enunciado.
    Formato: {"filas": {"pág|examen|nº": {"principal": "4.3", "secundarios": ["4.2"], "dudosa": true}},
              "excluir": {"pág|examen|nº": "motivo"}}
    La clave es «pág. PDF enunciado|examen|nº» tal como figura en el índice (columnas 1, 3 y 4, sin espacios
    sobrantes). «principal» = unidad que cuenta en el total (5.4 y 5.5 = «5.4-5.5»); «secundarios» = «como herramienta»;
    «excluir» = filas duplicadas en el índice (no cuentan). Las filas sin entrada usan las reglas 1-3 (palabras clave).
 4. Las filas de frontera se cuentan solo una vez para el total; la columna «herramienta» cuenta las apariciones secundarias.
Niveles: ver calcular_nivel()."""
import re, json, html, pathlib, collections

RAIZ = pathlib.Path(__file__).resolve().parent.parent
dep_json = json.loads((RAIZ / 'datos' / 'dependencias.json').read_text(encoding='utf8'))
ORDEN, DEP = dep_json['orden'], dep_json['dep']

# ---------- 1. Índice de exámenes ----------
def resolver_x(cod, tema, enun):
    t = (tema + ' ' + enun).lower()
    d = cod[0]
    if d == '4':
        if re.search(r'plano tangente', t): return '5.1'
        if re.search(r'gradiente|parcial|direccional|hessian|2ª derivadas|derivadas segundas', t): return '4.3'
        if re.search(r'producto escalar|norma|distancia|ángulo|angulo|ortogonal|polares|rⁿ|r\^n', t): return '4.1'
        return '4.2'
    if d == '5':
        if re.search(r'implícit|implicit', t): return '5.3'
        if re.search(r'cadena|valor medio|tvm', t): return '5.2'
        if re.search(r'diferencia|plano tangente', t): return '5.1'
        return '5.4-5.5'
    if d == '6':
        tl = tema.lower()
        if re.search(r'fundamental', tl): return '6.2'
        if re.search(r'técnicas|racional|cambio de variable', tl): return '6.3'
        if re.search(r'trapecio|simpson|numér|numer', t) and not re.search(r'impropia', tl): return '6.4'
        if re.search(r'impropi', t): return '6.5'
        if re.search(r'riemann|suma superior|suma inferior', t): return '6.1'
        return '6.3'
    return cod

def norm(cod, tema, enun):
    if cod in ('5.4', '5.5'): return '5.4-5.5'
    if cod.endswith('.x'): return resolver_x(cod, tema, enun)
    return cod

filas_ex = []
for i in range(1, 5):
    for l in (RAIZ / 'fuentes_txt' / f'indice_examenes_{i}.md').read_text(encoding='utf8').splitlines():
        if not l.startswith('|') or l.startswith('|---') or 'enunciado |' in l: continue
        # los enunciados pueden contener «|» sin escapar: 4 campos al principio y el tema al final
        a = l.strip().strip('|').split('|')
        if len(a) < 6: raise SystemExit('fila mal formada: ' + l[:90])
        p = [x.strip() for x in a[:4]] + ['|'.join(a[4:-1]).strip(), a[-1].strip()]
        filas_ex.append(dict(exam=p[2], n=p[3], enun=p[4], tema=p[5], clave=f'{p[0]}|{p[2]}|{p[3]}'))

MAP = json.loads((RAIZ / 'datos' / 'mapeo_examenes.json').read_text(encoding='utf8'))
MAN, EXC = MAP['filas'], MAP['excluir']
assert not (set(MAN) | set(EXC)) - {f['clave'] for f in filas_ex}, 'claves del mapeo que no existen en el índice'
cuenta = collections.Counter(); herr = collections.Counter(); excl = []
for f in filas_ex:
    t = f['tema'].lower()
    if f['clave'] in EXC:
        excl.append(f); continue
    if f['clave'] in MAN:
        m = MAN[f['clave']]
        cuenta[m['principal']] += 1
        for x in set(m['secundarios']) - {m['principal']}: herr[x] += 1
        continue
    if 'fuera' in t or t.startswith('1.5') or t.startswith('otro'):
        excl.append(f); continue
    cods = re.findall(r'\d\.[\dx]', f['tema'])
    if not cods: raise SystemExit('sin código: ' + f['tema'])
    u = [norm(c, f['tema'], f['enun']) for c in cods]
    cuenta[u[0]] += 1
    for x in set(u[1:]) - {u[0]}: herr[x] += 1
total_filas = len(filas_ex); TOT = sum(cuenta.values())
assert TOT + len(excl) == total_filas
desconocidos = [c for c in cuenta if c not in ORDEN]
assert not desconocidos, desconocidos
n_examenes = len({f['exam'] for f in filas_ex})

# ---------- 2. Temas: título, archivo, horas ----------
filas = []
for cod in ORDEN:
    pref = 'tema_' + cod.replace('.', '_').replace('-', '_') + '_'
    arch = sorted((RAIZ / 'temas').glob(pref + '*.html'))
    assert len(arch) == 1, (cod, arch)
    txt = arch[0].read_text(encoding='utf8')
    m = re.search(r'⏱ ~(\d+(?:[.,]\d+)?)(?:[–-](\d+(?:[.,]\d+)?))? h', txt)
    assert m, 'sin chip de horas en ' + arch[0].name
    nums = [float(x.replace(',', '.')) for x in m.groups() if x]
    tit = re.search(r'<title>[^·<]*·\s*([^<]*)</title>', txt).group(1).strip()
    tit = re.sub(r'^[\d.\-–\s]+(?:y\s*)?', '', tit) if cod != '5.4-5.5' else re.sub(r'^[\d.\s\-–y]+', '', tit)
    filas.append(dict(cod=cod, nombre=tit, url='temas/' + arch[0].name, h=sum(nums) / len(nums), ex=cuenta.get(cod, 0), herr=herr.get(cod, 0)))
assert len(filas) == 26
for r in filas:
    r['pct'] = 100 * r['ex'] / TOT
    r['ratio'] = r['ex'] / r['h']
    r['dep'] = DEP.get(r['cod'], [])

def calcular_nivel(r):
    """🔴 Imprescindible: >= 5 % del total de preguntas o >= 3 preguntas/hora.
       🟡 Recomendada: >= 3 % o >= 2 preguntas/hora. ⚪ Completa: el resto."""
    if r['pct'] >= 5 or r['ratio'] >= 3: return 1
    if r['pct'] >= 3 or r['ratio'] >= 2: return 2
    return 3
for r in filas: r['nivel'] = calcular_nivel(r)
por = {r['cod']: r for r in filas}

def cierre(cods):
    out, pend = set(), list(cods)
    while pend:
        c = pend.pop()
        if c in out: continue
        out.add(c); pend += DEP.get(c, [])
    return out
rutas = []
for titulo, niv, emoji, desc in [
    ('Imprescindible', 1, '🔴', 'Los temas que más caen o mejor rinden por hora, más los temas previos que necesitan.'),
    ('Recomendada', 2, '🟡', 'Lo anterior más los temas de frecuencia media.'),
    ('Completa', 3, '⚪', 'Todo el temario.')]:
    c = cierre([r['cod'] for r in filas if r['nivel'] <= niv])
    cods = sorted(c, key=ORDEN.index)
    ex = sum(por[x]['ex'] for x in cods); h = sum(por[x]['h'] for x in cods)
    rutas.append(dict(t=titulo, e=emoji, desc=desc, n=len(cods), h=h, ex=ex, pct=100 * ex / TOT, cods=cods))

def fh(x): return (f'{x:.1f}'.rstrip('0').rstrip('.') if x != int(x) else str(int(x))).replace('.', ',')
def pc(x): return f'{x:.1f}'.replace('.', ',')
NIVEL = {1: ('🔴', 'Imprescindible'), 2: ('🟡', 'Recomendada'), 3: ('⚪', 'Completa')}
mx = max(r['ex'] for r in filas) or 1

tr = []
for r in filas:
    e, n = NIVEL[r['nivel']]
    deps = ' · '.join(r['dep']) or '—'
    tr.append(
        f'<tr class="n{r["nivel"]}" data-i="{ORDEN.index(r["cod"])}" data-ex="{r["ex"]}" data-ratio="{r["ratio"]:.3f}">'
        f'<td class="tm"><a href="{r["url"]}"><b>{r["cod"]}</b> {html.escape(r["nombre"])}</a></td>'
        f'<td class="bar"><span class="fill" style="width:{100 * r["ex"] / mx:.0f}%"></span><span class="num">{r["ex"]}</span></td>'
        f'<td>{pc(r["pct"])} %</td><td>{fh(r["h"])}</td><td>{r["ratio"]:.1f}</td>'
        f'<td><span class="pr-tag t{r["nivel"]}">{e} {n}</span></td>'
        f'<td class="herr">{r["herr"] or "—"}</td><td class="dep">{deps}</td></tr>')

cards = ''.join(
    f'<div class="pr-ruta"><h3>{x["e"]} {x["t"]}</h3><p class="big">{fh(round(x["h"], 1))} h <small>· {x["n"]} temas · {pc(x["pct"])} % de las preguntas de examen</small></p>'
    f'<p>{x["desc"]}</p><p class="lst"><b>En este orden:</b> {" → ".join(x["cods"])}</p></div>' for x in rutas)

barras = ''.join(
    f'<div class="brow"><a href="{r["url"]}">{r["cod"]}</a><span class="bt"><i class="t{r["nivel"]}" style="width:{100 * r["ex"] / mx:.0f}%"></i></span><b>{pc(r["pct"])} %</b></div>'
    for r in sorted(filas, key=lambda r: (-r['ex'], ORDEN.index(r['cod']))))

nn = {k: [r['cod'] for r in filas if r['nivel'] == k] for k in (1, 2, 3)}
cero = [r['cod'] for r in filas if r['ex'] == 0]
doc = f'''<!DOCTYPE html>
<html lang="es" data-theme="light">
<head>
<meta charset="utf-8">
<script>try{{var t=localStorage.getItem('tema');if(t==='dark'||t==='light')document.documentElement.setAttribute('data-theme',t)}}catch(e){{}}</script>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Cálculo · Prioridades de estudio</title>
<link rel="stylesheet" href="assets/resumen.css">
<link rel="stylesheet" href="assets/estudio.css">
<script defer src="assets/resumen.js"></script>
</head>
<body class="prio-page">
<div class="topbar"><div class="in">
  <a href="index.html">← Índice de temas</a>
  <span><button id="btn-tema" type="button">Claro / oscuro</button></span>
</div></div>
<main class="prio-main">
<h1>🎯 ¿Por dónde empiezo? Prioridades de estudio</h1>
<p>No todos los temas «pagan» lo mismo en el examen: unos aparecen una y otra vez y otros casi nunca. Esta página cruza <b>cuánto ha caído</b> cada tema con <b>cuánto cuesta estudiarlo</b> y te propone tres rutas según el tiempo que tengas.</p>
<div class="box warn"><span class="h">Léelo con cuidado</span>
<p>Es una medida de <b>frecuencia histórica</b>, no una probabilidad de que algo caiga este año. Sirve para ordenar el esfuerzo, no para dejar temas sin ver: un tema con pocas preguntas puede ser requisito de otro que sí cae (por eso las rutas incluyen los temas previos). Las preguntas contadas son las de los exámenes de <i>Examenes-resueltos-Calculo.pdf</i> (págs. 1-152), no todos los exámenes que ha habido ni los de este curso.</p></div>

<h2>Tres rutas según tu tiempo</h2>
<div class="pr-rutas">{cards}</div>
<p class="pr-nota">Las horas de cada ruta incluyen los temas previos necesarios (columna «Necesitas antes»). Son las horas del chip «⏱» de cada tema, que corresponde al camino de estudio completo del resumen.</p>

<h2>Tema a tema</h2>
<div class="pr-ctl" role="group" aria-label="Ordenar la tabla">
  <button type="button" data-o="i" aria-pressed="true">Orden del temario</button>
  <button type="button" data-o="ex" aria-pressed="false">Más cae primero</button>
  <button type="button" data-o="ratio" aria-pressed="false">Más rentable primero</button>
</div>
<table id="tp" class="pr-tabla">
<thead><tr><th>Tema</th><th>Preguntas de examen</th><th>% total</th><th>Horas</th><th>Preg./hora</th><th>Prioridad</th><th class="herr" title="Preguntas de otro tema donde este aparece como herramienta (no suman al total)">Como herramienta</th><th class="dep">Necesitas antes</th></tr></thead>
<tbody>
{chr(10).join(tr)}
</tbody>
<tfoot><tr><td><b>Total</b></td><td><b>{TOT}</b></td><td>100 %</td><td><b>{fh(sum(r["h"] for r in filas))}</b></td><td>{TOT / sum(r["h"] for r in filas):.1f}</td><td></td><td></td><td></td></tr></tfoot>
</table>

<h2>Qué parte del examen es cada tema</h2>
<div class="pr-barras">{barras}</div>

<h2>Cómo leer los niveles</h2>
<ul>
<li>🔴 <b>Imprescindible</b> ({", ".join(nn[1])}): al menos el 5 % de las preguntas contadas o 3 o más preguntas por hora de estudio. Aquí se gana o se pierde el aprobado.</li>
<li>🟡 <b>Recomendada</b> ({", ".join(nn[2]) or "ninguno"}): entre el 3 % y el 5 %, o al menos 2 preguntas por hora. Se estudia después, en el orden del temario.</li>
<li>⚪ <b>Completa</b> ({", ".join(nn[3]) or "ninguno"}): caen poco en estos exámenes, pero siguen siendo materia{(" (" + ", ".join(cero) + ": ninguna pregunta contada)") if cero else ""}.</li>
</ul>

<h2>Cómo se ha calculado</h2>
<div class="box tip"><span class="h">Método y límites</span>
<ul>
<li><b>Cuánto cae.</b> Se han leído las 4 partes del índice de exámenes (<code>fuentes_txt/indice_examenes_1..4.md</code>), que cubre las págs. PDF 1-152 de <i>Examenes-resueltos-Calculo.pdf</i>: {total_filas} filas (una por pregunta o apartado) de unos {n_examenes} nombres de examen distintos (el mismo examen puede aparecer con nombres variantes, así que la cifra es aproximada). Se excluyen {len(excl)} filas marcadas «fuera de examen» (series y sucesiones de funciones, §1.5), ajenas a la asignatura o duplicadas en el índice; quedan <b>{TOT}</b>.</li>
<li><b>Una pregunta, un tema.</b> Cada fila se asigna una sola vez al tema principal, el primero que cita el índice (en «1.4 / 2.1 / 2.3» cuenta como 1.4). Los demás temas citados suman en «Como herramienta» ({sum(herr.values())} apariciones), pero no al total ni al porcentaje.</li>
<li><b>Códigos genéricos.</b> El índice a veces escribe solo «4.x», «5.x» o «6.x». Se han repartido <b>a mano</b>, leyendo cada enunciado (<code>datos/mapeo_examenes.json</code>; en un ejercicio de varios apartados cuenta el tema de la herramienta central y los demás van a «Como herramienta»). Criterio: producto escalar, normas, distancia y ángulo → 4.1; dominio, curvas de nivel, límites y continuidad → 4.2; gradiente, derivadas parciales, direccional y hessiana → 4.3; diferenciabilidad (y diferencial) → 5.1 (el plano tangente va con 4.3); regla de la cadena y valor medio → 5.2; función implícita → 5.3; extremos y Lagrange → 5.4-5.5 (se cuentan juntos); técnicas y primitivas → 6.3; trapecio, Simpson y error → 6.4; integrales impropias → 6.5. Los apartados «continuidad + parciales + diferenciabilidad» cuentan en 5.1 (el más exigente) y suman a 4.2 y 4.3 como herramienta.</li>
<li><b>Cuánto cuesta.</b> Las horas del chip «⏱ ~N h» de la cabecera de cada tema (si es un intervalo, su media). <b>Preg./hora</b> = preguntas de examen entre horas.</li>
<li><b>Dependencias.</b> Orientativas (criterio del autor, no del libro), en <code>datos/dependencias.json</code>.</li>
<li><b>Regenerar.</b> <code>python3 herramientas/prioridades.py</code> relee el índice y las cabeceras y reescribe esta página.</li>
</ul></div>
</main>
<script>
(function(){{
  var tb=document.querySelector('#tp tbody'),rows=[].slice.call(tb.rows);
  document.querySelectorAll('.pr-ctl button').forEach(function(b){{b.addEventListener('click',function(){{
    var o=b.dataset.o;document.querySelectorAll('.pr-ctl button').forEach(function(x){{x.setAttribute('aria-pressed',x===b?'true':'false')}});
    rows.slice().sort(function(a,c){{return o==='i'?a.dataset.i-c.dataset.i:c.dataset[o]-a.dataset[o]||a.dataset.i-c.dataset.i}}).forEach(function(r){{tb.appendChild(r)}});
  }})}});
}})();
</script>
</body>
</html>
'''
(RAIZ / 'prioridades.html').write_text(doc, encoding='utf8')
print(f'filas={total_filas} excluidas={len(excl)} contadas={TOT} exámenes(nombres)={n_examenes} herramienta={sum(herr.values())}')
print('cod\tej\t%\th\tratio\tnivel\therr')
for r in filas: print(f"{r['cod']}\t{r['ex']}\t{r['pct']:.1f}\t{fh(r['h'])}\t{r['ratio']:.1f}\t{NIVEL[r['nivel']][1]}\t{r['herr']}")
for x in rutas: print(x['t'], fh(x['h']), 'h', x['n'], 'temas', x['ex'], 'preg', pc(x['pct']), '%', ' '.join(x['cods']))
(RAIZ / 'datos' / 'temas_prioridad.json').write_text(json.dumps(filas, ensure_ascii=False, indent=1), encoding='utf8')
