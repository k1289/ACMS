from django.db import models

# Create your models here.

class Products(models.Model):
	ProductId = models.IntegerField(primary_key=True)
	ProductName = models.CharField(max_length=200)
	ProductModel = models.CharField(max_length=200)
	ProductType = models.CharField(max_length=200)

	def __str__(self):
		return self.ProductName
	
class Service_Centres(models.Model):
	ScID = models.IntegerField(primary_key=True)
	ScName = models.CharField(max_length=200)
	ScLocation = models.CharField(max_length=200)
	ScEmailID = models.CharField(max_length=200)
	ScPhoneNum = models.CharField(max_length=200)
	ScRatings = models.CharField(max_length=200)
	ScProductID = models.ManyToManyField(Products)
	Official = models.BooleanField(default=True)

	def __str__(self):
		return self.ScName
