from django.shortcuts import render
from .models import Post, Note, Link, Mcq
# Create your views here.
def cg(request):
    cgposts = Post.objects.all()
    context = {'cgposts': cgposts}
    return render(request, 'computergraphics/cg.html', context)

def cgNotes(request):
    cgnotes = Note.objects.all()
    context = {'cgnotes': cgnotes}
    return render(request, 'computergraphics/cgnotes.html', context)

def cgMcqs(request):
    cgmcqs = Mcq.objects.all()
    context = {'cgmcqs': cgmcqs}
    return render(request, 'computergraphics/cgmcqs.html', context)

def cgLinks(request):
    cglinks = Link.objects.all()
    context = {'cglinks': cglinks}
    return render(request, 'computergraphics/cglinks.html', context)

def cgPosts(request, slug):
    cgpost = Post.objects.filter(slug=slug).first()
    context = {'cgpost': cgpost}
    return render(request, 'computergraphics/cgposts.html', context)