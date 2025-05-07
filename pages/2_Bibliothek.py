import streamlit as st
from kombis import KOMBIS

st.title("📚 Hämatologie-Bibliothek")

if "entdeckte" not in st.session_state:
    st.session_state.entdeckte = set()
if "kombihistorie" not in st.session_state:
    st.session_state.kombihistorie = {}

# Zustand für offenen Dialog
if "offener_dialog" not in st.session_state:
    st.session_state.offener_dialog = None

# Alle Begriffe
alle_begriffe = set()
for (a, b), result in KOMBIS.items():
    alle_begriffe.update([a, b, result])

st.subheader("✅ Entdeckte Begriffe")

for begriff in sorted(st.session_state.entdeckte):
    if st.button(begriff):
        st.session_state.offener_dialog = begriff

# Wenn ein Dialog aktiv ist
if st.session_state.offener_dialog:
    with st.dialog(f"🧬 Kombination für: {st.session_state.offener_dialog}"):
        ziel = st.session_state.offener_dialog
        kombis = [
            f"{a} + {b} ➜ {c}"
            for (a, b), c in KOMBIS.items()
            if c == ziel
        ]
        if kombis:
            st.write("Mögliche Kombination(en):")
            for k in kombis:
                st.markdown(f"- {k}")
        else:
            st.write("🔍 Keine bekannte Kombination gefunden.")

        if st.button("❌ Schließen"):
            st.session_state.offener_dialog = None

st.subheader("📖 Alle möglichen Begriffe")
st.write(" | ".join(sorted(alle_begriffe)))
