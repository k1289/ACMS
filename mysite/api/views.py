from rest_framework.generics import ListAPIView
from repairs.models import Products,Service_Centres
from .serializers import ProductsSerializer,ServiceCentersSerializer
class ProductsListAPIView(ListAPIView):
	queryset = Products.objects.all()
	serializer_class=ProductsSerializer
class ServiceCentersListAPIView(ListAPIView):
	queryset = Service_Centres.objects.all()
	serializer_class=ServiceCentersSerializer

# class CategoryListView(TemplateView):
#     template_name = "category-list.html"    
    
# class CategoryDetailView(TemplateView):
# 	template_name = "category-detail.html" 
	

