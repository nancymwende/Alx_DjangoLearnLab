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
    path("search/", views.search_posts, name="search-posts"),

    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("post/<int:pk>/comments/new/", views.add_comment, name="add-comment"),
    path("comment/<int:pk>/edit/", views.edit_comment, name="edit-comment"),
    path("comment/<int:pk>/delete/", views.delete_comment, name="delete-comment"),
    path("post/<int:pk>/comments/new/", views.CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/update/", views.CommentUpdateView.as_view(), name="comment-update"),
    path("comment/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),
    path("tags/<str:tag_name>/",
     views.posts_by_tag,
         name="posts-by-tag"),
]