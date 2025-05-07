import sys
import os
import streamlit as st

# 🧠 Session-State initialisieren (ganz oben!)
if "entdeckte" not in st.session_state:
    st.session_state.entdeckte = set(["Stammzelle", "Blut", "Immunsystem", "Knochenmark"])

if "kombihistorie" not in st.session_state:
    st.session_state.kombihistorie = {}

# 🔗 kombis.py importieren (eine Ebene höher)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from kombis import kombiniere

st.title("🧬 Hämatologie Learning Game – MVP")
st.subheader("🔬 Begriffe kombinieren")

# 👉 Aktuell entdeckte Begriffe für die Auswahl
begriff_liste = sorted(list(st.session_state.entdeckte))

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
                st.session_state.kombihistorie[neu] = (begriff1, begriff2)  # 🔁 Herkunft merken
                st.success(f"✅ Neue Entdeckung: {neu}")
            else:
                st.info(f"🔁 {neu} ist bereits entdeckt.")
        else:
            st.error("❌ Keine gültige Kombination.")

# 📚 Ausgabe: entdeckte Begriffe
st.subheader("📚 Entdeckte Begriffe")
if st.session_state.entdeckte:
    st.write(" | ".join(sorted(st.session_state.entdeckte)))
else:
    st.info("Noch keine Begriffe entdeckt.")
