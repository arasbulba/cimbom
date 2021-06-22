from bulbablog.models import Post
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostFrom
from django.urls import reverse_lazy
class HomeView(ListView):
  
  model = Post
  template_name = 'home.html'
  ordering = ['-id']

class PostView(DetailView):
  model = Post
  template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostFrom
    template_name = 'add_post.html'
    
class UpdatePostView(UpdateView):    
  model = Post
  form_class = PostFrom
  template_name = 'update_post.html'
  #fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
  model = Post
  template_name = 'delete_post.html' 
  success_url = reverse_lazy('home')