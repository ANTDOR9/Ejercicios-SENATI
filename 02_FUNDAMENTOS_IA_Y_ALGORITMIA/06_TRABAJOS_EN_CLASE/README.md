# 🧪 06 — Trabajos en clase (octubre)

<p>
<a href="../README.md"><img src="https://img.shields.io/badge/⬅️_Menú_del_curso-333333?style=for-the-badge" /></a>
<a href="../05_INVESTIGACION_EXTRA"><img src="https://img.shields.io/badge/◀️_Anterior_(Investigación_extra)-6c757d?style=for-the-badge" /></a>
<a href="../07_TRABAJO_FINAL"><img src="https://img.shields.io/badge/▶️_Siguiente_(Trabajo_final)-6c757d?style=for-the-badge" /></a>
</p>

## 🎯 Objetivo

Aplicar modelos clásicos de clasificación de scikit-learn (Regresión Logística, Árbol de Decisión, KNN y SVM) sobre distintos datasets, y compararlos con métricas de evaluación.

## 📂 Contenido

| Archivo | Fecha | Tema |
|---|---|---|
| [`01_01oct_regresion_logistica_cancer_mama.ipynb`](01_01oct_regresion_logistica_cancer_mama.ipynb) | 01/10 | Regresión Logística con el dataset de cáncer de mama |
| [`02_02oct_regresion_logistica_titanic.ipynb`](02_02oct_regresion_logistica_titanic.ipynb) | 02/10 | Regresión Logística con el Titanic (`fetch_openml`) |
| [`03_03oct_arbol_decision_mnist.ipynb`](03_03oct_arbol_decision_mnist.ipynb) | 03/10 | Árbol de Decisión con MNIST |
| [`04_04oct_comparacion_arbol_knn_fashion_mnist.ipynb`](04_04oct_comparacion_arbol_knn_fashion_mnist.ipynb) | 04/10 | Comparación Árbol de Decisión vs. KNN con Fashion-MNIST |
| [`05_taller_svm_rostros_profesor.ipynb`](05_taller_svm_rostros_profesor.ipynb) | — | Práctica del profesor: SVM con rostros (LFW). Tarea: mejorar el código |

## 🗒️ Conclusión

Con scikit-learn todos los modelos siguen el mismo flujo: separar datos, escalar, `fit`, `predict` y evaluar con `accuracy_score` y `classification_report`. Cambiar de modelo es cambiar una sola línea, lo que facilita compararlos con los mismos datos.
