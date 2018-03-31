# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Product(models.Model):
	productID=models.IntegerField(primary_key=True)
	productName=models.CharField(max_length=1000)
	productModel=models.CharField(max_length=1000)
	productType=models.CharField(max_length=1000)

	def __str__(self):
		return self.productName