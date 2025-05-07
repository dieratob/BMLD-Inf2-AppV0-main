import streamlit as st

# Session-State initialisieren (falls noch nicht vorhanden)
if "entdeckte" not in st.session_state:
    st.session_state.entdeckte = set(["Stammzelle", "Blut", "Immunsystem", "Knochenmark"])

# Überschrift und Beschreibung
st.title("🧬 Hämatologie Learning Game – Begriff hinzufügen")
st.caption("Füge neue Begriffe hinzu, die du entdeckt hast.")

# Eingabe für den Begriff
begriff = st.text_input("Begriff hinzufügen", "")

# Button, um den Begriff zu speichern
if st.button("Begriff hinzufügen"):
    if begriff:
        # Begriff zum Session-State hinzufügen
        st.session_state.entdeckte.add(begriff)
        st.success(f"✅ Begriff '{begriff}' erfolgreich hinzugefügt!")
    else:
        st.warning("Bitte gib einen Begriff ein.")

# Anzeigen der entdeckten Begriffe
st.subheader("📚 Entdeckte Begriffe:")
st.write(" | ".join(sorted(st.session_state.entdeckte)))
