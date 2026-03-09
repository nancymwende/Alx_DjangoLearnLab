from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)
from blog import views

urlpatterns = [
    path("", PostListView.as_view(), name="home"),

    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("post/<int:pk>/comments/new/", views.add_comment, name="add-comment"),
    path("comment/<int:pk>/edit/", views.edit_comment, name="edit-comment"),
    path("comment/<int:pk>/delete/", views.delete_comment, name="delete-comment"),
]