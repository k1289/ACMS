from django.contrib import admin
from django.urls import include, path
from rest_framework import routers, serializers, viewsets

from .views import (
	OrderCreateAPIView,
	#UserProfileAPIView,
	UserViewSet,
	UserList,
	UserDetail,
	OrderAPIView
	)

#router = routers.DefaultRouter()
#router.register('users', UserViewSet)

urlpatterns=[
	path('create/',OrderCreateAPIView.as_view(),name="create"),
	path('users/',UserList.as_view(),name="create"),
	path('users/<pk>',UserDetail.as_view(),name="create"),
	path('list/',	OrderAPIView.as_view(),name="create"),
	#path('user/',UserProfileAPIView.as_view(),name="user_create"),
]
