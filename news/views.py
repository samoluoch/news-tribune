from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Article

import datetime as dt


# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')


# FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
def news_of_day(request):
    date = dt.date.today()
    news = Article.todays_news()
    return render(request, 'all-news/today-news.html', {"date": date, "news": news})


# View Function to present news from past days
def past_days_news(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_of_day)

    news = Article.days_news(date)
    return render(request, 'all-news/past-news.html', {"date": date, "news": news})
