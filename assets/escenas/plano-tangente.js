/* Plano tangente y diferenciabilidad (tema 5.1): al reducir la ventana, la superficie se confunde con el plano
   si f es diferenciable; si no lo es, no. */
Interactivos.registrar('plano-tangente', function (c) {
  var T = c.THREE, H = c.H;
  var q = function (x, y) { var s = x * x + y * y; return s; };
  var F = [
    { n: 'x² + y²', f: function (x, y) { return x * x + y * y; }, g: function (x, y) { return [2 * x, 2 * y]; }, a: 1, b: 0.5 },
    { n: 'x² − y² (silla)', f: function (x, y) { return x * x - y * y; }, g: function (x, y) { return [2 * x, -2 * y]; }, a: 0.8, b: 0.4 },
    { n: 'sen x · cos y', f: function (x, y) { return Math.sin(x) * Math.cos(y); }, g: function (x, y) { return [Math.cos(x) * Math.cos(y), -Math.sin(x) * Math.sin(y)]; }, a: 0.7, b: 0.5 },
    { n: 'xy/(x²+y²) con f(0,0)=0 (NO diferenciable en (0,0))', f: function (x, y) { return q(x, y) === 0 ? 0 : x * y / q(x, y); },
      g: function (x, y) { var s = q(x, y); return s === 0 ? [0, 0] : [y * (y * y - x * x) / (s * s), x * (x * x - y * y) / (s * s)]; }, a: 0, b: 0 }
  ];
  var k = 0, a = 1, b = 0.5, s = 0, P = c.colores(), malla = null, plano = null, pt = null, dir = new T.Vector3(1.2, -1.5, 1).normalize();
  var l1 = c.lectura('∇f(a, b)'), l2 = c.lectura('Error máximo en la ventana'), l3 = c.lectura('Error máximo / tamaño w'), lv = c.lectura('');
  function fm(t) { return (Math.round(t * 10000) / 10000).toString().replace('-', '−'); }
  function limpia(o) { if (o) { c.scene.remove(o); if (o.geometry) o.geometry.dispose(); } }
  function ventana() {
    var g = F[k], w = 2 * Math.pow(10, -s), fa = g.f(a, b), gr = g.g(a, b), i, j, emax = 0;
    var pl = function (x, y) { return fa + gr[0] * (x - a) + gr[1] * (y - b); };
    limpia(malla); limpia(plano); limpia(pt);
    malla = H.superficie(T, g.f, { n: 40, xr: [a - w, a + w], yr: [b - w, b + w], zmax: 1e6, opacity: 0.9, color: P.acc });
    plano = H.superficie(T, pl, { n: 1, xr: [a - w, a + w], yr: [b - w, b + w], zmax: 1e6, opacity: 0.45, color: P.S });
    plano.material.depthWrite = false; c.scene.add(malla, plano);
    var dist = 0.8 + 6 * w / 2, tgt = new T.Vector3(a, b, fa);
    pt = new T.Mesh(new T.SphereGeometry(0.012 * dist, 14, 10), new T.MeshBasicMaterial({ color: P.fg })); pt.position.copy(tgt); c.scene.add(pt);
    var off = c.camera.position.clone().sub(c.controls.target); if (off.length() > 1e-6) dir.copy(off).normalize();
    c.controls.target.copy(tgt); c.camera.position.copy(tgt).addScaledVector(dir, dist); c.controls.update();
    for (i = 0; i <= 20; i++) for (j = 0; j <= 20; j++) { var x = a - w + 2 * w * i / 20, y = b - w + 2 * w * j / 20; emax = Math.max(emax, Math.abs(g.f(x, y) - pl(x, y))); }
    l1('(' + fm(gr[0]) + ', ' + fm(gr[1]) + ')'); l2(fm(emax)); l3(fm(emax / w));
    lv(k === 3 && a === 0 && b === 0 ? 'En (0,0) existen las parciales (valen 0) pero el error/w NO tiende a 0: f no es diferenciable ahí y el plano z = 0 no aproxima.' :
       'Al reducir w el cociente error/w tiende a 0: f es diferenciable aquí y el plano tangente aproxima a f.');
  }
  var sa = c.slider('a', -2, 2, 0.05, a, function (v) { a = v; if (pt) ventana(); });
  var sb = c.slider('b', -2, 2, 0.05, b, function (v) { b = v; if (pt) ventana(); });
  c.slider('Ventana (zoom hacia el punto)', 0, 2.5, 0.01, s, function (v) { s = v; if (pt) ventana(); }, function (v) { return 'w = ' + fm(2 * Math.pow(10, -v)); });
  c.selector('Función ', F.map(function (g) { return g.n; }), 0, function (i) {
    k = i; sa.value = F[i].a; sb.value = F[i].b; a = F[i].a; b = F[i].b; sa.dispatchEvent(new Event('input')); sb.dispatchEvent(new Event('input'));
  });
  ventana();
  c.leyenda([['var(--acc)','superficie z = f(x, y)','area'],['var(--S)','plano tangente','area'],['var(--fg)','punto (a, b)','punto']]);
  c.alCambiarTema(function (qq) {
    P = qq; c.renderer.setClearColor(qq.bg);
    if (!pt) return;
    malla.material.color.set(qq.acc); plano.material.color.set(qq.S); pt.material.color.set(qq.fg);
  });
});
