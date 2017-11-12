from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Article
from .forms import AnalyzeForm
import datetime 
from django.utils import timezone
import json
import lassie
import pprint
import requests
from bs4 import BeautifulSoup

# Create your views here.
def articles(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:20]
    context = {'latest_article_list': latest_article_list}
    return render(request, 'main/articles.html', context)

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'main/detail.html', {'article': article })

def results(request, article_id):
    response = "Result page %s." % article_id
    return HttpResponse(response)

def vote(request, article_id):
    return HttpResponse("Vote page %s." % article_id)

def main(request):
    form = AnalyzeForm()
    return render(request, 'main/main.html', {'form': form})

def analyze(request):
    if request.method == 'POST':
        q = Article(article_url=request.POST.get("article_url", ""), pub_date=timezone.now())
        q.save()
        id = q.id
        p = Article.objects.get(pk=id)
        p.result_set.all() 
        p.result_set.create(author='Sith', recommend=True, rating=3)
        url = request.POST.get("article_url", "")
        data = lassie.fetch(url)
        extract_videos(url)
    
    return render(request, 'main/results.html', {'data': data, 'id': id})

def extract_videos(url):
    meet = requests.get(url).text 
    bso = BeautifulSoup(meet, "html.parser")
    videos = bso.findAll({"class": "powa-video"})
    print(videos)
    for i in videos:
        print (str(i))
    
    

