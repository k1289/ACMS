from django.contrib import admin
from django.urls import include, path
from .views import (
	ProductsListAPIView,
	ServiceCentreListAPIView,
	ServiceProductAPIView,
	)

urlpatterns=[
	path('products',ProductsListAPIView.as_view(), name="products-api"),
	path('sc',ServiceCentreListAPIView.as_view(),name="sc"),
	path('sl/<pk>',ServiceProductAPIView.as_view(),name="list"),
]

