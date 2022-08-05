from django.urls import path

from . import views

urlpatterns = [
    #path("wiki/", views.wiki_index, name="wiki/index"),
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("rand/", views.rand, name="rand"),
    path("create/", views.create, name="create"),
    path("post/", views.post, name="post"),
    path("edit/", views.edit, name="edit"),
    path("append/", views.append, name="append"),
    #path("wiki/<str:name>", views.page, name="page"),
]
