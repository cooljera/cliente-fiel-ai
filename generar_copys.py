import pandas as pd

# 1. Cargar archivo segmentado
df = pd.read_excel("clientes_segmentados.xlsx")

# 2. Crear función generadora de copy AIDA por segmento
def generar_copy(nombre, segmento):
    if segmento == "VIP ACTIVO":
        return f"""👑 ¡{nombre}, tú eres parte de la élite Roal Burger! 
Sabemos que valoras la buena sazón, por eso esta semana tienes una sorpresa 🔥
Disfruta un 15% en tu combo favorito 🍔💥
✅ Escríbenos ya por WhatsApp y te lo preparamos como a ti te gusta."""
    
    elif segmento == "EN RIESGO":
        return f"""👀 {nombre}, notamos que no te has pasado por Roal Burger últimamente... 
¿Todo bien? Te guardamos tu combo favorito 🫶
Solo por esta semana tienes 2x1 en pepitos 🌭🔥
✅ Escríbenos por WhatsApp y vuelve con todo el sabor."""
    
    elif segmento == "PERDIDO VALIOSO":
        return f"""😢 {nombre}, ¡Roal Burger te extraña!
Sabemos que eras de los buenos, y queremos verte de vuelta 🍔
Por eso tienes un descuento exclusivo del 25% solo esta semana 💥
✅ Mándanos un WhatsApp y vuelve con hambre."""
    
    else:
        return f"""🍟 {nombre}, esta semana hay sabor y promociones en Roal Burger.
¡Acércate y prueba lo nuevo! 
✅ Pide por WhatsApp y te lo llevamos en tiempo récord."""

# 3. Generar columna nueva
df["COPY PERSONALIZADO"] = df.apply(lambda row: generar_copy(row["NOMBRE DEL CLIENTE"], row["SEGMENTO"]), axis=1)

# 4. Guardar nuevo archivo
df.to_excel("clientes_con_copys.xlsx", index=False)
print("✅ Copys generados y guardados en 'clientes_con_copys.xlsx'")
 