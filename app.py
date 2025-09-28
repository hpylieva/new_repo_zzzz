import streamlit as st

st.set_page_config(page_title="Demo", page_icon="🧠", layout="centered")

st.title("Hello, Streamlit from Colab!")
name = st.text_input("Ваше ім'я:")
if name:
    st.success(f"Привіт, {name}!")
