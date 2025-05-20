import os
import sys
import streamlit as st

# Absoluten Pfad zum Ordner "hidden_pages" berechnen
hidden_pages_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hidden_pages'))

# Prüfen, ob Datei existiert
pfad_zur_kombis = os.path.join(hidden_pages_path, 'kombis.py')
if not os.path.exists(pfad_zur_kombis):
    st.error("❌ kombis.py nicht gefunden. Stelle sicher, dass die Datei in hidden_pages/ liegt.")
else:
    if hidden_pages_path not in sys.path:
        sys.path.append(hidden_pages_path)
    from kombis import kombiniere  # ohne .py-Endung und ohne "hidden_pages."

# 🧠 Session-State initialisieren
if "entdeckte" not in st.session_state:
    st.session_state.entdeckte = set(["Myeloische-Vorläuferzelle", "Immunsystem", "Lymphatisch-Vorläuferzelle", "Reifung"])

if "kombihistorie" not in st.session_state:
    st.session_state.kombihistorie = {}

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
            else:
                st.info(f"🔁 {neu} ist bereits entdeckt.")
        else:
            st.error("❌ Keine gültige Kombination.")

# 📚 Ausgabe
st.subheader("📚 Entdeckte Begriffe")
if st.session_state.entdeckte:
    st.write(" | ".join(sorted(st.session_state.entdeckte)))
else:
    st.info("Noch keine Begriffe entdeckt.")
