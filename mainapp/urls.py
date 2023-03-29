from django.urls import path, include

from . import views

# app_name = 'mainapp'
urlpatterns = [
    path("", views.mainpage, name='mainpage'),
    path("company/", views.company, name='company'),
    path("institute/", views.institute, name='institute'),
    path("news/", views.news, name='news'),
    path("student/", views.student, name='student'),
    path("login/", views.login, name="login"),
    # path("register/", views.register, name="register"),
    path("register/", views.UserCreateView.as_view(), name="register"),
]