import pandas as pd
import numpy as np
import random

# Semillas para reproducibilidad
np.random.seed(42)

# Fechas semanales
fechas = pd.date_range(start="2024-01-01", end="2024-12-31", freq='W-MON')

# Productos
productos = [
    {"id": 1, "nombre": "Chocolate 90gr"},
    {"id": 2, "nombre": "Fideos Spaghetti"},
    {"id": 3, "nombre": "Galletas 150gr"},
]

# Lista para guardar los datos
registros = []

for fecha in fechas:
    for prod in productos:
        base_ventas = {
            1: 120,  # Chocolate
            2: 200,  # Fideos
            3: 150   # Galletas
        }

        variacion = np.random.normal(0, 20)  # variación aleatoria
        promocion = random.choice([0, 1])    # 0: no, 1: sí

        # Ajuste por promoción
        if promocion:
            ventas = base_ventas[prod["id"]] + variacion + 30
        else:
            ventas = base_ventas[prod["id"]] + variacion

        # Garantizar que ventas no sean negativas
        ventas = max(0, int(ventas))

        registros.append({
            "fecha": fecha,
            "producto": prod["nombre"],
            "promocion": promocion,
            "ventas": ventas
        })

# Crear dataframe
df = pd.DataFrame(registros)

# Guardar en CSV
df.to_csv(r"C:\Users\arasidesen\Desktop\Proyecto VS Code\Proyecto  Inventario/datos_simulados.csv", index=False)

print("✅ Datos simulados creados.")