import streamlit as st
from urllib.parse import quote

entdeckte_begriffe = st.session_state.get("entdeckte", set())

st.title("📚 Hämatologie Bibliothek")

if entdeckte_begriffe:
    for begriff in sorted(entdeckte_begriffe):
        link = f"/Detail?name={quote(begriff)}"
        st.markdown(f"- [{begriff}]({link})")
else:
    st.info("Noch keine Begriffe entdeckt.")