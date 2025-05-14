from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponseRedirect, JsonResponse
from django.utils import translation
from django.utils.translation import gettext as _
import logging
import json

# Create your views here.
"""
    context = {
        "page_title": "Yönetim Paneli",
        "breadcrumbs": [{"title": "Yönetim", "url": reverse("admin_dashboard")}],
    }
"""

# Debug için logger oluştur
logger = logging.getLogger(__name__)

# Özel view fonksiyonlarınızı buraya ekleyebilirsiniz
# Django'nun standart dil değiştirme view'ini (django.views.i18n.set_language) kullandığımız için
# artık burada kendi set_language fonksiyonumuza ihtiyacımız yok
