from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Comment, Post
from .forms import CommentForm
@login_required
def profile_view(request):
    if request.method == "POST":
        request.user.email = request.POST.get("email")
        request.user.save()
        return redirect("profile")
    return render(request, "blog/profile.html")


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("post-detail", pk=post.pk)
        

@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if comment.author != request.user:
        return redirect("post-detail", pk=comment.post.pk)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect("post-detail", pk=comment.post.pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, "blog/comment_form.html", {"form": form})

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if comment.author != request.user:
        return redirect("post-detail", pk=comment.post.pk)

    if request.method == "POST":
        comment.delete()
        return redirect("post-detail", pk=comment.post.pk)

    return render(request, "blog/comment_confirm_delete.html", {"comment": comment})

def home(request):
    return render(request, "blog/base.html")

def login_view(request):
    return render(request, "blog/login.html")

def register_view(request):
    return render(request, "blog/register.html")

def profile_view(request):
    return render(request, "blog/profile.html")
# View all posts
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]


# View single post
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"


# Create new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Update post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


# Delete post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author