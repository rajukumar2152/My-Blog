# Generated by Django 3.1.5 on 2021-02-05 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210204_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='timeStamp',
        ),
    ]
