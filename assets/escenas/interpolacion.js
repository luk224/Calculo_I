/* Interpolación polinómica (tema 3.3): polinomio por n nodos (diferencias divididas de Newton).
   Modo libre: nodos arrastrables. Modos de Runge/seno: error máximo con nodos equiespaciados o de Chebyshev. */
Interactivos.registrar('interpolacion', function (c) {
  var T = c.THREE, H = c.H;
  var W = function (v) { var dx = 1.5 * (v[1] - v[0]), dy = 1.5 * (v[3] - v[2]); return [v[0] - dx, v[1] + dx, v[2] - dy, v[3] + dy]; };
  var runge = function (x) { return 1 / (1 + 25 * x * x); };
  var M = [
    { n: 'Nodos libres (arrastra los puntos)', libre: true, v: [-3, 3, -3, 3] },
    { n: 'Runge 1/(1+25x²), nodos equiespaciados', f: runge, a: -1, b: 1, v: [-1.2, 1.2, -0.7, 1.5] },
    { n: 'Runge 1/(1+25x²), nodos de Chebyshev', f: runge, a: -1, b: 1, cheb: true, v: [-1.2, 1.2, -0.7, 1.5] },
    { n: 'sen x en [−π, π], nodos equiespaciados', f: Math.sin, a: -Math.PI, b: Math.PI, v: [-4, 4, -2.2, 2.2] }
  ];
  var k = 0, N = 6, P = c.colores(), w, vw, xs = [], ys = [], dd = [];
  var ejes, curva, pol, dots = [];
  var ln = c.lectura('Nodos'), lg = c.lectura('Grado de pₙ'), le = c.lectura('');
  var fm = function (t) { return (Math.round(t * 1e4) / 1e4).toString().replace('-', '−'); };

  function nodos() {
    var m = M[k], i; xs = []; ys = [];
    for (i = 0; i < N; i++) {
      if (m.libre) xs.push(-2.4 + 4.8 * i / (N - 1));
      else xs.push(m.cheb ? (m.a + m.b) / 2 + (m.b - m.a) / 2 * Math.cos((2 * i + 1) * Math.PI / (2 * N)) : m.a + (m.b - m.a) * i / (N - 1));
      ys.push(m.libre ? 0.3 + 1.2 * Math.cos(1.7 * xs[i]) * Math.exp(-0.1 * xs[i] * xs[i]) : m.f(xs[i]));
    }
  }
  function diferencias() {
    var n = xs.length, i, j; dd = ys.slice();
    for (j = 1; j < n; j++) for (i = n - 1; i >= j; i--) dd[i] = (dd[i] - dd[i - 1]) / (xs[i] - xs[i - j]);
  }
  function p(t) { var s = dd[xs.length - 1], i; for (i = xs.length - 2; i >= 0; i--) s = s * (t - xs[i]) + dd[i]; return s; }

  function nuevo() {
    [ejes, curva, pol].forEach(function (o) { if (o) c.scene.remove(o); });
    dots.forEach(function (o) { c.scene.remove(o); }); dots = [];
    var m = M[k], v = m.v; w = 0.0055 * (v[3] - v[2]); c.vista(v[0], v[1], v[2], v[3]); vw = W(v);
    ejes = H.ejes2D(T, vw, w, P.fg, P.bd); c.scene.add(ejes);
    curva = H.cinta(T, m.f ? H.grafica(m.f, vw[0], vw[1], 1600, 1e3) : [], P.mut, w * 1.2, [w * 5, w * 3]); curva.position.z = 0.1; c.scene.add(curva);
    pol = H.cinta(T, [], P.S, w * 1.4); pol.position.z = 0.2; c.scene.add(pol);
    for (var i = 0; i < 21; i++) { var d = H.punto(T, 0, 0, w * 3, P.acc); d.position.z = 0.5; d.visible = false; dots.push(d); c.scene.add(d); }
  }
  function calc() {
    var m = M[k], i; diferencias();
    pol.set(H.grafica(p, vw[0], vw[1], 1600, 1e3));
    dots.forEach(function (d, j) { d.visible = j < xs.length; if (j < xs.length) d.mover(xs[j], ys[j]); });
    ln(String(xs.length)); lg('≤ ' + (xs.length - 1));
    if (m.f) {
      var e = 0, t; for (i = 0; i <= 600; i++) { t = m.a + (m.b - m.a) * i / 600; e = Math.max(e, Math.abs(m.f(t) - p(t))); }
      le('Error máximo |f − pₙ| en [' + fm(m.a) + ', ' + fm(m.b) + '] = ' + (e > 1e4 ? '> 10⁴' : fm(e)));
    } else le('');
  }
  // arrastrar nodos (modo libre): la x se mantiene distinta de la de los demás nodos
  c.arrastre = {
    coger: function (wx, wy, r) {
      if (!M[k].libre) return -1;
      var best = -1, bd = r * r, i; for (i = 0; i < xs.length; i++) { var d = (xs[i] - wx) * (xs[i] - wx) + (ys[i] - wy) * (ys[i] - wy); if (d < bd) { bd = d; best = i; } }
      return best;
    },
    mover: function (i, wx, wy) {
      var v = M[k].v, lo = v[0] + 0.1, hi = v[1] - 0.1; wx = Math.max(lo, Math.min(hi, wx));
      for (var j = 0; j < xs.length; j++) if (j !== i && Math.abs(xs[j] - wx) < 0.08) return;
      xs[i] = wx; ys[i] = Math.max(v[2] + 0.1, Math.min(v[3] - 0.1, wy)); calc();
    }
  };
  c.slider('Número de nodos', 3, 21, 1, N, function (v) { N = v; if (pol) { nodos(); calc(); } }, function (v) { return String(v); });
  c.selector('Caso ', M.map(function (m) { return m.n; }), 0, function (i) { k = i; nuevo(); nodos(); calc(); });
  c.alCambiarTema(function (q) {
    P = q; c.renderer.setClearColor(q.bg);
    if (!ejes) return;
    ejes.userData.eje.color.set(q.fg); ejes.userData.rejilla.color.set(q.bd); curva.material.color.set(q.mut); pol.material.color.set(q.S);
    dots.forEach(function (d) { d.material.color.set(q.acc); });
  });
});
