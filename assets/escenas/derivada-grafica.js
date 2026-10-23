/* f y f′ superpuestas (tema 2.2): arriba f con su tangente; abajo f′, que es la pendiente de esa tangente. */
Interactivos.registrar('derivada-grafica', function (c) {
  var T = c.THREE, H = c.H;
  var F = [
    { n: 'x³ − 3x', f: function (x) { return x * x * x - 3 * x; }, d: function (x) { return 3 * x * x - 3; }, x: [-2.2, 2.2], fy: [-4.5, 4.5], dy: [-4, 12] },
    { n: 'sen x', f: Math.sin, d: Math.cos, x: [-6.3, 6.3], fy: [-1.3, 1.3], dy: [-1.3, 1.3] },
    { n: 'x·e⁻ˣ  (regla del producto)', f: function (x) { return x * Math.exp(-x); }, d: function (x) { return (1 - x) * Math.exp(-x); }, x: [-0.5, 5], fy: [-1, 0.5], dy: [-0.6, 2.6] },
    { n: 'sen(x²)  (regla de la cadena)', f: function (x) { return Math.sin(x * x); }, d: function (x) { return 2 * x * Math.cos(x * x); }, x: [-2.5, 2.5], fy: [-1.3, 1.3], dy: [-5.5, 5.5] },
    { n: '1/(1 + x²)  (regla del cociente)', f: function (x) { return 1 / (1 + x * x); }, d: function (x) { return -2 * x / Math.pow(1 + x * x, 2); }, x: [-3, 3], fy: [-0.2, 1.1], dy: [-0.8, 0.8] }
  ];
  var X = 6.4, Hh = 3.2, Y0 = 3.8, w = 0.04, k = 0, x0 = 0.8, P = c.colores();
  var ejes, cf, cd, tg, pf, pd, guia, cero = [], crit = [];
  var l1 = c.lectura('f(x)'), l2 = c.lectura('f′(x) = pendiente de la tangente'), lv = c.lectura('');
  function fm(t) { return (Math.round(t * 1000) / 1000).toString().replace('-', '−'); }
  function mx(g, x) { return X * (x - g.x[0]) / (g.x[1] - g.x[0]); }
  function mf(g, y) { return Y0 + Hh * (y - g.fy[0]) / (g.fy[1] - g.fy[0]); }
  function md(g, y) { return Hh * (y - g.dy[0]) / (g.dy[1] - g.dy[0]); }
  function nuevo() {
    [ejes, cf, cd, tg, pf, pd, guia].forEach(function (o) { if (o) c.scene.remove(o); });
    crit.forEach(function (o) { c.scene.remove(o); }); crit = [];
    var g = F[k], i, n = 400, A = [], B = [], x, ax = [];
    c.vista(-0.4, X + 0.4, -0.4, Y0 + Hh + 0.3);
    ax.push([[0, 0], [0, Hh]], [[0, Y0], [0, Y0 + Hh]]);
    if (g.dy[0] < 0 && g.dy[1] > 0) ax.push([[0, md(g, 0)], [X, md(g, 0)]]); else ax.push([[0, 0], [X, 0]]);
    if (g.fy[0] < 0 && g.fy[1] > 0) ax.push([[0, mf(g, 0)], [X, mf(g, 0)]]); else ax.push([[0, Y0], [X, Y0]]);
    if (g.x[0] < 0 && g.x[1] > 0) ax.push([[mx(g, 0), 0], [mx(g, 0), Hh]], [[mx(g, 0), Y0], [mx(g, 0), Y0 + Hh]]);
    ejes = H.cinta(T, ax, P.mut, w); ejes.position.z = 0.05; c.scene.add(ejes);
    for (i = 0; i <= n; i++) { x = g.x[0] + (g.x[1] - g.x[0]) * i / n; A.push([mx(g, x), mf(g, g.f(x))]); B.push([mx(g, x), md(g, g.d(x))]); }
    cf = H.cinta(T, [A], P.fg, w * 1.4); cd = H.cinta(T, [B], P.acc, w * 1.4); cf.position.z = cd.position.z = 0.1; c.scene.add(cf, cd);
    guia = H.cinta(T, [], P.mut, w * 0.8, [w * 4, w * 3]); guia.position.z = 0.15; c.scene.add(guia);
    tg = H.cinta(T, [], P.S, w * 1.3); tg.position.z = 0.3; c.scene.add(tg);
    pf = H.punto(T, 0, 0, w * 2.8, P.S); pd = H.punto(T, 0, 0, w * 2.8, P.S); pf.position.z = pd.position.z = 0.6; c.scene.add(pf, pd);
    // puntos con f′ = 0 (tangente horizontal)
    for (i = 0; i < n; i++) { var a0 = g.x[0] + (g.x[1] - g.x[0]) * i / n, a1 = g.x[0] + (g.x[1] - g.x[0]) * (i + 1) / n;
      if (g.d(a0) * g.d(a1) < 0) { var r = (a0 + a1) / 2, p1 = H.punto(T, mx(g, r), mf(g, g.f(r)), w * 2.4, P.L), p2 = H.punto(T, mx(g, r), md(g, 0), w * 2.4, P.L); p1.position.z = p2.position.z = 0.4; crit.push(p1, p2); c.scene.add(p1, p2); } }
  }
  function calc() {
    var g = F[k], f = g.f(x0), d = g.d(x0), X1 = mx(g, x0), yf = mf(g, f), yd = md(g, d);
    pf.mover(X1, yf); pd.mover(X1, yd); guia.set([[[X1, yd], [X1, yf]]]);
    var m = d * (Hh / (g.fy[1] - g.fy[0])) / (X / (g.x[1] - g.x[0])), nn = Math.sqrt(1 + m * m), L = 0.9;
    tg.set([[[X1 - L / nn, yf - L * m / nn], [X1 + L / nn, yf + L * m / nn]]]);
    l1(fm(f)); l2(fm(d));
    lv(Math.abs(d) < 0.03 ? 'f′ ≈ 0: tangente horizontal (posible máximo o mínimo).' : d > 0 ? 'f′ > 0: la tangente sube y f crece.' : 'f′ < 0: la tangente baja y f decrece.');
  }
  var sl = c.slider('x', -1, 1, 0.001, 0.5, function (u) { var g = F[k]; x0 = g.x[0] + (g.x[1] - g.x[0]) * (u + 1) / 2; if (tg) calc(); }, function (u) { var g = F[k]; return fm(g.x[0] + (g.x[1] - g.x[0]) * (u + 1) / 2); });
  c.selector('Función ', F.map(function (g) { return g.n; }), 0, function (i) { k = i; nuevo(); sl.value = 0.5; sl.dispatchEvent(new Event('input')); });
  c.alCambiarTema(function (q) {
    P = q; c.renderer.setClearColor(q.bg);
    if (!tg) return;
    ejes.material.color.set(q.mut); cf.material.color.set(q.fg); cd.material.color.set(q.acc); guia.material.color.set(q.mut); tg.material.color.set(q.S);
    pf.material.color.set(q.S); pd.material.color.set(q.S); crit.forEach(function (o) { o.material.color.set(q.L); });
  });
});
