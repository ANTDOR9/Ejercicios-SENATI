# 🏁 07 — Trabajo Final: Seeds Dataset

<p>
<a href="../README.md"><img src="https://img.shields.io/badge/⬅️_Menú_del_curso-333333?style=for-the-badge" /></a>
<a href="../06_TRABAJOS_EN_CLASE"><img src="https://img.shields.io/badge/◀️_Anterior_(Trabajos_en_clase)-6c757d?style=for-the-badge" /></a>
</p>

## 🎯 Objetivo

Resolver el caso práctico **DataExpert**: aplicar en un mismo proyecto exploración de datos con Pandas, álgebra lineal con NumPy, estadística descriptiva, detección de valores atípicos, visualización y comparación de dos modelos de clasificación.

## 🌾 Dataset

**Seeds** (UCI Machine Learning Repository): 210 semillas de trigo de tres variedades (Kama, Rosa y Canadian), 70 de cada una, con 7 medidas del grano:

`Area` · `Perimeter` · `Compactness` · `KernelLength` · `KernelWidth` · `AsymmetryCoeff` · `KernelGrooveLength` → `Class`

## 📂 Contenido

| Archivo | Descripción |
|---|---|
| [`trabajo_final.ipynb`](trabajo_final.ipynb) | Desarrollo completo de las 7 actividades |
| [`data/seeds_dataset.csv`](data/seeds_dataset.csv) | Dataset con encabezados |
| [`graficos/`](graficos) | Histograma, dispersión y comparación de modelos |

## 📋 Actividades

| # | Actividad | Resultado principal |
|---|---|---|
| 1 | Carga y exploración con Pandas | 7 características, 0 valores nulos, 70 semillas por variedad |
| 2 | Separación de `Class` y `StandardScaler` | Columnas con media 0 y desviación 1 |
| 3 | NumPy: vectores, matrices, producto punto, norma, sistema de ecuaciones | Recta Perimeter = 0.481·Area + 7.50 resuelta con `np.linalg.solve` |
| 4 | Media, mediana, varianza y desviación de Area y Perimeter | Implementación manual igual a NumPy |
| 5 | Atípicos en Area (±2 desviaciones) | 4 semillas Rosa con Area > 20.65 |
| 6 | Histograma de Area y dispersión Area vs. Perimeter | Las variedades forman grupos separados |
| 7 | KNN vs. Árbol de Decisión | **KNN 90.48 %** · Árbol 88.10 % |

## ⚙️ Cómo ejecutar

```bash
pip install numpy pandas matplotlib seaborn scikit-learn jupyter
```

Abrir `trabajo_final.ipynb` desde esta carpeta (para que encuentre `data/`) y ejecutar todas las celdas en orden.
