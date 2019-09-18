from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import hub,CodeLinks

# Create your views here.


class hubDetail(DetailView):
    model = hub
    template_name = "detail.html"
    paginate_by =1
    context_object_name = 'detail'
    
    def get_object(self):
        obj = super(hubDetail,self).get_object()
        obj.View_counts +=1
        obj.save()
        return obj
    
    def get_context_data(self, **kwargs):
        context = super(hubDetail,self).get_context_data(**kwargs)
        context['link'] = CodeLinks.objects.all()
        return context
    
class hubList(ListView):
    model = hub
    context_object_name = 'list'
    template_name='list.html'
    paginate_by =2