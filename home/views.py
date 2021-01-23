from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Request
from django.contrib import messages
from datastructures.models import Post as Dsposts
from digitaltechniques.models import Post as Dtposts
from computergraphics.models import Post as Cgposts
from microprocessors.models import Post as Mpposts
from datastructures.models import Note as Dsnotes
from digitaltechniques.models import Note as Dtnotes
from computergraphics.models import Note as Cgnotes
from microprocessors.models import Note as Mpnotes
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def notices(request):
    return render(request, 'home/notices.html')

def search(request):
    if request.GET:
        query = request.GET['q']
        if len(query)>60 or len(query)<3:
            post1 = post2 = post3 = post4 = note1 = note2 = note3 = note4 = Dsposts.objects.none()
        else:
            post1 = Dsposts.objects.filter(title__icontains=query) | Dsposts.objects.filter(slug__icontains=query) | Dsposts.objects.filter(intro__icontains=query) | Dsposts.objects.filter(short__icontains=query)
            post2 = Dtposts.objects.filter(title__icontains=query) | Dtposts.objects.filter(slug__icontains=query) | Dtposts.objects.filter(intro__icontains=query) | Dtposts.objects.filter(short__icontains=query)
            post3 = Cgposts.objects.filter(title__icontains=query) | Cgposts.objects.filter(slug__icontains=query) | Cgposts.objects.filter(intro__icontains=query) | Cgposts.objects.filter(short__icontains=query)
            post4 = Mpposts.objects.filter(title__icontains=query) | Mpposts.objects.filter(slug__icontains=query) | Mpposts.objects.filter(intro__icontains=query) | Mpposts.objects.filter(short__icontains=query)
            note1 = Dsnotes.objects.filter(title__icontains=query) | Dsnotes.objects.filter(short__icontains=query)
            note2 = Dtnotes.objects.filter(title__icontains=query) | Dtnotes.objects.filter(short__icontains=query)
            note3 = Cgnotes.objects.filter(title__icontains=query) | Cgnotes.objects.filter(short__icontains=query)
            note4 = Mpnotes.objects.filter(title__icontains=query) | Mpnotes.objects.filter(short__icontains=query)
        context = {'post1': post1, 'post2': post2, 'post3': post3, 'post4': post4, 'note1': note1, 'note2': note2, 'note3': note3, 'note4': note4, 'query': query}
        return render(request, 'home/search.html', context)
    else:
        return render(request, 'home/search.html')

def request(request):
    if request.method=='POST':
        name = request.POST['name']
        subject = request.POST['subject']
        content = request.POST['content']
        if len(content)<60:
            messages.error(request, "your explanation is too short")
        else:
            newrequest = Request(name=name, subject=subject, content=content)
            newrequest.save()
            messages.success(request, "We have received your request")
    return render(request, 'home/request.html')

def handelSignup(request):
    if request.method=='POST':
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        # validate form
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('/')
        if not username.isalnum():
            messages.error(request, "Username should only contain letters and numbers")
            return redirect('/')
        if not username.islower():
            messages.error(request, "Username should be only in lowercase")
            return redirect('/')
        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('/')

        # create the user
        myuser = User.objects.create_user(username=username, email=email, password=pass1)
        myuser.first_name = name
        myuser.save()
        messages.success(request, "Your account has been created successfully")
        user=authenticate(username= username, password= pass2)
        if user is not None:
            login(request, user)
        return redirect('/')
    else:
        return HttpResponse("404 - Not Found")

def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginUsername']
        loginpassword=request.POST['loginPassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('/')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect('/')

    return HttpResponse("404- Not found")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')
