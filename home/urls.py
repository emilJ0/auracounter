from django.urls import path

from . import views

app_name = "home"
urlpatterns = [
    path("", views.index, name="index"),
    path("start_create_group/", views.start_create_group, name="start_create_group"),
    path("create_group/", views.create_group, name="create_group"),
    path("start_join_group/", views.start_join_group, name="join_group"),
    path("join_group/", views.join_group, name="join_group"),
    path("manage_aura/", views.manage_aura, name="manage_aura"),
    path("leave_group/", views.leave_group, name="leave_group"),
]
