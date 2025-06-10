from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("signup/", views.signup, name="signup"), #signup은 함수 만약 class 하고 싶다면 signup 뒤에 점 직고 클래스명 작성
    # 127.0.0.1:8000/accounts/signup/ 에서 회원가입 페이지 접근 가능 
]