# Generated by Django 3.1.7 on 2021-03-20 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMS', '0002_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='resume',
            field=models.FileField(null=True, upload_to='documents'),
        ),
    ]
