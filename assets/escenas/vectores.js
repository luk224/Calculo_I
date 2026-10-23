/* Producto escalar, norma y ángulo en R³ (tema 4.1): dos vectores con sliders, proyección de u sobre v. */
Interactivos.registrar('vectores', function (c) {
  var T = c.THREE, H = c.H;
  var u = [2, 1, 1], v = [1, 2, 0], P = c.colores(), r = 0.08;
  var rejilla, ejes, fu, fv, proy, arco, pt;
  var l1 = c.lectura('u · v'), l2 = c.lectura('‖u‖  ,  ‖v‖'), l3 = c.lectura('Ángulo α entre u y v'), l4 = c.lectura('Proyección de u sobre v (con signo)'), l5 = c.lectura('');
  function fm(t) { return (Math.round(t * 1000) / 1000).toString().replace('-', '−'); }
  function limpia(o) { if (o) { c.scene.remove(o); if (o.geometry) o.geometry.dispose(); } }
  function nuevo() {
    rejilla = new T.GridHelper(8, 8, P.mut, P.bd); rejilla.rotation.x = Math.PI / 2; c.scene.add(rejilla);
    ejes = H.ejes(T, 4, P.mut); c.scene.add(ejes);
    fu = H.flecha(T, P.S, r); fv = H.flecha(T, P.acc, r); c.scene.add(fu, fv);
    proy = H.tubo(T, [], r * 0.7, P.L); arco = H.tubo(T, [], r * 0.5, P.fg); c.scene.add(proy, arco);
    c.camera.position.set(-5, 3, 8); c.controls.target.set(0, 0, 0); c.controls.update();
  }
  function calc() {
    var uv = u[0] * v[0] + u[1] * v[1] + u[2] * v[2], nu = Math.hypot(u[0], u[1], u[2]), nv = Math.hypot(v[0], v[1], v[2]);
    fu.poner([0, 0, 0], u); fv.poner([0, 0, 0], v);
    if (nv > 1e-9) { var k = uv / (nv * nv); proy.set(Math.abs(k) * nv > 1e-6 ? [[0, 0, 0], [k * v[0], k * v[1], k * v[2]]] : []); } else proy.set([]);
    // arco del ángulo en el plano de u y v (radio 0,8)
    var pts = [];
    if (nu > 1e-9 && nv > 1e-9) {
      var cs = Math.max(-1, Math.min(1, uv / (nu * nv))), al = Math.acos(cs), eu = u.map(function (x) { return x / nu; });
      var w = [v[0] / nv - cs * eu[0], v[1] / nv - cs * eu[1], v[2] / nv - cs * eu[2]], nw = Math.hypot(w[0], w[1], w[2]);
      if (nw > 1e-9) { w = w.map(function (x) { return x / nw; }); for (var i = 0; i <= 24; i++) { var t = al * i / 24; pts.push([0.8 * (Math.cos(t) * eu[0] + Math.sin(t) * w[0]), 0.8 * (Math.cos(t) * eu[1] + Math.sin(t) * w[1]), 0.8 * (Math.cos(t) * eu[2] + Math.sin(t) * w[2])]); } }
      l3(fm(al * 180 / Math.PI) + '°   (cos α = ' + fm(cs) + ')');
    } else l3('no definido (algún vector es nulo)');
    arco.set(pts);
    l1(fm(uv)); l2(fm(nu) + '  ,  ' + fm(nv)); l4(nv > 1e-9 ? fm(uv / nv) : '—');
    l5(Math.abs(uv) < 0.03 && nu > 1e-9 && nv > 1e-9 ? 'u · v ≈ 0: los vectores son ortogonales (α = 90°)' : '');
  }
  nuevo();
  ['x', 'y', 'z'].forEach(function (nom, i) { c.slider('u' + nom, -3, 3, 0.1, u[i], function (a) { u[i] = a; if (arco) calc(); }); });
  ['x', 'y', 'z'].forEach(function (nom, i) { c.slider('v' + nom, -3, 3, 0.1, v[i], function (a) { v[i] = a; if (arco) calc(); }); });
  c.alCambiarTema(function (q) {
    P = q; c.renderer.setClearColor(q.bg);
    if (!arco) return;
    limpia(rejilla); rejilla = new T.GridHelper(8, 8, q.mut, q.bd); rejilla.rotation.x = Math.PI / 2; c.scene.add(rejilla);
    ejes.userData.mat.color.set(q.mut); proy.material.color.set(q.L); arco.material.color.set(q.fg);
    [[fu, q.S], [fv, q.acc]].forEach(function (e) { e[0].userData.eje.material.color.set(e[1]); e[0].userData.cono.material.color.set(e[1]); });
  });
});
