from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('home')

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/update.html'
    fields = ('body', 'image',)

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
