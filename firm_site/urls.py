from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView
from shared.views import set_language
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    # Özel dil değişim view fonksiyonumuzu kullanacağız
    path("i18n/setlang/", set_language, name="set_language"),
]


urlpatterns += i18n_patterns(
    # path("test/", index, name="test"),
    # Hem trailing slash'lı hem de slash'sız hali için pattern ekliyoruz
    path("panel/", include("admin_panel.urls", namespace="admin_panel")),
    # re_path(r"^ajans$", lambda request: redirect("admin_dashboard")),
    path("admin/", admin.site.urls),  # Django admin panelini yeniden adlandır
    # Anasayfa görünümü için geçici bir örnek
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    prefix_default_language=False,  # Varsayılan dil için prefix kullanma
)
# Statik dosyalar için URL ekle
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
