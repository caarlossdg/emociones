import streamlit as st
from textblob import TextBlob
import random

# Respuestas emocionales
respuestas_negativas = [
    "Siento que te sientas así. ¿Quieres hablar más sobre ello?",
    "Aquí estoy para escucharte. ¿Qué ha pasado?",
    "No estás solo/a en esto. Hablemos, si te parece bien.",
    "Gracias por confiar en mí. ¿Cómo te puedo ayudar mejor?"
]

respuestas_positivas = [
    "¡Qué bien escuchar eso! ¿Qué te ha hecho sentir así?",
    "Me alegra mucho por ti. Cuéntame más si quieres 😊",
    "¡Eso suena genial! Me encanta que compartas buenas noticias."
]

respuestas_neutrales = [
    "Gracias por compartirlo. ¿Quieres contarme más?",
    "Estoy aquí para escucharte, cuéntame cuando estés listo/a.",
    "¿Y cómo te hace sentir eso?"
]

# Interfaz
st.set_page_config(page_title="Chat psicológico IA", page_icon="🧠")
st.title("🧠 Chat emocional en Español")
st.write("Soy un asistente conversacional para ayudarte emocionalmente. Estoy aquí para escucharte.")

# Historial de conversación
if "chat" not in st.session_state:
    st.session_state.chat = []

for mensaje in st.session_state.chat:
    st.markdown(mensaje, unsafe_allow_html=True)

# Entrada del usuario
with st.form("formulario"):
    entrada = st.text_input("Cuéntame cómo te sientes:", key="input")
    enviar = st.form_submit_button("Enviar")

if enviar and entrada:
    st.session_state.chat.append(f"<div style='color:blue'><b>Tú:</b> {entrada}</div>")

    # Análisis de sentimiento
    analisis = TextBlob(entrada).sentiment
    if analisis.polarity < -0.2:
        respuesta = random.choice(respuestas_negativas)
    elif analisis.polarity > 0.2:
        respuesta = random.choice(respuestas_positivas)
    else:
        respuesta = random.choice(respuestas_neutrales)

    st.session_state.chat.append(f"<div style='color:green'><b>Psicobot:</b> {respuesta}</div>")
