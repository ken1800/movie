from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import hub

# Create your views here.


class hubDetail(DetailView):
    model = hub
    template_name = "detail.html"
    paginate_by =1
    #context_object_name = 'manze umeweza kwa details view'
    
class hubList(ListView):
    model = hub
    context_object_name = 'list'
    template_name='list.html'
    paginate_by =2