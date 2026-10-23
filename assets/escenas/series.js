/* Series y sumas parciales (tema 1.3): términos aₙ (barras) y sumas parciales Sₙ (curva) frente a la suma. */
Interactivos.registrar('series', function (c) {
  var T = c.THREE, H = c.H, MAXN = 200;
  var S = [
    { n: 'Σ 1/2ⁿ  (geométrica, r = 1/2)', a: function (n) { return Math.pow(0.5, n); }, suma: 1, y: [0, 1.15], txt: 'converge a 1' },
    { n: 'Σ 1/(n(n+1))  (telescópica)', a: function (n) { return 1 / (n * (n + 1)); }, suma: 1, y: [0, 1.15], txt: 'converge a 1 (Sₙ = 1 − 1/(n+1))' },
    { n: 'Σ 1/n²  (serie p = 2)', a: function (n) { return 1 / (n * n); }, suma: Math.PI * Math.PI / 6, y: [0, 1.9], txt: 'converge a π²/6 ≈ 1,6449' },
    { n: 'Σ (−1)ⁿ⁺¹/n  (armónica alternada)', a: function (n) { return (n % 2 ? 1 : -1) / n; }, suma: Math.LN2, y: [0, 1.15], txt: 'converge a ln 2 ≈ 0,6931 (Leibniz)' },
    { n: 'Σ 1/n  (armónica)', a: function (n) { return 1 / n; }, suma: null, y: [0, 6.3], txt: 'DIVERGE aunque aₙ → 0 (Sₙ ≈ ln n + 0,577)' },
    { n: 'Σ 1/√n  (serie p = 1/2)', a: function (n) { return 1 / Math.sqrt(n); }, suma: null, y: [0, 30], txt: 'DIVERGE (p ≤ 1)' }
  ];
  var k = 0, M = 20, P = c.colores(), w, sx, X, ejes, lim, bars, curva, pt, sn = [];
  var l1 = c.lectura('aₙ  (último término)'), l2 = c.lectura('Sₙ  (suma parcial)'), l3 = c.lectura('La serie'), lv = c.lectura('');
  function fm(t) { return (Math.round(t * 10000) / 10000).toString().replace('-', '−'); }
  function nuevo() {
    [ejes, lim, bars, curva, pt].forEach(function (o) { if (o) c.scene.remove(o); });
    var g = S[k], yr = g.y[1] - g.y[0]; X = yr * 1.8; sx = X / (M + 1); w = 0.0055 * yr;
    c.vista(0, X, g.y[0] - 0.02 * yr, g.y[1]);
    ejes = H.cinta(T, [[[0, g.y[0]], [0, g.y[1]]], [[0, 0], [X, 0]]], P.fg, w); ejes.position.z = 0.05; c.scene.add(ejes);
    lim = H.cinta(T, g.suma === null ? [] : [[[0, g.suma], [X, g.suma]]], P.L, w, [w * 5, w * 3]); lim.position.z = 0.1; c.scene.add(lim);
    bars = H.cinta(T, [], P.mut, w * 1.6); bars.position.z = 0.15; c.scene.add(bars);
    curva = H.cinta(T, [], P.S, w * 1.4); curva.position.z = 0.3; c.scene.add(curva);
    pt = H.punto(T, 0, 0, w * 2.6, P.S); pt.position.z = 0.5; c.scene.add(pt);
    var s = 0, i; sn = []; for (i = 1; i <= MAXN; i++) { s += g.a(i); sn.push(s); }
  }
  function calc() {
    var g = S[k], i, pts = [], bs = [];
    for (i = 1; i <= M; i++) { pts.push([i * sx, sn[i - 1]]); bs.push([[i * sx, 0], [i * sx, g.a(i)]]); }
    curva.set([pts]); bars.set(bs); pt.mover(M * sx, sn[M - 1]);
    l1(fm(g.a(M))); l2(fm(sn[M - 1])); l3(g.txt);
    lv(g.suma === null ? 'Las sumas parciales crecen sin cota (la barra gris, aₙ, se hace pequeña pero Sₙ no se frena).' : 'La curva naranja (Sₙ) se acerca a la línea verde, que es la suma de la serie.');
  }
  c.slider('Términos n', 1, MAXN, 1, M, function (v) { M = v; if (bars) { nuevo(); calc(); } }, function (v) { return String(v); });
  c.selector('Serie ', S.map(function (g) { return g.n; }), 0, function (i) { k = i; nuevo(); calc(); });
  c.alCambiarTema(function (q) {
    P = q; c.renderer.setClearColor(q.bg);
    if (!bars) return;
    ejes.material.color.set(q.fg); lim.material.color.set(q.L); bars.material.color.set(q.mut); curva.material.color.set(q.S); pt.material.color.set(q.S);
  });
});
