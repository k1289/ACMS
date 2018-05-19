from django.contrib import admin
from django.conf.urls import url
from django.urls import include, path
from django.contrib.auth import views as auth_views
from .views import home,register,productModels



urlpatterns = [
    path('login/', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    #path('api/v1/auth/login/$', LoginView.as_view(),name='login'),
   	#path('api/v1/', include(router.urls)),
    path('logout/', auth_views.logout, {'template_name': 'registration/logged_out.html'}, name='logout'),
    path('', home),
    path('register/',register),
    path('api/',include("mysite.api.urls"),name="products-api"),
    path('products/',productModels),
   	#url(r'^products/', ProductListView.as_view(), name='products')
   # url(r'^(?product/<int:pk>\d+)$', views.BookDetailView.as_view(), name='product-detail')
   

]






