from .models import Ordering#, OrderManager
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from repairs.models import Products, Service_Centres


# def order_detail_api_view(request):
# 	order_obj, new_obj = Ordering.objects.new_or_get(request)
# 	products = [{
# 			"id": x.id,
# 			#"url": x.get_absolute_url(),
# 			"problem":x.Problem
# 			"name": x.product, 
# 			"dateofrequest": x.Dateofrequest
#             } 
#             for x in order_obj.products.all()]
#     #order_data  = {"products": products, "subtotal": cart_obj.subtotal, "total": cart_obj.total}
#     return JsonResponse(order_data)

def orders_home(request):
	order_obj, new_obj = Ordering.objects.new_or_get(request)
	return render(request, "carts/home.html", {"cart": cart_obj})