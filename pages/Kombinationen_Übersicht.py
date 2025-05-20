import streamlit as st
import pandas as pd
from kombis import _kombis_roh  # nur _kombis_roh enthält die eindeutigen Original-Kombis
from PIL import Image  # Am Anfang der Datei einfügen


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

# Abschnitt: Hämatopoese-Bild
st.subheader("🧬 Hämatopoese-Diagramm")

# Bild über PIL laden (robuster als direkter Pfad in st.image)
bild = Image.open("../images/hematopoiesishumandiagram-kopie_original.jpg")
st.image(bild, use_container_width=True)

st.markdown("""
**Quelle des Bildes:**  
[Hämatopoese Diagramm auf DocCheck](https://www.doccheck.com/de/detail/photos/15065-haematopoese-diagramm)  
© DocCheck AG – Nutzung nur mit Genehmigung des Urhebers.
""")