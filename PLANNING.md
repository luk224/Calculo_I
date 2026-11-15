# PLANNING — Mejora pedagógica tema a tema (versión «academia»)

**Qué es:** plan para aplicar a cada tema lo hecho en el prototipo `temas/tema_2_3_lhopital.html`. Se trabaja **un tema por sesión**; al quedarte sin tokens, la sesión siguiente retoma desde el primer tema sin marcar.

**Cómo retomar (cualquier sesión, cualquier equipo):**
1. `git pull --rebase --autostash origin main`.
2. Abre este fichero, busca el primer tema con `[ ]` y lee su fila de «Notas».
3. Escribe al asistente: **«Haz el siguiente tema del PLANNING.md»** (o «Haz el tema 1.4 del PLANNING.md»).
4. Al terminar el tema: marca `[x]`, commit y `git push origin main` (CLAUDE.md §4b).

Coste orientativo del prototipo 2.3: ≈ 300-350 k tokens de subagentes (ejercicios nuevos + montaje + reestructuración). Calcula 1 tema por sesión; los temas cortos (4.x, 5.x) cuestan menos.

---

## 1. Qué se hace en cada tema (checklist de 6 fases)

Referencia viva: `temas/tema_2_3_lhopital.html` + `assets/estudio.css` + `assets/estudio.js` (compartidos; no duplicar).
**Regla dura: no se elimina ningún ejercicio (E, Propios ni Exámenes X).** Los exámenes se mantienen siempre con resolución completa y visible.

| Fase | Qué | Quién | Salida |
|---|---|---|---|
| **F1 Plan de estudio** | `div.camino` (Mínimo 🔴 / Completo 🔵 / Reto 🟣, con tiempo estimado), insignias `nv` (★ Básico, ★★ Medio, ★★★ Difícil y «Mínimo» en rojo) en el `summary` de cada ejercicio resuelto, `data-extra` en lo no esencial, `box` «En 1 minuto» bajo «La idea del tema». Mínimo para aprobar: 6-8 ejercicios imprescindibles (uno por tipo + 2-3 exámenes). | redactor-tema | cabecera del tema |
| **F2 Práctica** | 12-16 ejercicios nuevos «Ahora hazlo tú» (2 por tipo: ★ y ★★), con pista y solución, verificados con sympy; 8-10 preguntas de autoevaluación (V/F u opción) que absorben la sección de «errores típicos». | `resolutor-ejercicios` (opus) → `scratchpad/practica_X_Y.md` | md verificado |
| **F3 Mapa de decisión** | Diagrama SVG (`svg.flujo`) «¿Qué tipo de problema tengo y qué hago?» al inicio de la sección-síntesis; la tabla detallada va en `details.ver`. Si el tema no tiene decisión (p. ej. definiciones puras), sustituir por un esquema de dependencia de conceptos. | redactor-tema | SVG |
| **F4 Formato corto** | En ejercicios de E y Propios: visible enunciado + «Antes de calcular» + receta; pasos, gráfica y «Teoría:» en `details.ver`. Exámenes sin ocultar. Líneas «Mismo método que…» en repetidos. Teoría de fondo en `details.amp` con `data-extra`. | redactor-tema | tema reestructurado |
| **F5 Montaje** | Sección «Practica» única (h2) antes de «Ejercicios del libro», agrupada por tipo; autoevaluación tras ella; apartados con «Cómo lo reconoces → Qué haces → Ejemplo mínimo»; chuleta de media página; «Solo lo esencial» activado por defecto la 1.ª vez (ya lo hace `estudio.js`); renumerar h2 y comprobar enlaces. | redactor-tema | tema final |
| **F4b Estilo «academia» (importado de Álgebra, ver 2.3)** | (1) Cada ejercicio es una tarjeta `article.ejer`: cabecera con ★ + título con el origen + fuente, enunciado siempre visible, y un único `details.sol` «Ver solución paso a paso». (2) En los **exámenes**, lo primero de la solución es la caja `✍️ Así se redacta en el examen` (solución limpia, tal cual se escribiría a mano, verificada con sympy) y el resto va en `details.ampl` «Comentarios y comprobaciones». (3) La fila «Qué uso» de «Antes de calcular» es una línea: resultado + fórmula + `ver teoría` (enlace `#`) + (U p.NN). | redactor-tema | tema con tarjetas |
| **F6 Verificación y cierre** | Conteos antes/después de `details.sol` (no baja), `details.pr`, `.q`; exámenes presentes; ids únicos; enlaces `#` válidos; JSON `data-g` válidos; `\lim` con subíndice; sin menciones a erratas; palabras visibles en modo esencial (objetivo ≈ 2.500 de contenido). Commit y push. | coordinador | commit |

**Ideas aprobadas, pendientes de aplicar** (importadas de Álgebra/Física, ver registro): pestañas Teoría / Por tipo / Ejercicios / Examen y botón «Mostrar fuentes» (de `ALGEBRA/claude/assets/pedagogia.js`); pregunta motivadora antes de cada apartado; series de práctica generadas al azar con diagnóstico del error (de `practica.js`), empezando por límites, derivadas e integrales; test de integridad del sitio (recuentos de ejercicios/exámenes, enlaces, JSON de las gráficas); y, de Física, problemas gemelos y mini-examen de cierre.

Si se hace en una sola orden al asistente, el flujo recomendado es: **F2 (resolutor) → F1+F3+F4+F5 (un redactor con las instrucciones del 2.3 como modelo) → F6**.

### Plantilla de petición (copiar/pegar)
> Haz el tema X.Y del PLANNING.md: aplica F1-F6 siguiendo `temas/tema_2_3_lhopital.html` como modelo. No elimines ningún ejercicio. Primero el resolutor genera la práctica y el quiz (verificados con sympy), después el redactor monta el tema. Cuando termine: verificación, commit y push.

---

## 2. Estado y orden de trabajo

Orden = orden del cronograma de estudio (CLAUDE.md §2). `[x]` hecho · `[ ]` pendiente.

| ✓ | Tema | Ejercicios (v. CLAUDE.md §2) | Notas para este tema |
|---|---|---|---|
| [x] | **2.3 L'Hôpital** | E 2.24-2.33 + 6 X | **Prototipo hecho** (commits 08cff4c, 616e4bd, a870fc6; F4b: tarjetas, redacción de examen y «Qué uso» corto). Modelo de referencia. |
| [ ] | 1.1 El espacio ℝ | E 1.1-1.5 + X | Mapa: «qué desigualdad/valor absoluto tengo y qué método». Práctica: desigualdades, intervalos, supremo/ínfimo. Ojo: máx/mín/arquimediana son `P` (no U). |
| [ ] | 1.2 Sucesiones | E 1.6-1.16 + X | Mapa de decisión de límites de sucesiones (cociente de polinomios, e, Stolz, acotación, monotonía). **Tema largo: dividir F4 con cuidado.** |
| [ ] | 1.3 Series | E 1.17-1.22 + X | Mapa de criterios de convergencia (necesaria, comparación, cociente, raíz, alternada, geométrica, telescópica). |
| [ ] | 1.4 Límites y continuidad | E 1.23-1.41 + X | **Mayor volumen (40 `details.sol`)**: agrupar por tipo (límites, asíntotas, continuidad, Bolzano/bisección) y hacer F4 estricto. Dos o tres sesiones si hace falta: (a) límites, (b) continuidad+Bolzano. |
| [ ] | 2.1 Derivada | E 2.1,2.2,2.6-2.9,2.14,2.17-2.23 + X | Mapa: ¿derivable en el punto? (definición, laterales, continuidad). |
| [ ] | 2.2 Reglas de derivación | E 2.3-2.5,2.10-2.13,2.15,2.16 + X | Mapa: qué regla uso (producto, cociente, cadena, inversa, logarítmica). Práctica de derivación rápida. |
| [ ] | 2.4 Newton y punto fijo | E 2.34-2.38 + X | Mapa: ¿Newton o punto fijo?, condiciones de convergencia, cota de error. |
| [ ] | 2.5 Rolle, valor medio, monotonía | E 2.39-2.51 + X | Mapa: ¿cuántas raíces? / ¿qué teorema aplico? (Rolle, TVM, Bolzano). 2.50-2.51 requieren 3.4-3.5: marcar. |
| [ ] | 3.1 Taylor | E 3.1-3.14 + X | Mapa: orden y resto (Lagrange/Peano), desarrollos conocidos, estimación de error. |
| [ ] | 3.2 Series de Taylor | E 3.18-3.20 + X | Solo series de Taylor/analíticas son examen; el resto ya va en `details.fuera`. |
| [ ] | 3.3 Interpolación | E 3.21-3.28 + X | Ya tiene `graf` y tabla `dd`. Mapa: ¿Newton/Lagrange/cota de error? |
| [ ] | 3.4 Optimización y extremos | E 3.29-3.48 + X | Mapa: pasos para hallar extremos absolutos en intervalo cerrado / problema de optimización. |
| [ ] | 3.5 Concavidad y convexidad | E 3.39-3.48 + X | Mapa de gráfica de una función (dominio, asíntotas, crecimiento, extremos, concavidad). |
| [ ] | 4.1 Espacio ℝⁿ | E 4.x + X | Menos ejercicios de cálculo: priorizar conceptos y práctica corta. Sin `graf` (3D/interactivos). |
| [ ] | 4.2 Funciones de varias variables | E 4.x + X | Mapa: ¿existe el límite? (trayectorias, polares, acotación). |
| [ ] | 4.3 Derivadas parciales | E 4.x + X | Mapa: ¿diferenciable? (parciales continuas ⇒ sí; definición). |
| [ ] | 5.1 Diferencial | E 5.x + X | Menos gráficas 1D; mantener interactivos. |
| [ ] | 5.2 Regla de la cadena y TVM | E 5.x + X | Mapa: árbol de dependencias de variables (dibujo). |
| [ ] | 5.3 Función implícita | E 5.x + X | Mapa: ¿se puede despejar? (condición del Jacobiano/derivada). |
| [ ] | 5.4-5.5 Extremos y Lagrange | E 5.x + X | Mapa: libre / con ligaduras / en compacto. |
| [ ] | 6.1 Integral de Riemann | E 6.x + X | Mapa: ¿integrable? (continua, monótona, acotada con pocas discontinuidades). |
| [ ] | 6.2 Teoremas fundamentales | E 6.x + X | Mapa: ¿derivada de una integral con límites variables? (regla de Leibniz/TFC). |
| [ ] | 6.3 Cálculo de integrales | E 6.x + X | **Mapa clave:** qué técnica (inmediata, partes, sustitución, racionales, trigonométricas). |
| [ ] | 6.4 Integración numérica | E 6.x + X | Mapa: trapecio vs. Simpson, nº de subintervalos para un error dado. |
| [ ] | 6.5 Integrales impropias | E 6.x + X | Mapa: tipo (infinito/discontinuidad), comparación, convergencia absoluta. |

**Progreso:** 1 de 25 temas.

---

## 2b. Piezas globales (aprobadas el 2026-11-15; estilo Álgebra)

Se hacen **una sola vez** y conviene tenerlas pronto, porque deciden en qué orden se estudia y qué se hace primero.

| ✓ | Pieza | Qué es (modelo en `ALGEBRA/claude`) | Cómo hacerla aquí |
|---|---|---|---|
| [ ] | **G1. Página `prioridades.html`** | «¿Por dónde empiezo?»: cuánto cae cada tema en los exámenes (nº de ejercicios de X por tema) frente a cuánto cuesta (horas del camino mínimo). Tres rutas: **Imprescindible / Recomendada / Completa**, con las dependencias entre temas y las horas totales de cada ruta. | Datos: `fuentes_txt/indice_examenes_*.md` (preguntas de X por tema) + horas de la cabecera de cada tema. Un script `herramientas/prioridades.py` genera la página (modelo: `ALGEBRA/claude/herramientas/prioridades.py`) y un `datos/dependencias.json` con el orden y las dependencias. Enlazarla desde `index.html`. |
| [ ] | **G2. Página `ruta.html`** | Calendario hacia atrás desde las PA y la PEC (CLAUDE.md §2) según las horas semanales que tengas. | Modelo: `ALGEBRA/claude/herramientas/ruta.py`. |
| [ ] | **G3. «Exámenes arriba» y vistas por pestañas** | Dentro de cada tema: pestañas **Todo / Teoría / Por tipo / Ejercicios / Examen**, cada `h2` con `data-vista`; al elegir «Examen» se ven primero los problemas reales (redacción ✍️). Caja «Qué cae en el examen» al principio (tabla tipo de pregunta → receta → ejercicios enlazados). Botón «Mostrar fuentes» (ocultas por defecto). | Reutilizar `ALGEBRA/claude/assets/pedagogia.js|css` dentro de `assets/estudio.*`. Probar primero en el 2.3 y luego incluirlo en F5 de cada tema. |
| [ ] | **G4. «Lo esencial en 5 minutos» como bloque fijo** | Caja al inicio de cada tema (método en 4 pasos, fórmulas con su «cuándo se usa», qué cae). Sustituye al «En 1 minuto» actual del 2.3. | Parte de F1; usar el formato de `ALGEBRA/claude/temas/tema_2_3_*.html` (`div.box.esencial`). |
| [ ] | **G5. Test de integridad del sitio** | Que nunca baje el nº de ejercicios/exámenes, que los enlaces `#` y los JSON de gráficas sean válidos y que no haya `\lim` sin subíndice. | `herramientas/tests_sitio.py` (modelo: Álgebra/Física). |

**Orden recomendado:** G3 (probar en el 2.3) → G1 (prioridades, para decidir el orden de los demás temas) → G4 → resto de temas (F1-F6) → G2 → G5.

## 3. Antes de dar el producto por final (una vez hecho todo)

- [ ] Revisión visual con navegador real a 320 / 390 / 1280 px (sin scroll horizontal, tablas, SVG de mapas, interruptor «Solo lo esencial», casillas «hecho», quiz).
- [ ] Revisar en `index.html` que cada tarjeta muestre el estado y el tiempo estimado del camino mínimo.
- [ ] Generar los PDF (B/N y color) y comprobar que los desplegables salen abiertos y las ampliaciones se ven.
- [ ] Prueba con un estudiante que no conozca el tema (30 min por tema): anotar dónde se pierde.
- [ ] Segunda pasada de verificación de enunciados contra los libros en los temas con más ejercicios (1.4, 3.4, 6.3).

## 4. Registro de sesiones

| Fecha | Tema | Resultado | Commit |
|---|---|---|---|
| 2026-11-14 | Gráficas con coordenadas en 1.1-6.5 | 298 gráficas | 7502f1a |
| 2026-11-14 | 2.3 prototipo «academia» | F1-F6 hechas | 08cff4c, 616e4bd |
| 2026-11-15 | 2.3 estilo Álgebra (F4b) | tarjetas, ✍️ redacción en los 6 exámenes, «Qué uso» corto | ver `git log` |
