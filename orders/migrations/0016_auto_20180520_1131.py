# Generated by Django 2.0.3 on 2018-05-20 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_ordering_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordering',
            old_name='owner',
            new_name='username',
        ),
    ]