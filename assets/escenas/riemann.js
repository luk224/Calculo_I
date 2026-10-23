/* Sumas de Riemann (tema 6.1): n rectángulos con altura en el extremo izquierdo, derecho, punto medio, mínimo (suma inferior) o máximo (suma superior). */
Interactivos.registrar('riemann', function (c) {
  var T = c.THREE, H = c.H;
  var G = [
    { n: 'eˣ en [0, 1]  (U Ej. 6.1)', f: Math.exp, a: 0, b: 1, I: Math.E - 1, crit: [], v: [-0.3, 1.3, -0.3, 3] },
    { n: '2x en [−1, 2]  (U Ej. 6.2)', f: function (x) { return 2 * x; }, a: -1, b: 2, I: 3, crit: [], v: [-1.5, 2.5, -3, 5] },
    { n: 'x² en [0, 1]', f: function (x) { return x * x; }, a: 0, b: 1, I: 1 / 3, crit: [0], v: [-0.3, 1.3, -0.3, 1.3] },
    { n: 'sen x en [0, π]', f: Math.sin, a: 0, b: Math.PI, I: 2, crit: [Math.PI / 2], v: [-0.5, 3.7, -0.5, 1.5] },
    { n: 'x³ − x en [−1, 2]  (cambia de signo)', f: function (x) { return x * x * x - x; }, a: -1, b: 2, I: 9 / 4, crit: [-1 / Math.sqrt(3), 1 / Math.sqrt(3)], v: [-1.5, 2.5, -1.5, 6.5] },
    { n: 'e^(−x²) en [0, 1]', f: function (x) { return Math.exp(-x * x); }, a: 0, b: 1, I: 0.7468241328124270, crit: [0], v: [-0.3, 1.3, -0.3, 1.3] }
  ];
  var METODOS = ['Extremo izquierdo', 'Extremo derecho', 'Punto medio', 'Suma inferior (mínimo)', 'Suma superior (máximo)'];
  var W = function (v) { var dx = 1.5 * (v[1] - v[0]), dy = 1.5 * (v[3] - v[2]); return [v[0] - dx, v[1] + dx, v[2] - dy, v[3] + dy]; };
  var k = 0, m = 0, n = 5, P = c.colores(), w;
  var ejes, curva, bordes, relP, relN, area0;
  var lS = c.lectura('Suma de Riemann Sₙ'), lI = c.lectura('Integral exacta'), lE = c.lectura('Error |Sₙ − I|'), lF = c.lectura('Finura ‖P‖ = (b − a)/n');
  var fm = function (t) { return (Math.round(t * 10000) / 10000).toString().replace('-', '−').replace('.', ','); };

  function malla(color) {
    var geo = new T.BufferGeometry();
    var mesh = new T.Mesh(geo, new T.MeshBasicMaterial({ color: color, transparent: true, opacity: 0.38, side: T.DoubleSide }));
    mesh.set = function (rs) {
      var pos = [], i;
      for (i = 0; i < rs.length; i++) {
        var r = rs[i]; pos.push(r[0], 0, 0, r[1], 0, 0, r[1], r[2], 0, r[0], 0, 0, r[1], r[2], 0, r[0], r[2], 0);
      }
      mesh.geometry.dispose(); mesh.geometry = new T.BufferGeometry();
      mesh.geometry.setAttribute('position', new T.Float32BufferAttribute(pos, 3));
    };
    return mesh;
  }
  function nuevo() {
    [ejes, curva, bordes, relP, relN].forEach(function (o) { if (o) c.scene.remove(o); });
    var g = G[k], v = g.v, vw = W(v); w = 0.0055 * (v[3] - v[2]); c.vista(v[0], v[1], v[2], v[3]);
    ejes = H.ejes2D(T, vw, w, P.fg, P.bd); c.scene.add(ejes);
    relP = malla(P.S); relP.position.z = 0.02; c.scene.add(relP);
    relN = malla(P.E); relN.position.z = 0.03; c.scene.add(relN);
    bordes = H.cinta(T, [], P.mut, w * 0.8); bordes.position.z = 0.1; c.scene.add(bordes);
    curva = H.cinta(T, H.grafica(g.f, vw[0], vw[1], 1600, 1e3), P.fg, w * 1.4); curva.position.z = 0.2; c.scene.add(curva);
  }
  function altura(g, x0, x1) {
    if (m === 0) return g.f(x0);
    if (m === 1) return g.f(x1);
    if (m === 2) return g.f((x0 + x1) / 2);
    var lo = Infinity, hi = -Infinity, j, y;
    var xs = [], q; for (j = 0; j <= 60; j++) xs.push(x0 + (x1 - x0) * j / 60);
    g.crit.forEach(function (q) { if (q > x0 && q < x1) xs.push(q); });
    xs.forEach(function (x) { y = g.f(x); if (y < lo) lo = y; if (y > hi) hi = y; });
    return m === 3 ? lo : hi;
  }
  function calc() {
    var g = G[k], h = (g.b - g.a) / n, i, rs = [], rp = [], rn = [], pols = [], S = 0;
    for (i = 0; i < n; i++) {
      var x0 = g.a + i * h, x1 = x0 + h, y = altura(g, x0, x1), r = [x0, x1, y];
      S += y * h; rs.push(r); (y >= 0 ? rp : rn).push(r);
      pols.push([[x0, 0], [x0, y], [x1, y], [x1, 0], [x0, 0]]);
    }
    relP.set(rp); relN.set(rn); bordes.set(pols);
    lS(fm(S)); lI(fm(g.I)); lE(fm(Math.abs(S - g.I))); lF(fm(h));
  }
  c.slider('Subintervalos n', 1, 60, 1, n, function (v) { n = v; if (bordes) calc(); }, function (v) { return String(v); });
  c.selector('Altura ', METODOS, 0, function (i) { m = i; if (bordes) calc(); });
  c.selector('Función ', G.map(function (g) { return g.n; }), 0, function (i) { k = i; nuevo(); calc(); });
  c.alCambiarTema(function (p) {
    P = p; c.renderer.setClearColor(p.bg);
    if (!ejes) return;
    ejes.userData.eje.color.set(p.fg); ejes.userData.rejilla.color.set(p.bd); curva.material.color.set(p.fg);
    bordes.material.color.set(p.mut); relP.material.color.set(p.S); relN.material.color.set(p.E);
  });
});
