from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Post , BlogComment,Category


def blogHome(request):
    allPosts= Post.objects.all()
    cats= Category.objects.all()    
    context={'allPosts': allPosts ,'cats':cats}
    return render(request , 'blog/blogHome.html' ,context)

def blogPost(request ,slug):
    
    postbyfilter=Post.objects.filter(slug=slug)  #yaha slug ke hisab se filter kar diya hain
    cats= Category.objects.all()
    context={"postbyfilter":postbyfilter ,'cats':cats}
    return render(request, "blog/blogPost.html", context)

# def  comment(request):
#     allComment=BlogComment.objects.all()
#     context={'allComment':allComment}
#     return render(request , "blog/blogPost.html" , context)    

def showcat(request ,cid):
    # print(cid)
   
    cats= Category.objects.all()

    category = Category.objects.get(pk=cid)
    # print(category)
    # post_sort_by_category = Post.objects.filter(cat=category)
    sort = Post.objects.filter(cat=category)
    #  images = Image.objects.filter()
    # images = Image.objects.all()
    # print(cats)
    context ={"sort":sort ,"cats":cats}
    # return render(request, "blog/blogPost.html", context)
    return render(request, "blog/cate.html", context)


def catlist(request):
    # print(cid)
   
    cats= Category.objects.all()

    # category = Category.objects.get(pk=cid)
    # print(category)
    # post_sort_by_category = Post.objects.filter(cat=category)
    # sort = Post.objects.filter(cat=category)
    #  images = Image.objects.filter()
    # images = Image.objects.all()
    # print(cats)
    context ={"cats":cats}
    # return render(request, "blog/blogPost.html", context)
    return render(request, "blog/base.html", context)

def ccet(request):
    return render(request , "blog/CCET _ Degree Wing.html")






