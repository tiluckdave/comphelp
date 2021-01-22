from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Request
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home/index.html')

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
