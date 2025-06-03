import pandas as pd
import openai
from  dotenv import load_dotenv

# WhatsApp del negocio y nombre del restaurante
whatsapp = "+57 314 468 959"
nombre_restaurante = "Roal Burger"
eslogan = "Roal Burger te da más y sazón venezolano"

# Cargar archivo segmentado
df = pd.read_excel("clientes_segmentados.xlsx")

# Función generadora de copy AIDA por segmento
def generar_copy(nombre, segmento):
    if segmento == "VIP ACTIVO":
        return f"""👑 ¡{nombre}, tú eres parte de la élite de {nombre_restaurante}!
Sabemos que valoras la buena sazón y por eso tenemos una sorpresa especial solo para ti 🔥

🎁 Esta semana: 15% de descuento en tu combo favorito 🍔

👉 Pide ya por WhatsApp al {whatsapp} y disfruta lo mejor.

📣 {eslogan}"""

    elif segmento == "EN RIESGO":
        return f"""👀 {nombre}, hace rato no te vemos por {nombre_restaurante}…

¿Te estás perdiendo nuestras promos? Hoy te guardamos una de las buenas 💥

🎁 Promo exclusiva: 2x1 en pepitos solo por hoy 🌭

✅ Escríbenos al WhatsApp {whatsapp} y revive el sabor que tanto te gusta.

📣 {eslogan}"""

    elif segmento == "PERDIDO VALIOSO":
        return f"""😢 {nombre}, ¡te extrañamos en {nombre_restaurante}!

Sabemos que eras de los buenos, y esta es tu oportunidad para volver como rey 👑

🔥 25% de descuento solo esta semana en combos especiales 🍟🍔

✅ Pide ya por WhatsApp al {whatsapp} antes que se acabe.

📣 {eslogan}"""

    else:
        return f"""🍔 {nombre}, esta semana tenemos todo lo que te gusta en {nombre_restaurante}.

🎁 Acércate o pide domicilio: ¡promos en combos y pepitos!

👉 Escríbenos por WhatsApp al {whatsapp} y no te quedes sin probar.

📣 {eslogan}"""

# Crear columna con copies
df["COPY PERSONALIZADO"] = df.apply(lambda row: generar_copy(row["NOMBRE DEL CLIENTE"], row["SEGMENTO"]), axis=1)

# Guardar archivo final
df.to_excel("clientes_con_copys_final.xlsx", index=False)
print("✅ Copys con CTA generados y guardados en 'clientes_con_copys_final.xlsx'")
