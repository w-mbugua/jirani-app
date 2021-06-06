from django.shortcuts import render, redirect
from .forms import ContactCreateForm, BusinessForm, NewNeighborhoodForm
from .models import Contact, Business
from django.urls import reverse
from django.views.generic import DeleteView


def create_neighborhood(request):
    form = NewNeighborhoodForm()
    if request.method == 'POST':
        form = NewNeighborhoodForm(request.POST)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user
            hood.save()
            return redirect('home')
        else:
            print("form not valid", form.errors)
    return render(request, 'location/add_hood.html', {"form": form})

def BusinessListView(request):
    # hood = Neighborhood.objects.get(name=hood)
    businesses = Business.objects.all().order_by('-pk')
    user_location = request.user.profile.neighborhood

    new_businesses = []
    for business in businesses:
        if business.neighborhood == user_location:
            new_businesses.append(business)
    
    return render(request, 'location/biz_list.html', {"businesses": new_businesses})

def add_contact(request):
    form = ContactCreateForm()
    if request.method == 'POST':
        form = ContactCreateForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=True)
            contact.save()
            return redirect('contacts_list')
    return render(request, 'location/create_contact.html', {"form": form})

def ContactViewList(request):
    contacts = Contact.objects.all().order_by('-pk')

    new_contacts = []
    for contact in contacts:
        if contact.get_location() == request.user.get_location():
            new_contacts.append(contact)
    return render(request, 'location/contactlist.html', {"contacts": new_contacts})

def add_business(request):
    form = BusinessForm()
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            biz = form.save(commit=False)
            biz.owner = request.user
            biz.save()
            return redirect('business_list')
    return render(request, 'location/add_business.html', {"form": form})

def neighborhood_details(request):
    user = request.user
    area = user.get_location()
    occupants = area.get_count()
    biz_count = area.count_businesses()
    context = {"occupants": occupants, "area": area, "biz_count": biz_count}
    return render(request, 'location/about.html', context)

def search_business(request):
    searched_word = request.GET.get('searchword')
    results = Business.search_business(searched_word)
    business_list = []
    for business in results:
        if business.neighborhood == request.user.get_location():
            business_list.append(business)
    return render(request, 'location/search.html', {"business_list": business_list, "searched_word": searched_word})




