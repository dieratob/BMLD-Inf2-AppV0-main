import pickle
import streamlit as st
import secrets
import streamlit_authenticator as stauth
from utils.data_manager import DataManager

class LoginManager:
    def __init__(self, data_manager: DataManager = None,
                 auth_credentials_file: str = 'credentials.yaml',
                 auth_cookie_name: str = 'bmld_inf2_streamlit_app',
                 user_session_file: str = 'user_session.pkl'):
        if hasattr(self, 'authenticator'):  # check if instance is already initialized
            return
        
        if data_manager is None:
            return

        self.data_manager = data_manager
        self.auth_credentials_file = auth_credentials_file
        self.auth_cookie_name = auth_cookie_name
        self.user_session_file = user_session_file  # Datei für persistente Anmeldedaten
        self.auth_cookie_key = secrets.token_urlsafe(32)
        self.auth_credentials = self._load_auth_credentials()
        self.authenticator = stauth.Authenticate(self.auth_credentials, self.auth_cookie_name, self.auth_cookie_key)
        
        # Überprüfen, ob eine gespeicherte Sitzung existiert und laden
        self._load_user_session()

    def _load_auth_credentials(self):
        dh = self.data_manager._get_data_handler()
        try:
            return dh.load(self.auth_credentials_file, initial_value={"usernames": {}})
        except Exception as e:
            st.error(f"Fehler beim Laden der Anmeldedaten: {e}")
            return {"usernames": {}}

    def _save_auth_credentials(self):
        dh = self.data_manager._get_data_handler()
        try:
            dh.save(self.auth_credentials_file, self.auth_credentials)
            st.success("Anmeldedaten wurden erfolgreich gespeichert.")
        except Exception as e:
            st.error(f"Fehler beim Speichern der Anmeldedaten: {e}")

    def _load_user_session(self):
        """
        Lädt die Benutzersitzung aus der persistierten Datei.
        """
        try:
            with open(self.user_session_file, 'rb') as f:
                session_data = pickle.load(f)
                if session_data:
                    st.session_state['username'] = session_data['username']
                    st.session_state['authentication_status'] = session_data['authentication_status']
        except FileNotFoundError:
            st.session_state['authentication_status'] = False
            st.session_state['username'] = None

    def _save_user_session(self):
        """
        Speichert die Benutzersitzung in einer Datei.
        """
        with open(self.user_session_file, 'wb') as f:
            session_data = {
                'username': st.session_state.get('username'),
                'authentication_status': st.session_state.get('authentication_status')
            }
            pickle.dump(session_data, f)

    def login_register(self, login_title='Login', register_title='Register new user'):
        """
        Zeigt das Login- und Registrierungsformular an.
        """
        if st.session_state.get("authentication_status") is True:
            self.authenticator.logout()
        else:
            login_tab, register_tab = st.tabs((login_title, register_title))
            with login_tab:
                self.login(stop=False)
            with register_tab:
                self.register()

    def login(self, stop=True):
        """
        Zeigt das Login-Formular und behandelt den Authentifizierungsstatus.
        """
        if st.session_state.get("authentication_status") is True:
            self.authenticator.logout()
        else:
            self.authenticator.login()
            if st.session_state["authentication_status"] is False:
                st.error("Benutzername/Passwort ist inkorrekt.")
            else:
                st.session_state['username'] = self.authenticator.get_username()
                st.session_state['authentication_status'] = True
                self._save_user_session()  # Sitzung speichern, wenn Anmeldung erfolgreich
            if stop:
                st.stop()

    def register(self, stop=True):
        """
        Zeigt das Registrierungsformular und behandelt die Benutzerregistrierung.
        """
        if st.session_state.get("authentication_status") is True:
            self.authenticator.logout()
        else:
            st.info("""
            Das Passwort muss 8-20 Zeichen lang sein und mindestens einen Großbuchstaben, 
            einen Kleinbuchstaben, eine Zahl und ein Sonderzeichen enthalten.
            """)
            res = self.authenticator.register_user()
            if res[1] is not None:
                st.success(f"Benutzer {res[1]} wurde erfolgreich registriert.")
                self._save_auth_credentials()
            if stop:
                st.stop()

    def go_to_login(self, login_page_py_file):
        """
        Führt den Benutzer zur Login-Seite weiter, wenn er nicht angemeldet ist.
        """
        if st.session_state.get("authentication_status") is not True:
            st.switch_page(login_page_py_file)
        else:
            self.authenticator.logout()  # Logout-Button
