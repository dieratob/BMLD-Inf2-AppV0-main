# pages/2_Bibliothek.py

import sys
import os
import streamlit as st

# Pfad zur kombis.py eine Ebene höher
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.kombis import KOMBIS

# Alle Begriffe sammeln aus den Kombinationen
alle_begriffe = set()
for (a, b), result in KOMBIS.items():
    alle_begriffe.update([a, b, result])

# Session State abrufen
entdeckte = st.session_state.get("entdeckte", set())
kombihistorie = st.session_state.get("kombihistorie", {})

st.title("📖 Begriffsbibliothek")
st.caption("Klicke auf einen entdeckten Begriff, um Details zu sehen.")

# Anzeige aller Begriffe
for begriff in sorted(alle_begriffe):
    col1, col2 = st.columns([8, 2])
    with col1:
        if begriff in entdeckte:
            # Link zur Detailseite mit Query-Parameter ?name=...
            st.markdown(f"[🔍 {begriff}](Begriff?name={begriff})")
        else:
            st.markdown(f"🕵️‍♂️ *{begriff}* (noch nicht entdeckt)")
