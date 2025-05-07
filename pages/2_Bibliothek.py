# pages/2_Bibliothek.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from kombis import KOMBIS

# Begriffe aus Kombis extrahieren
alle_begriffe = set()
for (a, b), result in KOMBIS.items():
    alle_begriffe.update([a, b, result])

entdeckte = st.session_state.get("entdeckte", set())
kombihistorie = st.session_state.get("kombihistorie", {})

st.title("📖 Begriffsbibliothek")
st.caption("Klicke auf einen entdeckten Begriff, um die Herkunft zu sehen.")

for begriff in sorted(alle_begriffe):
    col1, col2 = st.columns([8, 2])
    with col1:
        if begriff in entdeckte:
            if st.button(f"🔍 {begriff}", key=begriff):
                ursprung = kombihistorie.get(begriff)
                with st.modal(f"🧬 Kombination für: {begriff}"):
                    if ursprung:
                        st.write(f"{ursprung[0]} + {ursprung[1]} → **{begriff}**")
                    else:
                        st.info("Für diesen Begriff ist keine Kombination bekannt (z. B. Startbegriff).")
        else:
            st.markdown(f"🕵️‍♂️ *{begriff}* (noch nicht entdeckt)")
