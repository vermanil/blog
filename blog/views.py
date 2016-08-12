from django.shortcuts import render
from django.utils import timezone
from .models import post

# Create your views here.
def index(request):
    posts = post.objects.filter(title="first post")
    return render(request, 'blog/home.html',{'posts':posts})
