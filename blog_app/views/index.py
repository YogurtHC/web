from django.shortcuts import render, get_object_or_404
from ..models import Post, Tag, Category


def index(request):
    post_list = Post.objects.all()
    tag_list = Tag.objects.all()
    category_list = Category.objects.all()

    return render(request, "blog_app/index.html",
                  context={
                      "post_list": post_list,
                      "tag_list": tag_list,
                      "category_list": category_list,
                  })


def archive(request, year, month):
    post_list = Post.objects.filter(
        created_time__year=year,
        created_time__month=month
    )

    return render(request, "blog_app/index.html",
                  context={
                      "post_list": post_list,
                  })


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by("-created_time")
    return render(request, "blog_app/index.html",
                  context={
                      "post_list": post_list
                  })


def tag(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t).order_by("-created_time")
    return render(request, "blog_app/index.html",
                  context={
                      "post_list": post_list
                  })
