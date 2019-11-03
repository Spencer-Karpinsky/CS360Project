from django.urls import paths

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
]
