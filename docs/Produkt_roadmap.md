# Produkt-Roadmap – Hämatologie Learning Game

## Phase 1 – MVP identifizieren
- [x] Start mit 4 Begriffen (Stammzelle, Blut, Immunsystem, Knochenmark)
- [x] Kombination von Begriffen -> MVP gefunden
- [x] Liste an vorgegebenen Kombinationen
- [x] Anzeige entdeckter Begriffe

## Phase 2 – Wireframe erstellen & Prototyp erarbeiten 
- [x] Ersten Fantasie-Entwurf erarbeiten
- [ ] Umsetzbarkeit überprüfen & Wireframe anpassen
- [ ] Prototyp erarbeiten & Nutzertest durchführen

## Phase 3 - Prototyp anpassen anhand Auswertung Nutzertest
- [ ] Tooltips mit medizinischen Erklärungen
- [ ] Suchfunktion für entdeckte Begriffe
- [ ] mehr Kategorien (z. B. Erythropoese, Leukozyten, etc.)

## Phase 4 – Nutzererlebnis verbessern & Prototyp finalisieren
- [ ] Speichern des Spielstands (lokal)
- [ ] Einfaches Tutorial
- [ ] Audio-/Animationseffekte(eventuell)
    (- [ ] Leaderboard / Herausforderungen (eventuell))
    (- [ ] Community-Editor für neue Kombinationen (eventuell))


## MVP Funktionen 

# kombis.py

# Vordefinierte Kombinationen: (Begriff1, Begriff2) → Neues Element
KOMBIS = {
    ("Stammzelle", "Erythropoese"): "Proerythroblast",
    ("Stammzelle", "Myelopoese"): "Myeloblast",
    ("Proerythroblast", "Reifung"): "Erythrozyt",
    ("Myeloblast", "Reifung"): "Neutrophiler Granulozyt",
    ("Knochenmark", "Blut"): "Hämatopoese",
    ("Stammzelle", "Immunsystem"): "Lymphoblast",
    ("Lymphoblast", "Reifung"): "T-Zelle"
}

def kombiniere(a, b):
    """Versucht eine Kombination in beide Richtungen."""
    kombi = KOMBIS.get((a, b)) or KOMBIS.get((b, a))
    return kombi


# main.py
import streamlit as st
from kombis import kombiniere

# Startbegriffe
startbegriffe = ["Stammzelle", "Blut", "Immunsystem", "Knochenmark"]
if "entdeckte" not in st.session_state:
    st.session_state.entdeckte = set(startbegriffe)

st.title("🧬 Hämatologie Learning Game")

st.subheader("🔍 Begriffe kombinieren")
auswahl = list(st.session_state.entdeckte)

col1, col2 = st.columns(2)
with col1:
    begriff1 = st.selectbox("Begriff 1", auswahl)
with col2:
    begriff2 = st.selectbox("Begriff 2", auswahl, index=1 if len(auswahl) > 1 else 0)

if st.button("Kombinieren"):
    if begriff1 == begriff2:
        st.warning("Bitte zwei verschiedene Begriffe auswählen.")
    else:
        ergebnis = kombiniere(begriff1, begriff2)
        if ergebnis:
            if ergebnis not in st.session_state.entdeckte:
                st.success(f"✅ Neue Entdeckung: {ergebnis}")
                st.session_state.entdeckte.add(ergebnis)
            else:
                st.info(f"🔁 {ergebnis} hast du schon entdeckt.")
        else:
            st.error("❌ Keine gültige Kombination.")

st.subheader("📚 Entdeckte Begriffe")
st.write(", ".join(sorted(st.session_state.entdeckte)))

# Begriffe sortieren (Drag-and-Drop Simulation)
auswahl = list(st.session_state.entdeckte)
sortiertes = sort_items(auswahl, multi_select=True)

if len(sortiertes) >= 2:
    begriff1, begriff2 = sortiertes[0], sortiertes[1]
    st.write(f"🧪 Ausgewählte Kombination: **{begriff1} + {begriff2}**")

    if st.button("Kombinieren"):
        if begriff1 == begriff2:
            st.warning("Bitte zwei verschiedene Begriffe auswählen.")
        else:
            ergebnis = kombiniere(begriff1, begriff2)
            if ergebnis:
                if ergebnis not in st.session_state.entdeckte:
                    st.success(f"✅ Neue Entdeckung: {ergebnis}")
                    st.session_state.entdeckte.add(ergebnis)
                else:
                    st.info(f"🔁 {ergebnis} hast du schon entdeckt.")
            else:
                st.error("❌ Keine gültige Kombination.")
else:
    st.info("Bitte mindestens zwei Begriffe per Drag auswählen.")
