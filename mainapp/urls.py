from django.urls import path, include

from . import views
# from .views import 

app_name = 'mainapp'
urlpatterns = [
    path("", views.mainpage, name='mainpage'),
    path('academicadvisors/', views.search_academic_advisor, name='academic_advisor'),
    path('<str:page>/', views.other_page, name='other'),
    # path('accounts/login/', views.WiSLoginView.as_view(), name='login'),
    path('accounts/login/', views.WisLoginView, name='login'),
    path('accounts/logout/', views.WiSLogoutView.as_view(), name='logout'),
    path('accounts/profile/<str:username>', views.profile, name='profile'),
    path('accounts/settings/<str:username>', views.profile_settings, name='profile_settings'),
    path("accounts/register/", views.register, name="register"),
]