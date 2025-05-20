import streamlit as st

def back_to_main():
    if st.button("🔙 Zurück zu Hämocraft"):
        st.switch_page("pages/1_Hämocraft.py")