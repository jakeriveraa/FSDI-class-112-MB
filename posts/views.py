from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.
#Class Based views and Function Based views


class PostListView(ListView):
    """
    PostListView is goint to retrieve all of the objects from the post table in the db
    """

    # template_name attribute is going to render an specific html file
    template_name = "posts/list.html"
    
    # model attribute is to let know django from which model we want to retrieve data
    model = Post
    
    #context_object_name would allow to modifu the name on how we call it inside of the html
    context_object_name = "posts"

class PostDetailView(DetailView):
    """
    PostDetailView class is going to retrieve a single element in the data base
    """
    template_name = "posts/detail.html"    
    model = Post
    context_object_name = "detailed"


class PostCreatView(CreateView):
    """
    PostCreateView class helps us to create a new post object
    """
    template_name = "posts/new.html"
    model = Post
    fields = ["title","subtitle","body"]

    def form_valid(self, form):
        print(form)
        print(User.objects.all())
        form.instance.author = User.objects.filter(is_superuser=True).first()
        return super().form_valid(form)
    

class PostUpdateView(UpdateView):
    """
    PostUpdateView class allow us to edit existing records from the data base
    """
    template_name = "posts/edit.html"
    model = Post
    fields = ["title","subtitle","body"]


class PostDeleteView(DeleteView):
    """
    PostDeletView class allows us to delete an existing record from the data base
    """
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("post_list")