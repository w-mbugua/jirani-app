from django.urls import path
from .views import home, SignUpView, create_post, PostView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', SignUpView.as_view(), name='signup'),
    path('home/feed/', home, name='home'),
    path('add_post/', create_post, name="add_post"),
    path('post/<int:post_id>', PostView.as_view(), name="post_details"),
]