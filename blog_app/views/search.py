from ..models import Post
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages


def search(request):
    q = request.GET.get("q")
    if not q:
        error_msg = "请输入搜索关键词"
        messages.add_message(request, messages.ERROR, error_msg, extra_tags="danger")
        return redirect("/")
    else:
        post_list = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
        return render(
            request,
            "blog_app/index.html",
            {"post_list": post_list}
        )
