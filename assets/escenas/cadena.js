/* Regla de la cadena (tema 5.2): una curva γ(t) = (g(t), h(t)) recorre la superficie z = f(x,y);
   d/dt f(γ(t)) = ∇f(γ(t)) · γ′(t). */
Interactivos.registrar('cadena', function (c) {
  var T = c.THREE, H = c.H;
  var F = [
    { n: 'x² + y²', f: function (x, y) { return x * x + y * y; }, g: function (x, y) { return [2 * x, 2 * y]; }, z: [0, 6] },
    { n: 'x² − y² (silla)', f: function (x, y) { return x * x - y * y; }, g: function (x, y) { return [2 * x, -2 * y]; }, z: [-4, 4] },
    { n: '4·e^−(x²+y²) (campana)', f: function (x, y) { return 4 * Math.exp(-(x * x + y * y)); }, g: function (x, y) { var e = Math.exp(-(x * x + y * y)); return [-8 * x * e, -8 * y * e]; }, z: [0, 4] }
  ];
  var G = [
    { n: 'circunferencia γ(t) = (1.3·cos t, 1.3·sen t)', p: function (t) { return [1.3 * Math.cos(t), 1.3 * Math.sin(t)]; }, d: function (t) { return [-1.3 * Math.sin(t), 1.3 * Math.cos(t)]; }, t: [0, 6.283] },
    { n: 'recta γ(t) = (t, 0.5·t)', p: function (t) { return [t, 0.5 * t]; }, d: function () { return [1, 0.5]; }, t: [-1.8, 1.8] },
    { n: 'parábola γ(t) = (t, t² − 1)', p: function (t) { return [t, t * t - 1]; }, d: function (t) { return [1, 2 * t]; }, t: [-1.5, 1.5] }
  ];
  var D = 2, k = 0, j = 1, t = 0.8, P = c.colores(), malla, rejilla, suelo, lev, pt, pp, vert, tang, flG, flV;
  var l1 = c.lectura('γ(t)  ,  γ′(t)'), l2 = c.lectura('∇f(γ(t))'), l3 = c.lectura('(f∘γ)′(t) = ∇f · γ′'), l4 = c.lectura('Comprobación: derivada numérica');
  function fm(x) { return (Math.round(x * 1000) / 1000).toString().replace('-', '−'); }
  function limpia(o) { if (o) { c.scene.remove(o); if (o.geometry) o.geometry.dispose(); } }
  function colorear() {
    if (!malla) return;
    var g = F[k], pos = malla.geometry.attributes.position, col = [], u1 = new T.Color(P.acc), u2 = new T.Color(P.bd), q = new T.Color(), i, u;
    for (i = 0; i < pos.count; i++) { u = (pos.getZ(i) - g.z[0]) / (g.z[1] - g.z[0]); q.copy(u1).lerp(u2, Math.max(0, Math.min(1, u))); col.push(q.r, q.g, q.b); }
    malla.geometry.setAttribute('color', new T.Float32BufferAttribute(col, 3));
  }
  function curvas() {
    var g = F[k], h = G[j], i, n = 120, A = [], B = [], tt;
    for (i = 0; i <= n; i++) { tt = h.t[0] + (h.t[1] - h.t[0]) * i / n; var p = h.p(tt); A.push([p[0], p[1], g.z[0] + 0.01]); B.push([p[0], p[1], g.f(p[0], p[1]) + 0.02]); }
    suelo.set(A); lev.set(B);
  }
  function nuevo() {
    [malla, rejilla, suelo, lev, pt, pp, vert, tang, flG, flV].forEach(limpia);
    var g = F[k], zm = (g.z[0] + g.z[1]) / 2, r = 0.035;
    malla = H.superficie(T, g.f, { n: 70, xr: [-D, D], yr: [-D, D], zmax: 20, opacity: 0.65 });
    malla.material.vertexColors = true; malla.material.color.set(0xffffff); colorear(); c.scene.add(malla);
    rejilla = new T.GridHelper(2 * D, 8, P.mut, P.bd); rejilla.rotation.x = Math.PI / 2; rejilla.position.z = g.z[0]; c.scene.add(rejilla);
    suelo = H.tubo(T, [], r * 0.8, P.L); lev = H.tubo(T, [], r, P.S); vert = H.tubo(T, [], r * 0.4, P.mut); tang = H.tubo(T, [], r * 1.1, P.S);
    pt = new T.Mesh(new T.SphereGeometry(r * 2.6, 16, 12), new T.MeshBasicMaterial({ color: P.fg })); pp = new T.Mesh(new T.SphereGeometry(r * 2, 14, 10), new T.MeshBasicMaterial({ color: P.mut }));
    flG = H.flecha(T, P.S, r * 1.6); flV = H.flecha(T, P.acc, r * 1.6);
    c.scene.add(suelo, lev, vert, tang, pt, pp, flG, flV); curvas();
    c.camera.position.set(D * 4, -D * 4.7, zm + (g.z[1] - g.z[0]) * 1.1 + D * 1.5); c.controls.target.set(0, 0, zm); c.controls.update();
  }
  function calc() {
    var g = F[k], h = G[j], p = h.p(t), v = h.d(t), z0 = g.z[0], fz = g.f(p[0], p[1]), gr = g.g(p[0], p[1]);
    var dd = gr[0] * v[0] + gr[1] * v[1], e = 1e-4, a = h.p(t + e), b = h.p(t - e), num = (g.f(a[0], a[1]) - g.f(b[0], b[1])) / (2 * e);
    pt.position.set(p[0], p[1], fz); pp.position.set(p[0], p[1], z0); vert.set([[p[0], p[1], z0], [p[0], p[1], fz]]);
    var nv = Math.hypot(v[0], v[1]), ng = Math.hypot(gr[0], gr[1]), L = 0.8;
    flV.poner([p[0], p[1], z0], [p[0] + L * v[0] / nv, p[1] + L * v[1] / nv, z0]);
    if (ng > 1e-9) flG.poner([p[0], p[1], z0], [p[0] + L * gr[0] / ng, p[1] + L * gr[1] / ng, z0]); else flG.visible = false;
    var Lt = 0.5, nn = Math.sqrt(nv * nv + dd * dd) || 1;
    tang.set([[p[0] - Lt * v[0] / nn, p[1] - Lt * v[1] / nn, fz - Lt * dd / nn], [p[0] + Lt * v[0] / nn, p[1] + Lt * v[1] / nn, fz + Lt * dd / nn]]);
    l1('(' + fm(p[0]) + ', ' + fm(p[1]) + ')  ,  (' + fm(v[0]) + ', ' + fm(v[1]) + ')'); l2('(' + fm(gr[0]) + ', ' + fm(gr[1]) + ')');
    l3(fm(dd)); l4(fm(num) + '  (coincide)');
  }
  var st = c.slider('Parámetro t', 0, 6.283, 0.01, t, function (x) { t = x; if (pt) calc(); });
  c.selector('Superficie f ', F.map(function (g) { return g.n; }), 0, function (i) { k = i; if (!pt && !malla) { /* primera vez */ } nuevo(); calc(); });
  c.selector('Curva γ ', G.map(function (g) { return g.n; }), 1, function (i) {
    j = i; st.min = G[i].t[0]; st.max = G[i].t[1]; t = (G[i].t[0] + G[i].t[1]) * 0.4 + G[i].t[0] * 0.2; st.value = t; if (suelo) { curvas(); } st.dispatchEvent(new Event('input'));
  });
  c.alCambiarTema(function (q) {
    P = q; c.renderer.setClearColor(q.bg); colorear();
    if (!pt) return;
    var g = F[k]; limpia(rejilla); rejilla = new T.GridHelper(2 * D, 8, q.mut, q.bd); rejilla.rotation.x = Math.PI / 2; rejilla.position.z = g.z[0]; c.scene.add(rejilla);
    suelo.material.color.set(q.L); lev.material.color.set(q.S); vert.material.color.set(q.mut); tang.material.color.set(q.S); pt.material.color.set(q.fg); pp.material.color.set(q.mut);
    [[flG, q.S], [flV, q.acc]].forEach(function (e) { e[0].userData.eje.material.color.set(e[1]); e[0].userData.cono.material.color.set(e[1]); });
  });
});
