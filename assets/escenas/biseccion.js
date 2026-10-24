/* Método de bisección (tema 1.4): cada paso se queda con la mitad donde f cambia de signo. */
Interactivos.registrar('biseccion', function (c) {
  var T = c.THREE, H = c.H, MAXN = 10;
  var F = [
    { n: 'e⁻ˣ − x en [0, 1] (Ej. 1.49 de U)', f: function (x) { return Math.exp(-x) - x; }, a: 0, b: 1, raiz: 0.5671432904097838 },
    { n: 'x³ − 2 en [1, 2]  (raíz cúbica de 2)', f: function (x) { return x * x * x - 2; }, a: 1, b: 2, raiz: Math.cbrt(2) },
    { n: 'cos x − x en [0, 1]', f: function (x) { return Math.cos(x) - x; }, a: 0, b: 1, raiz: 0.7390851332151607 },
    { n: 'x² − 2 en [0, 2]  (√2)', f: function (x) { return x * x - 2; }, a: 0, b: 2, raiz: Math.SQRT2 }
  ];
  var k = 0, n = 4, P = c.colores(), w, Lw, sy, ejes, curva, vA, vB, cur, filas, dots = [], raizPt, hist = [];
  var l1 = c.lectura('Intervalo [aₙ, bₙ]'), l2 = c.lectura('cₙ  (punto medio)'), l3 = c.lectura('f(cₙ)'), l4 = c.lectura('Cota (b − a)/2ⁿ'), lv = c.lectura('');
  function fm(t) { return (Math.round(t * 100000) / 100000).toString().replace('-', '−'); }
  function nuevo() {
    [ejes, curva, vA, vB, cur, filas, raizPt].forEach(function (o) { if (o) c.scene.remove(o); });
    dots.forEach(function (d) { c.scene.remove(d); }); dots = [];
    var g = F[k], i, pts = [], mx = 0, x;
    Lw = g.b - g.a; for (i = 0; i <= 200; i++) { x = g.a + Lw * i / 200; mx = Math.max(mx, Math.abs(g.f(x))); }
    sy = 0.5 * Lw / mx; w = 0.0055 * 2.2 * Lw;
    c.vista(g.a - 0.15 * Lw, g.b + 0.15 * Lw, -0.07 * Lw * (MAXN + 1), 0.6 * Lw);
    ejes = H.cinta(T, [[[g.a - 0.15 * Lw, 0], [g.b + 0.15 * Lw, 0]]], P.fg, w); ejes.position.z = 0.05; c.scene.add(ejes);
    for (i = 0; i <= 300; i++) { x = g.a + Lw * i / 300; pts.push([x, g.f(x) * sy]); }
    curva = H.cinta(T, [pts], P.fg, w * 1.4); curva.position.z = 0.1; c.scene.add(curva);
    vA = H.cinta(T, [], P.mut, w, [w * 4, w * 3]); vB = H.cinta(T, [], P.mut, w, [w * 4, w * 3]); vA.position.z = vB.position.z = 0.15; c.scene.add(vA, vB);
    cur = H.cinta(T, [], P.L, w * 2.2); cur.position.z = 0.4; c.scene.add(cur);
    filas = H.cinta(T, [], P.mut, w * 1.6); filas.position.z = 0.2; c.scene.add(filas);
    for (i = 0; i <= MAXN + 1; i++) { var d = H.punto(T, 0, 0, w * 2.4, P.S); d.position.z = 0.5; d.visible = false; dots.push(d); c.scene.add(d); }
    raizPt = H.punto(T, g.raiz, 0, w * 2.2, P.acc); raizPt.position.z = 0.6; c.scene.add(raizPt);
  }
  function calc() {
    var g = F[k], a = g.a, b = g.b, i, cc, fcv, cs = [];
    hist = [[a, b]];
    for (i = 1; i <= n; i++) {
      cc = (a + b) / 2; fcv = g.f(cc); cs.push(cc);
      if (fcv === 0) { a = b = cc; } else if (g.f(a) * fcv < 0) b = cc; else a = cc;
      hist.push([a, b]);
    }
    var ys = hist.map(function (h, j) { return -0.07 * Lw * j; });
    filas.set(hist.map(function (h, j) { return [[h[0], ys[j]], [h[1], ys[j]]]; }));
    dots.forEach(function (d, j) { d.visible = j < cs.length; if (j < cs.length) d.mover(cs[j], ys[j]); });
    var an = hist[n][0], bn = hist[n][1], cn = n ? cs[n - 1] : null;
    vA.set([[[an, 0], [an, g.f(an) * sy]]]); vB.set([[[bn, 0], [bn, g.f(bn) * sy]]]); cur.set([[[an, 0], [bn, 0]]]);
    l1('[' + fm(an) + ', ' + fm(bn) + ']'); l2(cn === null ? '—  (aún no se ha calculado ninguno)' : fm(cn)); l3(cn === null ? '—' : fm(g.f(cn))); l4(fm(Lw / Math.pow(2, n)));
    lv('Cada fila es un intervalo: arriba el inicial y debajo los siguientes, cada uno la mitad del anterior. El punto azul es la raíz y los naranjas son los puntos medios c₁, c₂, … ' + (cn === null ? '' : 'Error real de cₙ: ' + fm(Math.abs(cn - g.raiz)) + '.'));
  }
  c.slider('Iteraciones n', 0, MAXN, 1, n, function (v) { n = v; if (curva) calc(); }, function (v) { return String(v); });
  c.selector('Función ', F.map(function (g) { return g.n; }), 0, function (i) { k = i; nuevo(); calc(); });
  c.leyenda([['var(--fg)','f(x)','linea'],['var(--mut)','extremos aₙ, bₙ; intervalos anteriores','linea'],['var(--L)','intervalo actual [aₙ, bₙ]','linea'],['var(--S)','puntos medios cₙ','punto'],['var(--acc)','raíz','punto']]);
  c.alCambiarTema(function (q) {
    P = q; c.renderer.setClearColor(q.bg);
    if (!curva) return;
    ejes.material.color.set(q.fg); curva.material.color.set(q.fg); vA.material.color.set(q.mut); vB.material.color.set(q.mut); cur.material.color.set(q.L);
    filas.material.color.set(q.mut); dots.forEach(function (d) { d.material.color.set(q.S); }); raizPt.material.color.set(q.acc);
  });
});
