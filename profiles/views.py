from django.shortcuts import render
from django.views.generic import DetailView, UpdateView
from .models import Profile

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ('bio', 'photo')
    template_name = 'profiles/profile_edit.html'




