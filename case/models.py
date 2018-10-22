from django.db import models
from django.utils import timezone
from rbac.models import UserInfo
# Create your models here.


class ItemInfo(models.Model):
    """
    商品
    """
    name = models.CharField(max_length=64, blank=False, null=False)
    num = models.CharField(max_length=32, blank=False, null=False)
    model = models.CharField(max_length=32, blank=False, null=False)
    price = models.FloatField(blank=True, null=True, default=0)
    production_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    left_amount = models.IntegerField(blank=True, null=True, default=0)
    rate = models.FloatField(blank=False, null=False, default=10.0)

    def __str__(self):
        return str(self.name) + " " + str(self.model)


class OrderInfo(models.Model):
    """
    订单
    """
    item_id = models.ForeignKey(ItemInfo, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='customer_id')
    staff_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='staff_id')
    amount = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=False, null=False, default=timezone.now)
    is_rated = models.BooleanField(default=False)

    def __str__(self):

        return str(self.id) + " " + str(self.customer_id) + " " + str(self.item_id)

