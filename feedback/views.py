from django.shortcuts import render, redirect, HttpResponse
from django.utils import timezone
from .models import ServiceInfo, ComplaintInfo, OrderInfo
from .forms import ServiceModelForm, ComplaintModelForm
from rbac.models import UserInfo
from case.models import OrderInfo
from CRMSystem.settings import USER_ID, USER_TYPE
# Create your views here.


def service_list(request):
    if request.session[USER_TYPE] == 1:
        service_list = ServiceInfo.objects.filter(customer_id=request.session[USER_ID])
        return render(request, "service_list.html", {"services_list": service_list})
    else:
        service_list = ServiceInfo.objects.all()
        return render(request, "service_list.html", {"services_list": service_list})


def complaint_list(request):
    global complaint_list
    if request.session[USER_TYPE] == 1:
        complaint_list = ServiceInfo.objects.filter(customer_id=request.session[USER_ID])
    else:
        complaint_list = ServiceInfo.objects.all()
    return render(request, "complaint_list.html", {"complaint_list": complaint_list})


def add_service(request):
    customer_order = OrderInfo.objects.filter(customer_id=request.session[USER_ID])
    if request.method == 'GET':
        service_form = ServiceModelForm()
        return render(request, "add_service.html", {"service_form": service_form, "customer_order": customer_order})
    else:
        # service_form_test = ServiceModelForm(request.POST)
        order_message = request.POST.get("order_id", None)
        # print(order_message.split(' '))
        idx = int("".join(order_message.split(' ')[0]))
        order_id = OrderInfo.objects.filter(id=idx).first()
        staff_id = order_id.staff_id
        content = request.POST.get("content", None)
        submit_date = timezone.now()
        status = "submitted"
        customer_id = UserInfo.objects.filter(id=request.session[USER_ID]).first()
        service_obj = ServiceInfo()
        service_obj.customer_id = customer_id
        service_obj.order_id = order_id
        service_obj.staff_id = staff_id
        service_obj.content = content
        service_obj.submit_date = submit_date
        service_obj.status = status

        service_obj.save()
        return redirect(service_list)


# def add_complaint(request):
#     customer_id = UserInfo.objects.filter(id=request.session[USER_ID]).first()
#     if request.method == 'GET':
#
#         title = request.POST.get('title')
#         content =
