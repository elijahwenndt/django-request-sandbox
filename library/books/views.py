from django.shortcuts import render
from django.http import HttpResponse
from pprint import pprint
# Create your views here.
def get_books(request):
    return HttpResponse("this be books")