from django.http import HttpResponseRedirect
from django.shortcuts import render

from blog.forms import CommentForm
from blog.models import Comment, Post
from portfolio.models import About


def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    about_section = About.objects.first()  
    context = {
        "posts": posts,
        "about": about_section,
    }
    return render(request, "blog/blog.html", context)

def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by(
        "-created_on"
    )
    print(posts)
    about_section = About.objects.first()  
    context = {"category": category, "posts": posts, "about": about_section}
    return render(request, "blog/category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    about_section = About.objects.first() 
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(post=post)
    context = {"post": post, "comments": comments, "form": form, "about": about_section}

    return render(request, "blog/detail.html", context)
