from django.db import models
from django.utils.translation import gettext_lazy as _
from shared.models import BaseModel  # Tüm modellerin kalıtım aldığı yapı
from django.utils.text import slugify


class BlogCategory(BaseModel):
    name = models.CharField(max_length=150, verbose_name=_("Kategori Adı"))
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = _("Blog Kategorisi")
        verbose_name_plural = _("Blog Kategorileri")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
