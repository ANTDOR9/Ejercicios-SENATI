<!-- Slide number: 1 -->
# Fundamentos de manipulación de datos con Pandas
Sesión N° 01
Instructor: Jesús Romero Villanueva

### Notes:

<!-- Slide number: 2 -->
# OBJETIVO
Dadas las orientaciones del instructor y el análisis conceptual del tema, el participante será capaz de analizar los fundamentos de la manipulación de datos con Pandas y NumPy, relacionando los conceptos de vectores y matrices con las características y utilidad de ambas bibliotecas en el manejo y procesamiento de datos, conforme a los lineamientos de calidad educativa establecidos en la norma ISO 21001:2018, según los criterios establecidos para la sesión.

### Notes:

<!-- Slide number: 3 -->
# ¿Cuál es la importancia de Pandas?

![450+ Practice Questions That Will Make You a Pandas, NumPy, and SQL Pro | by Avi Chawla | Geek Culture | Medium](GoogleShape85p3.jpg)

### Notes:

<!-- Slide number: 4 -->
# INTRODUCCIÓN
"Los datos son el nuevo petróleo, pero sin Pandas, es como tratar de refinarlo con las manos."

### Notes:

<!-- Slide number: 5 -->
# INGENIERIOS …
Antes de Iniciar necesitaremos recordar los fundamentos y generalidades de VECTORES y MATRICES.

![Lógica de programación](GoogleShape98p5.jpg)

### Notes:

<!-- Slide number: 6 -->
# Vectores y Matrices
Un vector es una secuencia ordenada de números (o elementos) que se pueden operar de manera conjunta.

Una matriz es una estructura bidimensional de números organizados en filas y columnas.

![](GoogleShape105p6.jpg)

![](GoogleShape106p6.jpg)

### Notes:

<!-- Slide number: 7 -->
# Hablemos sobre PANDAS
Potente biblioteca de Python utilizada principalmente para la manipulación y análisis de datos.
Fue creada por Wes McKinney en 2008 y desde entonces se ha convertido en una herramienta fundamental en el ecosistema de Python para la ciencia de datos y el análisis estadístico.

![Descubre el poder de la librería Pandas para el análisis de datos en Python - CoDigital](GoogleShape113p7.jpg)

### Notes:

<!-- Slide number: 8 -->
# Manipulación y Análisis de Estructuras de Datos con Pandas
Manipular es transformar, limpiar, organizar, unir, filtrar, agregar o estructurar los datos.
Analizar es obtener conclusiones: promedios, totales, agrupaciones, comparaciones, resúmenes estadísticos, etc.

![Análisis de los datos - Iconos gratis de márketing](GoogleShape120p8.jpg)

### Notes:

<!-- Slide number: 9 -->
# Características principales de Pandas:
Estructuras de datos flexibles:
Series: Es un arreglo unidimensional etiquetado capaz de contener cualquier tipo de datos (enteros, cadenas, números de punto flotante, objetos Python, etc.).

DataFrame: Es una estructura de datos tabular bidimensional similar a una tabla de base de datos o una hoja de cálculo de Excel. Está formado por filas y columnas, donde cada columna puede contener diferentes tipos de datos.

![Introduction to Pandas Series and DataFrame | by Let's Decode | Medium](GoogleShape127p9.jpg)

### Notes:

<!-- Slide number: 10 -->
# Características principales de Pandas:
Manipulación de datos: Pandas ofrece una amplia gama de funcionalidades para limpiar, transformar y analizar datos:
Selección y filtrado de datos.
Manejo de valores faltantes.
Operaciones de agrupación y agregación.
Fusión y concatenación de datos.
Iteración sobre datos.

![Qué es un DataFrame? -](GoogleShape134p10.jpg)

### Notes:

<!-- Slide number: 11 -->
# Características principales de Pandas:
Indexación poderosa: Los objetos Series y DataFrame de Pandas tienen índices explícitos que permiten un acceso rápido y eficiente a los datos. Los índices pueden ser etiquetas (por ejemplo, nombres de columnas o índices de filas) o enteros.

![La librería Pandas | Aprende con Alf](GoogleShape141p11.jpg)

### Notes:

<!-- Slide number: 12 -->
# Ahora veamos un ejemplo…
Ejercicio1.py

![](GoogleShape148p12.jpg)

![](GoogleShape149p12.jpg)

### Notes:

<!-- Slide number: 13 -->
# Ahora veamos un ejemplo…
Ejercicio2.py

![](GoogleShape156p13.jpg)

![](GoogleShape157p13.jpg)

### Notes:

<!-- Slide number: 14 -->
# Ejemplo Nro 2

![](GoogleShape163p14.jpg)

![](GoogleShape164p14.jpg)

### Notes:

<!-- Slide number: 15 -->
# Información técnica sobre el código
Constructores
pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
data: Puede ser un diccionario, una lista de listas, una matriz numpy, o un DataFrame existente. Define los datos del DataFrame.
index: Lista de etiquetas para las filas. Si no se proporciona, se generará un índice numérico por defecto.
columns: Lista de etiquetas para las columnas. Si no se proporciona, se generará un rango numérico por defecto.
dtype: Tipo de datos para las columnas.
copy: Si se debe hacer una copia de los datos

### Notes:

<!-- Slide number: 16 -->
# Información técnica sobre el código
Métodos
head(n=5): Devuelve las primeras n filas del DataFrame.
tail(n=5): Devuelve las últimas n filas del DataFrame.
describe(): Genera estadísticas descriptivas (como conteo, media, desviación estándar, etc.) de las columnas numéricas.
info(): Proporciona un resumen conciso del DataFrame, incluyendo el tipo de datos y la cantidad de valores no nulos.
groupby(by): Agrupa los datos según una o varias columnas.
merge(right, how='inner', on=None): Realiza una combinación de dos DataFrames, similar a un JOIN en SQL.
pivot_table(values, index, columns, aggfunc): Crea una tabla dinámica que puede agregar datos en base a funciones de agregación.

### Notes:

<!-- Slide number: 17 -->
# Información técnica sobre el código
Propiedades
df.shape: Devuelve una tupla con el número de filas y columnas.
df.columns: Devuelve las etiquetas de las columnas.
df.index: Devuelve las etiquetas del índice (filas).
df.dtypes: Devuelve los tipos de datos de cada columna.
df.values: Devuelve los datos del DataFrame como una matriz numpy.

### Notes:

<!-- Slide number: 18 -->
# Información técnica sobre el código
Constructores
pd.Series(data=None, index=None, dtype=None, name=None, copy=False)
data: Puede ser una lista, un array numpy, un diccionario, o un escalar. Define los datos de la serie.
index: Lista de etiquetas para los datos. Si no se proporciona, se generará un índice numérico por defecto.
dtype: Tipo de datos para los datos de la serie.
name: Nombre de la serie.
copy: Si se debe hacer una copia de los datos.

### Notes:

<!-- Slide number: 19 -->
# Información técnica sobre el código
Métodos
head(n=5): Devuelve los primeros n elementos de la serie.
tail(n=5): Devuelve los últimos n elementos de la serie.
describe(): Genera estadísticas descriptivas de los datos de la serie.
value_counts(): Devuelve la frecuencia de valores únicos en la serie.
apply(func): Aplica una función a cada elemento de la serie.

### Notes:

<!-- Slide number: 20 -->
# Información técnica sobre el código
Propiedades
s.shape: Devuelve una tupla con el número de elementos.
s.index: Devuelve las etiquetas del índice.
s.values: Devuelve los datos de la serie como un array numpy.
s.dtype: Devuelve el tipo de datos de los elementos de la serie

### Notes:

<!-- Slide number: 21 -->
# Conclusiones

![LA INTELIGENCIA ARTIFICIAL LLEGÓ PARA QUEDARSE - Conexión SenatiConexión Senati](GoogleShape207p21.jpg)
Pandas es una herramienta poderosa para la manipulación y análisis de datos en Python. Ofrece una gran variedad de funcionalidades que facilitan el trabajo con datos tabulares, desde la importación y limpieza hasta el análisis y visualización.

### Notes:

<!-- Slide number: 22 -->

### Notes: