from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from orders.models import Profile, Order
from .serializers import OrderCreateSerializer
# Create your views here.

class OrderCreateAPIView(CreateAPIView):
	queryset = Order.objects.all()
	serializer_class=OrderCreateSerializer

