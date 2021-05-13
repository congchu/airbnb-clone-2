from django.contrib import admin
from django.urls import path, includes

admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path(
        "",
        includes(
            "core.urls",
        ),
    ),
    path("admin/", admin.site.urls),
]
