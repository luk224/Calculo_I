---
name: resumen-calculo
description: Crea o revisa el resumen HTML de una sección del temario de Cálculo (UNED) — p.ej. "tema 1.2" — con explicaciones para principiantes, ejercicios resueltos del libro de ejercicios y fuentes (libro+página) visibles. Úsalo cuando el usuario pida un tema, resumen o sección concreta de la asignatura.
---

# Skill: resumen de tema de Cálculo

Lee primero `CLAUDE.md` (fuentes, offsets de página, cronograma, reglas de contenido). Este skill solo fija el **procedimiento**.

## Procedimiento
1. **Identificar la sección** (ej. 1.2 Sucesiones) y su rango de páginas en U (`CLAUDE.md` §2), los ejercicios de E que le corresponden (mapear por enunciado; el cronograma llega hasta E p.41 en el Tema 1) y los apartados equivalentes en S y L.
2. **Dossier de fuentes**: lanzar `fuentes-calculo` (haiku) con el tema. Debe devolver extractos con página impresa por libro y los enunciados/soluciones de E.
3. **Ejercicios**: lanzar `resolutor-ejercicios` (opus) con la lista de ejercicios; en paralelo con el paso 4 si el dossier ya está.
4. **Redacción**: `redactor-tema` (sonnet) copia `plantilla_tema.html` a `temas/tema_X_Y_<slug>.html` y lo rellena siguiendo las reglas de contenido (CLAUDE.md §3). Usa solo `assets/resumen.css|js` y KaTeX local, sin dependencias externas.
5. **Revisión**: `revisor-tema` (opus) comprueba matemáticas, citas, cobertura y render. Aplicar sus correcciones.
6. **Cierre**: actualizar `index.html`, comprobar visualmente el HTML (Claude in Chrome o captura) en ancho de escritorio y móvil, y resumir al usuario qué hay y qué falta.

## Convenciones de marcado (resumen)
- Cajas: `.box.def|thm|ex|warn|tip|intu` con `<span class="h">Título</span>`; receta: `.recipe`; pasos: `ol.steps`; ejercicio: `details.sol > summary + .enun + …`.
- Fuente: `<span class="src" data-l="U|S|L|E|P" data-ref="Libro §sección, p. N">U p.N</span>`. Colocarlo **como hijo directo** del `.box`, `h2`, `h3` o `summary` para que salga en el margen derecho en escritorio.
- Encabezados `h2` con `id` único (alimentan el índice lateral). Fórmulas: `$…$` y `$$…$$`.
- Figuras: `<figure><svg class="fig" viewBox=…>…</svg><figcaption>…</figcaption></figure>` con clases `.ax .a .b .pt .op`.

## Calidad
- Nada de página inventada: verificar en `fuentes_txt/`.
- Cada ejercicio termina con una **receta** reutilizable y, si procede, el error típico.
- Skills de diseño para el pulido: `frontend-design:frontend-design`, `carattere`, `componi`, `scrutinio`, `lucida`.
