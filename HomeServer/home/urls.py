from django.urls import path

from . import views
from . import api

urlpatterns = [
    path('', views.index, name='index'),
    path('gnocchi', views.gnocchi, name='gnocchi'),
    path('ban-seagulls', views.banSeagulls, name='ban-seagulls'),
    path('justi', views.justi, name='justi'),
    path('home-control', views.homeControl, name='home-control'),
    path('poll', api.poll, name='poll'),
    path('recipe', api.recipe, name='recipe'),
    path('switch', api.switch, name='switch'),
    path('leashem', views.leashem, name='leashem'),
    path('truth', views.truth, name='truth'),
]