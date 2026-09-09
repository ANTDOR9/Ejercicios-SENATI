<!-- Slide number: 1 -->
# HT2-Estudia el uso de las librerías Scikit-learn y Pytorch
Sesión N° 1
Instructor: Jesús Romero Villanueva

<!-- Slide number: 2 -->
# OBJETIVO
Dadas las orientaciones del instructor y los recursos del laboratorio, el participante será capaz de describir los principios de la Visión Computacional y el Machine Learning, definiendo la segmentación y el reconocimiento de patrones, e identificando sus principales aplicaciones, con precisión en la tarea, cumpliendo las normas de seguridad en el uso de equipos informáticos y prevención de riesgos eléctricos conforme a la ISO 45001:2018 y la ISO 9241.

<!-- Slide number: 3 -->
# Desarrollo del seminario
HT1 – Realiza operaciones con las librerías Pandas y Numpy
Estudia los fundamentos de vectores y matrices.
Define la librería Pandas y Numpy.
Manipula y analiza estructuras de datos.
Lee archivos CSV con Numpy y Pandas
HT2 – Estudia el uso de las librerías Scikit-learn y Pytorch
Define el concepto de Machine Learning
Define la librería Scikit-Learn y Pytorch.
Identifica principales aplicaciones

<!-- Slide number: 4 -->
# Antes de iniciar
"El análisis de datos y el aprendizaje automático están cambiando el mundo. Hoy aprenderemos a dominar estas herramientas y ser parte de esta transformación."

![Iconos animados de Inteligencia artificial | Iconos animados de tecnología gratis](Picture2.jpg)

<!-- Slide number: 5 -->
# Fundamentos de Vectores y Matrices
Vectores: Una estructura unidimensional (una lista de elementos).
Matrices: Una estructura bidimensional (tabla con filas y columnas).

![Introduction to Scalars Vectors Matrices and Tensors using Python/Numpy examples and drawings](Picture3.jpg)

<!-- Slide number: 6 -->
# Ejemplo práctico - Numpy
import numpy as np
vector = np.array([1, 2, 3, 4])
print("Vector:", vector)matriz = np.array([[1, 2], [3, 4]])
print("Matriz:\n", matriz)

<!-- Slide number: 7 -->
# Definición de Pandas y Numpy
Numpy: Librería para manipular arrays multidimensionales. Es fundamental para realizar operaciones matemáticas eficientes.
Pandas: Librería especializada en la manipulación de datos en estructuras de DataFrames y Series.

![](Picture4.jpg)

<!-- Slide number: 8 -->
# Conceptos clave
Numpy:
Proporciona arrays que permiten realizar operaciones matemáticas rápidas.
Soporta operaciones vectorizadas que se aplican a todos los elementos de un array de manera simultánea.

Pandas:
DataFrame: Estructura bidimensional con filas y columnas, similar a una tabla en bases de datos o una hoja de cálculo.
Series: Estructura unidimensional que puede contener cualquier tipo de datos.

<!-- Slide number: 9 -->
# Ejemplo de uso
import pandas as pddata = {'Nombre': ['Sussie', 'Pepe', 'Alberto'],
        'Edad': [19, 20, 25],
        'Ciudad': ['Puno', 'Arequipa', 'Lima']}df = pd.DataFrame(data)
print(df)

![](Imagen4.jpg)

<!-- Slide number: 10 -->
# Manipulación y Análisis de Datos con Pandas y Numpy
Manipulación de DataFrames:
Seleccionar columnas y filas.
Filtrar datos.
Realizar operaciones matemáticas en columnas.

![](Imagen4.jpg)

![](Imagen6.jpg)

<!-- Slide number: 11 -->
# Lectura de Archivos CSV con Pandas y Numpy
Leer archivos CSV:
Pandas tiene una función fácil de usar para leer archivos CSV: pd.read_csv().
Numpy también puede leer CSVs con la función np.genfromtxt().

![](Imagen5.jpg)

<!-- Slide number: 12 -->
# Ejercicio práctico 1:
Instrucciones:
Leer un archivo CSV que contenga información sobre estudiantes (nombre, edad, calificación).
Filtrar los estudiantes con calificaciones mayores a 7.
Calcular el promedio de las edades de los estudiantes.

<!-- Slide number: 13 -->
# Ejercicio práctico 2:
Instrucciones:
Cargar un archivo CSV con información de ventas.
Filtrar las ventas superiores a un valor determinado.
Guardar los resultados en un nuevo archivo CSV.

<!-- Slide number: 14 -->
# OBJETIVO
Dadas las orientaciones del instructor y los recursos del laboratorio, el participante será capaz de estudiar el uso de las librerías Scikit-learn y PyTorch, definiendo sus características y principales aplicaciones en el desarrollo de modelos de Machine Learning, desarrollando cada operación con precisión operacional y cumpliendo las normas de seguridad en el uso de equipos informáticos y prevención de riesgos eléctricos conforme a la ISO 45001:2018 y la ISO 9241.

<!-- Slide number: 15 -->
# Uso de las Librerías Scikit-learn y Pytorch
Estudiar el uso de las librerías Scikit-learn y Pytorch.
Definir el concepto de Machine Learning.
Identificar las principales aplicaciones de Scikit-learn y Pytorch.

<!-- Slide number: 16 -->
# Aprendiendo con Scikit-learn y PyTorch

Aplicando Machine Learning de forma práctica

<!-- Slide number: 17 -->
# ¿Qué haremos hoy?
Reto 1: Clasificación de flores con Scikit-learn
Reto 2: Construcción de una red neuronal básica con PyTorch
Exploramos resultados y visualizamos predicciones en tiempo real.

<!-- Slide number: 18 -->
# Machine Learning?
“Es una rama de la inteligencia artificial que permite a las máquinas aprender patrones de datos para hacer predicciones o tomar decisiones sin ser programadas explícitamente.”

![Part II: Robots are reading receipts! And everything else you need to know about deep learning](Picture2.jpg)

<!-- Slide number: 19 -->
# Tipos de Machine Learning:
Aprendizaje supervisado: Se entrena un modelo con datos etiquetados (ej. clasificación).

Aprendizaje no supervisado: Se encuentran patrones en datos no etiquetados (ej. agrupamiento).

![Diferencia entre aprendizaje supervisado y NO supervisado | Machine Learning 101](Picture3.jpg)

![Diferencia entre aprendizaje supervisado y NO supervisado | Machine Learning 101](Picture3.jpg)

<!-- Slide number: 20 -->
# Ejemplo práctico

![](Marcadordecontenido4.jpg)

<!-- Slide number: 21 -->
# Scikit-learn para Machine Learning
Definición de Scikit-learn: Librería de Python usada para crear modelos de Machine Learning.
Modelos de clasificación (k-NN, SVM).
Modelos de regresión (Regresión lineal, regresión logística).
Evaluación de modelos (precisión, recall, etc.).

![scikit-learn](Picture2.jpg)

<!-- Slide number: 22 -->
# Modelo de clasificación con k-NN:

![](Marcadordecontenido4.jpg)

<!-- Slide number: 23 -->
# Entrenar un modelo de clasificación utilizando el dataset Iris
Instrucciones:
Dividir el dataset en entrenamiento y prueba.
Entrenar un modelo con k-NN.
Evaluar el modelo usando la precisión.

![Scikit-learn, the Iris Dataset, and Machine Learning: The Journey to a New Skill | by Trayshawn Webb | Medium](Picture2.jpg)

<!-- Slide number: 24 -->
# Pytorch para Deep Learning
Pytorch es una librería de deep learning que permite construir redes neuronales dinámicas y flexibles.

![](Imagen4.jpg)

<!-- Slide number: 25 -->
# Reto 1 – Clasificación con Scikit-learn

![](Imagen7.jpg)

<!-- Slide number: 26 -->
# Visualiza las predicciones

![](Imagen5.jpg)

<!-- Slide number: 27 -->
# Reto 2 – Red Neuronal con PyTorch

![](Imagen5.jpg)

<!-- Slide number: 28 -->
# Entrenamiento del modelo PyTorch

![](Imagen5.jpg)

<!-- Slide number: 29 -->
# ¿Qué aprendimos?
Scikit-learn: ideal para prototipado rápido y algoritmos clásicos
PyTorch: potencia total para redes neuronales personalizadas
Ambos permiten construir soluciones de IA con pocas líneas de código

<!-- Slide number: 30 -->
# Retos adicionales
Reto Scikit-learn: Clasificar imágenes con digits dataset
Reto PyTorch: Red neuronal para XOR
Proyecto libre: Detectar si un texto es positivo o negativo (NLP)

<!-- Slide number: 31 -->
# Conceptos Técnicos Clave
Scikit-learn:
- load_iris(): carga datos de flores
- train_test_split(): divide en entrenamiento/prueba
- KNeighborsClassifier(): modelo basado en vecinos
- fit(): entrena el modelo
- predict(): hace predicciones
- score(): mide precisión

 PyTorch:
- torch.tensor(): crea datos numéricos
- nn.Module: base de una red neuronal
- nn.Linear(): capa lineal
- sigmoid(): activa la salida (0 a 1)
- BCELoss(): función de error para clasificaciones
- SGD(): optimizador para entrenar
- backward() y step(): actualiza pesos

<!-- Slide number: 32 -->