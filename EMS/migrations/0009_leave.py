# Generated by Django 3.1.7 on 2021-03-26 05:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMS', '0008_employee_managerid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('leaveId', models.IntegerField(primary_key=True, serialize=False)),
                ('employeeId', models.CharField(max_length=20)),
                ('managerId', models.CharField(max_length=20, null=True)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('employeeReason', models.CharField(max_length=40)),
                ('managerReason', models.CharField(max_length=40)),
                ('appliedDate', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
    ]
