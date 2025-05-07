# Session-State initialisieren (muss ganz am Anfang stehen)
if "entdeckte" not in st.session_state:
    st.session_state.entdeckte = set(["Stammzelle", "Blut", "Immunsystem", "Knochenmark"])

if "kombihistorie" not in st.session_state:
    st.session_state.kombihistorie = {}



import sys
import os

# Kombis.py liegt eine Ebene höher
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from kombis import kombiniere

import streamlit as st

STARTBEGRIFFE = ["Stammzelle", "Blut", "Immunsystem", "Knochenmark"]

# Session-State initialisieren
if "entdeckte" not in st.session_state:
    st.session_state.entdeckte = set(STARTBEGRIFFE)

st.title("🧬 Hämatologie Learning Game – MVP")
st.subheader("🔬 Begriffe kombinieren")

begriff_liste = sorted(st.session_state.entdeckte)
col1, col2 = st.columns(2)
with col1:
    begriff1 = st.selectbox("Begriff 1", begriff_liste)
with col2:
    begriff2 = st.selectbox("Begriff 2", begriff_liste, index=1 if len(begriff_liste) > 1 else 0)

if st.button("Kombinieren"):
    if begriff1 == begriff2:
        st.warning("Bitte zwei unterschiedliche Begriffe wählen.")
    else:
        neu = kombiniere(begriff1, begriff2)
        if neu:
            if neu not in st.session_state.entdeckte:
                st.session_state.entdeckte.add(neu)
                st.success(f"✅ Neue Entdeckung: {neu}")
            else:
                st.info(f"🔁 {neu} ist bereits entdeckt.")
        else:
            st.error("❌ Keine gültige Kombination.")

st.subheader("📚 Entdeckte Begriffe")
st.write(" | ".join(sorted(st.session_state.entdeckte)))
