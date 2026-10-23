/* Método de Newton paso a paso (tema 2.4): tangente en (xₙ, f(xₙ)) y corte con el eje x. */
Interactivos.registrar('newton', function (c) {
  var T = c.THREE, H = c.H;
  var F = [
    { n: 'x² − 2 (raíz √2)', f: function (x) { return x * x - 2; }, d: function (x) { return 2 * x; }, raiz: Math.SQRT2, v: [-1, 3.6, -3, 7], x0: [0.3, 3.2, 2.5] },
    { n: 'cos x − x', f: function (x) { return Math.cos(x) - x; }, d: function (x) { return -Math.sin(x) - 1; }, raiz: 0.7390851332151607, v: [-1, 3.6, -3.5, 2.5], x0: [-0.5, 3, 2] },
    { n: 'x³ − 2x + 2 (cicla con x₀ = 0)', f: function (x) { return x * x * x - 2 * x + 2; }, d: function (x) { return 3 * x * x - 2; }, raiz: -1.7692923542386314, v: [-3, 3, -4, 8], x0: [-2.5, 2.5, 0] },
    { n: '∛x (diverge siempre)', f: Math.cbrt, d: function (x) { var q = Math.cbrt(x); return 1 / (3 * q * q); }, raiz: 0, v: [-4, 4, -2.5, 2.5], x0: [-1.2, 1.2, 0.5] }
  ];
  var W = function (v) { var dx = 1.5 * (v[1] - v[0]), dy = 1.5 * (v[3] - v[2]); return [v[0] - dx, v[1] + dx, v[2] - dy, v[3] + dy]; };
  var k = 0, x0 = F[0].x0[2], n = 3;
  var P = c.colores(), w, malla, ejes, curva, tang, vert, dots = [], raizPt;
  var lx = c.lectura('xₙ'), lf = c.lectura('f(xₙ)'), le = c.lectura('|xₙ − raíz|'), lm = c.lectura('');

  function nuevo() {
    [ejes, curva, tang, vert, raizPt].forEach(function (o) { if (o) c.scene.remove(o); });
    dots.forEach(function (o) { c.scene.remove(o); }); dots = [];
    var v = F[k].v; w = 0.0055 * (v[3] - v[2]); c.vista(v[0], v[1], v[2], v[3]);
    var vw = W(v);
    ejes = H.ejes2D(T, vw, w, P.fg, P.bd); c.scene.add(ejes);
    curva = H.cinta(T, H.grafica(F[k].f, vw[0], vw[1], 1600, 1e3), P.fg, w * 1.4); curva.position.z = 0.1; c.scene.add(curva);
    vert = H.cinta(T, [], P.mut, w * 0.7, [w * 4, w * 3]); vert.position.z = 0.2; c.scene.add(vert);
    tang = H.cinta(T, [], P.S, w * 1.2); tang.position.z = 0.3; c.scene.add(tang);
    raizPt = H.punto(T, F[k].raiz, 0, w * 2.2, P.fg); raizPt.position.z = 0.4; c.scene.add(raizPt);
    for (var i = 0; i <= 9; i++) { var d = H.punto(T, 0, 0, w * 2.4, P.acc); d.position.z = 0.5; d.visible = false; dots.push(d); c.scene.add(d); }
  }
  function calc() {
    var g = F[k], xs = [x0], i, tg = [], vt = [], parado = false;
    for (i = 0; i < n; i++) {
      var xi = xs[i], fi = g.f(xi), di = g.d(xi);
      if (!isFinite(di) || Math.abs(di) < 1e-9) { parado = true; break; }
      var xn = xi - fi / di; xs.push(xn);
      vt.push([[xi, 0], [xi, fi]]); tg.push([[xi, fi], [xn, 0]]);
    }
    tang.set(tg); vert.set(vt);
    dots.forEach(function (d, j) { d.visible = j < xs.length; if (j < xs.length) d.mover(xs[j], 0); });
    var u = xs[xs.length - 1], fm = function (t) { return (Math.round(t * 1e6) / 1e6).toString().replace('-', '−'); };
    lx(fm(u)); lf(fm(g.f(u))); le(Math.abs(u - g.raiz) > 1e4 ? '> 10⁴' : fm(Math.abs(u - g.raiz)));
    lm(parado ? 'f′(xₙ) = 0: la tangente es horizontal y no corta al eje' : '');
  }
  var sx = c.slider('x₀', F[0].x0[0], F[0].x0[1], 0.05, F[0].x0[2], function (v) { x0 = v; if (tang) calc(); });
  c.slider('Pasos n', 1, 9, 1, 3, function (v) { n = v; if (tang) calc(); }, function (v) { return String(v); });
  c.selector('Función ', F.map(function (g) { return g.n; }), 0, function (i) {
    k = i; nuevo(); sx.min = F[i].x0[0]; sx.max = F[i].x0[1]; sx.value = F[i].x0[2]; sx.dispatchEvent(new Event('input'));
  });
  c.alCambiarTema(function (p) {
    P = p; c.renderer.setClearColor(p.bg);
    if (!ejes) return;
    ejes.userData.eje.color.set(p.fg); ejes.userData.rejilla.color.set(p.bd); curva.material.color.set(p.fg);
    vert.material.color.set(p.mut); tang.material.color.set(p.S); raizPt.material.color.set(p.fg);
    dots.forEach(function (d) { d.material.color.set(p.acc); });
  });
});
