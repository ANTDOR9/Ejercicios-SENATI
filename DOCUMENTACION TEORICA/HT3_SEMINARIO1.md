<!-- Slide number: 1 -->
# HT3-Estudia el uso de las librerías Scipy y NLTK
Sesión N° 2
Instructor: Jesús Romero Villanueva

### Notes:

<!-- Slide number: 2 -->
# OBJETIVO
Dadas las orientaciones del instructor y los recursos del laboratorio, el participante será capaz de analizar el uso de las librerías SciPy y NLTK, relacionando los fundamentos del procesamiento de lenguaje natural (NLP) con las características de ambas librerías y sus principales aplicaciones en soluciones de Inteligencia Artificial, desarrollando la actividad según los criterios de evaluación establecidos y cumpliendo las normas de seguridad en el uso de equipos informáticos y prevención de riesgos eléctricos conforme a la ISO 45001:2018 y la ISO 9241.

### Notes:

<!-- Slide number: 3 -->
# OBJETIVO 1.1
Dadas las orientaciones del instructor y los recursos del laboratorio, el participante será capaz de aplicar conceptos relacionados con el uso de las librerías SciPy y NLTK, definiendo el procesamiento de lenguaje natural (NLP) y las características de ambas librerías, desarrollando la actividad según los criterios de evaluación establecidos y cumpliendo las normas de seguridad en el uso de equipos informáticos y prevención de riesgos eléctricos conforme a la ISO 45001:2018 y la ISO 9241..

### Notes:

<!-- Slide number: 4 -->
# Desarrollo del seminario
HT3 – Estudia el uso de las librerías Scipy y NLTK
Define el procesamiento de lenguaje natural (NLP)
Define la librería Scipy y NLTK
Identifica principales aplicaciones del NLP

### Notes:

<!-- Slide number: 5 -->
# Empezando…
"Las máquinas no entienden nuestro idioma... hasta que les enseñamos a pensarlo."

### Notes:

<!-- Slide number: 6 -->
# ¿Qué es el Procesamiento de Lenguaje Natural (NLP)?
Es una rama de la inteligencia artificial que permite a las máquinas comprender, interpretar y generar lenguaje humano.

![Part-1: Introduction to Natural Language Processing (NLP) | by Kabir Narayan Jha | Medium](GoogleShape110p5.jpg)

### Notes:

<!-- Slide number: 7 -->
# Tareas comunes del NLP:
Tokenización: Separar texto en palabras o frases.
Lematización y stemming: Reducir palabras a su raíz.
Análisis sintáctico: Determinar la estructura gramatical.
Reconocimiento de entidades nombradas (NER): Identificar nombres, fechas, organizaciones, etc.
Clasificación de texto: Sentimiento, spam, temas.
Traducción automática
Generación de texto (chatbots, GPT, etc.)

![](GoogleShape117p6.jpg)

### Notes:

<!-- Slide number: 8 -->
# Librería NLTK (Natural Language Toolkit)
NLTK es una de las librerías más completas y didácticas para trabajar NLP en Python. Es ideal para enseñanza y prototipos.
Características:
Incluye corpus en varios idiomas
Herramientas para tokenizar, etiquetar, analizar sintaxis
Compatible con otras herramientas (WordNet, TextBlob)
Viene con modelos estadísticos básicos

![Demystifying NLP Text Representation Techniques: A Comprehensive Guide | by Gopal Katariya | Medium](GoogleShape124p7.jpg)

### Notes:

<!-- Slide number: 9 -->
# Ejemplo básico

![](GoogleShape130p8.jpg)

![API de tokenización y lematización, basada en spaCy](GoogleShape131p8.jpg)

### Notes:

<!-- Slide number: 10 -->
# Librería SciPy
SciPy es una librería científica de Python que se usa para operaciones matemáticas avanzadas como álgebra lineal, estadísticas, transformadas de Fourier, etc.
Usos frecuentes:
Resolución de ecuaciones
Cálculo de derivadas, integrales
Estadística descriptiva e inferencial
Optimización (machine learning)
Señales, imágenes, y procesamiento de datos científicos

![SciPyindia](GoogleShape138p9.jpg)

### Notes:

<!-- Slide number: 11 -->
# Relación con NLP:
SciPy es útil en NLP para:
Analizar datos estadísticos del texto
Optimizar modelos (gradient descent)
Normalización y escalado de características
Visualización y análisis de resultados

![SciPy: All about the Python Machine Learning library](GoogleShape145p10.jpg)

### Notes:

<!-- Slide number: 12 -->
# Ejemplo

![](GoogleShape151p11.jpg)

![Cómo saber si una variable sigue una distribución normal en Python?](GoogleShape152p11.jpg)

### Notes:

<!-- Slide number: 13 -->
# OBJETIVO 1.2
Dadas las orientaciones del instructor y los recursos del laboratorio, el participante será capaz de analizar el uso de las librerías SciPy y NLTK, identificando las principales aplicaciones del procesamiento de lenguaje natural (NLP) y su relación con soluciones de Inteligencia Artificial, desarrollando la actividad según los criterios de evaluación establecidos y cumpliendo las normas de seguridad en el uso de equipos informáticos y prevención de riesgos eléctricos conforme a la ISO 45001:2018 y la ISO 9241.

### Notes:

<!-- Slide number: 14 -->
# Aplicaciones Principales del NLP
| Área | Aplicación |
| --- | --- |
| Salud | Chatbots médicos, análisis de historias clínicas |
| Educación | Corrección automática, asistentes de redacción |
| Política | Análisis de discursos, detección de sesgos |
| Marketing | Análisis de sentimiento en redes sociales |
| Justicia | Análisis de jurisprudencia y leyes |
| Servicio al cliente | Chatbots, clasificaciones de tickets |
| Traducción | Motores de traducción automática |
| Reclutamiento | Análisis de CV y descripciones de puesto |

### Notes:

<!-- Slide number: 15 -->
# Actividad 1 – Limpieza y análisis de texto con NLTK:

![](GoogleShape171p13.jpg)

### Notes:

<!-- Slide number: 16 -->
# Actividad 2 – Estadística con SciPy aplicada al texto:

![](GoogleShape177p14.jpg)

### Notes:

<!-- Slide number: 17 -->
# Ahora implementaremos…
Flujo completo de análisis de sentimientos con Machine Learning
Modelos de análisis basados en Deep Learning
Traductor y flujo conversacional.

Apunta estos datos para tu práctica:p1:  "translation" "Helsinki-NLP/opus-mt-es-en"

p2:
pipeline(
    "translation",
    model="facebook/nllb-200-distilled-600M",
    src_lang="spa_Latn",
    tgt_lang="quy_Latn"
)

### Notes:

<!-- Slide number: 18 -->

### Notes: