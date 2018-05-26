# Generated by Django 2.0.3 on 2018-05-19 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0003_products_productservicecentres'),
        ('orders', '0008_remove_ordering_centre'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordering',
            name='centre',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='selectcentre', to='repairs.Service_Centres'),
        ),
        migrations.AlterField(
            model_name='ordering',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='orders.Profile'),
        ),
    ]