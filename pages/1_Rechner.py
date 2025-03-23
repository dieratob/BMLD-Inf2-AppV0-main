# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======




import streamlit as st
from bmi_calculator import calculate_bmi

# App-Konfiguration
st.title('BMI Rechner')

with st.form("BMI Eingabeformular"):
    # Eingabe von Größe und Gewicht
    height = st.number_input('Geben Sie Ihre Größe ein (in Meter)', min_value=0.1, max_value=3.0, value=1.7, step=0.01)
    weight = st.number_input('Geben Sie Ihr Gewicht ein (in kg)', min_value=1.0, max_value=500.0, value=70.0, step=0.1)

    # Submit-Button für das Formular
    submitted = st.form_submit_button("Submit")

if submitted:
    result = calculate_bmi(height, weight)
    bmi_value = result["bmi"]
    category = result["category"]

    # Anzeige des berechneten BMI und der Kategorie
    st.write(f'Ihr BMI ist: {bmi_value}')
    st.write(f'Berechnet am: {result["timestamp"].strftime("%d.%m.%Y %H:%M:%S")}')
    st.write(f'Kategorie: {category}')
    
    # Farbliche Darstellung der BMI-Kategorie
    if category == "Untergewicht":
        color = "lightblue"
    elif category == "Normalgewicht":
        color = "green"
    elif category == "Übergewicht":
        color = "yellow"
    elif category == "Adipositas":
        color = "red"

    # Farbliche Darstellung des BMI
    st.markdown(f'<div style="background-color:{color}; padding: 10px; color: white; font-size: 20px;">'
                f'Ihr BMI fällt in die Kategorie: {category}</div>', unsafe_allow_html=True)

    # --- Speichern der BMI-Daten ---
    from utils.data_manager import DataManager
    DataManager().append_record(session_state_key='data_df', record_dict=result)  # update data in session state and storage
