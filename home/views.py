from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Request
from django.contrib import messages
from datastructures.models import Post as Dsposts
from digitaltechniques.models import Post as Dtposts
from computergraphics.models import Post as Cgposts
from microprocessors.models import Post as Mpposts
# Create your views here.
def home(request):
    return render(request, 'home/index.html')

def notices(request):
    return render(request, 'home/notices.html')

def search(request):
    if request.GET:
        query = request.GET['q']
        if len(query)>60:
            post1 = post2 = post3 = post4 = Dsposts.objects.none()
        else:
            post1 = Dsposts.objects.filter(title__icontains=query) | Dsposts.objects.filter(slug__icontains=query) | Dsposts.objects.filter(intro__icontains=query) | Dsposts.objects.filter(short__icontains=query)
            post2 = Dtposts.objects.filter(title__icontains=query) | Dtposts.objects.filter(slug__icontains=query) | Dtposts.objects.filter(intro__icontains=query) | Dtposts.objects.filter(short__icontains=query)
            post3 = Cgposts.objects.filter(title__icontains=query) | Cgposts.objects.filter(slug__icontains=query) | Cgposts.objects.filter(intro__icontains=query) | Cgposts.objects.filter(short__icontains=query)
            post4 = Mpposts.objects.filter(title__icontains=query) | Mpposts.objects.filter(slug__icontains=query) | Mpposts.objects.filter(intro__icontains=query) | Mpposts.objects.filter(short__icontains=query)
        context = {'post1': post1, 'post2': post2, 'post3': post3, 'post4': post4, 'query': query}
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
