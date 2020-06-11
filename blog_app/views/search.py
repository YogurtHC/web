from ..models import Post
from django.db.models import Q
from django.shortcuts import render, redirect


def search(request):
    q = request.GET.get("q")
    if not q:
        return redirect("/")
    else:
        post_list = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
        return render(
            request,
            "blog_app/index.html",
            {"post_list": post_list}
        )
