from django import forms 
from django.urls import reverse

class AnalyzeForm(forms.Form):
    article_url = forms.CharField(max_length=500, required=True)