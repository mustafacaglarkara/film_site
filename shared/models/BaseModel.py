from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Oluşturulma"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Güncellenme"))
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name=_("Silinme"))

    class Meta:
        abstract = True  # Bu modelden tablo oluşturulmaz
