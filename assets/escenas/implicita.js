/* Curva de nivel F(x,y) = c por el punto (a,b): pendiente de la tangente −F_x/F_y y puntos con F_y = 0 (tema 5.3). */
Interactivos.registrar('implicita', function (c) {
  var T = c.THREE, H = c.H;
  var W = function (v) { var dx = 1.5 * (v[1] - v[0]), dy = 1.5 * (v[3] - v[2]); return [v[0] - dx, v[1] + dx, v[2] - dy, v[3] + dy]; };
  var F = [
    { n: 'x² + y² (circunferencia)', f: function (x, y) { return x * x + y * y; }, fx: function (x) { return 2 * x; }, fy: function (x, y) { return 2 * y; }, a: 1.2, b: 0.8 },
    { n: 'x² + 3xy − y² (Ej. 5.13 de U)', f: function (x, y) { return x * x + 3 * x * y - y * y; }, fx: function (x, y) { return 2 * x + 3 * y; }, fy: function (x, y) { return 3 * x - 2 * y; }, a: 1, b: 0 },
    { n: 'x³ + y³ − 3xy (folium de Descartes)', f: function (x, y) { return x * x * x + y * y * y - 3 * x * y; }, fx: function (x, y) { return 3 * x * x - 3 * y; }, fy: function (x, y) { return 3 * y * y - 3 * x; }, a: 1.5, b: 1.5 },
    { n: 'y² − x³ + x (curva elíptica)', f: function (x, y) { return y * y - x * x * x + x; }, fx: function (x) { return -3 * x * x + 1; }, fy: function (x, y) { return 2 * y; }, a: 1.5, b: 1.1 }
  ];
  var v0 = [-3, 3, -3, 3], vw = W(v0), k = 0, a = 1, b = 0.5, P = c.colores(), w = 0.0055 * 6, ejes, curva, tg, gr, pt, vert = [];
  var l1 = c.lectura('Nivel c = F(a, b)'), l2 = c.lectura('(F_x, F_y) en (a, b)'), l3 = c.lectura('Pendiente y′ = −F_x / F_y'), lv = c.lectura('');
  function fm(t) { return (Math.round(t * 1000) / 1000).toString().replace('-', '−'); }
  function nuevo() {
    c.vista(v0[0], v0[1], v0[2], v0[3]);
    ejes = H.ejes2D(T, vw, w, P.fg, P.bd); c.scene.add(ejes);
    curva = H.cinta(T, [], P.fg, w * 1.4); curva.position.z = 0.1; c.scene.add(curva);
    tg = H.cinta(T, [], P.S, w * 1.3); tg.position.z = 0.3; c.scene.add(tg);
    gr = H.cinta(T, [], P.acc, w * 1.3); gr.position.z = 0.35; c.scene.add(gr);
    pt = H.punto(T, 0, 0, w * 2.8, P.S); pt.position.z = 0.6; c.scene.add(pt);
  }
  function calc() {
    var g = F[k], d = vw[1], fa = g.f(a, b), fx = g.fx(a, b), fy = g.fy(a, b), seg = H.nivel(g.f, fa, d, 360), i, s;
    curva.set(seg.map(function (q) { return [[q[0], q[1]], [q[2], q[3]]]; }));
    // puntos de la curva con F_y = 0 (tangente vertical): cambio de signo de F_y dentro de un segmento
    vert.forEach(function (o) { c.scene.remove(o); }); vert = [];
    for (i = 0; i < seg.length; i++) {
      s = seg[i]; var u = g.fy(s[0], s[1]), t = g.fy(s[2], s[3]);
      if (u * t < 0) { var r = u / (u - t), px = s[0] + (s[2] - s[0]) * r, py = s[1] + (s[3] - s[1]) * r;
        if (px > v0[0] && px < v0[1] && py > v0[2] && py < v0[3]) { var o = H.punto(T, px, py, w * 2.6, P.L); o.position.z = 0.5; vert.push(o); c.scene.add(o); } }
    }
    pt.mover(a, b);
    var L = 6, n = Math.hypot(fx, fy);
    if (Math.abs(fy) > 1e-6) { var m = -fx / fy; tg.set([[[vw[0], b + m * (vw[0] - a)], [vw[1], b + m * (vw[1] - a)]]]); } else tg.set([[[a, vw[2]], [a, vw[3]]]]);
    gr.set(n > 1e-9 ? [[[a, b], [a + 0.9 * fx / n, b + 0.9 * fy / n]]] : []);
    l1(fm(fa)); l2('(' + fm(fx) + ', ' + fm(fy) + ')');
    l3(Math.abs(fy) < 1e-3 ? 'F_y = 0: tangente vertical (aquí la curva no es la gráfica de una función y(x))' : fm(-fx / fy));
    lv(n < 1e-9 ? 'Gradiente nulo: punto singular, el teorema no se aplica.' : 'La línea azul corta es el gradiente (F_x, F_y): perpendicular a la tangente. Puntos verdes: F_y = 0.');
  }
  nuevo();
  var sa = c.slider('a', -2.5, 2.5, 0.05, a, function (v) { a = v; if (pt) calc(); });
  var sb = c.slider('b', -2.5, 2.5, 0.05, b, function (v) { b = v; if (pt) calc(); });
  c.selector('Función F ', F.map(function (g) { return g.n; }), 0, function (i) {
    k = i; a = F[i].a; b = F[i].b; sa.value = a; sb.value = b; sa.dispatchEvent(new Event('input')); sb.dispatchEvent(new Event('input'));
  });
  calc();
  c.alCambiarTema(function (q) {
    P = q; c.renderer.setClearColor(q.bg);
    if (!pt) return;
    ejes.userData.eje.color.set(q.fg); ejes.userData.rejilla.color.set(q.bd); curva.material.color.set(q.fg);
    tg.material.color.set(q.S); gr.material.color.set(q.acc); pt.material.color.set(q.S); vert.forEach(function (o) { o.material.color.set(q.L); });
  });
});
