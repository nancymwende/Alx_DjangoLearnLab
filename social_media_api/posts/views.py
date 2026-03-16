from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.contenttypes.models import ContentType
from notifications.models import Notification



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def feed(request):

    following_users = request.user.following.all()

    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

    serializer = PostSerializer(posts, many=True)

    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):

    post = Post.objects.get(pk=pk)

    like, created = Like.objects.get_or_create(
        user=request.user,
        post=post
    )

    if not created:
        return Response({"message": "You already liked this post"})

    Notification.objects.create(
        recipient=post.author,
        actor=request.user,
        verb="liked your post",
        content_type=ContentType.objects.get_for_model(post),
        object_id=post.id
    )

    return Response({"message": "Post liked"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):

    post = Post.objects.get(pk=pk)

    Like.objects.filter(
        user=request.user,
        post=post
    ).delete()

    return Response({"message": "Post unliked"})

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission: Only authors can edit or delete their posts/comments
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only for the author
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)