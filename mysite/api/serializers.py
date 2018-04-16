from rest_framework.serializers import ModelSerializer
from repairs.models import Products

class ProductsSerializer(ModelSerializer):
	class Meta:
		model = Products
		fields = [
		'ProductType',
		'ProductModel'

		]