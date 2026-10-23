/* Integración numérica (tema 6.4): trapecio compuesto, Simpson compuesta y punto medio con n subintervalos (convención de U: Simpson usa 2n+1 nodos).
   Se dibuja el área de la aproximación, la diferencia con f (zona del error), la aproximación, el valor exacto, el error y la cota de U (Teor. 6.3 y 6.4). */
Interactivos.registrar('integracion-numerica', function (c) {
  var T = c.THREE, H = c.H, E = Math.E;
  /* M2 = máx |f''|, M4 = máx |f⁽⁴⁾| en [a, b] (para las cotas de U). */
  var G = [
    { n: 'sen x en [0, π]', f: Math.sin, a: 0, b: Math.PI, I: 2, M2: 1, M4: 1, v: [-0.5, 3.7, -0.4, 1.4] },
    { n: 'eˣ en [0, 1]', f: Math.exp, a: 0, b: 1, I: E - 1, M2: E, M4: E, v: [-0.3, 1.3, -0.3, 3] },
    { n: '1/x en [1, 2]  (ln 2)', f: function (x) { return 1 / x; }, a: 1, b: 2, I: Math.LN2, M2: 2, M4: 24, v: [-0.3, 2.4, -0.2, 1.3] },
    { n: 'e^(−x²) en [0, 1]  (sin primitiva elemental)', f: function (x) { return Math.exp(-x * x); }, a: 0, b: 1, I: 0.7468241328124270, M2: 2, M4: 12, v: [-0.3, 1.3, -0.3, 1.3] }
  ];
  var METODOS = ['Trapecio compuesto', 'Simpson compuesta', 'Punto medio (rectángulos centrales)'];
  var W = function (v) { var dx = 1.5 * (v[1] - v[0]), dy = 1.5 * (v[3] - v[2]); return [v[0] - dx, v[1] + dx, v[2] - dy, v[3] + dy]; };
  var k = 0, m = 0, n = 4, P = c.colores(), w;
  var ejes, curva, bordes, nodos, medios, relA, relE, pts = [];
  var lA = c.lectura('Aproximación'), lI = c.lectura('Valor exacto'), lE = c.lectura('Error (aproximación − exacto)'), lC = c.lectura('Cota de U'), lN = c.lectura('Valores de f que se usan');
  var fm = function (t, d) { return t.toFixed(d).replace(/-/g, '−').replace('.', ','); };
  var SUP = { '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '-': '⁻' };
  /* Notación científica legible: 2,69·10⁻⁴ (con signo opcional). */
  var cien = function (t, signo) {
    var p = Math.abs(t).toExponential(2).split('e'), ex = String(parseInt(p[1], 10)).replace(/./g, function (ch) { return SUP[ch]; });
    return (t < 0 ? '−' : (signo ? '+' : '')) + p[0].replace('.', ',') + '·10' + ex;
  };
  var fe = function (t) { return t === 0 ? '0' : Math.abs(t) < 1e-3 ? cien(t, true) : (t > 0 ? '+' : '−') + fm(Math.abs(t), 6); };

  function malla(color) {
    var mesh = new T.Mesh(new T.BufferGeometry(), new T.MeshBasicMaterial({ color: color, transparent: true, opacity: 0.4, side: T.DoubleSide }));
    mesh.set = function (pos) {
      mesh.geometry.dispose(); mesh.geometry = new T.BufferGeometry();
      mesh.geometry.setAttribute('position', new T.Float32BufferAttribute(pos, 3));
    };
    return mesh;
  }
  function nuevo() {
    [ejes, curva, bordes, nodos, medios, relA, relE].concat(pts).forEach(function (o) { if (o) c.scene.remove(o); }); pts = [];
    var g = G[k], v = g.v, vw = W(v); w = 0.0055 * (v[3] - v[2]); c.vista(v[0], v[1], v[2], v[3]);
    ejes = H.ejes2D(T, vw, w, P.fg, P.bd); c.scene.add(ejes);
    relA = malla(P.S); relA.position.z = 0.02; c.scene.add(relA);
    relE = malla(P.E); relE.position.z = 0.03; c.scene.add(relE);
    nodos = H.cinta(T, [], P.mut, w * 0.8); nodos.position.z = 0.08; c.scene.add(nodos);
    medios = H.cinta(T, [], P.acc, w * 1.1, [w * 5, w * 3]); medios.position.z = 0.15; c.scene.add(medios);
    for (var q = 0; q < 20; q++) { var pt = H.punto(T, 0, 0, w * 2.2, P.acc); pt.position.z = 0.35; pt.visible = false; c.scene.add(pt); pts.push(pt); }
    bordes = H.cinta(T, [], P.L, w * 1.5); bordes.position.z = 0.1; c.scene.add(bordes);
    curva = H.cinta(T, H.grafica(g.f, vw[0], vw[1], 1600, Math.max(Math.abs(vw[2]), Math.abs(vw[3]))), P.fg, w * 1.4); curva.position.z = 0.2; c.scene.add(curva);
  }
  /* Parábola por (x0,y0), (xm,ym), (x1,y1) (interpolación de Lagrange). */
  function parab(x, x0, xm, x1, y0, ym, y1) {
    return y0 * (x - xm) * (x - x1) / ((x0 - xm) * (x0 - x1)) + ym * (x - x0) * (x - x1) / ((xm - x0) * (xm - x1)) + y1 * (x - x0) * (x - xm) / ((x1 - x0) * (x1 - xm));
  }
  function calc() {
    var g = G[k], f = g.f, h = (g.b - g.a) / n, i, j, S = 0, usados, cota;
    var area = [], dif = [], contorno = [], vert = [], marc = [];
    var f0 = f(g.a), fn = f(g.b), sInt = 0, sMed = 0;
    for (i = 1; i < n; i++) sInt += f(g.a + i * h);
    for (i = 0; i < n; i++) sMed += f(g.a + (i + 0.5) * h);
    if (m === 0) { S = h / 2 * (f0 + 2 * sInt + fn); usados = (n + 1) + ' (nodos)'; cota = Math.pow(g.b - g.a, 3) * g.M2 / (12 * n * n); }
    else if (m === 1) { S = h / 6 * (f0 + 4 * sMed + 2 * sInt + fn); usados = (2 * n + 1) + ' (nodos)'; cota = Math.pow(g.b - g.a, 5) * g.M4 / (2880 * Math.pow(n, 4)); }
    else { S = h * sMed; usados = n + ' (puntos medios)'; cota = null; }
    for (i = 0; i < pts.length; i++) pts[i].visible = false;
    for (i = 0; i < n; i++) {
      var x0 = g.a + i * h, x1 = x0 + h, xm = x0 + h / 2, y0 = f(x0), y1 = f(x1), ym = f(xm);
      var p = m === 0 ? function (x) { return y0 + (y1 - y0) * (x - x0) / h; } : m === 1 ? function (x) { return parab(x, x0, xm, x1, y0, ym, y1); } : function () { return ym; };
      var top = [], xs = [];
      var q = m === 1 ? 24 : 2;
      for (j = 0; j <= q; j++) { var x = x0 + h * j / q; xs.push(x); top.push([x, p(x)]); }
      for (j = 0; j + 1 < top.length; j++) {
        var a = top[j], b = top[j + 1];
        area.push(a[0], 0, 0, b[0], 0, 0, b[0], b[1], 0, a[0], 0, 0, b[0], b[1], 0, a[0], a[1], 0);
      }
      /* Zona del error: entre f y la aproximación (se muestrea f con 16 puntos por subintervalo). */
      var R = 16, prev = null;
      for (j = 0; j <= R; j++) {
        var xx = x0 + h * j / R, cur = [xx, f(xx), p(xx)];
        if (prev) dif.push(prev[0], prev[1], 0, prev[0], prev[2], 0, cur[0], cur[2], 0, prev[0], prev[1], 0, cur[0], cur[2], 0, cur[0], cur[1], 0);
        prev = cur;
      }
      if (m === 2) contorno.push([[x0, 0], [x0, ym], [x1, ym], [x1, 0]]);
      else { contorno.push(top); vert.push([[x0, 0], [x0, y0]]); if (i === n - 1) vert.push([[x1, 0], [x1, y1]]); }
      if (m !== 0) { marc.push([[xm, 0], [xm, ym]]); pts[i].mover(xm, ym); pts[i].visible = true; }
    }
    relA.set(area); relE.set(dif); bordes.set(contorno); nodos.set(vert); medios.set(marc);
    lA(fm(S, 6)); lI(fm(g.I, 6)); lE(fe(S - g.I)); lN(usados);
    lC(cota === null ? 'sin cota en este tema' : (m === 0 ? 'Teor. 6.3: ' : 'Teor. 6.4: ') + (cota < 1e-3 ? cien(cota, false) : fm(cota, 6)));
  }
  c.slider('Subintervalos n', 1, 20, 1, n, function (v) { n = v; if (bordes) calc(); }, function (v) { return String(v); });
  c.selector('Método ', METODOS, 0, function (i) { m = i; if (bordes) calc(); });
  c.selector('Función ', G.map(function (g) { return g.n; }), 0, function (i) { k = i; nuevo(); calc(); });
  c.leyenda([['var(--fg)', 'f(x)', 'linea'], ['var(--L)', 'borde de la aproximación (recta, parábola o rectángulo)', 'linea'],
    ['var(--acc)', 'punto medio de cada subintervalo (Simpson y punto medio)', 'punto'], ['var(--S)', 'área que se calcula', 'area'], ['var(--E)', 'diferencia entre f y la aproximación (el error)', 'area']]);
  c.alCambiarTema(function (p) {
    P = p; c.renderer.setClearColor(p.bg);
    if (!ejes) return;
    ejes.userData.eje.color.set(p.fg); ejes.userData.rejilla.color.set(p.bd); curva.material.color.set(p.fg);
    bordes.material.color.set(p.L); medios.material.color.set(p.acc); pts.forEach(function (o) { o.material.color.set(p.acc); }); nodos.material.color.set(p.mut); relA.material.color.set(p.S); relE.material.color.set(p.E);
  });
});
