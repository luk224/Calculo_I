/* Puntos críticos de z = f(x,y): plano tangente horizontal y clasificación con la Hessiana (tema 5.4). */
Interactivos.registrar('extremos', function (c) {
  var T = c.THREE, H = c.H, e = Math.E;
  var F = [
    { n: '(x² + 2y²)·e^(1−x²−y²) (Ej. 5.17 y 5.20 de U)', f: function (x, y) { return (x * x + 2 * y * y) * Math.exp(1 - x * x - y * y); }, d: 2, z: [0, 2],
      p: [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]] },
    { n: '3x² − y² (Ej. 5.19 de U, silla)', f: function (x, y) { return 3 * x * x - y * y; }, d: 2, z: [-4, 12], p: [[0, 0]] },
    { n: 'x³ + y² − xy (Ej. 5.31 de E)', f: function (x, y) { return x * x * x + y * y - x * y; }, d: 1.2, z: [-1.5, 2.5], p: [[0, 0], [1 / 6, 1 / 12]] },
    { n: 'x⁴ + y⁴ − 4xy (propio)', f: function (x, y) { return Math.pow(x, 4) + Math.pow(y, 4) - 4 * x * y; }, d: 1.6, z: [-2, 10], p: [[0, 0], [1, 1], [-1, -1]] }
  ];
  var k = 0, j0 = Math.max(1, parseInt(c.params.punto, 10) || 1), primera = true, j = j0, P = c.colores(), malla = null, rejilla = null, plano = null, pt = null;
  var l0 = c.lectura('Punto crítico (a, b)'), l1 = c.lectura('f(a, b)'), l2 = c.lectura('Hessiana (r, s; s, u)'), l3 = c.lectura('d = r·u − s²'), l4 = c.lectura('Clasificación');
  function fm(t) { return (Math.round(t * 100) / 100).toString().replace('-', '−'); }
  function etq(p) { return '(' + fm(p[0]) + ', ' + fm(p[1]) + ')'; }
  function limpia(o) { if (o) { c.scene.remove(o); if (o.geometry) o.geometry.dispose(); } }
  function colorear() {
    if (!malla) return;
    var g = F[k], pos = malla.geometry.attributes.position, col = [], a = new T.Color(P.acc), b = new T.Color(P.S), t = new T.Color(), i, u;
    for (i = 0; i < pos.count; i++) { u = (pos.getZ(i) - g.z[0]) / (g.z[1] - g.z[0]); t.copy(a).lerp(b, Math.max(0, Math.min(1, u))); col.push(t.r, t.g, t.b); }
    malla.geometry.setAttribute('color', new T.Float32BufferAttribute(col, 3));
  }
  function nuevo() {
    [malla, rejilla, plano, pt].forEach(limpia);
    var g = F[k], d = g.d, zm = (g.z[0] + g.z[1]) / 2, r = 0.03 * d;
    malla = H.superficie(T, g.f, { n: 70, xr: [-d, d], yr: [-d, d], zmax: 30, opacity: 0.8 });
    malla.material.vertexColors = true; malla.material.color.set(0xffffff); colorear(); c.scene.add(malla);
    rejilla = new T.GridHelper(2 * d, 8, P.mut, P.bd); rejilla.rotation.x = Math.PI / 2; rejilla.position.z = g.z[0]; c.scene.add(rejilla);
    plano = new T.Mesh(new T.PlaneGeometry(0.9 * d, 0.9 * d), new T.MeshBasicMaterial({ color: P.fg, transparent: true, opacity: 0.35, side: T.DoubleSide, depthWrite: false }));
    c.scene.add(plano);
    pt = new T.Mesh(new T.SphereGeometry(r, 16, 12), new T.MeshBasicMaterial({ color: P.L })); c.scene.add(pt);
    c.camera.position.set(d * 2.1, -d * 2.5, zm + (g.z[1] - g.z[0]) * 0.55 + d * 0.9); c.controls.target.set(0, 0, zm); c.controls.update();
  }
  function calc() {
    var g = F[k], p = g.p[Math.min(j, g.p.length) - 1], a = p[0], b = p[1], h = 1e-3, f = g.f;
    var fa = f(a, b), r = (f(a + h, b) - 2 * fa + f(a - h, b)) / (h * h), u = (f(a, b + h) - 2 * fa + f(a, b - h)) / (h * h);
    var s = (f(a + h, b + h) - f(a + h, b - h) - f(a - h, b + h) + f(a - h, b - h)) / (4 * h * h), dd = r * u - s * s, txt;
    plano.position.set(a, b, fa); pt.position.set(a, b, fa);
    if (Math.abs(dd) < 1e-4) txt = 'd = 0: caso dudoso (el criterio no decide)';
    else if (dd < 0) txt = 'd < 0: punto de silla';
    else if (Math.abs(r) < 1e-4) txt = 'd > 0 y r = 0: caso dudoso';
    else txt = r > 0 ? 'd > 0 y r > 0: mínimo relativo' : 'd > 0 y r < 0: máximo relativo';
    l0(etq(p)); l1(fm(fa)); l2('(' + fm(r) + ', ' + fm(s) + '; ' + fm(s) + ', ' + fm(u) + ')'); l3(fm(dd)); l4(txt);
  }
  var sl = c.slider('Punto crítico nº', 1, F[0].p.length, 1, j0, function (v) { j = v; if (pt) calc(); }, function (v) { return v + ' de ' + F[k].p.length; });
  c.selector('Función ', F.map(function (g) { return g.n; }), 0, function (i) {
    k = i; j = primera ? Math.min(j0, F[i].p.length) : 1; primera = false; nuevo(); sl.max = F[i].p.length; sl.value = j; sl.dispatchEvent(new Event('input'));
  });
  calc();
  c.leyenda([['var(--acc)','superficie: zona baja','area'],['var(--S)','superficie: zona alta','area'],['var(--fg)','plano tangente horizontal','area'],['var(--L)','punto crítico','punto']]);
  c.alCambiarTema(function (q) {
    P = q; c.renderer.setClearColor(q.bg); colorear();
    if (!pt) return;
    limpia(rejilla); var g = F[k]; rejilla = new T.GridHelper(2 * g.d, 8, q.mut, q.bd); rejilla.rotation.x = Math.PI / 2; rejilla.position.z = g.z[0]; c.scene.add(rejilla);
    plano.material.color.set(q.fg); pt.material.color.set(q.L);
  });
});
