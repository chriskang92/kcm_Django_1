from django.urls import path
from . import views

app_name = "polls"  # 이 앱의 URL 네임스페이스를 설정합니다. 다른 앱과 URL이 겹치지 않도록 합니다.

urlpatterns = [
    path("", views.index, name="index"), # mysite 에서 polls 앱의 index 뷰를 호출 했기 때문에  http://127.0.0.1:8000/polls/ 로 접근하면 index 뷰가 호출됨
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]