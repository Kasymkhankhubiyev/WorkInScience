from django.urls import path, include

from . import views
# from .views import 

app_name = 'mainapp'
urlpatterns = [
    path("", views.mainpage, name='mainpage'),
    path('accounts/login/', views.WiSLoginView.as_view(), name='login'),
    path('accounts/logout/', views.WiSLogoutView.as_view(), name='logout'),
    path('accounts/profile/<str:username>', views.profile, name='profile'),
    path('accounts/settings/<str:username>', views.profile_settings, name='profile_settings'),
    path('<str:page>/', views.other_page, name='other'),
    # path("register/", views.register, name="register"),
    path("accounts/register/", views.register, name="register"),
    # path("", views.register, name="register"),
]