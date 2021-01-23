from django.shortcuts import render, redirect
from .models import Post, Note, Link, Mcq, CgPostComment
from django.contrib import messages
from django.contrib.auth.models import User
from .templatetags import extras

# Create your views here.
def cg(request):
    cgposts = Post.objects.all().order_by('-date')
    context = {'cgposts': cgposts}
    return render(request, 'computergraphics/cg.html', context)

def cgNotes(request):
    cgnotes = Note.objects.all().order_by('-date')
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
    if not cgpost:
        return redirect('/computer-graphics')
    comments= CgPostComment.objects.filter(post=cgpost, parent=None).order_by('-timestamp')
    replies= CgPostComment.objects.filter(post=cgpost).exclude(parent=None).order_by('-timestamp')
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    context = {'cgpost': cgpost, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request, 'computergraphics/cgposts.html', context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST['comment']
        user=request.user
        postSno =request.POST['postSno']
        post= Post.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            mycomment=CgPostComment(comment=comment, user=user, post=post)
            mycomment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= CgPostComment.objects.get(sno=parentSno)
            mycomment=CgPostComment(comment=comment, user=user, post=post, parent=parent)
            mycomment.save()
            messages.success(request, "Your reply has been posted successfully")
    return redirect(f"/computer-graphics/{post.slug}")
    