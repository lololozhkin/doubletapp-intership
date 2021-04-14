from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def api_func(request: HttpRequest):
    return HttpResponse("hello world")
