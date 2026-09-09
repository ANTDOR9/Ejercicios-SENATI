<!-- Slide number: 1 -->
# Visualización de datos con Seaborn - PYTHON
Sesión N° 08
Instructor: Jesús Romero Villanueva

### Notes:

<!-- Slide number: 2 -->
# OBJETIVO
Dadas las orientaciones del instructor y el análisis conceptual del tema, el participante será capaz de explicar los fundamentos de la visualización de datos utilizando la biblioteca Seaborn, identificando con claridad los principales gráficos estadísticos y su aplicación en el análisis e interpretación de datos, conforme a los lineamientos de calidad educativa establecidos en la norma ISO 21001:2018, según los criterios establecidos para la sesión.

### Notes:

<!-- Slide number: 3 -->
# OBJETIVO
Dadas las orientaciones del instructor y el análisis conceptual del tema, el participante será capaz de explicar los fundamentos de la visualización de datos utilizando la biblioteca Seaborn, identificando con claridad los principales gráficos estadísticos y su aplicación en el análisis e interpretación de datos, conforme a los lineamientos de calidad educativa establecidos en la norma ISO 21001:2018, según los criterios establecidos para la sesión.

### Notes:

<!-- Slide number: 4 -->
# Iniciando…
“Seaborn convierte la estadística en una narrativa visual del comportamiento de los datos.”

### Notes:

<!-- Slide number: 5 -->
# IMPORTANCIA DE LA VISUALIZACIÓN DE DATOS

![Tutorial: ¿Qué es el Análisis de Datos? Cómo visualizar datos con Python, Numpy, Pandas, Matplotlib y Seaborn](GoogleShape98p4.jpg)

### Notes:

<!-- Slide number: 6 -->
# ¿Qué es Seaborn?
Biblioteca de Python basada en Matplotlib para gráficos estadísticos atractivos.
Diseñada para trabajar con DataFrames de Pandas.

![Tutorial de seaborn | Interactive Chaos](GoogleShape105p5.jpg)

### Notes:

<!-- Slide number: 7 -->
# Características principales:
Estilización automática de gráficos.
Soporte para gráficos estadísticos complejos.
Integración con Matplotlib y Pandas.

![Free NumPy Tutorial - numpy,pandas and data visualisation course | Udemy](GoogleShape112p6.jpg)

### Notes:

<!-- Slide number: 8 -->
# Tipos de Gráficos en Seaborn
Gráfico de Distribución (Histograma y KDE)
Descripción:
Representa la distribución de datos y estima la densidad de probabilidad.
Aplicaciones:
Visualización de la forma y la dispersión de los datos.

![Gráfica de la Distribución de Poisson. la Distribución de Poisson. | Download Scientific Diagram](GoogleShape119p7.jpg)

### Notes:

<!-- Slide number: 9 -->
# Tipos de Gráficos en Seaborn
Gráfico de Distribución (Histograma y KDE)

![](GoogleShape127p8.jpg)

![](GoogleShape126p8.jpg)

### Notes:

<!-- Slide number: 10 -->
# Tipos de Gráficos en Seaborn
Gráfico de Relación (Scatter Plot con Regresión)
Descripción:
Muestra la relación entre dos variables con una línea de regresión.
Aplicaciones:
Análisis de correlación y tendencias.

![correlación y regresión](GoogleShape134p9.jpg)

### Notes:

<!-- Slide number: 11 -->
# Tipos de Gráficos en Seaborn
Gráfico de Relación (Scatter Plot con Regresión)

![](GoogleShape141p10.jpg)

![](GoogleShape142p10.jpg)

### Notes:

<!-- Slide number: 12 -->
# Ejemplo

![](GoogleShape148p11.jpg)

![](GoogleShape149p11.jpg)

### Notes:

<!-- Slide number: 13 -->
# Ejemplo2

![](GoogleShape155p12.jpg)

### Notes:

<!-- Slide number: 14 -->
# Ejemplo3

![](GoogleShape161p13.jpg)

### Notes:

<!-- Slide number: 15 -->
# Ejemplo4

![](GoogleShape167p14.jpg)

### Notes:

<!-- Slide number: 16 -->
# Ejemplo5

![](GoogleShape173p15.jpg)

### Notes:

<!-- Slide number: 17 -->
# 1. Métodos para Crear Gráficos
sns.scatterplot: Crea un gráfico de dispersión.
import seaborn as sns
import matplotlib.pyplot as plt
sns.scatterplot(x='sepal_length', y='sepal_width', data=iris)
plt.show()
sns.lineplot: Crea un gráfico de líneas.
sns.lineplot(x='year', y='value', data=df)
plt.show()
sns.barplot: Crea un gráfico de barras.
sns.barplot(x='category', y='value', data=df)
plt.show()
sns.histplot: Crea un histograma (anteriormente sns.histplot reemplazó a sns.histplot).
sns.histplot(data=df['value'], bins=20)
plt.show()

### Notes:

<!-- Slide number: 18 -->
# 1. Métodos para Crear Gráficos
sns.boxplot: Crea un diagrama de caja.
sns.boxplot(x='category', y='value', data=df)
plt.show()
sns.violinplot: Crea un diagrama de violín.
sns.violinplot(x='category', y='value', data=df)
plt.show()
sns.heatmap: Crea un mapa de calor.
sns.heatmap(data=matrix, annot=True)
plt.show()
sns.pairplot: Crea una matriz de gráficos de dispersión.
sns.pairplot(df, hue='species')
plt.show()

### Notes:

<!-- Slide number: 19 -->
# 1. Métodos para Crear Gráficos
sns.kdeplot: Crea un gráfico KDE (Kernel Density Estimate).
sns.kdeplot(data=df['value'])
plt.show()
sns.countplot: Crea un gráfico de conteo.
sns.countplot(x='category', data=df)
plt.show()
sns.jointplot: Crea una combinación de gráficos de dispersión y KDE.
sns.jointplot(x='sepal_length', y='sepal_width', data=iris, kind='kde')
plt.show()

### Notes:

<!-- Slide number: 20 -->
# 2. Propiedades y Parámetros Comunes
data: El DataFrame que contiene los datos a graficar.
sns.scatterplot(x='x', y='y', data=df)
x y y: Especifican las variables para los ejes x e y.
sns.lineplot(x='x', y='y', data=df)
hue: Utiliza colores para diferenciar categorías dentro de los datos.
sns.scatterplot(x='x', y='y', hue='category', data=df)
palette: Define los colores a usar. Puede ser un nombre de paleta, una lista de colores, o un diccionario.
sns.barplot(x='category', y='value', data=df, palette='viridis')
style: Controla el estilo de los puntos en gráficos de dispersión y líneas.
sns.scatterplot(x='x', y='y', style='category', data=df)

### Notes:

<!-- Slide number: 21 -->
# 2. Propiedades y Parámetros Comunes
size: Cambia el tamaño de los puntos en gráficos de dispersión.
sns.scatterplot(x='x', y='y', size='value', data=df)
markers: Especifica los tipos de marcadores a usar en gráficos de dispersión.
sns.scatterplot(x='x', y='y', markers=['o', 's', 'D'], data=df)
legend: Controla la visualización de la leyenda
sns.lineplot(x='x', y='y', data=df, legend='full')
ax: Permite especificar un objeto Axes de Matplotlib en el que dibujar el gráfico.
fig, ax = plt.subplots()
sns.scatterplot(x='x', y='y', data=df, ax=ax)

### Notes:

<!-- Slide number: 22 -->
# 3. Configuración del Estilo
sns.set_style: Define el estilo general del gráfico. Opciones incluyen 'white', 'dark', 'whitegrid', 'darkgrid', 'ticks'.
sns.set_style('whitegrid')
sns.set_palette: Establece la paleta de colores a utilizar.
sns.set_palette('husl')
sns.set_context: Ajusta el tamaño del gráfico para diferentes contextos (e.g., paper, notebook, talk, poster).
sns.set_context('talk')

### Notes:

<!-- Slide number: 23 -->
# Conclusiones y Recursos Adicionales
Seaborn simplifica la creación de gráficos estadísticos complejos.
Ofrece una amplia gama de estilos y opciones de personalización.

![Spyder: Tu IDE de Elección para Desarrollo Python Científico - CodigosPython](GoogleShape216p22.jpg)

### Notes:

<!-- Slide number: 24 -->

### Notes: