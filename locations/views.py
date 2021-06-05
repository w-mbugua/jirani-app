from django.shortcuts import render, redirect
from .forms import ContactCreateForm
from .models import Contact

def add_contact(request):
    form = ContactCreateForm()
    if request.method == 'POST':
        form = ContactCreateForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=True)
            contact.save()
            return redirect('home')
    return render(request, 'location/create_contact.html', {"form": form})

def ContactViewList(request):
    contacts = Contact.objects.all().order_by('-pk')
    return render(request, 'locations/contactlist.html', {"contact": contacts})


