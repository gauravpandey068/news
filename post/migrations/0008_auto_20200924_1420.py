# Generated by Django 3.1.1 on 2020-09-24 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_auto_20200924_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='news/%y/%m/%d/'),
        ),
    ]