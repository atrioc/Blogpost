from django.shortcuts import render
from blog.models import posts

# Create your views here.

def home(request):
    posts_=posts.objects.all()
    return render(request ,"home.html",{"posts":posts_})




def post(request,pk):
    pk_=posts.objects.get(id=pk)
    return render(request ,"post.html",{"pk":pk_})