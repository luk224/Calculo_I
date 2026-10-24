/* Secante → tangente y normal (tema 2.1): f′(a) como límite de las pendientes de las secantes. */
Interactivos.registrar('secante-tangente', function (c) {
  var T = c.THREE, H = c.H;
  var W = function (v) { var dx = 1.5 * (v[1] - v[0]), dy = 1.5 * (v[3] - v[2]); return [v[0] - dx, v[1] + dx, v[2] - dy, v[3] + dy]; };
  var F = [
    { n: 'x²', f: function (x) { return x * x; }, d: function (x) { return 2 * x; }, v: [-3, 3, -1.5, 6.5] },
    { n: 'x³ − x', f: function (x) { return x * x * x - x; }, d: function (x) { return 3 * x * x - 1; }, v: [-2.5, 2.5, -4, 4] },
    { n: 'sen x', f: Math.sin, d: Math.cos, v: [-4, 4, -2.5, 2.5] },
    { n: 'eˣ', f: Math.exp, d: Math.exp, v: [-3, 3, -1.5, 6.5] }
  ];
  var k = 0, a = 1, h = 1, P = c.colores(), w, vw;
  var ejes, curva, sec, tg, nm, pP, pQ;
  var lms = c.lectura('Pendiente de la secante'), lmt = c.lectura('Pendiente de la tangente f′(a)'), let_ = c.lectura('Tangente'), len = c.lectura('Normal');
  var fm = function (t) { return (Math.round(t * 1000) / 1000).toString().replace('-', '−'); };
  var ec = function (y0, m, x0) { return 'y = ' + fm(y0) + (m < 0 ? ' − ' : ' + ') + fm(Math.abs(m)) + '·(x ' + (x0 < 0 ? '+ ' : '− ') + fm(Math.abs(x0)) + ')'; };

  function nuevo() {
    [ejes, curva, sec, tg, nm, pP, pQ].forEach(function (o) { if (o) c.scene.remove(o); });
    var v = F[k].v; w = 0.0055 * (v[3] - v[2]); c.vista(v[0], v[1], v[2], v[3]); vw = W(v);
    ejes = H.ejes2D(T, vw, w, P.fg, P.bd); c.scene.add(ejes);
    curva = H.cinta(T, H.grafica(F[k].f, vw[0], vw[1], 1600, 1e3), P.fg, w * 1.4); curva.position.z = 0.1; c.scene.add(curva);
    nm = H.cinta(T, [], P.L, w * 1.2); nm.position.z = 0.2; c.scene.add(nm);
    sec = H.cinta(T, [], P.mut, w, [w * 5, w * 3]); sec.position.z = 0.25; c.scene.add(sec);
    tg = H.cinta(T, [], P.S, w * 1.3); tg.position.z = 0.3; c.scene.add(tg);
    pQ = H.punto(T, 0, 0, w * 2.4, P.fg); pP = H.punto(T, 0, 0, w * 2.6, P.S);
    pQ.position.z = 0.5; pP.position.z = 0.6; c.scene.add(pQ, pP);
  }
  function recta(m) { var fa = F[k].f(a); return [[[vw[0], fa + m * (vw[0] - a)], [vw[1], fa + m * (vw[1] - a)]]]; }
  function calc() {
    var g = F[k], fa = g.f(a), m = g.d(a), hh = Math.abs(h) < 0.025 ? (h < 0 ? -0.025 : 0.025) : h, q = a + hh, fq = g.f(q), ms = (fq - fa) / hh;
    sec.set(recta(ms)); tg.set(recta(m));
    nm.set(Math.abs(m) < 1e-9 ? [[[a, vw[2]], [a, vw[3]]]] : recta(-1 / m));
    pP.mover(a, fa); pQ.mover(q, fq);
    lms(fm(ms)); lmt(fm(m)); let_(ec(fa, m, a));
    len(Math.abs(m) < 1e-9 ? 'x = ' + fm(a) + ' (vertical)' : ec(fa, -1 / m, a));
  }
  c.slider('Punto a', -2, 2, 0.05, a, function (v) { a = v; if (tg) calc(); });
  c.slider('Incremento h', -1.5, 1.5, 0.05, h, function (v) { h = v; if (tg) calc(); });
  c.selector('Función ', F.map(function (g) { return g.n; }), 0, function (i) { k = i; nuevo(); calc(); });
  c.leyenda([['var(--fg)','gráfica de f; punto Q','linea'],['var(--mut)','secante PQ','linea'],['var(--S)','tangente; punto P','linea'],['var(--L)','normal','linea']]);
  c.alCambiarTema(function (p) {
    P = p; c.renderer.setClearColor(p.bg);
    if (!ejes) return;
    ejes.userData.eje.color.set(p.fg); ejes.userData.rejilla.color.set(p.bd); curva.material.color.set(p.fg);
    nm.material.color.set(p.L); sec.material.color.set(p.mut); tg.material.color.set(p.S); pP.material.color.set(p.S); pQ.material.color.set(p.fg);
  });
});
