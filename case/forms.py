from django.forms import ModelForm
from .models import ItemInfo, OrderInfo


class ItemModelForm(ModelForm):
    class Meta:
        model = ItemInfo
        fields = '__all__'
        labels = {
            'name': '商品名称',
            'num': '商品编号',
            'model': '商品型号',
            'price': '商品价格',
            'production_date': '生产日期',
            'left_amount': '剩余数量',
            'rate': '评分',
        }


class OrderModelForm(ModelForm):
    class Meta:
        model = OrderInfo
        fields = '__all__'
        labels = {
            'item_id': '商品名',
            'customer_id': '客户名',
            'staff_id': '经办人',
            'amount': '数量',
            'date': '日期',
        }