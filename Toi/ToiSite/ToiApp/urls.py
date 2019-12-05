from django.urls import path
from .views import PostCreate, PostDetail, PostListView
from . import views
from accounts import views as account_views
urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('register', account_views.signup, name='register'),
    # path('index', views.index, name='index'),
    path('post/new', PostCreate.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('profile/', views.profile, name='profile'),
    path('index', PostListView.as_view(), name='index'),
    path('view_profile/<int:pk>', views.view_profile, name='view_profile'),
    path('sharableUsers/<int:pk>', views.shareableUsers, name='shareableUsers'),
    path('sharePost/<int:pk>/<int:post_pk>', views.sharePost, name='sharePost'),
    path('addFriends/', views.addFriends, name='addFriends'),
    path('addFriend/<int:pk>', views.addFriend, name='addFriend'),
]
