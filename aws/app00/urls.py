from django.urls import path
from . import views

urlpatterns = [
    path('', views.root_to_index, name='noname'),
    path('index/', views.index, name='index'),
    path('misc/dm/', views.dm, name='dm'),
    path('misc/options/', views.options, name='options'),
    path('misc/about/', views.about, name='about'),
]


