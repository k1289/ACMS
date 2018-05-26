from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from django.contrib.auth import views as auth_views
from rest_framework import routers
from . import views

urlpatterns=[
#	path('', include(router.urls)),
	path('orders/',include("orders.api.urls"),name="create"),
	#path('ordertable/',views.orders_home,name="table"),
]