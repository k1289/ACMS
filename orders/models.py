# Create your models here.
from django.db import models
from repairs.models import Products, Service_Centres
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from django import forms
#from mysite.views import get_username
from django.contrib.auth import authenticate, login
from django.contrib.auth.signals import user_logged_in
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Profile(models.Model):
	ProfileId = models.AutoField(primary_key=True)
	user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
	#orders = models.ForeignKey(Ordering,null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

'''class OrderManager(models.Manager):
	def new_or_get(self, request):
		order_id = request.session.get("ordering_Order", None)
		qs = self.get_queryset().filter(id=order_id)
		if qs.count() == 1:
			new_obj = False
			order_obj = qs.first()
			if request.user.is_authenticated() and order_obj.user is None:
				order_obj.user = request.user
				order_obj.save()
		else:
			order_obj = Ordering.objects.new(user=request.user)
			new_obj = True
			request.session['order_id'] = order_obj.id
		return order_obj, new_obj

	def new(self, user=None):
		order_obj = None
		if user is not None:
			if user.is_authenticated():
				user_obj = user
		return self.model.objects.create(user=user_obj)'''

class Ordering(models.Model):
	OrderId = models.AutoField(primary_key=True)
	product = models.ForeignKey(Products,related_name='placeorder',default=0,on_delete=models.CASCADE)
	#user = models.ForeignKey(User,related_name='orders',on_delete=models.CASCADE)
	user = models.CharField(max_length=20)
	Problem = models.CharField(max_length=500)
	OrderConfirmation = models.BooleanField(default=False)
	Dateofrequest = models.DateTimeField(default=datetime.now)
	NumOfrepairdays=models.IntegerField(default=5)

	#objects = OrderManager()

	# def __str__(self):
	# 	return str(self.id)
