from django.shortcuts import render

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView

from .forms import UserRegForm, UserLogInForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.template import TemplateDoesNotExist

# Create your views here.
def mainpage(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return render(request, 'wis/feed.html')
    return render(request, 'mainapp/mainpage.html')

def other_page(request: HttpRequest, page: str) -> HttpResponse:
    try:
        template = get_template('mainapp/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))

@login_required
def profile(request: HttpRequest) -> HttpResponse:
    return render(request, 'wis/profile.html')

# def login(request: HttpRequest) -> HttpResponse:
#     """Это контроллер входа в учетную запись.
#     """
#     if request.method == 'POST':
#         user_form = UserLogInForm(request.POST)
#         if user_form.is_valid():
#             user = user_form.get_user()
#             context = {'first_name': user.first_name,
#                        'last_name': user.last_name}
#             return render(request, 'wis/account.html', context)  # как перенаправить?
#         else:
#             context = {'form': user_form, 'heading': 'Вход'}
#             return render(request, 'mainapp/login.html', context)
#     else:
#         user_form = UserLogInForm()
#         context = {'form': user_form, 'heading': 'Вход'}
#         return render(request, 'mainapp/login.html', context)

class WiSLoginView(LoginView):
    template_name = 'mainapp/login.html'

class WiSLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'mainapp/logout.html'


def register(request: HttpRequest) -> HttpResponse:
    """Этот контроллер создает форму для регистрации нового участника
    шаблон: 'mainapp/register.html'
    Так же обрабатывает входные данные формы.
    """
    # проверяем, это запрос на создание формы или запрос с входными данными
    if request.method == 'POST':
        user_form = UserRegForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            return render(request, 'mainapp/registretion_proceeded.html', {'first_name': user.first_name,
                                                                           'last_name': user.last_name,})
        else:
            context = {'form': user_form, 'heading': 'Регистрация'}
            return render(request, 'mainapp/register.html', context)
    else:
        user_form = UserRegForm()
        context = {'form': user_form, 'heading': 'Регистрация'}
        return render(request, 'mainapp/register.html', context)
