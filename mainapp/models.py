from django.db import models


class Token(models.Model):
    token = models.CharField(max_length=127, default='')
    isActive = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.token