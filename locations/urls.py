from django.urls import path
from .views import add_contact

urlpatterns = [ 
    path('add_contact/', add_contact, name='add_contact')
]