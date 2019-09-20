from django.urls import path,include
from .views import hubList,hubDetail,ProjectCategory,ProjectLanguage
app_name= 'hub'
urlpatterns = [
  
    #path('kenny',views.index, name='index'),
     path('', hubList.as_view(), name='hublist_view'),
     path('<int:pk>/', hubDetail.as_view(), name='hubdetails-detail'),
     path('category/<str:category>/', ProjectCategory.as_view(), name='Cate'),
     path('Language/<str:lang>/', ProjectLanguage.as_view(), name='Lan'),
     
   
]
