# Generated by Django 3.1.5 on 2021-02-04 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=255)),
                ('phone', models.CharField(default='', max_length=13)),
                ('email', models.CharField(default='', max_length=100)),
                ('content', models.CharField(default='', max_length=500)),
            ],
        ),
    ]