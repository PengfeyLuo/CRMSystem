from django.db import models

# Create your models here.


class CustomerInfo(models.Model):
    company = models.CharField(max_length=64, blank=False, null=False)
    representative = models.CharField(max_length=32, blank=False, null=False)
    postcode = models.CharField(max_length=32, blank=False, null=False)
    address = models.CharField(max_length=64, blank=False, null=False)
    apartment = models.CharField(max_length=32, blank=False, null=False)
    agent = models.CharField(max_length=32, blank=False, null=False)
    telephone = models.CharField(max_length=32, blank=False, null=False)
    bank = models.CharField(max_length=32, blank=False, null=False)
    taxid = models.CharField(max_length=32, blank=False, null=False)

    def __str__(self):
        return "Customer " + str(self.id) + " " + self.representative


class StaffInfo(models.Model):
    age = models.IntegerField(blank=False, null=False)
    gender = models.CharField(max_length=32, blank=False, null=False)
    apartment = models.CharField(max_length=32, blank=False, null=False)
    role = models.CharField(max_length=32, blank=False, null=False)
    address = models.CharField(max_length=64, blank=True, null=True)

    rate = models.FloatField(default=10.0)

    def __str__(self):
        return "Staff" + str(self.id)
