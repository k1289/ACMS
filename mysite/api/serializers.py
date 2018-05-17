from rest_framework.serializers import ModelSerializer, SerializerMethodField
from repairs.models import Products,Service_Centres
#from mysite.models import Profile,Order
import rest_framework
class ProductsSerializer(ModelSerializer):
	class Meta:
		model = Products 
		fields = [
		'ProductName',
		'ProductModel',

		]
		

class ServiceCentreSerializer(ModelSerializer):
	class Meta:
		model = Service_Centres
		fields = [
		#'ScID',
		'ScName',
		'ScLocation',

		]


class ProductDetailSerializer(ModelSerializer):
#	sq=SerializerMethodField()
	ProductServiceCentres=ServiceCentreSerializer(many=True)
	class Meta:
		model =Products
		fields = [
		'ProductModel',
		'ProductServiceCentres'

		]
				
#	def get_sq(self, obj):
#		q=obj.ProductServiceCentres.all()
#		return str(q)
		
