# Generated by Django 2.0.3 on 2018-05-19 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20180519_0653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordering',
            name='centre',
        ),
    ]