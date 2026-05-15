from django.shortcuts import render, get_object_or_404
from .models import Post, Author


def post_list(request):
    posts = Post.objects.select_related('author').all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def posts_by_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author)
    return render(request, 'blog/author_posts.html', {
        'author': author,
        'posts': posts
    })


