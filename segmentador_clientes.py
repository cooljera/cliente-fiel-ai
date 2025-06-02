import pandas as pd
from datetime import datetime

# 1. Cargar el archivo Excel
archivo = "base_con_columna_objetivo.xlsx"  # Cambia este nombre si es diferente
df = pd.read_excel(archivo)

# 2. Limpiar columnas clave
df['FECHA ULTIMA VISITA'] = pd.to_datetime(df['FECHA ULTIMA VISITA'], errors='coerce')
df['GASTO TOTAL'] = df['GASTO TOTAL'].replace(r'[\$,]', '', regex=True).astype(float)
df['TOTAL DE VISITAS'] = df['TOTAL DE VISITAS'].astype(int)

# 3. Calcular días desde la última visita
hoy = pd.Timestamp.today()
df['DIAS DESDE ULTIMA VISITA'] = (hoy - df['FECHA ULTIMA VISITA']).dt.days

# 4. Clasificar clientes
def clasificar_cliente(row):
    if row['GASTO TOTAL'] > 150000 and row['DIAS DESDE ULTIMA VISITA'] <= 10:
        return 'VIP ACTIVO'
    elif row['GASTO TOTAL'] > 80000 and 10 < row['DIAS DESDE ULTIMA VISITA'] <= 30:
        return 'EN RIESGO'
    elif row['GASTO TOTAL'] > 80000 and row['DIAS DESDE ULTIMA VISITA'] > 30:
        return 'PERDIDO VALIOSO'
    else:
        return 'CLIENTE COMÚN'

df['SEGMENTO'] = df.apply(clasificar_cliente, axis=1)

# 5. Guardar archivo segmentado
salida = "clientes_segmentados.xlsx"
df.to_excel(salida, index=False)
print(f"✅ Archivo guardado como {salida}")
