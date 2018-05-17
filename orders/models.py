# Create your models here.
from django.db import models
from repairs.models import Products, Service_Centres
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
	ProfileId = models.IntegerField(primary_key=True)
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	FirstName = models.CharField(max_length=50)
	LastName =models.CharField(max_length=50)
	PhoneNum = models.CharField(max_length=10)
	Address = models.CharField(max_length=200) 

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Order(models.Model):
	OrderId = models.IntegerField(primary_key=True)
	#ProductId = models.ForeignKey(Products,related_name='placeorder',on_delete=models.CASCADE)
	#UserId = models.ForeignKey(Profile,related_name='customer')
	#ServiceProductId = models.OneToOneField(Service_Centres,related_name='selectcentre',on_delete=models.CASCADE)
	Problem = models.CharField(max_length=500)
	OrderConfirmation = models.BooleanField(default=False)
	Dateofrequest = models.DateField()
	NumOfrepairdays=models.IntegerField(default=5)

