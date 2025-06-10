from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def signup(request): # `회원가입 처리용 뷰 함수`로, `/accounts/signup/` 주소에서 동작하도록 설정
    if request.method == "POST": #사용자가 회원가입 폼을 제출한 경우 (즉, 데이터를 보내온 경우)
        form = UserCreationForm(request.POST) #`POST`로 전송된 데이터를 바탕으로 폼 생성
        if form.is_valid(): #입력된 데이터가 유효한지 확인 (예: 비밀번호 일치, 필드 누락 없음 등)
            form.save() #새 사용자 계정을 생성하여 데이터베이스에 저장
            return HttpResponseRedirect(reverse("login")) #회원가입 완료 후 `"login"` URL 이름을 가진 페이지로 리디렉션 (즉, 로그인 페이지로 이동)
    else:
        form = UserCreationForm() #`GET` 요청인 경우 (페이지를 처음 열었을 때), 빈 폼을 사용자에게 보여줌
    return render(request, "accounts/signup.html", {"form": form})
