from django.urls import path, include

from . import views

app_name = 'mainapp'
urlpatterns = [
    path("", views.mainpage, name='mainpage'),
]