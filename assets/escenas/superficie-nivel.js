/* Gráfica z = f(x,y), plano z = c, traza sobre la superficie y curva de nivel proyectada (tema 4.2). */
Interactivos.registrar('superficie-nivel', function (c) {
  var T = c.THREE, H = c.H;
  var F = [
    { n: 'x² + y² + 1 (Ej. 4.11 de U)', f: function (x, y) { return x * x + y * y + 1; }, d: 1.8, z: [0, 8], c: [0, 8, 3],
      info: function (k) { return k < 1 - 1e-9 ? 'vacía (x² + y² = ' + fm(k - 1) + ' < 0)' : k < 1 + 1e-9 ? 'el punto (0, 0)' : 'circunferencia de radio √(c − 1) = ' + fm(Math.sqrt(k - 1)); } },
    { n: 'x² − y² (silla)', f: function (x, y) { return x * x - y * y; }, d: 2, z: [-4, 4], c: [-4, 4, 1],
      info: function (k) { return Math.abs(k) < 0.03 ? 'el par de rectas y = x, y = −x' : k > 0 ? 'hipérbola x² − y² = c (ramas a derecha e izquierda)' : 'hipérbola x² − y² = c (ramas arriba y abajo)'; } },
    { n: '4·e^−(x²+y²) (campana)', f: function (x, y) { return 4 * Math.exp(-(x * x + y * y)); }, d: 2, z: [0, 4], c: [0.05, 4, 2],
      info: function (k) { return k > 4 + 1e-9 ? 'vacía (c > 4 = máximo)' : k > 4 - 0.03 ? 'el punto (0, 0)' : 'circunferencia de radio √ln(4/c) = ' + fm(Math.sqrt(Math.log(4 / k))); } },
    { n: 'x² + 2y² (paraboloide elíptico)', f: function (x, y) { return x * x + 2 * y * y; }, d: 2, z: [0, 8], c: [0, 8, 3],
      info: function (k) { return k < -1e-9 ? 'vacía' : k < 0.03 ? 'el punto (0, 0)' : 'elipse de semiejes √c = ' + fm(Math.sqrt(k)) + ' y √(c/2) = ' + fm(Math.sqrt(k / 2)); } }
  ];
  var k = 0, lvl = 3, P = c.colores(), malla = null, rejilla = null, plano = null, traza = null, proy = null;
  var lc = c.lectura('Curva de nivel f(x, y) = c');
  function fm(t) { return (Math.round(t * 100) / 100).toString().replace('-', '−'); }

  function colorear() {
    if (!malla) return;
    var g = F[k], pos = malla.geometry.attributes.position, col = [], a = new T.Color(P.acc), b = new T.Color(P.S), t = new T.Color(), i, u;
    for (i = 0; i < pos.count; i++) { u = (pos.getZ(i) - g.z[0]) / (g.z[1] - g.z[0]); t.copy(a).lerp(b, Math.max(0, Math.min(1, u))); col.push(t.r, t.g, t.b); }
    malla.geometry.setAttribute('color', new T.Float32BufferAttribute(col, 3));
  }
  function limpia(o) { if (o) { c.scene.remove(o); if (o.geometry) o.geometry.dispose(); } }
  function nuevo() {
    [malla, rejilla, plano].forEach(limpia);
    var g = F[k], d = g.d, zm = (g.z[0] + g.z[1]) / 2;
    malla = H.superficie(T, g.f, { n: 70, xr: [-d, d], yr: [-d, d], zmax: 20, opacity: 0.9 });
    malla.material.vertexColors = true; malla.material.color.set(0xffffff); colorear(); c.scene.add(malla);
    rejilla = new T.GridHelper(2 * d, 8, P.mut, P.bd); rejilla.rotation.x = Math.PI / 2; rejilla.position.z = g.z[0]; c.scene.add(rejilla);
    plano = new T.Mesh(new T.PlaneGeometry(2 * d, 2 * d), new T.MeshBasicMaterial({ color: P.S, transparent: true, opacity: 0.18, side: T.DoubleSide, depthWrite: false }));
    c.scene.add(plano);
    c.camera.position.set(d * 3.4, -d * 4, zm + (g.z[1] - g.z[0]) * 0.8 + d * 1.2); c.controls.target.set(0, 0, zm); c.controls.update();
  }
  /* Curva de nivel f = k por «marching squares»: segmentos [x1,y1,x2,y2]. */
  function nivel(f, k, d, n) {
    var seg = [], i, j, h = 2 * d / n;
    for (j = 0; j < n; j++) for (i = 0; i < n; i++) {
      var x0 = -d + i * h, y0 = -d + j * h, x1 = x0 + h, y1 = y0 + h;
      var v = [f(x0, y0) - k, f(x1, y0) - k, f(x1, y1) - k, f(x0, y1) - k], px = [x0, x1, x1, x0], py = [y0, y0, y1, y1];
      var idx = (v[0] > 0 ? 1 : 0) | (v[1] > 0 ? 2 : 0) | (v[2] > 0 ? 4 : 0) | (v[3] > 0 ? 8 : 0);
      var T_ = [[], [[3, 0]], [[0, 1]], [[3, 1]], [[1, 2]], [[3, 0], [1, 2]], [[0, 2]], [[2, 3]], [[2, 3]], [[0, 2]], [[0, 1], [2, 3]], [[1, 2]], [[1, 3]], [[0, 1]], [[3, 0]], []][idx];
      var pt = function (e) { var a = e, b = (e + 1) % 4, t = v[a] / (v[a] - v[b]); return [px[a] + (px[b] - px[a]) * t, py[a] + (py[b] - py[a]) * t]; };
      T_.forEach(function (s) { var p = pt(s[0]), q = pt(s[1]); seg.push([p[0], p[1], q[0], q[1]]); });
    }
    return seg;
  }
  function lineas(seg, z, col) {
    var pts = []; seg.forEach(function (s) { pts.push(s[0], s[1], z, s[2], s[3], z); });
    var geo = new T.BufferGeometry(); geo.setAttribute('position', new T.Float32BufferAttribute(pts, 3));
    return new T.LineSegments(geo, new T.LineBasicMaterial({ color: col }));
  }
  function calc() {
    var g = F[k]; limpia(traza); limpia(proy);
    var seg = nivel(g.f, lvl, g.d, 160);
    traza = lineas(seg, lvl, P.S); proy = lineas(seg, g.z[0], P.L); c.scene.add(traza, proy);
    plano.position.z = lvl; lc(g.info(lvl));
  }
  var sl = c.slider('Nivel c', 0, 8, 0.05, lvl, function (v) { lvl = v; if (plano) calc(); });
  c.selector('Función ', F.map(function (g) { return g.n; }), 0, function (i) {
    k = i; nuevo(); sl.min = F[i].c[0]; sl.max = F[i].c[1]; sl.value = F[i].c[2]; sl.dispatchEvent(new Event('input'));
  });
  c.alCambiarTema(function (q) {
    P = q; c.renderer.setClearColor(q.bg); colorear();
    if (rejilla) { limpia(rejilla); var g = F[k]; rejilla = new T.GridHelper(2 * g.d, 8, q.mut, q.bd); rejilla.rotation.x = Math.PI / 2; rejilla.position.z = g.z[0]; c.scene.add(rejilla); }
    if (plano) plano.material.color.set(q.S);
    if (traza) { traza.material.color.set(q.S); proy.material.color.set(q.L); }
  });
});
