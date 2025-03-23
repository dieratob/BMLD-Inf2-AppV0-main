import streamlit as st
import streamlit_authenticator as stauth
from secrets import token_hex

# Beispielbenutzerdaten
usernames = ["testuser"]
passwords = ["password123"]  # Passwörter sollten sicherer gemacht werden!
hashed_passwords = stauth.Hasher(passwords).generate()

# Authentifizierer erstellen
authenticator = stauth.Authenticate(
    {"usernames": {user: {"password": pwd} for user, pwd in zip(usernames, hashed_passwords)}},
    "cookie_name",
    "random_key",
    cookie_expiry_days=30,
)

# Login-Sektion
name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    st.success(f"Willkommen {name}!")
elif authentication_status == False:
    st.error("Benutzername oder Passwort falsch")
else:
    st.info("Bitte einloggen.")

# Registrierung (als Beispiel)
def register_user(username, password):
    hashed_password = stauth.Hasher([password]).generate()[0]
    usernames.append(username)
    hashed_passwords.append(hashed_password)
    st.success("Registrierung erfolgreich! Bitte einloggen.")

if st.sidebar.button("Registrieren"):
    new_user = st.sidebar.text_input("Benutzername")
    new_password = st.sidebar.text_input("Passwort", type="password")
    if new_user and new_password:
        register_user(new_user, new_password)

authenticator.logout("Abmelden", "sidebar")
