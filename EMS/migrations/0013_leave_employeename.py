# Generated by Django 3.1.7 on 2021-03-31 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMS', '0012_auto_20210331_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='employeeName',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
