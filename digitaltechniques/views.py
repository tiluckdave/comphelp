from django.shortcuts import render
from .models import Post
# Create your views here.
def dt(request):
    dtposts = Post.objects.all()
    context = {'dtposts': dtposts}
    return render(request, 'digitaltechniques/dt.html', context)

def dtNotes(request):
    return render(request, 'digitaltechniques/dtnotes.html')

def dtMcqs(request):
    return render(request, 'digitaltechniques/dtmcqs.html')

def dtLinks(request):
    return render(request, 'digitaltechniques/dtlinks.html')

def dtPosts(request, slug):
    dtpost = Post.objects.filter(slug=slug).first()
    context = {'dtpost': dtpost}
    return render(request, 'digitaltechniques/dtposts.html', context)