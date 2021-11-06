from django.shortcuts import render 
from django.http import HttpRequest, HttpResponse


def bidnow(request: HttpRequest) -> HttpResponse:
    return render(request, 'biders/bidnow.html')    
