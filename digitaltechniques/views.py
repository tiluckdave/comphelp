from django.shortcuts import render, redirect
from .models import Post, Note, Link, Mcq, DtPostComment
from django.contrib import messages
from django.contrib.auth.models import User
from .templatetags import extras
# Create your views here.
def dt(request):
    dtposts = Post.objects.all().order_by('-date')
    context = {'dtposts': dtposts}
    return render(request, 'digitaltechniques/dt.html', context)

def dtNotes(request):
    dtnotes = Note.objects.all().order_by('-date')
    context = {'dtnotes': dtnotes}
    return render(request, 'digitaltechniques/dtnotes.html', context)

def dtMcqs(request):
    dtmcqs = Mcq.objects.all()
    context = {'dtmcqs': dtmcqs}
    return render(request, 'digitaltechniques/dtmcqs.html', context)

def dtLinks(request):
    dtlinks = Link.objects.all()
    context = {'dtlinks': dtlinks}
    return render(request, 'digitaltechniques/dtlinks.html', context)

def dtPosts(request, slug):
    dtpost = Post.objects.filter(slug=slug).first()
    if not dtpost:
        return redirect('/digital-techniques')
    comments= DtPostComment.objects.filter(post=dtpost, parent=None).order_by('-timestamp')
    replies= DtPostComment.objects.filter(post=dtpost).exclude(parent=None).order_by('-timestamp')
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    context = {'dtpost': dtpost, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, 'digitaltechniques/dtposts.html', context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST['comment']
        user=request.user
        postSno =request.POST['postSno']
        post= Post.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            mycomment=DtPostComment(comment=comment, user=user, post=post)
            mycomment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= DtPostComment.objects.get(sno=parentSno)
            mycomment=DtPostComment(comment=comment, user=user, post=post, parent=parent)
            mycomment.save()
            messages.success(request, "Your reply has been posted successfully")
    return redirect(f"/digital-techniques/{post.slug}")
    