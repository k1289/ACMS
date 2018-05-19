# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from .forms import UserRegistrationForm
from django.views.generic.list import ListView
from django.utils import timezone

from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework import status,views


import json


# Create your views here.

def home(request):
    return render(request, 'mysite/home.html')

# def productModels(request,productType):
#     return render(request, 'mysite/productModels.html')
def productModels(request):
    return render(request, 'mysite/productModels.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')

    else:
        form = UserRegistrationForm()

    return render(request, 'mysite/register.html', {'form' : form})



# class AccountViewSet(viewsets.ModelViewSet):
#     lookup_field = 'username'
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer

#     def get_permissions(self):
#         if self.request.method in permissions.SAFE_METHODS:
#             return (permissions.AllowAny(),)

#         if self.request.method == 'POST':
#             return (permissions.AllowAny(),)

#         return (permissions.IsAuthenticated(), IsAccountOwner(),)

#     def create(self, request):
#         serializer = self.serializer_class(data=request.data)

#         if serializer.is_valid():
#             Account.objects.create_user(**serializer.validated_data)
#             return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

#         return Response({
#             'status': 'Bad request',
#             'message': 'Account could not be created with received data.'
#         }, status=status.HTTP_400_BAD_REQUEST)
    

# class LoginView(views.APIView):
#     def post(self, request, format=None):
#         data = json.loads(request.body)

#         email = data.get('email', None)
#         password = data.get('password', None)

#         account = authenticate(email=email, password=password)

#         if account is not None:
#             if account.is_active:
#                 login(request, account)

#                 serialized = AccountSerializer(account)

#                 return Response(serialized.data)
#             else:
#                 return Response({
#                     'status': 'Unauthorized',
#                     'message': 'This account has been disabled.'
#                 }, status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response({
#                 'status': 'Unauthorized',
#                 'message': 'Username/password combination invalid.'
#             }, status=status.HTTP_401_UNAUTHORIZED)


# def laptopIndex(request):
#     return HttpResponse("<h1>This is laptop index</h1>")

# def laptopdetail(request,ProductID):
#     return HttpResponse("<h2> </h2>")



