"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views.post_detail import PostDetailView
from .views.index import IndexView, CategoryView, ArchiveView, TagView

app_name = "blog_app"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("archives/<int:year>/<int:month>", ArchiveView.as_view(), name="archive"),
    path("category/<int:pk>", CategoryView.as_view(), name="category"),
    path("tag/<int:pk>", TagView.as_view(), name="tag"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
]
