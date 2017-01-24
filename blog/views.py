from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import post

# Create your views here.
def index(request):
    posts = post.objects.all()
    latestPost = post.objects.order_by('title', 'publish_date')
    print("hello1")
    print(latestPost)
    print("hello")
    return render(request, 'blog/home.html',{'posts':posts, 'latestPost': latestPost})
