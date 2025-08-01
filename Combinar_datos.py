import pandas as pd


# Cargar datos
ventas = pd.read_csv("datos_simulados.csv")
clima = pd.read_csv("clima_santiago_2024.csv")

# Convertir a datetime
ventas["fecha"] = pd.to_datetime(ventas["fecha"])
clima["fecha"] = pd.to_datetime(clima["fecha"])

# Combinar por fecha
combinado = pd.merge(ventas, clima, on="fecha", how="left")

# Guardar nuevo archivo
combinado.to_csv("ventas_clima_combinado.csv", index=False)

print("✅ Datos combinados correctamente.")
