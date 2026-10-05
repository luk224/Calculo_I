// Comportamiento compartido: KaTeX, índice lateral, panel de fuentes, tema claro/oscuro, soluciones.
(function () {
  var d = document;
  try { var t0 = localStorage.getItem('tema'); if (t0) d.documentElement.setAttribute('data-theme', t0); } catch (e) {}
  function ready(f) { d.readyState !== 'loading' ? f() : d.addEventListener('DOMContentLoaded', f); }
  ready(function () {
    try {
      if (window.renderMathInElement) renderMathInElement(d.body, {
        delimiters: [{ left: '$$', right: '$$', display: true }, { left: '\\[', right: '\\]', display: true },
                     { left: '$', right: '$', display: false }, { left: '\\(', right: '\\)', display: false }],
        throwOnError: false, ignoredTags: ['script', 'style', 'textarea', 'code'],
        macros: { '\\lim': '\\mathop{\\operatorname{lim}}\\limits' } /* subíndice siempre debajo de «lim», también en línea */
      });
    } catch (e) {}
    /* fórmulas en pantalla: si no caben, se reducen (hasta 55 %) para evitar el scroll horizontal */
    var MACROS = { '\\lim': '\\mathop{\\operatorname{lim}}\\limits' };
    /* parte un TeX en los puntos de profundidad 0 donde empieza un token de `re` */
    function splitTop(tex, re) {
      var out = [], depth = 0, last = 0, i = 0, m;
      while (i < tex.length) {
        var c = tex[i];
        if (c === '{' || c === '(' || c === '[') depth++; else if (c === '}' || c === ')' || c === ']') depth--;
        else if (c === '\\') {
          m = /^\\(left|right|begin|end)\b/.exec(tex.slice(i));
          if (m) { if (m[1] === 'left' || m[1] === 'begin') depth++; else depth--; }
        }
        if (depth === 0 && i > last && (m = re.exec(tex.slice(i))) && m.index === 0) { out.push(tex.slice(last, i)); last = i; i += m[0].length; continue; }
        if (c === '\\') i += 2; else i++;
      }
      out.push(tex.slice(last)); return out;
    }
    function fits(m) { return m.clientWidth && m.scrollWidth <= m.clientWidth + 1; }
    function wrapMath(m) {
      var an = m.querySelector('annotation'); if (!an || !window.katex || m.dataset.wrapped) return;
      var tex = an.textContent, tries = [];
      var l1 = splitTop(tex, /^\\q?quad/).map(function (x) { return x.replace(/^\\q?quad\s*/, ''); }).filter(function (x) { return x.trim(); });
      tries.push(l1);
      var l2 = []; l1.forEach(function (ln) {
        splitTop(ln, /^=|^\\(Longrightarrow|iff|Rightarrow)\b/).forEach(function (p, j) { l2.push(j ? '{}' + p : p); }); });
      tries.push(l2);
      var l3 = []; l2.forEach(function (ln) {
        splitTop(ln, /^[+]/).forEach(function (p, j) { l3.push(j ? '{}' + p : p); }); });
      tries.push(l3);
      for (var t = 0; t < tries.length; t++) {
        if (tries[t].length < 2) continue;
        var src = '\\begin{gathered}' + tries[t].map(function (x) { return /^[\s]*\[/.test(x) ? '{}' + x : x; }).join('\\\\') + '\\end{gathered}';
        var tmp = d.createElement('span');
        try { katex.render(src, tmp, { displayMode: true, throwOnError: true, macros: MACROS }); } catch (e) { continue; }
        m.innerHTML = tmp.firstChild.innerHTML; m.dataset.wrapped = '1';
        fitOne(m); if (fits(m)) return;
      }
    }
    function fitOne(m) {
      var k = m.querySelector('.katex'); if (!k || !m.clientWidth) return;
      k.style.fontSize = '';
      var r = m.clientWidth / m.scrollWidth;
      if (r < 1) k.style.fontSize = (1.21 * Math.max(0.55, r * 0.98)).toFixed(3) + 'em';
    }
    function fitMath() {
      [].forEach.call(d.querySelectorAll('.katex-display'), function (m) {
        if (m.dataset.wrapped) { fitOne(m); return; }
        fitOne(m);
        var k = m.querySelector('.katex');
        if (k && m.clientWidth && (m.scrollWidth > m.clientWidth + 1 || parseFloat(k.style.fontSize || '1.21') < 1.21 * 0.8)) wrapMath(m);
      });
    }
    fitMath(); window.addEventListener('resize', fitMath); window.addEventListener('load', fitMath);
    d.addEventListener('toggle', fitMath, true);
    var toc = d.querySelector('.side-toc');
    var hs = [].slice.call(d.querySelectorAll('main h2[id]'));
    if (toc) hs.forEach(function (h) {
      var a = d.createElement('a'); a.href = '#' + h.id;
      var c = h.cloneNode(true); c.querySelectorAll('.src').forEach(function (x) { x.remove(); });
      var n = c.querySelector('.n'); var num = n ? n.textContent.trim() + ' ' : ''; if (n) n.remove();
      a.innerHTML = num + c.innerHTML.replace(/\s+/g, ' ').trim(); toc.appendChild(a);
    });
    if ('IntersectionObserver' in window && toc) {
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) toc.querySelectorAll('a').forEach(function (a) {
          a.classList.toggle('on', a.getAttribute('href') === '#' + e.target.id); }); });
      }, { rootMargin: '-20% 0px -70% 0px' });
      hs.forEach(function (h) { io.observe(h); });
    }
    var tocLinks = toc ? [].slice.call(toc.querySelectorAll('a')) : [];
    if (tocLinks.length) {
      var mn = d.createElement('div'); mn.className = 'mnav';
      mn.innerHTML = '<button type="button" class="mnav-btn" aria-expanded="false" aria-controls="mnav-list">☰ Apartados</button><nav id="mnav-list" class="mnav-list" aria-label="Apartados del tema" hidden></nav>';
      var list = mn.querySelector('nav'), mb = mn.querySelector('button');
      tocLinks.forEach(function (a) { var c = d.createElement('a'); c.href = a.getAttribute('href'); c.innerHTML = a.innerHTML; list.appendChild(c); });
      function setOpen(o) { list.hidden = !o; mb.setAttribute('aria-expanded', o ? 'true' : 'false');
        if (o) { var cur = null; hs.forEach(function (h) { if (h.getBoundingClientRect().top < 120) cur = h.id; });
          [].forEach.call(list.children, function (x) { var on = x.getAttribute('href') === '#' + cur; x.classList.toggle('on', on); if (on) x.scrollIntoView({ block: 'center' }); }); } }
      mb.addEventListener('click', function (e) { e.stopPropagation(); setOpen(list.hidden); });
      list.addEventListener('click', function (e) { if (e.target.tagName === 'A') setOpen(false); });
      d.addEventListener('click', function (e) { if (!mn.contains(e.target)) setOpen(false); });
      d.addEventListener('keydown', function (e) { if (e.key === 'Escape') setOpen(false); });
      d.body.appendChild(mn);
    }
    var panel = d.getElementById('panel-fuentes');
    if (panel) {
      var seen = {}, ul = d.createElement('ul');
      d.querySelectorAll('main .src').forEach(function (s) {
        if (panel.contains(s)) return;
        var k = s.dataset.l + '|' + s.dataset.ref; if (seen[k]) return; seen[k] = 1;
        var li = d.createElement('li'), c = s.cloneNode(true);
        li.appendChild(c); li.appendChild(d.createTextNode(' ' + s.dataset.ref)); ul.appendChild(li);
      });
      panel.appendChild(ul);
    }
    d.querySelectorAll('.src').forEach(function (s) { s.tabIndex = 0; s.setAttribute('aria-label', s.dataset.ref); });
    var bt = d.getElementById('btn-tema');
    if (bt && !d.getElementById('btn-imprimir')) {
      var bi = d.createElement('button'); bi.id = 'btn-imprimir'; bi.type = 'button'; bi.textContent = 'Imprimir / PDF';
      bi.title = 'Abre el diálogo de impresión (A4, blanco y negro, sin fuentes ni «fuera de examen»)';
      bi.addEventListener('click', function () { window.print(); });
      bt.parentNode.insertBefore(bi, bt); bt.parentNode.insertBefore(d.createTextNode(' '), bt);
      var bc = d.createElement('button'); bc.id = 'btn-imprimir-color'; bc.type = 'button'; bc.textContent = 'Imprimir en color';
      bc.title = 'Igual, pero conservando los colores (activa «Gráficos de fondo» en el diálogo)';
      bc.addEventListener('click', function () { d.documentElement.classList.add('print-color'); window.print(); });
      window.addEventListener('afterprint', function () { d.documentElement.classList.remove('print-color'); });
      bt.parentNode.insertBefore(bc, bt); bt.parentNode.insertBefore(d.createTextNode(' '), bt);
    }
    var btn = d.getElementById('btn-tema');
    if (btn) btn.addEventListener('click', function () {
      var r = d.documentElement, cur = r.getAttribute('data-theme');
      var dark = cur ? cur === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;
      r.setAttribute('data-theme', dark ? 'light' : 'dark');
      try { localStorage.setItem('tema', dark ? 'light' : 'dark'); } catch (e) {}
    });
    var all = d.getElementById('btn-sol');
    if (all) { var open = false; all.addEventListener('click', function () {
      open = !open; d.querySelectorAll('details.sol').forEach(function (x) { x.open = open; });
      all.textContent = open ? 'Ocultar soluciones' : 'Mostrar soluciones'; }); }
    function abrirSoluciones() { d.querySelectorAll('details.sol').forEach(function (x) { x.open = true; }); }
    if (matchMedia('print').matches) abrirSoluciones();
    window.addEventListener('beforeprint', function () { d.querySelectorAll('details.sol').forEach(function (x) { x.open = true; }); });
  });
})();
