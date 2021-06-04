from django.urls import path
from .views import home, SignUpView, create_post, PostView

urlpatterns = [ 
    path('', home, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('add_post/', create_post, name="add_post"),
    path('post/<int:post_id>', PostView.as_view(), name="post_details"),
]