from django.shortcuts import render
from .models import Post, Note, Mcq, Link
# Create your views here.
def mp(request):
    mpposts = Post.objects.all()
    context = {'mpposts': mpposts}
    return render(request, 'microprocessors/mp.html', context)

def mpNotes(request):
    mpnotes = Note.objects.all()
    context = {'mpnotes': mpnotes}
    return render(request, 'microprocessors/mpnotes.html', context)

def mpMcqs(request):
    mpmcqs = Mcq.objects.all()
    context = {'mpmcqs': mpmcqs}
    return render(request, 'microprocessors/mpmcqs.html', context)

def mpLinks(request):
    mplinks = Link.objects.all()
    context = {'mplinks': mplinks}
    return render(request, 'microprocessors/mplinks.html', context)

def mpPosts(request, slug):
    mppost = Post.objects.filter(slug=slug).first()
    context = {'mppost': mppost}
    return render(request, 'microprocessors/mpposts.html', context)