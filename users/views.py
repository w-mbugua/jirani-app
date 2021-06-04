from django.shortcuts import render, redirect
from django.views.generic import CreateView, View
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, PostCreateForm
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Post

def home(request):
    form = PostCreateForm()

    posts = Post.objects.all().order_by('-pk')
  
    context = {"form": form, "posts": posts}
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

