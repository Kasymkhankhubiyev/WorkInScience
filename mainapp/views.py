from django.shortcuts import render

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView

from .forms import UserRegForm, UserLogInForm

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
    if request.method == 'POST':
        user_form = UserLogInForm(request.POST)
        if user_form.is_valid():
            pass
        else:
            context = {'form': user_form, 'heading': 'Вход'}
            return render(request, 'mainapp/login.html', context)
    else:
        user_form = UserLogInForm()
        context = {'form': user_form, 'heading': 'Вход'}
        return render(request, 'mainapp/login.html', context)


def register(request: HttpRequest) -> HttpResponse:
    """Этот контроллер создает форму для регистрации нового участника
    шаблон: 'mainapp/register.html'
    Так же обрабатывает входные данные формы.
    """
    # проверяем, это запрос на создание формы или запрос с входными данными
    if request.method == 'POST':
        user_form = UserRegForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return render(request, 'mainapp/registretion_proceeded.html')
        else:
            context = {'form': user_form, 'heading': 'Регистрация'}
            return render(request, 'mainapp/register.html', context)
    else:
        user_form = UserRegForm()
        context = {'form': user_form, 'heading': 'Регистрация'}
        return render(request, 'mainapp/register.html', context)


class UserCreateView(CreateView):
    template_name = 'mainapp/register.html'
    form_class = UserRegForm
    success_url = reverse_lazy('mainpage') #  '/mainapp/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
