# 🤖 Sesión 03 — Fundamentos de Machine Learning con Scikit-Learn y PyTorch

<p>
<a href="../../README.md"><img src="https://img.shields.io/badge/⬅️_Menú_principal-333333?style=for-the-badge" /></a>
<a href="../01_PANDAS"><img src="https://img.shields.io/badge/◀️_Sesión_anterior_(Pandas)-6c757d?style=for-the-badge" /></a>
</p>

## 🎯 Objetivo

Explicar los fundamentos del Machine Learning utilizando **Scikit-Learn** y **PyTorch**, identificando con claridad los conceptos de entrenamiento, validación y evaluación de modelos.

## 📖 Teoría

**Machine Learning** es el campo de la IA que permite a las computadoras aprender patrones a partir de datos, en vez de seguir instrucciones explícitas para cada tarea.

- **Aprendizaje supervisado**: el modelo se entrena con datos ya etiquetados (la respuesta correcta viene incluida).
- **Aprendizaje no supervisado**: no hay etiquetas; el modelo busca estructuras o patrones ocultos por sí solo.
- **Red neuronal artificial (RNA)**: modelo computacional inspirado en el cerebro, compuesto por neuronas organizadas en capas.
- **Deep Learning**: rama del ML que usa redes neuronales profundas (múltiples capas) para aprender representaciones complejas de los datos.

### Scikit-Learn vs PyTorch

| | Scikit-Learn | PyTorch |
|---|---|---|
| Enfoque | ML clásico (baja/moderada complejidad) | Deep Learning (redes neuronales profundas) |
| Aplicaciones | Clasificación, regresión, clustering, reducción de dimensionalidad, detección de anomalías | CNN, RNN, Transformers, visión por computadora, NLP, generación de contenido |
| Hardware | No requiere GPU | Aprovecha GPU para acelerar el entrenamiento |
| Estructura de datos | Arrays de NumPy | Tensores (arrays multidimensionales propios) |

### Flujo típico de un modelo (ciclo ML supervisado)

1. Cargar el dataset (ej. `load_iris`, `load_wine`).
2. Explorar los datos con Pandas.
3. Dividir en entrenamiento/prueba con `train_test_split` (típicamente 80/20).
4. Entrenar el modelo con `.fit()` (ej. `DecisionTreeClassifier`).
5. Predecir con `.predict()`.
6. Comparar predicción vs. realidad (métricas, gráficos).

## 🗒️ Conclusión de la sesión

Scikit-Learn es ideal para ML tradicional con datos de complejidad baja/moderada. PyTorch está enfocado en Deep Learning, aprovechando GPU para modelos más complejos (CNN, RNN, GANs).
