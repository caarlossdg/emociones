import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os

# Autenticación con Hugging Face
# Asegúrate de reemplazar 'TU_TOKEN_AQUI' con tu token de acceso personal
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "TU_TOKEN_AQUI"

# Cargar el modelo y el tokenizador
model_name = "ITG/DialoGPT-medium-spanish-chitchat"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Configurar la página de Streamlit
st.set_page_config(page_title="Chatbot en Español", page_icon="🤖")
st.title("🤖 Chatbot en Español")
st.write("Interactúa con un modelo de lenguaje en español.")

# Inicializar el historial de conversación
if "historial" not in st.session_state:
    st.session_state.historial = []

# Mostrar el historial de conversación
for mensaje in st.session_state.historial:
    st.markdown(mensaje, unsafe_allow_html=True)

# Entrada del usuario
with st.form(key="formulario_chat"):
    entrada_usuario = st.text_input("Escribe tu mensaje:", "")
    enviar = st.form_submit_button("Enviar")

# Procesar la entrada del usuario
if enviar and entrada_usuario:
    # Mostrar el mensaje del usuario
    st.session_state.historial.append(f"<div style='color:blue'><b>Tú:</b> {entrada_usuario}</div>")

    # Codificar la entrada del usuario
    entrada_ids = tokenizer.encode(entrada_usuario + tokenizer.eos_token, return_tensors="pt")

    # Generar la respuesta del modelo
    respuesta_ids = model.generate(
        entrada_ids,
        max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.7
    )

    # Decodificar y mostrar la respuesta del bot
    respuesta = tokenizer.decode(respuesta_ids[:, entrada_ids.shape[-1]:][0], skip_special_tokens=True)
    st.session_state.historial.append(f"<div style='color:green'><b>Bot:</b> {respuesta}</div>")
