from django.conf import settings
from django.contrib import admin
from django.urls import path, include
import debug_toolbar


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("", include("users.urls")),
    path("auctions/", include("auctions.urls")),
]

if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include(debug_toolbar.urls)))
