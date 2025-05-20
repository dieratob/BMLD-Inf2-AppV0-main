# kombis.py

_kombis_roh = {
    ("Myeloische-Vorläuferzelle", "Reifung"): "Megakaryoblast",
    ("Megakaryoblast", "Reifung"): "Promegakaryozyt",
    ("Promegakaryozyt", "Reifung"): "Megakaryozyt",
    ("Megakaryozyt", "Reifung"): "Thrombozyten",
    ("Myeloische-Vorläuferzelle", "Megakaryoblast"): "Proerythroblast",
    ("Proerythroblast", "Reifung"): "B.erythroblast",
    ("B.erythroblast", "Reifung"): "Polychromatischer erythroblast",
    ("Polychromatischer erythroblast", "Reifung"): "Normoblast",
    ("Normoblast", "Reifung"): "Retikulozyt",
    ("Retikulozyt", "Reifung"): "Erythrozyt",
    ("Myeloische-Vorläuferzelle", "Proerythroblast"): "Myeloblast",
    ("Myeloblast", "Reifung"): "B. Promyelzyt",
    ("B. Promyelzyt", "Reifung"): "B. Myelozyt",
    ("B. Myelozyt", "Reifung"): "B. Metamyelozyt",
    ("B. Metamyelozyt", "Reifung"): "Basophiler",
    ("Myeloblast", "B. Promyelzyt"): "N. Promyelzyt",
    ("N. Promyelzyt", "Reifung"): "N. Myelozyt",
    ("N. Myelozyt", "Reifung"): "N.Metamyelozyt",
    ("N.Metamyelozyt", "Reifung"): "Neutrophiler",
    ("Myeloblast", "N. Promyelzyt"): "E. Promyelzyt",
    ("E. Promyelzyt", "Reifung"): "E. Myelozyt",
    ("E. Myelozyt", "Reifung"): "E. Metamyelozyt",
    ("E. Metamyelozyt", "Reifung"): "Eosinophiler",
    ("Myeloblast", "E. Promyelzyt"): "Monoblast",
    ("Monoblast", "Reifung"): "Promonozyt",
    ("Promonozyt", "Reifung"): "Monozyt",
    ("Lymphatisch-Vorläuferzelle", "Reifung"): "Lymphoblast",
    ("Lymphoblast", "Reifung"): "Prolymphozyt",
    ("Prolymphozyt", "Reifung"): "NK-Zelle",
    ("Prolymphozyt", "NK-Zelle"): "B-Lymphozyt",
    ("Prolymphozyt", "B. Lymphozyt"): "T-Lymphozyt",
    ("Immunsystem", "T-Lymphozyt"): "Zellvermittelte Immunität",
    ("Immunsystem", "B-Lymphozyt"): "Humorale Immunität",
    ("Immunsystem", "Monozyt"): "Phagozytose",
    ("Immunsystem", "NK-Zelle"): "Immunüberwachung",
    ("Immunsystem", "Granulozyt"): "Entzündungsreaktion",
    ("Immunsystem", "Neutrophiler"): "Unspezifische Abwehr",
    ("Immunsystem", "Lymphozyt"): "Adaptive Immunantwort"
}


KOMBIS = {}
for (a, b), result in _kombis_roh.items():
    KOMBIS[(a, b)] = result
    KOMBIS[(b, a)] = result  # beide Richtungen

# Kombinationsfunktion
def kombiniere(a, b):
    return KOMBIS.get((a, b))

entdeckte = st.session_state.get("entdeckte", [])

if neuer_begriff not in entdeckte:
    entdeckte.append(neuer_begriff)
    st.session_state["entdeckte"] = entdeckte
    dm.save_data("entdeckte")


