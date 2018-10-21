from django.shortcuts import render, redirect
from .models import ServiceInfo, ComplaintInfo, OrderInfo
from .forms import ServiceModelForm, ComplaintModelForm
from CRMSystem.settings import USER_ID, USER_TYPE
# Create your views here.


def service_list(request):
    global service_list
    if request.session[USER_TYPE] == 1:
        service_list = ServiceInfo.objects.filter(customer_id=request.session[USER_ID])
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
        service_form = ServiceModelForm(request.POST)
        if service_form.is_valid():
            service_form.save()

            return redirect(service_list)
