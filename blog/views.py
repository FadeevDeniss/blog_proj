from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'post'
    fields = ['title', 'author', 'created_at']


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    fields = ['title', 'author', 'body', 'created_at']


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
