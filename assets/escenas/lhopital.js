/* L'Hôpital (tema 2.3): cerca de a, f y g se parecen a sus tangentes, y f/g se parece a f′/g′ (0/0). */
Interactivos.registrar('lhopital', function (c) {
  var T = c.THREE, H = c.H;
  var F = [
    { n: 'sen x / x  cuando x → 0', f: Math.sin, g: function (x) { return x; }, df: Math.cos, dg: function () { return 1; }, a: 0, L: 1 },
    { n: '(1 − cos x) / x²  cuando x → 0', f: function (x) { return 1 - Math.cos(x); }, g: function (x) { return x * x; }, df: Math.sin, dg: function (x) { return 2 * x; }, a: 0, L: 0.5 },
    { n: '(eˣ − 1 − x) / x²  cuando x → 0', f: function (x) { return Math.exp(x) - 1 - x; }, g: function (x) { return x * x; }, df: function (x) { return Math.exp(x) - 1; }, dg: function (x) { return 2 * x; }, a: 0, L: 0.5 },
    { n: 'ln x / (x − 1)  cuando x → 1', f: Math.log, g: function (x) { return x - 1; }, df: function (x) { return 1 / x; }, dg: function () { return 1; }, a: 1, L: 1 },
    { n: '(eˣ − e⁻ˣ) / sen x  cuando x → 0', f: function (x) { return Math.exp(x) - Math.exp(-x); }, g: Math.sin, df: function (x) { return Math.exp(x) + Math.exp(-x); }, dg: Math.cos, a: 0, L: 2 }
  ];
  var A = 5, B0 = 6.4, B = 5, Hh = 4, w = 0.045, k = 0, s = 0.12, P = c.colores();
  var wdv = 1, ejesL, ejesR, cfL, cgL, cqR, cdR, limR, pq, pd;
  var l1 = c.lectura('f(x)/g(x)  en x = a + w/2'), l2 = c.lectura('f′(x)/g′(x)  en el mismo x'), l3 = c.lectura('Límite L'), lv = c.lectura('');
  function fm(t) { return (Math.round(t * 100000) / 100000).toString().replace('-', '−'); }
  function limpia(arr) { arr.forEach(function (o) { if (o) c.scene.remove(o); }); }
  function nuevo() {
    limpia([ejesL, ejesR, cfL, cgL, cqR, cdR, limR, pq, pd]);
    c.vista(-0.3, B0 + B + 0.3, -0.4, Hh + 0.4);
    ejesL = H.cinta(T, [[[0, 0], [0, Hh]], [[0, Hh / 2], [A, Hh / 2]], [[A / 2, 0], [A / 2, Hh]]], P.mut, w); ejesL.position.z = 0.05; c.scene.add(ejesL);
    ejesR = H.cinta(T, [[[B0, 0], [B0, Hh]], [[B0 + B / 2, 0], [B0 + B / 2, Hh]]], P.mut, w); ejesR.position.z = 0.05; c.scene.add(ejesR);
    cfL = H.cinta(T, [], P.acc, w * 1.4); cgL = H.cinta(T, [], P.S, w * 1.4); cfL.position.z = cgL.position.z = 0.1; c.scene.add(cfL, cgL);
    limR = H.cinta(T, [], P.L, w, [w * 5, w * 3]); limR.position.z = 0.1; c.scene.add(limR);
    cqR = H.cinta(T, [], P.fg, w * 1.4); cdR = H.cinta(T, [], P.S, w * 1.2, [w * 4, w * 3]); cqR.position.z = 0.2; cdR.position.z = 0.25; c.scene.add(cqR, cdR);
    pq = H.punto(T, 0, 0, w * 2.6, P.fg); pd = H.punto(T, 0, 0, w * 2.6, P.S); pq.position.z = pd.position.z = 0.5; c.scene.add(pq, pd);
  }
  function calc() {
    var g = F[k], wd = 2 * Math.pow(10, -s * 3), i, n = 300, pf = [], pg = [], pq_ = [], pd_ = [], m = 0, x, y;
    for (i = 0; i <= n; i++) { x = g.a - wd + 2 * wd * i / n; m = Math.max(m, Math.abs(g.f(x)), Math.abs(g.g(x))); }
    for (i = 0; i <= n; i++) {
      x = g.a - wd + 2 * wd * i / n; var X = A * (x - (g.a - wd)) / (2 * wd);
      pf.push([X, Hh / 2 + (Hh / 2) * 0.95 * g.f(x) / m]); pg.push([X, Hh / 2 + (Hh / 2) * 0.95 * g.g(x) / m]);
      if (Math.abs(x - g.a) > 1e-12) { var q = g.f(x) / g.g(x), d = g.df(x) / g.dg(x), Y = Hh / 2 + (q - g.L) * (Hh / 2) / 0.5, Y2 = Hh / 2 + (d - g.L) * (Hh / 2) / 0.5;
        if (Math.abs(q - g.L) < 0.6) pq_.push([B0 + X * B / A, Y]); if (Math.abs(d - g.L) < 0.6) pd_.push([B0 + X * B / A, Y2]); }
    }
    var sp = function (pts, gap) { var out = [], cur = []; pts.forEach(function (p) { if (cur.length && Math.abs(p[0] - cur[cur.length - 1][0]) > gap) { out.push(cur); cur = []; } cur.push(p); }); if (cur.length) out.push(cur); return out; };
    cfL.set([pf]); cgL.set([pg]); cqR.set(sp(pq_, 3 * B / n)); cdR.set(sp(pd_, 3 * B / n)); limR.set([[[B0, Hh / 2], [B0 + B, Hh / 2]]]);
    wdv = wd; var xs = g.a + wd / 2, Xs = A * 0.75, qv = g.f(xs) / g.g(xs), dv = g.df(xs) / g.dg(xs);
    pq.mover(B0 + B * 0.75, Hh / 2 + (qv - g.L) * (Hh / 2) / 0.5); pd.mover(B0 + B * 0.75, Hh / 2 + (dv - g.L) * (Hh / 2) / 0.5);
    pq.visible = pd.visible = Math.abs(qv - g.L) < 0.6;
    l1(fm(qv)); l2(fm(dv)); l3(fm(g.L));
    lv('Ventana |x − a| < ' + fm(wd) + '. Izquierda: f (azul) y g (naranja) reescaladas; derecha: f/g (negro) y f′/g′ (naranja) frente al límite L (verde).');
  }
  c.slider('Ventana w (de 2 a 0,002)', 0, 1, 0.005, s, function (v) { s = v; if (cqR) calc(); }, function (v) { return fm(2 * Math.pow(10, -v * 3)); });
  c.selector('Límite ', F.map(function (g) { return g.n; }), 0, function (i) { k = i; nuevo(); calc(); });
  /* Izquierda: x de a − w a a + w; f y g van reescaladas, así que ese panel no lleva números en vertical. Derecha: x igual y valores de los cocientes (L ± 0,5). */
  c.marcasPropias(function (m) {
    var g = F[k], x0 = g.a - wdv, x1 = g.a + wdv;
    m.marcas('x', 0, A, x0, x1, 0);
    m.marcas('x', B0, B0 + B, x0, x1, 0);
    m.marcas('y', 0, Hh, g.L - 0.5, g.L + 0.5, B0);
  });
  c.leyenda([['var(--acc)','f','linea'],['var(--S)','g; f′/g′','linea'],['var(--fg)','cociente f/g','linea'],['var(--L)','límite L','linea']]);
  c.alCambiarTema(function (q) {
    P = q; c.renderer.setClearColor(q.bg);
    if (!cqR) return;
    ejesL.material.color.set(q.mut); ejesR.material.color.set(q.mut); cfL.material.color.set(q.acc); cgL.material.color.set(q.S); limR.material.color.set(q.L);
    cqR.material.color.set(q.fg); cdR.material.color.set(q.S); pq.material.color.set(q.fg); pd.material.color.set(q.S);
  });
});
