from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), # mysite 에서 polls 앱의 index 뷰를 호출 했기 때문에  http://127.0.0.1:8000/polls/ 로 접근하면 index 뷰가 호출됨
]