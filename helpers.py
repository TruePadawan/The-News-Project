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
    top_headlines = newsapi.get_top_headlines(language='en',
                                                page_size=10)
    return top_headlines