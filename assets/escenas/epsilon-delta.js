/* Definición ε-δ de límite de una función (tema 1.4): para cada ε hay que encontrar δ. */
Interactivos.registrar('epsilon-delta', function (c) {
  var T = c.THREE, H = c.H;
  var W = function (v) { var dx = 1.5 * (v[1] - v[0]), dy = 1.5 * (v[3] - v[2]); return [v[0] - dx, v[1] + dx, v[2] - dy, v[3] + dy]; };
  var F = [
    { n: 'x² cuando x → 1  (L = 1)', f: function (x) { return x * x; }, a: 1, L: 1, v: [-1.5, 3.5, -1, 5] },
    { n: '2x + 1 cuando x → 1  (L = 3)', f: function (x) { return 2 * x + 1; }, a: 1, L: 3, v: [-1.5, 3.5, 0, 6] },
    { n: '(x² − 1)/(x − 1) cuando x → 1  (L = 2; agujero en x = 1)', f: function (x) { return (x * x - 1) / (x - 1); }, a: 1, L: 2, v: [-1.5, 3.5, -0.5, 5.5] },
    { n: 'sen x / x cuando x → 0  (L = 1)', f: function (x) { return Math.sin(x) / x; }, a: 0, L: 1, v: [-5, 5, -0.7, 1.5] },
    { n: 'x/|x| cuando x → 0  (NO tiene límite; candidato L = 1)', f: function (x) { return x / Math.abs(x); }, a: 0, L: 1, v: [-3, 3, -2, 2] }
  ];
  var k = 0, ue = 0.5, ud = 0.5, P = c.colores(), w, vw, ejes, curva, ok, mal, bh, bv, hueco;
  var l1 = c.lectura('ε'), l2 = c.lectura('δ'), l3 = c.lectura('δ máximo que sirve para este ε'), lv = c.lectura('');
  function fm(t) { return (Math.round(t * 1000) / 1000).toString().replace('-', '−'); }
  function limpia(o) { if (o) { c.scene.remove(o); if (o.geometry) o.geometry.dispose(); } }
  function nuevo() {
    [ejes, curva, ok, mal, bh, bv, hueco].forEach(limpia);
    var g = F[k], v = g.v; w = 0.0055 * (v[3] - v[2]); c.vista(v[0], v[1], v[2], v[3]); vw = W(v);
    bh = new T.Mesh(new T.PlaneGeometry(1, 1), new T.MeshBasicMaterial({ color: P.L, transparent: true, opacity: 0.18, depthWrite: false })); bh.position.z = 0.02;
    bv = new T.Mesh(new T.PlaneGeometry(1, 1), new T.MeshBasicMaterial({ color: P.acc, transparent: true, opacity: 0.15, depthWrite: false })); bv.position.z = 0.03;
    c.scene.add(bh, bv);
    ejes = H.ejes2D(T, vw, w, P.fg, P.bd); c.scene.add(ejes);
    var pols = [[], []], i, n = 1600, x, y;
    for (i = 0; i <= n; i++) { x = vw[0] + (vw[1] - vw[0]) * (i + 0.5) / (n + 1); y = g.f(x); if (isFinite(y) && Math.abs(y) < 1e3 && Math.abs(x - g.a) > 1e-9) (x < g.a ? pols[0] : pols[1]).push([x, y]); }
    curva = H.cinta(T, pols, P.mut, w * 1.2); curva.position.z = 0.1; c.scene.add(curva);
    ok = H.cinta(T, [], P.L, w * 2); ok.position.z = 0.3; mal = H.cinta(T, [], P.S, w * 2); mal.position.z = 0.35; c.scene.add(ok, mal);
    hueco = H.punto(T, g.a, g.L, w * 3, P.acc); hueco.position.z = 0.6; c.scene.add(hueco);
  }
  function sirve(g, eps, d) {
    var i, n = 400, x, y;
    for (i = 1; i <= n; i++) for (var s = -1; s <= 1; s += 2) { x = g.a + s * d * i / n; y = g.f(x); if (!(Math.abs(y - g.L) < eps)) return false; }
    return true;
  }
  function calc() {
    var g = F[k], eps = Math.pow(10, -ue), d = Math.pow(10, -ud) * 2, i, n = 600, x, y, a0 = [], a1 = [], cur = null, curOk = null;
    var X = vw[1] - vw[0], Y = vw[3] - vw[2];
    bh.scale.set(X, 2 * eps, 1); bh.position.set((vw[0] + vw[1]) / 2, g.L, 0.02);
    bv.scale.set(2 * d, Y, 1); bv.position.set(g.a, (vw[2] + vw[3]) / 2, 0.03);
    var okp = [], malp = [], prev = null;
    for (var s = -1; s <= 1; s += 2) {
      var pa = [], pm = [];
      for (i = 1; i <= n; i++) { x = g.a + s * d * i / n; y = g.f(x); if (!isFinite(y) || Math.abs(y) > 1e3) continue; var p = [x, y]; if (Math.abs(y - g.L) < eps) pa.push(p); else pm.push(p); }
      // dibujar como pequeños segmentos entre puntos consecutivos de cada clase
      var seg = function (pts) { var out = []; for (var j = 0; j + 1 < pts.length; j++) if (Math.abs(pts[j + 1][0] - pts[j][0]) < 3 * d / n) out.push([pts[j], pts[j + 1]]); return out; };
      okp = okp.concat(seg(pa)); malp = malp.concat(seg(pm));
    }
    ok.set(okp); mal.set(malp);
    // δ máximo (bisección sobre δ en (0, 5])
    var lo = 0, hi = 5, m; if (sirve(g, eps, hi)) lo = hi; else for (i = 0; i < 40; i++) { m = (lo + hi) / 2; if (sirve(g, eps, m)) lo = m; else hi = m; }
    l1(fm(eps)); l2(fm(d)); l3(lo < 1e-6 ? 'ninguno' : lo >= 5 ? 'cualquiera' : fm(lo));
    lv(sirve(g, eps, d) ? 'Este δ SIRVE: toda la gráfica sobre (a−δ, a+δ) (sin el punto a) queda en la banda verde.' : (lo < 1e-6 ? 'Ningún δ sirve para este ε: no hay límite L.' : 'Este δ NO sirve: el trozo naranja se sale de la banda. Reduce δ.'));
  }
  c.slider('ε (de 1 a 0,01)', 0, 2, 0.01, ue, function (v) { ue = v; if (bh) calc(); }, function (v) { return fm(Math.pow(10, -v)); });
  c.slider('δ (de 2 a 0,02)', 0, 2, 0.01, ud, function (v) { ud = v; if (bh) calc(); }, function (v) { return fm(Math.pow(10, -v) * 2); });
  c.selector('Función ', F.map(function (g) { return g.n; }), 0, function (i) { k = i; nuevo(); calc(); });
  c.alCambiarTema(function (q) {
    P = q; c.renderer.setClearColor(q.bg);
    if (!bh) return;
    bh.material.color.set(q.L); bv.material.color.set(q.acc); ejes.userData.eje.color.set(q.fg); ejes.userData.rejilla.color.set(q.bd);
    curva.material.color.set(q.mut); ok.material.color.set(q.L); mal.material.color.set(q.S); hueco.material.color.set(q.acc);
  });
});
