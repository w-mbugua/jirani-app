from typing import List
from django.shortcuts import render, redirect
from django.views.generic import CreateView, View
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, PostCreateForm
from django.http import JsonResponse
from posts.models import Post
from locations.models import Neighborhood, Business
from .email import send_welcome_email
from profiles.models import Profile


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup/registration_form.html'

    def form_valid(self, form):
        name = form.cleaned_data['username']
        email = form.cleaned_data['email']
        send_welcome_email(name, email)
        return super().form_valid(form)

def home(request):
    form = PostCreateForm()
    user = request.user
    profile = Profile.objects.filter(user=user)
    # if the user has a profile
    if profile:
        new_area = user.profile.neighborhood
        posts = Post.objects.all().order_by('-pk')

        new_posts = []
        for post in posts:
            if post.get_location() == new_area:
                new_posts.append(post)
        hoods = Neighborhood.objects.all().order_by('-pk')
        businesses = Business.objects.all().order_by('-pk')
        context = {"form": form, "posts": new_posts, "hoods": hoods, "businesses": businesses}
        return render(request, 'home.html', context)
    else:
        return redirect('create_profile')
    
   


def create_post(request):
    form = PostCreateForm(request.POST, request.FILES)
    if form.is_valid():
            author = request.user
            post = form.save(commit=False)
            post.author = author
            post.save()

            data = []
            item = {"id": post.id, "body": post.body, "author": post.author.username, "image": post.image}
            data.append(item)
            return JsonResponse({'data': data}, status=200)
    else:
        print("form not valid", form.errors)
    return redirect('home')


class PostView(View):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        
        return render(request, 'posts/post_detail.html', {"post": post})





