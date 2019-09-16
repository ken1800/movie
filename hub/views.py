from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import hub

# Create your views here.


class hubDetail(DetailView):
    model = hub
    template_name = "index.html"
    #context_object_name = 'manze umeweza kwa details view'
    
class hubList(ListView):
    model = hub
    #context_object_name = ''
    template_name='index.html'