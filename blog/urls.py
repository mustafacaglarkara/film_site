from django.urls import path
from blog.views import latest_blog_posts, blog_detail_view

app_name = "blog"

urlpatterns = [
    path("", latest_blog_posts, name="index"),
    path("<slug:slug>/", blog_detail_view, name="detail"),
]
