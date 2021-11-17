from celery import shared_task
from accounts.models import User
import random, string


@shared_task
def annul_day_qr():
    for user in User.objects.all():
        user.qr_in_day = 0
        user.save()
    # name = ''.join([random.choice(string.ascii_letters) for _ in range(10)])
    # password = ''.join([random.choice(string.ascii_letters) for _ in range(10)])
    # User.objects.create_user(username=name, password=password)