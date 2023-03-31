from django.forms import ModelForm, EmailField, CharField, PasswordInput, EmailInput
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from .models import User, AvailableEmailDomens

from .exceptions import NotAvailableDomen, EmailIsBusy

class UserRegForm(ModelForm):
    first_name = CharField(label='Имя', required=True, max_length=64)
    last_name = CharField(label='Фамилия', required=True, max_length=64)
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
        email = self.cleaned_data['email']
        input_domen = email.split('@')[1]
        try:
            AvailableEmailDomens.objects.get(domen=input_domen)
            user = User.objects.get(email=email)
            if user:
                raise EmailIsBusy(email=email)
        except AvailableEmailDomens.DoesNotExist:
            raise NotAvailableDomen(input_domen)
        except User.DoesNotExist:
            pass

    def clean(self) -> None:
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2: 
            errors = {'password2': ValidationError('Введенные пароли не совпадают',
                                                    code='password_mismatch')}
            raise ValidationError(errors)
        try:
            self.email_is_available()
        except NotAvailableDomen as e:
            raise ValidationError({'email': ValidationError(e.args)})
        except EmailIsBusy as e:
            raise ValidationError({'email': ValidationError(e.args)})

    def save(self, commit=True) -> User:
        user = super().save(commit=False)
        # user = User()
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        # user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        user.username = self.cleaned_data['email'].split('@')[0]
        if commit:
            user.save()
        return user
    

class UserLogInForm(ModelForm):
    email = EmailField(label='Электронный адрес', required=True)
    password = CharField(label='Пароль', widget=PasswordInput, required=True)

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean(self):
        """Здесь проверяем ввод данных.
        Если нет совпадающего email - вызываем исключение
        Если пользователь с ввденным email существует, проверяем пароль.
        Если хэшированный пароль не овпадает - бросаем исключение.
        """
        super().clean()
        password = self.cleaned_data['password']
        email = self.cleaned_data['email']
        try:
            user = User.objects.get(email=email)
            if user.password != password:
                raise ValidationError({'email': ValidationError('Неверный логин или пароль')})
        except User.DoesNotExist as e:
            raise ValidationError({'email': ValidationError('Неверный логин или пароль')})
        
    def get_user(self) -> User:
        return  User.objects.get(email=self.cleaned_data['email'])
