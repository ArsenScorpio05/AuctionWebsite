from django.urls import path
from . import views

app_name = 'biders'


urlpatterns = [
    path ('', views.index, name="index"),
    path ('bidnow/', views.bidnow, name="bidnow"),
    
]
