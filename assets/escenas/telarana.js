/* Punto fijo y telaraña (tema 2.4): x_{n+1} = g(x_n). */
Interactivos.registrar('telarana', function (c) {
  var T = c.THREE, H = c.H;
  var m = 0.8;
  var G = [
    { n: 'g(x) = e⁻ˣ', g: function (x) { return Math.exp(-x); }, d: function (x) { return -Math.exp(-x); }, p: 0.5671432904097838, v: [0, 1.6, 0, 1.6], x0: [0, 1.5, 1] },
    { n: 'g(x) = ½ cos x', g: function (x) { return Math.cos(x) / 2; }, d: function (x) { return -Math.sin(x) / 2; }, p: 0.45018361129487357, v: [0, 1.6, 0, 1.6], x0: [0, 1.5, 1.2] },
    { n: 'g(x) = 0,5 + m·sen(x − 0,5) (m con el deslizador)', g: function (x) { return 0.5 + m * Math.sin(x - 0.5); }, d: function (x) { return m * Math.cos(x - 0.5); }, p: 0.5, v: [-0.5, 1.5, -0.5, 1.5], x0: [-0.4, 1.4, 1] }
  ];
  var W = function (v) { var dx = 1.5 * (v[1] - v[0]), dy = 1.5 * (v[3] - v[2]); return [v[0] - dx, v[1] + dx, v[2] - dy, v[3] + dy]; };
  var k = 0, x0 = 1, n = 6, P = c.colores(), w, ejes, curva, diag, red, dots = [];
  var lx = c.lectura('xₙ'), le = c.lectura('|xₙ − punto fijo|'), lg = c.lectura('g′(x*)');

  function nuevo() {
    [ejes, curva, diag, red].forEach(function (o) { if (o) c.scene.remove(o); });
    dots.forEach(function (o) { c.scene.remove(o); }); dots = [];
    var v = G[k].v; w = 0.0055 * (v[3] - v[2]); c.vista(v[0], v[1], v[2], v[3]);
    var vw = W(v);
    ejes = H.ejes2D(T, vw, w, P.fg, P.bd);
    c.scene.add(ejes);
    diag = H.cinta(T, [[[vw[0], vw[0]], [vw[1], vw[1]]]], P.mut, w, [w * 5, w * 3]); diag.position.z = 0.1; c.scene.add(diag);
    curva = H.cinta(T, [], P.fg, w * 1.4); curva.position.z = 0.2; c.scene.add(curva);
    red = H.cinta(T, [], P.S, w * 1.1); red.position.z = 0.3; c.scene.add(red);
    var d = H.punto(T, G[k].p, G[k].p, w * 2.4, P.fg); d.position.z = 0.4; dots.push(d); c.scene.add(d);
    pintaCurva();
  }
  function pintaCurva() { var v = W(G[k].v); if (curva) curva.set(H.grafica(G[k].g, v[0], v[1], 1200, 1e3)); }
  function calc() {
    var g = G[k], x = x0, pts = [[x, 0]], i, xs = [x0];
    for (i = 0; i < n; i++) { var y = g.g(x); pts.push([x, y], [y, y]); x = y; xs.push(x); }
    red.set([pts]);
    var fm = function (t) { return (Math.round(t * 1e5) / 1e5).toString().replace('-', '−'); };
    lx(fm(x)); le(fm(Math.abs(x - g.p))); lg(fm(g.d(g.p)) + (Math.abs(g.d(g.p)) < 1 ? '  (|g′| < 1: atrae)' : '  (|g′| ≥ 1: no atrae)'));
  }
  var sx = c.slider('x₀', 0, 1.5, 0.05, 1, function (v) { x0 = v; if (red) calc(); });
  c.slider('Iteraciones n', 0, 15, 1, 6, function (v) { n = v; if (red) calc(); }, function (v) { return String(v); });
  c.slider('m', -1.6, 1.6, 0.05, 0.8, function (v) { m = v; if (red) { pintaCurva(); calc(); } });
  c.selector('Función ', G.map(function (g) { return g.n; }), 0, function (i) {
    k = i; nuevo(); sx.min = G[i].x0[0]; sx.max = G[i].x0[1]; sx.value = G[i].x0[2]; sx.dispatchEvent(new Event('input'));
  });
  c.alCambiarTema(function (p) {
    P = p; c.renderer.setClearColor(p.bg);
    if (!ejes) return;
    ejes.userData.eje.color.set(p.fg); ejes.userData.rejilla.color.set(p.bd); curva.material.color.set(p.fg);
    diag.material.color.set(p.mut); red.material.color.set(p.S); dots[0].material.color.set(p.fg);
  });
});
