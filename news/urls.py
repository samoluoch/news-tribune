from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.news_of_day,name='newsToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews')
]
'''
In the above, we create a new URLpattern that will match the URL today and connect it to our view function news_of_day. 
'''


