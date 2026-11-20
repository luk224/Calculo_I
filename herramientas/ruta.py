#!/usr/bin/env python3
"""Genera ruta.html: calendario hacia atrás desde las PA y la PEC según las horas semanales que tengas.
Uso:  python3 herramientas/prioridades.py && python3 herramientas/ruta.py
Datos: datos/temas_prioridad.json (lo escribe prioridades.py: horas, preguntas de examen, nivel, dependencias) y los hitos del
cronograma (CLAUDE.md §2). Sin servidor: horas semanales y temas estudiados se guardan en `localStorage` (clave `ruta_calculo_v1`).
Modelo: ALGEBRA/claude/herramientas/ruta.py."""
import json, pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent
filas = json.loads((RAIZ / 'datos' / 'temas_prioridad.json').read_text(encoding='utf8'))
temas = [dict(cod=r['cod'], nombre=r['nombre'], h=round(r['h'], 2), ex=r['ex'], nivel=r['nivel'], dep=r['dep'], url=r['url']) for r in filas]
# hitos del cronograma 2026-27: (nombre, fecha, módulos que entran)
hitos = [
    dict(nombre='PA2 · módulos III y IV', fecha='2026-11-23', mods=[3, 4]),
    dict(nombre='PEC única · módulos I a V', fecha='2026-12-11', mods=[1, 2, 3, 4, 5]),
    dict(nombre='PA3 · módulos V y VI', fecha='2027-01-14', mods=[5, 6]),
]
datos = json.dumps(dict(temas=temas, hitos=hitos), ensure_ascii=False)

html = '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<script>try{var t=localStorage.getItem('tema');if(t==='dark'||t==='light')document.documentElement.setAttribute('data-theme',t)}catch(e){}</script>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Cálculo · Ruta de estudio</title>
<link rel="stylesheet" href="assets/resumen.css">
<style>
.ru main{max-width:980px;margin:0 auto;padding:24px 16px 60px}
.ru .ctl{display:flex;gap:14px;flex-wrap:wrap;align-items:center;margin:1em 0;font:15px var(--sans)}
.ru input[type=number]{font:16px var(--sans);width:5em;padding:5px 8px;border:1px solid var(--bd);border-radius:8px;background:var(--bg);color:var(--fg)}
.ru .pec{border:1px solid var(--bd);border-radius:12px;padding:6px 16px 12px;margin:1em 0;background:var(--card);font-family:var(--sans)}
.ru .pec h2{margin:.5em 0 .1em;font-size:1.25rem}.ru .res{color:var(--mut);font-size:14.5px}
.ru table{width:100%;border-collapse:collapse;font:15px/1.4 var(--sans);margin:.6em 0}
.ru th,.ru td{padding:7px 9px;border-bottom:1px solid var(--bd);text-align:left;vertical-align:top}
.ru th{font-size:12.5px;text-transform:uppercase;letter-spacing:.05em;color:var(--mut)}
.ru tr.hecho td{opacity:.5;text-decoration:line-through}
.ru .fuera{color:#b5701a}.ru a{color:var(--acc)}
.ru .tag{font:700 11.5px var(--sans);padding:2px 8px;border-radius:99px;border:1px solid currentColor;margin-left:6px;white-space:nowrap}
.ru .t1{color:#c0392b}.ru .t2{color:#b5701a}.ru .t3{color:var(--mut)}
@media(max-width:600px){.ru th,.ru td{padding:6px 5px;font-size:14px}.ru .tag{display:inline-block;margin:3px 0 0}}
</style>
</head>
<body class="ru">
<div class="topbar"><div class="in"><a href="index.html">← Índice de temas</a><span><button id="btn-tema" type="button">Claro / oscuro</button></span></div></div>
<main>
<h1>Ruta de estudio hasta las pruebas</h1>
<p>Dime cuántas horas por semana puedes dedicar y calculo qué temas te caben antes de cada hito (PA2, PEC única y PA3), empezando por los que más rinden en el examen (ver <a href="prioridades.html">prioridades</a>) y respetando lo que cada tema necesita antes. Marca lo que ya has estudiado y el plan se recalcula. Todo se guarda solo en este navegador.</p>
<div class="ctl"><label>Horas por semana: <input type="number" id="hs" min="1" max="60" value="8"></label><span id="hoy"></span></div>
<div id="out"></div>
<p class="res">Las horas por tema son las del camino completo de cada resumen (chip «⏱») y las dependencias son orientativas. Fechas del cronograma: PA2 el 23 de noviembre, PEC única del 11 al 13 de diciembre (se planifica hasta el 11), PA3 el 14 de enero de 2027; después, repaso y pruebas presenciales hasta el 24 de enero.</p>
</main>
<script type="application/json" id="datos">__DATOS__</script>
<script>
(function(){
  var D=JSON.parse(document.getElementById("datos").textContent), KEY="ruta_calculo_v1", S={hs:8,hecho:{}};
  try{var g=JSON.parse(localStorage.getItem(KEY));if(g){S.hs=g.hs||8;S.hecho=g.hecho||{}}}catch(e){}
  function guarda(){try{localStorage.setItem(KEY,JSON.stringify(S))}catch(e){}}
  var hs=document.getElementById('hs');hs.value=S.hs;
  var por={};D.temas.forEach(function(t){por[t.cod]=t});
  function mod(t){return parseInt(t.cod,10)}
  function f(d){return d.toLocaleDateString('es-ES',{day:'numeric',month:'short'})}
  function dias(a,b){return Math.round((b-a)/86400000)}
  function fila(t,a,b){var chk='<input type="checkbox" data-c="'+t.cod+'"'+(S.hecho[t.cod]?' checked':'')+' aria-label="Estudiado">';
    return '<tr class="'+(S.hecho[t.cod]?'hecho':'')+'"><td>'+chk+'</td><td><a href="'+t.url+'"><b>'+t.cod+'</b> '+t.nombre+'</a><span class="tag t'+t.nivel+'">'+['','Imprescindible','Recomendado','Completo'][t.nivel]+'</span></td><td>'+(a?f(a)+' – '+f(b):'—')+'</td><td>'+String(t.h).replace('.',',')+' h</td></tr>'}
  function pinta(){
    var hoy=new Date();hoy.setHours(0,0,0,0);
    document.getElementById('hoy').textContent='Hoy: '+hoy.toLocaleDateString('es-ES',{weekday:'long',day:'numeric',month:'long',year:'numeric'});
    var elegidos={}, ini=hoy, h='';
    D.hitos.forEach(function(hi){
      var fin=new Date(hi.fecha+'T00:00:00');
      if(fin<hoy){h+='<div class="pec"><h2>'+hi.nombre+'</h2><p class="res">Ya ha pasado.</p></div>';return}
      var grupo=D.temas.filter(function(t){return hi.mods.indexOf(mod(t))>=0});
      var rest=grupo.filter(function(t){return !S.hecho[t.cod]&&!elegidos[t.cod]});
      var cap=Math.max(0,dias(ini,fin))/7*S.hs, usada=0, sel=[];
      function mete(t){ if(elegidos[t.cod]||S.hecho[t.cod]||sel.indexOf(t)>=0) return;
        (t.dep||[]).forEach(function(d){if(!S.hecho[d]&&!elegidos[d]&&hi.mods.indexOf(mod(por[d]))>=0)mete(por[d])});
        if(usada+t.h<=cap+0.01&&sel.indexOf(t)<0){usada+=t.h;sel.push(t)} }
      [1,2,3].forEach(function(nv){rest.filter(function(t){return t.nivel===nv}).forEach(mete)});
      sel.sort(function(a,b){return D.temas.indexOf(a)-D.temas.indexOf(b)});
      var ac=0, filas=sel.map(function(t){var a=new Date(ini.getTime()+ac/S.hs*7*86400000);ac+=t.h;var b=new Date(ini.getTime()+ac/S.hs*7*86400000-86400000);elegidos[t.cod]=1;return fila(t,a,b)});
      var fuera=rest.filter(function(t){return !elegidos[t.cod]}), total=rest.reduce(function(s,t){return s+t.h},0);
      h+='<div class="pec"><h2>'+hi.nombre+' ('+f(fin)+')</h2><p class="res">Desde '+f(ini)+' hay '+Math.max(0,dias(ini,fin))+' días: caben ~<b>'+cap.toFixed(0)+' h</b> con '+S.hs+' h/semana; pendiente en estos módulos: <b>'+total.toFixed(0)+' h</b>. '+
        (fuera.length?'<span class="fuera">No cabe todo: se eligen primero los temas que más puntúan.</span>':'<b>Te da tiempo de todo.</b>')+'</p>';
      h+='<table><thead><tr><th></th><th>Tema</th><th>Cuándo</th><th>Horas</th></tr></thead><tbody>'+filas.join('')+grupo.filter(function(t){return S.hecho[t.cod]}).map(function(t){return fila(t)}).join('')+'</tbody></table>';
      if(fuera.length)h+='<p class="res"><b>Para después</b> (si sobra tiempo): '+fuera.map(function(t){return '<a href="'+t.url+'">'+t.cod+'</a> <label><input type="checkbox" data-c="'+t.cod+'"> ya lo he estudiado</label>'}).join(' · ')+'</p>';
      h+='</div>'; if(fin>ini) ini=new Date(Math.max(ini.getTime(),fin.getTime()+86400000)); });
    document.getElementById('out').innerHTML=h}
  hs.oninput=hs.onchange=function(){S.hs=Math.max(1,parseInt(hs.value,10)||8);guarda();pinta()};
  document.getElementById('out').addEventListener('change',function(e){if(e.target.dataset.c){S.hecho[e.target.dataset.c]=e.target.checked;guarda();pinta()}});
  document.getElementById('btn-tema').onclick=function(){var r=document.documentElement,d=r.getAttribute('data-theme')==='dark';r.setAttribute('data-theme',d?'light':'dark');try{localStorage.setItem('tema',d?'light':'dark')}catch(e){}};
  pinta();
})();
</script>
</body>
</html>
'''.replace('__DATOS__', datos)
(RAIZ / 'ruta.html').write_text(html, encoding='utf8')
print('ruta.html:', len(temas), 'temas')
