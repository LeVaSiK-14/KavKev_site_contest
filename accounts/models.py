from django.db import models
from django.contrib.auth.models import AbstractUser

class Contest(models.Model):
    need_qr = models.PositiveIntegerField(default=0)
    name_contest = models.CharField(max_length=127)\
    
    def __str__(self):
        return f'{self.name_contest} - {self.need_qr}'


class User(AbstractUser):


    qr_quantity = models.PositiveIntegerField(default=0)
    which_contest = models.ForeignKey(Contest, on_delete=models.SET_NULL, null=True)
    qr_in_day = models.PositiveIntegerField(default=0)
