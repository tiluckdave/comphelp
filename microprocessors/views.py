from django.shortcuts import render

# Create your views here.
def mp(request):
    return render(request, 'microprocessors/mp.html')

def mpPosts(request, slug):
    return render(request, 'microprocessors/mpposts.html')