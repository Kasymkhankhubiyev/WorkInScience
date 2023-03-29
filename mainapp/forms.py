from django.forms import ModelForm, EmailField, CharField, PasswordInput, EmailInput
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from .models import User, AvailableEmailDomens

class UserRegForm(ModelForm):
    email = EmailField(required=True, label='Email:')
    password1 = CharField(label='Пароль',widget=PasswordInput, help_text=password_validation.password_validators_help_text_html())
    password2 = CharField(label='Пароль (повторно)', widget=PasswordInput, help_text='Введите тот же самый пароль еще раз для проверки')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_password1(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1
    
    def email_is_available(self):
        email = self.changed_data['email']
        # domens = AvailableEmailDomens.
        """тут нужно проверить, есть ли доступный домен в указанном электронном адресе.
        Если нет - кидаем ошибку,
        Если есть - нет.

        Может нужно запихнуть в функцию clean() ниже????
        """


    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2: 
            errors = {'password2': ValidationError('Введенные пароли не совпадают',
                                                    code='password_mismatch')}
            raise ValidationError(errors)

    def save(self, commit=True):
        # user = super().save(commit=False)
        user = User()
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.password = self.cleaned_data['password1']
        # user.is_active = True  #  False
        # user.is_activated = False
        if commit:
            user.save()
        # user_registered.send(RegisterUserForm, instance=user)
        return user
    

class UserLogInForm(ModelForm):
    email = CharField(label='Электронный адрес', widget=EmailInput)
    password = CharField(label='Пароль', widget=PasswordInput)
    class Meta:
        model = User
        fields = ('email', 'password')

    def check_user(self):
        email = self.cleaned_data['email']
        pswd = self.cleaned_data['password']