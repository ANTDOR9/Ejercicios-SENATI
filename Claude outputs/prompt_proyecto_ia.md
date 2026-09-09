# Prompt para iniciar mi proyecto de IA: Generador de letras de canciones

## Contexto sobre mí

Soy estudiante de Tecnologías de la Información en SENATI, cursando el curso de Python aplicado a Machine Learning ("PIAD425"). Ya hice un Trabajo Final anterior (un predictor de tendencias de mercado financiero con datos sintéticos), así que no parto de cero. Esto es lo que ya vengo manejando en clase:

**Fundamentos de IA/ML:**
- Diferencia entre IA, Machine Learning y Deep Learning
- Flujo típico de un proyecto de ML: cargar datos → explorar/limpiar → visualizar → entrenar modelo → evaluar → conclusiones

**Matemática del perceptrón:**
- Fórmula: Z = ΣXiWi + b (suma ponderada + bias)
- Activación tipo escalón: f(Z) = 1 si Z≥0, si no 0
- Regla delta para entrenar: error = Target − f(Z), y actualizar pesos: Wi_nuevo = Wi_viejo + (error·tasa_aprendizaje)·Xi, y el bias: b_nuevo = b_viejo + (error·tasa_aprendizaje)
- El bias es un valor inicial arbitrario, no se calcula de la tabla de verdad, solo se ajusta con el error

**Librerías de Python para ML:**
- Pandas y NumPy para manejo y generación de datos (incluyendo generación de datos sintéticos con random walk)
- Matplotlib y Seaborn para visualización
- Scikit-learn: DecisionTreeClassifier, train_test_split, accuracy_score, classification_report
- PyTorch: StandardScaler, tensores, nn.Sequential, CrossEntropyLoss, optimizador Adam, loop de entrenamiento

**NLP (Procesamiento de Lenguaje Natural):**
- Tokenización con NLTK (word_tokenize, stopwords, TweetTokenizer)
- TF-IDF manual: tokenización → vocabulario → TF (frecuencia en el documento) → DF (frecuencia entre documentos) → IDF = ln(N/DF) → TF×IDF
- Con spaCy: tokenización, lematización, POS tagging (etiquetado gramatical), reconocimiento de entidades nombradas (NER)
- Con Transformers (Hugging Face): pipelines pre-entrenados (ej. traducción con modelos AutoModelForSeq2SeqLM)

## El proyecto que quiero construir

Un **generador de letras de canciones**: le doy al sistema una o varias líneas de una canción (el "punto de partida"), y el modelo predice y genera una continuación de letra nueva, coherente con ese estilo/contexto.

**Parte 1 (90% del proyecto, el foco principal): generación de texto con una red neuronal LSTM en PyTorch.**

Ya decidí el enfoque: quiero ir por el camino avanzado, no el simple de cadenas de Markov. Es decir:
- Entrenar una red neuronal recurrente (LSTM) con un corpus de letras de canciones (necesito ayuda para conseguir o armar ese dataset — puede ser un dataset público simple, o armar uno propio con letras que yo elija)
- El modelo debe aprender a predecir la siguiente palabra (o carácter, según lo que resulte más manejable a mi nivel) dado el contexto anterior
- Quiero entender bien: cómo se prepara el texto para entrenar una LSTM (tokenización, secuencias, embeddings), cómo se arma la arquitectura en PyTorch (capas LSTM, capa de salida), cómo se entrena, y cómo se genera texto nuevo a partir de una línea semilla que yo escriba
- Como ya vengo de un curso con la línea de trabajo pandas → scikit-learn → PyTorch → NLP, prefiero que el proyecto conecte con eso en vez de saltar a librerías completamente nuevas que no he visto en clase

**Parte 2 (extra/secundario, mucho más simple): darle voz a la letra generada.**

Ya decidimos explícitamente:
- NO vamos a generar música/ritmo con IA (evitar abrir un segundo proyecto de IA generativa de audio dentro de este)
- SÍ vamos a usar `pyttsx3` (voz robótica simple tipo "Loquendo", funciona offline) para que el sistema lea/"cante" en voz robótica la letra generada — es una demo simple, no el corazón técnico del proyecto
- Esto queda como algo que planeo mejorar más adelante (posiblemente una voz más elaborada o con ritmo), pero para esta primera versión el objetivo es que simplemente funcione de forma básica

## Lo que necesito de ti

1. **Un flujo claro de construcción de este proyecto específico**, adaptado a mi nivel de curso (no producción/empresa grande): de dónde sacar o cómo armar el dataset de letras, cómo preparar el texto para la LSTM, cómo estructurar y entrenar el modelo en PyTorch, cómo generar texto nuevo a partir de una semilla, y cómo integrar al final la voz con pyttsx3.
2. Ayuda para dimensionar bien el alcance para que sea completable en el tiempo de un trabajo de curso (no un proyecto de investigación de meses).
3. Sugerencias de cómo documentar/presentar esto (informe, README, diagramas) igual que en mi proyecto anterior.

No necesito que resuelvas el proyecto aquí — dame el flujo y el plan, para llevarlo a otra conversación y desarrollarlo ahí paso a paso.
