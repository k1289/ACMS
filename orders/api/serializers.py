from rest_framework.serializers import ModelSerializer, SerializerMethodField
from repairs.models import Products,Service_Centres
from orders.models import Profile,Ordering
from mysite.api.serializers import ProductsSerializer,ProductDetailSerializer, ServiceCentreSerializer
import rest_framework
from rest_framework.response import Response
from rest_framework import serializers,viewsets
from django.contrib.auth.models import User
from django.utils.functional import SimpleLazyObject
import json
from rest_framework.validators import UniqueValidator

# class OrderSerializer(ModelSerializer):
# 	class Meta:
# 		model=Ordering
# 		fields = (
# 		'Problem',
# 		'OrderConfirmation',
# 		'Dateofrequest',
# 		'NumOfrepairdays',
# 		)

class OrderCreateSerializer(ModelSerializer):
	product = ProductDetailSerializer()
	# def user(self,obj):
	# 	user = self.context['request'].user
	# 	return user

	class Meta:
		model = Ordering
		fields = (
			'product',
			'OrderId',
			'user',
			'Problem',
			'OrderConfirmation',
			'Dateofrequest',
			'NumOfrepairdays',
		)


class OrderPostSerializer(ModelSerializer):
	class Meta:
		model = Ordering
		fields=fields = (
			'product',
			'OrderId',
			'user',
			'Problem',
			'OrderConfirmation',
			'Dateofrequest',
			'NumOfrepairdays',
		)


class UserSerializer(serializers.HyperlinkedModelSerializer):
	#orders = serializers.PrimaryKeyRelatedField(many=True, queryset=Ordering.objects.all())
	orders = OrderPostSerializer()
	class Meta:
		model = User
		fields = ('url', 'username','orders')
