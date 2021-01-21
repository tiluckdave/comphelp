from django.shortcuts import render

# Create your views here.
def dt(request):
    return render(request, 'digitaltechniques/dt.html')

def dtPosts(request, slug):
    return render(request, 'digitaltechniques/dtposts.html')