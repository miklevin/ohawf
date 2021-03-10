# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['Credentials']

# Cell
"""
Google OAuth2 login module.
"""
import json
import pickle
from urllib.request import urlopen
import google.auth.transport.requests
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow


class Credentials:
    """Login to Google services."""

    def __init__(self):
        self.check_url = "https://www.googleapis.com/oauth2/v1/tokeninfo?access_token="
        self.scopes = []
        self.scopes.append("https://www.googleapis.com/auth/webmasters.readonly")
        self.scopes.append("https://www.googleapis.com/auth/analytics.readonly")
        self.credentials = None
        try:
            with open("./credentials.json", "rb") as handle:
                self.credentials = json.load(handle)
        except:
            self.credentials = json.loads('{"installed":{"client_id":"769904540573-knscs3mhvd56odnf7i8h3al13kiqulft.apps.googleusercontent.com","project_id":"seonotebook-1470430760084","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"D2F1D--b_yKNLrJSPmrn2jik","redirect_uris":["urn:ietf:wg:oauth:2.0:oob","http://localhost"]}}')
        self.get()

    def login(self):
        """Start web-based Google OAuth2 login prompt."""
        flow = InstalledAppFlow.from_client_config(self.credentials, self.scopes)
        self.credentials = flow.run_console()
        with open("credentials.pkl", "wb") as handle:
            pickle.dump(self.credentials, handle)
        return self.credentials

    def refresh_token(self):
        """Refresh token to make new logins generally not required."""
        with open("credentials.pkl", "rb") as handle:
            self.credentials = pickle.load(handle)
        cred_url = self.check_url + self.credentials.token
        try:
            cred_response = urlopen(cred_url)
        except:
            request = google.auth.transport.requests.Request()
            self.credentials.refresh(request)
            with open("credentials.pkl", "wb") as handle:
                pickle.dump(self.credentials, handle)
        return self.credentials

    def get(self):
        try:
            self.credentials = self.refresh_token()
        except:
            self.credentials = self.login()
        return self.credentials

if __name__ == "__main__":
    credentials = Credentials().get()
    print(credentials)