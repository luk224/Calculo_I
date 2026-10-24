/* Coordenadas polares, cilíndricas y esféricas (tema 4.1; convención de U: φ se mide desde el plano xy). */
Interactivos.registrar('coordenadas', function (c) {
  var T = c.THREE, H = c.H, D = Math.PI / 180;
  var modo = 2, rho = 2, th = 40, z = 1, ph = 30, P = c.colores(), r = 0.045;
  var rejilla, ejes, lRho, lRad, lVert, aTh, aPh, pt, pxy, lx, ly;
  var l1 = c.lectura('(x, y, z)'), l2 = c.lectura(''), l3 = c.lectura('Fórmulas');
  function fm(t) { return (Math.round(t * 1000) / 1000).toString().replace('-', '−'); }
  function limpia(o) { if (o) { c.scene.remove(o); if (o.geometry) o.geometry.dispose(); } }
  function arco(R, a0, a1, f) { var pts = [], i, n = 30; for (i = 0; i <= n; i++) pts.push(f(R, a0 + (a1 - a0) * i / n)); return pts; }
  function nuevo() {
    rejilla = new T.GridHelper(8, 8, P.mut, P.bd); rejilla.rotation.x = Math.PI / 2; c.scene.add(rejilla);
    ejes = H.ejes(T, 3.6, P.mut); c.scene.add(ejes);
    lRho = H.tubo(T, [], r * 1.3, P.S); lRad = H.tubo(T, [], r, P.S); lVert = H.tubo(T, [], r, P.L);
    aTh = H.tubo(T, [], r * 0.8, P.fg); aPh = H.tubo(T, [], r * 0.8, P.L);
    lx = H.tubo(T, [], r * 0.5, P.mut); ly = H.tubo(T, [], r * 0.5, P.mut);
    pt = new T.Mesh(new T.SphereGeometry(r * 3, 18, 14), new T.MeshBasicMaterial({ color: P.fg }));
    pxy = new T.Mesh(new T.SphereGeometry(r * 2, 14, 10), new T.MeshBasicMaterial({ color: P.mut }));
    c.scene.add(lRho, lRad, lVert, aTh, aPh, lx, ly, pt, pxy);
    c.camera.position.set(4.2, -5.4, 4); c.controls.target.set(0, 0, 0.4); c.controls.update();
  }
  function calc() {
    var t = th * D, f = ph * D, x, y, zz, rad;
    if (modo === 0) { x = rho * Math.cos(t); y = rho * Math.sin(t); zz = 0; rad = rho; }
    else if (modo === 1) { x = rho * Math.cos(t); y = rho * Math.sin(t); zz = z; rad = rho; }
    else { x = rho * Math.cos(f) * Math.cos(t); y = rho * Math.cos(f) * Math.sin(t); zz = rho * Math.sin(f); rad = rho * Math.cos(f); }
    var O = [0, 0, 0], Pp = [x, y, zz], Pxy = [x, y, 0];
    pt.position.set(x, y, zz); pxy.position.set(x, y, 0); pxy.visible = modo !== 0;
    lRho.set(modo === 2 ? [O, Pp] : []);                       // ρ al origen (esféricas)
    lRad.set(modo === 2 ? [O, Pxy] : [O, Pxy]);                // proyección / ρ en polares y cilíndricas
    lVert.set(modo === 0 ? [] : [Pxy, Pp]);
    lx.set(modo === 0 ? [[x, 0, 0], Pxy] : []); ly.set(modo === 0 ? [[0, y, 0], Pxy] : []);
    var R = Math.min(0.9, Math.max(0.25, rad * 0.45));
    aTh.set(rad > 1e-6 ? arco(R, 0, t, function (R_, a) { return [R_ * Math.cos(a), R_ * Math.sin(a), 0]; }) : []);
    var Rp = Math.min(1, Math.max(0.3, rho * 0.4)), ux = Math.cos(t), uy = Math.sin(t);
    aPh.set(modo === 2 && Math.abs(f) > 1e-3 ? arco(Rp, 0, f, function (R_, a) { return [R_ * Math.cos(a) * ux, R_ * Math.cos(a) * uy, R_ * Math.sin(a)]; }) : []);
    l1('(' + fm(x) + ', ' + fm(y) + ', ' + fm(zz) + ')');
    l2(modo === 0 ? 'Polares: ρ = ' + fm(rho) + ', θ = ' + fm(th) + '°   (la distancia ρ al origen se ve en naranja)' :
       modo === 1 ? 'Cilíndricas: ρ = ' + fm(rho) + ' (distancia al eje z), θ = ' + fm(th) + '°, z = ' + fm(z) :
       'Esféricas: ρ = ' + fm(rho) + ' (distancia al origen), θ = ' + fm(th) + '°, φ = ' + fm(ph) + '° (medido desde el plano xy)');
    l3(modo === 0 ? 'x = ρ cos θ,  y = ρ sen θ' : modo === 1 ? 'x = ρ cos θ,  y = ρ sen θ,  z = z' : 'x = ρ cos φ cos θ,  y = ρ cos φ sen θ,  z = ρ sen φ');
  }
  nuevo();
  c.slider('ρ', 0.2, 3, 0.05, rho, function (v) { rho = v; if (pt) calc(); });
  c.slider('θ', 0, 360, 1, th, function (v) { th = v; if (pt) calc(); }, function (v) { return v + '°'; });
  c.slider('z (cilíndricas)', -2, 2, 0.05, z, function (v) { z = v; if (pt) calc(); });
  c.slider('φ (esféricas)', -90, 90, 1, ph, function (v) { ph = v; if (pt) calc(); }, function (v) { return v + '°'; });
  c.selector('Sistema ', ['Polares (plano xy)', 'Cilíndricas (ρ, θ, z)', 'Esféricas (ρ, θ, φ)'], 2, function (i) { modo = i; if (pt) calc(); });
  c.leyenda([['var(--fg)','punto P; ángulo θ','punto'],['var(--S)','distancia al origen (r o ρ)','linea'],['var(--L)','altura z; ángulo φ (esféricas)','linea'],['var(--mut)','proyección en el plano xy; coordenadas x, y','linea']]);
  c.alCambiarTema(function (q) {
    P = q; c.renderer.setClearColor(q.bg);
    if (!pt) return;
    limpia(rejilla); rejilla = new T.GridHelper(8, 8, q.mut, q.bd); rejilla.rotation.x = Math.PI / 2; c.scene.add(rejilla);
    ejes.userData.mat.color.set(q.mut);
    lRho.material.color.set(q.S); lRad.material.color.set(q.S); lVert.material.color.set(q.L); aTh.material.color.set(q.fg); aPh.material.color.set(q.L);
    lx.material.color.set(q.mut); ly.material.color.set(q.mut); pt.material.color.set(q.fg); pxy.material.color.set(q.mut);
  });
});
