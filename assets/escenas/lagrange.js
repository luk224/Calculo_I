/* Extremos condicionados (tema 5.5): curvas de nivel de f, restricción g = 0 y gradientes. En los candidatos de Lagrange
   la curva de nivel que pasa por el punto es tangente a g = 0 y ∇f es paralelo a ∇g. */
Interactivos.registrar('lagrange', function (c) {
  var T = c.THREE, H = c.H, s2 = Math.SQRT1_2;
  var W = function (v) { var dx = 1.5 * (v[1] - v[0]), dy = 1.5 * (v[3] - v[2]); return [v[0] - dx, v[1] + dx, v[2] - dy, v[3] + dy]; };
  var F = [
    { n: 'f = x − y sobre x² + y² = 1 (E 5.42)', f: function (x, y) { return x - y; }, gf: function () { return [1, -1]; },
      g: function (x, y) { return x * x + y * y - 1; }, gg: function (x, y) { return [2 * x, 2 * y]; }, p: function (t) { return [Math.cos(t), Math.sin(t)]; }, t0: 60, d: 2.2 },
    { n: 'f = x² + 2y² sobre x² + y² = 1 (Ej. 5.24 de U)', f: function (x, y) { return x * x + 2 * y * y; }, gf: function (x, y) { return [2 * x, 4 * y]; },
      g: function (x, y) { return x * x + y * y - 1; }, gg: function (x, y) { return [2 * x, 2 * y]; }, p: function (t) { return [Math.cos(t), Math.sin(t)]; }, t0: 30, d: 2.2 },
    { n: 'f = xy sobre x² + y² = 1 (X, sept. 2017)', f: function (x, y) { return x * y; }, gf: function (x, y) { return [y, x]; },
      g: function (x, y) { return x * x + y * y - 1; }, gg: function (x, y) { return [2 * x, 2 * y]; }, p: function (t) { return [Math.cos(t), Math.sin(t)]; }, t0: 20, d: 2.2 },
    { n: 'f = x² + y² sobre la elipse 5x² + 6xy + 5y² = 8 (X, 2010)', f: function (x, y) { return x * x + y * y; }, gf: function (x, y) { return [2 * x, 2 * y]; },
      g: function (x, y) { return 5 * x * x + 6 * x * y + 5 * y * y - 8; }, gg: function (x, y) { return [10 * x + 6 * y, 6 * x + 10 * y]; },
      p: function (t) { var u = Math.cos(t), v = 2 * Math.sin(t); return [(u + v) * s2, (u - v) * s2]; }, t0: 30, d: 2.8 }
  ];
  var k = 0, th = F[0].t0, P = c.colores(), w = 0.033, ejes, rest, niv, gf, gg, pt, v0, vw;
  var l1 = c.lectura('Punto (x, y) sobre g = 0'), l2 = c.lectura('f(x, y)'), l3 = c.lectura('∇f y ∇g'), l4 = c.lectura('∇f × ∇g = f_x·g_y − f_y·g_x'), lv = c.lectura('');
  function fm(t) { return (Math.round(t * 1000) / 1000).toString().replace('-', '−'); }
  function flecha(a, b, q, len) {
    var n = Math.hypot(q[0], q[1]); if (n < 1e-9) return [];
    var ux = q[0] / n, uy = q[1] / n, e = [a + len * ux, b + len * uy], h = 0.16, k1 = 0.45;
    return [[[a, b], e], [e, [e[0] - h * (ux + k1 * uy), e[1] - h * (uy - k1 * ux)]], [e, [e[0] - h * (ux - k1 * uy), e[1] - h * (uy + k1 * ux)]]];
  }
  function limpiar() { [ejes, rest, niv, gf, gg, pt].forEach(function (o) { if (o) c.scene.remove(o); }); }
  function nuevo() {
    limpiar(); var g = F[k], d = g.d; v0 = [-d, d, -d, d]; vw = W(v0);
    c.vista(v0[0], v0[1], v0[2], v0[3]);
    ejes = H.ejes2D(T, vw, w, P.fg, P.bd); c.scene.add(ejes);
    rest = H.cinta(T, [H.nivel(g.g, 0, vw[1], 600).map(function (s) { return [[s[0], s[1]], [s[2], s[3]]]; })][0], P.fg, w * 1.6); rest.position.z = 0.1; c.scene.add(rest);
    niv = H.cinta(T, [], P.S, w * 1.3); niv.position.z = 0.2; c.scene.add(niv);
    gf = H.cinta(T, [], P.acc, w * 1.5); gf.position.z = 0.4; c.scene.add(gf);
    gg = H.cinta(T, [], P.L, w * 1.5); gg.position.z = 0.35; c.scene.add(gg);
    pt = H.punto(T, 0, 0, w * 3, P.fg); pt.position.z = 0.6; c.scene.add(pt);
  }
  function calc() {
    var g = F[k], t = th * Math.PI / 180, p = g.p(t), x = p[0], y = p[1], fa = g.f(x, y), a = g.gf(x, y), b = g.gg(x, y);
    var seg = H.nivel(g.f, fa, vw[1], 480), cruz = a[0] * b[1] - a[1] * b[0], na = Math.hypot(a[0], a[1]), nb = Math.hypot(b[0], b[1]);
    niv.set(seg.map(function (s) { return [[s[0], s[1]], [s[2], s[3]]]; }));
    pt.mover(x, y);
    gf.set(flecha(x, y, a, 0.7)); gg.set(flecha(x, y, b, 0.7));
    l1('(' + fm(x) + ', ' + fm(y) + ')'); l2(fm(fa)); l3('∇f = (' + fm(a[0]) + ', ' + fm(a[1]) + ');  ∇g = (' + fm(b[0]) + ', ' + fm(b[1]) + ')'); l4(fm(cruz));
    if (na > 1e-9 && nb > 1e-9 && Math.abs(cruz) / (na * nb) < 0.01) {
      var lam = -(a[0] * b[0] + a[1] * b[1]) / (nb * nb);
      lv('∇f ∥ ∇g: candidato de Lagrange, con λ = ' + fm(lam) + '. La curva de nivel (naranja) es tangente a la restricción.');
    } else lv('∇f y ∇g no son paralelos: la curva de nivel corta a la restricción, así que f todavía puede crecer o decrecer moviéndose sobre ella.');
  }
  c.selector('Problema ', F.map(function (g) { return g.n; }), 0, function (i) { k = i; nuevo(); if (sl) { th = F[i].t0; sl.value = th; sl.dispatchEvent(new Event('input')); } });
  var sl = c.slider('Posición sobre la restricción', 0, 360, 1, th, function (v) { th = v; if (pt) calc(); }, function (v) { return Math.round(v) + '°'; });
  calc();
  c.leyenda([['var(--fg)','restricción g = 0; punto','linea'],['var(--S)','curva de nivel de f por el punto','linea'],['var(--acc)','∇f','linea'],['var(--L)','∇g','linea']]);
  c.alCambiarTema(function (q) {
    P = q; c.renderer.setClearColor(q.bg);
    if (!pt) return;
    ejes.userData.eje.color.set(q.fg); ejes.userData.rejilla.color.set(q.bd); rest.material.color.set(q.fg);
    niv.material.color.set(q.S); gf.material.color.set(q.acc); gg.material.color.set(q.L); pt.material.color.set(q.fg);
  });
});
