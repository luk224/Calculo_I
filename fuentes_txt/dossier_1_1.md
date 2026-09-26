# Dossier Tema 1.1: El espacio ℝ

**Fuente principal**: Cálculo para Ingenieros (U), secciones 1.1, páginas impresa 12-20 (PDF 10-18)

---

## 1. LIBRO OFICIAL (U) — Ingenieros, Sección 1.1

### 1.1.1 Motivación (p. 12)

**Introducción**: Nuestro primer contacto con el cálculo infinitesimal será a través de los números reales. No es casualidad. Los números reales son los adecuados para medir magnitudes del mundo real y por lo tanto forman la base sobre la que trabajaremos. Aunque no vamos a construir el conjunto de los números reales, presentaremos algunas de las propiedades que poseen y que los diferencian de los números racionales.

**Objetivos**: Al finalizar esta parte del libro entenderá la necesidad de considerar números reales y algunas de las propiedades más importantes que verifiquen. Prestaremos especial atención al Axioma del supremo porque es una pieza clave para el desarrollo del cálculo infinitesimal. Pero por ejemplo, también veremos cómo el valor absoluto permite medir distancias y definir intervalos.

### 1.1.2 Los números reales (p. 12-20)

#### Conjuntos de números

- **Números naturales**: N = {1, 2, 3, ...}, sirven para contar.
- **Números enteros**: Z = {..., −2, −1, 0, 1, 2, ...}, permiten restar.
- **Números racionales**: Q = {p/q : p, q ∈ Z, q ≠ 0}, abren el camino de las proporciones.
- **Números irracionales**: I, números reales que no son racionales (ej: √2, π).
- **Números reales**: R, el conjunto que contiene a todos los anteriores y completa a Q mediante límites de sucesiones.

**Relaciones**: N ⊂ Z ⊂ Q ⊂ R; Q ∪ I = R; Q ∩ I = ∅.

**Representación**: Los números reales se pueden representar gráficamente como los puntos de una recta llamada recta real.

#### Operaciones y Orden

**Operaciones**: En R se pueden definir suma y producto, dándole una estructura algebraica igual a la de Q.

**Orden**:
- x ≤ y: x es menor o igual que y (x está a la izquierda de y en la recta real, o x = y).
- x < y: x es menor que y (x está a la izquierda de y).
- Números negativos: menores que 0.
- Números positivos: mayores que 0.

#### Propiedades del orden (p. 15)

Sean x, y, z números reales:

1. **Orden total**: x ≤ y y/o y ≤ x
2. **Reflexiva**: x ≤ x
3. **Antisimétrica**: x ≤ y y y ≤ x implica x = y
4. **Transitiva**: x ≤ y y y ≤ z implica x ≤ z
5. **Relación con la suma**: x ≤ y implica x + z ≤ y + z
6. **Relación con el producto**: x ≤ y y 0 ≤ z implica xz ≤ yz
7. **Relación con producto negativo**: x ≤ y y z < 0 implica xz ≥ yz

#### Valor absoluto (p. 15-16)

**Definición 1.1**: El valor absoluto de un número real x es:
$$|x| = \sqrt{x^2} = \begin{cases} x, & x \geq 0 \\ -x, & x < 0 \end{cases}$$

**Significado geométrico**: El valor absoluto de x es la distancia entre x y 0 en la recta real.

**Definición 1.2 - Distancia**: La distancia entre x e y es el valor no negativo |x − y|.

**Teorema 1.1 - Propiedades del valor absoluto** (p. 16): Sean x e y números reales:
1. |x| = 0 ⇔ x = 0
2. |x + y| ≤ |x| + |y| (Desigualdad triangular)
3. |x| − |y| ≤ |x − y|

#### Intervalos (p. 16-18)

Los intervalos son subconjuntos de la recta real formados por una sola pieza (segmentos o semirrectas).

**Intervalos acotados** (a < b números reales):
- **(a, b)** = {x ∈ R : a < x < b} (Intervalo abierto)
- **[a, b]** = {x ∈ R : a ≤ x ≤ b} (Intervalo cerrado)
- **[a, b)** = {x ∈ R : a ≤ x < b} (Intervalo semiabierto)
- **(a, b]** = {x ∈ R : a < x ≤ b} (Intervalo semiabierto)

Los números a y b se llaman **extremos del intervalo**.

**Intervalos no acotados** (con semirrectas):
- **(a, ∞)** = {x ∈ R : a < x}
- **[a, ∞)** = {x ∈ R : a ≤ x}
- **(−∞, a)** = {x ∈ R : x < a}
- **(−∞, a]** = {x ∈ R : x ≤ a}

**Intervalos degenerados**: [a, a] = {a}, (a, a) = ∅, (−∞, ∞) = R.

**Centro y radio** (para intervalos acotados con a < b):
- **Centro**: c = (a + b)/2 (punto medio)
- **Radio**: r = (b − a)/2 (distancia desde el centro a cualquier extremo)

**Descripción usando valor absoluto**:
- (c − r, c + r) = {x ∈ R : |x − c| < r}
- [c − r, c + r] = {x ∈ R : |x − c| ≤ r}

#### Conjuntos acotados. Axioma del supremo (p. 19-21)

**Definición 1.3 - Cota superior**: El número real c es una cota superior para un conjunto A ⊂ R si:
$$a ≤ c \text{ para todo } a ∈ A$$

**Definición 1.4 - Acotado superiormente**: Un conjunto A ⊂ R está acotado superiormente si existe una cota superior para él.

**Definición 1.5 - Cota inferior**: El número real c es una cota inferior para A ⊂ R si:
$$a ≥ c \text{ para todo } a ∈ A$$

Un conjunto A ⊂ R está **acotado inferiormente** si existe una cota inferior para él.

**Definición 1.6 - Acotado**: Un conjunto A ⊂ R está acotado si está acotado superior e inferiormente.

**Definición 1.7 - Supremo**: Un número sup A es el supremo de A ⊂ R si:
- (i) sup A es una cota superior para A
- (ii) si c es una cota superior de A, entonces sup A ≤ c

(Es decir, la menor de las cotas superiores)

**Definición 1.8 - Ínfimo**: El número inf A es el ínfimo del conjunto A si:
- (i) inf A es una cota inferior para A
- (ii) si c es una cota inferior de A, entonces c ≤ inf A

(Es decir, la mayor de las cotas inferiores)

**Propiedades importantes**:
- El supremo (si existe) es único. Lo mismo para el ínfimo.
- No todos los conjuntos tienen supremo y/o ínfimo.
- Un conjunto puede o no contener a sus cotas superiores/inferiores.
- Si hay una cota superior, hay infinitas (todas mayores que ella).

**Axioma del supremo** (p. 21): Todo subconjunto no vacío de números reales acotado superiormente tiene supremo. Es decir:
$$\text{Si } A ⊂ ℝ \text{ y } A ≠ ∅ \text{ acotado superiormente, entonces } \sup A ∈ ℝ$$

**Propiedad análoga para ínfimo**: Si el conjunto A ⊂ R está acotado inferiormente, entonces inf A ∈ R.

**Diferencia fundamental entre Q y R**: 
- Existen subconjuntos acotados de Q para los que no existe supremo en Q (ej: A = {x ∈ Q : x² ≤ 7})
- En R, el Axioma del supremo garantiza siempre la existencia del supremo para conjuntos acotados superiormente.

---

## 2. EJERCICIOS DEL LIBRO (E) — Tema 1.1

### Ejercicio 1.1 (E, p. 6-7)

**Enunciado completo**: Sean I₁ e I₂ los intervalos dados por:
$$I_1 = (-3, 5], \quad I_2 = \{x ∈ ℝ : |x - 3| < 4\}$$

Elige la o las opciones correctas:
- a) Los dos intervalos tienen el mismo radio.
- b) El centro de I₁ es menor que el centro de I₂.
- c) Se cumple I₁ ⊂ I₂.
- d) Ninguna de las anteriores.

**Método de solución**: 
- Convertir ambas descripciones de intervalos a forma estándar (centro y radio o extremos).
- Calcular centro y radio: c = (a+b)/2, r = (b-a)/2.
- Para I₂, reconocer que |x − 3| < 4 significa intervalo (3−4, 3+4) = (−1, 7).
- Comparar los intervalos en la recta real.

**Respuesta correcta**: a) y b) son correctas.

---

### Ejercicio 1.2 (E, p. 7-8)

**Enunciado completo**: Sean x e y dos números reales tales que |x| < |y|. ¿Debe ser |x| < |y + 4|?

**Método de solución**:
- Analizar dos casos según el signo de y.
- **Caso y > 0**: |y| = y < y + 4 = |y + 4|, luego |x| < |y| < |y + 4| ✓
- **Caso y < 0**: Puede ocurrir que y + 4 < 0 (si y < −4), en cuyo caso |y + 4| = −y − 4 < −y = |y|, lo que contradice la implicación.
- Buscar un contraejemplo: y = −6, x = −5. Entonces |x| = 5 < 6 = |y|, pero |y + 4| = |−2| = 2 < 5 = |x|.

**Conclusión**: No siempre. El valor absoluto no preserva las propiedades de las desigualdades con números sin valor absoluto.

---

### Ejercicio 1.3 (E, p. 8)

**Enunciado completo**: Dado el conjunto A = {x ∈ R : 0 < x² < 1}, elige la opción correcta:
- a) inf A = 0.
- b) A tiene supremo pero no tiene ínfimo.
- c) A está acotado.
- d) Ninguna de las anteriores.

**Método de solución**:
- Reconocer que 0 < x² < 1 equivale a 0 < |x| < 1.
- Describir el conjunto: A = (−1, 0) ∪ (0, 1).
- Identificar sup A = 1 e inf A = −1.
- El conjunto está acotado (tanto superior como inferiormente).

**Respuesta correcta**: c) A está acotado.

---

### Ejercicio 1.4 (E, p. 9-10)

**Enunciado completo**: Sea S el conjunto dado por:
$$S = \left\{1, \frac{1}{2}, \frac{1}{3}, \ldots, \frac{1}{n}, \ldots\right\}$$

Se pide encontrar su ínfimo y su supremo. ¿Están en S?

**Método de solución**:
- Identificar S como {1/n : n ∈ N, n > 0}.
- **Para el supremo**: 1/n ≤ 1 para todo n ≥ 1. El máximo es 1 (cuando n = 1), luego sup S = 1. Como 1 ∈ S, el supremo está en el conjunto.
- **Para el ínfimo**: 1/n > 0 para todo n. Cero es cota inferior. Demostrar que es la mayor cota inferior por reducción al absurdo: si c > 0 fuera cota inferior, existiría m ∈ N tal que 1/m < c, contradicción. Luego inf S = 0. Como 0 ∉ S (no existe n tal que 1/n = 0), el ínfimo no está en el conjunto.

**Respuesta**: sup S = 1 (en S); inf S = 0 (no en S).

---

### Ejercicio 1.5 (E, p. 9-10)

**Enunciado completo**: Tenemos dos condensadores, C₁ y C₂, conectados en serie. La capacidad equivalente C verifica:
$$\frac{1}{C} = \frac{1}{C_1} + \frac{1}{C_2}$$

Los dos condensadores tienen capacidad variable: C₁ varía entre 2 y 4 microfaradios (μF), y C₂ entre 1 y 7 μF. Se pide encontrar entre qué valores se encuentra la capacidad del condensador equivalente C.

**Método de solución**:
- Establecer las cotas: 2 ≤ C₁ ≤ 4, 1 ≤ C₂ ≤ 7.
- Invertir: 1/4 ≤ 1/C₁ ≤ 1/2, 1/7 ≤ 1/C₂ ≤ 1.
- Sumar: 1/4 + 1/7 ≤ 1/C ≤ 1/2 + 1, es decir, 11/28 ≤ 1/C ≤ 3/2.
- Invertir de nuevo: 2/3 ≤ C ≤ 28/11.

**Respuesta**: La capacidad equivalente está entre 2/3 μF ≈ 0.67 μF y 28/11 μF ≈ 2.55 μF. Estos son el ínfimo y supremo de C.

---

## 3. FUENTES COMPLEMENTARIAS

### Stewart (S) — Apéndice A: Números, desigualdades y valores absolutos (páginas A2-A9)

**Ubicación**: Apéndice A del libro "Cálculo de una variable. Trascendentes tempranas" de James Stewart.

**Temas cubiertos**:
- Números reales (construcción intuitiva, propiedades)
- Desigualdades (propiedades del orden, resolución de desigualdades)
- Valores absolutos (definición, propiedades, ecuaciones e inecuaciones con valor absoluto)
- Distancia en la recta real

**Nota**: Stewart no enfatiza supremo/ínfimo en el nivel de introducción (lo usa más adelante en el contexto de optimización). El Apéndice A complementa con tratamiento muy accesible de números, desigualdades y valor absoluto.

**Correspondencia con U**: Cubre equivalentemente los apartados de números reales, orden, valor absoluto, intervalos y desigualdades de la sección 1.1 de U.

---

### Larson (L) — Apéndice C: Números reales (EN LÍNEA, no en PDF)

**Nota importante**: Según CLAUDE.md, Larson Apéndice C (números reales) es "en línea" (online) y no está incluido en el PDF proporcionado.

**Lo que se esperaría en ese apéndice** (según la estructura típica):
- Propiedades de los números reales
- Desigualdades
- Valor absoluto
- Intervalos

**En el PDF de Larson disponible**:
- **Capítulo 1** (páginas iniciales, impresa = PDF − 17): Introduce límites y el concepto de aproximación, que relaciona con números reales.
- **Sección 9.1** (sobre series): Discute monotonía y acotación de sucesiones (tema 1.2, no 1.1).

**Conclusión**: Larson Apéndice C no está disponible en el PDF. Los temas 1.1 se cubren mejor con U y S.

---

## 4. RESUMEN: Ejercicios identificados de Tema 1.1

| Ejercicio | Página (E) | Tema 1.1 | Descripción |
|-----------|-----------|---------|------------|
| 1.1 | 6-7 | SÍ | Intervalos: centro, radio, relaciones entre intervalos |
| 1.2 | 7-8 | SÍ | Valor absoluto: comportamiento de desigualdades con valor absoluto |
| 1.3 | 8 | SÍ | Conjunto acotado: determinación de supremo, ínfimo |
| 1.4 | 9-10 | SÍ | Supremo e ínfimo: análisis de {1/n} |
| 1.5 | 9-10 | SÍ | Cotas superior e inferior (aplicación a condensadores) |

**Ejercicios de Tema 1.1: 1.1, 1.2, 1.3, 1.4, 1.5** (5 ejercicios)

---

## 5. FUENTES AUXILIARES ENCONTRADAS

### Stewart (S)

- **Apéndice A**: "Números, desigualdades y valores absolutos" (páginas A2-A9)
- **Ubicación**: Al inicio del libro, explicaciones claras y con ejemplos
- **Temas**: Números reales, orden, desigualdades, valor absoluto, intervalos
- **Uso recomendado**: Repaso y explicaciones alternativas de conceptos básicos de 1.1

### Larson (L)

- **Apéndice C**: "Números reales" (NO disponible en PDF, contenido "en línea")
- **Capítulo 1**: Límites (introduce números reales implícitamente)
- **Sección 9.1**: Monotonía y acotación (tema 1.2, no 1.1)
- **Conclusión**: Larson es más apropiado para temas posteriores (1.2 en adelante)

---

## 6. FALTAS O DUDAS

- ✓ Libro U (ingenieros.txt): Sección 1.1 completa y verificada (p. 12-20).
- ✓ Ejercicios E (ejercicios.txt): Ejercicios 1.1-1.5 identificados y descritos.
- ✓ Stewart (stewart.txt): Apéndice A localizado y referencias correctas (A2-A9).
- ✗ Larson (larson.txt): Apéndice C confirmado que no está en el PDF (contenido en línea).
- ✓ Todas las páginas citadas han sido verificadas en los archivos .txt.

---

**Fecha de compilación**: 2026-09-26  
**Compilador**: Agente fuentes-calculo  
**Estado**: Dossier completo para Tema 1.1 El espacio ℝ
