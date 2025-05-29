from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    html = """
    <html>
    <head>
        <title>🎬 영화 추천</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 2em; }
            .movie { border: 1px solid #ccc; padding: 1em; margin-bottom: 1em; border-radius: 10px; }
            .title { font-size: 1.5em; font-weight: bold; }
            .genre { color: gray; }
            .description { margin-top: 0.5em; }
            .btn { margin-top: 1em; display: inline-block; padding: 0.5em 1em; background: #007bff; color: white; text-decoration: none; border-radius: 5px; }
        </style>
    </head>
    <body> 
    <h1> 🎬 오늘의 영화 추천 </h>
    <div class= "movie">
        <div class="title">인터스텔라</div>
        <div Class="genre">장르 : SF, 드라마</div>
        <div Calss="descriptioo"> 우주를 배경으로 한 아버지의 위대한 사랑과 모험 이야기</div>
        <a href="#" class="btn">추천하기</a> 
    </div>    
        
    <div class= "movie">
        <div class="title">기생충</div>
        <div Class="genre">장르 : 드라마, 스릴러</div>
        <div Calss="descriptioo"> 상류층과 하류층의 현실을 꼬집는 블랙코미디 영화</div>
        <a href="#" class="btn">추천하기</a>
    </div>   

    <div class= "movie">
        <div class="title">토이스토리</div>
        <div Class="genre">장르 : 애니메이션, 가족</div>
        <div Calss="descriptioo"> 장난감들의 유쾌한 우정과 모험 이야기.</div>
        <a href="#" class="btn">추천하기</a>
    </div>   
    </body>

    </html>
    """
    return HttpResponse(html)
