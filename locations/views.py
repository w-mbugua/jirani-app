from django.shortcuts import render, redirect
from .forms import ContactCreateForm

def add_contact(request):
    form = ContactCreateForm()
    if request.method == 'POST':
        form = ContactCreateForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=True)
            contact.save()
            return redirect('home')
    return render(request, 'location/create_contact.html', {"form": form})

