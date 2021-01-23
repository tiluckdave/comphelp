from django.shortcuts import render, redirect
from .models import Post, Note, Link, Mcq, MpPostComment
from django.contrib import messages
from django.contrib.auth.models import User
from .templatetags import extras
# Create your views here.
def mp(request):
    mpposts = Post.objects.all().order_by('-date')
    context = {'mpposts': mpposts}
    return render(request, 'microprocessors/mp.html', context)

def mpNotes(request):
    mpnotes = Note.objects.all().order_by('-date')
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
    if not mppost:
        return redirect('/microprocessors')
    comments= MpPostComment.objects.filter(post=mppost, parent=None).order_by('-timestamp')
    replies= MpPostComment.objects.filter(post=mppost).exclude(parent=None).order_by('-timestamp')
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    context = {'mppost': mppost, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, 'microprocessors/mpposts.html', context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST['comment']
        user=request.user
        postSno =request.POST['postSno']
        post= Post.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            mycomment=MpPostComment(comment=comment, user=user, post=post)
            mycomment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= MpPostComment.objects.get(sno=parentSno)
            mycomment=MpPostComment(comment=comment, user=user, post=post, parent=parent)
            mycomment.save()
            messages.success(request, "Your reply has been posted successfully")
    return redirect(f"/microprocessors/{post.slug}")
    