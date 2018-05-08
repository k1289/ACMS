from rest_framework.serializers import ModelSerializer, SerializerMethodField
from repairs.models import Products,Service_Centres

class ProductsSerializer(ModelSerializer):
	class Meta:
		model = Products 
		fields = [
		'ProductType',
		'ProductModel',

		]
		

class ServiceCentreSerializer(ModelSerializer):
	class Meta:
		model = Service_Centres
		fields = [
		'ScName',
		'ScLocation',

		]


class ProductDetailSerializer(ModelSerializer):
	sq=SerializerMethodField()
	class Meta:
		model =Products
		fields = [
		'sq',

		]
				
	def get_sq(self, obj):
		q=obj.ProductServiceCentres.all()
		return str(q)
		
