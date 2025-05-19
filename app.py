import streamlit as st
import requests

# Token privado desde secrets
token = st.secrets["HUGGINGFACEHUB_API_TOKEN"]

# Modelo que responde en español (puedes cambiarlo)
modelo = "tiiuae/falcon-rw-1b"  # ligero y gratis

# Configurar API
API_URL = f"https://api-inference.huggingface.co/models/{modelo}"
headers = {"Authorization": f"Bearer {token}"}

# Función para generar respuesta desde Hugging Face Inference API
def generar_respuesta(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 150,
            "temperature": 0.7,
            "top_p": 0.95
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    resultado = response.json()
    if isinstance(resultado, list):
        return resultado[0]["generated_text"].split("Psicólogo:")[-1].strip()
    else:
        return "Lo siento, ahora mismo no puedo responder. Inténtalo en unos segundos."

# UI de Streamlit
st.set_page_config(page_title="Psicólogo IA", page_icon="💬")
st.title("🧠 Chat emocional con IA en Español")
st.write("Cuéntame cómo te sientes. Estoy aquí para ayudarte emocionalmente.")

if "historial" not in st.session_state:
    st.session_state.historial = []

for mensaje in st.session_state.historial:
    st.markdown(mensaje, unsafe_allow_html=True)

with st.form("formulario"):
    entrada = st.text_input("Tú:", key="entrada")
    enviar = st.form_submit_button("Enviar")

if enviar and entrada:
    st.session_state.historial.append(f"<div style='color:blue'><b>Tú:</b> {entrada}</div>")

    prompt = f"""
Actúa como un psicólogo empático que responde en español.
Tu objetivo es consolar, animar, escuchar o celebrar con el usuario, según cómo se sienta.

Usuario: {entrada}
Psicólogo:"""

    respuesta = generar_respuesta(prompt)
    st.session_state.historial.append(f"<div style='color:green'><b>Psicobot:</b> {respuesta}</div>")
