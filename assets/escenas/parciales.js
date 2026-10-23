/* Derivadas parciales como pendientes de los cortes y = b y x = a de la superficie (tema 4.3). */
Interactivos.registrar('parciales', function (c) {
  var T = c.THREE, H = c.H;
  var F = [
    { n: 'x² + y²', f: function (x, y) { return x * x + y * y; }, fx: function (x) { return 2 * x; }, fy: function (x, y) { return 2 * y; }, d: 2, z: [0, 8] },
    { n: 'x² − y² (silla)', f: function (x, y) { return x * x - y * y; }, fx: function (x) { return 2 * x; }, fy: function (x, y) { return -2 * y; }, d: 2, z: [-4, 4] },
    { n: '2·sen x·cos y', f: function (x, y) { return 2 * Math.sin(x) * Math.cos(y); }, fx: function (x, y) { return 2 * Math.cos(x) * Math.cos(y); }, fy: function (x, y) { return -2 * Math.sin(x) * Math.sin(y); }, d: 3, z: [-2, 2] },
    { n: '4·e^−(x²+y²) (campana)', f: function (x, y) { return 4 * Math.exp(-(x * x + y * y)); }, fx: function (x, y) { return -8 * x * Math.exp(-(x * x + y * y)); }, fy: function (x, y) { return -8 * y * Math.exp(-(x * x + y * y)); }, d: 2, z: [0, 4] }
  ];
  var k = 0, a = 1, b = 0.5, P = c.colores(), malla, rejilla, pY, pX, cx, cy, tx, ty, pt;
  var l0 = c.lectura('f(a, b)'), l1 = c.lectura('∂f/∂x (a, b) = pendiente del corte y = b'), l2 = c.lectura('∂f/∂y (a, b) = pendiente del corte x = a');
  function fm(t) { return (Math.round(t * 1000) / 1000).toString().replace('-', '−'); }
  function limpia(o) { if (o) { c.scene.remove(o); if (o.geometry) o.geometry.dispose(); } }
  function colorear() {
    if (!malla) return;
    var g = F[k], pos = malla.geometry.attributes.position, col = [], u1 = new T.Color(P.acc), u2 = new T.Color(P.bd), t = new T.Color(), i, u;
    for (i = 0; i < pos.count; i++) { u = (pos.getZ(i) - g.z[0]) / (g.z[1] - g.z[0]); t.copy(u1).lerp(u2, Math.max(0, Math.min(1, u))); col.push(t.r, t.g, t.b); }
    malla.geometry.setAttribute('color', new T.Float32BufferAttribute(col, 3));
  }
  function plano(x0, y0, col) {
    var g = F[k], geo = new T.PlaneGeometry(2 * g.d, g.z[1] - g.z[0]); geo.rotateX(Math.PI / 2); if (x0 !== null) geo.rotateZ(Math.PI / 2);
    var m = new T.Mesh(geo, new T.MeshBasicMaterial({ color: col, transparent: true, opacity: 0.12, side: T.DoubleSide, depthWrite: false }));
    m.position.set(x0 === null ? 0 : x0, y0 === null ? 0 : y0, (g.z[0] + g.z[1]) / 2); return m;
  }
  function nuevo() {
    [malla, rejilla, pY, pX, cx, cy, tx, ty, pt].forEach(limpia);
    var g = F[k], d = g.d, zm = (g.z[0] + g.z[1]) / 2, r = 0.035 * d / 2;
    malla = H.superficie(T, g.f, { n: 70, xr: [-d, d], yr: [-d, d], zmax: 20, opacity: 0.8 });
    malla.material.vertexColors = true; malla.material.color.set(0xffffff); colorear(); c.scene.add(malla);
    rejilla = new T.GridHelper(2 * d, 8, P.mut, P.bd); rejilla.rotation.x = Math.PI / 2; rejilla.position.z = g.z[0]; c.scene.add(rejilla);
    pY = plano(null, b, P.S); pX = plano(a, null, P.L); c.scene.add(pY, pX);
    cx = H.tubo(T, [], r, P.S); cy = H.tubo(T, [], r, P.L); tx = H.tubo(T, [], r * 1.2, P.S); ty = H.tubo(T, [], r * 1.2, P.L);
    pt = new T.Mesh(new T.SphereGeometry(r * 2.4, 16, 12), new T.MeshBasicMaterial({ color: P.fg })); c.scene.add(cx, cy, tx, ty, pt);
    c.camera.position.set(d * 3.4, -d * 4, zm + (g.z[1] - g.z[0]) * 0.8 + d * 1.2); c.controls.target.set(0, 0, zm); c.controls.update();
  }
  function calc() {
    var g = F[k], d = g.d, i, n = 60, A = [], B = [], fa = g.f(a, b), mx = g.fx(a, b), my = g.fy(a, b), L = d * 0.45;
    for (i = 0; i <= n; i++) { var t = -d + 2 * d * i / n; A.push([t, b, g.f(t, b) + 0.01]); B.push([a, t, g.f(a, t) + 0.01]); }
    cx.set(A); cy.set(B);
    var nx = Math.sqrt(1 + mx * mx), ny = Math.sqrt(1 + my * my);
    tx.set([[a - L / nx, b, fa - L * mx / nx], [a + L / nx, b, fa + L * mx / nx]]);
    ty.set([[a, b - L / ny, fa - L * my / ny], [a, b + L / ny, fa + L * my / ny]]);
    pt.position.set(a, b, fa); pY.position.y = b; pX.position.x = a;
    l0(fm(fa)); l1(fm(mx)); l2(fm(my));
  }
  var sa = c.slider('a', -2, 2, 0.05, a, function (v) { a = v; if (pt) calc(); });
  var sb = c.slider('b', -2, 2, 0.05, b, function (v) { b = v; if (pt) calc(); });
  c.selector('Función ', F.map(function (g) { return g.n; }), 0, function (i) {
    k = i; var m = F[i].d - 0.1; sa.min = sb.min = -m; sa.max = sb.max = m; nuevo(); sa.value = Math.min(1, m); sb.value = Math.min(0.5, m);
    sa.dispatchEvent(new Event('input')); sb.dispatchEvent(new Event('input'));
  });
  c.alCambiarTema(function (q) {
    P = q; c.renderer.setClearColor(q.bg); colorear();
    if (!pt) return;
    limpia(rejilla); var g = F[k]; rejilla = new T.GridHelper(2 * g.d, 8, q.mut, q.bd); rejilla.rotation.x = Math.PI / 2; rejilla.position.z = g.z[0]; c.scene.add(rejilla);
    pY.material.color.set(q.S); pX.material.color.set(q.L); cx.material.color.set(q.S); tx.material.color.set(q.S); cy.material.color.set(q.L); ty.material.color.set(q.L); pt.material.color.set(q.fg);
  });
});
