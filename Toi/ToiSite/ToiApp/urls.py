from django.urls import path
from .views import PostCreate, PostDetail
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('post/new/', PostCreate.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post-detail'),
]
