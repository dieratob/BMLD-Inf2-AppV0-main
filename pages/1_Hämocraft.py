import os
import sys
import streamlit as st
from utils.data_manager import DataManager

# 🔐 Login-Prüfung
if st.session_state.get("authentication_status") != True:
    st.warning("Bitte zuerst einloggen.")
    st.switch_page("Start.py")

# 📁 Kombis laden
hidden_pages_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hidden_pages'))
pfad_zur_kombis = os.path.join(hidden_pages_path, 'kombis.py')
if not os.path.exists(pfad_zur_kombis):
    st.error("❌ kombis.py nicht gefunden. Stelle sicher, dass die Datei in hidden_pages/ liegt.")
    st.stop()
else:
    if hidden_pages_path not in sys.path:
        sys.path.append(hidden_pages_path)
    from kombis import kombiniere

# 📦 DataManager initialisieren
dm = DataManager()

# 🎮 Startbegriffe
START_BEGRIFFE = [
    "Myeloische-Vorläuferzelle",
    "Immunsystem",
    "Lymphatisch-Vorläuferzelle",
    "Reifung"
]

# 🔁 Begriffe laden oder initialisieren
dm.load_user_data("entdeckte", "entdeckte.json", initial_value=START_BEGRIFFE)
dm.load_user_data("kombihistorie", "kombihistorie.json", initial_value={})

# Sicherstellen, dass entdeckte Begriffe als Set vorliegen
if not isinstance(st.session_state.entdeckte, set):
    st.session_state.entdeckte = set(st.session_state.entdeckte)

# 🎮 Titel & Auswahl
st.title("🧬 Hämocraft – Hämatologie Learning Game")
st.subheader("🔬 Begriffe kombinieren")

begriff_liste = sorted(list(st.session_state.entdeckte))

col1, col2 = st.columns(2)
with col1:
    begriff1 = st.selectbox("Begriff 1", begriff_liste)
with col2:
    begriff2 = st.selectbox("Begriff 2", begriff_liste, index=1 if len(begriff_liste) > 1 else 0)

# 🔁 Kombination starten
if st.button("Kombinieren"):
    if begriff1 == begriff2:
        st.warning("Bitte zwei unterschiedliche Begriffe wählen.")
    else:
        st.write(f"🔍 Kombiversuch: {begriff1} + {begriff2}")
        neu = kombiniere(begriff1, begriff2)
        st.write(f"🎯 Ergebnis: {neu}")
        if neu:
            if neu not in st.session_state.entdeckte:
                st.session_state.entdeckte.add(neu)
                st.session_state.kombihistorie[neu] = (begriff1, begriff2)
                st.success(f"✅ Neue Entdeckung: {neu}")
                # Begriffe speichern
                st.session_state.entdeckte = list(st.session_state.entdeckte)
                dm.save_data("entdeckte")
                dm.save_data("kombihistorie")
                st.session_state.entdeckte = set(st.session_state.entdeckte)
            else:
                st.info(f"🔁 {neu} ist bereits entdeckt.")
        else:
            st.error("❌ Keine gültige Kombination.")

st.subheader("Navigation")

col1, col2 = st.columns(2)
with col1:
    if st.button("📖 Zur Bibliothek"):
        st.session_state.entdeckte = list(st.session_state.entdeckte)  # Daten speichern ggf.
        dm.save_data("entdeckte")
        dm.save_data("kombihistorie")
        st.experimental_set_query_params()  # Optional, falls nötig
        st.experimental_rerun()  # Falls du einen Reload möchtest
        st.switch_page("Bibliothek")  # Name deiner Bibliothek-Seite hier anpassen

with col2:
    if st.button("🔍 Zur Kombinationen Übersicht"):
        st.session_state.entdeckte = list(st.session_state.entdeckte)
        dm.save_data("entdeckte")
        dm.save_data("kombihistorie")
        st.experimental_set_query_params()
        st.experimental_rerun()
        st.switch_page("Kombinationen")  # Name deiner Kombis-Seite hier anpassen

# 🔄 Reset-Funktion
if st.button("🔄 Reset – Alles zurücksetzen"):
    st.session_state.entdeckte = set(START_BEGRIFFE)
    st.session_state.kombihistorie = {}
    st.session_state.entdeckte = list(st.session_state.entdeckte)
    dm.save_data("entdeckte")
    dm.save_data("kombihistorie")
    st.session_state.entdeckte = set(st.session_state.entdeckte)
    st.success("✅ Alles zurückgesetzt.")
