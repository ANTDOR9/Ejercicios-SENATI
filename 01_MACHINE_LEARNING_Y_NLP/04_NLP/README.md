# 💬 Sesión 03/04 — Procesamiento de Lenguaje Natural con SciPy, NLTK y spaCy

<p>
<a href="../../README.md"><img src="https://img.shields.io/badge/⬅️_Menú_principal-333333?style=for-the-badge" /></a>
<a href="../03_TENSORFLOW_KERAS"><img src="https://img.shields.io/badge/◀️_Sesión_anterior_(TensorFlow%2FKeras)-6c757d?style=for-the-badge" /></a>
</p>

## 🎯 Objetivo

Explicar los fundamentos del Procesamiento de Lenguaje Natural (NLP) utilizando **SciPy**, **NLTK** y **spaCy**, identificando los principales procesos y técnicas para el análisis de texto.

## 📖 Teoría

**SciPy** es una biblioteca para matemáticas, ciencia e ingeniería (optimización, álgebra lineal, integración, transformadas de Fourier), construida sobre NumPy.

**NLTK (Natural Language Toolkit)** se usa para trabajar con texto: tokenización, análisis morfológico, etiquetado POS, análisis de sentimientos.

**spaCy** es una librería de NLP más moderna y orientada a producción: rápida, eficiente, con modelos de idioma pre-entrenados.

### Conceptos clave

| Concepto | Qué es |
|---|---|
| **Modelado de lenguaje** | Enseñar a una computadora los patrones de un idioma (qué palabras suelen ir juntas o después de otras) a partir de muchos ejemplos |
| **Tokenización** | Dividir un texto en unidades más pequeñas (tokens): palabras, frases o caracteres |
| **Stopwords** | Palabras muy frecuentes y de poco valor semántico (el, la, de...) que suelen filtrarse |
| **Lematización** | Convertir una palabra a su forma base/raíz válida del idioma (ej. "running" → "run"), a diferencia del *stemming* que solo recorta sufijos |
| **POS tagging** | Etiquetado gramatical: identificar si una palabra es sustantivo, verbo, adjetivo, etc. |
| **NER (Named Entity Recognition)** | Detectar nombres propios, lugares u organizaciones dentro de un texto |
| **TF-IDF** | Convierte texto en vectores numéricos ponderados por frecuencia/relevancia de cada palabra |

### Herramientas y su rol

| Librería | Uso típico |
|---|---|
| `word_tokenize` / `TweetTokenizer` (NLTK) | Tokenizar texto formal / informal (redes sociales) |
| `stopwords.words("spanish")` (NLTK) | Lista de palabras vacías en español para filtrar |
| `spacy.load("es_core_news_sm")` | Cargar un modelo de idioma en español para lematización, POS y NER |
| `TfidfVectorizer` + `MultinomialNB` (Scikit-learn) | Pipeline clásico de clasificación de texto (ej. análisis de sentimientos) |

## 🗒️ Conclusión de la sesión

SciPy se enfoca en cómputo numérico/científico general; NLTK es útil para operaciones léxicas simples; spaCy se usa cuando se necesita un análisis lingüístico más rico (lemas, gramática, entidades) con un modelo de idioma cargado.
