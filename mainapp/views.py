from django.shortcuts import render

from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView

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

def check_pswds(pswd1, pswd2):
        """Проверяем, совпадают ли два введенных пароля
        """
        if pswd1 == pswd2:
            return True
        return False

def register(request: HttpRequest) -> HttpResponse:
    """Этот контроллер создает форму для регистрации нового участника
    шаблон: 'mainapp/register.html'
    Так же обрабатывает входные данные формы.
    """
    # проверяем, это запрос на создание формы или запрос с входными данными
    if request.method == 'POST':
        form = request.POST
        print(f'form data: {form}')
        if check_pswds(form['pswd1'], form['pswd2']):
            pass
        else:
            first_name = form['first_name']
            last_name = form['last_name']
            email = form['email']
            organization = form['organization']
        # print(f'first name: {first_name}')
            return render(request, 'mainapp/register.html', {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'organization': organization
            })
    return render(request, 'mainapp/register.html', {
        'first_name': '',
        'last_name': '',
        'email': '',
        'organization': ''
    })


# class CreateUser(CreateView):
#     template_name = 'mainapp/register.html'
#     success_url = '/mainapp/'
