# ohawf
> Google OAuth2 login that's not oh... awful.


## Install

`pip install -U ohawf`

All Google services require this authentication and the difficulties are the biggest barrier for entry for newbs just getting started. If you have dreams of doing nifty Python with all your Google data (GA, GSC, GSheets, etc.) and have failed in the past over mere login issues, this package is for you. For example, ohawf simplifies the SEO-related processes described on their [GSC API quickstart](https://developers.google.com/webmaster-tools/search-console-api-original/v3/quickstart/quickstart-python) page.

## How to use

    import ohawf
    
    credentials = ohawf.Credentials().get()

Import ohawf and create a credentials object like this. You will immediately receive a link for the Web-based Google OAuth2 login prompt. If you're in Jupyter, you can just click it. If you're in Terminal, copy/paste it to the Browser address bar. Pick the account you want when the Google prompt pops up. Copy/paste the token back into Jupyter or terminal. You will then be sitting on top of an authenticated ***credentials object*** that is used to create new Google service objects.

I'm attempting to get App Verification from Google. Until I do, you may need to click ***Advanced*** and ***Go to OhAwf (unsafe)***.

## Google Services

After we have an authenticated credentials object, we build Google services objects with ***build*** from the Google API Python client installed as a requirement of ohawf.

    from apiclient.discovery import build
    
Connect to Google services by giving ***build*** any (activated) API name, version and credetials such listing your GSC sites:

    gsc_service = build('webmasters', 'v3', credentials=credentials)
    gsc_sites = gsc_service.sites().list().execute()
    [print(x['siteUrl']) for x in gsc_sites['siteEntry']];

...or this go list your GA accounts:

    ga_service = build('analytics', 'v3', credentials=credentials)
    ga_accounts = ga_service.management().accounts().list().execute()
    [print((x['id'], x['name'])) for x in ga_accounts['items']];

## Rant
Notice how clean this code is. Missing is all the authentication slop and needless spreading of this process over multiple functions. It seems to be every documenter's favorite game to obfuscate Google service examples, thus infuriating newbs and raising the bar to entry. Just as advancements like Jupyter make software development fun and easy, other things like login become more difficult, I suppose to maintain some comic balance.

## Become a Google Developer
This ohawf package is ready to go. You can pip install it, or clone the Github repo. If you pip install it, you'll be using my Pipulate credentials.json from pip's site-package folder. This is fine, but you have to live with whichever API services I happen to enable through the Google Developers Console. In other words, you can only do stuff with:

- Analytics Reporting
- Chrome UX Report
- Google Search
- Google Analytics
- Google Sheets
- Gmail
- PageSpeed Insights
- YouTube Analytics				
- YouTube Data

If you'd like me to add something to the default, reach out and let me know.

## Google Developers Console
If however you want to take control of your own destiny, using this login trick to perhaps to stuff with Google Photos, Big Query, Maps, or the Google Cloud Platform, you're going to want to replace the credentials.json file with your own. If you pip installed ohawf, then this is burried in pip's site-package folder and will be overwritten again with my own on every pip --upgrade. So git clone it instead, then go to the [Google Developers Console](https://console.developers.google.com/) and get your credentials.json. 

If you switch from a ***pip install*** to ***git clone***, then uninstall the pip version:

    pip uninstall ohawf

## Developers Console vs. Cloud Console
The [Google Developers Console](https://console.developers.google.com/) is the older and simpler version of the [Google Cloud Platform](https://console.cloud.google.com/). You can probably use either one, but these instructions are for the GDC. You have to make at least 1 Project to get a credential file. From the Project you can click *Credentials* on the left-nav and create a new *OAuth 2.0 Client IDs* for *desktop* (middle option). 

## OAuth 2.0 Client IDs (for Desktop)
The ohawf package runs as a user account in a ***Desktop App*** so it can masquerade as you through 3-legged OAuth2 (that Web-login thing). While the alternative ***Service Accounts*** are better for more reliable automation, they would not allow you access to your own data in this context. Think of Jupyter as the desktop app. It all stays private because Jupyter's on your machine. ***Beware sharing credentials on Colab, Asure Notebooks, [MyBinder](https://mybinder.org/) or the like.*** 

Download and rename your *OAuth 2.0 Client IDs* for *desktop* file to credentials.json. It should already have a .json extension. Drop the renamed file into the ohawf repo folder. If you're using Jupyter, it's fine to put it in the upper folder with the .ipynb files. If you're running from command-line, also put a copy of credentials.json in the nested ohawf folder.

## About the Author
I used to be Mike Levin, [SEO in NYC](https://mikelev.in/). Since our lovely pandemic I got my butt back to Pennsylvania and am now the [Poconos Pythonista](https://www.youtube.com/channel/UCd26IHBHcbtxD7pUdnIgiCw) focusing more on the type of data experimentation and automation folks are calling Data Engineering. Once upon a time, I worked for legendary Commodore Computers due to my love for their super ahead-of-its-time Amiga computer. Until recently everything paled in comparison. Finally I'm finding the love again using a certain mix of Linux, Python, vim and git (plus Jupyter and Virtual Desktops). Today, I'm part of the J2 family of sites including [Mashable](https://mashable.com/), [PCMag](https://www.pcmag.com/picks/the-best-seo-tools), [Everyday Health](https://www.everydayhealthgroup.com/) and [RetailMeNot](https://www.retailmenot.com/). To thank me for this package, visit these sites. In particular if you use browser shopping plugins and mobile apps, try RMN's [coupon app](https://www.retailmenot.com/mobile) or [coupon plugin](https://www.retailmenot.com/dealfinder/?utm_source=github&utm_medium=employee_miklevin).

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
