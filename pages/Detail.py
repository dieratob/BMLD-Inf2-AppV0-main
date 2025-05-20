import streamlit as st
from hidden_pages.Begriff import BEGRIFFSINFOS

# Wenn nicht eingeloggt, umleiten zur Startseite (Login)
if st.session_state.get("authentication_status") != True:
    st.warning("Bitte zuerst einloggen.")
    st.switch_page("Start.py")


params = st.experimental_get_query_params()
begriff = params.get("name", [None])[0]

st.title(f"🔍 Infos: {begriff}")

if begriff and begriff in BEGRIFFSINFOS:
    st.write(BEGRIFFSINFOS[begriff])
else:
    st.info("Für diesen Begriff sind noch keine Infos hinterlegt.")