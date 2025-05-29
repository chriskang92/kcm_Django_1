from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    html = """
    <html>
    <head>
        <title>메인 페이지입니다.</title>
    </head>
    <body>
        <h1><a href="/main">메인페이지입니다</a></h1>
        <h1><a href="/a">A페이지입니다</a></h1>
        <h1><a href="/b">B페이지입니다</a></h1>
        <h1><a href="/c">C페이지입니다</a></h1>
        <h1><a href="/introduce">소개 페이지입니다</a></h1>
    </body>
    </html>
    """
    return HttpResponse(html)