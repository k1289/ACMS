from django.contrib import admin
from django.urls import include, path
from .views import (
	ProductsListAPIView,
	ServiceCentreListAPIView,
	ServiceProductAPIView,
	#OrderCreateAPIView,
	ServiceRetrieveAPIView
	)

urlpatterns=[
	#path('create/',OrderCreateAPIView.as_view(),name="create"),
	path('',ProductsListAPIView.as_view(), name="products-api"),
	path('sc',ServiceCentreListAPIView.as_view(),name="sc"),
	path('<pk>',ServiceProductAPIView.as_view(),name="list"),
	path('list/<pk>',ServiceRetrieveAPIView.as_view(),name='product_centre'),
]
