import streamlit as st
from textblob import TextBlob
from datetime import datetime
import random

# Frases motivadoras
frases_positivas = [
    "🌞 Cada día es una nueva oportunidad para empezar de nuevo.",
    "🌱 No te olvides de ser amable contigo mismo hoy.",
    "💪 Incluso los pequeños pasos te acercan a tu meta.",
    "🧠 Tu valor no depende de tu productividad.",
    "🎨 Haz algo que te guste hoy, aunque sea solo respirar profundo."
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

# Registro de emociones
def registrar_emocion(emocion, detalle=""):
    with open("registro_emociones.txt", "a") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M')} - {emocion} - {detalle}\n")

# Interfaz
st.title("🤖 Asistente emocional")

opcion = st.radio("¿En qué te gustaría que te ayudara hoy?", [
    "Hablar sobre cómo me siento",
    "Hacer un ejercicio de respiración",
    "Recibir un consejo positivo"
])

# Opción 1
if opcion == "Hablar sobre cómo me siento":
    mensaje = st.text_input("Cuéntame cómo te sientes con tus propias palabras:")
    if mensaje:
        analisis = TextBlob(mensaje).sentiment
        polaridad = analisis.polarity

        if polaridad < -0.2:
            st.write(random.choice(frases_tristeza))
            registrar_emocion("triste", mensaje)
        elif polaridad > 0.2:
            st.write(random.choice(frases_alegria))
            registrar_emocion("feliz", mensaje)
        else:
            st.write("Gracias por compartir cómo te sientes. Estoy aquí contigo.")
            registrar_emocion("neutral", mensaje)

# Opción 2
elif opcion == "Hacer un ejercicio de respiración":
    if st.button("Empezar ejercicio de respiración"):
        st.write("Inhala profundamente... 🫁")
        st.sleep(2)
        st.write("Mantén el aire...")
        st.sleep(2)
        st.write("Exhala lentamente... 😌")
        st.sleep(3)
        st.success("Muy bien. Puedes repetirlo cuando lo necesites.")
        registrar_emocion("respiración", "Ejercicio hecho")

# Opción 3
elif opcion == "Recibir un consejo positivo":
    consejo = random.choice(frases_positivas)
    st.success(f"🌟 Consejo del día: {consejo}")
    registrar_emocion("consejo", consejo)
