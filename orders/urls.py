from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns=[
	path('orders/',include("orders.api.urls"),name="create"),
]