from django.forms import ModelForm
from .models import CustomerMessage, StaffMessage


class CustomerModelForm(ModelForm):
    class Meta:
        model = CustomerMessage
        fields = '__all__'
        labels = {
            'company': '公司',
            'representative': '公司代表人',
            'postcode': '邮政编码',
            'address': '地址',
            'apartment': '部门',
            'agent': '代理人',
            'telephone': '电话',
            'bank': '银行',
            'taxid': '税号',
        }


class StaffModelForm(ModelForm):
    class Meta:
        model = StaffMessage
        fields = '__all__'
        labels = {
            'age': '年龄',
            'gender': '性别',
            'apartment': '部门',
            'role': '角色',
            'address': '地址',
            'rate': '评分',
        }
