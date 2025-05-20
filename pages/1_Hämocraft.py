import os
import sys
import streamlit as st
from utils.data_manager import DataManager  # 👈 DataManager importieren

# 🔐 Wenn nicht eingeloggt, umleiten zur Startseite (Login)
if st.session_state.get("authentication_status") != True:
    st.warning("Bitte zuerst einloggen.")
    st.switch_page("Start.py")

# 📁 DataManager initialisieren & entdeckte Begriffe laden
dm = DataManager()
dm.load_user_data("entdeckte", "entdeckte.json", initial_value=[])  # Liste statt Set

# Optional: in ein Set umwandeln für schnelle Verarbeitung
entdeckte_set = set(st.session_state.entdeckte)

# 📂 Absoluten Pfad zum Ordner "hidden_pages" berechnen
hidden_pages_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hidden_pages'))

# 📄 kombis.py importieren
pfad_zur_kombis = os.path.join(hidden_pages_path, 'kombis.py')
if not os.path.exists(pfad_zur_kombis):
    st.error("❌ kombis.py nicht gefunden. Stelle sicher, dass die Datei in hidden_pages/ liegt.")
    st.stop()
else:
    if hidden_pages_path not in sys.path:
        sys.path.append(hidden_pages_path)
    from kombis import kombiniere

# 🧠 Kombihistorie initialisieren
if "kombihistorie" not in st.session_state:
    st.session_state.kombihistorie = {}

# 🎮 Titel & Auswahl
st.title("🧬 Hämocraft – Hämatologie Learning Game")
st.subheader("🔬 Begriffe kombinieren")

begriff_liste = sorted(list(entdeckte_set))

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
            if neu not in entdeckte_set:
                entdeckte_set.add(neu)
                st.session_state.kombihistorie[neu] = (begriff1, begriff2)
                st.success(f"✅ Neue Entdeckung: {neu}")
                # 🧠 Begriffe im Session-State & Datei aktualisieren
                st.session_state.entdeckte = list(entdeckte_set)
                dm.save_data("entdeckte")
            else:
                st.info(f"🔁 {neu} ist bereits entdeckt.")
        else:
            st.error("❌ Keine gültige Kombination.")

# 📚 Ausgabe
st.subheader("📚 Entdeckte Begriffe")
if entdeckte_set:
    st.write(" | ".join(sorted(entdeckte_set)))
else:
    st.info("Noch keine Begriffe entdeckt.")
