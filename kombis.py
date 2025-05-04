# kombis.py

# Definierte Kombinationen: (Begriff1, Begriff2) → Ergebnis
KOMBIS = {
    # Ausgangskombinationen (inkl. Umkehrung)
    ("Stammzelle", "Blut"): "Erythropoese",
    ("Blut", "Stammzelle"): "Erythropoese",

    ("Stammzelle", "Immunsystem"): "Lymphopoese",
    ("Immunsystem", "Stammzelle"): "Lymphopoese",

    ("Stammzelle", "Knochenmark"): "Myelopoese",
    ("Knochenmark", "Stammzelle"): "Myelopoese",

    # Reifungsschritte
    ("Erythropoese", "Reifung"): "Erythrozyt",
    ("Reifung", "Erythropoese"): "Erythrozyt",

    ("Lymphopoese", "Reifung"): "T-Zelle",
    ("Reifung", "Lymphopoese"): "T-Zelle",

    ("Myelopoese", "Reifung"): "Granulozyt",
    ("Reifung", "Myelopoese"): "Granulozyt",

    # Zusätzliche Startbegriff-Kombinationen für Vollständigkeit
    ("Blut", "Immunsystem"): "Leukozyt",
    ("Immunsystem", "Blut"): "Leukozyt",

    ("Blut", "Knochenmark"): "Hämatopoese",
    ("Knochenmark", "Blut"): "Hämatopoese",

    ("Immunsystem", "Knochenmark"): "B-Zelle",
    ("Knochenmark", "Immunsystem"): "B-Zelle"
}

def kombiniere(begriff1, begriff2):
    """Versuche Kombination in beide Richtungen"""
    return KOMBIS.get((begriff1, begriff2)) or KOMBIS.get((begriff2, begriff1))
