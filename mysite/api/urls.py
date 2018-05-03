from django.contrib import admin
from django.urls import include, path
from .views import (
	ProductsListAPIView,
	ServiceCentersListAPIView
	)
urlpatterns=[
	path('products',ProductsListAPIView.as_view(), name='list'),
	path('servicecenters',ServiceCentersListAPIView.as_view(), name='list'),
	
]
