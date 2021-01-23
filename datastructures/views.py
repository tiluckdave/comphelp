from django.shortcuts import render
from .models import Post, Note, Mcq, Link
# Create your views here.
def ds(request):
    dsposts = Post.objects.all()
    context = {'dsposts': dsposts}
    return render(request, 'datastructures/ds.html', context)

def dsNotes(request):
    dsnotes = Note.objects.all()
    context = {'dsnotes': dsnotes}
    return render(request, 'datastructures/dsnotes.html', context)

def dsMcqs(request):
    dsmcqs = Mcq.objects.all()
    context = {'dsmcqs': dsmcqs}
    return render(request, 'datastructures/dsmcqs.html', context)

def dsLinks(request):
    dslinks = Link.objects.all()
    context = {'dslinks': dslinks}
    return render(request, 'datastructures/dslinks.html', context)

def dsPosts(request, slug):
    dspost = Post.objects.filter(slug=slug).first()
    context = {'dspost': dspost}
    return render(request, 'datastructures/dsposts.html', context)