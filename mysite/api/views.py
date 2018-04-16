from rest_framework.generics import ListAPIView
from repairs.models import Products
from .serializers import ProductsSerializer
class ProductsListAPIView(ListAPIView):
	queryset = Products.objects.all()
	serializer_class=ProductsSerializer

# class CategoryListView(TemplateView):
#     template_name = "category-list.html"    
    
# class CategoryDetailView(TemplateView):
# 	template_name = "category-detail.html" 
	

