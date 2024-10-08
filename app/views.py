from django.shortcuts import render, redirect
from app.models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.utils import timezone
from app.forms import PostForm


# for the Post List
def postList(request):
    posts = Post.objects.filter(published_at__isnull=False)
    return render(request, "postList.html", {"posts": posts})


def postDetail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, "postDetail.html", {"post": post})


def postDelete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect("postList")


@login_required
def postCreate(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("draftDetail", pk = post.pk)
    else:
        return render(request, "postCreate.html", {"form": form})

@ login_required
def postUpdate(request, pk):
    post = Post.objects.get(id = pk)
    form = PostForm(instance= post)
    if request.method =='POST':
        form = PostForm(request.POST, instance=post)
        post = form.save()
        if post.published_at:
            return redirect('postDetail', post.pk)
        else:
            return redirect('draftDetail', post.pk)
    return render(
        request, 
        'postCreate.html',
        {'form': form}
    )


def draftList(request):
    posts = Post.objects.filter(published_at__isnull=True)
    return render(request, "draftList.html", {"posts": posts})


@login_required
def draftDetail(request, pk):
    post = Post.objects.get(id=pk, published_at__isnull=True)
    return render(request, "draftDetail.html", {"post": post})


def draftDelete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect("draftList")


@login_required
def draftPublish(request, pk):
    post = Post.objects.get(id=pk, published_at__isnull=True)
    post.published_at = timezone.now()
    post.save()
    return redirect("postDetail", pk)
