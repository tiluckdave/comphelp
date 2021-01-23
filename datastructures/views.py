from django.shortcuts import render, redirect
from .models import Post, Note, Link, Mcq, DsPostComment
from django.contrib import messages
from django.contrib.auth.models import User
from .templatetags import extras
# Create your views here.
def ds(request):
    dsposts = Post.objects.all().order_by('-date')
    context = {'dsposts': dsposts}
    return render(request, 'datastructures/ds.html', context)

def dsNotes(request):
    dsnotes = Note.objects.all().order_by('-date')
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
    if not dspost:
        return redirect('/data-structures')
    comments= DsPostComment.objects.filter(post=dspost, parent=None).order_by('-timestamp')
    replies= DsPostComment.objects.filter(post=dspost).exclude(parent=None).order_by('-timestamp')
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    context = {'dspost': dspost, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, 'datastructures/dsposts.html', context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST['comment']
        user=request.user
        postSno =request.POST['postSno']
        post= Post.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            mycomment=DsPostComment(comment=comment, user=user, post=post)
            mycomment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= DsPostComment.objects.get(sno=parentSno)
            mycomment=DsPostComment(comment=comment, user=user, post=post, parent=parent)
            mycomment.save()
            messages.success(request, "Your reply has been posted successfully")
        return redirect(f"/data-structures/{post.slug}")
    else:
        return redirect('/data-structures')

def addTopic(request):
    return render(request, 'datastructures/addtopic.html')

def addNote(request):
    return render(request, 'datastructures/addnote.html')

def addLink(request):
    return render(request, 'datastructures/addlink.html')

def addMcq(request):
    return render(request, 'datastructures/addmcq.html')
    