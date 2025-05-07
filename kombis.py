# kombis.py

KOMBIS = {
    ("Stammzelle", "Blut"): "Erythropoese",
    ("Blut", "Stammzelle"): "Erythropoese",

    ("Stammzelle", "Immunsystem"): "Lymphopoese",
    ("Immunsystem", "Stammzelle"): "Lymphopoese",

    ("Stammzelle", "Knochenmark"): "Myelopoese",
    ("Knochenmark", "Stammzelle"): "Myelopoese",

    ("Erythropoese", "Reifung"): "Erythrozyt",
    ("Reifung", "Erythropoese"): "Erythrozyt",

    ("Lymphopoese", "Reifung"): "T-Zelle",
    ("Reifung", "Lymphopoese"): "T-Zelle",

    ("Myelopoese", "Reifung"): "Granulozyt",
    ("Reifung", "Myelopoese"): "Granulozyt",

    ("Blut", "Immunsystem"): "Leukozyt",
    ("Immunsystem", "Blut"): "Leukozyt",

    ("Blut", "Knochenmark"): "Hämatopoese",
    ("Knochenmark", "Blut"): "Hämatopoese",

    ("Immunsystem", "Knochenmark"): "B-Zelle",
    ("Knochenmark", "Immunsystem"): "B-Zelle"
}


def kombiniere(a, b):
    return KOMBIS.get((a, b)) or KOMBIS.get((b, a))

if "kombihistorie" not in st.session_state:
    st.session_state.kombihistorie = {}



