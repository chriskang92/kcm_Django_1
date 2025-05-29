from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   return HttpResponse("<h1>B 페이지입니다.</h1>")