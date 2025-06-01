import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="BMLD-Inf2-AppV0-main")  # switch drive 

# initialize the login manager
login_manager = LoginManager(data_manager)
login_manager.login_register()  # open login/register page

# load the data from the persistent storage into the session state
data_manager.load_user_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )
# ====== End Init Block ======





import streamlit as st

st.title("Willkommen zu Hämocraft!")

- "Viel Spass beim kombinieren!"
# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

# Streamlit über den Text unten direkt in die App - cool!
"""
Diese App wurde von folgenden Personen entwickelt:
- Dierauer Tobias (dieratob@students.zhaw.ch)
- Assetta Anselmo (assetans@students.zhaw.ch)

basierend auf dem Grundgerüst von:

Samuel Wehrli (wehs@zhaw.ch)
"""