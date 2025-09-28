import streamlit as st

st.set_page_config(page_title="Demo", page_icon="🧠", layout="centered")

st.title("My new streamlit app!")
age = st.text_input("Скільки вам років:")
if age:
    st.success(f"Я знаю, що Вам {age} років!")