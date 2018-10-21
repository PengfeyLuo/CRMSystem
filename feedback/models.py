from django.db import models
from case.models import OrderInfo
from rbac.models import UserInfo
from django.utils import timezone
# Create your models here.


class ServiceInfo(models.Model):
    STATUS_CHOICES = (
        ('submitted', '已提交'),
        ('processing', '处理中'),
        ('finished', '已完成'),
    )
    order_id = models.ForeignKey(OrderInfo, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    content = models.TextField(null=False, blank=False)
    reply = models.TextField(null=True, blank=True, default='')
    submit_date = models.DateTimeField(default=timezone.now)
    last_modify_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=32, null=False, blank=False, choices=STATUS_CHOICES, default='submitted')

    def __str__(self):
        return str(self.order_id) + " " + str(self.status)


class ComplaintInfo(models.Model):
    TYPE_CHOICES = (
        ('item', '产品问题'),
        ('service', '服务问题'),
        ('advice', '意见建议'),
        ('other', '其他问题'),
    )
    STATUS_CHOICES = (
        ('submitted', '已提交'),
        ('processing', '处理中'),
        ('finished', '已完成'),
    )
    customer_id = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    title = models.CharField(max_length=32, null=False, blank=False)
    type = models.CharField(max_length=32, null=False, blank=False, choices=TYPE_CHOICES, default='')
    content = models.TextField(null=False, blank=False)
    reply = models.TextField(null=True, blank=True, default='')
    submit_date = models.DateTimeField(default=timezone.now)
    last_modify_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=32, null=False, blank=False, choices=STATUS_CHOICES, default='submitted')

    def __str__(self):
        return str(self.customer_id) + " " + str(self.title) + " " + self.get_status_display()

