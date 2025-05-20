import streamlit as st
from hidden_pages.Begriff import BEGRIFFSINFOS

# Neue API verwenden
begriff = st.query_params.get("name")

st.title(f"🔍 Infos: {begriff}")

if begriff and begriff in BEGRIFFSINFOS:
    st.write(BEGRIFFSINFOS[begriff])
else:
    st.info("Für diesen Begriff sind noch keine Infos hinterlegt.")
