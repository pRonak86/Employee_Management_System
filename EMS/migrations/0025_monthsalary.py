# Generated by Django 3.1.7 on 2021-04-19 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMS', '0024_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='monthSalary',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('empCode', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('month', models.CharField(max_length=20, null=True)),
                ('year', models.IntegerField(null=True)),
                ('totalTime', models.IntegerField()),
                ('daySalary', models.IntegerField()),
                ('finalSalary', models.IntegerField()),
            ],
        ),
    ]
