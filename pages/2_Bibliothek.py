import streamlit as st
from hidden_pages.Begriff import BEGRIFFSINFOS

# Entdeckte Begriffe laden
entdeckte_begriffe = st.session_state.get("entdeckte", set())
params = st.experimental_get_query_params()
ausgewählter_begriff = params.get("name", [None])[0]

st.title("📚 Hämatologie Bibliothek")

# Begriffe anzeigen mit Button
if entdeckte_begriffe:
    for begriff in sorted(entdeckte_begriffe):
        if st.button(begriff):
            st.experimental_set_query_params(name=begriff)
            st.experimental_rerun()
else:
    st.info("Noch keine Begriffe entdeckt.")

# Detailansicht anzeigen
if ausgewählter_begriff:
    st.markdown("---")
    st.subheader(f"🔍 Detailansicht: {ausgewählter_begriff}")
    st.write(BEGRIFFSINFOS.get(ausgewählter_begriff, "Keine Infos vorhanden."))


