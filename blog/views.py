from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

from .data import data_dict

post = data_dict()

def home(request):
    # return render(request, 'blog/home.html',{"posts":Post.objects.all()})
    return render(request, 'blog/home.html',{"posts":post})

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
