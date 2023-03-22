from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

# Create your views here.
def mainpage(request: HttpRequest) -> HttpResponse:
    return render(request, 'mainapp/mainpage.html')
