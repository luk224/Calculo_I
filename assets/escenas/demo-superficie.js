/* Escena de prueba de la infraestructura: z = a·(x²+y²) con un slider para a. */
Interactivos.registrar('demo-superficie', function (c) {
  var THREE = c.THREE, malla = null, ejes;
  ejes = c.H.ejes(THREE, 3, 0x888888); c.scene.add(ejes);
  c.alCambiarTema(function (p) { ejes.userData.mat.color.set(p.mut); c.renderer.setClearColor(p.bg); });
  var lee = c.lectura('f(1, 1)');
  c.slider('a', -1, 1, 0.05, 0.5, function (a) {
    if (malla) { c.scene.remove(malla); malla.geometry.dispose(); }
    malla = c.H.superficie(THREE, function (x, y) { return a * (x * x + y * y); }, { xr: [-2, 2], yr: [-2, 2], zmax: 5 });
    c.scene.add(malla); lee(String(Math.round(2 * a * 100) / 100).replace('-', '−'));
  });
});
