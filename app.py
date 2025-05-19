import streamlit as st
import requests

# Token privado de Hugging Face
token = st.secrets["HUGGINGFACEHUB_API_TOKEN"]

# Modelo ligero en español (puedes cambiarlo si quieres)
modelo = "tiiuae/falcon-rw-1b"  # o prueba "mistralai/Mistral-7B-Instruct"

headers = {
    "Authorization": f"Bearer {token}"
}

API_URL = f"https://api-inference.huggingface.co/models/{modelo}"

def generar_respuesta(prompt):
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 150,
            "temperature": 0.7,
            "top_k": 50,
            "top_p": 0.95
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()
    if isinstance(result, list):
        return result[0]["generated_text"].split("Psicólogo:")[-1].strip()
    else:
        return "Lo siento, no pude generar una respuesta en este momento."

# Interfaz Streamlit
st.set_page_config(page_title="Psicólogo IA (API)", page_icon="💬")
st.title("🧠 Chat emocional en Español (IA)")
st.write("Responde como un psicólogo empático gracias a IA de Hugging Face.")

if "historial" not in st.session_state:
    st.session_state.historial = []

for m in st.session_state.historial:
    st.markdown(m, unsafe_allow_html=True)

with st.form("form"):
    entrada = st.text_input("Tú:", key="entrada")
    enviar = st.form_submit_button("Enviar")

if enviar and entrada:
    st.session_state.historial.append(f"<div style='color:blue'><b>Tú:</b> {entrada}</div>")

    prompt = f"""Actúa como un psicólogo empático que responde en español.
Responde con comprensión si detectas tristeza, y con alegría si detectas positividad.

Usuario: {entrada}
Psicólogo:"""

    respuesta = generar_respuesta(prompt)
    st.session_state.historial.append(f"<div style='color:green'><b>Psicobot:</b> {respuesta}</div>")
