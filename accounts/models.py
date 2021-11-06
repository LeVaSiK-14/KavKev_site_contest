from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class ContestUser(models.TextChoices):
        LESS_5 = 'LESS_5'
        MORE_5_LESS_10 = 'MORE_5_LESS_10'
        MORE_10_LESS_100 = 'MORE_10_LESS_100'
        MORE_100 = 'MORE_100'

    qr_quantity = models.PositiveIntegerField(default=0)
    which_contest = models.CharField(max_length=50, choices=ContestUser.choices, default=ContestUser.LESS_5)
