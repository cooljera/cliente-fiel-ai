import numpy as np
import joblib

# 1. Cargar el modelo y el codificador
modelo = joblib.load("modelo_segmentador.pkl")
codificador = joblib.load("codificador_segmentos.pkl")

# 2. Solicitar datos del nuevo cliente
print("🔍 Ingresar datos del nuevo cliente:")
try:
    gasto = float(input("💰 Total gastado en pesos: "))
    dias = int(input("📆 Días desde la última compra: "))
    visitas = int(input("🔢 Total de visitas: "))
except ValueError:
    print("❌ Datos inválidos. Intenta de nuevo.")
    exit()

# 3. Crear vector de entrada
cliente = np.array([[gasto, dias, visitas]])

# 4. Predecir
pred = modelo.predict(cliente)[0]
segmento = codificador.inverse_transform([pred])[0]

# 5. Mostrar resultado
print(f"\n🧠 Segmento predicho: {segmento}")
