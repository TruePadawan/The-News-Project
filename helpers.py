from flask import redirect, session
from functools import wraps
from datetime import date
from newsapi import NewsApiClient
import json

def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def getNews():
    newsapi = NewsApiClient(api_key='e4d87e0f7a344caab7bb41c4f7318e84')
    news = newsapi.get_top_headlines(language='en', page_size=10)
    return news

def searchNews(info):
    newsapi = NewsApiClient(api_key='e4d87e0f7a344caab7bb41c4f7318e84')
    news = newsapi.get_everything(qintitle="+"+info, language='en', page_size=20, sort_by='relevancy', 
    from_param=date.today(), to=date.today(), exclude_domains='theonlinecitizen.com,investmentwatchblog.com,protothema.gr,dailymail.co.uk,adweek.com,twit.tv,sankakucomplex.com,guru3d.com,news.com.au,developers.google.com,punchng.com')
    return news