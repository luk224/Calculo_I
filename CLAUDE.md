# CLAUDE.md — Cálculo (UNED, Grado Ingeniería Industrial, curso 2026-27)

**Objetivo del proyecto:** que el usuario apruebe la asignatura y sepa resolver los ejercicios del libro de ejercicios.
**Producto principal:** un resumen HTML por cada tema/sección (`temas/tema_X_Y_nombre.html`), pensado para alguien que lo estudia **por primera vez**, con ejercicios resueltos y **la fuente (libro + página/capítulo) visible en lateral o al pasar el ratón**.

Idioma: **español** (todo el contenido, comentarios y comunicación con el usuario).

## 1. Fuentes (carpeta padre `E:\UNED\CALCULO\`)

| Clave | Libro | PDF | Texto extraído (`fuentes_txt/`) | Uso |
|---|---|---|---|---|
| **U** | *Cálculo para Ingenieros* — Franco, Gil, Ruiz (UNED, 2023). **Libro oficial** del cronograma | `Cálculo para ingenieros.pdf` (nombre con tilde descompuesta) | `ingenieros.txt` | Estructura, definiciones, notación y enunciados de referencia. **Manda el temario.** |
| **E** | *Libro de ejercicios Cálculo curso 24-25* (UNED) | `Libro ejercicios_Calculo_curso2425.pdf` | `ejercicios.txt` | Ejercicios a resolver (Tema 1 = pp. 5-50; en el cronograma, hasta la p. 41). Incluye soluciones/desarrollos. |
| **S** | *Cálculo de una variable. Trascendentes tempranas* — Stewart | `Cálculo_de_una_variable_Trascendentes.pdf` | `stewart.txt` | Mejores explicaciones intuitivas (límites cap. 2, series cap. 11, Apéndice A = números y desigualdades). |
| **L** | *Cálculo Tomo 1* — Ron Larson | `Cálculo_Tomo_1_Ron_Larson,.pdf` | `larson.txt` | Explicaciones paso a paso, muchos ejemplos (límites cap. 1, series cap. 9, Taylor 9.7). |
| **X** | *Exámenes resueltos de Cálculo* (pruebas presenciales UNED 2010-…, Ing. Industrial) | `Examenes-resueltos-Calculo.pdf` (153 págs.; carpeta `Examenes/` = enunciados sueltos) | `examenes.txt` (fórmulas desordenadas) + `indice_examenes_*.md` (índice por pregunta y tema) | Problemas reales de examen por tema. Citar `X p.NN (año, convocatoria)` con página PDF. **Leer el enunciado y la solución como imagen**: `Read` no renderiza PDFs aquí (falta pdftoppm); renderizar la página con PyMuPDF (`import fitz; fitz.open(pdf)[pág-1].get_pixmap(dpi=110).save('x.png')`, en el scratchpad) y leer el PNG. No fiarse del `.txt`. Algunas soluciones impresas tienen erratas: verificar con sympy y avisar. |
| **N** | NotebookLM «Calculo» | id `40b5c11a-b444-4528-abfd-9dc861ab982c` (MCP `gemini-notebook-mcp`) | — | Además de los libros: cronograma, vídeos UNED (T1.1, T1.2…), informe de vídeos, ejercicio 10 web. Sirve para consultas rápidas; **no fiarse de sus índices/páginas**, verificar en los `.txt`. |

Los `.txt` están generados con `pdftotext -layout -enc UTF-8` (las páginas se separan con `\f`). Regenerar copiando antes el PDF a un nombre ASCII (pdftotext de Git Bash falla con tildes).
Otros ficheros previos del usuario: `resumen_modulo1_calculo.html` (resumen antiguo del módulo 1), `tema1_1_espacio_R.html` (primer intento del 1.1, se sustituye por la versión con fuentes).

### Numeración de páginas (citar SIEMPRE la página **impresa**)
- **U**: pág. impresa = pág. PDF + 2 (p.ej. §1.1 empieza en p. 12 = PDF 10).
- **E**: impresa = PDF.
- **L**: impresa = PDF − 17 (capítulo 9 «Series infinitas» empieza en p. 583). Apéndice C (números reales) es «en línea», no está en el PDF.
- **S**: no hay offset fijo fiable en el `.txt` (algunas páginas se parten). Localizar la página impresa por la cabecera («SECCIÓN 1.3 …», «254 CAPÍTULO 3 …») o el pie. Apéndices con prefijo A (A2 = Apéndice A).
- El índice que devuelve NotebookLM es poco fiable: confirmar siempre contra el texto.

## 2. Temario y cronograma (curso 2026-27)

| Semana | Módulo | Libro de teoría **U** | Ejercicios **E** |
|---|---|---|---|
| 1-11 oct | **I. El paso al límite** | Tema 1, secciones **1.1-1.4** (p. 11-56) | Tema 1 hasta p. 41 (ej. 1.1 … ~1.41) |
| 12-25 oct | II. Funciones derivables | Tema 2 (p. 71+) | Tema 2 (E p. 51+) |
| 26 oct | PA1 (módulos I, II) | | |
| 26 oct-8 nov | III. Aplicaciones de la derivada | Tema 3 + **notas adicionales** (Landau, forma de Lagrange en interpolación, Taylor) | Tema 3 (E p. 87+) |
| 9-22 nov | IV. Funciones de varias variables | Tema 4 + material adicional (f: ℝⁿ→ℝᵐ) | Tema 4 (E p. 135+) |
| 23 nov | PA2 (módulos III, IV) | | |
| 23 nov-6 dic | V. Aplicaciones de la diferencial | Tema 5 | Tema 5 (E p. 167+) |
| 11-13 dic | PEC única (módulos I-V) | | |
| 7-20 dic, 8-13 ene | VI. Integral de Riemann | Tema 6 | Tema 6 (E p. 213+) |
| 14 ene | PA3 (módulos V, VI) | | |
| 14-24 ene | Repaso y pruebas presenciales | | |

**No es materia de examen:** sucesiones y series *funcionales* (§1.5 de U, p. 54-70). De series de funciones solo **series de Taylor** (módulo III).

### Estructura real del Tema 1 de U (comprobada en el texto)
- 1.1 El espacio ℝ (p. **12-21**): motivación, números reales, orden, valor absoluto, intervalos, cotas, supremo/ínfimo, axioma del supremo (p. 21, la fórmula impresa omite «acotado superiormente»). **U no define máximo/mínimo ni enuncia arquimediana, densidad ni caracterización ε del supremo**: se explican aparte (etiqueta `P` o S/L). Ejercicios de E propios de 1.1: **1.1-1.5** (E pp. 6-10; las sucesiones empiezan en 1.6). E tiene erratas en 1.2, 1.4, 1.5 (ver `fuentes_txt/soluciones_1_1.md`).
- Aviso de extracción: `pdftotext` pierde la barra de ≠, ∉, ⊄ en los `.txt`; confirmar en el PDF si importa.
- 1.2 Sucesiones (p. 22-33) incluye límites de sucesiones. 1.3 Series (p. 33-41; 1.3 empieza a mitad de la p.33) (autoevaluación al final del cap.). 1.4 Límites y continuidad de funciones (p. 42-56; bisección con cota de error p.54, Ej. 1.49 pp.55-56).
- 1.5 Sucesiones y series de funciones (p. 54-71): **fuera de examen**.
- Tema 2 (U pp. 74-101): 2.1 Derivada, 2.2 Reglas de derivación, 2.3 L'Hôpital, 2.4 Newton y punto fijo, **2.5 Rolle, valor medio y funciones monótonas** (el índice de NotebookLM omitía la 2.5). **Tema 3 de U (pp. 104-139)**: 3.1 Teorema de Taylor (pp.104-112), 3.2 Aplicaciones a series y sucesiones de funciones (pp.113-118: solo lo relativo a series de Taylor/funciones analíticas es examen), 3.3 Interpolación polinómica (pp.119-124), 3.4 Optimización. Extremos relativos y absolutos (pp.125-133), 3.5 Concavidad y convexidad (pp.134-139). Mapa E: 3.1 → E 3.1-3.14; 3.2 → E 3.15-3.20 (3.15-3.17 fuera de examen; 3.18-3.20 series de Taylor); 3.3 → E 3.21-3.28; 3.4/3.5 → E 3.29-3.48 (por confirmar). Tema 3: valor medio, crecimiento/concavidad/extremos, gráficas, Taylor e interpolación. Tema 4: ℝⁿ, funciones de varias variables, límites/continuidad, derivada parcial/gradiente. Tema 5: diferencial, regla de la cadena, TVM, función implícita, extremos, Lagrange. Tema 6: Riemann, teoremas fundamentales, técnicas, numérica, impropias (6.5.3 sucesiones funcionales: probablemente fuera).
- Los vídeos del notebook siguen la numeración «T1.1 El espacio R», «T1.2 Sucesiones»… (vídeos UNED del Grado en Ing. Industrial).

### Mapa de ejercicios de E por sección (Tema 1 y 2)
- 1.1: 1.1-1.5 · 1.2: 1.6-1.16 · 1.3: 1.17-1.22 · 1.4: 1.23-1.41 (cronograma hasta E p.41; 1.42-1.50 son sucesiones/series de funciones: fuera de examen).
- 2.1: 2.1, 2.2, 2.6-2.9, 2.14, 2.17-2.23 · 2.2: 2.3-2.5, 2.10-2.13, 2.15-2.16 · 2.3: 2.24-2.33 · 2.4: 2.34-2.38.
- **2.5 Teoremas de Rolle y del valor medio. Funciones monótonas** (U §2.5, pp. 94-101; **sí es parte del Tema 2**): E 2.39-2.51 (2.50-2.51 usan además extremos y concavidad de U §3.4-3.5).

### Unidades de resumen
Un HTML por sección del cronograma: `1.1, 1.2, 1.3, 1.4, 2.1, 2.2, 2.3, 2.4, 2.5, 3.1…3.4, 4.1…4.3, 5.1…5.5, 6.1…6.5`. Orden de trabajo = orden del cronograma. El usuario pide cada tema por su número («tema 1.2»).

## 3. Formato de los resúmenes HTML

Ficheros y estructura:
```
E:\UNED\CALCULO\claude\
  CLAUDE.md
  index.html                      índice de todos los temas (actualizarlo al terminar cada tema)
  assets/resumen.css, resumen.js  estilo y comportamiento COMPARTIDOS (no duplicar en cada tema)
  assets/katex/                   KaTeX local (offline)
  plantilla_tema.html             esqueleto que se copia para cada tema
  temas/tema_1_1_espacio_R.html   …
  fuentes_txt/                    texto de los PDF
  .claude/agents/, .claude/skills/
```

Reglas de contenido (para alguien que estudia por primera vez):
1. **Intuición primero**: cada concepto = idea en lenguaje llano + ejemplo/analogía → definición formal → ejemplo → error típico. Nada de «es evidente».
2. **Prerrequisitos** al principio y **mapa del tema** (qué se pide en los ejercicios y en el examen).
3. Cajas: `def` (definición), `thm` (teorema/propiedad), `ex` (ejemplo resuelto), `tip` (truco de examen), `warn` (error típico), `intu` (intuición).
4. **Ejercicios resueltos**: los del libro de ejercicios **E** correspondientes a la sección (con su número: «Ejercicio 1.5»), resueltos paso a paso y con el «por qué» de cada paso, más ejemplos propios sencillos → difíciles. Cada ejercicio enseña un **método reutilizable** (recuadro «Receta»).
4b. **«Así lo preguntan en el examen»** (sección obligatoria, antes de la chuleta): 3-6 problemas reales de X (o de `Examenes/`) de ese tema, enunciado fiel, resolución paso a paso verificada con sympy, «Receta» y fuente `X p.NN (año, convocatoria)`. Si la sección no cubre un tipo de pregunta del tema, decirlo. Los de temas aún no estudiados (p.ej. requieren §3.x) se omiten o se marcan.
5. Al final: **chuleta** (fórmulas/enunciados clave), **lista de comprobación** («sé hacer…») y errores frecuentes.
6. Matemáticas con **KaTeX** local (`$…$`, `$$…$$`). Figuras en **SVG inline** cuando aclaren (recta real, intervalos, gráficas de sucesiones/funciones). Todo debe verse bien en claro/oscuro y en móvil, e imprimirse.
7. **Fuentes visibles**: cada definición, teorema, ejemplo y ejercicio lleva una etiqueta `<span class="src" …>` con **libro + sección + página impresa** (ej. `U §1.1.2 p.14`, `S App. A p.A3`, `L §9.1 p.584`, `E Ej. 1.5 p.10`). En escritorio aparece en el **lateral** (nota marginal); en móvil/hover se muestra como tooltip; además hay un panel «Fuentes del tema» con todas. Si algo es explicación propia sin fuente, marcarlo `src="propia"`.
8. Prioridad de fuentes: **U** define lo que cae en examen (notación, enunciados); **S/L** se usan para explicar mejor (indicando qué apartado del libro U cubren). Si S/L contradicen U en notación o alcance, gana U y se avisa.
9. **Rigor**: no inventar páginas ni enunciados. Toda cita de página se verifica en `fuentes_txt`. Todo cálculo se comprueba (con Python/sympy cuando sea posible) antes de publicarlo.
9b. **Lo que NO entra en examen** (series/sucesiones funcionales fuera de Taylor, §1.5 y E 1.42-1.50, 3.2 salvo Taylor/analíticas, y lo que el cronograma o el equipo docente excluyan) va **colapsado por defecto** en `<details class="fuera"><summary>Fuera de examen: …</summary>…</details>` (estilo en `assets/resumen.css`). Los datos que solo son «no están en U» pero sí útiles para el examen no se colapsan.
10. Estilo de las cajas y componentes: ver `assets/resumen.css` y `plantilla_tema.html` (no reinventar).

11. **Figuras: preferir recortes de los libros a SVG.** Si el libro (U, E, S o L) ya tiene la figura, se recorta con `python herramientas/extraer_figura.py` (`list` para ver candidatas, `auto <libro> <pág PDF> "<pie>" <nombre>` o `crop`/`page`; ver cabecera del script; páginas PDF: U impresa−2, E igual, L impresa+17) y se guarda en `assets/img/`. En el HTML: `<figure class="bookfig"><img src="../assets/img/nombre.png" alt="descripción" loading="lazy"><figcaption>… <span class="src" …></span></figcaption></figure>` (la etiqueta de fuente va en el pie; comprobar con la imagen que el recorte es correcto). SVG inline **solo** para figuras propias que no existan en los libros (o que haya que adaptar). Las imágenes son solo para uso personal de estudio: no publicar los HTML con ellas.

## 4. Flujo de trabajo por tema (subagentes en `.claude/agents/`)

| Agente | Modelo | Función |
|---|---|---|
| `fuentes-calculo` | haiku | Busca en `fuentes_txt/*.txt` los pasajes de un tema en U, S, L, E y devuelve extractos con página impresa, más enunciados de ejercicios. Solo lectura. |
| `resolutor-ejercicios` | opus | Resuelve paso a paso los ejercicios del tema (compara con el desarrollo de E), verifica con sympy y devuelve soluciones con «receta». |
| `redactor-tema` | sonnet | Escribe el HTML final a partir de la plantilla, integrando teoría, explicaciones, ejercicios y fuentes. |
| `revisor-tema` | opus | Revisa rigor matemático, citas de página, cobertura de ejercicios y accesibilidad (render). Devuelve lista de correcciones. |

Pipeline: (1) `fuentes-calculo` → dossier del tema (incluye las preguntas de X según `fuentes_txt/indice_examenes_*.md`); (2) `resolutor-ejercicios` (en paralelo con 3 si es posible); (3) `redactor-tema`; (4) `revisor-tema`; (5) corregir, actualizar `index.html` y avisar al usuario. Al empezar un tema, la conversación principal coordina y **no** escribe el HTML a mano salvo retoques.
Skills de diseño ya disponibles y a usar por el redactor/maquetador: `frontend-design:frontend-design`, `carattere` (tipografía), `componi` (layout), `scrutinio` (accesibilidad/rendimiento), `lucida` (pulido final). Skill propio del proyecto: `resumen-calculo` (`.claude/skills/`).

## 4b. Publicación en GitHub (obligatorio tras cada cambio)
Repositorio: `git@github.com:luk224/Calculo_I.git` (rama `main`, **público**). Web: https://luk224.github.io/Calculo_I/ (GitHub Pages desde `main`, carpeta raíz; hay `.nojekyll`).
**Cada vez que se termine un tema nuevo o se haga un cambio en el proyecto (temas, assets, CLAUDE.md, agentes, soluciones, index.html), y antes de dar la tarea por cerrada:**
1. Actualizar `index.html` (marcar el tema como «listo») si se añadió o terminó un tema.
2. `git add -A`, revisar `git status` (no debe entrar nada de `.gitignore`: los `.pdf` y los 4 textos completos `fuentes_txt/{ingenieros,ejercicios,larson,stewart}.txt` se quedan fuera; regenerarlos desde los PDF si hacen falta).
3. `git commit` con mensaje en español que diga qué tema o cambio (p. ej. «Tema 3.2: series de Taylor»), terminado con la línea de coautoría que indique el entorno.
4. `git pull --rebase origin main` si hace falta y `git push origin main`.
5. Confirmar con `git log -1` y `git status` que quedó sincronizado, e indicar al usuario el enlace de la web.
Un commit por tema o cambio coherente; no acumular varios temas sin subir. No usar `--force`. Si el push falla (red, credenciales), avisar al usuario en lugar de dejarlo sin subir en silencio.

## 5. Comandos útiles
- Buscar en un libro: `Grep pattern=… path=fuentes_txt/ingenieros.txt` (usar `-C` para contexto).
- Leer una página de U: `python -c "print(open('fuentes_txt/ingenieros.txt',encoding='utf8').read().split('\f')[PDF-1])"` (PDF = impresa − 2; p. impresa 12 = PDF 10).
- Verificar cálculos: `python -c "import sympy…"` (instalar `sympy` si falta).
- Previsualizar: abrir el HTML en el navegador (o con Claude in Chrome y captura).
