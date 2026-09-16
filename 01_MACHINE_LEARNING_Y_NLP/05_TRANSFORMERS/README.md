# 🤗 Transformers — Modelos de lenguaje pre-entrenados

<p>
<a href="../../README.md"><img src="https://img.shields.io/badge/⬅️_Menú_principal-333333?style=for-the-badge" /></a>
<a href="../04_NLP"><img src="https://img.shields.io/badge/◀️_Sesión_anterior_(NLP)-6c757d?style=for-the-badge" /></a>
</p>

## 🎯 Objetivo

Usar modelos de lenguaje **Transformer** ya entrenados (vía Hugging Face) para tareas de NLP como el análisis de sentimientos, sin necesidad de entrenar un modelo propio desde cero.

## 📖 Teoría

Un **Transformer** es una arquitectura de red neuronal (basada en el mecanismo de "atención") que revolucionó el NLP: es la base de modelos como BERT, GPT y RoBERTa. A diferencia del enfoque clásico (TF-IDF + Naive Bayes, donde tú entrenas un modelo pequeño con tus propios datos), aquí se usa un modelo **gigante ya entrenado por otros** sobre enormes cantidades de texto, y solo se hace **inferencia** (usarlo, no entrenarlo).

**Hugging Face** es la plataforma/comunidad que aloja miles de estos modelos pre-entrenados, listos para descargar y usar.

### Flujo de uso típico

```python
from transformers import pipeline

clasificador = pipeline(
    "sentiment-analysis",
    model="pysentimiento/robertuito-sentiment-analysis",
    device=-1  # -1 = usar CPU
)

clasificador(["Me encantó el curso", "No me gustó nada"])
# → [{'label': 'POS', 'score': 0.98}, {'label': 'NEG', 'score': 0.95}]
```

- `pipeline(tarea, model=...)`: arma automáticamente todo el flujo (tokenizar → pasar por el modelo → interpretar salida) para una tarea específica.
- `label`: la categoría predicha (positivo/negativo/neutral).
- `score`: qué tan seguro está el modelo de su predicción (confianza).

## ⚖️ Entrenar propio vs. usar modelo pre-entrenado

| | TF-IDF + Naive Bayes (propio) | Transformer pre-entrenado |
|---|---|---|
| Esfuerzo | Alto: hay que limpiar datos, entrenar, ajustar | Bajo: solo se usa `pipeline(...)` |
| Calidad | Baseline razonable, limitada al dataset propio | Generalmente mucho mejor, entrenado con millones de ejemplos |
| Control | Total sobre el proceso | Depende del modelo elegido en Hugging Face |

## 🗒️ Conclusión

Los Transformers permiten obtener resultados de alta calidad en tareas de NLP con muy poco código, a costa de perder el control fino que sí se tiene al entrenar un modelo propio.
