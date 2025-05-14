from django.urls import path
from admin_panel.views import admin_dashboard

app_name = "admin_panel"
urlpatterns = [
    path("", admin_dashboard, name="admin_dashboard"),
]
