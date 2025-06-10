from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),  # polls 앱의 URL 연결 (polls.py로 이동) 
    path("admin/", admin.site.urls),  # 127.0.0.1:8000/admin/ 에서 관리자 페이지 접근 가능
    path("accounts/", include("accounts.urls")),  # accounts 앱의 URL 연결 (accounts.py로 이동)
    path("accounts/", include("django.contrib.auth.urls")),  # Django의 기본 인증 URL 연결, # 127.0.0.1:8000/accounts/로 접근 
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
