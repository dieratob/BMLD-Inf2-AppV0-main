import streamlit as st

# Hol dir alle entdeckten Begriffe aus dem Session-State
entdeckte_begriffe = st.session_state.get("entdeckte", set())

st.title("📚 Hämatologie Bibliothek")

if entdeckte_begriffe:
    for begriff in sorted(entdeckte_begriffe):
        # Erzeuge für jeden Begriff einen klickbaren Link, der auf die Detailseite mit ?name=begriff zeigt
        # Beispiel-Link zu Detailseite 'Detail.py' (passe den Dateinamen ggf. an)
        link = f"./Detail?name={begriff}"
        st.markdown(f"- [{begriff}]({link})")
else:
    st.info("Noch keine Begriffe entdeckt.")
