from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gnocchi', views.gnocchi, name='gnocchi'),
    path('ban-seagulls', views.banSeagulls, name='ban-seagulls'),
]