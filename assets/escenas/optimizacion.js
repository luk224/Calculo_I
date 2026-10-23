/* Problemas de optimización (tema 3.4): la figura cambia con x y la gráfica de A(x) marca el óptimo.
   A la izquierda, la gráfica (dominio y valores reescalados a un recuadro); a la derecha, la figura. */
Interactivos.registrar('optimizacion', function (c) {
  var T = c.THREE, H = c.H, PI = Math.PI;
  var circ = function (cx, cy, r) { var p = [], i; for (i = 0; i <= 60; i++) p.push([cx + r * Math.cos(2 * PI * i / 60), cy + r * Math.sin(2 * PI * i / 60)]); return p; };
  var rect = function (x0, y0, w, h) { return [[x0, y0], [x0 + w, y0], [x0 + w, y0 + h], [x0, y0 + h], [x0, y0]]; };
  var C = [
    { n: 'Recinto rectangular con 100 m de tela (Ej. 3.25 de U)', xa: 0, xb: 50, ya: 0, yb: 650, meta: 'max', xn: 'x (un lado, m)',
      A: function (x) { return x * (50 - x); }, dA: function (x) { return 50 - 2 * x; }, otro: function (x) { return 'otro lado = ' + fm(50 - x) + ' m'; }, ref: 'área en m²',
      forma: function (x) { var s = 4 / 50; return { marco: [rect(8, 0, 4, 4)], fig: [rect(8, 0, x * s, (50 - x) * s)] }; } },
    { n: 'Cuadrado + círculo con 100 m de tela (Ej. 3.26 de U)', xa: 0, xb: 25, ya: 300, yb: 850, meta: 'max', xn: 'x (lado del cuadrado, m)',
      A: function (x) { return x * x + Math.pow(50 - 2 * x, 2) / PI; }, dA: function (x) { return 2 * x - 4 * (50 - 2 * x) / PI; }, otro: function (x) { return 'radio del círculo = ' + fm((50 - 2 * x) / PI) + ' m'; }, ref: 'área total en m²',
      forma: function (x) { var s = 0.16, r = (50 - 2 * x) / PI; return { marco: [], fig: [rect(7.5, 0, x * s, x * s), circ(11.8, 2.5, r * s)] }; } },
    { n: 'Lata cilíndrica de 1 litro: menos material', xa: 2.5, xb: 9, ya: 500, yb: 880, meta: 'min', xn: 'r (radio, cm)',
      A: function (r) { return 2 * PI * r * r + 2000 / r; }, dA: function (r) { return 4 * PI * r - 2000 / (r * r); }, otro: function (r) { return 'altura = ' + fm(1000 / (PI * r * r)) + ' cm'; }, ref: 'superficie en cm²',
      forma: function (r) { var s = 4 / 55, h = 1000 / (PI * r * r); return { marco: [], fig: [rect(10.5 - r * s, 0, 2 * r * s, h * s)] }; } }
  ];
  var k = 0, x = 25, P = c.colores(), w = 0.04, ejes, curva, guia, pt, opt = [], crit = [], marco, fig;
  var l1 = c.lectura('x'), l2 = c.lectura(''), l3 = c.lectura('Cantidad a optimizar'), l4 = c.lectura('A′(x)'), lv = c.lectura('');
  function fm(t) { return (Math.round(t * 100) / 100).toString().replace('-', '−'); }
  var GX = 6, GY = 3.6;
  function mapa(g, xx, yy) { return [GX * (xx - g.xa) / (g.xb - g.xa), GY * (yy - g.ya) / (g.yb - g.ya)]; }
  function limpia(arr) { arr.forEach(function (o) { c.scene.remove(o); }); arr.length = 0; }
  function nuevo() {
    [ejes, curva, guia, pt, marco, fig].forEach(function (o) { if (o) c.scene.remove(o); });
    limpia(opt); limpia(crit);
    var g = C[k], i, n = 300, pts = [], xs;
    c.vista(-0.8, 14.6, -0.6, 4.6);
    ejes = H.cinta(T, [[[0, 0], [GX, 0]], [[0, 0], [0, GY]]], P.fg, w); ejes.position.z = 0.05; c.scene.add(ejes);
    for (i = 0; i <= n; i++) { xs = g.xa + (g.xb - g.xa) * i / n; pts.push(mapa(g, xs, g.A(xs))); }
    curva = H.cinta(T, [pts], P.fg, w * 1.4); curva.position.z = 0.1; c.scene.add(curva);
    guia = H.cinta(T, [], P.mut, w * 0.8, [w * 4, w * 3]); guia.position.z = 0.15; c.scene.add(guia);
    pt = H.punto(T, 0, 0, w * 2.8, P.S); pt.position.z = 0.6; c.scene.add(pt);
    marco = H.cinta(T, [], P.mut, w * 0.8, [w * 4, w * 3]); marco.position.z = 0.1; c.scene.add(marco);
    fig = H.cinta(T, [], P.S, w * 1.3); fig.position.z = 0.3; c.scene.add(fig);
    // óptimo absoluto (verde) y puntos críticos (azul)
    var best = g.xa, bv = g.A(best), cr = [];
    for (i = 0; i <= 4000; i++) { xs = g.xa + (g.xb - g.xa) * i / 4000; var v = g.A(xs); if (g.meta === 'max' ? v > bv : v < bv) { bv = v; best = xs; } }
    for (i = 0; i < 4000; i++) { var a0 = g.xa + (g.xb - g.xa) * i / 4000, a1 = g.xa + (g.xb - g.xa) * (i + 1) / 4000; if (g.dA(a0) * g.dA(a1) < 0) cr.push((a0 + a1) / 2); }
    cr.forEach(function (xc) { var m = mapa(g, xc, g.A(xc)), d = H.punto(T, m[0], m[1], w * 2.4, P.acc); d.position.z = 0.4; crit.push(d); c.scene.add(d); });
    var mb = mapa(g, best, bv), db = H.punto(T, mb[0], mb[1], w * 3.4, P.L); db.position.z = 0.35; opt.push(db); c.scene.add(db);
    g.best = best; g.bv = bv;
  }
  function calc() {
    var g = C[k], v = g.A(x), m = mapa(g, x, v), f = g.forma(x);
    pt.mover(m[0], m[1]); guia.set([[[m[0], 0], [m[0], m[1]]]]);
    marco.set(f.marco); fig.set(f.fig);
    l1(fm(x)); l2(g.otro(x)); l3(fm(v) + ' (' + g.ref + ')'); l4(fm(g.dA(x)));
    lv((g.meta === 'max' ? 'Máximo' : 'Mínimo') + ' absoluto (punto verde): x = ' + fm(g.best) + ', valor ' + fm(g.bv) + '. Puntos azules: A′ = 0.');
  }
  var sl = c.slider('x', 0, 1, 0.001, 0.5, function (u) { var g = C[k]; x = g.xa + (g.xb - g.xa) * u; if (pt) calc(); }, function (u) { var g = C[k]; return fm(g.xa + (g.xb - g.xa) * u); });
  c.selector('Problema ', C.map(function (g) { return g.n; }), 0, function (i) { k = i; nuevo(); sl.value = 0.5; sl.dispatchEvent(new Event('input')); });
  c.alCambiarTema(function (q) {
    P = q; c.renderer.setClearColor(q.bg);
    if (!pt) return;
    ejes.material.color.set(q.fg); curva.material.color.set(q.fg); guia.material.color.set(q.mut); pt.material.color.set(q.S); marco.material.color.set(q.mut); fig.material.color.set(q.S);
    crit.forEach(function (d) { d.material.color.set(q.acc); }); opt.forEach(function (d) { d.material.color.set(q.L); });
  });
});
