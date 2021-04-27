from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Post , BlogComment


def blogHome(request):
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    return render(request , 'blog/blogHome.html' ,context)

def blogPost(request ,slug):
    
    postbyfilter=Post.objects.filter(slug=slug)  #yaha slug ke hisab se filter kar diya hain
    context={"postbyfilter":postbyfilter}
    return render(request, "blog/blogPost.html", context)

# def  comment(request):
#     allComment=BlogComment.objects.all()
#     context={'allComment':allComment}
#     return render(request , "blog/blogPost.html" , context)    

def ccet(request):
    return render(request , "blog/CCET _ Degree Wing.html")






