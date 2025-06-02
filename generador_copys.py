from openai import OpenAI
from dotenv import load_dotenv
import os
import random

# Cargar variables de entorno
load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

openai_bloqueado = False

def generar_copy_local(segmento, nombre_cliente, restaurante, tipo, promo, direccion, whatsapp):
    """Genera un copy sin usar OpenAI"""
    
    # Plantillas de saludos personalizados por segmento
    saludos = {
        '0': [  # Cliente Normal
            f"¡{nombre_cliente}! 👋", f"¡Hola {nombre_cliente}! 💫", 
            f"¡Hey {nombre_cliente}! 🎯", f"¡{nombre_cliente}! 🌈",
            f"¡Adivina qué, {nombre_cliente}! ✨"
        ],
        '1': [  # VIP
            f"¡{nombre_cliente}! 👑", f"¡Distinguido {nombre_cliente}! 💎",
            f"¡Exclusivo para ti, {nombre_cliente}! ⭐", 
            f"¡{nombre_cliente}, cliente VIP! 🏆",
            f"¡Especialmente para ti, {nombre_cliente}! ✨"
        ],
        '2': [  # Especial
            f"¡{nombre_cliente}! ✨", f"¡Hola {nombre_cliente}! 🎁",
            f"¡{nombre_cliente}! 🌈", f"¡Hey {nombre_cliente}! 🎭",
            f"¡{nombre_cliente}, cliente especial! 🌺"
        ]
    }

    # Frases motivadoras por segmento
    frases = {
        '0': [
            "Te extrañamos en", "Queremos verte de nuevo en",
            "¡Es hora de volver a", "Hay algo especial para ti en",
            "Te esperamos con los brazos abiertos en"
        ],
        '1': [
            "Tu experiencia VIP te espera en", "Tu lugar preferido",
            "Tu momento exclusivo está en", "Como cliente VIP te esperamos en",
            "Tu espacio especial está reservado en"
        ],
        '2': [
            "Tenemos algo especial para ti en", "Tu lugar favorito",
            "Una sorpresa te espera en", "Preparamos algo único en",
            "Tu momento especial está en"
        ]
    }

    # Presentación de promociones
    promos = [
        f"¡Aprovecha esta promoción especial: {promo}! 🎉",
        f"¡Solo para ti: {promo}! 🎁",
        f"¡No te pierdas esta oportunidad: {promo}! ✨",
        f"¡Oferta exclusiva: {promo}! 💫",
        f"¡Promoción especial: {promo}! 🌟"
    ]

    # Llamadas a la acción
    ctas = [
        f"Visítanos en {direccion} o pide por WhatsApp al {whatsapp} 📱",
        f"¡Reserva ahora! WhatsApp {whatsapp} o ven a {direccion} 📍",
        f"Haz tu pedido al {whatsapp} o visítanos en {direccion} 🛵",
        f"¡Te esperamos! Contáctanos al {whatsapp} o ven a {direccion} 🏃‍♂️",
        f"Ordena ya al {whatsapp} o disfruta en {direccion} 🍽️"
    ]

    # Generar mensaje
    saludo = random.choice(saludos.get(str(segmento), saludos['2']))
    frase = random.choice(frases.get(str(segmento), frases['2']))
    promo_text = random.choice(promos)
    cta = random.choice(ctas)
    
    mensaje = (
        f"{saludo}\n"
        f"{frase} {restaurante}! {promo_text}\n"
        f"{cta}"
    )
    
    return mensaje

def generar_copy(segmento, nombre_cliente, restaurante, tipo, promo, direccion, whatsapp):
    global openai_bloqueado
    if openai_bloqueado:
        return generar_copy_local(segmento, nombre_cliente, restaurante, tipo, promo, direccion, whatsapp)
    try:
        # Intentar usar OpenAI
        prompt = f"""
        Genera un mensaje de WhatsApp corto y persuasivo para {nombre_cliente}.
        Restaurante: {restaurante} ({tipo})
        Segmento: {segmento}
        Promoción: {promo}
        Ubicación: {direccion}
        WhatsApp: {whatsapp}
        
        Usa emojis y máximo 3 líneas de texto.
        """

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Eres un experto en marketing gastronómico"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        if "insufficient_quota" in str(e):
            openai_bloqueado = True
        print(f"Usando generador local debido a: {str(e)}")
        return generar_copy_local(segmento, nombre_cliente, restaurante, tipo, promo, direccion, whatsapp)

# Ejemplo de uso
mensaje = generar_copy(1, "Juan", "Pizzería La Italiana", "pizza", "20% + papas gratis", "Calle 123", "555-1234")
print(mensaje)