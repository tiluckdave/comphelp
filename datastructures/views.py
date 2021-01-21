from django.shortcuts import render

# Create your views here.
def ds(request):
    return render(request, 'datastructures/ds.html')

def dsPosts(request, slug):
    return render(request, 'datastructures/dsposts.html')