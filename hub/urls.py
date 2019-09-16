from django.urls import path,include
from .views import hubList,hubDetail

urlpatterns = [
  
    #path('kenny',views.index, name='index'),
     path('', hubList.as_view(), name='hublist_view'),
     path('<int:pk>/', hubDetail.as_view(), name='hubdetails-detail'),
    #path('',)
    
]
