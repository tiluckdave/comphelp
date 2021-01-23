from django.shortcuts import render
from .models import Post, Note, Mcq, Link
# Create your views here.
def dt(request):
    dtposts = Post.objects.all()
    context = {'dtposts': dtposts}
    return render(request, 'digitaltechniques/dt.html', context)

def dtNotes(request):
    dtnotes = Note.objects.all()
    context = {'dtnotes': dtnotes}
    return render(request, 'digitaltechniques/dtnotes.html', context)

def dtMcqs(request):
    dtmcqs = Mcq.objects.all()
    context = {'dtmcqs': dtmcqs}
    return render(request, 'digitaltechniques/dtmcqs.html', context)

def dtLinks(request):
    dtlinks = Link.objects.all()
    context = {'dtlinks': dtlinks}
    return render(request, 'digitaltechniques/dtlinks.html', context)

def dtPosts(request, slug):
    dtpost = Post.objects.filter(slug=slug).first()
    context = {'dtpost': dtpost}
    return render(request, 'digitaltechniques/dtposts.html', context)