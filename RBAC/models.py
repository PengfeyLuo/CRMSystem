from django.db import models

# Create your models here.

class Menu(models.Model):
    """
    菜单模型
    """
    title = models.CharField(max_length=32, unique=True, null=False)
    parent = models.ForeignKey("Menu", null=False, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        title_list = [self.title]
        p = self.parent
        while p:
            title_list.append(0, p.title)
            p = p.parent
        return '-'.join(title_list)


class Permission(models.Model):
    """
    权限
    """
    title = models.CharField(max_length=32, unique=True, null=False)
    url = models.CharField(max_length=128, unique=False, null=False)
    menu = models.ForeignKey("Menu", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{menu} --- {permission}".format(menu=self.menu, permission=self.title)


class Role(models.Model):
    """
    角色
    """
    title = models.CharField(max_length=32, unique=True)
    permissions = models.ManyToManyField("Permission")

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """
    用户
    """
    username = models.CharField(max_length=32, unique=True, null=False)
    password = models.CharField(max_length=128, null=False)
    nickname = models.CharField(max_length=32, null=False)
    email = models.EmailField(null=True)
    is_customer = models.BooleanField(default=False, null=False)
    database_id = models.IntegerField(blank=False)

    roles = models.ManyToManyField("Role")

    def __str__(self):
        return self.nickname
