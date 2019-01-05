from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

app_name = 'user_auth'

urlpatterns = [
    # リダイレクト
    path('top/', views.top_page, name="top"),
    # ログイン
    path('login/', auth_views.LoginView.as_view(template_name='user_auth/login.html'), name='login'),
    # ログアウト
    path('logout/', auth_views.LogoutView.as_view(template_name='user_auth/logout.html'), name='logout'),
]