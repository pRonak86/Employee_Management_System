# Generated by Django 3.1.7 on 2021-04-10 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMS', '0018_auto_20210403_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='tasks',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('employeeId', models.CharField(max_length=20)),
                ('managerId', models.CharField(max_length=20)),
                ('clientId', models.IntegerField(null=True)),
                ('projectId', models.IntegerField()),
                ('date', models.DateField()),
                ('workDescription', models.CharField(max_length=40, null=True)),
                ('fileUpload', models.FileField(null=True, upload_to='documents')),
            ],
        ),
        migrations.AddField(
            model_name='clientproject',
            name='fileUpload1',
            field=models.FileField(null=True, upload_to='documents'),
        ),
        migrations.AddField(
            model_name='clientproject',
            name='fileUpload2',
            field=models.FileField(null=True, upload_to='documents'),
        ),
        migrations.AddField(
            model_name='employee',
            name='resume',
            field=models.FileField(null=True, upload_to='documents'),
        ),
    ]
