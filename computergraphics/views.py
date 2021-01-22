from django.shortcuts import render
from .models import Post
# Create your views here.
def cg(request):
    cgposts = Post.objects.all()
    context = {'cgposts': cgposts}
    return render(request, 'computergraphics/cg.html', context)

def cgNotes(request):
    return render(request, 'computergraphics/cgnotes.html')

def cgMcqs(request):
    return render(request, 'computergraphics/cgmcqs.html')

def cgLinks(request):
    return render(request, 'computergraphics/cglinks.html')

def cgPosts(request, slug):
    cgpost = Post.objects.filter(slug=slug).first()
    context = {'cgpost': cgpost}
    return render(request, 'computergraphics/cgposts.html', context)