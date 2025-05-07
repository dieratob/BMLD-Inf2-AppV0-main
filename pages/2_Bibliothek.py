# pages/2_Bibliothek.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from kombis import KOMBIS  # Wir lesen direkt das Dictionary ein

# Alle Begriffe aus dem Kombi-Dictionary extrahieren
alle_begriffe = set()
for (a, b), result in KOMBIS.items():
    alle_begriffe.update([a, b, result])

# Entdeckte Begriffe aus Session-State lesen
entdeckte = st.session_state.get("entdeckte", set())

st.title("📖 Begriffsbibliothek")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🧠 Entdeckte Begriffe")
    if entdeckte:
        st.write(" | ".join(sorted(entdeckte)))
    else:
        st.info("Noch keine Begriffe entdeckt.")

with col2:
    st.subheader("📚 Alle möglichen Begriffe")
    st.write(" | ".join(sorted(alle_begriffe)))