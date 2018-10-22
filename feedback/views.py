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
    if request.session[USER_TYPE] == 1:
        complaint_list = ComplaintInfo.objects.filter(customer_id=request.session[USER_ID])
        return render(request, "complaint_list.html", {"complaint_list": complaint_list})
    else:
        complaint_list = ComplaintInfo.objects.all()
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


def add_complaint(request):
    customer_id = UserInfo.objects.filter(id=request.session[USER_ID]).first()
    if request.method == 'GET':
        type_choices = dict(ComplaintInfo.TYPE_CHOICES).values()
        return render(request, 'add_complaint.html', {"type_choices": type_choices})
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        types = ComplaintInfo.HASH_TYPE[request.POST.get('types')]
        submit_date = timezone.now()
        status = 'submitted'

        complaint_obj = ComplaintInfo()
        complaint_obj.customer_id = customer_id
        complaint_obj.title = title
        complaint_obj.content = content
        complaint_obj.submit_date = submit_date
        complaint_obj.status = status
        complaint_obj.type = types

        complaint_obj.save()
        return redirect(complaint_list)


def edit_service(request, id):
    service_obj = ServiceInfo.objects.filter(id=id).first()
    if request.method == 'GET':
        status_choices = dict(ServiceInfo.STATUS_CHOICES).values()
        return render(request, 'edit_service.html', {"service_obj": service_obj, "status_choices": status_choices,
                                                     "now_status": dict(ServiceInfo.STATUS_CHOICES)[service_obj.status]})
    else:
        reply = request.POST.get('reply', None)
        last_modify_date = timezone.now()
        status = ServiceInfo.HASH_STATUS[request.POST.get('status', None)]
        service_obj.reply = reply
        service_obj.last_modify_date = last_modify_date
        service_obj.status = status

        service_obj.save()
        return redirect(service_list)

def edit_complaint(request, id):
    complaint_obj = ComplaintInfo.objects.filter(id=id).first()
    if request.method == 'GET':
        now_type = dict(ComplaintInfo.TYPE_CHOICES)[complaint_obj.type]
        status_choices = dict(ComplaintInfo.STATUS_CHOICES).values()
        now_status = dict(ComplaintInfo.STATUS_CHOICES)[complaint_obj.status]
        return render(request, 'edit_complaint.html', {"complaint_obj": complaint_obj, "now_type": now_type,
                                                       "now_status": now_status, "status_choices": status_choices})
    else:
        reply = request.POST.get('reply', None)
        last_modify_date = timezone.now()
        status = ServiceInfo.HASH_STATUS[request.POST.get('status', None)]
        complaint_obj.reply = reply
        complaint_obj.last_modify_date = last_modify_date
        complaint_obj.status = status
        complaint_obj.save()
        return redirect(complaint_list)