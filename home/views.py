from django.shortcuts import render ,redirect
from django.contrib import messages

# Create your views here.
from django.http import HttpResponse
from .models import Contact
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout

def home(request):  # jaruri nahi hain ki  hum home.html hi banaye hum kuch bhi bana sakte hain
    return render(request, 'home/home.html')
# def contact(reques
#     return HttpResponse("hello i am a contact ")


def about(request):
    return render(request, "home/about.html")

# def contact(request):
#     if request.method=="POST":
#         name=request.POST.get('name')
#         email=request.POST.get('email')   # yah bhi sahi hain
#         phone=request.POST.get('phone')
#         content =request.POST.get('content')
#         contact=Contact(name=name,email=email, phone=phone, content=content)
#         contact.save()
#         print("this is a post method we are using ")
#     return render(request,"home/contact.html")


def contact(request):
    # messages.error(request, 'welcome to messages')  ya chek karne ke liye hain kam kar raha hin ki nahi
    # messages.info(request, 'Three credits remain in your account.')
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if(len(name) < 2 or len(email) < 3 or len(phone) < 3 or len(content) < 4):
            messages.error(request, 'Please fill the form corretly')
        else:
            contact = Contact(name=name, email=email,
                              phone=phone, content=content)
            contact.save()
            messages.success(
                request, "Your message has been successfully sent")

    return render(request, "home/contact.html")


# def search(request):
#     query=request.GET('search')
#     allPosts= Post.objects.filter(title__icontains=query)
#     params={'allPosts': allPosts}
#     return render(request, 'home/search.html' , params )

# def search(request):
#     query = request.GET['query']
#     if(query.length > 78):
#         allPosts = Post.objects.none
#     else:
#     allPoststitle = Post.objects.filter(title__icontains=query)
#     allPostscontent = Post.objects.filter(content__icontains=query)
#     allPostsauthor = Post.objects.filter(author__icontains=query)
#     allPosts = allPoststitle.union(allPostscontent)
#     params = {'allPosts': allPosts}
#     return render(request, 'home/search.html', params)

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}  #is query ka use  karna hain html page me 
    return render(request, 'home/search.html', params)





def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)>15:
            messages.error(request, " Your user name must be under 15 characters")
            return redirect('home')

        # if not username.isalnum():
        #     messages.error(request, " User name should only contain letters and numbers")
        #     return redirect('home')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")



def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    # return HttpResponse("404- Not found")
   

    # return HttpResponse("login")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')


# def about(request): 
#     return render(request, "home/about.html")