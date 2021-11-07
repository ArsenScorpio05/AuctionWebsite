from django.urls import path
from . import views


app_name = "auctions"

urlpatterns = [
    path("create/", views.create_auction, name="auction_create"),
]
