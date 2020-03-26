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
from .views.index import index
from .views.index import archive
from .views.index import category
from .views.index import tag
from .views.post_detail import post_detail

app_name = "blog_app"
urlpatterns = [
    path("", index, name="index"),
    path("archives/<int:year>/<int:month>", archive, name="archive"),
    path("posts/<int:pk>/", post_detail, name="post_detail"),
    path("category/<int:pk>", category, name="category"),
    path("tag/<int:pk>", tag, name="tag"),
]
