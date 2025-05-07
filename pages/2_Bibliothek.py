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

# Session-State absichern
if "entdeckte" not in st.session_state:
    st.session_state.entdeckte = set()
if "kombihistorie" not in st.session_state:
    st.session_state.kombihistorie = {}
if "offener_dialog" not in st.session_state:
    st.session_state.offener_dialog = None

entdeckte = st.session_state.entdeckte
kombihistorie = st.session_state.kombihistorie

st.title("📖 Begriffsbibliothek")
st.caption("Klicke auf einen entdeckten Begriff, um die Herkunft zu sehen.")

for begriff in sorted(alle_begriffe):
    col1, col2 = st.columns([8, 2])
    with col1:
        if begriff in entdeckte:
            if st.button(f"🔍 {begriff}", key=begriff):
                st.session_state.offener_dialog = begriff
        else:
            st.markdown(f"🕵️‍♂️ *{begriff}* (noch nicht entdeckt)")

# Dialog anzeigen, falls gesetzt
if st.session_state.offener_dialog:
    ziel = st.session_state.offener_dialog
    ursprung = kombihistorie.get(ziel)

    with st.dialog(f"🧬 Kombination für: {ziel}"):
        if ursprung:
            st.write(f"{ursprung[0]} + {ursprung[1]} → **{ziel}**")
        else:
            st.info("Für diesen Begriff ist keine Kombination bekannt (z. B. Startbegriff).")

        if st.button("❌ Schließen"):
            st.session_state.offener_dialog = None
