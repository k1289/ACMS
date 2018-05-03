from rest_framework.serializers import ModelSerializer
from repairs.models import Products,Service_Centres

class ProductsSerializer(ModelSerializer):
	class Meta:
		model = Products
		fields = [
		'ProductType',
		'ProductModel',
		'ProductId'

		]

class ServiceCentersSerializer(ModelSerializer):
	class Meta:
		model =Service_Centres		
		fields = [
		'ScID',
		'ScName',
		'ScProductID'
		]