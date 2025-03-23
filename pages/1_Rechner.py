import streamlit as st

# App-Konfiguration
st.set_page_config(page_title="BMI Rechner", page_icon="⚖️")

# Titel und Beschreibung
st.title("⚖️ BMI Rechner")
st.write("Gib dein Gewicht und deine Größe ein, um deinen BMI zu berechnen.")

# Nutzer-Eingaben
weight = st.number_input("Gewicht (kg)", min_value=10.0, max_value=300.0, value=70.0, step=0.1)
height = st.number_input("Größe (m)", min_value=0.5, max_value=2.5, value=1.75, step=0.01)

# BMI Berechnung
if st.button("BMI berechnen"):
    try:
        result = calculate_bmi(weight, height)
        st.write(f"**Dein BMI beträgt:** {result['bmi']:.2f}")

        # Farbcodierung basierend auf BMI-Kategorien
        color_mapping = {
            "Untergewicht": "blue",
            "Normalgewicht": "green",
            "Übergewicht": "yellow",
            "Adipositas": "red"
        }
        color = color_mapping.get(result["category"], "gray")

        # Anzeige des BMI-Werts mit Farbskala
        st.markdown(
            f'<div style="padding:10px; border-radius:5px; background-color:{color}; color:white; font-size:20px; text-align:center;">'
            f'{result["category"]}</div>', unsafe_allow_html=True
        )
    except ValueError as e:
        st.error(str(e))
