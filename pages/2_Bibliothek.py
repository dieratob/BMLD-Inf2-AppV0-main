import streamlit as st
from urllib.parse import quote
from hidden_pages.Begriff import BEGRIFFSINFOS
import os

st.write("Aktuelle Seite:", __file__)

# 1. Aktuelle Seite ermitteln
current_page = os.path.basename(__file__).replace(".py", "")

# 2. Begriffe aus Session holen
entdeckte_begriffe = st.session_state.get("entdeckte", set())
params = st.experimental_get_query_params()
ausgewählter_begriff = params.get("name", [None])[0]

# 3. Seitentitel
st.title("📚 Hämatologie Bibliothek")

# 4. Begriffe als Links anzeigen
if entdeckte_begriffe:
    for begriff in sorted(entdeckte_begriffe):
        link = f"/{current_page}?name={quote(begriff)}"  # 👈 absoluter Link zur aktuellen Seite
        st.markdown(f"- [{begriff}]({link})")
else:
    st.info("Noch keine Begriffe entdeckt.")

# 5. Detailansicht anzeigen
if ausgewählter_begriff:
    st.markdown("---")
    st.subheader(f"🔍 Detailansicht: {ausgewählter_begriff}")
    if ausgewählter_begriff in BEGRIFFSINFOS:
        st.write(BEGRIFFSINFOS[ausgewählter_begriff])
    else:
        st.info("Für diesen Begriff sind noch keine Infos hinterlegt.")


