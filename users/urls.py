from django.urls import include, path
from . import views

app_name = "users"

urlpatterns = [
    path("accounts/", include("django_registration.backends.one_step.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]
