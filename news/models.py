from django.db import models
import datetime as dt


# news_today=news_of_day


# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()

    class Meta:
        ordering = ['first_name']


class Tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(Tags)
    pub_date = models.DateTimeField(auto_now_add=True)

    def save_article(self):
        self.save()
    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news


    @classmethod
    def days_news(cls, date):
        news = cls.objects.filter(pub_date__date=date)
        return news