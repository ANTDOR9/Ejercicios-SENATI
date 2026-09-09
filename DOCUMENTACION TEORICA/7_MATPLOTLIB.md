<!-- Slide number: 1 -->
# Visualización de Datos con Matplotlib - PYTHON
Sesión N° 07
Instructor: Jesús Romero Villanueva

### Notes:

<!-- Slide number: 2 -->
# OBJETIVO
Dadas las orientaciones del instructor y el análisis conceptual del tema, el participante será capaz de explicar los fundamentos de la visualización de datos utilizando la biblioteca Matplotlib, identificando con claridad los principales tipos de gráficos y su aplicación en la representación e interpretación de información, conforme a los lineamientos de calidad educativa establecidos en la norma ISO 21001:2018, según los criterios establecidos para la sesión.

### Notes:

<!-- Slide number: 3 -->
# INICIANDO…
“Cuando los datos se convierten en gráficos, el conocimiento deja de ser abstracto y se vuelve visible.”

### Notes:

<!-- Slide number: 4 -->
# IMPORTANCIA DE LA VISUALIZACIÓN DE DATOS

![Tutorial: ¿Qué es el Análisis de Datos? Cómo visualizar datos con Python, Numpy, Pandas, Matplotlib y Seaborn](GoogleShape91p4.jpg)

### Notes:

<!-- Slide number: 5 -->
# ¿Qué es Matplotlib?
Biblioteca de Python para gráficos 2D que produce figuras de calidad publicación.

![Matplotlib — Википедия](GoogleShape98p5.jpg)

### Notes:

<!-- Slide number: 6 -->
# Características principales:
Personalización completa de gráficos.
Soporte para diferentes formatos de salida (PNG, PDF, SVG, etc.).
Integración con NumPy y Pandas.

![Free NumPy Tutorial - numpy,pandas and data visualisation course | Udemy](GoogleShape105p6.jpg)

### Notes:

<!-- Slide number: 7 -->
# Tipos de Gráficos en Matplotlib
Gráficos de Líneas
Descripción:
Utilizados para mostrar tendencias a lo largo de un eje, típicamente con variables continuas en ambos ejes.
Aplicaciones:
Representación de series temporales, tendencias matemáticas, etc.

![Tarea](GoogleShape112p7.jpg)

### Notes:

<!-- Slide number: 8 -->
# Tipos de Gráficos en Matplotlib
Gráficos de Barras
Descripción:
Utilizados para comparar cantidades discretas o categorizadas.
Aplicaciones:
Comparación de datos categóricos, como ventas por categoría, resultados de encuestas, etc.

![R para principiantes](GoogleShape119p8.jpg)

### Notes:

<!-- Slide number: 9 -->
# Tipos de Gráficos en Matplotlib
Gráficos de Barras

![](GoogleShape127p9.jpg)

![](GoogleShape126p9.jpg)

### Notes:

<!-- Slide number: 10 -->
# Tipos de Gráficos en Matplotlib
Gráficos de Líneas

![](GoogleShape134p10.jpg)

### Notes:

<!-- Slide number: 11 -->
# Tipos de Gráficos en Matplotlib
Gráficos de Dispersión
Descripción:
Representan puntos de datos individuales con valores en dos dimensiones.
Aplicaciones:
Visualización de correlaciones entre variables, distribución de datos.

![](GoogleShape141p11.jpg)

### Notes:

<!-- Slide number: 12 -->
# Tipos de Gráficos en Matplotlib
Gráficos de Dispersión

![](GoogleShape148p12.jpg)

![](GoogleShape149p12.jpg)

### Notes:

<!-- Slide number: 13 -->
# Tipos de Gráficos en Matplotlib
Histogramas
Descripción:
Representan la distribución de datos mediante barras que muestran la frecuencia de ocurrencia en intervalos.
Aplicaciones:
Análisis de distribución de datos, identificación de patrones.

![Estadística básica: Histograma de datos](GoogleShape156p13.jpg)

### Notes:

<!-- Slide number: 14 -->
# Tipos de Gráficos en Matplotlib
Histogramas

![](GoogleShape164p14.jpg)

![](GoogleShape163p14.jpg)

### Notes:

<!-- Slide number: 15 -->
# Personalización y Estilos

![Crear un gráfico con gráficos recomendados - Soporte técnico de Microsoft](GoogleShape171p15.jpg)
Personalización:
Cambio de colores, estilos de línea y marcadores.
Ajuste de ejes, etiquetas y títulos.
Estilos predefinidos:
Uso de estilos predefinidos (ggplot, seaborn, etc.).

### Notes:

<!-- Slide number: 16 -->
# Integración con Pandas y Ejemplo de Gráfico Avanzado
Integración con Pandas:
Uso de DataFrames para generar gráficos automáticamente.

![](GoogleShape178p16.jpg)

### Notes:

<!-- Slide number: 17 -->
# 1. Propiedades de Figure y Axes
figsize: Controla el tamaño de la figura. Se especifica como una tupla (ancho, alto) en pulgadas.
plt.figure(figsize=(10, 5))
dpi: Define la resolución de la figura en puntos por pulgada.
plt.figure(dpi=100)
title: Añade un título a la figura.
plt.title('Título del Gráfico')
xlabel y ylabel: Etiquetan los ejes X e Y, respectivamente.
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
xlim y ylim: Establecen los límites de los ejes X e Y.
plt.xlim(0, 10)
plt.ylim(0, 100)
grid: Activa o desactiva la cuadrícula en el gráfico.
plt.grid(True)

### Notes:

<!-- Slide number: 18 -->
# 2. Métodos de Axes
plot: Crea un gráfico de líneas.	ax.plot(x, y, label='Línea')
scatter: Crea un gráfico de dispersión.	ax.scatter(x, y, color='red', label='Puntos')
bar: Crea un gráfico de barras.	ax.bar(x, height, color='blue', label='Barras')
hist: Crea un histograma.	ax.hist(data, bins=20, color='green', alpha=0.7)
pie: Crea un gráfico de torta.	ax.pie(sizes, labels=labels, autopct='%1.1f%%')
legend: Añade una leyenda al gráfico.	ax.legend()
savefig: Guarda la figura en un archivo.	plt.savefig('mi_grafico.png')
show: Muestra la figura en una ventana emergente.	plt.show()

### Notes:

<!-- Slide number: 19 -->
# 3. Propiedades de Estilo
linestyle: Define el estilo de la línea (sólida, punteada, etc.).
ax.plot(x, y, linestyle='--')
marker: Define el marcador para los puntos de datos en un gráfico de líneas.
ax.plot(x, y, marker='o')
alpha: Ajusta la transparencia de los elementos (0 es completamente transparente y 1 es completamente opaco).
ax.scatter(x, y, alpha=0.5)
fontsize: Ajusta el tamaño de la fuente para títulos, etiquetas y leyendas.
plt.title('Título', fontsize=14)
linewidth: Define el grosor de las líneas.
ax.plot(x, y, linewidth=2)

### Notes:

<!-- Slide number: 20 -->
# 4. Configuración de Ejes
set_xticks y set_yticks: Establecen los ticks en los ejes X e Y.
ax.set_xticks([0, 1, 2, 3])
set_xticklabels y set_yticklabels: Establecen las etiquetas de los ticks en los ejes X e Y.
ax.set_xticklabels(['A', 'B', 'C', 'D'])
set_xlim y set_ylim: Establecen los límites de los ejes X e Y.
ax.set_xlim(0, 10)
ax.set_ylim(0, 100)

### Notes:

<!-- Slide number: 21 -->
# 5. Subgráficos y Diseño
subplot: Permite crear múltiples subgráficos dentro de una figura.
plt.subplot(2, 2, 1)  # 2x2 grid, first subplot
subplots_adjust: Ajusta los espacios entre subgráficos.
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

### Notes:

<!-- Slide number: 22 -->
# Exportar y guardar imágenes
Después de generar tu gráfico con Matplotlib, usa la función savefig() para guardar la imagen.

![](GoogleShape215p22.jpg)

### Notes:

<!-- Slide number: 23 -->
# Parámetros útiles
dpi=300: Guarda con buena resolución (ideal para impresión o publicación).
bbox_inches='tight': Elimina márgenes en blanco innecesarios.

![](GoogleShape222p23.jpg)

### Notes:

<!-- Slide number: 24 -->
# Visualización de Datos con Matplotlib - PYTHON
Sesión N° 09
Instructor: Jesús Romero Villanueva

### Notes:

<!-- Slide number: 25 -->
# OBJETIVO
Dadas las orientaciones del instructor y el análisis conceptual del tema, el participante será capaz de analizar los tipos de gráficos estadísticos y los procesos de exportación de imágenes, relacionando su aplicación con la representación y comunicación de datos mediante Python, conforme a los lineamientos de calidad educativa establecidos en la norma ISO 21001:2018, según los criterios establecidos para la sesión.

### Notes:

<!-- Slide number: 26 -->
# Dónde se guarda el archivo
Si no especificas una ruta, se guarda en el directorio actual del script.
Puedes guardar en una carpeta específica así:

![](GoogleShape243p24.jpg)

### Notes:

<!-- Slide number: 27 -->
# Conclusiones y Recursos Adicionales
Matplotlib es esencial para visualización de datos en Python.
Amplias opciones de personalización y tipos de gráficos.

![Spyder: Tu IDE de Elección para Desarrollo Python Científico - CodigosPython](GoogleShape250p25.jpg)

### Notes:

<!-- Slide number: 28 -->

### Notes: