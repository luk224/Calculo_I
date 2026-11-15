/* Ayudas de estudio compartidas (ver estudio.css): casilla «hecho» con progreso, «solo lo esencial» y autoevaluación. */
(function () {
  var d = document, K = 'hecho:' + location.pathname, S = 'esencial:' + location.pathname;
  function leer(k) { try { return JSON.parse(localStorage.getItem(k)) || null; } catch (e) { return null; } }
  function guardar(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  function ready(f) { d.readyState !== 'loading' ? f() : d.addEventListener('DOMContentLoaded', f); }
  ready(function () {
    d.documentElement.classList.add('estudio-js');
    var marca = leer(K) || {}, items = Array.prototype.slice.call(d.querySelectorAll('article.ejer, details.pr')), prog = d.querySelector('.camino .prog'), bar = d.querySelector('.camino .bar i');
    function cuenta() {
      var solo = d.body.classList.contains('solo-esencial');
      var vis = items.filter(function (x) { return !(solo && x.closest('[data-extra]')); });
      var n = vis.filter(function (x) { return x.classList.contains('hecho-ok'); }).length;
      if (prog) prog.textContent = 'Hechos: ' + n + ' de ' + vis.length;
      if (bar) bar.style.width = (vis.length ? 100 * n / vis.length : 0) + '%';
      var mp = d.querySelector('.vistas .vprog'); if (mp) mp.textContent = 'Hechos: ' + n + ' de ' + vis.length;
    }
    items.forEach(function (x, i) {
      var s = x.tagName === 'ARTICLE' ? x.querySelector(':scope > .ejer-cab') : x.querySelector(':scope > summary'); if (!s) return;
      var id = x.id || ('i' + i), c = d.createElement('input');
      c.type = 'checkbox'; c.className = 'hecho'; c.setAttribute('aria-label', 'Marcar como hecho');
      c.checked = !!marca[id]; x.classList.toggle('hecho-ok', c.checked);
      c.addEventListener('click', function (e) { e.stopPropagation(); });
      c.addEventListener('change', function () { x.classList.toggle('hecho-ok', c.checked); marca[id] = c.checked; guardar(K, marca); cuenta(); });
      s.insertBefore(c, s.firstChild);
    });
    cuenta();
    var sw = d.querySelector('.camino input.esencial');
    function ponEsencial(v, guarda) { if (!sw) return; sw.checked = v; d.body.classList.toggle('solo-esencial', v); if (guarda) guardar(S, v); cuenta(); }
    if (sw) {
      // primera vez (sin valor guardado): «solo lo esencial» activado; si el usuario lo cambia, se guarda y se respeta
      var raw = null; try { raw = localStorage.getItem(S); } catch (e) {}
      ponEsencial(raw === null ? true : raw === 'true', false);
      sw.addEventListener('change', function () { ponEsencial(sw.checked, true); });
    }
    d.querySelectorAll('.quiz').forEach(function (qz) {
      var qs = qz.querySelectorAll('.q'), nota = qz.querySelector('.nota'), hechas = 0, buenas = 0;
      qs.forEach(function (q) {
        var ok = q.getAttribute('data-ok'), btns = q.querySelectorAll('.opts button');
        btns.forEach(function (b) {
          b.addEventListener('click', function () {
            if (q.classList.contains('ok') || q.classList.contains('mal')) return;
            var bien = b.getAttribute('data-v') === ok; b.classList.add('sel');
            q.classList.add(bien ? 'ok' : 'mal'); hechas++; if (bien) buenas++;
            var e = q.querySelector('.exp'); if (e) e.insertAdjacentHTML('afterbegin', '<b>' + (bien ? '✓ Correcto. ' : '✗ No: la respuesta es «' + (q.querySelector('.opts button[data-v="' + ok + '"]') || b).textContent + '». ') + '</b>');
            if (nota) nota.textContent = 'Aciertos: ' + buenas + ' de ' + hechas + (hechas === qs.length ? ' (preguntas: ' + qs.length + ')' : '');
          });
        });
      });
    });

    /* ===== Capa «pilot» (solo con <html class="pilot">): botón de fuentes y pestañas de vista ===== */
    var root = d.documentElement, pilot = root.classList.contains('pilot'), main = d.querySelector('main');
    var VK = 'vista:' + location.pathname, vistaAct = 'todo', barV = null;
    function porId(h) { try { return d.getElementById(decodeURIComponent(h.replace(/^#/, ''))); } catch (e) { return null; } }
    function tbAlto() { var tb = d.querySelector('.topbar'); return tb && getComputedStyle(tb).position === 'sticky' ? tb.offsetHeight : 0; }
    function filtraIndices(v) {
      [].forEach.call(d.querySelectorAll('.side-toc a[href^="#"], .mnav-list a[href^="#"]'), function (a) {
        var t = porId(a.getAttribute('href')), tv = t && t.getAttribute('data-vv');
        a.hidden = !!(v !== 'todo' && tv && tv !== v);
      });
    }
    function setV(v, guarda) {
      vistaAct = v; root.setAttribute('data-vista', v);
      if (barV) [].forEach.call(barV.querySelectorAll('[role="tab"]'), function (b) {
        var on = b.getAttribute('data-v') === v; b.setAttribute('aria-selected', on ? 'true' : 'false'); b.tabIndex = on ? 0 : -1;
      });
      filtraIndices(v);
      if (guarda) guardar(VK, v);
      try { window.dispatchEvent(new Event('resize')); } catch (e) {} /* reajusta tablas y fórmulas que estaban ocultas */
    }
    function scrollVista(v) {
      if (!barV) return;
      var t = v === 'todo' ? barV : main.querySelector('[data-vv="' + v + '"]'); if (!t) return;
      var off = tbAlto() + (getComputedStyle(barV).position === 'sticky' ? barV.offsetHeight : 0) + 8;
      window.scrollTo(0, Math.max(0, t.getBoundingClientRect().top + window.pageYOffset - off));
    }
    /* un enlace #id a un apartado de otra pestaña cambia de pestaña (si la vista no es «Todo») */
    function irAVista(t) {
      if (!pilot || !barV || !t || !t.closest) return;
      var p = t.closest('[data-vv]'), v = p && p.getAttribute('data-vv');
      if (v && vistaAct !== 'todo' && vistaAct !== v) { setV(v, true); t.scrollIntoView(); }
    }
    function iniciaFuentes() {
      var bt = d.getElementById('btn-tema'); if (!bt || !bt.parentNode) return;
      var bf = d.createElement('button'); bf.id = 'btn-fuentes'; bf.type = 'button';
      bf.title = 'Muestra u oculta las etiquetas de libro y página (U, E, L, X)';
      function set(v, g) {
        root.classList.toggle('con-fuentes', v); bf.setAttribute('aria-pressed', v ? 'true' : 'false');
        bf.textContent = v ? 'Ocultar fuentes' : 'Mostrar fuentes'; if (g) guardar('fuentes', v);
      }
      bf.addEventListener('click', function () { set(!root.classList.contains('con-fuentes'), true); });
      bt.parentNode.insertBefore(bf, bt); bt.parentNode.insertBefore(d.createTextNode(' '), bt);
      set(leer('fuentes') === true, false);
    }
    function iniciaVistas() {
      if (!main) return;
      var cur = null, hay = {}, cnt = { tipos: 0, ejercicios: 0, examen: 0 };
      [].forEach.call(main.children, function (el) {
        if (el.tagName === 'H2') cur = el.getAttribute('data-vista') || null;
        if (!cur) return;
        hay[cur] = true; el.setAttribute('data-vv', cur);
        if (cur === 'tipos') cnt.tipos += el.querySelectorAll('details.pr').length;
        else if (el.matches('article.ejer') && cnt[cur] !== undefined) cnt[cur]++;
      });
      var defs = [['todo', 'Todo'], ['teoria', '📘 Teoría'], ['tipos', '🧭 Por tipo'], ['ejercicios', '✏️ Ejercicios'], ['examen', '🎯 Examen']]
        .filter(function (x) { return x[0] === 'todo' || hay[x[0]]; });
      var primero = main.querySelector('[data-vv]'); if (!primero || defs.length < 2) return;
      barV = d.createElement('div'); barV.className = 'vistas'; barV.setAttribute('role', 'tablist'); barV.setAttribute('aria-label', 'Vista del tema');
      defs.forEach(function (x) {
        var b = d.createElement('button'); b.type = 'button'; b.setAttribute('role', 'tab'); b.setAttribute('data-v', x[0]); b.textContent = x[1];
        if (cnt[x[0]]) { var c = d.createElement('span'); c.className = 'cnt'; c.textContent = '(' + cnt[x[0]] + ')'; b.appendChild(c); }
        b.addEventListener('click', function () { setV(x[0], true); scrollVista(x[0]); });
        barV.appendChild(b);
      });
      var vp = d.createElement('span'); vp.className = 'vprog'; barV.appendChild(vp);
      barV.addEventListener('keydown', function (e) {
        var bs = [].slice.call(barV.querySelectorAll('[role="tab"]')), i = bs.indexOf(d.activeElement), n = -1;
        if (i < 0) return;
        if (e.key === 'ArrowRight') n = (i + 1) % bs.length; else if (e.key === 'ArrowLeft') n = (i + bs.length - 1) % bs.length;
        else if (e.key === 'Home') n = 0; else if (e.key === 'End') n = bs.length - 1;
        if (n < 0) return;
        e.preventDefault(); bs[n].focus(); setV(bs[n].getAttribute('data-v'), true);
      });
      main.insertBefore(barV, primero);
      function ajustaTop() { root.style.setProperty('--tbh', tbAlto() + 'px'); }
      ajustaTop(); window.addEventListener('resize', ajustaTop);
      var sv = leer(VK);
      setV(sv && barV.querySelector('[data-v="' + sv + '"]') ? sv : 'todo', false);
      window.addEventListener('load', function () { filtraIndices(vistaAct); });
      if (location.hash && vistaAct !== 'todo') { var t0 = porId(location.hash); if (t0) setTimeout(function () { irAVista(t0); t0.scrollIntoView(); }, 60); }
      d.addEventListener('click', function (e) {
        var a = e.target.closest && e.target.closest('a[href^="#"]'); if (!a) return;
        var h = a.getAttribute('href'); if (h.length < 2) return;
        var t = porId(h), ir = a.getAttribute('data-ir-vista');
        if (ir && t && barV.querySelector('[data-v="' + ir + '"]')) {
          e.preventDefault(); setV(ir, true); scrollVista(ir);
          try { history.replaceState(null, '', h); } catch (x) {}
          return;
        }
        irAVista(t);
      });
      cuenta();
    }
    if (pilot) { iniciaFuentes(); iniciaVistas(); }
    function abre() {
      var h = location.hash; if (h.length < 2) return;
      var t = d.getElementById(decodeURIComponent(h.slice(1)));
      if (!t) return;
      irAVista(t);
      // si el destino está dentro de una ampliación oculta por «solo lo esencial», se desactiva el modo
      if (d.body.classList.contains('solo-esencial') && t.closest('[data-extra]')) ponEsencial(false, true);
      var a = t.closest('details.amp'); if (a) a.open = true;
      // abre los desplegables que contienen al destino (p.ej. una nota dentro de una solución)
      for (var p = t.parentElement; p; p = p.parentElement) if (p.tagName === 'DETAILS') p.open = true;
      if (t.tagName === 'DETAILS') { t.open = true; t.scrollIntoView(); }
      else if (t.tagName === 'ARTICLE' && t.classList.contains('ejer')) { var sl = t.querySelector(':scope > details.sol'); if (sl) sl.open = true; t.scrollIntoView(); }
    }
    abre(); window.addEventListener('hashchange', abre);
    window.addEventListener('beforeprint', function () { d.querySelectorAll('details.pr, details.pista, details.respuesta, details.ver, details.sol, details.ampl').forEach(function (x) { x.open = true; }); });
  });
})();
