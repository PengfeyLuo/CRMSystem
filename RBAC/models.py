from django.db import models

# Create your models here.

class Menu(models.Model):
    """
    菜单模型
    """
    title = models.CharField(max_length=32, unique=True, null=False)
    parent = models.ForeignKey("Menu", null=False, blank=True， )