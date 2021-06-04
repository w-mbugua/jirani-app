from django.urls import path
from .views import home, SignUpView

urlpatterns = [ 
    path('', home, name='home'),
    path('signup/', SignUpView.as_view(), name='signup')
]