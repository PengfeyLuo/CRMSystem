from django.shortcuts import render, redirect, HttpResponse, reverse
from rbac.models import UserInfo
from rbac.service.init_permission import init_permission
from django.conf import settings
from rbac.forms import UserInfoModelForm
from .models import CustomerInfo, StaffInfo
from .forms import CustomerModelForm, StaffModelForm
import json
from case.models import ItemInfo
from CRMSystem.settings import USER_ID, USER_TYPE

# Create your views here.


def login(request):
    if request.method == "GET":
        print()
        try:
            tset = request.session[settings.SESSION_PERMISSION_URL_KEY]
        except:
            return render(request, "login.html", {'error': json.dumps(False)})
        else:
            return redirect('/index/')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = UserInfo.objects.filter(username=username, password=password).first()
        if not user_obj:
            return render(request, "login.html", {'error': json.dumps(True), 'message': '用户名或密码错误'})
        else:
            init_permission(request, user_obj)
            return redirect('/index/')


def index(request):
    tmp=ItemInfo.objects.order_by('-production_date')
    Item_name=[]
    Item_data=[]
    count=0
    for item in tmp:
        print(count)
        Item_name.append(item.name+item.model)
        #Item_name.append(item.name + item.model + '\\n' + str(item.production_date))
        Item_data.append(str(item.rate))        #注意传给前端Echarts的一定都要是字符串
        count+=1
        if count>=6:
            break

    content={"Item_name":Item_name,"Item_data":Item_data, 'user_type': request.session[USER_TYPE]}
    return render(request, 'index.html', content)


def logout(request):
    try:
        del request.session[settings.SESSION_PERMISSION_URL_KEY]
        del request.session[settings.SESSION_MENU_KEY]
    except:
        return redirect(login)
    else:
        return redirect(login)


def user_list(request):
    user_list = UserInfo.objects.all()
    return render(request, "user_list.html", {"user_list": user_list, 'user_type': request.session[USER_TYPE]})


def user_edit(request, id):
    user_obj = UserInfo.objects.filter(id=id).first()
    id_recorder = user_obj.database_id
    if user_obj.is_customer:
        customer_obj = CustomerInfo.objects.filter(id=user_obj.database_id).first()
        if request.method == "GET":
            user_form = UserInfoModelForm(instance=user_obj)
            customer_form = CustomerModelForm(instance=customer_obj)
            return render(request, 'edit_user.html', {'user_form': user_form, 'message_form': customer_form, 'user_type': request.session[USER_TYPE]})
        else:
            user_form = UserInfoModelForm(request.POST, instance=user_obj)
            customer_form = CustomerModelForm(request.POST, instance=customer_obj)
            if user_form.is_valid() and customer_form.is_valid():
                user_form.save()
                customer_form.save()
                user_obj = UserInfo.objects.filter(id=id).first()
                user_obj.is_customer = True
                user_obj.database_id = id_recorder
                user_obj.save()
                return redirect(reverse(user_list))
            else:
                return HttpResponse("错误")
    else:
        staff_obj = StaffInfo.objects.filter(id=user_obj.database_id).first()
        if request.method == 'GET':
            user_form = UserInfoModelForm(instance=user_obj)
            staff_form = StaffModelForm(instance=staff_obj)
            return render(request, 'edit_user.html', {'user_form': user_form, 'message_form': staff_form, 'user_type': request.session[USER_TYPE]})
        else:
            user_form = UserInfoModelForm(request.POST, instance=user_obj)
            staff_form = StaffModelForm(request.POST, instance=staff_obj)
            if user_form.is_valid() and staff_form.is_valid():
                user_form.save()
                staff_form.is_valid()
                user_obj = UserInfo.objects.filter(id=id).first()
                user_obj.is_customer = False
                user_obj.database_id = id_recorder
                user_obj.save()
                return redirect(reverse(user_list))
            else:
                return HttpResponse("错误")


def add_customer(request):
    if request.method == 'GET':
        user_form = UserInfoModelForm()
        customer_form = CustomerModelForm()
        return render(request, "edit_user.html", {"user_form": user_form, "message_form": customer_form, 'user_type': request.session[USER_TYPE]})
    else:
        user_form = UserInfoModelForm(request.POST)
        customer_form = CustomerModelForm(request.POST)
        if user_form.is_valid() and customer_form.is_valid():
            user_form.save()
            customer_form.save()
            user_obj = UserInfo.objects.last()
            user_obj.database_id = CustomerInfo.objects.last().id
            user_obj.is_customer = True
            user_obj.save()
            return redirect(user_list)
        else:
            return HttpResponse("错误")


def add_staff(request):
    if request.method == 'GET':
        user_form = UserInfoModelForm()
        staff_form = StaffModelForm()
        return render(request, "edit_user.html", {"user_form": user_form, "message_form": staff_form, 'user_type': request.session[USER_TYPE]})
    else:
        user_form = UserInfoModelForm(request.POST)
        staff_form = StaffModelForm(request.POST)
        if user_form.is_valid() and staff_form.is_valid():
            user_form.save()
            staff_form.save()
            user_obj = UserInfo.objects.last()
            user_obj.database_id = StaffInfo.objects.last().id
            user_obj.is_customer = False
            user_obj.save()
            return redirect(user_list)
        else:
            return HttpResponse("错误")


def profile(request):
    if request.session[USER_TYPE] == 1:
        tmp=UserInfo.objects.get(id=request.session[USER_ID])
        person=CustomerInfo.objects.get(id=tmp.database_id)
        return render(request, "profile.html", {"user":tmp, "person":person, 'user_type': request.session[USER_TYPE]})
    else:
        tmp=UserInfo.objects.get(id=request.session[USER_ID])
        person=StaffInfo.objects.get(id=request.session[USER_ID])
        return render(request, "profile.html", {"user":tmp, "person":person, 'user_type': request.session[USER_TYPE]})