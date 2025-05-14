from django.db import models
from django.utils.translation import gettext_lazy as _
from shared.models import BaseModel  # Tüm modellerin kalıtım aldığı yapı


class BlogCategory(BaseModel):
    name = models.CharField(max_length=150, verbose_name=_("Kategori Adı"))

    class Meta:
        verbose_name = _("Blog Kategorisi")
        verbose_name_plural = _("Blog Kategorileri")

    def __str__(self):
        return self.name
