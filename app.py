import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import os

# Token de Hugging Face (para Streamlit Cloud usar secrets)
TOKEN = st.secrets["HUGGINGFACEHUB_API_TOKEN"]
os.environ["HUGGINGFACEHUB_API_TOKEN"] = TOKEN

# Configurar modelo
model_name = "ITG/DialoGPT-medium-spanish-chitchat"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_auth_token=TOKEN)
model = AutoModelForCausalLM.from_pretrained(model_name, use_auth_token=TOKEN)
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# Página
st.set_page_config(page_title="Chatbot Español IA", page_icon="🧠")
st.title("🧠 Chatbot conversacional en Español")
st.write("Conversación basada en IA con un modelo de lenguaje en español.")

# Inicializar historial
if "chat" not in st.session_state:
    st.session_state.chat = []

# Mostrar historial
for mensaje in st.session_state.chat:
    st.markdown(mensaje, unsafe_allow_html=True)

# Entrada del usuario
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Tú:", key="entrada")
    enviado = st.form_submit_button("Enviar")

# Procesar mensaje
if enviado and user_input:
    st.session_state.chat.append(f"<div style='color:blue'><b>Tú:</b> {user_input}</div>")

    input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt").to(device)

    output_ids = model.generate(
        input_ids,
        max_length=250,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.75
    )

    respuesta = tokenizer.decode(output_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    st.session_state.chat.append(f"<div style='color:green'><b>Bot:</b> {respuesta}</div>")
