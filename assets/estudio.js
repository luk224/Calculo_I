/* Ayudas de estudio compartidas (ver estudio.css): casilla «hecho» con progreso, «solo lo esencial» y autoevaluación. */
(function () {
  var d = document, K = 'hecho:' + location.pathname, S = 'esencial:' + location.pathname;
  function leer(k) { try { return JSON.parse(localStorage.getItem(k)) || null; } catch (e) { return null; } }
  function guardar(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  function ready(f) { d.readyState !== 'loading' ? f() : d.addEventListener('DOMContentLoaded', f); }
  ready(function () {
    d.documentElement.classList.add('estudio-js');
    var marca = leer(K) || {}, items = Array.prototype.slice.call(d.querySelectorAll('details.sol, details.pr')), prog = d.querySelector('.camino .prog'), bar = d.querySelector('.camino .bar i');
    function cuenta() {
      var solo = d.body.classList.contains('solo-esencial');
      var vis = items.filter(function (x) { return !(solo && x.closest('[data-extra]')); });
      var n = vis.filter(function (x) { return x.classList.contains('hecho-ok'); }).length;
      if (prog) prog.textContent = 'Hechos: ' + n + ' de ' + vis.length;
      if (bar) bar.style.width = (vis.length ? 100 * n / vis.length : 0) + '%';
    }
    items.forEach(function (x, i) {
      var s = x.querySelector(':scope > summary'); if (!s) return;
      var id = x.id || ('i' + i), c = d.createElement('input');
      c.type = 'checkbox'; c.className = 'hecho'; c.setAttribute('aria-label', 'Marcar como hecho');
      c.checked = !!marca[id]; x.classList.toggle('hecho-ok', c.checked);
      c.addEventListener('click', function (e) { e.stopPropagation(); });
      c.addEventListener('change', function () { x.classList.toggle('hecho-ok', c.checked); marca[id] = c.checked; guardar(K, marca); cuenta(); });
      s.insertBefore(c, s.firstChild);
    });
    cuenta();
    var sw = d.querySelector('.camino input.esencial');
    if (sw) {
      sw.checked = !!leer(S); d.body.classList.toggle('solo-esencial', sw.checked); cuenta();
      sw.addEventListener('change', function () { d.body.classList.toggle('solo-esencial', sw.checked); guardar(S, sw.checked); cuenta(); });
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
    function abre() {
      var h = location.hash; if (h.length < 2) return;
      var t = d.getElementById(decodeURIComponent(h.slice(1)));
      if (t && t.tagName === 'DETAILS') { t.open = true; t.scrollIntoView(); }
    }
    abre(); window.addEventListener('hashchange', abre);
    window.addEventListener('beforeprint', function () { d.querySelectorAll('details.pr, details.pista, details.respuesta').forEach(function (x) { x.open = true; }); });
  });
})();
