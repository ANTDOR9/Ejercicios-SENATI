# 📐 Introducción — Fundamentos de Inteligencia Artificial

> Primer tema del curso (Semestre IV): "Estudia los fundamentos de Inteligencia Artificial"

## ¿Qué es la Inteligencia Artificial?

Es la capacidad que tienen las máquinas para aprender a realizar tareas que normalmente requieren inteligencia humana: reconocer imágenes, entender texto, tomar decisiones, hacer predicciones.

Dentro de la IA existen distintos niveles de especialización:

```
Inteligencia Artificial (concepto general)
   └── Machine Learning (aprender de datos, sin programar cada regla)
         └── Deep Learning (Machine Learning con redes neuronales profundas)
```

- **Machine Learning**: en vez de escribir reglas explícitas, se le muestran datos de ejemplo a un algoritmo y este "aprende" patrones por sí mismo.
- **Deep Learning**: un tipo particular de Machine Learning que usa redes neuronales con muchas capas, capaces de aprender representaciones más complejas de los datos (imágenes, texto, audio).

## ¿Qué es un modelo de IA?

Un modelo de IA es un sistema que aprende patrones a partir de datos para hacer predicciones o tomar decisiones. Se construye en dos grandes fases:

1. **Entrenamiento**: se le muestran datos de ejemplo al modelo, y este ajusta sus parámetros internos para acertar cada vez más.
2. **Inferencia / predicción**: una vez entrenado, el modelo recibe datos nuevos (que nunca vio) y da una respuesta.

### Tipos de aprendizaje

- **Supervisado**: los datos de entrenamiento ya incluyen la respuesta correcta (ej. fotos de perros y gatos ya etiquetadas). El modelo aprende a relacionar la entrada con esa respuesta.
- **No supervisado**: los datos NO tienen etiquetas. El modelo busca patrones o agrupaciones por su cuenta (ej. agrupar clientes parecidos sin que nadie le diga cómo).

### Tipos de modelo según la tarea

| Tarea | Qué predice | Ejemplo |
|---|---|---|
| Regresión | Un valor continuo | Precio de una casa |
| Clasificación | Una categoría | Spam / no spam |
| Clustering | Grupos sin etiquetas | Segmentación de clientes |

## ¿Por qué el curso empieza con álgebra lineal y estadística?

Porque son la base matemática sobre la que funciona todo modelo de IA:

- **Álgebra lineal (vectores y matrices)**: los datos que entran a un modelo (una imagen, una fila de una tabla) se representan como vectores; los "pesos" que aprende una red neuronal se organizan como matrices. Prácticamente toda operación interna de un modelo es, en el fondo, una multiplicación de matrices.

  - **Vector**: una secuencia ordenada de números, por ejemplo `[3, 7, 1]`.
  - **Matriz**: una tabla de números organizada en filas y columnas, por ejemplo:
    ```
    [ 1  2  3 ]
    [ 4  5  6 ]
    ```

- **Estadística (varianza y desviación estándar)**: sirven para entender qué tan dispersos están los datos.

  - **Varianza**: mide, en promedio, qué tan lejos está cada dato del promedio general (elevado al cuadrado).
  - **Desviación estándar**: es la raíz cuadrada de la varianza — más fácil de interpretar porque queda en las mismas unidades que los datos originales.

  Esto importa porque muchos modelos funcionan mejor cuando los datos están "normalizados" (con una escala/dispersión pareja), y para eso primero hay que medir esa dispersión.

## En resumen

Antes de entrenar cualquier modelo de Machine Learning o red neuronal, hace falta dominar el lenguaje matemático con el que esos modelos "piensan": vectores, matrices y algunas nociones básicas de estadística. Ese es el objetivo de este bloque del curso.
