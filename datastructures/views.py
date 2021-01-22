from django.shortcuts import render
from .models import Post
# Create your views here.
def ds(request):
    dsposts = Post.objects.all()
    context = {'dsposts': dsposts}
    return render(request, 'datastructures/ds.html', context)

def dsNotes(request):
    return render(request, 'datastructures/dsnotes.html')

def dsMcqs(request):
    return render(request, 'datastructures/dsmcqs.html')

def dsLinks(request):
    return render(request, 'datastructures/dslinks.html')

def dsPosts(request, slug):
    dspost = Post.objects.filter(slug=slug).first()
    context = {'dspost': dspost}
    return render(request, 'datastructures/dsposts.html', context)