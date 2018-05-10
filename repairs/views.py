from django.shortcuts import render
from django.template import loader
# Create your views here.
from .models import Products, Service_Centres
from django.http import HttpResponse
from django.views.generic import TemplateView

def index(request):
    latest_product_list = Products.objects.order_by('ProductName')[:100]
    context = {'latest_product_list': latest_product_list}
    return render(request, 'repairs/index.html', context)

def centres(request,product_id):
	try:
		p = Products.objects.get(pk=product_id)
		service_centre_list = Service_Centres.objects.filter(ScProductID__ProductName=p.ProductName,ScProductID__ProductModel=p.ProductModel)
		context = {'service_centre_list': service_centre_list}
	except Products.DoesNotExist:
		raise Http404("Product does not exist")
	return render(request, 'repairs/centres.html',context)



