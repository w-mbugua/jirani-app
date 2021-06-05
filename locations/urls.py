from django.urls import path
from .views import add_contact, ContactViewList

urlpatterns = [ 
    path('add_contact/', add_contact, name='add_contact'),
    path('contacts/', ContactViewList, name='contacts_list'),
]