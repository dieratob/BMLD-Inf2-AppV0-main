import streamlit as st
import pandas as pd
from hidden_pages.kombis import _kombis_roh  # nur _kombis_roh enthält die eindeutigen Original-Kombis


# Wenn nicht eingeloggt, umleiten zur Startseite (Login)
if st.session_state.get("authentication_status") != True:
    st.warning("Bitte zuerst einloggen.")
    st.switch_page("Start.py")

st.title("🔍 Übersicht aller Kombinationen")

st.markdown("""
Hier findest du eine vollständige Liste aller im Spiel möglichen Kombinationen.  
Die Reihenfolge der Begriffe spielt im Spiel keine Rolle – beide Varianten funktionieren.
""")

# Tabelle vorbereiten
kombis_liste = [
    {
        "Begriff 1": a,
        "Begriff 2": b,
        "Ergebnis": result
    }
    for (a, b), result in _kombis_roh.items()
]

# DataFrame erzeugen und anzeigen
df = pd.DataFrame(kombis_liste)
st.dataframe(df, use_container_width=True)

