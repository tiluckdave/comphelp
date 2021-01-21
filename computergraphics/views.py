from django.shortcuts import render

# Create your views here.
def cg(request):
    return render(request, 'computergraphics/cg.html')

def cgPosts(request, slug):
    return render(request, 'computergraphics/cgposts.html')