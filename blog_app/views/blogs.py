from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from pure_pagination import PaginationMixin

from ..models import Post, Tag, Category


class BlogsView(PaginationMixin, ListView):
    model = Post
    template_name = "blog_app/blogs.html"
    context_object_name = "post_list"

    paginate_by = 10


class CategoryView(BlogsView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get("pk"))
        return super(CategoryView, self).get_queryset().filter(category=cate)


class ArchiveView(BlogsView):
    def get_queryset(self):
        return super(ArchiveView, self).get_queryset().filter(
            created_time__year=self.kwargs.get("year"),
            created_time__month=self.kwargs.get("month")
        )


class TagView(BlogsView):
    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get("pk"))
        return super(TagView, self).get_queryset().filter(tags=tag)

