from django.db import models


from django.contrib.auth.models import (
                                    AbstractUser, 
                                    )

class Contest(models.Model):
    need_qr = models.PositiveIntegerField(default=0)
    name_contest = models.CharField(max_length=127)
    image = models.URLField(max_length=1028, default='')
    
    def __str__(self):
        return f'{self.name_contest} - {self.need_qr}'



class User(AbstractUser):

    qr_quantity = models.PositiveIntegerField(default=0)
    which_contest = models.ForeignKey(Contest, on_delete=models.SET_NULL, null=True)
    qr_in_day = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.number}'


# {
# "username" : "0700503339",
# "first_name": "Lev",
# "last_name": "Boiko",
# "password": "qwerty12345"
# }


# "id": 1,
#     "category": 1,
#     "name_product": "чечел",
#     "amount": 300,
#     "composition": "что то",
#     "price": 200,
#     "inStock": true,
#     "articul": "hgdfuygsdhufhsdiuhfuds",
#     "raiting_general": "0.0"