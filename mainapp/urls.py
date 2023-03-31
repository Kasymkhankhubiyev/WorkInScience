from django.urls import path, include

from . import views
# from .views import 

# app_name = 'mainapp'
urlpatterns = [
    path("", views.mainpage, name='mainpage'),
    path("company/", views.company, name='company'),
    path("institute/", views.institute, name='institute'),
    path("news/", views.news, name='news'),
    path("student/", views.student, name='student'),
    # path("login/", views.login, name="login"),
    path('accounts/login/', views.WiSLoginView.as_view(), name='login'),
    path('accounts/logout/', views.WiSLogoutView.as_view(), name='logout'),
    path('accounts/profile/', views.profile, name='profile'),
    path("register/", views.register, name="register"),
    # path("register/", views.UserCreateView.as_view(), name="register"),
]