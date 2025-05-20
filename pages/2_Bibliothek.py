import streamlit as st
from urllib.parse import quote
from hidden_pages.Begriff import BEGRIFFSINFOS

# 1. Aktuelle Begriffe aus Session holen
entdeckte_begriffe = st.session_state.get("entdeckte", set())
params = st.experimental_get_query_params()
ausgewählter_begriff = params.get("name", [None])[0]

# 2. Titel
st.title("📚 Hämatologie Bibliothek")

# 3. Liste der Begriffe als Links anzeigen
if entdeckte_begriffe:
    for begriff in sorted(entdeckte_begriffe):
        link = f"?name={quote(begriff)}"  # Achtung: nicht "/Detail?", da alles auf einer Seite bleibt!
        st.markdown(f"- [{begriff}]({link})")
else:
    st.info("Noch keine Begriffe entdeckt.")

# 4. Detailansicht, wenn ein Begriff per Query-Parameter übergeben wurde
if ausgewählter_begriff:
    st.markdown("---")
    st.subheader(f"🔍 Detailansicht: {ausgewählter_begriff}")
    if ausgewählter_begriff in BEGRIFFSINFOS:
        st.write(BEGRIFFSINFOS[ausgewählter_begriff])
    else:
        st.info("Für diesen Begriff sind noch keine Infos hinterlegt.")
