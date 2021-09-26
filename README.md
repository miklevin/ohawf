# ohawf
> Google OAuth2 login that's less ***oh awf*** ul


## Install

`pip install -U ohawf`

Google services require OAuth2 login which is often hard for newbs. If you're trying to do Python things with your Google data (GA, GSC, Sheets, Photos, etc.) and have failed in the past over login issues (should be the easy part but is not), ohawf is for you. It simplifies processes like [GSC API quickstart](https://developers.google.com/webmaster-tools/search-console-api-original/v3/quickstart/quickstart-python) for example.

## How to use

    import ohawf
    cred = ohawf.get()

If it is your first time running you will get a link for the Web-based Google OAuth2 login prompt that looks like:

    Please visit this URL to authorize this application: https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=[foo]&redirect_uri=[foo]&state=[foo]&prompt=consent&access_type=offline
    Enter the authorization code:_________________________

Click it and from the familiar Google login prompt that pops-up pick the account you want to use. If you get a security warning you have to click ***Advanced*** and ***Go to OhAwf (unsafe)***. If this bothers you, you can optionally create your own credentials.json file as described below. Copy/paste the resulting text (a.k.a. "token") back into the Jupyter field and hit Enter. You will then have the authenticated ***credentials object*** needed to connect to and interact with Google services. 

### Running from Terminal

If you are running from a command-line Terminal you will have to copy/paste the login link from your Terminal into a browser, login as normal, and copy the token back into the Terminal. This generally only ever has to be done once.

### Security

This process deposits a credentials.pkl file in that folder that will be continually refreshed eliminating the need for you to have to log in again. Keep both your credentials.json and credentials.pkl file secret. In other words, do not commit them to your Github repos. To help from doing it accidentally, add them both to your .gitignore file.

### Custom Credentials File

By default, the credentials.json file will be used. It is unverified by Google and will cause an OAuth2 security warning on the prompt. You may have to click **Advanced** and **Proceed Anyway** If you wish to provide your own credentials.json file to avoid this warning (optional), follow the below process. 

- Go to https://console.cloud.google.com/
- Create a new Project.
- Go to API & Services.
- Enable the APIs & Services you want to use.
- Go to Credentials.
- Create a new OAuth 2.0 Client IDs of the Desktop App type.
- Go to OAuth consent screen.
- Go to +Add users, under test users.
- Add the users for the test (your gmail, necessary even though already the app owner)
- Download that credentials file.
- Rename that file to default.json
- Drop that file into your working directory

Rename it to "credentials.json" and drop it into your working folder and it will use it instead of the provided credentials.json. 

### Adding Scopes

If you want to work with more Google services than just Analytics and Search Console ([there are hundreds](https://developers.google.com/identity/protocols/oauth2/scopes)) then activate them and add their scope URLs to the scopes.csv file, one per line.

## Google Services

After we have an authenticated credentials object, we build Google services objects with ***build*** from the Google API Python client installed as a requirement of ohawf.

    from apiclient.discovery import build
    
Connect to Google services by giving ***build*** any (activated) API name, version and credentials such listing your GSC sites:

    gsc_service = build('webmasters', 'v3', credentials=cred)
    gsc_sites = gsc_service.sites().list().execute()
    [print(x['siteUrl']) for x in gsc_sites['siteEntry']];

...or this go list your GA accounts:

    ga_service = build('analytics', 'v3', credentials=cred)
    ga_accounts = ga_service.management().accounts().list().execute()
    [print((x['id'], x['name'])) for x in ga_accounts['items']];

Notice how clean this code is compared to [GSC API quickstart](https://developers.google.com/webmaster-tools/search-console-api-original/v3/quickstart/quickstart-python). With better security (OAuth2) comes more complicated procedures. Ohawf is the most lightweight way I have found to alleviate this.

## About the Author
I used to be Mike Levin, [SEO in NYC](https://mikelev.in/). Since our lovely pandemic I got my butt back to Pennsylvania and am now the [Poconos Pythonista](https://www.youtube.com/channel/UCd26IHBHcbtxD7pUdnIgiCw) focusing on the kind of data exploration and automation folks are calling Data Engineering these days. Once upon a time, I worked for legendary Commodore Computers due to my love for the amazing Amiga computer, which spoiled me then caused me to be disappointed with everything to follow. Finally I'm finding the love again using a certain mix of Linux, Python, vim and git (plus Jupyter and Virtual Desktops). Today, I'm part of the J2 family of sites including [Mashable](https://mashable.com/), [PCMag](https://www.pcmag.com/picks/the-best-seo-tools), [Everyday Health](https://www.everydayhealthgroup.com/) and [RetailMeNot](https://www.retailmenot.com/). To thank me for this package, visit these sites. In particular if you use browser shopping plugins and mobile apps, try RMN's [coupon app](https://www.retailmenot.com/mobile) or [coupon plugin](https://www.retailmenot.com/dealfinder/?utm_source=github&utm_medium=employee_miklevin).

## Copyright (c) 2021 Mike Levin

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
##  Last updated: March 10, 2021

This app does not collect nor use any of Your Personal data.
