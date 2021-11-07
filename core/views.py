from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "core/index.html")


def contact(request: HttpRequest) -> HttpResponse:
    return render(request, "core/contact.html")


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "core/about.html")


def auctions(request: HttpRequest) -> HttpResponse:
    return render(request, "core/auctions.html")
