from django.contrib import admin
from django.urls import include, path
from .views import (
	ProductsListAPIView
	)
urlpatterns=[
	path('',ProductsListAPIView.as_view(), name='list'),
	
]
