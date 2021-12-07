from django.db import models

from django.contrib.auth.models import (
                                    AbstractBaseUser, 
                                    BaseUserManager, 
                                    PermissionsMixin)

class Contest(models.Model):
    need_qr = models.PositiveIntegerField(default=0)
    name_contest = models.CharField(max_length=127)
    image = models.URLField(max_length=1028)
    
    def __str__(self):
        return f'{self.name_contest} - {self.need_qr}'


class UserManager(BaseUserManager):
    
    def create_user(self, number, first_name, last_name, password=None):
        if number is None:
            raise TypeError('Users should have a number')
        

        user = self.model(
                        number=number,
                        first_name=first_name,
                        last_name=last_name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, number, first_name, last_name, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(number, first_name, last_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    number = models.CharField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=127)
    last_name = models.CharField(max_length=127)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    qr_quantity = models.PositiveIntegerField(default=0)
    which_contest = models.ForeignKey(Contest, on_delete=models.SET_NULL, null=True)
    qr_in_day = models.PositiveIntegerField(default=0)


    USERNAME_FIELD = 'number'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.number}'

