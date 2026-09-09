<!-- Slide number: 1 -->
# Fundamentos de manipulación de datos con NUMPY
Sesión N° 02
Instructor: Jesús Romero Villanueva

### Notes:

<!-- Slide number: 2 -->
# OBJETIVO
Dadas las orientaciones del instructor y el análisis conceptual del tema, el participante será capaz de explicar los fundamentos de manipulación de datos utilizando la biblioteca NumPy, identificando con claridad la creación y uso de arreglos multidimensionales, así como las operaciones básicas de indexación y cálculo vectorizado, conforme a los lineamientos de calidad educativa establecidos en la norma ISO 21001:2018, según los criterios establecidos para la sesión.

### Notes:

<!-- Slide number: 3 -->
# INICIANDO…
“Antes del modelo, antes del algoritmo, existe NumPy; porque en cada arreglo vibra la estructura fundamental del cálculo, y en cada operación vectorizada se revela la armonía entre lógica y eficiencia.”

### Notes:

<!-- Slide number: 4 -->
# ¿Por qué analizar datos con NUMPY?

![NumPy : La biblioteca de Python más utilizada en Data Science](GoogleShape91p4.jpg)

### Notes:

<!-- Slide number: 5 -->
# Fundamentos de Vectores y Matrices (con NumPy)
¿Qué es un vector?
Es una estructura unidimensional: una fila o columna de datos.
¿Qué es una matriz?
Es una estructura bidimensional: filas y columnas, como una tabla.

### Notes:

<!-- Slide number: 6 -->
# Ejemplo
import numpy as np
vector = np.array([1, 2, 3])
matriz = np.array([[1, 2], [3, 4]])
print(vector)
print('\n')
print(matriz)

![](GoogleShape104p6.jpg)

### Notes:

<!-- Slide number: 7 -->
# Operaciones básicas
import numpy as np
vector = np.array([1, 2, 3])
matriz = np.array([[1, 2], [3, 4]])
print(vector)
print(matriz)
print(vector * 2)
print(np.dot(vector, vector))
print(matriz.T)
print(np.linalg.inv(matriz))

![](GoogleShape111p7.jpg)

### Notes:

<!-- Slide number: 8 -->
# ¿Qué es NUMPY?
NumPy (Numerical Python) es uno de los módulos más importantes y, probablemente, el más utilizado en el campo del cálculo numérico en el ecosistema de Python

![Using NumPy reshape() to Change the Shape of an Array – Real Python](GoogleShape118p8.jpg)

### Notes:

<!-- Slide number: 9 -->
# Definición de Pandas y Numpy
| Característica | NumPy | Pandas |
| --- | --- | --- |
| ¿Qué es? | Librería para cálculo numérico eficiente | Librería para análisis de datos estructurados |
| Estructura principal | ndarray (arreglos n-dimensionales) | DataFrame y Series |
| Ideal para... | Álgebra lineal, vectores, matrices | Tablas, bases de datos, CSVs, Excel |
| Velocidad | Extremadamente rápida con arrays numéricos | Rápido, pero se basa internamente en NumPy |
| Uso común | Simulación, Machine Learning, estadística | Exploración de datos, limpieza, informes |

### Notes:

<!-- Slide number: 10 -->
# Lectura de Archivos CSV
Con NumPy (menos común, útil para datos numéricos sin cabecera):

	data = np.loadtxt('archivo.csv', delimiter=',', skiprows=1)

### Notes:

<!-- Slide number: 11 -->
# ¿Cuál usar?
| Si tienes... | Usa... |
| --- | --- |
| Datos tabulares con cabeceras | Pandas |
| Solo números, sin columnas con texto | NumPy |
| Necesitas filtrar, agrupar, limpiar | Pandas |
| Procesamiento matemático de vectores | NumPy |

### Notes:

<!-- Slide number: 12 -->
# Manipulación y Análisis de Estructuras de Datos
Con NumPy: Acceso por índice:

import numpy as np
vector = np.array([1, 2, 3])
matriz = np.array([[1, 2], [3, 4]])
matriz[0, 1]

### Notes:

<!-- Slide number: 13 -->
# Generalidades
Ofrece el objeto ndarray, similar a una lista de Python pero optimizada para el cálculo numérico. Nos referiremos a este objeto como array de NumPy, o simplemente array.
Implementa funciones matemáticas que pueden trabajar directamente sobre arrays sin tener que implementar bucles.
Proporciona funciones para leer/escribir datos a archivos de manera optimizada.
Permite aplicaciones de álgebra lineal, generación de números aleatorios y transformadas de Fourier.

### Notes:

<!-- Slide number: 14 -->
# Características principales de NumPy:
Arreglos (Arrays) N-dimensionales:
NumPy introduce un nuevo tipo de datos llamado ndarray, que es un arreglo multidimensional homogéneo y eficiente. Esto permite representar datos de manera más eficiente que las listas de Python estándar, especialmente cuando se trata de operaciones matemáticas y científicas.

![Numpy Array Cookbook: Generating and Manipulating Arrays in Python | by GreekDataGuy | Towards Data Science](GoogleShape155p14.jpg)

### Notes:

<!-- Slide number: 15 -->
# Características principales de NumPy:
Eficiencia y rendimiento: Las operaciones en NumPy se implementan en código C bajo el capó, lo que garantiza una ejecución rápida y eficiente de las operaciones matemáticas y algebraicas, incluso en grandes volúmenes de datos.

![Eficiencia o productividad, administre los recursos y el tiempo para optimizar el mejor resultado de trabajo, aumente el rendimiento con un proceso efectivo, el empresario combina el temporizador de reloj y la](GoogleShape162p15.jpg)

### Notes:

<!-- Slide number: 16 -->
# Comparación para ver rendimiento…

![](GoogleShape168p16.jpg)

### Notes:

<!-- Slide number: 17 -->
# Métodos NUMPY
Método Zeros()

![](GoogleShape175p17.jpg)

### Notes:

<!-- Slide number: 18 -->
# Otro ejemplo…

![](GoogleShape182p18.jpg)

![](GoogleShape181p18.jpg)

### Notes:

<!-- Slide number: 19 -->
# Algunas propiedades de NUMPY
Propiedades NP

![](GoogleShape190p19.jpg)

![](GoogleShape189p19.jpg)

### Notes:

<!-- Slide number: 20 -->
# Redimensionar Array y Método arange()

![](GoogleShape196p20.jpg)

![](GoogleShape197p20.jpg)

### Notes:

<!-- Slide number: 21 -->
# Operaciónes con Arrays

![](GoogleShape203p21.jpg)

![](GoogleShape204p21.jpg)

### Notes:

<!-- Slide number: 22 -->

### Notes: