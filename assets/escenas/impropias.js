/* Integrales impropias (tema 6.5): área acumulada hasta un extremo que se acerca al punto problemático.
   0) 1ª especie: ∫₁ᴹ dx/xᵖ con M = 10^s;  1) 2ª especie: ∫_c¹ dx/xᵖ con c = 10^(−s);  2) E 6.44: ∫₀ᴹ cos(2πx) dx (no hay límite).
   Valores en forma cerrada (sin integración numérica): carga inmediata. */
Interactivos.registrar('impropias', function (c) {
  var T = c.THREE, H = c.H, YM = 3.5, XM = 10, K2 = 4;
  var CASOS = ['1ª especie: área bajo 1/xᵖ entre 1 y M', '2ª especie: área bajo 1/xᵖ entre c y 1', 'E 6.44: ∫₀ᴹ cos(2πx) dx (oscila)'];
  var VISTAS = [[-0.4, XM, -0.2, 1.4], [-0.15, 1.4, -0.3, YM], [-0.3, K2, -1.4, 1.4]];
  var W = function (v) { var dx = 1.5 * (v[1] - v[0]), dy = 1.5 * (v[3] - v[2]); return [v[0] - dx, v[1] + dx, v[2] - dy, v[3] + dy]; };
  var k = 0, p = 2, s = 1, P = c.colores(), w;
  var ejes, curva, curvaF, vert, relP, relN, pt, ptF;
  var lA = c.lectura('Área acumulada'), lL = c.lectura('Valor al que tiende'), lF = c.lectura('Lo que falta');
  var fm = function (t, d) { return (Math.round(t * Math.pow(10, d)) / Math.pow(10, d)).toFixed(d).replace('-', '−').replace('.', ','); };
  var uno = function () { return Math.abs(p - 1) < 1e-9; };
  var ext = function () { return k === 0 ? Math.pow(10, s) : k === 1 ? Math.pow(10, -s) : s * K2 / 3; };
  var F2 = function (m) { return Math.sin(2 * Math.PI * m) / (2 * Math.PI); };

  function malla(color) {
    var mesh = new T.Mesh(new T.BufferGeometry(), new T.MeshBasicMaterial({ color: color, transparent: true, opacity: 0.4, side: T.DoubleSide }));
    mesh.set = function (rs) {
      var pos = [], i;
      for (i = 0; i < rs.length; i++) { var r = rs[i]; pos.push(r[0], 0, 0, r[1], 0, 0, r[1], r[3], 0, r[0], 0, 0, r[1], r[3], 0, r[0], r[2], 0); }
      mesh.geometry.dispose(); mesh.geometry = new T.BufferGeometry();
      mesh.geometry.setAttribute('position', new T.Float32BufferAttribute(pos, 3));
    };
    return mesh;
  }
  var f = function (x) { return k === 2 ? Math.cos(2 * Math.PI * x) : Math.pow(x, -p); };

  function nuevo() {
    [ejes, curva, curvaF, vert, relP, relN, pt, ptF].forEach(function (o) { if (o) c.scene.remove(o); });
    var v = VISTAS[k], vw = W(v); w = 0.0055 * (v[3] - v[2]); c.vista(v[0], v[1], v[2], v[3]);
    ejes = H.ejes2D(T, vw, w, P.fg, P.bd); c.scene.add(ejes);
    relP = malla(P.S); relP.position.z = 0.02; c.scene.add(relP);
    relN = malla(P.E); relN.position.z = 0.03; c.scene.add(relN);
    curva = H.cinta(T, [], P.fg, w * 1.4); curva.position.z = 0.2; c.scene.add(curva);
    curvaF = H.cinta(T, [], P.L, w * 1.5); curvaF.position.z = 0.25; c.scene.add(curvaF);
    vert = H.cinta(T, [], P.mut, w, [w * 5, w * 3]); vert.position.z = 0.1; c.scene.add(vert);
    pt = H.punto(T, 0, 0, w * 2.3, P.fg); ptF = H.punto(T, 0, 0, w * 2.6, P.L);
    [pt, ptF].forEach(function (o) { o.position.z = 0.5; c.scene.add(o); });
  }
  function calc() {
    var m = ext(), N = 360, i, pp = [], pn = [], cur = [], A, L, lim, falta;
    if (k === 0) {
      var tope = Math.min(m, XM);
      for (i = 0; i < N; i++) { var a = 1 + (tope - 1) * i / N, b = 1 + (tope - 1) * (i + 1) / N; pp.push([a, b, f(a), f(b)]); }
      cur = H.grafica(f, 1, XM, 400, 1e3);
      A = uno() ? Math.log(m) : (Math.pow(m, 1 - p) - 1) / (1 - p);
      lim = p > 1 + 1e-9 ? 1 / (p - 1) : Infinity;
      vert.set(m <= XM ? [[[m, 0], [m, f(m)]]] : []); pt.mover(m <= XM ? m : -10, f(m)); ptF.mover(-10, 0); curvaF.set([]);
    } else if (k === 1) {
      /* Puntos en progresión geométrica de c a 1 para resolver bien la zona cercana a 0. */
      for (i = 0; i < N; i++) { var a2 = m * Math.pow(1 / m, i / N), b2 = m * Math.pow(1 / m, (i + 1) / N); pp.push([a2, b2, Math.min(f(a2), YM), Math.min(f(b2), YM)]); }
      var x0 = Math.pow(YM, -1 / p), seg = [[x0 < 1 ? x0 : 1, YM]], j; /* la gráfica se corta en y = YM */
      for (j = 1; j <= 300; j++) { var xx = x0 + (1 - x0) * j / 300; seg.push([xx, f(xx)]); }
      cur = x0 < 1 ? [seg] : [];
      A = uno() ? -Math.log(m) : (1 - Math.pow(m, 1 - p)) / (1 - p);
      lim = p < 1 - 1e-9 ? 1 / (1 - p) : Infinity;
      vert.set([[[m, 0], [m, Math.min(f(m), YM)]]]); pt.mover(m, Math.min(f(m), YM)); ptF.mover(-10, 0); curvaF.set([]);
    } else {
      var Nn = 1400, h = m / Nn;
      for (i = 0; i < Nn; i++) { var a3 = i * h, b3 = a3 + h, r = [a3, b3, f(a3), f(b3)]; (f(a3 + h / 2) >= 0 ? pp : pn).push(r); }
      cur = H.grafica(f, 0, K2, 800, 10);
      A = F2(m); lim = NaN;
      var fs = []; for (i = 0; i <= 480; i++) { var u = m * i / 480; fs.push([u, F2(u)]); }
      curvaF.set([fs]); vert.set([[[m, 0], [m, f(m)]]]); pt.mover(m, f(m)); ptF.mover(m, A);
    }
    relP.set(pp); relN.set(pn); curva.set(cur);
    if (k === 2) { lA('F(M) = ' + fm(A, 4)); lL('no existe (F(M) oscila entre −0,1592 y 0,1592)'); lF('—'); return; }
    var nom = k === 0 ? 'M = ' + (m >= 100 ? fm(m, 0) : fm(m, 2)) : 'c = ' + (m >= 0.01 ? fm(m, 3) : fm(m, 4));
    lA(nom + ' → ' + fm(A, 4));
    if (isFinite(lim)) { lL(fm(lim, 4) + '  (converge)'); lF(fm(lim - A, 4)); } else { lL('+∞  (diverge)'); lF('crece sin tope'); }
  }
  var sr = c.slider('Extremo móvil (M en 1ª especie y E 6.44; c en 2ª especie)', 0, 3, 0.01, s, function (v) { s = v; if (curva) calc(); }, function (v) {
    var m = k === 0 ? Math.pow(10, v) : k === 1 ? Math.pow(10, -v) : v * K2 / 3;
    return k === 0 ? (m >= 100 ? fm(m, 0) : fm(m, 2)) : k === 1 ? (m >= 0.01 ? fm(m, 3) : fm(m, 4)) : fm(m, 2);
  });
  c.slider('Exponente p (no se usa en E 6.44)', 0.3, 3, 0.1, p, function (v) { p = Math.round(v * 10) / 10; if (curva) calc(); }, function (v) { return fm(Math.round(v * 10) / 10, 1); });
  c.selector('Integral ', CASOS, 0, function (i) { k = i; nuevo(); calc(); if (sr) sr.dispatchEvent(new Event('input')); });
  c.leyenda([['var(--fg)', 'integrando', 'linea'], ['var(--S)', 'área acumulada (positiva)', 'area'], ['var(--E)', 'área acumulada (negativa)', 'area'],
    ['var(--L)', 'F(M) (solo en E 6.44)', 'linea'], ['var(--mut)', 'recta vertical discontinua: extremo móvil', 'linea'], ['var(--fg)', 'extremo móvil', 'punto']]);
  c.alCambiarTema(function (q) {
    P = q; c.renderer.setClearColor(q.bg);
    if (!ejes) return;
    ejes.userData.eje.color.set(q.fg); ejes.userData.rejilla.color.set(q.bd); curva.material.color.set(q.fg); curvaF.material.color.set(q.L);
    vert.material.color.set(q.mut); relP.material.color.set(q.S); relN.material.color.set(q.E); pt.material.color.set(q.fg); ptF.material.color.set(q.L);
  });
});
