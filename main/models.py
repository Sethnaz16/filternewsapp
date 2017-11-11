import datetime
from django.db import models
from django.utils import timezone

# # Create your models here.
# class Greeting(models.Model):
#     when = models.DateTimeField('date created', auto_now_add=True)

class Article(models.Model):
    article_url = models.CharField(max_length = 500)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.article_url
    def was_article_recommended(self):
        return False

class Rating(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField(max_length = 200, default = 'Unknown')
    rating = models.IntegerField(default=0)

