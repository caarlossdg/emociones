import streamlit as st
from textblob import TextBlob
import random

# --- Frases base ---
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

# --- Inicializar sesión ---
if "chat" not in st.session_state:
    st.session_state.chat = []

# --- Estilo de la app ---
st.title("🧠 Chat emocional")
st.write("Habla conmigo sobre lo que sientas:")

# --- Mostrar historial de conversación ---
for mensaje in st.session_state.chat:
    st.markdown(mensaje, unsafe_allow_html=True)

# --- Input del usuario ---
entrada = st.text_input("Escribe aquí y presiona Enter:", key="input_text")

# --- Procesar mensaje si se escribe algo nuevo ---
if entrada and st.session_state.get("input_submitted", False) == False:
    # Mostrar mensaje del usuario
    st.session_state.chat.append(f"<div style='color:blue'><b>Tú:</b> {entrada}</div>")

    # Analizar emoción
    analisis = TextBlob(entrada).sentiment
    if analisis.polarity < -0.2:
        respuesta = random.choice(respuestas_tristeza)
    elif analisis.polarity > 0.2:
        respuesta = random.choice(respuestas_alegria)
    else:
        respuesta = random.choice(respuestas_neutrales)

    # Mostrar respuesta del bot
    st.session_state.chat.append(f"<div style='color:green'><b>Bot:</b> {respuesta}</div>")

    # Marcar como enviado y limpiar input
    st.session_state.input_submitted = True
    st.experimental_rerun()

# --- Resetear input para permitir más mensajes ---
if st.session_state.get("input_submitted", False):
    st.session_state.input_submitted = False
    st.session_state.input_text = ""
