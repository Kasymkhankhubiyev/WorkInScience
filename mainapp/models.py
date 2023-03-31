from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class User(models.Model):
#     first_name = models.CharField(max_length=64)
#     second_name = models.CharField(max_length=64, null=True, blank=True)
#     last_name = models.CharField(max_length=64)
#     email = models.EmailField(unique=True)
#     phone_number = models.TextField(unique=True, null=True, blank=True)
#     nickname = models.CharField(max_length=64, unique=True, null=True, blank=True)
#     birth_date = models.DateField(null=True, blank=True)
#     password = models.CharField(null=False, blank=False, max_length=64)
#     is_active = models.BooleanField(default=False)
#     # is_activated = models.BooleanField(default=False)  # позже добавим для валидации электронного адреса

#     def __str__(self) -> str:
#         if self.second_name:
#             return f'{self.first_name} {self.second_name} {self.last_name}'
#         return f'{self.first_name} {self.last_name}'
    
# class Passwords(models.Model):
#     user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='password')
#     password = models.TextField(null=False, blank=False)

class User(AbstractUser):
    second_name = models.CharField(max_length=64, null=True, blank=True)
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Прошел активацию?')
    send_messages = models.BooleanField(default=True, verbose_name='Присылать оповещения о новых событиях?')

    class Meta(AbstractUser.Meta):
        pass

    def __str__(self) -> str:
        if self.second_name:
            return f'{self.first_name} {self.second_name} {self.last_name}'
        return f'{self.first_name} {self.last_name}'
# class UserData(models.Model):
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)

# class Organization(models.Model):
#     name = models.CharField(max_length=64)
#     bin = models.CharField(max_length=64)
#     email_block = models.CharField(max_length=64)
#     organization_type = models.CharField(max_length=64, blank=False,
#                                          choices=(('None', 'Выберите должность'),
#                                                   ('c', 'Сотрудник Компании'), 
#                                                   ('i', 'Сотрудник Института'), 
#                                                   ('u', 'Сотрудник Университета'), 
#                                                   ('s', 'Студент')))

#     def __str__(self) -> str:
#         return f'Наименование: {self.name} ::: БИН {self.bin} ::: Тип {self.organization_type}'


class AvailableEmailDomens(models.Model):
    domen = models.CharField(max_length=64, null=False, blank=False)

