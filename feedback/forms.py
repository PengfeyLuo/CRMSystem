from django.forms import ModelForm
from .models import ServiceInfo, ComplaintInfo


class ServiceModelForm(ModelForm):
    class Meta:
        model = ServiceInfo
        fields = '__all__'
        labels = {
            'order_id': '订单编号',
            'staff_id': '处理人',
            'content': '内容',
            'reply': '回复',
            'submit_date': '提交时间',
            'last_modify_date': '最后修改时间',
            'status': '状态',
        }


class ComplaintModelForm(ModelForm):
    class Meta:
        model = ComplaintInfo
        fields = '__all__'
        labels = {
            'customer_id': '客户编号',
            'title': '标题',
            'type': '种类',
            'content': '内容',
            'reply': '回复',
            'submit_date': '提交时间',
            'last_modify_date': '最后修改时间',
            'status': '状态',
        }