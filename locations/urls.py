from django.urls import path
from .views import add_contact, ContactViewList, add_business

urlpatterns = [ 
    path('add_contact/', add_contact, name='add_contact'),
    path('contacts/', ContactViewList, name='contacts_list'),
    path('add_business/', add_business, name='add_business'),
]