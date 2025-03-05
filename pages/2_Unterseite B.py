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
    bmi = weight / (height ** 2)
    st.write(f"**Dein BMI beträgt:** {bmi:.2f}")

    # Farbcodierung basierend auf BMI-Kategorien und Anzeige von Peter Griffin GIFs
    if bmi < 18.5:
        color = "blue"
        category = "Untergewicht"
        st.image("https://tenor.com/bCjng.gif", caption="Trauriger Peter Griffin 😞")
    elif 18.5 <= bmi < 25:
        color = "green"
        category = "Normalgewicht"
        st.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExM25oeXhjdTFvbGc5ZW15YXZuNjh5Y3VwYmZxZ251ZWZiNGI4dm94byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/M0C1x0a4yP2uI/giphy.gif", caption="Glücklicher Peter Griffin 😄🎉")
    elif 25 <= bmi < 30:
        color = "yellow"
        category = "Übergewicht"
        st.image("https://tenor.com/bCjng.gif", caption="Trauriger Peter Griffin 😞")
    else:
        color = "red"
        category = "Adipositas (Fettleibigkeit)"
        st.image("https://tenor.com/bCjng.gif", caption="Trauriger Peter Griffin 😞")

    # Anzeige des BMI-Werts mit Farbskala
    st.markdown(
        f'<div style="padding:10px; border-radius:5px; background-color:{color}; color:white; font-size:20px; text-align:center;">'
        f'{category}</div>', unsafe_allow_html=True
    )

