from django.db import models

# Create your models here.


class ApartmentInfo(models.Model):
    choices = [
        ('all', 'مشاع'),
        ('unit', 'مجزا'),
    ]
    methods = [
        ('peopleCount', 'برحسب تعداد نفرات'),
        ('unitCount', 'برحسب تعداد واحدها'),
        ('fund', 'صندوق ساختمان'),
        ('manual', 'دستی'),
    ]
    name = models.CharField(max_length=50, blank=True)
    adres = models.CharField(max_length=250, blank=True)
    unit_count = models.CharField(max_length=5, default=6)
    floor_count = models.CharField(max_length=3, default=3)
    water_bill = models.CharField(choices=choices, default='all')
    gas_bill = models.CharField(choices=choices, default='all')
    charge_cost = models.CharField(max_length=15)
    water_bill_pay_mathod = models.CharField(choices=methods)
    gas_bill_pay_mathod = models.CharField(choices=methods)
    electric_bill_pay_mathod = models.CharField(choices=methods)

    def __str__(self) -> str:
        return self.name


class UnitInfo (models.Model):
    choices = [
        ('owner', 'مالک'),
        ('tenant', 'مستاجر'),
    ]
    genders = [
        ('M', 'آقا'),
        ('W', 'خانم'),
    ]
    unit_no = models.CharField(max_length=3)
    resident_no = models.CharField(max_length=3)
    unit_floor = models.CharField(max_length=3)
    mobile = models.CharField(max_length=11, unique=True)
    home_phone = models.CharField(max_length=11)
    emergency_phone = models.CharField(max_length=11)
    owner_tenant = models.CharField(choices=choices)
    owner_name = models.CharField(max_length=50)
    owner_phone = models.CharField(max_length=11)
    date_in = models.CharField(max_length=10, blank=True)
    date_out = models.CharField(max_length=10, blank=True)
    username = models.CharField(max_length=150, unique=True)
    gender = models.CharField(max_length=1, choices=genders)

    def __str__(self) -> str:
        return 'Unit:' + self.unit_no + ', Username:' + self.username
