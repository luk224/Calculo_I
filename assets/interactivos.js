/* Motor común de los ejemplos interactivos (three.js r147 local, sin CDN).
   Uso en un tema:
     <link rel="stylesheet" href="../assets/interactivos.css">
     <script defer src="../assets/interactivos.js"></script>
     <figure class="interactivo" data-escena="nombre" data-params='{"k":1}' data-estatica="../assets/img/int_nombre.png" aria-label="…">
       <figcaption>…</figcaption></figure>
   La escena vive en assets/escenas/<nombre>.js y se registra con Interactivos.registrar('nombre', function(ctx){…}).
   Nada se descarga hasta que la figura entra en pantalla. Se pinta solo cuando algo cambia. */
(function () {
  var base = (function () {
    var s = document.currentScript || document.querySelector('script[src*="interactivos.js"]');
    return s.src.replace(/interactivos\.js.*$/, '');
  })();
  var registro = {}, cargas = {};
  var reducir = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  function script(url) {
    return cargas[url] || (cargas[url] = new Promise(function (ok, ko) {
      var s = document.createElement('script'); s.src = url; s.onload = ok; s.onerror = ko; document.head.appendChild(s);
    }));
  }
  function webgl() {
    try { var c = document.createElement('canvas'); return !!(c.getContext('webgl2') || c.getContext('webgl')); } catch (e) { return false; }
  }
  function color(v) { return getComputedStyle(document.documentElement).getPropertyValue(v).trim() || '#888'; }
  function paleta() {
    return { bg: color('--bg'), fg: color('--fg'), mut: color('--mut'), acc: color('--acc'), S: color('--S'), L: color('--L'), E: color('--E'), bd: color('--bd') };
  }

  // ---- helpers de geometría ----
  var H = {
    /* Ejes x,y,z de longitud len (z hacia arriba, como en los libros). Devuelve el grupo. */
    ejes: function (THREE, len, col) {
      var g = new THREE.Group(), m = new THREE.LineBasicMaterial({ color: col });
      [[len, 0, 0], [0, len, 0], [0, 0, len]].forEach(function (p) {
        var geo = new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(-p[0], -p[1], -p[2]), new THREE.Vector3(p[0], p[1], p[2])]);
        g.add(new THREE.Line(geo, m));
      });
      g.userData.mat = m; return g;
    },
    /* Superficie z=f(x,y) en [xr]x[yr] con n×n celdas. f recibe (x,y) y devuelve z (NaN = hueco). */
    superficie: function (THREE, f, o) {
      o = o || {}; var n = o.n || 48, xr = o.xr || [-2, 2], yr = o.yr || [-2, 2], zmax = o.zmax || 6;
      var pos = [], idx = [], i, j;
      for (j = 0; j <= n; j++) for (i = 0; i <= n; i++) {
        var x = xr[0] + (xr[1] - xr[0]) * i / n, y = yr[0] + (yr[1] - yr[0]) * j / n, z = f(x, y);
        if (!isFinite(z)) z = 0; z = Math.max(-zmax, Math.min(zmax, z)); pos.push(x, y, z);
      }
      for (j = 0; j < n; j++) for (i = 0; i < n; i++) {
        var a = j * (n + 1) + i, b = a + 1, c = a + n + 1, d = c + 1; idx.push(a, b, d, a, d, c);
      }
      var geo = new THREE.BufferGeometry();
      geo.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3)); geo.setIndex(idx); geo.computeVertexNormals();
      var mat = new THREE.MeshStandardMaterial({ color: o.color || 0x4477dd, side: THREE.DoubleSide, transparent: true, opacity: o.opacity || 0.85, roughness: 0.6, metalness: 0 });
      return new THREE.Mesh(geo, mat);
    },
    /* Curva (polilínea) a partir de una lista de [x,y,z]. */
    curva: function (THREE, pts, col, w) {
      var geo = new THREE.BufferGeometry().setFromPoints(pts.map(function (p) { return new THREE.Vector3(p[0], p[1], p[2]); }));
      return new THREE.Line(geo, new THREE.LineBasicMaterial({ color: col, linewidth: w || 1 }));
    }
  };

  function montar(fig) {
    var nombre = fig.dataset.escena, params = {};
    try { params = JSON.parse(fig.dataset.params || '{}'); } catch (e) {}
    var stage = document.createElement('div'); stage.className = 'int-stage';
    var msg = document.createElement('div'); msg.className = 'int-msg'; msg.textContent = 'Cargando interactivo…'; stage.appendChild(msg);
    fig.insertBefore(stage, fig.firstChild);
    function fallo(t) { msg.textContent = t; }
    if (!webgl()) return fallo('Tu navegador no tiene WebGL: usa la imagen del libro o la versión impresa.');

    Promise.all([script(base + 'three/three.min.js')]).then(function () {
      return script(base + 'three/OrbitControls.js');
    }).then(function () { return script(base + 'escenas/' + nombre + '.js'); }).then(function () {
      var fn = registro[nombre]; if (!fn) return fallo('Escena «' + nombre + '» no registrada.');
      var THREE = window.THREE;
      var renderer = new THREE.WebGLRenderer({ antialias: true, preserveDrawingBuffer: true });
      renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
      stage.removeChild(msg); stage.appendChild(renderer.domElement);
      var scene = new THREE.Scene(), camera = new THREE.PerspectiveCamera(45, 1.6, 0.1, 200);
      camera.up.set(0, 0, 1); camera.position.set(6, -7, 5);
      var controls = new THREE.OrbitControls(camera, renderer.domElement);
      controls.enableDamping = false; controls.addEventListener('change', pedir);
      scene.add(new THREE.AmbientLight(0xffffff, 0.7));
      var luz = new THREE.DirectionalLight(0xffffff, 0.6); luz.position.set(4, -3, 8); scene.add(luz);

      var ctl = null, ro = null, temaCbs = [], visible = true, pendiente = false;
      function pedir() { if (!pendiente) { pendiente = true; requestAnimationFrame(pintar); } }
      function pintar() { pendiente = false; if (visible) renderer.render(scene, camera); }
      function ajustar() {
        var w = stage.clientWidth, h = stage.clientHeight; if (!w || !h) return;
        renderer.setSize(w, h, false); camera.aspect = w / h; camera.updateProjectionMatrix(); pedir();
      }
      var ctx = {
        el: fig, THREE: THREE, scene: scene, camera: camera, renderer: renderer, controls: controls, params: params, H: H,
        colores: paleta, reducirMovimiento: reducir, pedir: pedir,
        /* Slider accesible; cb(valor) se llama al mover y una vez al crearlo. fmt opcional para la lectura. */
        slider: function (etiqueta, min, max, paso, valor, cb, fmt) {
          if (!ctl) { ctl = document.createElement('div'); ctl.className = 'int-ctl'; stage.after(ctl); }
          var l = document.createElement('label'), o = document.createElement('output'), r = document.createElement('input');
          r.type = 'range'; r.min = min; r.max = max; r.step = paso; r.value = valor;
          fmt = fmt || function (v) { return String(Math.round(v * 100) / 100).replace('-', '−'); };
          l.appendChild(document.createTextNode(etiqueta + ' = ')); l.appendChild(o); l.appendChild(r); ctl.appendChild(l);
          function act() { var v = parseFloat(r.value); o.textContent = fmt(v); cb(v); pedir(); }
          r.addEventListener('input', act); act(); return r;
        },
        /* Lecturas numéricas bajo el lienzo: lectura('clave','Etiqueta') devuelve fn(texto). */
        lectura: function (etiqueta) {
          if (!ro) { ro = document.createElement('div'); ro.className = 'int-ro'; (ctl || stage).after(ro); }
          var d = document.createElement('div'), b = document.createElement('b');
          d.appendChild(document.createTextNode(etiqueta + ': ')); d.appendChild(b); ro.appendChild(d);
          return function (t) { b.textContent = t; };
        },
        alCambiarTema: function (cb) { temaCbs.push(cb); cb(paleta()); }
      };
      fn(ctx);
      new MutationObserver(function () { var p = paleta(); temaCbs.forEach(function (cb) { cb(p); }); pedir(); })
        .observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });
      new IntersectionObserver(function (e) { visible = e[0].isIntersecting; if (visible) pedir(); }).observe(stage);
      if (window.ResizeObserver) new ResizeObserver(ajustar).observe(stage); else window.addEventListener('resize', ajustar);
      ajustar();
    }).catch(function () { fallo('No se pudo cargar el interactivo.'); });
  }

  window.Interactivos = {
    registrar: function (nombre, fn) { registro[nombre] = fn; },
    helpers: H
  };

  function iniciar() {
    var figs = document.querySelectorAll('figure.interactivo[data-escena]'); if (!figs.length) return;
    if (!('IntersectionObserver' in window)) { [].forEach.call(figs, montar); return; }
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { io.unobserve(e.target); montar(e.target); } });
    }, { rootMargin: '200px' });
    [].forEach.call(figs, function (f) { io.observe(f); });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', iniciar); else iniciar();
})();
