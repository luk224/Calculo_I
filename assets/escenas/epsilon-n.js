/* Tubo ε-N (tema 1.2): la banda (L−ε, L+ε) y el primer N desde el que todos los términos caen dentro. */
Interactivos.registrar('epsilon-n', function (c) {
  var T = c.THREE, H = c.H, MAXN = 200, NCALC = 3000;
  var S = [
    { n: 'aₙ = 1/n  (L = 0)', a: function (n) { return 1 / n; }, L: 0, y: [-0.25, 1.1] },
    { n: 'aₙ = n/(n+1)  (L = 1)', a: function (n) { return n / (n + 1); }, L: 1, y: [0, 1.15] },
    { n: 'aₙ = (−1)ⁿ/n  (L = 0)', a: function (n) { return (n % 2 ? -1 : 1) / n; }, L: 0, y: [-1.15, 1.15] },
    { n: 'aₙ = ⁿ√n  (L = 1)', a: function (n) { return Math.pow(n, 1 / n); }, L: 1, y: [0.85, 1.5] },
    { n: 'aₙ = (1 + 1/n)ⁿ  (L = e)', a: function (n) { return Math.pow(1 + 1 / n, n); }, L: Math.E, y: [1.5, 3] }
  ];
  var k = 0, u = 1, M = 60, P = c.colores(), w, sx, ejes, banda, lineaL, lineaN, dots = [];
  var l1 = c.lectura('ε'), l2 = c.lectura('N: |aₙ − L| < ε para todo n ≥ N'), lv = c.lectura('');
  function fm(t) { return (Math.round(t * 10000) / 10000).toString().replace('-', '−'); }
  function nuevo() {
    [ejes, banda, lineaL, lineaN].forEach(function (o) { if (o) c.scene.remove(o); });
    dots.forEach(function (d) { c.scene.remove(d); }); dots = [];
    var g = S[k], yr = g.y[1] - g.y[0], X = yr * 1.8; sx = X / (M + 1); w = 0.0055 * yr;
    c.vista(0, X, g.y[0], g.y[1]);
    ejes = H.cinta(T, [[[0, g.y[0]], [0, g.y[1]]], [[0, Math.max(g.y[0], Math.min(0, g.y[1]))], [X, Math.max(g.y[0], Math.min(0, g.y[1]))]]], P.fg, w); ejes.position.z = 0.05; c.scene.add(ejes);
    banda = new T.Mesh(new T.PlaneGeometry(1, 1), new T.MeshBasicMaterial({ color: P.L, transparent: true, opacity: 0.18, depthWrite: false })); banda.position.z = 0.02; c.scene.add(banda);
    lineaL = H.cinta(T, [[[0, g.L], [X, g.L]]], P.L, w, [w * 5, w * 3]); lineaL.position.z = 0.1; c.scene.add(lineaL);
    lineaN = H.cinta(T, [], P.mut, w, [w * 4, w * 3]); lineaN.position.z = 0.1; c.scene.add(lineaN);
    for (var n = 1; n <= MAXN; n++) { var d = H.punto(T, n * sx, g.a(n), w * 2.2, P.S); d.position.z = 0.5; d.visible = n <= M; dots.push(d); c.scene.add(d); }
  }
  function calc() {
    var g = S[k], eps = Math.pow(10, -u), n, N = 1, X = (g.y[1] - g.y[0]) * 1.8;
    banda.scale.set(X, 2 * eps, 1); banda.position.set(X / 2, g.L, 0.02);
    for (n = 1; n <= NCALC; n++) if (Math.abs(g.a(n) - g.L) >= eps) N = n + 1;
    dots.forEach(function (d, i) { var nn = i + 1; d.visible = nn <= M; if (d.visible) d.material.color.set(Math.abs(g.a(nn) - g.L) < eps ? P.L : P.S); });
    lineaN.set(N <= M ? [[[N * sx, g.y[0]], [N * sx, g.y[1]]]] : []);
    l1(fm(eps));
    l2(N > NCALC ? 'mayor que ' + NCALC : String(N));
    lv(N <= M ? 'Los puntos verdes están dentro de la banda; la línea vertical marca n = N.' : 'N cae fuera de los ' + M + ' términos dibujados: sube «Términos mostrados».');
  }
  c.slider('ε (de 1 a 0,01)', 0, 2, 0.01, u, function (v) { u = v; if (banda) calc(); }, function (v) { return fm(Math.pow(10, -v)); });
  c.slider('Términos mostrados', 10, MAXN, 1, M, function (v) { M = v; if (banda) { nuevo(); calc(); } }, function (v) { return String(v); });
  c.selector('Sucesión ', S.map(function (g) { return g.n; }), 1, function (i) { k = i; nuevo(); calc(); });
  c.alCambiarTema(function (q) {
    P = q; c.renderer.setClearColor(q.bg);
    if (!banda) return;
    ejes.material.color.set(q.fg); banda.material.color.set(q.L); lineaL.material.color.set(q.L); lineaN.material.color.set(q.mut); calc();
  });
});
