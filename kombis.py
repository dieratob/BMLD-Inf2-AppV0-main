# kombis.py

_kombis_roh = {
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


KOMBIS = {}
for (a, b), result in _kombis_roh.items():
    KOMBIS[(a, b)] = result
    KOMBIS[(b, a)] = result  # beide Richtungen

# Kombinationsfunktion
def kombiniere(a, b):
    return KOMBIS.get((a, b))


