# 📊 Sesión 01 — Fundamentos de manipulación de datos con Pandas

<p>
<a href="../../README.md"><img src="https://img.shields.io/badge/⬅️_Menú_principal-333333?style=for-the-badge" /></a>
</p>

## 🎯 Objetivo

Analizar los fundamentos de la manipulación de datos con **Pandas** y **NumPy**, relacionando los conceptos de vectores y matrices con las características y utilidad de ambas bibliotecas en el manejo y procesamiento de datos.

## 📖 Teoría

**Pandas** es una biblioteca de Python para la manipulación y análisis de datos, creada por Wes McKinney en 2008. Se apoya en dos estructuras principales:

- **Series**: arreglo unidimensional etiquetado, puede contener cualquier tipo de dato.
- **DataFrame**: estructura tabular bidimensional (filas y columnas), similar a una hoja de Excel o una tabla de base de datos.

**Manipular** los datos es transformarlos, limpiarlos, organizarlos, unirlos o filtrarlos. **Analizar** es sacar conclusiones de ellos: promedios, totales, agrupaciones, resúmenes estadísticos.

### Funciones y métodos clave

| Elemento | Qué hace |
|---|---|
| `pd.DataFrame(data, index, columns)` | Crea una tabla a partir de un diccionario, lista o array |
| `pd.Series(data, index)` | Crea una columna/arreglo unidimensional etiquetado |
| `.head(n)` / `.tail(n)` | Primeras / últimas n filas |
| `.info()` | Resumen del DataFrame: tipos de dato, nulos |
| `.describe()` | Estadísticas descriptivas (media, desviación estándar, etc.) |
| `.groupby(by)` | Agrupa los datos según una o varias columnas |
| `.merge(right, how, on)` | Combina dos DataFrames (como un JOIN de SQL) |
| `.pivot_table(values, index, columns, aggfunc)` | Tabla dinámica con funciones de agregación |
| `df.shape` / `df.columns` / `df.index` / `df.dtypes` | Propiedades estructurales del DataFrame |
| `.value_counts()` | Frecuencia de valores únicos (en una Series) |
| `.apply(func)` | Aplica una función a cada elemento |

## 🗒️ Conclusión de la sesión

Pandas facilita el trabajo con datos tabulares en todo su ciclo: importación, limpieza, transformación, análisis y (en conjunto con matplotlib) visualización.
