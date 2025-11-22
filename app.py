import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configurar cliente OpenAI
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY", "docker"),
    base_url=os.getenv("OPENAI_BASE_URL", "http://localhost:12434/v1")
)

# Interfaz minimalista
st.title("Mini Chat Local 🐋💖")
st.write("Habla con tu modelo corriendo en Docker Model Runner.")

# Input del usuario
pregunta = st.text_input("Escribe tu pregunta:")

# Botón para enviar
if st.button("Enviar"):
    if pregunta.strip():
        try:
            with st.spinner("Pensando..."):
                respuesta = client.chat.completions.create(
                    model="phi3:mini",
                    messages=[{"role": "user", "content": pregunta}]
                )
                st.success(respuesta.choices[0].message.content)
        except Exception as e:
            st.error(f"Error: {e}")
            st.info("💡 Asegúrate de que Docker Model Runner está corriendo (ver README.md)")
    else:
        st.warning("Escribe algo primero 🙂")

