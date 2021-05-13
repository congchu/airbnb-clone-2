from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("admin/", admin.site.urls),
]
