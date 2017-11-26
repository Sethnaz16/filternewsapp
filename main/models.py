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

class Result(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # title = models.CharField(max_length=500)
    # description = models.CharField(max_length=1000)
    # # keywords = ArrayField(models.CharField(max_length = 300))
    # # images = ArrayField(models.CharField(max_length = 300))
    # # videos = ArrayField(models.CharField(max_length = 300))py
    author = models.CharField(max_length=200, default='author')
    recommend = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)



    # def get_tags(article):




class UntrustedSource(models.Model):
    source_url = models.CharField(max_length = 300)

class Source(models.Model):
    source_url = models.CharField(max_length = 300)
        
class Label(models.Model):
    label = models.CharField('Label', max_length = 100)
    description = models.TextField()

class UnreliableSource(models.Model):
    source = models.CharField(max_length = 300)
    label = models.CharField(max_length = 300)

    # article label/tags and their descriptions 

    





