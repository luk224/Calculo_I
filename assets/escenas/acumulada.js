/* Función área acumulada F(x) = ∫ₐˣ f(t) dt (tema 6.2): el área sombreada hasta x, la curva F y su tangente, cuya pendiente es f(x) (primer teorema fundamental). */
Interactivos.registrar('acumulada', function (c) {
  var T = c.THREE, H = c.H;
  function simpson(f, a, b, n) { n = n || 2000; var h = (b - a) / n, s = f(a) + f(b), i; for (i = 1; i < n; i++) s += f(a + i * h) * (i % 2 ? 4 : 2); return s * h / 3; }
  var G = [
    { n: 'cos t desde 0  (F = sen x)', f: Math.cos, a: 0, xm: 6.2, v: [-0.5, 6.5, -1.6, 1.6] },
    { n: 't·sen t desde 0  (E 6.13)', f: function (t) { return t * Math.sin(t); }, a: 0, xm: 23, v: [-1, 24, -26, 26] },
    { n: 'e^(−t²) desde 0  (U Ej. 6.5)', f: function (t) { return Math.exp(-t * t); }, a: 0, xm: 3.2, v: [-0.4, 3.5, -0.3, 1.2] },
    { n: '1/t desde 1  (F = ln x)', f: function (t) { return 1 / t; }, a: 1, xm: 6, v: [0.2, 6.5, -0.3, 2.2] }
  ];
  var W = function (v) { var dx = 1.5 * (v[1] - v[0]), dy = 1.5 * (v[3] - v[2]); return [v[0] - dx, v[1] + dx, v[2] - dy, v[3] + dy]; };
  var k = 0, x = 1, P = c.colores(), w, sx;
  var ejes, curvaf, curvaF, tg, relP, relN, pf, pF, vert;
  var lF = c.lectura('F(x) = ∫ₐˣ f'), lf = c.lectura('f(x)'), ld = c.lectura('Pendiente de F en x (cociente con h = 0,001)');
  var fm = function (t) { return (Math.round(t * 10000) / 10000).toString().replace('-', '−').replace('.', ','); };
  var F;
  /* Tabla de F precalculada por trozos (una vez por función): F(u) = F(nodo) + Simpson corto desde el nodo anterior. */
  var tabla = null;
  function hacerTabla() {
    var g = G[k], M = 600, h = (g.xm - g.a) / M, i; tabla = [0];
    for (i = 1; i <= M; i++) tabla.push(tabla[i - 1] + simpson(g.f, g.a + (i - 1) * h, g.a + i * h, 8));
    tabla.h = h;
  }
  F = function (u) {
    var g = G[k], i = Math.min(tabla.length - 2, Math.max(0, Math.floor((u - g.a) / tabla.h)));
    return tabla[i] + simpson(g.f, g.a + i * tabla.h, u, 8);
  };

  function malla(color) {
    var mesh = new T.Mesh(new T.BufferGeometry(), new T.MeshBasicMaterial({ color: color, transparent: true, opacity: 0.38, side: T.DoubleSide }));
    mesh.set = function (rs) {
      var pos = [], i;
      for (i = 0; i < rs.length; i++) { var r = rs[i]; pos.push(r[0], 0, 0, r[1], 0, 0, r[1], r[3], 0, r[0], 0, 0, r[1], r[3], 0, r[0], r[2], 0); }
      mesh.geometry.dispose(); mesh.geometry = new T.BufferGeometry();
      mesh.geometry.setAttribute('position', new T.Float32BufferAttribute(pos, 3));
    };
    return mesh;
  }
  function nuevo() {
    [ejes, curvaf, curvaF, tg, relP, relN, pf, pF, vert].forEach(function (o) { if (o) c.scene.remove(o); });
    hacerTabla(); var g = G[k], v = g.v, vw = W(v); w = 0.0055 * (v[3] - v[2]); c.vista(v[0], v[1], v[2], v[3]);
    ejes = H.ejes2D(T, vw, w, P.fg, P.bd); c.scene.add(ejes);
    relP = malla(P.S); relP.position.z = 0.02; c.scene.add(relP);
    relN = malla(P.E); relN.position.z = 0.03; c.scene.add(relN);
    curvaf = H.cinta(T, H.grafica(g.f, g.a, vw[1], 1600, 1e3), P.fg, w * 1.4); curvaf.position.z = 0.2; c.scene.add(curvaf);
    var xs = [], i, N = 400; for (i = 0; i <= N; i++) { var u = g.a + (g.xm - g.a) * i / N; xs.push([u, F(u)]); }
    curvaF = H.cinta(T, [xs], P.L, w * 1.6); curvaF.position.z = 0.25; c.scene.add(curvaF);
    tg = H.cinta(T, [], P.acc, w * 1.3); tg.position.z = 0.3; c.scene.add(tg);
    vert = H.cinta(T, [], P.mut, w, [w * 5, w * 3]); vert.position.z = 0.1; c.scene.add(vert);
    pf = H.punto(T, 0, 0, w * 2.3, P.fg); pF = H.punto(T, 0, 0, w * 2.6, P.L);
    [pf, pF].forEach(function (o) { o.position.z = 0.5; c.scene.add(o); });
    sx.min = g.a; sx.max = g.xm; sx.step = 0.01; x = Math.round((g.a + (g.xm - g.a) * 0.35) * 100) / 100; sx.value = x;
  }
  function calc() {
    var g = G[k], N = 240, h = (x - g.a) / N, i, pp = [], pn = [], Fx = F(x), fx = g.f(x), hh = 1e-3;
    for (i = 0; i < N; i++) {
      var x0 = g.a + i * h, x1 = x0 + h, y0 = g.f(x0), y1 = g.f(x1), r = [x0, x1, y0, y1];
      (y0 + y1 >= 0 ? pp : pn).push(r);
    }
    relP.set(pp); relN.set(pn);
    var d = 0.1 * (g.v[1] - g.v[0]);
    tg.set([[[x - d, Fx - fx * d], [x + d, Fx + fx * d]]]);
    vert.set([[[x, 0], [x, Math.max(fx, Fx)]], [[x, Math.min(fx, Fx, 0)], [x, 0]]]);
    pf.mover(x, fx); pF.mover(x, Fx);
    lF(fm(Fx)); lf(fm(fx)); ld(fm((F(x + hh) - F(x)) / hh));
  }
  sx = c.slider('x (extremo superior)', 0, 1, 0.01, x, function (v) { x = v; if (tg) calc(); });
  c.selector('Función ', G.map(function (g) { return g.n; }), 0, function (i) { k = i; nuevo(); calc(); });
  c.alCambiarTema(function (p) {
    P = p; c.renderer.setClearColor(p.bg);
    if (!ejes) return;
    ejes.userData.eje.color.set(p.fg); ejes.userData.rejilla.color.set(p.bd); curvaf.material.color.set(p.fg); curvaF.material.color.set(p.L);
    tg.material.color.set(p.acc); vert.material.color.set(p.mut); relP.material.color.set(p.S); relN.material.color.set(p.E);
    pf.material.color.set(p.fg); pF.material.color.set(p.L);
  });
});
