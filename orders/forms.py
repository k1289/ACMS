from django import forms
from .models import Ordering
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

class Createorders(forms.ModelForm){
	class Meta:
		model = Ordering
}