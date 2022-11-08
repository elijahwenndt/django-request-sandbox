from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from pprint import pprint
from .models import Book
# Create your views here.
def get_books(request):
    books = list(Book.objects.values())

    return JsonResponse({'data': books})

def books_by_year(request, year):
    books = list(Book.objects.filter(published_year=year).values())
    if (len(books)>0):
        return JsonResponse({'data': books})
    else:
        return HttpResponse('none matching')
def books_by_title(request, letter):
    books = list(Book.objects.values())

    return JsonResponse({'data': books})