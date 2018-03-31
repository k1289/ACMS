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

from .models import Product

class ProductListView(ListView):

    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


# Create your views here.

def home(request):
    return render(request, 'mysite/home.html')

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

# def laptopIndex(request):
#     return HttpResponse("<h1>This is laptop index</h1>")

# def laptopdetail(request,ProductID):
#     return HttpResponse("<h2> </h2>")


class ProductListlView(ListView):

    model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductListlView,self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

