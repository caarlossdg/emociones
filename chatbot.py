from datetime import datetime
import time
import random
from textblob import TextBlob

# Frases motivadoras
frases_positivas = [
    "🌞 Cada día es una nueva oportunidad para empezar de nuevo.",
    "🌱 No te olvides de ser amable contigo mismo hoy.",
    "💪 Incluso los pequeños pasos te acercan a tu meta.",
    "🧠 Recuerda: tu valor no depende de tu productividad.",
    "🎨 Haz algo pequeño que te guste hoy, aunque sea sonreír."
]

frases_tristeza = [
    "🌤️ Aunque hoy esté nublado, el sol volverá a salir.",
    "💙 Eres más fuerte de lo que crees.",
    "📘 A veces solo necesitamos hablar para empezar a sanar."
]

frases_alegria = [
    "🥳 ¡Sigue brillando!",
    "✨ Me encanta tu energía positiva.",
    "🌈 Qué bonito es compartir alegría."
]

frases_ansiedad = [
    "🌬️ La respiración es una herramienta poderosa. Confía en ella.",
    "🧘 El momento presente es un lugar seguro.",
    "💆‍♀️ Está bien parar y cuidar de ti."
]

# Guardar emociones y reflexiones
def registrar_emocion(emocion, detalle=""):
    with open("registro_emociones.txt", "a") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M')} - {emocion} - {detalle}\n")

# Inicio del chatbot
print("👋 Hola, soy tu asistente emocional.")
print("¿En qué te gustaría que te ayudara hoy?")
print("1. Hablar sobre cómo me siento")
print("2. Hacer un ejercicio de respiración")
print("3. Recibir un consejo positivo")
opcion = input("Escribe 1, 2 o 3: ").strip()

# Opción 1: Detección emocional con TextBlob
if opcion == "1":
    print("\nEstá bien. Puedes contarme cómo te sientes con tus propias palabras:")
    mensaje = input("Tú: ")
    analisis = TextBlob(mensaje).sentiment
    polaridad = analisis.polarity

    # Clasificación automática
    if polaridad < -0.2:
        emocion = "triste"
        print(random.choice(frases_tristeza))
        print("Gracias por compartirlo. ¿Quieres contarme algo más?")
        detalle = input("Tú: ")
        registrar_emocion(emocion, mensaje + " | " + detalle)
    elif polaridad > 0.2:
        emocion = "feliz"
        print(random.choice(frases_alegria))
        print("¡Me alegra mucho oírlo! ¿Qué más te gustaría compartir?")
        detalle = input("Tú: ")
        registrar_emocion(emocion, mensaje + " | " + detalle)
    else:
        emocion = "neutral"
        print("Gracias por contarme cómo te sientes. Estoy aquí para ti.")
        registrar_emocion(emocion, mensaje)

# Opción 2: Ejercicio de respiración
elif opcion == "2":
    print("\n🧘 Vamos a hacer un ejercicio de respiración juntos.")
    for i in range(3):
        print("Inhala profundamente... 🫁")
        time.sleep(2)
        print("Mantén el aire...")
        time.sleep(2)
        print("Exhala lentamente... 😌")
        time.sleep(3)
    print("Muy bien. ¿Cómo te sientes ahora?")
    respuesta = input("Tú: ")
    registrar_emocion("respiración", respuesta)

# Opción 3: Consejo positivo
elif opcion == "3":
    consejo = random.choice(frases_positivas)
    print("\n🌟 Consejo del día:")
    print(consejo)
    registrar_emocion("consejo", consejo)

# Opción inválida
else:
    print("❌ Opción no válida. Ejecuta el programa de nuevo.")
