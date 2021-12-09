from django.db import models
from accounts.models import User


class Token(models.Model):
    token = models.CharField(max_length=127, default='')
    isActive = models.BooleanField(default=True)
    slug = models.SlugField(max_length=127, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.token