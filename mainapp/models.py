from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64, unique=True)
    phone_number = models.TextField(unique=True, null=True, blank=True)
    nickname = models.CharField(max_length=64, unique=True, null=True, blank=True)
    birth_date = models.DateField(null=True)

    def __str__(self) -> str:
        if self.second_name:
            return f'{self.first_name} {self.second_name} {self.last_name}'
        return f'{self.first_name} {self.last_name}'
    
class UserData(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Organization(models.Model):
    name = models.CharField(max_length=64)
    bin = models.CharField(max_length=64)
    email_block = models.CharField(max_length=64)
    organization_type = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f'Наименование: {self.name} ::: БИН {self.bin} ::: Тип {self.organization_type}'

# class OrganizationStuff(models.Model):
#     pass

class Passwords(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.TextField()
