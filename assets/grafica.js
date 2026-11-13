/* Componentes compartidos para los temas (sin three.js, SVG/HTML puros: se ven igual al imprimir).

   1) Gráfica con lectura de coordenadas:
        <figure class="graf" data-g='{"p":[[1,3],[5,11]],"c":[{"interp":true,"n":"p₃(x)"}]}'><figcaption>…</figcaption></figure>
      data-g (JSON):
        p   puntos de datos [[x,y,"etiqueta opcional"],…] (se dibujan con su (x, y) escrito)
        q   puntos destacados (valores que se piden) [[x,y,"etiqueta"],…]
        c   curvas: {"e":"expresión en x","n":"nombre","d":1 (punto-raya)} o {"interp":true | [índices de p],"n":"nombre"}
            (interp = polinomio interpolador de Newton por esos puntos)
        x,y rangos [min,max] (si faltan, se calculan); ex,ey: nombres de los ejes (por defecto x, y)
      Al pasar el ratón / tocar / flechas ← → se ve la posición x sobre cada curva y el valor de y; sobre un punto de datos, sus coordenadas.

   2) Tabla de diferencias divididas «en escalera» con flechas que unen cada casilla con las dos de las que sale:
        <div class="dd" data-x="-2,-1,1,3" data-y="-35,-11,-5,25"></div>
      Opciones: data-solo="1" (solo valores, sin el cociente con números), data-cifras="5" (si hay decimales),
      data-newton="1" (escribe debajo el polinomio de Newton con la diagonal superior), data-nombre="p" y data-var="x" (nombres del polinomio y de la variable). */
(function () {
  var NS = 'http://www.w3.org/2000/svg';
  function el(tag, at, par) { var e = document.createElementNS(NS, tag), k; for (k in at || {}) e.setAttribute(k, at[k]); if (par) par.appendChild(e); return e; }
  function h(tag, cls, par, txt) { var e = document.createElement(tag); if (cls) e.className = cls; if (txt != null) e.textContent = txt; if (par) par.appendChild(e); return e; }
  function fmt(v) {
    if (!isFinite(v)) return '—';
    var a = Math.abs(v), s;
    if (Number.isInteger(v)) s = String(v); else { s = a >= 1000 ? v.toFixed(1) : a >= 100 ? v.toFixed(2) : v.toPrecision(4); if (s.indexOf('.') >= 0 && s.indexOf('e') < 0) s = s.replace(/0+$/, '').replace(/\.$/, ''); }
    return s.replace('.', ',').replace('-', '−');
  }
  function paso(r, n) { var e = Math.pow(10, Math.floor(Math.log(r / n) / Math.LN10)), m = r / n / e; return (m < 1.5 ? 1 : m < 3.5 ? 2 : m < 7.5 ? 5 : 10) * e; }
  function ready(f) { document.readyState !== 'loading' ? f() : document.addEventListener('DOMContentLoaded', f); }
  function tex(t) { return window.katex ? window.katex.renderToString(t, { throwOnError: false }) : t; }
  /* interpolador de Newton en coma flotante por los puntos P (lista de [x,y]) */
  function newton(P) {
    var n = P.length, d = P.map(function (p) { return p[1]; }), i, j;
    for (j = 1; j < n; j++) for (i = n - 1; i >= j; i--) d[i] = (d[i] - d[i - 1]) / (P[i][0] - P[i - j][0]);
    return function (t) { var s = d[n - 1]; for (var k = n - 2; k >= 0; k--) s = s * (t - P[k][0]) + d[k]; return s; };
  }
  function expr(e) {
    var f = new Function('x', 'with(Math){return ' + String(e).replace(/\^/g, '**').replace(/\bln\(/g, 'log(').replace(/\bsen\(/g, 'sin(') + '}');
    return f;
  }

  /* ---------------------------------------------------------------- 1) gráficas */
  var COL = ['var(--acc)', 'var(--S)', 'var(--L)', 'var(--E)'], DASH = ['', '8 4', '2 4', '10 3 2 3'];
  function graf(fig) {
    var cfg; try { cfg = JSON.parse(fig.getAttribute('data-g')); } catch (e) { return; }
    var P = cfg.p || [], Q = cfg.q || [], C = [];
    (cfg.c || []).forEach(function (c, k) {
      var f, idx;
      if (c.interp) { idx = c.interp === true ? P.map(function (_, i) { return i; }) : c.interp; f = newton(idx.map(function (i) { return P[i]; })); }
      else f = expr(c.e);
      C.push({ f: f, n: c.n || 'f(x)', col: c.d ? 'var(--mut)' : COL[k % COL.length], da: c.d ? '1 5' : DASH[k % DASH.length] });
    });
    var box = h('div', 'graf-box'), leg = h('div', 'graf-leg'), cap = fig.querySelector('figcaption');
    fig.insertBefore(leg, cap || null); fig.insertBefore(box, leg);
    C.forEach(function (c) { var s = h('span', null, leg), i = h('i', null, s); i.style.setProperty('--c', c.col); i.style.setProperty('--da', c.da ? 'dashed' : 'solid'); s.appendChild(document.createTextNode(c.n)); });
    if (P.length) { var sp = h('span', null, leg), ip = h('i', 'pt', sp); sp.appendChild(document.createTextNode('datos')); }
    if (Q.length) { var sq = h('span', null, leg), iq = h('i', 'pt q', sq); sq.appendChild(document.createTextNode('valor pedido')); }
    fig.setAttribute('role', 'group');
    var ancho = 0;
    function dibujar() {
      var W = Math.max(260, Math.floor(box.clientWidth)); if (W === ancho) return; ancho = W;
      var H = Math.round(Math.min(420, Math.max(250, W * 0.56))), m = { l: 46, r: 14, t: 14, b: 28 };
      var pts = P.concat(Q), xs = pts.map(function (p) { return p[0]; }), x0, x1, y0, y1, i;
      if (cfg.x) { x0 = cfg.x[0]; x1 = cfg.x[1]; } else { x0 = Math.min.apply(null, xs); x1 = Math.max.apply(null, xs); var sx = (x1 - x0) || 1; x0 -= 0.12 * sx; x1 += 0.12 * sx; }
      if (cfg.y) { y0 = cfg.y[0]; y1 = cfg.y[1]; } else {
        var ys = pts.map(function (p) { return p[1]; });
        C.forEach(function (c) { for (i = 0; i <= 120; i++) { var v = c.f(x0 + (x1 - x0) * i / 120); if (isFinite(v)) ys.push(v); } });
        y0 = Math.min.apply(null, ys); y1 = Math.max.apply(null, ys); var sy = (y1 - y0) || 1; y0 -= 0.08 * sy; y1 += 0.08 * sy;
      }
      var pw = W - m.l - m.r, ph = H - m.t - m.b;
      function X(v) { return m.l + (v - x0) / (x1 - x0) * pw; } function Y(v) { return m.t + (1 - (v - y0) / (y1 - y0)) * ph; }
      function inv(px) { return x0 + (px - m.l) / pw * (x1 - x0); }
      box.textContent = ''; var tip = h('div', 'graf-tip', box); tip.hidden = true;
      var svg = el('svg', { width: W, height: H, viewBox: '0 0 ' + W + ' ' + H, role: 'img', tabindex: 0,
        'aria-label': (fig.getAttribute('data-alt') || 'Gráfica') + '. Pasa el ratón o usa las flechas para leer coordenadas.' }, box);
      var cp = 'gc' + Math.random().toString(36).slice(2, 8);
      el('rect', { x: m.l, y: m.t, width: pw, height: ph }, el('clipPath', { id: cp }, svg));
      var g = el('g', { 'font-family': 'system-ui,sans-serif', 'font-size': 11 }, svg), t, tx = paso(x1 - x0, W / 80), ty = paso(y1 - y0, H / 45);
      for (t = Math.ceil(x0 / tx) * tx; t <= x1 + tx * 1e-9; t += tx) { var vx = Math.round(t / tx) * tx;
        el('line', { x1: X(vx), x2: X(vx), y1: m.t, y2: m.t + ph, stroke: 'var(--bd)', 'stroke-width': 1 }, g);
        var tt = el('text', { x: X(vx), y: m.t + ph + 16, 'text-anchor': 'middle', fill: 'var(--mut)' }, g); tt.textContent = fmt(vx); }
      for (t = Math.ceil(y0 / ty) * ty; t <= y1 + ty * 1e-9; t += ty) { var vy = Math.round(t / ty) * ty;
        el('line', { x1: m.l, x2: m.l + pw, y1: Y(vy), y2: Y(vy), stroke: 'var(--bd)', 'stroke-width': 1 }, g);
        var tl = el('text', { x: m.l - 6, y: Y(vy) + 4, 'text-anchor': 'end', fill: 'var(--mut)' }, g); tl.textContent = fmt(vy); }
      var ax = x0 <= 0 && x1 >= 0 ? X(0) : m.l, ay = y0 <= 0 && y1 >= 0 ? Y(0) : m.t + ph;
      el('line', { x1: m.l, x2: m.l + pw, y1: ay, y2: ay, stroke: 'var(--fg)', 'stroke-width': 1.3 }, g);
      el('line', { x1: ax, x2: ax, y1: m.t, y2: m.t + ph, stroke: 'var(--fg)', 'stroke-width': 1.3 }, g);
      var lx = el('text', { x: m.l + pw - 2, y: ay - 6, 'text-anchor': 'end', fill: 'var(--fg)', 'font-style': 'italic' }, g); lx.textContent = cfg.ex || 'x';
      var ly = el('text', { x: ax + 6, y: m.t + 10, fill: 'var(--fg)', 'font-style': 'italic' }, g); ly.textContent = cfg.ey || 'y';
      var cg = el('g', { 'clip-path': 'url(#' + cp + ')' }, svg);
      C.forEach(function (c) {
        var d = '', up = false, N = Math.max(200, Math.round(pw)), k;
        for (k = 0; k <= N; k++) { var v = c.f(x0 + (x1 - x0) * k / N); if (isFinite(v) && Math.abs(v) < 1e7) { d += (up ? 'L' : 'M') + X(x0 + (x1 - x0) * k / N).toFixed(1) + ' ' + Y(v).toFixed(1); up = true; } else up = false; }
        el('path', { d: d, fill: 'none', stroke: c.col, 'stroke-width': 2.4, 'stroke-dasharray': c.da, 'stroke-linejoin': 'round' }, cg);
      });
      function marca(p, q) {
        var cx = X(p[0]), cy = Y(p[1]);
        if (q) el('rect', { x: cx - 5.5, y: cy - 5.5, width: 11, height: 11, transform: 'rotate(45 ' + cx + ' ' + cy + ')', fill: 'var(--card)', stroke: 'var(--ex-b)', 'stroke-width': 2.4 }, svg);
        else el('circle', { cx: cx, cy: cy, r: 5, fill: 'var(--warn-b)', stroke: 'var(--card)', 'stroke-width': 1.5 }, svg);
        var tx2 = el('text', { x: cx + 8, y: cy - 8, 'font-size': 11, 'font-family': 'system-ui,sans-serif', 'font-weight': q ? 700 : 500, fill: q ? 'var(--ex-b)' : 'var(--fg)', stroke: 'var(--card)', 'stroke-width': 3, 'paint-order': 'stroke' }, svg);
        tx2.textContent = p[2] || '(' + fmt(p[0]) + ', ' + fmt(p[1]) + ')';
        if (cx + 8 + tx2.getComputedTextLength() > W - 4) tx2.setAttribute('x', cx - 8), tx2.setAttribute('text-anchor', 'end');
      }
      P.forEach(function (p) { marca(p, false); }); Q.forEach(function (p) { marca(p, true); });
      /* lectura de coordenadas */
      var gl = el('g', { 'pointer-events': 'none', visibility: 'hidden' }, svg), guia = el('line', { y1: m.t, y2: m.t + ph, stroke: 'var(--mut)', 'stroke-width': 1, 'stroke-dasharray': '4 3' }, gl);
      var dots = C.map(function (c) { return el('circle', { r: 5, fill: 'var(--card)', stroke: c.col, 'stroke-width': 2.6 }, gl); });
      function leer(px) {
        px = Math.max(m.l, Math.min(m.l + pw, px)); var xv = inv(px), snap = null, bd = 100;
        pts.forEach(function (p) { var d = Math.abs(X(p[0]) - px); if (d * d < bd) { bd = d * d; snap = p; } });
        if (snap) { xv = snap[0]; px = X(xv); }
        guia.setAttribute('x1', px); guia.setAttribute('x2', px); gl.setAttribute('visibility', 'visible');
        var html = '<b>x = ' + fmt(xv) + '</b>' + (snap ? ' · punto' : ''), ysum = 0, nn = 0;
        C.forEach(function (c, k) { var v = c.f(xv); if (isFinite(v)) { dots[k].setAttribute('cx', px); dots[k].setAttribute('cy', Y(v)); dots[k].setAttribute('visibility', 'visible'); ysum += Y(v); nn++;
          html += '<div><i style="--c:' + c.col + '"></i>' + c.n.replace(/</g, '&lt;') + ' = <b>' + fmt(v) + '</b></div>'; } else dots[k].setAttribute('visibility', 'hidden'); });
        if (snap && !C.length) html += '<div>y = <b>' + fmt(snap[1]) + '</b></div>';
        tip.innerHTML = html; tip.hidden = false;
        var tw = tip.offsetWidth, th = tip.offsetHeight, ty0 = nn ? ysum / nn : m.t + ph / 2;
        tip.style.left = Math.max(2, Math.min(W - tw - 2, px + 12 + tw > W ? px - 12 - tw : px + 12)) + 'px';
        tip.style.top = Math.max(2, Math.min(H - th - 2, ty0 - th - 10 < 2 ? ty0 + 14 : ty0 - th - 10)) + 'px';
        svg._x = xv;
      }
      function fuera() { gl.setAttribute('visibility', 'hidden'); tip.hidden = true; }
      svg.addEventListener('pointermove', function (e) { var r = svg.getBoundingClientRect(); leer(e.clientX - r.left); });
      svg.addEventListener('pointerdown', function (e) { var r = svg.getBoundingClientRect(); leer(e.clientX - r.left); });
      svg.addEventListener('pointerleave', function (e) { if (e.pointerType === 'mouse') fuera(); });
      svg.addEventListener('blur', fuera);
      svg.addEventListener('keydown', function (e) {
        if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return; e.preventDefault();
        var cur = svg._x == null ? (x0 + x1) / 2 : svg._x; leer(X(cur + (e.key === 'ArrowLeft' ? -1 : 1) * (x1 - x0) / 80));
      });
      svg.style.touchAction = 'pan-y';
    }
    dibujar();
    if (window.ResizeObserver) new ResizeObserver(dibujar).observe(box);
    window.addEventListener('beforeprint', function () { ancho = 0; dibujar(); });
  }

  /* ---------------------------------------------------------------- 2) tabla de diferencias divididas en escalera */
  function gcd(a, b) { a = Math.abs(a); b = Math.abs(b); while (b) { var t = a % b; a = b; b = t; } return a; }
  function Rat(n, d) { if (d < 0) { n = -n; d = -d; } var g = gcd(n, d) || 1; return { n: n / g, d: d / g }; }
  var QQ = {
    parse: function (s) { return Rat(parseInt(s, 10), 1); }, sub: function (a, b) { return Rat(a.n * b.d - b.n * a.d, a.d * b.d); },
    div: function (a, b) { return Rat(a.n * b.d, a.d * b.n); }, neg: function (a) { return a.n < 0; }, zero: function (a) { return a.n === 0; }, one: function (a) { return a.n === 1 && a.d === 1; },
    abs: function (a) { return Rat(Math.abs(a.n), a.d); },
    tex: function (a) { return a.d === 1 ? String(a.n) : (a.n < 0 ? '-' : '') + '\\tfrac{' + Math.abs(a.n) + '}{' + a.d + '}'; }
  };
  function FF(cifras) {
    return {
      parse: function (s) { return parseFloat(s); }, sub: function (a, b) { return a - b; }, div: function (a, b) { return a / b; },
      neg: function (a) { return a < 0; }, zero: function (a) { return a === 0; }, one: function (a) { return a === 1; }, abs: Math.abs,
      tex: function (a) { var s = String(parseFloat(a.toPrecision(cifras))); return s.replace('.', '{,}'); }
    };
  }
  function par(O, a) { var t = O.tex(a); return O.neg(a) ? '(' + t + ')' : t; }
  var ddN = 0;
  function dd(div) {
    var xsS = div.getAttribute('data-x').split(','), ysS = div.getAttribute('data-y').split(',');
    var O = /[.]/.test(div.getAttribute('data-x') + div.getAttribute('data-y')) ? FF(parseInt(div.getAttribute('data-cifras') || '5', 10)) : QQ;
    var solo = div.hasAttribute('data-solo'), n = xsS.length, x = xsS.map(O.parse.bind(O)), T = [ysS.map(O.parse.bind(O))], m, i;
    for (m = 1; m < n; m++) { T[m] = []; for (i = 0; i < n - m; i++) T[m][i] = O.div(O.sub(T[m - 1][i + 1], T[m - 1][i]), O.sub(x[i + m], x[i])); }
    var grid, cells, svg, defs, solo0 = solo, uid = 'dda' + (++ddN);
  function construir(solo) {
    div.textContent = '';
    grid = h('div', 'dd-grid' + (solo ? ' compacto' : ''), div); cells = {}; grid.style.gridTemplateColumns = 'repeat(' + (n + 1) + ',auto)';
    function put(txt, col, row, cls) { var c = h('div', 'dd-c' + (cls ? ' ' + cls : ''), grid); c.style.gridColumn = col; c.style.gridRow = row; c.innerHTML = tex(txt); return c; }
    put('x_k', 1, 1, 'dd-h'); put('f[x_k]', 2, 1, 'dd-h');
    for (m = 1; m < n; m++) put(m === 1 ? 'f[x_k,x_{k+1}]' : m === 2 ? 'f[x_k,x_{k+1},x_{k+2}]' : 'f[x_k,\\dots,x_{k+' + m + '}]', 2 + m, 1, 'dd-h');
    for (i = 0; i < n; i++) { put(O.tex(x[i]), 1, 2 + 2 * i, 'dd-x'); cells['0,' + i] = put(O.tex(T[0][i]), 2, 2 + 2 * i, 'dd-v' + (i === 0 ? ' top' : '')); }
    for (m = 1; m < n; m++) for (i = 0; i < n - m; i++) {
      var v = O.tex(T[m][i]), a = T[m - 1][i + 1], b = T[m - 1][i], den = O.sub(x[i + m], x[i]);
      var body = solo ? '\\mathbf{' + v + '}' : '\\dfrac{' + O.tex(a) + '-' + par(O, b) + '}{' + O.tex(x[i + m]) + '-' + par(O, x[i]) + '}=\\mathbf{' + v + '}';
      cells[m + ',' + i] = put(body, 2 + m, 2 + 2 * i + m, 'dd-v' + (i === 0 ? ' top' : ''));
    }
    svg = el('svg', { class: 'dd-lines', 'aria-hidden': 'true' }, grid);
    defs = el('defs', {}, svg); var mk = el('marker', { id: uid, viewBox: '0 0 8 8', refX: 7, refY: 4, markerWidth: 7, markerHeight: 7, orient: 'auto' }, defs);
    el('path', { d: 'M0 0L8 4L0 8z', fill: 'var(--mut)' }, mk);
    }
    function lineas() {
      var gr = grid.getBoundingClientRect(), sc = gr.width / (grid.offsetWidth || 1) || 1;
      while (svg.lastChild !== defs) svg.removeChild(svg.lastChild);
      svg.setAttribute('width', grid.offsetWidth); svg.setAttribute('height', grid.offsetHeight);
      function pos(c, lado) { var r = c.getBoundingClientRect(); return [((lado ? r.right : r.left) - gr.left) / sc, (r.top + r.height / 2 - gr.top) / sc]; }
      for (var mm = 1; mm < n; mm++) for (var ii = 0; ii < n - mm; ii++) {
        var hijo = cells[mm + ',' + ii], pa = [cells[(mm - 1) + ',' + ii], cells[(mm - 1) + ',' + (ii + 1)]];
        pa.forEach(function (p, k) {
          var a = pos(p, 1), b = pos(hijo, 0), mx = (a[0] + b[0]) / 2;
          el('path', { d: 'M' + (a[0] + 3) + ' ' + a[1] + 'C' + mx + ' ' + a[1] + ' ' + mx + ' ' + b[1] + ' ' + (b[0] - 3) + ' ' + b[1], fill: 'none', stroke: 'var(--mut)', 'stroke-width': 1.4, 'marker-end': 'url(#' + uid + ')' }, svg);
        });
      }
    }
    /* escalado al ancho disponible */
    var wrap = div;
    function ajustar() {
      var compacto = !solo0 && wrap.clientWidth > 0 && wrap.clientWidth < 560;
      if (compacto !== solo) { solo = compacto; construir(solo); }
      grid.style.transform = ''; wrap.style.height = ''; lineas();
      var w = grid.offsetWidth, a = wrap.clientWidth, s = Math.max(0.5, Math.min(1, a / w));
      if (s < 1) { grid.style.transform = 'scale(' + s + ')'; grid.style.transformOrigin = '0 0'; wrap.style.height = grid.offsetHeight * s + 'px'; }
      else wrap.style.height = '';
    }
    function pintarNewton() {
      var nombre = div.getAttribute('data-nombre') || 'p', v = div.getAttribute('data-var') || 'x', t = nombre + '_' + (n - 1) + '(' + v + ')=', prod = '', primero = true, k;
      for (k = 0; k < n; k++) {
        if (k > 0) prod += O.zero(x[k - 1]) ? v : '(' + v + (O.neg(x[k - 1]) ? '+' + O.tex(O.abs(x[k - 1])) : '-' + O.tex(x[k - 1])) + ')';
        var c = T[k][0]; if (O.zero(c)) continue;
        var ab = O.abs(c), cs = k > 0 && O.one(ab) ? '' : O.tex(ab);
        t += (O.neg(c) ? '-' : primero ? '' : '+') + cs + prod; primero = false;
      }
      var p = h('p', 'dd-newton'); div.parentNode.insertBefore(p, div.nextSibling); p.innerHTML = 'Diagonal superior → polinomio: ' + tex(t);
    }
    if (div.hasAttribute('data-newton')) pintarNewton();
    construir(solo);
    var pronto = function () { ajustar(); if (window.ResizeObserver) new ResizeObserver(function () { ajustar(); }).observe(wrap); };
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(pronto); else pronto();
    window.addEventListener('beforeprint', ajustar); window.addEventListener('afterprint', ajustar);
    if (window.matchMedia) { var mq = window.matchMedia('print'); if (mq.addEventListener) mq.addEventListener('change', ajustar); }
  }

  ready(function () {
    [].forEach.call(document.querySelectorAll('figure.graf[data-g]'), graf);
    [].forEach.call(document.querySelectorAll('div.dd[data-x]'), dd);
  });
})();
