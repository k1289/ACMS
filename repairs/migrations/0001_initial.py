# Generated by Django 2.0.3 on 2018-03-22 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('ProductId', models.IntegerField(primary_key=True, serialize=False)),
                ('ProductName', models.CharField(max_length=200)),
                ('ProductModel', models.CharField(max_length=200)),
                ('ProductType', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Service_Centres',
            fields=[
                ('ScID', models.IntegerField(primary_key=True, serialize=False)),
                ('ScName', models.CharField(max_length=200)),
                ('ScLocation', models.CharField(max_length=200)),
                ('ScEmailID', models.CharField(max_length=200)),
                ('ScPhoneNum', models.CharField(max_length=200)),
                ('ScRatings', models.CharField(max_length=200)),
                ('Official', models.BooleanField(default=True)),
                ('ScProductID', models.ManyToManyField(to='repairs.Products')),
            ],
        ),
    ]
