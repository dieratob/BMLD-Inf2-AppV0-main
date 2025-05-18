import streamlit as st
from Begriff import BEGRIFFSINFOS  # Oder wie auch immer deine Datenstruktur heißt

begriff = st.query_params.get("name", [None])[0]

st.title(f"🔍 Detailansicht: {begriff}")

if begriff and begriff in BEGRIFFSINFOS:
    st.write(BEGRIFFSINFOS[begriff])
else:
    st.info("Für diesen Begriff sind noch keine Infos hinterlegt.")
