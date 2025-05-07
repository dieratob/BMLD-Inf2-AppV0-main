# pages/Begriff.py

import streamlit as st

# Begriff aus der URL abholen
begriff = st.query_params.get("name")

st.title(f"🔍 Detailansicht: {begriff}")

# Beispiel-Inhalte – hier kannst du individuell Inhalte anzeigen
if begriff == "Erythrozyt":
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/32/Red_blood_cells.jpg", caption="Erythrozyten (rote Blutkörperchen)")
    st.write("""
        Erythrozyten sind die häufigsten Zellen im Blut und für den Sauerstofftransport zuständig.
        Sie entstehen aus Stammzellen über die **Erythropoese**.
    """)
elif begriff == "T-Zelle":
    st.write("T-Zellen sind Teil des adaptiven Immunsystems und entstehen in der Lymphopoese.")
else:
    st.info("Für diesen Begriff sind noch keine Infos hinterlegt.")
