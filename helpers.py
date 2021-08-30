from flask import redirect, session
from functools import wraps
from datetime import date
from newsapi import NewsApiClient
import json

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def getNews():
    newsapi = NewsApiClient(api_key='e4d87e0f7a344caab7bb41c4f7318e84')
    news = newsapi.get_top_headlines(language='en', page_size=20, category="general", page=1)
    return news

def searchNews(info):
    before = date.today()
    before = before.replace(month=(date.today().month - 1))
    newsapi = NewsApiClient(api_key='e4d87e0f7a344caab7bb41c4f7318e84')
    news = newsapi.get_everything(qintitle=info, language='en', page_size=20, 
    from_param=before, to=date.today(), 
    exclude_domains='theonlinecitizen.com,investmentwatchblog.com,protothema.gr,dailymail.co.uk,adweek.com,twit.tv,sankakucomplex.com,guru3d.com,news.com.au,developers.google.com,punchng.com,rappler.com,mb.com.ph,bbc.com,gmanetwork.com,fastcompany.com')
    return news