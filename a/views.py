from django.shortcuts import render
from django.http import HttpResponse

def index(request):
   return HttpResponse("<h1>A 페이지입니다.</h1>")