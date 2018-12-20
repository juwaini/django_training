from django.shortcuts import render

from django.shortcuts import HttpResponse

from .models import Book


def book_list(request):
    b = Book.objects.all()
    return HttpResponse(b)


def book_details(request):
    ...


def book_update(request, pk):
    ...
