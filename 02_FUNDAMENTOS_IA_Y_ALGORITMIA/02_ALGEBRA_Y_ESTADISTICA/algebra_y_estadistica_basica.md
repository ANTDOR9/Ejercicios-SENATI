# 🧮 Lo necesario para resolver ejercicios de Álgebra Lineal y Estadística

> Guía práctica y simple — enfocada en lo que realmente vas a usar en el código, no en teoría de matemático.

## 1. Vectores

Un vector es simplemente una lista ordenada de números.

```python
import numpy as np

v = np.array([3, 7, 1])
```

### Operaciones que te van a pedir

| Operación | Qué hace | Código |
|---|---|---|
| Suma de vectores | Suma elemento por elemento (misma posición) | `v1 + v2` |
| Resta de vectores | Resta elemento por elemento | `v1 - v2` |
| Multiplicación por un número (escalar) | Multiplica cada elemento por ese número | `v * 3` |
| Producto punto (dot product) | Multiplica elemento por elemento y SUMA todo el resultado (da un solo número) | `np.dot(v1, v2)` |
| Norma (magnitud/longitud del vector) | Qué tan "grande" es el vector | `np.linalg.norm(v)` |

**Ejemplo de producto punto:** si `v1 = [1, 2, 3]` y `v2 = [4, 5, 6]`, el resultado es `1*4 + 2*5 + 3*6 = 32`.

## 2. Matrices

Una matriz es una tabla de números (filas y columnas).

```python
m = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

### Operaciones que te van a pedir

| Operación | Qué hace | Código |
|---|---|---|
| Suma / resta de matrices | Elemento por elemento (deben ser del mismo tamaño) | `m1 + m2` |
| Multiplicación por escalar | Multiplica cada elemento | `m * 2` |
| Multiplicación de matrices | Combina filas de una con columnas de otra (NO es elemento por elemento) | `m1 @ m2` o `np.matmul(m1, m2)` |
| Transposición | Convierte filas en columnas y viceversa | `m.T` |
| Forma de la matriz (dimensiones) | Cuántas filas y columnas tiene | `m.shape` |
| Matriz identidad | Matriz "neutra" para multiplicar (como el número 1 en multiplicación normal) | `np.eye(3)` |

**Regla clave para multiplicar matrices:** el número de columnas de la primera matriz debe ser igual al número de filas de la segunda. Si no calzan, da error — es la causa más común de errores en estos ejercicios.

## 3. Estadística básica

Dado un conjunto de datos, por ejemplo `datos = [4, 8, 6, 5, 3]`:

| Medida | Qué significa | Código |
|---|---|---|
| Media (promedio) | Suma todos los valores y divide entre la cantidad | `np.mean(datos)` |
| Varianza | Qué tan lejos están, en promedio, los datos respecto a la media (elevado al cuadrado) | `np.var(datos)` |
| Desviación estándar | Raíz cuadrada de la varianza — más fácil de interpretar porque usa las mismas unidades que los datos | `np.std(datos)` |
| Mínimo / máximo | El valor más bajo / más alto | `np.min(datos)` / `np.max(datos)` |

### Cómo interpretar varianza y desviación estándar

- Si la desviación estándar es **baja**, los datos están muy juntos, cerca del promedio.
- Si es **alta**, los datos están muy dispersos, alejados del promedio.

**Ejemplo:** `[5, 5, 5, 5]` tiene desviación estándar = 0 (todos son iguales). `[1, 5, 9, 20]` tiene una desviación estándar alta (muy dispersos).

## 4. Errores típicos a evitar

- Confundir `*` (multiplica elemento por elemento) con `@` (multiplicación real de matrices) — son operaciones distintas en NumPy.
- Intentar sumar/restar vectores o matrices de tamaños distintos — deben coincidir en forma (`shape`).
- Olvidar que `np.var()` y `np.std()` necesitan un array o lista de números, no un solo número suelto.

## 5. Resumen rápido de funciones (chuleta)

```python
import numpy as np

np.array([...])        # crear vector o matriz
np.dot(v1, v2)         # producto punto de vectores
m1 @ m2                # multiplicación de matrices
m.T                    # transponer matriz
m.shape                # dimensiones
np.mean(datos)         # promedio
np.var(datos)          # varianza
np.std(datos)          # desviación estándar
```

Con esto ya tienes lo suficiente para resolver la mayoría de ejercicios básicos de este bloque. Cuando aparezca un ejercicio concreto, tráelo y lo resolvemos juntos aplicando estas mismas ideas.
