# pages/2_Bibliothek.py

import streamlit as st
from kombis import KOMBIS

st.title("📚 Hämatologie-Bibliothek")

# Session-Variablen absichern
if "entdeckte" not in st.session_state:
    st.session_state.entdeckte = set()
if "kombihistorie" not in st.session_state:
    st.session_state.kombihistorie = {}

# Alle bekannten Begriffe extrahieren
alle_begriffe = set()
for (a, b), result in KOMBIS.items():
    alle_begriffe.update([a, b, result])

# Entdeckte Begriffe anzeigen
st.subheader("✅ Entdeckte Begriffe")
for begriff in sorted(st.session_state.entdeckte):
    with st.expander(f"{begriff}"):
        kombis = [
            f"{a} + {b} ➜ {c}"
            for (a, b), c in KOMBIS.items()
            if c == begriff
        ]
        if kombis:
            st.write("Mögliche Kombination(en):")
            for k in kombis:
                st.markdown(f"- {k}")
        else:
            st.write("🔍 Keine bekannte Kombination gefunden.")

# Alle Begriffe anzeigen
st.subheader("📖 Alle möglichen Begriffe")
st.write(" | ".join(sorted(alle_begriffe)))
