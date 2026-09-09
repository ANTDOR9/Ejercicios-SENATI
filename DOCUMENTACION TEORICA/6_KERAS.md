<!-- Slide number: 1 -->
# DEEP LEARNING CON KERAS - PYTHON
Sesión N° 06
Instructor: Jesús Romero Villanueva

### Notes:

<!-- Slide number: 2 -->
# OBJETIVO
Dadas las orientaciones del instructor y el análisis conceptual del tema, el participante será capaz de explicar los fundamentos del Deep Learning utilizando la biblioteca Keras, identificando con claridad los principales componentes y estructuras de modelos de redes neuronales, conforme a los lineamientos de calidad educativa establecidos en la norma ISO 21001:2018, según los criterios establecidos para la sesión.

### Notes:

<!-- Slide number: 3 -->
# OBJETIVO
Dadas las orientaciones del instructor y el análisis conceptual del tema, el participante será capaz de explicar los fundamentos del Deep Learning utilizando la biblioteca Keras, identificando con claridad los principales componentes y estructuras de modelos de redes neuronales, conforme a los lineamientos de calidad educativa establecidos en la norma ISO 21001:2018, según los criterios establecidos para la sesión.

### Notes:

<!-- Slide number: 4 -->
#
“Con Keras, las redes neuronales dejan de ser abstracción y se vuelven pensamiento estructurado.”

### Notes:

<!-- Slide number: 5 -->
# Importancia de los paquetes para trabajar redes neuronales - KERAS

![Qué es el aprendizaje automático](GoogleShape98p4.jpg)

### Notes:

<!-- Slide number: 6 -->
# DeepLearning
Se centra en algoritmos y modelos computacionales inspirados en la estructura y función del cerebro humano, conocida como redes neuronales artificiales. Se caracteriza por utilizar redes neuronales profundas, que son capaces de aprender y realizar tareas complejas directamente a partir de datos, sin requerir programación específica para cada tarea

![What Are Some Tips And Tricks For Training Deep Neural Networks?](GoogleShape105p5.jpg)

### Notes:

<!-- Slide number: 7 -->
# ¿Qué es Keras?
Keras es una biblioteca de código abierto para redes neuronales en Python.
Proporciona una API simple y elegante para la construcción y entrenamiento de modelos de aprendizaje profundo.

![Build your first Deep Learning Basic model using Keras, Python and Tensorflow step by step approach | by Akash Deep | Analytics Vidhya | Medium](GoogleShape112p6.jpg)

### Notes:

<!-- Slide number: 8 -->
# Características Principales
Simple y modular: Facilita la creación rápida de prototipos.
Extensible: Puede integrarse con TensorFlow, Theano y otras bibliotecas de aprendizaje profundo.
Enfoque en la facilidad de uso: Diseñado para que los usuarios puedan experimentar fácilmente con ideas y modelos.

![Build Your Deep Learning Model In Keras Or Tensorflow Using, 42% OFF](GoogleShape119p7.jpg)

### Notes:

<!-- Slide number: 9 -->
# TIPOS DE REDES NEURONALES Y FUNCIONES DE ACTIVACIÓN
Instructor: Jesús Romero Villanueva
Sesión N° 06

### Notes:

<!-- Slide number: 10 -->
# OBJETIVO
Dadas las orientaciones del instructor y el análisis conceptual del tema, el participante será capaz de analizar los tipos de redes neuronales y las funciones de activación, relacionando sus características y aplicaciones con el funcionamiento de modelos de Inteligencia Artificial, conforme a los lineamientos de calidad educativa establecidos en la norma ISO 21001:2018, según los criterios establecidos para la sesión.

### Notes:

<!-- Slide number: 11 -->
# Tipos de redes neuronales
| Red | ¿Qué hace? | ¿Cuándo usarla? |
| --- | --- | --- |
| MLP | Clasifica o predice datos tabulares | Problemas generales, predicción simple |
| CNN | Detecta patrones en imágenes | Visión por computadora (fotos, escaneos) |
| RNN | Procesa secuencias | Texto, música, series de tiempo |
| LSTM / GRU | Recuerda contexto largo en secuencias | Traducción, chatbots, voz |
| Transformer | Procesa texto en paralelo (muy potente) | ChatGPT, traducción automática, BERT |

### Notes:

<!-- Slide number: 12 -->
# Funciones de activación
| Función | Fórmula / Descripción | ¿Cuándo usarla? |
| --- | --- | --- |
| ReLU | f(x) = max(0, x) | En capas ocultas (CNN, MLP, etc.) |
| Sigmoid | f(x) = 1 / (1 + e^-x) | Clasificación binaria (salida) |
| Tanh | f(x) = (e^x - e^-x)/(e^x + e^-x) | Mejor que Sigmoid en capas ocultas |
| Leaky ReLU | f(x) = x si x>0, 0.01x si x<0 | Variante de ReLU para evitar neuronas muertas |
| Softmax | f(xᵢ) = e^(xᵢ) / ∑ e^(xⱼ) | Para clasificación multiclase (salida) |

### Notes:

<!-- Slide number: 13 -->
# Clasificación BINARIA
La clasificación binaria es un tipo de problema de aprendizaje supervisado en el que el objetivo es predecir una de las dos clases posibles para cada instancia de entrada. Estas dos clases suelen etiquetarse como positiva (1) y negativa (0), o como clase 1 y clase 0. Ejemplos comunes de problemas de clasificación binaria incluyen:

![Aprendizaje Supervisado: Introducción a la Clasificación y Principales Algoritmos | by Victor Roman | Ciencia y Datos | Medium](GoogleShape152p10.jpg)

### Notes:

<!-- Slide number: 14 -->
# Clasificación BINARIA
Detección de Spam: Clasificar correos electrónicos como spam (positivo) o no spam (negativo).
Diagnóstico Médico: Clasificar pacientes como enfermos (positivo) o sanos (negativo) basándose en síntomas y pruebas.
Predicción de Fraude: Determinar si una transacción es fraudulenta (positiva) o legítima (negativa).

![Inteligencia artificial ya supera a médicos en el diagnóstico de cáncer | Cáncer | Salud | IA | Diagnóstico | CHEKA | PERU21](GoogleShape159p11.jpg)

### Notes:

<!-- Slide number: 15 -->
# Clasificación NO BINARIA
La clasificación no binaria, o multiclase, implica predecir una de varias clases posibles para cada instancia de entrada. En este caso, el número de clases es mayor que dos. Por ejemplo:

![Algoritmo de clasificación: definición y modelos principales](GoogleShape166p12.jpg)

### Notes:

<!-- Slide number: 16 -->
# Clasificación NO BINARIA
Clasificación de Imágenes: Identificar si una imagen contiene un gato, un perro o un pájaro (tres clases).
Clasificación de Texto: Determinar la categoría de un artículo de noticias entre deportes, política, tecnología, etc. (varias clases).

![Textos generados por IA: ¿El futuro de Internet? - Blog IDA Chile | Estrategia para el éxito de tu negocio](GoogleShape173p13.jpg)

### Notes:

<!-- Slide number: 17 -->
# Conceptos clave
1. Redes Neuronales Artificiales (ANNs)
Las Redes Neuronales Artificiales son el fundamento teórico de Keras. Estas redes están inspiradas en el funcionamiento del cerebro humano y están compuestas por capas de neuronas artificiales interconectadas. Keras permite la construcción de redes neuronales profundas (DNNs), que son redes con múltiples capas ocultas entre la entrada y la salida.

![Redes Neuronales artificiales | Blog Xeridia](GoogleShape180p14.jpg)

### Notes:

<!-- Slide number: 18 -->
# Conceptos clave
2. Aprendizaje Supervisado y No Supervisado
Keras se utiliza principalmente en problemas de aprendizaje supervisado, donde se entrenan modelos utilizando datos etiquetados (entrada y salida esperada). Sin embargo, también se puede adaptar para aplicaciones de aprendizaje no supervisado, como la generación de modelos de lenguaje (usando técnicas como redes generativas adversariales, GANs).

![Diferencia aprendizaje supervisado y no supervisado 3](GoogleShape187p15.jpg)

### Notes:

<!-- Slide number: 19 -->
# Conceptos clave
3. Optimización y Funciones de Pérdida
El proceso de entrenamiento de modelos en Keras implica la optimización de parámetros del modelo utilizando algoritmos como el descenso de gradiente estocástico (SGD) y sus variantes (Adam, RMSprop). La función de pérdida (loss function) define cómo se mide el error entre las predicciones del modelo y las etiquetas reales, siendo esencial para el proceso de optimización.

![Regresión lineal y descenso de gradiente con Python](GoogleShape194p16.jpg)

### Notes:

<!-- Slide number: 20 -->
# Conceptos clave
4. Regularización y Reducción del Sobreajuste
Keras facilita la implementación de técnicas de regularización como L1 y L2 para prevenir el sobreajuste (overfitting). El sobreajuste ocurre cuando un modelo se ajusta demasiado a los datos de entrenamiento y no generaliza bien a nuevos datos. La regularización ayuda a controlar la complejidad del modelo.

![Entendiendo el Sobreajuste en los Modelos de Machine Learning | by Jorge Luis | Medium](GoogleShape201p17.jpg)

### Notes:

<!-- Slide number: 21 -->
# Conceptos clave
5. Validación Cruzada y Evaluación del Modelo
Para evaluar la capacidad de generalización de un modelo entrenado, es crucial utilizar técnicas como la validación cruzada (cross-validation) y métodos de evaluación de rendimiento como precisión (accuracy), precisión-recall, ROC-AUC, entre otros. Keras proporciona herramientas para realizar estas evaluaciones de manera efectiva.

![Evaluación de errores en los modelos de Machine Learning - Azure Machine Learning | Microsoft Learn](GoogleShape208p18.jpg)

### Notes:

<!-- Slide number: 22 -->
# Conceptos clave
6. Redes Neuronales Convolucionales (CNNs) y Recurrentes (RNNs)
Keras es compatible con arquitecturas avanzadas como CNNs para procesamiento de imágenes y RNNs para secuencias de datos temporales, como texto o series temporales. Estas arquitecturas están optimizadas para capturar patrones espaciales y temporales respectivamente, ofreciendo flexibilidad en la implementación de modelos complejos.

![Red neuronal convolucional 4 | Download Scientific Diagram](GoogleShape215p19.jpg)

### Notes:

<!-- Slide number: 23 -->
# Conceptos clave
7. TensorFlow y Otros Backends
Keras puede utilizar varios backends de computación numérica, siendo TensorFlow el más utilizado. Otros backends incluyen Theano y Microsoft Cognitive Toolkit (CNTK). TensorFlow proporciona una base robusta y eficiente para la ejecución de operaciones matemáticas en hardware diverso, desde CPUs y GPUs hasta TPUs.

![Implementar proyectos de IA | OVHcloud Global](GoogleShape222p20.jpg)

### Notes:

<!-- Slide number: 24 -->
# Conceptos clave
8. Aprendizaje Profundo y Representaciones Jerárquicas
El aprendizaje profundo (deep learning) se centra en el aprendizaje de representaciones jerárquicas de datos, donde las características se extraen automáticamente a través de múltiples capas de transformación no lineal. Keras simplifica este proceso al ofrecer una interfaz intuitiva y modular para construir y entrenar redes profundas.

![Hacía el entendimiento del aprendizaje profundo y su aplicación en seguridad informática](GoogleShape229p21.jpg)

### Notes:

<!-- Slide number: 25 -->
# Conceptos clave
9. Desarrollo Rápido de Prototipos y Experimentación
Una de las ventajas principales de Keras es su diseño orientado al usuario, que permite a los desarrolladores experimentar rápidamente con diferentes arquitecturas de modelos y configuraciones de entrenamiento. Esto facilita la innovación y la iteración en proyectos de inteligencia artificial.

![Los 10 mejores proyectos de Machine Learning si eres Principiante](GoogleShape236p22.jpg)

### Notes:

<!-- Slide number: 26 -->
# Ejemplo 1

![](GoogleShape242p23.jpg)

![](GoogleShape243p23.jpg)

### Notes:

<!-- Slide number: 27 -->
# Conclusión
Keras es una herramienta poderosa para la creación de modelos de redes neuronales.
Facilita la experimentación y el desarrollo rápido de prototipos.
Integración perfecta con TensorFlow proporciona un entorno robusto para el aprendizaje profundo.

![Las claves de un proyecto de investigación | UCALP](GoogleShape250p24.jpg)

### Notes:

<!-- Slide number: 28 -->

### Notes: