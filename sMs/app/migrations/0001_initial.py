# Generated by Django 5.0 on 2024-01-07 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApartmentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('adres', models.CharField(blank=True, max_length=250)),
                ('unit_count', models.CharField(default=6, max_length=5)),
                ('floor_count', models.CharField(default=3, max_length=3)),
                ('water_bill', models.CharField(choices=[('all', 'مشاع'), ('unit', 'مجزا')], default='all')),
                ('gas_bill', models.CharField(choices=[('all', 'مشاع'), ('unit', 'مجزا')], default='all')),
                ('charge_cost', models.CharField(max_length=15)),
                ('water_bill_pay_mathod', models.CharField(choices=[('peopleCount', 'برحسب تعداد نفرات'), ('unitCount', 'برحسب تعداد واحدها'), ('fund', 'صندوق ساختمان'), ('manual', 'دستی')])),
                ('gas_bill_pay_mathod', models.CharField(choices=[('peopleCount', 'برحسب تعداد نفرات'), ('unitCount', 'برحسب تعداد واحدها'), ('fund', 'صندوق ساختمان'), ('manual', 'دستی')])),
                ('electric_bill_pay_mathod', models.CharField(choices=[('peopleCount', 'برحسب تعداد نفرات'), ('unitCount', 'برحسب تعداد واحدها'), ('fund', 'صندوق ساختمان'), ('manual', 'دستی')])),
            ],
        ),
        migrations.CreateModel(
            name='UnitInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_no', models.CharField(max_length=3)),
                ('resident_no', models.CharField(max_length=3)),
                ('unit_floor', models.CharField(max_length=3)),
                ('mobile', models.CharField(max_length=11, unique=True)),
                ('home_phone', models.CharField(max_length=11)),
                ('emergency_phone', models.CharField(max_length=11)),
                ('owner_tenant', models.CharField(choices=[('owner', 'مالک'), ('tenant', 'مستاجر')])),
                ('owner_name', models.CharField(max_length=50)),
                ('owner_phone', models.CharField(max_length=11)),
                ('date_in', models.CharField(blank=True, max_length=10)),
                ('date_out', models.CharField(blank=True, max_length=10)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('gender', models.CharField(choices=[('M', 'آقا'), ('W', 'خانم')], max_length=1)),
            ],
        ),
    ]
