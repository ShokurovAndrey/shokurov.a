from django.shortcuts import render
# класс создаёт ответ на запрос
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('Lol Wow')
