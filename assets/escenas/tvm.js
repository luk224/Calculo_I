/* Rolle y valor medio (tema 2.5). params: {"modo":"rolle"} fija f(a)=f(b) y propone casos donde falla una hipótesis. */
Interactivos.registrar('tvm', function (c) {
  var T = c.THREE, H = c.H, rolle = c.params.modo === 'rolle';
  var nd = function (x) { return Math.abs(x) < 1e-9 ? NaN : (x > 0 ? 1 : -1); };
  var G = rolle ? [
    { n: 'sen x en [0, π]', f: Math.sin, d: Math.cos, a: 0, b: Math.PI, v: [-0.5, 3.7, -0.5, 1.6] },
    { n: 'x³ − x en [−1, 1] (dos valores de c)', f: function (x) { return x * x * x - x; }, d: function (x) { return 3 * x * x - 1; }, a: -1, b: 1, v: [-1.6, 1.6, -1, 1] },
    { n: '|x| en [−1, 1] (no derivable en 0)', f: Math.abs, d: nd, a: -1, b: 1, v: [-1.6, 1.6, -0.5, 1.6] },
    { n: 'x − ⌊x⌋ en [0, 1] (no continua en 1)', f: function (x) { return x - Math.floor(x); }, d: function () { return 1; }, a: 0, b: 1, v: [-0.5, 1.5, -0.5, 1.5], salto: 1 }
  ] : [
    { n: 'x³ − x', f: function (x) { return x * x * x - x; }, d: function (x) { return 3 * x * x - 1; }, v: [-2.5, 2.5, -4, 4] },
    { n: 'sen x', f: Math.sin, d: Math.cos, v: [-2.5, 5.5, -2, 2] },
    { n: 'eˣ', f: Math.exp, d: Math.exp, v: [-2.5, 2.5, -1, 7] },
    { n: '|x| (no derivable en 0)', f: Math.abs, d: nd, v: [-2.5, 2.5, -1, 3] }
  ];
  var W = function (v) { var dx = 1.5 * (v[1] - v[0]), dy = 1.5 * (v[3] - v[2]); return [v[0] - dx, v[1] + dx, v[2] - dy, v[3] + dy]; };
  var k = 0, a = rolle ? 0 : -1.5, b = rolle ? Math.PI : 2, cc = 1, P = c.colores(), w;
  var ejes, curva, cuerda, tg, pa, pb, pc, validos = [];
  var lm = c.lectura('Pendiente de la cuerda'), ld = c.lectura('f′(c)'), lv = c.lectura('Valores de c con f′(c) = pendiente');

  function nuevo() {
    [ejes, curva, cuerda, tg, pa, pb, pc].forEach(function (o) { if (o) c.scene.remove(o); });
    validos.forEach(function (o) { c.scene.remove(o); }); validos = [];
    var v = G[k].v; w = 0.0055 * (v[3] - v[2]); c.vista(v[0], v[1], v[2], v[3]);
    var vw = W(v);
    ejes = H.ejes2D(T, vw, w, P.fg, P.bd); c.scene.add(ejes);
    var g = G[k], pols = g.salto
      ? [H.grafica(g.f, vw[0], g.salto - 1e-6, 100, 1e3), H.grafica(g.f, g.salto, vw[1], 100, 1e3)].reduce(function (s, e) { return s.concat(e); }, [])
      : H.grafica(g.f, vw[0], vw[1], 1600, 1e3);
    curva = H.cinta(T, pols, P.fg, w * 1.4); curva.position.z = 0.1; c.scene.add(curva);
    cuerda = H.cinta(T, [], P.mut, w, [w * 5, w * 3]); cuerda.position.z = 0.2; c.scene.add(cuerda);
    tg = H.cinta(T, [], P.S, w * 1.3); tg.position.z = 0.3; c.scene.add(tg);
    pa = H.punto(T, 0, 0, w * 2.3, P.fg); pb = H.punto(T, 0, 0, w * 2.3, P.fg); pc = H.punto(T, 0, 0, w * 2.6, P.S);
    [pa, pb, pc].forEach(function (o) { o.position.z = 0.5; c.scene.add(o); });
  }
  function calc() {
    var g = G[k], v = g.v, fa = g.f(a), fb = g.salto ? 0 : g.f(b), m = (fb - fa) / (b - a), fc = g.f(cc), dc = g.d(cc);
    var x0 = W(v)[0], x1 = W(v)[1];
    cuerda.set([[[x0, fa + m * (x0 - a)], [x1, fa + m * (x1 - a)]]]);
    pa.mover(a, fa); pb.mover(b, fb); pc.mover(cc, fc);
    if (isFinite(dc)) { tg.set([[[x0, fc + dc * (x0 - cc)], [x1, fc + dc * (x1 - cc)]]]); } else tg.set([]);
    // valores de c: cambios de signo de f′ − m en (a,b), afinados por bisección y comprobados
    var xs = [], N = 2000, i, prev = null;
    validos.forEach(function (o) { c.scene.remove(o); }); validos = [];
    for (i = 1; i < N; i++) {
      var p = a + (b - a) * i / N, q = a + (b - a) * (i + 1) / N, u = g.d(p) - m, t = g.d(q) - m;
      if (!isFinite(u) || !isFinite(t) || u * t > 0) continue;
      var lo = p, hi = q, j;
      for (j = 0; j < 40; j++) { var mid = (lo + hi) / 2; if ((g.d(lo) - m) * (g.d(mid) - m) <= 0) hi = mid; else lo = mid; }
      var r = (lo + hi) / 2; if (Math.abs(g.d(r) - m) < 1e-6 && (prev === null || Math.abs(r - prev) > 1e-3)) { xs.push(r); prev = r; }
    }
    xs.forEach(function (r) { var d = H.punto(T, r, g.f(r), w * 2.2, P.L); d.position.z = 0.45; validos.push(d); c.scene.add(d); });
    var fm = function (t) { return (Math.round(t * 1000) / 1000).toString().replace('-', '−'); };
    lm(fm(m)); ld(isFinite(dc) ? fm(dc) : 'no existe');
    lv(xs.length ? xs.map(fm).join(',  ') : 'ninguno: el teorema no se aplica (falla una hipótesis)');
  }
  var sa, sb, sc;
  if (!rolle) {
    sa = c.slider('a', -2.4, 1.9, 0.05, a, function (v) { a = v; if (b < a + 0.3) { b = a + 0.3; sb.value = b; sb.dispatchEvent(new Event('input')); } clampC(); if (tg) calc(); });
    sb = c.slider('b', -1.9, 2.4, 0.05, b, function (v) { b = v; if (a > b - 0.3) { a = b - 0.3; sa.value = a; sa.dispatchEvent(new Event('input')); } clampC(); if (tg) calc(); });
  }
  function clampC() { if (!sc) return; sc.min = a; sc.max = b; if (cc < a || cc > b) { cc = (a + b) / 2; sc.value = cc; sc.dispatchEvent(new Event('input')); } }
  sc = c.slider('c', a, b, 0.01, rolle ? Math.PI / 2 : 1, function (v) { cc = v; if (tg) calc(); });
  c.selector('Función ', G.map(function (g) { return g.n; }), 0, function (i) {
    k = i; nuevo();
    if (rolle) { a = G[i].a; b = G[i].b; sc.min = a; sc.max = b; sc.step = (b - a) / 200; cc = (a + b) / 2; sc.value = cc; sc.dispatchEvent(new Event('input')); }
    else { calc(); }
  });
  c.leyenda([['var(--fg)','gráfica de f; extremos a y b','linea'],['var(--mut)','cuerda (pendiente media)','linea'],['var(--S)','tangente en c','linea'],['var(--L)','puntos c que cumplen el teorema','punto']]);
  c.alCambiarTema(function (p) {
    P = p; c.renderer.setClearColor(p.bg);
    if (!ejes) return;
    ejes.userData.eje.color.set(p.fg); ejes.userData.rejilla.color.set(p.bd); curva.material.color.set(p.fg);
    cuerda.material.color.set(p.mut); tg.material.color.set(p.S); pa.material.color.set(p.fg); pb.material.color.set(p.fg); pc.material.color.set(p.S);
    validos.forEach(function (o) { o.material.color.set(p.L); });
  });
});
