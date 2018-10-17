from django.shortcuts import render, redirect, reverse
from .models import UserInfo, Role, Permission, Menu
from User.models import CustomerMessage, StaffMessage
from .forms import UserInfoModelForm, RoleModelForm, PermissionModelForm, MenuModelForm
from User.forms import CustomerModelForm, StaffModelForm
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def users(request):
    """查询所有用户信息"""
    user_list = UserInfo.objects.all()
    return render(request, 'users.html', {'user_list': user_list})


def users_new(request):
    if request.method =="GET":
        # 传入ModelForm对象
        model_form = UserInfoModelForm()
        return render(request, 'common_edit.html', {'model_form': model_form, 'title': '新增用户'})
    else:
        model_form = UserInfoModelForm(request.POST)
        if model_form.is_valid():
            model_form.save()
            return redirect(reverse(users))
        else:
            return render(request, 'common_edit.html',{'model_form': model_form, 'title': '新增用户'})


def users_edit(request,id):
    user_obj = UserInfo.objects.filter(id=id).first()
    if request.method == 'GET':
        model_form = UserInfoModelForm(instance=user_obj)
        return render(request, 'common_edit.html', {'model_form': model_form, 'title': '编辑用户'})
    else:
        model_form = UserInfoModelForm(request.POST, instance=user_obj)
        if model_form.is_valid():
            model_form.save()
            return redirect(reverse(users))
        else:
            return render(request, 'common_edit.html', {'model_form': model_form, 'title': '编辑用户'})


def users_delete(request, id):
    user_obj = UserInfo.objects.filter(id=id).first()
    user_obj.delete()
    return redirect(reverse(users))


def roles(request):
    role_list = Role.objects.all()
    return render(request, 'roles.html', {'role_list': role_list})


def roles_new(request):
    if request.method == "GET":
        # 传入ModelForm对象
        model_form = RoleModelForm()
        return render(request, 'common_edit.html', {'model_form': model_form, 'title': '新增角色'})
    else:
        model_form = RoleModelForm(request.POST)
        if model_form.is_valid():
            model_form.save()
            return redirect(reverse(roles))
        else:
            return render(request, 'common_edit.html', {'model_form': model_form, 'title': '新增角色'})


def roles_edit(request, id):
    role_obj = Role.objects.filter(id=id).first()
    if request.method == 'GET':
        model_form = RoleModelForm(instance=role_obj)
        return render(request, 'common_edit.html', {'model_form': model_form, 'title': '编辑角色'})
    else:
        model_form = RoleModelForm(request.POST, instance=role_obj)
        if model_form.is_valid():
            model_form.save()
            return redirect(reverse(roles))
        else:
            return render(request, 'common_edit.html', {'model_form': model_form, 'title': '编辑角色'})


def roles_delete(request, id):
    role_obj = Role.objects.filter(id=id).first()
    role_obj.delete()
    return redirect(reverse(roles))


def permissions(request):
    permission_list = Permission.objects.all()
    return render(request, 'permissions.html', {'permission_list': permission_list})


def permissions_new(request):
    if request.method == "GET":
        # 传入ModelForm对象
        model_form = PermissionModelForm()
        return render(request, 'common_edit.html', {'model_form': model_form, 'title': '新增权限'})
    else:
        model_form = PermissionModelForm(request.POST)
        if model_form.is_valid():
            model_form.save()
            return redirect(reverse(permissions))
        else:
            return render(request, 'common_edit.html', {'model_form': model_form, 'title': '新增权限'})


def permissions_edit(request, id):
    permission_obj = Permission.objects.filter(id=id).first()
    if request.method == 'GET':
        model_form = PermissionModelForm(instance=permission_obj)
        return render(request, 'common_edit.html', {'model_form': model_form, 'title': '编辑权限'})
    else:
        model_form = PermissionModelForm(request.POST, instance=permission_obj)
        if model_form.is_valid():
            model_form.save()
            return redirect(reverse(permissions))
        else:
            return render(request, 'common_edit.html', {'model_form': model_form, 'title': '编辑权限'})


def permissions_delete(request, id):
    permission_obj = Role.objects.filter(id=id).first()
    permission_obj.delete()
    return redirect(reverse(permissions))


def menus(request):
    menu_list = Menu.objects.all()
    print(str(menu_list))
    return render(request, 'menus.html', {'menu_list': menu_list})


def menus_new(request):
    if request.method == "GET":
        # 传入ModelForm对象
        model_form = MenuModelForm()
        return render(request, 'common_edit.html', {'model_form': model_form, 'title': '新增菜单'})
    else:
        model_form = MenuModelForm(request.POST)
        if model_form.is_valid():
            model_form.save()
            return redirect(reverse(menus))
        else:
            return render(request, 'rbac/common_edit.html', {'model_form': model_form, 'title': '新增菜单'})


def menus_edit(request, id):
    menu_obj = Menu.objects.filter(id=id).first()
    if request.method == 'GET':
        model_form = MenuModelForm(instance=menu_obj)
        return render(request, 'common_edit.html', {'model_form': model_form, 'title': '编辑菜单'})
    else:
        model_form = MenuModelForm(request.POST, instance=menu_obj)
        if model_form.is_valid():
            model_form.save()
            return redirect(reverse(menus))
        else:
            return render(request, 'common_edit.html', {'model_form': model_form, 'title': '编辑菜单'})


def menus_delete(request, id):
    menu_obj = Role.objects.filter(id=id).first()
    menu_obj.delete()
    return redirect(reverse(menus))


def message(request):
    userlist = UserInfo.objects.all()
    print(UserInfo.objects.last().id)
    # messagelist = list()
    # userlist = list(userlist)
    # cnt = 0
    # for user in userlist:
    #     print(user.username, user.iscustomer)
    #     if user.iscustomer == True:
    #         other = CustomerMessage.objects.filter(id=user.id).first()
    #         print(other.bank    )
    #         messagelist.append({'user': user, 'other': other})
    #     else:
    #         other = StaffMessage.objects.filter(id=user.id).first()
    #
    #         messagelist.append({'user': user, 'other': other})
    #     cnt = cnt + 1
    # # print(newlist[1]["otherinfo"])
    return render(request, "message.html", {'userlist': userlist})
    # return HttpResponse(newlist[0])


def message_edit(requst, id):
    user_obj = UserInfo.objects.filter(id=id).first()
    if user_obj.iscustomer == True:
        message_obj = CustomerMessage.objects.filter(id=user_obj.messageid).first()
        if requst.method == 'GET':
            user_form = UserInfoModelForm(instance=user_obj)
            message_form = CustomerModelForm(instance=message_obj)
            return render(requst, 'message_edit.html', {'user_form': user_form, 'message_form': message_form})
        else:
            user_form = UserInfoModelForm(requst.POST, instance=user_obj)
            message_form = CustomerModelForm(requst.POST, instance=message_obj)
            if user_form.is_valid() and message_form.is_valid():
                user_form.save()
                message_form.save()
                return redirect(reverse(message))
            else:
                return HttpResponse("错误")
    else:
        message_obj = StaffMessage.objects.filter(id=user_obj.messageid).first()
        if requst.method == 'GET':
            user_form = UserInfoModelForm(instance=user_obj)
            message_form = StaffModelForm(instance=message_obj)
            return render(requst, 'message_edit.html', {'user_form': user_form, 'message_form': message_form})
        else:
            user_form = UserInfoModelForm(requst.POST, instance=user_obj)
            message_form = StaffModelForm(requst.POST, instance=message_obj)
            if user_form.is_valid() and message_form.is_valid():
                user_form.save()
                message_form.is_valid()
                return redirect(reverse(message))
            else:
                return HttpResponse("错误")


def newcustomer(request):
    if request.method == 'GET':
        user_form = UserInfoModelForm()
        message_form = CustomerModelForm()
        return render(request, 'message_edit.html', {'user_form': user_form, 'message_form':message_form})
    else:
        user_form = UserInfoModelForm(request.POST)
        message_form = CustomerModelForm(request.POST)
        if user_form.is_valid() and message_form.is_valid():
            lastmessage = user_form.cleaned_data
            # print(lastmessage)
            user_form.save()
            message_form.save()
            user_obj = UserInfo.objects.last()
            user_obj.messageid = CustomerMessage.objects.last().id
            user_obj.iscustomer = True
            user_obj.save()
            return redirect(reverse(message))
        else:
            return HttpResponse("错误")


def newstaff(request):
    if request.method == 'GET':
        user_form = UserInfoModelForm()
        message_form = StaffModelForm()
        return render(request, 'message_edit.html', {'user_form': user_form, 'message_form': message_form})
    else:
        user_form = UserInfoModelForm(request.POST)
        message_form = StaffModelForm(request.POST)
        if user_form.is_valid() and message_form.is_valid():
            latest_message = user_form.cleaned_data
            user_form.save()
            message_form.save()
            user_obj = UserInfo.objects.last()
            user_obj.messageid = StaffMessage.objects.last().id
            user_obj.iscustomer = False
            user_obj.save()
            return redirect(reverse(message))
        else:
            return HttpResponse("错误")