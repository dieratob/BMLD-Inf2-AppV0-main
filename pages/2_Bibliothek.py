import streamlit as st
from urllib.parse import quote

# Wenn nicht eingeloggt, umleiten zur Startseite (Login)
if st.session_state.get("authentication_status") != True:
    st.warning("Bitte zuerst einloggen.")
    st.switch_page("Start.py")


entdeckte_begriffe = st.session_state.get("entdeckte", set())

st.title("📚 Hämatologie Bibliothek")

if entdeckte_begriffe:
    for begriff in sorted(entdeckte_begriffe):
        link = f"/Detail?name={quote(begriff)}"
        st.markdown(f"- [{begriff}]({link})")
else:
    st.info("Noch keine Begriffe entdeckt.")

def back_to_main():
    if st.button("🔙 Zurück zu Hämocraft"):
        st.switch_page("1_Hämocraft.py") 