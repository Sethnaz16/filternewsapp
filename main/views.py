from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Article
from .models import UnreliableSource
from .forms import AnalyzeForm
import datetime 
from django.utils import timezone
import json
import lassie
import pprint
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# Create your views here.
def articles(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:20]
    context = {'latest_article_list': latest_article_list}
    return render(request, 'main/articles.html', context)

def about(request):
    return render(request, 'main/about.html')

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
        # domain = get_domain(url)
        
        # # get labels/tags associated with any sketchy websites
        # label_results = result_data(domain)
        # source_descr = ''
        
        # # Note whether site is reliable or not
        # if label_results == {}:
        #     #Add statement that site isn't known to be unreliable
        #     source_descr = result_descr(0)
        #     is_in_db = 0
        # else:
        #     # Add statement that site is unreliable
        #     source_descr = result_descr(1)
        #     is_in_db = 1
        # # key-value pairs
      
        extract_videos(url)
        parsed_uri = urlparse(url)
        domain = '{uri.netloc}'.format(uri=parsed_uri)
        query_result = UnreliableSource.objects.filter(source__icontains = domain)
        labels = label_desc(query_result)
    
    return render(request, 'main/results.html', {'data': data, 'id': id, 'labels': labels})

def label_desc(query_result):
    desc_label = []
    result = {
        'label': '',
        'desc': ''
    }
    for query in query_result:
        if query.label == 'conspiracy':
            result['label'] = 'conspiracy'  
            result['desc'] = ('Hate Speech:\tSources that are well-known promoters of kooky conspiracy theories.' + 
                             ' Ex: 9/11 conspiracies, chem-trails, lizard people in the sewer systems,' + 
                             ' birther rumors, flat earth ‘theory,’ fluoride as mind control, vaccines as mind control etc')
        if query.label == 'fake':  
            result['label'] = 'fake'
            result['desc'] = ('Fake News:\tSources that entirely fabricate information, disseminate'+ 
                             'deceptive content, and/or grossly distort actual news reports.')
        if query.label == 'unreliable': 
            result['label'] = 'unreliable'
            result['desc'] = 'Proceed With Caution:\tSources that have been flagged but not yet analyzed.'
        if query.label == 'hate':  
            result['label'] = 'hate'
            result['desc'] = ('Hate Speech:\tSources that actively promote racism, misogyny, homophobia, and other' + 
                             'forms of discrimination.')
        if query.label == 'junksci':  
            result['label'] = 'junksci'
            result['desc'] = ('Junk Science:\tSources that promote pseudoscience, metaphysics, naturalistic'+ 
                             'fallacies, and other scientifically dubious claims.')
        if query.label == 'satire':  
            result['label'] = 'satire'
            result['desc'] = ('Satire:\tSources that use humor, irony, exaggeration, ridicule, and false '+
                             'information to comment on current events.')
        if query.label == 'bias':  
            result['label'] = 'bias'
            result['desc'] = ('Extreme Bias:\tSources that come from a particular point of view and '+
                             'may rely on propaganda, decontextualized information, and opinions distorted '+
                             ' as facts. ')
        if query.label == 'rumor':  
            result['label'] = 'rumor'
            result['desc'] = ('Rumor Mill:\tSources that traffic in rumors, gossip, innuendo, and '+
                             'unverified claims.')
        if query.label == 'state':  
            result['label'] = 'state'
            result['desc'] = ('State News:\tSources in repressive states operating under government sanction.')
        if query.label == 'clickbait':  
            result['label'] = 'clickbait'
            result['desc'] = ('Clickbait:\tSources that are well-known promoters of kooky conspiracy '+
                             'theories. Ex: 9/11 conspiracies, chem-trails, lizard people in the sewer '+
                             'systems, birther rumors, flat earth ‘theory,’ fluoride as mind control, '+
                             'vaccines as mind control etc.')
        if query.label == 'reliable':  
            result['label'] = 'reliable'
            result['desc'] = ('This source is reliable')
        if query.label == 'political':  
            result['label'] = 'political'
            result['desc'] = ('*Note:\tTags like political and credible are being used for two reasons: '+
                             '1.) they were suggested by viewers of the document or OpenSources and circulate news '+
                             '2.) the credibility of information and of organizations exists on a continuum, which '+
                             'this project aims to demonstrate. For now, mainstream news organizations are not '+
                             'included because they are well known to a vast majority of readers.')
            
        desc_label.append(result)
        
    return desc_label

def extract_videos(url):
    meet = requests.get(url).text 
    bso = BeautifulSoup(meet, "html.parser")
    videos = bso.findAll({"class": "powa-video"})
    print(videos)
    for i in videos:
        print (str(i))

# def result_descr(number):
#     result = ""
#     if number == 0:
#         result = " currently does not have a history of publishing misinformation. This source can generally be considered trustworthy, but it's still always good to seek information from a wide variety of sources."
#     else:
#         result = " has been identified as a potentially unreliable source of news. We suggest taking this article with a grain of salt and recommend searching for related information from other news sources."
#     return result

# Checks if submitted URL contained in source list database
# returns json of labels and descriptions
# def result_data(article_domain):

#     # Search for domain in database
#     query_result = UnreliableSource.objects.filter(source__iexact = article_domain)
#     # Extract labels/tags attached to each domain in database
    

#     domain_labels = {}
#     if query_result:  
#         # first item in list is site domain
#         # subsequent items are site tags  
#         for i in query_result:
#             domain_labels[i.label.capitalize()] = label_description(i.label)

#     return domain_labels


# Return the description corresponding to a give site tag
# def label_description(label):
#         label1 = str(label)
#         label_descriptions = { 
#                         'conspiracy' : """Conspiracy: Sources that are well-known promoters of kooky conspiracy 
#                         theories. Ex: 9/11 conspiracies, chem-trails, lizard people in the sewer systems, 
#                         birther rumors, flat earth ‘theory,’ fluoride as mind control, vaccines as mind 
#                         control etc.""",
                        
#                         'fake' : """Fake News: Sources that entirely fabricate information, disseminate 
#                             deceptive content, and/or grossly distort actual news reports. """,
                        
#                         'unreliable' : """Proceed With Caution: Sources that have been flagged but not yet analyzed.""",
                        
#                         'hate' : """Hate Speech: Sources that actively promote racism, misogyny, homophobia, and other 
#                             forms of discrimination.""",

#                         'junksci' : """Junk Science: Sources that promote pseudoscience, metaphysics, naturalistic 
#                             fallacies, and other scientifically dubious claims.""",

#                         'satire' : """Satire: Sources that use humor, irony, exaggeration, ridicule, and false 
#                             information to comment on current events. """,

#                         'bias' :  """Extreme Bias: Sources that come from a particular point of view and 
#                             may rely on propaganda, decontextualized information, and opinions distorted as facts. """,

#                         'rumor' : """Rumor Mill: Sources that traffic in rumors, gossip, innuendo, and 
#                             unverified claims.""",

#                         'state' : """State News: Sources in repressive states operating under government sanction.""",

#                         'clickbait' : """Clickbait: Sources that are well-known promoters of kooky conspiracy 
#                             theories. Ex: 9/11 conspiracies, chem-trails, lizard people in the sewer 
#                             systems, birther rumors, flat earth ‘theory,’ fluoride as mind control, 
#                             vaccines as mind control etc.""",

#                         'reliable' : """Political — Tags like political and credible are being used for two reasons: 
#                             1.) they were suggested by viewers of the document or OpenSources and circulate news 
#                             2.) the credibility of information and of organizations exists on a continuum, which 
#                             this project aims to demonstrate. For now, mainstream news organizations are not 
#                             included because they are well known to a vast majority of readers.""",

#                         'political' : """Political — Tags like political and credible are being used for two reasons: 
#                             1.) they were suggested by viewers of the document or OpenSources and circulate news 
#                             2.) the credibility of information and of organizations exists on a continuum, which 
#                             this project aims to demonstrate. For now, mainstream news organizations are not 
#                             included because they are well known to a vast majority of readers."""

#         }

#         label_desc1 = label_descriptions.get(label1, "None")
#         return label_desc1


# def get_domain(url):
#     article_domain = get_tld(url)
#     return str(article_domain).capitalize()



    

    
        

    

