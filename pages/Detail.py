import streamlit as st
from hidden_pages.Begriff import BEGRIFFSINFOS

# ✅ Neue Methode für URL-Parameter
params = st.query_params
begriff = params.get("name", [None])[0]

st.title(f"🔍 Infos: {begriff}")

if begriff and begriff in BEGRIFFSINFOS:
    st.write(BEGRIFFSINFOS[begriff])
else:
    st.info("Für diesen Begriff sind noch keine Infos hinterlegt.")
