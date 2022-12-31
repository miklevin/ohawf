## Install

`pip install -U ohawf`

Google services require OAuth2 login which is often hard for newbs. If you're trying to do Python things with your Google data (GA, GSC, Sheets, Photos, etc.) and have failed in the past over login issues (should be the easy part but is not), ohawf is for you. It simplifies processes like [GSC API quickstart](https://developers.google.com/webmaster-tools/search-console-api-original/v3/quickstart/quickstart-python) for example.

## How to use

```python
import ohawf

creds = ohawf.get()
```

### Why So Easy?

Ever try to do a project with Google Analytics, Search Console or even Google Photos? General advice sends you to [Goole Cloud Console](https://console.cloud.google.com/), set up a project and download a magic file, and somewhere in this process you give up. This package has done all that for you so that you need only go through the same ***Google Login Prompt*** that apps use.

### A Tale of 2 Installed App Flows

What makes ohawf work is this line:

```python
from google_auth_oauthlib.flow import InstalledAppFlow
```

#### The Old Way: Copy/Paste Token
InstalledAppFlow's ***run_console()*** prompts you to copy/paste a token from a browser tab to Jupyter and used to work well, but that approach has been deprecated. It can still be forced to work, but it's not so easy.

#### The New Way: Gotta Have a Webserver

The new which is now the ohawf default is ***run_local_server()***. This is what you encounter all the time with mobile apps when you see "Login with Google". An embedded browser pops up, goes through login, then returns you to the mobile app. This works in Jupyter too. If you have problems, run Jupyter <a href="https://mikelev.in/ux/">this way</a>. And if you need to force ohawf to use run_console() for a server installation, you can do this:

```python
import ohawf
creds = ohawf.get(cli=True)
```

But then you'll have to whitelist your email address, and you can only do that through the [Goole Cloud Console](https://console.cloud.google.com/) so chicken-and-egg. If you have to go that route, consider just registering as a Google developer and downloading a OAuth Client secret json file like this:

- Go to [https://console.cloud.google.com](https://console.cloud.google.com)
- Make sure you're in the correct Google account.
- Create a new Project.
- Go to API & Services.
- Enable the APIs & Services you want to use.
- Go to Credentials.
- Create a new OAuth 2.0 Client IDs of the Desktop App type.
- Go to OAuth consent screen and set it up.
- Go to +Add users, under test users (gets around tight security)
- Add the users for the test (your gmail, necessary even though already the app owner)
- Go back to Credentials and download OAuth Client.
  - Typically, ***client_secret_[secret].apps.googleusercontent.com.json***
- Use that file with ohawf
  
Once you have the Client Secret JSON file, you can call ohawf like this:

```python
import ohawf

creds = ohawf.get(file="client_secret.json")
```

### Adding Scopes

The ohawf package uses the following default scopes if you don't set any:

    https://www.googleapis.com/auth/spreadsheets
    https://www.googleapis.com/auth/gmail.modify
    https://www.googleapis.com/auth/userinfo.email
    https://www.googleapis.com/auth/youtube.readonly
    https://www.googleapis.com/auth/analytics.readonly
    https://www.googleapis.com/auth/webmasters.readonly
    https://www.googleapis.com/auth/yt-analytics.readonly
    https://www.googleapis.com/auth/photoslibrary.readonly

If you want to set your own scopes, create a Python list of scopes and feed it to ohawf:

```python
creds = ohawf(scopes=scopes)
```
## Google Services

    from apiclient.discovery import build
    
Connect to Google services by giving ***build*** any (activated) API name, version and credentials such listing your GSC sites:

    gsc_service = build('searchconsole', 'v1', credentials=cred)
    gsc_sites = gsc_service.sites().list().execute()
    [print(x['siteUrl']) for x in gsc_sites['siteEntry']];

...or this go list your GA accounts:

    ga_service = build('analytics', 'v3', credentials=cred)
    ga_accounts = ga_service.management().accounts().list().execute()
    [print((x['id'], x['name'])) for x in ga_accounts['items']];

## Copyright (c) 2023 Mike Levin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# Privacy Policy
##  Last updated: March 10, 2023

This app does not collect nor use any of Your Personal data.
