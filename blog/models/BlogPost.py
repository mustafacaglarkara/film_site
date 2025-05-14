from django.db import models
from django.utils.translation import gettext_lazy as _
from shared.models import BaseModel  # Tüm modellerin kalıtım aldığı yapı
from .BlogCategory import BlogCategory


class BlogPost(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_("Başlık"))
    slug = models.SlugField(unique=True)
    content = models.TextField(verbose_name=_("İçerik"))
    category = models.ForeignKey(
        BlogCategory, on_delete=models.SET_NULL, null=True, verbose_name=_("Kategori")
    )
    image = models.ImageField(
        upload_to="blog/", null=True, blank=True, verbose_name=_("Görsel")
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Yayında mı?"))

    class Meta:
        verbose_name = _("Blog Yazısı")
        verbose_name_plural = _("Blog Yazıları")

    def __str__(self):
        return self.title
