# 🧠 Sesión 05 — Deep Learning con TensorFlow y Keras

<p>
<a href="../../README.md"><img src="https://img.shields.io/badge/⬅️_Menú_principal-333333?style=for-the-badge" /></a>
<a href="../02_SCIKIT_LEARN"><img src="https://img.shields.io/badge/◀️_Sesión_anterior_(Scikit--Learn)-6c757d?style=for-the-badge" /></a>
</p>

## 🎯 Objetivo

Explicar los fundamentos del Deep Learning utilizando **TensorFlow** (con la API **Keras**), identificando con claridad los principales conceptos de redes neuronales.

## 📖 Teoría

**TensorFlow** es una biblioteca de código abierto para computación numérica y aprendizaje automático (desarrollada por Google Brain), optimizada para CPU, GPU y TPU. Su unidad básica de dato es el **Tensor** (arreglo multidimensional).

**Keras** (`tf.keras`) es la API de alto nivel de TensorFlow para construir redes neuronales capa por capa, de forma mucho más simple que manejar los tensores directamente.

### Terminología clave

| Término | Significado |
|---|---|
| **Capa (Layer)** | Componente que transforma los datos. La más común es `Dense` (cada neurona conectada a todas las de la capa anterior) |
| **Función de activación** | Introduce no linealidad: `ReLU`, `Sigmoid`, `Tanh`, `Softmax` |
| **Modelo** | Combinación de capas, ej. `tf.keras.Sequential` (capa por capa, lineal) |
| **Compilación** | Configura el optimizador, la función de pérdida y las métricas antes de entrenar |
| **Función de pérdida (Loss)** | Mide qué tan lejos está la predicción de la realidad |
| **Optimizador** | Ajusta los pesos para minimizar la pérdida (`Adam`, `SGD`) |
| **Entrenamiento (`fit`)** | Proceso de ajustar los pesos con los datos de entrenamiento |
| **Época (Epoch)** | Una pasada completa por todo el set de entrenamiento |

### Activación y loss según el tipo de problema

| Tipo de problema | Activación de salida | Función de pérdida |
|---|---|---|
| Regresión | `linear` | `mean_squared_error` (mse) |
| Clasificación binaria | `sigmoid` | `binary_crossentropy` |
| Clasificación multiclase | `softmax` | `sparse_categorical_crossentropy` (etiquetas enteras) |

Interpretación de la salida: con `sigmoid` se redondea (`np.round`) para obtener 0/1; con `softmax` se usa `argmax` para obtener la clase más probable.

## 🗒️ Conclusión de la sesión

TensorFlow/Keras permite construir redes neuronales completas con pocas líneas: se define la arquitectura (`Sequential` + capas `Dense`), se compila (optimizador + loss según el problema), se entrena (`fit`) y se interpreta la salida según la activación usada.
