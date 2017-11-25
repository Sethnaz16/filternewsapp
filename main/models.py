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

    def get_tags(article):




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
    label_descriptions = { 
                    'conspiracy' : """Conspiracy:\tSources that are well-known promoters of kooky conspiracy 
                    theories. Ex: 9/11 conspiracies, chem-trails, lizard people in the sewer systems, 
                    birther rumors, flat earth ‘theory,’ fluoride as mind control, vaccines as mind 
                    control etc.""",
                    
                    'fake' : """Fake News:\tSources that entirely fabricate information, disseminate 
                        deceptive content, and/or grossly distort actual news reports. """,
                    
                    'unreliable' : """Proceed With Caution:\tSources that have been flagged but not yet analyzed.""",
                    
                    'hate' : """Hate Speech:\tSources that actively promote racism, misogyny, homophobia, and other 
                        forms of discrimination.""",

                    'junksci' : """Junk Science:\tSources that promote pseudoscience, metaphysics, naturalistic 
                        fallacies, and other scientifically dubious claims.""",

                    'satire' : """Satire:\tSources that use humor, irony, exaggeration, ridicule, and false 
                        information to comment on current events. """,

                    'bias' :  """Extreme Bias:\tSources that come from a particular point of view and 
                        may rely on propaganda, decontextualized information, and opinions distorted 
                        as facts. """,

                    'rumor' : """Rumor Mill:\tSources that traffic in rumors, gossip, innuendo, and 
                        unverified claims.""",

                    'state' : """State News:\tSources in repressive states operating under government sanction.""",

                    'clickbait' : """Clickbait:\tSources that are well-known promoters of kooky conspiracy 
                        theories. Ex: 9/11 conspiracies, chem-trails, lizard people in the sewer 
                        systems, birther rumors, flat earth ‘theory,’ fluoride as mind control, 
                        vaccines as mind control etc.""",

                    'reliable' : """*Note:\tTags like political and credible are being used for two reasons: 
                        1.) they were suggested by viewers of the document or OpenSources and circulate news 
                        2.) the credibility of information and of organizations exists on a continuum, which 
                        this project aims to demonstrate. For now, mainstream news organizations are not 
                        included because they are well known to a vast majority of readers.""",

                    'political' : """*Note:\tTags like political and credible are being used for two reasons: 
                        1.) they were suggested by viewers of the document or OpenSources and circulate news 
                        2.) the credibility of information and of organizations exists on a continuum, which 
                        this project aims to demonstrate. For now, mainstream news organizations are not 
                        included because they are well known to a vast majority of readers."""

    }




