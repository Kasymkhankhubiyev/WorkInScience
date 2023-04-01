from django.db import models
from django.contrib.auth.models import AbstractUser

"""
#TODO 
1. нужно добавить модель "Направления" - связь многие-со-многими
"""

# Create your models here.
class User(AbstractUser):
    second_name = models.CharField(max_length=64, null=True, blank=True)
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Прошел активацию?')
    send_messages = models.BooleanField(default=True, verbose_name='Присылать оповещения о новых событиях?')
    position = models.CharField(max_length=64, blank=64, default='Студент',
                                choices=(('m', 'Менеджер'),
                                         ('s', 'Студент')))

    class Meta(AbstractUser.Meta):
        pass

    def __str__(self) -> str:
        if self.second_name:
            return f'{self.first_name} {self.second_name} {self.last_name}'
        return f'{self.first_name} {self.last_name}'
    
class UserAdditionalData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(null=True, blank=True, default=0, verbose_name='score')
    gpa = models.FloatField(null=True, blank=True, default=0.0, verbose_name='gpa')
    about = models.TextField(blank=True)
    score_is_visible = models.BooleanField(null=False, default=True)
    gpa_is_visible = models.BooleanField(null=False, default=True)

class Organization(models.Model):
    name = models.CharField(max_length=64)
    bin = models.CharField(max_length=64)
    email_block = models.CharField(max_length=64)
    organization_type = models.CharField(max_length=64, blank=False,
                                         choices=(('None', 'Выберите тип организации'),
                                                  ('c', 'Компания'), 
                                                  ('i', 'Институт'), 
                                                  ('u', 'Университет')))
    staff = models.ManyToManyField(User)

    def __str__(self) -> str:
        return f'Наименование: {self.name} ::: БИН {self.bin} ::: Тип {self.organization_type}'


class AvailableEmailDomens(models.Model):
    domen = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return f'@{self.domen}'

