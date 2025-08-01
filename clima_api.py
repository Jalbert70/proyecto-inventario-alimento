import requests
import pandas as pd
from datetime import datetime, timedelta

# Coordenadas de Santiago de Chile
latitude = -33.4489
longitude = -70.6693

# Generar fechas semanales
fechas = pd.date_range(start="2024-01-01", end="2024-12-31", freq="W-MON")

# Lista para guardar resultados
datos_clima = []

for fecha in fechas:
    # Obtener semana completa (lunes a domingo)
    start_date = fecha.strftime("%Y-%m-%d")
    end_date = (fecha + timedelta(days=6)).strftime("%Y-%m-%d")

    url = (
        f"https://archive-api.open-meteo.com/v1/archive?"
        f"latitude={latitude}&longitude={longitude}"
        f"&start_date={start_date}&end_date={end_date}"
        f"&daily=temperature_2m_max,temperature_2m_min"
        f"&timezone=America/Santiago"
    )

    response = requests.get(url)
    data = response.json()

    if "daily" in data:
        tmax = data["daily"]["temperature_2m_max"]
        tmin = data["daily"]["temperature_2m_min"]
        tavg = [(a + b) / 2 for a, b in zip(tmax, tmin)]

        avg_temp = sum(tavg) / len(tavg)
        datos_clima.append({
            "fecha": fecha,
            "temperatura_promedio": round(avg_temp, 1)
        })
    else:
        print(f"Error en {start_date} - {end_date}")

# Crear DataFrame
df_clima = pd.DataFrame(datos_clima)

# Guardar en CSV
df_clima.to_csv(r"C:\Users\arasidesen\Desktop\Proyecto VS Code\Proyecto  Inventario/clima_santiago_2024.csv", index=False)

print("✅ Clima descargado y guardado")

#Esta modificacion fue creada para prueba