# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['Credentials', 'get']

# %% ../nbs/00_core.ipynb 4
"""
Google OAuth2 login module.
"""

import json
import pickle
from sys import exit
from os import environ
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import urlopen
import google.auth.transport.requests
from googleapiclient.discovery import build
from google.auth.exceptions import RefreshError
from google_auth_oauthlib.flow import InstalledAppFlow


class Credentials:
    """Login to Google services."""

    def __init__(self, scopes=False):
        environ["OAUTHLIB_RELAX_TOKEN_SCOPE"] = "1"
        self.check_url = "https://www.googleapis.com/oauth2/v1/tokeninfo?access_token="
        self.credential_pickle_file = "credentials.pkl"
        scope_source = None
        if type(scopes) == list:
            scope_source = "Func args"
            self.scopes = scopes
        elif Path("./scopes.csv").is_file():
            scope_source = "scopes.csv"
            with open("./scopes.csv") as file_handle:
                self.scopes = file_handle.read().splitlines()
        else:
            scope_source = "ohawf source code"
            self.scopes = [
                "https://www.googleapis.com/auth/spreadsheets",
                "https://www.googleapis.com/auth/gmail.modify",
                "https://www.googleapis.com/auth/userinfo.email",
                "https://www.googleapis.com/auth/youtube.readonly",
                "https://www.googleapis.com/auth/analytics.readonly",
                "https://www.googleapis.com/auth/webmasters.readonly",
                "https://www.googleapis.com/auth/yt-analytics.readonly",
                "https://www.googleapis.com/auth/photoslibrary.readonly",
            ]
        self.credentials = None
        self.scope_source = scope_source
        credentials_file = "./credentials-default.json"
        if Path("./credentials.json").is_file():
            credentials_file = "./credentials.json"
        try:
            with open(credentials_file, "rb") as handle:
                self.credentials = json.load(handle)
        except:
            self.credentials = json.loads(
                '{"installed":{"client_id":"769904540573-knscs3mhvd56odnf7i8h3al13kiqulft.apps.googleusercontent.com","project_id":"seonotebook-1470430760084","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"D2F1D--b_yKNLrJSPmrn2jik","redirect_uris":["urn:ietf:wg:oauth:2.0:oob","http://localhost"]}}'
            )
        # self.get()

    def get(self):
        try:
            self.credentials = self.refresh_token()
        except Exception as error:
            print(error)
            exit(1)
        return self.credentials

    def login(self):
        """Start web-based Google OAuth2 login prompt."""
        flow = InstalledAppFlow.from_client_config(self.credentials, self.scopes)
        self.credentials = flow.run_local_server()
        with open(self.credential_pickle_file, "wb") as handle:
            pickle.dump(self.credentials, handle)
        return self.credentials

    def refresh_token(self):
        """Refresh token to make new logins generally not required."""

        print(f"Using scopes from {self.scope_source}.")
        print("Logging in... ", end="")
        try:
            with open(self.credential_pickle_file, "rb") as handle:
                self.credentials = pickle.load(handle)
        except FileNotFoundError:
            print("Stored login credentials not found. Login required...")
            self.credentials = self.login()

        request = google.auth.transport.requests.Request()
        login_required, bad_scope = False, False
        try:
            self.credentials.refresh(request)
        except RefreshError as error:
            print("Refresh error!")
            print(error.args[0])
            login_required = True
            if "scope" in error.args[0]:
                bad_scope = True
        if bad_scope:
            Path(self.credential_pickle_file).unlink()
        if login_required:
            self.credentials = self.login()

        # Test if credentials are good
        success = False
        cred_url = self.check_url + self.credentials.token
        try:
            cred_response = urlopen(cred_url)
            success = True
        except Exception as error:
            pass

        if success:
            service = build("oauth2", "v2", credentials=self.credentials)
            user_document = service.userinfo().get().execute()
            full_email = user_document["email"]
            m0, m1 = full_email.split("@")
            masked = [x[1] if x[0] in [0, len(m0)] else "*" for x in enumerate(m0)]
            display_email = f"{''.join(masked)}@{m1}"
            print(f"Successfully logged in as {display_email}")

        return self.credentials


def get():
    """Authenticate"""
    return Credentials().get()


if __name__ == "__main__":
    print("You may provide your own credentials.json and scopes.csv files.")
    print("To create a Google OAuth2 Credentials object:")
    print()
    print("cred = ohawf.get()")
