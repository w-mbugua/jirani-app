from django.urls import path
from .views import add_contact, ContactViewList, add_business, neighborhood_details, search_business, create_neighborhood, BusinessListView, BusinessEditView

urlpatterns = [ 
    path('add_contact/', add_contact, name='add_contact'),
    path('contacts/', ContactViewList, name='contacts_list'),
    path('add_neighborhood/', create_neighborhood, name='add_neighborhood'),
    path('about/', neighborhood_details, name='about_neighborhood'),
    path('add_business/', add_business, name='add_business'),
    path('search/', search_business, name='search_business'),
    path('businesses/', BusinessListView, name='business_list'),
    path('<int:pk>/edit_business/', BusinessEditView.as_view(), name='edit_business'),
]