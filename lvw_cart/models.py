from django.db import models
from lvw_user.models import User
from lvw_goods.models import GoodInfo

# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey('lvw_user.User',None)
    goods=models.ForeignKey('lvw_goods.GoodInfo',None)
    count=models.IntegerField(default=0)