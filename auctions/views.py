from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def create_auction(request: HttpRequest) -> HttpResponse:
    # if not request.user.is_authenticated:
    #     return redirect(settings.LOGIN_URL)
    return render(request, "auctions/auction_form.html")
