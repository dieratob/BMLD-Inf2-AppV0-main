# kombis.py

# Definierte Kombinationen: (Begriff1, Begriff2) → Ergebnis
KOMBIS = {
    ("Stammzelle", "Blut"): "Erythropoese",
    ("Stammzelle", "Immunsystem"): "Lymphopoese",
    ("Stammzelle", "Knochenmark"): "Myelopoese",
    ("Erythropoese", "Reifung"): "Erythrozyt",
    ("Lymphopoese", "Reifung"): "T-Zelle",
    ("Myelopoese", "Reifung"): "Granulozyt"
}

def kombiniere(begriff1, begriff2):
    """Versuche Kombination in beide Richtungen"""
    return KOMBIS.get((begriff1, begriff2)) or KOMBIS.get((begriff2, begriff1))
