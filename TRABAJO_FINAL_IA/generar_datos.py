"""
Genera un dataset sintetico y realista de mercado financiero
usando solo numpy y pandas (herramientas vistas en clase).
"""
import numpy as np
import pandas as pd

np.random.seed(42)  # reproducibilidad

# ---- Configuracion ----
n_dias = 500
precio_inicial = 100.0
fecha_inicio = "2023-01-01"

# ---- 1. Fechas de mercado (dias habiles) ----
fechas = pd.bdate_range(start=fecha_inicio, periods=n_dias)

# ---- 2. Precio de cierre con caminata aleatoria (random walk) ----
cambios_diarios = np.random.normal(loc=0.0005, scale=0.02, size=n_dias)
precio_cierre = precio_inicial * np.cumprod(1 + cambios_diarios)

# ---- 3. Apertura, maximo y minimo coherentes con el cierre ----
precio_apertura = precio_cierre * (1 + np.random.normal(0, 0.005, n_dias))
precio_max = np.maximum(precio_apertura, precio_cierre) * (1 + np.abs(np.random.normal(0, 0.008, n_dias)))
precio_min = np.minimum(precio_apertura, precio_cierre) * (1 - np.abs(np.random.normal(0, 0.008, n_dias)))

# ---- 4. Volumen de negociacion ----
volumen = np.random.randint(100_000, 5_000_000, size=n_dias)

# ---- 5. DataFrame final ----
df = pd.DataFrame({
    "fecha": fechas,
    "precio_apertura": precio_apertura.round(2),
    "precio_cierre": precio_cierre.round(2),
    "precio_max": precio_max.round(2),
    "precio_min": precio_min.round(2),
    "volumen": volumen
})

# ---- 6. Columna objetivo: tendencia (1=sube, 0=baja) ----
df["tendencia"] = (df["precio_cierre"].diff() > 0).astype(int)
df.loc[0, "tendencia"] = 0

df.to_csv("datos_mercado_financiero.csv", index=False)
print(df.head(10))
print("\nForma del dataset:", df.shape)
print("\nDistribucion de tendencia:")
print(df["tendencia"].value_counts())
print("\nCSV generado: datos_mercado_financiero.csv")
