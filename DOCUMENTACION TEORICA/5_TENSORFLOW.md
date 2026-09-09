<!-- Slide number: 1 -->
# DEEP LEARNING TENSORFLOW - PYTHON
Sesión N° 05
Instructor: Jesús Romero Villanueva

### Notes:

<!-- Slide number: 2 -->
# OBJETIVO
Dadas las orientaciones del instructor y el análisis conceptual del tema, el participante será capaz de explicar los fundamentos del Deep Learning utilizando la biblioteca TensorFlow, identificando con claridad los principales conceptos  de redes neuronales, conforme a los lineamientos de calidad educativa establecidos en la norma ISO 21001:2018, según los criterios establecidos para la sesión.

### Notes:

<!-- Slide number: 3 -->
# Iniciando…
“Con TensorFlow, el Deep Learning imita el misterio de la mente: capas de aprendizaje que transforman datos en comprensión.”

### Notes:

<!-- Slide number: 4 -->
# Importancia del paquete Tensowflow

![Qué es el aprendizaje automático](GoogleShape91p4.jpg)

### Notes:

<!-- Slide number: 5 -->
# I.A ???
Capacidad que tienen las máquinas para aprender a hacer tareas que normalmente requieren inteligencia humana

![Inteligencia Artificial y Big Data en los negocios, ¿Qué efectos tuvo el COVID-19 en estas tendencias? – DATLAS Investigación – Blog Datlas](GoogleShape98p5.jpg)

### Notes:

<!-- Slide number: 6 -->
# ¿Qué es un modelo de IA?
Un modelo de IA es un sistema que aprende patrones a partir de datos para hacer predicciones o tomar decisiones.

![Guía paso a paso para crear tu propio modelo de IA sin saber programar – Brain and code tech](GoogleShape105p6.jpg)

### Notes:

<!-- Slide number: 7 -->
# Tipos de modelos según la tarea
Regresión: predice valores continuos (ej. precio de una casa).
Clasificación: predice categorías (ej. spam o no spam).
Clustering: agrupa sin etiquetas (ej. segmentación de clientes).
Redes neuronales profundas (Deep Learning):
MLP (Perceptrón Multicapa)
CNN (Redes Convolucionales) – visión por computadora
RNN/LSTM – datos secuenciales como texto o series temporales

### Notes:

<!-- Slide number: 8 -->
# Datos VS Información
Hechos brutos y sin procesar que describen eventos, medidas, transacciones, etc. Los datos pueden ser simples observaciones o registros de eventos, pero por sí solos no tienen significado ni contexto.
Resultado del procesamiento y organización de los datos para que tengan sentido y utilidad. La información implica que los datos han sido interpretados, estructurados o resumidos de alguna manera que sea comprensible para los usuarios o sistemas.

![Datos GIF - Conseguir el mejor gif en GIFER](GoogleShape121p8.jpg)

![Transforma los datos empresariales en insights | Partner Power BI](GoogleShape119p8.jpg)
DATOS                            INFORMACIÓN           SENATINO

### Notes:

<!-- Slide number: 9 -->
# DeepLearning
Se centra en algoritmos y modelos computacionales inspirados en la estructura y función del cerebro humano, conocida como redes neuronales artificiales. Se caracteriza por utilizar redes neuronales profundas, que son capaces de aprender y realizar tareas complejas directamente a partir de datos, sin requerir programación específica para cada tarea

![What Are Some Tips And Tricks For Training Deep Neural Networks?](GoogleShape128p9.jpg)

### Notes:

<!-- Slide number: 10 -->
# Deep Learning
Lo que distingue al deep learning es su capacidad para aprender representaciones de datos a través de múltiples capas de procesamiento, conocidas como redes neuronales profundas.

![Deep Learning Tutorial: What is Deep Learning? - Intellipaat](GoogleShape135p10.jpg)

### Notes:

<!-- Slide number: 11 -->
# ¿Qué es TensorFlow?
•  Definición: TensorFlow es una biblioteca de código abierto para computación numérica y aprendizaje automático desarrollada por Google Brain.
•  Objetivo: Permite construir y entrenar modelos de aprendizaje automático, especialmente redes neuronales profundas.
•  Características: Escalable, flexible y optimizada para un rendimiento de computación intensivo en diferentes plataformas (CPU, GPU, TPU).

![TensorFlow: A Beginner's Guide to the Basics | by Suraj Yadav | Medium](GoogleShape142p11.jpg)

### Notes:

<!-- Slide number: 12 -->
# Características de TensorFlow
Arquitectura Flexible: Permite construir y desplegar modelos desde dispositivos móviles hasta clusters de servidores.
Computación Distribuida: Soporte para distribución de entrenamiento y evaluación en múltiples dispositivos y plataformas.
Optimización de Rendimiento: Utiliza aceleradores de hardware como GPUs y TPUs para mejorar la velocidad de entrenamiento y evaluación.

![5 ventajas de hacer Deep Learning con TensorFlow](GoogleShape149p12.jpg)

### Notes:

<!-- Slide number: 13 -->
# Componentes de TensorFlow
Tensores: Unidades fundamentales de datos en TensorFlow, similares a matrices multidimensionales.
Operaciones: Define las operaciones matemáticas sobre tensores, construyendo así grafos computacionales.
Grafos Computacionales: Representación de las operaciones y dependencias como un grafo para la ejecución eficiente en diferentes dispositivos.

![Optimizing any TensorFlow model using TensorFlow Transform Tools and using TensorRT | by Alex Punnen | Better Software | Medium](GoogleShape156p13.jpg)

### Notes:

<!-- Slide number: 14 -->
# Ejemplo Técnico

![](GoogleShape162p14.jpg)

![](GoogleShape163p14.jpg)

### Notes:

<!-- Slide number: 15 -->
# Ejemplo Técnico

![](GoogleShape170p15.jpg)

![](GoogleShape169p15.jpg)

### Notes:

<!-- Slide number: 16 -->
# Aplicaciones y Casos de Uso
Visión por Computadora: Reconocimiento de imágenes, detección de objetos.
Procesamiento del Lenguaje Natural: Traducción automática, análisis de sentimientos.
Modelos de Aprendizaje Profundo: Redes neuronales convolucionales, recurrentes, y más.

![Construyendo el buen uso de la inteligencia artificial](GoogleShape177p16.jpg)

### Notes:

<!-- Slide number: 17 -->
# Terminología clave – RNA TENSORFLOW
Capa (Layer): Un componente de la red neuronal que realiza transformaciones en los datos. Algunas capas comunes son:
Capa Densa (Dense Layer): También conocida como capa completamente conectada, cada neurona está conectada a todas las neuronas de la capa anterior.
Capa de Convolución (Convolutional Layer): Utilizada principalmente en redes neuronales convolucionales (CNN) para extraer características espaciales de los datos.
Capa de Normalización (Normalization Layer): Normaliza las salidas de una capa para estabilizar y acelerar el entrenamiento, como BatchNormalization.
Capa de Activación (Activation Layer): Aplica una función de activación a los datos de entrada, como ReLU (Rectified Linear Unit), Sigmoid, Tanh, etc.

### Notes:

<!-- Slide number: 18 -->
# Terminología clave – RNA TENSORFLOW
Tensor: La unidad básica de datos en TensorFlow. Son arreglos multidimensionales (tensores) que almacenan datos y se utilizan en los cálculos de la red neuronal.

Función de Activación: Una función no lineal aplicada a la salida de una neurona para introducir no linealidad en el modelo. Ejemplos incluyen:

ReLU: f(x) = max(0, x)
Sigmoid: f(x) = 1 / (1 + exp(-x))
Tanh: f(x) = (exp(x) - exp(-x)) / (exp(x) + exp(-x))

### Notes:

<!-- Slide number: 19 -->
# Terminología clave – RNA TENSORFLOW
Red Neuronal: Una arquitectura que consiste en una serie de capas conectadas. Existen varios tipos, como:
Red Neuronal Feedforward (Feedforward Neural Network): Datos pasan en una sola dirección desde la capa de entrada hasta la capa de salida.
Red Neuronal Convolucional (Convolutional Neural Network, CNN): Utiliza capas convolucionales para procesar datos con estructura espacial (como imágenes).
Red Neuronal Recurrente (Recurrent Neural Network, RNN): Tiene conexiones recurrentes que permiten manejar secuencias de datos (como texto o series temporales).

### Notes:

<!-- Slide number: 20 -->
# Terminología clave – RNA TENSORFLOW
Modelo: Una combinación de capas y funciones de activación que se utilizan para hacer predicciones. En TensorFlow, puedes construir modelos usando la API tf.keras, como:

tf.keras.Sequential: Para construir modelos capa por capa en una secuencia lineal.
tf.keras.Model: Permite definir modelos más complejos con múltiples entradas y salidas.

### Notes:

<!-- Slide number: 21 -->
# Terminología clave – RNA TENSORFLOW
Compilación: Configuración del modelo antes del entrenamiento, especificando el optimizador, la función de pérdida y las métricas.

Función de Pérdida (Loss Function): Mide la diferencia entre las predicciones del modelo y los valores reales. Ejemplos incluyen:

sparse_categorical_crossentropy: Para clasificación multiclase con etiquetas enteras.
mean_squared_error: Para problemas de regresión.
binary_crossentropy: Para clasificación binaria.

### Notes:

<!-- Slide number: 22 -->
# Terminología clave – RNA TENSORFLOW
Optimizador: Algoritmo que ajusta los pesos del modelo para minimizar la función de pérdida. Ejemplos incluyen:
Adam: Un optimizador basado en gradientes que ajusta el learning rate adaptativamente.
SGD: Stochastic Gradient Descent, un método de optimización que actualiza los pesos usando mini-lotes de datos.

### Notes:

<!-- Slide number: 23 -->
# Terminología clave – RNA TENSORFLOW
Entrenamiento (Training): Proceso de ajustar los pesos del modelo usando datos de entrenamiento. Se realiza mediante el método fit en TensorFlow.
Época (Epoch): Una iteración completa a través del conjunto de datos de entrenamiento.

Batch Size: El número de ejemplos procesados antes de actualizar el modelo.

Validación (Validation): Proceso de evaluar el modelo en un conjunto de datos separado del entrenamiento para verificar su rendimiento y evitar el sobreajuste (overfitting).

Predicción (Prediction): Utilizar el modelo entrenado para hacer inferencias sobre datos nuevos.

### Notes:

<!-- Slide number: 24 -->
# Terminología clave – RNA TENSORFLOW
Checkpoint: Guardar el estado del modelo en intervalos durante el entrenamiento para poder recuperarlo en caso de interrupciones o para continuar el entrenamiento más tarde.

TensorBoard: Herramienta de visualización que permite monitorear el entrenamiento, las métricas y los gráficos del modelo.

Regularización: Técnicas para prevenir el sobreajuste, como la regularización L1/L2 y el dropout.

### Notes:

<!-- Slide number: 25 -->
# Conclusión
TensorFlow es una herramienta esencial en el campo del aprendizaje automático y la inteligencia artificial.
Proporciona una plataforma robusta y escalable para construir y desplegar modelos complejos.
Es utilizado ampliamente en investigación y aplicaciones comerciales debido a su flexibilidad y rendimiento.

![Las claves de un proyecto de investigación | UCALP](GoogleShape232p25.jpg)

### Notes:

<!-- Slide number: 26 -->

### Notes: