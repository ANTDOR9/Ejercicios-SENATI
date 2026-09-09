<!-- Slide number: 1 -->
# Fundamentos de Machine Learning con Scikitlearn y Pytorch
Sesión N° 03
Instructor: Jesús Romero Villanueva

### Notes:

<!-- Slide number: 2 -->
# OBJETIVO
Dadas las orientaciones del instructor y el análisis conceptual del tema, el participante será capaz de explicar los fundamentos del Machine Learning utilizando las bibliotecas Scikit-Learn y PyTorch, identificando con claridad los conceptos de entrenamiento, validación y evaluación de modelos, conforme a los lineamientos de calidad educativa establecidos en la norma ISO 21001:2018, según los criterios establecidos para la sesión.

### Notes:

<!-- Slide number: 3 -->
# INICIANDO…
“Machine Learning no predice el futuro; interpreta las huellas que el pasado dejó en los datos.”

### Notes:

<!-- Slide number: 4 -->
# Antes de iniciar…
Importancia del manejo de los módulos para Machine Learning y Deep Learning
¿Cuál es la diferencia entre Machine y Deep Learning?

![Diferencias entre Machine Learning y Deep Learning | OpenWebinars](GoogleShape93p3.jpg)

### Notes:

<!-- Slide number: 5 -->
# Machine Learning
Campo de la inteligencia artificial (IA) que se centra en el desarrollo de técnicas que permiten a las computadoras aprender automáticamente a partir de datos y realizar tareas específicas sin una programación explícita para cada tarea.

![Python for Machine Learning — Libraries, ML Algorithms and Functionality | LITSLINK Blog](GoogleShape100p4.jpg)

### Notes:

<!-- Slide number: 6 -->

![Barry Pollard on X: "@rmondello @KonstantinRouda @css Heuristics. You mean AI? 😀 https://t.co/jUACNP3Cwc" / X](GoogleShape106p5.jpg)
# JAJAJA...

### Notes:

<!-- Slide number: 7 -->
# Principales aplicaciones
| Biblioteca | Principales Aplicaciones |
| --- | --- |
| Scikit-learn | - Clasificación (spam, diagnóstico médico) |
|  | - Regresión (predicción de precios, temperatura) |
|  | - Agrupamiento o clustering (segmentación de clientes) |
|  | - Reducción de dimensionalidad (PCA, t-SNE) |
|  | - Detección de anomalías (fraude, valores atípicos) |
|  | - Preprocesamiento de datos (escalado, codificación, imputación) |
| PyTorch | - Redes neuronales profundas (MLP, CNN, RNN, Transformers) |
|  | - Visión por computadora (clasificación, detección y segmentación de imágenes) |
|  | - Procesamiento de lenguaje natural (traducción, análisis de sentimientos, chatbots) |
|  | - Generación de contenido (texto, imágenes, música con GANs o autoencoders) |
|  | - Aprendizaje por refuerzo (juegos, robótica, decisiones autónomas) |
|  | - Transfer learning (usar modelos preentrenados para nuevas tareas) |

### Notes:

<!-- Slide number: 8 -->
# Machine Learning
En lugar de seguir instrucciones específicas, las máquinas aprenden patrones y reglas a partir de datos para tomar decisiones o realizar predicciones.

![What is a machine learning model? | Microsoft Learn](GoogleShape119p7.jpg)

### Notes:

<!-- Slide number: 9 -->
# ¿Qué es el Aprendizaje Supervisado?
El aprendizaje supervisado es un tipo de aprendizaje automático en el que el modelo se entrena con datos etiquetados, es decir, datos que ya incluyen la respuesta correcta.

![Introducción al Aprendizaje Supervisado | Dialéktico](GoogleShape126p8.jpg)

### Notes:

<!-- Slide number: 10 -->
# ¿Qué es el Aprendizaje No Supervisado?
El aprendizaje no supervisado se usa cuando no hay etiquetas en los datos. El modelo intenta encontrar estructuras o patrones ocultos en los datos por sí solo.

![Codideep](GoogleShape133p9.jpg)

### Notes:

<!-- Slide number: 11 -->
# ¿Qué es una Red Neuronal?
Una red neuronal artificial (RNA) es un modelo computacional inspirado en el cerebro humano. Está compuesta por neuronas artificiales (también llamadas nodos o unidades) organizadas en capas. Su función principal es aprender patrones a partir de datos.

![Crea tu primera Red Neuronal Artificial – Apuntes de Walther Curo](GoogleShape140p10.jpg)

### Notes:

<!-- Slide number: 12 -->
# Deep Learning
Rama del machine learning que se enfoca en algoritmos inspirados en la estructura y función del cerebro humano, conocidos como redes neuronales artificiales.

![El aprendizaje profundo (deep learning) en la optimización de estructuras – El blog de Víctor Yepes](GoogleShape147p11.jpg)

### Notes:

<!-- Slide number: 13 -->
# Deep Learning
Lo que distingue al deep learning es su capacidad para aprender representaciones de datos a través de múltiples capas de procesamiento, conocidas como redes neuronales profundas.

![convolutional-neural-networks-building-cnn-classifiers-es | AI Planet (formerly DPhi)](GoogleShape154p12.jpg)

### Notes:

<!-- Slide number: 14 -->
# Scikit-learn
Biblioteca de software de aprendizaje automático de código abierto para el lenguaje de programación Python

![Essential Python for Machine Learning: Scikit-learn | by Dagang Wei | Medium](GoogleShape161p13.jpg)

### Notes:

<!-- Slide number: 15 -->
# Scikit-learn / Características
Amplia variedad de algoritmos: Ofrece implementaciones de una amplia gama de algoritmos de aprendizaje supervisado y no supervisado, incluyendo clasificación, regresión, clustering, reducción de dimensionalidad y selección de características.

![](GoogleShape168p14.jpg)

### Notes:

<!-- Slide number: 16 -->
# Scikit-learn / Características
Interfaz consistente: Proporciona una interfaz simple y coherente para trabajar con diferentes algoritmos, lo que facilita el proceso de desarrollo y comparación de modelos.

![Dirección Estratégica: La consistencia en la estrategia](GoogleShape175p15.jpg)

### Notes:

<!-- Slide number: 17 -->
# Scikit-learn / Características
Integración con otras bibliotecas: Se integra bien con otras bibliotecas populares de Python utilizadas en ciencia de datos, como NumPy, SciPy y matplotlib, lo que permite un análisis de datos completo y eficiente.

![Introducción a la librería Scikit-Learn de Python - Aprende IA](GoogleShape182p16.jpg)

### Notes:

<!-- Slide number: 18 -->
# Scikit-learn / Características
Documentación extensa: Ofrece una documentación detallada y ejemplos prácticos que ayudan a los usuarios a comprender cómo utilizar eficazmente las funciones y métodos proporcionados.

![Documentación - Open edX](GoogleShape189p17.jpg)

### Notes:

<!-- Slide number: 19 -->
# Scikit-learn / Características
Licencia de código abierto: Es distribuido bajo la licencia BSD, lo que permite su uso gratuito, modificación y distribución, tanto en aplicaciones comerciales como no comerciales.

![Qué es el código abierto? - Explicación del código abierto - AWS](GoogleShape196p18.jpg)

### Notes:

<!-- Slide number: 20 -->
# Dentro de lo destacado sobre Scikitlearrn
Implementación de Algoritmos
Consistencia
Integración con NumPy y SciPy
Facilidades para Preprocesamiento de Datos
Evaluación de Modelos

### Notes:

<!-- Slide number: 21 -->
# Ejemplo 1

![](GoogleShape208p20.jpg)

![](GoogleShape209p20.jpg)

### Notes:

<!-- Slide number: 22 -->
# PYTORCH
Biblioteca de aprendizaje automático de código abierto desarrollada principalmente por Facebook's AI Research lab (FAIR). Se destaca por ser flexible y diseñada para ser eficiente en cuanto a la velocidad y el manejo de modelos de aprendizaje profundo.

![Python and PyTorch for AI Engineers | Niklas Heidloff](GoogleShape216p21.jpg)

### Notes:

<!-- Slide number: 23 -->
# Puntos clave - PYTORCH
Tensor Manipulation: PyTorch proporciona una abstracción para los tensores, que son estructuras de datos similares a matrices multidimensionales, esenciales para la programación de redes neuronales y otros modelos de aprendizaje automático.

![10 most common Maths Operation with Pytorch Tensor | by Nooras Fatima Ansari | Medium](GoogleShape223p22.jpg)

### Notes:

<!-- Slide number: 24 -->
# Puntos clave - PYTORCH
Computación en GPU: PyTorch está diseñado para aprovechar al máximo las capacidades de las unidades de procesamiento gráfico (GPU), lo que acelera significativamente el entrenamiento de modelos grandes y complejos.

![What Is GPU Computing and How is it Applied Today? | Cherry Servers](GoogleShape230p23.jpg)

### Notes:

<!-- Slide number: 25 -->
# Puntos clave - PYTORCH
Dynamic Computational Graphs: A diferencia de otros frameworks que utilizan gráficos computacionales estáticos, PyTorch utiliza gráficos computacionales dinámicos. Esto significa que los gráficos computacionales se construyen sobre la marcha durante la ejecución, lo cual facilita la depuración y la experimentación interactiva.

![Udemy Gratis: Curso en español de Interfaces Graficas en Python con Tkinter - Facialix](GoogleShape237p24.jpg)

### Notes:

<!-- Slide number: 26 -->
# Puntos clave - PYTORCH
Interfaz Pythonic: PyTorch está diseñado para ser familiar y fácil de usar para los desarrolladores de Python, permitiendo una integración fluida con el ecosistema de Python y otras bibliotecas populares como NumPy.

![Pythonic Way of Writing Code - AskPython](GoogleShape244p25.jpg)

### Notes:

<!-- Slide number: 27 -->
# Puntos clave - PYTORCH
Extensibilidad y Flexibilidad: PyTorch facilita la construcción y personalización de modelos complejos debido a su naturaleza modular y extensible. Además, permite la investigación avanzada en áreas como el aprendizaje por refuerzo, la visión por computadora y el procesamiento de lenguaje natural.

![TOP 12 IDEAS PROYECTOS DE PYTHON PARA PRINCIPIANTES](GoogleShape251p26.jpg)

### Notes:

<!-- Slide number: 28 -->
# Ejercicio 1

![](GoogleShape257p27.jpg)

![](GoogleShape258p27.jpg)

### Notes:

<!-- Slide number: 29 -->
# Conclusiones
Scikit-learn es ideal para tareas de aprendizaje automático tradicional (supervisado y no supervisado) como clasificación, regresión, clustering y reducción de dimensionalidad, especialmente cuando los datos son de baja o moderada complejidad y no requieren GPU.

![15 cosas que debes saber sobre Scikit-learn - Desafío Latam](GoogleShape265p28.jpg)

### Notes:

<!-- Slide number: 30 -->
# Conclusiones
PyTorch está enfocado en el aprendizaje profundo, ideal para construir y entrenar modelos complejos como CNNs, RNNs y GANs, aprovechando el poder de las GPUs para trabajar con grandes volúmenes de datos.

![PyTorch 简介| 菜鸟教程](GoogleShape272p29.jpg)

### Notes:

<!-- Slide number: 31 -->

### Notes: