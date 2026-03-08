from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

@login_required
def profile_view(request):
    if request.method == "POST":
        request.user.email = request.POST.get("email")
        request.user.save()
        return redirect("profile")
    return render(request, "blog/profile.html")

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