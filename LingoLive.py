import streamlit as st
from googletrans import Translator

st.title("LingoLive: Traductor IA Gratuito")

translator = Translator()

idiomas = {
    'Inglés': 'en',
    'Español': 'es',
    'Francés': 'fr',
    'Alemán': 'de',
    'Italiano': 'it',
    'Portugués': 'pt',
    'Ruso': 'ru',
    'Chino': 'zh-cn',
    'Japonés': 'ja'
}

texto_a_traducir = st.text_area("Ingresa el texto a traducir", height=150)

idioma_origen = st.selectbox("Idioma de origen", list(idiomas.keys()))
idioma_destino = st.selectbox("Idioma de destino", list(idiomas.keys()))

if st.button("Traducir"):
    if texto_a_traducir:
        try:
            traduccion = translator.translate(texto_a_traducir, src=idiomas[idioma_origen], dest=idiomas[idioma_destino])
            st.write("## Traducción:")
            st.write(traduccion.text)
        except Exception as e:
            st.error(f"Error en la traducción: {e}")
    else:
        st.warning("Por favor, ingresa el texto a traducir.")

st.subheader("¿Cómo funciona LingoLive?")

if idioma_origen == "Español" and idioma_destino == "Inglés":
    st.write("Para traducir del español al inglés, ingresa tu texto en español, selecciona 'Español' como idioma de origen e 'Inglés' como idioma de destino. Luego, haz clic en 'Traducir'.")
elif idioma_origen == "Inglés" and idioma_destino == "Español":
    st.write("Para traducir del inglés al español, ingresa tu texto en inglés, selecciona 'Inglés' como idioma de origen e 'Español' como idioma de destino. Luego, haz clic en 'Traducir'.")
else:
    st.write("Selecciona los idiomas de origen y destino para ver las instrucciones de traducción.")