from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from pure_pagination import PaginationMixin

from ..models import Post, Tag, Category


class ContactView(PaginationMixin, ListView):
    model = Post
    template_name = "blog_app/contact.html"
    paginate_by = 10
