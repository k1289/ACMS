from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveAPIView, ListAPIView
from orders.models import Profile, Ordering
from .serializers import OrderCreateSerializer, OrderPostSerializer, UserSerializer
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets

#class UserProfileAPIView(CreateAPIView):
#	queryset = Profile.objects.all()
#	serializer_class=UserProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#@login_required(login_url='/login/')
class OrderCreateAPIView(ListCreateAPIView):
	queryset = Ordering.objects.all()
	serializer_class=OrderCreateSerializer

	def get_serializer_class(self):
		assert self.serializer_class is not None, (
			"'%s' should either include a `serializer_class` attribute, "
			"or override the `get_serializer_class()` method."
			% self.__class__.__name__
		)

		if self.request.method in ('POST', 'PUT'):
			return OrderPostSerializer
		else:
			return self.serializer_class


class OrderAPIView(ListAPIView):
	queryset = Ordering.objects.all()
	serializer_class=OrderPostSerializer
