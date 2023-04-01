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

from .models import *

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
def search_for_academic_advisor(request: HttpRequest) -> HttpResponse:
    return render(request, 'wis/searchForAcademicAdvisor.html')

@login_required
def profile(request: HttpRequest, username: str) -> HttpResponse:
    user = User.objects.get(username=username)
    user_info = UserAdditionalData.objects.get(user=user.pk)
    context = {'user_info': user_info}
    return render(request, 'wis/profile.html', context)

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
                                                                           'last_name': user.last_name,
                                                                           'login': user.username,})
        else:
            context = {'form': user_form, 'heading': 'Регистрация'}
            return render(request, 'mainapp/register.html', context)
    else:
        user_form = UserRegForm()
        context = {'form': user_form, 'heading': 'Регистрация'}
        return render(request, 'mainapp/register.html', context)
