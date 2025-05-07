import streamlit as st

# Begriff aus der URL abholen
begriff = st.query_params.get("name")

# Titel der Seite
st.title(f"🔍 Detailansicht: {begriff}")

# Beispiel-Inhalte – hier kannst du individuell Inhalte anzeigen
if begriff == "Erythrozyt":
    st.write("""
        Erythrozyten sind die häufigsten Zellen im Blut und für den Sauerstofftransport zuständig.
        Sie entstehen aus Stammzellen über die **Erythropoese**.
    """)
elif begriff == "T-Zelle":
    st.write("T-Zellen sind Teil des adaptiven Immunsystems und entstehen in der Lymphopoese.")
elif begriff == "Granulozyt":
    st.write("Granulozyten sind eine Art von weißen Blutkörperchen, die in der Myelopoese entstehen.")
elif begriff == "B-Zelle":
    st.write("B-Zellen sind ein Teil des Immunsystems und entstehen in der Lymphopoese.")
else:
    st.info("Für diesen Begriff sind noch keine Infos hinterlegt.")
