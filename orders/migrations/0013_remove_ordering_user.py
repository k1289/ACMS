# Generated by Django 2.0.3 on 2018-05-20 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20180519_0807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordering',
            name='user',
        ),
    ]
