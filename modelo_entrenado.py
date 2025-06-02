import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
import joblib

# 1. Cargar el archivo segmentado
df = pd.read_excel("clientes_segmentados.xlsx")

# 2. Preparar las variables
df = df.dropna(subset=["GASTO TOTAL", "DIAS DESDE ULTIMA VISITA", "TOTAL DE VISITAS", "SEGMENTO"])

X = df[["GASTO TOTAL", "DIAS DESDE ULTIMA VISITA", "TOTAL DE VISITAS"]]
y = df["SEGMENTO"]

# 3. Codificar la variable objetivo
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# 4. Separar en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# 5. Entrenar el modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 6. Evaluar
y_pred = model.predict(X_test)
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("📊 Clasificación:\n", classification_report(y_test, y_pred, target_names=le.classes_))

# 7. Guardar modelo entrenado y codificador
joblib.dump(model, "modelo_segmentador.pkl")
joblib.dump(le, "codificador_segmentos.pkl")
print("💾 Modelo y codificador guardados.")

# Cargar modelo y codificador
modelo = joblib.load("modelo_segmentador.pkl")
label_encoder = joblib.load("codificador_segmentos.pkl")
