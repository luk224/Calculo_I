/* Radio de convergencia (tema 3.2): sumas parciales de series de Maclaurin frente a la función. */
Interactivos.registrar('radio-convergencia', function (c) {
  var T = c.THREE, H = c.H;
  var W = function (v) { var dx = 1.5 * (v[1] - v[0]), dy = 1.5 * (v[3] - v[2]); return [v[0] - dx, v[1] + dx, v[2] - dy, v[3] + dy]; };
  var fact = function (j) { var f = 1; for (var i = 2; i <= j; i++) f *= i; return f; };
  var F = [
    { n: '1/(1 + x²) = 1 − x² + x⁴ − …', f: function (x) { return 1 / (1 + x * x); }, a: function (j) { return j % 2 ? 0 : (j / 2 % 2 ? -1 : 1); }, R: 1, v: [-3, 3, -1.5, 2], rx: [-3, 3, 0.8] },
    { n: '1/(1 − x) = 1 + x + x² + …', f: function (x) { return 1 / (1 - x); }, a: function () { return 1; }, R: 1, v: [-3, 3, -3, 5], rx: [-3, 3, 0.8] },
    { n: 'ln(1 + x) = x − x²/2 + x³/3 − …', f: function (x) { return Math.log(1 + x); }, a: function (j) { return j ? (j % 2 ? 1 : -1) / j : 0; }, R: 1, v: [-1.5, 3.5, -3, 2.5], rx: [-0.95, 3.5, 0.8] },
    { n: 'eˣ = 1 + x + x²/2! + …', f: Math.exp, a: function (j) { return 1 / fact(j); }, R: Infinity, v: [-4, 4, -2, 8], rx: [-4, 4, 2] },
    { n: 'sen x = x − x³/3! + x⁵/5! − …', f: Math.sin, a: function (j) { return j % 2 ? ((j - 1) / 2 % 2 ? -1 : 1) / fact(j) : 0; }, R: Infinity, v: [-7, 7, -3, 3], rx: [-7, 7, 3] }
  ];
  var k = 0, N = 6, x0 = 0.8, P = c.colores(), w, vw, co = [], ejes, curva, suma, lim, seg, pf, ps;
  var l1 = c.lectura('f(x)'), l2 = c.lectura('Sₙ(x)'), lr = c.lectura('R'), lv = c.lectura('');
  var fm = function (t) { return (Math.round(t * 1e5) / 1e5).toString().replace('-', '−'); };
  function S(t) { var s = 0, j; for (j = N; j >= 0; j--) s = s * t + co[j]; return s; }

  function nuevo() {
    [ejes, curva, suma, lim, seg, pf, ps].forEach(function (o) { if (o) c.scene.remove(o); });
    var g = F[k], v = g.v; w = 0.0055 * (v[3] - v[2]); c.vista(v[0], v[1], v[2], v[3]); vw = W(v);
    co = []; for (var j = 0; j <= 60; j++) co.push(g.a(j));
    ejes = H.ejes2D(T, vw, w, P.fg, P.bd); c.scene.add(ejes);
    curva = H.cinta(T, H.grafica(g.f, vw[0], vw[1], 1600, 1e3), P.mut, w * 1.2, [w * 5, w * 3]); curva.position.z = 0.1; c.scene.add(curva);
    lim = H.cinta(T, g.R === Infinity ? [] : [[[-g.R, vw[2]], [-g.R, vw[3]]], [[g.R, vw[2]], [g.R, vw[3]]]], P.L, w * 1.1, [w * 6, w * 4]); lim.position.z = 0.15; c.scene.add(lim);
    suma = H.cinta(T, [], P.S, w * 1.4); suma.position.z = 0.2; c.scene.add(suma);
    seg = H.cinta(T, [], P.acc, w * 1.4); seg.position.z = 0.3; c.scene.add(seg);
    pf = H.punto(T, 0, 0, w * 2.2, P.fg); ps = H.punto(T, 0, 0, w * 2.2, P.S); pf.position.z = 0.5; ps.position.z = 0.5; c.scene.add(pf, ps);
  }
  function calc() {
    var g = F[k], fx = g.f(x0), sx = S(x0), d = Math.abs(x0);
    suma.set(H.grafica(S, vw[0], vw[1], 1600, 1e3));
    pf.mover(x0, fx); ps.mover(x0, sx); seg.set(isFinite(fx) && Math.abs(fx - sx) < 1e3 && Math.abs(sx) < 1e3 ? [[[x0, fx], [x0, sx]]] : []);
    l1(fm(fx)); l2(Math.abs(sx) > 1e6 ? 'enorme (' + (sx > 0 ? '+' : '−') + '10⁶ o más)' : fm(sx));
    lr(g.R === Infinity ? '∞ (converge para todo x)' : '1  (converge en |x| < 1)');
    lv(g.R === Infinity ? 'x dentro del intervalo de convergencia: las sumas parciales se acercan a f(x)' :
       Math.abs(d - g.R) < 0.03 ? 'x en un extremo del intervalo: hay que estudiar la serie numérica a mano' :
       d < g.R ? 'x dentro de (−R, R): al subir N, Sₙ(x) se acerca a f(x)' : 'x fuera de [−R, R]: al subir N, Sₙ(x) se aleja de f(x) (la serie diverge)');
  }
  var sx = c.slider('Punto x', -3, 3, 0.01, x0, function (v) { x0 = v; if (suma) calc(); });
  c.slider('Grado N de la suma parcial', 0, 40, 1, N, function (v) { N = v; if (suma) calc(); }, function (v) { return String(v); });
  c.selector('Serie ', F.map(function (g) { return g.n; }), 0, function (i) {
    k = i; nuevo(); sx.min = F[i].rx[0]; sx.max = F[i].rx[1]; sx.value = F[i].rx[2]; sx.dispatchEvent(new Event('input'));
  });
  c.alCambiarTema(function (q) {
    P = q; c.renderer.setClearColor(q.bg);
    if (!ejes) return;
    ejes.userData.eje.color.set(q.fg); ejes.userData.rejilla.color.set(q.bd); curva.material.color.set(q.mut);
    lim.material.color.set(q.L); suma.material.color.set(q.S); seg.material.color.set(q.acc); pf.material.color.set(q.fg); ps.material.color.set(q.S);
  });
});
