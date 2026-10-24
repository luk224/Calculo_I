/* Gradiente y derivada direccional (tema 4.3): D_v f = ∇f · v, máxima en la dirección del gradiente,
   y gradiente perpendicular a la curva de nivel. */
Interactivos.registrar('gradiente', function (c) {
  var T = c.THREE, H = c.H;
  var F = [
    { n: 'x² + y²', f: function (x, y) { return x * x + y * y; }, g: function (x, y) { return [2 * x, 2 * y]; }, d: 2, z: [0, 8] },
    { n: 'x² − y² (silla)', f: function (x, y) { return x * x - y * y; }, g: function (x, y) { return [2 * x, -2 * y]; }, d: 2, z: [-4, 4] },
    { n: '4·e^−(x²+y²) (campana)', f: function (x, y) { return 4 * Math.exp(-(x * x + y * y)); }, g: function (x, y) { var e = Math.exp(-(x * x + y * y)); return [-8 * x * e, -8 * y * e]; }, d: 2, z: [0, 4] },
    { n: 'x²y + y³ (Ej. 4.29 de U)', f: function (x, y) { return x * x * y + y * y * y; }, g: function (x, y) { return [2 * x * y, x * x + 3 * y * y]; }, d: 1.2, z: [-4, 4] }
  ];
  var k = 0, a = 1, b = 0.5, th = 45, P = c.colores();
  var malla, rejilla, nivelL, plano, curva, tang, pt, flG, flV;
  var l1 = c.lectura('∇f(a, b)'), l2 = c.lectura('‖∇f‖'), l3 = c.lectura('D_v f(a, b) = ∇f · v'), l4 = c.lectura('Ángulo del gradiente');
  function fm(t) { return (Math.round(t * 1000) / 1000).toString().replace('-', '−'); }
  function limpia(o) { if (o) { c.scene.remove(o); if (o.geometry) o.geometry.dispose(); } }
  function colorear() {
    if (!malla) return;
    var g = F[k], pos = malla.geometry.attributes.position, col = [], u1 = new T.Color(P.acc), u2 = new T.Color(P.bd), t = new T.Color(), i, u;
    for (i = 0; i < pos.count; i++) { u = (pos.getZ(i) - g.z[0]) / (g.z[1] - g.z[0]); t.copy(u1).lerp(u2, Math.max(0, Math.min(1, u))); col.push(t.r, t.g, t.b); }
    malla.geometry.setAttribute('color', new T.Float32BufferAttribute(col, 3));
  }
  function nuevo() {
    [malla, rejilla, nivelL, plano, curva, tang, pt, flG, flV].forEach(limpia);
    var g = F[k], d = g.d, zm = (g.z[0] + g.z[1]) / 2, r = 0.035 * d / 2;
    malla = H.superficie(T, g.f, { n: 70, xr: [-d, d], yr: [-d, d], zmax: 20, opacity: 0.75 });
    malla.material.vertexColors = true; malla.material.color.set(0xffffff); colorear(); c.scene.add(malla);
    rejilla = new T.GridHelper(2 * d, 8, P.mut, P.bd); rejilla.rotation.x = Math.PI / 2; rejilla.position.z = g.z[0]; c.scene.add(rejilla);
    var geo = new T.PlaneGeometry(2 * d * 1.5, g.z[1] - g.z[0]); geo.rotateX(Math.PI / 2);
    plano = new T.Mesh(geo, new T.MeshBasicMaterial({ color: P.acc, transparent: true, opacity: 0.12, side: T.DoubleSide, depthWrite: false }));
    plano.rotation.order = 'ZXY'; plano.position.z = zm; c.scene.add(plano);
    curva = H.tubo(T, [], r, P.acc); tang = H.tubo(T, [], r * 1.2, P.acc); c.scene.add(curva, tang);
    pt = new T.Mesh(new T.SphereGeometry(r * 2.4, 16, 12), new T.MeshBasicMaterial({ color: P.fg })); c.scene.add(pt);
    flG = H.flecha(T, P.S, r * 2.2); flV = H.flecha(T, P.acc, r * 2.2); c.scene.add(flG, flV);
    c.camera.position.set(d * 4.2, -d * 5, zm + (g.z[1] - g.z[0]) * 1 + d * 1.5); c.controls.target.set(0, 0, zm); c.controls.update();
  }
  function calc() {
    var g = F[k], d = g.d, rad = th * Math.PI / 180, vx = Math.cos(rad), vy = Math.sin(rad), fa = g.f(a, b), gr = g.g(a, b), ng = Math.hypot(gr[0], gr[1]);
    var dv = gr[0] * vx + gr[1] * vy, z0 = g.z[0], L = d * 0.6, i, n = 80, pts = [];
    pt.position.set(a, b, fa);
    plano.rotation.z = rad; plano.position.x = a; plano.position.y = b;
    for (i = 0; i <= n; i++) { var t = -d * 1.5 + 3 * d * i / n, x = a + t * vx, y = b + t * vy; if (Math.abs(x) <= d && Math.abs(y) <= d) pts.push([x, y, g.f(x, y) + 0.01]); }
    curva.set(pts);
    var Lt = d * 0.5, nn = Math.sqrt(1 + dv * dv);
    tang.set([[a - Lt * vx / nn, b - Lt * vy / nn, fa - Lt * dv / nn], [a + Lt * vx / nn, b + Lt * vy / nn, fa + Lt * dv / nn]]);
    flV.poner([a, b, z0], [a + L * vx, b + L * vy, z0]);
    if (ng > 1e-9) flG.poner([a, b, z0], [a + L * gr[0] / ng, b + L * gr[1] / ng, z0]); else flG.visible = false;
    limpia(nivelL); var seg = H.nivel(g.f, fa, d, 160), pp = []; seg.forEach(function (s) { pp.push(s[0], s[1], z0, s[2], s[3], z0); });
    var geo = new T.BufferGeometry(); geo.setAttribute('position', new T.Float32BufferAttribute(pp, 3)); nivelL = new T.LineSegments(geo, new T.LineBasicMaterial({ color: P.L })); c.scene.add(nivelL);
    l1('(' + fm(gr[0]) + ', ' + fm(gr[1]) + ')'); l2(fm(ng)); l3(fm(dv));
    var ang = Math.atan2(gr[1], gr[0]) * 180 / Math.PI; if (ang < 0) ang += 360;
    l4(ng > 1e-9 ? fm(ang) + '°  (en esa dirección D_v f vale ' + fm(ng) + ', el máximo)' : 'gradiente nulo: punto crítico');
  }
  var sa = c.slider('a', -2, 2, 0.05, a, function (v) { a = v; if (pt) calc(); });
  var sb = c.slider('b', -2, 2, 0.05, b, function (v) { b = v; if (pt) calc(); });
  c.slider('Dirección v (ángulo)', 0, 360, 1, th, function (v) { th = v; if (pt) calc(); }, function (v) { return v + '°'; });
  c.selector('Función ', F.map(function (g) { return g.n; }), 0, function (i) {
    k = i; var m = F[i].d - 0.1; sa.min = sb.min = -m; sa.max = sb.max = m; nuevo(); sa.value = Math.min(1, m); sb.value = Math.min(0.5, m);
    sa.dispatchEvent(new Event('input')); sb.dispatchEvent(new Event('input'));
  });
  c.leyenda([['var(--acc)','dirección v: corte de la superficie y su tangente','linea'],['var(--S)','gradiente ∇f','linea'],['var(--L)','curva de nivel por el punto','linea'],['var(--fg)','punto (a, b)','punto']]);
  c.alCambiarTema(function (q) {
    P = q; c.renderer.setClearColor(q.bg); colorear();
    if (!pt) return;
    var g = F[k]; limpia(rejilla); rejilla = new T.GridHelper(2 * g.d, 8, q.mut, q.bd); rejilla.rotation.x = Math.PI / 2; rejilla.position.z = g.z[0]; c.scene.add(rejilla);
    plano.material.color.set(q.acc); curva.material.color.set(q.acc); tang.material.color.set(q.acc); pt.material.color.set(q.fg);
    [[flG, q.S], [flV, q.acc]].forEach(function (e) { e[0].userData.eje.material.color.set(e[1]); e[0].userData.cono.material.color.set(e[1]); });
    if (nivelL) nivelL.material.color.set(q.L);
  });
});
