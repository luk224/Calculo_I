/* Polinomio de Taylor de grado n centrado en a frente a f (tema 3.1). Muestra el resto en un punto x. */
Interactivos.registrar('taylor', function (c) {
  var T = c.THREE, H = c.H;
  var W = function (v) { var dx = 1.5 * (v[1] - v[0]), dy = 1.5 * (v[3] - v[2]); return [v[0] - dx, v[1] + dx, v[2] - dy, v[3] + dy]; };
  // der(a, j) = f^(j)(a)
  var F = [
    { n: 'eˣ', f: Math.exp, der: function (a) { return Math.exp(a); }, v: [-3, 3, -3, 8], rA: [-2, 2, 0], rX: [-3, 3, 2] },
    { n: 'sen x', f: Math.sin, der: function (a, j) { return Math.sin(a + j * Math.PI / 2); }, v: [-6, 6, -3, 3], rA: [-3, 3, 0], rX: [-6, 6, 3] },
    { n: 'cos x', f: Math.cos, der: function (a, j) { return Math.cos(a + j * Math.PI / 2); }, v: [-6, 6, -3, 3], rA: [-3, 3, 0], rX: [-6, 6, 3] },
    { n: 'ln(1 + x)', f: function (x) { return Math.log(1 + x); },
      der: function (a, j) { if (j === 0) return Math.log(1 + a); var f = 1; for (var i = 2; i < j; i++) f *= i; return (j % 2 ? 1 : -1) * f / Math.pow(1 + a, j); },
      v: [-1.5, 4.5, -3, 3], rA: [-0.8, 3, 0], rX: [-0.95, 4, 1] }
  ];
  var k = 0, n = 3, a = 0, x = 2, P = c.colores(), w, vw, ejes, curva, pol, seg, pa, px, pxf;
  var lf = c.lectura('f(x)'), lp = c.lectura('pₙ(x)'), lr = c.lectura('|Rₙ(x)| = |f(x) − pₙ(x)|');
  var fm = function (t) { return (Math.round(t * 1e5) / 1e5).toString().replace('-', '−'); };
  function p(t) {
    var s = 0, term = 1, j;
    for (j = 0; j <= n; j++) { s += F[k].der(a, j) * term; term *= (t - a) / (j + 1); }
    return s;
  }
  function nuevo() {
    [ejes, curva, pol, seg, pa, px, pxf].forEach(function (o) { if (o) c.scene.remove(o); });
    var v = F[k].v; w = 0.0055 * (v[3] - v[2]); c.vista(v[0], v[1], v[2], v[3]); vw = W(v);
    ejes = H.ejes2D(T, vw, w, P.fg, P.bd); c.scene.add(ejes);
    curva = H.cinta(T, H.grafica(F[k].f, vw[0], vw[1], 1600, 1e3), P.fg, w * 1.4); curva.position.z = 0.1; c.scene.add(curva);
    pol = H.cinta(T, [], P.S, w * 1.4); pol.position.z = 0.2; c.scene.add(pol);
    seg = H.cinta(T, [], P.L, w * 1.6); seg.position.z = 0.3; c.scene.add(seg);
    pa = H.punto(T, 0, 0, w * 2.6, P.acc); px = H.punto(T, 0, 0, w * 2.2, P.fg); pxf = H.punto(T, 0, 0, w * 2.2, P.S);
    [pa, px, pxf].forEach(function (o) { o.position.z = 0.5; c.scene.add(o); });
  }
  function calc() {
    var g = F[k], dom = (g.n === 'ln(1 + x)');
    pol.set(H.grafica(p, vw[0], vw[1], 1600, 1e3));
    var fx = g.f(x), pxv = p(x);
    pa.mover(a, g.f(a)); px.mover(x, fx); pxf.mover(x, pxv);
    seg.set(Math.abs(fx - pxv) < 1e3 ? [[[x, fx], [x, pxv]]] : []);
    lf(fm(fx)); lp(fm(pxv)); lr(fm(Math.abs(fx - pxv)));
  }
  var sa = c.slider('Centro a', -2, 2, 0.05, 0, function (v) { a = v; if (pol) calc(); });
  var sx = c.slider('Punto x', -3, 3, 0.05, 2, function (v) { x = v; if (pol) calc(); });
  c.slider('Grado n', 0, 12, 1, 3, function (v) { n = v; if (pol) calc(); }, function (v) { return String(v); });
  function rango(s, r) { s.min = r[0]; s.max = r[1]; s.value = r[2]; s.dispatchEvent(new Event('input')); }
  c.selector('Función ', F.map(function (g) { return g.n; }), 0, function (i) { k = i; nuevo(); rango(sa, F[i].rA); rango(sx, F[i].rX); });
  c.alCambiarTema(function (q) {
    P = q; c.renderer.setClearColor(q.bg);
    if (!ejes) return;
    ejes.userData.eje.color.set(q.fg); ejes.userData.rejilla.color.set(q.bd); curva.material.color.set(q.fg);
    pol.material.color.set(q.S); seg.material.color.set(q.L); pa.material.color.set(q.acc); px.material.color.set(q.fg); pxf.material.color.set(q.S);
  });
});
