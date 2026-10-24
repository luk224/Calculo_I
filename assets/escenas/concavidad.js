/* Concavidad y puntos de inflexión (tema 3.5): una tangente que se desliza por la gráfica. */
Interactivos.registrar('concavidad', function (c) {
  var T = c.THREE, H = c.H;
  var W = function (v) { var dx = 1.5 * (v[1] - v[0]), dy = 1.5 * (v[3] - v[2]); return [v[0] - dx, v[1] + dx, v[2] - dy, v[3] + dy]; };
  var F = [
    { n: 'x³', f: function (x) { return x * x * x; }, d: function (x) { return 3 * x * x; }, dd: function (x) { return 6 * x; }, v: [-2, 2, -3, 3], r: [-2, 2, 1] },
    { n: 'x⁴/4 − x² (dos inflexiones en ±√(2/3))', f: function (x) { return Math.pow(x, 4) / 4 - x * x; }, d: function (x) { return x * x * x - 2 * x; },
      dd: function (x) { return 3 * x * x - 2; }, v: [-2.5, 2.5, -1.6, 4], r: [-2.5, 2.5, 1.5] },
    { n: 'sen x', f: Math.sin, d: Math.cos, dd: function (x) { return -Math.sin(x); }, v: [-6, 6, -2.5, 2.5], r: [-6, 6, 1] },
    { n: 'x⁴ (f″(0) = 0 pero NO hay inflexión)', f: function (x) { return Math.pow(x, 4); }, d: function (x) { return 4 * x * x * x; }, dd: function (x) { return 12 * x * x; }, v: [-2, 2, -1, 5], r: [-2, 2, 0.5] }
  ];
  var k = 0, x0 = 1, P = c.colores(), w, vw, ejes, curva, tg, pt, infl = [];
  var l1 = c.lectura('f′(x)'), l2 = c.lectura('f″(x)'), lv = c.lectura('');
  var fm = function (t) { return (Math.round(t * 1000) / 1000).toString().replace('-', '−'); };

  function nuevo() {
    [ejes, curva, tg, pt].forEach(function (o) { if (o) c.scene.remove(o); });
    infl.forEach(function (o) { c.scene.remove(o); }); infl = [];
    var g = F[k], v = g.v; w = 0.0055 * (v[3] - v[2]); c.vista(v[0], v[1], v[2], v[3]); vw = W(v);
    ejes = H.ejes2D(T, vw, w, P.fg, P.bd); c.scene.add(ejes);
    curva = H.cinta(T, H.grafica(g.f, vw[0], vw[1], 1600, 1e3), P.fg, w * 1.4); curva.position.z = 0.1; c.scene.add(curva);
    tg = H.cinta(T, [], P.S, w * 1.3); tg.position.z = 0.3; c.scene.add(tg);
    pt = H.punto(T, 0, 0, w * 2.6, P.S); pt.position.z = 0.6; c.scene.add(pt);
    // puntos de inflexión: cambios de signo de f″ (afinados por bisección)
    var N = 3000, i, a, b, lo, hi, j, m;
    for (i = 0; i < N; i++) {
      a = vw[0] + (vw[1] - vw[0]) * i / N; b = vw[0] + (vw[1] - vw[0]) * (i + 1) / N;
      if (g.dd(a) * g.dd(b) < 0) {
        lo = a; hi = b;
        for (j = 0; j < 50; j++) { m = (lo + hi) / 2; if (g.dd(lo) * g.dd(m) <= 0) hi = m; else lo = m; }
        var r = (lo + hi) / 2, d = H.punto(T, r, g.f(r), w * 2.6, P.L); d.position.z = 0.5; infl.push(d); c.scene.add(d);
      }
    }
  }
  function calc() {
    var g = F[k], fx = g.f(x0), m = g.d(x0), s = g.dd(x0);
    tg.set([[[vw[0], fx + m * (vw[0] - x0)], [vw[1], fx + m * (vw[1] - x0)]]]);
    pt.mover(x0, fx);
    l1(fm(m)); l2(fm(s));
    lv(Math.abs(s) < 0.02 ? 'f″ ≈ 0: aquí la tangente atraviesa o roza la curva' :
       s > 0 ? 'Convexa (f″ > 0): la curva queda por encima de la tangente' : 'Cóncava (f″ < 0): la curva queda por debajo de la tangente');
  }
  var sl = c.slider('x', -2, 2, 0.01, 1, function (v) { x0 = v; if (tg) calc(); });
  c.selector('Función ', F.map(function (g) { return g.n; }), 0, function (i) {
    k = i; nuevo(); sl.min = F[i].r[0]; sl.max = F[i].r[1]; sl.value = F[i].r[2]; sl.dispatchEvent(new Event('input'));
  });
  c.leyenda([['var(--fg)','gráfica de f','linea'],['var(--S)','tangente en x','linea'],['var(--L)','puntos de inflexión','punto']]);
  c.alCambiarTema(function (q) {
    P = q; c.renderer.setClearColor(q.bg);
    if (!ejes) return;
    ejes.userData.eje.color.set(q.fg); ejes.userData.rejilla.color.set(q.bd); curva.material.color.set(q.fg);
    tg.material.color.set(q.S); pt.material.color.set(q.S); infl.forEach(function (d) { d.material.color.set(q.L); });
  });
});
