from django.shortcuts import render, redirect
from .forms import ContactCreateForm, BusinessForm
from .models import Contact
from django.urls import reverse

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



