import streamlit as st
import requests

# Token desde secrets
token = st.secrets["HUGGINGFACEHUB_API_TOKEN"]

# Modelo compatible y funcional vía API
modelo = "PlanTL-GOB-ES/gpt2-base-bne"
API_URL = f"https://api-inference.huggingface.co/models/{modelo}"
headers = {"Authorization": f"Bearer {token}"}

def generar_respuesta(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 100,
            "temperature": 0.7,
            "top_p": 0.95
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    try:
        resultado = response.json()
        if isinstance(resultado, list) and "generated_text" in resultado[0]:
            return resultado[0]["generated_text"].split("Psicólogo:")[-1].strip()
        return "Lo siento, no pude generar una respuesta. ¿Puedes intentarlo de nuevo?"
    except Exception as e:
        return f"⚠️ Error en la respuesta de la API: {str(e)}"

# Interfaz
st.set_page_config(page_title="Chat psicológico", page_icon="🧠")
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
Si el usuario está triste, responde con comprensión. Si está feliz, alégrate con él.

Usuario: {entrada}
Psicólogo:"""

    respuesta = generar_respuesta(prompt)
    st.session_state.historial.append(f"<div style='color:green'><b>Psicobot:</b> {respuesta}</div>")
