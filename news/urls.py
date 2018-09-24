from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^today/$',views.news_of_day,name='newsToday')
]
'''
In the above, we create a new URLpattern that will match the URL today and connect it to our view function news_of_day. 
'''


