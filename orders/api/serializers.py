from rest_framework.serializers import ModelSerializer, SerializerMethodField
from repairs.models import Products,Service_Centres
from orders.models import Profile,Order
from mysite.api.serializers import ProductDetailSerializer, ServiceCentreSerializer
import rest_framework
from rest_framework.response import Response

class OrderSerializer(ModelSerializer):
	class Meta:
		model=Order
		fields = [
		'Problem',
		'OrderConfirmation',
		'Dateofrequest',
		'NumOfrepairdays',
		]

class OrderCreateSerializer(ModelSerializer):
	
	#placeorder=OrderSerializer(many=False)
	#selectcentre=ServiceCentreSerializer(many=False,read_only=True)
	class Meta:
		model = Order
		fields = [
			#'UserId',
	#		'ProductId',
	#		'selectcentre',
			#'placeorder',
		'Problem',
		'OrderConfirmation',
		'Dateofrequest',
		'NumOfrepairdays',
		]
