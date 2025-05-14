from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import translate_url
from django.utils import translation
from django.utils.translation import gettext as _, get_language
from django.views.decorators.http import require_POST
import json

# Create your views here.
"""
    context = {
        "page_title": "Yönetim Paneli",
        "breadcrumbs": [{"title": "Yönetim", "url": reverse("admin_dashboard")}],
    }
"""


@require_POST
def set_language(request):
    """
    Kullanıcının dil tercihini değiştirme fonksiyonu
    """
    lang_code = request.POST.get("language", None)
    if lang_code and lang_code in [lang[0] for lang in settings.LANGUAGES]:
        # Burada dil kodunu session'a kaydediyoruz
        request.session[settings.LANGUAGE_SESSION_KEY] = lang_code

    redirect_url = request.POST.get("next", "/")
    # Eğer kullanıcı prefix olmadan bir URL'deyse ve dil değiştirirse
    # Django'nun dil URL desenine uydurmak için başa dil kodu ekleyeceğiz
    current_lang = get_language()
    if current_lang != lang_code:
        # Burada sadece domain ve '/' ile başlayan URL'leri kontrol ediyoruz
        if redirect_url == "/":
            redirect_url = f"/{lang_code}/"
        elif redirect_url.startswith("/") and not redirect_url.startswith(
            f"/{lang_code}/"
        ):
            redirect_url = f"/{lang_code}{redirect_url}"

    return redirect(redirect_url)
