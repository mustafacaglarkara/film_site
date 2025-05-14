from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import translate_url
from django.utils import translation
from django.utils.translation import gettext as _, get_language
from django.views.decorators.http import require_POST
import json


def admin_dashboard(request):
    context = {
        "page_title": "Yönetim Paneli",
        "breadcrumbs": [
            {"title": "Yönetim", "url": reverse("admin_panel:admin_dashboard")}
        ],
    }
    return render(request, "admin_panel/dashboard.html", context)
