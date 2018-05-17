from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from repairs.models import Products,Service_Centres
#from mysite.models import Profile,Order
from .serializers import (ProductsSerializer,ServiceCentreSerializer,ProductDetailSerializer)

class ProductsListAPIView(CreateAPIView):
	queryset = Products.objects.all()
	serializer_class=ProductsSerializer

class ServiceCentreListAPIView(ListAPIView):
	queryset = Service_Centres.objects.all()
	serializer_class=ServiceCentreSerializer
	
class ServiceProductAPIView(RetrieveAPIView):
	queryset = Products.objects.all()
	serializer_class=ProductDetailSerializer

class ServiceRetrieveAPIView(RetrieveAPIView):
	queryset = Service_Centres.objects.all()
	serializer_class=ServiceCentreSerializer
	
