from django.urls import path
#from .models import Products, Service_Centres

from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('<int:product_id>/',views.centres,name='centres'),
]

