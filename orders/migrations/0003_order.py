# Generated by Django 2.0.3 on 2018-05-19 06:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0003_products_productservicecentres'),
        ('orders', '0002_auto_20180519_0637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('OrderId', models.AutoField(primary_key=True, serialize=False)),
                ('Problem', models.CharField(max_length=500)),
                ('OrderConfirmation', models.BooleanField(default=False)),
                ('Dateofrequest', models.DateField(default=datetime.datetime.today)),
                ('NumOfrepairdays', models.IntegerField(default=5)),
                ('centre', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='selectcentre', to='repairs.Service_Centres')),
                ('product', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='placeorder', to='repairs.Products')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='orders.Profile')),
            ],
        ),
    ]
