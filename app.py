import streamlit as st
from textblob import TextBlob
import random

# Frases base
respuestas_tristeza = [
    "💙 Siento que te sientas así. ¿Quieres contarme más?",
    "🌧️ Es normal sentirse así a veces. Estoy contigo.",
    "🫂 Aquí estoy, cuéntame lo que necesites."
]
respuestas_alegria = [
    "😊 Me alegra mucho oír eso.",
    "🎉 ¡Genial! Cuéntame más si quieres.",
    "🌞 Me gusta verte así de bien."
]
respuestas_neutrales = [
    "Gracias por compartirlo. ¿Qué más quieres contarme?",
    "Estoy aquí escuchándote.",
    "¿Y cómo te sientes con eso?"
]
respuestas_ayuda = [
    "🛟 Claro que sí, ¿en qué puedo ayudarte?",
    "Estoy aquí para ti, dime qué necesitas.",
    "💡 Intentaré ayudarte lo mejor que pueda, cuéntame más."
]

# Inicializar chat
if "chat" not in st.session_state:
    st.session_state.chat = []

# Título
st.title("🧠 Chat emocional")
st.write("Habla conmigo sobre lo que sientas:")

# Formulario de entrada
with st.form("chat_form", clear_on_submit=True):
    entrada = st.text_input("Escribe aquí:", key="input_text")
    enviar = st.form_submit_button("Enviar")

# Procesar entrada
if enviar and entrada:
    entrada = entrada.strip()
    st.session_state.chat.append(f"<div style='color:blue'><b>Tú:</b> {entrada}</div>")

    entrada_lower = entrada.lower()

    # Detectar intención por palabras clave
    if "ayuda" in entrada_lower or "puedes" in entrada_lower or "me podrías" in entrada_lower:
        respuesta = random.choice(respuestas_ayuda)
    else:
        # Usar TextBlob como apoyo
        analisis = TextBlob(entrada).sentiment
        if analisis.polarity < -0.2:
            respuesta = random.choice(respuestas_tristeza)
        elif analisis.polarity > 0.2:
            respuesta = random.choice(respuestas_alegria)
        else:
            respuesta = random.choice(respuestas_neutrales)

    st.session_state.chat.append(f"<div style='color:green'><b>Bot:</b> {respuesta}</div>")

# Mostrar historial después de procesar
for mensaje in st.session_state.chat:
    st.markdown(mensaje, unsafe_allow_html=True)
