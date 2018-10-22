from django.shortcuts import render, redirect, HttpResponse
from .models import ItemInfo, OrderInfo
from rbac.models import UserInfo
from user.models import StaffInfo
from .forms import ItemModelForm, OrderModelForm
from CRMSystem.settings import USER_TYPE, USER_ID
# Create your views here.


def item_list(request):

    item_list = ItemInfo.objects.all()
    return render(request, "item_list.html", {"item_list": item_list, "user_type": request.session[USER_TYPE]})


def order_list(request):
    if request.session[USER_TYPE] == 1:
        order_list = OrderInfo.objects.filter(customer_id=request.session[USER_ID])
        return render(request, "order_list.html", {"order_list": order_list, "user_type": request.session[USER_TYPE]})
    else:
        order_list = OrderInfo.objects.all()
        return render(request, "order_list.html", {"order_list": order_list, "user_type": request.session[USER_TYPE]})


def add_item(request):
    if request.method == 'GET':
        item_form = ItemModelForm()
        return render(request, "add_item.html", {"item_form": item_form})
    else:
        item_form = ItemModelForm(request.POST)
        if item_form.is_valid():
            datas = item_form.cleaned_data
            item_form.save()
            return redirect(item_list)
        else:
            return HttpResponse("错误")


def add_order(request):
    if request.method == 'GET':
        order_form = OrderModelForm()
        return render(request, "add_order.html", {"order_form": order_form, "error_message": ""})
    else:
        order_form = OrderModelForm(request.POST)
        if order_form.is_valid():
            data = order_form.cleaned_data
            staff = UserInfo.objects.filter(id=data['staff_id'].id).first()
            customer = UserInfo.objects.filter(id=data['customer_id'].id).first()
            staff_legal = False if staff.is_customer is True else True
            customer_legal = False if customer.is_customer is False else True
            error_message = ""
            if not staff_legal:
                error_message += "所选经办人不为管理人员！"
            if not customer_legal:
                error_message += " 所选客户不为客户！"
            if (not staff_legal) or (not customer_legal):
                return render(request, "add_order.html", {"order_form": order_form, "error_message": error_message})
            else:
                order_form.save()
                return redirect(order_list)
        else:
            return HttpResponse("错误")


def edit_order(request, id):
    order_obj = OrderInfo.objects.filter(id=id).first()
    if request.method == 'GET':
        order_form = OrderModelForm(instance=order_obj)
        return render(request, "add_order.html", {"order_form": order_form, "error_message": ""})
    else:
        order_form = OrderModelForm(request.POST, instance=order_obj)
        if order_form.is_valid():
            data = order_form.cleaned_data
            data = order_form.cleaned_data
            staff = UserInfo.objects.filter(id=data['staff_id'].id).first()
            customer = UserInfo.objects.filter(id=data['customer_id'].id).first()
            staff_legal = False if staff.is_customer is True else True
            customer_legal = False if customer.is_customer is False else True
            error_message = ""
            if not staff_legal:
                error_message += "所选经办人不为管理人员！"
            if not customer_legal:
                error_message += " 所选客户不为客户！"
            if (not staff_legal) or (not customer_legal):
                return render(request, "add_order.html", {"order_form": order_form, "error_message": error_message})
            else:
                order_form.save()
                return redirect(order_list)
        else:
            return HttpResponse("错误")


def add_item(request):
    if request.method == 'GET':
        item_form = ItemModelForm()
        return render(request, "add_item.html", {"item_form": item_form, "error_message": ""})
    else:
        item_form = ItemModelForm(request.POST)
        if item_form.is_valid():
            item_form.save()
            return redirect(item_list)
        else:
            return HttpResponse("错误")


def edit_item(request, id):
    item_obj = ItemInfo.objects.filter(id=id).first()
    if request.method == 'GET':
        item_form = ItemModelForm(instance=item_obj)
        return render(request, "add_item.html", {"item_form": item_form, "error_message": ""})
    else:
        item_form = ItemModelForm(request.POST, instance=item_obj)
        if item_form.is_valid():
            item_form.save()
            return redirect(item_list)
        else:
            return HttpResponse("错误")


def rate(request, id):
    order_obj = OrderInfo.objects.filter(id=id).first()
    print(order_obj.item_id)
    item_obj = ItemInfo.objects.filter(id=order_obj.item_id.id).first()

    staff_id = order_obj.staff_id
    staff_obj = StaffInfo.objects.filter(id=staff_id.id).first()
    title = "对[" + str(order_obj) + "]订单的评分"
    if request.method == 'GET':
        return render(request, "rate.html", {"title": title, "item_name": str(item_obj), "staff_name": str(staff_obj)})
    else:
        try:
            item_rate = float(request.POST.get("item_rate", None))
            staff_rate = float(request.POST.get("staff_rate", None))
            if item_rate > 10 or staff_rate > 10:
                raise RuntimeError("数值错误")
        except:
            return render(request, "rate.html",
                          {"title": title, "item_name": str(item_obj), "staff_name": str(staff_obj), "error_message": "请输入0-10以内的数字作为评分！"})
        else:
            ori_item_rate = item_obj.rate
            item_obj.rate = (ori_item_rate + item_rate) / 2
            item_obj.save()

            ori_staff_rate = staff_obj.rate
            staff_obj.rate = (ori_staff_rate + staff_rate) / 2
            staff_obj.save()

            order_obj.is_rated = True
            order_obj.save()

            return redirect(order_list)


