from rest_framework.generics import ListAPIView, RetrieveAPIView
from repairs.models import Products,Service_Centres
from .serializers import ProductsSerializer,ServiceCentreSerializer,ProductDetailSerializer

class ProductsListAPIView(ListAPIView):
	queryset = Products.objects.all()
	serializer_class=ProductsSerializer

class ServiceCentreListAPIView(ListAPIView):
	queryset = Service_Centres.objects.all()
	serializer_class=ServiceCentreSerializer
	
class ServiceProductAPIView(RetrieveAPIView):
	queryset = Products.objects.all()
	serializer_class=ProductDetailSerializer
	
