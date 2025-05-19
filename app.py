import streamlit as st
from transformers import pipeline
import os

# Cargar token desde secrets
token = st.secrets["HUGGINGFACEHUB_API_TOKEN"]

# Cargar modelo de Hugging Face
@st.cache_resource
def cargar_modelo():
    return pipeline(
        "text-generation",
        model="HuggingFaceH4/zephyr-7b-beta",
        tokenizer="HuggingFaceH4/zephyr-7b-beta",
        use_auth_token=token,
        max_new_tokens=200,
        do_sample=True,
        temperature=0.7,
        top_k=50,
        top_p=0.95
    )

generador = cargar_modelo()

# Interfaz
st.set_page_config(page_title="Psicólogo IA", page_icon="🧠")
st.title("🧠 Chat psicológico en Español")
st.write("Habla conmigo sobre cómo te sientes. Estoy aquí para escucharte y ayudarte.")

# Historial
if "historial" not in st.session_state:
    st.session_state.historial = []

for mensaje in st.session_state.historial:
    st.markdown(mensaje, unsafe_allow_html=True)

# Entrada
with st.form("formulario_chat", clear_on_submit=True):
    entrada = st.text_input("Tú:", key="entrada")
    enviar = st.form_submit_button("Enviar")

if enviar and entrada:
    st.session_state.historial.append(f"<div style='color:blue'><b>Tú:</b> {entrada}</div>")

    # Prompt empático
    prompt = f"""Actúa como un psicólogo empático que habla español. 
Tu tarea es consolar, escuchar, y dar apoyo emocional. 
Si el usuario se siente mal, responde con comprensión, ánimo y calidez. 
Si el mensaje es positivo, alégrate con él. 
Usa un tono cercano y profesional. 

Usuario: {entrada}
Psicólogo:"""

    respuesta = generador(prompt)[0]["generated_text"].split("Psicólogo:")[-1].strip()
    st.session_state.historial.append(f"<div style='color:green'><b>Psicobot:</b> {respuesta}</div>")
