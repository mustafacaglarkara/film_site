from django.shortcuts import render
from blog.services import get_active_posts, get_post_by_slug
from django.shortcuts import render, get_object_or_404
from django.http import Http404


def latest_blog_posts(request):
    latest_posts = get_active_posts(limit=3)
    return render(request, "frontend/blog/index.html", {"latest_posts": latest_posts})


def blog_detail_view(request, slug):
    blog = get_post_by_slug(slug)
    if not blog:
        raise Http404("Yazı bulunamadı.")
    return render(request, "blog/detail.html", {"blog": blog})
