# Generated by Django 3.1.1 on 2020-09-24 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20200924_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_by',
        ),
    ]
