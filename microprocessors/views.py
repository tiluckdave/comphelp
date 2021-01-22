from django.shortcuts import render
from .models import Post
# Create your views here.
def mp(request):
    mpposts = Post.objects.all()
    context = {'mpposts': mpposts}
    return render(request, 'microprocessors/mp.html', context)

def mpNotes(request):
    return render(request, 'microprocessors/mpnotes.html')

def mpMcqs(request):
    return render(request, 'microprocessors/mpmcqs.html')

def mpLinks(request):
    return render(request, 'microprocessors/mplinks.html')

def mpPosts(request, slug):
    mppost = Post.objects.filter(slug=slug).first()
    context = {'mppost': mppost}
    return render(request, 'microprocessors/mpposts.html', context)