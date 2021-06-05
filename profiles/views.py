from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, ListView, CreateView
from .models import Profile
from .forms import UserProfileForm

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ('bio', 'photo')
    template_name = 'profiles/profile_edit.html'

class ProfileListView(ListView):
    model = Profile
    context_object_name = 'profiles_list'
    template_name = 'profiles/profiles_list.html'

class ProfileCreateView(CreateView):
    form_class = UserProfileForm
    model = Profile
    template_name = 'profiles/profile_reg.html'

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        return super().form_valid(form)




