# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['OhAwf']

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


class OhAwf:
    """Login to Google services."""

    def __init__(self):
        self.url = "https://www.googleapis.com/oauth2/v1/tokeninfo?access_token="
        self.scopes = ["https://www.googleapis.com/auth/webmasters.readonly"]
        self.creds = None
        with open("credentials.json", "rb") as handle:
            self.creds = json.load(handle)
        self.run()

    def login(self):
        """Start web-based Google OAuth2 login prompt."""
        flow = InstalledAppFlow.from_client_config(self.creds, self.scopes)
        self.creds = flow.run_console()
        with open("credentials.pkl", "wb") as handle:
            pickle.dump(self.creds, handle)
        return self.creds

    def refresh_token(self):
        """Refresh token to make new logins generally not required."""
        with open("credentials.pkl", "rb") as handle:
            self.creds = pickle.load(handle)
        cred_url = self.url + self.creds.token
        cred_response = urlopen(cred_url)
        cred_bstring = cred_response.read()
        cred_json = json.loads(cred_bstring.decode("utf-8"))
        if "expires_in" in cred_json and cred_json["expires_in"] <= 0:
            request = google.auth.transport.requests.Request()
            self.creds.refresh(request)
            with open("credentials.pkl", "wb") as handle:
                pickle.dump(self.creds, handle)
        return self.creds

    def run(self):
        try:
            self.creds = self.refresh_token()
        except:
            self.creds = self.login()
        return self.creds

# Cell
if __name__ == "__main__":
    owauf = OhAwf()
    credentials = owauf.run()
    print(credentials)