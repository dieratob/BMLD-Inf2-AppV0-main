# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======

# ------------------------------------------------------------
# === BMI Grafik ===
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Titel der Seite
st.title('BMI Verlauf')

# Lade die Daten
data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine BMI Daten vorhanden. Berechnen Sie Ihren BMI auf der Startseite.')
    st.stop()

# Stil für Matplotlib und Seaborn setzen
sns.set(style="whitegrid")

# Erstelle die Plots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 12))

# Gewicht über Zeit
ax1.plot(data_df['timestamp'], data_df['weight'], color='royalblue', linewidth=2, marker='o', markersize=5)
ax1.set_title('Gewicht über Zeit (kg)', fontsize=14)
ax1.set_xlabel('Zeitpunkt', fontsize=12)
ax1.set_ylabel('Gewicht (kg)', fontsize=12)
ax1.grid(True)

# Größe über Zeit
ax2.plot(data_df['timestamp'], data_df['height'], color='forestgreen', linewidth=2, marker='s', markersize=5)
ax2.set_title('Größe über Zeit (m)', fontsize=14)
ax2.set_xlabel('Zeitpunkt', fontsize=12)
ax2.set_ylabel('Größe (m)', fontsize=12)
ax2.grid(True)

# BMI über Zeit
ax3.plot(data_df['timestamp'], data_df['bmi'], color='darkorange', linewidth=2, marker='D', markersize=5)
ax3.set_title('BMI über Zeit', fontsize=14)
ax3.set_xlabel('Zeitpunkt', fontsize=12)
ax3.set_ylabel('BMI', fontsize=12)
ax3.grid(True)

# Layout anpassen und anzeigen
plt.tight_layout()
st.pyplot(fig)
