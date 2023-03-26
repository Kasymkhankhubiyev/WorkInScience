from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

# Create your views here.
def mainpage(request: HttpRequest) -> HttpResponse:
    return render(request, 'mainapp/mainpage.html')

def news(request: HttpRequest) -> HttpResponse:
    return render(request, 'mainapp/news.html')

def company(request: HttpRequest) -> HttpResponse:
    return render(request, 'mainapp/company.html')

def institute(request: HttpRequest) -> HttpResponse:
    return render(request, 'mainapp/institute.html')

def student(request: HttpRequest) -> HttpResponse:
    return render(request, 'mainapp/student.html')

def login(request: HttpRequest) -> HttpResponse:
    return render(request, 'mainapp/login.html')

def register(request: HttpRequest) -> HttpResponse:
    return render(request, 'mainapp/register.html')