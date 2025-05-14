from django.shortcuts import get_object_or_404
from blog.models import BlogPost, BlogCategory
from django.db.models import Q
from django.utils.timezone import now
from datetime import timedelta
from django.db.models import Count


# Tüm aktif yazılar
def get_active_posts(limit=None):
    qs = BlogPost.objects.filter(is_active=True).order_by("-created_at")
    return qs[:limit] if limit else qs


# Slug ile yazı getir
def get_post_by_slug(slug):
    return get_object_or_404(BlogPost, slug=slug, is_active=True)


# Kategoriye göre filtrele
def get_posts_by_category_slug(category_slug, limit=None):
    qs = BlogPost.objects.filter(category__slug=category_slug, is_active=True).order_by(
        "-created_at"
    )
    return qs[:limit] if limit else qs


# Arama (başlık ve içerikte)
def search_posts(query):
    return BlogPost.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query), is_active=True
    )


# İlgili yazılar (aynı kategoride)
def get_related_posts(post, limit=3):
    return BlogPost.objects.filter(category=post.category, is_active=True).exclude(
        id=post.id
    )[:limit]


# Son 7 günde eklenen yazılar
def get_recent_posts(days=7):
    date_limit = now() - timedelta(days=days)
    return BlogPost.objects.filter(is_active=True, created_at__gte=date_limit).order_by(
        "-created_at"
    )


# Kategori listesi (içinde yazı olanlar)
def get_categories_with_post_count():
    return BlogCategory.objects.annotate(post_count=Count("blogpost")).filter(
        post_count__gt=0
    )
