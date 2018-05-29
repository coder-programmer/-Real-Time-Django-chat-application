from django.conf.urls import path
from django.contrib.auth import views as auth_views
from accounts import views


urlpatterns = [
    path('logout/', auth_views.logout),
    path('login/', views.Login.as_view()),
    path('register/', views.Register.as_view()),
]