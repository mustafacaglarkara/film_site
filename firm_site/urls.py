from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.views.i18n import set_language  # Django'nun resmi view'ini kullan

# Bu URL'ler hiçbir zaman i18n'e tabi olmaz (her dil için aynıdır)
urlpatterns = [
    # Django'nun standart dil değiştirme URL'si
    path("set_language/", set_language, name="set_language"),
    # Eski dil değiştirme URL'si - geriye uyumluluk için
    path("i18n/setlang/", set_language, name="legacy_set_language"),
]

# Bu URL'ler dil öneki alabilir (i18n)
urlpatterns += i18n_patterns(
    # Hem trailing slash'lı hem de slash'sız hali için pattern ekliyoruz
    path("panel/", include("admin_panel.urls", namespace="admin_panel")),
    path("blog/", include("blog.urls", namespace="blog")),
    path("admin/", admin.site.urls),  # Django admin panelini yeniden adlandır
    # Anasayfa görünümü için geçici bir örnek
    path("", TemplateView.as_view(template_name="index.html"), name="home"),
    # Bu ayar önemli: URL'lerde /en/ veya /tr/ öneki olmadan direkt içeriğe erişilebilir
    # Ancak dil değiştirildiğinde URL'ler önekli olarak değişir (/en/ veya /tr/)
    prefix_default_language=True,  # Varsayılan dil için de prefix kullan
)

# Debug Toolbar URL'leri
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]

# Statik dosyalar için URL ekle
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
