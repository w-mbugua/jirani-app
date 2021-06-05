from typing import List
from django.shortcuts import render, redirect
from django.views.generic import CreateView, View, DetailView, ListView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, PostCreateForm, NewNeighborhoodForm
from django.http import JsonResponse
from django.forms.models import model_to_dict
from posts.models import Post
from locations.models import Neighborhood, Business
from .email import send_welcome_email

def home(request):
    form = PostCreateForm()
    user = request.user
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



class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup/registration_form.html'

    def form_valid(self, form):
        name = form.cleaned_data['username']
        email = form.cleaned_data['email']
        send_welcome_email(name, email)
        return super().form_valid(form)


class PostView(View):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        
        return render(request, 'posts/post_detail.html', {"post": post})

def create_neighborhood(request):
    form = NewNeighborhoodForm()
    if request.method == 'POST':
        form = NewNeighborhoodForm(request.POST)
        if form.is_valid():
            hood = form.save(commit=True)
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



