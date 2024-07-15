from django.urls import path

from . import views

urlpatterns = [
    path("", views.start_login, name="start_login"),
    path("login_user/", views.login_user, name="login_user"),
    path("logout_user/", views.logout_user, name="logout_user"),
    path("start_signup/", views.start_signup, name="start_singup"),
    path("signup_user/", views.signup_user, name="signup_user"),
]
